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
    { key: 'S', desc: 'Marcar questão como Dominada (Solved) + 🎉 Confetti' },
    { key: 'R', desc: 'Marcar questão para Revisão (Review)' },
    { key: 'X', desc: 'Marcar questão como Erro a Repetir (Failed)' },
    { key: 'Z', desc: 'Alternar modo de Zoom / Tela Cheia do enunciado' },
    { key: 'T', desc: 'Ir diretamente para a Variante Irmã (Gêmea A/B)' },
    { key: '1 - 4', desc: 'Abrir / Fechar Níveis 1 a 4 da Escada Socrática de Pistas' },
    { key: 'P', desc: 'Alternar para Modo Cockpit de Prática' },
    { key: 'M', desc: 'Alternar para Mapa de Conhecimento' },
    { key: 'F', desc: 'Alternar para Formulário Oficial' },
    { key: '?', desc: 'Abrir este menu de ajuda' },
    { key: 'Esc', desc: 'Fechar modais abertos' },
  ];
</script>

{#if isOpen}
  <div
    class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4"
    role="dialog"
    aria-modal="true"
    tabindex="-1"
    onclick={() => isOpen = false}
    onkeydown={(e) => { if (e.key === 'Escape') isOpen = false; }}
  >
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <div
      class="bg-[#0f172a] rounded-xl p-5 max-w-lg w-full shadow-2xl space-y-4 border border-white/10 text-slate-200 font-mono select-none"
      role="document"
      onclick={(e) => e.stopPropagation()}
    >
      <div class="flex items-center justify-between pb-3 border-b border-white/10">
        <h3 class="font-bold text-sm text-white flex items-center gap-2">
          <HelpCircle size={16} class="text-sky-400" />
          Atalhos de Teclado Científicos
        </h3>
        <button
          onclick={() => isOpen = false}
          class="text-slate-400 hover:text-white p-1 rounded hover:bg-white/5 transition"
        >
          <X size={16} />
        </button>
      </div>

      <div class="space-y-1.5 max-h-[60vh] overflow-y-auto custom-scrollbar pr-1">
        {#each shortcuts as sc}
          <div class="flex items-center justify-between p-2 rounded bg-slate-950/70 border border-white/5 text-xs">
            <span class="text-slate-300 font-sans">{sc.desc}</span>
            <span class="key-cap">{sc.key}</span>
          </div>
        {/each}
      </div>

      <div class="pt-2 text-center border-t border-white/10">
        <button
          onclick={() => isOpen = false}
          class="w-full py-2 bg-sky-600 hover:bg-sky-500 text-white rounded text-xs font-bold transition shadow-lg"
        >
          Continuar Treino
        </button>
      </div>
    </div>
  </div>
{/if}
