"""EUF Physics Solution Strategy & Tri-Lingual Contextual Hint Engine.
Generates tailored, problem-specific and subtopic-specific physical principles, coordinate setups, intermediate checkpoints, and limit checks.
Covers 100% of EUF syllabus topics across all 6 physics areas in Portuguese (PT), Spanish (ES), and English (EN).
"""

# Comprehensive Tri-Lingual Physics Knowledge Base (Subtopics across 6 Areas)
HINT_KNOWLEDGE_BASE = {
    # =========================================================================
    # 1. ELECTROMAGNETISM / ELETROMAGNETISMO / ELECTROMAGNETISMO
    # =========================================================================
    "Continuous Charge Distributions & Electric Potentials": {
        "pt": {
            "title": "Distribuições Contínuas de Carga & Integrais de Potencial e Campo",
            "level1": "Divida a geometria contínua em elementos infinitesimais de carga: $dq = \\lambda dl'$ (linha), $\\sigma dA'$ (superfície) ou $\\rho dV'$ (volume). O potencial eletrostático é $V(\\vec{r}) = \\frac{1}{4\\pi\\varepsilon_0}\\int \\frac{dq}{|\\vec{r} - \\vec{r}'|}$ e o campo é $\\vec{E}(\\vec{r}) = -\\nabla V$.",
            "level2": "Explore simetrias geométricas: No eixo de simetria $z$ de um anel de raio $R$ com carga total $Q$, as componentes perpendiculares cancelam-se ($E_x = E_y = 0$). O campo axial é $E_z = \\frac{Q z}{4\\pi\\varepsilon_0 (z^2 + R^2)^{3/2}}$.",
            "level3": "Para um disco de raio $R$ com densidade $\\sigma$: $E_z = \\frac{\\sigma}{2\\varepsilon_0}\\left(1 - \\frac{z}{\\sqrt{z^2 + R^2}}\\right)$. Para o plano infinito ($R \\to \\infty$), obtém-se o campo uniforme $E = \\frac{\\sigma}{2\\varepsilon_0}$.",
            "level4": "Análise de limites assintóticos: Para $z \\gg R$, expanda $(1 + R^2/z^2)^{-3/2} \\approx 1 - \\frac{3}{2}\\frac{R^2}{z^2}$, recuperando o campo coulombiano de carga pontual $E_z \\to \\frac{Q}{4\\pi\\varepsilon_0 z^2}$."
        },
        "es": {
            "title": "Distribuciones Continuas de Carga & Integrales de Potencial y Campo",
            "level1": "Divida la geometría continua en elementos diferenciales de carga: $dq = \\lambda dl'$ (línea), $\\sigma dA'$ (superficie) o $\\rho dV'$ (volumen). El potencial electrostático es $V(\\vec{r}) = \\frac{1}{4\\pi\\varepsilon_0}\\int \\frac{dq}{|\\vec{r} - \\vec{r}'|}$ y el campo es $\\vec{E}(\\vec{r}) = -\\nabla V$.",
            "level2": "Aproveche la simetría geométrica: En el eje de simetría $z$ de un anillo de radio $R$ con carga $Q$, las componentes transversales se anulan ($E_x = E_y = 0$). El campo axial resulta $E_z = \\frac{Q z}{4\\pi\\varepsilon_0 (z^2 + R^2)^{3/2}}$.",
            "level3": "Para un disco de radio $R$ con densidad $\\sigma$: $E_z = \\frac{\\sigma}{2\\varepsilon_0}\\left(1 - \\frac{z}{\\sqrt{z^2 + R^2}}\\right)$. Para el plano infinito ($R \\to \\infty$), se recupera el campo uniforme $E = \\frac{\\sigma}{2\\varepsilon_0}$.",
            "level4": "Comprobación de límites asintóticos: Para $z \\gg R$, expanda $(1 + R^2/z^2)^{-3/2} \\approx 1 - \\frac{3}{2}\\frac{R^2}{z^2}$, recuperando el campo de Coulomb puntual $E_z \\to \\frac{Q}{4\\pi\\varepsilon_0 z^2}$."
        },
        "en": {
            "title": "Continuous Charge Distributions & Electric Field/Potential Integrals",
            "level1": "Divide the continuous geometry into differential charge elements $dq = \\lambda dl'$ (line), $\\sigma dA'$ (surface), or $\\rho dV'$ (volume). Potential is $V(\\vec{r}) = \\frac{1}{4\\pi\\varepsilon_0}\\int \\frac{dq}{|\\vec{r} - \\vec{r}'|}$ and electric field is $\\vec{E}(\\vec{r}) = -\\nabla V$.",
            "level2": "Exploit geometric symmetry: On symmetry axes (e.g. $z$-axis of a ring of radius $R$ carrying charge $Q$), transverse field components cancel symmetrically ($E_x = E_y = 0$). The axial field is $E_z = \\frac{Q z}{4\\pi\\varepsilon_0 (z^2 + R^2)^{3/2}}$.",
            "level3": "For disk of radius $R$ with surface charge $\\sigma$: $E_z = \\frac{\\sigma}{2\\varepsilon_0}\\left(1 - \\frac{z}{\\sqrt{z^2 + R^2}}\\right)$. For infinite plane ($R \\to \\infty$), field becomes uniform $E = \\frac{\\sigma}{2\\varepsilon_0}$.",
            "level4": "Asymptotic dipole and monopole checks: For $z \\gg R$, expand $(1 + R^2/z^2)^{-3/2} \\approx 1 - \\frac{3}{2}\\frac{R^2}{z^2}$, recovering the point-charge Coulomb field $E_z \\to \\frac{Q}{4\\pi\\varepsilon_0 z^2}$."
        }
    },
    "Gauss's Law & Electric Flux": {
        "pt": {
            "title": "Lei de Gauss & Fluxo Elétrico em Simetrias Elevadas",
            "level1": "A Lei de Gauss estabelece $\\Phi_E = \\oint_{\\mathcal{S}} \\vec{E}\\cdot d\\vec{A} = \\frac{Q_{\\text{int}}}{\\varepsilon_0}$. Ela é eficaz quando a simetria torna $|\\vec{E}|$ constante sobre a superfície gaussiana e paralelo a $d\\vec{A}$.",
            "level2": "Simetria esférica (raio $R$, carga $Q$): Para $r > R$, $\\vec{E} = \\frac{Q}{4\\pi\\varepsilon_0 r^2}\\hat{r}$. No interior de esfera isolante uniforme ($r < R$), $Q_{\\text{int}} = Q(r/R)^3 \\implies \\vec{E} = \\frac{Q r}{4\\pi\\varepsilon_0 R^3}\\hat{r}$.",
            "level3": "Simetria cilíndrica (densidade linear $\\lambda$): Cilindro gaussiano de raio $r$, comprimento $L$: $E(2\\pi r L) = \\frac{\\lambda L}{\\varepsilon_0} \\implies \\vec{E} = \\frac{\\lambda}{2\\pi\\varepsilon_0 r}\\hat{r}$. Potencial é $V(r) = -\\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln(r/r_0)$.",
            "level4": "Descontinuidade na fronteira: Através de qualquer superfície carregada com densidade $\\sigma$, o campo normal salta $\\Delta E_{\\perp} = E_{\\text{fora}} - E_{\\text{dentro}} = \\frac{\\sigma}{\\varepsilon_0}$, enquanto a componente tangencial é contínua."
        },
        "es": {
            "title": "Ley de Gauss & Flujo Eléctrico en Alta Simetría",
            "level1": "La Ley de Gauss establece $\\Phi_E = \\oint_{\\mathcal{S}} \\vec{E}\\cdot d\\vec{A} = \\frac{Q_{\\text{enc}}}{\\varepsilon_0}$. Es aplicable cuando la simetría hace que $|\\vec{E}|$ sea constante en la superficie gaussiana y paralelo a $d\\vec{A}$.",
            "level2": "Simetría esférica (radio $R$, carga $Q$): Para $r > R$, $\\vec{E} = \\frac{Q}{4\\pi\\varepsilon_0 r^2}\\hat{r}$. Dentro de una esfera uniforme ($r < R$), $Q_{\\text{enc}} = Q(r/R)^3 \\implies \\vec{E} = \\frac{Q r}{4\\pi\\varepsilon_0 R^3}\\hat{r}$.",
            "level3": "Simetría cilíndrica (densidad lineal $\\lambda$): Cilindro de radio $r$, longitud $L$: $E(2\\pi r L) = \\frac{\\lambda L}{\\varepsilon_0} \\implies \\vec{E} = \\frac{\\lambda}{2\\pi\\varepsilon_0 r}\\hat{r}$. Potencial $V(r) = -\\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln(r/r_0)$.",
            "level4": "Discontinuidad en la frontera: A través de una superficie cargada con densidad $\\sigma$, el campo normal salta $\\Delta E_{\\perp} = E_{\\text{ext}} - E_{\\text{int}} = \\frac{\\sigma}{\\varepsilon_0}$, mientras que la componente tangencial es continua."
        },
        "en": {
            "title": "Gauss's Law & Highly Symmetric Charge Distributions",
            "level1": "Gauss's Law states $\\Phi_E = \\oint_{\\mathcal{S}} \\vec{E}\\cdot d\\vec{A} = \\frac{Q_{\\text{enc}}}{\\varepsilon_0}$. It applies effectively when symmetry makes $|\\vec{E}|$ constant on the Gaussian surface and parallel/perpendicular to $d\\vec{A}$.",
            "level2": "Spherical symmetry (radius $R$, total charge $Q$): For $r > R$, $\\vec{E} = \\frac{Q}{4\\pi\\varepsilon_0 r^2}\\hat{r}$. Inside a uniform sphere ($r < R$), $Q_{\\text{enc}} = Q(r/R)^3 \\implies \\vec{E} = \\frac{Q r}{4\\pi\\varepsilon_0 R^3}\\hat{r}$.",
            "level3": "Cylindrical symmetry (linear charge density $\\lambda$): Gaussian cylinder of radius $r$, length $L$ yields $E(2\\pi r L) = \\frac{\\lambda L}{\\varepsilon_0} \\implies \\vec{E} = \\frac{\\lambda}{2\\pi\\varepsilon_0 r}\\hat{r}$. Potential is $V(r) = -\\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln(r/r_0)$.",
            "level4": "Boundary discontinuity check: Across any charged surface with local density $\\sigma$, the normal field has discontinuity $\\Delta E_{\\perp} = E_{\\text{out}} - E_{\\text{in}} = \\frac{\\sigma}{\\varepsilon_0}$, while tangential component is continuous."
        }
    },
    "Biot-Savart Law & Magnetic Fields of Currents": {
        "pt": {
            "title": "Lei de Biot-Savart & Campo Magnético de Correntes Estacionárias",
            "level1": "A Lei de Biot-Savart para fio percorrido por corrente $I$ é $d\\vec{B} = \\frac{\\mu_0 I}{4\\pi} \\frac{d\\vec{l}\\times\\hat{r}}{r^2}$. No centro de uma espira circular plana de raio $R$, o campo é $B = \\frac{\\mu_0 I}{2R}$.",
            "level2": "Superposição magnética: Para duas espiras concêntricas e coplanares com correntes opostas $i_1$ e $i_2$, os campos têm sentidos contrários. O campo resultante no centro é nulo quando $\\frac{\\mu_0 i_1}{2 R_1} = \\frac{\\mu_0 i_2}{2 R_2} \\implies \\frac{i_1}{R_1} = \\frac{i_2}{R_2}$.",
            "level3": "Para $R_1 = R$ e $R_2 = R/2$: $i_1/R = i_2/(R/2) = 2 i_2 / R \\implies i_1 = 2 i_2$.",
            "level4": "Verificação: A espira de menor raio produz maior campo por unidade de corrente ($B \\propto 1/R$), logo requer menor corrente para anular o campo da espira maior."
        },
        "es": {
            "title": "Ley de Biot-Savart & Campo Magnético de Corrientes Estacionarias",
            "level1": "La Ley de Biot-Savart para un conductor con corriente $I$ es $d\\vec{B} = \\frac{\\mu_0 I}{4\\pi} \\frac{d\\vec{l}\\times\\hat{r}}{r^2}$. En el centro de una espira circular plana de radio $R$, el campo es $B = \\frac{\\mu_0 I}{2R}$.",
            "level2": "Superposición magnética: Para dos espiras concéntricas y coplanares con corrientes opuestas $i_1$ e $i_2$, los campos tienen sentidos opuestos. El campo resultante en el centro es nulo cuando $\\frac{\\mu_0 i_1}{2 R_1} = \\frac{\\mu_0 i_2}{2 R_2} \\implies \\frac{i_1}{R_1} = \\frac{i_2}{R_2}$.",
            "level3": "Para $R_1 = R$ y $R_2 = R/2$: $i_1/R = i_2/(R/2) = 2 i_2 / R \\implies i_1 = 2 i_2$.",
            "level4": "Comprobación: La espira de menor radio produce mayor campo por unidad de corriente ($B \\propto 1/R$), por lo que requiere menor corriente para anular el campo de la espira mayor."
        },
        "en": {
            "title": "Biot-Savart Law & Magnetic Fields of Steady Currents",
            "level1": "The Biot-Savart Law for a current-carrying wire $I$ is $d\\vec{B} = \\frac{\\mu_0 I}{4\\pi} \\frac{d\\vec{l}\\times\\hat{r}}{r^2}$. At the center of a circular loop of radius $R$, the magnetic field is $B = \\frac{\\mu_0 I}{2R}$.",
            "level2": "Magnetic superposition: For two concentric, coplanar loops with opposing currents $i_1$ and $i_2$, field vectors oppose each other. Net field at center is zero when $\\frac{\\mu_0 i_1}{2 R_1} = \\frac{\\mu_0 i_2}{2 R_2} \\implies \\frac{i_1}{R_1} = \\frac{i_2}{R_2}$.",
            "level3": "For $R_1 = R$ and $R_2 = R/2$: $i_1/R = i_2/(R/2) \\implies i_1 = 2 i_2$.",
            "level4": "Consistency check: The smaller loop produces more field per unit current ($B \\propto 1/R$), so it requires smaller current to cancel the field of the larger loop."
        }
    },
    "Conductors, Cavities & Electrostatic Shielding": {
        "pt": {
            "title": "Condutores, Cavidades & Blindagem Eletrostática",
            "level1": "Em equilíbrio eletrostático: o campo elétrico no interior do condutor maciço é nulo ($\vec{E} = 0$), todo o condutor é equipotencial e a carga líquida livre reside exclusivamente na superfície.",
            "level2": "Cavidade com carga interna $q$: Pela lei de Gauss na cavidade, uma carga induzida $q_c = -q$ surge na parede interna da cavidade para garantir $\vec{E} = 0$ no metal.",
            "level3": "Superfície externa: Pela conservação da carga total do condutor $Q$, a carga na superfície externa é $q_{\\text{ext}} = Q - q_c = Q - (-q) = Q + q$. Se o condutor for um cubo com 6 faces idênticas, cada face recebe $q_f = \\frac{Q + q}{6}$.",
            "level4": "Verificação com valores numéricos: Se $q = -12\\,\\mu\\text{C}$ e $Q = 36\\,\\mu\\text{C}$, então $q_c = +12\\,\\mu\\text{C}$ e cada face tem $q_f = \\frac{36 + (-12)}{6} = 4{,}0\\,\\mu\\text{C}$."
        },
        "es": {
            "title": "Conductores, Cavidades & Blindaje Electrostático",
            "level1": "En equilibrio electrostático: el campo eléctrico en el interior de un conductor macizo es nulo ($\vec{E} = 0$), todo el conductor es equipotencial y la carga neta reside únicamente en las superficies.",
            "level2": "Cavidad con carga interior $q$: Por la ley de Gauss alrededor de la cavidad, se induce una carga $q_c = -q$ en la pared interior de la cavidad para asegurar $\vec{E} = 0$ en el metal.",
            "level3": "Superficie exterior: Por conservación de la carga total $Q$ del conductor, la carga en la superficie exterior es $q_{\\text{ext}} = Q - q_c = Q + q$. Para un cubo con 6 caras idénticas, cada cara recibe $q_f = \\frac{Q + q}{6}$.",
            "level4": "Comprobación numérica: Para $q = -12\\,\\mu\\text{C}$ y $Q = 36\\,\\mu\\text{C}$, resulta $q_c = +12\\,\\mu\\text{C}$ y cada cara contiene $q_f = \\frac{36 + (-12)}{6} = 4{,}0\\,\\mu\\text{C}$."
        },
        "en": {
            "title": "Conductors, Cavities & Electrostatic Shielding",
            "level1": "In electrostatic equilibrium: the electric field inside a bulk conductor is zero ($\vec{E} = 0$), the entire conductor is an equipotential, and net charge resides exclusively on boundaries.",
            "level2": "Cavity containing charge $q$: By Gauss's law enclosing the cavity, an induced charge $q_c = -q$ appears on the inner cavity wall to ensure $\vec{E} = 0$ in the metal.",
            "level3": "Outer surface: By total conductor charge conservation $Q$, charge on outer surface is $q_{\\text{ext}} = Q - q_c = Q + q$. For a cube with 6 identical faces, each face carries $q_f = \\frac{Q + q}{6}$.",
            "level4": "Numerical check: If $q = -12\\,\\mu\\text{C}$ and $Q = 36\\,\\mu\\text{C}$, then $q_c = +12\\,\\mu\\text{C}$ and each face has $q_f = \\frac{36 + (-12)}{6} = 4.0\\,\\mu\\text{C}$."
        }
    },
    "Lagrangian Mechanics & Generalized Coordinates": {
        "pt": {
            "title": "Mecânica Lagrangiana & Transformada de Legendre para Hamiltoniana",
            "level1": "A Lagrangiana é $L(q, \\dot{q})$. O momento conjugado generalizado é definido por $p = \\frac{\\partial L}{\\partial \\dot{q}}$.",
            "level2": "Para obter a Hamiltoniana $H(q, p)$, aplique a Transformada de Legendre: $H = p \\dot{q} - L(q, \\dot{q})$, invertendo $\\dot{q} = \\dot{q}(q, p)$ para eliminar completamente $\\dot{q}$.",
            "level3": "Se $L = (a\\dot{q} + bq)^2$: momento é $p = \\frac{\\partial L}{\\partial \\dot{q}} = 2a(a\\dot{q} + bq) \\implies a\\dot{q} + bq = \\frac{p}{2a} \\implies \\dot{q} = \\frac{p - 2abq}{2a^2}$.",
            "level4": "Substituindo em $H$: $H = p\\left(\\frac{p - 2abq}{2a^2}\\right) - \\left(\\frac{p}{2a}\\right)^2 = \\frac{p^2}{2a^2} - \\frac{bpq}{a} - \\frac{p^2}{4a^2} = \\frac{p^2}{4a^2} - \\frac{bpq}{a}$."
        },
        "es": {
            "title": "Mecánica Lagrangiana & Transformada de Legendre a Hamiltoniana",
            "level1": "El Lagrangiano es $L(q, \\dot{q})$. El momento canónico conjugado se define como $p = \\frac{\\partial L}{\\partial \\dot{q}}$.",
            "level2": "Para obtener el Hamiltoniano $H(q, p)$, aplique la Transformada de Legendre: $H = p \\dot{q} - L(q, \\dot{q})$, despejando $\\dot{q} = \\dot{q}(q, p)$ para eliminar por completo $\\dot{q}$.",
            "level3": "Si $L = (a\\dot{q} + bq)^2$: el momento es $p = \\frac{\\partial L}{\\partial \\dot{q}} = 2a(a\\dot{q} + bq) \\implies a\\dot{q} + bq = \\frac{p}{2a} \\implies \\dot{q} = \\frac{p - 2abq}{2a^2}$.",
            "level4": "Sustituyendo en $H$: $H = p\\left(\\frac{p - 2abq}{2a^2}\\right) - \\left(\\frac{p}{2a}\\right)^2 = \\frac{p^2}{2a^2} - \\frac{bpq}{a} - \\frac{p^2}{4a^2} = \\frac{p^2}{4a^2} - \\frac{bpq}{a}$."
        },
        "en": {
            "title": "Lagrangian Mechanics & Legendre Transformation to Hamiltonian",
            "level1": "The Lagrangian is $L(q, \\dot{q})$. The canonical momentum conjugate to $q$ is defined as $p = \\frac{\\partial L}{\\partial \\dot{q}}$.",
            "level2": "To obtain the Hamiltonian $H(q, p)$, perform Legendre transformation: $H = p \\dot{q} - L(q, \\dot{q})$, expressing $\\dot{q} = \\dot{q}(q, p)$ to eliminate $\\dot{q}$ entirely.",
            "level3": "For $L = (a\\dot{q} + bq)^2$: momentum is $p = \\frac{\\partial L}{\\partial \\dot{q}} = 2a(a\\dot{q} + bq) \\implies a\\dot{q} + bq = \\frac{p}{2a} \\implies \\dot{q} = \\frac{p - 2abq}{2a^2}$.",
            "level4": "Substituting into $H$: $H = p\\left(\\frac{p - 2abq}{2a^2}\\right) - \\left(\\frac{p}{2a}\\right)^2 = \\frac{p^2}{2a^2} - \\frac{bpq}{a} - \\frac{p^2}{4a^2} = \\frac{p^2}{4a^2} - \\frac{bpq}{a}$."
        }
    },
    "Calorimetry, Heat Capacities & Thermal Expansion": {
        "pt": {
            "title": "Calorimetria, Capacidade Térmica Variável & Equilíbrio Térmico",
            "level1": "Em um sistema termicamente isolado formado por dois corpos em contato térmico: o calor total trocado é nulo, $\\sum Q = 0 \\implies Q_1 + Q_2 = 0$.",
            "level2": "Quando a capacidade térmica $C_v(T)$ varia com a temperatura $T$: o calor trocado é a integral $Q = \\int_{T_i}^{T_f} C_v(T) dT$.",
            "level3": "Para $C_v(T) = B T$: $\\int_{T_1}^{T_{\\text{eq}}} B T dT + \\int_{T_2}^{T_{\\text{eq}}} B T dT = 0 \\implies \\frac{B}{2}(T_{\\text{eq}}^2 - T_1^2) + \\frac{B}{2}(T_{\\text{eq}}^2 - T_2^2) = 0$.",
            "level4": "Isolando a temperatura final: $2 T_{\\text{eq}}^2 = T_1^2 + T_2^2 \\implies T_{\\text{eq}} = \\sqrt{\\frac{T_1^2 + T_2^2}{2}}$. Para $T_1 = T_0$ e $T_2 = 2T_0$, $T_{\\text{eq}} = \\sqrt{\\frac{1+4}{2}} T_0 = \\sqrt{\\frac{5}{2}} T_0$."
        },
        "es": {
            "title": "Calorimetría, Capacidad Térmica Variable & Equilibrio Térmico",
            "level1": "En un sistema térmicamente aislado formado por dos cuerpos en contacto: el calor neto intercambiado es nulo, $\\sum Q = 0 \\implies Q_1 + Q_2 = 0$.",
            "level2": "Cuando la capacidad térmica $C_v(T)$ depende de la temperatura $T$: el calor transferido es la integral $Q = \\int_{T_i}^{T_f} C_v(T) dT$.",
            "level3": "Para $C_v(T) = B T$: $\\int_{T_1}^{T_{\\text{eq}}} B T dT + \\int_{T_2}^{T_{\\text{eq}}} B T dT = 0 \\implies \\frac{B}{2}(T_{\\text{eq}}^2 - T_1^2) + \\frac{B}{2}(T_{\\text{eq}}^2 - T_2^2) = 0$.",
            "level4": "Despejando la temperatura final: $2 T_{\\text{eq}}^2 = T_1^2 + T_2^2 \\implies T_{\\text{eq}} = \\sqrt{\\frac{T_1^2 + T_2^2}{2}}$. Para $T_1 = T_0$ y $T_2 = 2T_0$, resulta $T_{\\text{eq}} = \\sqrt{\\frac{5}{2}} T_0$."
        },
        "en": {
            "title": "Calorimetry, Temperature-Dependent Heat Capacity & Thermal Equilibrium",
            "level1": "In a thermally isolated system of two bodies in thermal contact: total net heat exchange is zero, $\\sum Q = 0 \\implies Q_1 + Q_2 = 0$.",
            "level2": "When heat capacity $C_v(T)$ depends on temperature $T$: heat exchanged is given by $Q = \\int_{T_i}^{T_f} C_v(T) dT$.",
            "level3": "For $C_v(T) = B T$: $\\int_{T_1}^{T_{\\text{eq}}} B T dT + \\int_{T_2}^{T_{\\text{eq}}} B T dT = 0 \\implies \\frac{B}{2}(T_{\\text{eq}}^2 - T_1^2) + \\frac{B}{2}(T_{\\text{eq}}^2 - T_2^2) = 0$.",
            "level4": "Solving for final equilibrium temperature: $2 T_{\\text{eq}}^2 = T_1^2 + T_2^2 \\implies T_{\\text{eq}} = \\sqrt{\\frac{T_1^2 + T_2^2}{2}}$. For $T_1 = T_0$ and $T_2 = 2T_0$, $T_{\\text{eq}} = \\sqrt{\\frac{5}{2}} T_0$."
        }
    },
    "Canonical & Microcanonical Ensembles": {
        "pt": {
            "title": "Estatística de Maxwell-Boltzmann, Função de Partição & Limites de Temperatura",
            "level1": "A função de partição de uma partícula com níveis de energia $\\varepsilon_j$ e degenerescência $g_j$ é $Z_1 = \\sum_j g_j e^{-\\beta \\varepsilon_j}$, onde $\\beta = \\frac{1}{k_B T}$.",
            "level2": "Limite $T \\to 0$ (ou $\\beta \\to \\infty$): O sistema congela no estado fundamental de menor energia $E_0$. A energia média é $\\langle E \\rangle \\to E_0$ e a entropia é $S = k_B \\ln g_0$ ($S \\to 0$ se não degenerado).",
            "level3": "Limite $T \\to \\infty$ (ou $\\beta \\to 0$): Todos os $M$ estados de energia tornam-se equiprováveis ($e^{-\\beta\\varepsilon_j} \\to 1$). A entropia de $N$ partículas atinge o valor máximo $S \\to N k_B \\ln M$.",
            "level4": "Para 5 níveis com menor energia $-2E$: Quando $T \\to 0$, energia média é $-2E$ e $S = 0$. Quando $T \\to \\infty$, $S = N k_B \\ln 5$."
        },
        "es": {
            "title": "Estadística de Maxwell-Boltzmann, Función de Partición & Límites Térmicos",
            "level1": "La función de partición de una partícula con niveles de energía $\\varepsilon_j$ y degeneración $g_j$ es $Z_1 = \\sum_j g_j e^{-\\beta \\varepsilon_j}$, donde $\\beta = \\frac{1}{k_B T}$.",
            "level2": "Límite $T \\to 0$ (o $\\beta \\to \\infty$): El sistema se congela en el estado fundamental de menor energía $E_0$. La energía media es $\\langle E \\rangle \\to E_0$ y la entropía es $S = k_B \\ln g_0$ ($S \\to 0$ si no es degenerado).",
            "level3": "Límite $T \\to \\infty$ (o $\\beta \\to 0$): Todos los $M$ niveles se vuelven equiprobables ($e^{-\\beta\\varepsilon_j} \\to 1$). La entropía de $N$ partículas alcanza el máximo $S \\to N k_B \\ln M$.",
            "level4": "Para 5 niveles con mínima energía $-2E$: Cuando $T \\to 0$, la energía media es $-2E$ y $S = 0$. Cuando $T \\to \\infty$, $S = N k_B \\ln 5$."
        },
        "en": {
            "title": "Maxwell-Boltzmann Statistics, Partition Function & Temperature Limits",
            "level1": "The single-particle partition function with energy levels $\\varepsilon_j$ and degeneracies $g_j$ is $Z_1 = \\sum_j g_j e^{-\\beta \\varepsilon_j}$, with $\\beta = \\frac{1}{k_B T}$.",
            "level2": "Low-temperature limit $T \\to 0$ ($\\beta \\to \\infty$): The system condenses into the lowest energy ground state $E_0$. Average energy $\\langle E \\rangle \\to E_0$ and entropy $S \\to k_B \\ln g_0$ ($S \\to 0$ if non-degenerate).",
            "level3": "High-temperature limit $T \\to \\infty$ ($\\beta \\to 0$): All $M$ states become equally populated ($e^{-\\beta\\varepsilon_j} \\to 1$). Total entropy for $N$ particles approaches $S \\to N k_B \\ln M$.",
            "level4": "For 5 levels with ground energy $-2E$: As $T \\to 0$, average energy is $-2E$ and $S = 0$. As $T \\to \\infty$, entropy is $S = N k_B \\ln 5$."
        }
    },
    "Nuclear Physics & Radioactive Decay": {
        "pt": {
            "title": "Física Nuclear, Lei do Decaimento Radioativo & Vida Média",
            "level1": "A taxa de emissão de partículas (atividade $R$) de uma amostra com $N$ núcleos radioativos e vida média $\\tau$ é dada por $R = \\left|\\frac{dN}{dt}\\right| = \\lambda N = \\frac{N}{\\tau}$.",
            "level2": "O número total de núcleos $N$ em uma amostra pura de massa $m$ e massa molar $M_A$ é $N = \\frac{m}{M_A} N_A$, onde $N_A$ é a constante de Avogadro.",
            "level3": "Substituindo $N$ na equação da atividade: $R = \\frac{m N_A}{M_A \\tau} \\implies \\tau = \\frac{m N_A}{R M_A}$.",
            "level4": "Análise dimensional: $[\tau] = \\frac{\\text{kg} \\cdot \\text{mol}^{-1}}{(\\text{s}^{-1}) \\cdot (\\text{kg}/\\text{mol})} = \\text{s}$ (unidade correta de tempo)."
        },
        "es": {
            "title": "Física Nuclear, Ley de Desintegración Radiactiva & Vida Media",
            "level1": "La tasa de emisión de partículas (actividad $R$) de una muestra con $N$ núcleos radiactivos y vida media $\\tau$ es $R = \\left|\\frac{dN}{dt}\\right| = \\lambda N = \\frac{N}{\\tau}$.",
            "level2": "El número de núcleos $N$ en una muestra pura de masa $m$ y masa molar $M_A$ es $N = \\frac{m}{M_A} N_A$, donde $N_A$ es la constante de Avogadro.",
            "level3": "Sustituyendo $N$ en la expresión de actividad: $R = \\frac{m N_A}{M_A \\tau} \\implies \\tau = \\frac{m N_A}{R M_A}$.",
            "level4": "Análisis dimensional: $[\tau] = \\frac{\\text{kg} \\cdot \\text{mol}^{-1}}{(\\text{s}^{-1}) \\cdot (\\text{kg}/\\text{mol})} = \\text{s}$ (unidad correcta de tiempo)."
        },
        "en": {
            "title": "Nuclear Physics, Radioactive Decay Law & Mean Lifetime",
            "level1": "The particle emission rate (activity $R$) of a sample containing $N$ nuclei with mean lifetime $\\tau$ is $R = \\left|\\frac{dN}{dt}\\right| = \\lambda N = \\frac{N}{\\tau}$.",
            "level2": "The total number of nuclei $N$ in a pure sample of mass $m$ and molar mass $M_A$ is $N = \\frac{m}{M_A} N_A$, where $N_A$ is Avogadro's number.",
            "level3": "Substituting $N$ into the activity equation: $R = \\frac{m N_A}{M_A \\tau} \\implies \\tau = \\frac{m N_A}{R M_A}$.",
            "level4": "Dimensional check: $[\\tau] = \\frac{\\text{kg}\\cdot\\text{mol}^{-1}}{(\\text{s}^{-1})\\cdot(\\text{kg}/\\text{mol})} = \\text{s}$ (valid unit of time)."
        }
    }
}


def get_physics_clues(area, subtopic, qid="", text="", lang="pt"):
    """Returns problem-specific physical guidance localized in PT, ES, or EN."""
    target_lang = lang if lang in ("pt", "es", "en") else "pt"
    t_lower = (text or "").lower()

    # 1. Problem-specific text keyword triggers
    if ("lagrangiana" in t_lower and ("hamiltoniana" in t_lower or "momento can" in t_lower)) or "l ( \dot{q},q)" in t_lower:
        data = HINT_KNOWLEDGE_BASE["Lagrangian Mechanics & Generalized Coordinates"]
        return data.get(target_lang, data["pt"])

    if "espiras circulares" in t_lower or "espiras conc" in t_lower:
        data = HINT_KNOWLEDGE_BASE["Biot-Savart Law & Magnetic Fields of Currents"]
        return data.get(target_lang, data["pt"])

    if "capacidade térmica" in t_lower and ("temperatura de equilíbrio" in t_lower or "cv =" in t_lower):
        data = HINT_KNOWLEDGE_BASE["Calorimetry, Heat Capacities & Thermal Expansion"]
        return data.get(target_lang, data["pt"])

    if "maxwell-boltzmann" in t_lower or ("níveis não degenerados de energia" in t_lower and "t \to0" in t_lower):
        data = HINT_KNOWLEDGE_BASE["Canonical & Microcanonical Ensembles"]
        return data.get(target_lang, data["pt"])

    if "decaimento alfa" in t_lower or ("partículas alfa" in t_lower and "vida média" in t_lower):
        data = HINT_KNOWLEDGE_BASE["Nuclear Physics & Radioactive Decay"]
        return data.get(target_lang, data["pt"])

    if "cavidade" in t_lower and "condutor" in t_lower and "carga" in t_lower:
        data = HINT_KNOWLEDGE_BASE["Conductors, Cavities & Electrostatic Shielding"]
        return data.get(target_lang, data["pt"])

    # 2. Direct subtopic match
    if subtopic in HINT_KNOWLEDGE_BASE:
        data = HINT_KNOWLEDGE_BASE[subtopic]
        if target_lang in data:
            return data[target_lang]
        if "pt" in data:
            return data["pt"]

    # 3. Fuzzy subtopic keyword match
    sub_lower = (subtopic or "").lower()
    for key, data in HINT_KNOWLEDGE_BASE.items():
        if any(w in sub_lower for w in key.lower().split() if len(w) > 4):
            if target_lang in data:
                return data[target_lang]
            if "pt" in data:
                return data["pt"]

    # 4. Area-based default fallback
    area_defaults = {
        "Mecânica Clássica": "Lagrangian Mechanics & Generalized Coordinates",
        "Eletromagnetismo": "Continuous Charge Distributions & Electric Potentials",
        "Mecânica Quântica": "Lagrangian Mechanics & Generalized Coordinates",
        "Termodinâmica": "Calorimetry, Heat Capacities & Thermal Expansion",
        "Física Estatística": "Canonical & Microcanonical Ensembles",
        "Física Moderna": "Nuclear Physics & Radioactive Decay",
    }
    fallback_key = area_defaults.get(area, "Continuous Charge Distributions & Electric Potentials")
    data = HINT_KNOWLEDGE_BASE.get(fallback_key, HINT_KNOWLEDGE_BASE["Continuous Charge Distributions & Electric Potentials"])
    return data.get(target_lang, data.get("pt"))


def get_all_physics_clues(area, subtopic, qid="", text=""):
    """Returns clues in all 3 supported languages for full static JSON exports."""
    return {
        "pt": get_physics_clues(area, subtopic, qid, text, lang="pt"),
        "es": get_physics_clues(area, subtopic, qid, text, lang="es"),
        "en": get_physics_clues(area, subtopic, qid, text, lang="en"),
    }
