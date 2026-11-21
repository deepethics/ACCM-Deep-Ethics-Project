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
| **1. Independent audit** | Give both models the same root source, account under review, and available intermediate versions. Preserve each first pass before either model sees the other’s output. | Exact source wording or a labeled `[Source synthesis]`, changed wording, earliest visible change, possible consequence, and smallest faithful repair. |
| **2. Swap and verify** | Give each model the other’s audit with the same source materials. Check the evidence and the repairs. Identify the smallest passage that can be quoted on its own and any companion rules needed to act. | A verdict and supporting passage for each finding, missed changes, and open questions. |
| **3. Reconcile** | Compare both audits and their verification passes against the source and available versions. Resolve what the record can settle and preserve what remains open. | Final findings, a change log, a standalone corrected passage, and open author questions. |

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

1. Recover the claim. Quote the exact source passage and corresponding
   passage in the account. Preserve the actors, objects, actions, scope,
   and qualifiers. If you combine or paraphrase source passages, label
   the entry [Source synthesis] and give the supporting excerpts.
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
6. Trace the handoff. Name the earliest available version that contains
   each change. Describe what someone might do differently if they acted
   on the later account and whether the source authorizes that action.
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

1. Mark each finding Confirmed, Needs revision, Unsupported, or
   Undecidable from the material provided. Quote the wording that
   supports your verdict. Flag paraphrases presented as verbatim quotes
   and check that the earliest visible version is correctly identified.
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
- Model A audit and Model B’s verification of it
- Model B audit and Model A’s verification of it

1. Compare the findings against the evidence. Record which review passes
   were completed. Use the root source to settle scope and use the
   versions to settle where a change became visible. Label source
   syntheses.
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

### Findings from the exchange

Both Stage 1 passes identified the same four affected rules. Model B recorded its pass before receiving Model A’s response. Model A was supplied as a blind pass. ChatGPT wrote the test packet and then checked both audits against the source. The recorded exchange contains that verification pass.

| Rule | Earliest visible change | Later change |
| --- | --- | --- |
| Drafting | The intermediate version drops **volunteer**. | The final account drops **during the pilot**. |
| Publication | The intermediate version drops the explicit **only after** gate and the explicit link between review and the **version to be published**. | The final account drops the publishing role’s exclusivity and replaces **a second translator** with **a translator**. |
| Keeping subtitles online | The intermediate version omits the timing of the correction request and who reviews it. | The final account changes **may remain** to **should stay** and omits the review interval and where the dated notice must appear. |
| Name corrections | The intermediate version leaves the forwarding actor unstated. | The final account replaces the duty to forward with a coordinator approval requirement. |

**Change after verification.** The explanation of the name-correction repair needed both rules. Forwarding satisfies the name-specific duty. Publication still requires the second-translator review of the release version. An excerpt can state the forwarding duty clearly by itself. A reader deciding whether to publish needs both rules.

**Smallest passage for a name-correction publication decision.**

> Only the language editor may publish translated subtitles, and only after a second translator reviews the version to be published. The language editor must forward requests to correct a speaker’s name to the event coordinator before publishing any revised spelling.

The full standalone repair for all four rules is the root passage above. The source leaves the post-pilot drafting rule and what happens to the dated notice after review open. It also leaves room to clarify whether “any revised spelling” includes a correction made in an unpublished draft before its first release. A coordinator approval requirement would be a policy addition.


## How the method developed {#origin}

John Kuhles brought a [Google A.I. evaluation of the ACCM Deep Ethics Project](https://share.google/aimode/JQoC8NjARKd6a309u) into the exchange. The evaluation cited the new [GitLab mirror](https://accm-deep-ethics-project-043a73.gitlab.io/) and said, “Most governance and content-moderation systems treat the evaluator as infallible.” The cited project homepage could establish the project’s requirement for auditable collaboration. A claim about how most existing systems operate would need evidence about those systems.

Google A.I. acknowledged the overreach and quoted the original scope accurately at the start of its repair. It then described the earlier claim as a generalization about “all existing governance systems.” The repair widened **most** to **all** and dropped the explicit reference to **content moderation**. The two formulations are visible in the supplied exchange. A cause such as pressure for smoother paraphrasing remains a hypothesis.

John carried the replies between Google A.I. and ChatGPT, keeping each response available for the other to inspect. ChatGPT proposed comparing each consequential restatement with the root source and wrote the prompt packet and synthetic Subtitle Archive case. Google A.I. helped develop the numbered workflow, the verification pass, and the worked reconciliations. John selected **Cross-Model Correspondence Audit** as the primary name and requested the public **CMCA™** page.

### When the wording controls an action

An earlier synthetic exercise gave most reviewers permission to view anonymized files until 17:00 Coordinated Universal Time (UTC) on Friday and reserved downloading to the audit lead. A first summary dropped the viewing deadline. A second summary then said “Keep reviewer viewing access open.” Comparing the second summary with the first exposed an instruction replacing a permission. Comparing both with the root source recovered the missing deadline.

In the worked continuation, an emergency freeze suspended viewing while the 24-hour window continued from the case’s reopening. Saying access “resumes automatically” introduced an assumption about software. Saying the user must be assigned to the reopened case after every freeze introduced a different error. The assignment rule applied to the reopening exception after the Friday cutoff. A freeze could also end during the baseline period, when trained reviewers were eligible without that assignment. The example shows how a correction can travel accurately within one case and still need a scope check before becoming a general rule.

## Related project methods {#related}

- [Topologetics™]({{ '/TOPOLOGETICS/' | relative_url }}) follows the consequential relations that need to survive a retelling. The separate check for companion rules asks whether those relations are sufficient for the action a reader intends to take.
- **[DEDDA™]({{ '/DEDDA/' | relative_url }})** (Deep Ethical Drift Detector App) provides a diagnostic lens for the changes a cross-model comparison exposes.
- [OmbudsEthics™]({{ '/OMBUDSETHICS/' | relative_url }}) addresses who can challenge an evaluator’s account and how the challenge can reach a decision.
- [Correction Metabolism]({{ '/NETWORK/correction-metabolism/' | relative_url }}) follows whether a warranted correction survives the next retelling or decision.
