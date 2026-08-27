<script lang="ts">
  import { profileStore } from '../storage.svelte';
  import { HelpCircle, X } from 'lucide-svelte';

  let {
    isOpen = $bindable(false)
  }: {
    isOpen: boolean;
  } = $props();

  const shortcuts = $derived([
    { key: 'K / ↓', desc: profileStore.t('scNext') },
    { key: 'J / ↑', desc: profileStore.t('scPrev') },
    { key: 'S', desc: profileStore.t('scSolved') },
    { key: 'R', desc: profileStore.t('scReview') },
    { key: 'X', desc: profileStore.t('scFailed') },
    { key: 'Z', desc: profileStore.t('scZoom') },
    { key: 'T', desc: profileStore.t('scTwin') },
    { key: '1 - 4', desc: profileStore.t('scHints') },
    { key: 'P', desc: profileStore.t('scModeStudy') },
    { key: 'M', desc: profileStore.t('scModeMap') },
    { key: 'F', desc: profileStore.t('scModeFormulas') },
    { key: '?', desc: profileStore.t('scHelp') },
    { key: 'Esc', desc: profileStore.t('scEsc') },
  ]);
</script>

{#if isOpen}
  <div
    class="fixed inset-0 z-50 bg-slate-900/40 dark:bg-black/80 backdrop-blur-xs flex items-center justify-center p-4"
    role="dialog"
    aria-modal="true"
    tabindex="-1"
    onclick={() => isOpen = false}
    onkeydown={(e) => { if (e.key === 'Escape') isOpen = false; }}
  >
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <div
      class="bg-white dark:bg-slate-900 rounded-3xl p-6 max-w-lg w-full shadow-xl space-y-4 border border-[#E5DFD4] dark:border-slate-800 text-slate-800 dark:text-slate-200 font-sans select-none"
      role="document"
      onclick={(e) => e.stopPropagation()}
    >
      <div class="flex items-center justify-between pb-3 border-b border-[#E8E2D8] dark:border-slate-800">
        <h3 class="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
          <HelpCircle size={18} class="text-sky-600 dark:text-sky-400" />
          {profileStore.t('shortcutsTitle')}
        </h3>
        <button
          onclick={() => isOpen = false}
          class="text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 p-1.5 rounded-xl hover:bg-[#FAF8F5] dark:hover:bg-slate-800 transition cursor-pointer"
        >
          <X size={18} />
        </button>
      </div>

      <div class="space-y-2 max-h-[60vh] overflow-y-auto custom-scrollbar pr-1">
        {#each shortcuts as sc}
          <div class="flex items-center justify-between p-2.5 rounded-xl bg-[#FAF8F5] dark:bg-slate-800/60 border border-[#E8E2D8] dark:border-slate-800 text-xs">
            <span class="text-slate-700 dark:text-slate-300">{sc.desc}</span>
            <span class="key-cap">{sc.key}</span>
          </div>
        {/each}
      </div>

      <div class="pt-2 text-center border-t border-[#E8E2D8] dark:border-slate-800">
        <button
          onclick={() => isOpen = false}
          class="w-full py-2.5 bg-slate-900 dark:bg-sky-600 hover:bg-slate-800 dark:hover:bg-sky-500 text-white rounded-xl text-xs font-bold transition shadow-xs cursor-pointer"
        >
          {profileStore.t('continueStudy')}
        </button>
      </div>
    </div>
  </div>
{/if}
