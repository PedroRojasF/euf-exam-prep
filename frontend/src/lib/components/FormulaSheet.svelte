<script lang="ts">
  import { OFFICIAL_FORMULAS } from '../constants';
  import { mathAction } from '../math';
  import { FileText, Search } from 'lucide-svelte';

  let searchQuery = $state<string>('');

  const filteredCategories = $derived(() => {
    if (!searchQuery.trim()) return OFFICIAL_FORMULAS;
    const q = searchQuery.toLowerCase().trim();
    return OFFICIAL_FORMULAS.map(cat => {
      const matchCat = cat.category.toLowerCase().includes(q);
      const filteredF = cat.formulas.filter(f => 
        f.name.toLowerCase().includes(q) || f.eq.toLowerCase().includes(q) || matchCat
      );
      return {
        ...cat,
        formulas: filteredF
      };
    }).filter(cat => cat.formulas.length > 0);
  });
</script>

<div class="flex-1 h-full flex flex-col bg-[#0b101d] overflow-hidden">
  <!-- Formula Header -->
  <div class="px-6 py-3 bg-[#080d18] border-b border-white/8 flex flex-wrap items-center justify-between gap-3 shrink-0 select-none">
    <div class="flex items-center space-x-3">
      <div class="p-1.5 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30">
        <FileText size={16} />
      </div>
      <div>
        <h2 class="text-sm font-bold text-white font-mono flex items-center gap-2">
          Formulário Oficial EUF (Tabela de Referência Rápida)
        </h2>
        <p class="text-[11px] text-slate-500 font-mono">
          Equações fundamentais e relações canônicas dos cadernos de prova oficiais.
        </p>
      </div>
    </div>

    <!-- Quick Formula Search -->
    <div class="relative w-64">
      <input
        type="text"
        bind:value={searchQuery}
        placeholder="Buscar fórmula (ex: Maxwell, Poisson, Carnot)..."
        class="w-full text-xs bg-slate-950 text-slate-200 border border-white/10 rounded px-7 py-1.5 placeholder-slate-500 focus:outline-none focus:border-sky-500 font-mono"
      />
      <Search size={12} class="absolute left-2.5 top-2.5 text-slate-500" />
    </div>
  </div>

  <!-- Equations Grid -->
  <div class="flex-1 overflow-y-auto custom-scrollbar p-6 bg-tech-grid">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      {#each filteredCategories() as cat}
        <div class="rounded-lg bg-[#0e1526] border border-white/8 p-4 space-y-3 shadow-xl">
          <h3 class="text-xs font-mono font-bold text-sky-300 uppercase pb-2 border-b border-white/8 flex items-center justify-between">
            <span>{cat.category}</span>
            <span class="text-[10px] text-slate-500 font-normal">{cat.formulas.length} equações</span>
          </h3>

          <div class="space-y-2.5">
            {#each cat.formulas as f}
              <div class="p-3 bg-slate-950/80 border border-white/6 rounded-md space-y-1">
                <div class="text-[11px] font-mono font-semibold text-slate-400">
                  {f.name}:
                </div>
                <div class="text-xs text-white overflow-x-auto py-1" use:mathAction={`$$${f.eq}$$`}></div>
              </div>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</div>
