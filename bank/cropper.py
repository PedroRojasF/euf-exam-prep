"""EUF Precision Question Cropper and High-Res Visual Renderer.
Crops individual question bounding boxes with exact LaTeX formulas, diagrams, and options.
"""

import os
import re
import pymupdf
from rapidocr_onnxruntime import RapidOCR

ocr_engine = RapidOCR()
RENDER_DIR = os.path.join(os.path.dirname(__file__), "rendered")
os.makedirs(RENDER_DIR, exist_ok=True)


def get_question_crop_rect(page, target_tag_or_label):
    """Finds the precise vertical bounding box (y_start, y_end) for an individual question on a page."""
    w, h = page.rect.width, page.rect.height
    pix = page.get_pixmap(dpi=200)
    res, _ = ocr_engine(pix.tobytes())
    
    if not res:
        return pymupdf.Rect(5, 5, w - 5, h - 5)
        
    scale_y = h / pix.height
    
    headers = []
    all_bottoms = []
    
    for item in res:
        box = item[0]
        txt = item[1].strip()
        y_top = box[0][1] * scale_y
        y_bot = box[2][1] * scale_y
        all_bottoms.append(y_bot)
        
        m_tag = re.search(r'\[([a-zA-Z]{2,4}\d*[a-zA-Z0-9_-]*)\]', txt)
        m_qnum = re.search(r'(?:Q\.\s*(\d+)|Quest[ãa]o\s*(\d+)|Q\s*(\d+))[\.:\s]?', txt, re.IGNORECASE)
        
        tag_val = m_tag.group(1).lower() if m_tag else ''
        qnum_val = (m_qnum.group(1) or m_qnum.group(2) or m_qnum.group(3) or '') if m_qnum else ''
        
        if tag_val or qnum_val:
            headers.append((y_top, tag_val, qnum_val, txt))
            
    if not headers:
        return pymupdf.Rect(5, 5, w - 5, h - 5)
        
    headers.sort(key=lambda x: x[0])
    
    # Deduplicate headers too close vertically (< 15pt)
    dedup = [headers[0]]
    for item in headers[1:]:
        if item[0] - dedup[-1][0] > 15:
            dedup.append(item)
    headers = dedup
    
    clean_target = target_tag_or_label.lower().replace('[', '').replace(']', '').strip()
    match_idx = -1
    
    for i, (y, tag_v, qnum_v, raw) in enumerate(headers):
        if clean_target and (clean_target in tag_v or tag_v in clean_target):
            match_idx = i
            break
        if clean_target and (clean_target == f"q{qnum_v}" or clean_target == qnum_v):
            match_idx = i
            break
            
    if match_idx == -1:
        m_num = re.search(r'\d+', clean_target)
        if m_num:
            target_num = m_num.group(0)
            for i, (y, tag_v, qnum_v, raw) in enumerate(headers):
                if qnum_v == target_num or target_num in tag_v:
                    match_idx = i
                    break
                    
    if match_idx == -1:
        if len(headers) == 1:
            match_idx = 0
        else:
            return pymupdf.Rect(5, 5, w - 5, h - 5)
            
    # Generous top margin (12 pt above header)
    y_start = max(5, headers[match_idx][0] - 12)
    
    # Generous bottom margin (extending down to next question header or bottom margin)
    if match_idx + 1 < len(headers):
        y_end = headers[match_idx + 1][0] - 4
    else:
        # Last question on page: extend generously to cover all options
        max_detected_bot = max(all_bottoms) if all_bottoms else (h - 10)
        y_end = min(h - 5, max(max_detected_bot + 20, h - 15))
        
    # Safety minimum height
    if y_end - y_start < 100:
        y_end = min(h - 5, y_start + 300)
        
    return pymupdf.Rect(5, y_start, w - 5, y_end)


def render_question_image(pdf_path, page_num, question_id, tag, dpi=200):
    """Renders and caches the precise high-resolution crop for a given question."""
    out_path = os.path.join(RENDER_DIR, f"{question_id.replace('/', '_')}.png")
    
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
