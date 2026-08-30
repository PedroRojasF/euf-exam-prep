"""Universal Discursive Question Precision Renderer (2010 to 2021).
Extracts exact, non-overlapping crops for every single discursive question (Q01 to Q10).
Handles both vector PDFs and scanned image PDFs with OCR fallback.
"""

import os
import re
import sys
import glob
import sqlite3
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr_engine = RapidOCR()

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RENDER_DIR = os.path.join(BASE_DIR, "bank", "rendered")
DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")
os.makedirs(RENDER_DIR, exist_ok=True)


def parse_discursive_pdf(pdf_path, exam_id):
    doc = pymupdf.open(pdf_path)
    num_pages = len(doc)
    extracted_questions = []

    for p_idx in range(num_pages):
        page = doc[p_idx]
        w, h = page.rect.width, page.rect.height
        raw_text = page.get_text()

        # Skip instruction and formula cover pages
        p_lower = raw_text.lower()
        if ("instruções para a prova" in p_lower or "intruções para a prova" in p_lower) and len(raw_text) < 1200:
            continue
        if "folha de respostas" in p_lower:
            continue
        if "formulário" in p_lower and ("constantes físicas" in p_lower or "regras de propagação" in p_lower):
            continue

        # 1. Native text blocks
        blocks = page.get_text("blocks")
        headers = []
        for b in blocks:
            txt = b[4].strip()
            m = re.search(r'(?:^|\n)(?:Q\s*\.?\s*(\d+)|Quest[ãa]o\s*(\d+))[\.:\s]', txt, re.IGNORECASE)
            if m:
                qnum = int(m.group(1) or m.group(2))
                if 1 <= qnum <= 12:
                    headers.append((b[1], qnum, b[4]))

        # 2. OCR fallback if scanned image PDF
        if not headers:
            pix = page.get_pixmap(dpi=150)
            res, _ = ocr_engine(pix.tobytes())
            scale_y = h / pix.height
            if res:
                for item in res:
                    box = item[0]
                    txt = item[1].strip()
                    y0 = box[0][1] * scale_y
                    m = re.search(r'(?:^|\n|\b)(?:Q\s*\.?\s*(\d+)|Quest[ãa]o\s*(\d+)|Q(\d+))[\.:\s]', txt, re.IGNORECASE)
                    if m:
                        qnum = int(m.group(1) or m.group(2) or m.group(3))
                        if 1 <= qnum <= 12:
                            headers.append((y0, qnum, txt))

        headers.sort(key=lambda x: x[0])
        
        # Deduplicate headers
        if headers:
            dedup = [headers[0]]
            for it in headers[1:]:
                if it[0] - dedup[-1][0] > 25:
                    dedup.append(it)
            headers = dedup

        if not headers:
            # If no header found on this page but it's a content page (p_idx > 0 and p_idx < num_pages - 1)
            # and only 1 question per page format
            continue

        for i, (y0, qnum, raw_header) in enumerate(headers):
            y_start = max(5, y0 - 10)
            if i + 1 < len(headers):
                y_end = max(y_start + 50, headers[i + 1][0] - 8)
            else:
                y_end = h - 15

            clip_rect = pymupdf.Rect(5, y_start, w - 5, y_end)
            q_text = page.get_text("text", clip=clip_rect).strip()

            extracted_questions.append({
                "exam_id": exam_id,
                "qnum": qnum,
                "page": p_idx + 1,
                "rect": clip_rect,
                "text": q_text,
                "page_obj": page
            })

    return extracted_questions


def re_render_all_discursive():
    print("=" * 70)
    print("🎨 RE-RENDERING ALL DISCURSIVE EXAMS (2010 - 2021) WITH EXACT CROPS")
    print("=" * 70)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    all_pdfs = sorted(glob.glob(os.path.join(BASE_DIR, "euf-201*.pdf")) + glob.glob(os.path.join(BASE_DIR, "euf-2020*.pdf")) + glob.glob(os.path.join(BASE_DIR, "euf-2021*.pdf")))

    total_rendered = 0

    for pdf_path in all_pdfs:
        fname = os.path.basename(pdf_path)
        m = re.search(r'(?:euf-)?(20\d{2})[-_]?([123])?', fname)
        if not m:
            continue
        year = int(m.group(1))
        sem = int(m.group(2)) if m.group(2) else 1
        exam_id = f"{year}-{sem}"

        questions = parse_discursive_pdf(pdf_path, exam_id)
        print(f"\n📁 {exam_id} ({fname}): Found {len(questions)} questions")

        for q in questions:
            qnum = q["qnum"]
            qid = f"{exam_id}-Q{qnum:02d}"
            tag = f"Q{qnum:02d}"

            out_img = os.path.join(RENDER_DIR, f"{qid}.png")
            pix = q["page_obj"].get_pixmap(clip=q["rect"], dpi=200)
            pix.save(out_img)

            cur.execute("""
            UPDATE questions
            SET page = ?, text = ?
            WHERE id = ?
            """, (q["page"], q["text"], qid))
            
            if cur.rowcount == 0:
                cur.execute("""
                INSERT OR IGNORE INTO questions (id, exam_id, question_num, tag, area, subtopic, language, page, has_image, question_type, text, status)
                VALUES (?, ?, ?, ?, 'Física', 'Core Problems', 'PT', ?, 1, 'discursiva', ?, 'unsolved')
                """, (qid, exam_id, qnum, tag, q["page"], q["text"]))

            print(f"  ✓ Rendered {qid} (Page {q['page']}, y={q['rect'].y0:.0f}..{q['rect'].y1:.0f})")
            total_rendered += 1

    conn.commit()
    conn.close()

    print(f"\n✅ Total discursive questions re-rendered with precision: {total_rendered}")
    print("🚀 Exporting questions.json...")
    export_bank_to_json()
    print("✨ Complete!")


if __name__ == "__main__":
    re_render_all_discursive()
