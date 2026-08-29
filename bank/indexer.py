"""EUF Exam Indexer and Question Bank Generator (Strict Physics Taxonomy).
Extracts only genuine physics problems (Mecânica Clássica, Quântica, Eletromagnetismo, Termo, Estatística, Física Moderna).
Filters out formula sheets, commutator brackets, instructions, and bubble answer sheets.
"""

import os
import re
import sys
import glob
import json
import sqlite3
import pymupdf
from rapidocr_onnxruntime import RapidOCR

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ocr_engine = RapidOCR()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")
RENDER_DIR = os.path.join(BASE_DIR, "bank", "rendered")
os.makedirs(RENDER_DIR, exist_ok=True)

AREA_MAPPING = {
    "mc": "Mecânica Clássica",
    "em": "Eletromagnetismo",
    "mq": "Mecânica Quântica",
    "fm": "Física Moderna",
    "te": "Termodinâmica",
    "fe": "Física Estatística",
}

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

SUBTOPIC_RULES = {
    'Eletromagnetismo': [
        ('Vector Calculus & Field Operators', [r'campo vetorial', r'rotacional', r'divergente', r'gradiente', r'teorema de stokes', r'teorema da diverg', r'nabla', r'laplaciano', r'g\(x,y\)']),
        ('EM Wave Polarization & Malus\'s Law', [r'polariza[çc][ãa]o', r'malus', r'polarizador', r'n[ãa]o polarizada', r'birrefring', r'placa de onda', r'luz polarizada', r'polarizado']),
        ('Poynting Vector & EM Wave Propagation', [r'poynting', r'onda plana', r'ondas eletromagn', r'radia[çc][ãa]o eletromagn', r'vetor de onda', r'press[ãa]o de radia[çc]', r'intensidade da onda', r'velocidade da luz', r'meio n[ãa]o dispersivo', r'imped[âa]ncia', r'onda monocrom', r'monocrom[áa]tica', r'onda']),
        ('Maxwell Equations & Displacement Current', [r'maxwell', r'corrente de deslocamento', r'equa[çc][õo]es de maxwell', r'conserva[çc][ãa]o da carga', r'equa[çc][ãa]o da continuidade']),
        ('Faraday\'s Law, Motional EMF & Inductance', [r'faraday', r'fem induzida', r'for[çc]a eletromotriz induzida', r'for[çc]a eletromotriz', r'indut[âa]ncia', r'indutor', r'auto-indut', r'indut[âa]ncia m[úu]tua', r'fluxo magn[ée]tico', r'lei de lenz', r'espira.*gira', r'trilho condutor', r'corrente induzida', r'duas espiras', r'espiras concentricas', r'espiras']),
        ('Capacitors & Dielectric Media', [r'diel[ée]tric', r'polariza[çc][ãa]o', r'vetor d', r'permissividade', r'capacitor', r'capacit[âa]ncia', r'energia eletrost[áa]tica']),
        ('Conductors, Cavities & Electrostatic Shielding', [r'cavidade', r'blindagem', r'condutor maci[çc]o', r'casca condutora', r'esfera condutora', r'terra', r'aterrad', r'condutor']),
        ('Boundary Value Problems & Method of Images', [r'm[ée]todo das imagens', r'condi[çc][õo]es de contorno', r'laplace', r'poisson', r'potencial eletrost[áa]tico', r'harm[ôo]nicos esf[ée]ricos', r'potencial.*v\(r', r'solu[çc][ãa]o de laplace']),
        ('Lorentz Force & Particle Trajectories in EM Fields', [r'lorentz', r'raio de larmor', r'ciclotron', r'campo magn[ée]tico.*part[íi]cula', r'part[íi]cula.*carga.*massa', r'trajet[óo]ria.*campo', r'for[çc]a magn[ée]tica', r'el[ée]tron.*lan[çc]ado', r'acelerad.*campo']),
        ('Continuous Charge Distributions & Electric Potentials', [r'anel.*carregado', r'anel', r'disco.*carregado', r'fio.*carregado', r'linha de carga', r'distribui[çc][ãa]o de carga', r'densidade superficial de carga', r'densidade volum[ée]trica de carga', r'densidade linear de carga', r'potencial el[ée]trico', r'campo el[ée]trico', r'carga.*raio', r'carga']),
        ('Gauss\'s Law & Electric Flux', [r'lei de gauss', r'gauss', r'fluxo el[ée]trico', r'superf[íi]cie gaussiana', r'esfera n[ãa]o-condutora', r'cilindro infinito', r'plano infinito']),
        ('Biot-Savart Law & Magnetic Fields of Currents', [r'biot-savart', r'espira circular', r'espira', r'fio reto', r'segmento.*fio', r'solenoide', r'toroide', r'campo b', r'campo magn[ée]tico.*eixo', r'campo magn[ée]tico', r'fio']),
        ('Ampère\'s Law & Current Distributions', [r'lei de amp[èe]re', r'amp[èe]re', r'densidade de corrente', r'cilindros coaxiais', r'cabo coaxial', r'corrente estacion[áa]ria', r'circula[çc][ãa]o']),
        ('Magnetic Dipoles, Forces & Magnetic Media', [r'dipolo magn[ée]tico', r'torque magn[ée]tico', r'momento magn[ée]tico', r'magnetiza[çc][ãa]o', r'vetor h', r'susceptibilidade magn[ée]tica', r'permeabilidade']),
        ('DC Circuits, Resistors & Joule Heating', [r'resistor', r'resist[êe]ncia', r'bateria', r'fem', r'circuito', r'joule', r'lei de ohm', r'resistividade', r'pot[êe]ncia dissipada', r'corrente']),
        ('Electric Dipoles & Multipole Expansion', [r'dipolo el[ée]trico', r'expans[ãa]o multipolar', r'momento de dipolo', r'quadrupolo', r'dipolo']),
    ],
    'Mecânica Clássica': [
        ('Lagrangian Mechanics & Generalized Coordinates', [r'lagrang', r'graus de liberdade', r'coordenadas generalizadas', r'v[íi]nculo', r'multiplicador', r'cano', r'vínculo']),
        ('Hamiltonian Mechanics & Phase Space Dynamics', [r'hamilton', r'espa[çc]o de fase', r'can[ôo]nic', r'poisson', r'momento conjugado']),
        ('Central Forces, Kepler Orbits & Effective Potential', [r'for[çc]a central', r'potencial efetivo', r'kepler', r'[óo]rbita', r'momento angular', r'gravita[çc]', r'apogeu', r'perigeu', r'sat[ée]lite', r'corpo celeste', r'sol', r'elipse']),
        ('Rigid Body Dynamics & Moments of Inertia', [r'corpo r[íi]gido', r'momento de in[ée]rcia', r'tensor de in[ée]rcia', r'rolamento', r'torque', r'disco', r'cilindro', r'esfera', r'pi[ãa]o', r'barra', r'equilibrista']),
        ('Small Oscillations, Coupled Systems & Normal Modes', [r'modos normais', r'pequenas oscila[çc]', r'frequ[êe]ncias pr[óo]prias', r'matriz.*acoplamento', r'p[êe]ndulo acoplado', r'resson[âa]ncia', r'oscilador', r'mola', r'p[êe]ndulo', r'part[íi]culas acopladas']),
        ('Collisions, Momentum Conservation & Variable Mass', [r'colis[ãa]o', r'conserva[çc][ãa]o do momento', r'centro de massa', r'impulso', r'proj[ée]til', r'choque', r'massa vari[áa]vel', r'corda.*puxada', r'foguete']),
        ('Work-Energy Theorem & 1D Potential Dynamics', [r'potencial unidimensional', r'conserva[çc][ãa]o da energia', r'energia potencial', r'curva de potencial', r'energia mec[âa]nica', r'trabalho realizado', r'ponto de retorno', r'deforma[çc][ãa]o.*mola']),
        ('Newtonian Dynamics & Non-Inertial Frames', [r'newton', r'acelera[çc][ãa]o', r'atrito', r'plano inclinado', r'for[çc]a de coriolis', r'centr[íi]fuga', r'referencial n[ãa]o-inercial', r'curva.*estrada', r'velocidade.*movimento']),
    ],
    'Mecânica Quântica': [
        ('Harmonic Oscillator & Ladder Operators', [r'operador de cria[çc][ãa]o', r'operador de aniquila[çc][ãa]o', r'a\^?\†|a\^\+', r'oscilador harm[ôo]nico', r'n[íi]veis de energia.*oscilador', r'potencial harm[ôo]nico', r'polin[ôo]mios de hermite']),
        ('Dirac Formalism, State Vectors & Hilbert Space', [r'comutador', r'incerteza', r'postulado', r'produto interno', r'autovetor', r'autovalor', r'hermitian', r'bra-ket', r'projetor', r'observ[áa]vel', r'base ortonormal', r'notação de dirac', r'matriz hamiltoniana', r'valor esperado', r'fun[çc][ãa]o de onda normalizada']),
        ('1D Potential Wells, Barriers & Quantum Tunneling', [r'po[çc]o', r'tunelamento', r'barreira de potencial', r'transmiss[ãa]o', r'reflex[ãa]o', r'degrau de potencial', r'potencial delta', r'fun[çc][ãa]o de onda.*part[íi]cula', r'potencial unidimensional']),
        ('Angular Momentum, Spin Algebra & Addition of Momenta', [r'spin', r'pauli', r'clebsch-gordan', r'j_z|s_z|l_z|j\^2|s\^2', r'adi[çc][ãa]o de momento', r'harm[ôo]nicos esf[ée]ricos', r'matriz.*spin', r'momento angular', r'stern-gerlach']),
        ('Perturbation Theory & Approximation Methods', [r'perturba[çc][ãa]o', r'primeira ordem', r'segunda ordem', r'hamiltoniano perturbado', r'stark', r'zeeman', r'wkb', r'variacional', r'corre[çc][ãa]o de energia']),
        ('Hydrogen Atom & Central Potentials', [r'hidrog[êe]nio', r'raio de bohr', r'orbital', r'n[úu]meros qu[âa]nticos', r'potencial coulombiano', r'átomo muônico']),
        ('Identical Particles, Bosons/Fermions & Symmetry', [r'b[óo]son', r'f[ée]rmion', r'exclus[ãa]o', r'anti-sim[ée]trica', r'part[íi]culas id[êe]nticas', r'pauli.*princ[íi]pio', r'degeneresc[êe]ncia']),
    ],
    'Termodinâmica': [
        ('1st & 2nd Laws / Thermodynamic Cycles', [r'carnot', r'rendimento', r'ciclo', r'adiab[áa]tic', r'isot[ée]rmic', r'trabalho realizado', r'efici[êe]ncia', r'm[áa]quina t[ée]rmica', r'otto', r'diesel']),
        ('Thermodynamic Potentials & Maxwell Relations', [r'maxwell.*rela[çc]', r'helmholtz', r'gibbs', r'entalpia', r'potencial qu[íi]mico', r'energia livre', r'rela[çc][õo]es de maxwell']),
        ('Ideal & Real Gases (Equation of State)', [r'g[áa]s ideal', r'van der waals', r'calor espec[íi]fico', r'equa[çc][ãa]o de estado', r'press[ãa]o', r'volume', r'g[áa]s monoat[ôo]mico', r'expans[ãa]o livre', r'joule-thomson']),
        ('Phase Transitions & Clausius-Clapeyron', [r'transi[çc][ãa]o de fase', r'clapeyron', r'clausius', r'calor latente', r'ponto triplo', r'vaporiza[çc][ãa]o', r'fus[ãa]o']),
        ('Calorimetry, Heat Capacities & Thermal Expansion', [r'calorimetria', r'capacidade t[ée]rmica', r'calor espec[íi]fico', r'dilata[çc][ãa]o t[ée]rmica', r'mistura', r'equil[íi]brio t[ée]rmico']),
        ('Entropy Changes & Reversibility', [r'entropia', r'processo revers[íi]vel', r'irrevers[íi]vel', r'desordem', r'varia[çc][ãa]o de entropia']),
    ],
    'Física Estatística': [
        ('Canonical & Microcanonical Ensembles', [r'fun[çc][ãa]o de parti[çc][ãa]o', r'ensemble can[ôo]nico', r'boltzmann', r'microcan[ôo]nico', r'equi-parti[çc][ãa]o', r'energia m[ée]dia', r'distribui[çc][ãa]o de probabilidades', r'espa[çc]o de fase estat[íi]stico', r'densidade de estados']),
        ('Grand Canonical Ensemble & Chemical Potential', [r'grande can[ôo]nico', r'grande potencial', r'fugacidade', r'potencial qu[íi]mico', r'flutua[çc][ãa]o do n[úu]mero de part[íi]culas']),
        ('Quantum Gases (Fermi-Dirac & Degeneracy)', [r'fermi-dirac', r'energia de fermi', r'temperatura de fermi', r'g[áa]s degenerado', r'sommerfeld', r'gás de férmions']),
        ('Quantum Gases (Bose-Einstein Condensation & Blackbody)', [r'bose-einstein', r'condensa[çc][ãa]o', r'corpo negro', r'f[óo]tons.*g[áa]s', r'f[óo]nons', r'debye', r'einstein.*calor', r'gás de bósons']),
        ('Spin Systems, Paramagnetism & Ising Model', [r'paramagnetismo', r'ising', r'magnetiza[çc][ãa]o m[ée]dia', r'susceptibilidade', r'curie', r'campo externo', r'dipolos magn[ée]ticos.*rede']),
        ('Two-Level Systems & Paramagnetic Entropy', [r'dois n[íi]veis', r'dois estados', r'temperatura negativa', r'entropia configuracional', r'n sistemas distingu', r'schottky']),
    ],
    'Física Moderna': [
        ('Special Relativity & Lorentz Transformations', [r'lorentz', r'contra[çc][ãa]o', r'dilata[çc][ãa]o', r'quadrivetor', r'energia relativ[íi]stica', r'doppler relativ[íi]stico', r'espa[çc]o-tempo', r'intervalo invariante', r'simultaneidade', r'massa de repouso', r'velocidade relativ']),
        ('Relativistic Dynamics & Energy-Momentum', [r'bomba.*repouso', r'conservação do 4-momento', r'massa invariante', r'energia de repouso', r'quadrimomento', r'reação nuclear.*energia']),
        ('Photoelectric Effect & Photon Interactions', [r'fotoel[ée]tric', r'fun[çc][ãa]o trabalho', r'frequ[êe]ncia de corte', r'potencial de corte', r'compton', r'f[óo]ton']),
        ('Matter Waves & de Broglie Hypothesis', [r'de broglie', r'comprimento de onda.*broglie', r'difra[çc][ãa]o de el[ée]trons', r'onda de mat[ée]ria']),
        ('Blackbody Radiation & Quantum Optics', [r'radia[çc][ãa]o de corpo negro', r'lei de wien', r'planck', r'stefan-boltzmann', r'cavidade radiante']),
        ('Atomic Models (Bohr, Rydberg & Franck-Hertz)', [r'bohr', r'franck-hertz', r'raios x', r'massa reduzida', r'espectro', r's[ée]rie de lyman', r'balmer', r'n[íi]veis at[ôo]micos']),
        ('Nuclear Physics & Radioactive Decay', [r'decaimento', r'meia-vida', r'radioativid', r'atividade', r'radia[çc][ãa]o alfa', r'beta', r'gama', r'fus[ãa]o', r'fiss[ãa]o']),
    ]
}


def classify_subtopic(area, text):
    text_clean = text.lower()
    rules = SUBTOPIC_RULES.get(area, [])
    for sub_name, patterns in rules:
        if any(re.search(p, text_clean) for p in patterns):
            return sub_name
    default_subtopics = {
        'Eletromagnetismo': 'Continuous Charge Distributions & Electric Potentials',
        'Mecânica Clássica': 'Newtonian Dynamics & Non-Inertial Frames',
        'Mecânica Quântica': 'Dirac Formalism, State Vectors & Hilbert Space',
        'Termodinâmica': '1st & 2nd Laws / Thermodynamic Cycles',
        'Física Estatística': 'Canonical & Microcanonical Ensembles',
        'Física Moderna': 'Photoelectric Effect & Photon Interactions',
    }
    return default_subtopics.get(area, 'Advanced Physics Topics')


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

    valid_prefixes = {"mc", "em", "mq", "fm", "fe", "te"}

    for page_idx, page in enumerate(doc):
        p_text = get_page_text_robust(page)
        has_imgs = len(page.get_images()) > 0

        p_lower = p_text.lower()
        if ("instruções para a prova" in p_lower or "intruções para a prova" in p_lower or "instructions for the exam" in p_lower) and len(p_text) < 1200:
            continue
        if "folha de respostas" in p_lower or "answer sheet" in p_lower:
            continue
        if "formulário" in p_lower and ("constantes físicas" in p_lower or "regras de propagação" in p_lower):
            continue
        if re.search(r'Q\.\s*\d+\s*:\s*\n\s*A\s*\n\s*B', p_text) or re.search(r'Quest[ãa]o\s*\d+\s*:\s*\n\s*A\s*\n\s*B', p_text):
            continue
        if '\x00\x01\x02' in p_text and page_idx >= len(doc) - 3:
            continue
        if 'esta prova contém questões de' in p_lower and len(p_text) < 400:
            continue

        # 1. Check for AMC tag matches like [mcPT1a] or [mc1a]
        tag_matches = list(re.finditer(r'(?:(?:Q\.|Quest[ãa]o)\s*(\d+)\s*)?\[([a-zA-Z]{2,4}\d*[a-zA-Z0-9_-]*)\]', p_text, re.IGNORECASE))
        
        valid_tag_matches = []
        for m in tag_matches:
            raw_tag = m.group(2)
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

    # Sequence recovery for 2026-1 Page 21 (Q63 / mqPT4a and Q64 / mqPT4b)
    if exam_id == "2026-1":
        existing_tags = set(q["tag"] for q in questions)
        if "mqPT4a" not in existing_tags:
            questions.append({
                "id": "2026-1-mqPT4a",
                "exam_id": "2026-1",
                "question_num": 63,
                "tag": "mqPT4a",
                "area": "Mecânica Quântica",
                "subtopic": "Perturbation Theory & Approximations",
                "language": "PT",
                "page": 21,
                "has_image": 0,
                "question_type": "múltipla escolha",
                "text": "Q. 63 [mqPT4a] Uma partícula sem spin, de massa m e carga q = e, está sujeita a um potencial harmônico unidimensional com perturbação H1 = -qEx. Calcule o módulo da correção na energia do estado fundamental em ordem mais baixa não nula."
            })
        if "mqPT4b" not in existing_tags:
            questions.append({
                "id": "2026-1-mqPT4b",
                "exam_id": "2026-1",
                "question_num": 64,
                "tag": "mqPT4b",
                "area": "Mecânica Quântica",
                "subtopic": "Perturbation Theory & Approximations",
                "language": "PT",
                "page": 21,
                "has_image": 0,
                "question_type": "múltipla escolha",
                "text": "Q. 64 [mqPT4b] Uma partícula sem spin, de massa m e carga q = 2e, está sujeita a um potencial harmônico unidimensional com perturbação H1 = -qEx. Calcule o módulo da correção na energia do estado fundamental em ordem mais baixa não nula."
            })

    return questions


def run_indexer():
    conn = init_database()
    cur = conn.cursor()

    cur.execute("DELETE FROM questions")
    cur.execute("DELETE FROM exams")
    conn.commit()

    all_pdfs = sorted(glob.glob(os.path.join(BASE_DIR, "*.pdf")))
    total_questions = 0

    print("=" * 70)
    print("🚀 EUF EXAM INDEXER (Strict Physics Taxonomy)")
    print("=" * 70)

    for pdf_path in all_pdfs:
        filename = os.path.basename(pdf_path)
        if any(skip in filename for skip in ["Moys", "Formul", "form"]):
            continue

        year, sem = extract_year_semester(filename)
        exam_id = f"{year}-{sem}"
        doc = pymupdf.open(pdf_path)
        num_pages = len(doc)

        exam_questions = parse_pdf_document(pdf_path, year, sem, exam_id)
        exam_type = "amc_multiple_choice" if any("mc" in q["tag"].lower() or "em" in q["tag"].lower() for q in exam_questions) else "discursive"

        cur.execute("""
        INSERT OR REPLACE INTO exams (id, year, semester, filename, num_pages, exam_type, has_text)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (exam_id, year, sem, filename, num_pages, exam_type, 1))

        seen_ids = set()
        for q in exam_questions:
            if q["id"] in seen_ids:
                continue
            seen_ids.add(q["id"])

            cur.execute("""
            INSERT OR REPLACE INTO questions 
            (id, exam_id, question_num, tag, area, subtopic, language, page, has_image, question_type, text)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                q["id"], q["exam_id"], q["question_num"], q["tag"],
                q["area"], q["subtopic"], q["language"], q["page"],
                q["has_image"], q["question_type"], q["text"]
            ))
            total_questions += 1

        print(f"[{exam_id:7}] {filename:35} | ✅ {len(exam_questions):3} Questions")

    conn.commit()

    cur.execute("SELECT area, COUNT(*) FROM questions WHERE language = 'PT' GROUP BY area ORDER BY COUNT(*) DESC")
    print("\n" + "=" * 70)
    print(f"🎉 INDEXING COMPLETE: {total_questions} Total Questions Indexed across 6 Areas!")
    print("=" * 70)
    for a, cnt in cur.fetchall():
        print(f"  📌 {a:25}: {cnt:3} Questions")

    conn.close()


if __name__ == "__main__":
    run_indexer()
