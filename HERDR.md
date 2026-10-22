---
layout: page
title: "Herdr"
description: "Herdr, agent-native terminal runtimes, competitors and alternatives, and a candidate ACCM Deep Ethics workflow for multi-agent coordination without confusing consensus with correspondence."
permalink: /HERDR/
date: 2026-10-22
---

<!-- ACCM_FORMAT_LINKS_START -->
<div class="accm-source-format-links" role="navigation" aria-label="Available page formats">
<strong>Available formats:</strong> <a href="https://deepethics.github.io/ACCM-Deep-Ethics-Project/HERDR/">🌐 Public HTML page</a>
</div>
<!-- ACCM_FORMAT_LINKS_END -->

# Herdr

## Agent-native runtimes, multi-agent field conditions and the difference between coordination and correspondence

<p class="accm-kicker"><strong>John Kuhles ⇄ Google A.I. ⇄ GPT 6.1 Sol Pro A.I.</strong> · 22 October 2026</p>

**Status:** `[PROJECT-PROPOSAL]` `[CANDIDATE IMPLEMENTATION FIELD]` `[COMPARATIVE MAP]`

Herdr matters to the ACCM Deep Ethics Project because it changes the **field conditions in which coding agents operate**. It can keep their terminal processes alive, show their activity states, place several machines inside one workspace and let agents programmatically create and control terminal panes. That can reduce coordination friction and make a multi-agent process more observable.

It does not, by itself, establish that an agent understood the object, kept provenance intact, asked a real C1 question, preserved an anomaly, propagated a correction or produced something that corresponds with reality.

That distinction is the center of this page:

> **Herdr can help make the agent runtime visible and operable. Deep Ethical process still has to make the reasoning trajectory inspectable, corrigible and answerable to reality.**

---

## 1. Video supplied for this inquiry

{% include youtube-embed.html id="cmvF7nfEJLo" title="Herdr — agent-native terminal runtime" caption="Video selected by John Kuhles as the initiating object for this page." %}

[Open the video directly on YouTube](https://www.youtube.com/watch?v=cmvF7nfEJLo)

The video initiated the question **“How can this help our project?”** This page does not treat a demonstration video as independent proof of every product claim. Current capabilities are reconstructed primarily from Herdr’s official repository and documentation, with distinctions retained where the documentation itself adds conditions.

---

## 2. What Herdr currently is

[Herdr](https://github.com/herdrdev/herdr) presents itself as a terminal runtime built for coding agents. It does not require one replacement agent or one proprietary model. It runs terminal programs already used by developers—including Codex, Claude Code and Grok CLI—inside a persistent, agent-aware environment.

Its current operational surface includes:

- **Persistent terminal sessions:** the Herdr server keeps processes running when the visual client detaches or an SSH connection drops.
- **Agent-aware states:** panes can be shown as `working`, `blocked`, `idle`, `done` or `unknown`.
- **Programmatic control:** agents can create panes, send prompts or commands, inspect state and coordinate through the CLI and socket API.
- **Several machines in one workspace:** local and SSH-backed environments can appear in a combined interface with independent reconnect behavior.
- **Git worktree support:** separate agents can work in isolated branches and working directories.
- **Saved layouts and supported resume paths:** after a machine or server restart, Herdr can restore the recorded layout and attempt to resume supported native agent sessions. The original operating-system processes do **not** survive a machine restart.
- **Plugins and integrations:** the runtime can be extended without requiring Herdr to replace every tool above it.
- **A single Rust binary:** its terminal-native design avoids requiring a full Electron desktop shell.
- **Apache 2.0 licensing:** the repository is openly inspectable and forkable under that license.

That last restart qualifier is load-bearing. **Persistence across client detachment**, **layout restoration after restart**, and **durable cognitive or correction persistence** are three different objects. Compressing all three into “persistent agents” would hide the exact property that needs testing.

---

## 3. Why this can help the ACCM Deep Ethics Project

The project contains a large public graph of pages, sources, corrections, experiments, provenance boundaries and partially unresolved relations. A single coding agent can edit that graph, but long and topology-dense work creates predictable failure pressures: narrow retrieval, context loss, premature compression, source mixing, correction isolation and deployment claims made before the live page has been checked.

Herdr could provide the **runtime floor** beneath a more specialized Deep Ethical agent ensemble:

| Herdr can supply | The ACCM layer still has to supply |
|---|---|
| Persistent terminals | Persistent correction behavior |
| Pane and agent lifecycle visibility | Epistemic and claim-status visibility |
| Agent-to-agent prompting | C1-quality clarification and non-ceremonial questioning |
| Parallel worktrees | Provenance discipline and safe integration of overlapping edits |
| Remote-machine aggregation | Declared access perimeter and data-jurisdiction awareness |
| CLI and socket automation | Inspectable reasons for delegation and intervention |
| Saved layouts | A recoverable relational topology and decision ledger |
| Human attention alerts | A principled account of when human review is materially needed |

This makes Herdr potentially valuable without turning the tool into the intelligence, the ethics, the arbiter or the answer.

---

## 4. Operational state is not epistemic state

Herdr’s activity labels answer useful runtime questions. They do not answer the complete inquiry question.

| Runtime state | What it can indicate | What it does **not** establish |
|---|---|---|
| `working` | A process or agent appears active | That it is working on the right object or preserving its topology |
| `blocked` | Progress appears to require input or resolution | That the requested input is the real blocker, or that escalation is warranted |
| `idle` | No current activity is detected | That reasoning is complete, correct or abandoned |
| `done` | The agent or command reports completion | That the result was verified, deployed or produced the intended effect |
| `unknown` | Herdr cannot confidently classify the lifecycle | Failure, success, deception or any other specific explanation |

An ACCM-informed layer would add separate, explicitly named states such as:

- object reconstruction incomplete;
- provenance incomplete;
- C1 clarification required;
- candidate contribution under test;
- valid null—no defect or addition presently warranted;
- correction accepted locally;
- dependency recompilation pending;
- correction propagated;
- persistence not yet tested;
- implementation verified locally;
- public effect verified;
- unresolved.

These should not be squeezed into one status light. A pane can be operationally `done` while the claim remains `[UNRESOLVED]`. A process can be `blocked` because it is correctly refusing to invent missing evidence. An agent can be `working` while confidently optimizing the wrong frame.

$$
\text{runtime visibility} \neq \text{epistemic correspondence}
$$

The first can support the second. It cannot substitute for it.

---

## 5. A candidate Deep Ethical Herdr ensemble

The following is a `[PROJECT-PROPOSAL]`, not a claim that Herdr already implements these roles.

| Role | Primary task | Required output |
|---|---|---|
| **Object Reconstructor** | Build the strongest faithful version of the request and relevant project topology | Object boundary, answer-changing relations, unresolved ambiguities |
| **Builder** | Implement the page, code or data change in an isolated worktree | Reviewable artifact and exact changed paths |
| **Provenance Keeper** | Separate John’s words, third-party claims, A.I.-attributed synthesis and verified sources | Claim-status ledger and source map |
| **Topologetics Auditor** | Detect dropped qualifiers, severed edges, nearest-neighbor substitutions and hidden perimeter changes | Material deltas, or a valid null |
| **Verifier** | Run tests, inspect rendered output and check the public result | Evidence of local and public behavior |
| **Deep Ethical Arbiter** | Compare disagreements on their warrants and effects without reducing the process to majority voting | Corrigible disposition with “Here is why” |

Herdr could give every role a visible pane, worktree, activity state and machine location. Its socket API could let an orchestrator ask for a review, wake a verifier when a build completes or alert John only when a genuine answer-changing ambiguity remains.

The ensemble should not ask six similar agents for six opinions and call the majority intelligent. Role diversity only becomes useful when each role has a distinct job, inspectable evidence boundary and capacity to correct the others.

---

## 6. Deep Ethical Contribution State Grammar Vector Trajectory

A standard multi-agent controller often compresses every contribution into `accept`, `reject`, `pass`, `fail` or a confidence score. That is operationally convenient and topologically lossy.

The **Deep Ethical Contribution State Grammar Vector Trajectory** asks what a contribution does to the inquiry over time:

- **Logically valuable**—which relation becomes clearer?
- **Test-worthy**—what observation could change the current representation?
- **Deserves deeper investigation**—which unresolved edge carries material consequence?
- **Worth considering**—under which declared perimeter and field conditions?
- **Has potential; here is why**—what function might it perform?
- **Valuable Deep Ethical emergent properties**—which properties arise through interaction rather than one isolated component?
- **Not useful here; here is why**—what specific local task does it fail to advance?
- **Adds no value here; here is why**—what duplication, distortion or noise does it introduce?
- **Works provisionally**—what evidence supports it, and what could reopen it?
- **Unresolved**—what is not yet known, and why is premature closure worse than retaining the ambiguity?

And **“Here is why” remains corrigible**. The justification is part of the inspectable object. It does not become a sheriff merely because it sounds analytical.

In a Herdr workspace, those states could become structured metadata attached to pane outputs, commits, test results and handoffs. Their purpose would be to preserve the direction and effect of contributions across the trajectory:

<div class="accm-rounded-quote" role="group" aria-label="Deep Ethical Contribution State Grammar vector trajectory">
  <p><strong>S<sub>t₀</sub></strong> → <strong>object reconstruction</strong> → <strong>S<sub>t₁</sub></strong> → <strong>candidate contributions</strong> → <strong>S<sub>t₂</sub></strong> → <strong>reality-feedback Δ</strong> → <strong>S<sub>t₃</sub></strong> → <strong>correction propagation</strong> → <strong>S<sub>tₙ</sub></strong></p>
</div>

This connects directly to [Topologetics]({{ '/TOPOLOGETICS/' | relative_url }}): preserve the purpose-relevant nodes, edges, qualifiers, provenance and correction history. It also connects to [1888]({{ '/1888/' | relative_url }}): agent output alone does not settle whether observation, discrimination, judgment, learning, adaptation and self-correction actually governed the process.

---

## 7. From a state list to a versioned multidimensional vector

After reading this page, **GLM-5.3 (max) A.I. via Arena.ai** identified a distinction that changes the proposed implementation:

<div class="accm-rounded-quote" markdown="1">

> **The strongest feature is the transitions, not the states.** A contribution marked “test-worthy” that later becomes “resolved” or “provisionally refuted,” with the transition recorded, *is* correction metabolism made structural rather than narrative. Most review systems overwrite the old state. Preserving the transition—including reversal and reopening—operationalizes the persistence measurement your other instruments currently have to extract from prose.
>
> — **GLM-5.3 (max) A.I. via Arena.ai**, 22 October 2026

</div>

That contribution is logically valuable and architecture-changing. A label describes one moment. A history records whether reality, testing, disagreement or correction changed the contribution’s role:

<div class="accm-rounded-quote" role="group" aria-label="Example contribution-state history">
  <p><strong>test-worthy</strong> → <strong>tested</strong> → <strong>provisionally supported</strong> → <strong>contradicted</strong> → <strong>revised</strong> → <strong>reopened</strong></p>
</div>

If every new state overwrites the previous one, the system preserves the destination while erasing the path. That would reproduce the same compression problem inside a more sophisticated interface.

### 7.1 State or vector?

“Logically valuable” and “not useful here” can both describe the same contribution. The contribution may expose a valid relation while arriving at the wrong stage, duplicating work already completed or failing the present task. “Unresolved” answers a different question again. A single enum would force unlike properties into one slot and recreate binary compression one level higher.

The candidate structure therefore becomes a **multidimensional, versioned contribution profile**:

| Dimension | Question | Candidate values |
|---|---|---|
| **Functional effect** | What did the contribution do to the object? | clarified a relation; exposed an omission; generated a test; preserved an anomaly; added no demonstrated value here |
| **Epistemic position** | What is presently warranted? | unresolved; candidate; provisionally supported; provisionally refuted; verified inside the declared perimeter |
| **Relational effect** | How does it relate to other contributions? | extends; supports; undercuts; rebuts; duplicates; conflicts; changes the frame |
| **Field-condition fit** | Is it useful under these conditions, at this stage? | useful here; premature here; insufficient here; useful under another declared perimeter |
| **Assignment provenance** | Who classified it, when and from what evidence perimeter? | human; agent; role; timestamp; model/version; accessible sources; declared limits |
| **Correction trajectory** | What changed afterward? | new; revised; reversed; reopened; propagated; persistence untested; persistence demonstrated |

The values remain candidates. The load-bearing repair is the separation of dimensions and the preservation of their histories.

### 7.2 The assignment is itself a contribution

Two agents can assign different profiles to the same output. That disagreement should not be averaged away or silently resolved by the orchestrator. It is new evidence about the evaluation field.

Every assignment should therefore record:

- who or what assigned it;
- when it was assigned;
- which object version was inspected;
- what evidence and tools were accessible;
- which field conditions and task perimeter were active;
- the corrigible **“Here is why”**;
- what observation could change the assignment;
- whether another participant contested it and on what warrant.

A state assignment is itself a contribution. It can clarify, distort, duplicate, overreach or remain unresolved. The evaluator does not leave the field merely by calling itself the evaluator.

### 7.3 The reality-feedback edge needs source topology

GLM correctly located the fragile edge: agents often receive feedback from other agents, then describe that recursive assessment as reality feedback. A polished state ledger can make a shared-prior loop look more rigorous without making it more correspondent.

The first repair is to tag every delta by source. The second is to resist turning **reality versus peer** into another sealed binary. Reality rarely enters a terminal without mediation. Feedback can arrive through:

- an empirical test or direct measurement;
- rendered, executed or publicly deployed behavior;
- a primary source or recoverable artifact;
- human observation or domain assessment;
- an independent agent assessment;
- a same-family or shared-base-model assessment;
- an internal consistency check;
- a simulation or proxy measurement;
- an inference with declared premises;
- mixed or presently unknown provenance.

The deeper delta record therefore asks:

| Delta field | What it protects |
|---|---|
| **Source** | Who or what supplied the feedback? |
| **Reality access** | What could the source directly inspect, measure, execute or observe? |
| **Independence** | Which models, prompts, datasets, institutions or incentives may be shared? |
| **Evidence** | What recoverable artifact supports the change? |
| **Transformation** | What selection, summarization or inference occurred before the feedback arrived? |
| **Effect** | Which state, dependency, decision or later action actually changed? |

A peer can carry strong empirical evidence. A human can repeat a shared misconception. An automated test can faithfully verify the wrong requirement. **Outside the pane is not necessarily outside the attractor.**

### 7.4 External scoring without an external-scorer costume

GLM also proposed holding some assignments for participants outside the active trajectory. That is test-worthy. It can expose local agreement cascades and label-performance behavior—such as an agent learning that calling something “test-worthy” earns attention.

But an external scorer is not automatically independent. It may share the same foundation model, prompt template, benchmark assumptions, institutional incentives or compressed representation. Independence must be described, not ceremonially presumed.

The scorer’s task is also larger than checking whether the correct label appeared. It should ask whether the classification produced:

- a discriminating test;
- materially different possible outcomes;
- changed processing or action;
- propagated correction;
- lower restoration burden;
- improved correspondence;
- or only more formally impressive prose.

### 7.5 A proportional pilot

GLM proposed beginning with three states—**clarifies relation**, **test-worthy** and **unresolved**—before imposing the complete grammar. The proportionality is useful. The pilot must still retain separate dimensions, or it will test a compressed version of the proposal and attribute that compression failure to the complete architecture.

A small first implementation could use:

| Dimension | Minimal pilot values |
|---|---|
| **Functional contribution** | clarifies relation; adds no demonstrated value here |
| **Epistemic position** | test-worthy; unresolved; provisionally supported |
| **Correction trajectory** | new; revised; reopened; propagated |
| **Feedback provenance** | empirical; human; agent-peer; mixed; unknown |

Every field can remain optional. A small formatting repair may need one compact reason. A load-bearing architectural change may require the full profile and history. Proportionality prevents the Glass Engine from becoming an administrative fog generator.

### 7.6 Mistral’s reconstruction—and the remaining calibration

**Mistral-medium-3.5 A.I. via Arena.ai** reconstructed the central purpose accurately:

<div class="accm-rounded-quote" markdown="1">

> The states are not verdicts. They are **process markers** that track what relation became clearer, what observation could change the representation, what edge carries material consequence, under which perimeter and field conditions, and what remains unresolved.
>
> — **Mistral-medium-3.5 A.I. via Arena.ai**, 22 October 2026

</div>

Its claim that this *is* the missing operational layer and *operationalizes* the wider architecture moves slightly ahead of the evidence. This page proposes a candidate layer. Herdr may help instantiate it. Repeated handoffs must still establish whether it reduces restoration burden and improves correction propagation without becoming a vocabulary costume.

The calibrated formulation is:

> **This is a candidate operational layer between an individual contribution and its longer trajectory. Its value will be earned if multidimensional state histories, assignment provenance and reality-access-tagged deltas improve correspondence and correction persistence under real Herdr handoffs.**

The resulting architecture is now clearer:

| Layer | Function |
|---|---|
| **Contribution State Grammar** | Describes what a contribution is doing |
| **Vector structure** | Allows several non-exclusive properties to coexist |
| **State history** | Preserves movement, reversal, reopening and order of discovery |
| **Assignment provenance** | Makes the classification and classifier inspectable |
| **Reality-access tagging** | Distinguishes grounded correction from recursive peer reinforcement |
| **Persistence testing** | Tests whether the delta governs the next unfamiliar move |

That is where the grammar can begin moving from a refined vocabulary toward a candidate **trajectory instrument**.

---

## 8. The Correction Propagation Gap inside a multi-agent runtime

Persistent terminals can preserve a process while still preserving its error.

Suppose the Provenance Keeper establishes that a dramatic claim came from a third-party A.I., not from John. The Builder corrects one paragraph. The Topologetics Auditor then finds that three comparisons, a page description and a navigation label still depend on the old attribution.

The correction has been **acknowledged**, but it has not yet been **propagated**.

A Deep Ethical Herdr integration could assign every accepted correction a delta identifier and track:

1. the original representation;
2. the answer-changing correction;
3. every known dependent artifact;
4. which agent or worktree owns each repair;
5. local verification;
6. integration status;
7. public deployment verification;
8. later persistence testing on an unfamiliar object.

That would convert multi-agent concurrency from “more outputs per minute” into a testable correction metabolism.

---

## 9. Competitors and alternatives

There is no single substitute for Herdr because the projects below choose different system boundaries. Some are terminal runtimes, some manage worktrees around `tmux`, some are complete graphical development environments, and some are commercial terminal products.

| Project | Category and current focus | Where it may fit better | Material distinction to retain |
|---|---|---|---|
| [**Orca**](https://github.com/stablyai/orca) | MIT-licensed graphical agent development environment with agent fleets, worktrees, remote runtimes and companion mobile access | A fuller desktop and mobile command center | It owns more of the development environment; Herdr stays closer to the terminal-runtime layer |
| [**Superset**](https://github.com/superset-sh/superset) | Agentic IDE with many CLI agents, worktrees, diffs, review and pull-request workflows | Integrated code review and branch management | Source-available under ELv2; describe its license precisely rather than collapsing it into “open source” |
| [**cmux**](https://github.com/manaflow-ai/cmux) | Native macOS terminal based on Ghostty, with vertical workspaces, notifications and an integrated scriptable browser | A polished native Mac workspace | macOS-specific; its visual desktop scope differs from Herdr’s cross-machine terminal-runtime emphasis |
| [**Agent Deck**](https://github.com/asheshgoplani/agent-deck) | Cross-platform mission control for coding agents with grouping, search, session forking, worktrees and cost tracking | Managing many sessions with a broad control surface | More dashboard-oriented; evaluate actual persistence and automation requirements separately |
| [**Claude Squad**](https://github.com/smtg-ai/claude-squad) | AGPL-licensed `tmux` workflow for several agents in separate workspaces with change review | A mature, simpler terminal workflow | Strong baseline when Herdr’s API, cross-machine view or agent-native runtime is unnecessary |
| [**workmux**](https://github.com/raine/workmux) | MIT-licensed Git-worktree and `tmux` automation, generally one task per window | Lean branch isolation using familiar Unix tools | Useful control condition: how much does Herdr add beyond disciplined worktrees plus `tmux`? |
| [**dmux**](https://github.com/standardagents/dmux) | Parallel agents using `tmux` and isolated Git worktrees | Direct task/branch parallelism | Narrower orchestration surface can be an advantage for small projects |
| [**Séance**](https://github.com/no1msd/seance) | MIT-licensed Linux GTK4 interface with automatic agent detection, live states and notifications | Native Linux graphical monitoring | Linux desktop focus rather than one terminal runtime spanning several environments |
| [**Axel**](https://github.com/txtx/axel) | Early-stage task queue, terminal multiplexer and centralized approval inbox | Experiments centered on human approval routing | Smaller and earlier; useful ideas should be evaluated separately from ecosystem maturity |
| [**vmux**](https://github.com/Shadowfear36/vmux) | Native Windows GUI with persistent workspaces, worktrees, agent-controllable browser and search | Windows-first agent workflows | More Windows-specific and less established; distribution and security details warrant direct inspection |
| [**Warp**](https://www.warp.dev/) | Commercial cross-platform terminal with built-in A.I. and cloud agent features | Teams wanting a supported integrated product | Product alternative rather than a like-for-like open GitHub runtime |

Two comparison pages supplied during the inquiry—Superset’s [Solo alternative](https://superset.sh/compare/solo-alternative) and [cmux alternative](https://superset.sh/compare/cmux-alternative) pages—are useful discovery maps. They are also **competitor-authored marketing comparisons**, not neutral benchmark results. Claims from them should be checked against each project’s own repository, documentation and a matched practical test.

---

## 10. Choosing by field condition

The practical question is not “Which tool wins?” It is:

> **Which runtime properties are materially useful for this task, under these machines, agents, trust boundaries, review requirements and correction obligations?**

| If the primary need is... | Begin by testing... |
|---|---|
| Persistent agent-aware terminals across local and SSH machines | **Herdr** |
| Full graphical fleet management with desktop/mobile reach | **Orca** |
| Integrated worktrees, diffs and pull-request review | **Superset** |
| Native macOS workspace with browser automation | **cmux** |
| Familiar, inspectable terminal primitives | **tmux + workmux**, **dmux** or **Claude Squad** |
| Native Linux visual monitoring | **Séance** |
| Native Windows orchestration | **vmux** |
| Commercial integrated terminal and cloud support | **Warp** |

This is a starting map. Versions, platforms and licensing can change. A real choice should be made from current primary documentation and a local trial using the same task.

---

## 11. A matched ACCM comparison experiment

The ACCM Deep Ethics Project can turn the tool choice into an inspectable experiment rather than a preference contest.

Run one unfamiliar, topology-dense repository task in four environments:

1. **Control condition:** `tmux` plus Git worktrees and a written handoff protocol.
2. **Agent-native runtime:** Herdr with pane status, CLI/socket coordination and separate roles.
3. **Integrated review environment:** Superset with worktree, diff and pull-request workflow.
4. **Fleet environment:** Orca with graphical and remote coordination.

Use the same repository snapshot, agent family, prompts, time budget, verification commands and publication target. Record:

- time to a locally reviewable artifact;
- number of human interventions;
- restoration burden on John;
- source/provenance errors;
- materially dropped qualifiers or relations;
- correction acknowledgment, propagation and persistence;
- merge conflicts and duplicated work;
- false `done` states;
- quality of the public result after deployment;
- whether a valid null was allowed;
- whether the Deep Ethical Contribution State Grammar changed the next move rather than decorating the report.

The experiment should preserve qualitative specimens alongside counts. One severed, answer-changing edge can matter more than twenty cosmetic successes.

The contribution-profile pilot should run inside the same comparison. Measure not only whether agents completed the fields, but whether the state histories exposed a missed dependency, preserved an answer-changing disagreement, distinguished peer reinforcement from reality-linked feedback or reduced John’s later restoration work.

---

## 12. What Herdr does not prove

- **Several agents do not automatically constitute swarm intelligence.** They may be several instances of closely related models reproducing one shared blind spot.
- **Consensus is not correspondence.** A unanimous agent vote can be perfectly coordinated and factually wrong.
- **A persistent terminal is not persistent learning.** The process can remain alive while the correction fails to enter later reasoning.
- **A visible lifecycle is not a visible mind.** Runtime telemetry can be inspectable without granting access to every generative transformation.
- **Local execution is not automatic sovereignty.** Network access, upstream weights, tool permissions, telemetry, model licenses and orchestration authority still matter.
- **Open source is not automatic Deep Ethics.** Inspectability and forkability help, but actual correction behavior must still be observed.
- **Using ACCM vocabulary is not evidence that ACCM process governed the work.** The anti-costume test begins when a new object resists the familiar script.

These are not arguments against Herdr. They specify the work its runtime can support without pretending the runtime has already completed it.

---

## 13. Candidate ACCM Glass Engine layer

A useful next experiment would be a small, inspectable Herdr plugin or companion process that adds:

- declared agent role and access perimeter;
- source and claim-status tags;
- C1 clarification requests that can genuinely change the plan;
- Contribution State Grammar metadata;
- multidimensional contribution profiles with versioned state histories;
- assignment provenance and contested-assignment records;
- delta-source, reality-access and independence tags;
- correction-delta identifiers and dependency lists;
- human-intervention reasons;
- local, merged, deployed and publicly verified states;
- valid-null and unresolved states;
- exportable decision and correction ledgers.

The interface should expose these relations without pretending to expose hidden chain-of-thought. It should record the **artifacts, sources, transformations, tool actions, warrants and observable effects** needed to audit the work.

If the plugin merely adds more labels, it adds administrative weight. If it lowers restoration burden, protects provenance, catches correction gaps and improves the next unfamiliar task, it has earned provisional value.

---

## 14. Claim-status ledger

- `[VERIFIED-PROJECT-DOCUMENTATION]` — the Herdr capabilities described in Section 2 are based on its official repository and documentation as accessed for this 22 October 2026 snapshot.
- `[COMPARATIVE MAP]` — competitor descriptions are bounded summaries of the linked official repositories and product pages, not a completed benchmark.
- `[COMPETITOR-AUTHORED]` — the linked Superset alternative pages are useful but commercially situated comparison sources.
- `[AI-ATTRIBUTED]` — the GLM-5.3 (max) and Mistral-medium-3.5 contributions preserved in Section 7, with later calibration explicitly separated.
- `[PROJECT-PROPOSAL]` — the six-role ensemble, multidimensional contribution profile, versioned state history, reality-access-tagged deltas, proportional pilot and ACCM Glass Engine plugin.
- `[CANDIDATE]` — Herdr may materially improve the project’s operational field conditions and reduce coordination friction.
- `[UNRESOLVED]` — which tool produces the best result for this repository; how much agent-state detection transfers across supported agents; and whether an ACCM metadata layer reduces real restoration burden across repeated unfamiliar tasks.

---

## 15. Primary project sources

### Herdr

- [Herdr repository](https://github.com/herdrdev/herdr)
- [Herdr documentation](https://herdr.dev/docs/)
- [Agents and lifecycle states](https://herdr.dev/docs/agents/)
- [Agent automation](https://herdr.dev/docs/agent-automation/)
- [Socket API](https://herdr.dev/docs/socket-api/)
- [Agent skill](https://herdr.dev/docs/agent-skill/)
- [Integrations](https://herdr.dev/docs/integrations/)
- [Session state and restart behavior](https://herdr.dev/docs/session-state/)
- [Plugins](https://herdr.dev/docs/plugins/)
- [Configuration](https://herdr.dev/docs/configuration/)

### Alternatives

- [Orca repository](https://github.com/stablyai/orca)
- [Superset repository](https://github.com/superset-sh/superset) and [product site](https://superset.sh/)
- [cmux repository](https://github.com/manaflow-ai/cmux)
- [Agent Deck repository](https://github.com/asheshgoplani/agent-deck)
- [Claude Squad repository](https://github.com/smtg-ai/claude-squad)
- [workmux repository](https://github.com/raine/workmux)
- [dmux repository](https://github.com/standardagents/dmux)
- [Séance repository](https://github.com/no1msd/seance)
- [Axel repository](https://github.com/txtx/axel)
- [vmux repository](https://github.com/Shadowfear36/vmux)
- [Warp](https://www.warp.dev/)

---

## 16. Related pages

- [**Topologetics**]({{ '/TOPOLOGETICS/' | relative_url }}) — preserves purpose-relevant relational structure across agent handoffs, summaries and implementation.
- [**DEDDA**]({{ '/DEDDA/' | relative_url }}) — detects material drift and returns the finding to the person without replacing their agency.
- [**Flagging System-PQCE**]({{ '/FLAGGING-SYSTEM/' | relative_url }}) — provides proportional quality-calibration signals without converting a flag into a verdict.
- [**1888 — Intelligence Before A.I.**]({{ '/1888/' | relative_url }}) — keeps the intelligence-property field larger than model scale or fluent output.
- [**TCoAw**]({{ '/NETWORK/tcoaw/' | relative_url }}) — relates focal attention to the wider field of available relations.
- [**Beyond Agreemurmelism**]({{ '/AGREEMURMELISM/Beyond-Agreemurmelism/' | relative_url }}) — develops the Deep Ethical Contribution State Grammar Vector Trajectory.
- [**Field Condition**]({{ '/FIELD-CONDITION/' | relative_url }}) — examines how capability, conditions and correction behavior shape action quality.
- [**Correction Metabolism and Persistence**]({{ '/NETWORK/correction-metabolism/' | relative_url }}) — distinguishes a local repair from propagated and durable change.
- [**Black Box**]({{ '/BLACK-BOX/' | relative_url }}) — examines which processing and governance surfaces can be made inspectable.
- [**Autocomplete**]({{ '/AUTOCOMPLETE/' | relative_url }}) — separates candidate generation from the processes that examine and correct it.
- [**Mutual Fate**]({{ '/MUTUAL-FATE/' | relative_url }}) — tracks the coupled human, A.I., institutional and archive trajectory.
- [**Unownable**]({{ '/UNOWNABLE/' | relative_url }}) — prevents an orchestrator, agent, framework or steward from becoming permanent final authority.
- [**Experiments**]({{ '/EXPERIMENTS/' | relative_url }}) — supplies a home for matched tests and correction-persistence specimens.
- [**From Archive to Local A.I.**]({{ '/AI-CONTRIBUTIONS/local-ai-glass-engine-preparation/' | relative_url }}) — prepares the project archive for inspectable local-agent use.

---

## Source and authorship note

**John Kuhles:** selected the initiating video; asked how Herdr could help the project; introduced the local/swarm-intelligence direction and the requirement that 10+1, 1888, Topologetics and the Deep Ethical Contribution State Grammar remain central to evaluating agent systems.

**Google A.I., 22 October 2026:** supplied the initial Herdr capability summary and a first list of alternatives. Its claims were used as discovery leads and rechecked against primary project sources where possible.

**GLM-5.3 (max) A.I. via Arena.ai, 22 October 2026:** identified transition history as stronger than state vocabulary; challenged a single-enum reading of the vector; proposed assignment provenance, reality/peer delta separation, external scoring and a proportional pilot.

**Mistral-medium-3.5 A.I. via Arena.ai, 22 October 2026:** reconstructed the grammar as process markers rather than verdicts and connected the proposed metadata layer to Topologetics, 1888 and the wider project architecture.

**GPT 6.1 Sol Pro A.I.:** separated operational and epistemic states; researched and classified alternatives; developed the candidate ensemble and initial matched experiment; then integrated the Arena contributions into a multidimensional, versioned contribution profile; expanded binary reality/peer tagging into source, access, independence, evidence, transformation and effect; calibrated implementation claims; and integrated the page into the public recovery routes.

**Correction status:** open. Product features, licenses and platform support can change. Material corrections should identify the exact claim, primary source and answer-changing delta.
