<script lang="ts">
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import type { BankData } from '../types';
  import { 
    Orbit, Zap, Atom, Flame, BarChart2, Radio, 
    Layers, Split, LayoutGrid, FileText, 
    HelpCircle, User, Download, Upload, UserPlus, Sparkles
  } from 'lucide-svelte';

  let {
    bankData,
    activeTab = $bindable<'practice' | 'twins' | 'concept' | 'formula'>('practice'),
    selectedAreaFilter = $bindable<string>('All'),
    onOpenHelp
  }: {
    bankData: BankData | null;
    activeTab: 'practice' | 'twins' | 'concept' | 'formula';
    selectedAreaFilter: string;
    onOpenHelp: () => void;
  } = $props();

  let isProfileMenuOpen = $state(false);

  function handleCreateProfile() {
    const name = prompt('Nome do novo perfil de estudo (ex: candidato_usp):');
    if (name && name.trim()) {
      profileStore.createProfile(name.trim());
      isProfileMenuOpen = false;
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
    isProfileMenuOpen = false;
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
          isProfileMenuOpen = false;
        } catch {
          alert('❌ Erro ao importar arquivo JSON.');
        }
      };
      reader.readAsText(input.files[0]);
    }
  }

  const userQs = $derived(profileStore.currentProfileData.questions);
  const totalSolved = $derived(
    Object.values(userQs).filter(q => q.status === 'solved').length
  );
</script>

<aside class="w-14 shrink-0 bg-[#060911] border-r border-white/8 flex flex-col items-center justify-between py-3 z-30 select-none">
  <!-- Top Logo & View Modes -->
  <div class="flex flex-col items-center space-y-4 w-full">
    <!-- Brand Stamp -->
    <button
      onclick={() => { activeTab = 'practice'; selectedAreaFilter = 'All'; }}
      class="w-9 h-9 rounded-md bg-linear-to-br from-sky-500 to-indigo-600 flex items-center justify-center font-mono font-bold text-xs text-white shadow-[0_0_15px_-3px_rgba(56,189,248,0.5)] cursor-pointer hover:scale-105 transition"
      title="EUF Exam Master"
    >
      Ψ
    </button>

    <div class="w-7 h-px bg-white/10"></div>

    <!-- Navigation Modes -->
    <div class="flex flex-col items-center space-y-1.5 w-full px-2">
      <!-- Cockpit View -->
      <button
        onclick={() => activeTab = 'practice'}
        class="w-10 h-10 rounded-md flex flex-col items-center justify-center transition {activeTab === 'practice' ? 'bg-sky-500/20 text-sky-400 border border-sky-500/40 shadow-[0_0_10px_rgba(56,189,248,0.2)]' : 'text-slate-400 hover:text-slate-200 hover:bg-white/5'}"
        title="1. Cockpit de Prática (P)"
      >
        <Layers size={17} />
        <span class="text-[8px] font-mono mt-0.5 font-semibold">TREINO</span>
      </button>

      <!-- Twin Lab View -->
      <button
        onclick={() => activeTab = 'twins'}
        class="w-10 h-10 rounded-md flex flex-col items-center justify-center transition {activeTab === 'twins' ? 'bg-sky-500/20 text-sky-400 border border-sky-500/40 shadow-[0_0_10px_rgba(56,189,248,0.2)]' : 'text-slate-400 hover:text-slate-200 hover:bg-white/5'}"
        title="2. Laboratório de Gêmeas A/B (T)"
      >
        <Split size={17} />
        <span class="text-[8px] font-mono mt-0.5 font-semibold">GÊMEAS</span>
      </button>

      <!-- Taxonomy Map View -->
      <button
        onclick={() => activeTab = 'concept'}
        class="w-10 h-10 rounded-md flex flex-col items-center justify-center transition {activeTab === 'concept' ? 'bg-sky-500/20 text-sky-400 border border-sky-500/40 shadow-[0_0_10px_rgba(56,189,248,0.2)]' : 'text-slate-400 hover:text-slate-200 hover:bg-white/5'}"
        title="3. Mapa de Domínio & Áreas (M)"
      >
        <LayoutGrid size={17} />
        <span class="text-[8px] font-mono mt-0.5 font-semibold">MAPA</span>
      </button>

      <!-- Formula Sheet View -->
      <button
        onclick={() => activeTab = 'formula'}
        class="w-10 h-10 rounded-md flex flex-col items-center justify-center transition {activeTab === 'formula' ? 'bg-sky-500/20 text-sky-400 border border-sky-500/40 shadow-[0_0_10px_rgba(56,189,248,0.2)]' : 'text-slate-400 hover:text-slate-200 hover:bg-white/5'}"
        title="4. Formulário Oficial (F)"
      >
        <FileText size={17} />
        <span class="text-[8px] font-mono mt-0.5 font-semibold">FORM</span>
      </button>
    </div>

    <div class="w-7 h-px bg-white/10"></div>

    <!-- Quick Area Filters Rail -->
    <div class="flex flex-col items-center space-y-1 w-full px-2">
      <button
        onclick={() => { activeTab = 'practice'; selectedAreaFilter = 'All'; }}
        class="w-9 h-7 rounded text-[10px] font-mono font-bold flex items-center justify-center transition {selectedAreaFilter === 'All' && activeTab === 'practice' ? 'bg-white text-slate-950 font-extrabold' : 'text-slate-400 hover:text-white hover:bg-white/5'}"
        title="Todas as 6 Áreas"
      >
        ALL
      </button>

      {#each Object.entries(AREA_THEMES) as [areaName, theme]}
        <button
          onclick={() => { activeTab = 'practice'; selectedAreaFilter = areaName; }}
          class="w-9 h-7 rounded text-[10px] font-mono font-bold flex items-center justify-center transition border {selectedAreaFilter === areaName && activeTab === 'practice' ? `${theme.badge} shadow-xs` : 'border-transparent text-slate-400 hover:text-slate-200 hover:bg-white/5'}"
          title={theme.name}
          style={selectedAreaFilter === areaName && activeTab === 'practice' ? `border-color: ${theme.accentHex}` : ''}
        >
          <span style={`color: ${theme.accentHex}`}>{theme.code.toUpperCase()}</span>
        </button>
      {/each}
    </div>
  </div>

  <!-- Bottom Profile & Help Trigger -->
  <div class="flex flex-col items-center space-y-2 relative">
    <!-- Profile Button & Popover -->
    <div class="relative">
      <button
        onclick={() => isProfileMenuOpen = !isProfileMenuOpen}
        class="w-9 h-9 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-slate-300 hover:text-white hover:border-slate-500 transition cursor-pointer"
        title={`Perfil Ativo: ${profileStore.activeProfileName} (${totalSolved} dominadas)`}
      >
        <User size={15} />
      </button>

      {#if isProfileMenuOpen}
        <!-- Backdrop -->
        <button
          type="button"
          tabindex="-1"
          aria-label="Fechar menu"
          class="fixed inset-0 z-40 bg-transparent border-0 cursor-default p-0 m-0 w-full h-full"
          onclick={() => isProfileMenuOpen = false}
          onkeydown={(e) => { if (e.key === 'Escape') isProfileMenuOpen = false; }}
        ></button>

        <!-- Menu Popover -->
        <div class="absolute bottom-0 left-12 z-50 w-56 bg-slate-900 border border-slate-700 rounded-lg shadow-2xl p-2.5 space-y-2 text-xs font-mono">
          <div class="text-[10px] text-slate-400 uppercase font-bold px-1 flex items-center justify-between">
            <span>Perfil de Estudo</span>
            <span class="text-emerald-400">{totalSolved} Dominadas</span>
          </div>

          <select
            class="w-full bg-slate-950 border border-slate-700 rounded p-1 text-slate-200 text-xs focus:outline-none"
            value={profileStore.activeProfileName}
            onchange={(e) => { profileStore.switchProfile((e.target as HTMLSelectElement).value); isProfileMenuOpen = false; }}
          >
            {#each profileStore.profilesList as p}
              <option value={p}>{p}</option>
            {/each}
          </select>

          <div class="grid grid-cols-2 gap-1 pt-1 border-t border-slate-800">
            <button
              onclick={handleCreateProfile}
              class="p-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded flex items-center justify-center gap-1 text-[11px] transition"
            >
              <UserPlus size={11} />
              <span>Novo</span>
            </button>
            <button
              onclick={handleExportProfile}
              class="p-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded flex items-center justify-center gap-1 text-[11px] transition"
            >
              <Download size={11} />
              <span>Exportar</span>
            </button>
          </div>

          <label class="block p-1.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded text-center text-[11px] cursor-pointer transition">
            <span class="flex items-center justify-center gap-1">
              <Upload size={11} />
              <span>Importar Perfil (.json)</span>
            </span>
            <input type="file" accept=".json" onchange={handleImportProfile} class="hidden" />
          </label>
        </div>
      {/if}
    </div>

    <!-- Help (?) Modal Button -->
    <button
      onclick={onOpenHelp}
      class="w-8 h-8 rounded text-slate-500 hover:text-slate-300 hover:bg-white/5 flex items-center justify-center transition"
      title="Atalhos de Teclado Científicos (?)"
    >
      <HelpCircle size={15} />
    </button>
  </div>
</aside>
