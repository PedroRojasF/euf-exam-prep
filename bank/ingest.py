"""EUF Automatic PDF Ingestion and Sync Engine.
Adds new exam PDFs to the database, extracts questions, classifies subtopics, and pre-renders high-res crops.
"""

import os
import re
import sys
import sqlite3
import pymupdf
from bank.indexer import extract_year_semester, parse_pdf_document, init_database
from bank.pre_renderer import get_fast_page_crops, compute_crop_rect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")
RENDER_DIR = os.path.join(BASE_DIR, "bank", "rendered")
os.makedirs(RENDER_DIR, exist_ok=True)


def ingest_pdf(pdf_path):
    """Ingests a single new PDF file into the EUF database and pre-renders its crops."""
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        return 0

    filename = os.path.basename(pdf_path)
    target_dest = os.path.join(BASE_DIR, filename)

    # If file is in another directory, copy to workspace root
    if os.path.abspath(pdf_path) != os.path.abspath(target_dest):
        import shutil
        shutil.copy2(pdf_path, target_dest)
        pdf_path = target_dest

    year, sem = extract_year_semester(filename)
    exam_id = f"{year}-{sem}"

    print(f"\n📥 Ingesting new exam PDF: {filename} (Exam ID: {exam_id})...")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    doc = pymupdf.open(pdf_path)
    num_pages = len(doc)

    # Extract questions
    questions = parse_pdf_document(pdf_path, year, sem, exam_id)
    exam_type = "amc_multiple_choice" if any("mc" in q["tag"].lower() or "em" in q["tag"].lower() for q in questions) else "discursive"

    cur.execute("""
    INSERT OR REPLACE INTO exams (id, year, semester, filename, num_pages, exam_type, has_text)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (exam_id, year, sem, filename, num_pages, exam_type, 1))

    # Pre-render crops and insert into DB
    page_headers_cache = {}
    total_added = 0

    for q in questions:
        qid = q["id"]
        tag = q["tag"]
        page = q["page"]

        cur.execute("""
        INSERT OR REPLACE INTO questions 
        (id, exam_id, question_num, tag, area, subtopic, language, page, has_image, question_type, text)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            qid, q["exam_id"], q["question_num"], q["tag"],
            q["area"], q["subtopic"], q["language"], q["page"],
            q["has_image"], q["question_type"], q["text"]
        ))
        total_added += 1

        # Render high-res crop
        out_path = os.path.join(RENDER_DIR, f"{qid.replace('/', '_')}.png")
        if not (os.path.exists(out_path) and os.path.getsize(out_path) > 5000):
            doc_page = doc[page - 1]
            if page not in page_headers_cache:
                page_headers_cache[page] = get_fast_page_crops(doc_page)
            headers = page_headers_cache[page]
            crop_rect = compute_crop_rect(doc_page, headers, tag)
            pix = doc_page.get_pixmap(clip=crop_rect, dpi=200)
            pix.save(out_path)

    conn.commit()
    conn.close()

    print(f"✅ Successfully ingested {total_added} questions from '{filename}' into the question bank!")
    return total_added


def sync_workspace():
    """Scans root directory and ingests any unindexed PDFs automatically."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT filename FROM exams")
    indexed_files = set(r[0] for r in cur.fetchall())
    conn.close()

    import glob
    all_pdfs = [os.path.basename(f) for f in glob.glob(os.path.join(BASE_DIR, "*.pdf"))]
    new_pdfs = [f for f in all_pdfs if f not in indexed_files and not any(k in f for k in ["Moys", "Formul", "form"])]

    if not new_pdfs:
        print("✨ Workspace is already up to date. No new PDFs found.")
        return 0

    print(f"🔍 Found {len(new_pdfs)} new PDF(s) to ingest: {new_pdfs}")
    total = 0
    for pdf_name in new_pdfs:
        total += ingest_pdf(os.path.join(BASE_DIR, pdf_name))
    return total


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ingest_pdf(sys.argv[1])
    else:
        sync_workspace()
