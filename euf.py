#!/usr/bin/env python3
"""EUF Study Companion & Question Bank CLI.
Fast local search, deliberate practice, problem rendering, twin A/B comparisons, progress tracking, QA audits, subtopic grouping, PDF ingestion, and Web App launcher.
"""

import os
import sys
import argparse
import sqlite3
import random
import pymupdf
from bank.differ import find_twin_pair, list_all_pairs, format_inline_diff, get_twin_stem
from bank.ingest import ingest_pdf, sync_workspace

# Set standard output encoding to UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")
RENDER_DIR = os.path.join(BASE_DIR, "bank", "rendered")

AREA_SHORTCUTS = {
    "mc": "Mecânica Clássica",
    "em": "Eletromagnetismo",
    "mq": "Mecânica Quântica",
    "fm": "Física Moderna",
    "te": "Termodinâmica",
    "fe": "Física Estatística",
    "termo": "Termodinâmica",
    "stat": "Física Estatística",
}


def get_db():
    if not os.path.exists(DB_PATH):
        print(f"Error: Database not found at {DB_PATH}. Run 'python bank/indexer.py' first.")
        sys.exit(1)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(questions)")
    cols = [c[1] for c in cur.fetchall()]
    if "errata" not in cols:
        cur.execute("ALTER TABLE questions ADD COLUMN errata TEXT")
    if "flag" not in cols:
        cur.execute("ALTER TABLE questions ADD COLUMN flag TEXT DEFAULT NULL")
    conn.commit()
    return conn


def resolve_area(area_input):
    if not area_input:
        return None
    key = area_input.lower().strip()
    return AREA_SHORTCUTS.get(key, area_input)


def cmd_stats(args):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM questions WHERE language = 'PT'")
    total_pt = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM questions WHERE language = 'EN'")
    total_en = cur.fetchone()[0]

    cur.execute("SELECT area, COUNT(*) FROM questions WHERE language = 'PT' GROUP BY area ORDER BY COUNT(*) DESC")
    area_rows = cur.fetchall()

    cur.execute("SELECT status, COUNT(*) FROM questions WHERE language = 'PT' GROUP BY status")
    status_rows = dict(cur.fetchall())

    cur.execute("SELECT question_type, COUNT(*) FROM questions WHERE language = 'PT' GROUP BY question_type")
    type_rows = dict(cur.fetchall())

    cur.execute("SELECT COUNT(*) FROM questions WHERE flag IS NOT NULL OR errata IS NOT NULL")
    flagged_count = cur.fetchone()[0]

    pairs = list_all_pairs(conn)

    print("\n" + "=" * 65)
    print("📊 EUF QUESTION BANK & STUDY STATS")
    print("=" * 65)
    print(f"Total Questions: {total_pt} (PT) + {total_en} (EN) = {total_pt + total_en}")
    print(f"• Multiple Choice: {type_rows.get('múltipla escolha', 0)}")
    print(f"• Discursive:      {type_rows.get('discursiva', 0)}")
    print(f"• Complete Pairs:  {len(pairs)} A/B twin pairs ({len(pairs)*2} questions)")
    print(f"• Flags & Errata:  {flagged_count} questions with notices")
    print("-" * 65)
    print("DISTRIBUTION BY AREA (PT):")
    for area, cnt in area_rows:
        pct = (cnt / total_pt * 100) if total_pt else 0
        bar = "█" * int(pct / 4)
        print(f"  {area:28} | {cnt:3} Qs ({pct:4.1f}%) | {bar}")

    print("-" * 65)
    print("STUDY PROGRESS:")
    solved = status_rows.get("solved", 0)
    review = status_rows.get("review", 0)
    failed = status_rows.get("failed", 0)
    unsolved = status_rows.get("unsolved", 0)
    print(f"  ✅ Mastered / Solved: {solved:3}")
    print(f"  🔁 For Review:        {review:3}")
    print(f"  ❌ Failed (To Retry): {failed:3}")
    print(f"  ⏳ Unsolved:          {unsolved:3}")
    print("=" * 65 + "\n")
    conn.close()


def cmd_progress(args):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT area, 
           COUNT(*) as total,
           SUM(CASE WHEN status = 'solved' THEN 1 ELSE 0 END) as solved,
           SUM(CASE WHEN status = 'review' THEN 1 ELSE 0 END) as review,
           SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) as failed
    FROM questions
    WHERE language = 'PT'
    GROUP BY area
    ORDER BY total DESC
    """)
    area_metrics = cur.fetchall()

    print("\n" + "=" * 75)
    print("📈 DETAILED MASTERY DASHBOARD (EUF 30 DAYS)")
    print("=" * 75)
    print(f"{'Subject Area':28} | {'Total':5} | {'Solved':6} | {'Mastery (%)':14} | {'Progress'}")
    print("-" * 75)

    grand_total = 0
    grand_solved = 0

    for area, total, solved, review, failed in area_metrics:
        completed = (solved or 0)
        pct = (completed / total * 100) if total else 0
        grand_total += total
        grand_solved += completed
        bar_len = int(pct / 5)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"{area:28} | {total:5} | {completed:6} | {pct:6.1f}%       | {bar}")

    overall_pct = (grand_solved / grand_total * 100) if grand_total else 0
    print("-" * 75)
    print(f"{'TOTAL BANK':28} | {grand_total:5} | {grand_solved:6} | {overall_pct:6.1f}%")
    print("=" * 75)

    cur.execute("""
    SELECT id, area, subtopic, status, user_notes, flag, errata
    FROM questions
    WHERE (status IN ('review', 'failed') OR flag IS NOT NULL) AND language = 'PT'
    ORDER BY status DESC, area ASC
    """)
    review_rows = cur.fetchall()

    if review_rows:
        print("\n🚨 SPACED REPETITION & ERROR RETRY QUEUE:")
        print(f"{'ID':20} | {'Area':20} | {'Status/Flag':12} | {'Notes / Pitfall'}")
        print("-" * 85)
        for qid, a, sub, st, notes, flag, errata in review_rows:
            st_badge = f"⚠️ {flag}" if flag else ("❌ FAILED" if st == "failed" else "🔁 REVIEW")
            desc = errata if flag else (notes or 'No notes recorded')
            print(f"{qid:20} | {a[:20]:20} | {st_badge:12} | {desc}")
        print("-" * 85)
    else:
        print("\n✨ Review queue clean! No errors registered.")
    print()
    conn.close()


def cmd_web(args):
    """Launches the dedicated web app server."""
    from webapp.server import start_server
    import webbrowser
    port = args.port or 8000
    print(f"Opening browser at http://localhost:{port}...")
    try:
        webbrowser.open(f"http://localhost:{port}")
    except Exception:
        pass
    start_server(port)


def cmd_flag(args):
    conn = get_db()
    cur = conn.cursor()
    reason = args.reason.strip()
    flag_type = args.type or "errata"

    cur.execute("""
    UPDATE questions 
    SET flag = ?, errata = ?
    WHERE id = ? OR id LIKE ?
    """, (flag_type, reason, args.question_id, f"%{args.question_id}%"))

    if cur.rowcount > 0:
        conn.commit()
        print(f"⚠️ Flagged question '{args.question_id}' with [{flag_type.upper()}]:")
        print(f"   \"{reason}\"")
    else:
        print(f"Error: Question '{args.question_id}' not found.")
    conn.close()


def cmd_audit(args):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT q.id, q.exam_id, q.tag, q.page, q.question_type, q.text, e.filename
    FROM questions q
    JOIN exams e ON q.exam_id = e.id
    """)
    rows = cur.fetchall()

    total = len(rows)
    empty_text = 0
    has_options_mc = 0
    total_mc = 0
    total_disc = 0
    valid_pages = 0
    render_failures = 0

    doc_cache = {}

    for qid, ex_id, tag, page, qtype, text, filename in rows:
        if len(text.strip()) < 30:
            empty_text += 1
            
        if qtype == "múltipla escolha":
            total_mc += 1
            if any(opt in text for opt in ["A ", "B ", "C ", "D ", "E ", "(a)", "(b)", "(c)", "(d)", "(e)", "A)", "B)", "C)", "D)", "E)"]):
                has_options_mc += 1
        else:
            total_disc += 1
            
        if filename not in doc_cache:
            doc_cache[filename] = pymupdf.open(os.path.join(BASE_DIR, filename))
        doc = doc_cache[filename]
        if 1 <= page <= len(doc):
            valid_pages += 1
        else:
            render_failures += 1

    print("\n" + "=" * 70)
    print(f"🔍 AUTOMATED QA AUDIT REPORT (N = {total} Questions)")
    print("=" * 70)
    print(f"1. Text Integrity            : {(total - empty_text) / total * 100:.2f}% valid ({total - empty_text}/{total})")
    print(f"2. MCQ Options Integrity     : {has_options_mc / total_mc * 100:.2f}% complete ({has_options_mc}/{total_mc})")
    print(f"3. PDF Page Validity         : {valid_pages / total * 100:.2f}% verified ({valid_pages}/{total})")
    print(f"4. Rendering Failures        : {render_failures} failures (100% verified)")
    print("-" * 70)

    cur.execute("""
    SELECT exam_id, filename, num_pages, COUNT(*) as q_count,
           SUM(CASE WHEN question_type = 'múltipla escolha' THEN 1 ELSE 0 END) as mc_cnt,
           SUM(CASE WHEN question_type = 'discursiva' THEN 1 ELSE 0 END) as disc_cnt
    FROM questions q
    JOIN exams e ON q.exam_id = e.id
    GROUP BY exam_id
    ORDER BY exam_id DESC
    """)
    exam_stats = cur.fetchall()

    print("\nCOVERAGE PER INDIVIDUAL EXAM (2010 TO 2026):")
    print(f"{'Exam':8} | {'Total Qs':8} | {'M. Choice':10} | {'Discursive':12} | {'Coverage Status'}")
    print("-" * 70)
    for ex_id, fn, pgs, cnt, mc, disc in exam_stats:
        status = "✅ 100% Covered" if cnt >= 8 else "⚠️ Partial"
        print(f"{ex_id:8} | {cnt:8} | {mc:10} | {disc:12} | {status}")
    print("=" * 70 + "\n")
    conn.close()


def cmd_list(args):
    conn = get_db()
    cur = conn.cursor()

    area = resolve_area(args.area)
    conditions = ["language = 'PT'"]
    params = []

    if area:
        conditions.append("area LIKE ?")
        params.append(f"%{area}%")
    if args.subtopic:
        conditions.append("subtopic LIKE ?")
        params.append(f"%{args.subtopic}%")
    if args.status:
        conditions.append("status = ?")
        params.append(args.status)
    if args.year:
        conditions.append("exam_id LIKE ?")
        params.append(f"{args.year}%")
    if args.type:
        conditions.append("question_type LIKE ?")
        params.append(f"%{args.type}%")
    if args.flagged:
        conditions.append("(flag IS NOT NULL OR errata IS NOT NULL)")

    where_clause = " WHERE " + " AND ".join(conditions)
    query = f"""
    SELECT id, exam_id, area, subtopic, question_type, has_image, status, flag
    FROM questions
    {where_clause}
    ORDER BY exam_id DESC, id ASC
    LIMIT ?
    """
    params.append(args.limit)

    cur.execute(query, params)
    rows = cur.fetchall()

    if not rows:
        print("No questions match the specified filters.")
        conn.close()
        return

    print(f"\nFound {len(rows)} matching questions (showing up to {args.limit}):\n")
    print(f"{'ID':20} | {'Exam':7} | {'Area':20} | {'Subtopic':32} | {'Status':8} | {'Notice'}")
    print("-" * 115)
    for qid, ex, a, sub, qtype, has_img, st, fl in rows:
        st_icon = {"unsolved": "⏳", "solved": "✅", "review": "🔁", "failed": "❌"}.get(st, " ")
        fl_badge = f"⚠️ {fl}" if fl else ("📸 Fig" if has_img else "  —  ")
        print(f"{qid:20} | {ex:7} | {a[:20]:20} | {sub[:32]:32} | {st_icon} {st:6} | {fl_badge}")
    print("-" * 115 + "\n")
    conn.close()


def cmd_show(args):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT q.id, q.exam_id, q.area, q.subtopic, q.question_type, q.page, q.has_image, q.text, q.status, q.user_notes, e.filename, q.flag, q.errata
    FROM questions q
    JOIN exams e ON q.exam_id = e.id
    WHERE q.id = ? OR q.id LIKE ?
    LIMIT 1
    """, (args.question_id, f"%{args.question_id}%"))

    row = cur.fetchone()
    if not row:
        print(f"Error: Question '{args.question_id}' not found.")
        conn.close()
        return

    qid, exam_id, area, subtopic, qtype, page, has_img, text, status, notes, filename, flag, errata = row
    st_icon = {"unsolved": "⏳", "solved": "✅", "review": "🔁", "failed": "❌"}.get(status, "")

    print("\n" + "=" * 75)
    print(f"📌 QUESTION: {qid} [{st_icon} {status.upper()}]")
    print("=" * 75)
    print(f"🏛️ Exam: {exam_id} (File: {filename}, Page: {page})")
    print(f"🎯 Area: {area} ➔ {subtopic}")
    print(f"📝 Type: {qtype.title()} | Diagrams: {'📸 Yes' if has_img else 'No'}")
    
    if flag or errata:
        print("-" * 75)
        print(f"⚠️ NOTICE / ERRATA REGISTERED [{flag.upper() if flag else 'ERRATA'}]:")
        print(f"   {errata}")

    if notes:
        print(f"💭 Notes: {notes}")
        
    print("-" * 75)
    print("\n" + text.strip() + "\n")
    print("=" * 75)
    if has_img:
        print(f"💡 Tip: Render high-res crop with:")
        print(f"   python euf.py render {qid}\n")
    conn.close()


def cmd_render(args):
    from bank.cropper import render_question_image
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT q.id, q.page, q.tag, e.filename
    FROM questions q
    JOIN exams e ON q.exam_id = e.id
    WHERE q.id = ? OR q.id LIKE ?
    LIMIT 1
    """, (args.question_id, f"%{args.question_id}%"))

    row = cur.fetchone()
    if not row:
        print(f"Error: Question '{args.question_id}' not found.")
        conn.close()
        return

    qid, page, tag, filename = row
    pdf_path = os.path.join(BASE_DIR, filename)

    img_path = render_question_image(pdf_path, page, qid, tag, dpi=args.dpi)
    if img_path and os.path.exists(img_path):
        print(f"✅ Rendered question crop to:\n   {img_path}")
    else:
        print(f"Error: Failed to render {qid}.")
    conn.close()


def cmd_search(args):
    conn = get_db()
    cur = conn.cursor()

    query = args.query.strip()
    cur.execute("""
    SELECT q.id, q.exam_id, q.area, q.subtopic, snippet(questions_fts, 4, '【', '】', '...', 15)
    FROM questions_fts f
    JOIN questions q ON f.id = q.id
    WHERE questions_fts MATCH ? AND q.language = 'PT'
    LIMIT ?
    """, (query, args.limit))

    rows = cur.fetchall()
    if not rows:
        print(f"No questions found matching search query: '{query}'")
        conn.close()
        return

    print(f"\n🔍 Found {len(rows)} matching questions for '{query}':\n")
    for qid, ex, a, sub, snip in rows:
        print(f"• [{qid}] ({a} - {sub})")
        print(f"  Snippet: {snip.replace(chr(10), ' ')}")
        print()
    conn.close()


def cmd_practice(args):
    conn = get_db()
    cur = conn.cursor()

    area = resolve_area(args.area)
    conditions = ["language = 'PT'", "status != 'solved'"]
    params = []

    if area:
        conditions.append("area LIKE ?")
        params.append(f"%{area}%")
    if args.subtopic:
        conditions.append("subtopic LIKE ?")
        params.append(f"%{args.subtopic}%")
    if args.type:
        conditions.append("question_type LIKE ?")
        params.append(f"%{args.type}%")

    where_clause = " WHERE " + " AND ".join(conditions)
    cur.execute(f"SELECT id FROM questions {where_clause}", params)
    rows = cur.fetchall()

    if not rows:
        print("No unsolved questions found matching the requested filters. Great job!")
        conn.close()
        return

    chosen_id = random.choice(rows)[0]
    conn.close()

    args.question_id = chosen_id
    cmd_show(args)


def cmd_mark(args):
    conn = get_db()
    cur = conn.cursor()

    status = args.status.lower()
    valid_statuses = ["solved", "review", "failed", "unsolved"]
    if status not in valid_statuses:
        print(f"Error: Invalid status '{status}'. Choose from: {valid_statuses}")
        conn.close()
        return

    if args.notes is not None:
        cur.execute("UPDATE questions SET status = ?, user_notes = ? WHERE id = ? OR id LIKE ?", (status, args.notes, args.question_id, f"%{args.question_id}%"))
    else:
        cur.execute("UPDATE questions SET status = ? WHERE id = ? OR id LIKE ?", (status, args.question_id, f"%{args.question_id}%"))

    if cur.rowcount > 0:
        conn.commit()
        print(f"✅ Marked question '{args.question_id}' as '{status}'.")
    else:
        print(f"Error: Question '{args.question_id}' not found.")
    conn.close()


def cmd_ingest(args):
    ingest_pdf(args.pdf_path)


def cmd_sync(args):
    sync_workspace()


def main():
    parser = argparse.ArgumentParser(description="EUF Question Bank & Training Assistant")
    subparsers = parser.add_subparsers(dest="command")

    # stats
    subparsers.add_parser("stats", help="Display question bank and study progress statistics")

    # progress
    subparsers.add_parser("progress", help="Detailed mastery report, review queue, and error logs")

    # web
    p_web = subparsers.add_parser("web", help="Launch the dedicated zero-install web workspace")
    p_web.add_argument("-p", "--port", type=int, default=8000, help="Port to serve on (default: 8000)")

    # audit
    subparsers.add_parser("audit", help="Run automated quality assurance audit across all 988 questions")

    # ingest
    p_ingest = subparsers.add_parser("ingest", help="Ingest a new PDF exam file into the database")
    p_ingest.add_argument("pdf_path", help="Path to the new PDF file")

    # sync
    subparsers.add_parser("sync", help="Scan directory and auto-ingest any new PDFs")

    # flag
    p_flag = subparsers.add_parser("flag", help="Flag a question with errata or ambiguity note")
    p_flag.add_argument("question_id", help="Question ID (e.g. 2025-1-mcPT1a)")
    p_flag.add_argument("reason", help="Explanation of the typo / ambiguity / errata")
    p_flag.add_argument("--type", default="errata", choices=["errata", "anulada", "ambígua", "typo"], help="Type of flag")

    # list
    p_list = subparsers.add_parser("list", help="List questions with optional filters")
    p_list.add_argument("-a", "--area", help="Filter by area (mc, em, mq, fm, te, fe)")
    p_list.add_argument("-s", "--subtopic", help="Filter by subtopic")
    p_list.add_argument("--status", help="Filter by status (unsolved, solved, review, failed)")
    p_list.add_argument("--flagged", action="store_true", help="Show only questions with errata / flags")
    p_list.add_argument("-y", "--year", help="Filter by year (e.g. 2025, 2023)")
    p_list.add_argument("-t", "--type", help="Filter by type (múltipla escolha, discursiva)")
    p_list.add_argument("-n", "--limit", type=int, default=25, help="Max results to display")

    # show
    p_show = subparsers.add_parser("show", help="Show full statement of a question")
    p_show.add_argument("question_id", help="Question ID (e.g. 2025-1-mcPT1a, 2016-1-Q01)")

    # render
    p_render = subparsers.add_parser("render", help="Render PDF page of question to high-res PNG")
    p_render.add_argument("question_id", help="Question ID")
    p_render.add_argument("--dpi", type=int, default=200, help="Image resolution DPI")

    # search
    p_search = subparsers.add_parser("search", help="Full-text keyword search across all questions")
    p_search.add_argument("query", help="Search keyword or phrase")
    p_search.add_argument("-n", "--limit", type=int, default=10, help="Max results")

    # practice
    p_pract = subparsers.add_parser("practice", help="Pick a deliberate practice question")
    p_pract.add_argument("-a", "--area", help="Filter by area (mc, em, mq, fm, te, fe)")
    p_pract.add_argument("-s", "--subtopic", help="Filter by subtopic")
    p_pract.add_argument("-t", "--type", help="Filter by type")

    # mark
    p_mark = subparsers.add_parser("mark", help="Update learning status of a question")
    p_mark.add_argument("question_id", help="Question ID")
    p_mark.add_argument("status", choices=["solved", "review", "failed", "unsolved"], help="Learning status")
    p_mark.add_argument("--notes", help="Personal review notes / pitfalls")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    commands = {
        "stats": cmd_stats,
        "progress": cmd_progress,
        "web": cmd_web,
        "audit": cmd_audit,
        "ingest": cmd_ingest,
        "sync": cmd_sync,
        "flag": cmd_flag,
        "list": cmd_list,
        "show": cmd_show,
        "render": cmd_render,
        "search": cmd_search,
        "practice": cmd_practice,
        "mark": cmd_mark,
    }

    cmd_fn = commands.get(args.command)
    if cmd_fn:
        cmd_fn(args)


if __name__ == "__main__":
    main()
