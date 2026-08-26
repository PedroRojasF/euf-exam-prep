<script lang="ts">
  import type { Question, QuestionStatus } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES, OFFICIAL_FORMULAS } from '../constants';
  import { mathAction } from '../math';
  import confetti from 'canvas-confetti';
  import { 
    CheckCircle2, Bookmark, XCircle, Clock, 
    ZoomIn, ZoomOut, Maximize2, Split, 
    Play, Pause, RotateCcw, AlertTriangle, FileText,
    Lightbulb, FileEdit, BookOpen, ChevronDown, ChevronUp,
    Check, Sparkles, HelpCircle, Hash
  } from 'lucide-svelte';

  let {
    question,
    onJumpToTwin
  }: {
    question: Question | null;
    onJumpToTwin?: (twinId: string) => void;
  } = $props();

  let isZoomModalOpen = $state(false);
  let isImageExpanded = $state(false);
  let selectedOption = $state<string | null>(null);
  let openClues = $state<Record<number, boolean>>({ 1: true, 2: false, 3: false, 4: false });
  let userNotes = $state<string>('');
  let isSavedNotice = $state<boolean>(false);
  let activeRightTab = $state<'hints' | 'notes' | 'formulas'>('hints');

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
      selectedOption = null;
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
          alert('⏱️ Tempo limite de 15 minutos atingido!');
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

  // Relevant physics formulas for this question's area
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
</script>

{#if !question}
  <div class="flex-1 h-full flex flex-col items-center justify-center text-slate-400 font-sans text-xs p-8 bg-study-grid">
    <div class="w-12 h-12 rounded-2xl bg-white border border-[#E5DFD4] shadow-xs flex items-center justify-center text-slate-500 mb-3 text-lg font-serif">
      Ψ
    </div>
    <span>Selecione uma questão no painel lateral para começar o estudo.</span>
  </div>
{:else}
  <div class="flex-1 h-full flex flex-col bg-[#FDFBF7] overflow-hidden">
    <!-- Top Cockpit Control Bar -->
    <div class="px-5 py-2.5 bg-white border-b border-[#E8E2D8] flex flex-wrap items-center justify-between gap-3 shrink-0 shadow-2xs">
      <!-- Question Identifiers & Path -->
      <div class="flex items-center space-x-3">
        <span class="px-2.5 py-1 rounded-lg text-xs font-sans font-bold border {theme?.badge || 'bg-slate-100 text-slate-800'}">
          {question.area}
        </span>

        <h2 class="text-slate-900 font-sans font-extrabold text-base tracking-tight">
          {question.id}
        </h2>

        <span class="text-slate-500 font-sans text-xs">
          (Pág {question.page} • {question.question_type})
        </span>

        {#if question.flag || question.errata}
          <span class="px-2 py-0.5 rounded-full bg-[#fef3c7] text-[#92400e] border border-[#fde68a] text-[11px] font-semibold flex items-center gap-1">
            <AlertTriangle size={12} />
            {question.flag || question.errata}
          </span>
        {/if}
      </div>

      <!-- Center Countdown Timer -->
      <div class="flex items-center space-x-2 bg-[#FAF8F5] border border-[#DDD6C8] px-3 py-1 rounded-xl shadow-2xs">
        <span class="text-[10px] font-sans uppercase text-slate-500 font-bold">⏱️ Tempo:</span>
        <span class="font-mono font-bold text-xs {timerSeconds < 180 ? 'text-rose-600 animate-pulse' : 'text-slate-800'} w-11 text-center">
          {formatTime(timerSeconds)}
        </span>
        <button
          onclick={toggleTimer}
          class="text-slate-500 hover:text-slate-900 p-0.5 rounded transition cursor-pointer"
          title={isTimerRunning ? 'Pausar' : 'Iniciar'}
        >
          {#if isTimerRunning}<Pause size={13} />{:else}<Play size={13} />{/if}
        </button>
        <button
          onclick={resetTimer}
          class="text-slate-400 hover:text-slate-700 p-0.5 rounded transition cursor-pointer"
          title="Reiniciar (15 min)"
        >
          <RotateCcw size={12} />
        </button>
      </div>

      <!-- Right Action Pastel Buttons -->
      <div class="flex items-center space-x-2 font-sans text-xs">
        <!-- Dominada (S) -->
        <button
          onclick={() => setStatus('solved')}
          class="px-3 py-1.5 rounded-xl font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'solved' ? 'bg-[#dcfce7] text-[#166534] border-[#86efac] shadow-xs' : 'bg-white hover:bg-[#f0fdf4] text-slate-700 border-[#DDD6C8]'}"
          title="Marcar Dominada (Atalho: S)"
        >
          <CheckCircle2 size={14} class="text-[#16a34a]" />
          <span>Dominada</span>
          <span class="key-cap text-[8px]">S</span>
        </button>

        <!-- Revisar (R) -->
        <button
          onclick={() => setStatus('review')}
          class="px-3 py-1.5 rounded-xl font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'review' ? 'bg-[#fef3c7] text-[#92400e] border-[#fde68a] shadow-xs' : 'bg-white hover:bg-[#fffbeb] text-slate-700 border-[#DDD6C8]'}"
          title="Marcar Revisão (Atalho: R)"
        >
          <Bookmark size={14} class="text-[#d97706]" />
          <span>Revisar</span>
          <span class="key-cap text-[8px]">R</span>
        </button>

        <!-- Erro (X) -->
        <button
          onclick={() => setStatus('failed')}
          class="px-3 py-1.5 rounded-xl font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'failed' ? 'bg-[#ffe4e6] text-[#9f1239] border-[#fecdd3] shadow-xs' : 'bg-white hover:bg-[#fff1f2] text-slate-700 border-[#DDD6C8]'}"
          title="Marcar Erro (Atalho: X)"
        >
          <XCircle size={14} class="text-[#e11d48]" />
          <span>Erro</span>
          <span class="key-cap text-[8px]">X</span>
        </button>
      </div>
    </div>

    <!-- Main Dual-Column Academic Workstation -->
    <div class="flex-1 grid grid-cols-1 lg:grid-cols-12 overflow-hidden">
      <!-- LEFT WORKBENCH (Cols 1-7): Problem Statement, Zoom, Interactive Option Picker -->
      <div class="lg:col-span-7 h-full flex flex-col border-r border-[#E8E2D8] overflow-hidden bg-study-grid">
        <!-- Subheader strip -->
        <div class="px-4 py-2 bg-[#FAF8F5] border-b border-[#E8E2D8] flex items-center justify-between text-xs font-sans shrink-0">
          <div class="flex items-center space-x-2 truncate">
            <span class="text-slate-400 uppercase text-[10px] font-bold">Subtópico:</span>
            <span class="text-slate-800 font-semibold truncate">{question.subtopic}</span>
          </div>

          <div class="flex items-center space-x-2">
            {#if question.twin_id && onJumpToTwin}
              <button
                onclick={() => onJumpToTwin?.(question!.twin_id!)}
                class="px-2.5 py-1 rounded-lg bg-[#eff8ff] hover:bg-[#e0f2fe] text-[#0369a1] border border-[#bae6fd] flex items-center gap-1 text-xs font-medium transition cursor-pointer"
                title="Ir para Variante Irmã (T)"
              >
                <Split size={13} />
                <span>Gêmea ({question.twin_id})</span>
                <span class="key-cap text-[7px]">T</span>
              </button>
            {/if}

            <button
              onclick={() => isImageExpanded = !isImageExpanded}
              class="p-1 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-[#EAE4D8] transition"
              title="Ajustar Tamanho"
            >
              {#if isImageExpanded}<ZoomOut size={15} />{:else}<ZoomIn size={15} />{/if}
            </button>

            <button
              onclick={() => isZoomModalOpen = true}
              class="p-1 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-[#EAE4D8] transition"
              title="Tela Cheia (Z)"
            >
              <Maximize2 size={15} />
            </button>
          </div>
        </div>

        <!-- Problem Statement Image Canvas (Full Height Scrollable) -->
        <div class="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-4">
          <!-- Vector Crop Card -->
          <div class="bg-white rounded-xl p-4 shadow-sm border border-[#E5DFD4] select-none">
            <img
              src={question.image}
              alt={`Problema ${question.id}`}
              class="w-full h-auto object-contain mx-auto transition-transform {isImageExpanded ? 'scale-105 my-2' : ''}"
              loading="eager"
              onerror={(e) => {
                (e.currentTarget as HTMLElement).style.display = 'none';
              }}
            />
          </div>

          <!-- Interactive Multiple Choice Option Selector (A, B, C, D, E) -->
          {#if question.question_type.toLowerCase().includes('múltipla') || question.question_type.toLowerCase().includes('multipla')}
            <div class="bg-white rounded-xl p-3.5 border border-[#E5DFD4] shadow-2xs space-y-2">
              <div class="flex items-center justify-between text-xs font-sans text-slate-600 font-semibold">
                <span>Gabarito Pessoal (Selecione sua resposta):</span>
                {#if selectedOption}
                  <span class="text-sky-700 font-bold text-[11px]">Opção {selectedOption} selecionada</span>
                {/if}
              </div>

              <div class="grid grid-cols-5 gap-2">
                {#each ['A', 'B', 'C', 'D', 'E'] as opt}
                  <button
                    onclick={() => selectedOption = opt}
                    class="py-2 rounded-lg font-sans font-bold text-sm border transition flex flex-col items-center justify-center cursor-pointer {selectedOption === opt ? 'bg-sky-600 text-white border-sky-700 shadow-sm' : 'bg-[#FAF8F5] hover:bg-[#F2ECE0] text-slate-700 border-[#DDD6C8]'}"
                  >
                    <span>({opt})</span>
                  </button>
                {/each}
              </div>
            </div>
          {/if}

          <!-- OCR Mathematical Text Backup -->
          {#if question.text}
            <div class="p-4 rounded-xl bg-white border border-[#E5DFD4] text-slate-800 text-xs font-serif leading-relaxed shadow-2xs">
              <div class="text-[10px] font-sans uppercase font-bold text-slate-400 mb-1 flex items-center gap-1">
                <FileText size={12} />
                <span>Transcrição Matemática:</span>
              </div>
              <div use:mathAction={question.text}></div>
            </div>
          {/if}
        </div>
      </div>

      <!-- RIGHT COMPANION WORKBENCH (Cols 8-12): Integrated Socratic Hints, Constants, Notes -->
      <div class="lg:col-span-5 h-full flex flex-col bg-[#FAF8F5] overflow-hidden">
        <!-- Companion Tab Switcher -->
        <div class="p-2.5 bg-white border-b border-[#E8E2D8] flex items-center justify-between shrink-0 shadow-2xs">
          <div class="flex items-center space-x-1.5">
            <!-- Hints Tab -->
            <button
              onclick={() => activeRightTab = 'hints'}
              class="px-3 py-1.5 rounded-lg text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeRightTab === 'hints' ? 'bg-[#FAF8F5] text-slate-900 shadow-2xs border border-[#DDD6C8]' : 'text-slate-500 hover:text-slate-800'}"
            >
              <Lightbulb size={14} class="text-amber-500" />
              <span>Pistas (1-4)</span>
            </button>

            <!-- Notes Tab -->
            <button
              onclick={() => activeRightTab = 'notes'}
              class="px-3 py-1.5 rounded-lg text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeRightTab === 'notes' ? 'bg-[#FAF8F5] text-slate-900 shadow-2xs border border-[#DDD6C8]' : 'text-slate-500 hover:text-slate-800'}"
            >
              <FileEdit size={14} />
              <span>Anotações</span>
            </button>

            <!-- Formulas Tab -->
            <button
              onclick={() => activeRightTab = 'formulas'}
              class="px-3 py-1.5 rounded-lg text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeRightTab === 'formulas' ? 'bg-[#FAF8F5] text-slate-900 shadow-2xs border border-[#DDD6C8]' : 'text-slate-500 hover:text-slate-800'}"
            >
              <BookOpen size={14} />
              <span>Constantes & Fórmulas</span>
            </button>
          </div>
        </div>

        <!-- Companion Content Panel (Scrollable) -->
        <div class="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-3 font-sans text-xs">
          <!-- TAB 1: SOCRATIC HINTS LADDER -->
          {#if activeRightTab === 'hints'}
            <div class="space-y-3">
              <div class="p-3 rounded-xl bg-white border border-[#E5DFD4] text-xs font-sans text-slate-700 shadow-2xs">
                <strong class="font-bold text-slate-900 block">{question.clues.title}</strong>
                <div class="text-[11px] text-slate-500 mt-0.5">Use as teclas <span class="key-cap text-[8px]">1</span> a <span class="key-cap text-[8px]">4</span> para abrir gradualmente.</div>
              </div>

              <!-- Level 1: Principle (Mint) -->
              <div class="rounded-xl border border-[#bbf7d0] bg-[#f0fdf4] overflow-hidden shadow-2xs">
                <button
                  onclick={() => toggleClue(1)}
                  class="w-full text-left px-3.5 py-2.5 text-xs font-sans font-bold text-[#166534] flex items-center justify-between hover:bg-[#e6fbf0] transition cursor-pointer"
                >
                  <span class="flex items-center gap-2">
                    <span class="px-1.5 py-0.5 rounded bg-[#bbf7d0] text-[#166534] font-mono text-[9px] font-bold">1</span>
                    Princípio Físico Fundamental
                  </span>
                  {#if openClues[1]}<ChevronUp size={14} />{:else}<ChevronDown size={14} />{/if}
                </button>
                {#if openClues[1]}
                  <div class="px-3.5 pb-3.5 text-xs font-serif text-slate-800 leading-relaxed border-t border-[#bbf7d0] pt-2.5 bg-white" use:mathAction={question.clues.level1}></div>
                {/if}
              </div>

              <!-- Level 2: Setup (Sky) -->
              <div class="rounded-xl border border-[#bae6fd] bg-[#f0f9ff] overflow-hidden shadow-2xs">
                <button
                  onclick={() => toggleClue(2)}
                  class="w-full text-left px-3.5 py-2.5 text-xs font-sans font-bold text-[#0369a1] flex items-center justify-between hover:bg-[#e0f2fe] transition cursor-pointer"
                >
                  <span class="flex items-center gap-2">
                    <span class="px-1.5 py-0.5 rounded bg-[#bae6fd] text-[#0369a1] font-mono text-[9px] font-bold">2</span>
                    Montagem Geométrica & Coordenadas
                  </span>
                  {#if openClues[2]}<ChevronUp size={14} />{:else}<ChevronDown size={14} />{/if}
                </button>
                {#if openClues[2]}
                  <div class="px-3.5 pb-3.5 text-xs font-serif text-slate-800 leading-relaxed border-t border-[#bae6fd] pt-2.5 bg-white" use:mathAction={question.clues.level2}></div>
                {/if}
              </div>

              <!-- Level 3: Checkpoint (Honey/Amber) -->
              <div class="rounded-xl border border-[#fde68a] bg-[#fffbeb] overflow-hidden shadow-2xs">
                <button
                  onclick={() => toggleClue(3)}
                  class="w-full text-left px-3.5 py-2.5 text-xs font-sans font-bold text-[#92400e] flex items-center justify-between hover:bg-[#fef3c7] transition cursor-pointer"
                >
                  <span class="flex items-center gap-2">
                    <span class="px-1.5 py-0.5 rounded bg-[#fde68a] text-[#92400e] font-mono text-[9px] font-bold">3</span>
                    Ponto de Checagem Intermediário
                  </span>
                  {#if openClues[3]}<ChevronUp size={14} />{:else}<ChevronDown size={14} />{/if}
                </button>
                {#if openClues[3]}
                  <div class="px-3.5 pb-3.5 text-xs font-serif text-slate-800 leading-relaxed border-t border-[#fde68a] pt-2.5 bg-white" use:mathAction={question.clues.level3}></div>
                {/if}
              </div>

              <!-- Level 4: Derivation & Traps (Rose/Coral) -->
              <div class="rounded-xl border border-[#fecdd3] bg-[#fff1f2] overflow-hidden shadow-2xs">
                <button
                  onclick={() => toggleClue(4)}
                  class="w-full text-left px-3.5 py-2.5 text-xs font-sans font-bold text-[#9f1239] flex items-center justify-between hover:bg-[#ffe4e6] transition cursor-pointer"
                >
                  <span class="flex items-center gap-2">
                    <span class="px-1.5 py-0.5 rounded bg-[#fecdd3] text-[#9f1239] font-mono text-[9px] font-bold">4</span>
                    Derivação Completa & Armadilhas
                  </span>
                  {#if openClues[4]}<ChevronUp size={14} />{:else}<ChevronDown size={14} />{/if}
                </button>
                {#if openClues[4]}
                  <div class="px-3.5 pb-3.5 text-xs font-serif text-slate-800 leading-relaxed border-t border-[#fecdd3] pt-2.5 bg-white" use:mathAction={question.clues.level4}></div>
                {/if}
              </div>
            </div>

          <!-- TAB 2: CANDIDATE SCRATCHPAD & NOTES -->
          {:else if activeRightTab === 'notes'}
            <div class="space-y-2 h-full flex flex-col">
              <div class="flex items-center justify-between text-xs font-sans font-bold text-slate-700">
                <span>Caderno de Resolução:</span>
                {#if isSavedNotice}
                  <span class="text-emerald-700 flex items-center gap-1 text-[11px] font-medium">
                    <Check size={13} /> Salvo no Perfil
                  </span>
                {/if}
              </div>

              <textarea
                value={userNotes}
                oninput={handleNotesInput}
                placeholder="Digite suas etapas de resolução, fórmulas matemáticas com $...$ ou observações importantes..."
                rows="14"
                class="w-full flex-1 bg-white text-slate-800 border border-[#DDD6C8] rounded-xl p-3.5 text-xs font-serif focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 leading-relaxed shadow-2xs custom-scrollbar"
              ></textarea>

              <div class="p-2.5 rounded-lg bg-white border border-[#E5DFD4] text-[11px] text-slate-600 font-sans shadow-2xs">
                💡 Suporta equações em LaTeX usando <code>$x = \frac&#123;a&#125;&#123;b&#125;$</code>.
              </div>
            </div>

          <!-- TAB 3: CONSTANTS & FORMULAS REFERENCE -->
          {:else if activeRightTab === 'formulas'}
            <div class="space-y-4">
              <!-- Physical Constants Quickcard -->
              <div class="bg-white rounded-xl p-3.5 border border-[#E5DFD4] shadow-2xs space-y-2">
                <div class="text-xs font-sans font-bold text-slate-800 flex items-center gap-1.5">
                  <Hash size={13} class="text-sky-600" />
                  <span>Constantes Fundamentais:</span>
                </div>
                <div class="grid grid-cols-2 gap-2">
                  {#each physicalConstants as pc}
                    <div class="p-2 rounded-lg bg-[#FAF8F5] border border-[#E8E2D8] text-[11px]">
                      <div class="text-[10px] text-slate-500">{pc.label}:</div>
                      <div class="font-serif text-slate-900 font-medium py-0.5" use:mathAction={`$${pc.symbol} = ${pc.val}$`}></div>
                    </div>
                  {/each}
                </div>
              </div>

              <!-- Area Formulas -->
              <div class="space-y-2">
                <div class="text-xs font-sans font-bold text-slate-800">
                  Formulário Oficial: {question.area}
                </div>

                {#each areaFormulas() as f}
                  <div class="p-3 bg-white border border-[#E5DFD4] rounded-xl shadow-2xs space-y-1">
                    <div class="text-[11px] font-sans font-bold text-slate-600">{f.name}:</div>
                    <div class="text-xs text-slate-900 overflow-x-auto py-1" use:mathAction={`$$${f.eq}$$`}></div>
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
    class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4"
    role="dialog"
    aria-modal="true"
    tabindex="-1"
    onclick={() => isZoomModalOpen = false}
    onkeydown={(e) => { if (e.key === 'Escape') isZoomModalOpen = false; }}
  >
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <div
      class="bg-white rounded-2xl p-5 max-w-6xl max-h-[95vh] overflow-auto shadow-2xl relative select-none border border-[#E5DFD4]"
      role="document"
      onclick={(e) => e.stopPropagation()}
    >
      <button
        onclick={() => isZoomModalOpen = false}
        class="absolute top-4 right-4 bg-[#FAF8F5] hover:bg-[#F2ECE0] text-slate-700 rounded-lg px-3 py-1 font-sans text-xs font-semibold transition z-10 border border-[#DDD6C8]"
      >
        ✕ Fechar (Esc)
      </button>
      <img
        src={question.image}
        alt={`Zoom ${question.id}`}
        class="max-w-full h-auto mx-auto"
      />
    </div>
  </div>
{/if}
