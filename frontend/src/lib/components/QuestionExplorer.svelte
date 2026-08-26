<script lang="ts">
  import type { Question, BankData } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import { Search, Shuffle, ChevronUp, ChevronDown, SlidersHorizontal, X } from 'lucide-svelte';

  let {
    bankData,
    selectedQuestion = $bindable<Question | null>(null),
    selectedArea = $bindable<string>('All'),
    onSelectQuestion
  }: {
    bankData: BankData | null;
    selectedQuestion: Question | null;
    selectedArea: string;
    onSelectQuestion: (q: Question) => void;
  } = $props();

  let selectedSubtopic = $state<string>('All');
  let selectedExam = $state<string>('All');
  let selectedStatus = $state<string>('All');
  let searchQuery = $state<string>('');
  let isFilterExpanded = $state<boolean>(false);

  $effect(() => {
    selectedSubtopic = 'All';
  });

  const availableSubtopics = $derived(() => {
    if (!bankData) return [];
    if (selectedArea === 'All') {
      const set = new Set<string>();
      Object.values(bankData.concept_tree).forEach(a => a.subtopics.forEach(s => set.add(s.name)));
      return Array.from(set).sort();
    }
    return bankData.concept_tree[selectedArea]?.subtopics.map(s => s.name) || [];
  });

  const allExams = $derived(
    bankData?.exams.map(e => e.id) || []
  );

  const filteredQuestions = $derived(() => {
    if (!bankData) return [];
    const userQs = profileStore.currentProfileData.questions;
    const query = searchQuery.toLowerCase().trim();

    return bankData.questions.filter(q => {
      if (selectedArea !== 'All' && q.area !== selectedArea) return false;
      if (selectedSubtopic !== 'All' && q.subtopic !== selectedSubtopic) return false;
      if (selectedExam !== 'All' && q.exam_id !== selectedExam) return false;

      const uState = userQs[q.id]?.status || 'unsolved';
      if (selectedStatus !== 'All' && uState !== selectedStatus) return false;

      if (query) {
        const inId = q.id.toLowerCase().includes(query);
        const inTag = q.tag.toLowerCase().includes(query);
        const inSub = q.subtopic.toLowerCase().includes(query);
        const inText = q.text.toLowerCase().includes(query);
        if (!inId && !inTag && !inSub && !inText) return false;
      }

      return true;
    });
  });

  const poolList = $derived(filteredQuestions());

  const poolStats = $derived(() => {
    const userQs = profileStore.currentProfileData.questions;
    const total = poolList.length;
    if (total === 0) return { total: 0, solved: 0, review: 0, failed: 0, pct: 0 };
    const solved = poolList.filter(q => userQs[q.id]?.status === 'solved').length;
    const review = poolList.filter(q => userQs[q.id]?.status === 'review').length;
    const failed = poolList.filter(q => userQs[q.id]?.status === 'failed').length;
    return {
      total,
      solved,
      review,
      failed,
      pct: Math.round((solved / total) * 100)
    };
  });

  export function selectNext() {
    if (poolList.length === 0) return;
    const idx = poolList.findIndex(q => q.id === selectedQuestion?.id);
    if (idx === -1 || idx >= poolList.length - 1) {
      onSelectQuestion(poolList[0]);
    } else {
      onSelectQuestion(poolList[idx + 1]);
    }
  }

  export function selectPrev() {
    if (poolList.length === 0) return;
    const idx = poolList.findIndex(q => q.id === selectedQuestion?.id);
    if (idx <= 0) {
      onSelectQuestion(poolList[poolList.length - 1]);
    } else {
      onSelectQuestion(poolList[idx - 1]);
    }
  }

  export function selectRandom() {
    if (poolList.length === 0) return;
    const rIdx = Math.floor(Math.random() * poolList.length);
    onSelectQuestion(poolList[rIdx]);
  }
</script>

<div class="w-80 lg:w-88 shrink-0 h-full bg-[#FAF8F5] border-r border-[#E8E2D8] flex flex-col select-none">
  <!-- Explorer Header -->
  <div class="p-3.5 border-b border-[#E8E2D8] space-y-3 bg-[#FAF8F5]">
    <!-- Header Title & Counter -->
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <span class="text-xs font-sans font-bold text-slate-800 tracking-tight">
          {selectedArea === 'All' ? 'Todas as Matérias' : selectedArea}
        </span>
        <span class="text-[10px] font-sans font-bold px-2 py-0.5 rounded-full bg-[#EDE7DC] text-slate-700">
          {poolStats().total} Qs
        </span>
      </div>

      <!-- Quick Actions -->
      <div class="flex items-center space-x-1">
        <button
          onclick={selectRandom}
          class="p-1 rounded-lg text-slate-500 hover:text-slate-900 hover:bg-[#EDE7DC] transition"
          title="Questão Aleatória"
        >
          <Shuffle size={14} />
        </button>
        <button
          onclick={selectPrev}
          class="p-1 rounded-lg text-slate-500 hover:text-slate-900 hover:bg-[#EDE7DC] transition"
          title="Anterior (J)"
        >
          <ChevronUp size={15} />
        </button>
        <button
          onclick={selectNext}
          class="p-1 rounded-lg text-slate-500 hover:text-slate-900 hover:bg-[#EDE7DC] transition"
          title="Próxima (K)"
        >
          <ChevronDown size={15} />
        </button>
        <button
          onclick={() => isFilterExpanded = !isFilterExpanded}
          class="p-1 rounded-lg text-slate-500 hover:text-slate-900 hover:bg-[#EDE7DC] transition {isFilterExpanded ? 'bg-[#E5DDCF] text-slate-900' : ''}"
          title="Filtros Específicos"
        >
          <SlidersHorizontal size={14} />
        </button>
      </div>
    </div>

    <!-- Mastery Progress Bar -->
    <div>
      <div class="flex items-center justify-between text-[10px] font-sans font-semibold text-slate-500 mb-1">
        <span>Progresso:</span>
        <span class="text-emerald-700 font-bold">{poolStats().solved}/{poolStats().total} ({poolStats().pct}%)</span>
      </div>
      <div class="w-full bg-[#E8E2D8] rounded-full h-1.5 overflow-hidden flex">
        <div class="bg-emerald-500 h-full rounded-full transition-all" style="width: {poolStats().pct}%"></div>
      </div>
    </div>

    <!-- Search Input -->
    <div class="relative">
      <input
        type="text"
        bind:value={searchQuery}
        placeholder="Buscar termo ou código..."
        class="w-full text-xs bg-white text-slate-800 border border-[#DDD6C8] rounded-lg pl-8 pr-7 py-2 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 font-sans shadow-2xs transition"
      />
      <Search size={13} class="absolute left-2.5 top-2.5 text-slate-400" />
      {#if searchQuery}
        <button
          onclick={() => searchQuery = ''}
          class="absolute right-2.5 top-2.5 text-slate-400 hover:text-slate-700"
        >
          <X size={13} />
        </button>
      {/if}
    </div>

    <!-- Expandable Filter Drawer -->
    {#if isFilterExpanded}
      <div class="pt-2 border-t border-[#E8E2D8] space-y-2 text-xs font-sans">
        <!-- Subtopic -->
        <div>
          <label for="subtopic-select" class="block text-[10px] font-bold text-slate-600 mb-1">Subtópico:</label>
          <select
            id="subtopic-select"
            value={selectedSubtopic}
            onchange={(e) => selectedSubtopic = (e.target as HTMLSelectElement).value}
            class="w-full bg-white border border-[#DDD6C8] rounded-lg p-1.5 text-slate-800 text-[11px] focus:outline-none"
          >
            <option value="All">Todos os Subtópicos</option>
            {#each availableSubtopics() as sub}
              <option value={sub}>{sub}</option>
            {/each}
          </select>
        </div>

        <!-- Exam Edition & Status -->
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label for="exam-select" class="block text-[10px] font-bold text-slate-600 mb-1">Edição:</label>
            <select
              id="exam-select"
              value={selectedExam}
              onchange={(e) => selectedExam = (e.target as HTMLSelectElement).value}
              class="w-full bg-white border border-[#DDD6C8] rounded-lg p-1.5 text-slate-800 text-[11px] focus:outline-none"
            >
              <option value="All">Todos ({allExams.length})</option>
              {#each allExams as ex}
                <option value={ex}>{ex}</option>
              {/each}
            </select>
          </div>

          <div>
            <label for="status-select" class="block text-[10px] font-bold text-slate-600 mb-1">Estado:</label>
            <select
              id="status-select"
              value={selectedStatus}
              onchange={(e) => selectedStatus = (e.target as HTMLSelectElement).value}
              class="w-full bg-white border border-[#DDD6C8] rounded-lg p-1.5 text-slate-800 text-[11px] focus:outline-none"
            >
              <option value="All">Todos</option>
              <option value="unsolved">⏳ Pendentes</option>
              <option value="solved">✅ Dominadas</option>
              <option value="review">📌 Revisão</option>
              <option value="failed">❌ Erros</option>
            </select>
          </div>
        </div>
      </div>
    {/if}
  </div>

  <!-- Questions Feed List -->
  <div class="flex-1 overflow-y-auto custom-scrollbar divide-y divide-[#EFE9DF]">
    {#if poolList.length === 0}
      <div class="p-8 text-center text-slate-400 font-sans text-xs">
        Nenhuma questão encontrada com estes filtros.
      </div>
    {:else}
      {#each poolList as q (q.id)}
        {@const uState = profileStore.getQuestionState(q.id)}
        {@const isSelected = selectedQuestion?.id === q.id}
        {@const theme = AREA_THEMES[q.area]}

        <button
          onclick={() => onSelectQuestion(q)}
          class="w-full text-left px-3.5 py-3 transition flex items-start space-x-3 group cursor-pointer {isSelected ? 'bg-white shadow-xs border-l-3 border-sky-600' : 'hover:bg-[#F4EFE6]'}"
        >
          <!-- Status Dot -->
          <div class="pt-1 shrink-0">
            <div class="w-2 h-2 rounded-full {uState.status === 'solved' ? 'led-solved' : uState.status === 'review' ? 'led-review' : uState.status === 'failed' ? 'led-failed' : 'led-unsolved'}"></div>
          </div>

          <!-- Question Meta -->
          <div class="min-w-0 flex-1">
            <div class="flex items-center justify-between gap-1 mb-0.5">
              <span class="font-sans font-bold text-xs tracking-tight {isSelected ? 'text-sky-900 font-extrabold' : 'text-slate-800'}">
                {q.id}
              </span>
              <span class="text-[9px] font-mono px-1.5 py-0.5 rounded border uppercase shrink-0 font-semibold {theme?.badge || 'bg-slate-100 text-slate-700'}">
                {theme?.code.toUpperCase() || 'FIS'}
              </span>
            </div>

            <div class="text-[11px] text-slate-500 truncate font-sans">
              {q.subtopic}
            </div>

            {#if q.flag}
              <div class="mt-1 text-[9px] font-sans text-amber-700 flex items-center gap-1 font-semibold">
                <span>⚠️ Errata/Aviso</span>
              </div>
            {/if}
          </div>
        </button>
      {/each}
    {/if}
  </div>
</div>
