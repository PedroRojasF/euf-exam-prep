export interface AreaTheme {
  code: string;
  name: string;
  shortName: string;
  pastelBg: string;
  pastelText: string;
  pastelBorder: string;
  badge: string;
  accentHex: string;
  iconName: string;
}

export const AREA_THEMES: Record<string, AreaTheme> = {
  'Mecânica Clássica': {
    code: 'mc',
    name: 'Mecânica Clássica',
    shortName: 'Clássica',
    pastelBg: 'bg-[#eafaf1]',
    pastelText: 'text-[#166534]',
    pastelBorder: 'border-[#bbf7d0]',
    badge: 'bg-[#eafaf1] text-[#166534] border-[#86efac]',
    accentHex: '#16a34a',
    iconName: 'Orbit'
  },
  'Eletromagnetismo': {
    code: 'em',
    name: 'Eletromagnetismo',
    shortName: 'Eletromag',
    pastelBg: 'bg-[#eff8ff]',
    pastelText: 'text-[#075985]',
    pastelBorder: 'border-[#bae6fd]',
    badge: 'bg-[#eff8ff] text-[#075985] border-[#7dd3fc]',
    accentHex: '#0284c7',
    iconName: 'Zap'
  },
  'Mecânica Quântica': {
    code: 'mq',
    name: 'Mecânica Quântica',
    shortName: 'Quântica',
    pastelBg: 'bg-[#f5f3ff]',
    pastelText: 'text-[#5b21b6]',
    pastelBorder: 'border-[#ddd6fe]',
    badge: 'bg-[#f5f3ff] text-[#5b21b6] border-[#c4b5fd]',
    accentHex: '#7c3aed',
    iconName: 'Atom'
  },
  'Termodinâmica': {
    code: 'te',
    name: 'Termodinâmica',
    shortName: 'Termo',
    pastelBg: 'bg-[#fffbeb]',
    pastelText: 'text-[#92400e]',
    pastelBorder: 'border-[#fde68a]',
    badge: 'bg-[#fffbeb] text-[#92400e] border-[#fcd34d]',
    accentHex: '#d97706',
    iconName: 'Flame'
  },
  'Física Estatística': {
    code: 'fe',
    name: 'Física Estatística',
    shortName: 'Estatística',
    pastelBg: 'bg-[#f0fdfa]',
    pastelText: 'text-[#115e59]',
    pastelBorder: 'border-[#99f6e4]',
    badge: 'bg-[#f0fdfa] text-[#115e59] border-[#5eead4]',
    accentHex: '#0d9488',
    iconName: 'BarChart2'
  },
  'Física Moderna': {
    code: 'fm',
    name: 'Física Moderna',
    shortName: 'Moderna',
    pastelBg: 'bg-[#fff1f2]',
    pastelText: 'text-[#9f1239]',
    pastelBorder: 'border-[#fecdd3]',
    badge: 'bg-[#fff1f2] text-[#9f1239] border-[#fda4af]',
    accentHex: '#e11d48',
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
