<script lang="ts">
  import { onMount } from 'svelte';
  import type { BankData, Question } from './lib/types';
  import { profileStore } from './lib/storage.svelte';
  import SidebarRail from './lib/components/SidebarRail.svelte';
  import QuestionExplorer from './lib/components/QuestionExplorer.svelte';
  import ProblemCanvas from './lib/components/ProblemCanvas.svelte';
  import InspectorTray from './lib/components/InspectorTray.svelte';
  import TwinLabView from './lib/components/TwinLabView.svelte';
  import TaxonomyMapView from './lib/components/TaxonomyMapView.svelte';
  import FormulaSheet from './lib/components/FormulaSheet.svelte';
  import KeyboardHelpModal from './lib/components/KeyboardHelpModal.svelte';

  let bankData = $state<BankData | null>(null);
  let activeTab = $state<'practice' | 'twins' | 'concept' | 'formula'>('practice');
  let selectedAreaFilter = $state<string>('All');
  let selectedQuestion = $state<Question | null>(null);
  let isHelpOpen = $state(false);
  let isLoading = $state(true);
  let loadError = $state<string | null>(null);

  // References to child components
  let explorerComponent = $state<any>(null);
  let canvasComponent = $state<any>(null);
  let inspectorComponent = $state<any>(null);

  onMount(async () => {
    try {
      const res = await fetch('/questions.json');
      if (!res.ok) {
        throw new Error(`Falha ao carregar banco de dados estático (HTTP ${res.status})`);
      }
      const data: BankData = await res.json();
      bankData = data;
      if (data.questions && data.questions.length > 0) {
        selectedQuestion = data.questions[0];
      }
    } catch (e: any) {
      console.error(e);
      loadError = e.message || 'Erro ao carregar questions.json';
    } finally {
      isLoading = false;
    }

    // Register global keyboard shortcuts
    window.addEventListener('keydown', handleGlobalKeydown);
    return () => {
      window.removeEventListener('keydown', handleGlobalKeydown);
    };
  });

  function handleGlobalKeydown(e: KeyboardEvent) {
    const tag = (e.target as HTMLElement)?.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') {
      return;
    }

    const key = e.key.toLowerCase();

    if (key === 'k' || e.key === 'ArrowDown') {
      e.preventDefault();
      explorerComponent?.selectNext();
    } else if (key === 'j' || e.key === 'ArrowUp') {
      e.preventDefault();
      explorerComponent?.selectPrev();
    } else if (key === 's') {
      e.preventDefault();
      if (selectedQuestion) {
        profileStore.updateQuestionStatus(selectedQuestion.id, 'solved');
      }
    } else if (key === 'r') {
      e.preventDefault();
      if (selectedQuestion) {
        profileStore.updateQuestionStatus(selectedQuestion.id, 'review');
      }
    } else if (key === 'x') {
      e.preventDefault();
      if (selectedQuestion) {
        profileStore.updateQuestionStatus(selectedQuestion.id, 'failed');
      }
    } else if (key === 'z') {
      e.preventDefault();
      canvasComponent?.triggerZoom();
    } else if (key === 't') {
      e.preventDefault();
      if (selectedQuestion?.twin_id) {
        jumpToTwin(selectedQuestion.twin_id);
      }
    } else if (['1', '2', '3', '4'].includes(key)) {
      e.preventDefault();
      inspectorComponent?.toggleClueByLevel(parseInt(key, 10));
    } else if (key === 'p') {
      e.preventDefault();
      activeTab = 'practice';
    } else if (key === 'm') {
      e.preventDefault();
      activeTab = 'concept';
    } else if (key === 'f') {
      e.preventDefault();
      activeTab = 'formula';
    } else if (key === '?') {
      e.preventDefault();
      isHelpOpen = !isHelpOpen;
    } else if (e.key === 'Escape') {
      isHelpOpen = false;
    }
  }

  function handleSelectQuestion(q: Question) {
    selectedQuestion = q;
  }

  function jumpToTwin(twinId: string) {
    if (!bankData) return;
    const target = bankData.questions.find(q => q.id === twinId);
    if (target) {
      selectedQuestion = target;
      activeTab = 'practice';
    }
  }

  function handleFilterBySubtopic(area: string, subtopic: string) {
    selectedAreaFilter = area;
    activeTab = 'practice';
  }
</script>

<div class="h-screen w-screen overflow-hidden flex flex-row bg-[#FBF9F5] text-slate-800 antialiased font-sans">
  <!-- 1. Left Narrow Tool & Area Rail (64px) -->
  <SidebarRail
    {bankData}
    bind:activeTab
    bind:selectedAreaFilter
    onOpenHelp={() => isHelpOpen = true}
  />

  <!-- 2. Main Workspace Dynamic Layout -->
  {#if isLoading}
    <div class="flex-1 h-full flex flex-col items-center justify-center space-y-3 font-sans text-xs text-slate-500 bg-study-grid">
      <div class="w-9 h-9 border-3 border-sky-500 border-t-transparent rounded-full animate-spin"></div>
      <div class="font-medium tracking-wide">Carregando banco de questões de física...</div>
    </div>
  {:else if loadError}
    <div class="flex-1 h-full flex flex-col items-center justify-center p-8 text-center font-sans text-xs text-rose-800 bg-study-grid">
      <div class="p-6 rounded-2xl bg-white border border-[#E5DFD4] shadow-sm max-w-md space-y-2">
        <div class="font-bold text-sm text-rose-700">⚠️ Erro ao carregar banco:</div>
        <div>{loadError}</div>
        <div class="text-[11px] text-slate-500 mt-2">Execute <code class="text-slate-800 bg-slate-100 px-1.5 py-0.5 rounded font-mono">python bank/exporter.py</code> para exportar os dados.</div>
      </div>
    </div>
  {:else}
    {#if activeTab === 'practice'}
      <!-- 3-Pane Deliberate Practice Cockpit (Explorer + Master Canvas + Inspector) -->
      <div class="flex-1 h-full flex flex-row overflow-hidden">
        <!-- Pane 1: Question Explorer (Index & Filters) -->
        <QuestionExplorer
          bind:this={explorerComponent}
          {bankData}
          {selectedQuestion}
          bind:selectedArea={selectedAreaFilter}
          onSelectQuestion={handleSelectQuestion}
        />

        <!-- Pane 2: Expansive Problem Canvas -->
        <ProblemCanvas
          bind:this={canvasComponent}
          question={selectedQuestion}
          onJumpToTwin={jumpToTwin}
        />

        <!-- Pane 3: Tabbed Socratic Inspector & Scratchpad -->
        <InspectorTray
          bind:this={inspectorComponent}
          question={selectedQuestion}
          {bankData}
          onJumpToTwin={jumpToTwin}
        />
      </div>
    {:else if activeTab === 'twins'}
      <!-- Dedicated Full-Screen Twin Laboratory -->
      <TwinLabView
        pairs={bankData?.pairs || []}
        onSelectQuestionById={jumpToTwin}
      />
    {:else if activeTab === 'concept'}
      <!-- Dedicated Knowledge Taxonomy & Mastery Map -->
      <TaxonomyMapView
        {bankData}
        onFilterBySubtopic={handleFilterBySubtopic}
      />
    {:else if activeTab === 'formula'}
      <!-- Dedicated Official EUF Formula Sheet -->
      <FormulaSheet />
    {/if}
  {/if}

  <!-- Keyboard Shortcuts Modal -->
  <KeyboardHelpModal bind:isOpen={isHelpOpen} />
</div>
