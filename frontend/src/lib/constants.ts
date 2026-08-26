export interface AreaTheme {
  code: string;
  name: string;
  shortName: string;
  accentHex: string;
  bg: string;
  text: string;
  border: string;
  badge: string;
  glow: string;
  iconName: string;
}

export const AREA_THEMES: Record<string, AreaTheme> = {
  'Mecânica Clássica': {
    code: 'mc',
    name: 'Mecânica Clássica',
    shortName: 'Clássica',
    accentHex: '#10b981',
    bg: 'bg-emerald-950/40',
    text: 'text-emerald-300',
    border: 'border-emerald-500/30',
    badge: 'bg-emerald-950/60 text-emerald-300 border-emerald-500/40',
    glow: 'shadow-[0_0_12px_-2px_rgba(16,185,129,0.3)]',
    iconName: 'Orbit'
  },
  'Eletromagnetismo': {
    code: 'em',
    name: 'Eletromagnetismo',
    shortName: 'Eletromag',
    accentHex: '#38bdf8',
    bg: 'bg-sky-950/40',
    text: 'text-sky-300',
    border: 'border-sky-500/30',
    badge: 'bg-sky-950/60 text-sky-300 border-sky-500/40',
    glow: 'shadow-[0_0_12px_-2px_rgba(56,189,248,0.3)]',
    iconName: 'Zap'
  },
  'Mecânica Quântica': {
    code: 'mq',
    name: 'Mecânica Quântica',
    shortName: 'Quântica',
    accentHex: '#818cf8',
    bg: 'bg-indigo-950/40',
    text: 'text-indigo-300',
    border: 'border-indigo-500/30',
    badge: 'bg-indigo-950/60 text-indigo-300 border-indigo-500/40',
    glow: 'shadow-[0_0_12px_-2px_rgba(129,140,248,0.3)]',
    iconName: 'Atom'
  },
  'Termodinâmica': {
    code: 'te',
    name: 'Termodinâmica',
    shortName: 'Termo',
    accentHex: '#f59e0b',
    bg: 'bg-amber-950/40',
    text: 'text-amber-300',
    border: 'border-amber-500/30',
    badge: 'bg-amber-950/60 text-amber-300 border-amber-500/40',
    glow: 'shadow-[0_0_12px_-2px_rgba(245,158,11,0.3)]',
    iconName: 'Flame'
  },
  'Física Estatística': {
    code: 'fe',
    name: 'Física Estatística',
    shortName: 'Estatística',
    accentHex: '#14b8a6',
    bg: 'bg-teal-950/40',
    text: 'text-teal-300',
    border: 'border-teal-500/30',
    badge: 'bg-teal-950/60 text-teal-300 border-teal-500/40',
    glow: 'shadow-[0_0_12px_-2px_rgba(20,184,166,0.3)]',
    iconName: 'BarChart2'
  },
  'Física Moderna': {
    code: 'fm',
    name: 'Física Moderna',
    shortName: 'Moderna',
    accentHex: '#f43f5e',
    bg: 'bg-rose-950/40',
    text: 'text-rose-300',
    border: 'border-rose-500/30',
    badge: 'bg-rose-950/60 text-rose-300 border-rose-500/40',
    glow: 'shadow-[0_0_12px_-2px_rgba(244,63,94,0.3)]',
    iconName: 'Radio'
  }
};

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
      { name: "Força de Lorentz e Tensor de Tensões", eq: "\\vec{F} = q(\\vec{E} + \\vec{v} \\times \\vec{B}),\\quad T_{ij} = \\varepsilon_0\\left(E_i E_j - \\frac{1}{2}\\delta_{ij}E^2\\right) + \\frac{1}{\\mu_0}\\left(B_i B_j - \\frac{1}{2}\\delta_{ij}B^2\\right)" }
    ]
  },
  {
    category: "Mecânica Quântica",
    formulas: [
      { name: "Equação de Schrödinger", eq: "i\\hbar \\frac{\\partial}{\\partial t} |\\psi(t)\\rangle = \\hat{H} |\\psi(t)\\rangle" },
      { name: "Operadores de Criação e Aniquilação", eq: "\\hat{a} = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\left(\\hat{x} + \\frac{i\\hat{p}}{m\\omega}\\right),\\quad [\\hat{a}, \\hat{a}^\\dagger] = 1,\\quad \\hat{H} = \\hbar\\omega\\left(\\hat{a}^\\dagger \\hat{a} + \\frac{1}{2}\\right)" },
      { name: "Relações de Comutação Angular", eq: "[\\hat{J}_i, \\hat{J}_j] = i\\hbar \\sum_k \\varepsilon_{ijk}\\hat{J}_k,\\quad \\hat{J}_\\pm = \\hat{J}_x \\pm i\\hat{J}_y" },
      { name: "Teoria de Perturbações Não-Degenerada", eq: "E_n^{(1)} = \\langle n^{(0)}|\\hat{H}'|n^{(0)}\\rangle,\\quad |n^{(1)}\\rangle = \\sum_{k \\ne n} \\frac{\\langle k^{(0)}|\\hat{H}'|n^{(0)}\\rangle}{E_n^{(0)} - E_k^{(0)}} |k^{(0)}\\rangle" }
    ]
  },
  {
    category: "Termodinâmica e Física Estatística",
    formulas: [
      { name: "Primeira e Segunda Lei", eq: "dU = T dS - P dV + \\mu dN,\\quad dF = -S dT - P dV + \\mu dN" },
      { name: "Relações de Maxwell", eq: "\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial P}{\\partial S}\\right)_V,\\quad \\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_V" },
      { name: "Coletividades Estatísticas", eq: "Z = \\sum_i e^{-\\beta E_i},\\quad \\Xi = \\sum_N e^{\\beta \\mu N} Z_N,\\quad F = -k_B T \\ln Z" },
      { name: "Distribuições Quânticas (FD & BE)", eq: "\\bar{n}_s = \\frac{1}{e^{\\beta(\\varepsilon_s - \\mu)} + 1}\\text{ (Fermi)},\\quad \\bar{n}_s = \\frac{1}{e^{\\beta(\\varepsilon_s - \\mu)} - 1}\\text{ (Bose)}" }
    ]
  }
];
