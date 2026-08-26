<script lang="ts">
  import type { TwinPair } from '../types';
  import { AREA_THEMES } from '../constants';
  import { Split, ChevronLeft, ChevronRight, ArrowUpRight, Search, Sun, Moon } from 'lucide-svelte';

  let {
    pairs,
    onSelectQuestionById
  }: {
    pairs: TwinPair[];
    onSelectQuestionById: (qid: string) => void;
  } = $props();

  let selectedArea = $state<string>('All');
  let selectedExam = $state<string>('All');
  let currentPairIndex = $state<number>(0);
  let searchQuery = $state<string>('');
  let isInverted = $state<boolean>(false);

  const areasList = $derived(
    Array.from(new Set(pairs.map(p => p.area))).sort()
  );

  const examsList = $derived(
    Array.from(new Set(pairs.map(p => p.exam_id))).sort().reverse()
  );

  const filteredPairs = $derived(
    pairs.filter(p => {
      if (selectedArea !== 'All' && p.area !== selectedArea) return false;
      if (selectedExam !== 'All' && p.exam_id !== selectedExam) return false;
      if (searchQuery) {
        const q = searchQuery.toLowerCase().trim();
        const inStem = p.stem.toLowerCase().includes(q);
        const inSub = p.subtopic.toLowerCase().includes(q);
        const inText = p.text_a.toLowerCase().includes(q) || p.text_b.toLowerCase().includes(q);
        if (!inStem && !inSub && !inText) return false;
      }
      return true;
    })
  );

  const activePair = $derived(
    filteredPairs[currentPairIndex] || filteredPairs[0] || null
  );

  function nextPair() {
    if (currentPairIndex < filteredPairs.length - 1) {
      currentPairIndex++;
    } else {
      currentPairIndex = 0;
    }
  }

  function prevPair() {
    if (currentPairIndex > 0) {
      currentPairIndex--;
    } else {
      currentPairIndex = filteredPairs.length - 1;
    }
  }
</script>

<div class="flex-1 h-full flex flex-col bg-[#0b101d] overflow-hidden">
  <!-- Twin Lab Command Bar -->
  <div class="px-5 py-3 bg-[#080d18] border-b border-white/8 flex flex-wrap items-center justify-between gap-3 shrink-0 select-none">
    <div class="flex items-center space-x-3">
      <div class="p-1.5 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30">
        <Split size={16} />
      </div>
      <div>
        <h2 class="text-sm font-bold text-white font-mono flex items-center gap-2">
          Laboratório de Variantes Gêmeas (Twin A/B)
          <span class="text-xs font-normal text-slate-400">
            [{filteredPairs.length} pares catalogados]
          </span>
        </h2>
        <p class="text-[11px] text-slate-500 font-mono">
          Comparação paramétrica e geométrica das versões A vs. B aplicadas no exame oficial.
        </p>
      </div>
    </div>

    <!-- Filters & Nav Controls -->
    <div class="flex items-center space-x-2 font-mono text-xs">
      <select
        value={selectedArea}
        onchange={(e) => { selectedArea = (e.target as HTMLSelectElement).value; currentPairIndex = 0; }}
        class="bg-slate-950 text-slate-200 border border-white/10 rounded px-2.5 py-1 focus:outline-none cursor-pointer"
      >
        <option value="All">Todas as Áreas</option>
        {#each areasList as a}
          <option value={a}>{a}</option>
        {/each}
      </select>

      <select
        value={selectedExam}
        onchange={(e) => { selectedExam = (e.target as HTMLSelectElement).value; currentPairIndex = 0; }}
        class="bg-slate-950 text-slate-200 border border-white/10 rounded px-2.5 py-1 focus:outline-none cursor-pointer"
      >
        <option value="All">Todos os Exames</option>
        {#each examsList as ex}
          <option value={ex}>{ex}</option>
        {/each}
      </select>

      <button
        onclick={() => isInverted = !isInverted}
        class="p-1 rounded text-slate-400 hover:text-white bg-slate-900 border border-white/10 transition"
        title="Inverter Modo Escuro dos Enunciados"
      >
        {#if isInverted}<Sun size={14} />{:else}<Moon size={14} />{/if}
      </button>

      <div class="flex items-center space-x-1 pl-2">
        <button
          onclick={prevPair}
          class="p-1 rounded bg-slate-900 hover:bg-slate-800 text-slate-300 border border-white/10 transition"
          title="Par Anterior"
        >
          <ChevronLeft size={15} />
        </button>
        <span class="font-bold text-slate-300 px-1">
          {filteredPairs.length > 0 ? currentPairIndex + 1 : 0}/{filteredPairs.length}
        </span>
        <button
          onclick={nextPair}
          class="p-1 rounded bg-slate-900 hover:bg-slate-800 text-slate-300 border border-white/10 transition"
          title="Próximo Par"
        >
          <ChevronRight size={15} />
        </button>
      </div>
    </div>
  </div>

  <!-- Dual Split Viewport -->
  {#if !activePair}
    <div class="flex-1 flex items-center justify-center text-slate-500 font-mono text-xs">
      Nenhum par de variantes gêmeas encontrado com os filtros selecionados.
    </div>
  {:else}
    {@const theme = AREA_THEMES[activePair.area]}

    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 space-y-4 bg-tech-grid">
      <!-- Subtopic & Stem Banner -->
      <div class="p-3 rounded-lg bg-[#0d1424] border border-white/10 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <span
            class="px-2 py-0.5 rounded text-xs font-mono font-bold border"
            style={theme ? `color: ${theme.accentHex}; border-color: ${theme.accentHex}40; background-color: ${theme.accentHex}15;` : ''}
          >
            {activePair.area}
          </span>
          <span class="text-white font-mono font-bold text-sm">
            Haste: {activePair.exam_id}-{activePair.stem}
          </span>
          <span class="text-slate-400 font-sans text-xs">
            Subtópico: <strong class="text-slate-200">{activePair.subtopic}</strong>
          </span>
        </div>
      </div>

      <!-- Side-by-Side Dual Problem Cards -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <!-- Variant A Column -->
        <div class="bg-[#0e1628] border border-sky-500/30 rounded-lg p-4 space-y-3 shadow-xl">
          <div class="flex items-center justify-between pb-2 border-b border-white/8">
            <div class="flex items-center space-x-2">
              <span class="px-2 py-0.5 rounded bg-sky-500 text-white font-mono font-bold text-xs">
                Variante A
              </span>
              <span class="font-mono font-bold text-xs text-sky-200">
                {activePair.qid_a}
              </span>
            </div>
            <button
              onclick={() => onSelectQuestionById(activePair.qid_a)}
              class="text-xs font-mono font-bold text-sky-400 hover:text-sky-200 flex items-center gap-1 hover:underline"
            >
              Abrir no Cockpit <ArrowUpRight size={12} />
            </button>
          </div>

          <div class="bg-white rounded-lg p-3 text-center border border-slate-300 shadow-inner select-none {isInverted ? 'invert hue-rotate-180 bg-slate-900 border-slate-700' : ''}">
            <img
              src={activePair.image_a}
              alt={activePair.qid_a}
              class="w-full h-auto object-contain max-h-[420px] mx-auto"
              loading="lazy"
            />
          </div>
        </div>

        <!-- Variant B Column -->
        <div class="bg-[#0e1628] border border-emerald-500/30 rounded-lg p-4 space-y-3 shadow-xl">
          <div class="flex items-center justify-between pb-2 border-b border-white/8">
            <div class="flex items-center space-x-2">
              <span class="px-2 py-0.5 rounded bg-emerald-500 text-white font-mono font-bold text-xs">
                Variante B
              </span>
              <span class="font-mono font-bold text-xs text-emerald-200">
                {activePair.qid_b}
              </span>
            </div>
            <button
              onclick={() => onSelectQuestionById(activePair.qid_b)}
              class="text-xs font-mono font-bold text-emerald-400 hover:text-emerald-200 flex items-center gap-1 hover:underline"
            >
              Abrir no Cockpit <ArrowUpRight size={12} />
            </button>
          </div>

          <div class="bg-white rounded-lg p-3 text-center border border-slate-300 shadow-inner select-none {isInverted ? 'invert hue-rotate-180 bg-slate-900 border-slate-700' : ''}">
            <img
              src={activePair.image_b}
              alt={activePair.qid_b}
              class="w-full h-auto object-contain max-h-[420px] mx-auto"
              loading="lazy"
            />
          </div>
        </div>
      </div>

      <!-- Difference Analysis Banner -->
      {#if activePair.diff}
        <div class="p-4 rounded-lg bg-[#090e1a] border border-white/10 space-y-2">
          <div class="text-xs font-mono font-bold text-slate-300 uppercase flex items-center gap-2">
            <span>🔬 Análise de Variação Física e Paramétrica:</span>
          </div>
          <div class="p-3 bg-slate-950 rounded border border-white/8 font-mono text-xs text-slate-300 whitespace-pre-wrap leading-relaxed">
            {activePair.diff}
          </div>
        </div>
      {/if}
    </div>
  {/if}
</div>
