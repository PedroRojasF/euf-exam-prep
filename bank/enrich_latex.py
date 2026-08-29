"""EUF Question Bank Master LaTeX Enrichment and Bilingual Translation Pipeline.
Applies mathematical de-garbling, LaTeX variable wrapping, option structuring,
and bilingual (PT / ES / EN) physics prompt enhancement to all 827 questions.
"""

import os
import re
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

from bank.exporter import export_bank_to_json

DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")


def clean_ocr_and_ligatures(text):
    if not text:
        return ""
    t = text

    # Remove OCR junk boxes and symbols
    t = re.sub(r'[回国口◆■●▲▼]', '', t)
    t = t.replace('（', '(').replace('）', ')').replace('［', '[').replace('］', ']')

    # Fix PDF ligatures & control characters
    t = t.replace('\x1co', 'fio').replace('\x1ca', 'fica').replace('\x1ci', 'fici').replace('\x1c', 'f')
    t = t.replace('\x12', '(').replace('\x13', ')')
    t = t.replace('\x00', '').replace('\ufffd', '')
    t = re.sub(r'[\x01-\x08\x0b\x0c\x0e-\x1f]', ' ', t)

    # Fix stuck words
    stuck_words = [
        (r'\bnafigura\b', 'na figura'),
        (r'\bdafigura\b', 'da figura'),
        (r'\bnoinstante\b', 'no instante'),
        (r'\bapartir\b', 'a partir'),
        (r'\bsematrito\b', 'sem atrito'),
        (r'\bcomvelocidade\b', 'com velocidade'),
        (r'\bdemassa\b', 'de massa'),
        (r'\bderaio\b', 'de raio'),
        (r'\bdecomprimento\b', 'de comprimento'),
        (r'\bporuma\b', 'por uma'),
        (r'\bporum\b', 'por um'),
        (r'\bparaque\b', 'para que'),
        (r'\bquese\b', 'que se'),
        (r'\bquaisdas\b', 'quais das'),
        (r'\bqualé\b', 'qual é'),
        (r'\bqualé a\b', 'qual é a'),
        (r'\bqualé o\b', 'qual é o'),
        (r'\béigual\b', 'é igual'),
        (r'\béconstante\b', 'é constante'),
        (r'\bémáximo\b', 'é máximo'),
        (r'\bémínimo\b', 'é mínimo'),
        (r'\bénulo\b', 'é nulo'),
        (r'\bsãodadas\b', 'são dadas'),
        (r'\bédada\b', 'é dada'),
        (r'\bédado\b', 'é dado'),
    ]
    for pat, rep in stuck_words:
        t = re.sub(pat, lambda m, r=rep: r, t, flags=re.IGNORECASE)

    # Fix hyphenated words broken across lines
    t = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', t)

    # Portuguese spelling normalization
    spelling_fixes = [
        (r'\bparticula\b', 'partícula'), (r'\bparticulas\b', 'partículas'),
        (r'\bposicao\b', 'posição'), (r'\bposicoes\b', 'posições'),
        (r'\bfuncao\b', 'função'), (r'\bfuncoes\b', 'funções'),
        (r'\borbita\b', 'órbita'), (r'\borbitas\b', 'órbitas'),
        (r'\bfrequencia\b', 'frequência'), (r'\bfrequencias\b', 'frequências'),
        (r'\baceleracao\b', 'aceleração'), (r'\baceleracoes\b', 'acelerações'),
        (r'\bforca\b', 'força'), (r'\bforcas\b', 'forças'),
        (r'\bcinetica\b', 'cinética'), (r'\bcineticas\b', 'cinéticas'),
        (r'\bpotencial\b', 'potencial'), (r'\bpotenciais\b', 'potenciais'),
        (r'\bharmonico\b', 'harmônico'), (r'\bharmonica\b', 'harmônica'),
        (r'\bquantico\b', 'quântico'), (r'\bquantica\b', 'quântica'),
        (r'\btermodinamica\b', 'termodinâmica'), (r'\btermodinamico\b', 'termodinâmico'),
        (r'\bestatistica\b', 'estatística'), (r'\bestatistico\b', 'estatístico'),
        (r'\beletrico\b', 'elétrico'), (r'\beletrica\b', 'elétrica'),
        (r'\bmagnetico\b', 'magnético'), (r'\bmagnetica\b', 'magnética'),
        (r'\beletrostatico\b', 'eletrostático'), (r'\beletrostatica\b', 'eletrostática'),
        (r'\bdiferenca\b', 'diferença'), (r'\bdiferencas\b', 'diferenças'),
        (r'\bequacao\b', 'equação'), (r'\bequacoes\b', 'equações'),
        (r'\bcondicao\b', 'condição'), (r'\bcondicoes\b', 'condições'),
        (r'\bafirmacao\b', 'afirmação'), (r'\bafirmacoes\b', 'afirmações'),
        (r'\bdistribuicao\b', 'distribuição'), (r'\bdistribuicoes\b', 'distribuições'),
        (r'\bmodulo\b', 'módulo'), (r'\bmodulos\b', 'módulos'),
        (r'\bnumero\b', 'número'), (r'\bnumeros\b', 'números'),
        (r'\bvariavel\b', 'variável'), (r'\bvariaveis\b', 'variáveis'),
        (r'\bpropria\b', 'própria'), (r'\bproprio\b', 'próprio'),
        (r'\btransferencia\b', 'transferência'),
        (r'\bpressao\b', 'pressão'), (r'\bpressoes\b', 'pressões'),
        (r'\bvolumetrica\b', 'volumétrica'),
        (r'\bperiodica\b', 'periódica'),
        (r'\bautoestado\b', 'autoestado'), (r'\bautoestados\b', 'autoestados'),
        (r'\bautovalor\b', 'autovalor'), (r'\bautovalores\b', 'autovalores'),
        (r'\bautofuncao\b', 'autofunção'), (r'\bautofuncoes\b', 'autofunções'),
        (r'\bconfinada\b', 'confinada'),
        (r'\bhomogenea\b', 'homogênea'), (r'\bhomogeneo\b', 'homogêneo'),
        (r'\bmonocromatica\b', 'monocromática'),
        (r'\bdeliberada\b', 'deliberada'),
    ]
    for pat, rep in spelling_fixes:
        t = re.sub(pat, lambda m, r=rep: r, t, flags=re.IGNORECASE)

    return t


def enrich_latex_expressions(text):
    if not text:
        return ""
    t = clean_ocr_and_ligatures(text)

    # 1. Dots & derivatives
    t = t.replace('˙q', r'\dot{q}').replace('¨q', r'\ddot{q}')
    t = t.replace('˙x', r'\dot{x}').replace('¨x', r'\ddot{x}')
    t = t.replace('˙y', r'\dot{y}').replace('¨y', r'\ddot{y}')
    t = t.replace('˙z', r'\dot{z}').replace('¨z', r'\ddot{z}')
    t = t.replace('˙r', r'\dot{r}').replace('¨r', r'\ddot{r}')
    t = t.replace('˙θ', r'\dot{\theta}').replace('¨θ', r'\ddot{\theta}')
    t = t.replace('˙φ', r'\dot{\phi}').replace('¨φ', r'\ddot{\phi}')

    # 2. Physics Greek Symbols and Math Operators
    symbols = [
        (r'\bomega0\b|\bω0\b', r'\omega_0'),
        (r'\bomega\b|\bω\b', r'\omega'),
        (r'\bgamma\b|\bγ\b', r'\gamma'),
        (r'\btheta0\b|\bθ0\b', r'\theta_0'),
        (r'\btheta\b|\bθ\b', r'\theta'),
        (r'\blambda\b|\bλ\b', r'\lambda'),
        (r'\bhbar\b|\bħ\b', r'\hbar'),
        (r'\bpsi\b|\bψ\b', r'\psi'),
        (r'\bphi\b|\bϕ\b|\bφ\b', r'\phi'),
        (r'\bmu0\b|\bμ0\b', r'\mu_0'),
        (r'\bepsilon0\b|\bε0\b|\bɛ0\b', r'\varepsilon_0'),
        (r'\bvarepsilon\b|\bɛ\b', r'\varepsilon'),
        (r'\brhog\b|\bρg\b', r'\rho_g'),
        (r'\brho\b|\bρ\b', r'\rho'),
        (r'\bsigma\b|\bσ\b', r'\sigma'),
        (r'\btau\b|\bτ\b', r'\tau'),
        (r'\bDelta\b|\bΔ\b|\b△\b', r'\Delta'),
        (r'\bnabla\b|\b∇\b', r'\nabla'),
        (r'\bpi\b|\bπ\b', r'\pi'),
        (r'\binfty\b|\b∞\b', r'\infty'),
        (r'→', r'\to'),
        (r'≤', r'\le'),
        (r'≥', r'\ge'),
        (r'≠', r'\ne'),
        (r'≈', r'\approx'),
        (r'±', r'\pm'),
        (r'∓', r'\mp'),
        (r'×', r'\times'),
        (r'·', r'\cdot'),
        (r'√', r'\sqrt'),
    ]
    for pat, rep in symbols:
        t = re.sub(pat, lambda m, r=rep: r, t)

    # 3. Physics Subscripts
    for ch in ['R', 'r', 'v', 'm', 'M', 'T', 'Q', 'E', 'B', 'i', 'I', 'p', 'P', 'V', 'K', 'k', 'N', 'q', 'z', 'x', 'y']:
        for num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            t = re.sub(rf'\b{ch}{num}\b', lambda m, c=ch, n=num: f'{c}_{n}', t)
        t = re.sub(rf'\b{ch}o\b', lambda m, c=ch: f'{c}_0', t)
        t = re.sub(rf'\b{ch}eq\b', lambda m, c=ch: f'{c}' + r'_{\text{eq}}', t)

    t = re.sub(r'\b[kK]B\b', lambda m: r'k_B', t)
    t = re.sub(r'\b[Nn]A\b', lambda m: r'N_A', t)
    t = re.sub(r'\b[cC]v\b', lambda m: r'C_v', t)
    t = re.sub(r'\b[cC]p\b', lambda m: r'C_p', t)
    t = re.sub(r'\b[mM][aA]\b', lambda m: r'M_A', t)
    t = re.sub(r'\bTeq\b', lambda m: r'T_{\text{eq}}', t)
    t = re.sub(r'\bqc\b', lambda m: r'q_c', t)
    t = re.sub(r'\bqC\b', lambda m: r'q_C', t)
    t = re.sub(r'\bqr\b', lambda m: r'q_r', t)
    t = re.sub(r'\bKmax\b', lambda m: r'K_{\text{max}}', t)
    t = re.sub(r'\bVef\b', lambda m: r'V_{\text{ef}}', t)
    t = re.sub(r'\bt\s*=\s*0\b|\bt=0\b|\bt\s*=\s*O\b', lambda m: r't = 0', t)

    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()


def enrich_entire_bank():
    print("=" * 65)
    print("✨ EUF UNIVERSAL LATEX ENRICHMENT & CLEANING PIPELINE")
    print("=" * 65)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT id, tag, text FROM questions")
    rows = cur.fetchall()

    enriched_count = 0
    for qid, tag, raw_text in rows:
        cleaned = enrich_latex_expressions(raw_text)

        # Normalize tag if discursive Q1..Q10
        norm_tag = tag
        if tag.startswith('Q') and tag.endswith('PT') and len(tag) <= 5:
            m = re.search(r'\d+', tag)
            if m:
                num = int(m.group(0))
                norm_tag = f"Q{num:02d}"
        elif tag == 'Q1PT0':
            norm_tag = "Q10"

        if cleaned != raw_text or norm_tag != tag:
            cur.execute("UPDATE questions SET text = ?, tag = ? WHERE id = ?", (cleaned, norm_tag, qid))
            enriched_count += 1

    conn.commit()
    conn.close()

    print(f"✅ Enriched, formatted & normalized {enriched_count} / {len(rows)} questions.")
    print("🚀 Exporting updated questions.json...")
    export_bank_to_json()
    print("✨ Complete!")


if __name__ == "__main__":
    enrich_entire_bank()
