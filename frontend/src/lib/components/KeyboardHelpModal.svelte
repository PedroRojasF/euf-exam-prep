<script lang="ts">
  import { HelpCircle, X } from 'lucide-svelte';

  let {
    isOpen = $bindable(false)
  }: {
    isOpen: boolean;
  } = $props();

  const shortcuts = [
    { key: 'K ou ↓', desc: 'Próxima questão da lista' },
    { key: 'J ou ↑', desc: 'Questão anterior da lista' },
    { key: 'S', desc: 'Marcar questão como Dominada (Solved) + 🎉' },
    { key: 'R', desc: 'Marcar questão para Revisão (Review)' },
    { key: 'X', desc: 'Marcar questão como Erro a Repetir (Failed)' },
    { key: 'Z', desc: 'Alternar modo de Zoom / Tela Cheia do enunciado' },
    { key: 'T', desc: 'Ir diretamente para a Variante Irmã (Gêmea A/B)' },
    { key: '1 - 4', desc: 'Abrir / Fechar Níveis 1 a 4 da Escada Socrática de Pistas' },
    { key: 'P', desc: 'Alternar para Modo Estudo' },
    { key: 'M', desc: 'Alternar para Mapa de Tópicos' },
    { key: 'F', desc: 'Alternar para Formulário Oficial' },
    { key: '?', desc: 'Abrir este menu de ajuda' },
    { key: 'Esc', desc: 'Fechar modais abertos' },
  ];
</script>

{#if isOpen}
  <div
    class="fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-xs flex items-center justify-center p-4"
    role="dialog"
    aria-modal="true"
    tabindex="-1"
    onclick={() => isOpen = false}
    onkeydown={(e) => { if (e.key === 'Escape') isOpen = false; }}
  >
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <div
      class="bg-white rounded-2xl p-6 max-w-lg w-full shadow-xl space-y-4 border border-[#E5DFD4] text-slate-800 font-sans select-none"
      role="document"
      onclick={(e) => e.stopPropagation()}
    >
      <div class="flex items-center justify-between pb-3 border-b border-[#E8E2D8]">
        <h3 class="font-bold text-sm text-slate-900 flex items-center gap-2">
          <HelpCircle size={17} class="text-sky-600" />
          Atalhos de Teclado Científicos
        </h3>
        <button
          onclick={() => isOpen = false}
          class="text-slate-400 hover:text-slate-700 p-1 rounded-lg hover:bg-[#FAF8F5] transition cursor-pointer"
        >
          <X size={17} />
        </button>
      </div>

      <div class="space-y-2 max-h-[60vh] overflow-y-auto custom-scrollbar pr-1">
        {#each shortcuts as sc}
          <div class="flex items-center justify-between p-2.5 rounded-xl bg-[#FAF8F5] border border-[#E8E2D8] text-xs">
            <span class="text-slate-700">{sc.desc}</span>
            <span class="key-cap">{sc.key}</span>
          </div>
        {/each}
      </div>

      <div class="pt-2 text-center border-t border-[#E8E2D8]">
        <button
          onclick={() => isOpen = false}
          class="w-full py-2.5 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold transition shadow-xs cursor-pointer"
        >
          Continuar Estudos
        </button>
      </div>
    </div>
  </div>
{/if}
