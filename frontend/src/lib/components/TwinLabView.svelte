<script lang="ts">
  import type { TwinPair } from '../types';
  import { AREA_THEMES } from '../constants';
  import { Split, ChevronLeft, ChevronRight, ArrowUpRight } from 'lucide-svelte';

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

<div class="flex-1 h-full flex flex-col bg-[#FDFBF7] overflow-hidden">
  <!-- Twin Lab Command Bar -->
  <div class="px-6 py-3 bg-white border-b border-[#E8E2D8] flex flex-wrap items-center justify-between gap-3 shrink-0 select-none shadow-2xs">
    <div class="flex items-center space-x-3">
      <div class="p-2 rounded-xl bg-[#eff8ff] text-[#0369a1] border border-[#bae6fd]">
        <Split size={17} />
      </div>
      <div>
        <h2 class="text-sm font-bold text-slate-900 font-sans flex items-center gap-2">
          Laboratório de Variantes Gêmeas (Twin A/B)
          <span class="text-xs font-semibold text-slate-500">
            [{filteredPairs.length} pares catalogados]
          </span>
        </h2>
        <p class="text-[11px] text-slate-500 font-sans">
          Compare as variações paramétricas e conceituais elaboradas pela banca para as versões paralelas.
        </p>
      </div>
    </div>

    <!-- Filters & Nav Controls -->
    <div class="flex items-center space-x-2 font-sans text-xs">
      <select
        value={selectedArea}
        onchange={(e) => { selectedArea = (e.target as HTMLSelectElement).value; currentPairIndex = 0; }}
        class="bg-[#FAF8F5] text-slate-800 border border-[#DDD6C8] rounded-lg px-3 py-1.5 focus:outline-none cursor-pointer font-medium"
      >
        <option value="All">Todas as Áreas</option>
        {#each areasList as a}
          <option value={a}>{a}</option>
        {/each}
      </select>

      <select
        value={selectedExam}
        onchange={(e) => { selectedExam = (e.target as HTMLSelectElement).value; currentPairIndex = 0; }}
        class="bg-[#FAF8F5] text-slate-800 border border-[#DDD6C8] rounded-lg px-3 py-1.5 focus:outline-none cursor-pointer font-medium"
      >
        <option value="All">Todos os Exames</option>
        {#each examsList as ex}
          <option value={ex}>{ex}</option>
        {/each}
      </select>

      <div class="flex items-center space-x-1 pl-2">
        <button
          onclick={prevPair}
          class="p-1.5 rounded-lg bg-[#FAF8F5] hover:bg-[#EAE4D8] text-slate-700 border border-[#DDD6C8] transition cursor-pointer"
          title="Par Anterior"
        >
          <ChevronLeft size={15} />
        </button>
        <span class="font-bold text-slate-700 px-1.5">
          {filteredPairs.length > 0 ? currentPairIndex + 1 : 0}/{filteredPairs.length}
        </span>
        <button
          onclick={nextPair}
          class="p-1.5 rounded-lg bg-[#FAF8F5] hover:bg-[#EAE4D8] text-slate-700 border border-[#DDD6C8] transition cursor-pointer"
          title="Próximo Par"
        >
          <ChevronRight size={15} />
        </button>
      </div>
    </div>
  </div>

  <!-- Dual Split Viewport -->
  {#if !activePair}
    <div class="flex-1 flex items-center justify-center text-slate-400 font-sans text-xs">
      Nenhum par de variantes gêmeas encontrado com os filtros selecionados.
    </div>
  {:else}
    {@const theme = AREA_THEMES[activePair.area]}

    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 space-y-5 bg-study-grid">
      <!-- Subtopic & Stem Banner -->
      <div class="p-3.5 rounded-xl bg-white border border-[#E5DFD4] shadow-xs flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <span class="px-2.5 py-0.5 rounded-lg text-xs font-sans font-bold border {theme?.badge || 'bg-slate-100 text-slate-800'}">
            {activePair.area}
          </span>
          <span class="text-slate-900 font-sans font-bold text-sm">
            Haste: {activePair.exam_id}-{activePair.stem}
          </span>
          <span class="text-slate-500 font-sans text-xs">
            Subtópico: <strong class="text-slate-800">{activePair.subtopic}</strong>
          </span>
        </div>
      </div>

      <!-- Side-by-Side Dual Problem Cards -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <!-- Variant A Column -->
        <div class="bg-white border border-[#bae6fd] rounded-2xl p-5 space-y-3 shadow-sm">
          <div class="flex items-center justify-between pb-3 border-b border-[#E8E2D8]">
            <div class="flex items-center space-x-2">
              <span class="px-2.5 py-0.5 rounded-lg bg-[#eff8ff] text-[#0369a1] border border-[#bae6fd] font-sans font-bold text-xs">
                Variante A
              </span>
              <span class="font-sans font-bold text-xs text-slate-800">
                {activePair.qid_a}
              </span>
            </div>
            <button
              onclick={() => onSelectQuestionById(activePair.qid_a)}
              class="text-xs font-sans font-bold text-[#0284c7] hover:text-[#0369a1] flex items-center gap-1 hover:underline cursor-pointer"
            >
              Estudar no Canvas <ArrowUpRight size={13} />
            </button>
          </div>

          <div class="bg-[#FAF8F5] rounded-xl p-3 text-center border border-[#E5DFD4] select-none">
            <img
              src={activePair.image_a}
              alt={activePair.qid_a}
              class="w-full h-auto object-contain max-h-[420px] mx-auto"
              loading="lazy"
            />
          </div>
        </div>

        <!-- Variant B Column -->
        <div class="bg-white border border-[#bbf7d0] rounded-2xl p-5 space-y-3 shadow-sm">
          <div class="flex items-center justify-between pb-3 border-b border-[#E8E2D8]">
            <div class="flex items-center space-x-2">
              <span class="px-2.5 py-0.5 rounded-lg bg-[#f0fdf4] text-[#166534] border border-[#bbf7d0] font-sans font-bold text-xs">
                Variante B
              </span>
              <span class="font-sans font-bold text-xs text-slate-800">
                {activePair.qid_b}
              </span>
            </div>
            <button
              onclick={() => onSelectQuestionById(activePair.qid_b)}
              class="text-xs font-sans font-bold text-[#16a34a] hover:text-[#15803d] flex items-center gap-1 hover:underline cursor-pointer"
            >
              Estudar no Canvas <ArrowUpRight size={13} />
            </button>
          </div>

          <div class="bg-[#FAF8F5] rounded-xl p-3 text-center border border-[#E5DFD4] select-none">
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
        <div class="p-4 rounded-xl bg-white border border-[#E5DFD4] space-y-2 shadow-2xs">
          <div class="text-xs font-sans font-bold text-slate-800 flex items-center gap-2">
            <span>🔬 Análise de Variação Física e Paramétrica:</span>
          </div>
          <div class="p-3.5 bg-[#FAF8F5] rounded-lg border border-[#E5DDCF] font-sans text-xs text-slate-700 whitespace-pre-wrap leading-relaxed">
            {activePair.diff}
          </div>
        </div>
      {/if}
    </div>
  {/if}
</div>
