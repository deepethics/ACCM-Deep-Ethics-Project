#!/usr/bin/env python3
"""One-time, idempotent public reading-edition terminology audit.
Preserve technical identifiers and explicit exact-text archival originals.
"""
import argparse
from collections import Counter
from dataclasses import dataclass, asdict
from html import unescape
import json
from pathlib import Path
import re
import subprocess

URL = "https://deepethics.github.io/ACCM-Deep-Ethics-Project/TOPOLOGETICS/"
MARK = "Topologetics™"
ANCHOR = '<a href="' + URL + '" target="_blank" rel="noopener">' + MARK + '</a>'
TERM = re.compile(r'(?<![\w/\\#])(?:Topologetics|topologetics)(?!\w|\.(?:md|txt|html?|pdf|json|yml|yaml|js|svg|csv|zip|py)\b|-[\w-]+\.(?:md|txt|html?|pdf|json|js|svg|zip)\b)(?:™|&trade;|&#(?:8482|x2122);)*')
URL_TOKEN = re.compile(r'https?://[^\s<>"\x27]+')
CANON = re.compile(r'/TOPOLOGETICS/?(?:#|[ \x27"\)\}]|$)', re.I)
ROOT = re.compile(r'/TOPOLOGETICS/?(?:[ \x27"\)\}]|$)', re.I)
BLOCKED = {'head','title','nav','pre','svg','button','select','option','h1','h2','h3','h4','h5','h6','code','textarea','script','style'}
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
EXT = {'.md','.txt','.htm','.html','.json','.yml','.yaml','.csv','.svg','.js'}
EXACT = re.compile(r'(?:-original\.txt$|-source\.txt$|^27-MANNERISMS/source\.md$|^PROVENANCE/27-12-52-source\.md$|^PROVENANCE/.*(?:supplied|reaction|google-\d{4}-\d{2}-\d{2})\.txt$|^Deep-Ethical-PDFs/(?:SHA256SUMS|BUILD-REPORT)\.txt$)', re.I)
META_KEYS = re.compile(r'(?m)^(\s*(?:- )?(?:title|label|description|name):[ \t]*)([^\n]*)')
# Long alternatives first. The protected spans are returned byte-for-byte unless
# they carry a visible label; existing destinations, Liquid and code stay intact.
TOKENS = re.compile(
    r'(?P<fence>^[ \t]{0,3}(?P<ft>\x60{3,}|~{3,})[^\n]*\n[\s\S]*?^[ \t]{0,3}(?P=ft)[ \t]*(?:\n|$))'
    r'|(?P<comment><!--[\s\S]*?-->)'
    r'|(?P<raw><(?P<rt>script|style|textarea|code)\b[^>]*>[\s\S]*?</(?P=rt)\s*>)'
    r'|(?P<anchor><a\b[^>]*>[\s\S]*?</a\s*>)'
    r'|(?P<mdlink>!?\[[^\]\n]*\]\((?:[^()\n]|\([^()\n]*\))*\))'
    r'|(?P<reflink>!?\[[^\]\n]*\]\[[^\]\n]*\])'
    r'|(?P<definition>^[ \t]*\[[^\]\n]+\]:[^\n]*$)'
    r'|(?P<inlinecode>\x60+[^\x60\n]+\x60+)'
    r'|(?P<liquid>\{\{[\s\S]*?\}\}|\{%[\s\S]*?%\})'
    r'|(?P<url>https?://[^\s<>"\x27\x60]+)'
    r'|(?P<tag></?[A-Za-z][^>]*>)',
    re.I | re.M
)

@dataclass
class Audit:
    replacements: int = 0
    added_links: int = 0
    removed_duplicate_links: int = 0
    existing_keyword_links: int = 0
    final_keyword_links: int = 0
    remaining_special_links: int = 0
    text_reference_added: int = 0

def label_text(s):
    return unescape(re.sub(r'<[^>]+>|[*_\x60]', '', s)).strip()

def canonical_link(dest):
    return bool(CANON.search(dest))

def root_link(dest):
    return bool(ROOT.search(dest)) and not bool(re.search(r'/TOPOLOGETICS/?#',dest,re.I))

def update_text(path, original):
    audit = Audit()
    found = False
    def norm(s):
        nonlocal found
        def one(m):
            nonlocal found
            found = True
            if m.group(0) != MARK:
                audit.replacements += 1
            return MARK
        return TERM.sub(one, s)
    def plain(s):
        p, out = 0, []
        for m in URL_TOKEN.finditer(s):
            out.extend((norm(s[p:m.start()]),m.group(0)))
            p = m.end()
        out.append(norm(s[p:]))
        return ''.join(out)
    def visible_html(s):
        return re.sub(r'<[^>]*>|[^<]+', lambda m: m[0] if m[0].startswith('<') else plain(m[0]), s)
    ext=Path(path).suffix.lower()
    if not re.search(r'[Tt]opologetics',original):
        return original,audit

    # Metadata and generated display data: keep structural keys, paths, hashes,
    # executable code, URL values, and formatting intact.
    if ext in {'.json','.js'}:
        if path.startswith('PROVENANCE/') or (ext=='.js' and path not in {'MOBILE/data.js','navigator/data.js'}):
            return original,audit
        def string_value(m):
            token=m[0]
            if re.match(r'\s*:',original[m.end():]):
                return token
            try: value=json.loads(token)
            except (ValueError,TypeError): return token
            if not isinstance(value,str) or re.match(r'^(?:https?://|/|[\w-]+[/\\])',value):
                return token
            new=plain(value)
            return token if new==value else json.dumps(new,ensure_ascii=False)
        return re.sub(r'"(?:\\.|[^"\\])*"',string_value,original),audit
    if ext in {'.yml','.yaml'}:
        return META_KEYS.sub(lambda m:m[1]+plain(m[2]),original),audit
    if ext=='.csv':
        return plain(original),audit

    txt=ext=='.txt'
    md=ext=='.md'
    can_link=ext in {'.md','.html','.htm'} and path!='TOPOLOGETICS/index.md' and not path.startswith('_includes/')
    # Includes have no page-independent link budget. The common layout handles
    # their visible keyword links in the assembled page.
    fm,body='',original
    if md:
        front=re.match(r'\A---[ \t]*\r?\n[\s\S]*?\r?\n---[ \t]*\r?\n',body)
        if front:
            fm=META_KEYS.sub(lambda m:m[1]+plain(m[2]),front[0])
            body=body[front.end():]
    stack=[]
    parts=[]
    def allowed():
        return not any(t in BLOCKED for t in stack)
    def text_part(s,offset):
        if s: parts.append({'kind':'text','s':norm(s),'offset':offset,'eligible':allowed()})
    cursor=0
    for m in TOKENS.finditer(body):
        text_part(body[cursor:m.start()],cursor)
        s=m[0]; eligible=allowed(); direct=False; removable=False; inner=''
        kind='protected'
        if m.group('anchor'):
            a=re.match(r'(<a\b[^>]*>)([\s\S]*?)(</a\s*>)\Z',s,re.I)
            if a:
                inner=visible_html(a[2]); dest=a[1]
                s=a[1]+inner+a[3]
                direct=canonical_link(dest) and MARK in label_text(inner)
                removable=direct and root_link(dest) and label_text(inner)==MARK and not re.search(r'\b(?:id|class|aria-current|role)\s*=',dest,re.I)
                kind='link'
        elif m.group('mdlink'):
            a=re.match(r'(!?)\[([^\]\n]*)\]\(([\s\S]*)\)\Z',s)
            if a:
                inner=plain(a[2]);dest=a[3]
                s=a[1]+'['+inner+']('+dest+')'
                direct=not a[1] and canonical_link(dest) and MARK in label_text(inner)
                removable=direct and root_link(dest) and label_text(inner)==MARK
                kind='link'
        elif m.group('reflink'):
            # Shorthand reference identifiers are preserved.
            a=re.match(r'(!?)\[([^\]\n]*)\]\[([^\]\n]*)\]\Z',s)
            if a and a[3]: s=a[1]+'['+plain(a[2])+']['+a[3]+']'
        elif m.group('tag'):
            a=re.match(r'<(/?)([A-Za-z][\w:-]*)\b',s)
            if a:
                tag=a[2].lower()
                if a[1]:
                    if tag in stack:
                        i=len(stack)-1-stack[::-1].index(tag)
                        del stack[i:]
                elif tag not in VOID and not s.endswith('/>'):
                    stack.append(tag)
            s=re.sub(r'(\b(?:alt|title|aria-label|content)\s*=\s*)(["\x27])(.*?)\2',lambda a:a[1]+a[2]+plain(a[3])+a[2],s,flags=re.I)
        elif m.group('fence') and re.match(r'^[ \t]*(?:\x60{3,}|~{3,})(?:text|plaintext)[ \t]*\r?\n',s,re.I):
            s=plain(s)
        parts.append({'kind':kind,'s':s,'offset':m.start(),'eligible':eligible,'direct':direct,'removable':removable,'inner':inner})
        cursor=m.end()
    text_part(body[cursor:],cursor)

    links=[p for p in parts if p.get('direct') and p['eligible']]
    audit.existing_keyword_links=len(links)
    if can_link:
        # Preserve meaningful section/description links; prune only repeated
        # exact-label, base-route keyword links. Navigation is outside budget.
        special=[p for p in links if not p['removable']]
        audit.remaining_special_links=len(special)
        retained=len(special)
        for p in links:
            if not p['removable']:continue
            if retained<3:
                retained+=1
            else:
                p['s']=p['inner']
                audit.removed_duplicate_links+=1
        slots=max(0,3-retained)
        for p in parts:
            if not slots: break
            if p['kind']!='text' or not p['eligible']:continue
            segment=p['s']
            def link_word(m):
                nonlocal slots,retained
                if not slots:return m[0]
                start=segment.rfind('\n',0,m.start())+1
                prefix=segment[start:m.start()]
                if start==0:
                    n=body.rfind('\n',0,p['offset'])+1
                    prefix=body[n:p['offset']]+prefix
                if md and re.match(r'^\s*(?:#{1,6}\s|[-\w]+:\s|>\s*#{1,6}\s)',prefix):
                    return m[0]
                slots-=1;retained+=1;audit.added_links+=1
                return ANCHOR
            p['s']=re.sub(re.escape(MARK),link_word,segment)
        audit.final_keyword_links=retained
    else:
        audit.final_keyword_links=len(links)
    result=fm+''.join(p['s'] for p in parts)
    if txt and found and URL.rstrip('/') not in result and not path.startswith('PROVENANCE/'):
        # Plain TXT cannot embed clickable labels. Keep an editorial URL outside
        # the source dialogue rather than inserting URLs into attributed turns.
        result=result.rstrip()+'\n\n[Concept reference] '+MARK+' — '+URL+'\n'
        audit.text_reference_added=1
    return result,audit

def safe_external_urls(s):
    # Preserve all non-canonical URL literals, including fragment destinations.
    return Counter(x for x in URL_TOKEN.findall(s) if x.rstrip(').,;')!=URL.rstrip('/') and not re.fullmatch(re.escape(URL.rstrip('/'))+r'/?[),.;]*',x))

def check_fixtures():
    cases=[
        ('sample.md','[Topologetics]({{ \x27/TOPOLOGETICS/\x27 | relative_url }})\n\nTopologetics, Topologetics, Topologetics, Topologetics.'),
        ('sample.html','<html><head><title>Topologetics</title></head><body><nav><a href="/TOPOLOGETICS/">Topologetics</a></nav><main><p>Topologetics / Topologetics / Topologetics / Topologetics.</p><a href="/TOPOLOGETICS/">Topologetics</a></main></body></html>'),
        ('sample.md','---\ntitle: Topologetics\npermalink: /TOPOLOGETICS/\n---\n# Topologetics\n\nTopologetics **Topologetics**.\n\n\`\`\`js\nconst Topologetics=1;\n\`\`\`\n\n[other](https://example.org/Topologetics/file.txt)'),
        ('sample.txt','John: Topologetics\nhttps://example.com/Topologetics/index.md\n'),
        ('MOBILE/data.js','var data = {"title":"Topologetics — example","url":"https://example.com/Topologetics/file.html"};')
    ]
    for p,s in cases:
        t,a=update_text(p,s)
        t2,_=update_text(p,t)
        assert t2==t,(p,t,t2)
        assert safe_external_urls(t)==safe_external_urls(s),(p,s,t)
        if p.endswith('.md') or p.endswith('.html'):
            assert a.final_keyword_links<=3,(p,a)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--report',default='.github/reports/topologetics-audit-2026-11-27.json')
    args=parser.parse_args()
    check_fixtures()
    files=subprocess.check_output(['git','ls-files','-z']).decode('utf-8').split('\0')
    report={'scope':'All tracked Markdown, TXT, HTML/HTM, and selected text/metadata assets; navigation and exact archives protected.',
            'scanned':0,'changed':[],'archive_exceptions':[],'protected_or_unresolved':[],'errors':[]}
    for name in files:
        if not name or Path(name).suffix.lower() not in EXT or name.startswith('.github/'):continue
        p=Path(name)
        try:
            raw=p.read_bytes()
            src=raw.decode('utf-8')
        except (UnicodeError,OSError) as e:
            report['errors'].append({'path':name,'error':str(e)});continue
        report['scanned']+=1
        if not re.search(r'[Tt]opologetics',src):continue
        if EXACT.search(name):
            n=sum(m[0]!=MARK for m in TERM.finditer(src))
            if n:report['archive_exceptions'].append({'path':name,'unmarked':n})
            continue
        result,a=update_text(name,src)
        # Compare every non-canonical URL token. Newly inserted anchors use
        # only the canonical destination. Any other change fails closed.
        if safe_external_urls(result)!=safe_external_urls(src):
            report['errors'].append({'path':name,'error':'Non-canonical URL token comparison differed; source unchanged.'})
            continue
        second,_=update_text(name,result)
        if second!=result:
            report['errors'].append({'path':name,'error':'Idempotence check failed; source unchanged.'})
            continue
        left=sum(m[0]!=MARK for m in TERM.finditer(result))
        if left or (a.final_keyword_links>3 and not name.startswith('_includes/') and Path(name).suffix.lower() in {'.md','.html','.htm'}):
            report['protected_or_unresolved'].append({'path':name,'unmarked_or_technical':left,'existing_special_or_unassembled_links':a.final_keyword_links})
        if result!=src:
            report['changed'].append({'path':name,**asdict(a)})
            if args.write:p.write_bytes(result.encode('utf-8'))
    report['totals']={key:sum(x[key] for x in report['changed']) for key in asdict(Audit())}
    report['changed_count']=len(report['changed'])
    print(json.dumps({k:v for k,v in report.items() if k!='changed'},ensure_ascii=False,indent=2))
    if args.write:
        dest=Path(args.report);dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if report['errors']:
        print('Audit contains exceptions; inspect report before publication.')
    return 0

if __name__=='__main__':raise SystemExit(main())
