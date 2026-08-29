<script lang="ts">
  import type { BankData, Question } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import { renderMathInString } from '../math';
  import confetti from 'canvas-confetti';
  import { 
    Clock, Award, CheckCircle2, Bookmark, AlertCircle,
    Play, Pause, RotateCcw, ArrowRight, ArrowLeft,
    Check, X, FileText, Send, Sparkles, Split, ChevronRight,
    ArrowUpRight, Gauge, Shuffle
  } from 'lucide-svelte';

  let {
    bankData,
    onJumpToQuestion
  }: {
    bankData: BankData | null;
    onJumpToQuestion?: (q: Question) => void;
  } = $props();

  // Mock Exam States: 'setup' | 'running' | 'completed'
  let examState = $state<'setup' | 'running' | 'completed'>('setup');
  let selectedMode = $state<string>('random_40');
  let shuffleOptions = $state<boolean>(false);
  let examQuestions = $state<Question[]>([]);
  let currentIdx = $state<number>(0);

  // User Answers: qid -> 'A' | 'B' | 'C' | 'D' | 'E'
  let userAnswers = $state<Record<string, string>>({});
  let flaggedQuestions = $state<Record<string, boolean>>({});
  let questionTimeSpent = $state<Record<string, number>>({}); // qid -> seconds spent

  // 4-Hour Timer (4 * 3600 seconds)
  let timerSeconds = $state(4 * 3600);
  let isTimerPaused = $state(false);
  let timerInterval: any = null;

  // Dialogs
  let isConfirmModalOpen = $state(false);
  let isCancelModalOpen = $state(false);

  // Canonical EUF Subject Area Order
  const AREA_PRIORITY: Record<string, number> = {
    'Mecânica Clássica': 1,
    'Eletromagnetismo': 2,
    'Termodinâmica': 3,
    'Física Estatística': 4,
    'Física Moderna': 5,
    'Mecânica Quântica': 6,
  };

  function sortQuestionsInOfficialOrder(qs: Question[]): Question[] {
    return [...qs].sort((a, b) => {
      const pA = AREA_PRIORITY[a.area] || 99;
      const pB = AREA_PRIORITY[b.area] || 99;
      if (pA !== pB) return pA - pB;
      return (a.question_num || 0) - (b.question_num || 0);
    });
  }

  // Current Question
  const currentQuestion = $derived(
    examQuestions.length > 0 && currentIdx < examQuestions.length 
      ? examQuestions[currentIdx] 
      : null
  );

  const answeredCount = $derived(
    Object.keys(userAnswers).filter(k => userAnswers[k]).length
  );

  const totalElapsedSeconds = $derived(
    (4 * 3600) - timerSeconds
  );

  const avgSecondsPerAnswered = $derived(
    answeredCount > 0 ? Math.round(totalElapsedSeconds / answeredCount) : 0
  );

  function startExam() {
    if (!bankData || !bankData.questions || bankData.questions.length === 0) return;

    let pool: Question[] = [];

    if (selectedMode === 'random_40') {
      const areaQuotas: [string, number][] = [
        ['Mecânica Clássica', 8],
        ['Eletromagnetismo', 8],
        ['Termodinâmica', 4],
        ['Física Estatística', 4],
        ['Física Moderna', 8],
        ['Mecânica Quântica', 8]
      ];

      for (const [area, quota] of areaQuotas) {
        const areaQs = bankData.questions
          .filter(q => q.area === area && q.question_type === 'múltipla escolha')
          .sort(() => Math.random() - 0.5)
          .slice(0, quota);
        pool.push(...areaQs);
      }

      if (pool.length < 40) {
        const remaining = bankData.questions
          .filter(q => !pool.some(p => p.id === q.id) && q.question_type === 'múltipla escolha')
          .sort(() => Math.random() - 0.5)
          .slice(0, 40 - pool.length);
        pool.push(...remaining);
      }
    } else {
      const examQs = bankData.questions
        .filter(q => q.exam_id === selectedMode && q.tag.endsWith('a'))
        .slice(0, 40);
      
      if (examQs.length > 0) {
        pool = examQs;
      } else {
        pool = bankData.questions.filter(q => q.exam_id === selectedMode).slice(0, 40);
      }
    }

    examQuestions = sortQuestionsInOfficialOrder(pool);
    userAnswers = {};
    flaggedQuestions = {};
    questionTimeSpent = {};
    currentIdx = 0;
    timerSeconds = 4 * 3600;
    isTimerPaused = false;
    examState = 'running';

    clearInterval(timerInterval);
    timerInterval = setInterval(() => {
      if (!isTimerPaused) {
        if (timerSeconds > 0) {
          timerSeconds--;
          if (currentQuestion) {
            questionTimeSpent[currentQuestion.id] = (questionTimeSpent[currentQuestion.id] || 0) + 1;
          }
        } else {
          submitExam();
        }
      }
    }, 1000);
  }

  function selectAnswer(letter: string) {
    if (!currentQuestion) return;
    if (userAnswers[currentQuestion.id] === letter) {
      delete userAnswers[currentQuestion.id];
    } else {
      userAnswers[currentQuestion.id] = letter;
    }
  }

  function toggleFlag() {
    if (!currentQuestion) return;
    flaggedQuestions[currentQuestion.id] = !flaggedQuestions[currentQuestion.id];
  }

  function submitExam() {
    clearInterval(timerInterval);
    examState = 'completed';
    isConfirmModalOpen = false;

    // Record study progress for answered questions
    for (const q of examQuestions) {
      if (userAnswers[q.id]) {
        profileStore.updateQuestionStatus(q.id, 'solved');
      }
    }

    confetti({
      particleCount: 80,
      spread: 70,
      origin: { y: 0.5 }
    });
  }

  function cancelExam() {
    clearInterval(timerInterval);
    isCancelModalOpen = false;
    userAnswers = {};
    flaggedQuestions = {};
    questionTimeSpent = {};
    examQuestions = [];
    examState = 'setup';
  }

  function formatTime(secs: number): string {
    const h = Math.floor(secs / 3600);
    const m = Math.floor((secs % 3600) / 60);
    const s = secs % 60;
    return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  function formatDurationMinutes(secs: number): string {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}m ${s}s`;
  }

  function getAreaScore(area: string) {
    const qs = examQuestions.filter(q => q.area === area);
    const answered = qs.filter(q => userAnswers[q.id]).length;
    return {
      total: qs.length,
      answered,
      pct: qs.length > 0 ? Math.round((answered / qs.length) * 100) : 0
    };
  }
</script>

<div class="flex-1 h-full flex flex-col bg-[#FDFBF7] dark:bg-[#080d16] overflow-hidden transition-colors duration-200">
  {#if examState === 'setup'}
    <!-- SETUP & CONFIGURATION SCREEN -->
    <div class="flex-1 overflow-y-auto custom-scrollbar flex items-center justify-center p-6 bg-study-grid">
      <div class="max-w-2xl w-full bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 rounded-3xl p-8 sm:p-10 shadow-lg space-y-8">
        <div class="text-center space-y-3">
          <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-sky-500 to-indigo-600 text-white flex items-center justify-center mx-auto shadow-md">
            <Clock size={30} />
          </div>
          <h1 class="text-2xl sm:text-3xl font-black font-sans text-slate-900 dark:text-white tracking-tight">
            {profileStore.t('mockExamTitle')}
          </h1>
          <p class="text-sm text-slate-500 dark:text-slate-400 font-sans max-w-md mx-auto">
            {profileStore.t('mockExamSubtitle')}
          </p>
        </div>

        <!-- Mode Selector -->
        <div class="space-y-3 font-sans">
          <label for="mock-edition-select" class="block text-xs font-bold text-slate-700 dark:text-slate-300 uppercase tracking-wider">
            Modalidad de Simulacro:
          </label>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <button
              onclick={() => selectedMode = 'random_40'}
              class="p-4 rounded-2xl border text-left transition cursor-pointer {selectedMode === 'random_40' ? 'bg-sky-50 dark:bg-sky-950/60 border-sky-500 text-sky-900 dark:text-sky-200 ring-2 ring-sky-500/20' : 'bg-[#FAF8F5] dark:bg-slate-950 border-[#E5DFD4] dark:border-slate-800 hover:border-slate-400'}"
            >
              <div class="font-bold text-sm">🎯 Simulacro Oficial Ordenado</div>
              <div class="text-xs text-slate-500 dark:text-slate-400 mt-1">40 preguntas canónicas en orden estricto (1. Mecánica, 2. Electromag, 3. Termo, 4. Estat, 5. Moderna, 6. Cuántica)</div>
            </button>

            {#if bankData && bankData.exams}
              <div class="p-3 rounded-2xl border border-[#E5DFD4] dark:border-slate-800 bg-[#FAF8F5] dark:bg-slate-950 flex flex-col justify-center">
                <label for="mock-edition-select" class="text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">
                  Examen Oficial Específico:
                </label>
                <select
                  id="mock-edition-select"
                  value={selectedMode}
                  onchange={(e) => selectedMode = (e.target as HTMLSelectElement).value}
                  class="w-full bg-white dark:bg-slate-900 border border-[#DDD6C8] dark:border-slate-700 rounded-xl p-2 text-xs font-bold focus:outline-none cursor-pointer"
                >
                  <option value="random_40">-- Seleccionar Edición --</option>
                  {#each bankData.exams as ex}
                    <option value={ex.id}>{ex.id} ({ex.exam_type === 'amc_multiple_choice' ? 'Múltipla Escolha' : 'Discursiva'})</option>
                  {/each}
                </select>
              </div>
            {/if}
          </div>
        </div>

        <!-- Rules and Target Pace info -->
        <div class="p-5 rounded-2xl bg-[#FAF8F5] dark:bg-slate-950 border border-[#E5DFD4] dark:border-slate-800 text-xs text-slate-600 dark:text-slate-400 font-sans space-y-2.5">
          <div class="font-bold text-slate-800 dark:text-slate-200 uppercase tracking-wider text-[11px] flex items-center gap-1.5">
            <Gauge size={14} class="text-sky-500" />
            <span>Condiciones Oficiales de Entrenamiento:</span>
          </div>
          <ul class="space-y-1.5 list-disc list-inside">
            <li><strong>Tiempo Total:</strong> 4 Horas (240 minutos cronometrados).</li>
            <li><strong>Ritmo Objetivo:</strong> 3.0 minutos por pregunta para 80 preguntas (o 6.0 min para 40).</li>
            <li><strong>Orden Canónico:</strong> Mecânica Clássica → Eletromagnetismo → Termodinâmica → Física Estatística → Física Moderna → Mecânica Quântica.</li>
            <li><strong>Hoja de Respuestas:</strong> Marcado directo de alternativas (A, B, C, D, E) y marcadores para revisión.</li>
          </ul>
        </div>

        <button
          onclick={startExam}
          class="w-full py-4 rounded-2xl bg-gradient-to-r from-sky-600 to-indigo-600 hover:from-sky-500 hover:to-indigo-500 text-white font-sans font-bold text-base shadow-md hover:shadow-lg transition cursor-pointer flex items-center justify-center gap-2"
        >
          <Play size={18} />
          <span>{profileStore.t('startMockExam')}</span>
        </button>
      </div>
    </div>

  {:else if examState === 'running'}
    <!-- RUNNING EXAM COCKPIT -->
    <!-- Top Control Bar -->
    <div class="px-6 py-3 bg-white dark:bg-[#0c121e] border-b border-[#E8E2D8] dark:border-white/10 flex items-center justify-between gap-4 shrink-0 shadow-2xs font-sans">
      <div class="flex items-center space-x-3">
        <span class="px-2.5 py-1 rounded-lg text-xs font-bold bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200">
          Q {currentIdx + 1} / {examQuestions.length}
        </span>
        {#if currentQuestion}
          {@const th = AREA_THEMES[currentQuestion.area]}
          <span class="px-2.5 py-1 rounded-lg text-xs font-bold border {th?.badgeClass || 'bg-slate-100 text-slate-800'}">
            {profileStore.tArea(currentQuestion.area)}
          </span>
        {/if}
      </div>

      <!-- Real-time Timer & Pace Gauge -->
      <div class="flex items-center space-x-3">
        <!-- Live Pace Badge -->
        <div class="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-800 text-xs font-mono {avgSecondsPerAnswered <= 180 && avgSecondsPerAnswered > 0 ? 'bg-emerald-50 text-emerald-800 dark:bg-emerald-950/40 dark:text-emerald-300' : 'bg-amber-50 text-amber-800 dark:bg-amber-950/40 dark:text-amber-300'}">
          <Gauge size={13} />
          <span>Ritmo: {avgSecondsPerAnswered > 0 ? `${(avgSecondsPerAnswered / 60).toFixed(1)}m/q` : '—'}</span>
          <span class="text-[10px] text-slate-400">(Meta: 3.0m)</span>
        </div>

        <!-- 4-Hour Countdown Clock -->
        <div class="px-4 py-1.5 rounded-xl bg-slate-900 text-white font-mono font-bold text-sm tracking-wider flex items-center gap-2 shadow-xs">
          <Clock size={15} class={timerSeconds < 1800 ? 'text-rose-400 animate-pulse' : 'text-sky-400'} />
          <span>{formatTime(timerSeconds)}</span>
        </div>

        <button
          onclick={() => isTimerPaused = !isTimerPaused}
          class="p-2 rounded-xl border border-[#DDD6C8] dark:border-slate-700 bg-[#FAF8F5] dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-[#F2ECE0] transition cursor-pointer"
          title={isTimerPaused ? 'Reanudar' : 'Pausar'}
        >
          {#if isTimerPaused}<Play size={15} />{:else}<Pause size={15} />{/if}
        </button>

        <button
          onclick={() => isConfirmModalOpen = true}
          class="px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-xs transition cursor-pointer flex items-center gap-1.5"
        >
          <Send size={14} />
          <span>{profileStore.t('submitExam')}</span>
        </button>

        <button
          onclick={() => isCancelModalOpen = true}
          class="px-3 py-1.5 rounded-xl border border-rose-200 dark:border-rose-900 bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 font-bold text-xs hover:bg-rose-100 transition cursor-pointer"
        >
          {profileStore.t('cancelExam')}
        </button>
      </div>
    </div>

    <!-- Main Viewport: Question Card & Bubble Sheet -->
    <div class="flex-1 grid grid-cols-1 lg:grid-cols-12 overflow-hidden">
      <!-- Question Presentation Canvas (Cols 1-8) -->
      <div class="lg:col-span-8 h-full overflow-y-auto custom-scrollbar p-6 space-y-5">
        {#if currentQuestion}
          <div class="bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 rounded-3xl p-6 sm:p-8 shadow-sm space-y-6">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono font-bold text-slate-400">
                {currentQuestion.id} • {currentQuestion.tag}
              </span>
              <button
                onclick={toggleFlag}
                class="px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 transition cursor-pointer {flaggedQuestions[currentQuestion.id] ? 'bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 border border-amber-300' : 'bg-slate-100 dark:bg-slate-800 text-slate-500 hover:text-slate-800'}"
              >
                <Bookmark size={14} />
                <span>{flaggedQuestions[currentQuestion.id] ? profileStore.t('flaggedForReview') : profileStore.t('flagForReview')}</span>
              </button>
            </div>

            <!-- Problem Graphic Image or Cropped Scan -->
            <div class="rounded-2xl bg-[#FAF8F5] dark:bg-slate-950 border border-[#E5DFD4] dark:border-slate-800 p-4 text-center select-none">
              <img
                src={currentQuestion.image}
                alt={currentQuestion.id}
                class="max-h-[460px] mx-auto object-contain w-full"
                loading="eager"
              />
            </div>
          </div>
        {/if}
      </div>

      <!-- Bubble Sheet & Navigation Grid (Cols 9-12) -->
      <div class="lg:col-span-4 h-full bg-white dark:bg-[#0c121e] border-l border-[#E8E2D8] dark:border-white/10 flex flex-col overflow-hidden">
        <div class="p-4 border-b border-[#E8E2D8] dark:border-white/10 space-y-3 font-sans">
          <div class="flex items-center justify-between text-xs font-bold text-slate-800 dark:text-slate-200">
            <span>{profileStore.t('answerSheetTitle')}</span>
            <span class="text-sky-600 dark:text-sky-400">{answeredCount} / {examQuestions.length}</span>
          </div>

          <!-- Answer Option Selector for Active Question -->
          {#if currentQuestion}
            <div class="p-3 rounded-2xl bg-[#FAF8F5] dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 space-y-2">
              <div class="text-[11px] font-bold text-slate-500 dark:text-slate-400">
                Seleccionar Alternativa (Q{currentIdx + 1}):
              </div>
              <div class="grid grid-cols-5 gap-2">
                {#each ['A', 'B', 'C', 'D', 'E'] as opt}
                  {@const isSelected = userAnswers[currentQuestion.id] === opt}
                  <button
                    onclick={() => selectAnswer(opt)}
                    class="py-3 rounded-xl font-bold font-sans text-sm transition cursor-pointer {isSelected ? 'bg-sky-600 text-white shadow-md scale-105' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-sky-400'}"
                  >
                    {opt}
                  </button>
                {/each}
              </div>
            </div>
          {/if}

          <!-- Prev / Next Navigation -->
          <div class="flex items-center space-x-2">
            <button
              onclick={() => currentIdx = Math.max(0, currentIdx - 1)}
              disabled={currentIdx === 0}
              class="flex-1 py-2 rounded-xl border border-[#DDD6C8] dark:border-slate-700 text-xs font-bold flex items-center justify-center gap-1 transition cursor-pointer disabled:opacity-30"
            >
              <ArrowLeft size={14} /> <span>Anterior</span>
            </button>
            <button
              onclick={() => currentIdx = Math.min(examQuestions.length - 1, currentIdx + 1)}
              disabled={currentIdx === examQuestions.length - 1}
              class="flex-1 py-2 rounded-xl border border-[#DDD6C8] dark:border-slate-700 text-xs font-bold flex items-center justify-center gap-1 transition cursor-pointer disabled:opacity-30"
            >
              <span>Siguiente</span> <ArrowRight size={14} />
            </button>
          </div>
        </div>

        <!-- 40-Question Bubble Matrix -->
        <div class="flex-1 overflow-y-auto custom-scrollbar p-4 grid grid-cols-4 gap-2 font-sans text-xs">
          {#each examQuestions as q, idx}
            {@const ans = userAnswers[q.id]}
            {@const isFlag = flaggedQuestions[q.id]}
            {@const isCurrent = currentIdx === idx}

            <button
              onclick={() => currentIdx = idx}
              class="p-2.5 rounded-xl border text-center transition flex flex-col items-center justify-center cursor-pointer {isCurrent ? 'ring-2 ring-sky-500 shadow-xs' : ''} {ans ? 'bg-emerald-50 dark:bg-emerald-950/60 border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-200 font-bold' : 'bg-white dark:bg-slate-900 border-[#E0D8CA] dark:border-slate-800 text-slate-600 dark:text-slate-400'}"
            >
              <div class="flex items-center gap-1 text-[10px] font-mono">
                <span>Q{idx + 1}</span>
                {#if isFlag}<span class="text-amber-500">🚩</span>{/if}
              </div>
              <div class="text-xs font-sans font-extrabold mt-0.5 {ans ? 'text-emerald-700 dark:text-emerald-300' : 'text-slate-300 dark:text-slate-600'}">
                {ans || '—'}
              </div>
            </button>
          {/each}
        </div>
      </div>
    </div>

    <!-- Confirm Submit Dialog -->
    {#if isConfirmModalOpen}
      <div class="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white dark:bg-slate-900 rounded-3xl p-6 sm:p-8 max-w-md w-full border border-[#E5DFD4] dark:border-slate-800 shadow-2xl space-y-6 font-sans">
          <div class="text-center space-y-2">
            <div class="w-12 h-12 rounded-2xl bg-emerald-50 dark:bg-emerald-950/80 text-emerald-600 dark:text-emerald-300 flex items-center justify-center mx-auto">
              <Send size={22} />
            </div>
            <h3 class="text-lg font-bold text-slate-900 dark:text-white">
              {profileStore.t('confirmSubmitTitle')}
            </h3>
            <p class="text-xs text-slate-500 dark:text-slate-400">
              Has respondido <strong>{answeredCount}</strong> de <strong>{examQuestions.length}</strong> preguntas.
            </p>
          </div>

          <div class="flex items-center space-x-3">
            <button
              onclick={() => isConfirmModalOpen = false}
              class="flex-1 py-3 rounded-xl border border-[#DDD6C8] dark:border-slate-700 font-bold text-xs text-slate-700 dark:text-slate-300 hover:bg-[#FAF8F5] cursor-pointer"
            >
              Seguir Practicando
            </button>
            <button
              onclick={submitExam}
              class="flex-1 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-xs cursor-pointer"
            >
              Entregar Definitivo
            </button>
          </div>
        </div>
      </div>
    {/if}

    <!-- Confirm Cancel Dialog -->
    {#if isCancelModalOpen}
      <div class="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-xs flex items-center justify-center p-4">
        <div class="bg-white dark:bg-slate-900 rounded-3xl p-6 sm:p-8 max-w-md w-full border border-[#E5DFD4] dark:border-slate-800 shadow-2xl space-y-6 font-sans">
          <div class="text-center space-y-2">
            <div class="w-12 h-12 rounded-2xl bg-rose-50 dark:bg-rose-950/80 text-rose-600 dark:text-rose-400 flex items-center justify-center mx-auto">
              <AlertCircle size={24} />
            </div>
            <h3 class="text-lg font-bold text-slate-900 dark:text-white">
              {profileStore.t('confirmCancelTitle')}
            </h3>
            <p class="text-xs text-slate-500 dark:text-slate-400">
              {profileStore.t('confirmCancelBody')}
            </p>
          </div>

          <div class="flex items-center space-x-3">
            <button
              onclick={() => isCancelModalOpen = false}
              class="flex-1 py-3 rounded-xl border border-[#DDD6C8] dark:border-slate-700 font-bold text-xs text-slate-700 dark:text-slate-300 hover:bg-[#FAF8F5] cursor-pointer"
            >
              {profileStore.t('continueExam')}
            </button>
            <button
              onclick={cancelExam}
              class="flex-1 py-3 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs shadow-xs cursor-pointer"
            >
              {profileStore.t('discardAndExit')}
            </button>
          </div>
        </div>
      </div>
    {/if}

  {:else if examState === 'completed'}
    <!-- DIAGNOSTIC & ADVANCED PACE SCORE REPORT -->
    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 sm:p-10 flex items-center justify-center bg-study-grid">
      <div class="max-w-3xl w-full bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 rounded-3xl p-8 sm:p-10 shadow-lg space-y-8">
        <div class="text-center space-y-3">
          <div class="w-16 h-16 rounded-2xl bg-emerald-500 text-white flex items-center justify-center mx-auto shadow-md">
            <Award size={32} />
          </div>
          <h1 class="text-2xl sm:text-3xl font-black font-sans text-slate-900 dark:text-white">
            {profileStore.t('mockExamCompleted')}
          </h1>
          <p class="text-sm text-slate-500 dark:text-slate-400 font-sans">
            Completaste el simulacro en <strong>{formatTime(totalElapsedSeconds)}</strong>.
          </p>
        </div>

        <!-- Score & Pace Metrics Banner -->
        <div class="p-6 rounded-2xl bg-gradient-to-r from-sky-50 to-indigo-50 dark:from-slate-950 dark:to-slate-900 border border-sky-200 dark:border-slate-800 grid grid-cols-3 gap-4 text-center">
          <div>
            <div class="text-xs font-sans font-bold text-slate-500 dark:text-slate-400 uppercase">Respondidas</div>
            <div class="text-2xl font-black text-slate-900 dark:text-white mt-1">{answeredCount} / {examQuestions.length}</div>
          </div>
          <div class="border-x border-slate-200 dark:border-slate-800 px-2">
            <div class="text-xs font-sans font-bold text-slate-500 dark:text-slate-400 uppercase">Cobertura</div>
            <div class="text-2xl font-black text-sky-600 dark:text-sky-400 mt-1">
              {Math.round((answeredCount / examQuestions.length) * 100)}%
            </div>
          </div>
          <div>
            <div class="text-xs font-sans font-bold text-slate-500 dark:text-slate-400 uppercase">Ritmo Medio</div>
            <div class="text-2xl font-black {avgSecondsPerAnswered <= 180 ? 'text-emerald-600 dark:text-emerald-400' : 'text-amber-600 dark:text-amber-400'} mt-1">
              {(avgSecondsPerAnswered / 60).toFixed(1)} <span class="text-xs font-normal">min/preg</span>
            </div>
          </div>
        </div>

        <!-- Performance Breakdown by Subject Area in Strict Canonical Order -->
        <div class="space-y-3 font-sans">
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">
            {profileStore.t('performanceByArea')}:
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {#each ['Mecânica Clássica', 'Eletromagnetismo', 'Termodinâmica', 'Física Estatística', 'Física Moderna', 'Mecânica Quântica'] as area}
              {@const stats = getAreaScore(area)}
              {#if stats.total > 0}
                <div class="p-4 rounded-xl border border-[#E5DFD4] dark:border-slate-800 bg-[#FAF8F5] dark:bg-slate-950 space-y-2">
                  <div class="flex items-center justify-between text-xs font-bold">
                    <span>{profileStore.tArea(area)}</span>
                    <span class="font-mono">{stats.answered}/{stats.total} ({stats.pct}%)</span>
                  </div>
                  <div class="w-full bg-[#E0D8CA] dark:bg-slate-800 rounded-full h-2 overflow-hidden">
                    <div class="bg-sky-500 h-full rounded-full transition-all duration-300" style="width: {stats.pct}%"></div>
                  </div>
                </div>
              {/if}
            {/each}
          </div>
        </div>

        <!-- Questions Review Drawer with 1-Click Jump to Study Canvas -->
        <div class="space-y-3 font-sans pt-2 border-t border-[#E8E2D8] dark:border-slate-800">
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 flex items-center justify-between">
            <span>Revisión Detallada de Preguntas:</span>
            <span class="text-[11px] font-normal text-slate-400">Toca para estudiar en Canvas</span>
          </h3>

          <div class="max-h-60 overflow-y-auto custom-scrollbar space-y-1.5">
            {#each examQuestions as q, idx}
              {@const ans = userAnswers[q.id]}
              {@const time = questionTimeSpent[q.id] || 0}
              <div class="p-2.5 rounded-xl bg-[#FAF8F5] dark:bg-slate-950 border border-[#E5DFD4] dark:border-slate-800 flex items-center justify-between text-xs">
                <div class="flex items-center gap-2">
                  <span class="font-mono font-bold w-7 text-slate-400">Q{idx + 1}</span>
                  <span class="px-1.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 font-bold text-[10px]">{profileStore.tArea(q.area)}</span>
                  <span class="font-mono text-slate-600 dark:text-slate-300 font-bold">Resp: {ans || '—'}</span>
                </div>
                <div class="flex items-center gap-3">
                  <span class="text-[11px] text-slate-400 font-mono">{formatDurationMinutes(time)}</span>
                  {#if onJumpToQuestion}
                    <button
                      onclick={() => onJumpToQuestion?.(q)}
                      class="px-2.5 py-1 rounded-lg bg-sky-50 dark:bg-sky-950/60 border border-sky-200 dark:border-sky-800 text-sky-700 dark:text-sky-300 font-bold text-[11px] hover:bg-sky-100 flex items-center gap-1 cursor-pointer"
                    >
                      Estudiar <ArrowUpRight size={12} />
                    </button>
                  {/if}
                </div>
              </div>
            {/each}
          </div>
        </div>

        <!-- Actions -->
        <div class="flex items-center space-x-4 pt-4 border-t border-[#E8E2D8] dark:border-slate-800">
          <button
            onclick={() => examState = 'setup'}
            class="flex-1 py-3.5 rounded-2xl bg-gradient-to-r from-sky-600 to-indigo-600 text-white font-sans font-bold text-sm shadow-md transition cursor-pointer flex items-center justify-center gap-2"
          >
            <RotateCcw size={16} />
            <span>{profileStore.t('retakeExam')}</span>
          </button>
        </div>
      </div>
    </div>
  {/if}
</div>
