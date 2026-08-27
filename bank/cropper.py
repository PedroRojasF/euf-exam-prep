"""EUF Precision Question Cropper and High-Res Visual Renderer.
Crops individual question bounding boxes with exact LaTeX formulas, diagrams, and options.
Strictly distinguishes Variant A (odd Q / tag-a) from Variant B (even Q / tag-b).
"""

import os
import re
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr_engine = RapidOCR()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RENDER_DIR = os.path.join(BASE_DIR, "bank", "rendered")
os.makedirs(RENDER_DIR, exist_ok=True)

STANDARD_80_TAGS = [
    # Classical Mechanics (Q1-Q16)
    'mcPT1a', 'mcPT1b', 'mcPT2a', 'mcPT2b', 'mcPT3a', 'mcPT3b', 'mcPT4a', 'mcPT4b',
    'mcPT5a', 'mcPT5b', 'mcPT6a', 'mcPT6b', 'mcPT7a', 'mcPT7b', 'mcPT8a', 'mcPT8b',
    # Electromagnetism (Q17-Q32)
    'emPT1a', 'emPT1b', 'emPT2a', 'emPT2b', 'emPT3a', 'emPT3b', 'emPT4a', 'emPT4b',
    'emPT5a', 'emPT5b', 'emPT6a', 'emPT6b', 'emPT7a', 'emPT7b', 'emPT8a', 'emPT8b',
    # Thermodynamics (Q33-Q40)
    'tePT1a', 'tePT1b', 'tePT2a', 'tePT2b', 'tePT3a', 'tePT3b', 'tePT4a', 'tePT4b',
    # Statistical Physics (Q41-Q48)
    'fePT1a', 'fePT1b', 'fePT2a', 'fePT2b', 'fePT3a', 'fePT3b', 'fePT4a', 'fePT4b',
    # Modern Physics (Q49-Q64)
    'fmPT1a', 'fmPT1b', 'fmPT2a', 'fmPT2b', 'fmPT3a', 'fmPT3b', 'fmPT4a', 'fmPT4b',
    'fmPT5a', 'fmPT5b', 'fmPT6a', 'fmPT6b', 'fmPT7a', 'fmPT7b', 'fmPT8a', 'fmPT8b',
    # Quantum Mechanics (Q65-Q80)
    'mqPT1a', 'mqPT1b', 'mqPT2a', 'mqPT2b', 'mqPT3a', 'mqPT3b', 'mqPT4a', 'mqPT4b',
    'mqPT5a', 'mqPT5b', 'mqPT6a', 'mqPT6b', 'mqPT7a', 'mqPT7b', 'mqPT8a', 'mqPT8b',
]

TAG_TO_QNUM = {tag.lower(): i + 1 for i, tag in enumerate(STANDARD_80_TAGS)}
for i, tag in enumerate(STANDARD_80_TAGS):
    short_tag = tag.replace('PT', '').lower()
    TAG_TO_QNUM[short_tag] = i + 1


def get_question_crop_rect(doc_page, target_tag):
    """Finds the exact non-overlapping bounding box (y_start, y_end) distinguishing A from B."""
    w, h = doc_page.rect.width, doc_page.rect.height
    clean_target = target_tag.lower().replace('[', '').replace(']', '').strip()
    target_variant = 'b' if clean_target.endswith('b') else ('a' if clean_target.endswith('a') else None)
    expected_qnum = TAG_TO_QNUM.get(clean_target)

    # 1. Try native text blocks first
    blocks = doc_page.get_text('blocks')
    headers = []
    for b in blocks:
        txt = b[4].strip()
        m_q = re.search(r'(?:Q\.\s*(\d+)|Quest[ãa]o\s*(\d+)|Q\s*(\d+))', txt, re.IGNORECASE)
        m_tag = re.search(r'\[([a-zA-Z]{2,4}\d*[a-zA-Z0-9_-]*)\]', txt)
        qnum = int(m_q.group(1) or m_q.group(2) or m_q.group(3)) if m_q else None
        tag_v = m_tag.group(1).lower() if m_tag else None
        if qnum or tag_v:
            headers.append((b[1], qnum, tag_v, txt))

    # 2. If no headers in native blocks, ALWAYS use OCR!
    if not headers:
        pix = doc_page.get_pixmap(dpi=150)
        res, _ = ocr_engine(pix.tobytes())
        scale_y = h / pix.height
        if res:
            for item in res:
                box = item[0]
                txt = item[1].strip()
                y0 = box[0][1] * scale_y
                m_q = re.search(r'(?:Q\.\s*(\d+)|Quest[ãa]o\s*(\d+)|Q\s*(\d+))', txt, re.IGNORECASE)
                m_tag = re.search(r'\[([a-zA-Z]{2,4}\d*[a-zA-Z0-9_-]*)\]', txt)
                qnum = int(m_q.group(1) or m_q.group(2) or m_q.group(3)) if m_q else None
                tag_v = m_tag.group(1).lower() if m_tag else None
                if qnum or tag_v:
                    headers.append((y0, qnum, tag_v, txt))

    headers.sort(key=lambda x: x[0])
    if headers:
        dedup = [headers[0]]
        for it in headers[1:]:
            if it[0] - dedup[-1][0] > 15:
                dedup.append(it)
        headers = dedup

    if not headers or len(headers) == 1:
        return pymupdf.Rect(5, 5, w - 5, h - 5)

    match_idx = -1

    # Priority 1: Exact tag match
    for i, (y, qnum, tag_v, raw) in enumerate(headers):
        if tag_v and tag_v == clean_target:
            match_idx = i
            break

    # Priority 2: Exact Q-number match
    if match_idx == -1 and expected_qnum:
        for i, (y, qnum, tag_v, raw) in enumerate(headers):
            if qnum == expected_qnum:
                match_idx = i
                break

    # Priority 3: Matching tag stem AND matching variant letter ('a' or 'b')
    if match_idx == -1 and target_variant:
        stem = clean_target[:-1]
        for i, (y, qnum, tag_v, raw) in enumerate(headers):
            if tag_v and stem in tag_v and tag_v.endswith(target_variant):
                match_idx = i
                break
            if qnum:
                q_variant = 'a' if qnum % 2 == 1 else 'b'
                if q_variant == target_variant:
                    m_num = re.search(r'\d+', stem)
                    if m_num and (int(m_num.group(0)) == (qnum + 1) // 2 or int(m_num.group(0)) == qnum):
                        match_idx = i
                        break

    # Priority 4: Discursive Q01..Q10
    if match_idx == -1:
        for i, (y, qnum, tag_v, raw) in enumerate(headers):
            if clean_target in [f'q{qnum:02d}', f'q{qnum}', str(qnum)]:
                match_idx = i
                break

    if match_idx == -1:
        if len(headers) == 2 and target_variant == 'b':
            match_idx = 1
        elif len(headers) == 2 and target_variant == 'a':
            match_idx = 0
        else:
            return pymupdf.Rect(5, 5, w - 5, h - 5)

    y_start = max(5, headers[match_idx][0] - 12)
    y_end = headers[match_idx + 1][0] - 4 if (match_idx + 1 < len(headers)) else (h - 8)

    if y_end - y_start < 80:
        y_end = min(h - 5, y_start + 250)

    return pymupdf.Rect(5, y_start, w - 5, y_end)


def render_question_image(pdf_path, page_num, question_id, tag, dpi=200):
    """Renders and caches the precise high-resolution crop for a given question."""
    out_path = os.path.join(RENDER_DIR, f"{question_id.replace('/', '_')}.png")

    if "2026-1-mqPT4a" in question_id:
        doc = pymupdf.open(pdf_path)
        p = doc[page_num - 1]
        p.get_pixmap(clip=pymupdf.Rect(5, 60, p.rect.width - 5, 368), dpi=dpi).save(out_path)
        return out_path
    elif "2026-1-mqPT4b" in question_id:
        doc = pymupdf.open(pdf_path)
        p = doc[page_num - 1]
        p.get_pixmap(clip=pymupdf.Rect(5, 368, p.rect.width - 5, 660), dpi=dpi).save(out_path)
        return out_path
    elif "2026-1-mqPT5a" in question_id:
        doc = pymupdf.open(pdf_path)
        p = doc[page_num - 1]
        p.get_pixmap(clip=pymupdf.Rect(5, 660, p.rect.width - 5, 740), dpi=dpi).save(out_path)
        return out_path

    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        return out_path

    if not os.path.exists(pdf_path):
        return None

    doc = pymupdf.open(pdf_path)
    if not (1 <= page_num <= len(doc)):
        return None

    page = doc[page_num - 1]
    crop_rect = get_question_crop_rect(page, tag)
    pix = page.get_pixmap(clip=crop_rect, dpi=dpi)
    pix.save(out_path)
    return out_path
