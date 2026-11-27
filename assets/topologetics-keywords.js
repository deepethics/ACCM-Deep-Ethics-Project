/* Canonical terminology in the assembled project page; excludes site navigation,
   literal code and original source downloads. Static reading copies also carry links. */
(() => {
  const url = "https://deepethics.github.io/ACCM-Deep-Ethics-Project/TOPOLOGETICS/";
  const mark = "Topologetics™";
  const term = /(?<![\p{L}\p{N}_/\\#])(?:Topologetics|topologetics)(?![\p{L}\p{N}_]|\.(?:md|txt|html?|pdf|json|js|svg|zip)\b)(?:™)*/gu;
  const root = document.querySelector(".accm-main-column") || document.querySelector("main");
  if (!root) return;
  const excluded = "nav, pre, code, script, style, textarea, input, button, select, svg, [data-no-keyword-link]";
  const self = /\/TOPOLOGETICS\/?$/i.test(location.pathname);
  const isCanonical = a => {
    try { return /\/TOPOLOGETICS\/?$/i.test(new URL(a.href, location.href).pathname); }
    catch (_) { return false; }
  };
  const isOrdinary = a => isCanonical(a) && !new URL(a.href, location.href).hash &&
    a.textContent.trim() === mark && !a.id && !a.className && !a.hasAttribute("aria-current");
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const nodes = [];
  for (let n = walker.nextNode(); n; n = walker.nextNode()) {
    if (!n.parentElement || n.parentElement.closest(excluded)) continue;
    const s = n.nodeValue;
    if (!/[Tt]opologetics/.test(s)) continue;
    // Preserve URL and file-path literals in visible text.
    n.nodeValue = s.split(/(https?:\/\/[^\s<>"']+)/g).map((part, i) =>
      i % 2 ? part : part.replace(term, mark)).join("");
    nodes.push(n);
  }
  const links = Array.from(root.querySelectorAll("a")).filter(a =>
    !a.closest(excluded) && isCanonical(a) && a.textContent.includes(mark));
  let count = links.filter(a => !isOrdinary(a)).length;
  for (const a of links) {
    if (!isOrdinary(a)) continue;
    if (count < 3 || self) { count++; continue; }
    a.replaceWith(...Array.from(a.childNodes));
  }
  if (self) return;
  for (const n of nodes) {
    if (count >= 3) break;
    if (!n.isConnected || !n.parentElement || n.parentElement.closest("a,h1,h2,h3,h4,h5,h6," + excluded)) continue;
    const s = n.nodeValue;
    const frag = document.createDocumentFragment();
    let cursor = 0, changed = false;
    for (const m of s.matchAll(/Topologetics™/g)) {
      if (count >= 3) break;
      const before = s.slice(0, m.index);
      if (/https?:\/\/[^\s<>"']*$/.test(before)) continue;
      frag.append(document.createTextNode(s.slice(cursor, m.index)));
      const a = document.createElement("a");
      a.href = url; a.target = "_blank"; a.rel = "noopener"; a.textContent = mark;
      frag.append(a); cursor = m.index + mark.length; count++; changed = true;
    }
    if (changed) { frag.append(document.createTextNode(s.slice(cursor))); n.replaceWith(frag); }
  }
})();
