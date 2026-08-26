<script lang="ts">
  import type { Question, QuestionStatus } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import { mathAction } from '../math';
  import confetti from 'canvas-confetti';
  import { 
    CheckCircle2, Bookmark, XCircle, Clock, 
    ZoomIn, ZoomOut, Maximize2, Split, 
    Play, Pause, RotateCcw, AlertTriangle, FileText
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

  // 15-Minute Countdown Timer
  let timerSeconds = $state(15 * 60);
  let isTimerRunning = $state(false);
  let timerInterval: any = null;

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

  export function triggerZoom() {
    isZoomModalOpen = !isZoomModalOpen;
  }

  const uState = $derived(
    question ? profileStore.getQuestionState(question.id) : null
  );

  const theme = $derived(
    question ? AREA_THEMES[question.area] : null
  );
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
    <div class="px-5 py-3 bg-white border-b border-[#E8E2D8] flex flex-wrap items-center justify-between gap-3 shrink-0 shadow-2xs">
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

    <!-- Secondary Context Bar: Subtopic + Errata / Flags + Toolbar -->
    <div class="px-5 py-2 bg-[#FAF8F5] border-b border-[#E8E2D8] flex items-center justify-between text-xs font-sans shrink-0">
      <div class="flex items-center space-x-2 truncate">
        <span class="text-slate-400 uppercase text-[10px] font-bold">Subtópico:</span>
        <span class="text-slate-800 font-semibold truncate">{question.subtopic}</span>

        {#if question.errata || question.flag}
          <span class="px-2 py-0.5 rounded-full bg-[#fef3c7] text-[#92400e] border border-[#fde68a] text-[11px] font-semibold flex items-center gap-1">
            <AlertTriangle size={12} />
            {question.flag || question.errata}
          </span>
        {/if}
      </div>

      <!-- Canvas Utilities -->
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
          class="p-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-[#EAE4D8] transition"
          title="Alternar Tamanho"
        >
          {#if isImageExpanded}<ZoomOut size={15} />{:else}<ZoomIn size={15} />{/if}
        </button>

        <button
          onclick={() => isZoomModalOpen = true}
          class="p-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-[#EAE4D8] transition"
          title="Tela Cheia (Z)"
        >
          <Maximize2 size={15} />
        </button>
      </div>
    </div>

    <!-- Main Problem Viewer Canvas (Expansive White Paper Card) -->
    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 flex flex-col items-center justify-start bg-study-grid min-h-0">
      <!-- High-Resolution Card Frame -->
      <div class="w-full max-w-4xl bg-white rounded-xl p-5 shadow-sm transition-all duration-200 border border-[#E5DFD4] select-none">
        <img
          src={question.image}
          alt={`Problema ${question.id}`}
          class="w-full h-auto object-contain mx-auto transition-transform {isImageExpanded ? 'scale-110 my-4' : ''}"
          loading="eager"
          onerror={(e) => {
            (e.currentTarget as HTMLElement).style.display = 'none';
          }}
        />
      </div>

      <!-- OCR Mathematical Backup if available -->
      {#if question.text}
        <div class="w-full max-w-4xl mt-4 p-5 rounded-xl bg-white border border-[#E5DFD4] text-slate-800 text-xs font-serif leading-relaxed shadow-2xs">
          <div class="text-[10px] font-sans uppercase font-bold text-slate-400 mb-1 flex items-center gap-1">
            <FileText size={12} />
            <span>Transcrição Matemática:</span>
          </div>
          <div use:mathAction={question.text}></div>
        </div>
      {/if}
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
