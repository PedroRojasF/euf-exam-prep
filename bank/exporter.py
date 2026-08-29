"""EUF Static Bank Exporter.
Exports SQLite database, physics hints, twin comparisons, and concept hierarchies to static JSON format
for client-side zero-server web applications (Svelte / React / Static SPA).
"""

import os
import sys
import json
import sqlite3

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bank.hints import get_physics_clues, get_all_physics_clues
from bank.differ import format_inline_diff, list_all_pairs
DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")


def export_bank_to_json(output_path=None):
    """Exports all questions, metadata, concept hierarchies, hints, and twin comparisons to JSON."""
    if output_path is None:
        output_path = os.path.join(BASE_DIR, "bank", "questions.json")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Fetch all questions (Language PT primary, but full metadata)
    cur.execute("""
    SELECT q.id, q.exam_id, q.tag, q.area, q.subtopic, q.question_type, q.page, q.has_image, q.text, e.filename, q.flag, q.errata
    FROM questions q
    JOIN exams e ON q.exam_id = e.id
    WHERE q.language = 'PT'
    ORDER BY q.exam_id DESC, q.id ASC
    """)
    rows = cur.fetchall()

    questions = []
    question_dict_by_id = {}

    for r in rows:
        qid = r[0]
        exam_id = r[1]
        tag = r[2]
        area = r[3]
        subtopic = r[4]
        qtype = r[5]
        page = r[6]
        has_image = bool(r[7])
        text = r[8] or ""
        filename = r[9]
        flag = r[10]
        errata = r[11]

        # Calculate twin information
        twin_id = None
        twin_stem = None
        if tag.endswith("a"):
            twin_stem = tag[:-1]
            twin_id = f"{exam_id}-{twin_stem}b"
        elif tag.endswith("b"):
            twin_stem = tag[:-1]
            twin_id = f"{exam_id}-{twin_stem}a"

        # Contextual Socratic Hints in PT, ES, EN
        clues = get_all_physics_clues(area, subtopic, qid, text)

        q_data = {
            "id": qid,
            "exam_id": exam_id,
            "tag": tag,
            "area": area,
            "subtopic": subtopic,
            "question_type": qtype,
            "page": page,
            "has_image": has_image,
            "text": text,
            "flag": flag,
            "errata": errata,
            "image": f"images/{qid.replace('/', '_')}.png",
            "clues": clues,
            "twin_id": twin_id,
            "twin_stem": twin_stem,
        }
        questions.append(q_data)
        question_dict_by_id[qid] = q_data

    # 2. Concept Tree / Taxonomy
    cur.execute("""
    SELECT area, subtopic, COUNT(*) as count
    FROM questions
    WHERE language = 'PT'
    GROUP BY area, subtopic
    ORDER BY area, COUNT(*) DESC
    """)
    concept_rows = cur.fetchall()

    concept_tree = {}
    for area, sub, cnt in concept_rows:
        if area not in concept_tree:
            concept_tree[area] = {"total": 0, "subtopics": []}
        concept_tree[area]["total"] += cnt
        concept_tree[area]["subtopics"].append({"name": sub, "count": cnt})

    # 3. Twin Pairs and Differences
    cur.execute("""
    SELECT DISTINCT exam_id, SUBSTR(tag, 1, LENGTH(tag)-1) as stem, area, subtopic
    FROM questions
    WHERE (tag LIKE '%a' OR tag LIKE '%b') AND language = 'PT'
    ORDER BY exam_id DESC, stem ASC
    """)
    stems = cur.fetchall()

    pairs = []
    for ex, stem, a, sub in stems:
        qid_a = f"{ex}-{stem}a"
        qid_b = f"{ex}-{stem}b"
        qa = question_dict_by_id.get(qid_a)
        qb = question_dict_by_id.get(qid_b)

        diff_text = ""
        if qa and qb and qa.get("text") and qb.get("text"):
            try:
                diff_text = format_inline_diff(qa["text"], qb["text"])
            except Exception:
                diff_text = ""

        pairs.append({
            "exam_id": ex,
            "stem": stem,
            "area": a or (qa["area"] if qa else "Física"),
            "subtopic": sub or (qa["subtopic"] if qa else "Core Problems"),
            "qid_a": qid_a,
            "qid_b": qid_b,
            "text_a": qa["text"] if qa else "",
            "text_b": qb["text"] if qb else "",
            "diff": diff_text,
            "image_a": f"images/{qid_a.replace('/', '_')}.png",
            "image_b": f"images/{qid_b.replace('/', '_')}.png"
        })

    # 4. Exams list
    cur.execute("""
    SELECT e.id, e.year, e.semester, e.filename, e.num_pages, e.exam_type, COUNT(q.id) as total_questions
    FROM exams e
    LEFT JOIN questions q ON e.id = q.exam_id AND q.language = 'PT'
    GROUP BY e.id
    ORDER BY e.year DESC, e.semester DESC
    """)
    exams = [{
        "id": r[0],
        "year": r[1],
        "semester": r[2],
        "filename": r[3],
        "num_pages": r[4],
        "exam_type": r[5],
        "total_questions": r[6]
    } for r in cur.fetchall()]

    conn.close()

    payload = {
        "version": "1.0.0",
        "generated_at": None,
        "stats": {
            "total_questions": len(questions),
            "total_pairs": len(pairs),
            "total_exams": len(exams),
            "areas_count": len(concept_tree)
        },
        "exams": exams,
        "concept_tree": concept_tree,
        "pairs": pairs,
        "questions": questions
    }

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    frontend_pub = os.path.join(BASE_DIR, "frontend", "public", "questions.json")
    if os.path.exists(os.path.dirname(frontend_pub)) and output_path != frontend_pub:
        with open(frontend_pub, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"✅ Successfully exported {len(questions)} questions & {len(pairs)} twin pairs to:")
    print(f"   📁 {output_path} ({os.path.getsize(output_path) / 1024:.1f} KB)")
    return payload


if __name__ == "__main__":
    export_bank_to_json()
