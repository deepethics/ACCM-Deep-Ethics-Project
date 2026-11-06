const BASE='https://deepethics.github.io/ACCM-Deep-Ethics-Project/';
const groupsEl=document.querySelector('#groups'),filtersEl=document.querySelector('#filters'),searchEl=document.querySelector('#search');
let data, active='All lists', query='';
const escapeHTML=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function compactName(name){return name.replace(/\s+/g,' ').trim()}
function makeFilters(sections){
 const preferred=['All lists','John’s quick doors','Current development routes','1. Fused core','2. How the topology moves','3. What keeps it corrigible','4. Source objects the topology reads','5. The topology applied','6. Doors and the record','7. Shelves','52 page-number routes','All page links · A–Z'];
 filtersEl.innerHTML=preferred.filter(n=>n==='All lists'||sections.some(s=>s.name===n)).map((n,i)=>`<button class="filter-chip ${n===active?'active':''}" data-filter="${escapeHTML(n)}">${n==='All lists'?'All lists':escapeHTML(n.replace(/^\d+\. /,''))}</button>`).join('');
 filtersEl.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{active=b.dataset.filter;makeFilters(sections);render()}));
}
function render(){
 const matchingGroups=sections.filter(s=>active==='All lists'||s.name===active).map(s=>({...s,pages:s.pages.filter(p=>!query||p.title.toLowerCase().includes(query)||p.url.toLowerCase().includes(query))})).filter(s=>s.pages.length);
 let total=matchingGroups.reduce((n,s)=>n+s.pages.length,0);
 document.querySelector('#resultCount').textContent=query?`${total} matching page${total===1?'':'s'} in ${matchingGroups.length} list${matchingGroups.length===1?'':'s'}`:`${data.sitePageCount} unique page links · ${data.sections.find(s=>s.name==='52 page-number routes')?.pages.length||52} numbered routes`;
 if(!matchingGroups.length){groupsEl.innerHTML='<div class="no-results">No page names match that search. Try a broader term or clear the search.</div>';return}
 groupsEl.innerHTML=matchingGroups.map((s,i)=>{
  const originalIndex=sections.findIndex(x=>x.name===s.name)+1;
  const isRoute=s.name.includes('page-number');
  const items=s.pages.map(p=>`<a class="page-link ${isRoute?'route-link':''}" href="${escapeHTML(p.url)}" target="_blank" rel="noopener noreferrer" title="Open ${escapeHTML(p.title)} in the original project"><span class="page-label">${escapeHTML(compactName(p.title))}</span><span class="arrow" aria-hidden="true">↗</span></a>`).join('');
  const defaultOpen=s.name==='John’s quick doors'||s.name==='Current development routes';
  const openAttr=(query||active!=='All lists'||defaultOpen)?' open':'';
  return `<details class="group-card"${openAttr}><summary><span class="group-num">${isRoute?'52':String(originalIndex).padStart(2,'0')}</span><span class="group-summary"><span class="group-title">${escapeHTML(s.name)}</span><span class="group-desc">${escapeHTML(s.description||'Explore related pages in this reading group.')}</span></span><span class="group-count">${s.pages.length} pages</span><span class="chevron">⌄</span></summary><div class="link-grid">${items}</div></details>`;
 }).join('');
}
let sections=[];
fetch('pages.json').then(r=>{if(!r.ok)throw new Error('Could not load the page index');return r.json()}).then(d=>{data=d;sections=d.sections;makeFilters(sections);render()}).catch(()=>{document.querySelector('#resultCount').textContent='Map data could not load';groupsEl.innerHTML='<div class="no-results">The page index could not be loaded. Try refreshing, or open the <a href="'+BASE+'PAGES/" target="_blank" rel="noopener">original PAGES index ↗</a>.</div>'});
searchEl.addEventListener('input',()=>{query=searchEl.value.toLowerCase().trim();document.querySelector('#clearSearch').hidden=!query;render()});
document.querySelector('#clearSearch').addEventListener('click',()=>{searchEl.value='';query='';document.querySelector('#clearSearch').hidden=true;render();searchEl.focus()});
document.querySelector('#expandAll').addEventListener('click',()=>groupsEl.querySelectorAll('details').forEach(d=>d.open=true));
document.querySelector('#collapseAll').addEventListener('click',()=>groupsEl.querySelectorAll('details').forEach(d=>d.open=false));
document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA'].includes(document.activeElement.tagName)){e.preventDefault();searchEl.focus()}if(e.key==='Escape'&&document.activeElement===searchEl){searchEl.value='';query='';document.querySelector('#clearSearch').hidden=true;render();searchEl.blur()}});
if('serviceWorker' in navigator && location.protocol.startsWith('http')) navigator.serviceWorker.register('./sw.js').catch(()=>{});
