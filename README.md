# ⚛️ EUF Exam Master

> **Interactive Precision Study Suite & Problem Bank for the Unified Graduate Physics Examination (Exame Unificado das Pós-Graduações em Física — Brasil).**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Framework: Svelte 5](https://img.shields.io/badge/Framework-Svelte_5-orange.svg)](https://svelte.dev/)
[![Engine: KaTeX](https://img.shields.io/badge/Math-KaTeX-brightgreen.svg)](https://katex.org/)
[![Database: SQLite / JSON](https://img.shields.io/badge/Database-SQLite%20%7C%20JSON-lightgrey.svg)](bank/)

---

## 📖 Overview

**EUF Exam Master** is a high-density, deliberate-practice web application and CLI toolkit designed for graduate candidates preparing for the **EUF** (the admission exam for MSc/PhD programs in Physics across top Brazilian universities, including USP, UNICAMP, UNESP, UFRJ, UFMG, CBPF, and others).

It consolidates all official exam editions (2010–2026) into a structured taxonomy across the 6 core physical domains, providing high-resolution vector crops, step-by-step Socratic physics hints in 3 languages, side-by-side twin variant analysis, and a personal spaced repetition error diary.

---

## ✨ Key Features

- 🎯 **783+ Official Questions (2010–2026)**:
  Every question is indexed and tagged by subject domain, specific subtopic, and exam edition.
- 📐 **Vector High-Fidelity Problem Cards**:
  Displays clean, vector-rendered crops of the original exam sheets, preserving complex multi-line LaTeX equations, circuit schematics, graphs, and formatting.
- 💡 **4-Level Socratic Hint Ladder (Tri-lingual: PT / ES / EN)**:
  Contextual physics clues structured into:
  1. *Fundamental Physical Principle & Conservation Laws*
  2. *Coordinate System Setup & Degrees of Freedom*
  3. *Intermediate Mathematical Checkpoint & Dimensional Analysis*
  4. *Physical Boundary Limits & Exam Traps*
- 🔬 **Twin A/B Variant Laboratory**:
  Side-by-side comparison of sister problems (Variant A vs. Variant B) to analyze how parameters and target variables change across test versions.
- ⏱️ **15-Minute Deliberate Practice Timer**:
  Simulates realistic exam conditions (average 15 minutes per problem in official sessions).
- 📝 **Spaced Repetition & Personal Error Diary**:
  Classify problems as **Mastered (`S`)**, **For Review (`R`)**, or **Failed / To Retry (`X`)** with personal LaTeX-enabled scratchpad notes.
- 🌐 **Tri-Lingual Interface**:
  Instant switching between **Português**, **Español**, and **English**.
- 🚀 **100% Client-Side Static SPA**:
  Runs locally or hosted on GitHub Pages / Cloudflare Pages with zero backend server requirement.

---

## 🏛️ Subject Taxonomy (6 Core Domains)

| Domain | Tag | Coverage Topics |
| :--- | :---: | :--- |
| **Mecânica Clássica** | `mc` | Lagrangian Mechanics, Hamiltonian Dynamics, Central Forces & Kepler Orbits, Rigid Body & Inertia Tensor, Small Oscillations & Normal Modes, Collisions & Variable Mass. |
| **Eletromagnetismo** | `em` | Gauss's Law, Boundary Value Problems, Method of Images, Dielectrics, Biot-Savart & Ampère's Laws, Faraday Motional EMF, Maxwell Equations, Poynting Vector & Polarization. |
| **Mecânica Quântica** | `mq` | Harmonic Oscillator Ladder Algebra, Dirac Bra-Ket Formalism, 1D Potential Wells & Tunneling, Angular Momentum & Spin, Perturbation Theory, Identical Particles. |
| **Termodinâmica** | `te` | 1st & 2nd Laws, Thermodynamic Cycles (Carnot/Otto), Potentials & Maxwell Relations, Ideal/Real Gases, Phase Transitions & Clausius-Clapeyron, Heat Capacities. |
| **Física Estatística** | `fe` | Microcanonical & Canonical Ensembles, Partition Functions, Grand Canonical Potential, Quantum Gases (Fermi-Dirac & Bose-Einstein), Spin Systems & Paramagnetism. |
| **Física Moderna** | `fm` | Special Relativity & Lorentz Transformations, Relativistic Dynamics, Photoelectric Effect, Compton Scattering, de Broglie Matter Waves, Bohr/Rydberg Atomic Models. |

---

## 🚀 Quick Start

### 1. Web Application (Svelte 5 + Vite)

```bash
# Clone the repository
git clone https://github.com/your-username/euf-master.git
cd euf-master

# Enter frontend directory
cd frontend

# Install dependencies (using npm, pnpm, or bun)
npm install

# Start local development server
npm run dev
```

Visit `http://localhost:5173` in your browser.

To compile a production-ready static build:
```bash
npm run build
# Output is generated in frontend/dist/ (ready for GitHub Pages or Cloudflare Pages)
```

---

### 2. Python CLI Assistant (`euf.py`)

The workspace includes a standalone Python CLI tool for quick terminal study, database inspection, and batch processing.

```bash
# Display bank taxonomy and your mastery statistics
python euf.py stats

# Launch local Python web workspace
python euf.py web --port 8000

# Compare twin variants A and B for a specific problem
python euf.py diff 2025-1-mcPT1a

# Search problems by physical concept
python euf.py search "Poynting"

# Export static questions.json from SQLite
python euf.py export
```

---

## ⚡ Remote VPS Processing Pipeline (`vps-build`)

For heavy OCR indexing and high-DPI rendering without consuming local CPU resources, `euf.py` includes a remote orchestration command:

```bash
# Executes PyMuPDF + RapidOCR + multi-core rendering on your remote server and syncs locally
python euf.py vps-build --host my-vps
```

**How it works:**
1. Connects to your configured VPS via SSH.
2. Transfers new PDF exam booklets.
3. Runs parallel multi-core OCR and vector cropping on the VPS.
4. Downloads the updated `questions.json`, SQLite database, and new rendered image cards back to your local machine.

---

## 🌐 Public Deployment (GitHub Pages / Cloudflare)

Since the entire application runs as a static Single-Page Application (SPA) reading from `questions.json`:

### Cloudflare Pages (Recommended - 0ms Cold Start)
1. Link your GitHub repository in Cloudflare Pages dashboard.
2. Build settings:
   - **Framework preset**: `Vite`
   - **Root directory**: `frontend`
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`

### GitHub Pages
1. A GitHub Actions workflow is included at `.github/workflows/deploy.yml`.
2. Go to repository **Settings -> Pages -> Source** and select **GitHub Actions**.

---

## 📜 Academic Fair Use & License

- **Software Platform**: Licensed under the [MIT License](LICENSE).
- **Exam Content**: The original exam questions, official diagrams, and answer keys are the intellectual property of the **Comissão do Exame Unificado das Pós-Graduações em Física (EUF)** and the **Sociedade Brasileira de Física (SBF)**. They are included strictly for non-profit academic training, deliberate practice, and educational research under Fair Use.
