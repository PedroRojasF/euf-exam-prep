<script lang="ts">
  import type { BankData } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import { LayoutGrid, ChevronRight, CheckCircle2, Award, Zap } from 'lucide-svelte';

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

<div class="flex-1 h-full flex flex-col bg-[#0b101d] overflow-hidden">
  <!-- Map Header -->
  <div class="px-6 py-3 bg-[#080d18] border-b border-white/8 flex items-center justify-between shrink-0 select-none">
    <div class="flex items-center space-x-3">
      <div class="p-1.5 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30">
        <LayoutGrid size={16} />
      </div>
      <div>
        <h2 class="text-sm font-bold text-white font-mono flex items-center gap-2">
          Taxonomia Oficial e Mapa de Conhecimento EUF
        </h2>
        <p class="text-[11px] text-slate-500 font-mono">
          Matriz de proficiência por área da física e subtópicos da pós-graduação.
        </p>
      </div>
    </div>
  </div>

  <!-- Content Grid -->
  {#if !bankData}
    <div class="flex-1 flex items-center justify-center text-slate-500 font-mono text-xs">
      Carregando mapa de conhecimento...
    </div>
  {:else}
    <div class="flex-1 overflow-y-auto custom-scrollbar p-6 bg-tech-grid">
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
        {#each Object.entries(bankData.concept_tree) as [area, info]}
          {@const aStats = getAreaStats(area)}
          {@const theme = AREA_THEMES[area]}

          <div class="rounded-lg bg-[#0e1526] border border-white/8 p-4 flex flex-col justify-between space-y-4 shadow-xl">
            <div>
              <!-- Area Header -->
              <div class="flex items-center justify-between pb-2.5 border-b border-white/8">
                <span
                  class="px-2.5 py-0.5 rounded text-xs font-mono font-bold border"
                  style={theme ? `color: ${theme.accentHex}; border-color: ${theme.accentHex}40; background-color: ${theme.accentHex}15;` : ''}
                >
                  {area}
                </span>
                <span class="font-mono text-xs font-bold text-slate-200">
                  {aStats.solved} / {aStats.total} <span class="text-slate-400 font-normal">({aStats.pct}%)</span>
                </span>
              </div>

              <!-- Mastery Bar -->
              <div class="w-full bg-slate-900 rounded-full h-1.5 mt-2.5 overflow-hidden">
                <div
                  class="h-full rounded-full transition-all duration-300"
                  style="width: {aStats.pct}%; background-color: {theme?.accentHex || '#38bdf8'};"
                ></div>
              </div>

              <!-- Subtopics List -->
              <div class="space-y-1 mt-4 max-h-[360px] overflow-y-auto custom-scrollbar pr-1 divide-y divide-white/4">
                {#each info.subtopics as sub}
                  {@const sStats = getSubtopicStats(sub.name)}
                  <button
                    onclick={() => onFilterBySubtopic(area, sub.name)}
                    class="w-full text-left py-2 px-1.5 rounded flex items-center justify-between hover:bg-white/5 transition group cursor-pointer"
                  >
                    <div class="min-w-0 pr-2">
                      <div class="text-xs text-slate-300 font-medium truncate group-hover:text-sky-300 font-sans">
                        {sub.name}
                      </div>
                    </div>
                    <div class="shrink-0 flex items-center space-x-1.5 font-mono text-[10px]">
                      <span class={sStats.pct === 100 ? 'text-emerald-400 font-bold' : 'text-slate-500'}>
                        {sStats.solved}/{sStats.total}
                      </span>
                      <ChevronRight size={12} class="text-slate-500 group-hover:text-sky-400" />
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
