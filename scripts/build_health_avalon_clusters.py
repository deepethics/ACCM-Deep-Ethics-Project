#!/usr/bin/env python3
"""Generate the cluster map from explicit memberships and canonical inventory rows."""
from pathlib import Path
from collections import Counter
import argparse,html,json,re
ROOT=Path(__file__).resolve().parents[1]
INVENTORY=ROOT/'_includes/health-avalon-scope-inventory.md';DATA=ROOT/'_data/health_avalon_clusters.json';OUTPUT=ROOT/'_includes/health-avalon-clusters.md'
ROW=re.compile(r'^(\| (A\d{3}) — \*\*(.*?)\*\*)(?: <span id="avalon-a\d{3}"></span>)? \|',re.M)
def build(check=False):
 d=json.loads(DATA.read_text());original=INVENTORY.read_text();topics={m[2]:m[3] for m in ROW.finditer(original)}
 assert len(topics)==d['topic_count']==336;assert list(topics)==[f'A{i:03}' for i in range(1,337)]
 clusters=d['clusters'];byid={c['id']:c for c in clusters};assert len(clusters)==len(byid)==d['cluster_count']==32
 memberships={k:[] for k in topics}
 for c in clusters:
  assert c['id']==f"cluster-{c['number']:02}";assert c['topics']==sorted(set(c['topics']))
  assert set(c['topics'])<=set(topics);assert set(c['spotlight_topics'])<=set(c['topics']);assert set(c['related'])<=set(byid)
  for n in c['source_posts']:assert str(n) in d['source_entries']
  for k in c['topics']:memberships[k].append(c['id'])
 assert all(memberships.values()),'unmapped topic'
 anchored=ROW.sub(lambda m:m[1]+f' <span id="avalon-{m[2].lower()}"></span> |',original)
 strip=lambda x:re.sub(r' <span id="avalon-a\d{3}"></span>','',x)
 assert strip(anchored)==strip(original),'topic text changed';assert len(re.findall(r'id="avalon-a\d{3}"',anchored))==336
 def link(k):return f'[{k} — {topics[k]}](#avalon-{k.lower()})'
 def clink(k,full=False):
  c=byid[k];label=f"Cluster {c['number']}"+(f" — {c['title']}" if full else '')
  return f'[{label}](#avalon-{k})'
 def source(n):
  x=d['source_entries'][str(n)];return f"[#{n} — {x['label']}]({x['url']})"
 s='''## Project Avalon: 32 overlapping investigation clusters {#avalon-clusters}

**John’s nine starting clusters lead this map.** Clusters 10–32 add care, clinical, research, information and process relationships from the inventory. Every topic A001–A336 appears in one or more clusters. Memberships are GPT / Codex’s editorial research routes, open to correction; each originating source retains its own type, date, qualifiers and status.

Open a cluster for its purpose, source entry points and topic links. Each topic link returns to the full question, investigation reason and forum sources in the [336-topic inventory](#avalon-scope-inventory). The [topic-to-cluster index](#avalon-cluster-topic-index) gives the reverse route. Cluster counts describe navigation, with overlapping membership allowed.

The first seven clusters foreground contributors, source forms and settings. Later clusters add mechanisms, care needs, methods, consequences and governing processes. A doctor can also be a patient; a case report can enter a hearing; a legal decision can affect access to care. [Topologetics]({{ '/TOPOLOGETICS/#health-scope-clusters' | relative_url }}) keeps these relationships recoverable through the [1888 intelligence-properties trajectory]({{ '/1888/' | relative_url }}), [10+1]({{ '/NETWORK/ten-plus-one/' | relative_url }}) and [Symmetric Grace]({{ '/NETWORK/asymmetric-grace/' | relative_url }}).

| Cluster | Inquiry purpose | Linked topics |
|---|---|---|
'''
 for c in clusters:s+=f"| {clink(c['id'],True)} | {c['purpose']} | {len(c['topics'])} |\n"
 s+='\n### Open a cluster and follow its relationships {#avalon-cluster-details}\n\n'
 for c in clusters:
  s+=f"<details id=\"avalon-{c['id']}\" markdown=\"1\">\n<summary><strong>Cluster {c['number']} — {html.escape(c['title'])}</strong> · {len(c['topics'])} linked topics</summary>\n\n"
  s+=f"**Inquiry purpose:** {c['purpose']}\n\n**Relations to preserve:** {c['preserve']}\n\n"
  if c.get('note'):s+=c['note']+'\n\n'
  s+='**Selected archive routes:** '+ '; '.join(source(n) for n in c['source_posts'])+'.\n\n'
  if c['number']==4:
   s+='Publication leads retain the type and version described in the archive. Originating records remain available for a deeper check of publication status, revisions, methods and conclusions.\n\n| Publication lead | Source form recorded | Archive route |\n|---|---|---|\n'
   for p in d['publication_leads']:s+=f"| [{p['title']}]({p['url']}) | {p['kind']} | {source(p['post'])} |\n"
   s+='\n'
  s+='**Named starting topics:**\n\n'+'\n'.join('- '+link(k) for k in c['spotlight_topics'])+'\n\n'
  s+='**All linked topic IDs** — full titles also appear in the topic-to-cluster index:\n\n'
  s+='<p class="avalon-cluster-members">'+' · '.join(f'<a href="#avalon-{k.lower()}" title="{html.escape(topics[k],quote=True)}" aria-label="{html.escape(k+" — "+topics[k],quote=True)}">{k}</a>' for k in c['topics'])+'</p>\n\n'
  s+='**Related clusters:** '+ ' · '.join(clink(k) for k in c['related'])+'.\n\n[Cluster overview](#avalon-clusters) · [Topic-to-cluster index](#avalon-cluster-topic-index)\n\n</details>\n\n'
 s+='''### Follow a relation across clusters {#avalon-cluster-paths}

These are suggested research routes through existing topics. Each step retains its own source and open question.

| Starting object | Relations that keep the field recoverable | Useful clusters |
|---|---|---|
| A clinician’s concern | Professional account → clinical record → reporting entry → investigation → response and care | [1](#avalon-cluster-01), [11](#avalon-cluster-11), [17](#avalon-cluster-17), [23](#avalon-cluster-23), [12](#avalon-cluster-12) |
| A death-care observation | Worker’s role and observation → sample and method → clinical history → population comparison | [5](#avalon-cluster-05), [21](#avalon-cluster-21), [11](#avalon-cluster-11), [13](#avalon-cluster-13), [22](#avalon-cluster-22) |
| A mandate or emergency measure | Authority and purpose → evidence and alternatives → affected people → consequences → challenge and repair | [8](#avalon-cluster-08), [3](#avalon-cluster-03), [22](#avalon-cluster-22), [26](#avalon-cluster-26), [28](#avalon-cluster-28), [2](#avalon-cluster-02) |
| A mass-psychology hypothesis | Message and commissioning → distribution and classification → audience conditions → interpretation and choice → notice and later conduct | [9](#avalon-cluster-09), [19](#avalon-cluster-19), [20](#avalon-cluster-20), [24](#avalon-cluster-24), [30](#avalon-cluster-30), [32](#avalon-cluster-32) |
| A person’s care needs | Lived account → diagnostic and rehabilitation pathway → household support → agency and meaningful participation | [10](#avalon-cluster-10), [11](#avalon-cluster-11), [12](#avalon-cluster-12), [28](#avalon-cluster-28), [26](#avalon-cluster-26) |

A cluster membership is revisable. A useful correction identifies the topic, the relation that is missing or misplaced, the source and what changes in the next inquiry. The evaluator’s framing remains available for the same scrutiny as the institutions, publications, communities and participants being examined.

<details markdown="1">
<summary id="avalon-cluster-topic-index"><strong>Topic-to-cluster index — all 336 topics</strong></summary>

This reverse index preserves multiple memberships. Topic links open their full inventory entry; cluster links return to the corresponding cluster.

| No. | Topic | Cluster memberships |
|---|---|---|
'''
 for n,(k,title) in enumerate(topics.items(),1):
  members=' · '.join(f"[{byid[j]['number']}](#avalon-{j})" for j in memberships[k])
  s+=f'| {n} | {link(k)} | {members} |\n'
 s+='\n</details>\n\n'
 if check:
  assert anchored==original,'topic anchors need regeneration';assert OUTPUT.read_text()==s,'cluster include needs regeneration'
 else:INVENTORY.write_text(anchored);OUTPUT.write_text(s)
 print(json.dumps(dict(clusters=len(clusters),topics=len(topics),memberships=sum(len(c['topics']) for c in clusters),source_routes=len(d['source_entries']),unmapped=0,membership_distribution=dict(sorted(Counter(len(v) for v in memberships.values()).items())),generated_bytes=len(s.encode())),indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');build(p.parse_args().check)
