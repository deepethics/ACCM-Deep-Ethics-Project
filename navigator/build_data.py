import urllib.request, json, re
from bs4 import BeautifulSoup
BASE='https://deepethics.github.io/ACCM-Deep-Ethics-Project/'
html=urllib.request.urlopen(BASE+'PAGES/',timeout=30).read()
soup=BeautifulSoup(html,'html.parser'); post=soup.select_one('.post-content')

def norm(a):
    href=a.get('href','').strip()
    if href.startswith('/ACCM-Deep-Ethics-Project/'): href='https://deepethics.github.io'+href
    if href.startswith('https://deepethics.github.io/ACCM-Deep-Ethics-Project'):
        return href
    return None

def title(a):
    return re.sub(r'\s+',' ',a.get_text(' ',strip=True)).strip().strip('·') or 'Open page'

def gather_between(h, stop_level='h2'):
    out=[]; node=h
    while True:
        node=node.find_next_sibling()
        if not node: break
        if node.name in ('h2','h3') and (stop_level=='h2' or node.name in ('h2','h3')): break
        for a in node.select('a[href]') if hasattr(node,'select') else []:
            u=norm(a)
            if u: out.append({'title':title(a),'url':u})
    return out

def unique(items):
    seen=set(); out=[]
    for p in items:
        k=p['url'].rstrip('/')
        if k not in seen: seen.add(k); out.append(p)
    return out

sections=[]
for h in post.select('h2'):
    name=h.get_text(' ',strip=True)
    if re.match(r'^[1-7]\. ',name):
        items=gather_between(h)
        # Retain the PAGES list's actual link names and sort-free reading order.
        sections.append({'name':name, 'description': {'1. Fused core':'The foundational topology, its vectors and core reference pages.', '2. How the topology moves':'Field, phase, flux and jurisdiction: how the core moves as context shifts.', '3. What keeps it corrigible':'Correction, challenge, due process, evidence and mutual dignity.', '4. Source objects the topology reads':'Source records, biography, origins and attributed contributions.', '5. The topology applied':'Domains, specimens, experiments and humor.', '6. Doors and the record':'Entry points, governance, project status and the audit trail.', '7. Shelves':'Open shelves for future pages; not ranked.'}.get(name,''), 'pages':unique(items)})

# current development routes / concise path prompts, links are the page links in their source table
h=next((x for x in post.select('h2') if x.get_text(' ',strip=True)=='Current development routes'),None)
if h:
    items=gather_between(h)
    sections.insert(0,{'name':'Current development routes','description':'Recent, task-oriented paths through the living reading map. Open each linked page in sequence.', 'pages':unique(items)})
# exact numbered index
h=next((x for x in post.select('h3') if x.get_text(' ',strip=True)=='Page numbers'),None)
route=[]
if h:
    node=h
    while True:
        node=node.find_next_sibling()
        if not node or node.name in ('h2','h3'): break
        if node.name in ('ul','ol'):
            for li in node.select(':scope > li'):
                a=li.find('a',href=True)
                if a:
                    u=norm(a)
                    if u:
                        label=title(a)
                        text=re.sub(r'^\d+\.?\s*','',li.get_text(' ',strip=True))
                        route.append({'number':len(route)+1,'title':text or label,'url':u})
sections.append({'name':'52 page-number routes','description':'A second sequence of destination pages. The numbers are route identifiers, not a score or a reading order.', 'pages':[{'title':f"{x['number']:02d} · {x['title']}",'url':x['url'],'number':x['number']} for x in route]})
# All unique linked page names that appear in the cluster reading map, including nested source links.
allpages=unique([p for sec in sections for p in sec['pages']])
# Keep only within-project pages, omit generated same-page anchors from directory index, while retaining them in route sections.
sitepages=[]
for p in allpages:
    if '#' not in p['url']: sitepages.append(p)
sitepages.sort(key=lambda x:x['title'].casefold())
sections.append({'name':'All page links · A–Z','description':f'Browse the page names from the reading map alphabetically. {len(sitepages)} unique page links.', 'pages':sitepages})
# Signature links not guaranteed in PAGES page extraction: explicit canonical destinations requested by John.
featured=[
('Core Disclaimers','CORE-DISCLAIMERS/'),('Biography','BIOGRAPHY/'),('Topologetics','TOPOLOGETICS/'),('Symbols · 🦜🦋🌳','SYMBOLS/'),('1888 intelligence-properties taxonomy','1888/'),('27 + 12','CORE/27-PLUS-12/'),('If you are new','IF-YOU-ARE-NEW/')]
sections.insert(1,{'name':'John’s quick doors','description':'A few high-signal entry points and canonical references.', 'pages':[{'title':n,'url':BASE+path} for n,path in featured]})
# Deduplicate groups yet preserve labels/order.
data={'title':'ACCM Deep Ethics Project','canonicalTitle':'ACCM Deep Ethics Project','source':BASE+'PAGES/','sourceUpdated':'5 November 2026 (source page date)','sections':sections,'sitePageCount':len(sitepages)}
with open('/home/user/deep-ethical-navigator/pages.json','w') as f: json.dump(data,f,ensure_ascii=False,indent=2)
print('sections',[(x['name'],len(x['pages'])) for x in sections], 'A-Z',len(sitepages),'routes',len(route))
