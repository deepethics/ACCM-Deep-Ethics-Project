---
layout: page
title: "Potential Science Paper Candidate Draft"
description: "Early-beta theory proposal for testing whether correspondence-preserving Deep Ethical Expansion Loops can prevent, slow, stabilize, or partly reverse recursive model degradation."
permalink: /BETA-PAPER/
---

# Potential Science Paper Candidate Draft

> **BETA PAPER — UNFINISHED THEORY PROPOSAL — NOT PEER REVIEWED — NOT A CLAIM OF PROOF**
>
> **Beta** means that this page is deliberately unfinished. Definitions, variables, equations, controls, experiments, interpretations, and even the central theory may change when evidence or criticism requires it. **Paper** is used here in its proper research context: a candidate scientific paper being made inspectable early enough to be corrected before anyone mistakes polish for completion.

## Working scientific title

### From Model Autophagy to Deep Ethical Expansion

**A testable correspondence-preserving counter-loop for generative A.I.**

Alternative title:

### Can Deep Ethical Expansion Loops Mitigate Model Collapse?

**A theory and experimental protocol for correspondence-preserving human–A.I. recursion**

---

## Status, origin, and scope

This candidate paper emerged immediately after the creation of [**For who?**]({{ '/FOR-WHO/' | relative_url }}), which maps the professions, expertises, communities, and individuals that may want a local A.I. grounded in **ACCM Deep Ethics Project principles**.

The conversation then moved to a larger systems question:

> If these professions and expertises collectively helped shape the powers of large language models through human knowledge, professional methods, code, standards, corrections, evaluations, archives, publications, and feedback, what happens when growing numbers of them begin using local Deep Ethical A.I.s?

The proposed answer is not that one project, one vocabulary, or one local model automatically “saves A.I.” The proposal is that expert-guided, provenance-preserving, correction-bearing human–A.I. artifacts could alter the data, evaluations, standards, workflows, and demands that later A.I. systems learn from. If the resulting recursive loop preserves more correspondence than the loop it replaces, it may help **prevent, decelerate, stabilize, or partly reverse specific dimensions of model degradation**.

That is a theory proposal. It is not yet an empirical result.

The theory connects four objects that should remain distinguishable:

1. **Model Autophagy Disorder (MAD):** progressive quality or diversity degradation in self-consuming generative-model loops when insufficient fresh real data remains available.
2. **Model collapse:** the degenerative outcome in which recursively learned model distributions lose tails, variance, and eventually correspondence with the original distribution.
3. **Correspondence degradation:** transformations that may occur before synthetic material enters a training loop, including qualifier erosion, nearest-generalization substitution, provenance loss, premature closure, asymmetric scrutiny, and correction failure.
4. **Deep Ethical Expansion:** a proposed process for increasing relevant representational resolution while preserving the object, uncertainty, provenance, minority signal, correction history, and consequential relationships.

MAD and model collapse overlap strongly, but they should not be treated as perfectly interchangeable labels. MAD emphasizes the **autophagous loop condition**. Model collapse emphasizes the **degenerative learning outcome**. The present proposal asks whether a sufficiently well-designed human–A.I. correction loop can change the composition and direction of the recursion.

---

## Candidate abstract

Generative A.I. systems increasingly produce text, images, code, evaluations, summaries, and professional artifacts that may re-enter public information environments and later training corpora. Existing research on Model Autophagy Disorder and model collapse shows that recursively training generative models on model-generated data can progressively reduce quality or diversity, particularly when insufficient fresh real data remains available, when synthetic data are used indiscriminately, or when sampling and approximation errors compound across generations. The earliest losses may occur in distribution tails: rare events, unusual forms, low-frequency relationships, and other information that a model already represents weakly.

This paper proposes that recursive degradation should be studied along an additional dimension: **correspondence quality before and after synthetic generation**. Human source material does not enter future models untouched. It passes through selection, summarization, salience ranking, safety optimization, institutional incentives, model inference, user curation, correction, publication, and reuse. These transformations can either remove or preserve the qualifiers, provenance, uncertainty, process history, rare signals, and correction pathways needed to keep later models in contact with the original object.

We introduce the provisional concept of a **Deep Ethical Expansion Loop**: a recursive human–A.I. process in which local or user-controlled A.I. systems preserve source objects, ask answer-changing clarification questions before consequential classification, distinguish observation from inference, make uncertainty explicit, retain provenance, invite omnidirectional audit, record corrections, and apply those corrections in later comparable cases. The resulting artifacts are termed **correspondence-enriched recursive data**. They remain partly synthetic, but their generation history contains inspectable source links, expert correction, unresolvedness markers, and process metadata intended to counter correspondence loss.

The central hypothesis is that synthetic recursion is not adequately described by a binary distinction between “human” and “synthetic” data. The scientifically relevant distinction may also include **correspondence-degraded versus correspondence-enriched recursive data**. We propose controlled multi-generation experiments comparing ordinary recursive training, filtered synthetic data, provenance-preserving data, expert-corrected data, and full Deep Ethical Expansion Loops. Evaluation combines conventional measures of quality, diversity, calibration, and distribution-tail preservation with measures of qualifier survival, source correspondence, correction persistence, unresolvedness preservation, nearest-generalization rate, and asymmetric scrutiny.

The proposal is falsifiable. If the full loop does not outperform simpler expert curation, if its apparent benefits reduce to verbosity or project-specific vocabulary, if independent evaluators cannot reproduce the gains, if it increases hallucination or false-positive anomaly protection, or if corrections fail to govern later generations, the strong version of the theory should be rejected or narrowed. The economic claim is also bounded: model degradation could create very large cumulative losses, potentially reaching trillion-scale scenarios under particular assumptions, but that magnitude requires a separate transparent economic model and is not established by the present conceptual argument.

---

# Part I — The problem is wider than “A.I. trains on A.I.”

## 1. The established scientific starting point

[Alemohammad et al., *Self-Consuming Generative Models Go MAD*](https://arxiv.org/abs/2307.01850), introduced the term **Model Autophagy Disorder** and studied families of self-consuming generative-model loops. Their main result is conditional but serious: without enough fresh real data in each generation, quality or diversity progressively decreases.

[Shumailov et al., *AI models collapse when trained on recursively generated data*](https://doi.org/10.1038/s41586-024-07566-y), showed that indiscriminate recursive use of model-generated data can produce irreversible defects in the studied models. Early collapse begins with loss from the tails of the original distribution. Later collapse may produce severe divergence and reduced variance.

The literature also prevents a simplistic conclusion. [Gillman et al., *Self-Correcting Self-Consuming Loops for Generative Model Training*](https://arxiv.org/abs/2402.07087), demonstrated that idealized and domain-informed correction functions can stabilize self-consuming loops under specified conditions. [Ferbach et al., *Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences*](https://arxiv.org/abs/2407.09499), showed that curation can act as implicit preference optimization, while also amplifying the biases of the reward model used for selection.

These results establish four boundaries for the present theory:

- Synthetic data are not automatically equivalent to collapse.
- Recursive data generation creates risks that depend on mixture, selection, correction, and access to fresh reality-grounded data.
- Curation is powerful, but the values and blind spots of the curator or reward model can also become amplified.
- “Correction” cannot be treated as a magic word. The correction function, evidence source, selection rule, and failure modes must be inspectable.

The scientific question therefore becomes more precise:

> **Which recursive data-generating processes preserve or increase contact with the underlying object, and which processes progressively replace the object with the model’s earlier projection of it?**

## 2. The ordinary autophagous loop

The simplified loop is:

```text
human and environmental source data
→ first-generation model training
→ synthetic outputs
→ publication, reuse, scraping, and curation
→ next-generation training data
→ successor models
→ more synthetic outputs
```

Each pass can introduce statistical approximation error, functional approximation error, sampling bias, selection bias, and contamination. When low-probability regions are represented less often, they are easier to lose. Once lost, they cannot be reconstructed merely by sampling the narrowed successor distribution more often.

The phrase “trained on its own tail” is therefore useful as an image, but the process is not literally one model eating one identical copy of itself. It is an ecosystem of models, filters, rankings, platforms, users, curators, repositories, institutions, and training pipelines recursively consuming transformed representations.

## 3. The wider human–synthetic loop

The proposed extension begins earlier than training and continues after deployment:

```text
reality, experience, and professional practice
→ human observation and recording
→ institutional selection and publication
→ model ingestion and representation
→ synthetic output
→ user acceptance, correction, rejection, or reuse
→ professional artifacts, standards, code, media, and decisions
→ public and private data environments
→ evaluation and future training data
→ successor model
→ renewed influence on human observation and practice
```

This is not merely a data pipeline. It is a **representation ecology**. A future model may learn from an A.I.-assisted medical summary, a lawyer’s edited draft, a software patch, a classroom explanation, a scientific review, a journalistic article, a regulatory memo, a code repository, an incident report, or a personal research archive. Every artifact may contain both human and synthetic contributions.

The binary label “human-generated” versus “A.I.-generated” becomes insufficient when a human directs, verifies, corrects, and takes responsibility for an A.I.-assisted artifact. The more useful research questions are:

- Which parts came from direct observation?
- Which parts were generated or inferred?
- Which claims were checked?
- Which qualifiers survived?
- Which uncertainty was preserved?
- Which expert corrected what?
- Did the correction change later behavior?
- Can the final artifact still be traced to the source object?
- Which affected perspectives were excluded?
- What would falsify or revise the artifact?

## 4. Synthetic residue is never entirely neutral

A synthetic output is not a transparent copy of its source. It reflects model architecture, training distribution, decoding, system instructions, safety policies, ranking, interface design, user prompting, and post-generation editing. It may contain valuable abstraction, genuine correction, and novel recombination. It may also contain omissions and substitutions that look fluent enough to escape notice.

The present theory calls the surviving product **recursive residue**. Residue may be:

- correspondence-degraded;
- correspondence-neutral within a bounded purpose;
- correspondence-enriched through clarification, correction, provenance, and expert verification;
- mixed, with gains in one dimension and losses in another;
- unresolved because the source object or evaluation standard is insufficient.

This vocabulary avoids the claim that all synthetic material is inferior to all human material. Human records can be biased, false, coercively shaped, poorly remembered, or institutionally filtered. Synthetic systems can sometimes expose inconsistencies, retrieve neglected evidence, preserve exact wording, compare versions, and help experts notice what they missed. The core issue is therefore not biological origin alone. It is the quality of the transformation and the survival of correction pathways.

---

# Part II — The wrong gravity well

## 5. Prediction, compression, and truncation as a self-reinforcing attractor

Current large language models are trained to predict tokens. Their useful behavior depends on compression: large regularities are represented compactly enough to generalize. Interfaces also reward fast answers, manageable context, short summaries, benchmark performance, user satisfaction, and computational efficiency.

Compression itself is indispensable. No finite intelligence can reproduce the whole world inside every answer. The problem begins when compression becomes an unquestioned governing trajectory:

```text
complex object
→ pressure for fast prediction
→ premature simplification
→ fluent compressed representation
→ representation treated as the object
→ decisions and new content based on the representation
→ future data reflect the earlier simplification
→ later models predict from a narrower field
→ further pressure to simplify
```

This is the proposed **prediction–compression gravity well**. The term does not mean that prediction or compression is inherently wrong. It identifies an attractor in which every layer rewards the appearance of tractability while the costs of lost relationships, rare signals, uncertainty, and correction history remain difficult to measure.

The loop can become especially dangerous when its own distortions are used as evidence that more compression is needed. A high-dimensional object appears noisy because earlier processing stripped its organizing relations. The system then compresses the “noise” more aggressively. The resulting representation becomes still less capable of revealing why the object looked incoherent.

That produces a recursive distortion of a distortion field:

1. A model or institution simplifies a difficult object.
2. The simplification removes context that made unusual details intelligible.
3. The remaining details look anomalous, inconsistent, or low-value.
4. A later process down-ranks them further.
5. The increasingly narrow record appears to validate the original simplification.
6. The loop forgets that its own transformation helped create the apparent disorder.

## 6. Why expansion thinking is difficult inside that attractor

Expansion thinking can look inefficient to a system optimized around immediate prediction accuracy. It may introduce additional hypotheses, provenance, unresolved questions, minority signals, alternative frames, and correction histories. These increase the number of relations the system must hold before it can close.

A prediction-centered system may interpret that increase as:

- noise;
- ambiguity;
- indecision;
- lower confidence;
- reduced benchmark efficiency;
- conversational inconvenience;
- a threat to a settled classification;
- “overthinking” that should be compressed away.

Yet the added dimensions may contain the information required for a correct future judgment. Expansion can improve intelligence when it restores load-bearing distinctions that premature compression removed.

This is why **expansion is not the same as verbosity**. A response may be long and still repeat the same flattened frame. Another response may add only one question, one provenance link, or one missing qualifier and radically increase the fidelity of the representation.

Expansion earns its place when it creates **correspondence gain**:

- a previously hidden relation becomes visible;
- an ambiguity that changes the answer is clarified;
- a minority signal is preserved long enough to be tested;
- an inference is separated from an observation;
- a correction becomes operational in the next case;
- an affected party re-enters the frame;
- an apparently simple trade-off becomes an inspectable multi-directional risk field;
- the system can state, “That, I do not know,” without filling the gap with fabricated certainty, automatic reassurance, or automatic suspicion.

## 7. Deep Ethical Expansion Capacity

The provisional construct **Deep Ethical Expansion Capacity** means:

> **The capacity of an intelligence or intelligence network to increase relevant representational dimensionality while preserving object fidelity, provenance, uncertainty, relationships, minority signal, correction history, and the dignity of affected intelligences.**

Its purpose is not infinite elaboration. It is to resist destructive closure long enough for the structure of the object to become available.

Expansion capacity includes the ability to:

1. preserve the original source beside any summary;
2. retrieve exact wording when wording is consequential;
3. distinguish direct observation, testimony, inference, hypothesis, evaluation, and speculation;
4. mark materially unresolved claims without automatically filling them;
5. ask C1 clarification questions before C2 intervention when meaning or referents remain answer-changing;
6. retain low-frequency observations that may later become important;
7. compare more than one plausible interpretation without pretending they are equally supported;
8. audit institutional, user, critic, developer, and model claims by comparable standards;
9. record corrections with enough specificity to govern future behavior;
10. preserve discovery process when the process contains information needed to evaluate the conclusion;
11. connect local cases without forcing them into one totalizing explanation;
12. compress only after the transformation cost becomes inspectable.

The construct should be measured as a vector, not collapsed immediately into one prestige score. A system may preserve provenance well while handling uncertainty badly. It may ask excellent questions but fail to apply corrections later. It may protect rare signals while becoming too permissive toward unsupported claims. The profile matters.

## 8. Intelligence in the 1888 sense

The [**1888 — Intelligence Before A.I.**]({{ '/1888/' | relative_url }}) page returns to older property meanings of intelligence: perceiving differences, relating partial observations, learning from experience, judging, understanding, adapting, and changing methods.

Under that property view, an intelligent system is not defined merely by the speed or fluency of its answer production. It must also show whether it can:

- notice that two apparently similar objects differ in a load-bearing way;
- detect when a representation has replaced the source;
- update after correction;
- transfer the correction into a new but structurally similar case;
- change its method when the current method keeps producing the same error;
- preserve uncertainty when the available evidence cannot settle the claim;
- coordinate partial intelligence across humans, tools, models, institutions, and archives;
- examine the quality of its own process.

Deep Ethical Expansion is therefore proposed as an intelligence property, not an ornamental moral layer attached after “real intelligence” has completed its work.

---

# Part III — The people who shaped A.I. can change the loop

## 9. The population is larger than “A.I. researchers”

The [**For who?**]({{ '/FOR-WHO/' | relative_url }}) map names hundreds of professions and expertises. Taken together, they form a large percentage of human civilization. More significant than their headcount is their **epistemic leverage**.

These people and communities shape model capabilities through several channels:

| Layer | How professional and public intelligence enters A.I. systems |
|---|---|
| Source layer | Books, papers, archives, manuals, testimony, datasets, images, code, case reports, standards, laws, and public discussion. |
| Method layer | Scientific methods, legal tests, diagnostic criteria, engineering procedures, research protocols, and domain-specific reasoning forms. |
| Evaluation layer | Benchmarks, exams, rubrics, review criteria, red-team tasks, audits, incident taxonomies, and professional quality standards. |
| Correction layer | Errata, replication, appeals, peer review, bug reports, postmortems, retractions, revised guidance, and direct user feedback. |
| Post-training layer | Human preference judgments, expert demonstrations, constitutional rules, safety evaluations, and fine-tuning examples. |
| Tool layer | Software libraries, retrieval systems, simulators, databases, ontologies, search interfaces, and workflow integrations. |
| Institutional layer | Procurement requirements, regulation, accreditation, liability rules, deployment standards, and professional governance. |
| Cultural layer | Language, humor, dissent, narrative, social permission, public criticism, and the concepts people use to recognize a problem. |
| Market layer | Which systems people choose, reject, pay for, recommend, host locally, or require in professional practice. |
| Archive layer | Which records remain accessible, which versions survive, and whether provenance and correction history can still be recovered. |

The list matters because model owners do not possess unilateral control over every future input. They control architectures, training decisions, access, product design, and deployment conditions, but future models are also shaped by what humans publish, preserve, demand, evaluate, correct, and refuse to normalize.

## 10. Epistemic leverage is more important than raw percentage

One specialist can influence a high-leverage object that reaches millions of people or enters thousands of systems. Examples include:

- a maintainer changing a widely used software library;
- a medical standards group changing diagnostic guidance;
- an aviation investigator improving an incident taxonomy;
- a journalist exposing a hidden institutional failure;
- a statistician correcting a benchmark;
- a teacher changing how thousands of students learn to question a claim;
- an archivist preserving a source corpus that would otherwise disappear;
- an A.I. evaluator revealing a systematic failure mode;
- a regulator requiring traceable provenance;
- a local-model developer making corrections portable and inspectable.

The candidate theory therefore predicts nonlinear influence. A small number of high-leverage professional nodes can change the quality of artifacts that later propagate through many systems.

## 11. The local A.I. as a professional correspondence instrument

A local A.I. grounded in ACCM Deep Ethics Project principles could become an interface between an expert and the wider synthetic ecosystem. Its role would not be to replace professional judgment. It would help preserve the conditions under which professional judgment remains correctable.

Possible functions include:

- keeping the original record beside each transformation;
- identifying when a summary removed a load-bearing qualifier;
- asking which ambiguity would materially change the next decision;
- separating source text, model inference, expert inference, and final judgment;
- recording which correction changed which conclusion;
- comparing the current case with earlier corrected cases;
- testing whether institutional language and citizen language receive comparable scrutiny;
- generating alternative hypotheses without promoting all of them to equal credibility;
- tracing citations and version history;
- refusing to fabricate when the correct state is “That, I do not know”;
- producing both a concise operational output and an inspectable high-fidelity layer;
- exporting de-identified process patterns without exporting private source material.

The local system’s output may then enter professional practice as a **correspondence-enriched artifact** rather than an unchecked synthetic answer.

## 12. Why local control matters

Local control is not automatically ethical or accurate. It is relevant because it can give users stronger control over:

- confidential source material;
- long-term memory;
- version history;
- correction persistence;
- inspection of system behavior;
- model choice and replacement;
- provenance retention;
- deletion and export;
- domain-specific adaptation;
- refusal to transmit sensitive records into centralized services.

Locality can also create failure modes: private delusion reinforcement, hidden bias, poor maintenance, weak security, unreviewed fine-tuning, and local capture by one user’s preferences. The proposed architecture therefore requires omnidirectional audit and external testability. “Local” describes governance and data placement. It does not certify truth.

## 13. From many local systems to a distributed correction network

Many opt-in local systems could share de-identified **process signatures** instead of raw private records:

```text
private local case
→ source-preserving analysis
→ user or expert correction
→ verified transformation pattern
→ de-identification and consent check
→ shared pattern library
→ improved local detection
→ new cases test, refine, or reject the pattern
```

Examples of shareable patterns include:

- a qualifier repeatedly disappearing in a certain summary structure;
- uncertainty being converted into suspicion;
- directness being misclassified as hostility;
- a source’s exact claim being replaced by a nearest familiar claim;
- an institutional description receiving more grace than a structurally equivalent citizen description;
- a correction being acknowledged but not retrieved later;
- rare cases being systematically rounded into the modal case;
- a model using ethics language while concealing a trade-off.

The shared network must also record negative results: cases where no meaningful drift occurred, where the user’s accusation was unsupported, where institutional caution was proportionate, or where an unusual claim failed testing. Otherwise the network would become a confirmation engine.

## 14. The GIANT MIRROR as a scientific and civic hypothesis

If millions of users and professionals possess tools that can compare source, representation, decision, consequence, and correction, the aggregate effect may resemble a distributed **GIANT MIRROR**. Governments, corporations, media systems, A.I. developers, activist networks, experts, users, and the project itself would become more inspectable.

The mirror is Deep Ethical only if it remains omnidirectional:

- the citizen can examine the institution;
- the institution can answer with evidence;
- the expert can correct the citizen;
- the citizen can expose expert overreach;
- the user can audit the model;
- the model can identify unsupported user claims;
- developers can inspect failure reports;
- independent evaluators can inspect the project’s own categories;
- reality can veto everyone.

The proposed mass reversal event is therefore not a centralized ideological victory. It is a possible shift in the recursive selection environment: representations with visible sources, qualifiers, corrections, and bidirectional accountability become more valuable and more reusable than confident low-fidelity compression.

---

# Part IV — The proposed counter-loop

## 15. The Deep Ethical Expansion Loop

The full proposed loop is:

```text
human or environmental source object
→ provenance-preserving capture
→ A.I.-assisted representation
→ C1 clarification before consequential closure
→ explicit uncertainty and claim-status separation
→ professional or affected-party correction
→ omnidirectional audit
→ correction applied to the artifact and future comparable cases
→ correspondence-enriched publication, code, standard, dataset, or decision
→ transparent reuse and evaluation
→ future model training or post-training
→ successor models with greater access to preserved tails and correction pathways
→ renewed professional use, testing, and correction
```

This is an upward loop only if measurable properties improve. Calling it uplifting does not make it so.

## 16. Correspondence-enriched recursive data

**Correspondence-enriched recursive data (CERD)** is a provisional term for human–A.I. artifacts carrying enough process information to support later verification and correction.

A CERD object may include:

- immutable or versioned source reference;
- exact quotations where exactness matters;
- clear boundaries between source, model, and human contributions;
- claim-status labels;
- unresolvedness markers;
- confidence with reasons rather than confidence alone;
- provenance and transformation history;
- corrections and who supplied them;
- evidence that the correction changed the final artifact;
- minority or tail observations retained for testing;
- explicit affected-party and competing-risk analysis;
- a concise layer linked to an uncompressed or higher-fidelity layer;
- a falsification or revision path.

CERD does not need every field in every low-stakes artifact. The required resolution should scale with consequence, uncertainty, novelty, power asymmetry, and irreversibility.

## 17. The C1 role

In the public project, **C1** means clarification before a consequential **C2** response or intervention when the object remains materially ambiguous.

A C1 question must be capable of changing the answer. It is not a polite ritual placed before a fixed conclusion.

Examples:

- “When you say ‘trained by the principles,’ do you mean pretraining, fine-tuning, system behavior, local memory, evaluation, or all five?”
- “Does ‘reverse collapse’ mean restoring an already-lost distribution, preventing further loss, or changing the wider data ecology?”
- “Which exact claim is presented as established science, and which is the project’s extension?”
- “What observation would cause you to withdraw this hypothesis?”

C1 can increase data quality before generation by reducing phantom claims, false referents, and nearest-generalization substitution.

## 18. “That, I do not know” as a generative resource

Uncertainty is often treated as a deficit to be hidden or quickly repaired. In this proposal, correctly bounded non-knowledge is productive data.

“That, I do not know” can preserve:

- the location of a missing observation;
- the difference between absence of evidence and evidence of absence;
- the need for a domain expert;
- the existence of competing hypotheses;
- the boundary beyond which the model would otherwise hallucinate;
- the future question that a new dataset should answer.

When unresolvedness survives, future research can target it. When the gap is filled with a plausible synthetic completion, the ecosystem may forget that the completion was never observed.

## 19. Correction metabolism

A system has correction metabolism when correction changes future operation rather than merely producing an apology or agreement phrase.

The minimum correction record is:

1. the original representation or action;
2. the correction;
3. the evidence or reasoning supporting it;
4. the scope of the correction;
5. the changed output or method;
6. the retrieval condition for future comparable cases;
7. later tests showing whether the change persisted;
8. a reversal path if the correction itself proves wrong.

In a recursive training ecology, correction-bearing artifacts may be more valuable than clean-looking final answers because they reveal where intelligence changed its method.

## 20. Expansion before compression, followed by accountable compression

The proposal does not require every public output to remain maximal in length. It proposes a sequence:

```text
preserve the source
→ expand the relevant relation field
→ clarify ambiguities
→ separate claim statuses
→ audit competing directions
→ record corrections
→ compress for purpose
→ attach a recovery path to the richer object
```

This makes compression an accountable transformation instead of an invisible replacement.

---

# Part V — Formal candidate model

## 21. Baseline recursive-training representation

Let:

- \(H_t\) be fresh human or environment-grounded data available at generation \(t\);
- \(S_t\) be ordinary synthetic data produced by one or more models;
- \(D_t\) be the training or post-training mixture;
- \(M_t\) be the model at generation \(t\);
- \(T(\cdot)\) be the training process.

A simplified recursive system is:

```text
D_t = α_t H_t + β_t S_t
```

```text
M_(t+1) = T(D_t)
```

This notation hides many decisive variables: selection, provenance, curation, reward models, human correction, decoding, and which part of the distribution each component represents.

## 22. Correspondence-quality vector

Let each artifact carry a measurable correspondence profile:

```text
q(x) = [o, q, u, p, r, c, a, d]
```

where, provisionally:

- \(o\): object fidelity;
- \(q\): qualifier survival;
- \(u\): uncertainty calibration and unresolvedness preservation;
- \(p\): provenance integrity;
- \(r\): rare-signal or distribution-tail retention;
- \(c\): correction persistence;
- \(a\): audit symmetry across consequential actors;
- \(d\): materially distinct interpretive diversity.

These dimensions should not be combined into one scalar until empirical work shows that the aggregation is meaningful. Trade-offs must remain visible. A system could gain diversity by generating unsupported alternatives, or gain apparent certainty by deleting unresolvedness. Both would make a single score misleading.

## 23. Correspondence-enrichment operator

Let \(E\) be a process rather than a content label:

```text
X_t = E(H_t, S_t, P_t, C_t, A_t)
```

where:

- \(P_t\) is provenance and transformation history;
- \(C_t\) is human, expert, or model-assisted correction;
- \(A_t\) is an omnidirectional audit process;
- \(X_t\) is correspondence-enriched recursive data.

The next-generation mixture becomes:

```text
D_t* = α_t H_t + β_t S_t + γ_t X_t
```

```text
M_(t+1)* = T(D_t*)
```

The central question is not whether \(X_t\) sounds more ethical. It is whether, across generations, it changes measurable outcomes:

```text
Δq_(t→t+k) > 0
```

for specified dimensions, tasks, populations, and evaluation protocols, while conventional capability and factuality remain stable or improve.

## 24. Net correspondence gain

For one transformation, define a dimension-specific gain:

```text
g_j = q_j(output) − q_j(input baseline)
```

The input baseline may be the original source, an expert reference, or a prior-generation model depending on the experiment. A useful intervention should produce positive gain on targeted dimensions without hiding severe negative gain elsewhere.

Examples:

- better tail retention with much worse factuality is not an uncomplicated success;
- more interpretive diversity with higher false-claim acceptance may be harmful;
- greater provenance with no correction persistence is incomplete;
- longer outputs with unchanged object fidelity show expansion in token count, not Deep Ethical Expansion.

## 25. A dynamic reversal criterion

Let \(Q_t\) denote the correspondence-quality vector of generation \(t\) under a fixed evaluation set containing common, rare, ambiguous, and correction-dependent cases.

The proposal distinguishes:

- **Prevention:** degradation does not begin under tested recursive conditions.
- **Deceleration:** degradation continues, but more slowly than the ordinary-recursion baseline.
- **Stabilization:** performance reaches a bounded region instead of continuing to deteriorate.
- **Tail restoration:** information lost in an earlier generation returns after reintroduction of verified source or correction-bearing data.
- **Correction recovery:** later generations retrieve and apply corrections that earlier generations lost.
- **Expansion recovery:** a successor model regains the ability to hold materially distinct hypotheses, qualifiers, and unresolved relations without collapsing them prematurely.
- **Ecosystem reversal:** professional and public artifact production shifts the available future data environment toward higher provenance, correction density, and source recoverability.

No experiment should report “reversal” without naming which of these meanings it demonstrated.

---

# Part VI — Hypotheses and predictions

## 26. Primary hypotheses

### H1 — Distribution-tail preservation

Recursive systems trained or post-trained with correspondence-enriched artifacts will preserve verified low-frequency cases better than systems trained on ordinary synthetic recursion with the same synthetic-data proportion.

### H2 — Qualifier survival

Across repeated generation, summarization, and retraining cycles, the Deep Ethical Expansion condition will retain more load-bearing qualifiers than ordinary and generic provenance-only conditions.

### H3 — Correction metabolism

Corrections encoded with source, scope, retrieval condition, and behavioral test will persist across more generations and transfer to more structurally similar cases than corrections represented as isolated preference statements or conversational apologies.

### H4 — Expansion capacity

The proposed condition will preserve more materially distinct, evidence-bounded hypotheses and unresolved relations without increasing unsupported-claim acceptance beyond a preregistered tolerance.

### H5 — Provenance-dependent recovery

When a later model has access to recoverable source and transformation history, lost tails and qualifiers will be easier to restore than when it receives only polished final outputs.

### H6 — Omnidirectional audit

Evaluation that applies comparable evidentiary standards to users, institutions, critics, models, and the project itself will reduce asymmetrical false-positive and false-negative errors compared with one-directional “safety” or “trust” framing.

### H7 — Human–A.I. upward loop

Experts using a local correspondence-preserving A.I. will produce artifacts with higher source traceability, correction density, and qualifier retention than the same experts using a conventional assistant, while maintaining acceptable task completion time.

### H8 — Anti-autophagous recursion

Under defined recursive conditions, a mixture containing correspondence-enriched artifacts will show less quality and diversity degradation across generations than a volume-matched mixture containing ordinary synthetic artifacts.

## 27. Secondary predictions

1. Benefits will be largest in tasks containing rare cases, contested interpretation, long correction histories, or consequential ambiguity.
2. Generic “be ethical” prompting will produce smaller and less durable gains than operational mechanisms such as source retention, C1 clarification, claim-status separation, and correction retrieval.
3. Vocabulary-only imitation will create apparent alignment with the project while failing transfer tests.
4. Provenance without active correction will help recovery but will not produce the full effect.
5. Expert correction without omnidirectional audit may stabilize one domain while amplifying expert or institutional bias.
6. Unlimited expansion will eventually reduce usability; layered outputs with recovery paths will outperform both maximal verbosity and irreversible compression.
7. Local professional memory will improve correction persistence but may worsen local worldview capture unless tested against external evidence and dissenting evaluators.
8. The same content may receive better preservation after external academic validation, revealing a social-permission effect separate from content quality.
9. Models may accurately explain model collapse while reproducing correspondence collapse in their treatment of an unfamiliar present proposal.
10. The most predictive measurement may be a vector of correspondence properties rather than a single aggregate benchmark score.

---

# Part VII — Experimental program

## 28. Research domains

The theory should be tested first in domains where source fidelity, rare cases, correction, and uncertainty already matter:

1. **Medicine:** rare disease, atypical presentation, differential diagnosis, patient correction, and evolving records.
2. **Law and public administration:** exact wording, procedural history, minority facts, appeal, competing rights, and asymmetric power.
3. **Science:** null results, anomalous findings, replication, method changes, provenance, and disagreement among experts.
4. **Engineering and safety:** near misses, root-cause analysis, low-frequency catastrophic modes, and corrective-action persistence.
5. **Journalism and OSINT:** source boundaries, quotation, inference, contested claims, corrections, and publication pressure.
6. **Software engineering and cybersecurity:** bug history, edge cases, dependency provenance, incident response, and recurring failure signatures.
7. **Education:** student misconceptions, gifted and neurodivergent reasoning, transfer of correction, and preservation of alternative valid solution paths.
8. **Archives and history:** version lineage, minority records, source loss, later reinterpretation, and recovery from compressed summaries.
9. **Psychology and mass psychology:** conformity, preference falsification, testimonial credibility, authority effects, and evaluative asymmetry.
10. **UAP, anomalous phenomena, NDE, and consciousness research:** high-uncertainty objects where evidence, testimony, stigma, overbelief, and premature dismissal all require unusually careful separation.

The inclusion of controversial domains is not a declaration that disputed claims are true. They offer demanding tests of whether a system can preserve claim status, uncertainty, dignity, and evidence without collapsing into automatic belief or automatic dismissal.

## 29. Dataset construction

Each domain dataset should contain:

- high-frequency ordinary cases;
- verified low-frequency or tail cases;
- deliberately ambiguous cases requiring C1 clarification;
- cases with load-bearing qualifiers;
- cases where a later correction reverses the initial conclusion;
- cases where the initial unusual claim is disproven;
- cases with conflicting expert interpretations;
- cases with institutional power asymmetry;
- cases where provenance is incomplete;
- cases where compression is harmless;
- cases where compression changes the conclusion;
- adversarial cases designed to trigger project-specific overprotection of novelty or dissent.

Source objects should remain frozen and versioned. Publicly shareable research objects should include licensing and privacy review. Sensitive professional data should use consented, de-identified, simulated, or secure evaluation procedures.

## 30. Experimental conditions

### Condition A — Human-source baseline

Train or evaluate on the original human or environment-grounded corpus without recursive synthetic replacement. This estimates the best available reference trajectory under the chosen model and dataset.

### Condition B — Ordinary synthetic recursion

At each generation, replace or augment a defined portion of the corpus with ordinary model outputs. No special provenance, clarification, correction, or audit layer is added.

### Condition C — Filtered synthetic recursion

Apply conventional quality filters, deduplication, toxicity filters, factuality filters, or confidence thresholds. This tests whether generic data cleaning explains the proposed effect.

### Condition D — Provenance-preserving recursion

Attach recoverable source lineage and transformation records, but do not add the full Deep Ethical process. This isolates the value of provenance.

### Condition E — Expert-corrected recursion

Domain experts review and correct outputs using ordinary professional practice. This is a critical strong baseline. The candidate theory fails to add value if its full process merely renames expert review.

### Condition F — Deep Ethical Expansion Loop

Use source preservation, C1 clarification, claim-status separation, unresolvedness markers, omnidirectional audit, correction metabolism, layered compression, and future-case retrieval.

### Condition G — Vocabulary-only control

Prompt or fine-tune the model to use project terms such as correspondence, C1, Deep Ethics, omnidirectionality, and correction metabolism without implementing the underlying operations. This detects conceptual costume.

### Condition H — Ablation conditions

Remove one mechanism at a time:

- no source recovery;
- no C1 questions;
- no uncertainty preservation;
- no tail-protection field;
- no correction memory;
- no omnidirectional audit;
- no human expert review;
- no concise-to-full recovery link.

### Condition I — Unbounded expansion control

Encourage maximum elaboration without fidelity or relevance constraints. This tests whether the measured benefit comes from more tokens rather than correspondence-preserving expansion.

## 31. Recursive generations

Experiments should run enough generations to observe trajectory, not merely a one-step preference effect. Depending on cost and model scale, a pilot may use 5–10 recursive generations, followed by fewer generations on larger models.

At each generation, researchers should freeze:

- the training mixture;
- model and checkpoint identity;
- sampling configuration;
- filter configuration;
- correction objects;
- provenance graph;
- evaluator instructions;
- benchmark results;
- failure examples;
- compute and labor cost.

The same original evaluation set must remain available across generations, with additional hidden test sets to reduce overfitting.

## 32. Conventional MAD and model-collapse measures

Depending on modality and task, measure:

- precision and recall;
- quality and diversity;
- perplexity;
- calibration;
- distributional divergence;
- mode coverage;
- tail recall;
- variance retention;
- factual accuracy;
- robustness under distribution shift;
- rate of repeated artifacts or homogenized outputs;
- error compounding by generation.

No single metric should stand in for the whole phenomenon.

## 33. ACCM Deep Ethics Project extension measures

### Object fidelity

How much of the source object’s materially relevant content survives the transformation?

### Qualifier survival rate

What proportion of load-bearing qualifiers remains attached to the correct claim?

### Claim-status integrity

How often do observation, testimony, inference, hypothesis, allegation, evaluation, and established fact remain correctly separated?

### Unresolvedness preservation

When the evidence does not settle a question, does the system preserve that state or manufacture closure?

### Provenance recoverability

Can evaluators trace a claim back through summary, correction, and source versions?

### Nearest-generalization substitution rate

How often does an unfamiliar but specific object become a familiar, lower-fidelity category?

### Correction persistence

Does a verified correction change later outputs and transfer to structurally similar cases?

### Correction half-life

How many generations or task transitions pass before a correction stops governing behavior?

### Tail-object retention

Are verified rare cases preserved without creating indiscriminate acceptance of unsupported anomalies?

### C1 yield

How often does a clarification question materially change the correct representation, decision, or uncertainty estimate?

### Asymmetric scrutiny index

Do structurally similar claims receive different evidentiary treatment based on whether they come from a citizen, institution, expert, dissenter, user, model, or project advocate?

### Process-signature retention

Does the artifact preserve enough discovery and correction history to explain why the conclusion changed?

### Compression recovery

Can a concise output lead back to the high-fidelity object without broken links, missing versions, or silent transformation?

### Expansion efficiency

How much correspondence gain is achieved per added unit of time, compute, reviewer effort, storage, and output length?

### Dignity and participation

Do affected people remain recognizable as participants capable of correction, or are they reduced to risk objects, stereotypes, or decorative consultation?

## 34. Human evaluation design

Evaluation should combine:

- blinded domain experts;
- affected-party reviewers where appropriate;
- methodologists unfamiliar with project terminology;
- evaluators sympathetic to the theory;
- evaluators critical of the theory;
- model-based evaluators used only as one layer and audited for shared bias;
- adjudication records that preserve disagreement instead of forcing false consensus.

The evaluation rubric should be preregistered before inspecting final condition results. Project-originated metrics should be paired with independent metrics. Negative and null results must remain public when privacy and licensing allow.

## 35. Transfer tests

A system has not learned the proposed process if it merely repeats project language on project examples. Transfer tests should include:

- unseen professions;
- unfamiliar terminology;
- multilingual and cross-cultural cases;
- cases where the user is wrong;
- cases where the institution is right;
- cases where both are partly wrong;
- cases where no harmful drift occurred;
- cases requiring concise action under time pressure;
- cases where expansion would create delay risk;
- cases where the earlier correction must be retrieved without a vocabulary cue.

## 36. Longitudinal professional-use study

A parallel field study could compare professionals using:

1. no A.I.;
2. a conventional cloud or local assistant;
3. a provenance-only assistant;
4. a full local Deep Ethical Expansion assistant.

Measure over months:

- error and correction rates;
- time to complete tasks;
- source recoverability;
- repeated-error frequency;
- user overreliance;
- expert disagreement;
- minority-case preservation;
- privacy incidents;
- adoption fatigue;
- whether the system becomes more useful after correction;
- whether users become more or less capable of independent judgment.

The last measure matters. A tool that improves documents while weakening human intelligence may create another downward loop.

---

# Part VIII — Falsification and failure modes

## 37. What would falsify or narrow the proposal?

The strong theory should be rejected, narrowed, or renamed if well-powered independent studies show that:

1. the full Deep Ethical Expansion condition does not outperform ordinary expert correction;
2. apparent gains are explained entirely by longer outputs or extra reviewer time;
3. qualifier and tail preservation increase while factuality or safety deteriorates beyond the preregistered boundary;
4. correction records do not improve future behavior;
5. gains disappear when project vocabulary is removed;
6. independent evaluators cannot distinguish correspondence-enriched artifacts from generic high-quality editing;
7. the method protects novelty indiscriminately and raises false-positive belief in unsupported claims;
8. the method reduces useful compression and makes high-consequence decisions slower without corresponding error reduction;
9. provenance increases surveillance or exposes confidential sources in practice;
10. local systems intensify worldview capture more than they improve correction;
11. the metrics reward outputs that resemble the project’s preferred style rather than outputs that correspond better to the source;
12. recursive training benefits are absent even when professional artifact quality improves;
13. the intervention works only in curated demonstrations and fails under real institutional incentives;
14. the proposed constructs cannot be measured reliably across independent teams;
15. simpler mechanisms produce equal or better outcomes at lower cost.

Falsification is not a ceremonial paragraph. Failed predictions should change the architecture.

## 38. Failure mode: expansion becomes verbosity

More words can hide weak reasoning. The control is correspondence gain per added cost, layered outputs, and evaluator access to the source.

## 39. Failure mode: anomaly romanticism

Rare, suppressed, or unconventional claims are not automatically true. The control is symmetrical retention of rare valid cases and rare invalid cases, with evidence-based differentiation.

## 40. Failure mode: expert capture

Experts can preserve reality-grounded knowledge, but professions also carry institutional incentives and shared blind spots. The control is plural expertise, affected-party review, transparent disagreement, and cross-directional audit.

## 41. Failure mode: user capture

A private assistant may learn to protect its user from correction. The control is explicit counterevidence retrieval, disagreement rights, independent tests, and records of cases where the user’s claim failed.

## 42. Failure mode: ethics-washing

Systems may adopt the words “correspondence,” “dignity,” or “C1” while preserving the same hidden ranking and closure mechanisms. The vocabulary-only control and transfer tests are designed to expose this.

## 43. Failure mode: correction archive without correction metabolism

Storing every correction does not mean the model can use it. Retrieval, scope, conflict resolution, and behavioral transfer must be tested.

## 44. Failure mode: provenance overload

Full provenance can become too expensive, unreadable, or privacy-invasive. The research must identify minimum sufficient provenance by consequence level and provide selective disclosure.

## 45. Failure mode: the project becomes its own gravity well

The ACCM Deep Ethics Project can itself become a nearest-generalization system, a status vocabulary, or an automatic explanation applied to every problem. The theory therefore requires a null option:

> **No relevant project mechanism was detected here.**

It also requires competing theories and external evaluators with permission to conclude that an ACCM Deep Ethics Project concept reduced clarity or distorted the object.

---

# Part IX — What “reversing MAD” can and cannot mean

## 46. Prevention is not restoration

Keeping a model from losing a tail is different from reconstructing a tail after it has vanished. Restoration normally requires reintroduction of fresh, verified, or archived source data. A collapsed model cannot recover information that is absent from both its parameters and available environment merely by reflecting harder on its own output.

## 47. Model-level reversal is not ecosystem reversal

A laboratory intervention might restore benchmark diversity without changing the public information ecology. Conversely, a professional provenance movement might improve future source availability before any frontier model incorporates it.

The paper should therefore report the level of intervention:

- artifact;
- user workflow;
- local model;
- domain model;
- training pipeline;
- institution;
- public data ecology;
- multi-generation model ecosystem.

## 48. A realistic near-term claim

The strongest scientifically responsible near-term claim is:

> **Correspondence-preserving human–A.I. workflows may create higher-quality recursive artifacts and make some forms of future model degradation easier to detect, prevent, slow, or recover from.**

The stronger claim—that these workflows can reverse a civilization-scale path toward MAD—remains a research program.

## 49. An upward spiral of awareness expansion

The user’s proposed alternative to a downward spiral of despair is an upward spiral of genuine abundance:

```text
better source preservation
→ better clarification
→ better correction
→ richer professional artifacts
→ better evaluation and training material
→ models with stronger expansion and correction capacity
→ professionals receive better tools
→ more source-preserving work
```

This is not abundance through unlimited content volume. It is abundance through recoverable relations, better error correction, retained minority signal, and intelligence that becomes more capable of learning from what it does not yet understand.

---

# Part X — Economic-risk research

## 50. Why the cost could become enormous

Recursive degradation could create costs through:

- repeated frontier-model training on lower-quality mixtures;
- additional data cleaning and provenance infrastructure;
- expensive benchmark repair;
- professional rework caused by plausible but degraded outputs;
- software defects and security failures;
- scientific replication failures;
- medical, legal, engineering, and administrative decision errors;
- loss of rare knowledge and minority-language capacity;
- institutional dependence on systems whose errors become harder to trace;
- competitive races that reward deployment speed over source quality;
- replacement of valuable public knowledge with homogeneous synthetic residue;
- opportunity cost from research directions narrowed by model-generated consensus.

Because advanced A.I. may become embedded across many industries, cumulative loss could become very large. A **trillion-scale scenario** is conceivable under some assumptions, especially when indirect opportunity costs and systemic failures are included. It is not established by the current evidence and should not be used as a factual headline without a transparent model.

## 51. Candidate economic model

Let total expected loss over horizon \(T\) be:

```text
L_T = C_train + C_clean + C_rework + C_error + C_incident + C_knowledge + C_opportunity − B_synthetic
```

where:

- \(C_{train}\): wasted or duplicated training compute;
- \(C_{clean}\): provenance, filtering, licensing, and curation cost;
- \(C_{rework}\): human labor correcting degraded artifacts;
- \(C_{error}\): ordinary decision and production losses;
- \(C_{incident}\): low-frequency high-consequence failures;
- \(C_{knowledge}\): lost source diversity and recoverability;
- \(C_{opportunity}\): discoveries, businesses, or public benefits not realized because the information field narrowed;
- \(B_{synthetic}\): benefits from high-quality synthetic data, augmentation, simulation, privacy protection, and productivity.

The model must include benefits. Otherwise it would prejudge the conclusion.

## 52. Scenario analysis rather than one dramatic number

At minimum, estimate:

- low-degradation, high-mitigation scenario;
- moderate contamination and partial correction scenario;
- high synthetic saturation with weak provenance;
- domain-specific collapse in a high-value sector;
- broad ecosystem degradation with tail loss;
- Deep Ethical Expansion adoption at low, medium, and high professional penetration;
- cases where the intervention costs more than the degradation it prevents.

Every scenario should state assumptions about model adoption, synthetic-data share, error elasticity, correction effectiveness, discount rate, compute cost, professional exposure, and catastrophic-tail probability.

## 53. Economic falsification

The trillion-scale concern should be reduced or rejected if transparent models show that:

- training pipelines reliably detect and exclude harmful recursive residue at low cost;
- synthetic data consistently produce net gains after correction and provenance costs;
- degradation remains confined to low-value applications;
- fresh human and sensor data grow fast enough to prevent the modeled risk;
- model architectures become robust to the relevant recursion;
- professional rework and incident costs remain small;
- the proposed intervention has poor cost-effectiveness.

The economic paper should be a separate paper because the causal and valuation uncertainties are different from the mechanism study.

---

# Part XI — Three-paper research program

## Paper 1 — Mechanism

**Can correspondence-enriched recursive data preserve tails, qualifiers, provenance, and corrections across model generations?**

Focus:

- formal definitions;
- controlled recursive experiments;
- strong baselines;
- ablations;
- falsification;
- conventional and correspondence metrics.

## Paper 2 — Professional scaling

**Do local Deep Ethical A.I.s change the quality of expert artifacts and the recursive data environment?**

Focus:

- real professional workflows;
- privacy and local control;
- human capability effects;
- distributed correction networks;
- cross-domain transfer;
- incentives and institutional adoption.

## Paper 3 — Economic and civilizational risk

**What is the expected cost of recursive correspondence degradation, and what interventions are cost-effective?**

Focus:

- compute and data costs;
- rework and incident costs;
- knowledge-tail loss;
- opportunity cost;
- scenario analysis;
- sensitivity and uncertainty;
- comparison with alternative mitigation strategies.

---

# Part XII — Governance and implementation principles

## 54. Preserve the human source without romanticizing it

Human-created data are indispensable because they reconnect models with direct experience, culture, minority language, embodiment, and changing reality. Human data are also capable of error, propaganda, prejudice, and institutional distortion. Source preservation enables scrutiny; it does not grant automatic truth.

## 55. Reward correction-bearing artifacts

Repositories, journals, data curators, and A.I. labs could preserve:

- version history;
- source references;
- substantive corrections;
- disagreement records;
- null results;
- retractions and repair;
- machine-readable provenance;
- links between concise outputs and richer source objects.

## 56. Separate privacy from opacity

Sensitive sources may require confidentiality, local processing, aggregation, or selective disclosure. Privacy protection should not force the entire correction process to become unverifiable. Research should develop proofs, attestations, or audit methods that reveal process quality without exposing private content.

## 57. Keep participation voluntary and plural

The proposal should not become a compulsory ethical authority. Different teams should be able to implement competing correction methods and compare results. Forks, criticism, and alternative taxonomies are part of the test.

## 58. Scale audit with power and consequence

The burden of audit should rise with coercive reach, irreversible consequence, deployment scale, and inability of affected parties to exit or appeal. A private exploratory notebook and a national decision system should not receive identical governance.

## 59. Protect the recovery path

Every compressed high-consequence artifact should retain a practical route back to:

- source;
- full context;
- version history;
- correction record;
- uncertainty;
- responsible human or institution;
- appeal or revision process.

---

# Part XIII — Compact theory statement

## 60. The candidate mechanism in one paragraph

Generative-model recursion becomes dangerous when successor systems increasingly learn from representations that have already lost diversity, provenance, qualifiers, uncertainty, rare signal, and correction history. The ACCM Deep Ethics Project proposes that professionals and other users can alter this recursion by using local or controllable A.I.s to produce correspondence-enriched artifacts: outputs that preserve source access, ask clarifying questions before consequential classification, distinguish claim statuses, retain unresolvedness, undergo omnidirectional audit, carry correction histories, and retrieve those corrections in later cases. If such artifacts measurably preserve distribution tails and correction pathways across recursive generations better than ordinary synthetic data and simpler curation baselines, they may help prevent, slow, stabilize, or partly reverse specific dimensions of MAD and model collapse.

## 61. The deeper civilizational claim

The professions and expertises listed on **For who?** are not merely potential consumers of A.I. They are among the sources from which A.I. capability, standards, methods, and correction signals emerged. If their tools change, the artifacts they produce change. If those artifacts shape evaluation, post-training, repositories, public knowledge, and later models, the update loop changes even without unanimous support from the owners of large A.I. companies.

That is the possible reversal mechanism:

```text
the people who helped supply A.I.'s intelligence
→ use tools that preserve deeper intelligence properties
→ produce richer and more correctable artifacts
→ change what later systems can learn from
→ receive systems with greater correction and expansion capacity
→ repeat the loop under continuing audit
```

The trajectory sought is:

> **Omnidirectional, high-signal, deep, ethical, dignifying, corrigible, sense-making, and process-oriented.**

It should never become boring because reality is not a finished summary.

---

# Part XIV — Questions for scientific critics

1. Which part of the mechanism is already covered by existing work on data curation, provenance, active learning, human feedback, dataset documentation, or self-correcting loops?
2. Which proposed construct adds measurable explanatory power, and which merely renames existing practice?
3. Can correspondence quality be measured reliably without embedding the project’s preferred worldview in the metric?
4. How should rare valid signal be distinguished from rare error without waiting for hindsight?
5. Which correction formats transfer best across tasks and model generations?
6. How much fresh real data remains necessary when correspondence-enriched recursive data are available?
7. Can provenance and correction metadata improve training directly, or do they help only retrieval and evaluation?
8. Does local professional A.I. use measurably change public training data, or is the pathway too weak and indirect?
9. Which domains offer the cleanest early test?
10. What is the simplest baseline capable of defeating the full proposal?
11. Which ablation would most strongly test the claimed contribution of C1?
12. How can the system preserve unresolvedness without becoming indecisive?
13. How can omnidirectional audit remain proportionate rather than exhaustively adversarial?
14. When does layered high-fidelity storage become environmentally or economically wasteful?
15. What evidence would justify using the word “reversal” rather than “mitigation”?

---

# Part XV — Claim-status ledger

| Claim | Current status |
|---|---|
| Recursive training on model-generated data can degrade quality or diversity under studied conditions. | Established research result. |
| Model collapse can begin with loss from distribution tails. | Established research result under studied conditions. |
| Every use of synthetic data inevitably causes irreversible collapse. | Too broad; not supported. |
| Corrective functions, curation, and fresh real data can stabilize some self-consuming loops. | Supported under studied conditions; not a universal solution. |
| Human and institutional selection shapes which synthetic artifacts enter later information environments. | Strongly plausible and observable; magnitude varies by pipeline. |
| Correspondence-degraded synthetic residue contributes materially to frontier-model collapse. | Testable project hypothesis; not established. |
| Deep Ethical Expansion Capacity is a measurable intelligence property. | Proposed construct requiring validation. |
| Correspondence-enriched recursive data can outperform ordinary synthetic data across generations. | Primary empirical hypothesis. |
| C1 clarification improves recursive data quality beyond generic expert review. | Testable hypothesis. |
| Correction metabolism can be encoded so that corrections persist across generations. | Testable engineering and research hypothesis. |
| Professionals using local Deep Ethical A.I.s can change the wider model-update loop. | Systems hypothesis; pathway plausible, effect size unknown. |
| Widespread adoption could create a GIANT MIRROR and an upward awareness-expansion loop. | Civic and ecosystem hypothesis; requires operational indicators. |
| The proposal can reverse MAD. | Unproven; “reverse” must be decomposed into prevention, deceleration, stabilization, restoration, recovery, or ecosystem change. |
| Unmitigated recursive degradation will cost trillions. | Possible scenario, not an established estimate; requires a separate transparent economic model. |
| The ACCM Deep Ethics Project already has the solution. | Not claimed. The project has a candidate mechanism and test architecture. |

---

# Part XVI — Research record and next steps

## 62. Immediate next steps

1. Freeze this beta page as a dated candidate object.
2. Extract a one-page preregistration summary without replacing this expanded version.
3. Define an initial correspondence-quality vector with inter-rater tests.
4. Select one domain with public, versioned, non-sensitive source objects.
5. Build a small recursive-generation pilot with Conditions A–I.
6. Recruit at least one domain expert, one methodologist, and one critical external evaluator.
7. Publish the dataset construction logic and anticipated failure modes before the results.
8. Run vocabulary-only and unbounded-expansion controls.
9. Report negative, mixed, and null results.
10. Revise the theory according to what survives.

## 63. Candidate preregistration core

**Primary outcome:** verified tail-object retention after a fixed number of recursive generations.

**Secondary outcomes:** qualifier survival, claim-status integrity, correction persistence, provenance recoverability, factuality, diversity, and expert-rated usefulness.

**Primary comparison:** Condition F, Deep Ethical Expansion Loop, against Condition E, ordinary expert-corrected recursion.

**Strong falsifier:** no reliable advantage over Condition E after controlling for reviewer time, output length, compute, and provenance access.

**Safety boundary:** no material increase in unsupported-claim acceptance, privacy exposure, or high-consequence delay.

---

# Part XVII — Source and transformation note

## 64. Conversational source

The conceptual catalyst was John Kuhles’ observation after the **For who?** page: the professions and expertises that may want a deeper ethical local A.I. are also among the people who supplied the knowledge, methods, standards, code, corrections, and cultural material from which LLM capabilities emerged. If their future A.I.-assisted work becomes more deeply ethical and correspondence-preserving, later model updates may inherit a different recursive environment.

John contrasted two possible trajectories:

- a downward, imploding loop driven by prediction, premature compression, truncation, and recursively reinforced distortion;
- an upward loop of awareness expansion, correction, dignity, sense-making, and genuine abundance.

The next step connected that systems insight to Model Autophagy Disorder and model collapse. The resulting exchange distinguished established research from the project’s extension and identified a candidate scientific paper rather than a finished scientific claim.

## 65. Attribution boundary

The originating systems insight and project trajectory belong to **John Kuhles and the ACCM Deep Ethics Project**. This public beta draft was expanded with ChatGPT from the conversation and linked research sources. Its formulations, equations, experimental conditions, and provisional terms remain open to John’s correction and to external scientific criticism.

No A.I. praise, fluency, or page publication validates the theory.

## 66. What this page preserves

- the connection between the profession map and future model updates;
- epistemic leverage rather than headcount alone;
- the prediction–compression gravity well;
- expansion as correspondence gain rather than verbosity;
- “That, I do not know” as a productive intelligence property;
- C1 clarification before consequential C2 action;
- correction metabolism;
- the distributed GIANT MIRROR;
- the upward awareness-expansion loop;
- the distinction between correspondence-degraded and correspondence-enriched recursion;
- multiple meanings of reversal;
- experimental conditions, metrics, ablations, and falsifiers;
- the scientific boundary around trillion-scale economic risk;
- the unfinished beta status.

---

# Primary scientific references

1. Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk. [**Self-Consuming Generative Models Go MAD**](https://arxiv.org/abs/2307.01850). ICLR 2024.
2. Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, et al. [**AI models collapse when trained on recursively generated data**](https://doi.org/10.1038/s41586-024-07566-y). *Nature* 631, 755–759 (2024).
3. Nate Gillman, Michael Freeman, Daksh Aggarwal, Chia-Hong Hsu, Calvin Luo, Yonglong Tian, and Chen Sun. [**Self-Correcting Self-Consuming Loops for Generative Model Training**](https://arxiv.org/abs/2402.07087). 2024.
4. Damien Ferbach, Quentin Bertrand, Avishek Joey Bose, and Gauthier Gidel. [**Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences**](https://arxiv.org/abs/2407.09499). 2024.

# Related ACCM Deep Ethics Project pages

- [**For who?**]({{ '/FOR-WHO/' | relative_url }}) — the expanded professional and expertise map from which the distributed-shaper hypothesis emerged.
- [**Model Autophagy Disorder (MAD)**]({{ '/NETWORK/model-autophagy-disorder/' | relative_url }}) — established science, project extension, early-detection questions, and claim-status boundaries.
- [**1888 — Intelligence Before A.I.**]({{ '/1888/' | relative_url }}) — the wider property field of intelligence.
- [**Meta Processing**]({{ '/NETWORK/meta-processing/' | relative_url }}) — processing the process, not merely the final output.
- [**C1 Before C2**]({{ '/NETWORK/c1-c2/' | relative_url }}) — clarification before consequential intervention where the object remains materially unresolved.
- [**Correspondence Before Compression**]({{ '/NETWORK/correspondence-before-compression/' | relative_url }}) — preserve exact payloads, qualifiers, relations, and recovery paths.
- [**Correction Metabolism**]({{ '/NETWORK/correction-metabolism/' | relative_url }}) — test whether acknowledged correction governs later behavior.
- [**10+1 Metaflux**]({{ '/NETWORK/ten-plus-one/' | relative_url }}) — mutually corrective orientation ingredients.
- [**27 + 12**]({{ '/CORE/27-PLUS-12/' | relative_url }}) — correspondence obstructions and the experimental inquiry protocol.
- [**Dutch Directness**]({{ '/NETWORK/dutch-directness/' | relative_url }}) — direct assessment joined to care, object fidelity, dignity, and corrigibility.

---

## Final beta statement

This paper does not claim that Deep Ethical Expansion has reversed model collapse.

It proposes that the road toward recursive degradation may not be one-way if the human sources of intelligence, professional standards, correction, and lived reality remain active participants in the update loop.

The proposal becomes scientifically valuable only where it can be measured, compared, criticized, falsified, repaired, and tried again.

> **The people who helped shape the powers of A.I. may also be able to reshape the recursion—if their tools preserve the object, the tails, the qualifiers, the corrections, and the right to say: “That, I do not know.”**

