"""EUF Question Bank Sanitizer and Integrity Engine.
Cleans all merged statements, removes junk instruction pages and duplicate bubble sheets,
fixes OCR artifacts, ensures 100% physics isolation, and exports clean static JSON and SQLite.
"""

import os
import re
import sys
import glob
import json
import sqlite3

# Standard output encoding
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bank.hints import get_physics_clues
from bank.exporter import export_bank_to_json

DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")
RENDER_DIR = os.path.join(BASE_DIR, "bank", "rendered")


def is_instruction_or_bubble_sheet(text):
    if not text:
        return True
    t = text.lower().strip()
    if len(t) < 30:
        return True
    if 'instruções para a prova' in t and len(t) < 800:
        return True
    if 'folha de respostas' in t and len(t) < 600:
        return True
    if 'precisar de mais espa' in t and 'folhas extras do caderno' in t and len(t) < 800:
        return True
    if 'utilize as folhas extras do caderno de respostas' in t and len(t) < 700:
        return True
    if 'esta prova contém' in t and 'questões discursivas' in t and len(t) < 600:
        return True
    if 'formulário' in t and ('constantes físicas' in t or 'regras de propagação' in t or 'tabela periódica' in t):
        return True
    if 'nao e permitido o uso de calculadoras' in t and len(t) < 500:
        return True
    # Bubble sheet answer keys
    if re.search(r'Q\.\s*\d+\s*:\s*A\s*B\s*C\s*D\s*E', text) and len(t) < 150:
        return True
    if text.count('A') >= 1 and text.count('B') >= 1 and text.count('C') >= 1 and text.count('D') >= 1 and text.count('E') >= 1 and len(t) < 80:
        return True
    return False


def clean_ocr_artifacts(text):
    if not text:
        return ""
    t = text

    # Remove OCR box / Asian checkbox artifacts
    t = re.sub(r'[回国口◆■●▲▼]', '', t)
    t = t.replace('（', '(').replace('）', ')').replace('［', '[').replace('］', ']')

    # Clean roman numeral option markers
    t = re.sub(r'\bIⅢI\b', 'III', t)
    t = re.sub(r'\bⅡI\b', 'II', t)

    # Clean OCR merged words & hyphens
    t = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', t)
    t = re.sub(r'capa-\s*0\s*0\.5\s*citorde', 'capacitor de', t)
    t = re.sub(r'deindu-\s*tanciaL', 'de indutância L', t)
    t = re.sub(r'cir-\s*cuitoéfechada', 'circuito é fechada', t)
    t = re.sub(r'totalQoeocircuito', 'total Q_0 e o circuito', t)
    t = re.sub(r'capacitanciaCeum', 'capacitância C e um', t)
    t = re.sub(r'esta & aberto', 'está aberto', t)
    t = re.sub(r'Ograficoque', 'O gráfico que', t)
    t = re.sub(r'melhorrepresenta', 'melhor representa', t)
    t = re.sub(r'em funcao do tempo', 'em função do tempo', t)
    t = re.sub(r'estao representados', 'estão representados', t)
    t = re.sub(r'possiveis graficos', 'possíveis gráficos', t)
    t = re.sub(r'encontra-seinicialmente', 'encontra-se inicialmente', t)

    # Normalize excessive blank lines
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()


def trim_to_single_question(text, tag, is_amc=True):
    if not text:
        return ""

    # 1. Truncate at subsequent physics tag headers (e.g. Q. 20 [emPT2b] or [em2b] or [emPT2b])
    tag_patt = re.compile(r'(?:Q\.\s*\d+\s*)?\[\s*((?:mc|em|te|fe|fm|mq|mm)(?:PT)?\s*\d+\s*[ab])\s*\]', re.IGNORECASE)
    matches = list(tag_patt.finditer(text))
    if len(matches) > 1:
        first_tag = matches[0].group(1).replace(' ', '').replace('mmPT', 'mcPT').replace('mm', 'mc')
        norm_first = first_tag if 'PT' in first_tag.upper() else f"{first_tag[:2]}PT{first_tag[2:]}"
        norm_tag = tag if 'PT' in tag.upper() else f"{tag[:2]}PT{tag[2:]}"
        if norm_tag.lower() in norm_first.lower() or norm_first.lower() in norm_tag.lower():
            text = text[:matches[1].start()].strip()
        else:
            for idx, m in enumerate(matches):
                c_tag = m.group(1).replace(' ', '').replace('mmPT', 'mcPT').replace('mm', 'mc')
                norm_c = c_tag if 'PT' in c_tag.upper() else f"{c_tag[:2]}PT{c_tag[2:]}"
                if norm_tag.lower() in norm_c.lower() or norm_c.lower() in norm_tag.lower():
                    nxt = matches[idx+1].start() if idx+1 < len(matches) else len(text)
                    text = text[m.start():nxt].strip()
                    break

    # 2. Truncate at subsequent 'Questao X' or 'Q. X'
    q_patt = re.compile(r'(?:^|\n)(?:Q\s*\.?\s*(\d+)|Quest[ãa]o\s*(\d+))[\.:\s]', re.IGNORECASE)
    q_matches = list(q_patt.finditer(text))
    if len(q_matches) > 1:
        text = text[:q_matches[1].start()].strip()

    return text.strip()


def sanitize_all():
    print("=" * 65)
    print("🧹 EUF MASTER QUESTION BANK SANITIZATION & INTEGRITY AUDIT")
    print("=" * 65)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Delete all -p duplicates from database
    cur.execute("DELETE FROM questions WHERE id LIKE '%-p%'")
    deleted_p = cur.rowcount
    print(f"✅ Removed {deleted_p} duplicate / bubble sheet records (-p suffixes).")

    # 2. Fetch active questions
    cur.execute("""
    SELECT id, exam_id, tag, area, subtopic, question_type, page, text, flag, errata
    FROM questions
    """)
    all_rows = cur.fetchall()

    deleted_count = 0
    updated_count = 0

    for r in all_rows:
        qid, exam_id, tag, area, subtopic, qtype, page, text, flag, errata = r
        
        # Check if junk / instruction / bubble sheet
        if is_instruction_or_bubble_sheet(text):
            cur.execute("DELETE FROM questions WHERE id = ?", (qid,))
            deleted_count += 1
            continue

        # Trim merged statements
        cleaned = trim_to_single_question(text, tag, qtype == "múltipla escolha")
        
        # Clean OCR artifacts
        cleaned = clean_ocr_artifacts(cleaned)

        if cleaned != text:
            cur.execute("UPDATE questions SET text = ? WHERE id = ?", (cleaned, qid))
            updated_count += 1

    conn.commit()

    # Re-sync FTS index
    cur.execute("INSERT OR REPLACE INTO questions_fts(questions_fts) VALUES('rebuild')")
    conn.commit()

    print(f"✅ Removed {deleted_count} junk/instruction records.")
    print(f"✅ Cleaned OCR artifacts & trimmed {updated_count} questions.")

    # 3. Clean orphan -p images from rendered directory
    orphan_imgs = glob.glob(os.path.join(RENDER_DIR, "*-p*.png"))
    for oi in orphan_imgs:
        try:
            os.remove(oi)
        except Exception:
            pass
    print(f"✅ Removed {len(orphan_imgs)} orphan crop images from bank/rendered/.")

    # 4. Run Integrity Checks
    cur.execute("SELECT id, tag, text FROM questions")
    remaining = cur.fetchall()

    tag_patt = re.compile(r'\[\s*((?:mc|em|te|fe|fm|mq|mm)(?:PT)?\s*\d+\s*[ab])\s*\]', re.IGNORECASE)
    multi_count = 0
    for qid, tag, text in remaining:
        t_matches = tag_patt.findall(text)
        if len(t_matches) > 1:
            multi_count += 1
            print(f"⚠️ Warning: Multi-tag still found in {qid}: {t_matches}")

    print(f"✨ Multi-tag count: {multi_count} (Target: 0)")
    print(f"📊 Clean Physics Questions: {len(remaining)}")

    conn.close()

    # 5. Export to static JSON (both bank/ and frontend/public/)
    print("\n📦 Exporting synchronized database to 'bank/questions.json' & 'frontend/public/questions.json'...")
    export_bank_to_json()
    print("✅ Bank synchronization complete!")


if __name__ == "__main__":
    sanitize_all()
