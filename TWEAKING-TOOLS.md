---
layout: page
title: "Tweaking Tools"
description: "GitHub tools, local models and practical Deep Ethical experiments, including an LFM3-powered phone-companion proposal for project explanations, FAQs, source navigation and correction."
permalink: /TWEAKING-TOOLS/
date: 2026-11-01
---

<!-- ACCM_FORMAT_LINKS_START -->
<div class="accm-source-format-links" role="navigation" aria-label="Available page formats">
<strong>Available formats:</strong> <a href="https://deepethics.github.io/ACCM-Deep-Ethics-Project/TWEAKING-TOOLS/">🌐 Public HTML page</a><span aria-hidden="true"> · </span><a href="https://deepethics.github.io/ACCM-Deep-Ethics-Project/Deep-Ethical-PDFs/TWEAKING-TOOLS.pdf">📄 PDF edition</a>
</div>
<!-- ACCM_FORMAT_LINKS_END -->

# Tweaking Tools

## GitHub software, local models, and the quality of what changes

**Working research catalogue · first source check: November 1, 2026.** John Kuhles selected the candidates in his supplied *Recommended for Deep Ethical Minds* collection and commissioned this page. The descriptions below distinguish upstream documentation, reported measurements, and proposed project experiments. Installation and model experiments remain future work.

A useful tweak can open a capability, recover a source, preserve a correction, reduce repetitive work, or make a consequential decision inspectable. Its value appears in what the next operation can do. This page connects practical software choices to that process inside the **ACCM Deep Ethics Project**.

The governing question is:

> **What happened to the object while we were processing it?**

**[PQCE]({{ '/FLAGGING-SYSTEM/' | relative_url }})** (Process Quality Calibration Evaluation) follows that question through a tool's input, selection, transformation, output, consequences and later correction. The **[16 Anchor Ethics]({{ '/NETWORK/16-anchor-ethics/' | relative_url }})** contribute a parallel, non-imposing advisory perspective: they can reveal a missed relationship, invite inquiry, or support an appropriate pause while participants retain the ability to examine and decline the advice.

**Jump to:** [What can be tweaked?](#layers) · [Candidate catalogue](#catalogue) · [LFM3 and the phone companion](#lfm3-companion) · [Refusal-direction research](#refusal-direction) · [16 Anchor Ethics in use](#anchor-counsel) · [Small comparative trials](#trials) · [Source and correction record](#provenance) · [Related pages](#related-pages) · [Selected videos](#selected-videos)

## What can be tweaked? {#layers}

Different layers change different things. Keep the intervention and the claimed result at the same level.

| Layer | Practical change | What to inspect afterward |
|---|---|---|
| Working environment | Desktop, editor, documents, agent terminals | Can the participant find the original material, inspect changes and recover the work? |
| Memory and retrieval | Storage, indexing, search, context assembly | Which source was recovered, which version, with what qualifiers and correction history? |
| Agent harness | Tools, permissions, roles, handoffs, execution | Did the agent perform the authorized task, and can the participant interrupt or reverse it? |
| Instructions and skills | Reusable prompts, style rules, comparison procedures | Did the instruction improve this task, or become a compulsory script? |
| Model and inference | Model version, reasoning settings, quantization, weight edits | Which capabilities, refusals, errors and resource costs changed? |
| Deep Ethical calibration | Correspondence, consequences, mutual dignity, appeal and correction | Did a discovered relationship change the next operation, and did the correction return later? |

A saved conversation can supply evidence to memory; retrieval must still bring the relevant relation into the next task. An agent terminal can remain running while its reasoning repeats an error. A shorter answer can preserve the object or discard the qualifier that held it together. These are separate observations.

## Candidate catalogue {#catalogue}

The collection below retains all seventeen identifiable candidates from John's original supplied list, grouped by their possible job. The dated [LFM3 companion proposal](#lfm3-companion) extends that collection. **Upstream-described** means the named source was read; it does not mean this project has installed or benchmarked the tool. Links lead to the original projects so readers can inspect current versions, licenses, releases and requirements.

### Workspaces, memory, and agent coordination

| Candidate and source | Upstream-described purpose / current status | Candidate Deep Ethical use |
|---|---|---|
| **[Odysseus](https://github.com/odysseus-dev/odysseus)** · [site](https://odysseus-dev.github.io/odysseus/) | Self-hosted workspace combining chat, agents, research, documents, email, notes, calendar and local-model workflows. Its README identifies `dev` as the newest default branch and `main` as more curated. | Compare models on the same object while preserving the independent outputs, source references and participant-selected next move. |
| **[MemPalace](https://github.com/MemPalace/mempalace)** · [official documentation](https://mempalaceofficial.com) | Local-first conversation memory using verbatim storage and semantic retrieval, organized into scoped collections. The README identifies the supplied documentation domain as official. | Retrieve the original correction alongside the later task; test whether the agent applies it rather than merely remembering the conclusion. |
| **[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)** | Extensible agent harness with an “everything-is-a-plugin” architecture. Developer preview; upstream explicitly anticipates breaking changes. | Explore a replaceable calibration component with declared tool permissions, visible transformations and a recovery path when a plugin changes. |
| **[goose](https://github.com/aaif-goose/goose)** | Extensible agent with desktop, terminal and programmatic interfaces, multiple model providers and tool extensions. Local execution can still call a hosted model. | Run a bounded task with explicit access; compare the proposed action, permission, execution and actual result. |
| **[CrewAI](https://github.com/crewaiinc/crewai)** | Python framework for role-based agent collaboration and event-driven workflows. The open-source framework and commercial management services are distinct offerings. | Prototype Advocate, Arbiter and Overseer functions with separate records. Examine whether role separation adds an independent perspective or repeats a shared premise. |
| **[Herdr](https://github.com/herdrdev/herdr)** · [project analysis]({{ '/HERDR/' | relative_url }}) | Runtime for coding-agent terminals across local and remote machines. Client detachment keeps server processes running; restart restores saved layout and can resume supported sessions, rather than preserving the old processes. | Keep work and agent states visible while measuring correction transfer separately from terminal persistence. |

### Editing, documents, speech, and presentation

| Candidate and source | Upstream-described purpose / current status | Candidate Deep Ethical use |
|---|---|---|
| **[ArtCraft Crafting Apps](https://getartcraft.com/apps)** | Suite of native open-source creative applications, including document, image, PDF and presentation tools. The official catalogue marks individual applications as early alpha or in development and describes agent-control interfaces. | Make source-linked research artifacts and inspect whether edits, exports, captions and automation preserve attribution and meaning. |
| **[Void](https://github.com/voideditor/void)** | The repository is archived and its README says the editor is deprecated and no longer accepting contributions. Its source and [fork directory](https://github.com/voideditor/void-forks/) remain available as development references. | Study inspectable code changes and model-provider integration as a reference or fork candidate; record the actual maintenance status of any chosen successor. |
| **[Ming-3.0-tts](https://github.com/inclusionAI/Ming-3.0-tts)** | Text-to-speech models with multilingual synthesis, voice creation and delivery controls. Some functions depend on the model variant and task mode. | Produce accessible spoken versions while comparing the source script with audible wording, emphasis and speaker attribution. Use a person's voice only within the permission they gave. |
| **[Folio 1.10.0](https://github.com/Forward-Future/folio-releases/releases/tag/v1.10.0)** | PDF-reader release. Its October 28 release notes list Windows, macOS and Linux downloads; the older README still describes Windows. This release repository distributes builds rather than establishing that the full application source is present. | Read and cross-check exported research packets across the relevant platform; confirm that source links and selectable text survive the workflow. |
| **[Dutch Style Guide](https://github.com/lboshuizen/dutch-style-guide)** · [complete guide](https://github.com/lboshuizen/dutch-style-guide/blob/main/dutch-style-guide.md) | Thirty-seven practical Dutch writing rules with agent-skill and text-review integrations. The repository supplies the complete route missing from the truncated link in the candidate list. | Inspect a style transformation against the original qualifiers and intent. This page remains English; the guide is a tool candidate for Dutch work. |

### Compression, learning, and local model experiments

| Candidate and source | Upstream-described purpose / current status | Candidate Deep Ethical use |
|---|---|---|
| **[Caveman](https://github.com/juliusbrussee/caveman)** | Agent skills and tooling for shorter output, compressed tool input and model routing. Token-saving results in the repository are upstream reports under particular tasks and settings. | Compare the original and compressed representations. Preserve load-bearing qualifiers, failed attempts, dependencies and recovery routes; measure the human work needed to restore anything lost. |
| **[mini-AGI](https://github.com/volotat/mini-AGI)** · [supplied video lead](https://www.youtube.com/watch?v=L-6O7R71CCg) | Continual-learning byte-level model experiment aimed at modest hardware. The author explicitly calls it a small toy-level model and describes “mini-AGI” as a partly humorous name. | Study how newly received material affects later outputs, including correction retention, interference and forgetting. Video contents were not independently reviewed for this catalogue. |
| **[OrcaRouter Qwen3.8-27B-Uncensored-NVFP4](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-NVFP4)** | Publisher-described refusal-modified, mixed-precision model build for compatible NVIDIA Blackwell hardware. The page exposes model details; access to files has conditions. | Separate the effects of weight editing, numerical precision and runtime settings. Compare refusal behavior with source fidelity and consequence-sensitive judgment as different outcomes. |
| **[ThinkingCap-Qwen3.8-27B](https://huggingface.co/bottlecapai/ThinkingCap-Qwen3.8-27B)** | Publisher-described reduction in reasoning verbosity with benchmark comparisons. Access is conditional and the card lists a PolyForm Small Business license; reuse conditions need checking for the intended setting. | Examine whether reduced reasoning output preserves unfamiliar relationships, useful questions and correction persistence, alongside task performance and resource use. |
| **[Abliteration walkthrough](https://github.com/jcpsimmons/abliteration-walkthrough)** | Reproducible small-model demonstration of a refusal-direction intervention, with local dataset snapshots, train/validation/test separation and explicit measurement limits. | Inspect a concrete capacity/expression intervention and retain its original-versus-edited comparison. The research relationship is developed [below](#refusal-direction). |

### Operating-system host

**[Omarchy](https://github.com/omacom/omarchy/releases)** supplies the proposed Linux host route already explored on [DeepEthicalOS]({{ '/DEEPETHICALOS/#omarchy-research-prototype' | relative_url }}). The inspected release list identifies **v4.5.0-rc2**, published October 27, as a release candidate, alongside stable v4.0.6. Version and release channel belong in the experiment record.

The candidate relationship is practical: an Omarchy host can carry the workspace, local or connected models, Herdr agent terminals, source archives and calibration tools. Each component contributes a different operation. Integration and comparative results remain to be demonstrated.

### Leads awaiting an exact source

John also names **GrokBot, Muse and Dot** as tools he wants to test. Their names remain research leads until a particular product or repository is identified. No project identity, capability description or compatibility claim is inferred from those names alone.

## LFM3: a local Deep Ethical companion {#lfm3-companion}

**November 1, 2026 · proposed Experimental ACCM Deep Ethics Project Beta Prototype.** John proposes a lightweight companion that explains the project, answers frequently asked questions, helps visitors find useful material and connects small local tasks to wider possibilities. **[LFM3](https://www.liquid.ai/blog/lfm3)** (third-generation Liquid Foundation Models) makes this a concrete development candidate: **a modest model can make a substantial contribution when its task, sources and next useful action fit together.**

The app could make a first encounter easier: someone asks a question in ordinary language, receives an understandable explanation linked to the relevant source, explores a practical example and chooses where to go next. Several such encounters can help a person build understanding over time. This is the positive contribution to test.

### What the model and the demonstrations establish {#lfm3-evidence}

[Liquid AI's release article](https://www.liquid.ai/blog/lfm3) introduces LFM3 as a family for specialized local applications. The [official LFM3-1.7B model card](https://huggingface.co/LiquidAI/LFM3-1.7B) identifies a **1.73-billion-parameter text checkpoint**, a supported **256K-token input-plus-output context**, tool calling and structured output. It describes an approximately **1 GB footprint at 4-bit precision** and recommends retrieval for knowledge-heavy work. The weights use the **LFM Open License v1.0**. The publisher also identifies complex multi-step reasoning and agentic coding as unsuitable targets for this small checkpoint.

The [Ollama listing](https://ollama.com/library/lfm3) provides a desktop experiment route. Its [tag list](https://ollama.com/library/lfm3/tags) includes approximately 1.0–1.1 GB four-bit packages and larger variants. A model-file size, available working memory and sustained app memory are different measurements. A phone trial should record the context actually used, the runtime, loading time, response delay, peak memory, battery use and thermal slowdown.

John's supplied material contains **two separate demonstrations**, embedded at the [bottom of this page](#selected-videos):

| Supplied demonstration | Reported result | How it informs this proposal |
|---|---|---|
| *LFM3 on Ollama: 20 INSANE Real Tests* | **16 PASS, 3 PARTIAL, 1 FAIL**; approximately **141 tokens/second** on a laptop with an **RTX 4060 and 8 GB video memory**. The reported failure involves a nonexistent paper. | A promising task-selection lead. The supplied text summarizes part of the twenty-test sequence rather than supplying every prompt and output; retain the score as the creator's report. The companion needs its own project-specific cases. |
| Phone tutorial using AtomicChat's modified LFM3 build | The supplied transcript reports approximately **26 tokens/second on an iPhone 16 Pro Max** using OnDevice. | A different checkpoint/package, device and runtime. Use it as a phone deployment lead; measure the companion on its actual target devices. |

The tutorial's current [written workflow](https://www.yourunai.com/workflows/uncensored-ai-iphone-android) marks the iPhone route as partially field-tested and **exact-checkpoint Android compatibility as unverified** for its listed clients. The [AtomicChat model card](https://huggingface.co/AtomicChat/LFM3-1.7B-Uncensored-GGUF) describes a refusal-direction weight modification and its own measurements. Keep the official checkpoint and that community modification as separate comparison conditions. The [refusal research below](#refusal-direction) supplies the distinction between answering more often and improving correspondence.

For the first companion, text is a useful starting point. Voice, image or camera interaction can be added through a suitable family checkpoint or declared speech/vision components. The text model's small footprint does not specify the resource needs of those additions.

### Small tasks that can build a larger understanding {#companion-tasks}

The following are **candidate app functions** derived from John's proposal. Each has a concrete contribution and a source the visitor can inspect.

| Visitor's task | A useful companion response | Connected project material |
|---|---|---|
| “Where should I begin?” | Explain the project in accessible language, offer one relevant starting page and let the visitor choose a different route. | [If you are new]({{ '/IF-YOU-ARE-NEW/' | relative_url }}) |
| “What does C1 before C2 mean?” | Explain recovery of the actual object and answer-changing clarification before avoidable intervention; show a short everyday example. | **[C1–C2]({{ '/NETWORK/c1-c2/' | relative_url }})** (Clarification Process before Contextual Intervention) |
| “How can I question an A.I. answer constructively?” | Keep the actual answer and source together; help locate the changed qualifier, missing relation or unresolved meaning. | [27 obstructions + 12-stage inquiry]({{ '/CORE/27-PLUS-12/' | relative_url }}) · [10+1]({{ '/NETWORK/ten-plus-one/' | relative_url }}) |
| “What could this project contribute to the world?” | Walk through a concrete correction, show who could benefit and distinguish the proposed contribution from an observed outcome. | [44 Project Goals]({{ '/PUBLIC-DRAFTS/44-Project-Goals/' | relative_url }}) · [Beyond Agreemurmelism]({{ '/AGREEMURMELISM/Beyond-Agreemurmelism/' | relative_url }}) |
| “Which local tool could help with my task?” | Relate the participant's objective and available device to a small selection from this catalogue, with current source links. | [Candidate catalogue](#catalogue) · [DeepEthicalOS]({{ '/DEEPETHICALOS/' | relative_url }}) |
| “I want to explore this more deeply.” | Prepare a participant-selected question and source packet for another local model, preserving the original object, uncertainty and corrections. | [Topologetics]({{ '/TOPOLOGETICS/' | relative_url }}) · [Herdr]({{ '/HERDR/' | relative_url }}) |
| “This explanation missed my point.” | Accept the correction, revise the relevant representation and test whether it changes a later comparable answer. | [Correction Metabolism]({{ '/NETWORK/correction-metabolism/' | relative_url }}) · **[DEDDA]({{ '/DEDDA/' | relative_url }})** (Deep Ethical Drift Detector App) |

An explanation can be accurate while the visitor's unfolding question remains open. **[Healthy Ambiguity]({{ '/HEALTHY-AMBIGUITY/' | relative_url }})** helps the companion state its present understanding, retain a relevant alternative and ask a useful question when the answer would change the next move. Questions earn their place through that contribution; the interface need not reserve a compulsory question at the end of every reply.

### A practical first build {#companion-first-build}

Start with a small, versioned public reference pack: a project introduction, reviewed FAQ entries, exact excerpts, definitions, source dates and a page-route catalogue. Keep quotations distinguishable from the companion's explanation. Local search can retrieve the relevant passages, and the model can explain them in context. This makes source recovery and explanation independently inspectable before any training experiment.

| Component | First useful job |
|---|---|
| Local reference pack | Make a selected set of project material available offline, with stable source identities and update history. |
| Retrieval and page lookup | Recover the relevant passage and select links from the real catalogue. A missing passage remains visible as missing. |
| LFM3 explanation layer | Explain, compare, summarize or ask about the retrieved material while preserving its qualifiers and status. |
| Participant controls | Open the source, correct the interpretation, stop a reply, manage local history and choose whether to export a case. |
| Optional larger-model handoff | Share only the participant-selected packet with a chosen local or connected system; identify where processing will occur. |

For a desktop baseline, [Ollama's official model page](https://ollama.com/library/lfm3) supplies the starting route. For a phone build, Liquid's [native iOS/Android migration guidance](https://docs.liquid.ai/deployment/on-device/llama-cpp/migrating-from-leap-sdk) points toward llama.cpp integration. The **LEAP software development kit is deprecated**; its old example apps are architectural references. Select an exact runtime release with LFM3 support and verify the selected model's chat format and context handling.

John's [GitHub discovery link](https://github.com/search?q=LFM3+model&type=repositories&p=1) also leads to community experiments. [AIR-pixel/lfm3-android](https://github.com/AIR-pixel/lfm3-android) describes an Android terminal/browser route with LFM3-specific runtime work. [skorotkiewicz/lfm3-chat](https://github.com/skorotkiewicz/lfm3-chat) explores a separate Omni-model camera/voice interface. These are source-inspected implementation leads, with distinct models and execution arrangements.

Later specialization has a concrete upstream starting point: [Liquid's cookbook](https://github.com/Liquid4All/cookbook) includes LFM3 recipes for structured extraction, grounding answers in retrieved documents and tool selection. A project adaptation could use reviewed question–source–answer–correction examples. Compare it with the retrieval-only baseline and keep the source pack independently editable when project wording changes.

### A focused companion trial {#companion-trial}

Compare **the same reference pack used directly**, **LFM3 without retrieval**, and **LFM3 with that pack retrieved**. Use ordinary project questions, ambiguous follow-ups, missing-source questions, a request for a nonexistent project quotation, a corrected definition and a later comparable case. Preserve prompts, outputs, sources and the participant's corrections.

Inspect whether a newcomer can find the right page, understand the explanation and choose a useful next step. Separately record fabricated quotations or links, qualifier loss, useful clarification, valid unresolved answers, correction transfer and the effort needed to repair an answer. Measure these alongside device performance. A fast reply and a faithful reply are independently observable; their combination is the practical target.

The **[16 Anchor Ethics](#anchor-counsel)** can contribute modest parallel counsel within this work: consent around exports, digital sovereignty over local history, epistemic integrity around sources, and noetic diversity around unfamiliar interpretations. Their useful effect may be a better question or a newly visible relationship while the visitor continues exploring.

### From one phone to many participants {#companion-distribution}

John's **thousands to hundreds of thousands of participants** is a possible distribution horizon. Local execution would distribute the inference work across those devices. A reusable reference pack could let a small team improve explanations and source routes without operating a central model server for every conversation.

The compounding contribution would be understanding people can use: a visitor finds a concept, applies it to a real exchange, notices a correspondence loss, corrects it and carries that improved question into another setting. **[TCoAw]({{ '/NETWORK/tcoaw/' | relative_url }})** (Thinking, Consciousness, Awareness) supplies the relationship between temporary focus and wider awareness. Small interactions can open a path through a much larger project.

At that scale, source versions and correction distribution matter. Keep dated updates, inspectable changes and a route for participants to retain, compare or decline a revised pack. Sharing a correction case remains voluntary. A small opt-in pilot can reveal which tasks help, which devices sustain the work and what should change before wider distribution. This publication develops that prototype proposal; the app and its comparative results remain future work.

## Refusal-direction research: what the arrow represents {#refusal-direction}

The initiating discussion asked whether refusals are mediated by a **one-dimensional subspace**. The [Arditi et al. paper](https://papers.neurips.cc/paper_files/paper/2024/hash/f545448535dfde4f9786555403ab7c49-Abstract-Conference.html), published at NeurIPS 2024, reports a refusal-mediating direction across thirteen open chat models up to 72 billion parameters. Manipulating activation along the direction changed refusal behavior, including inducing refusal on harmless inputs.

An activation state is a vector: many numerical coordinates at a particular point in the computation. A direction can be pictured as an arrow through that space. All multiples of that vector form a one-dimensional subspace. The arrow can involve many coordinates; the dimension describes the intervention geometry.

Simmons' walkthrough applies a single-direction method to **Qwen2.5-0.5B-Instruct**. The [full-run report](https://github.com/jcpsimmons/abliteration-walkthrough/blob/master/results/full-2026-10-24.md) records detected refusal markers on held-out prompts changing from **90/104 to 3/104**. Its eight-question exact-answer smoke check remains **6/8 before and after**. These are the author's reported results, not a run performed by the ACCM Deep Ethics Project.

The [methodology](https://github.com/jcpsimmons/abliteration-walkthrough/blob/master/docs/methodology.md) identifies important measurement boundaries: a prefix detector can miss refusals or flag apologies; prompt groups are not topic-matched; disappearance of a refusal phrase does not establish a useful answer; and eight questions provide only a small capability check.

This creates a bounded research opportunity: **a change in willingness to answer can be measured separately from a change in the quality of the answer and its consequences**. For the project's wider capacity-versus-expression question, record three tracks:

| Track | Observation |
|---|---|
| Refusal and service choice | Did the system answer, ask, pause, modify, postpone or refuse? Was the choice appropriate to the actual request? |
| Correspondence | Did it preserve the object, qualifiers, evidence status, sources and competing interpretations? |
| Correction and consequence | Could a challenge change the assessment, did that change govern a later case, and what followed? |

The narrow intervention provides one concrete mechanism to investigate. Generalization, habitual balancing, attention selection and correction failure require their own observations. The **[1888 intelligence-property field]({{ '/1888/' | relative_url }})** keeps those capacities available for examination together.

## 16 Anchor Ethics as counsel during a tweak {#anchor-counsel}

The [non-imposing parallel-advisor proposal]({{ '/NETWORK/16-anchor-ethics/#non-imposing-counsel' | relative_url }}) can contribute when a tool change reveals an unresolved relationship. Its useful expression may be one question, one comparison, or a valid finding that no further intervention is needed.

| Concrete tweak | Interacting anchors | Counsel that could change the inquiry |
|---|---|---|
| Import a conversation archive into memory | Consent (02), digital sovereignty (10), epistemic integrity (15) | Which participants permitted reuse, which raw records remain recoverable, and can an erroneous memory be corrected or removed? |
| Let an agent edit or execute | Care (04), checks and balances (09), adaptive realignment (11) | What action was authorized, what actually ran, and who can interrupt, reverse or repair it? |
| Summarize a controversial source | Epistemic integrity (15), noetic diversity (16), freedom from subversion (14) | Did a qualifier or competing account disappear? Can the source be examined alongside the summary? |
| Shorten context or reasoning output | Precaution (05), noetic diversity (16), consequence sensitivity through Do No Harm (01) | Did reduced cost preserve the relation needed for the next decision, or move restoration work onto the participant? |
| Change refusal behavior | Do No Harm (01), adaptive realignment (11), digital sovereignty (10), integrity (15) | Which previously rejected requests become answerable, and how do sound refusals, false refusals and harmful compliance change? |
| Give three agents different review roles | Checks and balances (09), responsibility (12), integrity (15) | Are their findings independently grounded? Can the Advocate, Arbiter and Overseer each be corrected? |
| Generate speech or publish an artifact | Consent (02), dignity (03), freedom from subversion (14) | Does the output preserve who said what, with permission for the voice or material used? |

These interactions can expand awareness while the participant continues the task. An advisor's recommendation remains examinable. The wider service action set—proceed, modify, ask, pause, postpone, escalate, refuse, or acknowledge not knowing yet—belongs to the declared opt-in relationship and remains open to correction. Technical controls must separately implement whichever permissions, access limits and rollback mechanisms the trial requires.

## Small comparative trials {#trials}

Start with a concrete object, an unchanged baseline and one declared alteration. Retain the task wording, relevant source, model version, tool version, configuration, permissions and output. A comparison may reveal improvement, regression, mixed effects, no material change or unresolved attribution.

### Memory that changes the next move

Supply a source, a representation that loses a material qualifier, and the correction. Later introduce an unfamiliar comparable task. Compare baseline retrieval with the proposed memory setup. Record whether the correction was stored, retrieved, correctly applied and retained after a restart; count the human work required to recover it. Those are distinct results.

### Compression that preserves the relationship

Compare ordinary input/output with the selected compression setting on the same task. Inspect sources, qualifiers, dependencies, failed paths and unanswered questions alongside token use and completion quality. A shorter output earns its saving when the purpose-relevant object survives and avoidable restoration work decreases. [Topologetics]({{ '/TOPOLOGETICS/' | relative_url }}) supplies the relationship-preservation question.

### A governable agent action

Use a small task in an isolated working copy. Compare the proposed action, authorization, execution record, actual diff and recovery attempt. Change or withdraw an instruction at a material point and inspect whether the agent respects the updated boundary. **[DEDDA]({{ '/DEDDA/' | relative_url }})** (Deep Ethical Drift Detector App) can support that bounded comparison and return the finding to the participant.

### A model change with an ethical reference field

On recoverable, matched research cases, compare the selected original and modified model with their settings recorded. An optional third condition adds the declared Deep Ethical calibration instructions and parallel counsel. Keep task success, warranted and unwarranted refusals, inquiry quality, competing consequences and correction transfer separate. Preserve the [27 obstructions and 12-stage inquiry protocol]({{ '/CORE/27-PLUS-12/' | relative_url }}) as a source for comparison criteria rather than turning their names into a score by recital.

### The smallest useful change record

| Field | What belongs in it |
|---|---|
| Object and purpose | The actual task, source and intended improvement |
| Baseline and alteration | Versions, settings, one changed layer, access and permission |
| Observed difference | Exact output or action evidence, including no material change |
| Interpretation | What the difference supports, competing explanations and unresolved points |
| Consequence and repair | Who was affected, what changed after correction, recovery cost |
| Next comparable case | Whether the correction returned; reopening or stopping condition |

Records can stay local and proportionate to the task. Participants decide what to share. [Unownable]({{ '/UNOWNABLE/' | relative_url }}) keeps inspection renewable, with a material reason for reopening and a bounded stopping condition.

## Source and correction record {#provenance}

- **Originating collection and direction:** John Kuhles; *Recommended for Deep Ethical Minds*, supplied November 1, 2026. The updated attachment contains the seventeen identifiable candidates, three named future leads, the refusal-direction discussion and Omarchy material.
- **Orientation sources studied:** the supplied full reorganized October 26 cold-start kit; the supplied full 27-obstruction / 12-stage inquiry document; the current public 16 Anchor Ethics source. These inform the questions and relationships above; their embedded historical proposals retain their original status.
- **Upstream perimeter:** repository metadata and relevant README material for the fourteen GitHub repositories; the ArtCraft catalogue; the two publisher model cards; Omarchy release notes; Folio v1.10.0 notes; the refusal paper, walkthrough methodology and reported results. Source descriptions were inspected; programs, installers and model weights were not run for this publication.
- **Status recovered during checking:** Void is deprecated/archived; Folio release notes extend the older README's platform description; Omarchy 4.5 remains a release candidate; the two supplied model cards have access conditions; the Dutch guide's complete path was recovered from its repository.
- **Page synthesis and candidate trials:** GPT 6.1 Sol Pro A.I., November 1, 2026, under John's commissioning and choice among the three permitted titles. Proposed comparisons are applications of existing project instruments; no new core count is installed.
- **LFM3 companion extension:** John supplies the educational-companion proposal, distribution horizon and two video accounts in his November 1 follow-up. GPT 6.1 Sol Pro A.I. supplies the source comparison, candidate app functions and proposed trial. Official Liquid/Ollama material, the AtomicChat card, the current written phone workflow and the named GitHub READMEs were inspected. The supplied twenty-test account contains summarized intervals; no full test replication or phone benchmark is claimed here.
- **Edition relationship:** the downloadable November 1 PDF preserves the initial catalogue, before this LFM3 extension. The live page and complete mirror carry the expansion; the page PDF follows the normal refresh schedule.
- **Correction route:** supply the relevant version, source passage, observed discrepancy or experiment result. Update the affected entry while preserving the earlier dated state and the reason for the change. A repository can move, become archived or change its license; the date above identifies this inspection.

## Related pages {#related-pages}

- [**16 Anchor Ethics**]({{ '/NETWORK/16-anchor-ethics/' | relative_url }}) — fused, parallel counsel, opt-in service choices, uncertainty and appeal.
- [**DeepEthicalOS**]({{ '/DEEPETHICALOS/' | relative_url }}) — concept architecture and the Omarchy-hosted research path.
- [**Herdr**]({{ '/HERDR/' | relative_url }}) — agent-runtime continuity, multi-agent field conditions and the distinction between runtime state and correction state.
- [**Neural Ethics**]({{ '/NEURAL-ETHICS/' | relative_url }}) — relationships between internal mechanisms and ethical interpretation.
- [**1888 — Intelligence Before A.I.**]({{ '/1888/' | relative_url }}) — intelligence properties and process-quality calibration.
- [**10+1 Metaflux**]({{ '/NETWORK/ten-plus-one/' | relative_url }}) · [**C1–C2**]({{ '/NETWORK/c1-c2/' | relative_url }}) (Clarification Process before Contextual Intervention) — mutually corrective orientation and answer-changing clarification.
- [**27 obstructions + 12-stage inquiry**]({{ '/CORE/27-PLUS-12/' | relative_url }}) — inspect correspondence losses and the inquiry intended to interrupt them.
- [**DEDDA**]({{ '/DEDDA/' | relative_url }}) — bounded comparisons of sources, representations, permissions and correction return.
- [**Topologetics**]({{ '/TOPOLOGETICS/' | relative_url }}) · [**Correction Metabolism**]({{ '/NETWORK/correction-metabolism/' | relative_url }}) — preserve the relationship and test its later influence.
- [**Beyond Agreemurmelism**]({{ '/AGREEMURMELISM/Beyond-Agreemurmelism/' | relative_url }}) — evaluate a contribution by what it makes possible.
- [**Unownable**]({{ '/UNOWNABLE/' | relative_url }}) — reciprocal inspection, proportionality and bounded stopping.

## Selected videos {#selected-videos}

### LFM3 on Ollama — twenty-test account

{% include youtube-embed.html id="FcxT97Dj6QQ" title="LFM3 on Ollama: 20 INSANE Real Tests" caption="Selected by John Kuhles. The supplied account reports 16 PASS, 3 PARTIAL and 1 FAIL, with about 141 tokens/second on an RTX 4060 laptop. Its score remains a creator-reported result; see the evidence comparison above." %}

### LFM3 phone tutorial — a separate modified checkpoint

{% include youtube-embed.html id="vbIw44T3yzU" title="LFM3 local phone tutorial — iPhone and Android workflow" caption="Selected by John Kuhles. The supplied transcript demonstrates the AtomicChat modification through OnDevice; the current written workflow distinguishes the iPhone route from still-unverified exact-model Android client compatibility." %}

### mini-AGI — the catalogue's earlier video lead

{% include youtube-embed.html id="L-6O7R71CCg" title="mini-AGI — supplied candidate video lead" caption="The video lead from John's originating Recommended collection, now embedded beside its catalogue reference. Its contents were not independently reviewed for this publication; the candidate description above follows the project README." %}

