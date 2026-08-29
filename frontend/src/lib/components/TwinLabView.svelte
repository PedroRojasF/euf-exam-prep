<script lang="ts">
  import type { TwinPair } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import { renderMathInString } from '../math';
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

<div class="flex-1 h-full flex flex-col bg-[#FDFBF7] dark:bg-[#080d16] overflow-hidden transition-colors duration-200">
  <!-- Twin Lab Command Bar -->
  <div class="px-6 py-3 bg-white dark:bg-[#0c121e] border-b border-[#E8E2D8] dark:border-white/10 flex flex-wrap items-center justify-between gap-3 shrink-0 select-none shadow-2xs">
    <div class="flex items-center space-x-3">
      <div class="p-2 rounded-xl bg-[#eff8ff] dark:bg-sky-950 text-[#0369a1] dark:text-sky-300 border border-[#bae6fd] dark:border-sky-800">
        <Split size={17} />
      </div>
      <div>
        <h2 class="text-sm font-bold text-slate-900 dark:text-white font-sans flex items-center gap-2">
          {profileStore.t('twinLabTitle')}
          <span class="text-xs font-semibold text-slate-500 dark:text-slate-400">
            [{filteredPairs.length} {profileStore.t('twinPairsCataloged')}]
          </span>
        </h2>
        <p class="text-[11px] text-slate-500 dark:text-slate-400 font-sans">
          {profileStore.t('twinLabSubtitle')}
        </p>
      </div>
    </div>

    <!-- Filters & Nav Controls -->
    <div class="flex items-center space-x-2 font-sans text-xs">
      <select
        value={selectedArea}
        onchange={(e) => { selectedArea = (e.target as HTMLSelectElement).value; currentPairIndex = 0; }}
        class="bg-[#FAF8F5] dark:bg-slate-800 text-slate-800 dark:text-slate-200 border border-[#DDD6C8] dark:border-slate-700 rounded-lg px-3 py-1.5 focus:outline-none cursor-pointer font-medium"
      >
        <option value="All">{profileStore.t('allAreas')}</option>
        {#each areasList as a}
          <option value={a}>{a}</option>
        {/each}
      </select>

      <select
        value={selectedExam}
        onchange={(e) => { selectedExam = (e.target as HTMLSelectElement).value; currentPairIndex = 0; }}
        class="bg-[#FAF8F5] dark:bg-slate-800 text-slate-800 dark:text-slate-200 border border-[#DDD6C8] dark:border-slate-700 rounded-lg px-3 py-1.5 focus:outline-none cursor-pointer font-medium"
      >
        <option value="All">{profileStore.t('allExams')}</option>
        {#each examsList as ex}
          <option value={ex}>{ex}</option>
        {/each}
      </select>

      <div class="flex items-center space-x-1 pl-2">
        <button
          onclick={prevPair}
          class="p-1.5 rounded-lg bg-[#FAF8F5] dark:bg-slate-800 hover:bg-[#EAE4D8] dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-[#DDD6C8] dark:border-slate-700 transition cursor-pointer"
          title={profileStore.t('prevPair')}
        >
          <ChevronLeft size={15} />
        </button>
        <span class="font-bold text-slate-700 dark:text-slate-200 px-1.5">
          {filteredPairs.length > 0 ? currentPairIndex + 1 : 0}/{filteredPairs.length}
        </span>
        <button
          onclick={nextPair}
          class="p-1.5 rounded-lg bg-[#FAF8F5] dark:bg-slate-800 hover:bg-[#EAE4D8] dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-[#DDD6C8] dark:border-slate-700 transition cursor-pointer"
          title={profileStore.t('nextPair')}
        >
          <ChevronRight size={15} />
        </button>
      </div>
    </div>
  </div>

  <!-- Dual Split Viewport -->
  {#if !activePair}
    <div class="flex-1 flex items-center justify-center text-slate-400 dark:text-slate-500 font-sans text-xs">
      {profileStore.t('noQuestionsFound')}
    </div>
  {:else}
    {@const theme = AREA_THEMES[activePair.area]}

    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 space-y-5 bg-study-grid">
      <!-- Subtopic & Stem Banner -->
      <div class="p-3.5 rounded-xl bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 shadow-xs flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <span class="px-2.5 py-0.5 rounded-lg text-xs font-sans font-bold border {theme?.badge || 'bg-slate-100 text-slate-800'}">
            {profileStore.tArea(activePair.area)}
          </span>
          <span class="text-slate-900 dark:text-white font-sans font-bold text-sm">
            {profileStore.t('stemLabel')}: {activePair.exam_id}-{activePair.stem}
          </span>
          <span class="text-slate-500 dark:text-slate-400 font-sans text-xs">
            {profileStore.t('subtopicLabel')}: <strong class="text-slate-800 dark:text-slate-200">{profileStore.tSubtopic(activePair.subtopic)}</strong>
          </span>
        </div>
      </div>

      <!-- Side-by-Side Dual Problem Cards -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-5">
        <!-- Variant A Column -->
        <div class="bg-white dark:bg-slate-900 border border-[#bae6fd] dark:border-sky-800 rounded-2xl p-5 space-y-3 shadow-sm">
          <div class="flex items-center justify-between pb-3 border-b border-[#E8E2D8] dark:border-slate-800">
            <div class="flex items-center space-x-2">
              <span class="px-2.5 py-0.5 rounded-lg bg-[#eff8ff] dark:bg-sky-950 text-[#0369a1] dark:text-sky-300 border border-[#bae6fd] dark:border-sky-800 font-sans font-bold text-xs">
                {profileStore.t('variantA')}
              </span>
              <span class="font-sans font-bold text-xs text-slate-800 dark:text-slate-200">
                {activePair.qid_a}
              </span>
            </div>
            <button
              onclick={() => onSelectQuestionById(activePair.qid_a)}
              class="text-xs font-sans font-bold text-[#0284c7] dark:text-sky-400 hover:underline flex items-center gap-1 cursor-pointer"
            >
              {profileStore.t('studyInCanvas')} <ArrowUpRight size={13} />
            </button>
          </div>

          <div class="bg-[#FAF8F5] dark:bg-slate-950 rounded-xl p-3 text-center border border-[#E5DFD4] dark:border-slate-800 select-none">
            <img
              src={activePair.image_a}
              alt={activePair.qid_a}
              class="w-full h-auto object-contain max-h-[420px] mx-auto"
              loading="lazy"
            />
          </div>
        </div>

        <!-- Variant B Column -->
        <div class="bg-white dark:bg-slate-900 border border-[#bbf7d0] dark:border-emerald-800 rounded-2xl p-5 space-y-3 shadow-sm">
          <div class="flex items-center justify-between pb-3 border-b border-[#E8E2D8] dark:border-slate-800">
            <div class="flex items-center space-x-2">
              <span class="px-2.5 py-0.5 rounded-lg bg-[#f0fdf4] dark:bg-emerald-950 text-[#166534] dark:text-emerald-300 border border-[#bbf7d0] dark:border-emerald-800 font-sans font-bold text-xs">
                {profileStore.t('variantB')}
              </span>
              <span class="font-sans font-bold text-xs text-slate-800 dark:text-slate-200">
                {activePair.qid_b}
              </span>
            </div>
            <button
              onclick={() => onSelectQuestionById(activePair.qid_b)}
              class="text-xs font-sans font-bold text-[#16a34a] dark:text-emerald-400 hover:underline flex items-center gap-1 cursor-pointer"
            >
              {profileStore.t('studyInCanvas')} <ArrowUpRight size={13} />
            </button>
          </div>

          <div class="bg-[#FAF8F5] dark:bg-slate-950 rounded-xl p-3 text-center border border-[#E5DFD4] dark:border-slate-800 select-none">
            <img
              src={activePair.image_b}
              alt={activePair.qid_b}
              class="w-full h-auto object-contain max-h-[420px] mx-auto"
              loading="lazy"
            />
          </div>
        </div>
      </div>

      <!-- Difference Analysis Banner with Full LaTeX KaTeX Rendering -->
      {#if activePair.diff}
        <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 space-y-3 shadow-2xs">
          <div class="text-xs font-sans font-bold text-slate-800 dark:text-slate-200 flex items-center gap-2">
            <Split size={14} class="text-sky-500" />
            <span>{profileStore.t('variationAnalysis')}</span>
          </div>

          <div class="p-3.5 bg-[#FAF8F5] dark:bg-slate-950 rounded-lg border border-[#E5DDCF] dark:border-slate-800 space-y-2 font-serif text-xs text-slate-700 dark:text-slate-300 leading-relaxed overflow-x-auto">
            {#each activePair.diff.split('\n') as line}
              {#if line.startsWith('  [-]')}
                <div class="p-2.5 rounded-lg bg-rose-50/80 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800/60 text-rose-900 dark:text-rose-200 flex items-start gap-2">
                  <span class="px-1.5 py-0.5 rounded bg-rose-200 dark:bg-rose-900 font-sans font-bold text-[10px] text-rose-800 dark:text-rose-200 shrink-0">A</span>
                  <div class="flex-1 font-serif select-text">{@html renderMathInString(line.replace(/^\s*\[-\]\s*(?:VARIANTE A(?:\s*\(.*?\))?:\s*)?/, ''))}</div>
                </div>
              {:else if line.startsWith('  [+]')}
                <div class="p-2.5 rounded-lg bg-emerald-50/80 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/60 text-emerald-900 dark:text-emerald-200 flex items-start gap-2">
                  <span class="px-1.5 py-0.5 rounded bg-emerald-200 dark:bg-emerald-900 font-sans font-bold text-[10px] text-emerald-800 dark:text-emerald-200 shrink-0">B</span>
                  <div class="flex-1 font-serif select-text">{@html renderMathInString(line.replace(/^\s*\[\+\]\s*(?:VARIANTE B(?:\s*\(.*?\))?:\s*)?/, ''))}</div>
                </div>
              {:else if line.trim().length > 0}
                <div class="py-0.5 px-2 text-slate-600 dark:text-slate-400 font-serif select-text">
                  {@html renderMathInString(line.replace(/^\s*\[=\]\s*/, ''))}
                </div>
              {/if}
            {/each}
          </div>
        </div>
      {/if}
    </div>
  {/if}
</div>
