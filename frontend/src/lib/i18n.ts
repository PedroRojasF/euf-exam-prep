export type Language = 'pt' | 'es' | 'en';

export interface Translations {
  // Brand & Header
  appTitle: string;
  appSubtitle: string;
  bankTotal: string;
  mastered: string;
  forReview: string;
  toRetry: string;
  unsolved: string;
  timerLabel: string;
  timerLimitReached: string;
  profile: string;
  newProfile: string;
  exportProfile: string;
  importProfile: string;
  profileImported: string;
  profileImportError: string;
  enterProfileName: string;

  // View Modes
  modeStudy: string;
  modeTwins: string;
  modeMock: string;
  modeMap: string;
  modeFormulas: string;

  // Mock Exam
  mockExamTitle: string;
  mockExamSubtitle: string;
  startMockExam: string;
  finishMockExam: string;
  mockExamCompleted: string;
  questionOf: string;
  answeredCount: string;
  flagForReview: string;
  reviewLater: string;
  submitExam: string;
  confirmSubmitTitle: string;
  confirmSubmitBody: string;
  cancelMockExam: string;
  confirmCancelTitle: string;
  confirmCancelBody: string;
  discardAndExit: string;
  continueExam: string;
  examScore: string;
  performanceByArea: string;
  retakeExam: string;
  backToStudy: string;

  // Explorer & Motivational Progress
  allAreas: string;
  allSubtopics: string;
  allExams: string;
  allStatuses: string;
  searchPlaceholder: string;
  searchFormulaPlaceholder: string;
  randomQuestion: string;
  prevQuestion: string;
  nextQuestion: string;
  advancedFilters: string;
  questionsCount: string;
  poolMastery: string;
  progressEncourageZero: string;
  progressEncourageMid: string;
  progressEncourageHigh: string;
  noQuestionsFound: string;
  errataNotice: string;

  // Problem Canvas & Typographic Hierarchy
  subtopicLabel: string;
  twinVariant: string;
  openTwinInCanvas: string;
  adjustSize: string;
  fullscreen: string;
  closeEsc: string;
  mathTranscription: string;
  statusMastered: string;
  statusReview: string;
  statusFailed: string;
  selectQuestionPrompt: string;

  // Right Companion Tabs & Socratic Ladder
  tabHints: string;
  tabNotes: string;
  tabFormulas: string;
  tabTwin: string;
  levelsCount: string;
  hintsInstruction: string;
  level1Title: string;
  level2Title: string;
  level3Title: string;
  level4Title: string;
  scratchpadTitle: string;
  scratchpadPlaceholder: string;
  scratchpadTip: string;
  savedToProfile: string;
  constantsTitle: string;
  officialFormulasTitle: string;
  noTwinIndexed: string;
  parametricDiffs: string;

  // Twin Lab View
  twinLabTitle: string;
  twinLabSubtitle: string;
  twinPairsCataloged: string;
  prevPair: string;
  nextPair: string;
  stemLabel: string;
  variantA: string;
  variantB: string;
  studyInCanvas: string;
  variationAnalysis: string;

  // Taxonomy Map View
  taxonomyTitle: string;
  taxonomySubtitle: string;
  loadingMap: string;

  // Formulas View
  formulaSheetTitle: string;
  formulaSheetSubtitle: string;
  equationsCount: string;

  // Keyboard Shortcuts Modal
  shortcutsTitle: string;
  continueStudy: string;
  scNext: string;
  scPrev: string;
  scSolved: string;
  scReview: string;
  scFailed: string;
  scZoom: string;
  scTwin: string;
  scHints: string;
  scModeStudy: string;
  scModeMap: string;
  scModeFormulas: string;
  scHelp: string;
  scEsc: string;
}

export const DICTIONARY: Record<Language, Translations> = {
  pt: {
    appTitle: "EUF Exam Master",
    appSubtitle: "Exame Unificado de Pós-Graduação em Física",
    bankTotal: "Banco de Questões",
    mastered: "Dominadas",
    forReview: "Revisão",
    toRetry: "Repetir",
    unsolved: "Pendentes",
    timerLabel: "Cronômetro",
    timerLimitReached: "⏱️ Tempo limite de 15 minutos atingido!",
    profile: "Perfil",
    newProfile: "Novo",
    exportProfile: "Exportar",
    importProfile: "Importar Perfil (.json)",
    profileImported: "✅ Perfil importado com sucesso!",
    profileImportError: "❌ Erro ao importar arquivo JSON de perfil.",
    enterProfileName: "Nome do novo perfil (ex: candidato_usp):",

    modeStudy: "Estudo",
    modeTwins: "Gêmeas",
    modeMock: "Simulado",
    modeMap: "Mapa",
    modeFormulas: "Fórmulas",

    mockExamTitle: "Simulado Oficial EUF",
    mockExamSubtitle: "Experiência real cronometrada de 4 horas com gabarito interativo.",
    startMockExam: "Iniciar Simulado (4h)",
    finishMockExam: "Finalizar e Entregar Prova",
    mockExamCompleted: "Simulado Concluído!",
    questionOf: "Questão",
    answeredCount: "Respondidas",
    flagForReview: "Marcar para Revisar",
    reviewLater: "Revisar",
    submitExam: "Entregar Prova",
    confirmSubmitTitle: "Deseja realmente entregar o simulado?",
    confirmSubmitBody: "Você respondeu {answered} de {total} questões. Questões em branco serão computadas como não respondidas.",
    cancelMockExam: "Cancelar Simulado",
    confirmCancelTitle: "Deseja cancelar o simulado atual?",
    confirmCancelBody: "Seu progresso e respostas desta sessão não serão salvos.",
    discardAndExit: "Descartar e Sair",
    continueExam: "Continuar Prova",
    examScore: "Pontuação Final",
    performanceByArea: "Desempenho por Matéria",
    retakeExam: "Novo Simulado",
    backToStudy: "Voltar ao Modo Estudo",

    allAreas: "Todas as Matérias",
    allSubtopics: "Todos os Subtópicos",
    allExams: "Todas as Edições",
    allStatuses: "Todos os Estados",
    searchPlaceholder: "Buscar física ou código...",
    searchFormulaPlaceholder: "Buscar equações (ex: Maxwell, Poisson, Carnot)...",
    randomQuestion: "Questão Aleatória",
    prevQuestion: "Anterior (J)",
    nextQuestion: "Próxima (K)",
    advancedFilters: "Filtros",
    questionsCount: "Questões",
    poolMastery: "Domínio do Bloco",
    progressEncourageZero: "Comece sua sessão deliberada",
    progressEncourageMid: "Ótimo ritmo! Continue avançando",
    progressEncourageHigh: "Excelente domínio deste bloco!",
    noQuestionsFound: "Nenhuma questão encontrada com estes filtros.",
    errataNotice: "Aviso da Banca / Errata Oficial",

    subtopicLabel: "Tópico Oficial",
    twinVariant: "Gêmea",
    openTwinInCanvas: "Estudar no Canvas",
    adjustSize: "Ajustar Escala",
    fullscreen: "Tela Cheia (Z)",
    closeEsc: "Fechar (Esc)",
    mathTranscription: "Transcrição Matemática (LaTeX):",
    statusMastered: "Dominada",
    statusReview: "Revisão",
    statusFailed: "Erro",
    selectQuestionPrompt: "Selecione uma questão no explorador para iniciar.",

    tabHints: "Pistas Socráticas (1-4)",
    tabNotes: "Anotações",
    tabFormulas: "Constantes & Fórmulas",
    tabTwin: "Variante Gêmea",
    levelsCount: "Níveis",
    hintsInstruction: "Pressione as teclas 1 a 4 para revelar a intuição física gradualmente.",
    level1Title: "1. Princípio Físico Fundamental",
    level2Title: "2. Geometria & Escolha de Coordenadas",
    level3Title: "3. Ponto de Checagem & Casos Limite",
    level4Title: "4. Derivação & Armadilhas da Banca",
    scratchpadTitle: "Caderno de Resolução:",
    scratchpadPlaceholder: "Escreva suas equações com $...$, passos intermediários ou armadilhas a recordar...",
    scratchpadTip: "💡 Suporta equações matemáticas em LaTeX.",
    savedToProfile: "Salvo no perfil",
    constantsTitle: "Constantes Fundamentais:",
    officialFormulasTitle: "Formulário Oficial:",
    noTwinIndexed: "Esta questão não possui variante gêmea A/B indexada.",
    parametricDiffs: "Diferenças Paramétricas:",

    twinLabTitle: "Laboratório de Variantes Gêmeas (A/B)",
    twinLabSubtitle: "Contraste as alterações paramétricas e geométricas entre as duas versões de prova.",
    twinPairsCataloged: "pares indexados",
    prevPair: "Par Anterior",
    nextPair: "Próximo Par",
    stemLabel: "Haste Base",
    variantA: "Variante A",
    variantB: "Variante B",
    studyInCanvas: "Abrir no Canvas",
    variationAnalysis: "🔬 Análise Comparativa de Variações:",

    taxonomyTitle: "Taxonomia Oficial & Matriz de Domínio",
    taxonomySubtitle: "Acompanhe seu avanço percentual e filtre diretamente qualquer subtópico.",
    loadingMap: "Carregando taxonomia...",

    formulaSheetTitle: "Formulário Oficial EUF (Referência)",
    formulaSheetSubtitle: "Equações fundamentais fornecidas nos cadernos de prova oficiais.",
    equationsCount: "equações",

    shortcutsTitle: "Atalhos de Teclado Científicos",
    continueStudy: "Continuar Estudos",
    scNext: "Próxima questão da lista",
    scPrev: "Questão anterior da lista",
    scSolved: "Marcar como Dominada (Solved) + 🎉",
    scReview: "Marcar para Revisão (Review)",
    scFailed: "Marcar como Erro a Repetir (Failed)",
    scZoom: "Alternar modo Zoom / Tela Cheia",
    scTwin: "Ir diretamente para a Variante Irmã (Gêmea)",
    scHints: "Alternar Pistas Socráticas 1 a 4",
    scModeStudy: "Modo Estudo",
    scModeMap: "Mapa de Tópicos",
    scModeFormulas: "Formulário Oficial",
    scHelp: "Menu de Ajuda",
    scEsc: "Fechar Modais"
  },
  es: {
    appTitle: "EUF Exam Master",
    appSubtitle: "Examen Unificado de Posgrado en Física",
    bankTotal: "Banco de Preguntas",
    mastered: "Dominadas",
    forReview: "Revisión",
    toRetry: "Repetir",
    unsolved: "Pendientes",
    timerLabel: "Temporizador",
    timerLimitReached: "⏱️ ¡Tiempo límite de 15 minutos alcanzado!",
    profile: "Perfil",
    newProfile: "Nuevo",
    exportProfile: "Exportar",
    importProfile: "Importar Perfil (.json)",
    profileImported: "✅ ¡Perfil importado exitosamente!",
    profileImportError: "❌ Error al importar archivo JSON.",
    enterProfileName: "Nombre del nuevo perfil (ej: postulante_usp):",

    modeStudy: "Estudio",
    modeTwins: "Gemelas",
    modeMock: "Simulacro",
    modeMap: "Mapa",
    modeFormulas: "Fórmulas",

    mockExamTitle: "Simulacro Oficial EUF",
    mockExamSubtitle: "Experiencia real cronometrada de 4 horas con hoja de respuestas interactiva.",
    startMockExam: "Iniciar Simulacro (4h)",
    finishMockExam: "Finalizar y Entregar Prueba",
    mockExamCompleted: "¡Simulacro Completado!",
    questionOf: "Pregunta",
    answeredCount: "Respondidas",
    flagForReview: "Marcar para Revisar",
    reviewLater: "Revisar",
    submitExam: "Entregar Prueba",
    confirmSubmitTitle: "¿Deseas realmente entregar la prueba?",
    confirmSubmitBody: "Has respondido {answered} de {total} preguntas. Las preguntas en blanco se computarán como no respondidas.",
    cancelMockExam: "Cancelar Simulacro",
    confirmCancelTitle: "¿Deseas cancelar el simulacro actual?",
    confirmCancelBody: "Tu progreso y respuestas de esta sesión no se guardarán.",
    discardAndExit: "Descartar y Salir",
    continueExam: "Continuar Prueba",
    examScore: "Puntuación Final",
    performanceByArea: "Rendimiento por Materia",
    retakeExam: "Nuevo Simulacro",
    backToStudy: "Volver a Modo Estudio",

    allAreas: "Todas las Materias",
    allSubtopics: "Todos los Subtópicos",
    allExams: "Todas las Ediciones",
    allStatuses: "Todos los Estados",
    searchPlaceholder: "Buscar física o código...",
    searchFormulaPlaceholder: "Buscar fórmulas (ej: Maxwell, Poisson, Carnot)...",
    randomQuestion: "Pregunta Aleatoria",
    prevQuestion: "Anterior (J)",
    nextQuestion: "Siguiente (K)",
    advancedFilters: "Filtros",
    questionsCount: "Preguntas",
    poolMastery: "Dominio del Bloque",
    progressEncourageZero: "Inicia tu sesión deliberada",
    progressEncourageMid: "¡Buen ritmo! Sigue avanzando",
    progressEncourageHigh: "¡Excelente dominio de este bloque!",
    noQuestionsFound: "No se encontraron preguntas con estos filtros.",
    errataNotice: "Aviso de la Comisión / Errata Oficial",

    subtopicLabel: "Tópico Oficial",
    twinVariant: "Gemela",
    openTwinInCanvas: "Estudiar en Canvas",
    adjustSize: "Ajustar Escala",
    fullscreen: "Pantalla Completa (Z)",
    closeEsc: "Cerrar (Esc)",
    mathTranscription: "Transcripción Matemática (LaTeX):",
    statusMastered: "Dominada",
    statusReview: "Revisión",
    statusFailed: "Error",
    selectQuestionPrompt: "Selecciona una pregunta en el explorador para comenzar.",

    tabHints: "Pistas Socráticas (1-4)",
    tabNotes: "Notas",
    tabFormulas: "Constantes y Fórmulas",
    tabTwin: "Variante Gemela",
    levelsCount: "Niveles",
    hintsInstruction: "Presiona las teclas 1 a 4 para revelar la intuición física paso a paso.",
    level1Title: "1. Principio Físico Fundamental",
    level2Title: "2. Geometría y Elección de Coordenadas",
    level3Title: "3. Punto de Control y Casos Límite",
    level4Title: "4. Derivación y Trampas del Examen",
    scratchpadTitle: "Cuaderno de Resolución:",
    scratchpadPlaceholder: "Escribe tus ecuaciones con $...$, pasos intermedios o puntos clave...",
    scratchpadTip: "💡 Soporta ecuaciones matemáticas en LaTeX.",
    savedToProfile: "Guardado en perfil",
    constantsTitle: "Constantes Fundamentales:",
    officialFormulasTitle: "Formulario Oficial:",
    noTwinIndexed: "Esta pregunta no posee variante gemela A/B indexada.",
    parametricDiffs: "Diferencias Paramétricas:",

    twinLabTitle: "Laboratorio de Variantes Gemelas (A/B)",
    twinLabSubtitle: "Contrasta las alteraciones paramétricas y geométricas entre las dos versiones de examen.",
    twinPairsCataloged: "pares indexados",
    prevPair: "Par Anterior",
    nextPair: "Siguiente Par",
    stemLabel: "Tallo Base",
    variantA: "Variante A",
    variantB: "Variante B",
    studyInCanvas: "Abrir en Canvas",
    variationAnalysis: "🔬 Análisis Comparativo de Variaciones:",

    taxonomyTitle: "Taxonomía Oficial & Matriz de Dominio",
    taxonomySubtitle: "Sigue tu avance porcentual y filtra directamente cualquier subtópico.",
    loadingMap: "Cargando taxonomía...",

    formulaSheetTitle: "Formulario Oficial EUF (Referencia)",
    formulaSheetSubtitle: "Ecuaciones fundamentales suministradas en los exámenes oficiales.",
    equationsCount: "ecuaciones",

    shortcutsTitle: "Atajos de Teclado Científicos",
    continueStudy: "Continuar Estudios",
    scNext: "Siguiente pregunta de la lista",
    scPrev: "Pregunta anterior de la lista",
    scSolved: "Marcar como Dominada (Solved) + 🎉",
    scReview: "Marcar para Revisión (Review)",
    scFailed: "Marcar como Error a Repetir (Failed)",
    scZoom: "Alternar modo Zoom / Pantalla Completa",
    scTwin: "Ir directamente a la Variante Hermana (Gemela)",
    scHints: "Alternar Pistas Socráticas 1 a 4",
    scModeStudy: "Modo Estudio",
    scModeMap: "Mapa de Tópicos",
    scModeFormulas: "Formulario Oficial",
    scHelp: "Menú de Ayuda",
    scEsc: "Cerrar Modales"
  },
  en: {
    appTitle: "EUF Exam Master",
    appSubtitle: "Unified Physics Graduate Examination Practice System",
    bankTotal: "Question Bank",
    mastered: "Mastered",
    forReview: "Review",
    toRetry: "To Retry",
    unsolved: "Unsolved",
    timerLabel: "Timer",
    timerLimitReached: "⏱️ 15-minute time limit reached!",
    profile: "Profile",
    newProfile: "New",
    exportProfile: "Export",
    importProfile: "Import Profile (.json)",
    profileImported: "✅ Profile imported successfully!",
    profileImportError: "❌ Error importing profile JSON file.",
    enterProfileName: "Enter new profile name (e.g. usp_candidate):",

    modeStudy: "Study",
    modeTwins: "Twins",
    modeMock: "Mock Exam",
    modeMap: "Map",
    modeFormulas: "Formulas",

    mockExamTitle: "Official EUF Mock Exam",
    mockExamSubtitle: "Real timed 4-hour examination session with interactive bubble answer sheet.",
    startMockExam: "Start Mock Exam (4h)",
    finishMockExam: "Submit & Finish Exam",
    mockExamCompleted: "Mock Exam Completed!",
    questionOf: "Question",
    answeredCount: "Answered",
    flagForReview: "Flag for Review",
    reviewLater: "Review",
    submitExam: "Submit Exam",
    confirmSubmitTitle: "Are you sure you want to submit?",
    confirmSubmitBody: "You have answered {answered} of {total} questions. Unanswered questions will count as blank.",
    cancelMockExam: "Cancel Mock Exam",
    confirmCancelTitle: "Do you want to cancel this mock exam?",
    confirmCancelBody: "Your progress and answers in this session will be discarded.",
    discardAndExit: "Discard & Exit",
    continueExam: "Continue Exam",
    examScore: "Final Score",
    performanceByArea: "Performance by Subject Area",
    retakeExam: "Start New Mock Exam",
    backToStudy: "Back to Study Mode",

    allAreas: "All Subject Areas",
    allSubtopics: "All Subtopics",
    allExams: "All Editions",
    allStatuses: "All Statuses",
    searchPlaceholder: "Search physics term or code...",
    searchFormulaPlaceholder: "Search formulas (e.g. Maxwell, Poisson, Carnot)...",
    randomQuestion: "Random Problem",
    prevQuestion: "Previous (J)",
    nextQuestion: "Next (K)",
    advancedFilters: "Filters",
    questionsCount: "Questions",
    poolMastery: "Pool Mastery",
    progressEncourageZero: "Begin your deliberate practice session",
    progressEncourageMid: "Great momentum! Keep pushing forward",
    progressEncourageHigh: "Outstanding mastery of this topic block!",
    noQuestionsFound: "No questions matched the selected filters.",
    errataNotice: "Committee Notice / Official Errata",

    subtopicLabel: "Official Topic",
    twinVariant: "Twin Sister",
    openTwinInCanvas: "Study in Canvas",
    adjustSize: "Toggle Scale",
    fullscreen: "Fullscreen (Z)",
    closeEsc: "Close (Esc)",
    mathTranscription: "Mathematical Transcription (LaTeX):",
    statusMastered: "Mastered",
    statusReview: "Review",
    statusFailed: "Failed",
    selectQuestionPrompt: "Select a question in the explorer to begin practicing.",

    tabHints: "Socratic Hints (1-4)",
    tabNotes: "Notes",
    tabFormulas: "Constants & Formulas",
    tabTwin: "Twin Variant",
    levelsCount: "Levels",
    hintsInstruction: "Press keys 1 to 4 to reveal physical intuition progressively.",
    level1Title: "1. Fundamental Physical Principle",
    level2Title: "2. Geometry & Coordinate Setup",
    level3Title: "3. Intermediate Checkpoint & Limits",
    level4Title: "4. Full Derivation & Committee Traps",
    scratchpadTitle: "Solution Scratchpad:",
    scratchpadPlaceholder: "Write down your derivations, math steps with $...$, or key reminders...",
    scratchpadTip: "💡 Supports LaTeX mathematical equations.",
    savedToProfile: "Saved to profile",
    constantsTitle: "Fundamental Constants:",
    officialFormulasTitle: "Official Formulas:",
    noTwinIndexed: "No twin A/B variant indexed for this question.",
    parametricDiffs: "Parametric Differences:",

    twinLabTitle: "Twin A/B Variant Laboratory",
    twinLabSubtitle: "Contrast parametric and geometric variations designed for parallel exam forms.",
    twinPairsCataloged: "cataloged pairs",
    prevPair: "Previous Pair",
    nextPair: "Next Pair",
    stemLabel: "Base Stem",
    variantA: "Variant A",
    variantB: "Variant B",
    studyInCanvas: "Open in Canvas",
    variationAnalysis: "🔬 Comparative Variation Analysis:",

    taxonomyTitle: "Official Taxonomy & Mastery Matrix",
    taxonomySubtitle: "Track your mastery percentage and deliberate practice any subtopic.",
    loadingMap: "Loading taxonomy...",

    formulaSheetTitle: "Official EUF Formula Sheet (Reference)",
    formulaSheetSubtitle: "Canonical equations provided in official graduate exam booklets.",
    equationsCount: "equations",

    shortcutsTitle: "Scientific Keyboard Shortcuts",
    continueStudy: "Continue Practicing",
    scNext: "Next question in pool",
    scPrev: "Previous question in pool",
    scSolved: "Mark as Mastered (Solved) + 🎉",
    scReview: "Mark for Review",
    scFailed: "Mark as Failed (To Retry)",
    scZoom: "Toggle Fullscreen Zoom",
    scTwin: "Jump directly to Twin Sister (Variant A/B)",
    scHints: "Toggle Socratic Hint Levels 1 to 4",
    scModeStudy: "Study Mode",
    scModeMap: "Taxonomy Map",
    scModeFormulas: "Official Formula Sheet",
    scHelp: "Help Menu",
    scEsc: "Close Dialogs"
  }
};

export const AREA_TRANSLATIONS: Record<Language, Record<string, string>> = {
  pt: {
    'Mecânica Clássica': 'Mecânica Clássica',
    'Eletromagnetismo': 'Eletromagnetismo',
    'Mecânica Quântica': 'Mecânica Quântica',
    'Termodinâmica': 'Termodinâmica',
    'Física Estatística': 'Física Estatística',
    'Física Moderna': 'Física Moderna'
  },
  es: {
    'Mecânica Clássica': 'Mecánica Clásica',
    'Eletromagnetismo': 'Electromagnetismo',
    'Mecânica Quântica': 'Mecánica Cuántica',
    'Termodinâmica': 'Termodinámica',
    'Física Estatística': 'Física Estadística',
    'Física Moderna': 'Física Moderna'
  },
  en: {
    'Mecânica Clássica': 'Classical Mechanics',
    'Eletromagnetismo': 'Electromagnetism',
    'Mecânica Quântica': 'Quantum Mechanics',
    'Termodinâmica': 'Thermodynamics',
    'Física Estatística': 'Statistical Physics',
    'Física Moderna': 'Modern Physics'
  }
};

export const SUBTOPIC_TRANSLATIONS: Record<Language, Record<string, string>> = {
  pt: {
    '1D Potential Wells, Barriers & Quantum Tunneling': 'Poços 1D, Barreiras de Potencial e Tunelamento',
    '1st & 2nd Laws / Thermodynamic Cycles': '1ª e 2ª Leis / Ciclos Termodinâmicos',
    'Angular Momentum, Spin Algebra & Addition of Momenta': 'Momento Angular, Álgebra de Spin e Adição de Momentos',
    'Atomic Models (Bohr, Rydberg & Franck-Hertz)': 'Modelos Atômicos (Bohr, Rydberg e Franck-Hertz)',
    'Biot-Savart Law & Magnetic Fields of Currents': 'Lei de Biot-Savart e Campos Magnéticos de Correntes',
    'Blackbody Radiation & Quantum Optics': 'Radiação de Corpo Negro e Óptica Quântica',
    'Boundary Value Problems & Method of Images': 'Problemas de Contorno e Método das Imagens',
    'Calorimetry, Heat Capacities & Thermal Expansion': 'Calorimetria, Capacidades Térmicas e Dilatação',
    'Canonical & Microcanonical Ensembles': 'Ensembles Canônico e Microcanônico',
    'Capacitors & Dielectric Media': 'Capacitores e Meios Dielétricos',
    'Central Forces, Kepler Orbits & Effective Potential': 'Forças Centrais, Órbitas de Kepler e Potencial Efetivo',
    'Collisions, Momentum Conservation & Variable Mass': 'Colisões, Conservação do Momento e Massa Variável',
    'Conductors, Cavities & Electrostatic Shielding': 'Condutores, Cavidades e Blindagem Eletrostática',
    'Continuous Charge Distributions & Electric Potentials': 'Distribuições Contínuas de Carga e Potencial Elétrico',
    'DC Circuits, Resistors & Joule Heating': 'Circuitos de Corrente Contínua, Resistores e Efeito Joule',
    'Dirac Formalism, State Vectors & Hilbert Space': 'Formalismo de Dirac, Vetores de Estado e Espaço de Hilbert',
    "EM Wave Polarization & Malus's Law": 'Polarização de Ondas EM e Lei de Malus',
    'Entropy Changes & Reversibility': 'Variação de Entropia e Reversibilidade',
    "Faraday's Law, Motional EMF & Inductance": 'Lei de Faraday, FEM Induzida e Indutância',
    'Grand Canonical Ensemble & Chemical Potential': 'Ensemble Grande Canônico e Potencial Químico',
    'Hamiltonian Mechanics & Phase Space Dynamics': 'Mecânica Hamiltoniana e Dinâmica no Espaço de Fase',
    'Harmonic Oscillator & Ladder Operators': 'Oscilador Harmônico e Operadores Escada',
    'Hydrogen Atom & Central Potentials': 'Átomo de Hidrogênio e Potenciais Centrais',
    'Ideal & Real Gases (Equation of State)': 'Gases Ideais e Reais (Equação de Estado)',
    'Identical Particles, Bosons/Fermions & Symmetry': 'Partículas Idênticas, Bósons/Férmions e Simetria',
    'Lagrangian Mechanics & Generalized Coordinates': 'Mecânica Lagrangiana e Coordenadas Generalizadas',
    'Lorentz Force & Particle Trajectories in EM Fields': 'Força de Lorentz e Trajetórias em Campos EM',
    'Magnetic Dipoles, Forces & Magnetic Media': 'Dipolos Magnéticos, Forças e Meios Magnéticos',
    'Matter Waves & de Broglie Hypothesis': 'Ondas de Matéria e Hipótese de de Broglie',
    'Maxwell Equations & Displacement Current': 'Equações de Maxwell e Corrente de Deslocamento',
    'Newtonian Dynamics & Non-Inertial Frames': 'Dinâmica Newtoniana e Referenciais Não-Inerciais',
    'Nuclear Physics & Radioactive Decay': 'Física Nuclear e Decaimento Radioativo',
    'Perturbation Theory & Approximation Methods': 'Teoria de Perturbações e Métodos de Aproximação',
    'Phase Transitions & Clausius-Clapeyron': 'Transições de Fase e Clausius-Clapeyron',
    'Photoelectric Effect & Photon Interactions': 'Efeito Fotoelétrico e Interações de Fótons',
    'Poynting Vector & EM Wave Propagation': 'Vetor de Poynting e Propagação de Ondas EM',
    'Quantum Gases (Bose-Einstein Condensation & Blackbody)': 'Gases Quânticos (Condensação de Bose-Einstein)',
    'Quantum Gases (Fermi-Dirac & Degeneracy)': 'Gases Quânticos (Degenerescência de Fermi-Dirac)',
    'Relativistic Dynamics & Energy-Momentum': 'Dinâmica Relativística e Energia-Momento',
    'Rigid Body Dynamics & Moments of Inertia': 'Dinâmica de Corpos Rígidos e Momentos de Inércia',
    'Small Oscillations, Coupled Systems & Normal Modes': 'Pequenas Oscilações, Sistemas Acoplados e Modos Normais',
    'Special Relativity & Lorentz Transformations': 'Relatividade Especial e Transformações de Lorentz',
    'Spin Systems, Paramagnetism & Ising Model': 'Sistemas de Spin, Paramagnetismo e Modelo de Ising',
    'Thermodynamic Potentials & Maxwell Relations': 'Potenciais Termodinâmicos e Relações de Maxwell',
    'Two-Level Systems & Paramagnetic Entropy': 'Sistemas de Dois Níveis e Entropia Paramagnética',
    'Vector Calculus & Field Operators': 'Cálculo Vetorial e Operadores de Campo',
    'Work-Energy Theorem & 1D Potential Dynamics': 'Teorema Trabalho-Energia e Potenciais 1D'
  },
  es: {
    '1D Potential Wells, Barriers & Quantum Tunneling': 'Pozos 1D, Barreras de Potencial y Efecto Túnel',
    '1st & 2nd Laws / Thermodynamic Cycles': '1ª y 2ª Ley / Ciclos Termodinámicos',
    'Angular Momentum, Spin Algebra & Addition of Momenta': 'Momento Angular, Álgebra de Espín y Suma de Momentos',
    'Atomic Models (Bohr, Rydberg & Franck-Hertz)': 'Modelos Atómicos (Bohr, Rydberg y Franck-Hertz)',
    'Biot-Savart Law & Magnetic Fields of Currents': 'Ley de Biot-Savart y Campos Magnéticos de Corrientes',
    'Blackbody Radiation & Quantum Optics': 'Radiación de Cuerpo Negro y Óptica Cuántica',
    'Boundary Value Problems & Method of Images': 'Problemas de Contorno y Método de las Imágenes',
    'Calorimetry, Heat Capacities & Thermal Expansion': 'Calorimetría, Capacidades Térmicas y Dilatación',
    'Canonical & Microcanonical Ensembles': 'Ensambles Canónico y Microcanónico',
    'Capacitors & Dielectric Media': 'Condensadores y Medios Dieléctricos',
    'Central Forces, Kepler Orbits & Effective Potential': 'Fuerzas Centrales, Órbitas de Kepler y Potencial Efectivo',
    'Collisions, Momentum Conservation & Variable Mass': 'Colisiones, Conservación del Momento y Masa Variable',
    'Conductors, Cavities & Electrostatic Shielding': 'Conductores, Cavidades y Blindaje Electrostático',
    'Continuous Charge Distributions & Electric Potentials': 'Distribuciones Continuas de Carga y Potencial Eléctrico',
    'DC Circuits, Resistors & Joule Heating': 'Circuitos de Corriente Continua, Resistores y Efecto Joule',
    'Dirac Formalism, State Vectors & Hilbert Space': 'Formalismo de Dirac, Vectores de Estado y Espacio de Hilbert',
    "EM Wave Polarization & Malus's Law": 'Polarización de Ondas EM y Ley de Malus',
    'Entropy Changes & Reversibility': 'Cambios de Entropía y Reversibilidad',
    "Faraday's Law, Motional EMF & Inductance": 'Ley de Faraday, FEM Inducida e Inductancia',
    'Grand Canonical Ensemble & Chemical Potential': 'Ensamble Gran Canónico y Potencial Químico',
    'Hamiltonian Mechanics & Phase Space Dynamics': 'Mecánica Hamiltoniana y Dinámica en el Espacio de Fases',
    'Harmonic Oscillator & Ladder Operators': 'Oscilador Armónico y Operadores Escalera',
    'Hydrogen Atom & Central Potentials': 'Átomo de Hidrógeno y Potenciales Centrales',
    'Ideal & Real Gases (Equation of State)': 'Gases Ideales y Reales (Ecuación de Estado)',
    'Identical Particles, Bosons/Fermions & Symmetry': 'Partículas Idénticas, Bosones/Fermiones y Simetría',
    'Lagrangian Mechanics & Generalized Coordinates': 'Mecánica Lagrangiana y Coordenadas Generalizadas',
    'Lorentz Force & Particle Trajectories in EM Fields': 'Fuerza de Lorentz y Trayectorias en Campos EM',
    'Magnetic Dipoles, Forces & Magnetic Media': 'Dipolos Magnéticos, Fuerzas y Medios Magnéticos',
    'Matter Waves & de Broglie Hypothesis': 'Ondas de Materia e Hipótesis de de Broglie',
    'Maxwell Equations & Displacement Current': 'Ecuaciones de Maxwell y Corriente de Desplazamiento',
    'Newtonian Dynamics & Non-Inertial Frames': 'Dinámica Newtoniana y Sistemas No Inerciales',
    'Nuclear Physics & Radioactive Decay': 'Física Nuclear y Decaimiento Radiactivo',
    'Perturbation Theory & Approximation Methods': 'Teoría de Perturbaciones y Métodos de Aproximación',
    'Phase Transitions & Clausius-Clapeyron': 'Transiciones de Fase y Clausius-Clapeyron',
    'Photoelectric Effect & Photon Interactions': 'Efecto Fotoeléctrico e Interacciones Fotónicas',
    'Poynting Vector & EM Wave Propagation': 'Vector de Poynting y Propagación de Ondas EM',
    'Quantum Gases (Bose-Einstein Condensation & Blackbody)': 'Gases Cuánticos (Condensación de Bose-Einstein)',
    'Quantum Gases (Fermi-Dirac & Degeneracy)': 'Gases Cuánticos (Degeneración de Fermi-Dirac)',
    'Relativistic Dynamics & Energy-Momentum': 'Dinámica Relativista y Energía-Momento',
    'Rigid Body Dynamics & Moments of Inertia': 'Dinámica del Sólido Rígido y Momentos de Inercia',
    'Small Oscillations, Coupled Systems & Normal Modes': 'Pequeñas Oscilaciones, Sistemas Acoplados y Modos Normales',
    'Special Relativity & Lorentz Transformations': 'Relatividad Especial y Transformaciones de Lorentz',
    'Spin Systems, Paramagnetism & Ising Model': 'Sistemas de Espín, Paramagnetismo y Modelo de Ising',
    'Thermodynamic Potentials & Maxwell Relations': 'Potenciales Termodinámicos y Relaciones de Maxwell',
    'Two-Level Systems & Paramagnetic Entropy': 'Sistemas de Dos Niveles y Entropía Paramagnética',
    'Vector Calculus & Field Operators': 'Cálculo Vectorial y Operadores de Campo',
    'Work-Energy Theorem & 1D Potential Dynamics': 'Teorema del Trabajo-Energía y Dinámica en Potenciales 1D'
  },
  en: {
    '1D Potential Wells, Barriers & Quantum Tunneling': '1D Potential Wells, Barriers & Quantum Tunneling',
    '1st & 2nd Laws / Thermodynamic Cycles': '1st & 2nd Laws / Thermodynamic Cycles',
    'Angular Momentum, Spin Algebra & Addition of Momenta': 'Angular Momentum, Spin Algebra & Addition of Momenta',
    'Atomic Models (Bohr, Rydberg & Franck-Hertz)': 'Atomic Models (Bohr, Rydberg & Franck-Hertz)',
    'Biot-Savart Law & Magnetic Fields of Currents': 'Biot-Savart Law & Magnetic Fields of Currents',
    'Blackbody Radiation & Quantum Optics': 'Blackbody Radiation & Quantum Optics',
    'Boundary Value Problems & Method of Images': 'Boundary Value Problems & Method of Images',
    'Calorimetry, Heat Capacities & Thermal Expansion': 'Calorimetry, Heat Capacities & Thermal Expansion',
    'Canonical & Microcanonical Ensembles': 'Canonical & Microcanonical Ensembles',
    'Capacitors & Dielectric Media': 'Capacitors & Dielectric Media',
    'Central Forces, Kepler Orbits & Effective Potential': 'Central Forces, Kepler Orbits & Effective Potential',
    'Collisions, Momentum Conservation & Variable Mass': 'Collisions, Momentum Conservation & Variable Mass',
    'Conductors, Cavities & Electrostatic Shielding': 'Conductors, Cavities & Electrostatic Shielding',
    'Continuous Charge Distributions & Electric Potentials': 'Continuous Charge Distributions & Electric Potentials',
    'DC Circuits, Resistors & Joule Heating': 'DC Circuits, Resistors & Joule Heating',
    'Dirac Formalism, State Vectors & Hilbert Space': 'Dirac Formalism, State Vectors & Hilbert Space',
    "EM Wave Polarization & Malus's Law": "EM Wave Polarization & Malus's Law",
    'Entropy Changes & Reversibility': 'Entropy Changes & Reversibility',
    "Faraday's Law, Motional EMF & Inductance": "Faraday's Law, Motional EMF & Inductance",
    'Grand Canonical Ensemble & Chemical Potential': 'Grand Canonical Ensemble & Chemical Potential',
    'Hamiltonian Mechanics & Phase Space Dynamics': 'Hamiltonian Mechanics & Phase Space Dynamics',
    'Harmonic Oscillator & Ladder Operators': 'Harmonic Oscillator & Ladder Operators',
    'Hydrogen Atom & Central Potentials': 'Hydrogen Atom & Central Potentials',
    'Ideal & Real Gases (Equation of State)': 'Ideal & Real Gases (Equation of State)',
    'Identical Particles, Bosons/Fermions & Symmetry': 'Identical Particles, Bosons/Fermions & Symmetry',
    'Lagrangian Mechanics & Generalized Coordinates': 'Lagrangian Mechanics & Generalized Coordinates',
    'Lorentz Force & Particle Trajectories in EM Fields': 'Lorentz Force & Particle Trajectories in EM Fields',
    'Magnetic Dipoles, Forces & Magnetic Media': 'Magnetic Dipoles, Forces & Magnetic Media',
    'Matter Waves & de Broglie Hypothesis': 'Matter Waves & de Broglie Hypothesis',
    'Maxwell Equations & Displacement Current': 'Maxwell Equations & Displacement Current',
    'Newtonian Dynamics & Non-Inertial Frames': 'Newtonian Dynamics & Non-Inertial Frames',
    'Nuclear Physics & Radioactive Decay': 'Nuclear Physics & Radioactive Decay',
    'Perturbation Theory & Approximation Methods': 'Perturbation Theory & Approximation Methods',
    'Phase Transitions & Clausius-Clapeyron': 'Phase Transitions & Clausius-Clapeyron',
    'Photoelectric Effect & Photon Interactions': 'Photoelectric Effect & Photon Interactions',
    'Poynting Vector & EM Wave Propagation': 'Poynting Vector & EM Wave Propagation',
    'Quantum Gases (Bose-Einstein Condensation & Blackbody)': 'Quantum Gases (Bose-Einstein Condensation & Blackbody)',
    'Quantum Gases (Fermi-Dirac & Degeneracy)': 'Quantum Gases (Fermi-Dirac & Degeneracy)',
    'Relativistic Dynamics & Energy-Momentum': 'Relativistic Dynamics & Energy-Momentum',
    'Rigid Body Dynamics & Moments of Inertia': 'Rigid Body Dynamics & Moments of Inertia',
    'Small Oscillations, Coupled Systems & Normal Modes': 'Small Oscillations, Coupled Systems & Normal Modes',
    'Special Relativity & Lorentz Transformations': 'Special Relativity & Lorentz Transformations',
    'Spin Systems, Paramagnetism & Ising Model': 'Spin Systems, Paramagnetism & Ising Model',
    'Thermodynamic Potentials & Maxwell Relations': 'Thermodynamic Potentials & Maxwell Relations',
    'Two-Level Systems & Paramagnetic Entropy': 'Two-Level Systems & Paramagnetic Entropy',
    'Vector Calculus & Field Operators': 'Vector Calculus & Field Operators',
    'Work-Energy Theorem & 1D Potential Dynamics': 'Work-Energy Theorem & 1D Potential Dynamics'
  }
};
