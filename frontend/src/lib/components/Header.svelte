<script lang="ts">
  import { profileStore } from '../storage.svelte';
  import type { BankData } from '../types';
  import { Play, Pause, RotateCcw, HelpCircle, FileText, Split, LayoutGrid, BookOpen, Download, Upload, UserPlus } from 'lucide-svelte';

  let {
    bankData,
    activeTab = $bindable<'practice' | 'twins' | 'concept' | 'formula'>('practice'),
    onOpenHelp
  }: {
    bankData: BankData | null;
    activeTab: 'practice' | 'twins' | 'concept' | 'formula';
    onOpenHelp: () => void;
  } = $props();

  // Timer State
  let timerSeconds = $state(15 * 60);
  let isTimerRunning = $state(false);
  let timerInterval: any = null;

  function toggleTimer() {
    if (isTimerRunning) {
      clearInterval(timerInterval);
      isTimerRunning = false;
    } else {
      isTimerRunning = true;
      timerInterval = setInterval(() => {
        if (timerSeconds > 0) {
          timerSeconds--;
        } else {
          clearInterval(timerInterval);
          isTimerRunning = false;
          alert('⏱️ Tempo limite de 15 minutos atingido!');
        }
      }, 1000);
    }
  }

  function resetTimer() {
    clearInterval(timerInterval);
    isTimerRunning = false;
    timerSeconds = 15 * 60;
  }

  function formatTime(secs: number): string {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  // Reactive Stats
  const totalQuestions = $derived(bankData?.questions.length || 0);
  const userQuestions = $derived(profileStore.currentProfileData.questions);
  
  const solvedCount = $derived(
    Object.values(userQuestions).filter(q => q.status === 'solved').length
  );
  const reviewCount = $derived(
    Object.values(userQuestions).filter(q => q.status === 'review').length
  );
  const failedCount = $derived(
    Object.values(userQuestions).filter(q => q.status === 'failed').length
  );
  const masteryPercentage = $derived(
    totalQuestions > 0 ? ((solvedCount / totalQuestions) * 100).toFixed(1) : '0.0'
  );

  function handleCreateProfile() {
    const name = prompt('Digite o nome do novo perfil (ex: candidato_usp):');
    if (name && name.trim()) {
      profileStore.createProfile(name.trim());
    }
  }

  function handleExportProfile() {
    const json = profileStore.exportProfileAsJSON();
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `euf_perfil_${profileStore.activeProfileName}.json`;
    a.click();
    URL.revokeObjectURL(url);
  }

  function handleImportProfile(e: Event) {
    const input = e.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      const reader = new FileReader();
      reader.onload = (ev) => {
        try {
          const content = ev.target?.result as string;
          profileStore.importProfileFromJSON(content);
          alert('✅ Perfil importado com sucesso!');
        } catch {
          alert('❌ Erro ao importar arquivo JSON de perfil.');
        }
      };
      reader.readAsText(input.files[0]);
    }
  }
</script>

<header class="bg-white border-b border-slate-200 sticky top-0 z-40 shadow-xs">
  <div class="max-w-7xl mx-auto px-4 sm:px-6">
    <!-- Top Bar -->
    <div class="flex flex-wrap items-center justify-between py-3 gap-3">
      <!-- Title & Branding -->
      <div class="flex items-center space-x-3">
        <div class="bg-slate-900 text-white font-mono font-bold text-xs px-2.5 py-1.5 rounded shadow-inner">
          EUF
        </div>
        <div>
          <h1 class="text-sm font-bold text-slate-900 tracking-tight flex items-center gap-2">
            Exam Master
            <span class="text-[10px] font-mono font-normal bg-sky-50 text-sky-700 border border-sky-200 px-1.5 py-0.5 rounded">
              2010–2026
            </span>
          </h1>
          <p class="text-[11px] text-slate-500 font-mono">Exame Unificado de Pós-Graduação em Física</p>
        </div>
      </div>

      <!-- Live Metrics Strip -->
      <div class="hidden md:flex items-center space-x-5 text-xs font-mono bg-slate-50 border border-slate-200 px-3.5 py-1.5 rounded-md">
        <div class="flex items-center space-x-1.5">
          <span class="text-slate-400 uppercase text-[10px]">Banco:</span>
          <span class="font-bold text-slate-900">{totalQuestions} Qs</span>
        </div>
        <div class="h-3 w-px bg-slate-300"></div>
        <div class="flex items-center space-x-1.5">
          <span class="text-slate-400 uppercase text-[10px]">Dominadas:</span>
          <span class="font-bold text-emerald-600">{solvedCount} ({masteryPercentage}%)</span>
        </div>
        <div class="h-3 w-px bg-slate-300"></div>
        <div class="flex items-center space-x-1.5">
          <span class="text-slate-400 uppercase text-[10px]">Revisão:</span>
          <span class="font-bold text-amber-600">{reviewCount}</span>
        </div>
        <div class="h-3 w-px bg-slate-300"></div>
        <div class="flex items-center space-x-1.5">
          <span class="text-slate-400 uppercase text-[10px]">A Repetir:</span>
          <span class="font-bold text-rose-600">{failedCount}</span>
        </div>
      </div>

      <!-- Controls: Profile + Stopwatch + Help -->
      <div class="flex items-center space-x-3">
        <!-- Profile Manager -->
        <div class="flex items-center space-x-1 bg-slate-100 border border-slate-200 rounded px-2 py-1 text-xs">
          <span class="text-[10px] font-mono text-slate-500 uppercase">Perfil:</span>
          <select
            class="bg-transparent font-mono text-xs font-semibold text-slate-800 focus:outline-none cursor-pointer"
            value={profileStore.activeProfileName}
            onchange={(e) => profileStore.switchProfile((e.target as HTMLSelectElement).value)}
          >
            {#each profileStore.profilesList as p}
              <option value={p}>{p}</option>
            {/each}
          </select>
          <button
            onclick={handleCreateProfile}
            title="Criar novo perfil"
            class="text-slate-500 hover:text-slate-800 p-0.5 rounded hover:bg-slate-200 transition"
          >
            <UserPlus size={13} />
          </button>
          <button
            onclick={handleExportProfile}
            title="Exportar perfil (JSON)"
            class="text-slate-500 hover:text-slate-800 p-0.5 rounded hover:bg-slate-200 transition"
          >
            <Download size={13} />
          </button>
          <label
            title="Importar perfil (JSON)"
            class="text-slate-500 hover:text-slate-800 p-0.5 rounded hover:bg-slate-200 transition cursor-pointer"
          >
            <Upload size={13} />
            <input type="file" accept=".json" onchange={handleImportProfile} class="hidden" />
          </label>
        </div>

        <!-- 15-Minute Scientific Stopwatch -->
        <div class="flex items-center space-x-1.5 bg-slate-900 text-white px-2.5 py-1 rounded shadow-xs">
          <span class="font-mono font-bold text-xs text-sky-400 w-12 text-center">
            {formatTime(timerSeconds)}
          </span>
          <button
            onclick={toggleTimer}
            class="p-0.5 hover:text-sky-300 transition"
            title={isTimerRunning ? 'Pausar temporizador' : 'Iniciar temporizador'}
          >
            {#if isTimerRunning}
              <Pause size={13} />
            {:else}
              <Play size={13} />
            {/if}
          </button>
          <button
            onclick={resetTimer}
            class="p-0.5 hover:text-sky-300 transition text-slate-400"
            title="Reiniciar para 15 minutos"
          >
            <RotateCcw size={12} />
          </button>
        </div>

        <!-- Hotkeys Help Button -->
        <button
          onclick={onOpenHelp}
          title="Atalhos de teclado (?)"
          class="text-slate-500 hover:text-slate-800 p-1.5 rounded-md hover:bg-slate-100 transition border border-slate-200"
        >
          <HelpCircle size={16} />
        </button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="flex space-x-1 border-t border-slate-200 pt-1">
      <button
        onclick={() => activeTab = 'practice'}
        class="flex items-center gap-1.5 px-3 py-2 text-xs font-mono font-bold border-b-2 transition {activeTab === 'practice' ? 'border-sky-600 text-sky-700 bg-sky-50/50' : 'border-transparent text-slate-600 hover:text-slate-900'}"
      >
        <BookOpen size={14} />
        1. Cockpit de Prática
      </button>

      <button
        onclick={() => activeTab = 'twins'}
        class="flex items-center gap-1.5 px-3 py-2 text-xs font-mono font-bold border-b-2 transition {activeTab === 'twins' ? 'border-sky-600 text-sky-700 bg-sky-50/50' : 'border-transparent text-slate-600 hover:text-slate-900'}"
      >
        <Split size={14} />
        2. Laboratório Gêmeas A/B
        {#if bankData?.pairs}
          <span class="text-[10px] bg-slate-200 text-slate-700 px-1.5 rounded-full">
            {bankData.pairs.length}
          </span>
        {/if}
      </button>

      <button
        onclick={() => activeTab = 'concept'}
        class="flex items-center gap-1.5 px-3 py-2 text-xs font-mono font-bold border-b-2 transition {activeTab === 'concept' ? 'border-sky-600 text-sky-700 bg-sky-50/50' : 'border-transparent text-slate-600 hover:text-slate-900'}"
      >
        <LayoutGrid size={14} />
        3. Taxonomia & Mapa
      </button>

      <button
        onclick={() => activeTab = 'formula'}
        class="flex items-center gap-1.5 px-3 py-2 text-xs font-mono font-bold border-b-2 transition {activeTab === 'formula' ? 'border-sky-600 text-sky-700 bg-sky-50/50' : 'border-transparent text-slate-600 hover:text-slate-900'}"
      >
        <FileText size={14} />
        4. Formulário Oficial
      </button>
    </div>
  </div>
</header>
