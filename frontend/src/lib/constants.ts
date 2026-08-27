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
    category: "Mecânica Clássica",
    formulas: [
      { name: "Lagrangiana e Vínculos", eq: "L(q, \\dot{q}, t) = T - V,\\quad \\frac{d}{dt}\\left(\\frac{\\partial L}{\\partial \\dot{q}_i}\\right) - \\frac{\\partial L}{\\partial q_i} = Q_i" },
      { name: "Hamiltoniana & Momentos Conjugados", eq: "p_i = \\frac{\\partial L}{\\partial \\dot{q}_i},\\quad H = \\sum_i p_i \\dot{q}_i - L" },
      { name: "Equações Canônicas de Hamilton", eq: "\\dot{q}_i = \\frac{\\partial H}{\\partial p_i},\\quad \\dot{p}_i = -\\frac{\\partial H}{\\partial q_i}" },
      { name: "Parênteses de Poisson", eq: "\\{u, v\\} = \\sum_i \\left( \\frac{\\partial u}{\\partial q_i}\\frac{\\partial v}{\\partial p_i} - \\frac{\\partial u}{\\partial p_i}\\frac{\\partial v}{\\partial q_i} \\right)" },
      { name: "Potencial Efetivo e Força Central", eq: "V_{\\text{eff}}(r) = V(r) + \\frac{L^2}{2 m r^2},\\quad E = \\frac{1}{2}m\\dot{r}^2 + V_{\\text{eff}}(r)" }
    ]
  },
  {
    category: "Eletromagnetismo",
    formulas: [
      { name: "Equações de Maxwell (Vácuo)", eq: "\\nabla \\cdot \\vec{E} = \\frac{\\rho}{\\varepsilon_0},\\quad \\nabla \\cdot \\vec{B} = 0,\\quad \\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t},\\quad \\nabla \\times \\vec{B} = \\mu_0 \\vec{J} + \\mu_0\\varepsilon_0 \\frac{\\partial \\vec{E}}{\\partial t}" },
      { name: "Vetor de Poynting e Densidade de Energia", eq: "\\vec{S} = \\frac{1}{\\mu_0}(\\vec{E} \\times \\vec{B}),\\quad u = \\frac{1}{2}\\left(\\varepsilon_0 E^2 + \\frac{1}{\\mu_0} B^2\\right)" },
      { name: "Potenciais e Transformação de Calibre", eq: "\\vec{B} = \\nabla \\times \\vec{A},\\quad \\vec{E} = -\\nabla V - \\frac{\\partial \\vec{A}}{\\partial t},\\quad \\nabla \\cdot \\vec{A} + \\frac{1}{c^2}\\frac{\\partial V}{\\partial t} = 0" },
      { name: "Força de Lorentz e Tensor de Maxwell", eq: "\\vec{F} = q(\\vec{E} + \\vec{v} \\times \\vec{B})" }
    ]
  },
  {
    category: "Mecânica Quântica",
    formulas: [
      { name: "Equação de Schrödinger Temporal", eq: "i\\hbar \\frac{\\partial}{\\partial t} |\\psi(t)\\rangle = \\hat{H} |\\psi(t)\\rangle" },
      { name: "Operadores de Criação e Aniquilação", eq: "\\hat{a} = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\left(\\hat{x} + \\frac{i\\hat{p}}{m\\omega}\\right),\\quad [\\hat{a}, \\hat{a}^\\dagger] = 1,\\quad \\hat{H} = \\hbar\\omega\\left(\\hat{a}^\\dagger \\hat{a} + \\frac{1}{2}\\right)" },
      { name: "Relações de Comutação de Momento Angular", eq: "[\\hat{J}_i, \\hat{J}_j] = i\\hbar \\sum_k \\varepsilon_{ijk}\\hat{J}_k,\\quad \\hat{J}_\\pm = \\hat{J}_x \\pm i\\hat{J}_y" },
      { name: "Teoria de Perturbações Não-Degenerada", eq: "E_n^{(1)} = \\langle n^{(0)}|\\hat{H}'|n^{(0)}\\rangle,\\quad |n^{(1)}\\rangle = \\sum_{k \\ne n} \\frac{\\langle k^{(0)}|\\hat{H}'|n^{(0)}\\rangle}{E_n^{(0)} - E_k^{(0)}} |k^{(0)}\\rangle" }
    ]
  },
  {
    category: "Termodinâmica e Física Estatística",
    formulas: [
      { name: "Primeira e Segunda Lei", eq: "dU = T dS - P dV + \\mu dN,\\quad dF = -S dT - P dV + \\mu dN" },
      { name: "Relações de Maxwell", eq: "\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial P}{\\partial S}\\right)_V,\\quad \\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_V" },
      { name: "Função de Partição Canônica & Grande Canônica", eq: "Z = \\sum_i e^{-\\beta E_i},\\quad \\Xi = \\sum_N e^{\\beta \\mu N} Z_N,\\quad F = -k_B T \\ln Z" },
      { name: "Distribuições Quânticas (Fermi-Dirac & Bose-Einstein)", eq: "\\bar{n}_s = \\frac{1}{e^{\\beta(\\varepsilon_s - \\mu)} \\pm 1}" }
    ]
  }
];
