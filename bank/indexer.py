"""EUF Exam Indexer and Question Bank Generator (OCR-Enhanced).
Extracts questions, metadata, formulas, and diagrams from ALL exams (2010-2026).
"""

import os
import re
import sys
import glob
import json
import sqlite3
import unicodedata
import pymupdf
from rapidocr_onnxruntime import RapidOCR

# Set standard output encoding to UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ocr_engine = RapidOCR()

DB_PATH = os.path.join(os.path.dirname(__file__), "euf_bank.sqlite")
RENDER_DIR = os.path.join(os.path.dirname(__file__), "rendered")

AREA_MAPPING = {
    "mc": "Mecânica Clássica",
    "em": "Eletromagnetismo",
    "mq": "Mecânica Quântica",
    "fm": "Física Moderna",
    "te": "Termodinâmica",
    "fe": "Física Estatística",
    "termo": "Termodinâmica e Física Estatística",
}

SUBTOPIC_KEYWORDS = {
    "Mecânica Clássica": [
        ("Mecânica Lagrangiana e Vínculos", [r"lagrang", r"graus de liberdade", r"coordenadas generalizadas", r"v[íi]nculo", r"multiplicador de lagrange"]),
        ("Mecânica Hamiltoniana e Espaço de Fase", [r"hamiltonian", r"espa[çc]o de fase", r"equa[çc][õo]es de hamilton", r"transforma[çc][ãa]o can[ôo]nica", r"colchetes de poisson"]),
        ("Pequenas Oscilações e Modos Normais", [r"modos normais", r"pequenas oscila[çc][õo]es", r"frequ[êe]ncias pr[óo]prias", r"matriz de acoplamento", r"autovetores"]),
        ("Potenciais Centrais e Gravitação", [r"for[çc]a central", r"potencial efetivo", r"kepler", r"[óo]rbita", r"momento angular conservado"]),
        ("Dinâmica de Rotação e Corpo Rígido", [r"corpo r[íi]gido", r"momento de in[ée]rcia", r"tensor de in[ée]rcia", r"rolamento sem desliz", r"torque"]),
        ("Colisões e Leis de Conservação", [r"colis[ãa]o", r"conserva[çc][ãa]o do momento", r"centro de massa", r"impulso"]),
        ("Oscilador Amortecido e Forçado", [r"amortecid", r"for[çc]ado", r"fator de qualidade", r"resson[âa]ncia"]),
    ],
    "Eletromagnetismo": [
        ("Eletrostática e Problemas de Contorno", [r"equa[çc][ãa]o de laplace", r"equa[çc][ãa]o de poisson", r"m[ée]todo das imagens", r"condi[çc][õo]es de contorno", r"potencial eletrost[áa]tico", r"esfera condutora"]),
        ("Dielétricos e Polarização", [r"polariza[çc][ãa]o", r"vetor d", r"permissividade", r"diel[ée]trico", r"densidade de carga ligada"]),
        ("Magnetostática e Materiais Magnéticos", [r"lei de biot-savart", r"vetor a", r"potencial vetor", r"magnetiza[çc][ãa]o", r"campo h", r"solenoide", r"torque magn[ée]tico"]),
        ("Indução Eletromagnética e Lei de Faraday", [r"faraday", r"fem induzida", r"autoindut[âa]ncia", r"corrente induzida", r"indut[âa]ncia m[úu]tua"]),
        ("Equações de Maxwell e Ondas EM", [r"vetor de poynting", r"ondas eletromagn[ée]ticas", r"equa[çc][õo]es de maxwell", r"press[ãa]o de radia[çc][ãa]o", r"polariza[çc][ãa]o da luz", r"fresnel"]),
        ("Radiação e Dipolos", [r"radia[çc][ãa]o dipolar", r"potenciais retardados", r"f[óo]rmula de larmor", r"antena"]),
    ],
    "Mecânica Quântica": [
        ("Oscilador Harmônico Quântico", [r"operador de cria[çc][ãa]o", r"operador de aniquila[çc][ãa]o", r"a\^?\†|a\^\+", r"oscilador harm[ôo]nico", r"n[íi]veis de energia.*oscilador"]),
        ("Formalismo de Dirac e Espaço de Hilbert", [r"comutador", r"incerteza", r"postulado", r"produto escalar", r"autovetores.*autovalores", r"opera[çc][ãa]o hermitiana", r"bra-ket", r"projec"]),
        ("Poços e Barreiras de Potencial", [r"po[çc]o infinito", r"po[çc]o finito", r"tunelamento", r"barreira de potencial", r"coeficiente de transmiss[ãa]o"]),
        ("Momento Angular e Spin", [r"spin", r"matrizes de pauli", r"clebsch-gordan", r"j_z|s_z|l_z", r"adi[çc][ãa]o de momentos angulares", r"harm[ôo]nicos esf[ée]ricos"]),
        ("Teoria de Perturbações", [r"perturba[çc][ãa]o.*primeira ordem", r"perturba[çc][ãa]o.*segunda ordem", r"hamiltoniano perturbado", r"termo de perturba[çc][ãa]o"]),
        ("Átomo de Hidrogênio e Átomos Monoeletrônicos", [r"[áa]tomo de hidrog[êe]nio", r"raio de bohr", r"orbital", r"n[úu]meros qu[âa]nticos"]),
        ("Partículas Idênticas e Simetria", [r"b[óo]sons", r"f[ée]rmions", r"princ[íi]pio de exclus[ãa]o", r"fun[çc][ãa]o de onda anti-sim[ée]trica"]),
    ],
    "Termodinâmica": [
        ("Primeira e Segunda Leis / Ciclos", [r"ciclo de carnot", r"rendimento", r"ciclo", r"adiab[áa]tico", r"isot[ée]rmico", r"trabalho realizado"]),
        ("Potenciais Termodinâmicos e Relações de Maxwell", [r"rela[çc][õo]es de maxwell", r"energia livre de helmholtz", r"energia de gibbs", r"entalpia", r"potencial qu[íi]mico"]),
        ("Gases Ideais e Reais", [r"g[áa]s ideal", r"van der waals", r"calor espec[íi]fico", r"equa[çc][ãa]o de estado"]),
        ("Transições de Fase e Entropia", [r"transi[çc][ãa]o de fase", r"clapeyron", r"calor latente", r"varia[çc][ãa]o de entropia"]),
    ],
    "Física Estatística": [
        ("Ensemble Canônico e Microcanônico", [r"fun[çc][ãa]o de parti[çc][ãa]o", r"ensemble can[ôo]nico", r"distribui[çc][ãa]o de boltzmann", r"microcan[ôo]nico"]),
        ("Ensemble Grande Canônico", [r"grande can[ôo]nico", r"grande potencial", r"fugacidade"]),
        ("Gases Quânticos (Fermi-Dirac e Bose-Einstein)", [r"bose-einstein", r"fermi-dirac", r"energia de fermi", r"temperatura de fermi", r"condensa[çc][ãa]o de bose", r"radia[çc][ãa]o de corpo negro"]),
        ("Sistemas de Spins e Paramagnetismo", [r"paramagnetismo", r"modelo de ising", r"magnetiza[çc][ãa]o m[ée]dia", r"susceptibilidade"]),
    ],
    "Física Moderna": [
        ("Relatividade Restrita", [r"transforma[çc][ãa]o de lorentz", r"contraction", r"dilata[çc][ãa]o temporal", r"quadrivetor", r"energia relativ[íi]stica", r"efeito doppler relativ[íi]stico"]),
        ("Radiação Térmica e Fótons", [r"efeito fotoel[ée]trico", r"espalhamento compton", r"comprimento de onda de de broglie", r"f[óo]ton"]),
        ("Modelos Atômicos e Estrutura", [r"modelo de bohr", r"experi[êe]ncia de franck-hertz", r"raios x", r"massa reduzida"]),
    ]
}


def is_garbled(text):
    """Detects if raw extracted text has broken character encodings or missing OCR."""
    if len(text.strip()) < 50:
        return True
    if '\x00' in text or '\ufffd' in text:
        return True
    alpha = sum(1 for c in text if c.isalpha())
    if alpha == 0:
        return True
    vowels = sum(1 for c in text if c.lower() in 'aeiouáéíóúâêîôûãõ')
    if vowels / alpha < 0.2:
        return True
    return False


def clean_latex_accents(text):
    """Replaces combined LaTeX-style accents and broken ligatures with standard UTF-8 characters."""
    t = text
    replacements = [
        ('ˆa', 'â'), ('´a', 'á'), ('`a', 'à'), ('˜a', 'ã'),
        ('ˆe', 'ê'), ('´e', 'é'), ('`e', 'è'),
        ('ˆı', 'î'), ('´ı', 'í'), ('`ı', 'ì'), ('ˆi', 'î'), ('´i', 'í'),
        ('ˆo', 'ô'), ('´o', 'ó'), ('`o', 'ò'), ('˜o', 'õ'),
        ('ˆu', 'û'), ('´u', 'ú'), ('`u', 'ù'),
        ('¸c', 'ç'), ('¨u', 'ü'),
        ('ˆA', 'Â'), ('´A', 'Á'), ('`A', 'À'), ('˜A', 'Ã'),
        ('ˆE', 'Ê'), ('´E', 'É'),
        ('´I', 'Í'), ('ˆI', 'Î'),
        ('ˆO', 'Ô'), ('´O', 'Ó'), ('˜O', 'Õ'),
        ('´U', 'Ú'), ('ˆU', 'Û'),
        ('¸C', 'Ç')
    ]
    for old, new in replacements:
        t = t.replace(old, new)

    t = re.sub(r'a\s+rmaç', 'afirmaç', t)
    t = re.sub(r'a\s+rma', 'afirma', t)
    t = re.sub(r'\b\s+gura\b', 'figura', t)
    t = re.sub(r'\b\s+guras\b', 'figuras', t)
    t = re.sub(r'con\s+nada', 'confinada', t)
    t = re.sub(r'con\s+nado', 'confinado', t)
    t = re.sub(r'espec[íi]\s+ca', 'específica', t)
    t = re.sub(r'espec[íi]\s+co', 'específico', t)
    t = re.sub(r'\b\s+o inextens', 'fio inextens', t)
    t = re.sub(r'\b\s+nal\b', 'final', t)
    return t


def get_page_text_robust(page):
    """Extracts text using direct PDF extraction, with instant OCR fallback for scanned or Type 3 fonts."""
    raw = page.get_text()
    if not is_garbled(raw):
        return clean_latex_accents(raw)
    
    # Fallback to OCR
    pix = page.get_pixmap(dpi=150)
    res, _ = ocr_engine(pix.tobytes())
    if res:
        ocr_text = "\n".join([line[1] for line in res])
        return clean_latex_accents(ocr_text)
    return ""


def classify_subtopic(area, text):
    """Classifies a question into a fine-grained subtopic based on keyword matching."""
    text_clean = clean_latex_accents(text).lower()
    for a in [area] if area in SUBTOPIC_KEYWORDS else SUBTOPIC_KEYWORDS.keys():
        for subtopic, patterns in SUBTOPIC_KEYWORDS.get(a, []):
            for pat in patterns:
                if re.search(pat, text_clean):
                    return subtopic
    return f"{area} Geral"


def init_database(db_path=DB_PATH):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    os.makedirs(RENDER_DIR, exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS exams (
        id TEXT PRIMARY KEY,
        year INTEGER,
        semester INTEGER,
        filename TEXT,
        num_pages INTEGER,
        exam_type TEXT,
        has_text INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY,
        exam_id TEXT,
        question_num INTEGER,
        tag TEXT,
        area TEXT,
        subtopic TEXT,
        language TEXT,
        page INTEGER,
        has_image INTEGER,
        question_type TEXT,
        text TEXT,
        status TEXT DEFAULT 'unsolved',
        user_notes TEXT,
        FOREIGN KEY (exam_id) REFERENCES exams(id)
    )
    """)

    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS questions_fts USING fts5(
        id UNINDEXED,
        exam_id,
        area,
        subtopic,
        text,
        content='questions',
        content_rowid='rowid'
    )
    """)

    cur.execute("""
    CREATE TRIGGER IF NOT EXISTS questions_ai AFTER INSERT ON questions BEGIN
        INSERT INTO questions_fts(rowid, id, exam_id, area, subtopic, text)
        VALUES (new.rowid, new.id, new.exam_id, new.area, new.subtopic, new.text);
    END;
    """)

    cur.execute("""
    CREATE TRIGGER IF NOT EXISTS questions_ad AFTER DELETE ON questions BEGIN
        INSERT INTO questions_fts(questions_fts, rowid, id, exam_id, area, subtopic, text)
        VALUES('delete', old.rowid, old.id, old.exam_id, old.area, old.subtopic, old.text);
    END;
    """)

    cur.execute("""
    CREATE TRIGGER IF NOT EXISTS questions_au AFTER UPDATE ON questions BEGIN
        INSERT INTO questions_fts(questions_fts, rowid, id, exam_id, area, subtopic, text)
        VALUES('delete', old.rowid, old.id, old.exam_id, old.area, old.subtopic, old.text);
        INSERT INTO questions_fts(rowid, id, exam_id, area, subtopic, text)
        VALUES (new.rowid, new.id, new.exam_id, new.area, new.subtopic, new.text);
    END;
    """)

    conn.commit()
    return conn


def extract_year_semester(filename):
    # Matches: 20261, 2025-1, 2025-2, euf-2024-1, euf-2016-2, etc.
    m = re.search(r'(?:euf-)?(20\d{2})[-_]?([123])?', filename)
    if m:
        year = int(m.group(1))
        sem = int(m.group(2)) if m.group(2) else 1
        return year, sem
    return 2020, 1


def parse_pdf_document(pdf_path, year, sem, exam_id):
    """Universal parser with hybrid text+OCR extraction and automatic page rendering."""
    doc = pymupdf.open(pdf_path)
    questions = []
    
    # Pre-render pages for instant dashboard display
    for page_idx, page in enumerate(doc):
        # Extract page text robustly
        p_text = get_page_text_robust(page)
        has_imgs = len(page.get_images()) > 0
        
        # 1. Check for AMC tag matches like [mcPT1a] or [mc1a]
        tag_matches = list(re.finditer(r'(?:(?:Q\.|Quest[ãa]o)\s*(\d+)\s*)?\[([a-zA-Z]{2,4}\d*[a-zA-Z0-9_-]*)\]', p_text, re.IGNORECASE))
        
        if tag_matches:
            for i, m in enumerate(tag_matches):
                q_num_str = m.group(1)
                tag = m.group(2)
                q_num = int(q_num_str) if q_num_str else (i + 1)
                start_pos = m.start()
                end_pos = tag_matches[i+1].start() if i+1 < len(tag_matches) else len(p_text)
                q_text = p_text[start_pos:end_pos].strip()

                tag_match = re.match(r'([a-zA-Z]{2})(PT|EN)?(.*)', tag, re.IGNORECASE)
                if tag_match:
                    prefix = tag_match.group(1).lower()
                    lang = "EN" if (tag_match.group(2) and tag_match.group(2).upper() == "EN") else "PT"
                    area = AREA_MAPPING.get(prefix, "Física Geral")
                else:
                    lang = "PT"
                    area = "Física Geral"

                subtopic = classify_subtopic(area, q_text)
                qid = f"{exam_id}-{tag}"

                questions.append({
                    "id": qid,
                    "exam_id": exam_id,
                    "question_num": q_num,
                    "tag": tag,
                    "area": area,
                    "subtopic": subtopic,
                    "language": lang,
                    "page": page_idx + 1,
                    "has_image": 1 if has_imgs else 0,
                    "question_type": "múltipla escolha",
                    "text": q_text
                })
        else:
            # 2. Check for Discursive Q1., Q2., Q10. or Questão 1
            q_pattern = re.compile(r'(?:^|\n)(Q\s*(\d+)|Quest[ãa]o\s*(\d+))[\.:\s]', re.MULTILINE)
            matches = list(q_pattern.finditer(p_text))
            
            standard_area_map = {
                1: "Mecânica Clássica",
                2: "Mecânica Clássica",
                3: "Física Moderna",
                4: "Mecânica Quântica",
                5: "Termodinâmica",
                6: "Eletromagnetismo",
                7: "Eletromagnetismo",
                8: "Mecânica Quântica",
                9: "Mecânica Quântica",
                10: "Física Estatística",
            }
            
            for i, m in enumerate(matches):
                q_num_val = int(m.group(2) or m.group(3))
                start = m.start()
                end = matches[i+1].start() if i+1 < len(matches) else len(p_text)
                q_text = p_text[start:end].strip()

                area = standard_area_map.get(q_num_val, "Física Geral")
                subtopic = classify_subtopic(area, q_text)
                qid = f"{exam_id}-Q{q_num_val:02d}"

                questions.append({
                    "id": qid,
                    "exam_id": exam_id,
                    "question_num": q_num_val,
                    "tag": f"Q{q_num_val}",
                    "area": area,
                    "subtopic": subtopic,
                    "language": "PT",
                    "page": page_idx + 1,
                    "has_image": 1 if has_imgs else 0,
                    "question_type": "discursiva",
                    "text": q_text
                })
                
    return questions


def run_indexer():
    """Main indexing execution across ALL years (2010 to 2026)."""
    conn = init_database()
    cur = conn.cursor()

    cur.execute("DELETE FROM questions")
    cur.execute("DELETE FROM exams")
    conn.commit()

    pdf_files = sorted(glob.glob("*.pdf"))
    total_indexed = 0

    print("=" * 70)
    print("🚀 EUF EXAM INDEXING PIPELINE (Full 2010-2026 Universe)")
    print("=" * 70)

    for pdf_path in pdf_files:
        if any(skip in pdf_path for skip in ["Moys", "Formul", "form"]):
            continue

        year, sem = extract_year_semester(pdf_path)
        exam_id = f"{year}-{sem}"
        doc = pymupdf.open(pdf_path)
        num_pages = len(doc)

        exam_questions = parse_pdf_document(pdf_path, year, sem, exam_id)
        exam_type = "amc_multiple_choice" if any("mc" in q["tag"].lower() or "em" in q["tag"].lower() for q in exam_questions) else "discursive"

        cur.execute("""
        INSERT OR REPLACE INTO exams (id, year, semester, filename, num_pages, exam_type, has_text)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (exam_id, year, sem, pdf_path, num_pages, exam_type, 1))

        seen_ids = set()
        for q in exam_questions:
            if q["id"] in seen_ids:
                q["id"] = f"{q['id']}-p{q['page']}"
            seen_ids.add(q["id"])

            cur.execute("""
            INSERT OR REPLACE INTO questions 
            (id, exam_id, question_num, tag, area, subtopic, language, page, has_image, question_type, text)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                q["id"], q["exam_id"], q["question_num"], q["tag"],
                q["area"], q["subtopic"], q["language"], q["page"],
                q["has_image"], q["question_type"], q["text"]
            ))
            total_indexed += 1

        print(f"[{exam_id:7}] {pdf_path:35} | ✅ {len(exam_questions):3} Questões")

    conn.commit()

    # Statistics
    cur.execute("SELECT area, COUNT(*) FROM questions WHERE language = 'PT' GROUP BY area ORDER BY COUNT(*) DESC")
    area_stats = cur.fetchall()

    print("\n" + "=" * 70)
    print(f"🎉 INDEXING COMPLETE: {total_indexed} total questions indexed across 2010-2026!")
    print("=" * 70)
    for area, count in area_stats:
        print(f"  📌 {area:33}: {count:3} questões")

    generate_catalog_markdown(conn)
    conn.close()


def generate_catalog_markdown(conn):
    cur = conn.cursor()
    cur.execute("""
    SELECT area, subtopic, id, exam_id, page, question_type, has_image
    FROM questions
    WHERE language = 'PT'
    ORDER BY area, subtopic, exam_id DESC
    """)
    rows = cur.fetchall()

    catalog_path = os.path.join(os.path.dirname(__file__), "CATALOG.md")
    with open(catalog_path, "w", encoding="utf-8") as f:
        f.write("# 📚 EUF Question Bank Catalog (2010 - 2026)\n\n")
        f.write(f"Total Portuguese Questions: **{len(rows)}**\n\n")

        current_area = None
        current_subtopic = None

        for area, subtopic, qid, exam_id, page, q_type, has_img in rows:
            if area != current_area:
                current_area = area
                f.write(f"\n## 🎯 {area}\n\n")
            if subtopic != current_subtopic:
                current_subtopic = subtopic
                f.write(f"\n### 📖 {subtopic}\n\n")
                f.write("| ID | Exame | Pág | Tipo | Diagrama |\n")
                f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            img_badge = "📸 Sim" if has_img else "—"
            f.write(f"| `{qid}` | {exam_id} | p.{page} | {q_type} | {img_badge} |\n")


if __name__ == "__main__":
    run_indexer()
