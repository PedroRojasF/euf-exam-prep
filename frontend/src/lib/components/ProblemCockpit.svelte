<script lang="ts">
  import type { Question, QuestionStatus } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_CONFIG } from '../constants';
  import { mathAction } from '../math';
  import confetti from 'canvas-confetti';
  import { CheckCircle2, Bookmark, XCircle, Clock, ZoomIn, ZoomOut, Maximize2, Split, ChevronDown, ChevronUp, AlertTriangle, Lightbulb } from 'lucide-svelte';

  let {
    question,
    onJumpToTwin
  }: {
    question: Question | null;
    onJumpToTwin?: (twinId: string) => void;
  } = $props();

  let isZoomModalOpen = $state(false);
  let isImageExpanded = $state(false);
  let openClues = $state<Record<number, boolean>>({ 1: false, 2: false, 3: false, 4: false });
  let userNotes = $state<string>('');

  // Sync notes when question changes
  $effect(() => {
    if (question) {
      const uState = profileStore.getQuestionState(question.id);
      userNotes = uState.notes || '';
      openClues = { 1: false, 2: false, 3: false, 4: false };
    }
  });

  function setStatus(status: QuestionStatus) {
    if (!question) return;
    profileStore.updateQuestionStatus(question.id, status);

    if (status === 'solved') {
      triggerConfetti();
    }
  }

  function handleNotesChange(e: Event) {
    if (!question) return;
    const val = (e.target as HTMLTextAreaElement).value;
    userNotes = val;
    profileStore.updateQuestionNotes(question.id, val);
  }

  function toggleClue(level: number) {
    openClues[level] = !openClues[level];
  }

  export function toggleClueByLevel(level: number) {
    toggleClue(level);
  }

  export function triggerZoom() {
    isZoomModalOpen = !isZoomModalOpen;
  }

  function triggerConfetti() {
    confetti({
      particleCount: 50,
      spread: 60,
      origin: { y: 0.7 }
    });
  }

  const uState = $derived(
    question ? profileStore.getQuestionState(question.id) : null
  );

  const areaColor = $derived(
    question ? (AREA_CONFIG[question.area] || { bg: 'bg-slate-50', text: 'text-slate-900', border: 'border-slate-300', badge: 'bg-slate-100 text-slate-800 border-slate-300', accent: 'slate' }) : null
  );
</script>

{#if !question}
  <div class="lab-card p-12 text-center text-slate-400 font-mono text-xs">
    Selecione uma questão no menu lateral para iniciar o estudo.
  </div>
{:else}
  <div class="space-y-4">
    <!-- Active Question Card -->
    <div class="lab-card p-5 space-y-4">
      <!-- Header: ID, Meta pills, Actions -->
      <div class="flex flex-wrap items-start justify-between gap-3 pb-3.5 border-b border-slate-200">
        <div>
          <div class="flex items-center gap-2 flex-wrap">
            <h2 class="text-base font-mono font-bold text-slate-900 tracking-tight">
              {question.id}
            </h2>
            <span class="text-xs font-mono px-2 py-0.5 rounded border {areaColor?.badge}">
              {question.area}
            </span>
            <span class="text-xs font-sans px-2 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-300">
              {question.question_type}
            </span>
            <span class="text-xs font-mono text-slate-500">
              Exame {question.exam_id} • Pág {question.page}
            </span>
          </div>
          <div class="text-xs font-serif italic text-slate-600 mt-1">
            Subtópico Oficial: <strong class="font-sans font-semibold text-slate-800 not-italic">{question.subtopic}</strong>
          </div>
        </div>

        <!-- Quick Status Buttons -->
        <div class="flex items-center space-x-1.5 font-mono text-xs">
          <!-- Solved -->
          <button
            onclick={() => setStatus('solved')}
            class="px-2.5 py-1.5 rounded font-bold transition flex items-center gap-1 border {uState?.status === 'solved' ? 'bg-emerald-600 text-white border-emerald-700 shadow-xs' : 'bg-slate-100 hover:bg-emerald-50 text-slate-700 border-slate-300'}"
            title="Marcar como Dominada (Atalho: S)"
          >
            <CheckCircle2 size={13} />
            <span>Dominada</span>
            <span class="key-cap text-[8px]">S</span>
          </button>

          <!-- Review -->
          <button
            onclick={() => setStatus('review')}
            class="px-2.5 py-1.5 rounded font-bold transition flex items-center gap-1 border {uState?.status === 'review' ? 'bg-amber-500 text-white border-amber-600 shadow-xs' : 'bg-slate-100 hover:bg-amber-50 text-slate-700 border-slate-300'}"
            title="Marcar para Revisão (Atalho: R)"
          >
            <Bookmark size={13} />
            <span>Revisar</span>
            <span class="key-cap text-[8px]">R</span>
          </button>

          <!-- Failed -->
          <button
            onclick={() => setStatus('failed')}
            class="px-2.5 py-1.5 rounded font-bold transition flex items-center gap-1 border {uState?.status === 'failed' ? 'bg-rose-600 text-white border-rose-700 shadow-xs' : 'bg-slate-100 hover:bg-rose-50 text-slate-700 border-slate-300'}"
            title="Marcar como Erro a Repetir (Atalho: X)"
          >
            <XCircle size={13} />
            <span>Erro</span>
            <span class="key-cap text-[8px]">X</span>
          </button>

          <!-- Unsolved -->
          <button
            onclick={() => setStatus('unsolved')}
            class="px-2 py-1.5 rounded font-bold transition text-slate-500 hover:text-slate-800 bg-slate-100 border border-slate-300"
            title="Redefinir como Não Resolvida"
          >
            <Clock size={13} />
          </button>
        </div>
      </div>

      <!-- Errata / Warning Notice if any -->
      {#if question.errata || question.flag}
        <div class="p-3 bg-amber-50 border border-amber-300 rounded text-xs text-amber-900 flex items-start gap-2">
          <AlertTriangle size={15} class="shrink-0 text-amber-600 mt-0.5" />
          <div>
            {#if question.flag}
              <strong>Aviso da Banca:</strong> {question.flag}<br />
            {/if}
            {#if question.errata}
              <strong>Errata:</strong> {question.errata}
            {/if}
          </div>
        </div>
      {/if}

      <!-- High-Precision Problem Image View -->
      <div class="relative group bg-white border border-slate-200 rounded p-3 text-center flex flex-col items-center justify-center min-h-[300px]">
        <img
          src={question.image}
          alt={`Enunciado ${question.id}`}
          class="max-w-full h-auto object-contain max-h-[600px] rounded transition duration-200 select-none {isImageExpanded ? 'scale-110' : ''}"
          loading="eager"
          onerror={(e) => {
            (e.currentTarget as HTMLElement).style.display = 'none';
          }}
        />

        <!-- Fallback OCR Text View if image not available -->
        {#if question.text}
          <div class="w-full text-left text-xs font-serif text-slate-800 p-2 mt-2 bg-slate-50 border border-slate-200 rounded leading-relaxed" use:mathAction={question.text}></div>
        {/if}

        <!-- Top Right Floating Image Actions -->
        <div class="absolute top-2 right-2 flex items-center space-x-1 opacity-80 group-hover:opacity-100 transition bg-white/90 backdrop-blur-xs p-1 rounded border border-slate-200 shadow-xs">
          {#if question.twin_id && onJumpToTwin}
            <button
              onclick={() => onJumpToTwin?.(question!.twin_id!)}
              class="px-2 py-1 text-[11px] font-mono font-bold bg-sky-50 hover:bg-sky-100 text-sky-800 rounded border border-sky-300 flex items-center gap-1"
              title="Abrir Variante Irmã (Atalho: T)"
            >
              <Split size={12} />
              Gêmea ({question.twin_id})
              <span class="key-cap text-[7px]">T</span>
            </button>
          {/if}

          <button
            onclick={() => isImageExpanded = !isImageExpanded}
            class="p-1 text-slate-600 hover:text-slate-900 rounded hover:bg-slate-100"
            title="Expandir tamanho da imagem"
          >
            {#if isImageExpanded}
              <ZoomOut size={14} />
            {:else}
              <ZoomIn size={14} />
            {/if}
          </button>

          <button
            onclick={() => isZoomModalOpen = true}
            class="p-1 text-slate-600 hover:text-slate-900 rounded hover:bg-slate-100"
            title="Abrir Zoom em Tela Cheia (Atalho: Z)"
          >
            <Maximize2 size={14} />
          </button>
        </div>
      </div>

      <!-- Socratic AI Hint Ladder (Principles & Checkpoints) -->
      <div class="space-y-2 pt-2 border-t border-slate-200">
        <div class="flex items-center justify-between">
          <span class="text-xs font-mono font-bold text-slate-700 uppercase flex items-center gap-1.5">
            <Lightbulb size={14} class="text-amber-500" />
            Escada Socrática de Pistas ({question.clues.title})
          </span>
          <span class="text-[10px] font-mono text-slate-400">
            Atalhos: <span class="key-cap text-[8px]">1</span> a <span class="key-cap text-[8px]">4</span>
          </span>
        </div>

        <div class="grid grid-cols-1 gap-2">
          <!-- Level 1: Principle -->
          <div class="border border-slate-200 rounded-md overflow-hidden bg-slate-50">
            <button
              onclick={() => toggleClue(1)}
              class="w-full text-left px-3 py-2 text-xs font-mono font-semibold text-slate-800 flex items-center justify-between hover:bg-slate-100 transition"
            >
              <span class="flex items-center gap-2">
                <span class="key-cap text-[8px]">1</span>
                Nível 1: Princípio Físico Fundamental
              </span>
              {#if openClues[1]}<ChevronUp size={14} />{:else}<ChevronDown size={14} />{/if}
            </button>
            {#if openClues[1]}
              <div class="px-3 pb-3 text-xs font-serif text-slate-700 leading-relaxed border-t border-slate-200 pt-2 bg-white" use:mathAction={question.clues.level1}></div>
            {/if}
          </div>

          <!-- Level 2: Coordinate Setup -->
          <div class="border border-slate-200 rounded-md overflow-hidden bg-slate-50">
            <button
              onclick={() => toggleClue(2)}
              class="w-full text-left px-3 py-2 text-xs font-mono font-semibold text-slate-800 flex items-center justify-between hover:bg-slate-100 transition"
            >
              <span class="flex items-center gap-2">
                <span class="key-cap text-[8px]">2</span>
                Nível 2: Montagem Geométrica e Coordenadas
              </span>
              {#if openClues[2]}<ChevronUp size={14} />{:else}<ChevronDown size={14} />{/if}
            </button>
            {#if openClues[2]}
              <div class="px-3 pb-3 text-xs font-serif text-slate-700 leading-relaxed border-t border-slate-200 pt-2 bg-white" use:mathAction={question.clues.level2}></div>
            {/if}
          </div>

          <!-- Level 3: Intermediate Checkpoint -->
          <div class="border border-slate-200 rounded-md overflow-hidden bg-slate-50">
            <button
              onclick={() => toggleClue(3)}
              class="w-full text-left px-3 py-2 text-xs font-mono font-semibold text-slate-800 flex items-center justify-between hover:bg-slate-100 transition"
            >
              <span class="flex items-center gap-2">
                <span class="key-cap text-[8px]">3</span>
                Nível 3: Ponto de Checagem Intermediário
              </span>
              {#if openClues[3]}<ChevronUp size={14} />{:else}<ChevronDown size={14} />{/if}
            </button>
            {#if openClues[3]}
              <div class="px-3 pb-3 text-xs font-serif text-slate-700 leading-relaxed border-t border-slate-200 pt-2 bg-white" use:mathAction={question.clues.level3}></div>
            {/if}
          </div>

          <!-- Level 4: Deep Derivation & Trap Analysis -->
          <div class="border border-slate-200 rounded-md overflow-hidden bg-slate-50">
            <button
              onclick={() => toggleClue(4)}
              class="w-full text-left px-3 py-2 text-xs font-mono font-semibold text-slate-800 flex items-center justify-between hover:bg-slate-100 transition"
            >
              <span class="flex items-center gap-2">
                <span class="key-cap text-[8px]">4</span>
                Nível 4: Derivação Completa e Armadilhas da Banca
              </span>
              {#if openClues[4]}<ChevronUp size={14} />{:else}<ChevronDown size={14} />{/if}
            </button>
            {#if openClues[4]}
              <div class="px-3 pb-3 text-xs font-serif text-slate-700 leading-relaxed border-t border-slate-200 pt-2 bg-white" use:mathAction={question.clues.level4}></div>
            {/if}
          </div>
        </div>
      </div>

      <!-- Personal Study Notes Editor -->
      <div class="space-y-1.5 pt-2 border-t border-slate-200">
        <label for="study-notes-textarea" class="block text-xs font-mono font-bold text-slate-700 uppercase">
          Minhas Anotações de Resolução (Salvas no Perfil):
        </label>
        <textarea
          id="study-notes-textarea"
          value={userNotes}
          oninput={handleNotesChange}
          placeholder="Escreva seus passos, armadilhas a lembrar ou dúvidas nesta questão..."
          rows="3"
          class="w-full text-xs font-mono bg-slate-50 border border-slate-300 rounded p-2.5 focus:ring-1 focus:ring-slate-700 focus:outline-none transition leading-relaxed"
        ></textarea>
      </div>
    </div>
  </div>
{/if}

<!-- Fullscreen Zoom Modal -->
{#if isZoomModalOpen && question}
  <div
    class="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-xs flex items-center justify-center p-4"
    role="dialog"
    aria-modal="true"
    tabindex="-1"
    onclick={() => isZoomModalOpen = false}
    onkeydown={(e) => { if (e.key === 'Escape') isZoomModalOpen = false; }}
  >
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <div
      class="bg-white rounded-lg p-4 max-w-5xl max-h-[90vh] overflow-auto shadow-2xl relative"
      role="document"
      onclick={(e) => e.stopPropagation()}
    >
      <button
        onclick={() => isZoomModalOpen = false}
        class="absolute top-2 right-2 bg-slate-100 hover:bg-slate-200 text-slate-800 rounded-full p-1 font-mono text-xs"
      >
        ✕ Esc
      </button>
      <img
        src={question.image}
        alt={`Zoom ${question.id}`}
        class="max-w-full h-auto mx-auto select-none"
      />
    </div>
  </div>
{/if}
