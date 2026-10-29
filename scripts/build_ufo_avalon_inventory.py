#!/usr/bin/env python3
"""Render the source-linked UFO–UAP inquiry inventory and overlapping clusters."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
obj=json.loads((ROOT/'_data/ufo_avalon_inventory.json').read_text())
records=obj['topics'];coverage=obj['coverage']
clusters=[(c['title'],[int(t[1:]) for t in c['topics']]) for c in obj['clusters']]
assert len({x['id'] for x in records})==len(records)
assert [p['post_number'] for p in records[0]['sources']]
text=['## Scope inventory — first batch {#ufo-scope-inventory}','', '**Covered: pages 1–10, posts #1–200 · U001–U067 · next unexamined page: 11.**','', 'Entries are editorial questions with a reason for further inquiry. A source link locates the contribution that prompted the question. It also lets participants repair the question, add context or connect another source.','']
for lo in range(0,len(records),8):
 text+=['| ID / potential topic | Investigation question and why it could help | Forum starting points |','|---|---|---|']
 for x in records[lo:lo+8]:
  src=' · '.join(f"[#{s['post_number']}]({s['url']})" for s in x['sources'])
  text.append(f"| <span id=\"ufo-{x['id'].lower()}\"></span>**{x['id']} — {x['title']}** | {x['question']} **Why:** {x['why']} | {src} |")
 text+=['']
text+=['## Overlapping clusters {#ufo-clusters}','','These **18 initial editorial lenses** connect the first 67 topics. Membership can change as later batches recover more of the thread. Select a topic ID to recover its question, reason and sources.','']
for i,(name,ids) in enumerate(clusters,1):
 text += [f'### C{i:02} — {name} {{#ufo-cluster-{i:02}}}', '', ' · '.join(f'[U{j:03}](#ufo-u{j:03})' for j in ids), '']
text+=['## Reverse topic–cluster index {#ufo-reverse-index}','','| Topic | Cluster memberships |','|---|---|']
for x in records:text.append('| ['+x['id']+'](#ufo-'+x['id'].lower()+') | '+' · '.join('['+c+'](#ufo-cluster-'+c[1:]+')' for c in x['clusters'])+' |')
text+=['','## Batch and access record {#ufo-coverage}','','Retrieved 29 October 2026. All 200 post containers in this range were recovered. Text and linked-source descriptions were inspected for topic discovery; long articles were skimmed. Quotes inside replies remain part of the local context and are not counted as new independent observations. Image-only or minimally described posts enter U063 and the access queue.','', '| Forum page | Posts | Post containers | Text-empty posts: visual/media pass pending |','|---|---|---:|---|']
for x in coverage:text.append(f"| {x['page']} | #{x['first_post']}–#{x['last_post']} | {x['post_count']} | "+(', '.join('#'+str(n) for n in x['text_empty_posts']) or '—')+' |')
text+=['','**Continuation:** start at [page 11]('+obj['source_thread']+'/page11), post #201. Preserve U001–U067, add a new ID for a distinct question and attach later source routes to existing topics when they develop the same relation. Keep batch coverage separate from the thread’s changing total.','']
output='\n'.join(text)
target=ROOT/'_includes/ufo-avalon-scope-inventory.md'
if '--check' in sys.argv:
 assert target.read_text()==output, 'Inventory include differs from its source data'
 print('UFO inventory include matches the source data')
else:
 target.write_text(output)
