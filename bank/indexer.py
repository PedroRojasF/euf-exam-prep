"""EUF Exam Indexer and Question Bank Generator (Strict Physics Taxonomy).
Extracts only genuine physics problems (Mecânica Clássica, Quântica, Eletromagnetismo, Termo/Estatística, Física Moderna).
Filters out formula sheets, commutator brackets, instructions, and bubble answer sheets.
"""

import os
import re
import sys
import glob
import json
import sqlite3
import unicodedata
import pymupdf
from rapidocr_onnxruntime import RapidOCR

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ocr_engine = RapidOCR()

DB_PATH = os.path.join(os.path.dirname(__file__), "euf_bank.sqlite")
RENDER_DIR = os.path.join(os.path.dirname(__file__), "rendered")

AREA_MAPPING = {
    "mc": "Mecânica Clássica",
    "em": "Eletromagnetismo",
    "mq": "Mecânica Quântica",
    "fm": "Física Moderna",
    "te": "Termodinâmica",
    "fe": "Física Estatística",
}

SUBTOPIC_RULES = {
    "Mecânica Clássica": [
        ("Lagrangian Mechanics & Constraints", [r"lagrang", r"graus de liberdade", r"coordenadas generalizadas", r"v[íi]nculo", r"multiplicador"]),
        ("Hamiltonian Mechanics & Phase Space", [r"hamilton", r"espa[çc]o de fase", r"can[ôo]nic", r"poisson"]),
        ("Central Forces & Kepler Orbits", [r"for[çc]a central", r"potencial efetivo", r"kepler", r"[óo]rbita", r"momento angular", r"gravita[çc]", r"apogeu", r"perigeu", r"sat[ée]lite"]),
        ("Rigid Body & Rotational Dynamics", [r"corpo r[íi]gido", r"momento de in[ée]rcia", r"tensor de in[ée]rcia", r"rolamento", r"torque", r"disco", r"cilindro", r"esfera", r"pi[ãa]o"]),
        ("Small Oscillations & Normal Modes", [r"modos normais", r"pequenas oscila[çc]", r"frequ[êe]ncias pr[óo]prias", r"matriz.*acoplamento", r"p[êe]ndulo acoplado", r"resson[âa]ncia", r"oscilador"]),
        ("Collisions & Momentum Conservation", [r"colis[ãa]o", r"conserva[çc][ãa]o do momento", r"centro de massa", r"impulso", r"proj[ée]til", r"choque", r"massa vari[áa]vel", r"corda.*puxada"]),
        ("Newtonian Dynamics & Energy", [r"newton", r"energia mec[âa]nica", r"atrito", r"trabalho", r"plano inclinado", r"acelera[çc][ãa]o"]),
    ],
    "Eletromagnetismo": [
        ("Electrostatics & Boundary Value Problems", [r"laplace", r"poisson", r"m[ée]todo das imagens", r"condi[çc][õo]es de contorno", r"potencial eletrost[áa]tico", r"esfera condutora", r"lei de gauss", r"carga.*anel", r"casca esf[ée]rica", r"campo el[ée]trico", r"densidade de carga", r"potencial el[ée]trico", r"distribui[çc][ãa]o de carga"]),
        ("Capacitors & Dielectric Media", [r"diel[ée]tric", r"polariza[çc][ãa]o", r"vetor d", r"permissividade", r"capacitor", r"capacit[âa]ncia", r"energia eletrost[áa]tica"]),
        ("Magnetostatics & Magnetic Fields", [r"biot-savart", r"potencial vetor", r"magnetiza[çc][ãa]o", r"campo h", r"solenoide", r"torque magn[ée]tico", r"lei de amp[èe]re", r"campo magn[ée]tico", r"espira", r"corrente estacion[áa]ria"]),
        ("Electromagnetic Induction & Faraday", [r"faraday", r"fem induzida", r"indut[âa]ncia", r"corrente induzida", r"fluxo magn[ée]tico", r"lei de lenz"]),
        ("Maxwell Equations & EM Waves", [r"poynting", r"ondas eletromagn[ée]ticas", r"equa[çc][õo]es de maxwell", r"radia[çc][ãa]o", r"polariza[çc][ãa]o da luz", r"fresnel", r"vetor de onda", r"velocidade da luz", r"vácuo"]),
        ("Electromagnetic Radiation & Dipoles", [r"radia[çc][ãa]o dipolar", r"potenciais retardados", r"larmor", r"antena", r"dipolo"]),
    ],
    "Mecânica Quântica": [
        ("Harmonic Oscillator & Ladder Operators", [r"operador de cria[çc][ãa]o", r"operador de aniquila[çc][ãa]o", r"a\^?\†|a\^\+", r"oscilador harm[ôo]nico", r"n[íi]veis de energia.*oscilador", r"potencial harm[ôo]nico"]),
        ("Dirac Formalism & Hilbert Space", [r"comutador", r"incerteza", r"postulado", r"produto interno", r"autovetor", r"autovalor", r"hermitian", r"bra-ket", r"projetor", r"observ[áa]vel", r"base ortonormal", r"notação de dirac", r"matriz hamiltoniana"]),
        ("Potential Wells & Tunneling", [r"po[çc]o", r"tunelamento", r"barreira de potencial", r"transmiss[ãa]o", r"reflex[ãa]o", r"fun[çc][ãa]o de onda", r"degrau de potencial", r"coeficiente"]),
        ("Angular Momentum & Spin Algebra", [r"spin", r"pauli", r"clebsch-gordan", r"j_z|s_z|l_z|j\^2|s\^2", r"adi[çc][ãa]o de momento", r"harm[ôo]nicos esf[ée]ricos", r"matriz.*spin", r"momento angular"]),
        ("Perturbation Theory & Approximations", [r"perturba[çc][ãa]o", r"primeira ordem", r"segunda ordem", r"hamiltoniano perturbado", r"stark", r"zeeman", r"wkb", r"variacional", r"corre[çc][ãa]o"]),
        ("Hydrogen Atom & Central Potentials", [r"hidrog[êe]nio", r"raio de bohr", r"orbital", r"n[úu]meros qu[âa]nticos", r"potencial coulombiano", r"raio.*bohr"]),
        ("Identical Particles & Multi-State Systems", [r"b[óo]son", r"f[ée]rmion", r"exclus[ãa]o", r"anti-sim[ée]trica", r"part[íi]culas id[êe]nticas", r"pauli.*princ[íi]pio"]),
    ],
    "Termodinâmica": [
        ("1st & 2nd Laws / Thermodynamic Cycles", [r"carnot", r"rendimento", r"ciclo", r"adiab[áa]tic", r"isot[ée]rmic", r"trabalho realizado", r"efici[êe]ncia", r"m[áa]quina t[ée]rmica"]),
        ("Thermodynamic Potentials & Maxwell Relations", [r"maxwell.*rela[çc]", r"helmholtz", r"gibbs", r"entalpia", r"potencial qu[íi]mico", r"energia livre"]),
        ("Ideal & Real Gases", [r"g[áa]s ideal", r"van der waals", r"calor espec[íi]fico", r"equa[çc][ãa]o de estado", r"press[ãa]o", r"volume", r"g[áa]s monoat[ôo]mico"]),
        ("Phase Transitions & Entropy", [r"transi[çc][ãa]o de fase", r"clapeyron", r"calor latente", r"entropia", r"equil[íi]brio t[ée]rmico"]),
    ],
    "Física Estatística": [
        ("Canonical & Microcanonical Ensembles", [r"fun[çc][ãa]o de parti[çc][ãa]o", r"ensemble can[ôo]nico", r"boltzmann", r"microcan[ôo]nico", r"equi-parti[çc][ãa]o", r"energia m[ée]dia", r"distribui[çc][ãa]o"]),
        ("Grand Canonical Ensemble", [r"grande can[ôo]nico", r"grande potencial", r"fugacidade", r"potencial qu[íi]mico"]),
        ("Quantum Gases (Fermi-Dirac & Bose-Einstein)", [r"bose-einstein", r"fermi-dirac", r"energia de fermi", r"temperatura de fermi", r"condensa[çc][ãa]o", r"corpo negro", r"f[óo]tons.*g[áa]s", r"g[áa]s degenerado"]),
        ("Spin Systems & Paramagnetism", [r"paramagnetismo", r"ising", r"magnetiza[çc][ãa]o m[ée]dia", r"susceptibilidade", r"curie", r"campo externo"]),
    ],
    "Física Moderna": [
        ("Special Relativity & Lorentz Transformations", [r"lorentz", r"contraction", r"dilata[çc][ãa]o", r"quadrivetor", r"energia relativ[íi]stica", r"doppler relativ[íi]stico", r"espa[çc]o-tempo", r"intervalo invariante", r"simultaneidade", r"massa de repouso"]),
        ("Early Quantum & Thermal Radiation", [r"fotoel[ée]tric", r"compton", r"de broglie", r"f[óo]ton", r"radia[çc][ãa]o de corpo negro", r"lei de wien", r"planck"]),
        ("Atomic Models & Quantum Phenomena", [r"bohr", r"franck-hertz", r"raios x", r"massa reduzida", r"espectro"]),
    ]
}


def is_garbled(text):
    if len(text.strip()) < 50:
        return True
    if '\x00' in text or '\ufffd' in text:
        return True
    alpha = sum(1 for c in text if c.isalpha())
    if alpha == 0:
        return True
    vowels = sum(1 for c in text if c.lower() in 'aeiouáéíóúâêîôûãõ')
    if vowels / alpha < 0.2:
        return True
    return False


def clean_latex_accents(text):
    t = text
    replacements = [
        ('ˆa', 'â'), ('´a', 'á'), ('`a', 'à'), ('˜a', 'ã'),
        ('ˆe', 'ê'), ('´e', 'é'), ('`e', 'è'),
        ('ˆı', 'î'), ('´ı', 'í'), ('`ı', 'ì'), ('ˆi', 'î'), ('´i', 'í'),
        ('ˆo', 'ô'), ('´o', 'ó'), ('`o', 'ò'), ('˜o', 'õ'),
        ('ˆu', 'û'), ('´u', 'ú'), ('`u', 'ù'),
        ('¸c', 'ç'), ('¨u', 'ü'),
        ('ˆA', 'Â'), ('´A', 'Á'), ('`A', 'À'), ('˜A', 'Ã'),
        ('ˆE', 'Ê'), ('´E', 'É'),
        ('´I', 'Í'), ('ˆI', 'Î'),
        ('ˆO', 'Ô'), ('´O', 'Ó'), ('˜O', 'Õ'),
        ('´U', 'Ú'), ('ˆU', 'Û'),
        ('¸C', 'Ç')
    ]
    for old, new in replacements:
        t = t.replace(old, new)

    t = re.sub(r'a\s+rmaç', 'afirmaç', t)
    t = re.sub(r'a\s+rma', 'afirma', t)
    t = re.sub(r'\b\s+gura\b', 'figura', t)
    t = re.sub(r'\b\s+guras\b', 'figuras', t)
    t = re.sub(r'con\s+nada', 'confinada', t)
    t = re.sub(r'con\s+nado', 'confinado', t)
    t = re.sub(r'espec[íi]\s+ca', 'específica', t)
    t = re.sub(r'espec[íi]\s+co', 'específico', t)
    t = re.sub(r'\b\s+o inextens', 'fio inextens', t)
    t = re.sub(r'\b\s+nal\b', 'final', t)
    return t


def get_page_text_robust(page):
    raw = page.get_text()
    if not is_garbled(raw):
        return clean_latex_accents(raw)
    pix = page.get_pixmap(dpi=150)
    res, _ = ocr_engine(pix.tobytes())
    if res:
        return clean_latex_accents("\n".join([line[1] for line in res]))
    return ""


def classify_subtopic(area, text):
    text_clean = clean_latex_accents(text).lower()
    rules = SUBTOPIC_RULES.get(area, [])
    for sub_name, patterns in rules:
        if any(re.search(p, text_clean) for p in patterns):
            return sub_name
    return f"{area} - Core Problems"


def init_database(db_path=DB_PATH):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    os.makedirs(RENDER_DIR, exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS exams (
        id TEXT PRIMARY KEY,
        year INTEGER,
        semester INTEGER,
        filename TEXT,
        num_pages INTEGER,
        exam_type TEXT,
        has_text INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY,
        exam_id TEXT,
        question_num INTEGER,
        tag TEXT,
        area TEXT,
        subtopic TEXT,
        language TEXT,
        page INTEGER,
        has_image INTEGER,
        question_type TEXT,
        text TEXT,
        status TEXT DEFAULT 'unsolved',
        user_notes TEXT,
        flag TEXT DEFAULT NULL,
        errata TEXT DEFAULT NULL,
        FOREIGN KEY (exam_id) REFERENCES exams(id)
    )
    """)

    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS questions_fts USING fts5(
        id UNINDEXED,
        exam_id,
        area,
        subtopic,
        text,
        content='questions',
        content_rowid='rowid'
    )
    """)

    conn.commit()
    return conn


def extract_year_semester(filename):
    m = re.search(r'(?:euf-)?(20\d{2})[-_]?([123])?', filename)
    if m:
        year = int(m.group(1))
        sem = int(m.group(2)) if m.group(2) else 1
        return year, sem
    return 2020, 1


def parse_pdf_document(pdf_path, year, sem, exam_id):
    """Universal parser with strict physics tag validation (rejects formula sheets & bubble sheets)."""
    doc = pymupdf.open(pdf_path)
    questions = []

    # Valid EUF tag prefixes
    valid_prefixes = {"mc", "em", "mq", "fm", "fe", "te"}

    for page_idx, page in enumerate(doc):
        p_text = get_page_text_robust(page)
        has_imgs = len(page.get_images()) > 0

        # Skip instructions, formula sheets, and bubble answer sheets
        p_lower = p_text.lower()
        if "instruções para a prova" in p_lower and len(p_text) < 600:
            continue
        if "folha de respostas" in p_lower or "gabarito" in p_lower and "questão 1 :" in p_lower:
            continue
        if "formulário" in p_lower and ("constantes físicas" in p_lower or "regras de propagação" in p_lower):
            continue

        # 1. Check for AMC tag matches like [mcPT1a] or [mc1a]
        tag_matches = list(re.finditer(r'(?:(?:Q\.|Quest[ãa]o)\s*(\d+)\s*)?\[([a-zA-Z]{2,4}\d*[a-zA-Z0-9_-]*)\]', p_text, re.IGNORECASE))
        
        valid_tag_matches = []
        for m in tag_matches:
            raw_tag = m.group(2)
            # Fix common OCR typos
            clean_tag = raw_tag.replace("mmPT", "mcPT").replace("mm", "mc")
            prefix = clean_tag[:2].lower()
            if prefix in valid_prefixes:
                valid_tag_matches.append((m, clean_tag, prefix))

        if valid_tag_matches:
            for i, (m, tag, prefix) in enumerate(valid_tag_matches):
                q_num_str = m.group(1)
                q_num = int(q_num_str) if q_num_str else (i + 1)
                start_pos = m.start()
                end_pos = valid_tag_matches[i+1][0].start() if i+1 < len(valid_tag_matches) else len(p_text)
                q_text = p_text[start_pos:end_pos].strip()

                lang = "EN" if "EN" in tag.upper() else "PT"
                area = AREA_MAPPING[prefix]
                subtopic = classify_subtopic(area, q_text)
                qid = f"{exam_id}-{tag}"

                questions.append({
                    "id": qid,
                    "exam_id": exam_id,
                    "question_num": q_num,
                    "tag": tag,
                    "area": area,
                    "subtopic": subtopic,
                    "language": lang,
                    "page": page_idx + 1,
                    "has_image": 1 if has_imgs else 0,
                    "question_type": "múltipla escolha",
                    "text": q_text
                })
        else:
            # 2. Check for Discursive Q1., Q2., Q10. or Questão 1
            q_pattern = re.compile(r'(?:^|\n)(Q\s*(\d+)|Quest[ãa]o\s*(\d+))[\.:\s]', re.MULTILINE)
            matches = list(q_pattern.finditer(p_text))

            standard_area_map = {
                1: "Mecânica Clássica",
                2: "Mecânica Clássica",
                3: "Física Moderna",
                4: "Mecânica Quântica",
                5: "Termodinâmica",
                6: "Eletromagnetismo",
                7: "Eletromagnetismo",
                8: "Mecânica Quântica",
                9: "Mecânica Quântica",
                10: "Física Estatística",
            }

            for i, m in enumerate(matches):
                q_num_val = int(m.group(2) or m.group(3))
                if not (1 <= q_num_val <= 12):
                    continue

                start = m.start()
                end = matches[i+1].start() if i+1 < len(matches) else len(p_text)
                q_text = p_text[start:end].strip()

                area = standard_area_map.get(q_num_val, "Mecânica Clássica")
                subtopic = classify_subtopic(area, q_text)
                qid = f"{exam_id}-Q{q_num_val:02d}"

                questions.append({
                    "id": qid,
                    "exam_id": exam_id,
                    "question_num": q_num_val,
                    "tag": f"Q{q_num_val}",
                    "area": area,
                    "subtopic": subtopic,
                    "language": "PT",
                    "page": page_idx + 1,
                    "has_image": 1 if has_imgs else 0,
                    "question_type": "discursiva",
                    "text": q_text
                })

    return questions
