<script lang="ts">
  import type { BankData } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import { LayoutGrid, ChevronRight } from 'lucide-svelte';

  let {
    bankData,
    onFilterBySubtopic
  }: {
    bankData: BankData | null;
    onFilterBySubtopic: (area: string, subtopic: string) => void;
  } = $props();

  const userQs = $derived(profileStore.currentProfileData.questions);

  function getSubtopicStats(subName: string) {
    if (!bankData) return { total: 0, solved: 0, pct: 0 };
    const qs = bankData.questions.filter(q => q.subtopic === subName);
    const solved = qs.filter(q => userQs[q.id]?.status === 'solved').length;
    return {
      total: qs.length,
      solved,
      pct: qs.length > 0 ? Math.round((solved / qs.length) * 100) : 0
    };
  }

  function getAreaStats(areaName: string) {
    if (!bankData) return { total: 0, solved: 0, pct: 0 };
    const qs = bankData.questions.filter(q => q.area === areaName);
    const solved = qs.filter(q => userQs[q.id]?.status === 'solved').length;
    return {
      total: qs.length,
      solved,
      pct: qs.length > 0 ? Math.round((solved / qs.length) * 100) : 0
    };
  }
</script>

<div class="flex-1 h-full flex flex-col bg-[#FDFBF7] dark:bg-[#080d16] overflow-hidden transition-colors duration-200">
  <!-- Map Header -->
  <div class="px-6 py-3 bg-white dark:bg-[#0c121e] border-b border-[#E8E2D8] dark:border-white/10 flex items-center justify-between shrink-0 select-none shadow-2xs">
    <div class="flex items-center space-x-3">
      <div class="p-2 rounded-xl bg-[#f5f3ff] dark:bg-indigo-950 text-[#5b21b6] dark:text-indigo-300 border border-[#ddd6fe] dark:border-indigo-800">
        <LayoutGrid size={17} />
      </div>
      <div>
        <h2 class="text-sm font-bold text-slate-900 dark:text-white font-sans flex items-center gap-2">
          {profileStore.t('taxonomyTitle')}
        </h2>
        <p class="text-[11px] text-slate-500 dark:text-slate-400 font-sans">
          {profileStore.t('taxonomySubtitle')}
        </p>
      </div>
    </div>
  </div>

  <!-- Content Grid -->
  {#if !bankData}
    <div class="flex-1 flex items-center justify-center text-slate-400 dark:text-slate-500 font-sans text-xs">
      {profileStore.t('loadingMap')}
    </div>
  {:else}
    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 bg-study-grid">
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
        {#each Object.entries(bankData.concept_tree) as [area, info]}
          {@const aStats = getAreaStats(area)}
          {@const theme = AREA_THEMES[area]}

          <div class="rounded-2xl bg-white dark:bg-slate-900 border border-[#E5DFD4] dark:border-slate-800 p-5 flex flex-col justify-between space-y-4 shadow-xs">
            <div>
              <!-- Area Header -->
              <div class="flex items-center justify-between pb-3 border-b border-[#E8E2D8] dark:border-slate-800">
                <span class="px-2.5 py-1 rounded-lg text-xs font-sans font-bold border {theme?.badge || 'bg-slate-100 text-slate-800'}">
                  {profileStore.tArea(area)}
                </span>
                <span class="font-sans text-xs font-bold text-slate-700 dark:text-slate-200">
                  {aStats.solved} / {aStats.total} <span class="text-slate-500 dark:text-slate-400 font-normal">({aStats.pct}%)</span>
                </span>
              </div>

              <!-- Mastery Bar -->
              <div class="w-full bg-[#EAE4D8] dark:bg-slate-800 rounded-full h-2 mt-3 overflow-hidden">
                <div
                  class="h-full rounded-full transition-all duration-300"
                  style="width: {aStats.pct}%; background-color: {theme?.accentHex || '#0284c7'};"
                ></div>
              </div>

              <!-- Subtopics List -->
              <div class="space-y-1 mt-4 max-h-[360px] overflow-y-auto custom-scrollbar pr-1 divide-y divide-[#EFE9DF] dark:divide-white/5">
                {#each info.subtopics as sub}
                  {@const sStats = getSubtopicStats(sub.name)}
                  <button
                    onclick={() => onFilterBySubtopic(area, sub.name)}
                    class="w-full text-left py-2.5 px-2 rounded-lg flex items-center justify-between hover:bg-[#FAF8F5] dark:hover:bg-slate-800 transition group cursor-pointer"
                  >
                    <div class="min-w-0 pr-2">
                      <div class="text-xs text-slate-700 dark:text-slate-300 font-medium truncate group-hover:text-sky-800 dark:group-hover:text-sky-300 font-sans">
                        {profileStore.tSubtopic(sub.name)}
                      </div>
                    </div>
                    <div class="shrink-0 flex items-center space-x-1.5 font-mono text-[10px]">
                      <span class={sStats.pct === 100 ? 'text-emerald-700 dark:text-emerald-400 font-bold' : 'text-slate-500 dark:text-slate-400'}>
                        {sStats.solved}/{sStats.total}
                      </span>
                      <ChevronRight size={13} class="text-slate-400 group-hover:text-sky-700 dark:group-hover:text-sky-300" />
                    </div>
                  </button>
                {/each}
              </div>
            </div>
          </div>
        {/each}
      </div>
    </div>
  {/if}
</div>
