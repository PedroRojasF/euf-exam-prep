<script lang="ts">
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import type { BankData } from '../types';
  import { 
    Layers, Split, LayoutGrid, FileText, 
    HelpCircle, User, Download, Upload, UserPlus, Compass
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

<aside class="w-16 shrink-0 bg-[#F4EFE6] border-r border-[#E6DFD3] flex flex-col items-center justify-between py-4 z-30 select-none shadow-xs">
  <!-- Top Logo & View Modes -->
  <div class="flex flex-col items-center space-y-4 w-full">
    <!-- Brand Avatar / Logo -->
    <button
      onclick={() => { activeTab = 'practice'; selectedAreaFilter = 'All'; }}
      class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-400 via-indigo-400 to-rose-300 flex items-center justify-center font-serif font-bold text-base text-white shadow-sm hover:scale-105 transition cursor-pointer"
      title="EUF Exam Master — Início"
    >
      Ψ
    </button>

    <div class="w-8 h-px bg-[#E2D9CB]"></div>

    <!-- Navigation View Mode Buttons -->
    <div class="flex flex-col items-center space-y-2 w-full px-2">
      <!-- Cockpit -->
      <button
        onclick={() => activeTab = 'practice'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition {activeTab === 'practice' ? 'bg-white text-sky-800 shadow-sm border border-[#E0D8CA]' : 'text-slate-500 hover:text-slate-800 hover:bg-[#EAE4D8]'}"
        title="Modo Estudo / Prática (P)"
      >
        <Layers size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">Estudo</span>
      </button>

      <!-- Twin Lab -->
      <button
        onclick={() => activeTab = 'twins'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition {activeTab === 'twins' ? 'bg-white text-emerald-800 shadow-sm border border-[#E0D8CA]' : 'text-slate-500 hover:text-slate-800 hover:bg-[#EAE4D8]'}"
        title="Gêmeas A/B (T)"
      >
        <Split size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">Gêmeas</span>
      </button>

      <!-- Taxonomy Map -->
      <button
        onclick={() => activeTab = 'concept'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition {activeTab === 'concept' ? 'bg-white text-indigo-800 shadow-sm border border-[#E0D8CA]' : 'text-slate-500 hover:text-slate-800 hover:bg-[#EAE4D8]'}"
        title="Mapa de Tópicos (M)"
      >
        <LayoutGrid size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">Mapa</span>
      </button>

      <!-- Formulas -->
      <button
        onclick={() => activeTab = 'formula'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition {activeTab === 'formula' ? 'bg-white text-amber-800 shadow-sm border border-[#E0D8CA]' : 'text-slate-500 hover:text-slate-800 hover:bg-[#EAE4D8]'}"
        title="Formulário Oficial (F)"
      >
        <FileText size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">Fórmulas</span>
      </button>
    </div>

    <div class="w-8 h-px bg-[#E2D9CB]"></div>

    <!-- Quick Area Filters Pill Rail -->
    <div class="flex flex-col items-center space-y-1.5 w-full px-2">
      <button
        onclick={() => { activeTab = 'practice'; selectedAreaFilter = 'All'; }}
        class="w-10 h-7 rounded-lg text-[10px] font-mono font-bold flex items-center justify-center transition {selectedAreaFilter === 'All' && activeTab === 'practice' ? 'bg-slate-800 text-white shadow-xs' : 'text-slate-600 hover:bg-[#EAE4D8]'}"
        title="Todas as Áreas"
      >
        ALL
      </button>

      {#each Object.entries(AREA_THEMES) as [areaName, theme]}
        <button
          onclick={() => { activeTab = 'practice'; selectedAreaFilter = areaName; }}
          class="w-10 h-7 rounded-lg text-[10px] font-mono font-bold flex items-center justify-center transition border {selectedAreaFilter === areaName && activeTab === 'practice' ? `${theme.badge} shadow-xs font-extrabold ring-1 ring-slate-400` : 'border-transparent text-slate-600 hover:bg-[#EAE4D8]'}"
          title={theme.name}
        >
          {theme.code.toUpperCase()}
        </button>
      {/each}
    </div>
  </div>

  <!-- Bottom User Profile & Shortcuts Help -->
  <div class="flex flex-col items-center space-y-2 relative">
    <!-- Profile Button -->
    <div class="relative">
      <button
        onclick={() => isProfileMenuOpen = !isProfileMenuOpen}
        class="w-10 h-10 rounded-full bg-white border border-[#DDD6C8] flex items-center justify-center text-slate-700 hover:text-slate-900 shadow-xs hover:scale-105 transition cursor-pointer"
        title={`Perfil Ativo: ${profileStore.activeProfileName} (${totalSolved} resolvidas)`}
      >
        <User size={17} />
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

        <!-- Menu Popover Card -->
        <div class="absolute bottom-0 left-14 z-50 w-60 bg-white border border-[#DDD6C8] rounded-xl shadow-xl p-3 space-y-2.5 text-xs font-sans">
          <div class="text-[10px] text-slate-500 uppercase font-bold px-1 flex items-center justify-between">
            <span>Perfil de Estudo</span>
            <span class="text-emerald-700 font-semibold">{totalSolved} Dominadas</span>
          </div>

          <select
            class="w-full bg-[#FAF8F5] border border-[#DDD6C8] rounded-lg p-2 text-slate-800 text-xs font-semibold focus:outline-none"
            value={profileStore.activeProfileName}
            onchange={(e) => { profileStore.switchProfile((e.target as HTMLSelectElement).value); isProfileMenuOpen = false; }}
          >
            {#each profileStore.profilesList as p}
              <option value={p}>{p}</option>
            {/each}
          </select>

          <div class="grid grid-cols-2 gap-1.5 pt-1 border-t border-slate-100">
            <button
              onclick={handleCreateProfile}
              class="p-2 bg-[#FAF8F5] hover:bg-[#F2ECE0] text-slate-700 rounded-lg flex items-center justify-center gap-1 text-[11px] font-medium transition"
            >
              <UserPlus size={12} />
              <span>Novo</span>
            </button>
            <button
              onclick={handleExportProfile}
              class="p-2 bg-[#FAF8F5] hover:bg-[#F2ECE0] text-slate-700 rounded-lg flex items-center justify-center gap-1 text-[11px] font-medium transition"
            >
              <Download size={12} />
              <span>Exportar</span>
            </button>
          </div>

          <label class="block p-2 bg-[#FAF8F5] hover:bg-[#F2ECE0] text-slate-700 rounded-lg text-center text-[11px] font-medium cursor-pointer transition">
            <span class="flex items-center justify-center gap-1">
              <Upload size={12} />
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
      class="w-8 h-8 rounded-lg text-slate-500 hover:text-slate-800 hover:bg-[#EAE4D8] flex items-center justify-center transition"
      title="Atalhos de Teclado (?)"
    >
      <HelpCircle size={17} />
    </button>
  </div>
</aside>
