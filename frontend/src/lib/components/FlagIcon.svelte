<script lang="ts">
  let { lang, size = 18 }: { lang: 'pt' | 'es' | 'en' | string; size?: number } = $props();
  const height = $derived(Math.round(size * 0.72));
</script>

{#if lang === 'pt'}
  <!-- Brazil Flag SVG -->
  <svg width={size} height={height} viewBox="0 0 720 504" class="rounded-xs shadow-2xs inline-block shrink-0 overflow-hidden" style="vertical-align: middle;">
    <rect width="720" height="504" fill="#009c3b" rx="24"/>
    <polygon points="360,54 666,252 360,450 54,252" fill="#ffdf00"/>
    <circle cx="360" cy="252" r="115" fill="#002776"/>
    <path d="M250,280 C295,245 425,245 470,280 C425,255 295,255 250,280 Z" fill="#ffffff"/>
  </svg>
{:else if lang === 'es'}
  <!-- Spain Flag SVG -->
  <svg width={size} height={height} viewBox="0 0 720 504" class="rounded-xs shadow-2xs inline-block shrink-0 overflow-hidden" style="vertical-align: middle;">
    <rect width="720" height="504" fill="#c60b1e" rx="24"/>
    <rect y="126" width="720" height="252" fill="#ffc400"/>
    <circle cx="220" cy="252" r="38" fill="#c60b1e" opacity="0.8"/>
  </svg>
{:else}
  <!-- UK / English Flag SVG -->
  <svg width={size} height={height} viewBox="0 0 720 504" class="rounded-xs shadow-2xs inline-block shrink-0 overflow-hidden" style="vertical-align: middle;">
    <clipPath id="uk-clip-badge"><rect width="720" height="504" rx="24"/></clipPath>
    <g clip-path="url(#uk-clip-badge)">
      <rect width="720" height="504" fill="#012169"/>
      <path d="M0,0 L720,504 M720,0 L0,504" stroke="#ffffff" stroke-width="75"/>
      <path d="M0,0 L720,504 M720,0 L0,504" stroke="#c8102e" stroke-width="45"/>
      <path d="M360,0 V504 M0,252 H720" stroke="#ffffff" stroke-width="115"/>
      <path d="M360,0 V504 M0,252 H720" stroke="#c8102e" stroke-width="70"/>
    </g>
  </svg>
{/if}
