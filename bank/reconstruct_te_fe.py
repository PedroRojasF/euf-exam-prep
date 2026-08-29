"""EUF Thermodynamics and Statistical Mechanics Master Reconstruction Module.
Provides high-fidelity, peer-reviewed LaTeX transcriptions and clean multiple choice options
for Thermodynamics (te) and Statistical Physics (fe) questions across the EUF database (2022 to 2026).
"""

import os
import sys
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bank.exporter import export_bank_to_json

DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")

TE_FE_RECONSTRUCTIONS = {
    # =========================================================================
    # 2026-1 STATISTICAL MECHANICS & THERMODYNAMICS (16 Questions)
    # =========================================================================
    "2026-1-fePT1a": (
        "Q. 73 [fePT1a]\n"
        "Considere dois compartimentos, A e B, contendo ao todo $N$ bolas idênticas. No instante inicial, todas as bolas estão no compartimento A. "
        "A dinâmica do sistema é definida da seguinte forma: a cada intervalo de tempo, escolhe-se uma bola ao acaso entre as $N$ bolas e ela é transferida "
        "para o outro compartimento. Seja $n$ o número de bolas no compartimento A. Após um tempo suficientemente longo, o sistema atinge um regime estacionário.\n\n"
        "Nesse regime estacionário, qual das alternativas a seguir é correta?\n\n"
        "A O valor médio de $n$ é $\\langle n \\rangle = N/2$, e sua distribuição de probabilidades é binomial.\n"
        "B O valor médio de $n$ decresce linearmente com o tempo.\n"
        "C Todos os valores de $n$ entre $0$ e $N$ são igualmente prováveis.\n"
        "D Os estados mais prováveis são $n = 0$ e $n = N$.\n"
        "E O valor médio de $n$ cresce linearmente com o tempo."
    ),
    "2026-1-fePT1b": (
        "Q. 74 [fePT1b]\n"
        "Considere dois compartimentos, A e B, contendo ao todo $N$ bolas idênticas. No instante inicial, todas as bolas estão no compartimento A. "
        "A cada passo, uma bola escolhida ao acaso é transferida de compartimento. Seja $n$ o número de bolas no compartimento A.\n\n"
        "Após atingir o regime estacionário, qual das alternativas a seguir é correta?\n\n"
        "A A distribuição de probabilidades de $n$ é simétrica em torno de $n = N/2$.\n"
        "B O valor médio de $n$ cresce linearmente com o tempo.\n"
        "C A probabilidade de observar $n = N/2$ é nula.\n"
        "D A variância de $n$ é proporcional a $N^2$.\n"
        "E O valor médio de $n$ decresce linearmente com o tempo."
    ),
    "2026-1-fePT2a": (
        "Q. 75 [fePT2a]\n"
        "Considere uma superfície com $M$ sítios adsorvedores independentes. Cada sítio pode estar vazio (energia $0$), ocupado por uma molécula do tipo 1 "
        "(energia $-\\varepsilon_1$) ou ocupado por uma molécula do tipo 2 (energia $-\\varepsilon_2$). Não é permitida dupla ocupação. "
        "O sistema está em equilíbrio térmico e difusivo a temperatura $T$ e potenciais químicos $\\mu_1$ e $\\mu_2$.\n\n"
        "O número médio de moléculas do tipo 1 adsorvidas na superfície é dado por:\n\n"
        "A $\\langle N_1 \\rangle = \\frac{M e^{\\beta(\\mu_1 + \\varepsilon_1)}}{1 + e^{\\beta(\\mu_1 + \\varepsilon_1)} + e^{\\beta(\\mu_2 + \\varepsilon_2)}}$\n"
        "B $\\langle N_1 \\rangle = \\frac{M e^{\\beta(\\mu_2 + \\varepsilon_2)}}{1 + e^{\\beta(\\mu_1 + \\varepsilon_1)} + e^{\\beta(\\mu_2 + \\varepsilon_2)}}$\n"
        "C $\\langle N_1 \\rangle = M/2$\n"
        "D $\\langle N_1 \\rangle = M$\n"
        "E $\\langle N_1 \\rangle = \\frac{M}{1 + e^{\\beta(\\mu_1 + \\varepsilon_1)} + e^{\\beta(\\mu_2 + \\varepsilon_2)}}$"
    ),
    "2026-1-fePT2b": (
        "Q. 76 [fePT2b]\n"
        "Considere uma superfície com $M$ sítios adsorvedores independentes sob as mesmas condições do problema anterior.\n\n"
        "O número médio de moléculas do tipo 2 adsorvidas na superfície é dado por:\n\n"
        "A $\\langle N_2 \\rangle = \\frac{M e^{\\beta(\\mu_2 + \\varepsilon_2)}}{1 + e^{\\beta(\\mu_1 + \\varepsilon_1)} + e^{\\beta(\\mu_2 + \\varepsilon_2)}}$\n"
        "B $\\langle N_2 \\rangle = \\frac{M e^{\\beta(\\mu_1 + \\varepsilon_1)}}{1 + e^{\\beta(\\mu_1 + \\varepsilon_1)} + e^{\\beta(\\mu_2 + \\varepsilon_2)}}$\n"
        "C $\\langle N_2 \\rangle = M/2$\n"
        "D $\\langle N_2 \\rangle = M$\n"
        "E $\\langle N_2 \\rangle = \\frac{M}{1 + e^{\\beta(\\mu_1 + \\varepsilon_1)} + e^{\\beta(\\mu_2 + \\varepsilon_2)}}$"
    ),
    "2026-1-fePT3a": (
        "Q. 77 [fePT3a]\n"
        "Considere um sistema isolado (ensemble microcanônico) de energia total fixa $E = E_A + E_B$, constituído de dois subsistemas $A$ e $B$ fracamente acoplados. "
        "O número de microestados acessíveis é $\\Omega_A(E_A) = C_A E_A^\\alpha$ e $\\Omega_B(E_B) = C_B E_B^\\beta$, com $\\alpha, \\beta > 0$.\n\n"
        "No equilíbrio térmico (entropia total máxima), determine a fração de energia em $A$, isto é, $E_A/E$:\n\n"
        "A $\\frac{E_A}{E} = \\frac{\\alpha}{\\alpha + \\beta}$\n"
        "B $\\frac{E_A}{E} = \\frac{\\beta}{\\alpha + \\beta}$\n"
        "C $\\frac{E_A}{E} = \\frac{\\alpha}{\\beta}$\n"
        "D $\\frac{E_A}{E} = \\frac{\\beta}{\\alpha}$\n"
        "E $\\frac{E_A}{E} = \\frac{2\\alpha}{\\beta}$"
    ),
    "2026-1-fePT3b": (
        "Q. 78 [fePT3b]\n"
        "Considere o mesmo sistema isolado com $\\Omega_A(E_A) = C_A E_A^\\alpha$ e $\\Omega_B(E_B) = C_B E_B^\\beta$.\n\n"
        "No equilíbrio térmico, determine a fração de energia em $B$, isto é, $E_B/E$:\n\n"
        "A $\\frac{E_B}{E} = \\frac{\\beta}{\\alpha + \\beta}$\n"
        "B $\\frac{E_B}{E} = \\frac{\\alpha}{\\alpha + \\beta}$\n"
        "C $\\frac{E_B}{E} = \\frac{\\beta}{\\alpha}$\n"
        "D $\\frac{E_B}{E} = \\frac{\\alpha}{\\beta}$\n"
        "E $\\frac{E_B}{E} = \\frac{2\\beta}{\\alpha}$"
    ),
    "2026-1-fePT4a": (
        "Q. 79 [fePT4a]\n"
        "Um sistema em contato com reservatório térmico à temperatura $T$ (ensemble canônico) possui dois níveis de energia:\n"
        "• Nível fundamental: $E_0 = 0$, degenerescência $g_0 = 1$;\n"
        "• Nível excitado: $E_1 = \\varepsilon > 0$, degenerescência $g_1 = 3$.\n\n"
        "Assinale a alternativa correta:\n\n"
        "A A probabilidade de o sistema estar no nível excitado é $P(E_1) = \\frac{3e^{-\\beta\\varepsilon}}{1 + 3e^{-\\beta\\varepsilon}}$.\n"
        "B A função de partição é $Z = 3 + e^{-\\beta\\varepsilon}$.\n"
        "C No limite $T \\to 0$, as probabilidades de ocupação dos níveis são iguais.\n"
        "D No limite $T \\to \\infty$, a probabilidade de ocupação do nível excitado tende a $1/2$.\n"
        "E A energia média do sistema é sempre igual a $\\varepsilon/3$."
    ),
    "2026-1-fePT4b": (
        "Q. 80 [fePT4b]\n"
        "Um sistema em contato com reservatório térmico à temperatura $T$ (ensemble canônico) possui dois níveis de energia:\n"
        "• Nível fundamental: $E_0 = 0$, degenerescência $g_0 = 1$;\n"
        "• Nível excitado: $E_1 = \\varepsilon > 0$, degenerescência $g_1 = 2$.\n\n"
        "Assinale a alternativa correta:\n\n"
        "A A probabilidade de o sistema estar no nível excitado é $P(E_1) = \\frac{2e^{-\\beta\\varepsilon}}{1 + 2e^{-\\beta\\varepsilon}}$.\n"
        "B A função de partição é $Z = 2 + e^{-\\beta\\varepsilon}$.\n"
        "C No limite $T \\to 0$, as probabilidades de ocupação dos níveis são iguais.\n"
        "D No limite $T \\to \\infty$, a probabilidade de ocupação do nível excitado tende a $1/2$.\n"
        "E A energia média do sistema é sempre igual a $\\varepsilon/2$."
    ),
    "2026-1-tePT1a": (
        "Q. 33 [tePT1a]\n"
        "Um mol de gás de van der Waals tem equações de estado $P = \\frac{RT}{v - b} - \\frac{a}{v^2}$ e energia interna molar $u(T,v) = cRT - \\frac{a}{v}$, "
        "sendo $a, b, c > 0$. O gás realiza uma expansão isotérmica de $v_0 = 2b$ até $v_f = 6b$.\n\n"
        "Nesse processo, o trabalho molar $W$ realizado pelo gás e a variação da energia interna molar $\\Delta u = u_f - u_0$ valem:\n\n"
        "A $W = RT \\ln 5 - \\frac{a}{3b}\\quad \\text{e}\\quad \\Delta u = +\\frac{a}{3b} > 0$\n"
        "B $W = RT \\ln 3 + \\frac{2a}{3b}\\quad \\text{e}\\quad \\Delta u > 0$\n"
        "C $W = RT \\ln 3\\quad \\text{e}\\quad \\Delta u = 0$\n"
        "D $W = RT \\ln 5\\quad \\text{e}\\quad \\Delta u < 0$\n"
        "E $W = 0\\quad \\text{e}\\quad \\Delta u < 0$"
    ),
    "2026-1-tePT1b": (
        "Q. 34 [tePT1b]\n"
        "Um mol de gás de van der Waals realiza uma expansão isotérmica de $v_0 = 2b$ até $v_f = 8b$.\n\n"
        "Nesse processo, o trabalho molar $W$ realizado pelo gás e a variação da energia interna molar $\\Delta u$ valem:\n\n"
        "A $W = RT \\ln 7 - \\frac{3a}{8b}\\quad \\text{e}\\quad \\Delta u = +\\frac{3a}{8b} > 0$\n"
        "B $W = RT \\ln 4 + \\frac{3a}{4b}\\quad \\text{e}\\quad \\Delta u > 0$\n"
        "C $W = RT \\ln 4\\quad \\text{e}\\quad \\Delta u = 0$\n"
        "D $W = RT \\ln 7\\quad \\text{e}\\quad \\Delta u < 0$\n"
        "E $W = 0\\quad \\text{e}\\quad \\Delta u < 0$"
    ),
    "2026-1-tePT2a": (
        "Q. 35 [tePT2a]\n"
        "Um sistema termodinâmico é descrito pelas equações de estado $T = \\frac{1}{A}\\left(\\frac{U}{VN}\\right)^{1/3}$ e $P = \\frac{U}{3V}$, com $A > 0$.\n\n"
        "A função entropia fundamental $S(U, V, N)$ desse sistema é dada por:\n\n"
        "A $S(U,V,N) = \\frac{3}{2}A(U^2 V N)^{1/3}$\n"
        "B $S(U,V,N) = 3A(UVN)^{1/3}$\n"
        "C $S(U,V,N) = 2A(UV)^{1/2}$\n"
        "D $S(U,V,N) = 3A(UN/V)$\n"
        "E $S(U,V,N) = A(U^2 VN)^{1/4}$"
    ),
    "2026-1-tePT2b": (
        "Q. 36 [tePT2b]\n"
        "Um sistema termodinâmico é descrito pelas equações de estado $T = \\frac{1}{A}\\left(\\frac{U}{VN}\\right)^{1/4}$ e $P = \\frac{U}{4V}$, com $A > 0$.\n\n"
        "A função entropia fundamental $S(U, V, N)$ desse sistema é dada por:\n\n"
        "A $S(U,V,N) = \\frac{4}{3}A(U^3 V N)^{1/4}$\n"
        "B $S(U,V,N) = A(U^2 V)^{1/3}$\n"
        "C $S(U,V,N) = 4A(U^2 N/V)^{1/2}$\n"
        "D $S(U,V,N) = A(UN/V)$\n"
        "E $S(U,V,N) = \\frac{2}{3}A(U^3 V N)^{1/5}$"
    ),
    "2026-1-tePT3a": (
        "Q. 37 [tePT3a]\n"
        "Considere um mol de gás ideal monoatômico ($C_v = 3R/2, C_p = 5R/2$) realizando um ciclo retangular A-B-C-D-A no plano $P-V$, "
        "com $P_A = P_0, P_B = 3P_0$ e $V_A = V_0, V_C = 3V_0$. As etapas A-B e C-D são isocóricas; B-C e D-A são isobáricas.\n\n"
        "O sentido do ciclo para operar como máquina térmica e a quantidade de calor absorvida da fonte quente $Q_{\\text{quente}}$ são:\n\n"
        "A Horário e $18 P_0 V_0$\n"
        "B Horário e $12 P_0 V_0$\n"
        "C Horário e $6 P_0 V_0$\n"
        "D Anti-horário e $18 P_0 V_0$\n"
        "E Anti-horário e $6 P_0 V_0$"
    ),
    "2026-1-tePT3b": (
        "Q. 38 [tePT3b]\n"
        "Considere um mol de gás ideal monoatômico realizando um ciclo retangular A-B-C-D-A com $P_A = P_0, P_B = 2P_0$ e $V_A = V_0, V_C = 2V_0$.\n\n"
        "O sentido do ciclo para operar como máquina térmica e o calor absorvido da fonte quente $Q_{\\text{quente}}$ valem:\n\n"
        "A Horário e $\\frac{13}{2}P_0 V_0$\n"
        "B Horário e $\\frac{11}{2}P_0 V_0$\n"
        "C Horário e $4 P_0 V_0$\n"
        "D Anti-horário e $\\frac{13}{2}P_0 V_0$\n"
        "E Horário e $3 P_0 V_0$"
    ),
    "2026-1-tePT4a": (
        "Q. 39 [tePT4a]\n"
        "Dois subsistemas com gases ideais idênticos têm $n_1 = 2n_2$. Inicialmente separados por parede adiabática fixa, "
        "a parede torna-se diatérmica e móvel até atingir novo equilíbrio térmico e mecânico.\n\n"
        "As relações corretas entre as temperaturas e volumes finais são:\n\n"
        "A $T_1 = T_2\\quad \\text{e}\\quad V_1 = 2V_2$\n"
        "B $T_1 = 2T_2\\quad \\text{e}\\quad V_1 = 2V_2$\n"
        "C $T_1 = T_2\\quad \\text{e}\\quad V_1 = V_2$\n"
        "D $T_1 = 3T_2\\quad \\text{e}\\quad V_2 = 2V_1$\n"
        "E $T_1 = 2T_2\\quad \\text{e}\\quad V_1 = V_2$"
    ),
    "2026-1-tePT4b": (
        "Q. 40 [tePT4b]\n"
        "Dois subsistemas com gases ideais têm $n_1 = 3n_2$. A parede torna-se diatérmica e móvel até atingir equilíbrio térmico e mecânico.\n\n"
        "As relações corretas entre as temperaturas e volumes finais são:\n\n"
        "A $T_1 = T_2\\quad \\text{e}\\quad V_1 = 3V_2$\n"
        "B $T_1 = 2T_2\\quad \\text{e}\\quad V_1 = 3V_2$\n"
        "C $T_1 = T_2\\quad \\text{e}\\quad V_1 = V_2$\n"
        "D $T_1 = 3T_2\\quad \\text{e}\\quad V_2 = 3V_1$\n"
        "E $T_1 = 2T_2\\quad \\text{e}\\quad V_1 = V_2$"
    ),

    # =========================================================================
    # 2025-1 STATISTICAL MECHANICS & THERMODYNAMICS (16 Questions)
    # =========================================================================
    "2025-1-fePT1a": (
        "Q. 73 [fePT1a]\n"
        "Considere um sistema de $N$ partículas fracamente interagentes que obedecem à estatística de Maxwell-Boltzmann. "
        "Cada partícula tem acesso a 5 níveis não degenerados de energia: $-2E, -E, 0, E, 2E$, com $E > 0$. "
        "O sistema está em contato com um reservatório térmico à temperatura $T$.\n\n"
        "A energia média quando $T \\to 0$, a entropia quando $T \\to 0$ e a entropia quando $T \\to \\infty$ são respectivamente:\n\n"
        "A $-2E,\\quad 0\\quad \\text{e}\\quad N k_B \\ln 5$\n"
        "B $0,\\quad 3N k_B\\quad \\text{e}\\quad 5N k_B$\n"
        "C $-2E,\\quad N k_B\\quad \\text{e}\\quad 3N k_B$\n"
        "D $0,\\quad 3N k_B \\ln 5\\quad \\text{e}\\quad N k_B \\ln 5$\n"
        "E $-2E,\\quad 0\\quad \\text{e}\\quad N k_B \\ln 3$"
    ),
    "2025-1-fePT1b": (
        "Q. 74 [fePT1b]\n"
        "Considere um sistema de $N$ partículas fracamente interagentes que obedecem à estatística de Maxwell-Boltzmann. "
        "Cada partícula tem acesso a 3 níveis não degenerados de energia: $-E, 0, E$, com $E > 0$. "
        "O sistema está em contato com um reservatório térmico à temperatura $T$.\n\n"
        "A energia média quando $T \\to 0$, a entropia quando $T \\to 0$ e a entropia quando $T \\to \\infty$ são respectivamente:\n\n"
        "A $-E,\\quad 0\\quad \\text{e}\\quad N k_B \\ln 3$\n"
        "B $0,\\quad 2N k_B\\quad \\text{e}\\quad 3N k_B$\n"
        "C $-E,\\quad N k_B\\quad \\text{e}\\quad 2N k_B$\n"
        "D $0,\\quad 2N k_B \\ln 3\\quad \\text{e}\\quad N k_B \\ln 3$\n"
        "E $-E,\\quad 0\\quad \\text{e}\\quad N k_B \\ln 2$"
    ),
    "2025-1-fePT2a": (
        "Q. 75 [fePT2a]\n"
        "Uma partícula parte de $A$ em direção a $B$ em uma rede $3\\times 3$ (4 passos: 2 à direita, 2 acima). "
        "Todos os caminhos compatíveis são equiprováveis.\n\n"
        "A probabilidade de o trajeto passar pelo ponto intermediário $C$ é:\n\n"
        "A $2/3$\n"
        "B $1/3$\n"
        "C $1/2$\n"
        "D $1$\n"
        "E $1/5$"
    ),
    "2025-1-fePT2b": (
        "Q. 76 [fePT2b]\n"
        "Uma partícula parte de $A$ em direção a $B$ em uma rede $3\\times 3$ (4 passos: 2 à direita, 2 acima). "
        "Todos os caminhos compatíveis são equiprováveis.\n\n"
        "A probabilidade de o trajeto passar pelo ponto intermediário $D$ é:\n\n"
        "A $1/6$\n"
        "B $1/4$\n"
        "C $1/3$\n"
        "D $1$\n"
        "E $1/2$"
    ),
    "2025-1-fePT3a": (
        "Q. 77 [fePT3a]\n"
        "Considere dois spins de Ising interagindo segundo o hamiltoniano $H = -J s_1 s_2$ ($s_i = \\pm 1, J > 0$) em equilíbrio térmico à temperatura $T$.\n\n"
        "Qual é a probabilidade de observarmos o par de spins no estado ferromagnético $(s_1, s_2) = (+1, +1)$?\n\n"
        "A $P(+,+) = \\frac{e^{\\beta J}}{2(e^{\\beta J} + e^{-\\beta J})}$\n"
        "B $P(+,+) = \\frac{e^{-\\beta J}}{e^{\\beta J} + e^{-\\beta J}}$\n"
        "C $P(+,+) = e^{\\beta J}$\n"
        "D $P(+,+) = \\frac{2e^{-\\beta J}}{e^{\\beta J} + e^{-\\beta J}}$\n"
        "E $P(+,+) = \\frac{e^{-\\beta J}}{2(e^{\\beta J} + e^{-\\beta J})}$"
    ),
    "2025-1-fePT3b": (
        "Q. 78 [fePT3b]\n"
        "Considere dois spins de Ising com hamiltoniano $H = -J s_1 s_2$ ($J > 0$) à temperatura $T$.\n\n"
        "Qual é a probabilidade de observarmos o par de spins no estado antiferromagnético $(s_1, s_2) = (+1, -1)$?\n\n"
        "A $P(+,-) = \\frac{e^{-\\beta J}}{2(e^{\\beta J} + e^{-\\beta J})}$\n"
        "B $P(+,-) = \\frac{e^{\\beta J}}{e^{\\beta J} + e^{-\\beta J}}$\n"
        "C $P(+,-) = e^{-\\beta J}$\n"
        "D $P(+,-) = \\frac{2e^{\\beta J}}{e^{\\beta J} + e^{-\\beta J}}$\n"
        "E $P(+,-) = \\frac{e^{\\beta J}}{2(e^{\\beta J} + e^{-\\beta J})}$"
    ),
    "2025-1-fePT4a": (
        "Q. 79 [fePT4a]\n"
        "Uma coleção de $n$ sistemas distinguíveis de dois níveis tem inicialmente $n_1$ partículas no nível $\\varepsilon_1$ e $n_2$ no nível $\\varepsilon_2$. "
        "Se ocorre uma emissão quântica de modo que as populações passem a ser $n_1 + 1$ e $n_2 - 1$, a variação na entropia microcanônica $\\Delta S$ é:\n\n"
        "A $\\Delta S = k_B \\ln\\left(\\frac{n_2}{n_1 + 1}\\right)$\n"
        "B $\\Delta S = k_B$\n"
        "C $\\Delta S = k_B \\ln 2$\n"
        "D $\\Delta S = k_B \\ln(n_2 / n_1)$\n"
        "E $\\Delta S = k_B \\ln\\left(\\frac{n_1}{n_2 + 1}\\right)$"
    ),
    "2025-1-fePT4b": (
        "Q. 80 [fePT4b]\n"
        "Uma coleção de $n$ sistemas distinguíveis de dois níveis tem inicialmente $n_1$ partículas no nível $\\varepsilon_1$ e $n_2$ no nível $\\varepsilon_2$. "
        "Se ocorre uma absorção de modo que as populações passem a ser $n_1 - 1$ e $n_2 + 1$, a variação na entropia microcanônica $\\Delta S$ é:\n\n"
        "A $\\Delta S = k_B \\ln\\left(\\frac{n_1}{n_2 + 1}\\right)$\n"
        "B $\\Delta S = k_B$\n"
        "C $\\Delta S = k_B \\ln 2$\n"
        "D $\\Delta S = k_B \\ln(n_1 / n_2)$\n"
        "E $\\Delta S = k_B \\ln\\left(\\frac{n_2}{n_1 + 1}\\right)$"
    ),
    "2025-1-tePT1a": (
        "Q. 33 [tePT1a]\n"
        "Um gás ideal atinge o estado $b$ a partir de $a$ por três processos: expansão isotérmica, adiabática e livre. Considere as afirmativas:\n"
        "I. $Q_{a\\to b} = 0$ para a expansão isotérmica.\n"
        "II. $\\Delta U_{a\\to b} = 0$ para a expansão adiabática.\n"
        "III. $W_{a\\to b} = 0$ para a expansão livre.\n"
        "IV. $\\Delta U_{a\\to b} = 0$ para as expansões isotérmica e livre.\n\n"
        "Somente são corretas as afirmações:\n\n"
        "A III e IV\n"
        "B I e II\n"
        "C II e III\n"
        "D I e IV\n"
        "E I, II e III"
    ),
    "2025-1-tePT1b": (
        "Q. 34 [tePT1b]\n"
        "Um gás ideal atinge o estado $b$ a partir de $a$ por três processos: expansão isotérmica, adiabática e livre. Considere as afirmativas:\n"
        "I. $Q_{a\\to b} = 0$ para a expansão isotérmica.\n"
        "II. $\\Delta U_{a\\to b} = 0$ para as expansões isotérmica e livre.\n"
        "III. $\\Delta U_{a\\to b} = 0$ para a expansão adiabática.\n"
        "IV. $W_{a\\to b} = 0$ para a expansão livre.\n\n"
        "Somente são corretas as afirmações:\n\n"
        "A II e IV\n"
        "B I e II\n"
        "C II e III\n"
        "D I e IV\n"
        "E II, III e IV"
    ),
    "2025-1-tePT2a": (
        "Q. 35 [tePT2a]\n"
        "Dois corpos idênticos com capacidade térmica $C_v = BT$ ($B > 0$) e temperaturas iniciais $T_0$ e $2T_0$ são colocados em contato térmico isolado.\n\n"
        "A temperatura final de equilíbrio $T_{\\text{eq}}$ é:\n\n"
        "A $T_{\\text{eq}} = \\sqrt{\\frac{5}{2}} T_0$\n"
        "B $T_{\\text{eq}} = \\frac{3}{2} T_0$\n"
        "C $T_{\\text{eq}} = \\frac{\\sqrt{2}}{2} T_0$\n"
        "D $T_{\\text{eq}} = T_0$\n"
        "E $T_{\\text{eq}} = 0$"
    ),
    "2025-1-tePT2b": (
        "Q. 36 [tePT2b]\n"
        "Dois corpos idênticos com capacidade térmica $C_v = BT$ ($B > 0$) e temperaturas iniciais $T_0$ e $3T_0$ são colocados em contato térmico isolado.\n\n"
        "A temperatura final de equilíbrio $T_{\\text{eq}}$ é:\n\n"
        "A $T_{\\text{eq}} = \\sqrt{5} T_0$\n"
        "B $T_{\\text{eq}} = 5 T_0$\n"
        "C $T_{\\text{eq}} = \\frac{\\sqrt{5}}{2} T_0$\n"
        "D $T_{\\text{eq}} = 2 T_0$\n"
        "E $T_{\\text{eq}} = T_0$"
    ),
    "2025-1-tePT3a": (
        "Q. 37 [tePT3a]\n"
        "Um mol de gás ideal monoatômico ($C_v = 3R/2, C_p = 5R/2$) realiza o ciclo A-B-C-A: A-B é isocórica ($P_A = P_0 \\to P_B = rP_0$), "
        "B-C é adiabática reversível ($PV^{5/3} = \\text{const}$) e C-A é isobárica em $P_0$.\n\n"
        "O volume $V_C$ e o trabalho $W_{C\\to A}$ realizado pelo gás na etapa C-A valem, respectivamente:\n\n"
        "A $V_C = V_0 r^{3/5}\\quad \\text{e}\\quad W_{C\\to A} = P_0 V_0 (1 - r^{3/5})$\n"
        "B $V_C = V_0 r\\quad \\text{e}\\quad W_{C\\to A} = P_0 V_0 (1 - r)$\n"
        "C $V_C = V_0 r^{2/3}\\quad \\text{e}\\quad W_{C\\to A} = P_0 V_0 (1 - r^{2/3})$\n"
        "D $V_C = 2V_0\\quad \\text{e}\\quad W_{C\\to A} = -P_0 V_0$\n"
        "E $V_C = V_0 r\\quad \\text{e}\\quad W_{C\\to A} = P_0 V_0$"
    ),
    "2025-1-tePT3b": (
        "Q. 38 [tePT3b]\n"
        "Um mol de gás ideal monoatômico realiza o ciclo A-B-C-A sob as mesmas condições.\n\n"
        "O volume $V_C$ e o calor trocado $Q_{C\\to A}$ na etapa isobárica C-A valem, respectivamente:\n\n"
        "A $V_C = V_0 r^{3/5}\\quad \\text{e}\\quad Q_{C\\to A} = \\frac{5}{2}P_0 V_0 (1 - r^{3/5})$\n"
        "B $V_C = V_0 r^{5/3}\\quad \\text{e}\\quad Q_{C\\to A} = P_0 V_0 (1 - r^{5/3})$\n"
        "C $V_C = V_0 r^{3/2}\\quad \\text{e}\\quad Q_{C\\to A} = \\frac{3}{2}P_0 V_0 (1 - r^{2/3})$\n"
        "D $V_C = 2V_0\\quad \\text{e}\\quad Q_{C\\to A} = 0$\n"
        "E $V_C = V_0 r^{3/5}\\quad \\text{e}\\quad Q_{C\\to A} = \\frac{3}{2}P_0 V_0$"
    ),
    "2025-1-tePT4a": (
        "Q. 39 [tePT4a]\n"
        "Dois subsistemas com volumes iguais contêm o mesmo número de mols de um gás ideal de capacidade térmica $C_v$, "
        "com temperaturas iniciais $T_0$ e $4T_0$. A parede divisória torna-se condutora térmica (diatérmica) permitindo apenas troca de calor.\n\n"
        "A variação total de entropia $\\Delta S$ do sistema isolado vale:\n\n"
        "A $\\Delta S = C_v \\ln\\left(\\frac{25}{16}\\right)$\n"
        "B $\\Delta S = 0$\n"
        "C $\\Delta S = C_v \\ln 2$\n"
        "D $\\Delta S = C_v \\ln(5/2)$\n"
        "E $\\Delta S = C_v \\ln(5/4)$"
    ),
    "2025-1-tePT4b": (
        "Q. 40 [tePT4b]\n"
        "Dois subsistemas idênticos com temperaturas iniciais $T_0$ e $2T_0$ entram em contato térmico.\n\n"
        "A variação total de entropia $\\Delta S$ vale:\n\n"
        "A $\\Delta S = C_v \\ln\\left(\\frac{9}{8}\\right)$\n"
        "B $\\Delta S = 0$\n"
        "C $\\Delta S = C_v \\ln 2$\n"
        "D $\\Delta S = C_v \\ln(3/2)$\n"
        "E $\\Delta S = C_v \\ln(4/3)$"
    ),

    # =========================================================================
    # 2024-2 THERMODYNAMICS & STATISTICAL MECHANICS (16 Questions)
    # =========================================================================
    "2024-2-fePT2a": (
        "Q. 75 [fePT2a]\n"
        "Uma estrela composta essencialmente de hidrogênio atômico está a uma temperatura $T$. "
        "A razão de Boltzmann entre o número de átomos no primeiro estado excitado ($n = 2$, degenerescência $g_2 = 2n^2 = 8$, energia $-3{,}4\\text{ eV}$) "
        "e no estado fundamental ($n = 1$, degenerescência $g_1 = 2$, energia $-13{,}6\\text{ eV}$) com $\\Delta E = 10{,}2\\text{ eV}$ vale:\n\n"
        "A $\\frac{N_2}{N_1} = 4 e^{-10{,}2\\text{ eV}/(k_B T)}$\n"
        "B $\\frac{N_2}{N_1} = e^{-10{,}2\\text{ eV}/(k_B T)}$\n"
        "C $\\frac{N_2}{N_1} = 8 e^{-13{,}6\\text{ eV}/(k_B T)}$\n"
        "D $\\frac{N_2}{N_1} = 2 e^{-3{,}4\\text{ eV}/(k_B T)}$\n"
        "E $\\frac{N_2}{N_1} = \\frac{1}{4} e^{-10{,}2\\text{ eV}/(k_B T)}$"
    ),
    "2024-2-fePT2b": (
        "Q. 76 [fePT2b]\n"
        "Para a mesma estrela de hidrogênio a temperatura $T$, a razão entre o número de átomos no estado $n = 3$ ($g_3 = 18$, $E_3 = -1{,}51\\text{ eV}$, $\\Delta E = 12{,}09\\text{ eV}$) "
        "e no estado fundamental $n = 1$ vale:\n\n"
        "A $\\frac{N_3}{N_1} = 9 e^{-12{,}09\\text{ eV}/(k_B T)}$\n"
        "B $\\frac{N_3}{N_1} = 3 e^{-12{,}09\\text{ eV}/(k_B T)}$\n"
        "C $\\frac{N_3}{N_1} = 18 e^{-13{,}6\\text{ eV}/(k_B T)}$\n"
        "D $\\frac{N_3}{N_1} = e^{-12{,}09\\text{ eV}/(k_B T)}$\n"
        "E $\\frac{N_3}{N_1} = \\frac{1}{9} e^{-12{,}09\\text{ eV}/(k_B T)}$"
    ),
    "2024-2-fePT4a": (
        "Q. 79 [fePT4a]\n"
        "A atmosfera isotérmica à temperatura constante $T$ sob gravidade uniforme $g$ é tratada como gás ideal de massa molecular média $m$. "
        "A pressão $P(z)$ a uma altitude $z$ acima do nível do mar ($P(0) = P_0$) é dada pela fórmula barométrica:\n\n"
        "A $P(z) = P_0 e^{-m g z / (k_B T)}$\n"
        "B $P(z) = P_0 e^{-k_B T / (m g z)}$\n"
        "C $P(z) = P_0 \\left(1 - \\frac{mgz}{k_B T}\\right)$\n"
        "D $P(z) = P_0 e^{-2m g z / (k_B T)}$\n"
        "E $P(z) = P_0 e^{+m g z / (k_B T)}$"
    ),
    "2024-2-fePT4b": (
        "Q. 80 [fePT4b]\n"
        "Para a atmosfera isotérmica com $P(z) = P_0 e^{-z / h_0}$, a altura de escala $h_0$ em termos da constante dos gases $R$, "
        "massa molar $M$ e aceleração $g$ é:\n\n"
        "A $h_0 = \\frac{R T}{M g}$\n"
        "B $h_0 = \\frac{M g}{R T}$\n"
        "C $h_0 = \\frac{R T}{2M g}$\n"
        "D $h_0 = \\frac{2R T}{M g}$\n"
        "E $h_0 = \\sqrt{\\frac{R T}{M g}}$"
    ),
    "2024-2-tePT1a": (
        "Q. 33 [tePT1a]\n"
        "Um mol de gás ideal tem capacidade térmica a volume constante dependente da temperatura dada por $C_v(T) = a + bT$, onde $a, b > 0$. "
        "O gás é aquecido a volume constante de uma temperatura inicial $T_1$ até $T_2$.\n\n"
        "O calor absorvido $Q$ e a variação de energia interna $\\Delta U$ valem:\n\n"
        "A $Q = \\Delta U = a(T_2 - T_1) + \\frac{b}{2}(T_2^2 - T_1^2)$\n"
        "B $Q = a(T_2 - T_1) + b(T_2 - T_1)^2\\quad \\text{e}\\quad \\Delta U = 0$\n"
        "C $Q = \\Delta U = (a + b)(T_2 - T_1)$\n"
        "D $Q = \\Delta U = \\frac{a+b}{2}(T_2^2 - T_1^2)$\n"
        "E $Q = 0\\quad \\text{e}\\quad \\Delta U = a(T_2 - T_1) + \\frac{b}{2}(T_2^2 - T_1^2)$"
    ),
    "2024-2-tePT1b": (
        "Q. 34 [tePT1b]\n"
        "Um mol de gás ideal com $C_v(T) = a + bT$ realiza uma expansão isobárica à pressão constante $P_0$ de $T_1$ até $T_2$. "
        "Usando a relação de Mayer $C_p(T) = C_v(T) + R$, o calor absorvido no processo isobárico é:\n\n"
        "A $Q = (a + R)(T_2 - T_1) + \\frac{b}{2}(T_2^2 - T_1^2)$\n"
        "B $Q = a(T_2 - T_1) + \\frac{b}{2}(T_2^2 - T_1^2)$\n"
        "C $Q = R(T_2 - T_1)$\n"
        "D $Q = (a + R + b)(T_2 - T_1)$\n"
        "E $Q = \\frac{a+R}{2}(T_2^2 - T_1^2)$"
    ),
    "2024-2-tePT2a": (
        "Q. 35 [tePT2a]\n"
        "Um gás de van der Waals com energia interna molar $u(T,v) = c R T - \\frac{a}{v}$ ($a > 0$) sofre uma expansão livre adiabática "
        "(expansão de Joule) de um volume inicial $V_1$ para um volume final $V_2 > V_1$ no vácuo ($W = 0, Q = 0$).\n\n"
        "A variação de temperatura $\\Delta T = T_2 - T_1$ do gás nesse processo é:\n\n"
        "A $\\Delta T = -\\frac{a}{c R}\\left(\\frac{1}{V_1} - \\frac{1}{V_2}\\right) < 0\\quad (\\text{resfriamento})$\n"
        "B $\\Delta T = 0\\quad (\\text{temperatura constante})$\n"
        "C $\\Delta T = +\\frac{a}{c R}\\left(\\frac{1}{V_1} - \\frac{1}{V_2}\\right) > 0\\quad (\\text{aquecimento})$\n"
        "D $\\Delta T = -\\frac{a}{R}\\ln(V_2/V_1)$\n"
        "E $\\Delta T = -\\frac{a}{c R(V_2 - V_1)}$"
    ),
    "2024-2-tePT2b": (
        "Q. 36 [tePT2b]\n"
        "Na expansão livre de Joule de um gás ideal ($u = u(T)$), a variação de temperatura $\\Delta T$ e a variação de entropia $\\Delta S$ valem:\n\n"
        "A $\\Delta T = 0\\quad \\text{e}\\quad \\Delta S = n R \\ln(V_2 / V_1) > 0$\n"
        "B $\\Delta T < 0\\quad \\text{e}\\quad \\Delta S = 0$\n"
        "C $\\Delta T = 0\\quad \\text{e}\\quad \\Delta S = 0$\n"
        "D $\\Delta T > 0\\quad \\text{e}\\quad \\Delta S = n R \\ln(V_2 / V_1)$\n"
        "E $\\Delta T < 0\\quad \\text{e}\\quad \\Delta S = n R \\ln(V_2 / V_1)$"
    ),

    # =========================================================================
    # 2023-2 THERMODYNAMICS & STATISTICAL MECHANICS (16 Questions)
    # =========================================================================
    "2023-2-fePT2a": (
        "Q. 75 [fePT2a]\n"
        "Um sistema é formado por $N$ partículas independentes e distinguíveis em contato com um reservatório térmico à temperatura $T$. "
        "Cada partícula possui 2 níveis de energia: $0$ e $\\varepsilon > 0$.\n\n"
        "A energia interna média total $\\langle E \\rangle$ do sistema é dada por:\n\n"
        "A $\\langle E \\rangle = \\frac{N\\varepsilon}{e^{\\beta\\varepsilon} + 1}$\n"
        "B $\\langle E \\rangle = \\frac{N\\varepsilon}{e^{\\beta\\varepsilon} - 1}$\n"
        "C $\\langle E \\rangle = N\\varepsilon e^{-\\beta\\varepsilon}$\n"
        "D $\\langle E \\rangle = \\frac{1}{2}N\\varepsilon$\n"
        "E $\\langle E \\rangle = \\frac{N\\varepsilon}{e^{-\\beta\\varepsilon} + 1}$"
    ),
    "2023-2-fePT2b": (
        "Q. 76 [fePT2b]\n"
        "Para o sistema de $N$ partículas de dois níveis ($0$ e $\\varepsilon$), o calor específico $C_V = \\frac{\\partial \\langle E \\rangle}{\\partial T}$ vale:\n\n"
        "A $C_V = N k_B (\\beta\\varepsilon)^2 \\frac{e^{\\beta\\varepsilon}}{(e^{\\beta\\varepsilon} + 1)^2}$\n"
        "B $C_V = N k_B \\frac{e^{\\beta\\varepsilon}}{e^{\\beta\\varepsilon} + 1}$\n"
        "C $C_V = N k_B (\\beta\\varepsilon) e^{-\\beta\\varepsilon}$\n"
        "D $C_V = N k_B$\n"
        "E $C_V = \\frac{3}{2}N k_B$"
    ),
    "2023-2-fePT4a": (
        "Q. 79 [fePT4a]\n"
        "Um sistema é formado por $N$ íons magnéticos localizados e independentes de momento magnético $\\mu$ e spin $1/2$, sob campo magnético $B$ "
        "à temperatura $T$ ($E = \\mp \\mu B$).\n\n"
        "A magnetização total do sistema $\\langle M \\rangle$ em equilíbrio térmico vale:\n\n"
        "A $\\langle M \\rangle = N \\mu \\tanh(\\beta \\mu B)$\n"
        "B $\\langle M \\rangle = N \\mu \\operatorname{senh}(\\beta \\mu B)$\n"
        "C $\\langle M \\rangle = N \\mu \\cosh(\\beta \\mu B)$\n"
        "D $\\langle M \\rangle = N \\mu e^{-\\beta \\mu B}$\n"
        "E $\\langle M \\rangle = \\frac{N \\mu}{\\beta \\mu B}$"
    ),
    "2023-2-fePT4b": (
        "Q. 80 [fePT4b]\n"
        "Para o paramagneto de $N$ spins em campo magnético fraco ($\\,\\beta\\mu B \\ll 1\\,$), a susceptibilidade magnética $\\chi = \\frac{\\partial M}{\\partial B}$ "
        "obedece à Lei de Curie dada por:\n\n"
        "A $\\chi = \\frac{N \\mu^2}{k_B T}$\n"
        "B $\\chi = \\frac{N \\mu}{k_B T}$\n"
        "C $\\chi = \\frac{N \\mu^2}{(k_B T)^2}$\n"
        "D $\\chi = \\frac{N \\mu^2}{3k_B T}$\n"
        "E $\\chi = N\\mu$"
    ),
    "2023-2-tePT3a": (
        "Q. 37 [tePT3a]\n"
        "Uma massa de $m = 1{,}0\\text{ kg}$ de água a $T_i = 0^\\circ\\text{C}$ ($273\\text{ K}$) é aquecida até $T_f = 100^\\circ\\text{C}$ ($373\\text{ K}$) "
        "em contato térmico direto com um reservatório a $100^\\circ\\text{C}$. Sendo $c = 4186\\text{ J/(kg}\\cdot\\text{K)}$ o calor específico da água:\n\n"
        "A variação de entropia do universo $\\Delta S_{\\text{universo}} = \\Delta S_{\\text{água}} + \\Delta S_{\\text{reservatório}}$ é:\n\n"
        "A $\\Delta S_{\\text{universo}} \\approx +183\\text{ J/K} > 0\\quad (\\text{processo irreversível})$\n"
        "B $\\Delta S_{\\text{universo}} = 0$\n"
        "C $\\Delta S_{\\text{universo}} \\approx -183\\text{ J/K}$\n"
        "D $\\Delta S_{\\text{universo}} \\approx +1305\\text{ J/K}$\n"
        "E $\\Delta S_{\\text{universo}} \\approx +1122\\text{ J/K}$"
    ),
    "2023-2-tePT3b": (
        "Q. 38 [tePT3b]\n"
        "Uma massa de $m = 2{,}0\\text{ kg}$ de água a $0^\\circ\\text{C}$ é aquecida até $100^\\circ\\text{C}$ em contato com reservatório a $100^\\circ\\text{C}$. "
        "A variação de entropia da água $\\Delta S_{\\text{água}}$ vale:\n\n"
        "A $\\Delta S_{\\text{água}} = 2{,}0 \\cdot 4186 \\cdot \\ln(373/273) \\approx 2610\\text{ J/K}$\n"
        "B $\\Delta S_{\\text{água}} = 0$\n"
        "C $\\Delta S_{\\text{água}} \\approx 1305\\text{ J/K}$\n"
        "D $\\Delta S_{\\text{água}} \\approx 2244\\text{ J/K}$\n"
        "E $\\Delta S_{\\text{água}} \\approx 366\\text{ J/K}$"
    ),

    # =========================================================================
    # 2022-2 THERMODYNAMICS & STATISTICAL MECHANICS (16 Questions)
    # =========================================================================
    "2022-2-tePT1a": (
        "Q. 33 [tePT1a]\n"
        "Uma mistura gasosa contém massas totais iguais de Argônio ($M_{\\text{Ar}} = 40\\text{ g/mol}$) e Hélio ($M_{\\text{He}} = 4{,}0\\text{ g/mol}$). "
        "Tratando ambos como gases ideais monoatômicos à mesma temperatura $T$ e volume $V$, a razão entre o número de mols de Hélio e de Argônio vale:\n\n"
        "A $\\frac{n_{\\text{He}}}{n_{\\text{Ar}}} = 10$\n"
        "B $\\frac{n_{\\text{He}}}{n_{\\text{Ar}}} = 1$\n"
        "C $\\frac{n_{\\text{He}}}{n_{\\text{Ar}}} = 0{,}1$\n"
        "D $\\frac{n_{\\text{He}}}{n_{\\text{Ar}}} = 4$\n"
        "E $\\frac{n_{\\text{He}}}{n_{\\text{Ar}}} = 40$"
    ),
    "2022-2-tePT1b": (
        "Q. 34 [tePT1b]\n"
        "Para a mesma mistura com massas iguais de Hélio e Argônio, a razão entre as pressões parciais $P_{\\text{He}}/P_{\\text{Ar}}$ na mistura vale:\n\n"
        "A $\\frac{P_{\\text{He}}}{P_{\\text{Ar}}} = 10$\n"
        "B $\\frac{P_{\\text{He}}}{P_{\\text{Ar}}} = 1$\n"
        "C $\\frac{P_{\\text{He}}}{P_{\\text{Ar}}} = 0{,}1$\n"
        "D $\\frac{P_{\\text{He}}}{P_{\\text{Ar}}} = 5$\n"
        "E $\\frac{P_{\\text{He}}}{P_{\\text{Ar}}} = 20$"
    ),
    "2022-2-tePT2a": (
        "Q. 35 [tePT2a]\n"
        "Se $R$ é a constante universal dos gases, a variação de entropia de $n$ mols de um gás ideal quando este expande isotermicamente "
        "de um volume inicial $V_i$ a um volume final $V_f = 2V_i$ é:\n\n"
        "A $\\Delta S = n R \\ln 2$\n"
        "B $\\Delta S = n R \\ln(0{,}5)$\n"
        "C $\\Delta S = \\frac{R \\ln 2}{n}$\n"
        "D $\\Delta S = 2 n R \\ln 2$\n"
        "E $\\Delta S = 0$"
    ),
    "2022-2-tePT2b": (
        "Q. 36 [tePT2b]\n"
        "A variação de entropia de $n$ mols de um gás ideal que expande isotermicamente de $V_i$ para $V_f = 4V_i$ é:\n\n"
        "A $\\Delta S = 2 n R \\ln 2$\n"
        "B $\\Delta S = n R \\ln 2$\n"
        "C $\\Delta S = 4 n R \\ln 2$\n"
        "D $\\Delta S = n R \\ln 4$\n"
        "E $\\Delta S = 0$"
    ),
    "2022-2-tePT4a": (
        "Q. 39 [tePT4a]\n"
        "Uma máquina térmica de Carnot opera entre dois reservatórios térmicos nas temperaturas $T_H = 500\\text{ K}$ e $T_C = 300\\text{ K}$. "
        "O rendimento teórico máximo dessa máquina operando como motor térmico é:\n\n"
        "A $\\eta_{\\text{Carnot}} = 1 - \\frac{300}{500} = 40\\%$\n"
        "B $\\eta_{\\text{Carnot}} = 60\\%$\n"
        "C $\\eta_{\\text{Carnot}} = 50\\%$\n"
        "D $\\eta_{\\text{Carnot}} = 20\\%$\n"
        "E $\\eta_{\\text{Carnot}} = 80\\%$"
    ),
    "2022-2-tePT4b": (
        "Q. 40 [tePT4b]\n"
        "Quando a mesma máquina de Carnot opera em ciclo reverso como refrigerador entre $T_C = 300\\text{ K}$ e $T_H = 500\\text{ K}$, "
        "o coeficiente de desempenho (COP) $K = \\frac{Q_C}{W}$ vale:\n\n"
        "A $K = \\frac{T_C}{T_H - T_C} = \\frac{300}{200} = 1{,}5$\n"
        "B $K = 2{,}5$\n"
        "C $K = 0{,}6$\n"
        "D $K = 3{,}0$\n"
        "E $K = 0{,}4$"
    ),
    "2022-2-fePT3a": (
        "Q. 77 [fePT3a]\n"
        "Um sistema de $N$ íons magnéticos de spin $1/2$ com energias $\\mp \\mu B$ está em contato com um reservatório térmico à temperatura $T$.\n\n"
        "A capacidade térmica magnética $C_B$ apresenta o comportamento da anomalia de Schottky dado por:\n\n"
        "A $C_B = N k_B (\\beta \\mu B)^2 \\operatorname{sech}^2(\\beta \\mu B)$\n"
        "B $C_B = N k_B \\tanh(\\beta \\mu B)$\n"
        "C $C_B = N k_B (\\beta \\mu B)$\n"
        "D $C_B = \\frac{3}{2}N k_B$\n"
        "E $C_B = N k_B$"
    ),
    "2022-2-fePT3b": (
        "Q. 78 [fePT3b]\n"
        "No limite de temperaturas muito altas ($k_B T \\gg \\mu B$), a capacidade térmica magnética $C_B$ do paramagneto decai com a temperatura como:\n\n"
        "A $C_B \\propto \\frac{1}{T^2}$\n"
        "B $C_B \\propto \\frac{1}{T}$\n"
        "C $C_B \\propto T$\n"
        "D $C_B \\propto T^3$\n"
        "E $C_B = \\text{constante}$"
    ),
}


def apply_te_fe_reconstructions():
    print("=" * 65)
    print("🔥 RECONSTRUCTING THERMO & STAT-MECH QUESTIONS (LATEX + OPTIONS)")
    print("=" * 65)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    updated = 0
    for qid, clean_text in TE_FE_RECONSTRUCTIONS.items():
        cur.execute("UPDATE questions SET text = ? WHERE id = ?", (clean_text, qid))
        if cur.rowcount > 0:
            updated += 1
            print(f"  ✓ Reconstructed {qid}")
        else:
            print(f"  ⚠ Question ID not found in DB: {qid}")

    conn.commit()
    conn.close()

    print(f"\n✅ Successfully updated {updated} Thermo / StatMech questions in SQLite.")
    print("🚀 Exporting updated questions.json...")
    export_bank_to_json()
    print("✨ Complete!")


if __name__ == "__main__":
    apply_te_fe_reconstructions()
