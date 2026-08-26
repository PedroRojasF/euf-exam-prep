<script lang="ts">
  import type { TwinPair, Question } from '../types';
  import { AREA_CONFIG } from '../constants';
  import { mathAction } from '../math';
  import { Split, ArrowRight, CheckCircle, ChevronLeft, ChevronRight } from 'lucide-svelte';

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

<div class="space-y-4">
  <!-- Twin Lab Header & Controls -->
  <div class="lab-card p-4 space-y-3">
    <div class="flex flex-wrap items-center justify-between gap-3">
      <div>
        <h2 class="text-sm font-bold text-slate-900 font-mono flex items-center gap-2">
          <Split size={16} class="text-sky-600" />
          Laboratório de Variantes Gêmeas (A/B)
          <span class="text-xs font-normal text-slate-500">
            ({filteredPairs.length} pares encontrados)
          </span>
        </h2>
        <p class="text-xs text-slate-500 font-sans mt-0.5">
          Compare as duas versões paralelas elaboradas pela banca para identificar sutilezas conceituais e variações paramétricas.
        </p>
      </div>

      <!-- Filters & Nav -->
      <div class="flex flex-wrap items-center gap-2">
        <select
          value={selectedArea}
          onchange={(e) => { selectedArea = (e.target as HTMLSelectElement).value; currentPairIndex = 0; }}
          class="text-xs font-semibold bg-slate-50 border border-slate-300 rounded p-1.5 focus:outline-none"
        >
          <option value="All">Todas as Áreas</option>
          {#each areasList as a}
            <option value={a}>{a}</option>
          {/each}
        </select>

        <select
          value={selectedExam}
          onchange={(e) => { selectedExam = (e.target as HTMLSelectElement).value; currentPairIndex = 0; }}
          class="text-xs font-mono bg-slate-50 border border-slate-300 rounded p-1.5 focus:outline-none"
        >
          <option value="All">Todos os Exames</option>
          {#each examsList as ex}
            <option value={ex}>{ex}</option>
          {/each}
        </select>

        <div class="flex items-center space-x-1 font-mono text-xs">
          <button
            onclick={prevPair}
            class="bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 px-2 py-1.5 rounded transition"
            title="Par Anterior"
          >
            <ChevronLeft size={14} />
          </button>
          <span class="font-bold text-slate-700 px-2">
            {filteredPairs.length > 0 ? currentPairIndex + 1 : 0} / {filteredPairs.length}
          </span>
          <button
            onclick={nextPair}
            class="bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 px-2 py-1.5 rounded transition"
            title="Próximo Par"
          >
            <ChevronRight size={14} />
          </button>
        </div>
      </div>
    </div>
  </div>

  {#if !activePair}
    <div class="lab-card p-12 text-center text-slate-400 font-mono text-xs">
      Nenhum par de variantes gêmeas encontrado com os filtros selecionados.
    </div>
  {:else}
    {@const areaColor = AREA_CONFIG[activePair.area] || { bg: 'bg-slate-50', text: 'text-slate-900', border: 'border-slate-300', badge: 'bg-slate-100' }}

    <!-- Dual Comparison Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <!-- Variant A -->
      <div class="lab-card p-4 space-y-3 border-t-4 border-t-sky-600">
        <div class="flex items-center justify-between pb-2 border-b border-slate-200">
          <div class="flex items-center gap-2">
            <span class="bg-sky-600 text-white font-mono font-bold text-xs px-2 py-0.5 rounded">
              Variante A
            </span>
            <span class="font-mono font-bold text-xs text-slate-900">
              {activePair.qid_a}
            </span>
          </div>
          <button
            onclick={() => onSelectQuestionById(activePair.qid_a)}
            class="text-xs font-mono font-bold text-sky-700 hover:text-sky-900 flex items-center gap-1 hover:underline"
          >
            Treinar esta ➔
          </button>
        </div>

        <div class="bg-white border border-slate-200 rounded p-2 text-center min-h-[220px] flex items-center justify-center">
          <img
            src={activePair.image_a}
            alt={activePair.qid_a}
            class="max-w-full h-auto object-contain max-h-[360px]"
            loading="lazy"
          />
        </div>
      </div>

      <!-- Variant B -->
      <div class="lab-card p-4 space-y-3 border-t-4 border-t-emerald-600">
        <div class="flex items-center justify-between pb-2 border-b border-slate-200">
          <div class="flex items-center gap-2">
            <span class="bg-emerald-600 text-white font-mono font-bold text-xs px-2 py-0.5 rounded">
              Variante B
            </span>
            <span class="font-mono font-bold text-xs text-slate-900">
              {activePair.qid_b}
            </span>
          </div>
          <button
            onclick={() => onSelectQuestionById(activePair.qid_b)}
            class="text-xs font-mono font-bold text-emerald-700 hover:text-emerald-900 flex items-center gap-1 hover:underline"
          >
            Treinar esta ➔
          </button>
        </div>

        <div class="bg-white border border-slate-200 rounded p-2 text-center min-h-[220px] flex items-center justify-center">
          <img
            src={activePair.image_b}
            alt={activePair.qid_b}
            class="max-w-full h-auto object-contain max-h-[360px]"
            loading="lazy"
          />
        </div>
      </div>
    </div>

    <!-- Highlighted Text Diff Box if available -->
    {#if activePair.diff}
      <div class="lab-card p-4 space-y-2">
        <h3 class="text-xs font-mono font-bold text-slate-700 uppercase">
          Análise de Diferenças Textuais e Paramétricas:
        </h3>
        <div class="p-3 bg-slate-50 border border-slate-200 rounded font-mono text-xs text-slate-800 leading-relaxed overflow-x-auto whitespace-pre-wrap">
          {activePair.diff}
        </div>
      </div>
    {/if}
  {/if}
</div>
