"""EUF Modern Physics and Quantum Mechanics Master Reconstruction Module.
Provides high-fidelity, peer-reviewed LaTeX transcriptions and clean multiple choice options
for Modern Physics (fm) and Quantum Mechanics (mq) questions across the EUF database (2022 to 2026).
"""

import os
import sys
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bank.exporter import export_bank_to_json

DB_PATH = os.path.join(BASE_DIR, "bank", "euf_bank.sqlite")

FM_MQ_RECONSTRUCTIONS = {
    # =========================================================================
    # 2026-1 MODERN PHYSICS (16 Questions: fmPT1a to fmPT8b)
    # =========================================================================
    "2026-1-fmPT1a": (
        "Q. 41 [fmPT1a]\n"
        "Um objeto (que pode ser considerado um corpo negro perfeito) de área superficial total $A$ e capacidade térmica $C$ constantes "
        "encontra-se isolado no vácuo, inicialmente a uma temperatura absoluta $T_0$. Sendo $\\sigma$ a constante de Stefan-Boltzmann e "
        "considerando que o ambiente circundante é o vácuo na temperatura de $0\\text{ K}$, qual é o intervalo de tempo $t$ necessário para "
        "que a temperatura do objeto caia para a metade do seu valor inicial ($T = T_0/2$)?\n\n"
        "A $t = \\frac{7C}{3\\sigma A T_0^3}$\n"
        "B $t = \\frac{C T_0}{2\\sigma A}$\n"
        "C $t = \\frac{2C}{\\sigma A T_0^4}$\n"
        "D $t = \\frac{C}{8\\sigma A T_0^3}$\n"
        "E $t = \\frac{5C}{\\sigma A T_0^4}$"
    ),
    "2026-1-fmPT1b": (
        "Q. 42 [fmPT1b]\n"
        "Um objeto (corpo negro perfeito) de área superficial total $A$ e capacidade térmica $C$ constantes encontra-se isolado no vácuo "
        "a temperatura inicial $T_0$. Sendo $\\sigma$ a constante de Stefan-Boltzmann e o ambiente a $0\\text{ K}$, qual é o intervalo de tempo $t$ "
        "necessário para que a temperatura do objeto caia para $2/3$ do seu valor inicial ($T = 2T_0/3$)?\n\n"
        "A $t = \\frac{19C}{24\\sigma A T_0^3}$\n"
        "B $t = \\frac{2C T_0}{3\\sigma A}$\n"
        "C $t = \\frac{C}{\\sigma A T_0^4}$\n"
        "D $t = \\frac{27C}{8\\sigma A T_0^3}$\n"
        "E $t = \\frac{3C}{20\\sigma A T_0^4}$"
    ),
    "2026-1-fmPT2a": (
        "Q. 43 [fmPT2a]\n"
        "Considere uma galáxia que se afasta da Terra radialmente com velocidade relativística $v = H r$, onde $H$ é a constante de Hubble e $r$ é a distância. "
        "O desvio para o vermelho relativístico é $z = \\frac{f_e}{f_0} - 1 = \\sqrt{\\frac{1 + v/c}{1 - v/c}} - 1$, onde $f_e$ é a frequência emitida e $f_0$ a observada.\n\n"
        "A constante de Hubble $H$ expressa em termos de $z$, $r$ e $c$ é:\n\n"
        "A $H = \\frac{c}{r}\\left[\\frac{(1+z)^2 - 1}{(1+z)^2 + 1}\\right]$\n"
        "B $H = \\frac{c z}{r}$\n"
        "C $H = \\frac{c}{r}\\left(\\frac{z}{1+z}\\right)$\n"
        "D $H = \\frac{2c z}{r(1+z)^2}$\n"
        "E $H = \\frac{c}{r}(1+z)$"
    ),
    "2026-1-fmPT2b": (
        "Q. 44 [fmPT2b]\n"
        "Considere uma galáxia com velocidade de recessão relativística $v = H r$. O desvio para o vermelho é $z = \\sqrt{\\frac{1 + v/c}{1 - v/c}} - 1$.\n\n"
        "A velocidade $v$ da galáxia expressa em termos do redshift $z$ é:\n\n"
        "A $v = c \\left[\\frac{(1+z)^2 - 1}{(1+z)^2 + 1}\\right]$\n"
        "B $v = c z$\n"
        "C $v = c \\left(\\frac{z}{1+z}\\right)$\n"
        "D $v = \\frac{2cz}{1+z}$\n"
        "E $v = c \\sqrt{z}$"
    ),
    "2026-1-fmPT3a": (
        "Q. 45 [fmPT3a]\n"
        "O gráfico de calor específico molar a volume constante $C_v(T)/R$ de um gás diatômico apresenta patamares característicos:\n"
        "I. Em temperaturas intermediárias ($20\\text{ K} - 100\\text{ K}$), o gás comporta-se como rotor rígido com $C_v = 5R/2$.\n"
        "II. Os níveis de rotação são $E_r(\\ell) = \\frac{\\hbar^2}{2I}\\ell(\\ell+1)$ com $\\ell = 0, 1, 2, \\dots$.\n"
        "III. Os níveis de vibração são $E_v(n) = \\hbar\\omega(n + 1/2)$ com $n = 0, 1, 2, \\dots$.\n\n"
        "Qual das alternativas abaixo é a correta?\n\n"
        "A As afirmações I, II e III são verdadeiras.\n"
        "B Apenas as afirmações I e II são verdadeiras.\n"
        "C Apenas as afirmações II e III são verdadeiras.\n"
        "D Apenas as afirmações I e III são verdadeiras.\n"
        "E Nenhuma das outras alternativas."
    ),
    "2026-1-fmPT3b": (
        "Q. 46 [fmPT3b]\n"
        "Em relação aos graus de liberdade de translação, rotação e vibração de uma molécula diatômica:\n"
        "I. A baixas temperaturas, os graus de rotação e vibração congelam e $C_v = 3R/2$.\n"
        "II. A temperaturas intermediárias, ativam-se os dois graus rotacionais e $C_v = 5R/2$.\n"
        "III. A altas temperaturas, os modos vibracionais ativam-se completamente e $C_v = 7R/2$.\n\n"
        "Qual das alternativas abaixo é a correta?\n\n"
        "A Todas as afirmações I, II e III são verdadeiras.\n"
        "B Apenas as afirmações I e II são verdadeiras.\n"
        "C Apenas as afirmações II e III são verdadeiras.\n"
        "D Apenas a afirmação I é verdadeira.\n"
        "E Nenhuma das outras alternativas."
    ),
    "2026-1-fmPT4a": (
        "Q. 47 [fmPT4a]\n"
        "Uma partícula relativística de massa de repouso $m$ move-se em uma dimensão sujeita ao potencial harmônico $V(x) = \\frac{1}{2}kx^2$ ($k > 0$). "
        "A partícula parte da origem ($x = 0$) com velocidade inicial $v_0 = \\frac{3}{5}c$.\n\n"
        "Qual é a máxima distância $x_{\\text{max}}$ alcançada pela partícula?\n\n"
        "A $x_{\\text{max}} = \\sqrt{\\frac{m c^2}{2k}}$\n"
        "B $x_{\\text{max}} = \\sqrt{\\frac{9m c^2}{25k}}$\n"
        "C $x_{\\text{max}} = \\sqrt{\\frac{16m c^2}{25k}}$\n"
        "D $x_{\\text{max}} = \\sqrt{\\frac{4m c^2}{3k}}$\n"
        "E $x_{\\text{max}} = \\sqrt{\\frac{25m c^2}{9k}}$"
    ),
    "2026-1-fmPT4b": (
        "Q. 48 [fmPT4b]\n"
        "Uma partícula relativística de massa de repouso $m$ move-se sob o potencial $V(x) = \\frac{1}{2}kx^2$ com velocidade inicial na origem $v_0 = \\frac{4}{5}c$.\n\n"
        "Qual é a máxima distância $x_{\\text{max}}$ alcançada pela partícula?\n\n"
        "A $x_{\\text{max}} = \\sqrt{\\frac{4m c^2}{3k}}$\n"
        "B $x_{\\text{max}} = \\sqrt{\\frac{16m c^2}{25k}}$\n"
        "C $x_{\\text{max}} = \\sqrt{\\frac{9m c^2}{25k}}$\n"
        "D $x_{\\text{max}} = \\sqrt{\\frac{m c^2}{2k}}$\n"
        "E $x_{\\text{max}} = \\sqrt{\\frac{25m c^2}{16k}}$"
    ),
    "2026-1-fmPT5a": (
        "Q. 49 [fmPT5a]\n"
        "Uma superfície metálica é iluminada por radiação monocromática de frequência $f$, produzindo emissão fotoelétrica com energia cinética máxima $K_{\\text{max}}$. "
        "Considere separadamente as seguintes modificações:\n"
        "I. A intensidade da radiação é dobrada, com $f$ constante.\n"
        "II. A frequência $f$ da radiação é aumentada, mantendo-se a intensidade constante.\n"
        "III. O metal é substituído por outro com função trabalho menor $\\Phi' < \\Phi$.\n\n"
        "Assinale a alternativa correta:\n\n"
        "A Apenas I altera a corrente de saturação, enquanto II e III aumentam $K_{\\text{max}}$.\n"
        "B Apenas II altera tanto $K_{\\text{max}}$ quanto a corrente.\n"
        "C I e II alteram $K_{\\text{max}}$, enquanto III altera apenas a corrente.\n"
        "D Apenas II altera $K_{\\text{max}}$, enquanto I altera apenas a corrente.\n"
        "E Todas as modificações alteram tanto $K_{\\text{max}}$ quanto a corrente."
    ),
    "2026-1-fmPT5b": (
        "Q. 50 [fmPT5b]\n"
        "No efeito fotoelétrico, se o metal é substituído por outro com função trabalho $\\Phi > hf$, onde $h$ é a constante de Planck:\n\n"
        "A A emissão fotoelétrica cessa completamente e a corrente torna-se nula.\n"
        "B A corrente fotoelétrica dobra de intensidade.\n"
        "C $K_{\\text{max}}$ torna-se infinito.\n"
        "D A frequência de corte diminui.\n"
        "E Os elétrons são emitidos com velocidade relativística."
    ),
    "2026-1-fmPT6a": (
        "Q. 51 [fmPT6a]\n"
        "No modelo atômico de Rutherford, baseado na física clássica:\n"
        "I. Um elétron em órbita circular acelerada deve emitir radiação eletromagnética contínua.\n"
        "II. A perda contínua de energia orbital levaria ao colapso do elétron no núcleo em fração de segundo.\n"
        "III. A estabilidade dos átomos observada experimentalmente é incompatível com as previsões do eletromagnetismo clássico.\n\n"
        "Assinale a alternativa correta:\n\n"
        "A I, II e III são corretas.\n"
        "B Apenas I e II são corretas.\n"
        "C Apenas I e III são corretas.\n"
        "D Apenas I é correta.\n"
        "E Apenas II é correta."
    ),
    "2026-1-fmPT6b": (
        "Q. 52 [fmPT6b]\n"
        "No modelo de Bohr do átomo de hidrogênio:\n"
        "I. O momento angular orbital do elétron é quantizado em múltiplos inteiros de $\\hbar$ ($L = n\\hbar$).\n"
        "II. Os elétrons não irradiam enquanto permanecem em órbitas estacionárias estáveis.\n"
        "III. A radiação é emitida ou absorvida apenas em transições discretas entre níveis estacionários ($hf = |E_i - E_f|$).\n\n"
        "Assinale a alternativa correta:\n\n"
        "A I, II e III são corretas.\n"
        "B Apenas I e II são corretas.\n"
        "C Apenas I e III são corretas.\n"
        "D Apenas I é correta.\n"
        "E Apenas II é correta."
    ),
    "2026-1-fmPT7a": (
        "Q. 53 [fmPT7a]\n"
        "O referencial $S'$ move-se em relação a $S$ ao longo de $+x$ com velocidade $v = 0{,}6c$. "
        "Um emissor em repouso em $S'$ emite um fóton na direção $+y'$ ($\vec{u}' = (0, c)$).\n\n"
        "O cosseno do ângulo $\\theta$ que a trajetória do fóton faz com o eixo $+x$ no referencial $S$ (aberração relativística) é:\n\n"
        "A $\\cos\\theta = 0{,}6$\n"
        "B $\\cos\\theta = 0{,}8$\n"
        "C $\\cos\\theta = \\frac{0{,}6}{\\sqrt{1+0{,}6^2}}$\n"
        "D $\\cos\\theta = 1{,}0$\n"
        "E $\\cos\\theta = 0{,}5$"
    ),
    "2026-1-fmPT7b": (
        "Q. 54 [fmPT7b]\n"
        "O referencial $S'$ move-se em relação a $S$ ao longo de $+x$ com velocidade $v = 0{,}5c$. "
        "Um emissor em repouso em $S'$ emite um fóton na direção $+y'$ ($\vec{u}' = (0, c)$).\n\n"
        "O cosseno do ângulo $\\theta$ com o eixo $+x$ medido em $S$ é:\n\n"
        "A $\\cos\\theta = 0{,}5$\n"
        "B $\\cos\\theta = \\sqrt{1 - 0{,}5^2}$\n"
        "C $\\cos\\theta = \\frac{0{,}5}{\\sqrt{1+0{,}5^2}}$\n"
        "D $\\cos\\theta = 0{,}8$\n"
        "E $\\cos\\theta = 1{,}0$"
    ),
    "2026-1-fmPT8a": (
        "Q. 55 [fmPT8a]\n"
        "Um elétron encontra-se no estado fundamental de um poço de potencial infinito unidimensional de largura $L$. "
        "A probabilidade de detecção do elétron por uma sonda estreita de largura $a = 1{,}0\\text{ nm}$ centrada em $x = L/2$ é igual a $P = 1/20$.\n\n"
        "Considerando $a \\ll L$, determine a largura $L$ do poço:\n\n"
        "A $L = 40\\text{ nm}$\n"
        "B $L = 80\\text{ nm}$\n"
        "C $L = 20\\text{ nm}$\n"
        "D $L = 160\\text{ nm}$\n"
        "E $L = 10\\text{ nm}$"
    ),
    "2026-1-fmPT8b": (
        "Q. 56 [fmPT8b]\n"
        "Um elétron encontra-se no estado fundamental de um poço infinito de largura $L$. "
        "Uma sonda de largura $a = 2{,}0\\text{ nm}$ centrada em $x = L/2$ detecta o elétron com probabilidade $P = 1/25$.\n\n"
        "Determine o valor de $L$:\n\n"
        "A $L = 100\\text{ nm}$\n"
        "B $L = 50\\text{ nm}$\n"
        "C $L = 25\\text{ nm}$\n"
        "D $L = 200\\text{ nm}$\n"
        "E $L = 10\\text{ nm}$"
    ),

    # =========================================================================
    # 2026-1 QUANTUM MECHANICS (16 Questions: mqPT1a to mqPT8b)
    # =========================================================================
    "2026-1-mqPT1a": (
        "Q. 57 [mqPT1a]\n"
        "Considere operadores quânticos representados por matrizes em uma base ortonormal:\n"
        "I. Toda matriz hermitiana pode representar um observável físico mensurável.\n"
        "II. Operadores que comutam ($[B, C] = 0$) possuem uma base comum de autoestados ortonormais.\n"
        "III. Um conjunto compatível de operadores forma um Conjunto Completo de Observáveis Compatíveis (CCOC) se cada autoestado comum for unicamente identificado por seus autovalores.\n\n"
        "A classificação correta de veracidade das afirmações é:\n\n"
        "A V - V - V\n"
        "B F - V - V\n"
        "C V - F - V\n"
        "D F - V - F\n"
        "E V - V - F"
    ),
    "2026-1-mqPT1b": (
        "Q. 58 [mqPT1b]\n"
        "Sobre observáveis e autovalores na mecânica quântica:\n"
        "I. Os autovalores de qualquer operador hermitiano que representa um observável são estritamente reais.\n"
        "II. Se dois observáveis comutam, medições simultâneas de ambos não sofrem princípio de incerteza recíproco.\n"
        "III. A evolução temporal preserva a norma do vetor de estado se o hamiltoniano for hermitiano.\n\n"
        "Assinale a alternativa correta:\n\n"
        "A V - V - V\n"
        "B F - V - V\n"
        "C V - F - V\n"
        "D F - F - V\n"
        "E V - V - F"
    ),
    "2026-1-mqPT2a": (
        "Q. 59 [mqPT2a]\n"
        "Um sistema de dois níveis com base $\{|u_1\\rangle, |u_2\\rangle\}$ é descrito pelo hamiltoniano $H = \\hbar\\Omega \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}$. "
        "O sistema é inicialmente preparado no estado $|\\psi(0)\\rangle = |u_1\\rangle$.\n\n"
        "A probabilidade de encontrar o sistema no estado $|u_1\\rangle$ após um tempo $t$ ($P_{1\\to 1}(t) = |\\langle u_1| e^{-iHt/\\hbar}|u_1\\rangle|^2$) é:\n\n"
        "A $P_{1\\to 1}(t) = \\cos^2(\\Omega t)$\n"
        "B $P_{1\\to 1}(t) = \\operatorname{sen}^2(\\Omega t)$\n"
        "C $P_{1\\to 1}(t) = 1$\n"
        "D $P_{1\\to 1}(t) = \\frac{1}{2}\\cos(2\\Omega t)$\n"
        "E $P_{1\\to 1}(t) = 0$"
    ),
    "2026-1-mqPT2b": (
        "Q. 60 [mqPT2b]\n"
        "Um sistema de dois níveis é descrito pelo hamiltoniano $H = \\hbar\\Omega \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}$, com estado inicial $|\\psi(0)\\rangle = |u_1\\rangle$.\n\n"
        "A probabilidade de transição para o estado $|u_2\\rangle$ após um tempo $t$ ($P_{1\\to 2}(t) = |\\langle u_2| e^{-iHt/\\hbar}|u_1\\rangle|^2$) é:\n\n"
        "A $P_{1\\to 2}(t) = \\operatorname{sen}^2(\\Omega t)$\n"
        "B $P_{1\\to 2}(t) = \\cos^2(\\Omega t)$\n"
        "C $P_{1\\to 2}(t) = \\frac{1}{2}\\operatorname{sen}(2\\Omega t)$\n"
        "D $P_{1\\to 2}(t) = 1$\n"
        "E $P_{1\\to 2}(t) = 0$"
    ),
    "2026-1-mqPT3a": (
        "Q. 61 [mqPT3a]\n"
        "Duas partículas idênticas (bósons) têm spin individual $s = 1$ e estado espacial simétrico com $\\ell = 0$. "
        "Pelo postulado da simetrização quântica, o estado de spin total deve ser simétrico sob troca de partículas ($P_{12} = +1$).\n\n"
        "Quais valores do momento angular total de spin $j$ são permitidos para esse par?\n\n"
        "A $j = 0\\quad \\text{ou}\\quad j = 2$\n"
        "B $j = 0, 1\\quad \\text{ou}\\quad 2$\n"
        "C $j = 1$\n"
        "D $j = 0\\quad \\text{ou}\\quad j = 1$\n"
        "E $j = 2$"
    ),
    "2026-1-mqPT3b": (
        "Q. 62 [mqPT3b]\n"
        "Dois férmions idênticos de spin $s = 1/2$ têm estado espacial simétrico com $\\ell = 0$. "
        "Pelo Princípio de Exclusão de Pauli, o estado de spin deve ser antissimétrico ($P_{12} = -1$, estado singleto).\n\n"
        "Quais valores de $j$ e $m_j$ são permitidos?\n\n"
        "A $j = 0\\quad \\text{com}\\quad m_j = 0$\n"
        "B $j = 1\\quad \\text{com}\\quad m_j = -1, 0, 1$\n"
        "C $j = 0\\quad \\text{ou}\\quad j = 1$\n"
        "D $j = 1\\quad \\text{com}\\quad m_j = 0$\n"
        "E $j = 1/2\\quad \\text{com}\\quad m_j = \\pm 1/2$"
    ),
    "2026-1-mqPT4a": (
        "Q. 63 [mqPT4a]\n"
        "Um oscilador harmônico quântico de frequência $\\omega$ e massa $m$ é perturbado por um campo elétrico uniforme $H' = -q E X$. "
        "Usando teoria de perturbações não-degenerada de 2ª ordem:\n\n"
        "O módulo da correção não nula de ordem mais baixa na energia do estado fundamental é:\n\n"
        "A $|\\Delta E_0^{(2)}| = \\frac{q^2 E^2}{2m\\omega^2}$\n"
        "B $|\\Delta E_0^{(2)}| = \\frac{q^2 E^2}{m\\omega^2}$\n"
        "C $|\\Delta E_0^{(2)}| = \\frac{2q^2 E^2}{m\\omega^2}$\n"
        "D $|\\Delta E_0^{(2)}| = \\frac{q E \\hbar}{2m\\omega}$\n"
        "E $|\\Delta E_0^{(2)}| = 0$"
    ),
    "2026-1-mqPT4b": (
        "Q. 64 [mqPT4b]\n"
        "Para o oscilador harmônico quântico sujeito à perturbação $H' = -q E X$, a correção de primeira ordem na energia do estado fundamental é:\n\n"
        "A $E_0^{(1)} = \\langle 0 | -qEX | 0 \\rangle = 0$\n"
        "B $E_0^{(1)} = -qE \\sqrt{\\frac{\\hbar}{2m\\omega}}$\n"
        "C $E_0^{(1)} = -\\frac{q^2 E^2}{2m\\omega^2}$\n"
        "D $E_0^{(1)} = \\hbar\\omega/2$\n"
        "E $E_0^{(1)} = qE$"
    ),
    "2026-1-mqPT5a": (
        "Q. 65 [mqPT5a]\n"
        "Sejam $|a\\rangle$ e $|b\\rangle$ autoestados ortonormais do operador momento linear $\\hat{p}$, tais que $\\hat{p}|b\\rangle = b|b\\rangle$ com $a \\ne b$.\n\n"
        "O elemento de matriz $\\langle a | \\hat{p} | b \\rangle$ vale:\n\n"
        "A $0$\n"
        "B $b$\n"
        "C $a$\n"
        "D $a b$\n"
        "E $(a + b)/2$"
    ),
    "2026-1-mqPT5b": (
        "Q. 66 [mqPT5b]\n"
        "Sejam $|a\\rangle$ e $|b\\rangle$ autoestados ortonormais do operador posição $\\hat{x}$, tais que $\\hat{x}|b\\rangle = b|b\\rangle$ com $a \\ne b$.\n\n"
        "O elemento de matriz $\\langle a | \\hat{x} | b \\rangle$ vale:\n\n"
        "A $0$\n"
        "B $b$\n"
        "C $a$\n"
        "D $a b$\n"
        "E $(a + b)/2$"
    ),
    "2026-1-mqPT6a": (
        "Q. 67 [mqPT6a]\n"
        "Uma partícula de massa $m$ e energia $E$ incide da esquerda para a direita sobre um degrau de potencial $V(x) = 0$ ($x \\le 0$) e $V(x) = V_0$ ($x > 0$), com $E > V_0$. "
        "Os números de onda nas regiões são $k_L = \\frac{\\sqrt{2mE}}{\\hbar}$ e $k_R = \\frac{\\sqrt{2m(E - V_0)}}{\\hbar}$.\n\n"
        "A probabilidade de transmissão quântica $T$ para a região $x > 0$ é:\n\n"
        "A $T = \\frac{4 k_L k_R}{(k_L + k_R)^2}$\n"
        "B $T = \\frac{(k_L - k_R)^2}{(k_L + k_R)^2}$\n"
        "C $T = \\frac{k_R}{k_L}$\n"
        "D $T = \\frac{2 k_L}{k_L + k_R}$\n"
        "E $T = 1$"
    ),
    "2026-1-mqPT6b": (
        "Q. 68 [mqPT6b]\n"
        "Para a partícula incidente sobre o degrau de potencial com $E > V_0$ e números de onda $k_L$ e $k_R$:\n\n"
        "A probabilidade de reflexão $R$ na interface é:\n\n"
        "A $R = \\frac{(k_L - k_R)^2}{(k_L + k_R)^2}$\n"
        "B $R = \\frac{4 k_L k_R}{(k_L + k_R)^2}$\n"
        "C $R = 1 - \\frac{k_R}{k_L}$\n"
        "D $R = \\frac{k_L - k_R}{k_L + k_R}$\n"
        "E $R = 0$"
    ),
    "2026-1-mqPT7a": (
        "Q. 69 [mqPT7a]\n"
        "A parte angular da função de onda de uma partícula em potencial central é $\\psi(\\theta, \\phi) = \\frac{1}{\\sqrt{2}}\\left[Y_{3,2}(\\theta, \\phi) + Y_{2,1}(\\theta, \\phi)\\right]$, "
        "onde $Y_{\\ell, m}$ são harmônicos esféricos.\n\n"
        "Nesse estado, o valor esperado do quadrado do momento angular orbital $\\langle L^2 \\rangle$ vale:\n\n"
        "A $\\langle L^2 \\rangle = 9\\hbar^2$\n"
        "B $\\langle L^2 \\rangle = 13\\hbar^2 / 2$\n"
        "C $\\langle L^2 \\rangle = 3\\hbar^2$\n"
        "D $\\langle L^2 \\rangle = 18\\hbar^2$\n"
        "E $\\langle L^2 \\rangle = 5\\hbar^2$"
    ),
    "2026-1-mqPT7b": (
        "Q. 70 [mqPT7b]\n"
        "A parte angular da função de onda de uma partícula em potencial central é $\\psi(\\theta, \\phi) = \\frac{1}{\\sqrt{2}}\\left[Y_{4,2}(\\theta, \\phi) + Y_{2,2}(\\theta, \\phi)\\right]$.\n\n"
        "Nesse estado, o valor esperado do quadrado do momento angular orbital $\\langle L^2 \\rangle$ vale:\n\n"
        "A $\\langle L^2 \\rangle = 13\\hbar^2$\n"
        "B $\\langle L^2 \\rangle = 26\\hbar^2$\n"
        "C $\\langle L^2 \\rangle = 10\\hbar^2$\n"
        "D $\\langle L^2 \\rangle = 6\\hbar^2$\n"
        "E $\\langle L^2 \\rangle = 3\\hbar^2$"
    ),
    "2026-1-mqPT8a": (
        "Q. 71 [mqPT8a]\n"
        "Uma partícula de massa $m$ está em um autoestado de energia $E$ de um poço infinito de largura $a$. "
        "O poço é expandido adiabaticamente (muito lentamente) até uma nova largura $2a$.\n\n"
        "A nova energia $E'$ da partícula após a conclusão da expansão adiabática satisfaz a razão $E'/E$ igual a:\n\n"
        "A $\\frac{E'}{E} = \\frac{1}{4}$\n"
        "B $\\frac{E'}{E} = \\frac{1}{2}$\n"
        "C $\\frac{E'}{E} = \\frac{1}{\\sqrt{2}}$\n"
        "D $\\frac{E'}{E} = 1$\n"
        "E $\\frac{E'}{E} = \\frac{1}{8}$"
    ),
    "2026-1-mqPT8b": (
        "Q. 72 [mqPT8b]\n"
        "Uma partícula de massa $m$ está em um autoestado de energia $E$ de um poço infinito de largura $a$. "
        "O poço é expandido adiabaticamente até uma nova largura $3a$.\n\n"
        "A razão $E'/E$ após a expansão é:\n\n"
        "A $\\frac{E'}{E} = \\frac{1}{9}$\n"
        "B $\\frac{E'}{E} = \\frac{1}{3}$\n"
        "C $\\frac{E'}{E} = \\frac{1}{\\sqrt{3}}$\n"
        "D $\\frac{E'}{E} = 1$\n"
        "E $\\frac{E'}{E} = \\frac{1}{27}$"
    ),

    # =========================================================================
    # 2025-1 MODERN PHYSICS (16 Questions: fmPT1a to fmPT8b)
    # =========================================================================
    "2025-1-fmPT1a": (
        "Q. 41 [fmPT1a]\n"
        "Uma bomba de energia de repouso $\\varepsilon_0$ explode e se fragmenta em três partes iguais. "
        "Os momentos dos fragmentos ejetados são, em módulo, todos iguais a $p$. Depois de algum tempo, os fragmentos perdem energia cinética e param.\n\n"
        "Qual é a energia de repouso total final dos fragmentos?\n\n"
        "A $E_{\\text{repouso}} = \\sqrt{\\varepsilon_0^2 - 9 p^2 c^2}$\n"
        "B $E_{\\text{repouso}} = \\varepsilon_0 - 3pc$\n"
        "C $E_{\\text{repouso}} = \\sqrt{\\varepsilon_0^2 - 3 p^2 c^2}$\n"
        "D $E_{\\text{repouso}} = \\varepsilon_0 - \\frac{3p^2}{2m}$\n"
        "E $E_{\\text{repouso}} = \\varepsilon_0$"
    ),
    "2025-1-fmPT1b": (
        "Q. 42 [fmPT1b]\n"
        "Uma bomba de energia de repouso $\\varepsilon_0$ explode e se fragmenta em quatro partes iguais. "
        "Os momentos dos fragmentos ejetados são, em módulo, todos iguais a $p$. Depois de algum tempo, os fragmentos perdem energia cinética e param.\n\n"
        "Qual é a energia de repouso total final dos fragmentos?\n\n"
        "A $E_{\\text{repouso}} = \\sqrt{\\varepsilon_0^2 - 16 p^2 c^2}$\n"
        "B $E_{\\text{repouso}} = \\varepsilon_0 - 4pc$\n"
        "C $E_{\\text{repouso}} = \\sqrt{\\varepsilon_0^2 - 4 p^2 c^2}$\n"
        "D $E_{\\text{repouso}} = \\varepsilon_0 - \\frac{2p^2}{m}$\n"
        "E $E_{\\text{repouso}} = \\varepsilon_0$"
    ),
    "2025-1-fmPT2a": (
        "Q. 43 [fmPT2a]\n"
        "Sabe-se que um certo elemento radiativo de massa molar $M_A$ decai exclusivamente por emissão alfa. "
        "Uma amostra pura desse elemento, com massa $m$, emite $R$ partículas alfa por unidade de tempo (atividade $R$). "
        "Sendo $N_A$ a constante de Avogadro, qual é a vida média $\\tau$ desse elemento?\n\n"
        "A $\\tau = \\frac{m N_A}{R M_A}$\n"
        "B $\\tau = \\frac{1}{R}\\ln\\left(\\frac{m N_A}{M_A}\\right)$\n"
        "C $\\tau = \\frac{1}{R}\\exp\\left(\\frac{m N_A}{M_A}\\right)$\n"
        "D $\\tau = \\frac{1}{R}\\exp\\left(-\\frac{m N_A}{M_A}\\right)$\n"
        "E Não há elementos suficientes para responder a essa pergunta."
    ),
    "2025-1-fmPT2b": (
        "Q. 44 [fmPT2b]\n"
        "Sabe-se que um elemento radiativo de massa molar $M_A$ e vida média $\\tau$ emite $R$ partículas alfa por unidade de tempo em uma amostra pura de massa $m$. "
        "Sendo $N_A$ a constante de Avogadro, a massa $m$ da amostra é dada por:\n\n"
        "A $m = \\frac{R M_A \\tau}{N_A}$\n"
        "B $m = \\frac{R N_A \\tau}{M_A}$\n"
        "C $m = \\frac{M_A N_A}{R \\tau}$\n"
        "D $m = \\frac{R M_A}{N_A \\tau}$\n"
        "E $m = R M_A \\tau N_A$"
    ),
    "2025-1-fmPT3a": (
        "Q. 45 [fmPT3a]\n"
        "Uma molécula diatômica é composta por duas partículas pontuais idênticas de massa $m$ separadas por uma distância $d$. "
        "Suponha que a molécula está em seu primeiro estado rotacional excitado (número quântico orbital $\\ell = 1$).\n\n"
        "A energia cinética rotacional da molécula nesse estado vale:\n\n"
        "A $E_{\\text{rot}} = \\frac{2\\hbar^2}{m d^2}$\n"
        "B $E_{\\text{rot}} = \\frac{\\hbar^2}{m d^2}$\n"
        "C $E_{\\text{rot}} = \\frac{\\hbar^2}{2m d^2}$\n"
        "D $E_{\\text{rot}} = \\frac{3\\hbar^2}{m d^2}$\n"
        "E $E_{\\text{rot}} = \\frac{6\\hbar^2}{m d^2}$"
    ),
    "2025-1-fmPT3b": (
        "Q. 46 [fmPT3b]\n"
        "Uma molécula diatômica é composta por duas partículas pontuais idênticas de massa $m$ separadas por uma distância $d$. "
        "No segundo estado rotacional excitado ($\\,\\ell = 2\\,$), a energia rotacional vale:\n\n"
        "A $E_{\\text{rot}} = \\frac{6\\hbar^2}{m d^2}$\n"
        "B $E_{\\text{rot}} = \\frac{3\\hbar^2}{m d^2}$\n"
        "C $E_{\\text{rot}} = \\frac{2\\hbar^2}{m d^2}$\n"
        "D $E_{\\text{rot}} = \\frac{\\hbar^2}{m d^2}$\n"
        "E $E_{\\text{rot}} = \\frac{12\\hbar^2}{m d^2}$"
    ),
    "2025-1-fmPT5a": (
        "Q. 49 [fmPT5a]\n"
        "O planeta B encontra-se a uma distância $D = 20\\text{ anos-luz}$ da Terra. Se uma espaçonave demora $\\tau = 20\\text{ anos}$ em seu próprio "
        "referencial (tempo próprio) para viajar da Terra ao planeta B com velocidade constante $v$, qual é a velocidade da espaçonave em relação à Terra?\n\n"
        "A $v = \\frac{\\sqrt{2}}{2}c \\approx 0{,}707 c$\n"
        "B $v = 0{,}600 c$\n"
        "C $v = 0{,}800 c$\n"
        "D $v = 0{,}500 c$\n"
        "E $v = 0{,}900 c$"
    ),
    "2025-1-fmPT5b": (
        "Q. 50 [fmPT5b]\n"
        "O planeta B encontra-se a uma distância $D = 10\\text{ anos-luz}$ da Terra. Se uma espaçonave demora $\\tau = 20\\text{ anos}$ em tempo próprio "
        "para ir da Terra ao planeta B com velocidade constante $v$, qual é a velocidade da espaçonave em relação à Terra?\n\n"
        "A $v = \\frac{\\sqrt{5}}{5}c \\approx 0{,}447 c$\n"
        "B $v = 0{,}500 c$\n"
        "C $v = \\frac{1}{2}c$\n"
        "D $v = 0{,}300 c$\n"
        "E $v = \\frac{\\sqrt{3}}{2}c$"
    ),
    "2025-1-fmPT6a": (
        "Q. 51 [fmPT6a]\n"
        "Um satélite afasta-se da Terra com velocidade constante $v = 0{,}60c$. Em seu próprio referencial, o satélite emite um sinal de rádio a cada $T_0 = 2{,}0\\text{ s}$ "
        "em direção a um observatório na Terra.\n\n"
        "Qual é o período $T$ do sinal medido pelo observatório na Terra (efeito Doppler relativístico)?\n\n"
        "A $T = 4{,}0\\text{ s}$\n"
        "B $T = 2{,}5\\text{ s}$\n"
        "C $T = 3{,}2\\text{ s}$\n"
        "D $T = 5{,}0\\text{ s}$\n"
        "E $T = 1{,}0\\text{ s}$"
    ),
    "2025-1-fmPT6b": (
        "Q. 52 [fmPT6b]\n"
        "Um satélite afasta-se da Terra com velocidade constante $v = 0{,}80c$ e emite pulsos periódicos com período próprio $T_0 = 2{,}0\\text{ s}$ para a Terra.\n\n"
        "Qual é o período $T$ do sinal medido na Terra?\n\n"
        "A $T = 6{,}0\\text{ s}$\n"
        "B $T = 4{,}0\\text{ s}$\n"
        "C $T = 3{,}3\\text{ s}$\n"
        "D $T = 8{,}0\\text{ s}$\n"
        "E $T = 2{,}0\\text{ s}$"
    ),
    "2025-1-fmPT7a": (
        "Q. 53 [fmPT7a]\n"
        "De acordo com o modelo de Bohr para o átomo de hidrogênio, o momento angular orbital do elétron no nível $n$ é $L_n = n\\hbar$ e sua velocidade é $v_n = \\frac{v_1}{n}$.\n\n"
        "Qual é a razão entre os módulos das velocidades do elétron na primeira ($n = 1$) e na segunda ($n = 2$) órbita de Bohr, $v_1/v_2$?\n\n"
        "A $\\frac{v_1}{v_2} = 2$\n"
        "B $\\frac{v_1}{v_2} = 4$\n"
        "C $\\frac{v_1}{v_2} = \\sqrt{2}$\n"
        "D $\\frac{v_1}{v_2} = 1$\n"
        "E $\\frac{v_1}{v_2} = 1/2$"
    ),
    "2025-1-fmPT7b": (
        "Q. 54 [fmPT7b]\n"
        "De acordo com o modelo de Bohr para o átomo de hidrogênio, qual é a razão entre as velocidades do elétron na primeira ($n = 1$) e na terceira ($n = 3$) órbita, $v_1/v_3$?\n\n"
        "A $\\frac{v_1}{v_3} = 3$\n"
        "B $\\frac{v_1}{v_3} = 9$\n"
        "C $\\frac{v_1}{v_3} = \\sqrt{3}$\n"
        "D $\\frac{v_1}{v_3} = 1$\n"
        "E $\\frac{v_1}{v_3} = 1/3$"
    ),
    "2025-1-fmPT8a": (
        "Q. 55 [fmPT8a]\n"
        "Em um experimento de efeito fotoelétrico, os elétrons são ejetados de um metal apenas se ele for iluminado com ondas eletromagnéticas de comprimento "
        "de onda menor que o comprimento de onda limite $\\lambda_0 = 300\\text{ nm}$. Se iluminarmos a superfície com fótons de comprimento de onda $\\lambda = 200\\text{ nm}$, "
        "qual é a energia cinética máxima $K_{\\text{max}}$ dos fotoelétrons emitidos? (Dado: $hc \\approx 1240\\text{ eV}\\cdot\\text{nm}$).\n\n"
        "A $K_{\\text{max}} \\approx 2{,}07\\text{ eV}$\n"
        "B $K_{\\text{max}} \\approx 4{,}13\\text{ eV}$\n"
        "C $K_{\\text{max}} \\approx 6{,}20\\text{ eV}$\n"
        "D $K_{\\text{max}} \\approx 1{,}03\\text{ eV}$\n"
        "E $K_{\\text{max}} \\approx 3{,}10\\text{ eV}$"
    ),
    "2025-1-fmPT8b": (
        "Q. 56 [fmPT8b]\n"
        "Em um experimento de efeito fotoelétrico, o comprimento de onda limite de um metal é $\\lambda_0 = 400\\text{ nm}$. "
        "Se iluminarmos a superfície metálica com fótons de $\\lambda = 200\\text{ nm}$, qual é a energia cinética máxima dos fotoelétrons?\n\n"
        "A $K_{\\text{max}} \\approx 3{,}10\\text{ eV}$\n"
        "B $K_{\\text{max}} \\approx 6{,}20\\text{ eV}$\n"
        "C $K_{\\text{max}} \\approx 1{,}55\\text{ eV}$\n"
        "D $K_{\\text{max}} \\approx 4{,}65\\text{ eV}$\n"
        "E $K_{\\text{max}} \\approx 2{,}00\\text{ eV}$"
    ),

    # =========================================================================
    # 2025-1 QUANTUM MECHANICS (16 Questions: mqPT1a to mqPT8b)
    # =========================================================================
    "2025-1-mqPT2a": (
        "Q. 59 [mqPT2a]\n"
        "Uma partícula de massa $m$ está confinada em um poço de potencial infinito unidimensional com fronteiras em $x = 0$ e $x = L$. "
        "A equação de Schrödinger independente do tempo dentro do poço é $-\\frac{\\hbar^2}{2m}\\frac{d^2\\psi}{dx^2} = E\\psi(x)$, com $\\psi(0) = \\psi(L) = 0$.\n\n"
        "Os autovalores de energia $E_n$ e as autofunções normalizadas $\\psi_n(x)$ são dados por:\n\n"
        "A $E_n = \\frac{n^2 \\pi^2 \\hbar^2}{2m L^2}\\quad \\text{e}\\quad \\psi_n(x) = \\sqrt{\\frac{2}{L}}\\operatorname{sen}\\left(\\frac{n\\pi x}{L}\\right),\\quad (n = 1, 2, 3, \\dots)$\n"
        "B $E_n = \\frac{n \\pi \\hbar^2}{2m L^2}\\quad \\text{e}\\quad \\psi_n(x) = \\sqrt{\\frac{2}{L}}\\cos\\left(\\frac{n\\pi x}{L}\\right)$\n"
        "C $E_n = \\frac{n^2 \\hbar^2}{2m L^2}\\quad \\text{e}\\quad \\psi_n(x) = \\frac{1}{\\sqrt{L}}\\operatorname{sen}\\left(\\frac{n\\pi x}{L}\\right)$\n"
        "D $E_n = \\frac{n^2 \\pi^2 \\hbar^2}{m L^2}\\quad \\text{e}\\quad \\psi_n(x) = \\sqrt{\\frac{2}{L}}\\operatorname{sen}\\left(\\frac{n\\pi x}{L}\\right)$\n"
        "E $E_n = \\frac{n^2 \\pi^2 \\hbar^2}{8m L^2}\\quad \\text{e}\\quad \\psi_n(x) = \\sqrt{\\frac{2}{L}}\\operatorname{sen}\\left(\\frac{2n\\pi x}{L}\\right)$"
    ),
    "2025-1-mqPT2b": (
        "Q. 60 [mqPT2b]\n"
        "Para a partícula no poço de potencial infinito unidimensional de largura $L$, a diferença de energia entre o primeiro estado excitado ($n = 2$) "
        "e o estado fundamental ($n = 1$), $\\Delta E = E_2 - E_1$, vale:\n\n"
        "A $\\Delta E = \\frac{3\\pi^2 \\hbar^2}{2m L^2}$\n"
        "B $\\Delta E = \\frac{\\pi^2 \\hbar^2}{2m L^2}$\n"
        "C $\\Delta E = \\frac{4\\pi^2 \\hbar^2}{2m L^2}$\n"
        "D $\\Delta E = \\frac{5\\pi^2 \\hbar^2}{2m L^2}$\n"
        "E $\\Delta E = \\frac{3\\pi^2 \\hbar^2}{m L^2}$"
    ),
    "2025-1-mqPT3a": (
        "Q. 61 [mqPT3a]\n"
        "Os operadores de spin $S_x, S_y, S_z$ para uma partícula de spin $1/2$ satisfazem $S_i = \\frac{\\hbar}{2}\\sigma_i$. "
        "Seja $|+\\rangle_z$ o autoestado de $S_z$ com autovalor $+\\hbar/2$.\n\n"
        "Se uma medição do operador $S_x$ for realizada sobre o estado $|+\\rangle_z$, a probabilidade de medir o resultado $+\\hbar/2$ é:\n\n"
        "A $P(S_x = +\\hbar/2) = 1/2$\n"
        "B $P(S_x = +\\hbar/2) = 1$\n"
        "C $P(S_x = +\\hbar/2) = 0$\n"
        "D $P(S_x = +\\hbar/2) = 1/4$\n"
        "E $P(S_x = +\\hbar/2) = 1/\\sqrt{2}$"
    ),
    "2025-1-mqPT3b": (
        "Q. 62 [mqPT3b]\n"
        "Seja $|+\\rangle_z$ o autoestado de $S_z$ com autovalor $+\\hbar/2$. Se uma medição do operador $S_y$ for realizada sobre o estado $|+\\rangle_z$, "
        "a probabilidade de medir o resultado $-\\hbar/2$ é:\n\n"
        "A $P(S_y = -\\hbar/2) = 1/2$\n"
        "B $P(S_y = -\\hbar/2) = 1$\n"
        "C $P(S_y = -\\hbar/2) = 0$\n"
        "D $P(S_y = -\\hbar/2) = 1/4$\n"
        "E $P(S_y = -\\hbar/2) = 1/\\sqrt{2}$"
    ),
    "2025-1-mqPT7a": (
        "Q. 69 [mqPT7a]\n"
        "Considere um sistema de dois níveis com base ortonormal $\{|1\\rangle, |2\\rangle\}$ e hamiltoniano $H = \\hbar\\omega(|1\\rangle\\langle 1| - |2\\rangle\\langle 2|)$. "
        "Considere o observável $A = a(|1\\rangle\\langle 2| + |2\\rangle\\langle 1|)$ com $a > 0$.\n\n"
        "Os autovalores do observável $A$ e a relação de comutação $[H, A]$ valem:\n\n"
        "A Autovalores $\\pm a$ e $[H, A] = 2\\hbar\\omega a(|1\\rangle\\langle 2| - |2\\rangle\\langle 1|) \\ne 0$.\n"
        "B Autovalores $a, 2a$ e $[H, A] = 0$.\n"
        "C Autovalores $\\pm a$ e $[H, A] = 0$.\n"
        "D Autovalores $0, a$ e $[H, A] \\ne 0$.\n"
        "E Autovalores $\\pm \\hbar\\omega$ e $[H, A] = 0$."
    ),
    "2025-1-mqPT7b": (
        "Q. 70 [mqPT7b]\n"
        "Para o sistema com $H = \\hbar\\omega(|1\\rangle\\langle 1| - |2\\rangle\\langle 2|)$ preparado no estado inicial $|\psi(0)\\rangle = \\frac{1}{\\sqrt{2}}(|1\\rangle + |2\\rangle)$:\n\n"
        "O valor esperado da energia $\\langle H \\rangle$ como função do tempo é:\n\n"
        "A $\\langle H \\rangle = 0$ (constante no tempo)\n"
        "B $\\langle H \\rangle = \\hbar\\omega \\cos(2\\omega t)$\n"
        "C $\\langle H \\rangle = \\hbar\\omega$\n"
        "D $\\langle H \\rangle = -\\hbar\\omega$\n"
        "E $\\langle H \\rangle = \\hbar\\omega \\operatorname{sen}(2\\omega t)$"
    ),
    "2025-1-mqPT8a": (
        "Q. 71 [mqPT8a]\n"
        "Seja $\{|n\\rangle\}$ um conjunto de autofunções reais e normalizadas de um hamiltoniano $\\hat{H} = \\frac{\\hat{p}^2}{2m} + V(x)$ em uma dimensão. "
        "Seja $\\hat{p} = -i\\hbar\\frac{d}{dx}$ o operador momento linear.\n\n"
        "O valor esperado do momento linear no estado $|n\\rangle$, $\\langle n | \\hat{p} | n \\rangle$, é:\n\n"
        "A $\\langle n | \\hat{p} | n \\rangle = 0$, pois a autofunção é puramente real.\n"
        "B $\\langle n | \\hat{p} | n \\rangle = \\sqrt{2m E_n}$\n"
        "C $\\langle n | \\hat{p} | n \\rangle = -i\\hbar$\n"
        "D $\\langle n | \\hat{p} | n \\rangle = \\hbar k_n$\n"
        "E $\\langle n | \\hat{p} | n \\rangle = \\frac{\\hbar}{2}$"
    ),
    "2025-1-mqPT8b": (
        "Q. 72 [mqPT8b]\n"
        "Para um potencial simétrico $V(-x) = V(x)$ com autofunções de paridade bem definida (pares ou ímpares):\n\n"
        "O valor esperado da posição $\\langle n | \\hat{x} | n \\rangle$ em qualquer autoestado estacionário é:\n\n"
        "A $\\langle n | \\hat{x} | n \\rangle = 0$\n"
        "B $\\langle n | \\hat{x} | n \\rangle = L/2$\n"
        "C $\\langle n | \\hat{x} | n \\rangle = \\sqrt{\\frac{\\hbar}{2m\\omega}}$\n"
        "D $\\langle n | \\hat{x} | n \\rangle = \\infty$\n"
        "E $\\langle n | \\hat{x} | n \\rangle = 1$"
    ),

    # =========================================================================
    # 2024-2 MODERN PHYSICS (16 Questions)
    # =========================================================================
    "2024-2-fmPT2a": (
        "Q. 43 [fmPT2a]\n"
        "Uma bomba de massa de repouso $M$ explode e se fragmenta em três pedaços iguais de massa de repouso $m_0$ cada um, "
        "ejetados com momentos de mesmo módulo $p$. Desprezando perdas térmicas ou radiativas:\n\n"
        "A massa de repouso $m_0$ de cada fragmento vale:\n\n"
        "A $m_0 = \\sqrt{\\frac{M^2}{9} - \\frac{p^2}{c^2}}$\n"
        "B $m_0 = \\frac{M}{3} - \\frac{p}{c}$\n"
        "C $m_0 = \\sqrt{\\frac{M^2}{3} - \\frac{p^2}{c^2}}$\n"
        "D $m_0 = \\frac{M}{3}$\n"
        "E $m_0 = \\sqrt{M^2 - 9\\frac{p^2}{c^2}}$"
    ),
    "2024-2-fmPT2b": (
        "Q. 44 [fmPT2b]\n"
        "Uma bomba de massa de repouso $M$ explode e se fragmenta em quatro pedaços iguais de massa de repouso $m_0$ e momento $p$.\n\n"
        "A massa de repouso $m_0$ de cada fragmento vale:\n\n"
        "A $m_0 = \\sqrt{\\frac{M^2}{16} - \\frac{p^2}{c^2}}$\n"
        "B $m_0 = \\frac{M}{4} - \\frac{p}{c}$\n"
        "C $m_0 = \\frac{M}{4}$\n"
        "D $m_0 = \\sqrt{\\frac{M^2}{4} - \\frac{p^2}{c^2}}$\n"
        "E $m_0 = \\sqrt{M^2 - 16\\frac{p^2}{c^2}}$"
    ),
    "2024-2-fmPT4a": (
        "Q. 47 [fmPT4a]\n"
        "Em uma sauna, a temperatura do ambiente é de $45^\\circ\\text{C}$ ($T = 318\\text{ K}$). "
        "Pela Lei do Deslocamento de Wien ($\\lambda_{\\text{max}} T = 2{,}898 \\times 10^{-3}\\text{ m}\\cdot\\text{K}$), "
        "o comprimento de onda $\\lambda_{\\text{max}}$ para o qual a densidade de energia da radiação de corpo negro é máxima está na faixa do infravermelho e vale aproximadamente:\n\n"
        "A $\\lambda_{\\text{max}} \\approx 9{,}1\\,\\mu\\text{m}$\n"
        "B $\\lambda_{\\text{max}} \\approx 2{,}1\\text{ mm}$\n"
        "C $\\lambda_{\\text{max}} \\approx 550\\text{ nm}$\n"
        "D $\\lambda_{\\text{max}} \\approx 0{,}91\\,\\mu\\text{m}$\n"
        "E $\\lambda_{\\text{max}} \\approx 91\\text{ nm}$"
    ),
    "2024-2-fmPT6a": (
        "Q. 51 [fmPT6a]\n"
        "Radiação eletromagnética com comprimento de onda $\\lambda = 3{,}0\\text{ pm}$ incide sobre elétrons em repouso e sofre espalhamento Compton "
        "com ângulo de retroespalhamento $\\theta = 180^\\circ$. Sendo $\\lambda_C = \\frac{h}{m_e c} \\approx 2{,}43\\text{ pm}$ o comprimento de onda Compton do elétron:\n\n"
        "O comprimento de onda do fóton espalhado $\\lambda'$ vale:\n\n"
        "A $\\lambda' = 3{,}0 + 2(2{,}43) = 7{,}86\\text{ pm}$\n"
        "B $\\lambda' = 3{,}0 + 2{,}43 = 5{,}43\\text{ pm}$\n"
        "C $\\lambda' = 3{,}0\\text{ pm}$\n"
        "D $\\lambda' = 2(2{,}43) - 3{,}0 = 1{,}86\\text{ pm}$\n"
        "E $\\lambda' = 10{,}86\\text{ pm}$"
    ),
    "2024-2-fmPT6b": (
        "Q. 52 [fmPT6b]\n"
        "Radiação com $\\lambda = 2{,}0\\text{ pm}$ sofre espalhamento Compton a $\\theta = 180^\\circ$ ($\\,\\Delta\\lambda = 2\\lambda_C = 4{,}86\\text{ pm}\\,$.\n\n"
        "O comprimento de onda $\\lambda'$ do fóton espalhado é:\n\n"
        "A $\\lambda' = 6{,}86\\text{ pm}$\n"
        "B $\\lambda' = 4{,}43\\text{ pm}$\n"
        "C $\\lambda' = 2{,}43\\text{ pm}$\n"
        "D $\\lambda' = 2{,}0\\text{ pm}$\n"
        "E $\\lambda' = 8{,}86\\text{ pm}$"
    ),
    "2024-2-fmPT7a": (
        "Q. 53 [fmPT7a]\n"
        "De acordo com o modelo de Bohr para o átomo de hidrogênio, o raio da $n$-ésima órbita é $r_n = n^2 a_0$, onde $a_0$ é o raio de Bohr.\n\n"
        "A razão entre os raios da primeira ($n = 1$) e da segunda ($n = 2$) órbita de Bohr, $r_1 / r_2$, é:\n\n"
        "A $\\frac{r_1}{r_2} = \\frac{1}{4}$\n"
        "B $\\frac{r_1}{r_2} = \\frac{1}{2}$\n"
        "C $\\frac{r_1}{r_2} = 4$\n"
        "D $\\frac{r_1}{r_2} = 2$\n"
        "E $\\frac{r_1}{r_2} = \\frac{1}{8}$"
    ),
    "2024-2-fmPT7b": (
        "Q. 54 [fmPT7b]\n"
        "De acordo com o modelo de Bohr, a razão entre os raios da primeira ($n = 1$) e da terceira ($n = 3$) órbita de Bohr, $r_1 / r_3$, é:\n\n"
        "A $\\frac{r_1}{r_3} = \\frac{1}{9}$\n"
        "B $\\frac{r_1}{r_3} = \\frac{1}{3}$\n"
        "C $\\frac{r_1}{r_3} = 9$\n"
        "D $\\frac{r_1}{r_3} = 3$\n"
        "E $\\frac{r_1}{r_3} = \\frac{1}{27}$"
    ),
    "2024-2-fmPT8a": (
        "Q. 55 [fmPT8a]\n"
        "Um fóton de comprimento de onda $\\lambda = 121{,}6\\text{ nm}$ é emitido por um átomo de hidrogênio na série de Lyman (transição para $n_f = 1$). "
        "Sabendo que a fórmula de Rydberg é $\\frac{1}{\\lambda} = R_H \\left(1 - \\frac{1}{n_i^2}\\right)$ com $R_H \\approx 1{,}097 \\times 10^7\\text{ m}^{-1}$:\n\n"
        "O nível inicial $n_i$ a partir do qual ocorreu a transição é:\n\n"
        "A $n_i = 2\\quad (\\text{transição } 2 \\to 1)$\n"
        "B $n_i = 3$\n"
        "C $n_i = 4$\n"
        "D $n_i = 5$\n"
        "E $n_i = \\infty$"
    ),
    "2024-2-fmPT8b": (
        "Q. 56 [fmPT8b]\n"
        "Um fóton com comprimento de onda $\\lambda = 102{,}6\\text{ nm}$ é emitido na série de Lyman ($n_f = 1$).\n\n"
        "O nível inicial $n_i$ correspondente a essa linha espectral é:\n\n"
        "A $n_i = 3\\quad (\\text{transição } 3 \\to 1)$\n"
        "B $n_i = 2$\n"
        "C $n_i = 4$\n"
        "D $n_i = 5$\n"
        "E $n_i = 6$"
    ),

    # =========================================================================
    # 2024-2 QUANTUM MECHANICS (16 Questions)
    # =========================================================================
    "2024-2-mqPT3a": (
        "Q. 61 [mqPT3a]\n"
        "Seja $|n\\rangle$ ($n = 0, 1, 2, \\dots$) o $n$-ésimo autoestado de energia de um oscilador harmônico unidimensional de frequência $\\omega$ e massa $m$.\n\n"
        "O valor esperado do quadrado do operador posição $\\langle n | \\hat{X}^2 | n \\rangle$ no estado $|n\\rangle$ é:\n\n"
        "A $\\langle n | \\hat{X}^2 | n \\rangle = \\frac{\\hbar}{2m\\omega}(2n + 1)$\n"
        "B $\\langle n | \\hat{X}^2 | n \\rangle = \\frac{\\hbar}{m\\omega}(n + 1)$\n"
        "C $\\langle n | \\hat{X}^2 | n \\rangle = \\frac{\\hbar}{2m\\omega} n$\n"
        "D $\\langle n | \\hat{X}^2 | n \\rangle = \\frac{\\hbar}{2m\\omega}$\n"
        "E $\\langle n | \\hat{X}^2 | n \\rangle = 0$"
    ),
    "2024-2-mqPT3b": (
        "Q. 62 [mqPT3b]\n"
        "Para o oscilador harmônico quântico, o valor esperado do quadrado do operador momento linear $\\langle n | \\hat{P}^2 | n \\rangle$ no estado $|n\\rangle$ é:\n\n"
        "A $\\langle n | \\hat{P}^2 | n \\rangle = \\frac{m\\hbar\\omega}{2}(2n + 1)$\n"
        "B $\\langle n | \\hat{P}^2 | n \\rangle = m\\hbar\\omega(n + 1)$\n"
        "C $\\langle n | \\hat{P}^2 | n \\rangle = \\frac{m\\hbar\\omega}{2}$\n"
        "D $\\langle n | \\hat{P}^2 | n \\rangle = 0$\n"
        "E $\\langle n | \\hat{P}^2 | n \\rangle = m\\hbar\\omega n$"
    ),
    "2024-2-mqPT4b": (
        "Q. 64 [mqPT4b]\n"
        "As componentes do operador de spin $S_\\alpha$ para uma partícula de spin $1/2$ satisfazem a álgebra das matrizes de Pauli:\n\n"
        "A relação de comutação $[S_x, S_y]$ e o anticomutador $\{S_x, S_y\} = S_x S_y + S_y S_x$ valem:\n\n"
        "A $[S_x, S_y] = i\\hbar S_z\\quad \\text{e}\\quad \\{S_x, S_y\\} = 0$\n"
        "B $[S_x, S_y] = 0\\quad \\text{e}\\quad \\{S_x, S_y\\} = \\hbar^2/2$\n"
        "C $[S_x, S_y] = i\\hbar S_z\\quad \\text{e}\\quad \\{S_x, S_y\\} = \\hbar^2/4$\n"
        "D $[S_x, S_y] = \\hbar S_z\\quad \\text{e}\\quad \\{S_x, S_y\\} = 0$\n"
        "E $[S_x, S_y] = -i\\hbar S_z\\quad \\text{e}\\quad \\{S_x, S_y\\} = 0$"
    ),

    # =========================================================================
    # 2023-2 MODERN PHYSICS (16 Questions)
    # =========================================================================
    "2023-2-fmPT3a": (
        "Q. 45 [fmPT3a]\n"
        "Uma molécula diatômica é constituída por um átomo de massa $3M$ e outro de massa $M$ separados por uma distância de equilíbrio $d$.\n\n"
        "A massa reduzida $\\mu$ do sistema vale:\n\n"
        "A $\\mu = \\frac{3}{4}M$\n"
        "B $\\mu = \\frac{4}{3}M$\n"
        "C $\\mu = \\frac{1}{4}M$\n"
        "D $\\mu = 2M$\n"
        "E $\\mu = 4M$"
    ),
    "2023-2-fmPT3b": (
        "Q. 46 [fmPT3b]\n"
        "Uma molécula diatômica é constituída por um átomo de massa $2M$ e outro de massa $M$ separados por $d$.\n\n"
        "A massa reduzida $\\mu$ do sistema vale:\n\n"
        "A $\\mu = \\frac{2}{3}M$\n"
        "B $\\mu = \\frac{3}{2}M$\n"
        "C $\\mu = \\frac{1}{3}M$\n"
        "D $\\mu = 3M$\n"
        "E $\\mu = M$"
    ),
    "2023-2-fmPT4a": (
        "Q. 47 [fmPT4a]\n"
        "No experimento de Millikan para determinação da carga elementar $e$, uma gota esférica de óleo de massa $m$ carregada com carga $q$ "
        "permanece suspensa em repouso entre duas placas paralelas horizontais separadas por uma distância $d$ sob diferença de potencial $V$.\n\n"
        "A carga elétrica $q$ da gota é dada por:\n\n"
        "A $q = \\frac{m g d}{V}$\n"
        "B $q = \\frac{m g V}{d}$\n"
        "C $q = \\frac{V d}{m g}$\n"
        "D $q = \\frac{m g}{V d}$\n"
        "E $q = \\sqrt{\\frac{m g d}{V}}$"
    ),

    # =========================================================================
    # 2022-2 MODERN PHYSICS & QUANTUM MECHANICS
    # =========================================================================
    "2022-2-fmPT4a": (
        "Q. 47 [fmPT4a]\n"
        "Uma superfície de lítio cuja função trabalho é $\\Phi = 3{,}0\\text{ eV}$ é irradiada com radiação monocromática de comprimento de onda $\\lambda = 100\\text{ nm}$. "
        "Adotando $hc \\approx 1240\\text{ eV}\\cdot\\text{nm}$:\n\n"
        "A energia cinética máxima $K_{\\text{max}}$ dos fotoelétrons emitidos é:\n\n"
        "A $K_{\\text{max}} = 12{,}4 - 3{,}0 = 9{,}4\\text{ eV}$\n"
        "B $K_{\\text{max}} = 3{,}0\\text{ eV}$\n"
        "C $K_{\\text{max}} = 12{,}4\\text{ eV}$\n"
        "D $K_{\\text{max}} = 6{,}2\\text{ eV}$\n"
        "E $K_{\\text{max}} = 15{,}4\\text{ eV}$"
    ),
    "2022-2-fmPT4b": (
        "Q. 48 [fmPT4b]\n"
        "Se a superfície de lítio com $\\Phi = 3{,}0\\text{ eV}$ for irradiada com luz de comprimento de onda $\\lambda = 200\\text{ nm}$ ($hf = 6{,}2\\text{ eV}$):\n\n"
        "A energia cinética máxima $K_{\\text{max}}$ dos fotoelétrons emitidos vale:\n\n"
        "A $K_{\\text{max}} = 6{,}2 - 3{,}0 = 3{,}2\\text{ eV}$\n"
        "B $K_{\\text{max}} = 6{,}2\\text{ eV}$\n"
        "C $K_{\\text{max}} = 1{,}5\\text{ eV}$\n"
        "D $K_{\\text{max}} = 9{,}2\\text{ eV}$\n"
        "E $K_{\\text{max}} = 0$"
    ),
    "2022-2-fmPT8a": (
        "Q. 55 [fmPT8a]\n"
        "Em um tubo de raios X, elétrons são acelerados por uma diferença de potencial $V$. Pelo limite de Duane-Hunt, o comprimento de onda mínimo "
        "dos raios X emitidos no espectro contínuo (Bremsstrahlung) é:\n\n"
        "A $\\lambda_{\\text{mín}} = \\frac{hc}{eV}$\n"
        "B $\\lambda_{\\text{mín}} = \\frac{eV}{hc}$\n"
        "C $\\lambda_{\\text{mín}} = \\frac{h}{eV}$\n"
        "D $\\lambda_{\\text{mín}} = \\frac{hc}{2eV}$\n"
        "E $\\lambda_{\\text{mín}} = \\frac{2hc}{eV}$"
    ),
    "2022-2-mqPT4a": (
        "Q. 63 [mqPT4a]\n"
        "O hamiltoniano de uma partícula de spin $1/2$ sob campo magnético uniforme $B$ ao longo do eixo $z$ é $H = -\\gamma B S_z$.\n\n"
        "A frequência de precessão de Larmor do spin em torno do eixo $z$ é:\n\n"
        "A $\\omega_L = \\gamma B$\n"
        "B $\\omega_L = \\frac{1}{2}\\gamma B$\n"
        "C $\\omega_L = 2\\gamma B$\n"
        "D $\\omega_L = \\frac{\\gamma B}{\\hbar}$\n"
        "E $\\omega_L = \\gamma B \\hbar$"
    ),
    "2022-2-mqPT4b": (
        "Q. 64 [mqPT4b]\n"
        "Para a partícula de spin $1/2$ sob $H = -\\gamma B S_z$, a separação de energia entre os estados de spin 'up' e 'down' vale:\n\n"
        "A $\\Delta E = \\hbar \\gamma B$\n"
        "B $\\Delta E = \\frac{1}{2}\\hbar \\gamma B$\n"
        "C $\\Delta E = 2\\hbar \\gamma B$\n"
        "D $\\Delta E = \\gamma B$\n"
        "E $\\Delta E = 0$"
    ),
}


def apply_fm_mq_reconstructions():
    print("=" * 65)
    print("⚛️ RECONSTRUCTING MODERN PHYSICS & QUANTUM MECHANICS QUESTIONS")
    print("=" * 65)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    updated = 0
    for qid, clean_text in FM_MQ_RECONSTRUCTIONS.items():
        cur.execute("UPDATE questions SET text = ? WHERE id = ?", (clean_text, qid))
        if cur.rowcount > 0:
            updated += 1
            print(f"  ✓ Reconstructed {qid}")
        else:
            print(f"  ⚠ Question ID not found in DB: {qid}")

    conn.commit()
    conn.close()

    print(f"\n✅ Successfully updated {updated} Modern/Quantum questions in SQLite.")
    print("🚀 Exporting updated questions.json...")
    export_bank_to_json()
    print("✨ Complete!")


if __name__ == "__main__":
    apply_fm_mq_reconstructions()
