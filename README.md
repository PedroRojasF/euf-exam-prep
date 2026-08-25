# 🎓 EUF Exam Master (2010 – 2026)

Unified Graduate Physics Exam Practice System (*Exame Unificado de Pós-Graduação em Física - USP, UNICAMP, UNESP, UFRJ, UFMG*).

---

## 🚀 Features

* **Complete Exam Bank (2010–2026)**: 988 official questions indexed across Classical Mechanics, Electromagnetism, Quantum Mechanics, Thermodynamics & Statistical Physics, and Modern Physics.
* **100% Visual High-Res Rendering**: Precision-cropped vector cards (200 DPI) preserving exact LaTeX typography, equations, diagrams, and full options A–E.
* **Twin A/B Laboratory**: 304 complete pairs of Variant A vs Variant B with side-by-side comparison.
* **Hierarchical Cascading Taxonomy**: 3-level filtering (Subject Area ➔ Specific Subtopic ➔ Exam Year ➔ Status).
* **Multi-User Profile Manager**: Personal study notes, solved status, and error logs are isolated in portable profile files (`profiles/<username>.json`), allowing easy sharing without overwriting personal progress.
* **Interactive Visual Mind Map**: Zoomable Sunburst knowledge map and taxonomy overview.
* **Socratic AI Feedback Ladder**: 4-tiered hint progression (Principle ➔ Coordinates/Setup ➔ Checkpoint ➔ Full Derivation & Committee Trap Analysis).

---

## 💻 Quick Start

### 1. Launch Interactive Marimo Web App
```bash
marimo run app.py
```

### 2. Launch Dedicated Web App (Fast & Mobile Friendly)
```bash
python -m webapp.server
# or
python euf.py web
```

### 3. CLI Helper Commands
```bash
# Check stats and mastery
python euf.py stats
python euf.py progress

# List questions by subtopic
python euf.py list -a mc -s "Lagrangian"

# View specific question details & render crop
python euf.py show 2026-1-emPT1a
python euf.py render 2026-1-emPT1a

# Compare twin variants A and B
python euf.py diff 2025-1-mcPT1a
python euf.py pair 2025-1-mcPT1

# Ingest new exam PDF
python euf.py ingest path/to/new_exam.pdf
python euf.py sync
```
