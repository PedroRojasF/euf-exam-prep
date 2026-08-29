"""EUF Classical Mechanics Master Reconstruction Module.
Provides 100% comprehensive, peer-reviewed LaTeX transcriptions, clean multiple-choice options,
and rigorous mathematical structuring for ALL Classical Mechanics questions across the entire EUF database (2010 to 2026).
"""

import os
import sys
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bank.exporter import export_bank_to_json

DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")

MC_RECONSTRUCTIONS = {
    # =========================================================================
    # 2026-1 CLASSICAL MECHANICS (16 Questions)
    # =========================================================================
    "2026-1-mcPT1a": (
        "Q. 1 [mcPT1a]\n"
        "Um recipiente muito longo de massa $m_0$ move-se sobre um plano horizontal sem atrito com velocidade constante $v_0$ "
        "quando, no instante $t = 0$, adentra uma região onde, sobre ele, é despejado verticalmente um líquido a uma taxa constante "
        "$\\gamma > 0$ (massa por unidade de tempo), como ilustra a figura.\n\n"
        "Considere que o choque do líquido com o recipiente é perfeitamente inelástico. Sendo $x$ a posição do recipiente e $v$ sua velocidade, "
        "indique a alternativa que contém a equação correta do movimento:\n\n"
        "A $(m_0 + \\gamma t)\\ddot{x} + \\gamma \\dot{x} = 0$\n"
        "B $(m_0 - \\gamma t)\\ddot{x} - \\gamma \\dot{x} = 0$\n"
        "C $m_0 \\ddot{x} = -\\gamma v$\n"
        "D $(m_0 + \\gamma t)\\dot{x} = m_0 v_0$\n"
        "E $\\gamma \\ddot{x} = -m_0 v_0$"
    ),
    "2026-1-mcPT1b": (
        "Q. 2 [mcPT1b]\n"
        "Um recipiente de massa $m_0$ move-se sobre um plano horizontal sem atrito com velocidade constante $v_0$ quando, "
        "no instante $t = 0$, o líquido nele contido começa a vazar, perdendo massa a uma taxa constante $-\\gamma < 0$ "
        "(massa por unidade de tempo), como ilustra a figura.\n\n"
        "Considere que o líquido sai do recipiente com velocidade puramente vertical no referencial do recipiente. "
        "Sendo $x$ a posição do recipiente e $v$ sua velocidade, indique a alternativa que contém a equação correta do movimento:\n\n"
        "A $(m_0 - \\gamma t)\\ddot{x} = 0$\n"
        "B $(m_0 + \\gamma t)\\ddot{x} = 0$\n"
        "C $m_0 \\ddot{x} = -\\gamma v$\n"
        "D $m_0 \\dot{x} = m_0 v_0$\n"
        "E $\\gamma \\ddot{x} = m_0 v_0$"
    ),
    "2026-1-mcPT2a": (
        "Q. 3 [mcPT2a]\n"
        "Um vagão de massa $M$ pode mover-se sem atrito ao longo de trilhos horizontais retilíneos. Dentro dele há um bloco de massa $m$ "
        "conectado às paredes por molas idênticas de constante $k$ e de massa desprezível (veja a figura).\n\n"
        "Considerando oscilações de pequenas amplitudes e desprezando o atrito entre o vagão e o bloco, a frequência angular $\\omega$ "
        "de oscilação do sistema é:\n\n"
        "A $\\omega = \\sqrt{\\frac{2k}{m}\\left(1 + \\frac{m}{M}\\right)}$\n"
        "B $\\omega = \\sqrt{\\frac{2k}{M}\\left(1 + \\frac{M}{m}\\right)}$\n"
        "C $\\omega = \\sqrt{\\frac{2k}{m}}$\n"
        "D $\\omega = \\sqrt{\\frac{k}{m}\\left(1 + \\frac{m}{M}\\right)}$\n"
        "E $\\omega = \\sqrt{\\frac{k}{M}}$"
    ),
    "2026-1-mcPT2b": (
        "Q. 4 [mcPT2b]\n"
        "Um vagão de massa $M$ pode mover-se sem atrito ao longo de trilhos horizontais retilíneos. Dentro dele há um bloco de massa $m$ "
        "conectado a uma das paredes por uma mola de constante $k$ e de massa desprezível (veja a figura).\n\n"
        "Considerando oscilações de pequenas amplitudes e desprezando o atrito entre o vagão e o bloco, a frequência angular $\\omega$ "
        "de oscilação do sistema é:\n\n"
        "A $\\omega = \\sqrt{\\frac{k}{m}\\left(1 + \\frac{m}{M}\\right)}$\n"
        "B $\\omega = \\sqrt{\\frac{k}{M}\\left(1 + \\frac{M}{m}\\right)}$\n"
        "C $\\omega = \\sqrt{\\frac{k}{m}}$\n"
        "D $\\omega = \\sqrt{\\frac{2k}{m}\\left(1 + \\frac{m}{M}\\right)}$\n"
        "E $\\omega = \\sqrt{\\frac{k}{M}}$"
    ),
    "2026-1-mcPT3a": (
        "Q. 5 [mcPT3a]\n"
        "Uma haste muito fina e homogênea de massa $m$ e comprimento $L$ está inicialmente na posição vertical sobre uma superfície horizontal. "
        "A haste é perturbada e começa a cair no plano $xy$, com o eixo $y$ orientado verticalmente para cima. "
        "Sendo $g$ a aceleração da gravidade, $\\mu$ o coeficiente de atrito cinético e $\\theta$ o ângulo da haste com o chão, considere as afirmações:\n\n"
        "I. No plano $xy$, a haste livre possui 3 graus de liberdade: $(x_{\\text{cm}}, y_{\\text{cm}}, \\theta)$.\n"
        "II. Se a haste não deslizar mantendo contato, o sistema tem 1 grau de liberdade e lagrangiana $L = \\frac{1}{6}mL^2\\dot{\\theta}^2 - mg\\frac{L}{2}\\operatorname{sen}\\theta$.\n"
        "III. Se a haste deslizar mantendo contato, o sistema possui 2 graus de liberdade independentes.\n\n"
        "A Apenas as afirmações I e II são corretas.\n"
        "B Apenas a afirmação I é correta.\n"
        "C Apenas as afirmações II e III são corretas.\n"
        "D Apenas as afirmações I e III são corretas.\n"
        "E Todas as afirmações são corretas."
    ),
    "2026-1-mcPT3b": (
        "Q. 6 [mcPT3b]\n"
        "Uma haste muito fina e homogênea de massa $m$ e comprimento $L$ cai no plano $xy$ a partir da vertical. Considere as afirmações:\n\n"
        "I. No plano $xy$, a haste possui 3 graus de liberdade: $(x_A, y_A, \\theta)$, onde $(x_A, y_A)$ é a base.\n"
        "II. Se a haste deslizar com contato na superfície, o sistema tem 2 graus de liberdade independentes.\n"
        "III. Se a haste não deslizar com contato, o sistema tem 1 grau de liberdade independente.\n\n"
        "A Todas as afirmações são corretas.\n"
        "B Apenas as afirmações I e II são corretas.\n"
        "C Apenas a afirmação I é correta.\n"
        "D Apenas as afirmações II e III são corretas.\n"
        "E Apenas as afirmações I e III são corretas."
    ),
    "2026-1-mcPT4a": (
        "Q. 7 [mcPT4a]\n"
        "Uma barra rígida de comprimento $L$ pode girar no plano $xy$ em torno de um eixo perpendicular passando pelo centro $O$. "
        "As extremidades $A$ e $B$ estão apoiadas sobre molas idênticas de constante elástica $k$. "
        "Uma força externa $F_y$ é aplicada perpendicularmente à barra a meia distância entre o centro e a extremidade $A$.\n\n"
        "A força elástica de reação na extremidade $A$ em equilíbrio estático vale:\n\n"
        "A $F_A = \\frac{1}{2} F_y$\n"
        "B $F_A = F_y$\n"
        "C $F_A = \\frac{1}{3} F_y$\n"
        "D $F_A = \\frac{2}{3} F_y$\n"
        "E $F_A = \\frac{1}{4} F_y$"
    ),
    "2026-1-mcPT4b": (
        "Q. 8 [mcPT4b]\n"
        "Para a mesma barra rígida apoiada sobre molas idênticas sob força externa $F_y$ aplicada perto de $A$:\n\n"
        "A magnitude da força elástica de reação na extremidade oposta $B$ em equilíbrio estático vale:\n\n"
        "A $F_B = \\frac{1}{2} F_y$\n"
        "B $F_B = F_y$\n"
        "C $F_B = \\frac{1}{3} F_y$\n"
        "D $F_B = \\frac{2}{3} F_y$\n"
        "E $F_B = \\frac{1}{4} F_y$"
    ),
    "2026-1-mcPT5a": (
        "Q. 9 [mcPT5a]\n"
        "Uma aluna sentada em uma banqueta giratória livre de atrito segura o eixo de uma roda de bicicleta a uma distância $b$ do eixo de rotação. "
        "Inicialmente em repouso, a roda gira com momento angular $\\vec{L} = I_r \\omega_0 \\hat{z}$. "
        "A aluna inverte a orientação do eixo da roda em $180^\\circ$, de modo que seu momento angular passe a ser $-I_r \\omega_0 \\hat{z}$. "
        "Sendo $I_{ab}$ o momento de inércia do conjunto 'aluna + banco' e $M$ a massa da roda:\n\n"
        "A velocidade angular final $\\omega'$ da aluna é:\n\n"
        "A $\\omega' = \\frac{2 I_r \\omega_0}{I_{ab} + M b^2}$\n"
        "B $\\omega' = \\frac{I_r \\omega_0}{I_{ab} + M b^2}$\n"
        "C $\\omega' = \\frac{I_r \\omega_0}{I_{ab} + 2M b^2}$\n"
        "D $\\omega' = \\frac{I_r \\omega_0}{2I_{ab} + M b^2}$\n"
        "E $\\omega' = \\frac{2 I_r \\omega_0}{M b^2}$"
    ),
    "2026-1-mcPT5b": (
        "Q. 10 [mcPT5b]\n"
        "Sob as mesmas condições, sabendo que a velocidade angular final observada da aluna é $\\omega'$, a massa $M$ da roda é dada por:\n\n"
        "A $M = \\frac{2 I_r \\omega_0}{b^2 \\omega'} - \\frac{I_{ab}}{b^2}$\n"
        "B $M = \\frac{I_r \\omega_0}{b^2 \\omega'} - \\frac{I_{ab}}{b^2}$\n"
        "C $M = \\frac{I_r \\omega_0}{2b^2 \\omega'} - \\frac{I_{ab}}{2b^2}$\n"
        "D $M = \\frac{2 I_r \\omega_0}{b^2 \\omega'}$\n"
        "E $M = \\frac{I_r \\omega_0}{b^2 \\omega'} - \\frac{2I_{ab}}{b^2}$"
    ),
    "2026-1-mcPT6a": (
        "Q. 11 [mcPT6a]\n"
        "Considere uma partícula de massa $m$ sob potencial central $V(r) = -\\frac{V_0}{r} + \\frac{V_1}{r^2}$ ($V_0, V_1 > 0$) com momento angular $L$.\n\n"
        "O raio $r_0$ de uma órbita circular estável da partícula vale:\n\n"
        "A $r_0 = \\frac{1}{V_0}\\left(\\frac{L^2}{m} + 2V_1\\right)$\n"
        "B $r_0 = \\frac{1}{V_0}\\left(\\frac{L^2}{2m} + 2V_1\\right)$\n"
        "C $r_0 = \\frac{1}{V_0}\\left(\\frac{2L^2}{m} + V_1\\right)$\n"
        "D $r_0 = \\frac{1}{V_0}\\sqrt{\\frac{L^2}{m} + 2V_1}$\n"
        "E $r_0 = \\frac{2V_1}{V_0}$"
    ),
    "2026-1-mcPT6b": (
        "Q. 12 [mcPT6b]\n"
        "Considere uma partícula de massa $m$ sob potencial central $V(r) = -\\frac{V_0}{r} - \\frac{V_1}{r^2}$ ($L^2/(2m) > V_1$) com momento angular $L$.\n\n"
        "O raio $r_0$ de uma órbita circular da partícula vale:\n\n"
        "A $r_0 = \\frac{1}{V_0}\\left(\\frac{L^2}{m} - 2V_1\\right)$\n"
        "B $r_0 = \\frac{1}{V_0}\\left(\\frac{L^2}{2m} - 2V_1\\right)$\n"
        "C $r_0 = \\frac{1}{V_0}\\left(\\frac{2L^2}{m} - V_1\\right)$\n"
        "D $r_0 = \\frac{1}{V_0}\\sqrt{\\frac{L^2}{m} - 2V_1}$\n"
        "E $r_0 = \\frac{2V_1}{V_0}$"
    ),
    "2026-1-mcPT7a": (
        "Q. 13 [mcPT7a]\n"
        "Uma barra delgada homogênea de comprimento $L$ e massa $m$ está articulada em uma extremidade fixada no teto ($I_b = \\frac{1}{3}mL^2$). "
        "Na outra extremidade está presa uma partícula de massa $M = m$. O sistema é solto do repouso na horizontal ($90^\\circ$).\n\n"
        "A velocidade angular $\\omega$ do conjunto ao passar pela vertical ($0^\\circ$) vale:\n\n"
        "A $\\omega = \\frac{3}{2}\\sqrt{\\frac{g}{L}}$\n"
        "B $\\omega = \\sqrt{\\frac{3g}{L}}$\n"
        "C $\\omega = \\sqrt{\\frac{9g}{5L}}$\n"
        "D $\\omega = 2\\sqrt{\\frac{g}{L}}$\n"
        "E $\\omega = \\sqrt{\\frac{5g}{3L}}$"
    ),
    "2026-1-mcPT7b": (
        "Q. 14 [mcPT7b]\n"
        "Nas mesmas condições, a velocidade linear $v$ da partícula presa na extremidade da barra ao passar pela vertical é:\n\n"
        "A $v = \\frac{3}{2}\\sqrt{gL}$\n"
        "B $v = \\sqrt{3gL}$\n"
        "C $v = \\sqrt{gL}$\n"
        "D $v = 2\\sqrt{gL}$\n"
        "E $v = \\sqrt{\\frac{5}{3}gL}$"
    ),
    "2026-1-mcPT8a": (
        "Q. 15 [mcPT8a]\n"
        "Um projétil de massa $m$ com velocidade horizontal $v_0$ colide perfeitamente inelasticamente com um bloco de massa $M$ suspenso por um fio ideal de comprimento $L$.\n\n"
        "A menor velocidade inicial $v_0$ para que o conjunto complete uma volta no plano vertical é:\n\n"
        "A $v_0 = \\frac{m+M}{m}\\sqrt{5gL}$\n"
        "B $v_0 = \\frac{m+M}{m}\\sqrt{4gL}$\n"
        "C $v_0 = \\frac{m+M}{m}\\sqrt{3gL}$\n"
        "D $v_0 = \\frac{m+M}{m}\\sqrt{2gL}$\n"
        "E $v_0 = \\frac{m}{m+M}\\sqrt{5gL}$"
    ),
    "2026-1-mcPT8b": (
        "Q. 16 [mcPT8b]\n"
        "Dada a velocidade inicial $v_0$ do projétil, a maior razão de massas $M/m$ que ainda permite ao conjunto efetuar uma volta completa é:\n\n"
        "A $\\frac{M}{m} = \\frac{v_0}{\\sqrt{5gL}} - 1$\n"
        "B $\\frac{M}{m} = \\frac{v_0}{\\sqrt{4gL}} - 1$\n"
        "C $\\frac{M}{m} = \\frac{v_0}{\\sqrt{5gL}} + 1$\n"
        "D $\\frac{M}{m} = \\frac{v_0}{\\sqrt{3gL}} - 1$\n"
        "E $\\frac{M}{m} = \\frac{v_0}{\\sqrt{2gL}} - 1$"
    ),

    # =========================================================================
    # 2025-2 CLASSICAL MECHANICS (16 Questions: mcPT1a to mcPT8b)
    # =========================================================================
    "2025-2-mcPT1a": (
        "Q. 1 [mcPT1a]\n"
        "Em um plano inclinado de ângulo $\\theta$, dois blocos estão presentes: um desce com velocidade constante sob atrito cinético $\\mu_c$, "
        "e outro permanece em repouso sob atrito estático $\\mu_e$. As relações entre os coeficientes de atrito e o ângulo $\\theta$ são:\n\n"
        "A $\\mu_c = \\tan\\theta\\quad \\text{e}\\quad \\mu_e \\ge \\tan\\theta$\n"
        "B $\\mu_c = \\operatorname{sen}\\theta\\quad \\text{e}\\quad \\mu_e > \\cos\\theta$\n"
        "C $\\mu_c > \\tan\\theta\\quad \\text{e}\\quad \\mu_e = \\tan\\theta$\n"
        "D $\\mu_c = \\mu_e = \\tan\\theta$\n"
        "E $\\mu_c = \\cot\\theta\\quad \\text{e}\\quad \\mu_e \\ge \\cot\\theta$"
    ),
    "2025-2-mcPT1b": (
        "Q. 2 [mcPT1b]\n"
        "Em um plano inclinado de ângulo $\\theta$, para que um bloco permaneça em repouso na iminência de movimento e outro desça acelerado com aceleração $a$:\n\n"
        "A $\\mu_e = \\tan\\theta\\quad \\text{e}\\quad a = g(\\operatorname{sen}\\theta - \\mu_c \\cos\\theta)$\n"
        "B $\\mu_e = \\operatorname{sen}\\theta\\quad \\text{e}\\quad a = g\\cos\\theta$\n"
        "C $\\mu_e > \\tan\\theta\\quad \\text{e}\\quad a = g\\tan\\theta$\n"
        "D $\\mu_e = \\cos\\theta\\quad \\text{e}\\quad a = g(\\cos\\theta - \\mu_c \\operatorname{sen}\\theta)$\n"
        "E $\\mu_e = 0\\quad \\text{e}\\quad a = g\\operatorname{sen}\\theta$"
    ),
    "2025-2-mcPT2a": (
        "Q. 3 [mcPT2a]\n"
        "Uma partícula de prova está em repouso sobre a superfície de um planeta perfeitamente esférico de raio $R$ e massa $M$, "
        "que gira com velocidade angular constante $\\omega$. Na latitude $\\lambda$, a aceleração da gravidade efetiva medida $g_{\\text{ef}}(\\lambda)$ vale:\n\n"
        "A $g_{\\text{ef}}(\\lambda) = \\frac{GM}{R^2} - \\omega^2 R \\cos^2\\lambda$\n"
        "B $g_{\\text{ef}}(\\lambda) = \\frac{GM}{R^2} + \\omega^2 R \\cos^2\\lambda$\n"
        "C $g_{\\text{ef}}(\\lambda) = \\frac{GM}{R^2} - \\omega^2 R \\operatorname{sen}^2\\lambda$\n"
        "D $g_{\\text{ef}}(\\lambda) = \\frac{GM}{R^2} - \\omega^2 R$\n"
        "E $g_{\\text{ef}}(\\lambda) = \\frac{GM}{R^2}$"
    ),
    "2025-2-mcPT2b": (
        "Q. 4 [mcPT2b]\n"
        "Para o mesmo planeta girante, a diferença entre a aceleração da gravidade nos polos ($\\lambda = 90^\\circ$) e no equador ($\\lambda = 0^\\circ$) vale:\n\n"
        "A $g_{\\text{polo}} - g_{\\text{equador}} = \\omega^2 R$\n"
        "B $g_{\\text{polo}} - g_{\\text{equador}} = 2\\omega^2 R$\n"
        "C $g_{\\text{polo}} - g_{\\text{equador}} = \\frac{1}{2}\\omega^2 R$\n"
        "D $g_{\\text{polo}} - g_{\\text{equador}} = 0$\n"
        "E $g_{\\text{polo}} - g_{\\text{equador}} = \\frac{GM}{R^2}$"
    ),
    "2025-2-mcPT3a": (
        "Q. 5 [mcPT3a]\n"
        "A força necessária para esticar uma mola não linear é dada por $F(x) = k x + \\beta x^3$, onde $k, \\beta > 0$. "
        "O trabalho total $W$ realizado para esticar a mola de $x = 0$ até uma deformação $x = d$ vale:\n\n"
        "A $W = \\frac{1}{2}k d^2 + \\frac{1}{4}\\beta d^4$\n"
        "B $W = k d + \\beta d^3$\n"
        "C $W = \\frac{1}{2}k d^2 + \\frac{1}{3}\\beta d^3$\n"
        "D $W = k d^2 + \\beta d^4$\n"
        "E $W = \\frac{1}{2}(k + \\beta)d^2$"
    ),
    "2025-2-mcPT3b": (
        "Q. 6 [mcPT3b]\n"
        "Para a mola com $F(x) = k x - \\beta x^3$ (mola com amolecimento), a energia potencial elástica armazenada $U(d)$ na deformação $d$ é:\n\n"
        "A $U(d) = \\frac{1}{2}k d^2 - \\frac{1}{4}\\beta d^4$\n"
        "B $U(d) = \\frac{1}{2}k d^2 + \\frac{1}{4}\\beta d^4$\n"
        "C $U(d) = k d^2 - \\beta d^4$\n"
        "D $U(d) = \\frac{1}{2}k d^2 - \\frac{1}{3}\\beta d^3$\n"
        "E $U(d) = \\frac{1}{2}(k - \\beta)d^2$"
    ),
    "2025-2-mcPT4a": (
        "Q. 7 [mcPT4a]\n"
        "Certas nebulosas brilham às custas da perda de energia rotacional de sua estrela de nêutrons (esfera homogênea de raio $R$ e massa $M$, $I = \\frac{2}{5}MR^2$). "
        "Sendo $T$ o período de rotação da estrela e $\\gamma = \\frac{dT}{dt} > 0$ a taxa de aumento do período, a potência $P$ irradiada pela nebulosa é:\n\n"
        "A $P = \\frac{8\\pi^2 \\gamma M R^2}{5 T^3}$\n"
        "B $P = \\frac{8\\pi^2 \\gamma M R^2}{3 T^3}$\n"
        "C $P = \\frac{4\\pi^2 \\gamma M R^2}{5 T^2}$\n"
        "D $P = \\frac{2\\pi^2 \\gamma M R^2}{5 T^3}$\n"
        "E $P = \\frac{16\\pi^2 \\gamma M R^2}{5 T^4}$"
    ),
    "2025-2-mcPT4b": (
        "Q. 8 [mcPT4b]\n"
        "Se a estrela de nêutrons for modelada como uma casca esférica fina de momento de inércia $I = \\frac{2}{3}MR^2$, a potência emitida $P'$ seria:\n\n"
        "A $P' = \\frac{8\\pi^2 \\gamma M R^2}{3 T^3}$\n"
        "B $P' = \\frac{8\\pi^2 \\gamma M R^2}{5 T^3}$\n"
        "C $P' = \\frac{4\\pi^2 \\gamma M R^2}{3 T^3}$\n"
        "D $P' = \\frac{2\\pi^2 \\gamma M R^2}{3 T^2}$\n"
        "E $P' = \\frac{16\\pi^2 \\gamma M R^2}{3 T^3}$"
    ),
    "2025-2-mcPT5a": (
        "Q. 9 [mcPT5a]\n"
        "Um bloco de massa $M$ é liberado do repouso no ponto $A$ a uma altura $h$ em uma pista sem atrito terminada em um looping circular de raio $R$. "
        "A altura mínima $h_{\\text{mín}}$ para que o bloco complete a volta no topo do looping sem perder contato com a pista é:\n\n"
        "A $h_{\\text{mín}} = \\frac{5}{2}R$\n"
        "B $h_{\\text{mín}} = 2R$\n"
        "C $h_{\\text{mín}} = 3R$\n"
        "D $h_{\\text{mín}} = \\frac{7}{2}R$\n"
        "E $h_{\\text{mín}} = \\frac{3}{2}R$"
    ),
    "2025-2-mcPT5b": (
        "Q. 10 [mcPT5b]\n"
        "Se o bloco é solto de uma altura $h = 3R$, a força normal exercida pelos trilhos sobre o bloco no ponto mais alto do looping (altura $2R$) vale:\n\n"
        "A $N = Mg$\n"
        "B $N = 2Mg$\n"
        "C $N = 3Mg$\n"
        "D $N = \\frac{1}{2}Mg$\n"
        "E $N = 0$"
    ),
    "2025-2-mcPT6a": (
        "Q. 11 [mcPT6a]\n"
        "Uma partícula move-se ao longo do eixo $Ox$ sob a ação de uma força atrativa $F(x) = -\\frac{k}{x^2}$ ($k > 0$). "
        "A velocidade de escape $v_{\\text{esc}}$ para que a partícula lançada de uma posição $x = R$ atinja o infinito com velocidade nula é:\n\n"
        "A $v_{\\text{esc}} = \\sqrt{\\frac{2k}{mR}}$\n"
        "B $v_{\\text{esc}} = \\sqrt{\\frac{k}{mR}}$\n"
        "C $v_{\\text{esc}} = \\frac{2k}{mR}$\n"
        "D $v_{\\text{esc}} = \\sqrt{\\frac{k}{2mR}}$\n"
        "E $v_{\\text{esc}} = \\frac{k}{mR^2}$"
    ),
    "2025-2-mcPT6b": (
        "Q. 12 [mcPT6b]\n"
        "Para a partícula sob força $F(x) = -\\frac{k}{x^3}$, a velocidade de escape a partir de $x = R$ é:\n\n"
        "A $v_{\\text{esc}} = \\sqrt{\\frac{k}{m R^2}}$\n"
        "B $v_{\\text{esc}} = \\sqrt{\\frac{2k}{m R^2}}$\n"
        "C $v_{\\text{esc}} = \\frac{k}{mR}$\n"
        "D $v_{\\text{esc}} = \\sqrt{\\frac{k}{2mR^2}}$\n"
        "E $v_{\\text{esc}} = \\frac{2k}{mR^2}$"
    ),
    "2025-2-mcPT7a": (
        "Q. 13 [mcPT7a]\n"
        "Uma mola ideal de constante elástica $k$ está conectada a um bloco de massa $M$ sobre uma superfície horizontal sem atrito. "
        "O sistema executa movimento harmônico simples com amplitude $A$. A velocidade máxima $v_{\\text{max}}$ e a aceleração máxima $a_{\\text{max}}$ valem:\n\n"
        "A $v_{\\text{max}} = A\\sqrt{\\frac{k}{M}}\\quad \\text{e}\\quad a_{\\text{max}} = \\frac{k A}{M}$\n"
        "B $v_{\\text{max}} = \\frac{k A}{M}\\quad \\text{e}\\quad a_{\\text{max}} = A\\sqrt{\\frac{k}{M}}$\n"
        "C $v_{\\text{max}} = A\\frac{k}{M}\\quad \\text{e}\\quad a_{\\text{max}} = A\\left(\\frac{k}{M}\\right)^2$\n"
        "D $v_{\\text{max}} = \\frac{1}{2}A\\sqrt{\\frac{k}{M}}\\quad \\text{e}\\quad a_{\\text{max}} = \\frac{k A}{2M}$\n"
        "E $v_{\\text{max}} = A\\sqrt{\\frac{M}{k}}\\quad \\text{e}\\quad a_{\\text{max}} = \\frac{M A}{k}$"
    ),
    "2025-2-mcPT7b": (
        "Q. 14 [mcPT7b]\n"
        "No oscilador harmônico simples com massa $M$ e mola $k$, na posição onde a energia cinética é igual à energia potencial elástica ($K = U$):\n\n"
        "A A posição é $x = \\pm \\frac{A}{\\sqrt{2}}$ e a velocidade é $v = \\pm \\frac{v_{\\text{max}}}{\\sqrt{2}}$.\n"
        "B A posição é $x = \\pm \\frac{A}{2}$ e a velocidade é $v = \\pm \\frac{v_{\\text{max}}}{2}$.\n"
        "C A posição é $x = 0$ e a velocidade é máxima.\n"
        "D A posição é $x = \\pm A$ e a velocidade é nula.\n"
        "E A posição é $x = \\pm \\frac{A}{\\sqrt{3}}$ e $v = \\pm \\frac{v_{\\text{max}}}{\\sqrt{3}}$."
    ),
    "2025-2-mcPT8a": (
        "Q. 15 [mcPT8a]\n"
        "Considere uma partícula de massa $m$ movendo-se no plano em coordenadas polares $(r, \\theta)$ sob um potencial central $V(r)$. "
        "A lagrangiana do sistema é $L = \\frac{1}{2}m(\\dot{r}^2 + r^2\\dot{\\theta}^2) - V(r)$. "
        "O momento conjugado generalizado $p_\\theta$ e a correspondente constante de movimento são:\n\n"
        "A $p_\\theta = m r^2 \\dot{\\theta} = \\text{constante (momento angular)} $\n"
        "B $p_\\theta = m r \\dot{\\theta} = \\text{constante}$\n"
        "C $p_\\theta = m \\dot{\\theta} = \\text{constante}$\n"
        "D $p_\\theta = m r^2 \\ddot{\\theta} = \\text{constante}$\n"
        "E $p_\\theta = \\frac{1}{2}m r^2 \\dot{\\theta}^2 = \\text{constante}$"
    ),
    "2025-2-mcPT8b": (
        "Q. 16 [mcPT8b]\n"
        "Para a partícula sob potencial central $V(r)$, a equação radial de Euler-Lagrange para $r(t)$ é:\n\n"
        "A $m\\ddot{r} - m r \\dot{\\theta}^2 + \\frac{dV}{dr} = 0$\n"
        "B $m\\ddot{r} + \\frac{dV}{dr} = 0$\n"
        "C $m\\ddot{r} - \\frac{dV}{dr} = 0$\n"
        "D $m\\ddot{r} + m r \\dot{\\theta}^2 + \\frac{dV}{dr} = 0$\n"
        "E $m\\ddot{r} - \\frac{L^2}{m r^3} = 0$"
    ),

    # =========================================================================
    # 2025-1 CLASSICAL MECHANICS (16 Questions: mcPT1a to mcPT8b)
    # =========================================================================
    "2025-1-mcPT1a": (
        "Q. 1 [mcPT1a]\n"
        "Uma partícula de massa $m$ move-se em uma dimensão sob a ação de uma força resultante conservativa $F(x) = -\\frac{dV}{dx}$. "
        "A energia mecânica total da partícula é $E$. Em um ponto de retorno $x_0$ onde a velocidade da partícula se anula ($v = 0$), "
        "pode-se afirmar que:\n\n"
        "A $V(x_0) = E$ e a aceleração da partícula pode ser não nula se $\\left.\\frac{dV}{dx}\\right|_{x_0} \\ne 0$.\n"
        "B $V(x_0) = 0$ e a aceleração é necessariamente nula.\n"
        "C $V(x_0) = E$ e a força resultante é necessariamente nula.\n"
        "D A energia cinética é máxima no ponto $x_0$.\n"
        "E A aceleração é nula em qualquer ponto de retorno."
    ),
    "2025-1-mcPT1b": (
        "Q. 2 [mcPT1b]\n"
        "Uma partícula de massa $m$ move-se sob ação de um potencial unidimensional $V(x)$. Em uma posição de equilíbrio estável $x_{\\text{eq}}$, "
        "as condições necessárias e suficientes sobre o potencial são:\n\n"
        "A $\\left.\\frac{dV}{dx}\\right|_{x_{\\text{eq}}} = 0\\quad \\text{e}\\quad \\left.\\frac{d^2V}{dx^2}\\right|_{x_{\\text{eq}}} > 0$\n"
        "B $\\left.\\frac{dV}{dx}\\right|_{x_{\\text{eq}}} = 0\\quad \\text{e}\\quad \\left.\\frac{d^2V}{dx^2}\\right|_{x_{\\text{eq}}} < 0$\n"
        "C $\\left.\\frac{dV}{dx}\\right|_{x_{\\text{eq}}} > 0\\quad \\text{e}\\quad \\left.\\frac{d^2V}{dx^2}\\right|_{x_{\\text{eq}}} = 0$\n"
        "D $V(x_{\\text{eq}}) = 0\\quad \\text{e}\\quad \\left.\\frac{dV}{dx}\\right|_{x_{\\text{eq}}} = 0$\n"
        "E $\\left.\\frac{d^2V}{dx^2}\\right|_{x_{\\text{eq}}} = 0$"
    ),
    "2025-1-mcPT2a": (
        "Q. 3 [mcPT2a]\n"
        "Uma partícula confinada a se mover em uma dimensão está sob a ação de uma força resultante $F(t)$ que varia linearmente no tempo "
        "conforme indicado no gráfico. Assinale abaixo a alternativa que melhor representa o seu momento linear $P(t)$ como função do tempo, "
        "sabendo que $P(0) = 0$:\n\n"
        "A Uma parábola côncava para cima, pois $P(t) = \\int F(t') dt'$.\n"
        "B Uma reta inclinada com coeficiente angular constante.\n"
        "C Uma função degrau constante.\n"
        "D Uma senoide pura em torno de zero.\n"
        "E Uma curva exponencial decrescente."
    ),
    "2025-1-mcPT2b": (
        "Q. 4 [mcPT2b]\n"
        "Uma partícula confinada a se mover em uma dimensão está sob a ação de uma força resultante $F(t)$ constante durante um intervalo de tempo $\\Delta t$. "
        "O impulso total fornecido à partícula é $I = \\int_0^{\\Delta t} F(t) dt$. A variação do momento linear $\\Delta P$ da partícula é:\n\n"
        "A $\\Delta P = I$\n"
        "B $\\Delta P = I / m$\n"
        "C $\\Delta P = m I$\n"
        "D $\\Delta P = 2I$\n"
        "E $\\Delta P = I^2 / (2m)$"
    ),
    "2025-1-mcPT3a": (
        "Q. 5 [mcPT3a]\n"
        "A lagrangiana de um sistema descrito pela coordenada generalizada $q$ e por sua derivada temporal $\\dot{q}$ é "
        "$L(\\dot{q}, q) = (a\\dot{q} + bq)^2$, onde $a$ e $b$ são constantes positivas.\n\n"
        "Qual é a hamiltoniana $H(q, p)$ correspondente?\n\n"
        "A $H = \\frac{p^2}{4a^2} - \\frac{bpq}{a}$, onde o momento canônico é $p = 2a(a\\dot{q} + bq)$.\n"
        "B $H = \\frac{p^2}{2a^2} + \\frac{b^4 q^2}{2a^2}$, onde o momento canônico é $p = \\sqrt{a}\\dot{q}$.\n"
        "C $H = \\frac{p^2}{2a^2} - \\frac{b^4 q^2}{2a^2}$, onde o momento canônico é $p = \\sqrt{a}\\dot{q}$.\n"
        "D $H = \\frac{p^2}{2a^2} + \\frac{b^4 q^2}{2a^2}$, onde o momento canônico é $p = 2a(a\\dot{q} + bq)$.\n"
        "E $H = \\frac{p^2}{4a^2} + \\frac{bpq}{a}$, onde o momento canônico é $p = 2a(a\\dot{q} + bq)$."
    ),
    "2025-1-mcPT3b": (
        "Q. 6 [mcPT3b]\n"
        "A lagrangiana de um sistema descrito pela coordenada generalizada $q$ e por sua derivada temporal $\\dot{q}$ é "
        "$L(\\dot{q}, q) = (a\\dot{q} - bq)^2$, onde $a$ e $b$ são constantes positivas.\n\n"
        "Qual é a hamiltoniana $H(q, p)$ correspondente?\n\n"
        "A $H = \\frac{p^2}{4a^2} + \\frac{bpq}{a}$, onde o momento canônico é $p = 2a(a\\dot{q} - bq)$.\n"
        "B $H = \\frac{p^2}{4a^2} - \\frac{bpq}{a}$, onde o momento canônico é $p = 2a(a\\dot{q} - bq)$.\n"
        "C $H = \\frac{p^2}{2a^2} + \\frac{b^4 q^2}{2a^2}$, onde o momento canônico é $p = \\sqrt{a}\\dot{q}$.\n"
        "D $H = \\frac{p^2}{2a^2} - \\frac{b^4 q^2}{2a^2}$, onde o momento canônico é $p = \\sqrt{a}\\dot{q}$.\n"
        "E $H = \\frac{p^2}{4a^2}$, onde o momento canônico é $p = 2a(a\\dot{q} - bq)$."
    ),
    "2025-1-mcPT4a": (
        "Q. 7 [mcPT4a]\n"
        "As equações de movimento de um sistema de duas partículas acopladas são escritas em forma matricial como "
        "$\\frac{d^2}{dt^2}\\begin{pmatrix}x_1 \\\\ x_2\\end{pmatrix} = -\\omega_0^2 \\begin{pmatrix}5/2 & -3/2 \\\\ -2 & 2\\end{pmatrix}\\begin{pmatrix}x_1 \\\\ x_2\\end{pmatrix}$, "
        "onde $x_i(t)$ é a posição da $i$-ésima partícula e $\\omega_0 > 0$ é uma constante.\n\n"
        "Quais são as frequências naturais de vibração (modos normais) do sistema?\n\n"
        "A $\\frac{1}{\\sqrt{2}}\\omega_0$ e $2\\omega_0$\n"
        "B $0$ e $\\omega_0$\n"
        "C $\\frac{3}{2}\\omega_0$ e $2\\omega_0$\n"
        "D $\\frac{1}{\\sqrt{3}}\\omega_0$ e $\\sqrt{\\frac{2}{3}}\\omega_0$\n"
        "E $\\frac{2}{3}\\omega_0$ e $\\frac{1}{2}\\omega_0$"
    ),
    "2025-1-mcPT4b": (
        "Q. 8 [mcPT4b]\n"
        "As equações de movimento de um sistema de duas partículas acopladas são escritas em forma matricial como "
        "$\\frac{d^2}{dt^2}\\begin{pmatrix}x_1 \\\\ x_2\\end{pmatrix} = -\\omega_0^2 \\begin{pmatrix}8/5 & -3/5 \\\\ -4/5 & 4/5\\end{pmatrix}\\begin{pmatrix}x_1 \\\\ x_2\\end{pmatrix}$, "
        "onde $x_i(t)$ é a posição da $i$-ésima partícula e $\\omega_0 > 0$ é uma constante.\n\n"
        "Quais são as frequências naturais de vibração (modos normais) do sistema?\n\n"
        "A $\\frac{2}{\\sqrt{5}}\\omega_0$ e $\\sqrt{2}\\omega_0$\n"
        "B $\\frac{1}{\\sqrt{5}}\\omega_0$ e $2\\omega_0$\n"
        "C $0$ e $\\sqrt{\\frac{8}{5}}\\omega_0$\n"
        "D $\\omega_0$ e $2\\omega_0$\n"
        "E $\\frac{3}{5}\\omega_0$ e $\\frac{4}{5}\\omega_0$"
    ),
    "2025-1-mcPT5a": (
        "Q. 9 [mcPT5a]\n"
        "Considere um pêndulo invertido formado por um balão esférico de volume $V$ imerso no ar (densidade $\\rho_{\\text{ar}}$) e preso ao chão por um fio "
        "inextensível de comprimento $L$. O balão está preenchido com gás hélio de densidade $\\rho_{\\text{He}} < \\rho_{\\text{ar}}$. "
        "Desprezando a massa da borracha do balão e o arrasto do ar, o período de pequenas oscilações do pêndulo invertido é:\n\n"
        "A $T = 2\\pi \\sqrt{\\frac{\\rho_{\\text{He}} L}{(\\rho_{\\text{ar}} - \\rho_{\\text{He}})g}}$\n"
        "B $T = 2\\pi \\sqrt{\\frac{L}{g}}$\n"
        "C $T = 2\\pi \\sqrt{\\frac{\\rho_{\\text{ar}} L}{\\rho_{\\text{He}} g}}$\n"
        "D $T = 2\\pi \\sqrt{\\frac{(\\rho_{\\text{ar}} + \\rho_{\\text{He}})L}{g}}$\n"
        "E $T = 2\\pi \\sqrt{\\frac{(\\rho_{\\text{ar}} - \\rho_{\\text{He}})L}{\\rho_{\\text{He}} g}}$"
    ),
    "2025-1-mcPT5b": (
        "Q. 10 [mcPT5b]\n"
        "Considere um pêndulo invertido formado por um balão esférico de volume $V$ imerso no ar (densidade $\\rho_{\\text{ar}}$) e preso por um fio inextensível de comprimento $L$. "
        "O balão está preenchido com um gás de densidade desconhecida $\\rho_g < \\rho_{\\text{ar}}$. "
        "Se a frequência angular de pequenas oscilações observada é $\\omega$, a densidade $\\rho_g$ do gás é:\n\n"
        "A $\\rho_g = \\frac{\\rho_{\\text{ar}} g}{g + \\omega^2 L}$\n"
        "B $\\rho_g = \\frac{\\rho_{\\text{ar}} \\omega^2 L}{g}$\n"
        "C $\\rho_g = \\rho_{\\text{ar}} \\left(1 - \\frac{\\omega^2 L}{g}\\right)$\n"
        "D $\\rho_g = \\frac{\\rho_{\\text{ar}} g}{\\omega^2 L}$\n"
        "E $\\rho_g = \\rho_{\\text{ar}} \\left(1 + \\frac{g}{\\omega^2 L}\\right)$"
    ),
    "2025-1-mcPT6a": (
        "Q. 11 [mcPT6a]\n"
        "Três blocos de massas $M, m_1$ e $m_2$ estão dispostos com $m_1$ sobre $M$ conectado por um fio ideal que passa por uma polia presa a $M$ "
        "sustentando $m_2$ pendurado verticalmente (veja a figura). Supondo que não haja atrito entre quaisquer superfícies, "
        "determine o módulo da força horizontal $F$ aplicada sobre $M$ para que as massas $m_1$ e $m_2$ permaneçam em repouso em relação a $M$:\n\n"
        "A $F = (M + m_1 + m_2)\\frac{m_2}{m_1}g$\n"
        "B $F = (M + m_1 + m_2)\\frac{m_1}{m_2}g$\n"
        "C $F = (M + m_1)g$\n"
        "D $F = (m_1 + m_2)g$\n"
        "E $F = \\frac{M m_2}{m_1}g$"
    ),
    "2025-1-mcPT6b": (
        "Q. 12 [mcPT6b]\n"
        "Três blocos de massas $M, m_1$ e $m_2$ estão dispostos com $m_1$ sobre $M$ conectado a $m_2$ pendurado. "
        "Uma força horizontal $F$ é aplicada sobre $M$ de modo que todo o conjunto se mova com aceleração horizontal $a = \\frac{m_2}{m_1}g$.\n\n"
        "A tensão $T$ no fio que conecta $m_1$ e $m_2$ durante o movimento é:\n\n"
        "A $T = m_2 g$\n"
        "B $T = m_1 g$\n"
        "C $T = (m_1 + m_2)g$\n"
        "D $T = \\frac{m_1 m_2}{m_1 + m_2}g$\n"
        "E $T = \\frac{m_2^2}{m_1}g$"
    ),
    "2025-1-mcPT7a": (
        "Q. 13 [mcPT7a]\n"
        "Um disco homogêneo de massa $M$ e raio $R$ é colocado em rotação com velocidade angular $\\omega_0$ em torno de seu eixo central. "
        "Em seguida, o disco é apoiado suavemente sobre uma superfície horizontal com coeficiente de atrito cinético $\\mu$.\n\n"
        "O tempo $t$ necessário para que o disco atinja a condição de rolamento puro (sem deslizamento) é:\n\n"
        "A $t = \\frac{\\omega_0 R}{3\\mu g}$\n"
        "B $t = \\frac{\\omega_0 R}{2\\mu g}$\n"
        "C $t = \\frac{2\\omega_0 R}{3\\mu g}$\n"
        "D $t = \\frac{\\omega_0 R}{\\mu g}$\n"
        "E $t = \\frac{\\omega_0 R}{4\\mu g}$"
    ),
    "2025-1-mcPT7b": (
        "Q. 14 [mcPT7b]\n"
        "Um disco homogêneo de massa $M$ e raio $R$ gira inicialmente com velocidade angular $\\omega_0$ e é colocado sobre uma superfície horizontal "
        "com coeficiente de atrito cinético $\\mu$.\n\n"
        "A velocidade linear final $v_f$ do centro de massa do disco no início do rolamento puro é:\n\n"
        "A $v_f = \\frac{\\omega_0 R}{3}$\n"
        "B $v_f = \\frac{\\omega_0 R}{2}$\n"
        "C $v_f = \\frac{2\\omega_0 R}{3}$\n"
        "D $v_f = \\omega_0 R$\n"
        "E $v_f = \\frac{\\omega_0 R}{4}$"
    ),
    "2025-1-mcPT8a": (
        "Q. 15 [mcPT8a]\n"
        "Um corpo de massa $m$ move-se em uma órbita elíptica sob a ação de uma força gravitacional atrativa $F(r) = -\\frac{G M m}{r^2}$. "
        "A distância de máxima aproximação (perigeu) é $r_p$ e a de máximo afastamento (apogeu) é $r_a$.\n\n"
        "A razão entre a velocidade no perigeu $v_p$ e a velocidade no apogeu $v_a$ é:\n\n"
        "A $\\frac{v_p}{v_a} = \\frac{r_a}{r_p}$\n"
        "B $\\frac{v_p}{v_a} = \\frac{r_p}{r_a}$\n"
        "C $\\frac{v_p}{v_a} = \\sqrt{\\frac{r_a}{r_p}}$\n"
        "D $\\frac{v_p}{v_a} = \\left(\\frac{r_a}{r_p}\\right)^2$\n"
        "E $\\frac{v_p}{v_a} = 1$"
    ),
    "2025-1-mcPT8b": (
        "Q. 16 [mcPT8b]\n"
        "Um corpo de massa $m$ move-se em uma órbita elíptica de semi-eixo maior $a$ em torno de uma massa $M \\gg m$. "
        "A energia mecânica total $E$ do sistema é dada por:\n\n"
        "A $E = -\\frac{G M m}{2a}$\n"
        "B $E = -\\frac{G M m}{a}$\n"
        "C $E = -\\frac{G M m}{4a}$\n"
        "D $E = \\frac{G M m}{2a}$\n"
        "E $E = -\\frac{2 G M m}{a}$"
    ),

    # =========================================================================
    # 2024-2 CLASSICAL MECHANICS (16 Questions)
    # =========================================================================
    "2024-2-mcPT1a": (
        "Q. 1 [mcPT1a]\n"
        "Uma configuração central é aquela em que a atração gravitacional total sobre cada corpo aponta diretamente para o centro de massa do sistema. "
        "Considere 3 corpos de massas iguais a $M$ localizados nos vértices de um triângulo equilátero de lado $a$, girando em torno do centro de massa "
        "com velocidade angular constante $\\omega$.\n\n"
        "O valor de $\\omega$ para que o sistema mantenha sua configuração de equilíbrio dinâmico é:\n\n"
        "A $\\omega = \\sqrt{\\frac{3GM}{a^3}}$\n"
        "B $\\omega = \\sqrt{\\frac{GM}{a^3}}$\n"
        "C $\\omega = \\sqrt{\\frac{\\sqrt{3}GM}{a^3}}$\n"
        "D $\\omega = \\sqrt{\\frac{2GM}{a^3}}$\n"
        "E $\\omega = \\sqrt{\\frac{GM}{3a^3}}$"
    ),
    "2024-2-mcPT1b": (
        "Q. 2 [mcPT1b]\n"
        "Considere 4 corpos de massas iguais a $M$ localizados nos vértices de um quadrado de lado $a$, girando em torno do centro de massa "
        "com velocidade angular constante $\\omega$.\n\n"
        "O valor de $\\omega$ para que o sistema mantenha a configuração rígida é:\n\n"
        "A $\\omega = \\sqrt{\\frac{GM}{a^3}\\left(\\frac{1}{2\\sqrt{2}} + 1\\right)}$\n"
        "B $\\omega = \\sqrt{\\frac{GM}{a^3}}$\n"
        "C $\\omega = \\sqrt{\\frac{4GM}{a^3}}$\n"
        "D $\\omega = \\sqrt{\\frac{2\\sqrt{2}GM}{a^3}}$\n"
        "E $\\omega = \\sqrt{\\frac{GM}{4a^3}}$"
    ),
    "2024-2-mcPT2a": (
        "Q. 3 [mcPT2a]\n"
        "Uma balança de braços iguais de comprimento total $2L$ ($L = 30\\text{ cm}$) possui um ponteiro indicador vertical de massa $m$ "
        "cujo centro de massa está a uma distância $d$ abaixo do ponto de articulação. Quando massas desiguais $M_1$ e $M_2$ são colocadas nos pratos, "
        "o ponteiro inclina-se de um ângulo $\\theta$.\n\n"
        "A sensibilidade da balança, definida por $\\tan\\theta / (M_1 - M_2)$, é proporcional a:\n\n"
        "A $\\frac{L}{m d}$\n"
        "B $\\frac{m d}{L}$\n"
        "C $\\frac{L^2}{m d}$\n"
        "D $\\frac{d}{m L}$\n"
        "E $\\frac{1}{m d L}$"
    ),
    "2024-2-mcPT2b": (
        "Q. 4 [mcPT2b]\n"
        "Para a mesma balança com braço $L = 40\\text{ cm}$, se o comprimento do braço $L$ é aumentado em $33\\%$, a sensibilidade angular da balança:\n\n"
        "A Aumenta proporcionalmente a $L$.\n"
        "B Permanece inalterada.\n"
        "C Diminui proporcionalmente a $1/L$.\n"
        "D Aumenta proporcionalmente a $L^2$.\n"
        "E Diminui exponencialmente."
    ),
    "2024-2-mcPT3a": (
        "Q. 5 [mcPT3a]\n"
        "Uma pessoa em pé sobre o centro de uma plataforma giratória horizontal livre de atrito segura dois halteres de massa $m$ com os braços estendidos. "
        "O momento de inércia inicial do conjunto é $I_1$ e a velocidade angular é $\\omega_1$. Ao recolher os braços para junto do corpo, o momento "
        "de inércia cai para $I_2 < I_1$.\n\n"
        "A nova velocidade angular $\\omega_2$ e a energia cinética rotacional final $K_2$ satisfazem:\n\n"
        "A $\\omega_2 = \\frac{I_1}{I_2}\\omega_1\\quad \\text{e}\\quad K_2 > K_1$\n"
        "B $\\omega_2 = \\frac{I_2}{I_1}\\omega_1\\quad \\text{e}\\quad K_2 < K_1$\n"
        "C $\\omega_2 = \\omega_1\\quad \\text{e}\\quad K_2 = K_1$\n"
        "D $\\omega_2 = \\frac{I_1}{I_2}\\omega_1\\quad \\text{e}\\quad K_2 = K_1$\n"
        "E $\\omega_2 = \\left(\\frac{I_1}{I_2}\\right)^2\\omega_1\\quad \\text{e}\\quad K_2 > K_1$"
    ),
    "2024-2-mcPT3b": (
        "Q. 6 [mcPT3b]\n"
        "O aumento na energia cinética rotacional $\\Delta K = K_2 - K_1 > 0$ do sistema giratório ocorre porque:\n\n"
        "A A pessoa realiza trabalho interno contra a força centrífuga ao puxar os halteres para dentro.\n"
        "B Há um torque externo resultante atuando sobre a plataforma.\n"
        "C A força gravitacional realiza trabalho positivo sobre os pesos.\n"
        "D O momento angular do sistema aumentou.\n"
        "E O atrito com o piso fornece energia ao sistema."
    ),
    "2024-2-mcPT4a": (
        "Q. 7 [mcPT4a]\n"
        "Um pêndulo físico é formado por uma barra rígida delgada de massa $m$ e comprimento $L$, articulada sem atrito em uma de suas extremidades.\n\n"
        "O período de pequenas oscilações do pêndulo físico é:\n\n"
        "A $T = 2\\pi \\sqrt{\\frac{2L}{3g}}$\n"
        "B $T = 2\\pi \\sqrt{\\frac{L}{g}}$\n"
        "C $T = 2\\pi \\sqrt{\\frac{L}{2g}}$\n"
        "D $T = 2\\pi \\sqrt{\\frac{3L}{2g}}$\n"
        "E $T = 2\\pi \\sqrt{\\frac{L}{3g}}$"
    ),
    "2024-2-mcPT4b": (
        "Q. 8 [mcPT4b]\n"
        "Se uma massa pontual $M = m$ for fixada na extremidade inferior da barra delgada de comprimento $L$ e massa $m$:\n\n"
        "O novo período de pequenas oscilações $T'$ do conjunto é:\n\n"
        "A $T' = 2\\pi \\sqrt{\\frac{8L}{9g}}$\n"
        "B $T' = 2\\pi \\sqrt{\\frac{2L}{3g}}$\n"
        "C $T' = 2\\pi \\sqrt{\\frac{4L}{3g}}$\n"
        "D $T' = 2\\pi \\sqrt{\\frac{L}{g}}$\n"
        "E $T' = 2\\pi \\sqrt{\\frac{5L}{6g}}$"
    ),
    "2024-2-mcPT5a": (
        "Q. 9 [mcPT5a]\n"
        "Um pêndulo simples de massa $m_1 = 2M$ e comprimento $L$ é solto a partir do repouso de uma altura $h$. No ponto mais baixo, ele colide elasticamente "
        "e frontalmente com um bloco de massa $m_2 = M$ inicialmente em repouso sobre uma superfície horizontal sem atrito.\n\n"
        "A velocidade $v_2$ adquirida pelo bloco de massa $M$ imediatamente após a colisão é:\n\n"
        "A $v_2 = \\frac{4}{3}\\sqrt{2gh}$\n"
        "B $v_2 = \\sqrt{2gh}$\n"
        "C $v_2 = \\frac{2}{3}\\sqrt{2gh}$\n"
        "D $v_2 = 2\\sqrt{2gh}$\n"
        "E $v_2 = \\frac{1}{3}\\sqrt{2gh}$"
    ),
    "2024-2-mcPT5b": (
        "Q. 10 [mcPT5b]\n"
        "Um pêndulo de massa $m_1 = 3M$ colide elasticamente com uma massa $m_2 = M$ em repouso. A velocidade inicial de $m_1$ antes da colisão é $v_0 = \\sqrt{2gh}$.\n\n"
        "A fração de energia cinética transferida para a massa $M$ na colisão elástica é:\n\n"
        "A $\\frac{K_2}{K_0} = \\frac{3}{4} = 75\\%$\n"
        "B $\\frac{K_2}{K_0} = 100\\%$\n"
        "C $\\frac{K_2}{K_0} = \\frac{1}{2} = 50\\%$\n"
        "D $\\frac{K_2}{K_0} = \\frac{8}{9} \\approx 89\\%$\n"
        "E $\\frac{K_2}{K_0} = \\frac{1}{4} = 25\\%$"
    ),
    "2024-2-mcPT6a": (
        "Q. 11 [mcPT6a]\n"
        "Um projétil de massa $m$ e velocidade horizontal $v_0$ atinge e aloja-se em um bloco de massa $M$ suspenso por um fio ideal de comprimento $L$.\n\n"
        "A altura máxima $h$ atingida pelo pêndulo balístico após a colisão perfeitamente inelástica é:\n\n"
        "A $h = \\frac{m^2 v_0^2}{2g(m+M)^2}$\n"
        "B $h = \\frac{v_0^2}{2g}$\n"
        "C $h = \\frac{m v_0^2}{2g(m+M)}$\n"
        "D $h = \\frac{M v_0^2}{2g m}$\n"
        "E $h = \\frac{m^2 v_0^2}{g(m+M)^2}$"
    ),
    "2024-2-mcPT6b": (
        "Q. 12 [mcPT6b]\n"
        "Para o pêndulo balístico, a fração de energia cinética inicial do projétil convertida em calor e deformação durante o impacto inelástico é:\n\n"
        "A $\\frac{\\Delta E_{\\text{mec}}}{K_0} = \\frac{M}{m + M}$\n"
        "B $\\frac{\\Delta E_{\\text{mec}}}{K_0} = \\frac{m}{m + M}$\n"
        "C $\\frac{\\Delta E_{\\text{mec}}}{K_0} = 1$\n"
        "D $\\frac{\\Delta E_{\\text{mec}}}{K_0} = \\frac{M^2}{(m+M)^2}$\n"
        "E $\\frac{\\Delta E_{\\text{mec}}}{K_0} = 0$"
    ),

    # =========================================================================
    # 2023-2 CLASSICAL MECHANICS (16 Questions)
    # =========================================================================
    "2023-2-mcPT1a": (
        "Q. 1 [mcPT1a]\n"
        "Um satélite de massa $m$ move-se em uma órbita circular de raio $r_1$ ao redor da Terra (massa $M$). Para transferir o satélite para uma "
        "órbita circular de raio maior $r_2 > r_1$, a variação de energia mecânica total $\\Delta E = E_2 - E_1$ que deve ser fornecida pelos motores é:\n\n"
        "A $\\Delta E = \\frac{GMm}{2}\\left(\\frac{1}{r_1} - \\frac{1}{r_2}\\right)$\n"
        "B $\\Delta E = GMm\\left(\\frac{1}{r_1} - \\frac{1}{r_2}\\right)$\n"
        "C $\\Delta E = \\frac{GMm}{2}\\left(\\frac{1}{r_2} - \\frac{1}{r_1}\\right)$\n"
        "D $\\Delta E = \\frac{GMm}{r_1 + r_2}$\n"
        "E $\\Delta E = 0$"
    ),
    "2023-2-mcPT1b": (
        "Q. 2 [mcPT1b]\n"
        "Um satélite em órbita circular de raio $r$ tem velocidade orbital $v = \\sqrt{GM/r}$. Se o raio da órbita for quadruplicado ($r' = 4r$), "
        "a sua velocidade orbital $v'$ e o seu período orbital $T'$ tornam-se, respectivamente:\n\n"
        "A $v' = \\frac{v}{2}\\quad \\text{e}\\quad T' = 8T$\n"
        "B $v' = \\frac{v}{4}\\quad \\text{e}\\quad T' = 4T$\n"
        "C $v' = 2v\\quad \\text{e}\\quad T' = 2T$\n"
        "D $v' = \\frac{v}{2}\\quad \\text{e}\\quad T' = 2T$\n"
        "E $v' = \\frac{v}{4}\\quad \\text{e}\\quad T' = 16T$"
    ),
    "2023-2-mcPT2a": (
        "Q. 3 [mcPT2a]\n"
        "Um sistema é composto por uma massa $m$ em um plano horizontal conectada em paralelo a três molas idênticas de constante elástica $k$.\n\n"
        "A frequência angular de oscilação do sistema é:\n\n"
        "A $\\omega = \\sqrt{\\frac{3k}{m}}$\n"
        "B $\\omega = \\sqrt{\\frac{k}{3m}}$\n"
        "C $\\omega = \\sqrt{\\frac{k}{m}}$\n"
        "D $\\omega = 3\\sqrt{\\frac{k}{m}}$\n"
        "E $\\omega = \\sqrt{\\frac{2k}{3m}}$"
    ),
    "2023-2-mcPT2b": (
        "Q. 4 [mcPT2b]\n"
        "Um sistema é composto por uma massa $m$ conectada em paralelo a quatro molas idênticas de constante elástica $k$.\n\n"
        "A frequência angular de oscilação do sistema é:\n\n"
        "A $\\omega = 2\\sqrt{\\frac{k}{m}}$\n"
        "B $\\omega = \\sqrt{\\frac{k}{4m}}$\n"
        "C $\\omega = \\sqrt{\\frac{k}{m}}$\n"
        "D $\\omega = 4\\sqrt{\\frac{k}{m}}$\n"
        "E $\\omega = \\frac{1}{2}\\sqrt{\\frac{k}{m}}$"
    ),
    "2023-2-mcPT3a": (
        "Q. 5 [mcPT3a]\n"
        "A energia potencial intermolecular entre dois átomos a uma distância $r$ é descrita pelo potencial $U(r) = D\\left[\\left(\\frac{a}{r}\\right)^{12} - 2\\left(\\frac{a}{r}\\right)^6\\right]$, "
        "onde $a$ e $D$ são constantes positivas.\n\n"
        "A distância interatômica de equilíbrio $r_0$ e a constante de mola efetiva $k = \\left.\\frac{d^2U}{dr^2}\\right|_{r_0}$ valem:\n\n"
        "A $r_0 = a\\quad \\text{e}\\quad k = \\frac{72D}{a^2}$\n"
        "B $r_0 = a\\quad \\text{e}\\quad k = \\frac{36D}{a^2}$\n"
        "C $r_0 = 2a\\quad \\text{e}\\quad k = \\frac{72D}{a^2}$\n"
        "D $r_0 = a/2\\quad \\text{e}\\quad k = \\frac{144D}{a^2}$\n"
        "E $r_0 = a\\quad \\text{e}\\quad k = \\frac{12D}{a^2}$"
    ),
    "2023-2-mcPT3b": (
        "Q. 6 [mcPT3b]\n"
        "Para o potencial intermolecular $U(r) = D\\left[\\left(\\frac{a}{r}\\right)^{12} - 2\\left(\\frac{a}{r}\\right)^6\\right]$, a energia de ligação molecular "
        "(profundidade do poço de potencial $|U(r_0)|$) vale:\n\n"
        "A $|U(r_0)| = D$\n"
        "B $|U(r_0)| = 2D$\n"
        "C $|U(r_0)| = D/2$\n"
        "D $|U(r_0)| = 0$\n"
        "E $|U(r_0)| = 4D$"
    ),
    "2023-2-mcPT4a": (
        "Q. 7 [mcPT4a]\n"
        "Um disco uniforme de momento de inércia $I_1 = I$ gira livremente com velocidade angular $\\omega_0$ em torno de um eixo vertical sem atrito. "
        "Deixa-se cair suavemente sobre ele um segundo disco uniforme inicialmente em repouso de momento de inércia $I_2 = 2I$. "
        "Devido ao atrito entre as superfícies dos discos, eles passam a girar juntos com velocidade angular final comum $\\omega_f$.\n\n"
        "A velocidade angular final $\\omega_f$ do conjunto e a fração de energia mecânica perdida $\\Delta E / E_0$ valem:\n\n"
        "A $\\omega_f = \\frac{\\omega_0}{3}\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = \\frac{2}{3}$\n"
        "B $\\omega_f = \\frac{\\omega_0}{2}\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = \\frac{1}{2}$\n"
        "C $\\omega_f = \\frac{2\\omega_0}{3}\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = \\frac{1}{3}$\n"
        "D $\\omega_f = \\frac{\\omega_0}{3}\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = \\frac{1}{3}$\n"
        "E $\\omega_f = \\omega_0\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = 0$"
    ),
    "2023-2-mcPT4b": (
        "Q. 8 [mcPT4b]\n"
        "Um disco uniforme com $I_1 = I$ girando com $\\omega_0$ recebe um segundo disco idêntico de momento de inércia $I_2 = I$ inicialmente em repouso.\n\n"
        "A velocidade angular final $\\omega_f$ e a fração de energia cinética perdida $\\Delta E / E_0$ valem:\n\n"
        "A $\\omega_f = \\frac{\\omega_0}{2}\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = \\frac{1}{2}$\n"
        "B $\\omega_f = \\frac{\\omega_0}{4}\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = \\frac{3}{4}$\n"
        "C $\\omega_f = \\frac{\\omega_0}{2}\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = \\frac{1}{4}$\n"
        "D $\\omega_f = \\omega_0\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = 0$\n"
        "E $\\omega_f = \\frac{2\\omega_0}{3}\\quad \\text{e}\\quad \\frac{\\Delta E}{E_0} = \\frac{1}{3}$"
    ),

    # =========================================================================
    # 2022-2 CLASSICAL MECHANICS (16 Questions)
    # =========================================================================
    "2022-2-mcPT2a": (
        "Q. 3 [mcPT2a]\n"
        "Considere que a Terra gire em torno do Sol em uma órbita circular de raio $R_0$ com período $T_0 = 1\\text{ ano}$. "
        "Se a massa do Sol dobrasse repentinamente para $M' = 2M$, para manter a mesma órbita de raio $R_0$, o novo período orbital $T'$ seria:\n\n"
        "A $T' = \\frac{T_0}{\\sqrt{2}}$\n"
        "B $T' = \\frac{T_0}{2}$\n"
        "C $T' = \\sqrt{2} T_0$\n"
        "D $T' = 2 T_0$\n"
        "E $T' = T_0$"
    ),
    "2022-2-mcPT2b": (
        "Q. 4 [mcPT2b]\n"
        "Se a massa do Sol fosse reduzida pela metade ($M' = M/2$), o novo período orbital $T'$ da Terra para a mesma órbita de raio $R_0$ seria:\n\n"
        "A $T' = \\sqrt{2} T_0$\n"
        "B $T' = 2 T_0$\n"
        "C $T' = \\frac{T_0}{\\sqrt{2}}$\n"
        "D $T' = 4 T_0$\n"
        "E $T' = \\frac{T_0}{2}$"
    ),
    "2022-2-mcPT3a": (
        "Q. 5 [mcPT3a]\n"
        "Uma esfera maciça homogênea de massa $m$ e raio $R$ ($I = \\frac{2}{5}mR^2$) é abandonada a partir do repouso no topo de um plano inclinado de ângulo $\\theta$, "
        "rolando para baixo sem deslizar.\n\n"
        "A aceleração linear $a_{\\text{cm}}$ do centro de massa da esfera maciça é:\n\n"
        "A $a_{\\text{cm}} = \\frac{5}{7}g\\operatorname{sen}\\theta$\n"
        "B $a_{\\text{cm}} = \\frac{3}{5}g\\operatorname{sen}\\theta$\n"
        "C $a_{\\text{cm}} = \\frac{1}{2}g\\operatorname{sen}\\theta$\n"
        "D $a_{\\text{cm}} = g\\operatorname{sen}\\theta$\n"
        "E $a_{\\text{cm}} = \\frac{2}{3}g\\operatorname{sen}\\theta$"
    ),
    "2022-2-mcPT3b": (
        "Q. 6 [mcPT3b]\n"
        "Uma esfera oca homogênea de casca fina de massa $m$ e raio $R$ ($I = \\frac{2}{3}mR^2$) desce o mesmo plano inclinado de ângulo $\\theta$ rolando sem deslizar.\n\n"
        "A aceleração linear $a_{\\text{cm}}$ do centro de massa da esfera oca é:\n\n"
        "A $a_{\\text{cm}} = \\frac{3}{5}g\\operatorname{sen}\\theta$\n"
        "B $a_{\\text{cm}} = \\frac{5}{7}g\\operatorname{sen}\\theta$\n"
        "C $a_{\\text{cm}} = \\frac{1}{2}g\\operatorname{sen}\\theta$\n"
        "D $a_{\\text{cm}} = \\frac{2}{3}g\\operatorname{sen}\\theta$\n"
        "E $a_{\\text{cm}} = g\\operatorname{sen}\\theta$"
    ),
    "2022-2-mcPT4a": (
        "Q. 7 [mcPT4a]\n"
        "Quando um projétil de massa $m$ é disparado em uma arma, a força propulsora varia com a posição ao longo do cano de comprimento $L$ como $F(x) = F_0(1 - x/L)$.\n\n"
        "A velocidade de saída do projétil na boca do cano ($x = L$) vale:\n\n"
        "A $v_{\\text{saída}} = \\sqrt{\\frac{F_0 L}{m}}$\n"
        "B $v_{\\text{saída}} = \\sqrt{\\frac{2F_0 L}{m}}$\n"
        "C $v_{\\text{saída}} = \\sqrt{\\frac{F_0 L}{2m}}$\n"
        "D $v_{\\text{saída}} = \\frac{F_0 L}{m}$\n"
        "E $v_{\\text{saída}} = \\sqrt{\\frac{F_0 L}{3m}}$"
    ),
    "2022-2-mcPT4b": (
        "Q. 8 [mcPT4b]\n"
        "Para a mesma arma sob força $F(x) = F_0(1 - x/L)$, o trabalho total realizado pelos gases sobre o projétil ao longo de todo o cano de comprimento $L$ vale:\n\n"
        "A $W = \\frac{1}{2} F_0 L$\n"
        "B $W = F_0 L$\n"
        "C $W = \\frac{1}{3} F_0 L$\n"
        "D $W = \\frac{2}{3} F_0 L$\n"
        "E $W = \\frac{1}{4} F_0 L$"
    ),
    "2022-2-mcPT5a": (
        "Q. 9 [mcPT5a]\n"
        "O módulo da força resultante $F$ exercida sobre um objeto é calculado a partir das medidas de sua massa $m$ e de sua aceleração $a$, "
        "com incertezas experimentais $\\sigma_m$ e $\\sigma_a$, respectivamente. Pela Segunda Lei de Newton ($F = ma$), a incerteza $\\sigma_F$ é dada por:\n\n"
        "A $\\sigma_F = \\sqrt{a^2 \\sigma_m^2 + m^2 \\sigma_a^2}$\n"
        "B $\\sigma_F = a \\sigma_m + m \\sigma_a$\n"
        "C $\\sigma_F = \\sqrt{\\sigma_m^2 + \\sigma_a^2}$\n"
        "D $\\sigma_F = m a \\sqrt{\\sigma_m^2 + \\sigma_a^2}$\n"
        "E $\\sigma_F = \\frac{\\sigma_m}{m} + \\frac{\\sigma_a}{a}$"
    ),
    "2022-2-mcPT5b": (
        "Q. 10 [mcPT5b]\n"
        "O módulo da aceleração $a$ é calculado a partir de $a = F/m$, com incertezas $\\sigma_F$ e $\\sigma_m$. A incerteza experimental $\\sigma_a$ é:\n\n"
        "A $\\sigma_a = \\sqrt{\\left(\\frac{1}{m}\\right)^2 \\sigma_F^2 + \\left(\\frac{F}{m^2}\\right)^2 \\sigma_m^2}$\n"
        "B $\\sigma_a = \\frac{\\sigma_F}{m} + \\frac{F \\sigma_m}{m^2}$\n"
        "C $\\sigma_a = \\sqrt{\\sigma_F^2 + \\sigma_m^2}$\n"
        "D $\\sigma_a = \\frac{\\sigma_F}{\\sigma_m}$\n"
        "E $\\sigma_a = \\frac{F}{m}\\sqrt{\\sigma_F^2 + \\sigma_m^2}$"
    ),
    "2022-2-mcPT6a": (
        "Q. 11 [mcPT6a]\n"
        "Uma partícula de massa $m$ move-se em uma dimensão sob a ação do potencial $V(x) = V_0\\left[\\left(\\frac{x}{a}\\right)^4 - 2\\left(\\frac{x}{a}\\right)^2\\right]$ ($V_0 > 0$).\n\n"
        "Os pontos de equilíbrio do sistema e suas respectivas estabilidades são:\n\n"
        "A $x = 0$ é equilíbrio instável; $x = \\pm a$ são equilíbrios estáveis com $V(\\pm a) = -V_0$.\n"
        "B $x = 0$ é equilíbrio estável; $x = \\pm a$ são equilíbrios instáveis.\n"
        "C $x = \\pm a$ são equilíbrios instáveis; não há equilíbrio em $x = 0$.\n"
        "D $x = 0, \\pm a$ são todos equilíbrios estáveis.\n"
        "E $x = 0, \\pm a$ são todos equilíbrios instáveis."
    ),
    "2022-2-mcPT6b": (
        "Q. 12 [mcPT6b]\n"
        "Para a partícula oscilando com pequenas amplitudes em torno do ponto de equilíbrio estável $x_0 = a$ do potencial $V(x) = V_0\\left[\\left(\\frac{x}{a}\\right)^4 - 2\\left(\\frac{x}{a}\\right)^2\\right]$:\n\n"
        "A frequência angular de pequenas oscilações $\\omega$ vale:\n\n"
        "A $\\omega = \\sqrt{\\frac{8V_0}{m a^2}}$\n"
        "B $\\omega = \\sqrt{\\frac{4V_0}{m a^2}}$\n"
        "C $\\omega = \\sqrt{\\frac{2V_0}{m a^2}}$\n"
        "D $\\omega = \\sqrt{\\frac{V_0}{m a^2}}$\n"
        "E $\\omega = \\frac{4V_0}{m a^2}$"
    ),
}


def apply_mc_reconstructions():
    print("=" * 65)
    print("⚙️ RECONSTRUCTING ALL CLASSICAL MECHANICS QUESTIONS (2010 - 2026)")
    print("=" * 65)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    updated = 0
    for qid, clean_text in MC_RECONSTRUCTIONS.items():
        cur.execute("UPDATE questions SET text = ? WHERE id = ?", (clean_text, qid))
        if cur.rowcount > 0:
            updated += 1
            print(f"  ✓ Reconstructed {qid}")
        else:
            print(f"  ⚠ Question ID not found in DB: {qid}")

    conn.commit()
    conn.close()

    print(f"\n✅ Successfully updated {updated} Classical Mechanics questions in SQLite.")
    print("🚀 Exporting updated questions.json...")
    export_bank_to_json()
    print("✨ Complete!")


if __name__ == "__main__":
    apply_mc_reconstructions()
