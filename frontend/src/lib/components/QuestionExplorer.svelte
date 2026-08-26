<script lang="ts">
  import type { Question, BankData } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import { Search, Shuffle, ChevronUp, ChevronDown, CheckCircle2, Bookmark, XCircle, Clock, SlidersHorizontal, X } from 'lucide-svelte';

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

  // When selectedArea changes from outside (e.g. Sidebar rail), reset subtopic
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

<div class="w-80 lg:w-88 shrink-0 h-full bg-[#0a0f1d] border-r border-white/8 flex flex-col select-none">
  <!-- Explorer Header -->
  <div class="p-3 border-b border-white/8 space-y-2.5 bg-[#090e1a]">
    <!-- Header Title & Pool Counter -->
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <span class="text-xs font-mono font-bold text-white tracking-wider uppercase">
          {selectedArea === 'All' ? 'Todas as Áreas' : selectedArea}
        </span>
        <span class="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-white/10 text-slate-300">
          {poolStats().total}
        </span>
      </div>

      <!-- Quick Actions -->
      <div class="flex items-center space-x-1">
        <button
          onclick={selectRandom}
          class="p-1 rounded text-slate-400 hover:text-white hover:bg-white/5 transition"
          title="Questão Aleatória"
        >
          <Shuffle size={13} />
        </button>
        <button
          onclick={selectPrev}
          class="p-1 rounded text-slate-400 hover:text-white hover:bg-white/5 transition flex items-center"
          title="Anterior (J)"
        >
          <ChevronUp size={14} />
        </button>
        <button
          onclick={selectNext}
          class="p-1 rounded text-slate-400 hover:text-white hover:bg-white/5 transition flex items-center"
          title="Próxima (K)"
        >
          <ChevronDown size={14} />
        </button>
        <button
          onclick={() => isFilterExpanded = !isFilterExpanded}
          class="p-1 rounded text-slate-400 hover:text-white hover:bg-white/5 transition {isFilterExpanded ? 'bg-sky-500/20 text-sky-400' : ''}"
          title="Filtros Avançados"
        >
          <SlidersHorizontal size={13} />
        </button>
      </div>
    </div>

    <!-- Live Pool Progress Bar -->
    <div>
      <div class="flex items-center justify-between text-[10px] font-mono text-slate-400 mb-1">
        <span>Domínio do Pool:</span>
        <span class="font-bold text-emerald-400">{poolStats().solved}/{poolStats().total} ({poolStats().pct}%)</span>
      </div>
      <div class="w-full bg-slate-800 rounded-full h-1 overflow-hidden flex">
        <div class="bg-emerald-500 h-full" style="width: {poolStats().pct}%"></div>
        <div class="bg-amber-500 h-full" style="width: {poolStats().total > 0 ? (poolStats().review / poolStats().total) * 100 : 0}%"></div>
        <div class="bg-rose-500 h-full" style="width: {poolStats().total > 0 ? (poolStats().failed / poolStats().total) * 100 : 0}%"></div>
      </div>
    </div>

    <!-- Search Input -->
    <div class="relative">
      <input
        type="text"
        bind:value={searchQuery}
        placeholder="Buscar termo ou tag..."
        class="w-full text-xs bg-slate-950/80 text-slate-200 border border-white/10 rounded px-7 py-1.5 placeholder-slate-500 focus:outline-none focus:border-sky-500 font-mono transition"
      />
      <Search size={12} class="absolute left-2.5 top-2.5 text-slate-500" />
      {#if searchQuery}
        <button
          onclick={() => searchQuery = ''}
          class="absolute right-2 top-2 text-slate-400 hover:text-white"
        >
          <X size={12} />
        </button>
      {/if}
    </div>

    <!-- Expandable Filter Drawer -->
    {#if isFilterExpanded}
      <div class="pt-2 border-t border-white/5 space-y-2 text-xs font-mono">
        <!-- Subtopic -->
        <div>
          <label for="explorer-subtopic-select" class="block text-[9px] uppercase font-bold text-slate-500 mb-0.5">Subtópico:</label>
          <select
            id="explorer-subtopic-select"
            value={selectedSubtopic}
            onchange={(e) => selectedSubtopic = (e.target as HTMLSelectElement).value}
            class="w-full bg-slate-950 border border-white/10 rounded p-1 text-slate-300 text-[11px] focus:outline-none"
          >
            <option value="All">Todos os Subtópicos</option>
            {#each availableSubtopics() as sub}
              <option value={sub}>{sub}</option>
            {/each}
          </select>
        </div>

        <!-- Exam Edition & Status in 2 cols -->
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label for="explorer-exam-select" class="block text-[9px] uppercase font-bold text-slate-500 mb-0.5">Exame:</label>
            <select
              id="explorer-exam-select"
              value={selectedExam}
              onchange={(e) => selectedExam = (e.target as HTMLSelectElement).value}
              class="w-full bg-slate-950 border border-white/10 rounded p-1 text-slate-300 text-[11px] focus:outline-none"
            >
              <option value="All">Todos ({allExams.length})</option>
              {#each allExams as ex}
                <option value={ex}>{ex}</option>
              {/each}
            </select>
          </div>

          <div>
            <label for="explorer-status-select" class="block text-[9px] uppercase font-bold text-slate-500 mb-0.5">Estado:</label>
            <select
              id="explorer-status-select"
              value={selectedStatus}
              onchange={(e) => selectedStatus = (e.target as HTMLSelectElement).value}
              class="w-full bg-slate-950 border border-white/10 rounded p-1 text-slate-300 text-[11px] focus:outline-none"
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

  <!-- Questions Feed -->
  <div class="flex-1 overflow-y-auto custom-scrollbar divide-y divide-white/4">
    {#if poolList.length === 0}
      <div class="p-8 text-center text-slate-500 font-mono text-xs">
        Nenhuma questão encontrada.
      </div>
    {:else}
      {#each poolList as q (q.id)}
        {@const uState = profileStore.getQuestionState(q.id)}
        {@const isSelected = selectedQuestion?.id === q.id}
        {@const theme = AREA_THEMES[q.area]}

        <button
          onclick={() => onSelectQuestion(q)}
          class="w-full text-left px-3 py-2.5 transition flex items-start space-x-2.5 group cursor-pointer {isSelected ? 'bg-sky-500/15 border-l-2 border-sky-400 text-white' : 'hover:bg-white/4 text-slate-300'}"
        >
          <!-- Status LED Pin -->
          <div class="pt-1 shrink-0">
            <div class="w-2 h-2 rounded-full {uState.status === 'solved' ? 'led-solved' : uState.status === 'review' ? 'led-review' : uState.status === 'failed' ? 'led-failed' : 'led-unsolved'}"></div>
          </div>

          <!-- Question Content snippet -->
          <div class="min-w-0 flex-1">
            <div class="flex items-center justify-between gap-1 mb-0.5">
              <span class="font-mono font-bold text-xs tracking-tight {isSelected ? 'text-sky-300' : 'text-slate-200'}">
                {q.id}
              </span>
              <span
                class="text-[9px] font-mono px-1 rounded border uppercase shrink-0"
                style={theme ? `color: ${theme.accentHex}; border-color: ${theme.accentHex}40; background-color: ${theme.accentHex}15;` : ''}
              >
                {theme?.code.toUpperCase() || 'FIS'}
              </span>
            </div>

            <div class="text-[11px] text-slate-400 truncate font-sans">
              {q.subtopic}
            </div>

            {#if q.flag}
              <div class="mt-1 text-[9px] font-mono text-amber-400 flex items-center gap-1">
                <span>⚠️ Errata/Aviso</span>
              </div>
            {/if}
          </div>
        </button>
      {/each}
    {/if}
  </div>
</div>
