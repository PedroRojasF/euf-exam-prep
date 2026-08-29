"""EUF Electromagnetism Master Reconstruction Module.
Provides high-fidelity, peer-reviewed LaTeX transcriptions and clean multiple choice options
for Electromagnetism questions across the EUF database (2022 to 2026).
"""

import os
import sys
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bank.exporter import export_bank_to_json

DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")

EM_RECONSTRUCTIONS = {
    # =========================================================================
    # 2026-1 ELECTROMAGNETISM (16 Questions: emPT1a to emPT8b)
    # =========================================================================
    "2026-1-emPT1a": (
        "Q. 17 [emPT1a]\n"
        "Considere um anel fino de raio $R$, uniformemente carregado com carga total $Q > 0$, "
        "fixo no plano $xy$ e centrado na origem do sistema de coordenadas. Uma partícula de massa $m$ e carga $q_0 > 0$ "
        "é colocada sobre o eixo $z$, ao longo do eixo de simetria do sistema, a uma altura $z$ acima do centro do anel. "
        "Além da força elétrica exercida pelo anel sobre a partícula, atua também a força peso, associada à aceleração da gravidade $g$, "
        "dirigida no sentido negativo do eixo $z$.\n\n"
        "Sabendo que a partícula está posicionada a uma altura igual ao raio do anel, isto é, $z = R$, "
        "qual deve ser o valor da massa $m$ para que a partícula permaneça em equilíbrio nessa posição?\n\n"
        "A $m = \\frac{q_0 Q}{8\\sqrt{2}\\pi\\varepsilon_0 g R^2}$\n"
        "B $m = \\frac{q_0 Q}{4\\sqrt{2}\\pi\\varepsilon_0 g R^2}$\n"
        "C $m = \\frac{q_0 Q}{8\\sqrt{3}\\pi\\varepsilon_0 g R^2}$\n"
        "D $m = \\frac{q_0 Q}{4\\pi\\varepsilon_0 g R^2}$\n"
        "E $m = \\frac{q_0 Q}{2\\sqrt{2}\\pi\\varepsilon_0 g R^2}$"
    ),
    "2026-1-emPT1b": (
        "Q. 18 [emPT1b]\n"
        "Considere um anel fino de raio $R$, uniformemente carregado com carga total $Q > 0$, "
        "fixo no plano $xy$ e centrado na origem do sistema de coordenadas. Uma partícula de massa $m$ e carga $q_0 > 0$ "
        "é colocada sobre o eixo $z$, ao longo do eixo de simetria do sistema, a uma altura $z$ acima do centro do anel. "
        "Além da força elétrica exercida pelo anel sobre a partícula, atua também a força peso, associada à aceleração da gravidade $g$, "
        "dirigida no sentido negativo do eixo $z$.\n\n"
        "Sabendo que a partícula está posicionada a uma altura igual a metade do raio do anel, isto é, $z = R/2$, "
        "qual deve ser o valor da massa $m$ para que a partícula permaneça em equilíbrio nessa posição?\n\n"
        "A $m = \\frac{q_0 Q}{5\\sqrt{5}\\pi\\varepsilon_0 g R^2}$\n"
        "B $m = \\frac{q_0 Q}{8\\sqrt{5}\\pi\\varepsilon_0 g R^2}$\n"
        "C $m = \\frac{q_0 Q}{10\\sqrt{3}\\pi\\varepsilon_0 g R^2}$\n"
        "D $m = \\frac{q_0 Q}{8\\pi\\varepsilon_0 g R^2}$\n"
        "E $m = \\frac{q_0 Q}{4\\sqrt{3}\\pi\\varepsilon_0 g R^2}$"
    ),
    "2026-1-emPT2a": (
        "Q. 19 [emPT2a]\n"
        "Duas cascas cilíndricas longas e concêntricas possuem raios $a$ e $b$, sendo $b > a$. "
        "A casca interna possui uma densidade linear de carga igual a $\\lambda$, enquanto a casca externa possui uma densidade linear de carga igual a $-\\lambda$.\n\n"
        "Determine a diferença de potencial elétrico entre as cascas, definida por $\\Delta V = V(b) - V(a)$, no caso em que $b = 2a$.\n\n"
        "A $\\Delta V = -\\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln 2$\n"
        "B $\\Delta V = \\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln 2$\n"
        "C $\\Delta V = -\\frac{\\lambda}{4\\pi\\varepsilon_0}\\ln 2$\n"
        "D $\\Delta V = -\\frac{\\lambda}{\\varepsilon_0}\\ln 2$\n"
        "E $\\Delta V = 0$"
    ),
    "2026-1-emPT2b": (
        "Q. 20 [emPT2b]\n"
        "Duas cascas cilíndricas longas e concêntricas possuem raios $a$ e $b$, sendo $b > a$. "
        "A casca interna possui uma densidade linear de carga igual a $\\lambda$, enquanto a casca externa possui uma densidade linear de carga igual a $-\\lambda$.\n\n"
        "Determine a diferença de potencial elétrico entre as cascas, definida por $\\Delta V = V(b) - V(a)$, no caso em que $b = 3a$.\n\n"
        "A $\\Delta V = -\\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln 3$\n"
        "B $\\Delta V = \\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln 3$\n"
        "C $\\Delta V = -\\frac{\\lambda}{4\\pi\\varepsilon_0}\\ln 3$\n"
        "D $\\Delta V = -\\frac{\\lambda}{\\varepsilon_0}\\ln 3$\n"
        "E $\\Delta V = 0$"
    ),
    "2026-1-emPT3a": (
        "Q. 21 [emPT3a]\n"
        "Uma carga puntiforme $Q$ está fixa na origem de um sistema de coordenadas. "
        "Considere uma superfície esférica de raio $R$, também centrada na origem.\n\n"
        "Qual é o fluxo de campo elétrico, $\\Phi_E$, que atravessa a porção da superfície esférica que corresponde, "
        "em coordenadas esféricas $(r, \\theta, \\phi)$, à região angular definida por $\\alpha \\le \\theta \\le \\beta$ e $0 \\le \\phi \\le 2\\pi$, "
        "onde $\\alpha = 0$ e $\\beta = \\pi/4$?\n\n"
        "A $\\Phi_E = \\frac{Q}{2\\varepsilon_0}\\left(1 - \\frac{\\sqrt{2}}{2}\\right)$\n"
        "B $\\Phi_E = \\frac{Q}{4\\pi\\varepsilon_0}$\n"
        "C $\\Phi_E = \\frac{Q}{2\\varepsilon_0}$\n"
        "D $\\Phi_E = \\frac{Q}{4\\varepsilon_0}$\n"
        "E $\\Phi_E = \\frac{Q}{\\varepsilon_0}\\left(1 - \\frac{\\sqrt{2}}{2}\\right)$"
    ),
    "2026-1-emPT3b": (
        "Q. 22 [emPT3b]\n"
        "Uma carga puntiforme $Q$ está fixa na origem de um sistema de coordenadas. "
        "Considere uma superfície esférica de raio $R$, também centrada na origem.\n\n"
        "Qual é o fluxo de campo elétrico, $\\Phi_E$, que atravessa a porção da superfície esférica que corresponde, "
        "em coordenadas esféricas $(r, \\theta, \\phi)$, à região angular definida por $\\alpha \\le \\theta \\le \\beta$ e $0 \\le \\phi \\le 2\\pi$, "
        "onde $\\alpha = 0$ e $\\beta = \\pi/6$?\n\n"
        "A $\\Phi_E = \\frac{Q}{2\\varepsilon_0}\\left(1 - \\frac{\\sqrt{3}}{2}\\right)$\n"
        "B $\\Phi_E = \\frac{Q}{4\\pi\\varepsilon_0}$\n"
        "C $\\Phi_E = \\frac{Q}{2\\varepsilon_0}$\n"
        "D $\\Phi_E = \\frac{Q}{4\\varepsilon_0}$\n"
        "E $\\Phi_E = \\frac{Q}{\\varepsilon_0}\\left(1 - \\frac{\\sqrt{3}}{2}\\right)$"
    ),
    "2026-1-emPT4a": (
        "Q. 23 [emPT4a]\n"
        "O campo elétrico de uma onda eletromagnética plana, no vácuo, propagando-se na direção $+z$, é dado por "
        "$\\vec{E}(z,t) = E_0 \\cos(\\omega t - kz)\\hat{x}$.\n\n"
        "Qual é o valor de $\\langle S \\rangle$, a média temporal do módulo do vetor de Poynting?\n\n"
        "A $\\langle S \\rangle = \\frac{E_0^2}{2\\mu_0 c}$\n"
        "B $\\langle S \\rangle = \\frac{E_0^2}{\\mu_0 c}$\n"
        "C $\\langle S \\rangle = \\frac{E_0^2}{4\\mu_0 c}$\n"
        "D $\\langle S \\rangle = \\frac{E_0^2}{2\\pi\\mu_0 c}$\n"
        "E $\\langle S \\rangle = \\frac{c E_0^2}{2\\mu_0}$"
    ),
    "2026-1-emPT4b": (
        "Q. 24 [emPT4b]\n"
        "O campo magnético de uma onda eletromagnética plana, no vácuo, propagando-se na direção $+z$, é dado por "
        "$\\vec{B}(z,t) = B_0 \\cos(\\omega t - kz)\\hat{y}$.\n\n"
        "Qual é o valor de $\\langle S \\rangle$, a média temporal do módulo do vetor de Poynting?\n\n"
        "A $\\langle S \\rangle = \\frac{c B_0^2}{2\\mu_0}$\n"
        "B $\\langle S \\rangle = \\frac{c B_0^2}{\\mu_0}$\n"
        "C $\\langle S \\rangle = \\frac{c B_0^2}{4\\mu_0}$\n"
        "D $\\langle S \\rangle = \\frac{c B_0^2}{2\\pi\\mu_0}$\n"
        "E $\\langle S \\rangle = \\frac{B_0^2}{2\\mu_0 c}$"
    ),
    "2026-1-emPT5a": (
        "Q. 25 [emPT5a]\n"
        "Considere um cilindro que carrega uma magnetização permanente paralela à direção de seu eixo de simetria. "
        "Denotando a direção deste eixo por $\\hat{z}$, podemos escrever $\\vec{M} = M_0 \\hat{z}$.\n\n"
        "As densidades de correntes ligadas na superfície ($\\vec{K}_M$) e no volume ($\\vec{J}_M$) associadas a essa magnetização são dadas por:\n\n"
        "A $\\vec{K}_M = M_0\\hat{\\phi}$ na superfície lateral do cilindro e $\\vec{J}_M = 0$ em todo o volume do cilindro.\n"
        "B $\\vec{K}_M = -M_0\\hat{z}$ nas tampas inferior e superior do cilindro, e $\\vec{J}_M = 0$ em todo o volume do cilindro.\n"
        "C $\\vec{K}_M = 0$ em toda a superfície do cilindro e $\\vec{J}_M = M_0\\hat{\\phi}$ em todo o volume do cilindro.\n"
        "D $\\vec{K}_M = 0$ em toda a superfície do cilindro e $\\vec{J}_M = M_0\\hat{z}$ em todo o volume do cilindro.\n"
        "E $\\vec{K}_M = 0$ em toda a superfície do cilindro e $\\vec{J}_M = 0$ em todo o volume do cilindro."
    ),
    "2026-1-emPT5b": (
        "Q. 26 [emPT5b]\n"
        "Considere um cilindro de comprimento $L$ que carrega uma magnetização permanente na direção radial a partir de seu eixo de simetria. "
        "Em um sistema de coordenadas cilíndricas, podemos escrever $\\vec{M} = M_0 \\rho \\hat{\\rho}$ para todos os pontos no interior do cilindro a uma distância $\\rho \\ne 0$ do eixo.\n\n"
        "As densidades de correntes ligadas na superfície ($\\vec{K}_M$) associadas a essa magnetização são dadas por:\n\n"
        "A $\\vec{K}_M = \\mp M_0 \\rho \\hat{\\phi}$ nas tampas superior e inferior do cilindro, respectivamente, e $\\vec{K}_M = 0$ na superfície lateral do cilindro.\n"
        "B $\\vec{K}_M = M_0\\hat{\\phi}$ na superfície lateral do cilindro e $\\vec{K}_M = 0$ em suas tampas inferior e superior.\n"
        "C $\\vec{K}_M = \\pm M_0 \\rho \\hat{\\phi}$ nas tampas superior e inferior do cilindro, respectivamente, e $\\vec{K}_M = 0$ na superfície lateral do cilindro.\n"
        "D $\\vec{K}_M = \\pm M_0 \\hat{z}$ nas tampas superior e inferior do cilindro, respectivamente, e $\\vec{K}_M = 0$ na superfície lateral do cilindro.\n"
        "E $\\vec{K}_M = 0$ em toda a superfície do cilindro."
    ),
    "2026-1-emPT6a": (
        "Q. 27 [emPT6a]\n"
        "Considere um circuito constituído por um capacitor de capacitância $C$ e um indutor de indutância $L$. "
        "O capacitor encontra-se inicialmente carregado com carga total $Q_0$ e o circuito está aberto.\n\n"
        "Na figura abaixo, estão representados possíveis gráficos para a carga $Q(t)$ no capacitor (em unidades de $Q_0$), "
        "em função do tempo $t$ (em unidades de $2\\pi\\sqrt{LC}$). Em $t = 0$, a chave do circuito é fechada. "
        "O gráfico que melhor representa $Q(t)$ é dado por:\n\n"
        "A I\n"
        "B II\n"
        "C III\n"
        "D IV\n"
        "E V"
    ),
    "2026-1-emPT6b": (
        "Q. 28 [emPT6b]\n"
        "Considere um circuito constituído por um capacitor de capacitância $C$ e um indutor de indutância $L$. "
        "O capacitor encontra-se inicialmente carregado com carga total $Q_0$ e o circuito está aberto.\n\n"
        "Na figura abaixo, estão representados possíveis gráficos para a corrente $I(t)$ no circuito (em unidades de $Q_0/\\sqrt{LC}$), "
        "em função do tempo $t$ (em unidades de $2\\pi\\sqrt{LC}$). Em $t = 0$, a chave do circuito é fechada. "
        "O gráfico que melhor representa $I(t)$ é dado por:\n\n"
        "A I\n"
        "B II\n"
        "C III\n"
        "D IV\n"
        "E V"
    ),
    "2026-1-emPT7a": (
        "Q. 29 [emPT7a]\n"
        "A figura representa um corte transversal perpendicular ao eixo comum de dois cilindros condutores coaxiais de mesmo comprimento. "
        "Os raios internos e externos de cada um dos cilindros estão indicados na figura ($a, b$ para o cilindro interno e $c, d$ para o externo). "
        "Os cilindros estão em equilíbrio eletrostático. Sobre a superfície condutora de raio $\\rho = b$, existe uma densidade superficial de carga $\\sigma_0$.\n\n"
        "A densidade superficial de carga na superfície interna do cilindro externo ($\\,\\rho = c\\,$) é:\n\n"
        "A $\\sigma_c = -\\frac{b}{c}\\sigma_0$\n"
        "B $\\sigma_c = \\frac{b}{c}\\sigma_0$\n"
        "C $\\sigma_c = -\\frac{c}{b}\\sigma_0$\n"
        "D $\\sigma_c = -\\sigma_0$\n"
        "E $\\sigma_c = 0$"
    ),
    "2026-1-emPT7b": (
        "Q. 30 [emPT7b]\n"
        "A figura representa um corte transversal perpendicular ao eixo comum de dois cilindros condutores coaxiais de mesmo comprimento. "
        "Os raios internos e externos de cada um dos cilindros estão indicados na figura ($a, b$ para o cilindro interno e $c, d$ para o externo). "
        "Os cilindros estão em equilíbrio eletrostático e o cilindro externo é eletricamente neutro no total. "
        "Sobre a superfície condutora de raio $\\rho = b$, existe uma densidade superficial de carga $\\sigma_0$.\n\n"
        "A densidade superficial de carga na superfície externa do cilindro externo ($\\,\\rho = d\\,$) é:\n\n"
        "A $\\sigma_d = \\frac{b}{d}\\sigma_0$\n"
        "B $\\sigma_d = -\\frac{b}{d}\\sigma_0$\n"
        "C $\\sigma_d = \\frac{c}{d}\\sigma_0$\n"
        "D $\\sigma_d = \\sigma_0$\n"
        "E $\\sigma_d = 0$"
    ),
    "2026-1-emPT8a": (
        "Q. 31 [emPT8a]\n"
        "Um feixe de luz não polarizada, correspondente a uma onda plana de intensidade $I_0$, viaja ao longo da direção $+z$ e "
        "incide sobre um conjunto de dois polarizadores lineares ideais. O eixo de transmissão do primeiro polarizador está ao longo do eixo $x$, "
        "enquanto o eixo de transmissão do segundo polarizador faz um ângulo $\\theta$ com o eixo $x$.\n\n"
        "Sabendo que a intensidade final do feixe após atravessar ambos os polarizadores é $\\frac{3}{8}I_0$, o ângulo $\\theta$ é:\n\n"
        "A $30^\\circ$\n"
        "B $45^\\circ$\n"
        "C $60^\\circ$\n"
        "D $90^\\circ$\n"
        "E $15^\\circ$"
    ),
    "2026-1-emPT8b": (
        "Q. 32 [emPT8b]\n"
        "Um feixe de luz não polarizada, correspondente a uma onda plana de intensidade $I_0$, viaja ao longo da direção $+z$ e "
        "incide sobre um conjunto de dois polarizadores lineares ideais. O eixo de transmissão do primeiro polarizador está ao longo do eixo $x$, "
        "enquanto o eixo de transmissão do segundo polarizador faz um ângulo $\\theta$ com o eixo $x$.\n\n"
        "Sabendo que a intensidade final do feixe após atravessar ambos os polarizadores é $\\frac{1}{8}I_0$, o ângulo $\\theta$ é:\n\n"
        "A $60^\\circ$\n"
        "B $30^\\circ$\n"
        "C $45^\\circ$\n"
        "D $90^\\circ$\n"
        "E $15^\\circ$"
    ),

    # =========================================================================
    # 2025-1 ELECTROMAGNETISM (16 Questions: emPT1a to emPT8b)
    # =========================================================================
    "2025-1-emPT1a": (
        "Q. 17 [emPT1a]\n"
        "Considere duas espiras circulares, concêntricas e coplanares, de raios $R_1 = R$ e $R_2 = R/2$. "
        "A espira de raio $R_1$ é percorrida por uma corrente elétrica $i_1$, cujo sentido é oposto ao da corrente $i_2$ que percorre a espira de raio $R_2$.\n\n"
        "Qual é a relação entre $i_1$ e $i_2$ para que o campo magnético $B$ no centro das espiras seja nulo?\n\n"
        "A $i_1 = 2i_2$\n"
        "B $i_1 = 4i_2$\n"
        "C $i_1 = i_2/2$\n"
        "D $i_1 = i_2/4$\n"
        "E $i_1 = i_2 \\ln 2$"
    ),
    "2025-1-emPT1b": (
        "Q. 18 [emPT1b]\n"
        "Considere duas espiras circulares, concêntricas e coplanares, de raios $R_1 = R$ e $R_2 = R/3$. "
        "A espira de raio $R_1$ é percorrida por uma corrente elétrica $i_1$, cujo sentido é oposto ao da corrente $i_2$ que percorre a espira de raio $R_2$.\n\n"
        "Qual é a relação entre $i_1$ e $i_2$ para que o campo magnético $B$ no centro das espiras seja nulo?\n\n"
        "A $i_1 = 3i_2$\n"
        "B $i_1 = 9i_2$\n"
        "C $i_1 = i_2/3$\n"
        "D $i_1 = i_2/9$\n"
        "E $i_1 = i_2 \\ln 3$"
    ),
    "2025-1-emPT2a": (
        "Q. 19 [emPT2a]\n"
        "Considere um campo vetorial dado por $\\vec{G}(x,y,z) = a \\cos(bx)\\hat{x} + cy \\operatorname{sen}(bx)\\hat{y}$, "
        "onde $a, b$ e $c$ são constantes reais não nulas.\n\n"
        "Qual é a relação entre as constantes para que $\\vec{G}$ possa representar um campo magnético físico (isto é, $\\nabla \\cdot \\vec{G} = 0$)?\n\n"
        "A $c = ab$\n"
        "B $b = -ac$\n"
        "C $a = bc$\n"
        "D $b = -2c$\n"
        "E $b = 2ac$"
    ),
    "2025-1-emPT2b": (
        "Q. 20 [emPT2b]\n"
        "Considere um campo vetorial dado por $\\vec{G}(x,y,z) = a \\operatorname{sen}(bx)\\hat{x} + cy \\cos(bx)\\hat{y}$, "
        "onde $a, b$ e $c$ são constantes reais não nulas.\n\n"
        "Qual é a relação entre as constantes para que $\\vec{G}$ possa representar um campo magnético físico (isto é, $\\nabla \\cdot \\vec{G} = 0$)?\n\n"
        "A $c = -ab$\n"
        "B $b = ac$\n"
        "C $a = -bc$\n"
        "D $b = -2c$\n"
        "E $b = 2ac$"
    ),
    "2025-1-emPT3a": (
        "Q. 21 [emPT3a]\n"
        "Uma carga elétrica estática é distribuída em uma casca esférica de raio interno $R_1$ e raio externo $R_2$. "
        "A densidade volumétrica de carga elétrica na casca é dada por $\\rho(r) = a + br$, sendo igual a zero para $r < R_1$ e $r > R_2$, "
        "em que $r$ é a distância até a origem e $a, b$ são constantes positivas.\n\n"
        "Qual é o módulo do campo elétrico $E(r)$ na região $r > R_2$?\n\n"
        "A $E(r) = \\frac{1}{\\varepsilon_0 r^2}\\left[\\frac{a}{3}(R_2^3 - R_1^3) + \\frac{b}{4}(R_2^4 - R_1^4)\\right]$\n"
        "B $E(r) = \\frac{1}{\\varepsilon_0 r^2}\\left[\\frac{a}{2}(R_2^2 - R_1^2) + \\frac{b}{3}(R_2^3 - R_1^3)\\right]$\n"
        "C $E(r) = \\frac{1}{\\varepsilon_0 r^2}\\left[a(R_2 - R_1) + b(R_2^2 - R_1^2)\\right]$\n"
        "D $E(r) = \\frac{1}{4\\pi\\varepsilon_0 r^2}\\left[\\frac{a}{3}(R_2^3 - R_1^3) + \\frac{b}{4}(R_2^4 - R_1^4)\\right]$\n"
        "E $E(r) = \\frac{1}{\\varepsilon_0 r^2}\\left[\\frac{a}{4}(R_2^4 - R_1^4) + \\frac{b}{5}(R_2^5 - R_1^5)\\right]$"
    ),
    "2025-1-emPT3b": (
        "Q. 22 [emPT3b]\n"
        "Uma carga elétrica estática é distribuída em uma casca esférica de raio interno $R_1$ e raio externo $R_2$. "
        "A densidade volumétrica de carga elétrica na casca é dada por $\\rho(r) = a + br$, sendo igual a zero para $r < R_1$ e $r > R_2$, "
        "em que $r$ é a distância até a origem e $a, b$ são constantes positivas.\n\n"
        "Qual é o potencial elétrico $V(r)$ na região $r > R_2$? Considere $V(\\infty) = 0$.\n\n"
        "A $V(r) = \\frac{1}{\\varepsilon_0 r}\\left[\\frac{a}{3}(R_2^3 - R_1^3) + \\frac{b}{4}(R_2^4 - R_1^4)\\right]$\n"
        "B $V(r) = \\frac{1}{\\varepsilon_0 r}\\left[\\frac{a}{2}(R_2^2 - R_1^2) + \\frac{b}{3}(R_2^3 - R_1^3)\\right]$\n"
        "C $V(r) = \\frac{1}{\\varepsilon_0 r}\\left[a(R_2 - R_1) + b(R_2^2 - R_1^2)\\right]$\n"
        "D $V(r) = \\frac{1}{4\\pi\\varepsilon_0 r}\\left[\\frac{a}{3}(R_2^3 - R_1^3) + \\frac{b}{4}(R_2^4 - R_1^4)\\right]$\n"
        "E $V(r) = \\frac{1}{\\varepsilon_0 r}\\left[\\frac{a}{4}(R_2^4 - R_1^4) + \\frac{b}{5}(R_2^5 - R_1^5)\\right]$"
    ),
    "2025-1-emPT4a": (
        "Q. 23 [emPT4a]\n"
        "Um resistor de resistência $R$ é ligado em série a uma bateria com força eletromotriz $\\mathcal{E}$ e resistência interna $r$. "
        "Supondo que o valor de $r$ seja fixo, para qual valor de $R$ a taxa de dissipação de energia (potência dissipada) no resistor é máxima?\n\n"
        "A $R = r$\n"
        "B $R = 2r$\n"
        "C $R = 4r$\n"
        "D $R = r/2$\n"
        "E $R = r/4$"
    ),
    "2025-1-emPT4b": (
        "Q. 24 [emPT4b]\n"
        "Um resistor de resistência $R$ é ligado em série a uma bateria com força eletromotriz $\\mathcal{E}$ e resistência interna $r$. "
        "Supondo que o valor de $r$ seja fixo, qual é a taxa máxima de dissipação de energia (potência máxima) no resistor?\n\n"
        "A $P_{\\text{max}} = \\frac{\\mathcal{E}^2}{4r}$\n"
        "B $P_{\\text{max}} = \\frac{\\mathcal{E}^2}{r}$\n"
        "C $P_{\\text{max}} = \\frac{\\mathcal{E}^2}{2r}$\n"
        "D $P_{\\text{max}} = \\frac{4\\mathcal{E}^2}{r}$\n"
        "E $P_{\\text{max}} = \\frac{\\mathcal{E}^2}{8r}$"
    ),
    "2025-1-emPT5a": (
        "Q. 25 [emPT5a]\n"
        "Um cubo condutor maciço possui uma cavidade esférica cujo centro coincide com o centro do cubo. "
        "No centro da cavidade há uma carga pontual $q = -6{,}0\\,\\mu\\text{C}$ (veja a figura). "
        "Além da carga no centro da cavidade, o condutor maciço está carregado com uma carga total líquida $Q = 18{,}0\\,\\mu\\text{C}$. Pede-se:\n"
        "i) a carga $q_c$ na superfície da cavidade esférica;\n"
        "ii) a carga $q_f$ em cada uma das 6 faces externas do cubo.\n\n"
        "A $q_c = 6{,}0\\,\\mu\\text{C};\\quad q_f = 2{,}0\\,\\mu\\text{C}$\n"
        "B $q_c = -6{,}0\\,\\mu\\text{C};\\quad q_f = 3{,}0\\,\\mu\\text{C}$\n"
        "C $q_c = 6{,}0\\,\\mu\\text{C};\\quad q_f = 3{,}0\\,\\mu\\text{C}$\n"
        "D $q_c = -6{,}0\\,\\mu\\text{C};\\quad q_f = 2{,}0\\,\\mu\\text{C}$\n"
        "E $q_c = 24{,}0\\,\\mu\\text{C};\\quad q_f = -1{,}0\\,\\mu\\text{C}$"
    ),
    "2025-1-emPT5b": (
        "Q. 26 [emPT5b]\n"
        "Um cubo condutor maciço possui uma cavidade esférica cujo centro coincide com o centro do cubo. "
        "No centro da cavidade há uma carga pontual $q = -12{,}0\\,\\mu\\text{C}$ (veja a figura). "
        "Além da carga no centro da cavidade, o condutor maciço está carregado com uma carga total líquida $Q = 36{,}0\\,\\mu\\text{C}$. Pede-se:\n"
        "i) a carga $q_c$ na superfície da cavidade esférica;\n"
        "ii) a carga $q_f$ em cada uma das 6 faces externas do cubo.\n\n"
        "A $q_c = 12{,}0\\,\\mu\\text{C};\\quad q_f = 4{,}0\\,\\mu\\text{C}$\n"
        "B $q_c = -12{,}0\\,\\mu\\text{C};\\quad q_f = 4{,}0\\,\\mu\\text{C}$\n"
        "C $q_c = 12{,}0\\,\\mu\\text{C};\\quad q_f = 6{,}0\\,\\mu\\text{C}$\n"
        "D $q_c = -12{,}0\\,\\mu\\text{C};\\quad q_f = -4{,}0\\,\\mu\\text{C}$\n"
        "E $q_c = 48{,}0\\,\\mu\\text{C};\\quad q_f = -2{,}0\\,\\mu\\text{C}$"
    ),
    "2025-1-emPT6a": (
        "Q. 27 [emPT6a]\n"
        "Partículas de carga $q$ e massa $m$ são aceleradas a partir do repouso ($v_i = 0$) por uma diferença de potencial $\\Delta V$. "
        "Em seguida, as partículas entram numa região com campo magnético uniforme $B = 0{,}5\\text{ T}$ perpendicular à velocidade das mesmas, "
        "e passam a descrever uma trajetória circular de raio $r$ (veja a figura).\n\n"
        "O gráfico apresenta os resultados para os valores de $r^2$ obtidos variando-se a diferença de potencial $\\Delta V$. "
        "Qual é o valor da razão $q/m$ dessas partículas?\n\n"
        "A $q/m = 1{,}0 \\times 10^6\\text{ C/kg}$\n"
        "B $q/m = 1{,}0 \\times 10^{-6}\\text{ C/kg}$\n"
        "C $q/m = 5{,}0 \\times 10^5\\text{ C/kg}$\n"
        "D $q/m = 1{,}0 \\times 10^2\\text{ C/kg}$\n"
        "E $q/m = 5{,}0 \\times 10^1\\text{ C/kg}$"
    ),
    "2025-1-emPT6b": (
        "Q. 28 [emPT6b]\n"
        "Partículas de carga $q$ e massa $m$ são aceleradas a partir do repouso ($v_i = 0$) por uma diferença de potencial $\\Delta V$. "
        "Em seguida, as partículas entram numa região com campo magnético uniforme $B = 0{,}5\\text{ T}$ perpendicular à velocidade das mesmas, "
        "e passam a descrever uma trajetória circular de raio $r$ (veja a figura).\n\n"
        "O gráfico apresenta os resultados para os valores de $r^2$ obtidos variando-se a diferença de potencial $\\Delta V$. "
        "Qual é o valor da razão $q/m$ dessas partículas?\n\n"
        "A $q/m = 2{,}0 \\times 10^6\\text{ C/kg}$\n"
        "B $q/m = 5{,}0 \\times 10^{-7}\\text{ C/kg}$\n"
        "C $q/m = 1{,}0 \\times 10^6\\text{ C/kg}$\n"
        "D $q/m = 2{,}0 \\times 10^2\\text{ C/kg}$\n"
        "E $q/m = 1{,}0 \\times 10^2\\text{ C/kg}$"
    ),
    "2025-1-emPT7a": (
        "Q. 29 [emPT7a]\n"
        "Uma barra condutora de comprimento $a$, resistência elétrica $R$ e massa $m$ pode deslizar sem atrito sobre um par de trilhos "
        "condutores paralelos e horizontais de resistência desprezível (veja a figura). Um campo magnético uniforme $B$ é perpendicular "
        "ao plano dos trilhos e a barra encontra-se inicialmente em repouso ($v_i = 0$).\n\n"
        "Uma bateria de força eletromotriz $V_0$ e resistência interna nula é conectada entre os dois trilhos no instante $t = 0$, "
        "gerando uma corrente inicial $i_0$. Pede-se:\n"
        "i) a força $F(v)$ que age sobre a barra em função da sua velocidade $v$;\n"
        "ii) a velocidade $v$ da barra quando a corrente for igual a $1/4$ do seu valor inicial ($i = i_0/4$).\n\n"
        "A $F(v) = \\frac{aB}{R}(V_0 - aBv);\\quad v = \\frac{3V_0}{4aB}$\n"
        "B $F(v) = \\frac{aB}{R}(V_0 + aBv);\\quad v = \\frac{3V_0}{4aB}$\n"
        "C $F(v) = \\frac{aB}{R}V_0;\\quad v = \\frac{3V_0}{4aBm}$\n"
        "D $F(v) = -\\frac{aB}{R}(aBv);\\quad v = \\frac{V_0}{4aB}$\n"
        "E $F(v) = \\frac{aB}{R}(V_0 - aBv);\\quad v = \\frac{V_0}{4aBm}$"
    ),
    "2025-1-emPT7b": (
        "Q. 30 [emPT7b]\n"
        "Uma barra condutora de comprimento $L$, resistência elétrica $r$ e massa $M$ pode deslizar sem atrito sobre um par de trilhos "
        "condutores paralelos e horizontais de resistência desprezível (veja a figura). Um campo magnético uniforme $B$ é perpendicular "
        "ao plano dos trilhos e a barra encontra-se inicialmente em repouso ($v_i = 0$).\n\n"
        "Uma bateria de força eletromotriz $\\mathcal{E}_0$ e resistência interna nula é conectada entre os dois trilhos no instante $t = 0$, "
        "gerando uma corrente inicial $i_0$. Pede-se:\n"
        "i) a força $F(v)$ que age sobre a barra em função da sua velocidade $v$;\n"
        "ii) a velocidade $v$ da barra quando a corrente for igual a $1/5$ do seu valor inicial ($i = i_0/5$).\n\n"
        "A $F(v) = \\frac{LB}{r}(\\mathcal{E}_0 - LBv);\\quad v = \\frac{4\\mathcal{E}_0}{5LB}$\n"
        "B $F(v) = \\frac{LB}{r}(\\mathcal{E}_0 + LBv);\\quad v = \\frac{4\\mathcal{E}_0}{5LB}$\n"
        "C $F(v) = \\frac{LB}{r}\\mathcal{E}_0;\\quad v = \\frac{4\\mathcal{E}_0}{5LBM}$\n"
        "D $F(v) = -\\frac{LB}{r}(LBv);\\quad v = \\frac{\\mathcal{E}_0}{5LB}$\n"
        "E $F(v) = \\frac{LB}{r}(\\mathcal{E}_0 - LBv);\\quad v = \\frac{\\mathcal{E}_0}{5LBM}$"
    ),
    "2025-1-emPT8a": (
        "Q. 31 [emPT8a]\n"
        "Radiação eletromagnética monocromática, de intensidade uniforme, incide perpendicularmente sobre uma placa metálica polida "
        "de formato quadrado e de área $A = b^2$. A placa reflete $80\\%$ da intensidade da radiação incidente e absorve o restante na superfície.\n\n"
        "Os campos elétrico e magnético da radiação incidente são dados, respectivamente, pelas partes reais das seguintes expressões: "
        "$\\vec{E}(z,t) = E_0 e^{-i(\\omega t - kz)}\\hat{x}$ e $\\vec{B}(z,t) = \\frac{E_0}{c}e^{-i(\\omega t - kz)}\\hat{y}$.\n\n"
        "Qual é a força média $\\vec{F}_{\\text{rad}}$ que a radiação exerce sobre a placa metálica?\n\n"
        "A $\\vec{F}_{\\text{rad}} = 0{,}9 \\frac{E_0^2}{\\mu_0 c^2} b^2\\hat{z}$\n"
        "B $\\vec{F}_{\\text{rad}} = 0{,}6 \\frac{E_0^2}{\\mu_0 c^2} b^2\\hat{z}$\n"
        "C $\\vec{F}_{\\text{rad}} = 0{,}5 \\frac{E_0^2}{\\mu_0 c^2} b^2\\hat{z}$\n"
        "D $\\vec{F}_{\\text{rad}} = 0{,}7 \\frac{E_0^2}{\\mu_0 c^2} b^2\\hat{z}$\n"
        "E $\\vec{F}_{\\text{rad}} = 0{,}2 \\frac{E_0^2}{\\mu_0 c^2} b^2\\hat{z}$"
    ),
    "2025-1-emPT8b": (
        "Q. 32 [emPT8b]\n"
        "Radiação eletromagnética monocromática, de intensidade uniforme, incide perpendicularmente sobre uma placa metálica polida "
        "de formato circular e de área $A = \\pi R^2$. A placa reflete $60\\%$ da intensidade da radiação incidente e absorve o restante na superfície.\n\n"
        "Os campos elétrico e magnético da radiação incidente são dados, respectivamente, pelas partes reais das seguintes expressões: "
        "$\\vec{E}(z,t) = E_0 e^{-i(\\omega t - kz)}\\hat{x}$ e $\\vec{B}(z,t) = \\frac{E_0}{c}e^{-i(\\omega t - kz)}\\hat{y}$.\n\n"
        "Qual é a força média $\\vec{F}_{\\text{rad}}$ que a radiação exerce sobre a placa metálica?\n\n"
        "A $\\vec{F}_{\\text{rad}} = 0{,}8 \\frac{E_0^2}{\\mu_0 c^2}(\\pi R^2)\\hat{z}$\n"
        "B $\\vec{F}_{\\text{rad}} = 0{,}7 \\frac{E_0^2}{\\mu_0 c^2}(\\pi R^2)\\hat{z}$\n"
        "C $\\vec{F}_{\\text{rad}} = 0{,}5 \\frac{E_0^2}{\\mu_0 c^2}(\\pi R^2)\\hat{z}$\n"
        "D $\\vec{F}_{\\text{rad}} = 0{,}4 \\frac{E_0^2}{\\mu_0 c^2}(\\pi R^2)\\hat{z}$\n"
        "E $\\vec{F}_{\\text{rad}} = 0{,}2 \\frac{E_0^2}{\\mu_0 c^2}(\\pi R^2)\\hat{z}$"
    ),

    # =========================================================================
    # 2024-2 ELECTROMAGNETISM (16 Questions: emPT1a to emPT8b)
    # =========================================================================
    "2024-2-emPT1a": (
        "Q. 17 [emPT1a]\n"
        "Um isolante cilíndrico de raio $R$, infinitamente longo, possui uma distribuição uniforme de cargas com densidade volumétrica $\\rho_0 > 0$.\n\n"
        "Qual é o módulo do campo elétrico $E(\\rho)$ a uma distância $\\rho < R$ do eixo de simetria do cilindro?\n\n"
        "A $E = \\frac{\\rho_0 \\rho}{2\\varepsilon_0}$\n"
        "B $E = \\frac{\\rho_0 \\rho}{\\varepsilon_0}$\n"
        "C $E = \\frac{2\\rho_0 \\rho}{\\varepsilon_0}$\n"
        "D $E = \\frac{\\rho_0 R^2}{2\\varepsilon_0 \\rho}$\n"
        "E $E = \\frac{\\rho_0 R^2}{4\\varepsilon_0 \\rho}$"
    ),
    "2024-2-emPT1b": (
        "Q. 18 [emPT1b]\n"
        "Um isolante cilíndrico de raio $R$, infinitamente longo, possui uma distribuição uniforme de cargas com densidade volumétrica $\\rho_0 > 0$.\n\n"
        "Qual é o módulo do campo elétrico $E(\\rho)$ a uma distância $\\rho > R$ do eixo de simetria do cilindro?\n\n"
        "A $E = \\frac{\\rho_0 R^2}{2\\varepsilon_0 \\rho}$\n"
        "B $E = \\frac{\\rho_0 R^2}{4\\varepsilon_0 \\rho}$\n"
        "C $E = \\frac{\\rho_0 \\rho}{2\\varepsilon_0}$\n"
        "D $E = \\frac{\\rho_0 R^2}{2\\varepsilon_0}$\n"
        "E $E = \\frac{\\rho_0 \\rho^2}{2\\varepsilon_0 R}$"
    ),
    "2024-2-emPT2a": (
        "Q. 19 [emPT2a]\n"
        "Num determinado instante, um capacitor de capacitância $C$, totalmente carregado com uma carga $Q_0$, "
        "começa a descarregar através de um resistor de resistência $R$.\n\n"
        "Em qual instante $t$ o capacitor terá a metade de sua carga inicial ($Q(t) = Q_0/2$)?\n\n"
        "A $t = RC \\ln 2$\n"
        "B $t = \\frac{1}{2}RC \\ln 2$\n"
        "C $t = 2RC \\ln 2$\n"
        "D $t = RC \\ln 3$\n"
        "E $t = \\frac{1}{2}RC \\ln 3$"
    ),
    "2024-2-emPT2b": (
        "Q. 20 [emPT2b]\n"
        "Num determinado instante, um capacitor de capacitância $C$, totalmente carregado com uma carga $Q_0$, "
        "começa a descarregar através de um resistor de resistência $R$.\n\n"
        "Em qual instante $t$ o capacitor terá um terço de sua carga inicial ($Q(t) = Q_0/3$)?\n\n"
        "A $t = RC \\ln 3$\n"
        "B $t = \\frac{1}{3}RC \\ln 3$\n"
        "C $t = 3RC \\ln 3$\n"
        "D $t = RC \\ln 2$\n"
        "E $t = \\frac{1}{3}RC \\ln 2$"
    ),
    "2024-2-emPT3a": (
        "Q. 21 [emPT3a]\n"
        "Um cabo coaxial é constituído por um cilindro condutor interno de raio $a$ envolto por uma casca cilíndrica externa condutora fina, "
        "coaxial ao cilindro interno e de raio $b > a$. O cilindro interno é percorrido por uma corrente $I$ uniformemente distribuída em sua seção reta. "
        "O cilindro externo é percorrido por uma corrente de mesma intensidade $I$, uniformemente distribuída na sua superfície, mas que flui em sentido oposto.\n\n"
        "Considerando que o eixo de simetria do cabo coaxial é o eixo $z$, qual é o campo magnético $\\vec{B}$ na região $0 < \\rho < a$ (no interior do condutor interno)?\n\n"
        "A $\\vec{B} = \\frac{\\mu_0 I \\rho}{2\\pi a^2}\\hat{\\phi}$\n"
        "B $\\vec{B} = \\frac{\\mu_0 I \\rho^2}{2\\pi a^3}\\hat{\\phi}$\n"
        "C $\\vec{B} = \\frac{\\mu_0 I}{2\\pi a}\\hat{\\phi}$\n"
        "D $\\vec{B} = \\frac{\\mu_0 I a}{2\\pi \\rho^2}\\hat{\\phi}$\n"
        "E $\\vec{B} = 0$"
    ),
    "2024-2-emPT3b": (
        "Q. 22 [emPT3b]\n"
        "Um cabo coaxial é constituído por um cilindro condutor interno de raio $a$ envolto por uma casca cilíndrica externa condutora fina, "
        "coaxial ao cilindro interno e de raio $b > a$. O cilindro interno é percorrido por uma corrente $I$ uniformemente distribuída em sua seção reta. "
        "O cilindro externo é percorrido por uma corrente de mesma intensidade $I$, uniformemente distribuída na sua superfície, mas que flui em sentido oposto.\n\n"
        "Considerando que o eixo de simetria do cabo coaxial é o eixo $z$, qual é o campo magnético $\\vec{B}$ na região $a < \\rho < b$ (entre os condutores)?\n\n"
        "A $\\vec{B} = \\frac{\\mu_0 I}{2\\pi \\rho}\\hat{\\phi}$\n"
        "B $\\vec{B} = \\frac{\\mu_0 I a}{2\\pi \\rho^2}\\hat{\\phi}$\n"
        "C $\\vec{B} = \\frac{\\mu_0 I \\rho}{2\\pi a^2}\\hat{\\phi}$\n"
        "D $\\vec{B} = \\frac{\\mu_0 I b}{2\\pi \\rho^2}\\hat{\\phi}$\n"
        "E $\\vec{B} = 0$"
    ),
    "2024-2-emPT4a": (
        "Q. 23 [emPT4a]\n"
        "Em uma determinada região do espaço o campo elétrico é dado, em coordenadas esféricas, por $\\vec{E}(r) = k r^2 \\hat{r}$, onde $k$ é uma constante positiva.\n\n"
        "Qual é a densidade volumétrica de carga $\\rho(r)$ nessa região?\n\n"
        "A $\\rho = 4 k \\varepsilon_0 r$\n"
        "B $\\rho = 2\\pi k \\varepsilon_0 r$\n"
        "C $\\rho = 4\\pi \\varepsilon_0 r$\n"
        "D $\\rho = k \\varepsilon_0 r$\n"
        "E $\\rho = \\pi k \\varepsilon_0 r$"
    ),
    "2024-2-emPT4b": (
        "Q. 24 [emPT4b]\n"
        "Em uma determinada região do espaço o campo elétrico é dado, em coordenadas esféricas, por $\\vec{E}(r) = k r^3 \\hat{r}$, onde $k$ é uma constante positiva.\n\n"
        "Qual é a densidade volumétrica de carga $\\rho(r)$ nessa região?\n\n"
        "A $\\rho = 5 k \\varepsilon_0 r^2$\n"
        "B $\\rho = 10 k \\varepsilon_0 r^2$\n"
        "C $\\rho = 4\\pi k \\varepsilon_0 r^2$\n"
        "D $\\rho = 5\\pi k \\varepsilon_0 r^2$\n"
        "E $\\rho = 10\\pi \\varepsilon_0 r^2$"
    ),
    "2024-2-emPT5a": (
        "Q. 25 [emPT5a]\n"
        "Uma espira situa-se no plano $xy$ e é formada por dois arcos de circunferência de abertura angular $\\theta_0$, centrados na origem $C$, "
        "de raios $R_1$ e $R_2 > R_1$, conectados por dois segmentos radiais retos (ver figura). A corrente elétrica na espira é $I_0$ e tem sentido "
        "anti-horário no arco de maior raio ($R_2$) quando vista de cima ($z > 0$).\n\n"
        "O campo magnético $\\vec{B}$ na origem $C$ é dado por:\n\n"
        "A $\\vec{B} = \\frac{\\mu_0 I_0 \\theta_0}{4\\pi}\\left(\\frac{1}{R_2} - \\frac{1}{R_1}\\right)\\hat{z}$\n"
        "B $\\vec{B} = \\frac{\\mu_0 I_0 \\theta_0}{4\\pi}\\left(\\frac{1}{R_1} + \\frac{1}{R_2}\\right)\\hat{z}$\n"
        "C $\\vec{B} = \\frac{\\mu_0 I_0 \\theta_0}{2\\pi}\\left(\\frac{1}{R_2} - \\frac{1}{R_1}\\right)\\hat{z}$\n"
        "D $\\vec{B} = \\frac{\\mu_0 I_0}{4\\pi(R_2 - R_1)}\\hat{z}$\n"
        "E $\\vec{B} = 0$"
    ),
    "2024-2-emPT5b": (
        "Q. 26 [emPT5b]\n"
        "Uma espira situa-se no plano $xy$ e é formada por dois arcos de circunferência de abertura angular $2\\theta_0$, centrados na origem $C$, "
        "de raios $R_1$ e $R_2 > R_1$, conectados por dois segmentos radiais retos (ver figura). A corrente elétrica na espira é $I_0$ e tem sentido "
        "anti-horário no arco de maior raio ($R_2$) quando vista de cima ($z > 0$).\n\n"
        "O campo magnético $\\vec{B}$ na origem $C$ é dado por:\n\n"
        "A $\\vec{B} = \\frac{\\mu_0 I_0 \\theta_0}{2\\pi}\\left(\\frac{1}{R_2} - \\frac{1}{R_1}\\right)\\hat{z}$\n"
        "B $\\vec{B} = \\frac{\\mu_0 I_0 \\theta_0}{2\\pi}\\left(\\frac{1}{R_1} + \\frac{1}{R_2}\\right)\\hat{z}$\n"
        "C $\\vec{B} = \\frac{\\mu_0 I_0 \\theta_0}{4\\pi}\\left(\\frac{1}{R_2} - \\frac{1}{R_1}\\right)\\hat{z}$\n"
        "D $\\vec{B} = \\frac{\\mu_0 I_0}{2\\pi(R_2 - R_1)}\\hat{z}$\n"
        "E $\\vec{B} = 0$"
    ),
    "2024-2-emPT6a": (
        "Q. 27 [emPT6a]\n"
        "O potencial vetor de certa distribuição de corrente elétrica em uma região do espaço é dado, em coordenadas cilíndricas, por "
        "$\\vec{A}(\\rho, \\phi, z) = \\frac{1}{2} C_0 \\rho \\hat{\\phi}$, com $C_0$ constante positiva.\n\n"
        "i) Calcule o campo magnético $\\vec{B}(\\rho, \\phi, z) = \\nabla \\times \\vec{A}$;\n"
        "ii) Em que região espacial próxima a qual distribuição de corrente pode-se observar esse campo magnético?\n\n"
        "A $\\vec{B}(\\rho, \\phi, z) = C_0 \\hat{z}$; interior de um solenoide longo\n"
        "B $\\vec{B}(\\rho, \\phi, z) = \\frac{1}{2}C_0 \\rho^2 \\hat{z}$; proximidades de um fio retilíneo longo\n"
        "C $\\vec{B}(\\rho, \\phi, z) = C_0 \\hat{\\phi}$; interior de um solenoide longo\n"
        "D $\\vec{B}(\\rho, \\phi, z) = \\frac{1}{2}C_0 \\hat{z}$; ao longo do eixo de uma espira circular\n"
        "E $\\vec{B}(\\rho, \\phi, z) = C_0 \\hat{\\rho}$; ao longo do eixo de uma espira circular"
    ),
    "2024-2-emPT6b": (
        "Q. 28 [emPT6b]\n"
        "O potencial vetor de certa distribuição de corrente elétrica em uma região do espaço é dado, em coordenadas cilíndricas, por "
        "$\\vec{A}(\\rho, \\phi, z) = -C_0 \\ln(\\rho/a)\\hat{z}$, com $C_0$ e $a$ constantes positivas.\n\n"
        "i) Calcule o campo magnético $\\vec{B}(\\rho, \\phi, z) = \\nabla \\times \\vec{A}$;\n"
        "ii) Em que região espacial próxima a qual distribuição de corrente pode-se observar esse campo magnético?\n\n"
        "A $\\vec{B}(\\rho, \\phi, z) = \\frac{C_0}{\\rho}\\hat{\\phi}$; proximidades de um fio retilíneo longo\n"
        "B $\\vec{B}(\\rho, \\phi, z) = C_0 \\ln(\\rho/a)\\hat{\\phi}$; proximidades de um fio retilíneo longo\n"
        "C $\\vec{B}(\\rho, \\phi, z) = \\frac{C_0}{\\rho}\\hat{z}$; ao longo do eixo de uma espira circular\n"
        "D $\\vec{B}(\\rho, \\phi, z) = C_0 \\hat{\\phi}$; interior de um solenoide longo\n"
        "E $\\vec{B}(\\rho, \\phi, z) = C_0 \\rho \\hat{z}$; interior de um solenoide longo"
    ),
    "2024-2-emPT7a": (
        "Q. 29 [emPT7a]\n"
        "Uma onda eletromagnética plana propaga-se ao longo da direção $+z$ num meio dielétrico, não magnético ($\\mu = \\mu_0$), homogêneo e isotrópico. "
        "O campo elétrico da onda é dado, em notação complexa, por $\\vec{E}(z,t) = E_0 e^{i(kz - \\omega t)}(\\hat{x} + 3\\hat{y})$, "
        "com $k = 1{,}8 \\times 10^7\\text{ m}^{-1}$, $\\omega = 3{,}6 \\times 10^{15}\\text{ s}^{-1}$ e $E_0$ constante. "
        "A velocidade da luz no vácuo é $c = 3{,}0 \\times 10^8\\text{ m/s}$.\n\n"
        "Calcule: i) a velocidade de fase $v_f$ da onda; ii) o índice de refração $n$ do meio dielétrico; iii) o campo magnético $\\vec{B}(z,t)$ da onda.\n\n"
        "A $v_f = 2{,}0 \\times 10^8\\text{ m/s};\\quad n = 1{,}5;\\quad \\vec{B}(z,t) = -\\frac{E_0}{v_f} e^{i(kz - \\omega t)}(3\\hat{x} - \\hat{y})$\n"
        "B $v_f = 2{,}0 \\times 10^8\\text{ m/s};\\quad n = 1{,}5;\\quad \\vec{B}(z,t) = \\frac{E_0}{v_f} e^{i(kz - \\omega t)}(3\\hat{x} + \\hat{y})$\n"
        "C $v_f = 5{,}0 \\times 10^8\\text{ m/s};\\quad n = 0{,}6;\\quad \\vec{B}(z,t) = -\\frac{E_0}{v_f} e^{i(kz - \\omega t)}(3\\hat{x} - \\hat{y})$\n"
        "D $v_f = 5{,}0 \\times 10^8\\text{ m/s};\\quad n = 0{,}6;\\quad \\vec{B}(z,t) = \\frac{E_0}{v_f} e^{i(kz - \\omega t)}(3\\hat{x} + \\hat{y})$\n"
        "E $v_f = 1{,}5 \\times 10^8\\text{ m/s};\\quad n = 2{,}0;\\quad \\vec{B}(z,t) = \\frac{E_0}{v_f} e^{i(kz - \\omega t)}(\\hat{x} - 3\\hat{y})$"
    ),
    "2024-2-emPT7b": (
        "Q. 30 [emPT7b]\n"
        "Uma onda eletromagnética plana propaga-se ao longo da direção $+z$ num meio dielétrico, não magnético ($\\mu = \\mu_0$), homogêneo e isotrópico. "
        "O campo elétrico da onda é dado, em notação complexa, por $\\vec{E}(z,t) = E_0 e^{i(kz - \\omega t)}(2\\hat{x} - \\hat{y})$, "
        "com $k = 1{,}2 \\times 10^7\\text{ m}^{-1}$, $\\omega = 3{,}0 \\times 10^{15}\\text{ s}^{-1}$ e $E_0$ constante. "
        "A velocidade da luz no vácuo é $c = 3{,}0 \\times 10^8\\text{ m/s}$.\n\n"
        "Calcule: i) a velocidade de fase $v_f$ da onda; ii) o índice de refração $n$ do meio dielétrico; iii) o campo magnético $\\vec{B}(z,t)$ da onda.\n\n"
        "A $v_f = 2{,}5 \\times 10^8\\text{ m/s};\\quad n = 1{,}2;\\quad \\vec{B}(z,t) = \\frac{E_0}{v_f} e^{i(kz - \\omega t)}(\\hat{x} + 2\\hat{y})$\n"
        "B $v_f = 2{,}5 \\times 10^8\\text{ m/s};\\quad n = 1{,}2;\\quad \\vec{B}(z,t) = \\frac{E_0}{v_f} e^{i(kz - \\omega t)}(\\hat{x} - 2\\hat{y})$\n"
        "C $v_f = 4{,}0 \\times 10^8\\text{ m/s};\\quad n = 0{,}75;\\quad \\vec{B}(z,t) = -\\frac{E_0}{v_f} e^{i(kz - \\omega t)}(\\hat{x} + 2\\hat{y})$\n"
        "D $v_f = 4{,}0 \\times 10^8\\text{ m/s};\\quad n = 0{,}75;\\quad \\vec{B}(z,t) = -\\frac{E_0}{v_f} e^{i(kz - \\omega t)}(\\hat{x} - 2\\hat{y})$\n"
        "E $v_f = 7{,}5 \\times 10^8\\text{ m/s};\\quad n = 0{,}4;\\quad \\vec{B}(z,t) = \\frac{E_0}{v_f} e^{i(kz - \\omega t)}(2\\hat{x} + \\hat{y})$"
    ),
    "2024-2-emPT8a": (
        "Q. 31 [emPT8a]\n"
        "Uma espira condutora quadrada de lado $D$ encontra-se no interior de um solenoide longo de comprimento $L$ e de seção reta circular de raio $a$ ($D \\le 2a \\ll L$). "
        "O plano da espira é perpendicular ao eixo do solenoide. O número total de voltas do solenoide é $N$ e a corrente elétrica que nele circula é "
        "dada por $I(t) = I_0 \\cos(\\omega t)$.\n\n"
        "Qual é a força eletromotriz $\\mathcal{E}(t)$ induzida na espira?\n\n"
        "A $\\mathcal{E}(t) = \\frac{\\omega \\mu_0 I_0 N D^2}{L}\\operatorname{sen}(\\omega t)$\n"
        "B $\\mathcal{E}(t) = \\frac{\\omega \\mu_0 I_0 N D^2}{L}\\cos(\\omega t)$\n"
        "C $\\mathcal{E}(t) = \\frac{\\mu_0 I_0 N^2 D^2}{L^2}\\operatorname{sen}(\\omega t)$\n"
        "D $\\mathcal{E}(t) = \\frac{\\mu_0 I_0 N (\\pi a^2)}{L}\\cos(\\omega t)$\n"
        "E $\\mathcal{E}(t) = \\frac{\\mu_0 I_0 N^2 (\\pi a^2)}{L^2}\\operatorname{sen}(\\omega t)$"
    ),
    "2024-2-emPT8b": (
        "Q. 32 [emPT8b]\n"
        "Uma espira condutora quadrada de lado $C$ encontra-se no interior de um solenoide longo de comprimento $L$ e de seção reta circular de raio $b$ ($C \\le 2b \\ll L$). "
        "O plano da espira é perpendicular ao eixo do solenoide. O número total de voltas do solenoide é $N$ e a corrente elétrica que nele circula é "
        "dada por $I(t) = I_0 \\operatorname{sen}(\\omega t)$.\n\n"
        "Qual é a força eletromotriz $\\mathcal{E}(t)$ induzida na espira?\n\n"
        "A $\\mathcal{E}(t) = -\\frac{\\omega \\mu_0 I_0 N C^2}{L}\\cos(\\omega t)$\n"
        "B $\\mathcal{E}(t) = \\frac{\\omega \\mu_0 I_0 N C^2}{L}\\operatorname{sen}(\\omega t)$\n"
        "C $\\mathcal{E}(t) = \\frac{\\mu_0 I_0 N^2 C^2}{L^2}\\cos(\\omega t)$\n"
        "D $\\mathcal{E}(t) = \\frac{\\mu_0 I_0 N (\\pi b^2)}{L}\\operatorname{sen}(\\omega t)$\n"
        "E $\\mathcal{E}(t) = \\frac{\\mu_0 I_0 N^2 (\\pi b^2)}{L^2}\\cos(\\omega t)$"
    ),

    # =========================================================================
    # 2023-2 ELECTROMAGNETISM (16 Questions: emPT1a to emPT8b)
    # =========================================================================
    "2023-2-emPT1a": (
        "Q. 17 [emPT1a]\n"
        "Duas esferas condutoras, com raios iguais a $R_A$ e $R_B$, onde $R_A > R_B$, encontram-se muito distantes uma da outra ($d \\gg R_A$). "
        "As esferas são conectadas por um fio condutor fino. O sistema possui uma carga líquida total $Q$, distribuída entre as esferas em equilíbrio eletrostático.\n\n"
        "Qual é o potencial elétrico $V$ na superfície das esferas em termos de $Q$? Assuma $V = 0$ no infinito.\n\n"
        "A $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{R_A + R_B}$\n"
        "B $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{R_A - R_B}$\n"
        "C $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{R_A + 2R_B}$\n"
        "D $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{2R_A + R_B}$\n"
        "E $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{3R_A - R_B}$"
    ),
    "2023-2-emPT1b": (
        "Q. 18 [emPT1b]\n"
        "Duas esferas condutoras, com raios iguais a $R_A$ e $R_B$, onde $R_A = 2R_B$, encontram-se muito distantes uma da outra ($d \\gg R_A$). "
        "As esferas são conectadas por um fio condutor fino. O sistema possui uma carga líquida total $Q$, distribuída entre as esferas em equilíbrio eletrostático.\n\n"
        "Qual é o potencial elétrico $V$ na superfície das esferas em termos de $Q$? Assuma $V = 0$ no infinito.\n\n"
        "A $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{3R_B}$\n"
        "B $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{R_B}$\n"
        "C $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{4R_B}$\n"
        "D $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{5R_B}$\n"
        "E $V = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q}{2R_B}$"
    ),
    "2023-2-emPT2a": (
        "Q. 19 [emPT2a]\n"
        "Duas espiras condutoras circulares concêntricas A e B, com raios iguais a $a$ e $b$ ($b \\gg a$), respectivamente, estão inicialmente no mesmo plano. "
        "No instante $t = 0$, a espira A, com resistência $R$, começa a girar em torno de um de seus diâmetros com velocidade angular constante $\\omega$, "
        "enquanto a espira B permanece em repouso percorrida por uma corrente constante $I_B$.\n\n"
        "Qual é a força eletromotriz $\\mathcal{E}(t)$ induzida na espira A? Despreze efeitos de autoindutância.\n\n"
        "A $\\mathcal{E}(t) = \\frac{\\mu_0 \\omega I_B \\pi a^2}{2b}\\operatorname{sen}(\\omega t)$\n"
        "B $\\mathcal{E}(t) = \\frac{\\mu_0 \\omega I_B \\pi a^2}{2b}\\cos(\\omega t)$\n"
        "C $\\mathcal{E}(t) = \\frac{\\mu_0 \\omega I_B \\pi b^2}{4a}\\operatorname{sen}(\\omega t)$\n"
        "D $\\mathcal{E}(t) = \\frac{\\mu_0 \\omega I_B \\pi b^2}{4a}\\cos(\\omega t)$\n"
        "E $\\mathcal{E}(t) = \\frac{\\mu_0 \\omega I_B a^2}{2\\pi b}\\operatorname{sen}(\\omega t)$"
    ),
    "2023-2-emPT2b": (
        "Q. 20 [emPT2b]\n"
        "Duas espiras condutoras circulares concêntricas A e B, com raios iguais a $a$ e $b$ ($b \\gg a$), respectivamente, estão inicialmente no mesmo plano. "
        "No instante $t = 0$, a espira A, com resistência $R$, começa a girar em torno de um de seus diâmetros com velocidade angular constante $\\omega$, "
        "enquanto a espira B permanece em repouso percorrida por uma corrente constante $I_B$.\n\n"
        "Qual é a corrente elétrica $I_A(t)$ induzida na espira A? Despreze efeitos de autoindutância.\n\n"
        "A $I_A(t) = \\frac{\\mu_0 \\omega I_B \\pi a^2}{2Rb}\\operatorname{sen}(\\omega t)$\n"
        "B $I_A(t) = \\frac{\\mu_0 \\omega I_B \\pi a^2}{2Rb}\\cos(\\omega t)$\n"
        "C $I_A(t) = \\frac{\\mu_0 \\omega I_B \\pi b^2}{4Ra}\\operatorname{sen}(\\omega t)$\n"
        "D $I_A(t) = \\frac{\\mu_0 \\omega I_B \\pi b^2}{4Ra}\\cos(\\omega t)$\n"
        "E $I_A(t) = \\frac{\\mu_0 \\omega I_B a^2}{2\\pi Rb}\\operatorname{sen}(\\omega t)$"
    ),
    "2023-2-emPT3a": (
        "Q. 21 [emPT3a]\n"
        "Um capacitor de capacitância $C$ está totalmente carregado com uma carga $Q_0$ e com uma energia total armazenada igual a $U_0$. "
        "No instante $t = 0$ o capacitor começa a descarregar através de um resistor de resistência $R$.\n\n"
        "Em termos da constante de tempo $\\tau = RC$, em qual instante $t$ a energia armazenada no capacitor será igual a $U_0/4$?\n\n"
        "A $t = \\tau \\ln 2$\n"
        "B $t = \\frac{\\tau}{2} \\ln 2$\n"
        "C $t = \\tau \\ln 4$\n"
        "D $t = 2\\tau$\n"
        "E $t = \\frac{\\tau}{4}$"
    ),
    "2023-2-emPT3b": (
        "Q. 22 [emPT3b]\n"
        "Um capacitor de capacitância $C$ está totalmente carregado com uma carga $Q_0$ e com uma energia total armazenada igual a $U_0$. "
        "No instante $t = 0$ o capacitor começa a descarregar através de um resistor de resistência $R$.\n\n"
        "Em termos da constante de tempo $\\tau = RC$, em qual instante $t$ a energia armazenada no capacitor será igual a $U_0/9$?\n\n"
        "A $t = \\tau \\ln 3$\n"
        "B $t = \\frac{\\tau}{2} \\ln 3$\n"
        "C $t = \\tau \\ln 9$\n"
        "D $t = 3\\tau$\n"
        "E $t = \\frac{\\tau}{3}$"
    ),
    "2023-2-emPT4a": (
        "Q. 23 [emPT4a]\n"
        "O campo elétrico no interior de um capacitor de placas paralelas circulares de raio $R$ varia no tempo como "
        "$\\vec{E}(t) = E_0 \\left(\\frac{t}{\\tau}\\right)^2\\hat{z}$.\n\n"
        "Qual é o campo magnético induzido $\\vec{B}(r,t)$ a uma distância radial $r < R$ do eixo central das placas?\n\n"
        "A $\\vec{B}(r,t) = \\frac{\\mu_0 \\varepsilon_0 r E_0 t}{\\tau^2}\\hat{\\phi}$\n"
        "B $\\vec{B}(r,t) = \\frac{\\mu_0 \\varepsilon_0 r E_0 t^2}{2\\tau^2}\\hat{\\phi}$\n"
        "C $\\vec{B}(r,t) = \\frac{\\pi r \\mu_0 \\varepsilon_0 E_0 t}{\\tau^2}\\hat{\\phi}$\n"
        "D $\\vec{B}(r,t) = \\frac{2\\pi r \\mu_0 \\varepsilon_0 E_0 t}{\\tau^2}\\hat{\\phi}$\n"
        "E $\\vec{B}(r,t) = \\frac{\\mu_0 \\varepsilon_0 R^2 E_0 t}{2r \\tau^2}\\hat{\\phi}$"
    ),
    "2023-2-emPT4b": (
        "Q. 24 [emPT4b]\n"
        "O campo elétrico no interior de um capacitor de placas paralelas circulares de raio $R$ varia linearmente no tempo como "
        "$\\vec{E}(t) = E_0 \\left(\\frac{t}{\\tau}\\right)\\hat{z}$.\n\n"
        "Qual é o campo magnético induzido $\\vec{B}(r,t)$ a uma distância radial $r < R$ do eixo central das placas?\n\n"
        "A $\\vec{B}(r,t) = \\frac{\\mu_0 \\varepsilon_0 r E_0}{2\\tau}\\hat{\\phi}$\n"
        "B $\\vec{B}(r,t) = \\frac{\\mu_0 \\varepsilon_0 r E_0}{\\tau}\\hat{\\phi}$\n"
        "C $\\vec{B}(r,t) = \\frac{\\pi r \\mu_0 \\varepsilon_0 E_0}{2\\tau}\\hat{\\phi}$\n"
        "D $\\vec{B}(r,t) = \\frac{\\mu_0 \\varepsilon_0 R^2 E_0}{2r \\tau}\\hat{\\phi}$\n"
        "E $\\vec{B}(r,t) = \\frac{2\\pi r \\mu_0 \\varepsilon_0 E_0}{\\tau}\\hat{\\phi}$"
    ),
    "2023-2-emPT5a": (
        "Q. 25 [emPT5a]\n"
        "Uma barra metálica muito fina, homogênea e de comprimento $d$ move-se sem girar e com velocidade constante $\\vec{v}$. "
        "A velocidade $\\vec{v}$ faz um ângulo $\\theta \\ne 0$ com a barra (ver figura). A barra move-se numa região onde há um campo "
        "magnético constante e uniforme $\\vec{B}$, perpendicular à barra e a $\\vec{v}$.\n\n"
        "Qual(is) das seguintes afirmações é(são) verdadeira(s)?\n"
        "I. Existe uma diferença de potencial elétrico não nula entre as extremidades da barra.\n"
        "II. A força magnética total sobre a barra em regime estacionário é nula.\n"
        "III. O torque magnético total sobre a barra em regime estacionário é nulo.\n\n"
        "A I, II e III\n"
        "B Apenas I e II\n"
        "C Apenas II e III\n"
        "D Apenas I\n"
        "E Apenas III"
    ),
    "2023-2-emPT5b": (
        "Q. 26 [emPT5b]\n"
        "Uma barra metálica muito fina, homogênea e de comprimento $d$ move-se sem girar e com velocidade constante $\\vec{v}$. "
        "A velocidade $\\vec{v}$ faz um ângulo $\\theta \\ne 0$ com a barra. A barra move-se numa região onde há um campo "
        "magnético constante e uniforme $\\vec{B}$, perpendicular à barra e a $\\vec{v}$.\n\n"
        "Qual(is) das seguintes afirmações é(são) verdadeira(s)?\n"
        "I. Existe uma diferença de potencial elétrico não nula entre as extremidades da barra.\n"
        "II. A força magnética total sobre a barra é não nula.\n"
        "III. O torque magnético total sobre a barra é não nulo.\n\n"
        "A Apenas I\n"
        "B I, II e III\n"
        "C Apenas I e II\n"
        "D Apenas II\n"
        "E Apenas III"
    ),
    "2023-2-emPT6a": (
        "Q. 27 [emPT6a]\n"
        "A figura ilustra um condutor elipsoidal, isolado e neutro, que possui uma cavidade esférica em seu interior. "
        "Uma carga pontual $q > 0$ está fixa no centro da cavidade esférica.\n\n"
        "Assinale a alternativa que melhor representa a distribuição de densidades superficiais de carga nas superfícies do condutor:\n\n"
        "A Carga superficial interna é uniforme e negativa ($-q$); carga superficial externa é positiva ($+q$) e concentrada nas regiões de maior curvatura.\n"
        "B Carga superficial interna é não-uniforme e negativa; carga superficial externa é uniforme e positiva.\n"
        "C Carga superficial interna e externa são ambas perfeitamente uniformes.\n"
        "D Carga superficial interna é nula e externa é uniforme ($+q$).\n"
        "E Carga superficial interna é $-q$ e externa é nula."
    ),
    "2023-2-emPT6b": (
        "Q. 28 [emPT6b]\n"
        "A figura ilustra um condutor cúbico, isolado e neutro, que possui uma cavidade esférica em seu interior. "
        "Uma carga pontual $q < 0$ está fixa no centro da cavidade esférica.\n\n"
        "Assinale a alternativa que melhor representa a distribuição de densidades superficiais de carga nas superfícies do condutor:\n\n"
        "A Carga superficial interna é uniforme e positiva ($+|q|$); carga superficial externa é negativa ($-|q|$) e concentrada nos vértices e arestas (maior curvatura).\n"
        "B Carga superficial interna é não-uniforme e positiva; carga superficial externa é uniforme e negativa.\n"
        "C Carga superficial interna e externa são ambas perfeitamente uniformes.\n"
        "D Carga superficial interna é nula e externa é $-|q|$.\n"
        "E Carga superficial interna é $+|q|$ e externa é nula."
    ),
    "2023-2-emPT7a": (
        "Q. 29 [emPT7a]\n"
        "Sangue fluindo em uma artéria de diâmetro $d = 8{,}0\\text{ mm}$ pode atingir velocidades de até $v = 60\\text{ cm/s}$ em módulo. "
        "Sabendo que há íons no plasma sanguíneo, estime a máxima diferença de potencial elétrico (tensão de Hall) que pode surgir nas paredes "
        "dessa artéria sob a ação de um campo magnético transversal de módulo $B = 0{,}20\\text{ T}$:\n\n"
        "A $\\Delta V = 0{,}96\\text{ mV}$\n"
        "B $\\Delta V = 9{,}6\\text{ mV}$\n"
        "C $\\Delta V = 9{,}6\\,\\mu\\text{V}$\n"
        "D $\\Delta V = 0{,}96\\,\\mu\\text{V}$\n"
        "E $\\Delta V = 96\\,\\mu\\text{V}$"
    ),
    "2023-2-emPT7b": (
        "Q. 30 [emPT7b]\n"
        "Sangue fluindo em uma artéria de diâmetro $d = 9{,}0\\text{ mm}$ pode atingir velocidades de até $v = 70\\text{ cm/s}$ em módulo. "
        "Sabendo que há íons no plasma sanguíneo, estime a máxima diferença de potencial elétrico (tensão de Hall) que pode surgir nas paredes "
        "dessa artéria sob a ação de um campo magnético transversal de módulo $B = 0{,}10\\text{ T}$:\n\n"
        "A $\\Delta V = 0{,}63\\text{ mV}$\n"
        "B $\\Delta V = 63\\,\\mu\\text{V}$\n"
        "C $\\Delta V = 6{,}3\\,\\mu\\text{V}$\n"
        "D $\\Delta V = 0{,}63\\,\\mu\\text{V}$\n"
        "E $\\Delta V = 6{,}3\\text{ mV}$"
    ),
    "2023-2-emPT8a": (
        "Q. 31 [emPT8a]\n"
        "A figura ilustra a seção reta de dois condutores cilíndricos paralelos idênticos e muito longos que transportam, em sentidos opostos, "
        "densidades de corrente de módulo $J$ uniformemente distribuídas. Essa distribuição é equivalente a dois cilindros de raio $R$ com eixos separados por $d < R$, "
        "onde as correntes se cancelam na região de superposição.\n\n"
        "Qual é o campo magnético $\\vec{B}$ no interior da região vazada (superposição), em função da distância entre eixos $\\vec{d}$?\n\n"
        "A $\\vec{B} = \\frac{\\mu_0 J d}{2}\\hat{y}$\n"
        "B $\\vec{B} = \\mu_0 J d \\hat{y}$\n"
        "C $\\vec{B} = -\\frac{\\mu_0 J d}{2}\\hat{y}$\n"
        "D $\\vec{B} = \\frac{\\mu_0 J R^2}{2d}\\hat{y}$\n"
        "E $\\vec{B} = 0$"
    ),
    "2023-2-emPT8b": (
        "Q. 32 [emPT8b]\n"
        "A figura ilustra a seção reta de dois condutores cilíndricos paralelos idênticos e muito longos que transportam, em sentidos opostos, "
        "densidades de corrente de módulo $J$ uniformemente distribuídas. Os eixos dos cilindros distam de $d < R$.\n\n"
        "O campo magnético $\\vec{B}$ em qualquer ponto no interior da cavidade (região de superposição) é:\n\n"
        "A Perfeitamente uniforme e dado por $\\vec{B} = \\frac{\\mu_0}{2}(\\vec{J}\\times\\vec{d})$\n"
        "B Nulo em todos os pontos da cavidade\n"
        "C Dependente linearmente da distância ao centro da cavidade\n"
        "D Dependente inversamente da distância ao centro da cavidade\n"
        "E Perfeitamente uniforme e dado por $\\vec{B} = \\mu_0 (\\vec{J}\\times\\vec{d})$"
    ),

    # =========================================================================
    # 2022-2 ELECTROMAGNETISM (14 Questions: emPT1a to emPT8b)
    # =========================================================================
    "2022-2-emPT1a": (
        "Q. 17 [emPT1a]\n"
        "Uma carga pontual $q$ é colocada no centro de uma das faces de um cubo de aresta $a$.\n\n"
        "Qual é o fluxo elétrico $\\Phi_E$ através de todas as outras 5 faces do cubo?\n\n"
        "A $\\Phi_E = \\frac{q}{2\\varepsilon_0}$\n"
        "B $\\Phi_E = \\frac{q}{4\\varepsilon_0}$\n"
        "C $\\Phi_E = \\frac{q}{6\\varepsilon_0}$\n"
        "D $\\Phi_E = \\frac{q}{8\\varepsilon_0}$\n"
        "E $\\Phi_E = \\frac{5q}{6\\varepsilon_0}$"
    ),
    "2022-2-emPT1b": (
        "Q. 18 [emPT1b]\n"
        "Uma carga pontual $q$ é colocada em um dos vértices de um cubo de aresta $a$.\n\n"
        "Qual é o fluxo elétrico $\\Phi_E$ através de todas as faces do cubo que não incluem o vértice no qual a carga está localizada?\n\n"
        "A $\\Phi_E = \\frac{q}{8\\varepsilon_0}$\n"
        "B $\\Phi_E = \\frac{q}{4\\varepsilon_0}$\n"
        "C $\\Phi_E = \\frac{q}{6\\varepsilon_0}$\n"
        "D $\\Phi_E = \\frac{q}{12\\varepsilon_0}$\n"
        "E $\\Phi_E = \\frac{q}{24\\varepsilon_0}$"
    ),
    "2022-2-emPT2a": (
        "Q. 19 [emPT2a]\n"
        "Um capacitor de placas paralelas é constituído por dois discos de raio $R$ separados por uma distância $d \\ll R$. "
        "O capacitor é carregado de modo que sua carga varia no tempo como $q(t) = q_0(1 - e^{-2t/\\tau})$, uniformemente distribuída nas placas.\n\n"
        "Qual é a corrente de deslocamento $i_d(t)$ entre as placas em função do tempo?\n\n"
        "A $i_d(t) = \\frac{2q_0}{\\tau} e^{-2t/\\tau}$\n"
        "B $i_d(t) = \\frac{q_0}{\\tau} e^{-2t/\\tau}$\n"
        "C $i_d(t) = \\frac{2q_0}{\\tau} e^{-t/\\tau}$\n"
        "D $i_d(t) = \\frac{q_0}{\\tau} e^{-t/\\tau}$\n"
        "E $i_d(t) = \\frac{q_0}{2\\tau} e^{-2t/\\tau}$"
    ),
    "2022-2-emPT2b": (
        "Q. 20 [emPT2b]\n"
        "Um capacitor de placas paralelas é constituído por dois discos de raio $R$ separados por uma distância $d \\ll R$. "
        "O capacitor é carregado de modo que sua carga varia no tempo como $q(t) = q_0(1 - e^{-t/\\tau})$, uniformemente distribuída nas placas.\n\n"
        "Qual é a corrente de deslocamento $i_d(t)$ entre as placas em função do tempo?\n\n"
        "A $i_d(t) = \\frac{q_0}{\\tau} e^{-t/\\tau}$\n"
        "B $i_d(t) = \\frac{q_0}{\\tau} e^{-2t/\\tau}$\n"
        "C $i_d(t) = \\frac{2q_0}{\\tau} e^{-t/\\tau}$\n"
        "D $i_d(t) = \\frac{2q_0}{\\tau} e^{-2t/\\tau}$\n"
        "E $i_d(t) = \\frac{q_0}{2\\tau} e^{-t/\\tau}$"
    ),
    "2022-2-emPT3a": (
        "Q. 21 [emPT3a]\n"
        "Em um certo instante uma partícula com carga $q$ se desloca com velocidade $\\vec{v}$ cuja direção é paralela a um fio infinito "
        "com densidade linear de carga $\\lambda > 0$ constante. A distância entre o fio e a partícula é $R$. O fio também transporta uma corrente "
        "elétrica $I$ no mesmo sentido de $\\vec{v}$.\n\n"
        "Qual deve ser o módulo da velocidade $v$ para que a partícula continue se deslocando paralelamente ao fio com trajetória retilínea?\n\n"
        "A $v = \\frac{\\lambda}{\\varepsilon_0 \\mu_0 I}$\n"
        "B $v = \\frac{\\lambda}{2\\pi \\varepsilon_0 \\mu_0 I}$\n"
        "C $v = \\frac{\\lambda}{4\\pi \\varepsilon_0 \\mu_0 I}$\n"
        "D $v = \\frac{2\\pi\\lambda}{\\varepsilon_0 \\mu_0 I}$\n"
        "E $v = \\frac{4\\pi\\lambda}{\\varepsilon_0 \\mu_0 I}$"
    ),
    "2022-2-emPT3b": (
        "Q. 22 [emPT3b]\n"
        "Em um certo instante uma partícula com carga $q$ se desloca com velocidade $\\vec{v}$ cuja direção é paralela a um fio infinito "
        "com densidade linear de carga $\\lambda > 0$ constante. A distância entre o fio e a partícula é $R$. O fio também transporta uma corrente "
        "elétrica $I$ no mesmo sentido de $\\vec{v}$.\n\n"
        "Qual deve ser o valor da corrente elétrica $I$ para que a partícula continue se deslocando paralelamente ao fio com trajetória retilínea?\n\n"
        "A $I = \\frac{\\lambda}{\\varepsilon_0 \\mu_0 v}$\n"
        "B $I = \\frac{\\lambda}{2\\pi \\varepsilon_0 \\mu_0 v}$\n"
        "C $I = \\frac{\\lambda}{4\\pi \\varepsilon_0 \\mu_0 v}$\n"
        "D $I = \\frac{2\\pi\\lambda}{\\varepsilon_0 \\mu_0 v}$\n"
        "E $I = \\frac{4\\pi\\lambda}{\\varepsilon_0 \\mu_0 v}$"
    ),
    "2022-2-emPT4a": (
        "Q. 23 [emPT4a]\n"
        "Um condutor cilíndrico longo, de raio interno $a$, raio externo $b$ e permeabilidade $\\mu_0$, transporta uma corrente elétrica $I$ "
        "com densidade de corrente uniforme em sua seção reta.\n\n"
        "Qual é o módulo do campo magnético $B(r)$ a uma distância radial $r = \\frac{a + b}{2}$ do eixo de simetria do condutor?\n\n"
        "A $B(r) = \\frac{\\mu_0 I (b + 3a)}{4\\pi(a + b)^2}$\n"
        "B $B(r) = \\frac{\\mu_0 I [(a+b)^2 - 2a^2]}{4\\pi(a+b)(b-a)^2}$\n"
        "C $B(r) = \\frac{\\mu_0 I}{2\\pi(a+b)}$\n"
        "D $B(r) = \\frac{\\mu_0 I (a+b)}{4\\pi(b^2 - a^2)}$\n"
        "E $B(r) = 0$"
    ),
    "2022-2-emPT4b": (
        "Q. 24 [emPT4b]\n"
        "Um condutor cilíndrico longo, de raio interno $a$, raio externo $b$ e permeabilidade $\\mu_0$, transporta uma corrente elétrica $I$ "
        "com densidade de corrente uniforme em sua seção reta.\n\n"
        "Qual é o módulo do campo magnético $B(r)$ a uma distância radial $r = \\frac{a + b}{2}$ do eixo de simetria do condutor?\n\n"
        "A $B(r) = \\frac{\\mu_0 I (b + 3a)}{4\\pi(a + b)^2}$\n"
        "B $B(r) = \\frac{\\mu_0 I [(a+b)^2 - 2a^2]}{4\\pi(a+b)(b-a)^2}$\n"
        "C $B(r) = \\frac{\\mu_0 I}{2\\pi(a+b)}$\n"
        "D $B(r) = \\frac{\\mu_0 I (a+b)}{4\\pi(b^2 - a^2)}$\n"
        "E $B(r) = 0$"
    ),
    "2022-2-emPT5a": (
        "Q. 25 [emPT5a]\n"
        "Uma esfera condutora de raio $a$ está inicialmente carregada com carga elétrica $q$. No instante $t = 0$, a esfera é aterrada "
        "através de um fio de resistência elétrica $R$.\n\n"
        "Qual é o módulo da corrente elétrica $i(t)$ no fio em função do tempo?\n\n"
        "A $i(t) = \\frac{q}{4\\pi\\varepsilon_0 R a} e^{-t/(4\\pi\\varepsilon_0 R a)}$\n"
        "B $i(t) = \\frac{q}{4\\pi\\varepsilon_0 R} e^{-t/(4\\pi\\varepsilon_0 R a)}$\n"
        "C $i(t) = \\frac{q a}{4\\pi\\varepsilon_0 R^2} e^{-t/(4\\pi\\varepsilon_0 R a)}$\n"
        "D $i(t) = \\frac{q}{4\\pi\\varepsilon_0 R a^2} e^{-t/(4\\pi\\varepsilon_0 R a)}$\n"
        "E $i(t) = \\frac{4\\pi q R a}{\\varepsilon_0} e^{-t/(4\\pi\\varepsilon_0 R a)}$"
    ),
    "2022-2-emPT5b": (
        "Q. 26 [emPT5b]\n"
        "Uma esfera condutora de raio $a$ está inicialmente carregada com carga elétrica $q$. No instante $t = 0$, a esfera é aterrada "
        "através de um fio de resistência elétrica $R$.\n\n"
        "Qual é a carga elétrica $q(t)$ restante na esfera em função do tempo?\n\n"
        "A $q(t) = q e^{-t/(4\\pi\\varepsilon_0 R a)}$\n"
        "B $q(t) = q e^{-t/(4\\pi\\varepsilon_0 R^2)}$\n"
        "C $q(t) = q e^{-t/(4\\pi\\varepsilon_0 a^2)}$\n"
        "D $q(t) = q e^{-t/(2\\pi\\varepsilon_0 R a)}$\n"
        "E $q(t) = q e^{-t/(\\varepsilon_0 R a)}$"
    ),
    "2022-2-emPT6a": (
        "Q. 27 [emPT6a]\n"
        "O circuito elétrico é alimentado por uma fonte ideal de tensão contínua $V$. O circuito contém um resistor ideal e um elemento não-ôhmico. "
        "Se a corrente total medida no circuito é $I = 3{,}0\\text{ mA}$, os possíveis valores para a tensão $V$ da fonte são:\n\n"
        "A $300\\text{ mV}$, ou $500\\text{ mV}$, ou $675\\text{ mV}$\n"
        "B necessariamente $250\\text{ mV}$\n"
        "C necessariamente $500\\text{ mV}$\n"
        "D $50\\text{ mV}$, ou $250\\text{ mV}$, ou $425\\text{ mV}$\n"
        "E Nenhuma das outras alternativas"
    ),
    "2022-2-emPT6b": (
        "Q. 28 [emPT6b]\n"
        "O circuito elétrico é alimentado por uma fonte ideal de tensão contínua $V$. O circuito contém um resistor ideal e um elemento não-ôhmico. "
        "Se a corrente que atravessa o componente desconhecido é $I = 1{,}5\\text{ mA}$, os possíveis valores para a tensão $V$ da fonte são:\n\n"
        "A $50\\text{ mV}$, ou $250\\text{ mV}$, ou $425\\text{ mV}$\n"
        "B necessariamente $250\\text{ mV}$\n"
        "C necessariamente $500\\text{ mV}$\n"
        "D $300\\text{ mV}$, ou $500\\text{ mV}$, ou $675\\text{ mV}$\n"
        "E Nenhuma das outras alternativas"
    ),
    "2022-2-emPT7a": (
        "Q. 29 [emPT7a]\n"
        "Um feixe de luz despolarizada incide consecutivamente sobre três polarizadores lineares ideais paralelos. "
        "O ângulo entre os eixos de polarização do primeiro e do segundo polarizador é $\\alpha$, e entre o primeiro e o terceiro é $\\theta$ ($0 \\le \\theta \\le \\pi/2$).\n\n"
        "Com relação à intensidade da luz que emerge do terceiro polarizador, pode-se afirmar que:\n\n"
        "A É máxima quando $\\alpha = \\theta/2$\n"
        "B É máxima quando $\\alpha = 0$ ou $\\alpha = \\theta$\n"
        "C É mínima quando $\\alpha = \\theta/2$\n"
        "D É mínima quando $\\alpha = 0$ ou $\\alpha = \\theta$\n"
        "E Nenhuma luz é transmitida quando $\\theta = \\pi/2$"
    ),
    "2022-2-emPT8a": (
        "Q. 31 [emPT8a]\n"
        "A figura ilustra um ímã permanente caindo sob a ação da gravidade dentro de um tubo de vidro vertical. "
        "O tubo está envolto por uma espira condutora conectada a um resistor.\n\n"
        "Assinale a alternativa que melhor descreve o comportamento da corrente elétrica induzida $i(t)$ no circuito em função do tempo:\n\n"
        "A Dois pulsos de polaridades opostas, com o segundo pulso apresentando maior amplitude e menor duração devido à aceleração da gravidade.\n"
        "B Um único pulso positivo simétrico centrado no instante de passagem pelo meio da espira.\n"
        "C Dois pulsos idênticos de mesma polaridade e mesma amplitude.\n"
        "D Uma corrente constante e positiva durante todo o tempo de queda.\n"
        "E Corrente nula durante toda a trajetória do ímã."
    ),
    "2022-2-emPT8b": (
        "Q. 32 [emPT8b]\n"
        "A figura ilustra um ímã permanente caindo sob a ação da gravidade dentro de um tubo de vidro vertical. "
        "O tubo está envolto por uma espira condutora conectada a um resistor de resistência $R$.\n\n"
        "Assinale a alternativa que melhor descreve a diferença de potencial elétrico $V_R(t)$ medida nos terminais do resistor em função do tempo:\n\n"
        "A Dois pulsos de sinais opostos, onde o segundo pulso tem maior amplitude que o primeiro pois a velocidade do ímã aumenta durante a queda.\n"
        "B Um pulso positivo e constante enquanto o ímã estiver dentro da espira.\n"
        "C Dois pulsos simétricos de mesmo sinal e mesma amplitude.\n"
        "D Uma onda senoidal contínua de amplitude constante.\n"
        "E Tensão nula durante todo o movimento."
    ),
}


def apply_em_reconstructions():
    print("=" * 65)
    print("⚡ RECONSTRUCTING ELECTROMAGNETISM QUESTIONS (LATEX + OPTIONS)")
    print("=" * 65)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    updated = 0
    for qid, clean_text in EM_RECONSTRUCTIONS.items():
        cur.execute("UPDATE questions SET text = ? WHERE id = ?", (clean_text, qid))
        if cur.rowcount > 0:
            updated += 1
            print(f"  ✓ Reconstructed {qid}")
        else:
            print(f"  ⚠ Question ID not found in DB: {qid}")

    conn.commit()
    conn.close()

    print(f"\n✅ Successfully updated {updated} Electromagnetism questions in SQLite.")
    print("🚀 Exporting updated questions.json...")
    export_bank_to_json()
    print("✨ Complete!")


if __name__ == "__main__":
    apply_em_reconstructions()
