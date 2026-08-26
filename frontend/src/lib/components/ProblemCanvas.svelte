<script lang="ts">
  import type { Question, QuestionStatus } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import { mathAction } from '../math';
  import confetti from 'canvas-confetti';
  import { 
    CheckCircle2, Bookmark, XCircle, Clock, 
    ZoomIn, ZoomOut, Maximize2, Split, 
    Play, Pause, RotateCcw, AlertTriangle, Moon, Sun
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
  let isImageInverted = $state(false); // Invert black-on-white PDF crop to match dark mode

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
        particleCount: 60,
        spread: 70,
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
  <div class="flex-1 h-full flex flex-col items-center justify-center text-slate-500 font-mono text-xs p-8 bg-tech-grid">
    <div class="w-12 h-12 rounded-full border border-white/10 flex items-center justify-center text-slate-400 mb-3">
      Ψ
    </div>
    <span>Selecione uma questão no explorador lateral para carregar o canvas de física.</span>
  </div>
{:else}
  <div class="flex-1 h-full flex flex-col bg-[#0b101d] overflow-hidden">
    <!-- Top Cockpit Control Bar -->
    <div class="px-4 py-2.5 bg-[#080d18] border-b border-white/8 flex flex-wrap items-center justify-between gap-3 shrink-0">
      <!-- Question Identifiers & Path -->
      <div class="flex items-center space-x-2.5">
        <span
          class="px-2 py-0.5 rounded text-[11px] font-mono font-bold border"
          style={theme ? `color: ${theme.accentHex}; border-color: ${theme.accentHex}40; background-color: ${theme.accentHex}15;` : ''}
        >
          {question.area}
        </span>

        <span class="text-white font-mono font-extrabold text-sm tracking-tight">
          {question.id}
        </span>

        <span class="text-slate-400 font-mono text-xs">
          (Pág {question.page} • {question.question_type})
        </span>
      </div>

      <!-- Center Countdown Timer -->
      <div class="flex items-center space-x-2 bg-slate-950 border border-white/10 px-2.5 py-1 rounded">
        <span class="text-[10px] font-mono uppercase text-slate-400 font-bold">⏱️ Exame:</span>
        <span class="font-mono font-bold text-xs {timerSeconds < 180 ? 'text-rose-400 animate-pulse' : 'text-sky-400'} w-11 text-center">
          {formatTime(timerSeconds)}
        </span>
        <button
          onclick={toggleTimer}
          class="text-slate-400 hover:text-white p-0.5 rounded transition"
          title={isTimerRunning ? 'Pausar temporizador' : 'Iniciar cronômetro'}
        >
          {#if isTimerRunning}<Pause size={12} />{:else}<Play size={12} />{/if}
        </button>
        <button
          onclick={resetTimer}
          class="text-slate-500 hover:text-slate-300 p-0.5 rounded transition"
          title="Reiniciar (15 min)"
        >
          <RotateCcw size={11} />
        </button>
      </div>

      <!-- Right Action Keycaps -->
      <div class="flex items-center space-x-1.5 font-mono text-xs">
        <!-- Dominada (S) -->
        <button
          onclick={() => setStatus('solved')}
          class="px-2.5 py-1 rounded font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'solved' ? 'bg-emerald-600 text-white border-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.3)]' : 'bg-slate-900 hover:bg-emerald-950 text-slate-300 border-white/10 hover:border-emerald-500/40'}"
          title="Marcar Dominada (S)"
        >
          <CheckCircle2 size={13} />
          <span>Dominada</span>
          <span class="key-cap text-[8px]">S</span>
        </button>

        <!-- Revisar (R) -->
        <button
          onclick={() => setStatus('review')}
          class="px-2.5 py-1 rounded font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'review' ? 'bg-amber-600 text-white border-amber-500 shadow-[0_0_10px_rgba(245,158,11,0.3)]' : 'bg-slate-900 hover:bg-amber-950 text-slate-300 border-white/10 hover:border-amber-500/40'}"
          title="Marcar Revisão (R)"
        >
          <Bookmark size={13} />
          <span>Revisão</span>
          <span class="key-cap text-[8px]">R</span>
        </button>

        <!-- Erro (X) -->
        <button
          onclick={() => setStatus('failed')}
          class="px-2.5 py-1 rounded font-bold transition flex items-center gap-1.5 border cursor-pointer {uState?.status === 'failed' ? 'bg-rose-600 text-white border-rose-500 shadow-[0_0_10px_rgba(244,63,94,0.3)]' : 'bg-slate-900 hover:bg-rose-950 text-slate-300 border-white/10 hover:border-rose-500/40'}"
          title="Marcar Erro (X)"
        >
          <XCircle size={13} />
          <span>Erro</span>
          <span class="key-cap text-[8px]">X</span>
        </button>
      </div>
    </div>

    <!-- Secondary Context Bar: Subtopic + Errata / Flags + Toolbar -->
    <div class="px-4 py-1.5 bg-[#090e1a] border-b border-white/6 flex items-center justify-between text-xs font-mono shrink-0">
      <div class="flex items-center space-x-2 truncate">
        <span class="text-slate-500 uppercase text-[10px] font-bold">Subtópico:</span>
        <span class="text-slate-200 font-semibold truncate">{question.subtopic}</span>

        {#if question.errata || question.flag}
          <span class="px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 text-[10px] flex items-center gap-1">
            <AlertTriangle size={11} />
            {question.flag || question.errata}
          </span>
        {/if}
      </div>

      <!-- Canvas Utilities -->
      <div class="flex items-center space-x-2">
        {#if question.twin_id && onJumpToTwin}
          <button
            onclick={() => onJumpToTwin?.(question!.twin_id!)}
            class="px-2 py-0.5 rounded bg-sky-500/15 hover:bg-sky-500/25 text-sky-300 border border-sky-500/30 flex items-center gap-1 text-[11px] transition"
            title="Ir para Variante Irmã (T)"
          >
            <Split size={12} />
            <span>Gêmea ({question.twin_id})</span>
            <span class="key-cap text-[7px]">T</span>
          </button>
        {/if}

        <button
          onclick={() => isImageInverted = !isImageInverted}
          class="p-1 rounded text-slate-400 hover:text-white hover:bg-white/5 transition"
          title={isImageInverted ? 'Modo Papel Claro Original' : 'Inverter Cores (Modo Escuro)'}
        >
          {#if isImageInverted}<Sun size={14} />{:else}<Moon size={14} />{/if}
        </button>

        <button
          onclick={() => isImageExpanded = !isImageExpanded}
          class="p-1 rounded text-slate-400 hover:text-white hover:bg-white/5 transition"
          title="Alternar Tamanho de Visualização"
        >
          {#if isImageExpanded}<ZoomOut size={14} />{:else}<ZoomIn size={14} />{/if}
        </button>

        <button
          onclick={() => isZoomModalOpen = true}
          class="p-1 rounded text-slate-400 hover:text-white hover:bg-white/5 transition"
          title="Tela Cheia (Z)"
        >
          <Maximize2 size={14} />
        </button>
      </div>
    </div>

    <!-- Main Problem Viewer Canvas (Expansive Scrolling Viewport) -->
    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 flex flex-col items-center justify-start bg-tech-grid min-h-0">
      <!-- High-Resolution Card Frame -->
      <div class="w-full max-w-4xl bg-white rounded-lg p-4 shadow-2xl transition-all duration-200 border border-slate-300 select-none {isImageInverted ? 'invert hue-rotate-180 bg-slate-900 border-slate-700' : ''}">
        <img
          src={question.image}
          alt={`Problema ${question.id}`}
          class="w-full h-auto object-contain mx-auto transition-transform {isImageExpanded ? 'scale-110 my-6' : ''}"
          loading="eager"
          onerror={(e) => {
            (e.currentTarget as HTMLElement).style.display = 'none';
          }}
        />
      </div>

      <!-- OCR Mathematical Backup if available -->
      {#if question.text}
        <div class="w-full max-w-4xl mt-4 p-4 rounded-lg bg-slate-900/90 border border-white/10 text-slate-200 text-xs font-serif leading-relaxed">
          <div class="text-[10px] font-mono uppercase font-bold text-slate-500 mb-1">Transcrição Matemática (OCR KaTeX):</div>
          <div use:mathAction={question.text}></div>
        </div>
      {/if}
    </div>
  </div>
{/if}

<!-- Fullscreen High-Precision Zoom Modal -->
{#if isZoomModalOpen && question}
  <div
    class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4"
    role="dialog"
    aria-modal="true"
    tabindex="-1"
    onclick={() => isZoomModalOpen = false}
    onkeydown={(e) => { if (e.key === 'Escape') isZoomModalOpen = false; }}
  >
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <div
      class="bg-white rounded-lg p-4 max-w-6xl max-h-[95vh] overflow-auto shadow-2xl relative select-none {isImageInverted ? 'invert hue-rotate-180 bg-slate-900' : ''}"
      role="document"
      onclick={(e) => e.stopPropagation()}
    >
      <button
        onclick={() => isZoomModalOpen = false}
        class="absolute top-3 right-3 bg-slate-900 text-white rounded px-2.5 py-1 font-mono text-xs hover:bg-slate-800 transition z-10"
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
