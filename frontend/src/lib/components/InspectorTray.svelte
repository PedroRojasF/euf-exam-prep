<script lang="ts">
  import type { Question, BankData } from '../types';
  import { profileStore } from '../storage.svelte';
  import { OFFICIAL_FORMULAS, AREA_THEMES } from '../constants';
  import { mathAction } from '../math';
  import { 
    Lightbulb, FileEdit, Split, BookOpen, 
    ChevronDown, ChevronUp, ChevronRight, ChevronLeft,
    Check, Sparkles, AlertCircle
  } from 'lucide-svelte';

  let {
    question,
    bankData,
    onJumpToTwin
  }: {
    question: Question | null;
    bankData: BankData | null;
    onJumpToTwin?: (twinId: string) => void;
  } = $props();

  let activeInspectorTab = $state<'hints' | 'notes' | 'twin' | 'formulas'>('hints');
  let isTrayCollapsed = $state<boolean>(false);
  let openClues = $state<Record<number, boolean>>({ 1: true, 2: false, 3: false, 4: false });
  let userNotes = $state<string>('');
  let isSavedNotice = $state<boolean>(false);

  // Sync notes and clues when question changes
  $effect(() => {
    if (question) {
      const uState = profileStore.getQuestionState(question.id);
      userNotes = uState.notes || '';
      openClues = { 1: true, 2: false, 3: false, 4: false };
    }
  });

  function toggleClue(lvl: number) {
    openClues[lvl] = !openClues[lvl];
  }

  export function toggleClueByLevel(lvl: number) {
    toggleClue(lvl);
  }

  function handleNotesInput(e: Event) {
    if (!question) return;
    const val = (e.target as HTMLTextAreaElement).value;
    userNotes = val;
    profileStore.updateQuestionNotes(question.id, val);
    isSavedNotice = true;
    setTimeout(() => { isSavedNotice = false; }, 1500);
  }

  // Find twin question and pair data
  const twinQuestion = $derived(() => {
    if (!question?.twin_id || !bankData) return null;
    return bankData.questions.find(q => q.id === question.twin_id) || null;
  });

  const twinPair = $derived(() => {
    if (!question?.twin_stem || !bankData) return null;
    return bankData.pairs.find(p => p.exam_id === question.exam_id && p.stem === question.twin_stem) || null;
  });

  // Find formulas for current question's area
  const areaFormulas = $derived(() => {
    if (!question) return [];
    const cat = OFFICIAL_FORMULAS.find(c => c.category === question.area || c.category.includes(question.area.split(' ')[0]));
    return cat ? cat.formulas : OFFICIAL_FORMULAS[0].formulas;
  });
</script>

<div class="h-full bg-[#080d19] border-l border-white/8 flex flex-col select-none transition-all duration-200 {isTrayCollapsed ? 'w-10' : 'w-88 lg:w-96'} shrink-0">
  <!-- Tray Collapsed Strip -->
  {#if isTrayCollapsed}
    <div class="h-full flex flex-col items-center justify-between py-3">
      <button
        onclick={() => isTrayCollapsed = false}
        class="text-slate-400 hover:text-white p-1.5 rounded hover:bg-white/5 transition"
        title="Expandir Painel de Análise"
      >
        <ChevronLeft size={16} />
      </button>

      <div class="writing-mode-vertical text-slate-500 font-mono text-xs uppercase tracking-widest py-4">
        ANÁLISE SOCRÁTICA
      </div>

      <div class="w-2 h-2 rounded-full bg-sky-500"></div>
    </div>
  {:else}
    <!-- Tray Header with Tab Switcher -->
    <div class="p-2 bg-[#060a14] border-b border-white/8 flex items-center justify-between">
      <div class="flex items-center space-x-1">
        <!-- Hints Tab -->
        <button
          onclick={() => activeInspectorTab = 'hints'}
          class="px-2.5 py-1 rounded text-xs font-mono font-bold flex items-center gap-1.5 transition {activeInspectorTab === 'hints' ? 'bg-sky-500/20 text-sky-300 border border-sky-500/30' : 'text-slate-400 hover:text-slate-200'}"
          title="Pistas Socráticas (1-4)"
        >
          <Lightbulb size={13} class="text-amber-400" />
          <span>Pistas</span>
        </button>

        <!-- Notes Tab -->
        <button
          onclick={() => activeInspectorTab = 'notes'}
          class="px-2.5 py-1 rounded text-xs font-mono font-bold flex items-center gap-1.5 transition {activeInspectorTab === 'notes' ? 'bg-sky-500/20 text-sky-300 border border-sky-500/30' : 'text-slate-400 hover:text-slate-200'}"
          title="Minhas Anotações"
        >
          <FileEdit size={13} />
          <span>Notas</span>
        </button>

        <!-- Twin Tab -->
        <button
          onclick={() => activeInspectorTab = 'twin'}
          class="px-2.5 py-1 rounded text-xs font-mono font-bold flex items-center gap-1.5 transition {activeInspectorTab === 'twin' ? 'bg-sky-500/20 text-sky-300 border border-sky-500/30' : 'text-slate-400 hover:text-slate-200'}"
          title="Variante Irmã A/B"
        >
          <Split size={13} />
          <span>Gêmea</span>
        </button>

        <!-- Formulas Tab -->
        <button
          onclick={() => activeInspectorTab = 'formulas'}
          class="px-2 py-1 rounded text-xs font-mono font-bold flex items-center gap-1 transition {activeInspectorTab === 'formulas' ? 'bg-sky-500/20 text-sky-300 border border-sky-500/30' : 'text-slate-400 hover:text-slate-200'}"
          title="Formulário da Área"
        >
          <BookOpen size={13} />
        </button>
      </div>

      <!-- Collapse Toggle -->
      <button
        onclick={() => isTrayCollapsed = true}
        class="text-slate-500 hover:text-white p-1 rounded hover:bg-white/5 transition"
        title="Recolher Painel"
      >
        <ChevronRight size={15} />
      </button>
    </div>

    <!-- Inspector Content Pane -->
    <div class="flex-1 overflow-y-auto custom-scrollbar p-3 space-y-3 font-sans text-xs">
      {#if !question}
        <div class="text-center text-slate-500 font-mono py-12">
          Nenhuma questão ativa.
        </div>
      {:else}
        <!-- TAB 1: SOCRATIC HINTS LADDER -->
        {#if activeInspectorTab === 'hints'}
          <div class="space-y-2.5">
            <div class="p-2 rounded bg-sky-950/30 border border-sky-500/20 text-[11px] text-sky-200 font-mono leading-tight">
              <strong>{question.clues.title}</strong>
              <div class="text-[10px] text-slate-400 mt-0.5">Use as teclas <span class="key-cap text-[8px]">1</span> a <span class="key-cap text-[8px]">4</span> para abrir gradualmente.</div>
            </div>

            <!-- Level 1: Principle -->
            <div class="rounded border border-white/10 bg-[#0d1424] overflow-hidden">
              <button
                onclick={() => toggleClue(1)}
                class="w-full text-left px-3 py-2 text-xs font-mono font-semibold text-slate-200 flex items-center justify-between hover:bg-white/5 transition"
              >
                <span class="flex items-center gap-2">
                  <span class="key-cap text-[8px]">1</span>
                  Princípio Físico Fundamental
                </span>
                {#if openClues[1]}<ChevronUp size={13} />{:else}<ChevronDown size={13} />{/if}
              </button>
              {#if openClues[1]}
                <div class="px-3 pb-3 text-xs font-serif text-slate-300 leading-relaxed border-t border-white/5 pt-2 bg-[#090f1d]" use:mathAction={question.clues.level1}></div>
              {/if}
            </div>

            <!-- Level 2: Setup -->
            <div class="rounded border border-white/10 bg-[#0d1424] overflow-hidden">
              <button
                onclick={() => toggleClue(2)}
                class="w-full text-left px-3 py-2 text-xs font-mono font-semibold text-slate-200 flex items-center justify-between hover:bg-white/5 transition"
              >
                <span class="flex items-center gap-2">
                  <span class="key-cap text-[8px]">2</span>
                  Montagem Geométrica & Coordenadas
                </span>
                {#if openClues[2]}<ChevronUp size={13} />{:else}<ChevronDown size={13} />{/if}
              </button>
              {#if openClues[2]}
                <div class="px-3 pb-3 text-xs font-serif text-slate-300 leading-relaxed border-t border-white/5 pt-2 bg-[#090f1d]" use:mathAction={question.clues.level2}></div>
              {/if}
            </div>

            <!-- Level 3: Checkpoint -->
            <div class="rounded border border-white/10 bg-[#0d1424] overflow-hidden">
              <button
                onclick={() => toggleClue(3)}
                class="w-full text-left px-3 py-2 text-xs font-mono font-semibold text-slate-200 flex items-center justify-between hover:bg-white/5 transition"
              >
                <span class="flex items-center gap-2">
                  <span class="key-cap text-[8px]">3</span>
                  Ponto de Checagem Intermediário
                </span>
                {#if openClues[3]}<ChevronUp size={13} />{:else}<ChevronDown size={13} />{/if}
              </button>
              {#if openClues[3]}
                <div class="px-3 pb-3 text-xs font-serif text-slate-300 leading-relaxed border-t border-white/5 pt-2 bg-[#090f1d]" use:mathAction={question.clues.level3}></div>
              {/if}
            </div>

            <!-- Level 4: Derivation & Traps -->
            <div class="rounded border border-white/10 bg-[#0d1424] overflow-hidden">
              <button
                onclick={() => toggleClue(4)}
                class="w-full text-left px-3 py-2 text-xs font-mono font-semibold text-slate-200 flex items-center justify-between hover:bg-white/5 transition"
              >
                <span class="flex items-center gap-2">
                  <span class="key-cap text-[8px]">4</span>
                  Derivação Completa & Armadilhas
                </span>
                {#if openClues[4]}<ChevronUp size={13} />{:else}<ChevronDown size={13} />{/if}
              </button>
              {#if openClues[4]}
                <div class="px-3 pb-3 text-xs font-serif text-slate-300 leading-relaxed border-t border-white/5 pt-2 bg-[#090f1d]" use:mathAction={question.clues.level4}></div>
              {/if}
            </div>
          </div>

        <!-- TAB 2: CANDIDATE SCRATCHPAD & NOTES -->
        {:else if activeInspectorTab === 'notes'}
          <div class="space-y-2 h-full flex flex-col">
            <div class="flex items-center justify-between text-[11px] font-mono text-slate-400">
              <span>Caderno de Resolução:</span>
              {#if isSavedNotice}
                <span class="text-emerald-400 flex items-center gap-1 text-[10px]">
                  <Check size={11} /> Salvo
                </span>
              {/if}
            </div>

            <textarea
              value={userNotes}
              oninput={handleNotesInput}
              placeholder="Digite seus passos de resolução, equações $...$ ou pontos a lembrar..."
              rows="12"
              class="w-full flex-1 bg-slate-950 text-slate-200 border border-white/10 rounded p-3 text-xs font-mono focus:outline-none focus:border-sky-500 leading-relaxed custom-scrollbar"
            ></textarea>

            <div class="p-2 rounded bg-white/4 border border-white/5 text-[10px] text-slate-400 font-mono">
              💡 Suporta equações matemáticas LaTeX com `$..$` ou `$$..$$`.
            </div>
          </div>

        <!-- TAB 3: TWIN A/B SISTER COMPARISON -->
        {:else if activeInspectorTab === 'twin'}
          <div class="space-y-3">
            {#if !question.twin_id}
              <div class="p-4 rounded bg-slate-900 border border-white/5 text-center text-slate-500 font-mono text-xs">
                Esta questão não possui variante gêmea A/B indexada.
              </div>
            {:else}
              <div class="p-2.5 rounded bg-sky-950/40 border border-sky-500/30 flex items-center justify-between">
                <div>
                  <div class="text-[11px] font-mono font-bold text-sky-300">Variante Irmã: {question.twin_id}</div>
                  <div class="text-[10px] text-slate-400 font-mono">Exame {question.exam_id}</div>
                </div>
                {#if onJumpToTwin}
                  <button
                    onclick={() => onJumpToTwin?.(question!.twin_id!)}
                    class="px-2 py-1 rounded bg-sky-600 hover:bg-sky-500 text-white font-mono text-[10px] font-bold transition"
                  >
                    Carregar no Canvas ➔
                  </button>
                {/if}
              </div>

              <!-- Twin Crop Thumbnail -->
              {#if twinQuestion}
                <div class="bg-white rounded p-2 text-center border border-slate-300">
                  <img
                    src={twinQuestion.image}
                    alt={twinQuestion.id}
                    class="max-w-full h-auto object-contain max-h-[220px] mx-auto"
                    loading="lazy"
                  />
                </div>
              {/if}

              <!-- Textual Diff Snippet -->
              {#if twinPair?.diff}
                <div class="space-y-1">
                  <div class="text-[10px] font-mono font-bold text-slate-400 uppercase">Diferenças Paramétricas:</div>
                  <div class="p-2.5 bg-slate-950 rounded border border-white/10 font-mono text-[11px] text-slate-300 whitespace-pre-wrap leading-relaxed">
                    {twinPair.diff}
                  </div>
                </div>
              {/if}
            {/if}
          </div>

        <!-- TAB 4: OFFICIAL FORMULA CHEAT SHEET -->
        {:else if activeInspectorTab === 'formulas'}
          <div class="space-y-2.5">
            <div class="text-[11px] font-mono font-bold text-slate-300 uppercase">
              Formulário Oficial: {question.area}
            </div>

            {#each areaFormulas() as f}
              <div class="p-2 bg-slate-950 border border-white/10 rounded">
                <div class="text-[10px] font-mono text-slate-400 mb-0.5">{f.name}:</div>
                <div class="text-xs text-white overflow-x-auto" use:mathAction={`$$${f.eq}$$`}></div>
              </div>
            {/each}
          </div>
        {/if}
      {/if}
    </div>
  {/if}
</div>
