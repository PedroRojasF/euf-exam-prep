import katex from 'katex';

export function renderInlineMath(text: string): string {
  if (!text) return '';

  // Replace $$...$$ with block math
  let processed = text.replace(/\$\$([\s\S]*?)\$\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: true, throwOnError: false });
    } catch {
      return `$$${math}$$`;
    }
  });

  // Replace $...$ with inline math
  processed = processed.replace(/\$([^\$\n]+?)\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: false, throwOnError: false });
    } catch {
      return `$${math}$`;
    }
  });

  return processed;
}

export function mathAction(node: HTMLElement, textContent: string) {
  function update(content: string) {
    node.innerHTML = renderInlineMath(content);
  }

  update(textContent);

  return {
    update(newContent: string) {
      update(newContent);
    }
  };
}
