<script lang="ts">
  import type { Question, QuestionStatus } from '../types';
  import { profileStore, resolveImageUrl } from '../storage.svelte';
  import { AREA_THEMES, OFFICIAL_FORMULAS, HINT_LEVELS } from '../constants';
  import { mathAction, parseAndRenderQuestion } from '../math';
  import confetti from 'canvas-confetti';
  import { 
    CheckCircle2, Bookmark, XCircle, Clock, 
    ZoomIn, ZoomOut, Maximize2, Split, 
    Play, Pause, RotateCcw, AlertTriangle, FileText,
    Lightbulb, FileEdit, BookOpen, ChevronDown, ChevronUp,
    Check, Hash, Compass, Scale, Zap, Sparkles
  } from 'lucide-svelte';

  let {
    question,
    onJumpToTwin,
    onSelectNext,
    onSelectPrev
  }: {
    question: Question | null;
    onJumpToTwin?: (twinId: string) => void;
    onSelectNext?: () => void;
    onSelectPrev?: () => void;
  } = $props();

  let isZoomModalOpen = $state(false);
  let isImageExpanded = $state(false);
  let openClues = $state<Record<number, boolean>>({ 1: true, 2: false, 3: false, 4: false });
  let userNotes = $state<string>('');
  let isSavedNotice = $state<boolean>(false);
  let showTranscription = $state<boolean>(false);
  let activeRightTab = $state<'hints' | 'notes' | 'formulas'>('hints');

  // Mobile Touch Swipe Handling
  let touchStartX = $state(0);
  let touchStartY = $state(0);

  function handleTouchStart(e: TouchEvent) {
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
  }

  function handleTouchEnd(e: TouchEvent) {
    const deltaX = e.changedTouches[0].clientX - touchStartX;
    const deltaY = e.changedTouches[0].clientY - touchStartY;
    if (Math.abs(deltaX) > 60 && Math.abs(deltaX) > Math.abs(deltaY) * 1.4) {
      if (deltaX < 0 && onSelectNext) {
        onSelectNext();
      } else if (deltaX > 0 && onSelectPrev) {
        onSelectPrev();
      }
    }
  }

  // Mobile Bottom Drawer State
  let isMobileDrawerOpen = $state<boolean>(false);

  // 15-Minute Countdown Timer
  let timerSeconds = $state(15 * 60);
  let isTimerRunning = $state(false);
  let timerInterval: any = null;

  // Sync state when question changes
  $effect(() => {
    if (question) {
      const uState = profileStore.getQuestionState(question.id);
      userNotes = uState.notes || '';
      openClues = { 1: true, 2: false, 3: false, 4: false };
    }
  });

  function toggleTimer() {
    if (isTimerRunning) {
      clearInterval(timerInterval);
      isTimerRunning = false;
    } else {
      isTimerRunning = true;
      timerInterval = setInterval(() => {
        if (timerSeconds > 0) {
          timerSeconds--;
        } else {
          clearInterval(timerInterval);
          isTimerRunning = false;
          alert(profileStore.t('timerLimitReached'));
        }
      }, 1000);
    }
  }

  function resetTimer() {
    clearInterval(timerInterval);
    isTimerRunning = false;
    timerSeconds = 15 * 60;
  }

  function formatTime(secs: number): string {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  function setStatus(status: QuestionStatus) {
    if (!question) return;
    profileStore.updateQuestionStatus(question.id, status);

    if (status === 'solved') {
      confetti({
        particleCount: 50,
        spread: 65,
        origin: { y: 0.6 }
      });
    }
  }

  function handleNotesInput(e: Event) {
    if (!question) return;
    const val = (e.target as HTMLTextAreaElement).value;
    userNotes = val;
    profileStore.updateQuestionNotes(question.id, val);
    isSavedNotice = true;
    setTimeout(() => { isSavedNotice = false; }, 1500);
  }

  function toggleClue(lvl: number) {
    openClues[lvl] = !openClues[lvl];
  }

  export function toggleClueByLevel(lvl: number) {
    toggleClue(lvl);
  }

  export function triggerZoom() {
    isZoomModalOpen = !isZoomModalOpen;
  }

  const uState = $derived(
    question ? profileStore.getQuestionState(question.id) : null
  );

  const theme = $derived(
    question ? AREA_THEMES[question.area] : null
  );

  const areaFormulas = $derived(() => {
    if (!question) return [];
    const cat = OFFICIAL_FORMULAS.find(c => c.category === question.area || c.category.includes(question.area.split(' ')[0]));
    return cat ? cat.formulas : OFFICIAL_FORMULAS[0].formulas;
  });

  const physicalConstants = [
    { symbol: 'c', val: '2.998 \\times 10^8\\text{ m/s}', label: 'Velocidade da luz' },
    { symbol: '\\hbar', val: '1.055 \\times 10^{-34}\\text{ J}\\cdot\\text{s}', label: 'Constante de Planck' },
    { symbol: '\\varepsilon_0', val: '8.854 \\times 10^{-12}\\text{ F/m}', label: 'Permissividade do vácuo' },
    { symbol: '\\mu_0', val: '4\\pi \\times 10^{-7}\\text{ N/A}^2', label: 'Permeabilidade do vácuo' },
    { symbol: 'k_B', val: '1.381 \\times 10^{-23}\\text{ J/K}', label: 'Constante de Boltzmann' },
    { symbol: 'e', val: '1.602 \\times 10^{-19}\\text{ C}', label: 'Carga elementar' },
  ];

  const activeClues = $derived.by(() => {
    if (!question || !question.clues) return null;
    const c = question.clues as any;
    if (c[profileStore.lang]) {
      return c[profileStore.lang];
    }
    return c;
  });

  function cleanTextForDisplay(raw: string): string {
    if (!raw) return '';
    return raw
      .replace(/\x00/g, '')
      .replace(/\ufffd/g, '')
      .replace(/[\x01-\x08\x0b\x0c\x0e-\x1f]/g, ' ')
      .replace(/[ \t]+/g, ' ')
      .trim();
  }
  // Helper for clue level icon component
  function getHintIcon(name: string) {
    if (name === 'Lightbulb') return Lightbulb;
    if (name === 'Compass') return Compass;
    if (name === 'Scale') return Scale;
    return Zap;
  }
</script>

{#if !question}
  <div class="flex-1 h-full flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 font-sans text-xs p-8 bg-study-grid transition-colors">
    <div class="w-12 h-12 rounded-2xl bg-white dark:bg-slate-800 border border-[#E5DFD4] dark:border-slate-700 shadow-xs flex items-center justify-center text-slate-500 dark:text-slate-300 mb-3 text-lg font-serif">
      Ψ
    </div>
    <span>{profileStore.t('selectQuestionPrompt')}</span>
  </div>
{:else}
  <div 
    class="flex-1 h-full flex flex-col bg-[#FDFBF7] dark:bg-[#080d16] overflow-hidden transition-colors duration-200"
    ontouchstart={handleTouchStart}
    ontouchend={handleTouchEnd}
  >
    <!-- Top Header: Strict Visual Hierarchy (1. What question -> 2. Progress/Timer -> 3. Actions) -->
    <div class="px-6 py-3 bg-white dark:bg-[#0c121e] border-b border-[#E8E2D8] dark:border-white/10 flex flex-wrap items-center justify-between gap-4 shrink-0 shadow-2xs">
      <!-- (1) PRIMARY HERO ANCHOR: Question Identity & Subtopic -->
      <div class="flex items-center space-x-3 min-w-0">
        <span class="px-2.5 py-1 rounded-lg text-xs font-sans font-bold border {theme?.badgeClass || 'bg-slate-100 text-slate-800'}">
          {profileStore.tArea(question.area)}
        </span>

        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-slate-950 dark:text-white font-sans font-black text-lg sm:text-xl tracking-tight">
              {question.id}
            </h1>
            <span class="text-xs font-sans text-slate-400 dark:text-slate-500 font-medium">
              • Pág {question.page}
            </span>
          </div>
          <div class="text-xs font-sans font-semibold text-slate-600 dark:text-slate-400 truncate mt-0.5">
            {profileStore.tSubtopic(question.subtopic)}
          </div>
        </div>

        {#if question.flag || question.errata}
          <span class="hidden md:inline-flex px-2.5 py-0.5 rounded-full bg-amber-50 dark:bg-amber-950 text-amber-800 dark:text-amber-300 border border-amber-200 dark:border-amber-700 text-xs font-semibold items-center gap-1">
            <AlertTriangle size={13} />
            {question.flag || question.errata}
          </span>
        {/if}
      </div>

      <!-- (2 & 3) SECONDARY CONTEXT & ACTIONS: Timer + Status Pills -->
      <div class="flex items-center space-x-3">
        <!-- Timer Widget -->
        <div class="flex items-center space-x-2 bg-[#FAF8F5] dark:bg-slate-900 border border-[#DDD6C8] dark:border-slate-700 px-3 py-1.5 rounded-xl shadow-2xs">
          <span class="text-[10px] font-sans uppercase text-slate-500 dark:text-slate-400 font-bold">⏱️ {profileStore.t('timerLabel')}:</span>
          <span class="font-mono font-bold text-xs {timerSeconds < 180 ? 'text-rose-600 dark:text-rose-400 animate-pulse' : 'text-slate-800 dark:text-sky-300'} w-11 text-center">
            {formatTime(timerSeconds)}
          </span>
          <button
            onclick={toggleTimer}
            class="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white p-0.5 rounded transition cursor-pointer"
            title={isTimerRunning ? 'Pausar' : 'Iniciar'}
          >
            {#if isTimerRunning}<Pause size={13} />{:else}<Play size={13} />{/if}
          </button>
          <button
            onclick={resetTimer}
            class="text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 p-0.5 rounded transition cursor-pointer"
            title="Reiniciar (15 min)"
          >
            <RotateCcw size={12} />
          </button>
        </div>

        <!-- Semantic Status Actions (Subtle Pastel Tints) -->
        <div class="flex items-center space-x-1.5 font-sans text-xs">
          <!-- Dominada (S) -->
          <button
            onclick={() => setStatus('solved')}
            class="px-3 py-1.5 rounded-xl font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'solved' ? 'bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 border-emerald-300 dark:border-emerald-700 shadow-xs' : 'bg-white dark:bg-slate-900 hover:bg-emerald-50 dark:hover:bg-emerald-950/40 text-slate-700 dark:text-slate-300 border-[#DDD6C8] dark:border-slate-700'}"
            title={`${profileStore.t('scSolved')} (S)`}
          >
            <CheckCircle2 size={15} class="text-emerald-600 dark:text-emerald-400" />
            <span>{profileStore.t('statusMastered')}</span>
            <span class="key-cap text-[8px]">S</span>
          </button>

          <!-- Revisar (R) -->
          <button
            onclick={() => setStatus('review')}
            class="px-3 py-1.5 rounded-xl font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'review' ? 'bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 border-amber-300 dark:border-amber-700 shadow-xs' : 'bg-white dark:bg-slate-900 hover:bg-amber-50 dark:hover:bg-amber-950/40 text-slate-700 dark:text-slate-300 border-[#DDD6C8] dark:border-slate-700'}"
            title={`${profileStore.t('scReview')} (R)`}
          >
            <Bookmark size={15} class="text-amber-600 dark:text-amber-400" />
            <span>{profileStore.t('statusReview')}</span>
            <span class="key-cap text-[8px]">R</span>
          </button>

          <!-- Erro (X) -->
          <button
            onclick={() => setStatus('failed')}
            class="px-3 py-1.5 rounded-xl font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'failed' ? 'bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300 border-rose-300 dark:border-rose-700 shadow-xs' : 'bg-white dark:bg-slate-900 hover:bg-rose-50 dark:hover:bg-rose-950/40 text-slate-700 dark:text-slate-300 border-[#DDD6C8] dark:border-slate-700'}"
            title={`${profileStore.t('scFailed')} (X)`}
          >
            <XCircle size={15} class="text-rose-600 dark:text-rose-400" />
            <span>{profileStore.t('statusFailed')}</span>
            <span class="key-cap text-[8px]">X</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Main Dual-Column Study Suite -->
    <div class="flex-1 grid grid-cols-1 lg:grid-cols-12 overflow-hidden">
      <!-- LEFT WORKBENCH (Cols 1-7): Clean Problem Statement & Figure (High Breathing Room) -->
      <div class="lg:col-span-7 h-full flex flex-col border-r border-[#E8E2D8] dark:border-white/10 overflow-hidden bg-study-grid">
        <!-- Sub-bar utilities -->
        <div class="px-5 py-2 bg-[#FAF8F5] dark:bg-[#0b101c] border-b border-[#E8E2D8] dark:border-white/10 flex items-center justify-between text-xs font-sans shrink-0">
          <div class="flex items-center space-x-2 text-slate-500 dark:text-slate-400 text-xs">
            <span>{question.question_type}</span>
          </div>

          <div class="flex items-center space-x-2">
            {#if question.twin_id && onJumpToTwin}
              <button
                onclick={() => onJumpToTwin?.(question!.twin_id!)}
                class="px-2.5 py-1 rounded-lg bg-sky-50 dark:bg-sky-950/60 hover:bg-sky-100 text-sky-800 dark:text-sky-300 border border-sky-200 dark:border-sky-800 flex items-center gap-1.5 text-xs font-semibold transition cursor-pointer"
                title={`${profileStore.t('scTwin')} (T)`}
              >
                <Split size={13} />
                <span>{profileStore.t('twinVariant')} ({question.twin_id})</span>
                <span class="key-cap text-[7px]">T</span>
              </button>
            {/if}

            <button
              onclick={() => isImageExpanded = !isImageExpanded}
              class="p-1.5 rounded-lg text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-[#EAE4D8] dark:hover:bg-slate-800 transition cursor-pointer"
              title={profileStore.t('adjustSize')}
            >
              {#if isImageExpanded}<ZoomOut size={15} />{:else}<ZoomIn size={15} />{/if}
            </button>

            <button
              onclick={() => isZoomModalOpen = true}
              class="p-1.5 rounded-lg text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-[#EAE4D8] dark:hover:bg-slate-800 transition cursor-pointer"
              title={profileStore.t('fullscreen')}
            >
              <Maximize2 size={15} />
            </button>
          </div>
        </div>

        <!-- Problem Statement Canvas with Generous Padding -->
        <div class="flex-1 overflow-y-auto custom-scrollbar p-6 sm:p-8 space-y-6">
          <!-- Vector Cropped Card with Breathable Margin & Shadow -->
          <div class="bg-white dark:bg-slate-900 rounded-2xl p-6 sm:p-8 shadow-xs border border-[#E5DFD4] dark:border-slate-800 select-none">
            <img
              src={resolveImageUrl(question.image)}
              alt={`Problema ${question.id}`}
              class="w-full h-auto object-contain mx-auto transition-transform duration-200 {isImageExpanded ? 'scale-105 my-2' : ''}"
              loading="eager"
              onerror={(e) => {
                (e.currentTarget as HTMLElement).style.display = 'none';
              }}
            />
          </div>

          <!-- Mathematical Transcription Collapsible Section -->
          {#if question.text && question.text.trim().length > 10}
            <div class="rounded-2xl bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 text-slate-800 dark:text-slate-200 text-sm font-serif shadow-2xs overflow-hidden">
              <button
                onclick={() => showTranscription = !showTranscription}
                class="w-full px-5 py-3 flex items-center justify-between text-left hover:bg-slate-50 dark:hover:bg-slate-800/50 transition cursor-pointer font-sans"
              >
                <div class="flex items-center gap-2 text-xs font-bold text-slate-600 dark:text-slate-400">
                  <FileText size={14} class="text-slate-500" />
                  <span>{profileStore.t('mathTranscription')}</span>
                  <span class="text-[10px] font-normal text-slate-400">({showTranscription ? 'Ocultar' : 'Texto OCR / Busca'})</span>
                </div>
                {#if showTranscription}
                  <ChevronUp size={15} class="text-slate-400" />
                {:else}
                  <ChevronDown size={15} class="text-slate-400" />
                {/if}
              </button>
              {#if showTranscription}
                {@const parsed = parseAndRenderQuestion(question.text, profileStore.lang)}
                <div class="px-6 pb-6 pt-4 border-t border-slate-100 dark:border-[#3e4451] space-y-4">
                  <!-- Statement with KaTeX & Spanish/Portuguese Translation -->
                  <div class="leading-relaxed font-serif text-sm text-slate-700 dark:text-[#abb2bf] select-text">
                    {@html parsed.statementHtml}
                  </div>

                  <!-- Options List (Strictly non-nested) -->
                  {#if parsed.options && parsed.options.length > 0}
                    <div class="space-y-2 pt-2 border-t border-slate-100 dark:border-[#353b45]/60">
                      {#each parsed.options as opt}
                        <div class="p-3 rounded-xl bg-slate-50 dark:bg-[#21252b] border border-slate-200 dark:border-[#3e4451] flex items-start gap-3 transition hover:border-sky-400">
                          <span class="inline-flex items-center justify-center w-6 h-6 rounded-lg bg-white dark:bg-[#2c313a] text-sky-600 dark:text-[#61afef] font-sans font-black text-xs shrink-0 border border-slate-200 dark:border-[#3e4451] shadow-2xs">
                            {opt.letter}
                          </span>
                          <div class="flex-1 font-serif text-slate-800 dark:text-[#abb2bf] text-sm leading-relaxed overflow-x-auto select-text">
                            {@html opt.html}
                          </div>
                        </div>
                      {/each}
                    </div>
                  {/if}
                </div>
              {/if}
            </div>
          {/if}
        </div>
      </div>

      <!-- RIGHT COMPANION WORKBENCH (Cols 8-12): The Socratic Ladder Jewel & Notes -->
      <div class="lg:col-span-5 h-full flex flex-col bg-[#FAF8F5] dark:bg-[#0b101c] overflow-hidden">
        <!-- Companion Tab Switcher -->
        <div class="p-3 bg-white dark:bg-[#0c121e] border-b border-[#E8E2D8] dark:border-white/10 flex items-center justify-between shrink-0 shadow-2xs">
          <div class="flex items-center space-x-2">
            <!-- Hints Tab -->
            <button
              onclick={() => activeRightTab = 'hints'}
              class="px-3.5 py-1.5 rounded-xl text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeRightTab === 'hints' ? 'bg-[#FAF8F5] dark:bg-slate-800 text-slate-900 dark:text-white shadow-2xs border border-[#DDD6C8] dark:border-slate-700' : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white'}"
            >
              <Lightbulb size={14} class="text-amber-500" />
              <span>{profileStore.t('tabHints')}</span>
            </button>

            <!-- Notes Tab -->
            <button
              onclick={() => activeRightTab = 'notes'}
              class="px-3.5 py-1.5 rounded-xl text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeRightTab === 'notes' ? 'bg-[#FAF8F5] dark:bg-slate-800 text-slate-900 dark:text-white shadow-2xs border border-[#DDD6C8] dark:border-slate-700' : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white'}"
            >
              <FileEdit size={14} />
              <span>{profileStore.t('tabNotes')}</span>
            </button>

            <!-- Formulas Tab -->
            <button
              onclick={() => activeRightTab = 'formulas'}
              class="px-3.5 py-1.5 rounded-xl text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeRightTab === 'formulas' ? 'bg-[#FAF8F5] dark:bg-slate-800 text-slate-900 dark:text-white shadow-2xs border border-[#DDD6C8] dark:border-slate-700' : 'text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white'}"
            >
              <BookOpen size={14} />
              <span>{profileStore.t('tabFormulas')}</span>
            </button>
          </div>
        </div>

        <!-- Companion Content Panel (Scrollable) -->
        <div class="flex-1 overflow-y-auto custom-scrollbar p-5 space-y-4 font-sans text-xs">
          <!-- TAB 1: SOCRATIC HINTS LADDER (THE PRODUCT JEWEL) -->
          {#if activeRightTab === 'hints'}
            <div class="space-y-3.5">
              <!-- Header Card -->
              <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 text-xs font-sans text-slate-700 dark:text-slate-300 shadow-2xs space-y-1">
                <div class="flex items-center justify-between">
                  <strong class="font-bold text-slate-950 dark:text-white text-sm block">{activeClues?.title || question.subtopic}</strong>
                  <span class="text-[10px] font-mono font-bold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    4 {profileStore.t('levelsCount')}
                  </span>
                </div>
                <div class="text-[11px] text-slate-500 dark:text-slate-400">{profileStore.t('hintsInstruction')}</div>
              </div>

              <!-- Socratic Ladder Steps (1-4) -->
              {#each HINT_LEVELS as hl}
                {@const IconComponent = getHintIcon(hl.iconName)}
                {@const isUnlocked = openClues[hl.level]}
                {@const clueText = activeClues ? activeClues[`level${hl.level}` as keyof typeof activeClues] : ''}

                <div class="rounded-2xl border transition-all duration-200 overflow-hidden shadow-2xs {isUnlocked ? `${hl.badgeBg} ring-1 ring-black/5 dark:ring-white/10` : 'bg-white dark:bg-slate-900 border-[#E5DFD4] dark:border-slate-800'}">
                  <button
                    onclick={() => toggleClue(hl.level)}
                    class="w-full text-left px-4 py-3 text-xs font-sans font-bold flex items-center justify-between transition cursor-pointer"
                  >
                    <div class="flex items-center space-x-3">
                      <div class="w-6 h-6 rounded-lg flex items-center justify-center {isUnlocked ? 'bg-white/80 dark:bg-white/10 shadow-2xs' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'}">
                        <IconComponent size={14} />
                      </div>
                      <span class="{isUnlocked ? 'text-slate-950 dark:text-white' : 'text-slate-700 dark:text-slate-300'}">
                        {profileStore.t(hl.titleKey as any)}
                      </span>
                    </div>

                    <div class="flex items-center space-x-2">
                      <span class="key-cap text-[8px]">{hl.level}</span>
                      {#if isUnlocked}<ChevronUp size={15} />{:else}<ChevronDown size={15} />{/if}
                    </div>
                  </button>

                  {#if isUnlocked}
                    <div class="px-5 pb-5 text-sm font-serif text-slate-800 dark:text-slate-200 leading-relaxed border-t border-black/5 dark:border-white/5 pt-3.5 bg-white/90 dark:bg-slate-900/90" use:mathAction={clueText}></div>
                  {/if}
                </div>
              {/each}
            </div>

          <!-- TAB 2: CANDIDATE SCRATCHPAD & NOTES -->
          {:else if activeRightTab === 'notes'}
            <div class="space-y-3 h-full flex flex-col">
              <div class="flex items-center justify-between text-xs font-sans font-bold text-slate-700 dark:text-slate-300">
                <span>{profileStore.t('scratchpadTitle')}</span>
                {#if isSavedNotice}
                  <span class="text-emerald-700 dark:text-emerald-400 flex items-center gap-1 text-[11px] font-medium">
                    <Check size={13} /> {profileStore.t('savedToProfile')}
                  </span>
                {/if}
              </div>

              <textarea
                value={userNotes}
                oninput={handleNotesInput}
                placeholder={profileStore.t('scratchpadPlaceholder')}
                rows="14"
                class="w-full flex-1 bg-white dark:bg-slate-900 text-slate-800 dark:text-slate-200 border border-[#DDD6C8] dark:border-slate-700 rounded-2xl p-4 text-sm font-serif focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 leading-relaxed shadow-2xs custom-scrollbar"
              ></textarea>

              <div class="p-3 rounded-xl bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 text-xs text-slate-600 dark:text-slate-400 font-sans shadow-2xs">
                {profileStore.t('scratchpadTip')}
              </div>
            </div>

          <!-- TAB 3: CONSTANTS & FORMULAS REFERENCE -->
          {:else if activeRightTab === 'formulas'}
            <div class="space-y-4">
              <!-- Physical Constants Quickcard -->
              <div class="bg-white dark:bg-slate-900 rounded-2xl p-4 border border-[#E5DFD4] dark:border-slate-800 shadow-2xs space-y-2.5">
                <div class="text-xs font-sans font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                  <Hash size={14} class="text-sky-600 dark:text-sky-400" />
                  <span>{profileStore.t('constantsTitle')}</span>
                </div>
                <div class="grid grid-cols-2 gap-2.5">
                  {#each physicalConstants as pc}
                    <div class="p-2.5 rounded-xl bg-[#FAF8F5] dark:bg-slate-800 border border-[#E8E2D8] dark:border-slate-700 text-xs">
                      <div class="text-[10px] text-slate-500 dark:text-slate-400 font-medium">{pc.label}:</div>
                      <div class="font-serif text-slate-950 dark:text-white font-medium py-0.5" use:mathAction={`$${pc.symbol} = ${pc.val}$`}></div>
                    </div>
                  {/each}
                </div>
              </div>

              <!-- Area Formulas -->
              <div class="space-y-2.5">
                <div class="text-xs font-sans font-bold text-slate-800 dark:text-slate-200">
                  {profileStore.t('officialFormulasTitle')} {question.area}
                </div>

                {#each areaFormulas() as f}
                  <div class="p-3.5 bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 rounded-2xl shadow-2xs space-y-1">
                    <div class="text-[11px] font-sans font-bold text-slate-600 dark:text-slate-400">{f.name}:</div>
                    <div class="text-xs text-slate-900 dark:text-white overflow-x-auto py-1" use:mathAction={`$$${f.eq}$$`}></div>
                  </div>
                {/each}
              </div>
            </div>
          {/if}
        </div>
      </div>
    </div>
  </div>
{/if}

<!-- Fullscreen Zoom Modal -->
{#if isZoomModalOpen && question}
  <div
    class="fixed inset-0 z-50 bg-slate-900/60 dark:bg-black/80 backdrop-blur-xs flex items-center justify-center p-4"
    role="dialog"
    aria-modal="true"
    tabindex="-1"
    onclick={() => isZoomModalOpen = false}
    onkeydown={(e) => { if (e.key === 'Escape') isZoomModalOpen = false; }}
  >
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <div
      class="bg-white dark:bg-slate-900 rounded-3xl p-6 max-w-6xl max-h-[95vh] overflow-auto shadow-2xl relative select-none border border-[#E5DFD4] dark:border-slate-700"
      role="document"
      onclick={(e) => e.stopPropagation()}
    >
      <button
        onclick={() => isZoomModalOpen = false}
        class="absolute top-5 right-5 bg-[#FAF8F5] dark:bg-slate-800 hover:bg-[#F2ECE0] dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 rounded-xl px-3.5 py-1.5 font-sans text-xs font-bold transition z-10 border border-[#DDD6C8] dark:border-slate-700 cursor-pointer shadow-xs"
      >
        ✕ {profileStore.t('closeEsc')}
      </button>
      <img
        src={resolveImageUrl(question.image)}
        alt={`Zoom ${question.id}`}
        class="max-w-full h-auto mx-auto"
      />
    </div>
  </div>
{/if}
