<script lang="ts">
  import type { Question, BankData } from '../types';
  import { profileStore } from '../storage.svelte';
  import { OFFICIAL_FORMULAS, AREA_THEMES } from '../constants';
  import { mathAction } from '../math';
  import { 
    Lightbulb, FileEdit, Split, BookOpen, 
    ChevronDown, ChevronUp, ChevronRight, ChevronLeft,
    Check
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

<div class="h-full bg-[#FAF8F5] border-l border-[#E8E2D8] flex flex-col select-none transition-all duration-200 {isTrayCollapsed ? 'w-12' : 'w-88 lg:w-96'} shrink-0 shadow-2xs">
  <!-- Tray Collapsed Strip -->
  {#if isTrayCollapsed}
    <div class="h-full flex flex-col items-center justify-between py-4">
      <button
        onclick={() => isTrayCollapsed = false}
        class="text-slate-500 hover:text-slate-900 p-2 rounded-xl hover:bg-[#EAE4D8] transition cursor-pointer"
        title="Abrir Painel de Pistas e Anotações"
      >
        <ChevronLeft size={18} />
      </button>

      <div class="writing-mode-vertical text-slate-400 font-sans text-[11px] font-bold uppercase tracking-widest py-4">
        PISTAS & NOTAS
      </div>

      <div class="w-2 h-2 rounded-full bg-sky-400"></div>
    </div>
  {:else}
    <!-- Tray Header with Tab Switcher -->
    <div class="p-2.5 bg-[#FAF8F5] border-b border-[#E8E2D8] flex items-center justify-between">
      <div class="flex items-center space-x-1">
        <!-- Hints Tab -->
        <button
          onclick={() => activeInspectorTab = 'hints'}
          class="px-3 py-1.5 rounded-lg text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeInspectorTab === 'hints' ? 'bg-white text-slate-900 shadow-2xs border border-[#DDD6C8]' : 'text-slate-500 hover:text-slate-800'}"
          title="Pistas Socráticas (1-4)"
        >
          <Lightbulb size={14} class="text-amber-500" />
          <span>Pistas</span>
        </button>

        <!-- Notes Tab -->
        <button
          onclick={() => activeInspectorTab = 'notes'}
          class="px-3 py-1.5 rounded-lg text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeInspectorTab === 'notes' ? 'bg-white text-slate-900 shadow-2xs border border-[#DDD6C8]' : 'text-slate-500 hover:text-slate-800'}"
          title="Minhas Anotações"
        >
          <FileEdit size={14} />
          <span>Notas</span>
        </button>

        <!-- Twin Tab -->
        <button
          onclick={() => activeInspectorTab = 'twin'}
          class="px-3 py-1.5 rounded-lg text-xs font-sans font-bold flex items-center gap-1.5 transition cursor-pointer {activeInspectorTab === 'twin' ? 'bg-white text-slate-900 shadow-2xs border border-[#DDD6C8]' : 'text-slate-500 hover:text-slate-800'}"
          title="Variante Gêmea A/B"
        >
          <Split size={14} />
          <span>Gêmea</span>
        </button>

        <!-- Formulas Tab -->
        <button
          onclick={() => activeInspectorTab = 'formulas'}
          class="px-2 py-1.5 rounded-lg text-xs font-sans font-bold flex items-center gap-1 transition cursor-pointer {activeInspectorTab === 'formulas' ? 'bg-white text-slate-900 shadow-2xs border border-[#DDD6C8]' : 'text-slate-500 hover:text-slate-800'}"
          title="Fórmulas da Área"
        >
          <BookOpen size={14} />
        </button>
      </div>

      <!-- Collapse Button -->
      <button
        onclick={() => isTrayCollapsed = true}
        class="text-slate-400 hover:text-slate-700 p-1.5 rounded-lg hover:bg-[#EAE4D8] transition cursor-pointer"
        title="Ocultar Painel"
      >
        <ChevronRight size={16} />
      </button>
    </div>

    <!-- Inspector Content Pane -->
    <div class="flex-1 overflow-y-auto custom-scrollbar p-4 space-y-3 font-sans text-xs">
      {#if !question}
        <div class="text-center text-slate-400 font-sans py-12">
          Nenhuma questão selecionada.
        </div>
      {:else}
        <!-- TAB 1: SOCRATIC HINTS LADDER (PASTEL ACCORDION) -->
        {#if activeInspectorTab === 'hints'}
          <div class="space-y-3">
            <div class="p-3 rounded-xl bg-[#F4EFE6] border border-[#E5DDCF] text-xs font-sans text-slate-700 leading-relaxed">
              <strong class="font-bold text-slate-900">{question.clues.title}</strong>
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
        {:else if activeInspectorTab === 'notes'}
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
              rows="12"
              class="w-full flex-1 bg-white text-slate-800 border border-[#DDD6C8] rounded-xl p-3.5 text-xs font-serif focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 leading-relaxed shadow-2xs custom-scrollbar"
            ></textarea>

            <div class="p-2.5 rounded-lg bg-[#F4EFE6] border border-[#E5DDCF] text-[11px] text-slate-600 font-sans">
              💡 Você pode escrever equações em LaTeX usando <code>$x = \frac&#123;a&#125;&#123;b&#125;$</code>.
            </div>
          </div>

        <!-- TAB 3: TWIN A/B SISTER COMPARISON -->
        {:else if activeInspectorTab === 'twin'}
          <div class="space-y-3">
            {#if !question.twin_id}
              <div class="p-5 rounded-xl bg-white border border-[#E5DFD4] text-center text-slate-400 font-sans text-xs">
                Esta questão não possui variante gêmea A/B indexada.
              </div>
            {:else}
              <div class="p-3 rounded-xl bg-[#eff8ff] border border-[#bae6fd] flex items-center justify-between">
                <div>
                  <div class="text-xs font-sans font-bold text-[#0369a1]">Variante Irmã: {question.twin_id}</div>
                  <div class="text-[11px] text-slate-500 font-sans">Exame {question.exam_id}</div>
                </div>
                {#if onJumpToTwin}
                  <button
                    onclick={() => onJumpToTwin?.(question!.twin_id!)}
                    class="px-2.5 py-1 rounded-lg bg-[#0284c7] hover:bg-[#0369a1] text-white font-sans text-xs font-bold transition shadow-xs cursor-pointer"
                  >
                    Carregar ➔
                  </button>
                {/if}
              </div>

              <!-- Twin Thumbnail -->
              {#if twinQuestion}
                <div class="bg-white rounded-xl p-3 text-center border border-[#E5DFD4] shadow-2xs">
                  <img
                    src={twinQuestion.image}
                    alt={twinQuestion.id}
                    class="max-w-full h-auto object-contain max-h-[220px] mx-auto"
                    loading="lazy"
                  />
                </div>
              {/if}

              <!-- Difference Analysis -->
              {#if twinPair?.diff}
                <div class="space-y-1.5">
                  <div class="text-xs font-sans font-bold text-slate-700">Diferenças Paramétricas:</div>
                  <div class="p-3 bg-white rounded-xl border border-[#E5DFD4] font-sans text-xs text-slate-700 whitespace-pre-wrap leading-relaxed shadow-2xs">
                    {twinPair.diff}
                  </div>
                </div>
              {/if}
            {/if}
          </div>

        <!-- TAB 4: OFFICIAL FORMULA CHEAT SHEET -->
        {:else if activeInspectorTab === 'formulas'}
          <div class="space-y-3">
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
        {/if}
      {/if}
    </div>
  {/if}
</div>
