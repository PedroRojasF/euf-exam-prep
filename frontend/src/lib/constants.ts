export interface AreaTheme {
  code: string;
  name: string;
  shortName: string;
  badgeClass: string;
  colorHex: string;
}

export const AREA_THEMES: Record<string, AreaTheme> = {
  'Mecânica Clássica': {
    code: 'mc',
    name: 'Mecânica Clássica',
    shortName: 'Clássica',
    badgeClass: 'bg-emerald-50 text-emerald-800 border-emerald-200 dark:bg-emerald-950/40 dark:text-emerald-300 dark:border-emerald-800/60',
    colorHex: '#10b981'
  },
  'Eletromagnetismo': {
    code: 'em',
    name: 'Eletromagnetismo',
    shortName: 'Eletromag',
    badgeClass: 'bg-sky-50 text-sky-800 border-sky-200 dark:bg-sky-950/40 dark:text-sky-300 dark:border-sky-800/60',
    colorHex: '#0ea5e9'
  },
  'Mecânica Quântica': {
    code: 'mq',
    name: 'Mecânica Quântica',
    shortName: 'Quântica',
    badgeClass: 'bg-violet-50 text-violet-800 border-violet-200 dark:bg-violet-950/40 dark:text-violet-300 dark:border-violet-800/60',
    colorHex: '#8b5cf6'
  },
  'Termodinâmica': {
    code: 'te',
    name: 'Termodinâmica',
    shortName: 'Termo',
    badgeClass: 'bg-amber-50 text-amber-800 border-amber-200 dark:bg-amber-950/40 dark:text-amber-300 dark:border-amber-800/60',
    colorHex: '#f59e0b'
  },
  'Física Estatística': {
    code: 'fe',
    name: 'Física Estatística',
    shortName: 'Estatística',
    badgeClass: 'bg-teal-50 text-teal-800 border-teal-200 dark:bg-teal-950/40 dark:text-teal-300 dark:border-teal-800/60',
    colorHex: '#14b8a6'
  },
  'Física Moderna': {
    code: 'fm',
    name: 'Física Moderna',
    shortName: 'Moderna',
    badgeClass: 'bg-rose-50 text-rose-800 border-rose-200 dark:bg-rose-950/40 dark:text-rose-300 dark:border-rose-800/60',
    colorHex: '#f43f5e'
  }
};

export const HINT_LEVELS = [
  {
    level: 1,
    titleKey: 'level1Title',
    iconName: 'Lightbulb',
    color: 'emerald',
    badgeBg: 'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/50 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800',
    dotBg: 'bg-emerald-500'
  },
  {
    level: 2,
    titleKey: 'level2Title',
    iconName: 'Compass',
    color: 'sky',
    badgeBg: 'bg-sky-50 text-sky-700 dark:bg-sky-950/50 dark:text-sky-300 border-sky-200 dark:border-sky-800',
    dotBg: 'bg-sky-500'
  },
  {
    level: 3,
    titleKey: 'level3Title',
    iconName: 'Scale',
    color: 'amber',
    badgeBg: 'bg-amber-50 text-amber-700 dark:bg-amber-950/50 dark:text-amber-300 border-amber-200 dark:border-amber-800',
    dotBg: 'bg-amber-500'
  },
  {
    level: 4,
    titleKey: 'level4Title',
    iconName: 'Zap',
    color: 'rose',
    badgeBg: 'bg-rose-50 text-rose-700 dark:bg-rose-950/50 dark:text-rose-300 border-rose-200 dark:border-rose-800',
    dotBg: 'bg-rose-500'
  }
];

export const OFFICIAL_FORMULAS = [
  {
    category: "Constantes Físicas & Numéricas",
    formulas: [
      { name: "Velocidade da luz no vácuo", eq: "c = 3{,}00 \\times 10^8\\text{ m/s}" },
      { name: "Constante de Planck", eq: "h = 6{,}63 \\times 10^{-34}\\text{ J}\\cdot\\text{s} = 4{,}14 \\times 10^{-15}\\text{ eV}\\cdot\\text{s},\\quad \\hbar = \\frac{h}{2\\pi} = 1{,}06 \\times 10^{-34}\\text{ J}\\cdot\\text{s}" },
      { name: "Produtos fundamentais", eq: "hc \\simeq 1240\\text{ eV}\\cdot\\text{nm} = 1240\\text{ MeV}\\cdot\\text{fm},\\quad \\hbar c \\simeq 200\\text{ eV}\\cdot\\text{nm} = 200\\text{ MeV}\\cdot\\text{fm}" },
      { name: "Permeabilidade & Permissividade do vácuo", eq: "\\mu_0 = 4\\pi \\times 10^{-7}\\text{ N/A}^2,\\quad \\varepsilon_0 = \\frac{1}{\\mu_0 c^2} = 8{,}85 \\times 10^{-12}\\text{ F/m},\\quad \\frac{1}{4\\pi\\varepsilon_0} = 8{,}99 \\times 10^9\\text{ N}\\cdot\\text{m}^2/\\text{C}^2" },
      { name: "Carga e massas fundamentais", eq: "e = 1{,}60 \\times 10^{-19}\\text{ C},\\quad m_e = 9{,}11 \\times 10^{-31}\\text{ kg} = 511\\text{ keV}/c^2,\\quad m_p = 1{,}673 \\times 10^{-27}\\text{ kg} = 938\\text{ MeV}/c^2" },
      { name: "Constantes termodinâmicas", eq: "k_B = 1{,}38 \\times 10^{-23}\\text{ J/K} = 8{,}62 \\times 10^{-5}\\text{ eV/K},\\quad N_A = 6{,}02 \\times 10^{23}\\text{ mol}^{-1},\\quad R = 8{,}31\\text{ J}/(\\text{mol}\\cdot\\text{K})" },
      { name: "Constantes atômicas e radiação", eq: "a_0 = 5{,}29 \\times 10^{-11}\\text{ m},\\quad R_H = 1{,}10 \\times 10^7\\text{ m}^{-1},\\quad \\sigma = 5{,}67 \\times 10^{-8}\\text{ W}/(\\text{m}^2\\cdot\\text{K}^4),\\quad W = 2{,}898 \\times 10^{-3}\\text{ m}\\cdot\\text{K}" },
      { name: "Propagação de Incertezas", eq: "F = f(a,b) \\implies \\sigma_F = \\sqrt{\\left(\\frac{\\partial f}{\\partial a}\\right)^2 \\sigma_a^2 + \\left(\\frac{\\partial f}{\\partial b}\\right)^2 \\sigma_b^2}" }
    ]
  },
  {
    category: "Mecânica Clássica",
    formulas: [
      { name: "Lagrangiana e Equações de Euler-Lagrange", eq: "L = T - V,\\quad \\frac{d}{dt}\\left(\\frac{\\partial L}{\\partial \\dot{q}_k}\\right) - \\frac{\\partial L}{\\partial q_k} = 0,\\quad Q_k = \\sum_i \\vec{F}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_k}" },
      { name: "Hamiltoniana & Equações Canônicas", eq: "p_k = \\frac{\\partial L}{\\partial \\dot{q}_k},\\quad H = \\sum_{k} p_k \\dot{q}_k - L,\\quad \\dot{q}_k = \\frac{\\partial H}{\\partial p_k},\\quad \\dot{p}_k = -\\frac{\\partial H}{\\partial q_k},\\quad \\frac{\\partial H}{\\partial t} = -\\frac{\\partial L}{\\partial t}" },
      { name: "Cinemática Polar e Cilíndrica", eq: "\\vec{v} = \\dot{r}\\hat{e}_r + r\\dot{\\theta}\\hat{e}_\\theta,\\quad \\vec{a} = (\\ddot{r} - r\\dot{\\theta}^2)\\hat{e}_r + (r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta})\\hat{e}_\\theta" },
      { name: "Cinemática Esférica", eq: "\\vec{a} = (\\ddot{r} - r\\dot{\\theta}^2 - r\\dot{\\phi}^2\\sin^2\\theta)\\hat{e}_r + (r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta} - r\\dot{\\phi}^2\\sin\\theta\\cos\\theta)\\hat{e}_\\theta + (r\\ddot{\\phi}\\sin\\theta + 2\\dot{r}\\dot{\\phi}\\sin\\theta + 2r\\dot{\\theta}\\dot{\\phi}\\cos\\theta)\\hat{e}_\\phi" },
      { name: "Problema de Força Central e Órbitas", eq: "V_{\\text{ef}} = V(r) + \\frac{L^2}{2mr^2},\\quad E = \\frac{1}{2}m\\dot{r}^2 + V_{\\text{ef}}(r),\\quad \\dot{\\theta} = \\frac{L}{mr^2}" },
      { name: "Dinâmica do Corpo Rígido", eq: "L_i = \\sum_j I_{ij}\\omega_j,\\quad T_{\\text{rot}} = \\frac{1}{2}\\sum_{ij} I_{ij}\\omega_i \\omega_j,\\quad I = \\int r_\\perp^2 dm" },
      { name: "Referenciais Não-Inerciais", eq: "\\left(\\frac{d^2\\vec{r}}{dt^2}\\right)_{\\text{fixo}} = \\left(\\frac{d^2\\vec{r}}{dt^2}\\right)_{\\text{rot}} + 2\\vec{\\omega}\\times\\left(\\frac{d\\vec{r}}{dt}\\right)_{\\text{rot}} + \\vec{\\omega}\\times(\\vec{\\omega}\\times\\vec{r}) + \\dot{\\vec{\\omega}}\\times\\vec{r}" }
    ]
  },
  {
    category: "Eletromagnetismo",
    formulas: [
      { name: "Equações de Maxwell (Forma Integral)", eq: "\\oint \\vec{E}\\cdot d\\vec{l} = -\\frac{d}{dt}\\int \\vec{B}\\cdot d\\vec{S},\\quad \\oint \\vec{B}\\cdot d\\vec{l} = \\mu_0 I_{\\text{enc}} + \\mu_0\\varepsilon_0 \\frac{d}{dt}\\int \\vec{E}\\cdot d\\vec{S}" },
      { name: "Equações de Maxwell (Forma Diferencial)", eq: "\\nabla \\cdot \\vec{E} = \\frac{\\rho}{\\varepsilon_0},\\quad \\nabla \\cdot \\vec{B} = 0,\\quad \\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t},\\quad \\nabla \\times \\vec{B} = \\mu_0\\vec{J} + \\mu_0\\varepsilon_0\\frac{\\partial \\vec{E}}{\\partial t}" },
      { name: "Potenciais e Calibre de Lorenz", eq: "\\vec{B} = \\nabla \\times \\vec{A},\\quad \\vec{E} = -\\nabla V - \\frac{\\partial \\vec{A}}{\\partial t},\\quad \\vec{A}(\\vec{r}) = \\frac{\\mu_0}{4\\pi}\\int \\frac{\\vec{J}(\\vec{r}')}{|\\vec{r} - \\vec{r}'|}dV'" },
      { name: "Força de Lorentz e Vetor de Poynting", eq: "\\vec{F} = q(\\vec{E} + \\vec{v}\\times\\vec{B}),\\quad \\vec{S} = \\frac{1}{\\mu_0}(\\vec{E}\\times\\vec{B}),\\quad u = \\frac{1}{2}\\varepsilon_0 E^2 + \\frac{1}{2\\mu_0}B^2" },
      { name: "Campos em Meios Materiais", eq: "\\vec{D} = \\varepsilon_0\\vec{E} + \\vec{P} = \\varepsilon\\vec{E},\\quad \\vec{H} = \\frac{1}{\\mu_0}\\vec{B} - \\vec{M},\\quad \\rho_b = -\\nabla\\cdot\\vec{P},\\quad \\vec{J}_b = \\nabla\\times\\vec{M}" }
    ]
  },
  {
    category: "Relatividade Especial",
    formulas: [
      { name: "Transformações de Lorentz", eq: "\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}},\\quad x' = \\gamma(x - vt),\\quad t' = \\gamma\\left(t - \\frac{vx}{c^2}\\right)" },
      { name: "Transformação Relativística de Velocidades", eq: "u'_x = \\frac{u_x - v}{1 - vu_x/c^2},\\quad u'_y = \\frac{u_y}{\\gamma(1 - vu_x/c^2)},\\quad u'_z = \\frac{u_z}{\\gamma(1 - vu_x/c^2)}" },
      { name: "Dinâmica e Energia-Momento", eq: "\\vec{p} = \\gamma m_0 \\vec{v},\\quad E = \\gamma m_0 c^2,\\quad E^2 = p^2 c^2 + m_0^2 c^4" },
      { name: "Efeito Doppler Relativístico Longitudinal", eq: "\\nu = \\nu_0 \\sqrt{\\frac{1 - v/c}{1 + v/c}}\\quad (\\text{fonte e detector se afastando})" }
    ]
  },
  {
    category: "Mecânica Quântica",
    formulas: [
      { name: "Equação de Schrödinger", eq: "i\\hbar \\frac{\\partial \\Psi}{\\partial t} = \\hat{H}\\Psi,\\quad \\hat{H} = -\\frac{\\hbar^2}{2m}\\nabla^2 + V(\\vec{r})" },
      { name: "Operadores Escada do Oscilador Harmônico", eq: "\\hat{a} = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\left(\\hat{x} + \\frac{i\\hat{p}}{m\\omega}\\right),\\quad \\hat{a}|n\\rangle = \\sqrt{n}|n-1\\rangle,\\quad \\hat{a}^\\dagger|n\\rangle = \\sqrt{n+1}|n+1\\rangle,\\quad \\hat{H} = \\hbar\\omega\\left(\\hat{a}^\\dagger\\hat{a} + \\frac{1}{2}\\right)" },
      { name: "Momento Angular & Matrizes de Pauli", eq: "[\\hat{L}_i, \\hat{L}_j] = i\\hbar\\varepsilon_{ijk}\\hat{L}_k,\\quad \\hat{L}_\\pm Y_{\\ell m} = \\hbar\\sqrt{\\ell(\\ell+1) - m(m\\pm 1)}Y_{\\ell, m\\pm 1},\\quad \\vec{S} = \\frac{\\hbar}{2}\\vec{\\sigma}" },
      { name: "Matrizes de Pauli Explícitas", eq: "\\sigma_x = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix},\\quad \\sigma_y = \\begin{pmatrix} 0 & -i \\\\ i & 0 \\end{pmatrix},\\quad \\sigma_z = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}" },
      { name: "Teoria de Perturbações Independente do Tempo", eq: "E_n^{(1)} = \\langle n^{(0)}|\\delta \\hat{H}|n^{(0)}\\rangle,\\quad E_n^{(2)} = \\sum_{m\\ne n} \\frac{|\\langle m^{(0)}|\\delta \\hat{H}|n^{(0)}\\rangle|^2}{E_n^{(0)} - E_m^{(0)}}" }
    ]
  },
  {
    category: "Física Moderna",
    formulas: [
      { name: "Relações de Planck e de Broglie", eq: "E = h\\nu = \\hbar\\omega,\\quad p = \\frac{h}{\\lambda} = \\hbar k,\\quad \\Delta x \\Delta p \\ge \\frac{\\hbar}{2}" },
      { name: "Modelo de Bohr para Átomos Hidrogenóides", eq: "E_n = -\\frac{Z^2 R_H hc}{n^2} = -\\frac{13{,}6 Z^2}{n^2}\\text{ eV},\\quad r_n = \\frac{n^2 a_0}{Z}" },
      { name: "Efeito Fotoelétrico e Efeito Compton", eq: "K_{\\text{max}} = h\\nu - \\Phi,\\quad \\lambda' - \\lambda = \\frac{h}{m_e c}(1 - \\cos\\theta)" },
      { name: "Radiação de Corpo Negro", eq: "R_T = \\sigma T^4,\\quad \\lambda_{\\text{max}} T = W = 2{,}898 \\times 10^{-3}\\text{ m}\\cdot\\text{K}" }
    ]
  },
  {
    category: "Termodinâmica e Física Estatística",
    formulas: [
      { name: "Leis da Termodinâmica e Potenciais", eq: "dU = TdS - pdV + \\mu dN,\\quad dF = -SdT - pdV + \\mu dN,\\quad dG = -SdT + Vdp + \\mu dN" },
      { name: "Relações de Maxwell", eq: "\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial p}{\\partial S}\\right)_V,\\quad \\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial p}{\\partial T}\\right)_V,\\quad \\left(\\frac{\\partial T}{\\partial p}\\right)_S = \\left(\\frac{\\partial V}{\\partial S}\\right)_p" },
      { name: "Gases e Relações de Calor Específico", eq: "pV = nRT,\\quad C_V = T\\left(\\frac{\\partial S}{\\partial T}\\right)_V,\\quad C_p = T\\left(\\frac{\\partial S}{\\partial T}\\right)_p,\\quad C_p - C_V = nR" },
      { name: "Ensemble Canônico & Grande Canônico", eq: "Z = \\sum_n e^{-\\beta E_n},\\quad F = -k_B T \\ln Z,\\quad U = -\\frac{\\partial}{\\partial \\beta}\\ln Z,\\quad \\Xi = \\sum_N Z_N e^{\\beta \\mu N},\\quad \\Phi = -k_B T \\ln \\Xi" },
      { name: "Distribuições Quânticas de Fermi-Dirac e Bose-Einstein", eq: "f_{\\text{FD}}(\\varepsilon) = \\frac{1}{e^{\\beta(\\varepsilon - \\mu)} + 1},\\quad f_{\\text{BE}}(\\varepsilon) = \\frac{1}{e^{\\beta(\\varepsilon - \\mu)} - 1}" }
    ]
  },
  {
    category: "Operadores Diferenciais e Sistemas de Coordenadas",
    formulas: [
      { name: "Coordenadas Cartesianas", eq: "\\nabla f = \\frac{\\partial f}{\\partial x}\\hat{i} + \\frac{\\partial f}{\\partial y}\\hat{j} + \\frac{\\partial f}{\\partial z}\\hat{k},\\quad \\nabla \\cdot \\vec{A} = \\frac{\\partial A_x}{\\partial x} + \\frac{\\partial A_y}{\\partial y} + \\frac{\\partial A_z}{\\partial z},\\quad \\nabla^2 f = \\frac{\\partial^2 f}{\\partial x^2} + \\frac{\\partial^2 f}{\\partial y^2} + \\frac{\\partial^2 f}{\\partial z^2}" },
      { name: "Coordenadas Cilíndricas (Gradiente & Divergente)", eq: "\\nabla f = \\frac{\\partial f}{\\partial \\rho}\\hat{e}_\\rho + \\frac{1}{\\rho}\\frac{\\partial f}{\\partial \\phi}\\hat{e}_\\phi + \\frac{\\partial f}{\\partial z}\\hat{e}_z,\\quad \\nabla \\cdot \\vec{A} = \\frac{1}{\\rho}\\frac{\\partial(\\rho A_\\rho)}{\\partial \\rho} + \\frac{1}{\\rho}\\frac{\\partial A_\\phi}{\\partial \\phi} + \\frac{\\partial A_z}{\\partial z}" },
      { name: "Coordenadas Cilíndricas (Rotacional & Laplaciano)", eq: "\\nabla \\times \\vec{A} = \\left(\\frac{1}{\\rho}\\frac{\\partial A_z}{\\partial \\phi} - \\frac{\\partial A_\\phi}{\\partial z}\\right)\\hat{e}_\\rho + \\left(\\frac{\\partial A_\\rho}{\\partial z} - \\frac{\\partial A_z}{\\partial \\rho}\\right)\\hat{e}_\\phi + \\frac{1}{\\rho}\\left(\\frac{\\partial(\\rho A_\\phi)}{\\partial \\rho} - \\frac{\\partial A_\\rho}{\\partial \\phi}\\right)\\hat{e}_z" },
      { name: "Coordenadas Esféricas (Gradiente & Divergente)", eq: "\\nabla f = \\frac{\\partial f}{\\partial r}\\hat{e}_r + \\frac{1}{r}\\frac{\\partial f}{\\partial \\theta}\\hat{e}_\\theta + \\frac{1}{r\\sin\\theta}\\frac{\\partial f}{\\partial \\phi}\\hat{e}_\\phi,\\quad \\nabla \\cdot \\vec{A} = \\frac{1}{r^2}\\frac{\\partial(r^2 A_r)}{\\partial r} + \\frac{1}{r\\sin\\theta}\\frac{\\partial(\\sin\\theta A_\\theta)}{\\partial \\theta} + \\frac{1}{r\\sin\\theta}\\frac{\\partial A_\\phi}{\\partial \\phi}" },
      { name: "Coordenadas Esféricas (Laplaciano)", eq: "\\nabla^2 f = \\frac{1}{r^2}\\frac{\\partial}{\\partial r}\\left(r^2 \\frac{\\partial f}{\\partial r}\\right) + \\frac{1}{r^2\\sin\\theta}\\frac{\\partial}{\\partial \\theta}\\left(\\sin\\theta \\frac{\\partial f}{\\partial \\theta}\\right) + \\frac{1}{r^2\\sin^2\\theta}\\frac{\\partial^2 f}{\\partial \\phi^2}" }
    ]
  },
  {
    category: "Resultados Matemáticos, Integrais e Harmônicos Esféricos",
    formulas: [
      { name: "Integrais Gaussianas", eq: "\\int_{-\\infty}^\\infty x^{2n} e^{-a x^2} dx = \\frac{1\\cdot 3 \\cdot 5 \\cdots (2n-1)}{2^n a^n} \\sqrt{\\frac{\\pi}{a}},\\quad \\int_{-\\infty}^\\infty e^{-a x^2} dx = \\sqrt{\\frac{\\pi}{a}}" },
      { name: "Aproximação de Stirling", eq: "\\ln N! \\simeq N\\ln N - N,\\quad \\Gamma(n) = (n-1)!" },
      { name: "Harmônicos Esféricos Fundamentais", eq: "Y_{0,0} = \\sqrt{\\frac{1}{4\\pi}},\\quad Y_{1,0} = \\sqrt{\\frac{3}{4\\pi}}\\cos\\theta,\\quad Y_{1,\\pm 1} = \\mp \\sqrt{\\frac{3}{8\\pi}}\\sin\\theta e^{\\pm i\\phi},\\quad Y_{2,0} = \\sqrt{\\frac{5}{16\\pi}}(3\\cos^2\\theta - 1)" },
      { name: "Polinômios de Legendre", eq: "P_0(x) = 1,\\quad P_1(x) = x,\\quad P_2(x) = \\frac{1}{2}(3x^2 - 1),\\quad V(r,\\theta) = \\sum_{\\ell=0}^\\infty \\left(A_\\ell r^\\ell + \\frac{B_\\ell}{r^{\\ell+1}}\\right)P_\\ell(\\cos\\theta)" }
    ]
  }
];
