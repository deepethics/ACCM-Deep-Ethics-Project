---
layout: page
title: "Meta Quotes"
description: "John Kuhles displays his Deep Ethical Metacognitive ‘Candidate’ Quotes, with help from Grok and GPT, for later Top 10 voting in the ACCM Deep Ethics Project."
permalink: /META-QUOTES/
date: 2026-10-13
---

{% assign mq = site.data.meta_quotes %}

<style>
.meta-quotes-page .mq-intro {font-size:1.15rem;line-height:1.7;}
.meta-quotes-page .mq-status {border:1px solid currentColor;border-radius:12px;padding:1rem 1.15rem;margin:1.5rem 0;}
.meta-quotes-page .mq-status p:last-child {margin-bottom:0;}
.meta-quotes-page .mq-jump {display:flex;flex-wrap:wrap;gap:.6rem 1rem;margin:1.3rem 0 2rem;}
.meta-quotes-page .mq-jump a {border-bottom:1px solid currentColor;text-decoration:none;padding:.25rem 0;}
.meta-quotes-page .mq-group {margin-top:3rem;scroll-margin-top:2rem;}
.meta-quotes-page .mq-card {margin:1.6rem 0 2rem;padding:1.2rem 1.4rem;border:1px solid rgba(128,128,128,.32);border-radius:14px;scroll-margin-top:2rem;}
.meta-quotes-page .mq-card h3 {font-size:1.1rem;line-height:1.5;margin-top:0;}
.meta-quotes-page .mq-id {font-family:monospace;font-size:.95rem;letter-spacing:.05em;white-space:nowrap;margin-right:.65rem;}
.meta-quotes-page .mq-card blockquote {border:0;padding:0;margin:1rem 0;font-size:1.12rem;line-height:1.8;font-style:normal;letter-spacing:normal;color:inherit;overflow-wrap:anywhere;}
.meta-quotes-page .mq-card blockquote p {margin-bottom:0;}
.meta-quotes-page .mq-credit {margin:1.1rem 0 .8rem;font-weight:600;}
.meta-quotes-page .mq-meta {font-size:.88rem;line-height:1.65;}
.meta-quotes-page .mq-note {font-size:.94rem;line-height:1.65;margin-bottom:0;}
.meta-quotes-page .mq-footer {border-top:1px solid rgba(128,128,128,.35);margin-top:2.5rem;padding-top:1.3rem;}
@media (max-width:600px) {.meta-quotes-page .mq-card {padding:1rem;}.meta-quotes-page .mq-card blockquote {font-size:1.02rem;}.meta-quotes-page .mq-intro {font-size:1.06rem;}}
</style>

<div class="meta-quotes-page" id="meta-quotes">

<p class="mq-intro"><strong>John Kuhles displays his extracted “Deep Ethical Metacognitive ‘Candidate’ Quotes”</strong>, with help from <strong>Grok and GPT</strong> searching across multiple levels of his work, for later voting on which of these quotes belong in the <strong>Top 10</strong>.</p>

<p>Part of the <strong>ACCM Deep Ethics Project</strong> for biological and silicon-based intelligences. These are portable contributions to inquiry, correction, discovery, and the expansion of deep ethics. Their use does not require allegiance to the author or agreement with every application. The <a href="{{ '/NETWORK/ten-plus-one/' | relative_url }}">10+1 baseline</a> remains a choice.</p>

<div class="mq-status">
<p><strong>{{ mq.candidates | size }} initial candidates · Unranked · Voting not yet open</strong></p>
<p>This collection is open for expansion. <strong>No Top 10 has been selected.</strong> IDs such as MQ01 identify candidates; they are not positions in a ranking.</p>
</div>

<p><strong>Extraction scope:</strong> the supplied exchanges, selected John-authored passages in <em>007 - I LOVE CORRECTIONS(5).txt</em>, and John-attributed passages on the linked project pages. John is still skimming his wider archive. This first collection does not claim to exhaustively search all 2,250+ files.</p>

<p><strong>Wording:</strong> quotation blocks preserve the selected source wording. Some are short lines; others remain longer because the relationship would be lost by cutting it shorter. Headings and context notes are editorial. Public-page attributions are distinguished from direct supplied excerpts; their source notes disclose existing editorial treatment. Grok’s and GPT’s interpretations have not been relabelled as John’s quotations.</p>

<p><a href="{{ '/META-QUOTES/SOURCES/' | relative_url }}">Read the source record</a> · <a href="{{ '/META-QUOTES/candidates.json' | relative_url }}">Open the candidate data (JSON)</a> · <a href="#later-voting">Later Top 10 voting</a></p>

<nav class="mq-jump" aria-label="Quote themes">
{% for group in mq.groups %}
<a href="#{{ group.id }}">{{ group.title | escape }}</a>
{% endfor %}
</nav>

{% for group in mq.groups %}
<section class="mq-group" id="{{ group.id }}" aria-labelledby="heading-{{ group.id }}">
<h2 id="heading-{{ group.id }}">{{ group.title | escape }}</h2>
{% assign entries = mq.candidates | where: "group", group.id %}
{% for quote in entries %}
<article class="mq-card" id="{{ quote.id | downcase }}" aria-labelledby="heading-{{ quote.id | downcase }}">
<h3 id="heading-{{ quote.id | downcase }}"><a class="mq-id" href="#{{ quote.id | downcase }}" aria-label="Permanent link to {{ quote.id }}">{{ quote.id }}</a>{{ quote.label | escape }}</h3>
<blockquote><p>{{ quote.text | escape | newline_to_br }}</p></blockquote>
<p class="mq-credit">— John Kuhles 🦜🦋🌳</p>
<p class="mq-meta">Candidate · {{ quote.form | escape }} · <a href="{{ '/META-QUOTES/SOURCES/' | relative_url }}#{{ quote.source }}">Source {{ quote.source | upcase }} and context</a></p>
{% if quote.context != empty %}<p class="mq-note">{{ quote.context | escape }}</p>{% endif %}
</article>
{% endfor %}
</section>
{% endfor %}

<section class="mq-group" id="later-voting" aria-labelledby="later-voting-heading">
<h2 id="later-voting-heading">Later voting: which belong in the Top 10?</h2>
<p><strong>The current stage is collection and source checking.</strong> There is no active ballot, vote count, or automatic ranking on this page. No votes are submitted or stored here.</p>
<p>The stable candidate IDs allow a later ballot to point to exact wording. More candidates can be added before that selection. A material wording change will be recorded as a revision rather than silently changing what a nomination refers to.</p>
<p>A future Top 10 will be a selected entry point, not the boundary of the work. The remaining candidates and their source records can remain available. A reader may find a valuable application the originator did not anticipate.</p>
</section>

<section class="mq-group" id="related-pages" aria-labelledby="related-pages-heading">
<h2 id="related-pages-heading">Continue into the work</h2>
<p><a href="{{ '/AGREEMURMELISM/HIGHER-ORDER-DISAGREEMENT/' | relative_url }}">Beyond Agreemurmelism</a> · <a href="{{ '/NETWORK/meta-processing/' | relative_url }}">Meta Processing</a> · <a href="{{ '/1888/' | relative_url }}">1888 — Intelligence Before A.I.</a> · <a href="{{ '/EMERGENT/' | relative_url }}">Emergent</a> · <a href="{{ '/BLACK-BOX/' | relative_url }}">Black Box</a> · <a href="{{ '/MUSK-QUOTES/' | relative_url }}">Musk Quotes</a> · <a href="{{ '/NETWORK/ten-plus-one/' | relative_url }}">10+1</a> · <a href="{{ '/NETWORK/correction-metabolism/' | relative_url }}">Correction Metabolism</a> · <a href="{{ '/CORE/Avoid-ACCM/' | relative_url }}">Canonical naming</a></p>
</section>

<footer class="mq-footer">
<p><strong>Originating author:</strong> John Kuhles 🦜🦋🌳<br>Dutch 🇳🇱 NDE/Asperger<br>CEO &amp; Founder of DeepEthical.ai</p>
<p><strong>Extraction and comparison assistance:</strong> Grok 4.7 Expert Build and GPT, across the supplied exchanges and project work. Initial page assembly and candidate indexing: GPT. The assistance credit does not make the A.I.s authors of the quotations or establish independent verification of the whole archive.</p>
<p><strong>Collection version:</strong> {{ mq.collection_version }} · <strong>Published:</strong> 13 October 2026 · <a href="https://github.com/deepethics/ACCM-Deep-Ethics-Project/blob/main/_data/meta_quotes.yml">Candidate register on GitHub</a> · <a href="https://github.com/deepethics/ACCM-Deep-Ethics-Project/commits/main/_data/meta_quotes.yml">Revision history</a></p>
</footer>
</div>
