<script lang="ts">
  import type { Question, BankData, QuestionStatus } from '../types';
  import { profileStore } from '../storage.svelte';
  import { AREA_CONFIG } from '../constants';
  import { Search, Shuffle, ChevronLeft, ChevronRight, Filter } from 'lucide-svelte';

  let {
    bankData,
    selectedQuestion = $bindable<Question | null>(null),
    onSelectQuestion
  }: {
    bankData: BankData | null;
    selectedQuestion: Question | null;
    onSelectQuestion: (q: Question) => void;
  } = $props();

  let selectedArea = $state<string>('All');
  let selectedSubtopic = $state<string>('All');
  let selectedExam = $state<string>('All');
  let selectedStatus = $state<string>('All');
  let searchQuery = $state<string>('');

  // Extract unique lists
  const allAreas = $derived(
    bankData ? Object.keys(bankData.concept_tree) : []
  );

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

  // When area changes, reset subtopic if not valid
  function onAreaChange(e: Event) {
    const val = (e.target as HTMLSelectElement).value;
    selectedArea = val;
    selectedSubtopic = 'All';
  }

  // Filter questions
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

  // Mastery percentage in current pool
  const poolMastery = $derived(() => {
    if (poolList.length === 0) return 0;
    const userQs = profileStore.currentProfileData.questions;
    const solved = poolList.filter(q => userQs[q.id]?.status === 'solved').length;
    return Math.round((solved / poolList.length) * 100);
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

<div class="space-y-3">
  <!-- Filter Console Card -->
  <div class="lab-card p-3.5 space-y-3">
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
      <!-- 1. Area Selector -->
      <div>
        <label for="filter-area-select" class="block text-[10px] font-mono font-bold text-slate-600 uppercase mb-1">
          1. Matéria / Área
        </label>
        <select
          id="filter-area-select"
          value={selectedArea}
          onchange={onAreaChange}
          class="w-full text-xs font-semibold bg-slate-50 border border-slate-300 rounded p-1.5 focus:ring-1 focus:ring-slate-700 focus:outline-none transition cursor-pointer"
        >
          <option value="All">Todas as 6 Áreas</option>
          {#each allAreas as area}
            <option value={area}>{area}</option>
          {/each}
        </select>
      </div>

      <!-- 2. Subtopic Selector -->
      <div>
        <label for="filter-subtopic-select" class="block text-[10px] font-mono font-bold text-slate-600 uppercase mb-1">
          2. Subtópico
        </label>
        <select
          id="filter-subtopic-select"
          value={selectedSubtopic}
          onchange={(e) => selectedSubtopic = (e.target as HTMLSelectElement).value}
          class="w-full text-xs font-semibold bg-slate-50 border border-slate-300 rounded p-1.5 focus:ring-1 focus:ring-slate-700 focus:outline-none transition cursor-pointer"
        >
          <option value="All">Todos os Subtópicos</option>
          {#each availableSubtopics() as sub}
            <option value={sub}>{sub}</option>
          {/each}
        </select>
      </div>

      <!-- 3. Exam Edition -->
      <div>
        <label for="filter-exam-select" class="block text-[10px] font-mono font-bold text-slate-600 uppercase mb-1">
          3. Edição do Exame
        </label>
        <select
          id="filter-exam-select"
          value={selectedExam}
          onchange={(e) => selectedExam = (e.target as HTMLSelectElement).value}
          class="w-full text-xs font-mono bg-slate-50 border border-slate-300 rounded p-1.5 focus:ring-1 focus:ring-slate-700 focus:outline-none transition cursor-pointer"
        >
          <option value="All">Todos os Exames ({allExams.length})</option>
          {#each allExams as ex}
            <option value={ex}>{ex}</option>
          {/each}
        </select>
      </div>

      <!-- 4. Status Selector -->
      <div>
        <label for="filter-status-select" class="block text-[10px] font-mono font-bold text-slate-600 uppercase mb-1">
          4. Estado de Estudo
        </label>
        <select
          id="filter-status-select"
          value={selectedStatus}
          onchange={(e) => selectedStatus = (e.target as HTMLSelectElement).value}
          class="w-full text-xs font-semibold bg-slate-50 border border-slate-300 rounded p-1.5 focus:ring-1 focus:ring-slate-700 focus:outline-none transition cursor-pointer"
        >
          <option value="All">Todos os Estados</option>
          <option value="unsolved">⏳ Não Resolvidas</option>
          <option value="solved">✅ Dominadas (Solved)</option>
          <option value="review">📌 Para Revisão (Review)</option>
          <option value="failed">❌ A Repetir (Failed)</option>
        </select>
      </div>
    </div>

    <!-- Search Bar & Instant Actions -->
    <div class="flex flex-wrap items-center justify-between gap-2.5 pt-2.5 border-t border-slate-200">
      <div class="flex-1 min-w-[220px] relative">
        <input
          type="text"
          bind:value={searchQuery}
          placeholder="Buscar termo físico (e.g. Hamiltoniano, Poynting, Dirac, Rydberg, Carnot, Gauss)..."
          class="w-full text-xs bg-slate-50 border border-slate-300 rounded pl-8 pr-3 py-1.5 focus:ring-1 focus:ring-slate-700 focus:outline-none transition"
        />
        <Search size={14} class="absolute left-2.5 top-2 text-slate-400" />
      </div>

      <div class="flex items-center space-x-1.5 font-mono text-xs">
        <button
          onclick={selectRandom}
          title="Escolher questão aleatória"
          class="font-bold bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 px-2.5 py-1.5 rounded transition flex items-center gap-1 shadow-2xs"
        >
          <Shuffle size={13} />
          Aleatória
        </button>

        <button
          onclick={selectPrev}
          title="Questão Anterior (Atalho: J ou ↑)"
          class="font-bold bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 px-2 py-1.5 rounded transition flex items-center gap-1"
        >
          <ChevronLeft size={14} />
          <span class="key-cap text-[8px]">J</span>
        </button>

        <button
          onclick={selectNext}
          title="Próxima Questão (Atalho: K ou ↓)"
          class="font-bold bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 px-2 py-1.5 rounded transition flex items-center gap-1"
        >
          <span class="key-cap text-[8px]">K</span>
          <ChevronRight size={14} />
        </button>
      </div>
    </div>
  </div>

  <!-- Questions List Panel -->
  <div class="lab-card p-3 flex flex-col h-[680px]">
    <div class="flex items-center justify-between pb-2 border-b border-slate-200 mb-2">
      <div>
        <span class="text-[11px] font-mono font-bold text-slate-700 uppercase">
          Questões ({poolList.length})
        </span>
        <div class="text-[10px] text-slate-400 font-mono">
          Navegue com <span class="key-cap text-[8px]">J</span> / <span class="key-cap text-[8px]">K</span>
        </div>
      </div>
      <span class="text-xs font-mono font-bold px-2 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-300">
        {poolMastery()}% Dominado
      </span>
    </div>

    <div class="flex-1 overflow-y-auto custom-scrollbar space-y-1 pr-1">
      {#if poolList.length === 0}
        <div class="text-center py-12 text-slate-400 text-xs font-mono">
          Nenhuma questão encontrada com os filtros selecionados.
        </div>
      {:else}
        {#each poolList as q (q.id)}
          {@const uState = profileStore.getQuestionState(q.id)}
          {@const isSelected = selectedQuestion?.id === q.id}
          {@const areaColor = AREA_CONFIG[q.area] || { bg: 'bg-slate-50', text: 'text-slate-800', border: 'border-slate-200', badge: 'bg-slate-100' }}

          <button
            onclick={() => onSelectQuestion(q)}
            class="w-full text-left p-2 rounded text-xs transition border flex items-center justify-between gap-2 {isSelected ? 'bg-sky-50 border-sky-600 shadow-xs' : 'bg-white hover:bg-slate-50 border-slate-200'}"
          >
            <div class="flex items-center space-x-2 min-w-0">
              <!-- Status Indicator Dot -->
              <span class="w-2 h-2 rounded-full shrink-0 {uState.status === 'solved' ? 'bg-emerald-500 ring-2 ring-emerald-200' : uState.status === 'review' ? 'bg-amber-500 ring-2 ring-amber-200' : uState.status === 'failed' ? 'bg-rose-500 ring-2 ring-rose-200' : 'bg-slate-300'}"></span>

              <div class="truncate">
                <div class="font-mono font-bold text-slate-900 flex items-center gap-1.5">
                  <span>{q.id}</span>
                  {#if q.flag}
                    <span class="text-[9px] font-sans px-1 rounded bg-amber-100 text-amber-800 border border-amber-300">
                      aviso
                    </span>
                  {/if}
                </div>
                <div class="text-[11px] text-slate-500 truncate font-sans">
                  {q.subtopic}
                </div>
              </div>
            </div>

            <!-- Area Badge -->
            <span class="shrink-0 text-[10px] font-mono font-semibold px-1.5 py-0.5 rounded border {areaColor.badge}">
              {q.area.split(' ')[0]}
            </span>
          </button>
        {/each}
      {/if}
    </div>
  </div>
</div>
