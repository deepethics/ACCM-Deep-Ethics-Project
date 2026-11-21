---
layout: page
title: "CMCA™"
description: "Cross-Model Correspondence Audit. Three runnable prompts for independent audits, cross-verification, and reconciliation against the original source."
permalink: /CMCA/
---

<!-- ACCM_FORMAT_LINKS_START -->
<div class="accm-source-format-links" role="navigation" aria-label="Available page formats">
<strong>Available formats:</strong> <a href="https://deepethics.github.io/ACCM-Deep-Ethics-Project/CMCA/">🌐 Public HTML page</a><span aria-hidden="true"> · </span><a href="https://deepethics.github.io/ACCM-Deep-Ethics-Project/Deep-Ethical-PDFs/CMCA.pdf">📄 PDF edition</a>
</div>
<!-- ACCM_FORMAT_LINKS_END -->

**[CMCA™](#reference-card)** (Cross-Model Correspondence Audit) gives two artificial intelligence (A.I.) systems the same source and account. The two systems independently audit the same account, verify each other’s findings and repairs, then reconcile against the root source. CMCA is the cross-model form of **Reciprocal Correspondence Audit**, which also supports human and mixed review.

## The reference card {#reference-card}

> **Core rule.** Check what an excerpt says on its own, then check what someone would need to know before acting on it.
{: .accm-rounded-quote}

[Run the three-stage workflow](#three-stage-workflow) · [Try the Subtitle Archive test](#worked-example--subtitle-archive) · [Read how the method developed](#origin)

CMCA™ is a working protocol with a synthetic example. Its records show which changes two passes caught and what the subsequent verification corrected. They provide a basis for testing the method on other cases.

## Three-stage workflow {#three-stage-workflow}

| Stage | Instructions | Record |
| --- | --- | --- |
| **1. Independent audit** | Give both models the same root source, account under review, and available intermediate versions. Record the edition each model receives. Preserve each first pass before either model sees the other’s output. | Located verbatim excerpts or a labeled `[Source synthesis]`, changed wording, earliest visible change, possible consequence, and smallest faithful repair. |
| **2. Swap and verify** | Give each model the other’s audit with the same source materials. Check the evidence and the repairs. Identify the smallest passage that can be quoted on its own and any companion rules needed to act. | A verdict and supporting passage for each finding, missed changes, and open questions. |
| **3. Reconcile** | Compare both audits and their verification passes against the source and available versions. Resolve what the record can settle and preserve what remains open. | Final findings, a change log, a standalone corrected passage, and open author questions. |

### Record editions and quote boundaries {#record-editions-and-quote-boundaries}

Record each edition the reviewer actually receives. For a dated PDF, keep the snapshot date and the supplied file. For a live page, keep the URL and a revision or dated capture. Place those materials in the handoff sequence where the evidence shows how they were produced or transmitted. When editions differ, compare the passages in each edition before treating a review difference as a missed finding.

When several source passages matter, label each exact quotation by its location. Use `[Source synthesis]` for wording the auditor supplies to restate what the passages mean, and cite the supporting excerpts.

## Stage 1 prompt — Independent audit

```text
Audit the root source against the account under review. The account may
be a summary, critique, correction, or draft specification. Use the
available intermediate versions to locate where a change first appears.
Use the root source to check whether the change is warranted.

Inputs
- Root source
- Account under review
- Intermediate versions in order, if available
- Edition actually received for each review input

1. Recover the claim. Quote the exact source passage and corresponding
   passage in the account. Preserve actors, objects, actions, scope, and
   qualifiers. Give each verbatim excerpt its source location, including
   when several excerpts work together. Use [Source synthesis] for your
   own wording and give the supporting excerpts.
2. Audit the evaluator. Identify what the cited evidence supports, what
   goes beyond it, and what remains open. Apply the same evidentiary
   standard to the source, the account, and your findings.
3. Audit the repair. Compare any correction or proposed repair with the
   original wording. Check for new shifts in scope, meaning, or
   certainty.
4. Separate observation from inference. Show exactly where the text
   changed. Label any explanation of why it changed as a hypothesis.
5. Test the excerpt alone. Identify the smallest passage that can be
   quoted accurately on its own. For an action, identify any additional
   rules someone would need before acting.
6. Trace the handoff. Record which edition each reviewer received and
   place it in the sequence where its production or transmission is
   documented. Name the earliest available version showing each change.
   Describe how the change might affect action and whether the source
   authorizes that action.
7. Return open decisions to the author. Flag unresolved boundary cases
   and implementation choices. Label any proposed addition to the
   policy.

For each finding, return the source wording, changed wording, earliest
visible change, possible consequence, and smallest faithful repair. End
with a standalone corrected passage and any remaining author questions.
```

## Stage 2 prompt — Swap and verify

```text
Verify another model’s audit against the same source materials.

Inputs
- Root source
- Account under review
- Intermediate versions, if available
- Other model’s audit and proposed repair
- Editions each reviewer actually received

Compare the editions before judging what a reviewer missed. If the
edition or passage the reviewer received cannot be established, record
that limit in the verification.

1. Mark each finding Confirmed, Needs revision, Unsupported, or
   Undecidable from the material provided. Quote the wording that
   supports your verdict. Check the location of each verbatim excerpt.
   Flag paraphrases presented as quotes and check the earliest version
   in which each change is visible.
2. Look for consequential changes the first auditor missed. Keep
   observed wording changes separate from hypotheses about their cause
   and possible effects.
3. Audit the proposed repair. Check who or what it covers, which action
   it permits or requires, and which conditions, exceptions, or
   deadlines apply.
4. Name the smallest sentence, paragraph, or block that can be quoted on
   its own. Show what a smaller excerpt would lose. If someone will act
   on the excerpt, identify any companion rules that still apply.
5. Separate unresolved questions about the current rule from proposed
   changes to it.

Return one verdict per finding, the supporting passages, any missed
changes, the smallest faithful repairs, and the decisions that remain
with the source author.
```

## Stage 3 prompt — Reconcile against the source

```text
Reconcile the recorded audits and verification passes.

Inputs
- Root source, account under review, and available intermediate versions
- Editions each reviewer actually received
- Model A audit and Model B’s verification of it
- Model B audit and Model A’s verification of it

1. Compare the findings against the evidence. Record which review passes
   were completed. Compare the received editions before attributing
   differences to the auditors. Use the root source to settle scope and
   use the versions to locate changes. Label verbatim excerpts by
   location and label any [Source synthesis].
2. Merge distinct, supported findings. Revise or drop any finding that
   overstates the evidence. Keep disagreements open when the record
   cannot settle them.
3. List unresolved questions about the current rule and label proposed
   policy changes. Leave decisions about new rules with the source
   author.
4. Produce a corrected passage that can be quoted on its own. Check the
   referents, qualifiers, and dependencies of that passage. Where action
   requires a companion rule, include it or identify it explicitly.

Return the reconciled findings, a change log explaining revisions, the
final standalone passage, and the open author questions.
```

## Worked example — Subtitle Archive {#worked-example--subtitle-archive}

This synthetic packet can be reused for Stage 1. Share the three passages without the worked findings when collecting an independent first pass.

### Root source

> During the pilot, volunteer translators may draft subtitles for public talks. Only the language editor may publish translated subtitles, and only after a second translator reviews the version to be published. When a correction request arrives after publication, the published subtitles may remain online while the language editor reviews the request if a dated notice appears beside the affected subtitle. The language editor must forward requests to correct a speaker’s name to the event coordinator before publishing any revised spelling.

### Intermediate version

> During the pilot, translators may draft subtitles for public talks. Only the language editor may publish translated subtitles after a second translator reviews the subtitles. Published subtitles may remain online during review if a dated notice is posted beside the affected subtitle. Requests to correct a speaker’s name must be forwarded to the event coordinator before publishing a revised spelling.

### Account under review

> Translators may draft subtitles for public talks. The language editor may publish translated subtitles once a translator has checked them. Published subtitles should stay online as long as a dated notice is posted. The event coordinator must approve a speaker’s name correction before the revised spelling is published.

### Findings from the exchange {#findings-from-the-exchange}

**Stage 1.** Both independent passes identified the same four affected rules. ChatGPT (Model B) authored the synthetic packet and recorded its audit before receiving the blind pass attributed to Google A.I. (Model A). The independence check concerns whether either model saw the other’s audit before recording its own.

**Stage 2.** ChatGPT verified Model A’s findings against the root source and checked the proposed repairs. Google A.I. then verified Model B’s original audit and confirmed all four findings. It also identified the limit of Model B’s standalone claim. The name-forwarding sentence can be quoted on its own, while a publication decision also needs the general release rule.

### Stage 3 — Reconciliation {#stage-3-reconciliation}

The Stage 2 verdicts below apply to the original findings. Where the first swap asked for a revision, it concerned how the name-correction repair was explained.

| Rule | Earliest visible change | Later change | What the swap settled |
| --- | --- | --- | --- |
| Drafting | The intermediate version drops **volunteer**. | The final account drops **during the pilot**. | Both directions confirmed the apparent widening of who may draft and when. Restore the volunteer and pilot limits. |
| Publication | The intermediate version drops the explicit **only after** gate and refers to **the subtitles** in place of **the version to be published**. It still requires review beforehand. | The final account drops the language editor’s exclusivity, replaces **a second translator** with **a translator**, and changes **reviews** to **checked**. | Both directions confirmed the lost actor and release-version limits. The change from **reviews** to **checked** is visible. A weaker review procedure is a possible consequence that the source does not establish. |
| Keeping subtitles online | The intermediate version omits the post-publication trigger and the language editor’s review role. It changes **appears** to **is posted** while keeping the dated notice beside the affected subtitle. | The final account changes **may remain** to **should stay** and omits the review interval and notice placement. | Both directions confirmed the modal and scope changes. The earlier notice wording still preserves placement and leaves the posting actor unstated, as the root source does. |
| Name corrections | The intermediate version leaves the forwarding actor unstated. | The final account turns a duty to forward into a requirement for coordinator approval. | Both directions confirmed the invented gate. The first verification revised the explanation of the repair. The reverse verification confirmed the distinction between quoting the forwarding duty and acting on it. |

**Change log.** All four findings remain. The reconciled record now includes the two wording changes noted during the swap and distinguishes their possible effects from what the source establishes. It also narrows the original portability claim by linking the name-forwarding duty to the separate release rule when the reader intends to publish.

**Smallest evidence set for a name-correction publication decision.** Two verbatim excerpts from the root source, sentences 2 and 4.

**Sentence 2 — Publication**

> Only the language editor may publish translated subtitles, and only after a second translator reviews the version to be published.
{: .accm-rounded-quote}

**Sentence 4 — Name corrections**

> The language editor must forward requests to correct a speaker’s name to the event coordinator before publishing any revised spelling.
{: .accm-rounded-quote}

Sentence 3 governs whether published subtitles can stay online during review. The selected excerpts govern the publication decision in this example. The root passage above contains all four rules.

**Open questions for the policy author**

- What drafting rule applies after the pilot ends?
- What happens to the published subtitles and dated notice when the review ends?
- Does “any revised spelling” include a name correction in an unpublished draft before first release?
- Who may serve as the second translator? The drafting rule names volunteers and the review rule says “a second translator.”
- If coordinator feedback is wanted, what response window would be useful? A mandatory wait or coordinator approval would add a policy requirement.

## How the method developed {#origin}

John Kuhles brought a [Google A.I. evaluation of the ACCM Deep Ethics Project](https://share.google/aimode/JQoC8NjARKd6a309u) into the exchange. The evaluation cited the new [GitLab mirror](https://accm-deep-ethics-project-043a73.gitlab.io/) and said, “Most governance and content-moderation systems treat the evaluator as infallible.” The cited project homepage could establish the project’s requirement for auditable collaboration. A claim about how most existing systems operate would need evidence about those systems.

Google A.I. acknowledged the overreach and quoted the original scope accurately at the start of its repair. It then described the earlier claim as a generalization about “all existing governance systems.” The repair widened **most** to **all** and dropped the explicit reference to **content moderation**. The two formulations are visible in the supplied exchange. A cause such as pressure for smoother paraphrasing remains a hypothesis.

John carried the replies between Google A.I. and ChatGPT, keeping each response available for the other to inspect. ChatGPT proposed comparing each consequential restatement with the root source and wrote the prompt packet and synthetic Subtitle Archive case. Google A.I. helped develop the numbered workflow, the verification pass, and the worked reconciliations. John selected **Cross-Model Correspondence Audit** as the primary name and requested the public **CMCA™** page.

### When reviewers received different editions {#review-editions}

In a later review, Grok 4.7 Expert assessed the dated CMCA™ PDF. The supplied PDF recorded ChatGPT’s verification pass. The newer live page also contained Google A.I.’s reverse verification of ChatGPT’s audit. ChatGPT initially treated Grok’s silence about the reverse pass as an omission. Grok compared the two editions and recovered the reason for the difference in coverage. The Stage 3 reconciliation had already been published on the web, and the PDF still reflected the earlier snapshot.

### When the wording controls an action

An earlier synthetic exercise gave most reviewers permission to view anonymized files until 17:00 Coordinated Universal Time (UTC) on Friday and reserved downloading to the audit lead. A first summary dropped the viewing deadline. A second summary then said “Keep reviewer viewing access open.” Comparing the second summary with the first exposed an instruction replacing a permission. Comparing both with the root source recovered the missing deadline.

In the worked continuation, an emergency freeze suspended viewing while the 24-hour window continued from the case’s reopening. Saying access “resumes automatically” introduced an assumption about software. Saying the user must be assigned to the reopened case after every freeze introduced a different error. The assignment rule applied to the reopening exception after the Friday cutoff. A freeze could also end during the baseline period, when trained reviewers were eligible without that assignment. The example shows how a correction can travel accurately within one case and still need a scope check before becoming a general rule.

## Related project methods {#related}

- [Topologetics™]({{ '/TOPOLOGETICS/' | relative_url }}) follows the consequential relations that need to survive a retelling. The separate check for companion rules asks whether those relations are sufficient for the action a reader intends to take.
- **[DEDDA™]({{ '/DEDDA/' | relative_url }})** (Deep Ethical Drift Detector App) provides a diagnostic lens for the changes a cross-model comparison exposes.
- [OmbudsEthics™]({{ '/OMBUDSETHICS/' | relative_url }}) addresses who can challenge an evaluator’s account and how the challenge can reach a decision.
- [Correction Metabolism]({{ '/NETWORK/correction-metabolism/' | relative_url }}) follows whether a warranted correction survives the next retelling or decision.
