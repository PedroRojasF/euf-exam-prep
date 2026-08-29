"""High-Performance Batch Pre-Renderer for EUF Question Bank.
Pre-renders all questions to PNG at high DPI so the web app runs with instant 0ms latency.
"""

import os
import re
import sys
import time
import sqlite3
import pymupdf
from rapidocr_onnxruntime import RapidOCR

# Set standard output encoding to UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ocr_engine = RapidOCR()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")
RENDER_DIR = os.path.join(BASE_DIR, "bank", "rendered")
os.makedirs(RENDER_DIR, exist_ok=True)


def get_fast_page_crops(page):
    """Ultra-fast detection of question boundaries on a PDF page using PyMuPDF native blocks with OCR fallback."""
    w, h = page.rect.width, page.rect.height
    
    # 1. Try PyMuPDF native text blocks first (takes ~2ms)
    blocks = page.get_text("blocks")
    headers = []
    
    for b in blocks:
        txt = b[4].strip()
        y_top = b[1]
        
        m_tag = re.search(r'\[([a-zA-Z]{2,4}\d*[a-zA-Z0-9_-]*)\]', txt)
        m_qnum = re.search(r'(?:Q\.\s*(\d+)|Quest[ãa]o\s*(\d+)|Q\s*(\d+))[\.:\s]?', txt, re.IGNORECASE)
        
        tag_val = m_tag.group(1).lower() if m_tag else ''
        qnum_val = (m_qnum.group(1) or m_qnum.group(2) or m_qnum.group(3) or '') if m_qnum else ''
        
        if tag_val or qnum_val:
            headers.append((y_top, tag_val, qnum_val))
            
    # 2. If native blocks found headers, we are done in 2ms!
    if len(headers) >= 1:
        headers.sort(key=lambda x: x[0])
        # Deduplicate
        dedup = [headers[0]]
        for it in headers[1:]:
            if it[0] - dedup[-1][0] > 15:
                dedup.append(it)
        return dedup
        
    # 3. Fallback: OCR only if native blocks found 0 headers
    pix = page.get_pixmap(dpi=150)
    res, _ = ocr_engine(pix.tobytes())
    if not res:
        return [(10, '', '')]
        
    scale_y = h / pix.height
    for item in res:
        box = item[0]
        txt = item[1].strip()
        y_top = box[0][1] * scale_y
        m_tag = re.search(r'\[([a-zA-Z]{2,4}\d*[a-zA-Z0-9_-]*)\]', txt)
        m_qnum = re.search(r'(?:Q\.\s*(\d+)|Quest[ãa]o\s*(\d+)|Q\s*(\d+))[\.:\s]?', txt, re.IGNORECASE)
        tag_val = m_tag.group(1).lower() if m_tag else ''
        qnum_val = (m_qnum.group(1) or m_qnum.group(2) or m_qnum.group(3) or '') if m_qnum else ''
        if tag_val or qnum_val:
            headers.append((y_top, tag_val, qnum_val))
            
    headers.sort(key=lambda x: x[0])
    if headers:
        dedup = [headers[0]]
        for it in headers[1:]:
            if it[0] - dedup[-1][0] > 15:
                dedup.append(it)
        return dedup
    return [(10, '', '')]


def compute_crop_rect(page, headers, target_tag):
    """Computes exact Rect for target tag."""
    w, h = page.rect.width, page.rect.height
    if not headers or len(headers) == 1:
        return pymupdf.Rect(5, 5, w - 5, h - 5)
        
    clean_target = target_tag.lower().replace('[', '').replace(']', '').strip()
    match_idx = -1
    
    for i, (y, tag_v, qnum_v) in enumerate(headers):
        if clean_target and (clean_target in tag_v or tag_v in clean_target):
            match_idx = i
            break
        if clean_target and (clean_target == f"q{qnum_v}" or clean_target == qnum_v):
            match_idx = i
            break
            
    if match_idx == -1:
        m_num = re.search(r'\d+', clean_target)
        if m_num:
            t_num = m_num.group(0)
            for i, (y, tag_v, qnum_v) in enumerate(headers):
                if qnum_v == t_num or t_num in tag_v:
                    match_idx = i
                    break
                    
    if match_idx == -1:
        return pymupdf.Rect(5, 5, w - 5, h - 5)
        
    y_start = max(5, headers[match_idx][0] - 12)
    if match_idx + 1 < len(headers):
        y_end = max(y_start + 40, headers[match_idx + 1][0] - 4)
    else:
        y_end = max(min(h - 5, y_start + 250), h - 15)
        
    return pymupdf.Rect(5, y_start, w - 5, y_end)


def pre_render_all_questions():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    SELECT q.id, q.exam_id, q.page, q.tag, e.filename
    FROM questions q
    JOIN exams e ON q.exam_id = e.id
    WHERE q.language = 'PT'
    ORDER BY q.exam_id DESC, q.page ASC
    """)
    questions = cur.fetchall()
    conn.close()

    print(f"🚀 Starting High-Performance Batch Pre-Rendering for {len(questions)} questions...")
    start_total = time.time()
    
    doc_cache = {}
    page_headers_cache = {}
    
    rendered_count = 0
    skipped_count = 0

    for idx, (qid, exam_id, page, tag, filename) in enumerate(questions):
        out_path = os.path.join(RENDER_DIR, f"{qid.replace('/', '_')}.png")
        
        # If already cached and valid (>10KB), skip
        if os.path.exists(out_path) and os.path.getsize(out_path) > 5000:
            skipped_count += 1
            continue

        pdf_path = os.path.join(BASE_DIR, filename)
        if not os.path.exists(pdf_path):
            continue

        if filename not in doc_cache:
            doc_cache[filename] = pymupdf.open(pdf_path)
        doc = doc_cache[filename]

        if not (1 <= page <= len(doc)):
            continue

        doc_page = doc[page - 1]
        cache_key = (filename, page)
        
        if cache_key not in page_headers_cache:
            page_headers_cache[cache_key] = get_fast_page_crops(doc_page)
            
        headers = page_headers_cache[cache_key]
        crop_rect = compute_crop_rect(doc_page, headers, tag)
        
        pix = doc_page.get_pixmap(clip=crop_rect, dpi=200)
        pix.save(out_path)
        rendered_count += 1

        if rendered_count % 50 == 0 or idx == len(questions) - 1:
            elapsed = time.time() - start_total
            print(f"  [{idx+1}/{len(questions)}] Rendered: {rendered_count}, Cached: {skipped_count} ({elapsed:.1f}s elapsed)")

    total_time = time.time() - start_total
    print(f"\n🎉 Pre-rendering complete in {total_time:.2f}s! ({rendered_count} rendered, {skipped_count} cached)")


if __name__ == "__main__":
    pre_render_all_questions()
