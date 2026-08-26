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

<div class="flex-1 h-full flex flex-col bg-[#FDFBF7] overflow-hidden">
  <!-- Formula Header -->
  <div class="px-6 py-3 bg-white border-b border-[#E8E2D8] flex flex-wrap items-center justify-between gap-3 shrink-0 select-none shadow-2xs">
    <div class="flex items-center space-x-3">
      <div class="p-2 rounded-xl bg-[#fffbeb] text-[#92400e] border border-[#fde68a]">
        <FileText size={17} />
      </div>
      <div>
        <h2 class="text-sm font-bold text-slate-900 font-sans flex items-center gap-2">
          Formulário Oficial EUF (Tabela de Referência Rápida)
        </h2>
        <p class="text-[11px] text-slate-500 font-sans">
          Relações canônicas e equações fornecidas nos cadernos oficiais de prova do Exame Unificado.
        </p>
      </div>
    </div>

    <!-- Quick Formula Search -->
    <div class="relative w-64">
      <input
        type="text"
        bind:value={searchQuery}
        placeholder="Buscar fórmula (ex: Maxwell, Poisson)..."
        class="w-full text-xs bg-[#FAF8F5] text-slate-800 border border-[#DDD6C8] rounded-lg pl-8 pr-3 py-1.5 placeholder-slate-400 focus:outline-none focus:border-sky-500 font-sans"
      />
      <Search size={13} class="absolute left-2.5 top-2.5 text-slate-400" />
    </div>
  </div>

  <!-- Equations Grid -->
  <div class="flex-1 overflow-y-auto custom-scrollbar p-6 bg-study-grid">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
      {#each filteredCategories() as cat}
        <div class="rounded-2xl bg-white border border-[#E5DFD4] p-5 space-y-3 shadow-xs">
          <h3 class="text-xs font-sans font-bold text-slate-900 uppercase pb-2 border-b border-[#E8E2D8] flex items-center justify-between">
            <span>{cat.category}</span>
            <span class="text-[11px] text-slate-400 font-normal">{cat.formulas.length} equações</span>
          </h3>

          <div class="space-y-3">
            {#each cat.formulas as f}
              <div class="p-3.5 bg-[#FAF8F5] border border-[#E8E2D8] rounded-xl space-y-1 shadow-2xs">
                <div class="text-[11px] font-sans font-bold text-slate-600">
                  {f.name}:
                </div>
                <div class="text-xs text-slate-900 overflow-x-auto py-1" use:mathAction={`$$${f.eq}$$`}></div>
              </div>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</div>
