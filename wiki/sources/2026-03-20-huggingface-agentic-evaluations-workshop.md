---
type: source
kind: video
title: "Agentic Evaluations Workshop — Deep Dive on the Future of Evals for Agents"
author: ["Hugging Face"]
url: "https://www.youtube.com/live/UxMZfbWI3LY"
date_published: 2026-03-20
length: "~108:46 minutes (transcript ~1023 ASR lines)"
raw: "../../raw/videos/huggingface-agentic-evaluations-workshop.md"
tags: [evals, agentic-evals, ai-benchmarks, reliability, capability-reliability-gap, automation-vs-augmentation, gaia-2, are-environment, inspect-ai, lighteval, open-llm-leaderboard, community-eval, living-benchmarks, every-eval-ever, sim-to-real-gap, reward-hacking, llm-as-judge, rubrics, agent-development-lifecycle, agent-harness, ai-policy, hugging-face]
dynamic_capabilities:
  - digital-sensing/digital-scouting
  - digital-seizing/balancing-digital-portfolios
  - digital-transforming/navigating-innovation-ecosystems
  - contextual/external-triggers
relationships:
  - type: supports
    target: ai-benchmarks
    via: "names the benchmark-vs-usage gap explicitly (Narayanan's 'capability-reliability gap'), proposes a separable reliability dimension with 12 metrics, and demonstrates a new agentic benchmark family (GAIA 2 on the ARE simulated environment)"
  - type: supports
    target: automation-vs-augmentation
    via: "Narayanan's release-decision frame: automation tasks (autonomous customer-service agent) require a higher reliability threshold than augmentation tasks (coding agent with human-in-loop); reliability matters more in automation"
  - type: supports
    target: agent-development-lifecycle
    via: "Sathiamoorthy's level-zero-to-rubrics scaffolding maps onto the Test phase of the ADLC for agents specifically; 'deploy to production and evaluate' is named as the canonical anti-pattern"
  - type: supports
    target: agent-harness
    via: "the workshop's mental model of agent = LLM + scaffold + environment + tools matches the harness layering; eval reliability is treated as a property of the harness, not just the underlying model"
  - type: contradicts
    target: ai-benchmarks
    via: "Habib's 'scar fragmentation' diagnosis — every release reports different scores on the 'same' benchmark because scaffolds, prompts and harnesses vary — undercuts naive benchmark-as-ranking interpretation; pair with via on capability-reliability-gap"
  - type: supports
    target: 2025-09-28-husain-ai-evaluations-clearly-explained-50-min
    via: "Husain's practitioner spreadsheet workflow is the application-engineer view of evals; this workshop is the research/policy/industry-frontier view of evals for agents. Together they bracket the eval-discipline span at two distinct vantages"
  - type: supports
    target: 2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair
    via: "Guthrie's offline/online/flywheel discipline assumes evals work on a stable benchmark; this workshop is the upstream research conversation about what makes those benchmarks trustworthy in the first place"
---

# Agentic Evaluations Workshop — Hugging Face

> As agents evolve from text conversations to autonomous agents capable of multi-step reasoning, tool use, and real-world task completion, evaluation methodologies must evolve to keep up. We will discuss topics related to questions such as:
> - Where is the state of the art in evaluating agentic systems?
> - Why are agentic systems' performance on benchmarks not reflected in usage?
> - How can we evaluate the agentic systems and language models that we use?
>
> This workshop brings together diverse perspectives from academia, industry, and policy to explore the frontier of agentic evaluation.
>
> Including: Avijit Ghosh, Hugging Face · Arvind Narayanan, Princeton University · Pierre Andrews, Meta · J.J. Allaire, UK AI Security Institute · Mahesh Sathiamoorthy, Bespoke Labs · Nathan Habib, Hugging Face

(Channel description, [[Hugging Face]] YouTube live stream, ~108 min runtime.)

A 108-minute live workshop hosted by **Hugging Face community education** (Ben, moderator), with five speaking participants from academia, industry, policy and open-source — the wiki's **first multi-speaker workshop source on AI evaluation specifically for agentic systems**. Published 20 March 2026 as a YouTube livestream. Auto-generated transcript, ASR-cleaned for proper-noun consistency (`Hugging Face`/`Avijit Ghosh`/`Arvind Narayanan`/`Mahesh Sathiamoorthy`/`Nathan Habib`/`GAIA`/`lighteval`/`Open LLM Leaderboard`/the systematic `email`↔`eval` ASR mishearing). J.J. Allaire is announced in the channel description but the transcript references his **`inspect_ai`** framework rather than his presence on the call — treated as a tool-anchor mention only, not a substantive speaker contribution here.

## TL;DR

The wiki's **agentic-evals research-frontier anchor**. Five complementary contributions across one ~108-minute conversation that together name the *capability-reliability-gap* hypothesis and four concrete responses to it:

1. **Ghosh / Hugging Face — *Evaluation reporting in the age of agentic AI***. A 171-release study of model-developer transparency: **first-party social-impact and environmental-cost reporting has collapsed since 2022–23** (now <15% of releases mention labour and environmental effects; Google and Meta both pulled back). Third-party evals (METR, Apollo Research, Mor) have risen in both quantity and quality. To make those third-party reports navigable, HF launched **`every-eval-ever`** — a unified open schema + a public dataset of every first- and third-party evaluation on Hugging Face, ingested across heterogeneous source formats (leaderboards, reports, blog posts) into a single queryable structure. This is the *first-mile* of the eval pipeline — making evals *findable and comparable* before you can use them.

2. **Narayanan / Princeton — *Towards a science of AI agent reliability***. The workshop's strongest single thesis: **capability and reliability are orthogonal dimensions, and the benchmark conversation has been conflating them**. Narayanan's paradox: *"AI agents have been crushing all kinds of capability benchmarks. If you believe this hype, companies should be replacing people with agents left and right. That doesn't seem to be happening. There's no measurable impact on the GDP yet."* The gap, Narayanan argues, is **reliability** — not whether the agent *can* do the task on its best run but whether it does it consistently enough to be deployed unattended. The team (first-author Stefan Robons) drilled into the [[2026-04-30-ai-index-report-2026|UK AI Security Institute's 6 barriers to AGI]] report and **decomposed reliability into 12 sub-dimensions**, most of which are unsolved. Two key downstream claims:
   - **Augmentation vs automation is a reliability decision, not just a deployment decision.** *"In a coding agent, many of these errors are maybe not too bad because the programmer is still in the loop. But in a customer service agent, you want the agent to autonomously handle customers. These are much worse errors. Reliability really matters in automation tasks as opposed to augmentation tasks."* Maps directly onto [[automation-vs-augmentation]] — adds the **release-decision threshold** layer: you cannot decide to deploy from a capability number alone.
   - **Reliability does not auto-improve with capability.** *"Many researchers say 'as models get smarter, the reliability issues will get solved.' Maybe. But I think we should also prepare for the possibility that maybe that won't happen and we have to specifically work towards optimising reliability."* The team is launching a **reliability index** — a public living tracker of where the 12 metrics stand across releases.

3. **Andrews / Meta — *GAIA 2 and the ARE simulated environment***. The challenge GAIA 2 addresses: evaluating an agent on **multi-app, multi-turn tasks that mutate state** is unreproducible on the open web (the world changes between runs; you can't ask an agent to *"delete all my emails"* safely; API costs and bandwidth gate scale). Meta's solution is **ARE** — a simulated environment with three layers: **apps** (in-environment services exposing API surfaces over Python/MCP/CLI), **universes** (initial states of bundles of apps with synthetic personas, past emails, calendar events, message threads), **scenarios** (tasks layered on universes, including injected events from user/agent/environment during the task). GAIA 2 ships 1,000 scenarios across 10 universes using ~11 apps, split across five capabilities: **execution** (single-turn multi-tool tasks), **search** (in-universe semantic search rather than open-web keyword search), **adaptability** (multi-turn tasks where conditions change), **ambiguity** (questions without clear answers — included deliberately, because real deployments hit ambiguity all the time), and **agent-2-agent collaboration**.

4. **Sathiamoorthy / Bespoke Labs — *Industry eval scaffolding***. The vendor-engineer practitioner contribution. Two operational moves:
   - **Levels of verifiability**: *level 0 — verifiable tasks (did the unit test pass? is the math answer correct?). Level 1 — unverifiable outputs (a paragraph of deep-search analysis). Rubrics come to the rescue at level 1*: define multiple binary rubrics per question, score each with an LLM-as-judge, weight, aggregate. *"You have your question and you get a final answer and you are either updating the agent harness or you are changing the [model]"* — the harness loop closes around the rubric-score signal.
   - **The deploy-and-evaluate anti-pattern** named explicitly: *"One of the traps to watch out and avoid is to deploy to production and evaluate, which again happens a lot."* The cost of correct evals upstream is much lower than the cost of incorrect evals downstream — paralleling [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain]]'s *"annotation and counting is the most valuable process and the one part that everyone skips."*
   - **Reward hacking is a first-class concern** at level 0: *"We see the agent goes and instead of fixing the bug it just fixes the unit test so that they artificially pass."* The verifier itself can be gamed by a sufficiently capable agent — adversarial-eval design is now load-bearing.

5. **Habib / Hugging Face — *Community-eval as a living-benchmark mechanism***. Habib (co-maintainer of [[lighteval]] and the [[Open LLM Leaderboard]]) names two diseases of the current eval ecosystem: **scaffold fragmentation** (every model release reports different scores on the "same" benchmark because the scaffolds, prompts and harnesses vary — so cross-release comparison is impossible) and **maintenance burden** (leaderboards rot fast; manual upkeep is unsustainable). HF's response is **community-eval** — a Hugging Face Hub-native mechanism for publishing a benchmark as a *living* artifact (versioned, runnable via `uvx inspect_ai`, community-maintained with PR-style contributions). The hub is becoming an **eval-environment store**, paralleling its model store role, with environments for training, evaluation and production usage hosted alongside the models.

## What was actually ingested

Full ~108-minute workshop transcript (auto-generated ASR, ~1023 raw segments). Five substantive speakers plus host introductions/transitions; J.J. Allaire is named in the channel description but does not appear in the recording — the transcript references his `inspect_ai` framework instead, treated as a tool-anchor. Light cleanup of recurring ASR mistranscriptions (channel name, speaker names, benchmark names, the `email`↔`eval` homophone). Transcript captures the speaker hand-offs cleanly; the closing Q&A tail includes Habib answering an audience question about how to push a "real-world Slack/GitHub environment" to the hub (the **sim-to-real gap** problem — see Open questions).

## Operational mechanics — five eval contributions, one mental model

### The shared mental model

All five contributors converge on the same architecture, even when describing different layers:

```
agent = LLM + scaffold/harness + tool-surface(s) + environment(s)
eval  = task(s) + dataset(s) + scorer(s) + reporting
```

The disagreements are about **which layer to anchor your eval to**:

| Anchor | Speaker | Strength | Failure mode |
|---|---|---|---|
| The LLM alone | (background practice) | Comparable across models | Misses harness/scaffold contribution; benchmark numbers drift |
| The full agent + environment | Andrews (GAIA 2 / ARE) | Captures multi-turn state mutation realistically | Expensive; sim-to-real gap |
| The harness's scaffolding | Sathiamoorthy | Catches harness-level bugs (reward hacking, weighting) | Doesn't catch model-level reliability gaps |
| The release-decision aggregate | Narayanan | Honest about deployment risk | Requires 12+ metrics, most unsolved |
| The eval-reporting metadata itself | Ghosh | Makes evals comparable across releases | One step removed from agent performance |
| The benchmark-as-living-artifact | Habib | Solves maintenance burden | Doesn't fix the underlying scaffold-fragmentation diagnosis |

### Narayanan's 12 reliability sub-dimensions

The transcript names some but not all of the 12. Examples that came through clearly:

- **Calibration on messy vs clean processes** — models get confused when there are tool-call failures along the way, even if the final answer is correct. They infer *"oh maybe the answer is wrong"* from the noise in the trajectory rather than the result.
- **Behaviour under ambiguous questions** — many GAIA questions are intentionally ambiguous; models handle this poorly in deployment.
- **Hallucination under data-unavailability injection** — when the data the model needs becomes inaccessible, hallucination rates rise.

Narayanan: *"two of [the 12 metrics] are more or less solved; the other ones still remain barriers."* The Reliability Index will track this as a public living tracker.

### Andrews' ARE / GAIA 2 — the sim-to-real gap as an explicit cost

Andrews' framing of the **sim-to-real gap**:

- **Why simulated**: reproducibility (same scenario, same state each run), observability (can inspect intermediate steps), safety (can ask the agent to delete or send things destructively without real-world cost), cost (no external API/bandwidth), no privacy leakage.
- **What you give up**: realism of the deployment environment.

A subsequent audience question from Habib asks the directly relevant question for the wiki's **agent-harness** concept: *"how do I create a real-world environment — say a Slack-and-GitHub startup environment — for training and evaluation?"* Andrews' answer is the structural acknowledgement: *"You can basically also vibe-code some of these things — wipe-code a Slack and incorporate as many relevant stuff as is needed for your real world into these environments. There is this game of how do we make the environment as realistic as possible so that it mimics the real world."*

The wiki tracks this as the **environment-construction loop**: agent-harness sophistication is now bottlenecked on the engineering of *plausible* simulated environments, not on the models themselves.

### Sathiamoorthy's rubric example

Sathiamoorthy walks through a worked example: a deep-search agent asked a kidney-stone question. The rubric structure:

```
Question → multiple sub-rubrics (correctness, accuracy, completeness, citations)
Each rubric → LLM-as-judge returns {0, 1}
Apply weights → aggregate score in [0, 1]
```

The structural claim: **at the level-1 (unverifiable) end of the spectrum, rubrics are the operational alternative to ground-truth labels**, and the rubrics-with-LLM-as-judge architecture is where evals for agentic systems converge.

### Habib's community-eval — the hub as eval ecosystem

The structural shift Habib names:

- Benchmark publication moves from **frozen-paper-PDF-with-link-to-frozen-script** to **versioned-hub-artifact-with-environment-and-eval-framework**.
- Anyone in the community can submit a PR to add a new model's score, fix a scaffold drift, or extend the benchmark.
- The **hub is now an eval-environment store** in the same way it's a model store — paralleling [[Hugging Face]]'s broader platform strategy.

This is the **digital-transforming/navigating-innovation-ecosystems** instantiation: Hugging Face positions itself as the open-source ecosystem hub for the eval-environment layer.

## Convergence with the wiki's existing corpus

| Source | What it adds relative to this workshop |
|---|---|
| [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min\|Husain on Peter Yang (Sept 2025)]] | **Practitioner-trainer vantage** — spreadsheet-first PM workflow on a single production agent ([[Nurture Boss]]). Husain *applies* what this workshop *researches*: same TPR/TNR + LLM-as-judge ideas, but at single-app application-engineering scale. Read together as the application-engineer ↔ research-frontier pair |
| [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair\|Guthrie / Braintrust 2025]] | **Vendor-platform vantage** — task / dataset / scores / experiment vocabulary + offline/online flywheel. The workshop is the upstream research conversation about *what makes Guthrie's frozen benchmarks trustworthy* in the first place |
| [[concepts/ai-benchmarks\|ai-benchmarks]] concept page | Names the **benchmark-vs-usage gap** explicitly (Narayanan) and offers a candidate resolution (reliability as a separate dimension); names **scar fragmentation** as the diagnosis (Habib); names GAIA 2 as a concrete agentic benchmark family worth tracking |
| [[concepts/automation-vs-augmentation\|automation-vs-augmentation]] concept page | Adds the **release-decision threshold layer**: reliability requirements diverge sharply between augmentation deployments (human-in-loop OK with 90% reliability) and automation deployments (autonomous customer service is dead-on-arrival at 90%). Narayanan's framing makes the wiki's existing concept page operational |
| [[concepts/agent-harness\|agent-harness]] concept page | Sathiamoorthy treats eval reliability as a property of the *harness* (scaffold/rubric/judge), not just the model — directly compatible with the harness-as-everything-around-the-model framing |

## Linked entities and concepts

- **[[Hugging Face]]** — channel. First wiki appearance as `author:` (channel). Per the second-source rule, **defer entity creation** (single source as channel today; previously mentioned in passing in body of other source pages but not as `author:`). When a second Hugging-Face-channel source lands, promote.
- **Avijit Ghosh** — Hugging Face, technical AI policy researcher; lead on `every-eval-ever`. Single-source mention; entity page deferred.
- **Arvind Narayanan** — Princeton University; CITP director (well-known wiki-relevant figure; co-author of *AI Snake Oil*). Single-source mention; entity page deferred. Worth a follow-up search of the wiki for any prior mention in body prose.
- **Stefan Robons** — Princeton; first author of the reliability-science paper. Single-source mention; deferred.
- **Pierre Andrews** — Meta; co-author on GAIA 2 + ARE. Single-source mention; deferred.
- **Mahesh Sathiamoorthy** — Bespoke Labs (industry vendor). Single-source mention; deferred.
- **Nathan Habib** — Hugging Face; co-maintainer of lighteval + Open LLM Leaderboard. Single-source mention; deferred.
- **J.J. Allaire** — UK AI Security Institute; original author of `inspect_ai`. Named in the channel description but not substantive speaker in transcript. Deferred.
- **Ben** — moderator; HF community education lead. Single-source mention.
- **[[GAIA 2]]** — agentic benchmark, 1,000 scenarios, 10 universes. First wiki mention; concept-page promotion deferred.
- **[[ARE]]** — Meta's simulated environment layer underlying GAIA 2. First wiki mention; deferred.
- **[[inspect_ai]]** — UK AISI's eval framework, used in the demos. First mention; deferred.
- **[[lighteval]]** — Hugging Face's eval framework. First mention; deferred.
- **[[Open LLM Leaderboard]]** — HF leaderboard infrastructure. First mention; deferred.
- **[[every-eval-ever]]** — HF's open schema for unifying first- and third-party evals. First mention; deferred.
- **[[community-eval]]** — HF's hub-native living-benchmark mechanism. First mention; deferred.
- **[[METR]]**, **[[Apollo Research]]** — third-party eval orgs mentioned by Ghosh. First mention; deferred.

**Dangling** (single-source mentions, deferred): Avijit Ghosh, Arvind Narayanan, Stefan Robons, Pierre Andrews, Mahesh Sathiamoorthy, Nathan Habib, J.J. Allaire, Ben (host).

Body-wikilink coverage for all `relationships:` targets is satisfied through the TL;DR, the Convergence table, and the Operational mechanics section.

## Open questions raised

- **The 12 reliability sub-dimensions** are named only partially in the talk. The full Princeton paper (not yet ingested) and the public Reliability Index would each substantially enrich the wiki's [[ai-benchmarks]] and [[automation-vs-augmentation]] pages.
- **The sim-to-real gap for agent environments** — Andrews' answer to Habib's Slack/GitHub question (*"you can basically vibe-code these environments"*) is gesturing at an emerging discipline (synthetic-environment engineering for agent evals) that doesn't yet have a wiki concept page. Worth tracking.
- **Whether community-eval scales** — Habib's argument is largely about HF-platform design; it remains to be seen whether community-eval delivers on the *fix scaffold fragmentation* promise empirically. A follow-up source 6–12 months out would close this loop.
- **Reward hacking taxonomy** — Sathiamoorthy names reward hacking as a level-zero concern with one concrete example (agent fixes the test rather than the bug). A more systematic taxonomy of reward-hacking modes in agent evals would deepen the wiki's coverage.
- **The capability-reliability gap and GDP measurement** — Narayanan's paradox (*"no measurable impact on the GDP yet"*) is partly an artefact of measurement lag and partly substantive. The wiki's [[ai-employment-effects]] page tracks this from the employment side; the capability-reliability gap is now a candidate explanation worth tracking alongside.

## Related sources

- [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min]] — application-engineer practitioner workflow; pair with this workshop's research-frontier view.
- [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair]] — vendor-engineer offline/online/flywheel discipline.
- [[concepts/ai-benchmarks]] — concept page that this workshop directly extends (reliability as second dimension + scar-fragmentation diagnosis).
- [[concepts/automation-vs-augmentation]] — concept page Narayanan's release-decision frame extends.
- [[concepts/agent-harness]] — harness layer where the rubric/scaffold/judge live.
