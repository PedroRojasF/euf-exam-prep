# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "pymupdf",
#     "rapidocr_onnxruntime",
#     "plotly",
#     "pandas",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="full", app_title="EUF Exam Master: Interactive Physics Workspace")


@app.cell
def _():
    import os
    import re
    import json
    import sqlite3
    import pandas as pd
    import plotly.express as px
    import marimo as mo
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

    db_path = os.path.join(os.path.dirname(__file__), "bank", "euf_bank.sqlite")
    render_dir = os.path.join(os.path.dirname(__file__), "bank", "rendered")
    os.makedirs(render_dir, exist_ok=True)
    return (
        db_path,
        get_active_profile_name,
        get_physics_clues,
        get_question_user_state,
        json,
        list_profiles,
        load_user_profile,
        mo,
        os,
        pd,
        px,
        re,
        render_dir,
        save_user_profile,
        set_active_profile_name,
        sqlite3,
        update_question_user_state,
    )


@app.cell
def _(db_path, sqlite3):
    def get_connection():
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("PRAGMA table_info(questions)")
        cols = [c[1] for c in cur.fetchall()]
        if "errata" not in cols:
            cur.execute("ALTER TABLE questions ADD COLUMN errata TEXT")
        if "flag" not in cols:
            cur.execute("ALTER TABLE questions ADD COLUMN flag TEXT DEFAULT NULL")
        conn.commit()
        return conn
    return (get_connection,)


@app.cell
def _(get_connection):
    conn_mem = get_connection()
    cur_mem = conn_mem.cursor()
    cur_mem.execute("""
    SELECT q.id, q.exam_id, q.tag, q.area, q.subtopic, q.question_type, q.page, q.has_image, q.text, e.filename, q.flag, q.errata
    FROM questions q
    JOIN exams e ON q.exam_id = e.id
    WHERE q.language = 'PT'
    ORDER BY q.exam_id DESC, q.id ASC
    """)
    all_questions_list = cur_mem.fetchall()
    all_questions_dict = {r[0]: r for r in all_questions_list}

    cur_mem.execute("""
    SELECT DISTINCT exam_id, SUBSTR(tag, 1, LENGTH(tag)-1) as stem, area, subtopic
    FROM questions
    WHERE (tag LIKE '%a' OR tag LIKE '%b') AND language = 'PT'
    ORDER BY exam_id DESC, stem ASC
    """)
    pair_stems_list = cur_mem.fetchall()
    conn_mem.close()
    return (
        all_questions_dict,
        all_questions_list,
        conn_mem,
        cur_mem,
        pair_stems_list,
    )


@app.cell
def _(list_profiles, mo):
    existing_profiles, active_name = list_profiles()
    profile_dropdown = mo.ui.dropdown(
        options=existing_profiles,
        value=active_name,
        label="👤 Active Study Profile:"
    )
    new_profile_input = mo.ui.text(placeholder="Create new user profile (e.g. carlos, guest)...", label="➕ New Profile:")
    create_profile_btn = mo.ui.button(label="Create / Switch", kind="neutral")

    header_profile_bar = mo.hstack([profile_dropdown, new_profile_input, create_profile_btn], justify="end", align="center")

    title_banner = mo.md(
        """
        # 🎓 EUF Exam Master: Interactive Physics Workspace
        ### *Unified Physics Graduate Exam (USP • UNICAMP • UNESP • UFRJ • UFMG)*
        ---
        """
    )
    mo.vstack([header_profile_bar, title_banner])
    return (
        active_name,
        create_profile_btn,
        existing_profiles,
        header_profile_bar,
        new_profile_input,
        profile_dropdown,
        title_banner,
    )


@app.cell
def _(
    create_profile_btn,
    new_profile_input,
    profile_dropdown,
    set_active_profile_name,
):
    current_profile = profile_dropdown.value
    if create_profile_btn.value and new_profile_input.value.strip():
        current_profile = set_active_profile_name(new_profile_input.value.strip())
    elif profile_dropdown.value != current_profile:
        current_profile = set_active_profile_name(profile_dropdown.value)
    return (current_profile,)


@app.cell
def _(all_questions_list, current_profile, load_user_profile, mo):
    user_data = load_user_profile(current_profile)
    user_qs = user_data.get("questions", {})

    total_q = len(all_questions_list)
    solved_q = sum(1 for q in all_questions_list if user_qs.get(q[0], {}).get("status") == 'solved')
    review_q = sum(1 for q in all_questions_list if user_qs.get(q[0], {}).get("status") == 'review')
    failed_q = sum(1 for q in all_questions_list if user_qs.get(q[0], {}).get("status") == 'failed')

    pct_done = (solved_q / total_q * 100) if total_q else 0

    stats_cards = mo.hstack([
        mo.stat(value=f"{total_q}", label="Total Questions (2010-2026)"),
        mo.stat(value=f"{solved_q}", label="Mastered / Solved", caption=f"{pct_done:.1f}% Profile Mastery"),
        mo.stat(value=f"{review_q}", label="Flagged for Review"),
        mo.stat(value=f"{failed_q}", label="To Retry (Failed)")
    ], justify="space-around")

    stats_cards
    return (
        failed_q,
        pct_done,
        review_q,
        solved_q,
        stats_cards,
        total_q,
        user_data,
        user_qs,
    )


@app.cell
def _(all_questions_list, mo):
    areas = ["All Subject Areas"] + sorted(list(set(q[3] for q in all_questions_list)))
    area_select = mo.ui.dropdown(options=areas, value="All Subject Areas", label="🎯 1. Subject Area:")

    exams = ["All Exams (2010-2026)"] + sorted(list(set(q[1] for q in all_questions_list)), reverse=True)
    exam_select = mo.ui.dropdown(options=exams, value="All Exams (2010-2026)", label="🏛️ 3. Exam / Year:")

    status_select = mo.ui.dropdown(options=["All Statuses", "unsolved", "solved", "review", "failed"], value="All Statuses", label="⏳ 4. Status:")
    search_input = mo.ui.text(placeholder="Search concept (e.g. Poynting, Dirac, Carnot, Kepler, Hamilton)...", label="🔍 Search Keyword:")

    return (
        area_select,
        areas,
        exam_select,
        exams,
        search_input,
        status_select,
    )


@app.cell
def _(all_questions_list, area_select, mo):
    if area_select.value == "All Subject Areas":
        available_subtopics = ["All Subtopics"] + sorted(list(set(q[4] for q in all_questions_list)))
    else:
        available_subtopics = ["All Subtopics"] + sorted(list(set(q[4] for q in all_questions_list if q[3] == area_select.value)))

    subtopic_select = mo.ui.dropdown(options=available_subtopics, value="All Subtopics", label="📖 2. Subtopic:")
    return available_subtopics, subtopic_select


@app.cell
def _(
    area_select,
    exam_select,
    mo,
    search_input,
    status_select,
    subtopic_select,
):
    controls = mo.vstack([
        mo.hstack([area_select, subtopic_select, exam_select], justify="start", align="center"),
        mo.hstack([status_select, search_input], justify="start", align="center")
    ])
    controls
    return (controls,)


@app.cell
def _(
    all_questions_list,
    area_select,
    exam_select,
    mo,
    search_input,
    status_select,
    subtopic_select,
    user_qs,
):
    filtered_qs = []
    _search_term = search_input.value.strip().lower()

    for _q in all_questions_list:
        _qid, _exam_id, _tag, _area, _subtopic, _qtype, _page, _has_img, _text, _fn, _flag, _errata = _q
        _u_state = user_qs.get(_qid, {})
        _status = _u_state.get("status", "unsolved")

        if area_select.value != "All Subject Areas" and _area != area_select.value:
            continue
        if subtopic_select.value != "All Subtopics" and _subtopic != subtopic_select.value:
            continue
        if exam_select.value != "All Exams (2010-2026)" and _exam_id != exam_select.value:
            continue
        if status_select.value != "All Statuses" and _status != status_select.value:
            continue
        if _search_term and (_search_term not in _text.lower() and _search_term not in _subtopic.lower() and _search_term not in _qid.lower()):
            continue

        filtered_qs.append((_q, _status))

    sub_total = len(filtered_qs)
    sub_solved = sum(1 for q, st in filtered_qs if st == 'solved')
    sub_pct = (sub_solved / sub_total * 100) if sub_total else 0

    q_options = {f"[{r[0][0]}] {r[0][3]} ➔ {r[0][4]} ({r[1]})" + (f" ⚠️ {r[0][10]}" if r[0][10] else ""): r[0][0] for r in filtered_qs}

    if not q_options:
        selected_q = mo.ui.dropdown(options={"No questions match current filters": ""}, value="No questions match current filters")
    else:
        selected_q = mo.ui.dropdown(options=q_options, value=list(q_options.keys())[0], label="📌 Select Individual Question:")

    selector_pane = mo.vstack([
        mo.md(f"**⚡ Filtered Pool: {sub_total} questions | Subtopic Mastery: `{sub_pct:.1f}%` ({sub_solved}/{sub_total} solved)**"),
        selected_q
    ])
    selector_pane
    return (
        filtered_qs,
        q_options,
        selected_q,
        selector_pane,
        sub_pct,
        sub_solved,
        sub_total,
    )


@app.cell
def _(
    all_questions_dict,
    current_profile,
    get_physics_clues,
    get_question_user_state,
    mo,
    os,
    render_dir,
    selected_q,
):
    if not selected_q.value or selected_q.value not in all_questions_dict:
        content_pane = mo.md("*Please select a question from the dropdown above.*")
        mark_status = None
        notes_input = None
        flag_select = None
        errata_input = None
        save_btn = None
    else:
        row = all_questions_dict[selected_q.value]
        qid, exam_id, q_tag, area, subtopic, qtype, page, has_img, text, filename, flag, errata = row

        u_state = get_question_user_state(qid, current_profile)
        status = u_state.get("status", "unsolved")
        user_notes = u_state.get("notes", "")

        clues = get_physics_clues(area, subtopic, qid, text)

        img_path = os.path.join(render_dir, f"{qid.replace('/', '_')}.png")
        if os.path.exists(img_path):
            img_element = mo.image(src=img_path, width=840)
        else:
            img_element = mo.md("*(Rendering official visual card...)*")

        status_icon = {"unsolved": "⏳ Unsolved", "solved": "✅ Mastered", "review": "🔁 Needs Review", "failed": "❌ Failed / Retry"}.get(status, status)

        mark_status = mo.ui.dropdown(options=["unsolved", "solved", "review", "failed"], value=status, label="Update Status:")
        notes_input = mo.ui.text_area(value=user_notes or "", placeholder="Personal notes, key formulas, algebra pitfalls, shortcuts...", label="Personal Study Notes:")
        
        flag_select = mo.ui.dropdown(options={"No Warning": "", "⚠️ Official Errata / Annulled": "anulada", "⚠️ Ambiguous Statement": "ambígua", "⚠️ Typo in Options": "typo"}, value="No Warning" if not flag else ("⚠️ Official Errata / Annulled" if flag=="anulada" else "⚠️ Ambiguous Statement"), label="Flag / Notice:")
        errata_input = mo.ui.text(value=errata or "", placeholder="e.g. Annulled by committee due to sign error in option B...", label="Errata Description:")
        save_btn = mo.ui.button(label="💾 Save Progress & Notes", kind="success")

        # Dynamic Contextual Physics Clues
        physics_clues = mo.accordion({
            "💡 Level 1: Core Physical Principle & Conservation Law": mo.md(clues["level1"]),
            "📐 Level 2: Coordinates, Setup & Equations of Motion": mo.md(clues["level2"]),
            "🔍 Level 3: Intermediate Math Checkpoint & Dimensional Check": mo.md(clues["level3"]),
            "🎯 Level 4: Physical Boundary Limits & Option Traps": mo.md(clues["level4"])
        })

        errata_banner = mo.md("")
        if flag or errata:
            errata_banner = mo.md(
                f"""
                > ⚠️ **OFFICIAL NOTICE / ERRATA REGISTERED:**  
                > {errata or 'Question flagged with notice by student/committee.'}
                """
            )

        info_header = mo.md(
            f"""
            ### 📝 {qid} [Profile: `{current_profile}`]
            **Exam:** `{exam_id}` (Page {page}, File: `{filename}`) | **Area:** `{area}` ➔ **{subtopic}**  
            **Type:** *{qtype.title()}* | **Status:** `{status_icon}`
            ---
            """
        )

        content_pane = mo.vstack([
            info_header,
            errata_banner,
            mo.md("#### 📸 Official Question Card (Original LaTeX Formulas, Diagrams & Options A-E):"),
            img_element,
            mo.md("#### 📐 Physics Solution Strategy & Clues (Self-Evaluation):"),
            physics_clues,
            mo.hstack([mark_status, notes_input], align="start"),
            mo.hstack([flag_select, errata_input, save_btn], align="center")
        ])

    content_pane
    return (
        area,
        clues,
        content_pane,
        errata,
        errata_banner,
        errata_input,
        exam_id,
        filename,
        flag,
        flag_select,
        has_img,
        img_element,
        img_path,
        info_header,
        mark_status,
        notes_input,
        page,
        physics_clues,
        q_tag,
        qid,
        qtype,
        row,
        save_btn,
        status,
        status_icon,
        subtopic,
        text,
        u_state,
        user_notes,
    )


@app.cell
def _(
    current_profile,
    errata_input,
    flag_select,
    mark_status,
    mo,
    notes_input,
    save_btn,
    selected_q,
    update_question_user_state,
):
    if save_btn is not None and save_btn.value and selected_q.value:
        flag_val = flag_select.value if flag_select and flag_select.value else None
        errata_val = errata_input.value if errata_input and errata_input.value.strip() else None
        update_question_user_state(
            selected_q.value,
            status=mark_status.value,
            notes=notes_input.value,
            flag=flag_val,
            errata=errata_val,
            profile_name=current_profile
        )
        saved_msg = mo.md(f"✅ **Saved progress for `{selected_q.value}` to profile `{current_profile}`!**")
    else:
        saved_msg = mo.md("")
    saved_msg
    return errata_val, flag_val, saved_msg


@app.cell
def _(all_questions_list, mo, pd, px):
    df_map = pd.DataFrame([{
        "Area": q[3],
        "Subtopic": q[4],
        "Exam": q[1]
    } for q in all_questions_list])

    df_counts = df_map.groupby(["Area", "Subtopic"]).size().reset_index(name="Questions")

    fig_sunburst = px.sunburst(
        df_counts,
        path=["Area", "Subtopic"],
        values="Questions",
        color="Area",
        title="🧠 Interactive EUF Knowledge Map (Click any slice to zoom into subtopics)",
        height=520
    )
    fig_sunburst.update_layout(margin=dict(t=40, l=0, r=0, b=0))

    map_component = mo.vstack([
        mo.md("--- \n## 🧠 Interactive Visual Knowledge Map"),
        mo.ui.plotly(fig_sunburst)
    ])
    map_component
    return df_counts, df_map, fig_sunburst, map_component


@app.cell
def _(mo, pair_stems_list):
    pair_options = {f"{r[0]} | {r[1]} ({r[2]} - {r[3]})": f"{r[0]}:::{r[1]}" for r in pair_stems_list}
    pair_select = mo.ui.dropdown(options=pair_options, value=list(pair_options.keys())[0] if pair_options else "", label="👥 Choose an A/B Pair:")

    mo.vstack([
        mo.md("--- \n## 👥 Twin Question Lab (Side-by-Side Visual Variant A vs Variant B)"),
        pair_select
    ])
    return pair_options, pair_select


@app.cell
def _(mo, os, pair_select, render_dir):
    if not pair_select.value:
        diff_view = mo.md("Select a pair above.")
    else:
        exam_id_p, stem_p = pair_select.value.split(":::", 1)

        qid_a = f"{exam_id_p}-{stem_p}a"
        qid_b = f"{exam_id_p}-{stem_p}b"

        img_a_path = os.path.join(render_dir, f"{qid_a.replace('/', '_')}.png")
        img_b_path = os.path.join(render_dir, f"{qid_b.replace('/', '_')}.png")

        img_a = mo.image(src=img_a_path, width=540) if os.path.exists(img_a_path) else mo.md(f"*(Card A not found for {qid_a})*")
        img_b = mo.image(src=img_b_path, width=540) if os.path.exists(img_b_path) else mo.md(f"*(Card B not found for {qid_b})*")

        diff_view = mo.vstack([
            mo.hstack([
                mo.vstack([mo.md(f"#### 🅰️ Variant A (`{qid_a}`)"), img_a]),
                mo.vstack([mo.md(f"#### 🅱️ Variant B (`{qid_b}`)"), img_b])
            ], justify="space-between")
        ])

    diff_view
    return diff_view, exam_id_p, img_a, img_a_path, img_b, img_b_path, qid_a, qid_b, stem_p


@app.cell
def _(mo):
    pdf_upload = mo.ui.file(filetypes=[".pdf"], multiple=False, label="📤 Upload New Exam PDF:")
    
    ingest_panel = mo.accordion({
        "📥 Add / Ingest New Exam PDF to Bank": mo.vstack([
            mo.md(
                """
                **How to add future exam PDFs:**  
                1. Upload or drag & drop any new EUF PDF into this box, OR drop the PDF in the folder and run `python euf.py sync`.  
                2. The engine parses the PDF, classifies subtopics, and pre-renders high-res crops automatically.
                """
            ),
            pdf_upload
        ])
    })
    ingest_panel
    return ingest_panel, pdf_upload


if __name__ == "__main__":
    app.run()
