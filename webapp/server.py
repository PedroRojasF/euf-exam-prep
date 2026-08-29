"""EUF Dedicated Web App Server.
High-performance standalone HTTP REST API & SPA server for desktop, tablet, and mobile.
"""

import os
import sys
import json
import sqlite3
import mimetypes
import urllib.parse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bank.profile import (
    get_active_profile_name,
    set_active_profile_name,
    load_user_profile,
    save_user_profile,
    get_question_user_state,
    update_question_user_state,
    list_profiles
)
from bank.hints import get_physics_clues
DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")
RENDER_DIR = os.path.join(BASE_DIR, "bank", "rendered")
FRONTEND_DIST = os.path.join(BASE_DIR, "frontend", "dist")
STATIC_DIR = FRONTEND_DIST if os.path.exists(os.path.join(FRONTEND_DIST, "index.html")) else os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")


def get_db():
    return sqlite3.connect(DB_PATH)


class EUFWebHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # 1. API Endpoints
        if path == "/api/stats":
            self.handle_api_stats()
        elif path == "/api/questions":
            self.handle_api_questions(query)
        elif path.startswith("/api/question/"):
            qid = path[len("/api/question/"):]
            self.handle_api_question_detail(qid)
        elif path == "/api/pairs":
            self.handle_api_pairs(query)
        elif path.startswith("/api/pair/"):
            stem = path[len("/api/pair/"):]
            self.handle_api_pair_detail(stem)
        elif path == "/api/profiles":
            self.handle_api_profiles()
        elif path == "/api/concept-map":
            self.handle_api_concept_map()
        # 2. Image Serving
        elif path.startswith("/images/"):
            img_name = path[len("/images/"):]
            img_path = os.path.join(RENDER_DIR, img_name)
            if not os.path.exists(img_path) or os.path.getsize(img_path) < 1000:
                qid = os.path.splitext(img_name)[0]
                conn = get_db()
                cur = conn.cursor()
                cur.execute("""
                SELECT q.page, q.tag, e.filename
                FROM questions q
                JOIN exams e ON q.exam_id = e.id
                WHERE q.id = ?
                """, (qid,))
                row = cur.fetchone()
                conn.close()
                if row:
                    p_num, tag, filename = row
                    full_pdf = os.path.join(BASE_DIR, filename)
                    if os.path.exists(full_pdf):
                        try:
                            from bank.cropper import render_question_image
                            render_question_image(full_pdf, p_num, qid, tag)
                        except Exception as e:
                            print(f"Dynamic render error for {qid}: {e}")

            if os.path.exists(img_path):
                self.send_response(200)
                self.send_header("Content-Type", "image/png")
                self.send_header("Cache-Control", "public, max-age=86400")
                self.end_headers()
                with open(img_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "Image not found")
        # 3. Static Files & SPA Root
        else:
            if path == "/" or path == "":
                filepath = os.path.join(STATIC_DIR, "index.html")
            else:
                filepath = os.path.join(STATIC_DIR, path.lstrip("/"))
                if not os.path.exists(filepath):
                    filepath = os.path.join(STATIC_DIR, "index.html")

            if os.path.exists(filepath) and not os.path.isdir(filepath):
                self.send_response(200)
                ctype, _ = mimetypes.guess_type(filepath)
                self.send_header("Content-Type", ctype or "text/html; charset=utf-8")
                self.end_headers()
                with open(filepath, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File not found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(length) if length > 0 else b"{}"

        try:
            body = json.loads(post_data.decode("utf-8")) if post_data else {}
        except Exception:
            body = {}

        if path.startswith("/api/question/") and path.endswith("/status"):
            qid = path[len("/api/question/"):-len("/status")]
            self.handle_post_question_status(qid, body)
        elif path == "/api/profiles/switch":
            self.handle_post_switch_profile(body)
        elif path == "/api/ingest":
            self.handle_post_ingest(body)
        else:
            self.send_error(404, "Endpoint not found")

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def handle_api_stats(self):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM questions WHERE language = 'PT'")
        total = cur.fetchone()[0]

        cur.execute("SELECT area, COUNT(*) FROM questions WHERE language = 'PT' GROUP BY area ORDER BY COUNT(*) DESC")
        areas = [{"area": r[0], "count": r[1]} for r in cur.fetchall()]
        conn.close()

        profile_name = get_active_profile_name()
        profile_data = load_user_profile(profile_name)
        user_qs = profile_data.get("questions", {})

        solved = sum(1 for q in user_qs.values() if q.get("status") == "solved")
        review = sum(1 for q in user_qs.values() if q.get("status") == "review")
        failed = sum(1 for q in user_qs.values() if q.get("status") == "failed")
        unsolved = total - solved

        self.send_json({
            "total_questions": total,
            "solved": solved,
            "review": review,
            "failed": failed,
            "unsolved": max(0, unsolved),
            "mastery_percentage": round(solved / total * 100, 1) if total else 0,
            "active_profile": profile_name,
            "areas": areas
        })

    def handle_api_questions(self, query):
        conn = get_db()
        cur = conn.cursor()

        area = query.get("area", [None])[0]
        subtopic = query.get("subtopic", [None])[0]
        exam = query.get("exam", [None])[0]
        status_filter = query.get("status", [None])[0]
        search = query.get("search", [None])[0]

        conditions = ["q.language = 'PT'"]
        params = []

        if area and area != "All Subject Areas":
            conditions.append("q.area = ?")
            params.append(area)
        if subtopic and subtopic != "All Subtopics":
            conditions.append("q.subtopic = ?")
            params.append(subtopic)
        if exam and exam != "All Exams":
            conditions.append("q.exam_id = ?")
            params.append(exam)
        if search and search.strip():
            conditions.append("(q.text LIKE ? OR q.id LIKE ? OR q.subtopic LIKE ?)")
            params.extend([f"%{search.strip()}%", f"%{search.strip()}%", f"%{search.strip()}%"])

        where_clause = " AND ".join(conditions)
        sql = f"""
        SELECT q.id, q.exam_id, q.tag, q.area, q.subtopic, q.question_type, q.page, q.has_image, q.flag, q.errata
        FROM questions q
        WHERE {where_clause}
        ORDER BY q.exam_id DESC, q.id ASC
        """
        cur.execute(sql, params)
        rows = cur.fetchall()
        conn.close()

        profile_name = get_active_profile_name()
        profile_data = load_user_profile(profile_name)
        user_qs = profile_data.get("questions", {})

        results = []
        for r in rows:
            qid = r[0]
            u_state = user_qs.get(qid, {})
            st = u_state.get("status", "unsolved")

            if status_filter and status_filter != "All Statuses" and st != status_filter:
                continue

            results.append({
                "id": qid,
                "exam_id": r[1],
                "tag": r[2],
                "area": r[3],
                "subtopic": r[4],
                "question_type": r[5],
                "page": r[6],
                "has_image": bool(r[7]),
                "flag": r[8],
                "errata": r[9],
                "status": st,
                "user_notes": u_state.get("notes", ""),
                "image_url": f"/images/{qid.replace('/', '_')}.png"
            })

        self.send_json({
            "total_matched": len(results),
            "questions": results
        })

    def handle_api_question_detail(self, qid):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
        SELECT q.id, q.exam_id, q.tag, q.area, q.subtopic, q.question_type, q.page, q.has_image, q.text, e.filename, q.flag, q.errata
        FROM questions q
        JOIN exams e ON q.exam_id = e.id
        WHERE q.id = ?
        """, (qid,))
        row = cur.fetchone()
        conn.close()

        if not row:
            self.send_json({"error": "Question not found"}, status=404)
            return

        area = row[3]
        subtopic = row[4]
        text = row[8]
        clues = get_physics_clues(area, subtopic, qid, text)

        profile_name = get_active_profile_name()
        u_state = get_question_user_state(qid, profile_name)

        self.send_json({
            "id": row[0],
            "exam_id": row[1],
            "tag": row[2],
            "area": row[3],
            "subtopic": row[4],
            "question_type": row[5],
            "page": row[6],
            "has_image": bool(row[7]),
            "text": row[8],
            "filename": row[9],
            "flag": row[10],
            "errata": row[11],
            "status": u_state.get("status", "unsolved"),
            "user_notes": u_state.get("notes", ""),
            "image_url": f"/images/{qid.replace('/', '_')}.png",
            "clues": clues
        })

    def handle_post_question_status(self, qid, body):
        status = body.get("status", "unsolved")
        notes = body.get("notes", "")
        flag = body.get("flag", None)
        errata = body.get("errata", None)
        profile_name = get_active_profile_name()

        update_question_user_state(qid, status=status, notes=notes, flag=flag, errata=errata, profile_name=profile_name)
        self.send_json({"success": True, "id": qid, "status": status, "profile": profile_name})

    def handle_api_pairs(self, query):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
        SELECT DISTINCT exam_id, SUBSTR(tag, 1, LENGTH(tag)-1) as stem, area, subtopic
        FROM questions
        WHERE (tag LIKE '%a' OR tag LIKE '%b') AND language = 'PT'
        ORDER BY exam_id DESC, stem ASC
        """)
        stems = cur.fetchall()
        conn.close()

        pairs = []
        for ex, stem, a, sub in stems:
            pairs.append({
                "exam_id": ex,
                "stem": stem,
                "area": a,
                "subtopic": sub,
                "qid_a": f"{ex}-{stem}a",
                "qid_b": f"{ex}-{stem}b",
                "image_a": f"/images/{ex}-{stem}a.png",
                "image_b": f"/images/{ex}-{stem}b.png"
            })
        self.send_json({"total_pairs": len(pairs), "pairs": pairs})

    def handle_api_pair_detail(self, stem_combined):
        if ":::" in stem_combined:
            exam_id, stem = stem_combined.split(":::", 1)
        elif "-" in stem_combined:
            parts = stem_combined.split("-")
            exam_id = f"{parts[0]}-{parts[1]}"
            stem = "-".join(parts[2:])
        else:
            exam_id, stem = "", stem_combined

        qid_a = f"{exam_id}-{stem}a"
        qid_b = f"{exam_id}-{stem}b"

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT text, area, subtopic FROM questions WHERE id = ?", (qid_a,))
        row_a = cur.fetchone()
        cur.execute("SELECT text, area, subtopic FROM questions WHERE id = ?", (qid_b,))
        row_b = cur.fetchone()
        conn.close()

        text_a = row_a[0] if row_a else ""
        text_b = row_b[0] if row_b else ""
        area = (row_a[1] if row_a else None) or (row_b[1] if row_b else "Física")
        subtopic = (row_a[2] if row_a else None) or (row_b[2] if row_b else "Core Problems")

        diff_text = ""
        if text_a and text_b:
            try:
                from bank.differ import format_inline_diff
                diff_text = format_inline_diff(text_a, text_b)
            except Exception:
                diff_text = ""

        self.send_json({
            "exam_id": exam_id,
            "stem": stem,
            "area": area,
            "subtopic": subtopic,
            "qid_a": qid_a,
            "qid_b": qid_b,
            "text_a": text_a,
            "text_b": text_b,
            "diff": diff_text,
            "image_a": f"/images/{qid_a.replace('/', '_')}.png",
            "image_b": f"/images/{qid_b.replace('/', '_')}.png"
        })

    def handle_api_profiles(self):
        profiles, active = list_profiles()
        self.send_json({"profiles": profiles, "active_profile": active})

    def handle_post_switch_profile(self, body):
        name = body.get("profile_name", "default").strip()
        active = set_active_profile_name(name)
        self.send_json({"success": True, "active_profile": active})

    def handle_post_ingest(self, body):
        pdf_path = body.get("pdf_path", "").strip()
        if not pdf_path or not os.path.exists(pdf_path):
            self.send_json({"error": "Invalid PDF file path"}, status=400)
            return
        from bank.ingest import ingest_pdf
        total = ingest_pdf(pdf_path)
        self.send_json({"success": True, "questions_ingested": total})

    def handle_api_concept_map(self):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
        SELECT area, subtopic, COUNT(*) as count
        FROM questions
        WHERE language = 'PT'
        GROUP BY area, subtopic
        ORDER BY area, COUNT(*) DESC
        """)
        rows = cur.fetchall()
        conn.close()

        tree = {}
        for area, sub, cnt in rows:
            if area not in tree:
                tree[area] = {"total": 0, "subtopics": []}
            tree[area]["total"] += cnt
            tree[area]["subtopics"].append({"name": sub, "count": cnt})

        self.send_json({"concept_tree": tree})


def start_server(port=8000):
    server = ThreadingHTTPServer(("0.0.0.0", port), EUFWebHandler)
    print("=" * 65)
    print(f"🚀 EUF Dedicated Web Workspace is running live at:")
    print(f"   👉 http://localhost:{port}")
    print(f"   (Zero-install, works on Mobile, Tablet & Desktop)")
    print("=" * 65)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()


if __name__ == "__main__":
    start_server(8000)
