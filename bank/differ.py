"""Twin Question Diff and Comparison Engine for EUF Exams.
Detects, matches, compares, and highlights differences between Exam Variants A and B.
"""

import re
import difflib
import sqlite3


def get_twin_stem(tag_or_id):
    """Extracts the base stem of a question identifier.
    e.g., '2025-1-mcPT1a' -> ('2025-1', 'mcPT1', 'a')
          'mcPT1b' -> (None, 'mcPT1', 'b')
    """
    cleaned = tag_or_id.strip()
    
    # Check if format is EXAM_ID-TAG (e.g. 2025-1-mcPT1a)
    m = re.match(r'^(?:(20\d{2}[-_]\d+)-)?(.*)$', cleaned)
    exam_id = m.group(1) if m else None
    rest = m.group(2) if m else cleaned
    
    # Check if tag ends with a or b
    tm = re.match(r'^(.*?)([abAB])$', rest)
    if tm:
        stem = tm.group(1)
        variant = tm.group(2).lower()
        return exam_id, stem, variant
    return exam_id, rest, None


def find_twin_pair(conn, query_id):
    """Finds both variants A and B for a given question ID or stem."""
    cur = conn.cursor()
    
    # Check if query_id is a specific ID
    cur.execute("SELECT id, exam_id, tag, text, page, has_image, area, subtopic FROM questions WHERE id = ? OR id LIKE ?", (query_id, f"%{query_id}%"))
    exact = cur.fetchone()
    
    if exact:
        qid, exam_id, tag, text, page, has_img, area, subtopic = exact
        _, stem, variant = get_twin_stem(tag)
        if stem:
            # Look for both variant 'a' and 'b' for this stem in the same exam
            cur.execute("""
            SELECT id, exam_id, tag, text, page, has_image, area, subtopic
            FROM questions
            WHERE exam_id = ? AND (tag = ? OR tag = ?)
            ORDER BY tag ASC
            """, (exam_id, f"{stem}a", f"{stem}b"))
            rows = cur.fetchall()
            row_dict = {}
            for r in rows:
                v = r[2][-1].lower()
                row_dict[v] = r
            return row_dict
            
    # Try looking by exam and stem directly
    exam_id, stem, _ = get_twin_stem(query_id)
    if exam_id and stem:
        cur.execute("""
        SELECT id, exam_id, tag, text, page, has_image, area, subtopic
        FROM questions
        WHERE exam_id LIKE ? AND (tag = ? OR tag = ? OR tag LIKE ?)
        ORDER BY tag ASC
        """, (f"%{exam_id}%", f"{stem}a", f"{stem}b", f"{stem}%"))
    else:
        cur.execute("""
        SELECT id, exam_id, tag, text, page, has_image, area, subtopic
        FROM questions
        WHERE tag = ? OR tag = ? OR tag LIKE ?
        ORDER BY tag ASC
        """, (f"{stem}a", f"{stem}b", f"{stem}%"))
        
    rows = cur.fetchall()
    row_dict = {}
    for r in rows:
        v = r[2][-1].lower() if r[2] else 'a'
        if v in ['a', 'b']:
            row_dict[v] = r
    return row_dict


def list_all_pairs(conn, area=None, year=None):
    """Lists all detected A/B question twin pairs in the database."""
    cur = conn.cursor()
    conditions = ["language = 'PT'"]
    params = []
    
    if area:
        conditions.append("area LIKE ?")
        params.append(f"%{area}%")
    if year:
        conditions.append("exam_id LIKE ?")
        params.append(f"{year}%")
        
    where = " WHERE " + " AND ".join(conditions)
    cur.execute(f"""
    SELECT id, exam_id, tag, area, subtopic, page, has_image
    FROM questions
    {where}
    ORDER BY exam_id DESC, tag ASC
    """, params)
    
    rows = cur.fetchall()
    pairs = {}
    for qid, ex, tag, a, sub, pg, has_img in rows:
        _, stem, variant = get_twin_stem(tag)
        if stem and variant in ['a', 'b']:
            key = (ex, stem, a, sub)
            if key not in pairs:
                pairs[key] = {}
            pairs[key][variant] = (qid, pg, has_img)
            
    # Filter complete pairs
    complete = []
    for (ex, stem, a, sub), variants in pairs.items():
        if 'a' in variants and 'b' in variants:
            complete.append({
                "exam_id": ex,
                "stem": stem,
                "area": a,
                "subtopic": sub,
                "id_a": variants['a'][0],
                "page_a": variants['a'][1],
                "has_image_a": variants['a'][2],
                "id_b": variants['b'][0],
                "page_b": variants['b'][1],
                "has_image_b": variants['b'][2],
            })
    return complete


def format_inline_diff(text_a, text_b):
    """Produces a clean, human-readable side-by-side or highlighted diff between variant A and B."""
    lines_a = [l.strip() for l in text_a.splitlines() if l.strip()]
    lines_b = [l.strip() for l in text_b.splitlines() if l.strip()]
    
    # Remove header line with Q. X [tag] to compare the actual physical content
    if lines_a and re.search(r'\[.*?\]', lines_a[0]):
        lines_a = lines_a[1:]
    if lines_b and re.search(r'\[.*?\]', lines_b[0]):
        lines_b = lines_b[1:]
        
    matcher = difflib.SequenceMatcher(None, lines_a, lines_b)
    diff_output = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            for l in lines_a[i1:i2]:
                diff_output.append(f"  [=] {l}")
        elif tag == 'replace':
            for l in lines_a[i1:i2]:
                diff_output.append(f"  [-] VARIANTE A: {l}")
            for l in lines_b[j1:j2]:
                diff_output.append(f"  [+] VARIANTE B: {l}")
        elif tag == 'delete':
            for l in lines_a[i1:i2]:
                diff_output.append(f"  [-] VARIANTE A (solo en A): {l}")
        elif tag == 'insert':
            for l in lines_b[j1:j2]:
                diff_output.append(f"  [+] VARIANTE B (solo en B): {l}")
                
    return "\n".join(diff_output)
