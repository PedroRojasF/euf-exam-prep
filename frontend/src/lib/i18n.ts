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
  modeMap: string;
  modeFormulas: string;

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
    modeMap: "Mapa",
    modeFormulas: "Fórmulas",

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
    modeMap: "Mapa",
    modeFormulas: "Fórmulas",

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
    modeMap: "Map",
    modeFormulas: "Formulas",

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
