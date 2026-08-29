<script lang="ts">
  import { profileStore } from '../storage.svelte';
  import { AREA_THEMES } from '../constants';
  import type { BankData } from '../types';
  import type { Language } from '../i18n';
  import { 
    Layers, Split, LayoutGrid, FileText, 
    HelpCircle, User, Download, Upload, UserPlus,
    Sun, Moon, Globe, Clock, Menu, X
  } from 'lucide-svelte';
  import FlagIcon from './FlagIcon.svelte';

  let {
    bankData,
    activeTab = $bindable<'practice' | 'twins' | 'mock' | 'concept' | 'formula'>('practice'),
    selectedAreaFilter = $bindable<string>('All'),
    onOpenHelp
  }: {
    bankData: BankData | null;
    activeTab: 'practice' | 'twins' | 'mock' | 'concept' | 'formula';
    selectedAreaFilter: string;
    onOpenHelp: () => void;
  } = $props();

  let isProfileMenuOpen = $state(false);
  let isLangMenuOpen = $state(false);
  let isMobileMenuOpen = $state(false);

  function handleCreateProfile() {
    const name = prompt(profileStore.t('enterProfileName'));
    if (name && name.trim()) {
      profileStore.createProfile(name.trim());
      isProfileMenuOpen = false;
      isMobileMenuOpen = false;
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
    isMobileMenuOpen = false;
  }

  function handleImportProfile(e: Event) {
    const input = e.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      const reader = new FileReader();
      reader.onload = (ev) => {
        try {
          const content = ev.target?.result as string;
          profileStore.importProfileFromJSON(content);
          alert(profileStore.t('profileImported'));
          isProfileMenuOpen = false;
          isMobileMenuOpen = false;
        } catch {
          alert(profileStore.t('profileImportError'));
        }
      };
      reader.readAsText(input.files[0]);
    }
  }

  const userQs = $derived(profileStore.currentProfileData.questions);
  const totalSolved = $derived(
    Object.values(userQs).filter(q => q.status === 'solved').length
  );

  const langFlags: Record<Language, { label: string; flag: string }> = {
    pt: { label: 'Português', flag: 'BR' },
    es: { label: 'Español', flag: 'ES' },
    en: { label: 'English', flag: 'GB' }
  };
</script>

<!-- ========================================================================= -->
<!-- 1. DESKTOP VERTICAL SIDEBAR RAIL (md:flex) -->
<!-- ========================================================================= -->
<aside class="hidden md:flex w-16 shrink-0 bg-[#F4EFE6] dark:bg-[#070b13] border-r border-[#E6DFD3] dark:border-white/10 flex-col items-center justify-between py-4 z-30 select-none shadow-xs transition-colors duration-200">
  <!-- Top Logo & View Modes -->
  <div class="flex flex-col items-center space-y-4 w-full">
    <!-- Brand Logo Button -->
    <button
      onclick={() => { activeTab = 'practice'; selectedAreaFilter = 'All'; }}
      class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-400 via-indigo-400 to-rose-300 flex items-center justify-center font-serif font-bold text-base text-white shadow-sm hover:scale-105 transition cursor-pointer"
      title={`${profileStore.t('appTitle')} — ${profileStore.t('appSubtitle')}`}
    >
      Ψ
    </button>

    <div class="w-8 h-px bg-[#E2D9CB] dark:bg-white/10"></div>

    <!-- Navigation View Mode Buttons -->
    <div class="flex flex-col items-center space-y-2 w-full px-2">
      <!-- Cockpit -->
      <button
        onclick={() => activeTab = 'practice'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition cursor-pointer {activeTab === 'practice' ? 'bg-white dark:bg-slate-800 text-sky-800 dark:text-sky-300 shadow-sm border border-[#E0D8CA] dark:border-slate-700 font-bold' : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-[#EAE4D8] dark:hover:bg-slate-800/50'}"
        title={`${profileStore.t('modeStudy')} (P)`}
      >
        <Layers size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">{profileStore.t('modeStudy')}</span>
      </button>

      <!-- Twin Lab -->
      <button
        onclick={() => activeTab = 'twins'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition cursor-pointer {activeTab === 'twins' ? 'bg-white dark:bg-slate-800 text-emerald-800 dark:text-emerald-300 shadow-sm border border-[#E0D8CA] dark:border-slate-700 font-bold' : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-[#EAE4D8] dark:hover:bg-slate-800/50'}"
        title={`${profileStore.t('modeTwins')} (T)`}
      >
        <Split size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">{profileStore.t('modeTwins')}</span>
      </button>

      <!-- Mock Exam Simulator -->
      <button
        onclick={() => activeTab = 'mock'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition cursor-pointer {activeTab === 'mock' ? 'bg-white dark:bg-slate-800 text-rose-800 dark:text-rose-300 shadow-sm border border-[#E0D8CA] dark:border-slate-700 font-bold' : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-[#EAE4D8] dark:hover:bg-slate-800/50'}"
        title={`${profileStore.t('modeMock')}`}
      >
        <Clock size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">{profileStore.t('modeMock')}</span>
      </button>

      <!-- Taxonomy Map -->
      <button
        onclick={() => activeTab = 'concept'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition cursor-pointer {activeTab === 'concept' ? 'bg-white dark:bg-slate-800 text-indigo-800 dark:text-indigo-300 shadow-sm border border-[#E0D8CA] dark:border-slate-700 font-bold' : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-[#EAE4D8] dark:hover:bg-slate-800/50'}"
        title={`${profileStore.t('modeMap')} (M)`}
      >
        <LayoutGrid size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">{profileStore.t('modeMap')}</span>
      </button>

      <!-- Formulas -->
      <button
        onclick={() => activeTab = 'formula'}
        class="w-11 h-11 rounded-xl flex flex-col items-center justify-center transition cursor-pointer {activeTab === 'formula' ? 'bg-white dark:bg-slate-800 text-amber-800 dark:text-amber-300 shadow-sm border border-[#E0D8CA] dark:border-slate-700 font-bold' : 'text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-[#EAE4D8] dark:hover:bg-slate-800/50'}"
        title={`${profileStore.t('modeFormulas')} (F)`}
      >
        <FileText size={18} />
        <span class="text-[8px] font-sans font-bold mt-0.5">{profileStore.t('modeFormulas')}</span>
      </button>
    </div>

    <div class="w-8 h-px bg-[#E2D9CB] dark:bg-white/10"></div>

    <!-- Quick Area Filters Pill Rail -->
    <div class="flex flex-col items-center space-y-1.5 w-full px-2">
      <button
        onclick={() => { activeTab = 'practice'; selectedAreaFilter = 'All'; }}
        class="w-10 h-7 rounded-lg text-[10px] font-mono font-bold flex items-center justify-center transition cursor-pointer {selectedAreaFilter === 'All' && activeTab === 'practice' ? 'bg-slate-800 dark:bg-slate-200 text-white dark:text-slate-900 shadow-xs' : 'text-slate-600 dark:text-slate-400 hover:bg-[#EAE4D8] dark:hover:bg-slate-800'}"
        title={profileStore.t('allAreas')}
      >
        ALL
      </button>

      {#each Object.entries(AREA_THEMES) as [areaName, theme]}
        <button
          onclick={() => { activeTab = 'practice'; selectedAreaFilter = areaName; }}
          class="w-10 h-7 rounded-lg text-[10px] font-mono font-bold flex items-center justify-center transition border cursor-pointer {selectedAreaFilter === areaName && activeTab === 'practice' ? `${theme.badge} shadow-xs font-extrabold ring-1 ring-slate-400 dark:ring-white/40` : 'border-transparent text-slate-600 dark:text-slate-400 hover:bg-[#EAE4D8] dark:hover:bg-slate-800'}"
          title={profileStore.tArea(areaName)}
        >
          {theme.code.toUpperCase()}
        </button>
      {/each}
    </div>
  </div>

  <!-- Bottom Utilities: Dark Mode, Language, Profile, Help -->
  <div class="flex flex-col items-center space-y-2.5 relative">
    <!-- Dark / Light Mode Toggle Button -->
    <button
      onclick={() => profileStore.toggleTheme()}
      class="w-9 h-9 rounded-xl bg-white dark:bg-slate-800 border border-[#DDD6C8] dark:border-slate-700 flex items-center justify-center text-slate-700 dark:text-slate-200 hover:text-slate-950 dark:hover:text-white shadow-2xs hover:scale-105 transition cursor-pointer"
      title={profileStore.theme === 'light' ? 'Ativar Modo Escuro' : 'Ativar Modo Claro'}
    >
      {#if profileStore.theme === 'light'}
        <Moon size={16} class="text-indigo-600" />
      {:else}
        <Sun size={16} class="text-amber-400" />
      {/if}
    </button>

    <!-- Language Selector Dropdown -->
    <div class="relative">
      <button
        onclick={() => { isLangMenuOpen = !isLangMenuOpen; isProfileMenuOpen = false; }}
        class="w-9 h-9 rounded-xl bg-white dark:bg-[#2c313a] border border-[#DDD6C8] dark:border-[#3e4451] flex items-center justify-center shadow-2xs hover:scale-105 transition cursor-pointer"
        title="Idioma / Language"
      >
        <FlagIcon lang={profileStore.lang} size={20} />
      </button>

      {#if isLangMenuOpen}
        <button
          type="button"
          tabindex="-1"
          aria-label="Fechar menu de idiomas"
          class="fixed inset-0 z-40 bg-transparent border-0 cursor-default p-0 m-0 w-full h-full"
          onclick={() => isLangMenuOpen = false}
          onkeydown={(e) => { if (e.key === 'Escape') isLangMenuOpen = false; }}
        ></button>

        <div class="absolute bottom-0 left-12 z-50 w-44 bg-white dark:bg-[#21252b] border border-[#DDD6C8] dark:border-[#3e4451] rounded-2xl shadow-xl p-2 space-y-1 text-xs font-sans">
          {#each Object.entries(langFlags) as [code, item]}
            <button
              onclick={() => { profileStore.setLanguage(code as Language); isLangMenuOpen = false; }}
              class="w-full text-left px-3 py-2 rounded-xl flex items-center justify-between transition cursor-pointer {profileStore.lang === code ? 'bg-sky-50 dark:bg-sky-950/80 text-sky-800 dark:text-sky-300 font-bold border border-sky-200 dark:border-sky-800' : 'text-slate-700 dark:text-[#abb2bf] hover:bg-[#FAF8F5] dark:hover:bg-[#2c313a]'}"
            >
              <div class="flex items-center gap-2.5">
                <FlagIcon lang={code} size={18} />
                <span>{item.label}</span>
              </div>
              <span class="text-[10px] font-mono font-bold text-slate-400 dark:text-slate-500 uppercase">{code}</span>
            </button>
          {/each}
        </div>
      {/if}
    </div>

    <!-- Profile Button & Popover -->
    <div class="relative">
      <button
        onclick={() => { isProfileMenuOpen = !isProfileMenuOpen; isLangMenuOpen = false; }}
        class="w-9 h-9 rounded-full bg-white dark:bg-slate-800 border border-[#DDD6C8] dark:border-slate-700 flex items-center justify-center text-slate-700 dark:text-slate-200 shadow-2xs hover:scale-105 transition cursor-pointer"
        title={`${profileStore.t('profile')}: ${profileStore.activeProfileName} (${totalSolved} ${profileStore.t('mastered')})`}
      >
        <User size={16} />
      </button>

      {#if isProfileMenuOpen}
        <button
          type="button"
          tabindex="-1"
          aria-label="Fechar menu de perfil"
          class="fixed inset-0 z-40 bg-transparent border-0 cursor-default p-0 m-0 w-full h-full"
          onclick={() => isProfileMenuOpen = false}
          onkeydown={(e) => { if (e.key === 'Escape') isProfileMenuOpen = false; }}
        ></button>

        <div class="absolute bottom-0 left-12 z-50 w-60 bg-white dark:bg-slate-900 border border-[#DDD6C8] dark:border-slate-700 rounded-xl shadow-xl p-3 space-y-2.5 text-xs font-sans">
          <div class="text-[10px] text-slate-500 dark:text-slate-400 uppercase font-bold px-1 flex items-center justify-between">
            <span>{profileStore.t('profile')}</span>
            <span class="text-emerald-700 dark:text-emerald-400 font-semibold">{totalSolved} {profileStore.t('mastered')}</span>
          </div>

          <select
            class="w-full bg-[#FAF8F5] dark:bg-slate-800 border border-[#DDD6C8] dark:border-slate-700 rounded-lg p-2 text-slate-800 dark:text-slate-200 text-xs font-semibold focus:outline-none cursor-pointer"
            value={profileStore.activeProfileName}
            onchange={(e) => { profileStore.switchProfile((e.target as HTMLSelectElement).value); isProfileMenuOpen = false; }}
          >
            {#each profileStore.profilesList as p}
              <option value={p}>{p}</option>
            {/each}
          </select>

          <div class="grid grid-cols-2 gap-1.5 pt-1 border-t border-slate-100 dark:border-slate-800">
            <button
              onclick={handleCreateProfile}
              class="p-2 bg-[#FAF8F5] dark:bg-slate-800 hover:bg-[#F2ECE0] dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 rounded-lg flex items-center justify-center gap-1 text-[11px] font-medium transition cursor-pointer"
            >
              <UserPlus size={12} />
              <span>{profileStore.t('newProfile')}</span>
            </button>
            <button
              onclick={handleExportProfile}
              class="p-2 bg-[#FAF8F5] dark:bg-slate-800 hover:bg-[#F2ECE0] dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 rounded-lg flex items-center justify-center gap-1 text-[11px] font-medium transition cursor-pointer"
            >
              <Download size={12} />
              <span>{profileStore.t('exportProfile')}</span>
            </button>
          </div>

          <label class="block p-2 bg-[#FAF8F5] dark:bg-slate-800 hover:bg-[#F2ECE0] dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 rounded-lg text-center text-[11px] font-medium cursor-pointer transition">
            <span class="flex items-center justify-center gap-1">
              <Upload size={12} />
              <span>{profileStore.t('importProfile')}</span>
            </span>
            <input type="file" accept=".json" onchange={handleImportProfile} class="hidden" />
          </label>
        </div>
      {/if}
    </div>

    <!-- Help (?) Modal Button -->
    <button
      onclick={onOpenHelp}
      class="w-8 h-8 rounded-lg text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white hover:bg-[#EAE4D8] dark:hover:bg-slate-800 flex items-center justify-center transition cursor-pointer"
      title={`${profileStore.t('shortcutsTitle')} (?)`}
    >
      <HelpCircle size={17} />
    </button>
  </div>
</aside>

<!-- ========================================================================= -->
<!-- 2. MOBILE FIXED BOTTOM NAVIGATION BAR (md:hidden) -->
<!-- ========================================================================= -->
<nav class="flex md:hidden fixed bottom-0 left-0 right-0 z-40 bg-white/95 dark:bg-[#0b101c]/95 backdrop-blur-md border-t border-[#E6DFD3] dark:border-white/10 px-2 py-1.5 items-center justify-around shadow-lg select-none">
  <!-- Study / Explorer Tab -->
  <button
    onclick={() => activeTab = 'practice'}
    class="flex flex-col items-center justify-center py-1 px-3 rounded-xl transition cursor-pointer {activeTab === 'practice' ? 'text-sky-600 dark:text-sky-400 font-bold' : 'text-slate-500 dark:text-slate-400'}"
  >
    <Layers size={19} />
    <span class="text-[9px] font-sans font-bold mt-0.5">{profileStore.t('modeStudy')}</span>
  </button>

  <!-- Twin Lab Tab -->
  <button
    onclick={() => activeTab = 'twins'}
    class="flex flex-col items-center justify-center py-1 px-3 rounded-xl transition cursor-pointer {activeTab === 'twins' ? 'text-emerald-600 dark:text-emerald-400 font-bold' : 'text-slate-500 dark:text-slate-400'}"
  >
    <Split size={19} />
    <span class="text-[9px] font-sans font-bold mt-0.5">{profileStore.t('modeTwins')}</span>
  </button>

  <!-- Mock Exam Tab -->
  <button
    onclick={() => activeTab = 'mock'}
    class="flex flex-col items-center justify-center py-1 px-3 rounded-xl transition cursor-pointer {activeTab === 'mock' ? 'text-rose-600 dark:text-rose-400 font-bold' : 'text-slate-500 dark:text-slate-400'}"
  >
    <Clock size={19} />
    <span class="text-[9px] font-sans font-bold mt-0.5">{profileStore.t('modeMock')}</span>
  </button>

  <!-- Formulas Tab -->
  <button
    onclick={() => activeTab = 'formula'}
    class="flex flex-col items-center justify-center py-1 px-3 rounded-xl transition cursor-pointer {activeTab === 'formula' ? 'text-amber-600 dark:text-amber-400 font-bold' : 'text-slate-500 dark:text-slate-400'}"
  >
    <FileText size={19} />
    <span class="text-[9px] font-sans font-bold mt-0.5">{profileStore.t('modeFormulas')}</span>
  </button>

  <!-- Mobile Settings Toggle Button -->
  <button
    onclick={() => isMobileMenuOpen = !isMobileMenuOpen}
    class="flex flex-col items-center justify-center py-1 px-3 rounded-xl transition cursor-pointer {isMobileMenuOpen ? 'text-indigo-600 dark:text-indigo-400 font-bold' : 'text-slate-500 dark:text-slate-400'}"
  >
    <Menu size={19} />
    <span class="text-[9px] font-sans font-bold mt-0.5">Menu</span>
  </button>
</nav>

<!-- Mobile Settings Modal / Drawer -->
{#if isMobileMenuOpen}
  <button
    type="button"
    tabindex="-1"
    aria-label="Fechar menu móvil"
    class="fixed inset-0 z-50 bg-black/40 backdrop-blur-xs border-0 cursor-default p-0 m-0 w-full h-full md:hidden"
    onclick={() => isMobileMenuOpen = false}
    onkeydown={(e) => { if (e.key === 'Escape') isMobileMenuOpen = false; }}
  ></button>

  <div class="fixed bottom-16 left-3 right-3 z-50 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-2xl p-4 space-y-4 md:hidden font-sans text-xs">
    <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
      <div class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
        <span class="font-serif text-sky-500 font-black">Ψ</span>
        <span>Configurações & Perfil</span>
      </div>
      <button onclick={() => isMobileMenuOpen = false} class="p-1 rounded-lg text-slate-400 hover:text-slate-600">
        <X size={16} />
      </button>
    </div>

    <!-- Theme & Language row -->
    <div class="grid grid-cols-2 gap-2">
      <!-- Dark mode -->
      <button
        onclick={() => profileStore.toggleTheme()}
        class="p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-between font-bold text-slate-700 dark:text-slate-200 cursor-pointer"
      >
        <span>{profileStore.theme === 'light' ? 'Modo Escuro' : 'Modo Claro'}</span>
        {#if profileStore.theme === 'light'}
          <Moon size={15} class="text-indigo-600" />
        {:else}
          <Sun size={15} class="text-amber-400" />
        {/if}
      </button>

      <!-- Language -->
      <div class="relative">
        <select
          value={profileStore.lang}
          onchange={(e) => profileStore.setLanguage((e.target as HTMLSelectElement).value as Language)}
          class="w-full p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-bold text-slate-700 dark:text-slate-200 text-xs cursor-pointer focus:outline-none"
        >
          <option value="pt">🇧🇷 Português</option>
          <option value="es">🇪🇸 Español</option>
          <option value="en">🇬🇧 English</option>
        </select>
      </div>
    </div>

    <!-- Area Filter on Mobile -->
    <div class="space-y-1.5">
      <div class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Filtrar por Matéria</div>
      <div class="grid grid-cols-3 gap-1.5">
        <button
          onclick={() => { selectedAreaFilter = 'All'; isMobileMenuOpen = false; activeTab = 'practice'; }}
          class="p-2 rounded-lg text-[11px] font-bold text-center border cursor-pointer {selectedAreaFilter === 'All' ? 'bg-slate-800 text-white dark:bg-slate-200 dark:text-slate-900 border-slate-800' : 'bg-slate-50 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700'}"
        >
          TODAS
        </button>
        {#each Object.entries(AREA_THEMES) as [areaName, theme]}
          <button
            onclick={() => { selectedAreaFilter = areaName; isMobileMenuOpen = false; activeTab = 'practice'; }}
            class="p-2 rounded-lg text-[11px] font-bold text-center border cursor-pointer {selectedAreaFilter === areaName ? `${theme.badge} ring-1 ring-slate-400` : 'bg-slate-50 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border-slate-200 dark:border-slate-700'}"
          >
            {theme.shortName}
          </button>
        {/each}
      </div>
    </div>

    <!-- Profile and Stats -->
    <div class="pt-2 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between text-[11px]">
      <span class="text-slate-500">Perfil: <strong>{profileStore.activeProfileName}</strong></span>
      <span class="text-emerald-600 dark:text-emerald-400 font-bold">{totalSolved} resolvidas</span>
    </div>
  </div>
{/if}
