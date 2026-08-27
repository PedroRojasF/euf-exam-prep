<script lang="ts">
  import type { BankData } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_CONFIG } from '../constants';
  import { LayoutGrid, CheckCircle2, ChevronRight } from 'lucide-svelte';

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

<div class="space-y-4">
  <div class="lab-card p-4 space-y-1">
    <h2 class="text-sm font-bold text-slate-900 font-mono flex items-center gap-2">
      <LayoutGrid size={16} class="text-sky-600" />
      Taxonomia Oficial e Mapa de Conhecimento EUF
    </h2>
    <p class="text-xs text-slate-500 font-sans">
      Acompanhe o domínio percentual por área da física e clique em qualquer subtópico para focar seus estudos nele.
    </p>
  </div>

  {#if !bankData}
    <div class="lab-card p-12 text-center text-slate-400 font-mono text-xs">
      Carregando taxonomia de física...
    </div>
  {:else}
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {#each Object.entries(bankData.concept_tree) as [area, info]}
        {@const areaStats = getAreaStats(area)}
        {@const areaColor = AREA_CONFIG[area] || { bg: 'bg-slate-50', text: 'text-slate-900', border: 'border-slate-300', badge: 'bg-slate-100' }}

        <div class="lab-card p-4 space-y-3 flex flex-col justify-between">
          <div>
            <!-- Area Header -->
            <div class="flex items-center justify-between pb-2 border-b border-slate-200">
              <span class="text-xs font-mono font-bold px-2 py-0.5 rounded border {areaColor.badge}">
                {area}
              </span>
              <span class="text-xs font-mono font-bold text-slate-700">
                {areaStats.solved} / {areaStats.total} ({areaStats.pct}%)
              </span>
            </div>

            <!-- Master Progress Bar -->
            <div class="w-full bg-slate-200 rounded-full h-1.5 mt-2">
              <div
                class="bg-emerald-500 h-1.5 rounded-full transition-all duration-300"
                style="width: {areaStats.pct}%"
              ></div>
            </div>

            <!-- Subtopics List -->
            <div class="space-y-1 mt-3 max-h-[300px] overflow-y-auto custom-scrollbar pr-1">
              {#each info.subtopics as sub}
                {@const sStats = getSubtopicStats(sub.name)}
                <button
                  onclick={() => onFilterBySubtopic(area, sub.name)}
                  class="w-full text-left p-1.5 rounded text-xs flex items-center justify-between hover:bg-slate-50 transition border border-transparent hover:border-slate-200 group"
                >
                  <div class="min-w-0 pr-2">
                    <div class="font-medium text-slate-800 truncate text-[11px] group-hover:text-sky-700">
                      {sub.name}
                    </div>
                  </div>
                  <div class="shrink-0 flex items-center space-x-1 font-mono text-[10px]">
                    <span class={sStats.pct === 100 ? 'text-emerald-600 font-bold' : 'text-slate-500'}>
                      {sStats.solved}/{sStats.total}
                    </span>
                    <ChevronRight size={12} class="text-slate-400 group-hover:text-sky-600" />
                  </div>
                </button>
              {/each}
            </div>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>
