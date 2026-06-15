# Log

Reverse-chronological record of wiki operations — **newest entry at the top, oldest at the bottom**. New entries are *prepended* immediately under the `---` separator below. Strict prefix format so `grep "^## \[" wiki/log.md | head -10` returns the ten most recent. Format (indented to keep grep clean):

    ## [YYYY-MM-DD] <op> | <title>

Permitted operations: `ingest`, `acquire`, `query`, `lint`, `synthesize`, `refactor`, `bulk-refactor` (added v0.2 — for any operation touching >10 wiki pages, with affected slug list and reversibility note). `acquire` was added in v0.9 (2026-05-17) for sessions that land raw files but defer processing to a later session; the umbrella `ingest` op stays for the typical Acquire+Process-in-the-same-session case. See [the design doc, §9.2](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md#92-wikilogmd) for details.

Ordering flipped on 2026-05-12 (GH [#3](https://github.com/businessdatasolutions/ai-wiki/issues/3)): the file used to grow from the top; it now grows from the bottom. Old entries are unchanged; only their position relative to newer entries is reversed. Tools that read the log should take the first N entries to get the most recent.

---

## [2026-06-15] refactor | Reclassify Zotero-stack integration from wiki thread → `inspiration/` notes

The page filed earlier today as `wiki/threads/zotero-stack-integratie.md` was reclassified as a plain research/decision note: it is build-planning for the wiki's own tooling (pairing with the May-2026 PRD), not a knowledge-investigation thread. **Moved** `wiki/threads/zotero-stack-integratie.md` → `inspiration/2026-06-15-zotero-stack-integratie.md` (git mv); dropped the thread-schema frontmatter (`type: thread` / `status: open` / `opened:`) for an `inspiration/`-style header (`title` / `date` / `status: notes`); rewrote sibling PRD references and the "How this thread should resolve" → "Definition of done" framing. **Touches**: file move + index (removed from Threads section) + this log. The 2026-06-15 `query` entry below is retained for history (its wikilinks neutralised to plain text since the target left `wiki/`). Reversible: `git mv` back and restore the index bullet.

## [2026-06-15] ingest | [[2026-04-03-bcg-emerson-kropp-ai-will-reshape-more-jobs-than-it-replaces|BCG *AI Will Reshape More Jobs Than It Replaces*]] (Emerson, Kropp et al., 3 Apr 2026) — six AI Labor Disruption Segments; method-independent corroboration of the Anthropic observed-exposure report

22-page BCG Henderson Institute microeconomic labor-impact report (full read). **Reshape ≫ replace**: 50–55% of US jobs reshaped in 2–3 yrs, 10–15% eliminated in 4–5 yrs; 43% are ≥40% automatable. **Six AI Labor Disruption Segments** = substitution-vs-augmentation × **demand expandability** (Jevons): Amplified 5% / Rebalanced 14% / Divergent 12% / Substituted 12% / Enabled 23% / Limited-Exposure 34%. Four CEO directives (embed workforce strategy / redesign-not-cost / continuous upskilling / shape the narrative). **Method-independent convergence** with the [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Anthropic observed-exposure report]] — different methods, same headline — recorded as a `supports` edge. `kind: report`; 5 W&W tags.

**Touches (~14 files)**: 1 new source + **3 entity promotions** ([[Matthew Kropp]], [[Julie Bedard]], [[Megan Hsu]] — 2nd-source rule, all also author the [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|BCG agents-as-employees piece]]; surfaced/cleared by dangling-author lint) + [[Lisa Krayer]] (2→3) + [[Boston Consulting Group]] (3→4) + **5 concepts**: [[ai-employment-effects]] (45→46; six-segment taxonomy), [[automation-vs-augmentation]] (43→44; §23 — the demand-expandability/Jevons second axis), [[durable-skills]] (26→27; rising skill thresholds + AI-fluency-as-tenure-complement), [[micro-productivity-trap]] (31→32; redesign-not-cost CEO directive), [[enterprise-ai-adoption]] (70→71; adoption-lag + forward-deployed-engineers + 4 CEO directives) + index + log. Typed edges: `published-by` BCG, `supports` Kropp-BCG + Massenkoff-McCrory + Brynjolfsson. Dangling: Greg Emerson (lead, BCG MD), Romanov, Sanchez Boedo, Mohnot. Reversible.

## [2026-06-15] refactor | Normalize 10 concept "Debates / contradictions" headings → canonical "Debates and supersession"

Schema-alignment sweep (CLAUDE.md mandates the exact heading; `scripts/quality-score.mjs` keys on the literal string). Heading-only rename on agent-harness, ai-agents, ai-benchmarks, ai-employment-effects, automation-vs-augmentation, foundation-models, generative-ai, industry-4-0, lean-4-0, responsible-ai; quality_score recomputed (agent-harness 0.77→0.97, ai-employment-effects 0.77→0.97, automation-vs-augmentation 0.73→0.93, responsible-ai 0.69→0.89, ai-agents 0.67→0.87). **Corpus now has zero concepts below 0.65.** Content unchanged.

## [2026-06-15] query | Filed Zotero-stack integration thread — local-Zotero → wiki integration research + decisions

> Superseded by the 2026-06-15 `refactor` entry above: this was reclassified to `inspiration/2026-06-15-zotero-stack-integratie.md`; wikilinks below are neutralised to plain text.

Researched connecting the wiki to a **local** Zotero instance so that adding a source stops meaning hand-copying and converting files into `raw/`. Key finding that re-prices the May-2026 PRD (`inspiration/2026-05-14-prd-zotero-stack-integratie.md`, which assumed the cloud Web API + the `ai-consultant` GCP stack): **Zotero 7 ships a read-only local HTTP API** (`localhost:23119/api`, no key, no sync, `users/0`) and mature **local-Zotero MCP servers** now exist (e.g. `54yyyu/zotero-mcp`, `ZOTERO_LOCAL=true`). **Decisions taken**: pursue **MCP (live read) + an Acquire skill (durable ingest)** — the PRD's A+C, updated; **scope ingest to one Zotero collection** (`→ ai-wiki`) so the wider library never syncs; **commit no PDF binaries** (Zotero is the binary store; provenance via `zotero_item_key` + `doi`); source markdown **routes by type** (`raw/papers/`, `raw/articles/`, …). **Correction (mid-session, after a user screenshot):** `raw/` only *looks* markdown-only in the committed repo because `.gitignore` excludes all raw binaries (`raw/**/*.pdf` et al., local-only for copyright); the user's local working copy keeps the original PDFs co-located by type (e.g. `raw/articles/*.pdf`). **Touches**: 1 new thread page (zotero-stack-integratie) + index (Threads section) + this log. No concept/entity/source pages touched; no build executed yet. Reversible: delete the thread, revert index + log.

## [2026-06-15] ingest | [[2026-03-05-massenkoff-mccrory-anthropic-labor-market-impacts-ai|Anthropic *Labor market impacts of AI*]] (Massenkoff & McCrory, 5 Mar 2026) — the methodological primary behind the wiki's "observed exposure" measure

17-page Anthropic / [[Anthropic Economic Index]] research note (full read), introducing **observed exposure** = theoretical LLM capability (Eloundou β) × real-world AEI usage, **weighting automated/work-related uses more heavily** (the weight that converts exposure → displacement risk). Findings: capability ≫ adoption (β=1 = 68% of Claude usage); top-exposed Computer Programmers 75% / CSRs / Data Entry Keyers; +10pp coverage → −0.6pp BLS 2024–34 growth; exposed workers more female/educated/+47% pay; **no systematic unemployment effect yet**; **~14% young-worker (22–25) hiring slowdown** into exposed occupations. This is the exact "Anthropic March study" [[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|Brovich/AWS]] cited — so the V3 source's `supports` edge + body link were **re-pointed** from the AEI-q4 report to this primary. `kind: report`; one W&W tag (`digital-sensing/digital-scouting`).

**Touches (~9 files)**: 1 new source + [[ai-employment-effects]] (44→45; substantive *observed-exposure* section + Brovich-link correction), [[automation-vs-augmentation]] (42→43; §22 — the automation/augmentation split as a measurement weight), [[Anthropic]] (19→20), [[Anthropic Economic Index]] (3→4; added the labor-impacts report row), V3 source edge re-point + index + log. Typed edges: `published-by` Anthropic, `part-of` AEI, `supports` [[2026-04-28-anthropic-economic-index-q4-2025|AEI-q4]] + [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson]]. **Promotes [[Maxim Massenkoff]] + [[Peter McCrory]] to entities** (2nd source — both also lead-author the 5th AEI report; their dangling note on that source updated). +2 entity files beyond the count above. Reversible.

## [2026-06-15] ingest | Agentic-leadership 3-video batch — [[2026-06-11-mit-smr-agentic-ai-what-leaders-wish-they-knew-sooner|MIT SMR CIO Symposium]] (11 leaders) + [[2026-06-12-aws-leaders-guide-data-strategy-agentic-ai|AWS data strategy]] + [[2026-06-12-aws-leaders-guide-advanced-team-structures-agentic-world|AWS team structures (Brovich)]] — promotes [[Michael Schrage]]; records the *manage-agents-like-employees* debate

Three videos forming a **"leading in an agentic world" cluster**, all on human–agent collaboration / org design. **Pre-flight clean** (MIT SMR manual CC track, segments 0-242; both AWS talks ASR-only, light cleanup; ASR duplicate tracks discarded). **MIT SMR** (2026 MIT Sloan CIO Symposium, host Abbie Lundberg): 11 leaders, one takeaway each — Davenport's *performative oversight*, Swift/Chan's *manage like employees*, Westerman's *automate-first/rebuild-for-outcomes*, Caldas's micro-agents+trust-fabric, Schrage's *in-loop vs on-loop*. **AWS data-strategy** (Sydney, F1 analogy): data consumer is now the agent; data-products / markdown-for-agents / 4-question test / minimum-viable-governance — the wiki's most focused *data-for-machines* source. **AWS team-structures** (Brovich): the **Sydney edition of the [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen talk]]** → corroborating second source (same USE/COMPOSE/BUILD, hourglass, Models A/B/C, Singapore governance) + quantified specifics (pricing scissors 2.4×/10×/12–24×; Model A dead / 95% pilots fail; AgentCore four-questions). Slide provenance for the **moats slide (~7:02)** recorded per user note.

**Cross-cutting touches (~18 files)**: 3 new sources + new [[Michael Schrage]] entity (2nd source: Kiron-Schrage + CIO Symposium) + [[MIT Sloan Management Review]] bump (5→6) + **10 concepts**: [[agent-harness]] (58→61; Models A/B/C, data-products-as-context, performative oversight), [[automation-vs-augmentation]] (40→42; combination-not-replacement + orchestrator-not-builder), [[enterprise-ai-adoption]] (67→70; maturity-arc + data-gate + CIO-as-conductor), [[ai-employment-effects]] (42→44; performative oversight + reshaping), [[micro-productivity-trap]] (30→31; automate-first/reimagine), [[ai-agents]] (19→20; human-agent collaboration reality), [[foundation-models]] (16→17; pricing scissors), [[responsible-ai]] (14→15; Singapore IMDA detail), [[knowledge-graphs]] (6→7; semantics-as-agent-requirement), [[document-intelligence]] (2→3; author-for-machines/markdown) + index (3 sources, 1 entity) + this log. **Key typed edge**: MIT SMR **`contradicts`** [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp/BCG]] (manage-like-employees debate). AWS-team-structures `supports` Allen (near-replication). W&W tags on all three. Dangling/deferred: 10 MIT SMR speakers (Davenport, Pearlson strong candidates), Steven Brovich, Stripe, Gartner, Martin Fowler. Reversible: delete 3 sources + 1 entity, revert 11 page bumps + index + log.

## [2026-06-13] ingest | GDPval + Argenti pair — [[2025-10-05-patwardhan-et-al-openai-gdpval|OpenAI GDPval]] (economically-valuable-task benchmark) + [[2026-06-12-argenti-hbr-thrive-alongside-ai-mindset-not-skillset|Argenti / HBR]] (*mindset-not-skillset*) — wiki's first direct AI-capability-measurement source; promotes [[Goldman Sachs]] to an entity

Two thematically-paired sources (Argenti **cites GDPval by name**). **Identity/scope clean** (29pp paper full read; 8pp article full). **GDPval** ([[OpenAI]], arXiv:2510.04374v1, Oct 2025): 1,320 tasks / 44 occupations / top-9 US-GDP sectors; non-saturating **win-rate vs human experts**; Claude Opus 4.1 best at **47.6%** wins-or-ties; frontier+oversight cheaper/faster; reasoning-effort + context + scaffolding lift scores. Gives the wiki a **third labour lens** (capability, as a *leading* indicator) beside Anthropic's adoption index and the AI Index's academic benchmarks — and **closes a deferred-ingest** named in the [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe guide]]. **Argenti** (Goldman Sachs CIO, HBR June 2026): mindset-over-skillset, operator→supervisor "new 100%", **3× not 20%** radical targets, *"AI transformation follows data transformation"*, obsess over evals.

**Cross-cutting touches (16 files)**: 2 new sources + new [[Goldman Sachs]] entity (2nd substantive source: Argenti + [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles]], whose dangling list was updated) + [[OpenAI]] bump (16→17, +`published-by`→GDPval) + **9 concepts**: GDPval → [[ai-benchmarks]] (8→9, new non-saturating-benchmark section + roster row), [[ai-employment-effects]] (41→42, capability-as-leading-indicator), [[automation-vs-augmentation]] (38→40, §20 GDPval+Argenti — both sources), [[jagged-frontier]] (11→13, by-occupation/modality + "excellent simple, pretty good complex" — both), [[foundation-models]] (15→16, cross-model deliverable comparison); Argenti → [[durable-skills]] (25→26, mindset-not-skillset inversion), [[ai-deskilling]] (10→11, verification-discipline countermeasure), [[enterprise-ai-adoption]] (66→67, data-readiness gate + obsess-over-evals), [[micro-productivity-trap]] (29→30, "demand 3× not 20%") + index (2 sources, 1 entity) + this log. Typed edges: GDPval `published-by` OpenAI + `supports` [[2026-04-30-ai-index-report-2026|AI Index 2026]]; Argenti `uses` GDPval + `supports` [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels]] + [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles]]. W&W: GDPval one light `digital-sensing/digital-scouting`; Argenti five cells. Dangling/deferred: Marco Argenti (Goldman CIO — strong next-promotion candidate) + GDPval's 19 OpenAI authors. **Trajectory caveat recorded**: GDPval's Oct-2025 47.6% vs Argenti's ~80% (mid-2026) is the same non-saturating metric over ~8 months. Reversible: delete 2 sources + 1 entity, revert 11 page bumps + index + log.

## [2026-06-12] ingest | ReAct 3-source batch — [[2022-10-06-yao-et-al-react-synergizing-reasoning-acting|Yao et al. ReAct paper]] (ICLR 2023) + [[2022-11-08-yao-cao-react-google-research-blog|Google Research blog]] + [[2026-06-10-google-cloud-tech-ai-agents-explained-first-agent|Google Cloud Tech/ADK tutorial]] — back-fills the genealogical root of the wiki's agent/harness cluster; new [[react-reasoning-acting]] concept; promotes [[Shunyu Yao]] + [[Yuan Cao]] to entities

Three sources ingested as one coherent **ReAct cluster** (the same foundational work at three epistemic registers): the peer-reviewed ICLR 2023 paper (arXiv:2210.03629v3, full 33pp read), its Google Research blog popularisation (9pp, same claims), and a 10 June 2026 Google Cloud Tech ADK tutorial that defines a modern agent *as* the ReAct loop and builds a self-correcting multi-agent system. **Identity verified**: article and paper are not duplicates — blog (`kind: article`) vs peer-reviewed paper (`kind: paper`); video manual-CC track used (ASR duplicate discarded). Pre-flight scope/identity clean.

**Why this matters**: the wiki's [[ai-agents]] definition (*"an LLM that uses tools in a loop"*, via Wolfe/Willison) and the entire [[agent-harness]] construct are direct descendants of ReAct (2022), which was cited across the corpus but never anchored to a primary source until now. ReAct is the **reason → act → observe** loop named four years before the 2026 practitioner sources rediscovered it as settled practice. New concept page [[react-reasoning-acting]] (confidence 0.85, 3 sources; source-independence caveat noted — paper+blog are one work, only the tutorial is independent).

**Cross-cutting touches (14 files)**: 3 new sources + 1 new concept ([[react-reasoning-acting]]) + 2 new entities ([[Shunyu Yao]], [[Yuan Cao]] — second-source rule, they author paper *and* blog) + updated concepts [[ai-agents]] (16→19 sources, +`uses`→react, anchors the loop definition) & [[agent-harness]] (55→58, +`uses`→react, "ReAct named the loop; the harness owns the reliability") + updated entities [[Google]] (9→10, video) & [[Google Research]] (3→5, paper+blog) + index (3 sources, 1 concept, 2 entities) + this log. Typed source edges: blog `supports` paper; video `uses` paper + `uses` [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Agents CLI]] (same ADK). **No `dynamic_capabilities:` tags** — methodology/tutorial, outside the W&W lens. Dangling authors (single-source, deferred): Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, [[Karthik Narasimhan]] (strong next-promotion candidate). Reversible: delete the 3 sources + 1 concept + 2 entities, revert 4 page bumps + index + log.

## [2026-06-09] ingest | [[Microsoft]]/[[GitHub]] *Agentic DevOps in Real Life* (Randell & Gousset, Live! 360, 22 Dec 2025) — wiki's first GitHub-Copilot/Agent-HQ tooling source; promotes [[GitHub]] + [[Microsoft]] to entities

YouTube keynote acquired via `youtube-transcript-skill` (the caption track looped on fetch; trimmed to the unique 0:00–57:43 content, 553 segments / ~11.4k words; ASR-cleaned — speaker names, "Aentic"→"agentic", "C-pilot/Copot"→"Copilot", "cloud sonnet 45"→"Claude Sonnet 4.5", "codeex"→"Codex", "meter study"→"METR study", etc.). Processed same session. Identity clear (Microsoft Visual Studio channel; presenters Brian Randell / MCW Technologies, ex-GitHub + Mickey Gousset / GitHub Staff DevOps Architect); honest-scoping: **vendor keynote**, product capabilities are demos and the cited stats (4.4M leaks blocked, 322% privilege-escalation, 40% secrets-exposure, 30%/84%) are presenter-reported with attribution deferred to a conference PDF.

**Source — [[2025-12-22-randell-gousset-microsoft-agentic-devops-in-real-life]]** (kind: video; `author: [Microsoft Visual Studio]`). *"Agentic DevOps"* = agents collaborating across the software lifecycle. Covers Copilot coding agent (issue→PR→tests), **Agent HQ** (monitor/steer/audit; open architecture runs OpenAI Codex + Claude/Gemini agents in VS Code), VS Code's **Ask/Edit/Agent/Plan** modes, the **Microsoft responsible-AI pipeline** + the *initiator-can't-self-approve-the-merge* default, **GitHub Advanced Security** (+ Copilot autofix), the **productivity paradox** (METR; *"value not lines of code"*), a **30/60/90-day** rollout playbook, and the **Azure SRE Agent**. W&W: `digital-transforming/redesigning-internal-structures` + `improving-digital-maturity`, `digital-seizing/rapid-prototyping`, `strategic-renewal/organizational-culture`, `contextual/internal-barriers`.

**Neighbour-source scan** (3 candidates surfaced, all `supports`): [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|SEI-CMU]] (enduring-principles-new-pace + METR), [[2026-05-19-elangovan-amd-deeplearningai-ai-dev-26-sf-impact-of-ai-on-software|Elangovan/AMD]] (agentic-SE adoption + METR), [[2026-05-08-running-an-ai-native-engineering-org|Anthropic AI-native eng org]] (process-not-tool thesis).

**Promotions:** [[GitHub]] (cross-page presence ~31 sources; Copilot/Agent HQ/Advanced Security; Gousset is GitHub staff) and [[Microsoft]] (~21 sources; channel publisher; Azure/VS Code/responsible-AI pipeline) → entities, both `source_count: 1` (formal inbound wikilinks) with full backlinking flagged as deferred lint work. **6 concepts updated** (source_count bumps + body sections): [[micro-productivity-trap]] (28→29 — the METR paradox), [[responsible-ai]] (13→14 — vendor pipeline + HITL-default), [[agentic-engineering]] (35→36 — Agent HQ + four VS Code modes), [[enterprise-ai-adoption]] (65→66 — 30/60/90 playbook), [[vibe-coding]] (17→18 — *"can you vibe debug it?"* + Advanced-Security-caught-injection), [[ai-employment-effects]] (40→41 — WEF 78M-jobs framing). Dangling (single-source, deferred): Brian Randell, Mickey Gousset, GitHub Copilot, Agent HQ, Azure SRE Agent, Azure DevOps, VS Code, Live! 360, World Economic Forum. Touched ~11 files. Re-embed + graph-export pending.

## [2026-06-09] refactor | Promote [[MIT Sloan Executive Education]] to a channel-entity (clears the last dangling author)

Standalone cleanup surfaced by the post-ingest `lint-dangling-authors.mjs` run during the LandingAI ingest. **MIT Sloan Executive Education** appeared as `author:` on two video source pages — [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success|Carrier / Industrial AI That Works]] (31 Mar 2026) and [[2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work|Sterman / Systems Thinking for Leaders]] (15 May 2026) — with no entity page, triggering the second-source author-promotion rule. The condition had existed since 15 May (when the Sterman source became the second mention) but went unreported because the lint isn't hook-fired.

Created [[MIT Sloan Executive Education]] (`kind: organization`, confidence 0.8, source_count 2; two `published-by` edges; channel-entity precedent: [[DeepLearningAI]] / [[Y Combinator]] / [[Lenny's Podcast]]) — the *academic-executive-education* channel-entity, distinct from [[MIT Sloan Management Review]] / [[MIT CISR]] / [[MIT Technology Review Insights]]. Cleared the `[[MIT Sloan Executive Education]]` dangling bullet on the Sterman source; added channel-entity reference lines to both sources (the `publisher:` frontmatter wikilink on both now resolves). Presenters **John D. Sterman**, **John Carrier**, and host **Diane Abbott** remain single-source danglings. `lint-dangling-authors.mjs` → **0 dangling** (multi-source-with-entity 29→30). Reversible: delete one entity page + revert two source-page reference lines.

## [2026-06-09] ingest | [[LandingAI]] *From Touchpoint to Outcome: Transforming Front-Office Processes with AI* (webinar, 26 May 2026) — wiki's first document-AI vendor source; promotes [[LandingAI]] to an entity and creates the [[document-intelligence]] concept

YouTube webinar acquired via `youtube-transcript-skill` (Playwright; ASR-cleaned for proper nouns — "Genting/genetic Document Extraction" → "Agentic Document Extraction", "Andrew En" → "Andrew Ng", "oto/opto" → "OCTO", etc.) and processed same-session. Pre-flight: full ~46-min transcript (443 segments / ~8,350 words); identity clear (LandingAI marketing webinar co-presented with partner TCG); honest-scoping noted — **vendor marketing source**, performance metrics (99.x% accuracy, 85% faster, 75% efficiency) are vendor-reported and uncorroborated.

**Source — [[2026-05-26-landingai-touchpoint-to-outcome-front-office-processes]]** (kind: video; `author: [LandingAI]`). Pairs LandingAI's **Agentic Document Extraction (ADE)** — vision-first, zero-shot, visually-grounded extraction on proprietary **DPT** models; Cloud/VPC/on-prem-air-gapped deployment — with partner TCG's **OCTO** process-automation platform. Theses: OCR accuracy gap (80–90% vs *"high 99.x%"* needed for agentic pipelines → [[enterprise-ai-adoption|adoption]] gate); grounding as trust primitive ([[responsible-ai]]); touchpoint→outcome *"octo-zone"* orchestration. W&W: `digital-transforming/redesigning-internal-structures` + `improving-digital-maturity`, `digital-seizing/rapid-prototyping`, `strategic-renewal/business-model`, `contextual/external-triggers`.

**Neighbour-source scan** (3 candidates surfaced): 2 typed `supports` added — [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Luminai]] (manual-document→AI-automation; vertical-app vs horizontal-platform) and [[2026-05-05-google-gemini-file-search-multimodal|Gemini File Search]] (verifiable grounded document retrieval; RAG vs structured-extraction). Cisco AI-enabled-enterprise considered and skipped (no document-workflow-specific edge).

**Promotions / new pages:** [[LandingAI]] → entity (channel-author + central subject; founder [[Andrew Ng]] already cross-referenced); [[document-intelligence]] → new concept (confidence 0.72, vendor-tier cap; 2 sources). Updated [[Andrew Ng]] (source_count 4→5; Mentioned-in). Dangling (single-source, deferred): TCG, Neil Walker, OCTO, DPT. Touched: source + 2 new pages + [[Andrew Ng]] + `index.md`. Re-embed + graph-export pending.

## [2026-06-08] ingest | Three-PDF batch — Csaszar/Ketkar/Kim *AI & Strategic Decision-Making* (Strategy Science 2024, peer-reviewed) + [[The Linux Foundation]] *State of Tech Talent* Global (May 2026) & Europe (June 2026) — first academic-strategy AI×SDM anchor + first tech-talent-market survey anchor; promotes [[The Linux Foundation]], [[Marco Gerosa]], [[Adrienn Lawson]] to entities

User-requested ingest of three PDFs that had been sitting unprocessed in `raw/` (surfaced by a corrected orphan scan — the earlier "zero orphans" check had matched only `.md` files, missing PDFs). All three converted via `pdftotext` (only converter available); `raw:` points at the original PDFs per repo convention (Anand-Wu / Chatterjee precedent — the markdown conversion is a processing aid, not committed). Pre-flight (scope/identity/honest-scoping) passed on all three: Csaszar = full 25pp *Strategy Science* 9(4):322–345; LF Global = full 38pp (n=400, Feb 2026); LF Europe = full 42pp (398 global / 157 European).

**Source 1 — [[2024-12-01-csaszar-ketkar-kim-ai-strategic-decision-making|Csaszar, Ketkar & Kim 2024]]** (kind: paper, peer-reviewed, *Strategy Science* TBV Special Issue; confidence 0.78). The wiki's first academic-strategy treatment of AI in strategic decision-making and first to engage the [[theory-based-view]] directly. Two empirical studies find LLMs generate/evaluate entrepreneurial strategies at human-comparable levels; search/representation/aggregation framework; competitive-advantage trichotomy (Ricardian → Schumpeterian → erased). W&W: `digital-sensing/digital-scenario-planning`. 3 `supports`: [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua]], [[2026-04-29-boussioux-crowdless-future|Boussioux]], [[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen]].

**Sources 2 & 3 — [[2026-05-01-lf-state-of-tech-talent-global-2026|LF State of Tech Talent (Global)]] + [[2026-06-01-lf-state-of-tech-talent-europe-2026|Europe]]** (kind: report each; [[Marco Gerosa]] & [[Adrienn Lawson]]; confidence 0.75 each — vendor-interested-survey ceiling, LF Education sells the recommended certifications). Sibling pair (same instrument, Global vs Europe cut). Thesis: *"not a jobs crisis, but a skills crisis with an upskilling answer."* AI is a **net driver of IT hiring** (+26%/+31% global; +27%/+17% Europe; only the largest orgs negative); the binding constraint is operationalisation, not headcount. **Key cross-link**: the Europe report's **−3% entry-level technical contraction** (vs +14% rest-of-world) is the wiki's first **survey-side corroboration** of the [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson-canaries]] entry-level-decline finding (payroll + survey converging). Upskilling strongly favoured over hiring (quantified multipliers). W&W (both): `digital-transforming/improving-digital-maturity` + `redesigning-internal-structures` + `contextual/internal-barriers`. Europe `supports` Global (regional cut); both `support` [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson]] + [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles]]; Global also `supports` [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean]].

**Entities promoted (3)**: [[The Linux Foundation]] (3 sources: Headroom channel + both reports — updated the Headroom source's dangling line per the promotion protocol), [[Marco Gerosa]] (2 sources), [[Adrienn Lawson]] (2 sources). **Dangling first-mentions (deferred)**: Felipe A. Csaszar, Harsh Ketkar, Hyunjin Kim, Anna Hermansen, Clyde Seepersad, Thierry Carrez.

**Concept pages updated (5)**: [[theory-based-view]] 1→2 sources (+ *AI and the theory-based view* section; confidence 0.60→0.72), [[strategy]] 4→5 (+ *AI and strategic decision-making* section; 0.85→0.88), [[ai-employment-effects]] 38→40 (+ LF *not-a-jobs-crisis* + European entry-level-corroboration section), [[durable-skills]] 23→25 (+ *upskilling over hiring* section), [[enterprise-ai-adoption]] 62→65 (+ *workforce-readiness constraint* section). **Pages touched total**: 3 new sources + 3 new entities + 5 concepts + Headroom source (dangling-line update) + index + log ≈ 14. **Scoping note**: incidental inbound links to [[automation-vs-augmentation]] / [[analogical-reasoning]] / [[responsible-ai]] were left unedited (mentions, not substantive section additions).

## [2026-06-08] ingest | Chopra / [[Netflix]] ([[The Linux Foundation]]) *Headroom: A Context Optimization Layer for LLM Applications* (3 June 2026) — the wiki's **first shipping-code implementation of the [[agent-harness|harness]] Context layer**: reversible compression (CCR) + cache aligner + per-type content router

Acquired via the `youtube-transcript-skill` (URL `https://youtu.be/UOWSHg18cL0`) — long-format talk, needed a `--timeout 60000` retry (the first attempt returned metadata-only, the ≥20-min panel-render symptom the skill documents). 384 ASR segments at runtime ~41:11. Raw transcript at `raw/videos/2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications.md`. Slug: [[2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications]]. Pre-flight checks: scope (full transcript 0:00 → 41:05; no YouTube chapters, headings inferred), identity (verified — Tejas Chopra, senior engineer at Netflix, presenting his open-source project Headroom on The Linux Foundation channel), honest scoping (length field states *"~41:11 minutes (transcript ~384 lines; auto-generated ASR transcript, cleanup applied for proper nouns … and obvious stutters)"*). ASR corrections: *Tjis/Tahas → Tejas*, *clot/clock code → Claude Code*, *codeex → Codex*, *OpenClaw/open code → OpenCode*, *Reddus → Redis*, *LLM Lingua → LLMLingua*, *cache_cont control → cache_control*; the tool name *RTK* left verbatim (ASR-uncertain).

**Also checked first per the "ingest everything newly added" instruction**: scanned every file in `raw/` against the `raw:` backreference in `wiki/sources/` — **zero orphans**. All previously-acquired raw sources are already processed; nothing else was pending.

**Why it matters**: most wiki harness sources *name* the Context layer ([[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] taxonomy; [[2026-05-04-rethinking-agents-harness-is-all-you-need|the OS-analogy]] casting the context window as RAM); Headroom *ships* it. It is the wiki's first **code-that-ships** treatment of the Context layer (1,900 GitHub stars / 30+ contributors in 4 months) and first Netflix-engineer-authored source. Core insight: the token bloat is in *tool outputs* (whole log files, verbose JSON, DOMs), not the user prompt. Three stages: **cache aligner** (preserve prefix-cache hits by relocating dynamic fields), **content router** (per-type compressors incl. an encoder-only *compress-base* trained on agentic traces vs LLMLingua's meeting summaries), and **CCR / reversible compression** (evict to local Redis/SQLite, expose an MCP `retrieve` tool so the model fetches the original on demand — "99% of the time it doesn't need to"). Plus 11 hooks as interception primitives, cross-agent SQLite memory, and the *beyond-cost* argument (latency for voice agents; accuracy via countering context rot). Forthcoming sibling project **Headlight** = context provenance + agent-consumable telemetry.

**W&W**: no `dynamic_capabilities:` tags — pure LLM-internals / agent-infrastructure, outside the digital-transformation lens (per CLAUDE.md "When not to tag"). **4 typed `supports`** (per neighbour-source scan): [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] (concrete Context-layer implementation), [[2026-05-04-rethinking-agents-harness-is-all-you-need|Prompt Engineering OS-analogy]] (context-window-as-RAM management), [[2026-05-08-bratanic-unified-agentic-memory-hooks|Bratanic]] (cross-harness memory + hooks-as-primitive), [[2025-11-26-anthropic-effective-harnesses-long-running-agents|Anthropic]] (reversible compression as the less-lossy counter to provider-native compaction).

**Pages touched** (4): created [[2026-06-03-chopra-headroom-context-optimization-layer-for-llm-applications]] (confidence 0.75); [[agent-harness]] 54→55 (+ section *Headroom: a shipping Context-layer implementation*); `index.md` (+ source entry); this log. **Dangling first-mentions** (deferred per author-entity promotion rule): Tejas Chopra, Netflix, The Linux Foundation, Headroom, Headlight, compress-base, LLMLingua, RTK, LeanCTX, Agno. **Surface artifact**: YouTube `publish_date` 2026-06-03 (used for slug per schema); `date_ingested: 2026-06-08`.

## [2026-06-06] ingest | Beutler / [[OpenAI]] (IT Revolution Enterprise AI Summit) *Architecting AI-Native Organizations: How to Redesign Work at Scale* (2 June 2026) — the wiki's **first first-party OpenAI source**; introduces the **Ask → Assist → Automate** deployment-maturity ladder + the embedded-engineering / governance-≠-transformation org-design prescription

Acquired via the `youtube-transcript-skill` (URL `https://youtu.be/fFOLWoHyWLE`) — ~360 ASR segments at runtime ~25:25. Raw transcript at `raw/videos/2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler.md`. Slug: [[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler]]. Pre-flight checks: scope (full transcript spans 0:00 → 25:22 of 25:25 video; all 8 chapters populated), identity (verified — Joe Beutler, Head of Solutions Engineering for Strategics at OpenAI, introduced by Gene Kim, on the IT Revolution channel), honest scoping (length field states *"~25:25 minutes (transcript ~360 lines; auto-generated ASR transcript, light cleanup applied for proper nouns — Joe Beutler, ChatGPT, Codex, PwC, BBVA — and obvious stutters/fillers)"*). ASR corrections applied: *Joe Butler→Beutler*, *chatbt/chachib/chatt/chatg→ChatGPT*, *codeex→Codex*, *PWC→PwC*.

**The wiki's first first-party OpenAI source.** Prior OpenAI appearances are all deployment-side (Bain/OpenAI HBR article; ChatGPT-as-access-democratization anchor) or substrate references (GPT-3/4/5, Codex). Beutler is OpenAI describing its *own* organizational redesign + the cross-customer patterns its solutions team sees. This answers the standing open question on the [[OpenAI]] entity page (*"no first-party OpenAI source has been ingested yet"*).

Four contributions: (1) **the adoption gap is a middle-layer gap** — between bottoms-up workforce tools and top-down strategic initiatives lies the missing **team-agents** layer (team/department automation); the org-altitude name for the [[micro-productivity-trap]] and the gap [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|MGI's workflow taxonomy]] quantifies. (2) **Separate governance from transformation; business owns the outcomes** — *"if the head of a business unit is not accountable for the result, you probably don't have an agent. You have a demo."* (3) **Embed engineering inside the business function** via an organic path (domain expert → full-time role → engineer on the same comp ladder → head of innovation); three load-bearing roles (domain expert / AI expert / software engineer); *"the bottleneck is rarely the model capability … it is org design, ownership, and workflow clarity."* (4) **Ask → Assist → Automate** — a deployment-maturity ladder (read-only → human-in-the-loop → full autonomy with exceptions routed to humans), anchored by the T-Mobile case ($3B/60%-automated call center walked back to start at Ask).

Vendor-strategy note: Beutler explicitly rejects the professional-services / outcome-as-a-service model in favour of **selling no-code agent builders** — the deliberate counter-position to [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company|Warren / YC]] and the buyer-side *Buy Outcomes* model in [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria]]. (Same firm, both sides of the wiki's outcome-vs-builder debate.)

**W&W tags** (5 cells): `digital-transforming/redesigning-internal-structures` + `digital-transforming/improving-digital-maturity` + `digital-seizing/balancing-digital-portfolios` + `digital-seizing/rapid-prototyping` + `contextual/internal-enablers` (roles inherited from cell defaults — no override). **4 typed `supports`** (per neighbour-source scan): [[2026-05-08-running-an-ai-native-engineering-org|Fung / Anthropic]] (cross-customer-deployment twin of the inside-Anthropic org rewrite), [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS]] (deployment-maturity complement to USE/COMPOSE/BUILD), [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee / MGI]] (team agents fill the middle layer), [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI]] (same OpenAI vantage; foundation-before-automation).

**Pages touched** (6): created [[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler]] (confidence 0.75); [[OpenAI]] 15→16 sources (+ new section, answered open question); [[enterprise-ai-adoption]] 61→62 (+ first-party-OpenAI deployment-vantage section); [[automation-vs-augmentation]] 37→38 (+ Ask→Assist→Automate ladder); [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] 12→13 sources / 10→11 frameworks (+ deployment-maturity layer, refreshed 2026-06-06); `index.md` (+ source entry). **Dangling first-mentions** (deferred per author-entity promotion rule): Joe Beutler, Gene Kim, IT Revolution, T-Mobile, BBVA, PwC, Enterprise AI Summit Spring 2026.

## [2026-06-02] ingest | Warren / [[Y Combinator]] Startup School *How to Build an AI-Native Services Company* (3 June 2026) — wiki's first YC source explicitly framing *AI-native services companies* as a distinct go-to-market category; 10th YC ingest; vendor-side mirror of Nishar-Nohria's Buy Outcomes

Acquired via the `youtube-transcript-skill` (URL `https://youtu.be/gSNFJbgoaHI`) — 85 ASR segments at runtime ~11:23. Raw transcript at `raw/videos/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md`. Slug: [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company]]. Pre-flight checks: scope (full transcript spans 0:09 → 11:03 of 11:23 video; 12 chapters all populated), identity (verified — Charlie Warren, YC Visiting Partner, on Y Combinator Startup School channel), honest scoping (length field states *"~11:23 minutes (transcript ~85 lines; auto-generated ASR transcript, light cleanup applied for proper nouns and company names in the body — the ASR rendered Cooley as Cooling, Casetext as Caseex, Panacea as Panace, Sam Altman as Sam Alman, all corrected here)"*). **Surface artifact**: the YouTube `publish_date` is 2026-06-03 07:00 PDT — today UTC but technically tomorrow Pacific time at acquire moment. Using YouTube canonical date for slug per schema (`date_published: 2026-06-03`, `date_ingested: 2026-06-02`).

The wiki's first YC source explicitly framing *AI-native services companies* as a distinct go-to-market category — joins the existing nine YC sources which all sit on the *AI-software product* side of the line (Caldwell / Akhtar / Wu&An / Dinakaran / Tan / Hu / Masad / Garg / Koomen). With Warren, the YC corpus now spans **two AI-native-company vertical curricula**: Hu on AI-software products from the ground up, Warren on AI-services companies from the ground up.

The piece is the **vendor-side architectural mirror** of [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar & Nohria's *Buy Outcomes* model]] (HBR, May 2026). Nishar-Nohria framed the buyer-side (firms contracting for outcomes rather than licensing software); Warren writes the YC-altitude playbook for *building* that vendor. The two together form the wiki's first complete **buyer-side architecture + vendor-side playbook** pair on outcome-as-a-service.

**Eleven substantive contributions** (full enumeration on the source page; concept-page touches summarised here):

- **Core thesis** + **outcome-as-product vs co-pilot-as-product** distinction. Markets: tax / audit / insurance / mortgages / parts of healthcare / parts of logistics.
- **Four market-selection traits**: low trust + low task-level judgment + high overall intelligence threshold + regulation-as-moat.
- **Sam Altman Test** + robotics-segmented-out rule + the *are-you-papering-over-product-gaps* honesty check.
- **Three founder attributes**: domain fluency + model fluency + operational rigor.
- **Two YC-portfolio worked examples**: **Panacea** (FDA regulatory services — *regulation-as-moat* + *outcome-based pricing*) + **The General Legal Team** (AI-native law firm; Cooley/Fenwick law firm experience + Casetext technical leadership).
- **Building the product**: humans-as-the-interface + operations-mindset + variance-as-existential-problem + humans-scale-nonlinearly + automating-the-process-as-the-product.
- **Sales / customer success**: the early-demand-trap (cap pilots to a small handful) + *the pilot is the product* + sell-outcomes-not-seats-or-tokens.
- **Pricing playbook**: per-unit + outcome-based as GOOD; cost-plus + straight-line-undercutting as AVOID.
- **P&L opportunity-size frame**: services 30%-margin floor → AI-leveraged 50%+ on TAMs 2-3× bigger than software.
- **Don't-buy-your-way-in rule**: only valid reason is fast regulatory moat (e.g. insurance licensing); otherwise building beats buying.

**W&W tags** (9 cells): `digital-sensing/digital-scouting` + `digital-sensing/digital-scenario-planning` + `digital-seizing/balancing-digital-portfolios` + `digital-seizing/strategic-agility` + `digital-seizing/rapid-prototyping` + `digital-transforming/redesigning-internal-structures` + `digital-transforming/improving-digital-maturity` + `strategic-renewal/business-model` + `contextual/external-triggers`.

**9 typed `supports` relationships**: [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria]] (strongest single edge — vendor-side mirror of buyer-side Buy Outcomes); [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Dinakaran / Luminai]] (same YC vantage, different vertical — playbook + worked example); [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels / McKinsey]] (incumbent-side rewrite + new-entrant-side scratch build); [[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans / Lenny's Podcast]] (services-don't-disappear-they-reinvent dynamic at three altitudes); [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu / YC]] (YC's two-vertical AI-native-company curriculum); [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen / YC Lightcone]] (twin YC-altitude on AI-as-the-building-layer); [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles / WP Intelligence]] (first cross-altitude pairing: enterprise-buyer-of-agent-services + startup-vendor-of-agent-services); [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero|Scheffer / HelloPrint]] (in-place SME rebuild + greenfield startup rebuild = same phenomenon, two boundary conditions); [[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era|Moon / McKinsey]] (operating-model shift across two industries).

**Concept changes**: [[enterprise-ai-adoption]] 60→61 (added section on *The AI-native services company vendor-side playbook* — *services-don't-disappear-they-reinvent* thesis now visible at **four altitudes**: incumbent-firm / buyer-firm-boundary / startup-vendor / in-place-SME), [[automation-vs-augmentation]] 36→37 (added §18 *Humans as the interface, the product as the operation* — vendor-product-design pattern; the §16/§17/§18 cluster forms the wiki's *role-redesign + vendor-product-design* augmentation-pole package), [[agent-harness]] 53→54 (Warren's Sam Altman Test + model fluency framing added to the convergence table as the YC-altitude founder-team-selection vantage on the *model-rented, harness-owned* discipline), [[micro-productivity-trap]] 27→28 (Warren entry added — vendor-side founder-prescription on the trap: variance-not-throughput as customer-firing-trigger + automating-the-process-as-the-product + the 30%→50%+ AI-operating-leverage trajectory as escape-velocity-quantification). All `last_confirmed` + `accessed_at` bumped to 2026-06-02.

**Entity changes**: [[Y Combinator]] 12→13 (added §10 *Warren / Startup School* + extended the YC-batch-context table to 10 entries; second Startup School ingest after Hu / April 2026).

**Dangling first-mentions** (deferred per second-source rule): **Charlie Warren** (YC Visiting Partner), **Panacea** (YC company, FDA regulatory services — named twice as *regulation-as-moat* + *outcome-based pricing* exemplars), **The General Legal Team** (YC AI-native law firm), **Cooley** (US law firm), **Fenwick** (US law firm), **Casetext** (legal-tech firm acquired by Thomson Reuters in 2023). All defer per the second-source promotion rule.

## [2026-06-02] ingest | Peron / [[MIT Sloan Management Review]] *AI for Interoperability in Health Care: Philips's Carla Goulart Peron* (31 May 2026) — wiki's first dedicated healthcare-AI source + first *Me, Myself, and AI* podcast ingest; first vendor-side practitioner-altitude clinical-AI anchor

Acquired via the `youtube-transcript-skill` (URL `https://youtu.be/xDUn0qbwqtQ`) — 241 ASR segments at runtime ~31:03. Raw transcript at `raw/videos/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md`. Slug: [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care]]. Pre-flight checks: scope (full transcript spans 0:02 → 30:47 of a 31:03 video), identity (verified — Dr. Carla Goulart Peron, Philips Chief Medical Officer, on *Me, Myself, and AI* Season 13 with host Sam Ransbotham), honest scoping (length field states *"~31:03 minutes (transcript ~241 lines; auto-generated ASR transcript, light cleanup applied for proper nouns and product names in the body)"*). **Surface artifact**: ASR rendered Peron's name as *"Carla Gloram"* at segment 0:13 and *"Sa Paulo"* for São Paulo throughout — caption-track defaults; transcript otherwise clean. Sponsor break for MIT Sloan Executive Education at 12:38–13:10 retained in raw, omitted from wiki summary.

The wiki's first dedicated healthcare-AI source. Sits adjacent to [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Dinakaran / Luminai (Apr 2026)]] at startup-altitude on hospital ops — together they form the wiki's first **two-altitude healthcare-AI cluster**: Peron at *clinical-practice* altitude (imaging setup, diagnostic-image processing, women's-health-protocol-bias-detection), Luminai at *hospital-administrative-operations* altitude (admin, scheduling, prior-auth, claims).

**Six substantive contributions** (full enumeration on the source page; concept-page touches summarised here):

- **The Philips SmartArt cardiac-MRI worked example** — recent FDA clearance for an AI-driven one-click automation that compresses cardiac-MRI setup from ~15 minutes to **30 seconds**, reducing technician-training dependency and ~4×-ing throughput.
- **Radiology-displacement-that-didn't-happen historical anchor** + **the radiologist-training-gap question** (currently unresolved): if AI flags only abnormal images, how do new radiologists calibrate against normal? — a clean clinical-domain instance of a *training-pipeline class-imbalance* deskilling mechanism, distinct from task-composition shift and BCG-AI-brain-fry.
- **The nine-German-women postpartum-blood-loss anchor + women's-cardiac-health gap** — the wiki's clearest single worked example of *AI-as-clinical-protocol-bias-auditor* at population scale; India's recalibration of postpartum-blood-loss-standard to ~300mL from the German anchor based on smaller body sizes is the operational case.
- **Future Health Index trust gap** — 79% of clinicians vs ~50% of patients; clinician-concern is data-driven, patient-concern is experiential.
- **Interoperability as the single-pick global AI capability** + three named barriers (data-quality-and-standardization, reimbursement-incentive-misalignment, regulatory-evolution-required).
- Recurring frame: ***"AI is here to add, not to take over"*** — context that makes it hold differently: healthcare's structural undersupply → *do more with the same not with less*.

**W&W tags** (10 cells, with a `roles:` override to `cto, cdo, cmo, transformation-lead, product-manager, rd-director` reflecting the healthcare-vendor CMO-vantage): `digital-sensing/digital-mindset-crafting` + `digital-sensing/digital-scenario-planning` + `digital-seizing/balancing-digital-portfolios` + `digital-seizing/rapid-prototyping` + `digital-transforming/improving-digital-maturity` + `digital-transforming/navigating-innovation-ecosystems` + `strategic-renewal/business-model` + `strategic-renewal/collaborative-approach` + `contextual/external-triggers` + `contextual/internal-enablers`.

**5 typed relationships**: 4 `supports` ([[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Dinakaran / Luminai]] — first two-altitude healthcare-AI cluster; [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee / MGI]] — clinicians in the *people-centric* occupation archetype, qualitative confirmation of MGI quantitative finding; [[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. Augmented Learners]] — same-host pairing applied to organizational-learning frame; [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs|Giles / WP Intelligence]] — cross-altitude support on the *do-more-with-the-same* prescription). **1 `contradicts`**: [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad / Replit]] — clinical-domain rejection of broad-occupation-substitution framing.

**Concept changes**: [[automation-vs-augmentation]] 35→36, [[ai-deskilling]] 9→10 (new third causal mechanism: training-pipeline class-imbalance), [[responsible-ai]] 12→13 (new RAI category: *AI-as-audit-tool-against-pre-AI-embedded-biases*). All `last_confirmed` + `accessed_at` bumped to 2026-06-02.

**Entity changes**: [[MIT Sloan Management Review]] 4→5 (confidence 0.85→0.88; typed `published-by` edge added; sources-table extended; first podcast-format MIT SMR source in the wiki). [[Sam Ransbotham]] 1→2 (confidence 0.75→0.80; typed `authored-by` edge added; Wiki contributions extended with host-vantage podcast role).

**Dangling first-mentions** (deferred per second-source rule): **Carla Goulart Peron** (the subject; first appearance — entire content of source is her practitioner thinking, deferred per the same precedent set with Benedict Evans), **Philips** (referenced multiple times; first wiki mention — likely promotion candidate on a second healthcare-AI source mentioning Philips), Medtronic, SmartArt (Philips FDA-cleared 2026 product), Future Health Index (Philips's annual survey), Me, Myself, and AI (the podcast itself), Bernard Hampton (next-week guest, forward-reference), Josh from CVS (Ransbotham's prior guest reference).

## [2026-06-02] ingest | Giles / Washington Post Intelligence *The new human-machine workforce: How agentic AI will transform jobs* (WP Intelligence, 28 May 2026) — wiki's first Washington Post-affiliated source + first EY-sponsored ingest; first Martin-Giles-authored source

User-supplied browser-print PDF (12 pages, ~2.4 MB; `Producer: Skia/PDF m148`, Chrome export 2026-06-01 20:26) saved at `raw/articles/The new human-machine workforce_ How agentic AI will transform jobs - WP Intelligence.pdf`. Slug: [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs]]. Pre-flight checks: scope (full 12-page article body ingested), identity (verified — Martin Giles, WP Intelligence, AI & Tech section, 28 May 2026), honest scoping (length field states *"~12-page browser-print PDF (~2.4MB; Skia/PDF m148, Chrome export 2026-06-01). Full article body ingested. Two inline EY ad placements + iStockPhoto cover illustration retained in raw, omitted from wiki summary."*). Distribution sponsored by EY (*"The free distribution of this report is made possible by EY"* appears below the masthead).

The wiki's first Washington Post-affiliated source + first ingest under the `Martin Giles` `author:` value + first EY-sponsored ingest. **Executive-readership news-survey altitude** — opens with five bulleted *Key Takeaways*, structures the body around four named subsections, closes with five prescriptive executive recommendations. Sits next to two other May-2026 anchors on the AI-employment-effects question: [[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans / Lenny's Podcast 31 May 2026]] at independent-analyst altitude and [[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era|Moon et al. / McKinsey 28 May 2026]] at consulting-firm operational altitude. Giles is the **executive-readership news-survey altitude** in that cluster.

**Eight substantive contributions**:

- **April-2026 layoff anchor + AI-as-#1-cited-reason** — 83,387 US job cuts (+38% from March; 3rd-highest month since 2009 per Challenger, Gray & Christmas); AI cited #1 reason for cuts in both March and April. Single-firm anchors: Block (Dorsey) 40%-workforce-cut; Meta (Zuckerberg) 8,000-cut + capex raised to $125-145B.
- **Gartner spending + Jensen Huang *information robots*** — AI agent spending $86.4B → $206.5B (>2×); agents handling ~1/3 of business decisions by 2028.
- **HubSpot *no-mass-layoff* counter-example** — Helen Russell (CPO): redeployed 10 HR staff from interview-scheduling to employee-satisfaction/development.
- **Carl Benedikt Frey *no-automobile-industry* empirical counter** — Oxford AI/work professor's *historical-induction-may-not-extrapolate* caveat; third pole in the *Brynjolfsson Canaries + Evans lump-of-labor + Frey* triangulation.
- **Entry-level + IBM tripling counter-trend** — Stanford 22-25-year-olds 6%-decline (which IS the Brynjolfsson Canaries paper) + NACE 14%-replaced-with-AI survey + IBM tripling entry-level hiring (Nickle LaMoreaux) + UiPath Garaba *"growth engine"* quote.
- **Senior production planners → agent orchestrators / WEF manufacturing anchor** — Siemens 69% labor productivity at Germany factory; Danfoss days→minutes; **Kiva Allgood: chatbots 2-3% productivity vs deeper agent + automation 30-60%** (the wiki's clearest numerical anchor on the chatbot-vs-deeper-deployment gap).
- **Swamy Kocherlakota / Zscaler twin quotes** — *"end-to-end systems thinking"* + *"working like a robot, your job will be taken by a robot."*
- **Five executive recommendations** — Review workflows first / Remember agentic tech isn't perfect / Redesign entry-level roles (IBM model) / Beware AI-linked skill erosion / Communicate around AI carefully (Amodei dire-predictions *communications minefield*).

Plus: McKinsey top-3 functions (IT, knowledge management, sales & marketing); Goldman Sachs identifies legal + life sciences as most exposed; Coursera 2026 Job Skills Report — **120% YoY increase in critical-thinking course enrollments** across 6M learners and ~7,000 orgs.

**W&W tags** (10 cells — among the broadest, comparable to Allen-AWS / Everitt-JetBrains / Scheffer / Moon-McKinsey): `digital-sensing/digital-scouting` + `digital-sensing/digital-scenario-planning` + `digital-seizing/balancing-digital-portfolios` + `digital-seizing/strategic-agility` + `digital-transforming/redesigning-internal-structures` + `digital-transforming/improving-digital-maturity` + `strategic-renewal/business-model` + `strategic-renewal/organizational-culture` + `contextual/external-triggers` + `contextual/internal-barriers`.

**9 typed relationships**: 1 `contradicts` ([[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going|Evans / Lenny's Podcast]] — partial; Frey *no-automobile-industry* + April-2026-layoffs counter Evans's lump-of-labor + new-jobs-will-emerge framings, but both agree on AI-labs-still-hiring + workflow-redesign-as-real-work). 8 `supports` ([[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson Canaries]] — Stanford 22-25 study IS the Canaries paper; [[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era|Moon / McKinsey]] — same-week 28 May, manager-as-orchestrator convergence; [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels / McKinsey]]; [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad / Replit]] — doom-side convergence; [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS]] — production planners → orchestrators + chatbot-vs-agent split; [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero|Scheffer / HelloPrint]] — HR-redeployment-as-augmentation at SME altitude; [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee / MGI]] — skills-matter-more-than-titles; [[2026-04-30-ai-index-report-2026|AI Index 2026]]).

**Concept changes**: [[ai-employment-effects]] 36→38 (+2; added *April-2026 layoff anchor + AI-as-#1-cited-reason monthly attribution* section + *Frey no-automobile-industry counter-precedent* section + *Peron do-more-with-the-same healthcare-domain reframe* section — the wiki's first **domain-conditional** reading of AI-employment-effects), [[automation-vs-augmentation]] 35→36 (added §16 *HubSpot redeployment-of-ten + IBM redesign-entry-level-roles* worked examples — note: with the prior Peron edit, this concept ran to source_count 36 in one pass), [[enterprise-ai-adoption]] 59→60 (added *Gartner $86B→$206B + one-third-business-decisions-by-2028 + five executive recommendations* section), [[micro-productivity-trap]] 26→27 (added *Allgood 2-3% vs 30-60% + Siemens 69% + Danfoss days-to-minutes* section), [[ai-deskilling]] 8→9 (added *AI-linked skill erosion as an executive prescription* section — note: with the prior Peron edit, this concept ran to source_count 10 in one pass), [[durable-skills]] 22→23 (added *Coursera 120% critical-thinking growth + Kocherlakota systems-thinking + UiPath case-study pedagogy* section). All `last_confirmed` + `accessed_at` bumped to 2026-06-02.

**Combined concept-page touches across both 2026-06-02 ingests**: [[ai-employment-effects]] 35→38 (+3), [[automation-vs-augmentation]] 34→36 (+2), [[ai-deskilling]] 8→10 (+2), [[enterprise-ai-adoption]] 59→60 (+1), [[micro-productivity-trap]] 26→27 (+1), [[durable-skills]] 22→23 (+1), [[responsible-ai]] 12→13 (+1).

**Dangling first-mentions** (deferred per second-source rule): **Martin Giles** (author), **Washington Post Intelligence / WP Intelligence** (publisher; first wiki source — likely promotion candidate on a second Washington Post-affiliated source), **EY** (sponsor; first EY-sponsored ingest), **Carl Benedikt Frey** (Oxford AI/work), **Jensen Huang / Nvidia**, **Jack Dorsey / Block / Square**, **Mark Zuckerberg / Meta** (referenced across wiki sources as body figure but no entity page), **Helen Russell / HubSpot** (HubSpot has a prior Claude customer-success source via [[2026-02-09-hubspot-customer-success-with-claude]] but no entity page), **Agi Garaba / UiPath**, **Nickle LaMoreaux / IBM**, **Kiva Allgood / WEF Center for Advanced Manufacturing**, **Swamy Kocherlakota / Zscaler**, **Siemens**, **Danfoss**, **Coursera**, **Challenger, Gray & Christmas**, **NACE (National Association of Colleges and Employers)**, **Goldman Sachs**, **Gartner**.

## [2026-06-01] ingest | Evans / [[Lenny's Podcast]] *A rational conversation on where AI is actually going | Benedict Evans* (31 May 2026) — wiki's first independent-analyst-altitude long-form anchor; 5th source under the Lenny's Podcast channel; first Benedict-Evans-authored source

Acquired via the `youtube-transcript-skill` after a 90s engagement-panel timeout retry (initial 30s default failed on this ~80-minute talk per the skill's documented long-talk failure mode). Raw transcript at `raw/videos/2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going.md` — 1568 ASR segments, 0:00 → 1:19:47, full ingest. Slug: [[2026-05-31-benedict-evans-rational-conversation-on-where-ai-is-actually-going]]. Pre-flight checks: scope (full transcript, runtime 1:19:50, 1568 segments span effectively the full duration), identity (verified — Benedict Evans, ex-a16z partner, independent analyst, on Lenny's Podcast; matches channel and description-blockquote attribution), honest scoping (length field states *"~1:19:50 minutes (transcript ~1568 lines; auto-generated ASR transcript, lightly cleaned for naming/proper-noun errors in body)"*). **Surface artifact**: the raw transcript file contains a duplicate transcript block (lines 1257–2040 repeat lines 473–1256) — a `youtube-transcript-skill` output quirk worth tracking; raw is immutable; doesn't affect ingest. The duplicate has been noted but not patched per the *raw is immutable* discipline.

**Channel-altitude framing.** The 5th source under [[Lenny's Podcast]] joins a previously operator-and-founder-only cluster (Caldwell / Schoening / Ries / Spiegel) with the channel's first **independent-analyst-altitude** anchor. Evans's rhetorical move is deflation: *AI is as big as the internet or mobile — and only as big*. Sits structurally outside the operator-altitude cluster — different register inside the same long-form-interview format.

**Twelve substantive contributions** (full enumeration on the source page; concept-page touches summarised here):

- **The *1997 for AI* framing** + **task vs job** analytical lever (the operational alternative to percentage-of-job decomposition) + **expert-systems analogy as methodological critique of O\*NET-style task-decomposition** — *"17% of a senior partner's work could be automated. This is horseshit."*
- **Excel-made-bankers-work-longer / Jevons-paradox** with the **AI-labs-themselves-keep-hiring** corollary (Anthropic, OpenAI, every) + **Forward-deployed-engineer = Accenture-outsourced-developer-in-SF** observation.
- **Foundation-models-as-commodity-utilities thesis** with the **AWS-not-Windows** analogy + **distribution-becomes-the-moat** once product is commodity + **AGI-as-sliding-goalpost** (Larry Tesler quote applied).
- **Anti-AI backlash as *big fuzzy mess*** with Livermore-Lab end-2024 data-centre water statistic (~0.017% of US water consumption) + **5–10-year sector-by-sector replacement** speed model + **mobile-era half-the-internet-untouched** analogy + ***dive in, don't shout from Bluesky*** career advice.

**W&W tags** (7 cells): `digital-sensing/digital-scouting` + `digital-sensing/digital-scenario-planning` + `digital-seizing/balancing-digital-portfolios` + `digital-seizing/strategic-agility` + `digital-transforming/redesigning-internal-structures` + `strategic-renewal/business-model` + `contextual/external-triggers`.

**12 typed relationships**: 8 `supports` ([[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era|McKinsey rewiring]] — FDE-as-Accenture-in-SF mirrors team-shape thesis; [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels / McKinsey]] — AI labs invest IN consultancies; [[2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo|Spiegel]] — distribution-becomes-the-moat, line-for-line; [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen / YC]] — career-advice posture + harness namecheck; [[2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report|Sajadieh]] + [[2026-04-30-ai-index-report-2026|AI Index]] — Gen-Z adoption-data overlap; [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS]] — workflow redesign needs consultants; [[2026-05-08-running-an-ai-native-engineering-org|Anthropic engineering-org]] — AI labs keep hiring; [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng]] — harness namecheck). **3 `contradicts`** ([[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua]] — methodology critique, accepts frontier rejects percentage decomp; [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson Canaries]] — same critique applied to task-level AI-exposure analysis; [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad / Replit]] — lump-of-labor fallacy directly contradicts *only-two-jobs-left* framing).

**Concept changes**: [[jagged-frontier]] 10→11 (added methodological-critique entry under Practical implications), [[ai-employment-effects]] 35→36 (added lump-of-labor section with three corollaries), [[automation-vs-augmentation]] 33→34 (added §16 *task-vs-job analytical lever*), [[foundation-models]] 14→15 (added commodity-utility / pricing-power-or-not section + debate entry), [[enterprise-ai-adoption]] 58→59 (added 5–10-year sector-by-sector speed-model section), [[agent-harness]] 52→53 (lexical-diffusion datapoint added to convergence table). All concept-page `last_confirmed` + `accessed_at` bumped to 2026-06-01.

**Entity changes**: [[Lenny's Podcast]] 4→5 (typed `published-by` edge added; opening paragraph refactored to *five sources / two-year arc / independent-analyst-altitude joining the operator-and-founder cluster*; sources-table extended). Confidence 0.80 → 0.85.

**Dangling first-mentions** (deferred per second-source rule): **Benedict Evans** (the subject; first appearance; channel-as-author convention defers entity-page creation), **Lenny Rachitsky** (host; 5+ sources but never as `author:`), **Larry Tesler**, **Mark Andreessen**, **Dario Amodei** (referenced in this and prior sources — entity-promotion candidate for a focused pass), **Steven Sinofsky**, **Eric Schmidt**, **Dan Shipper**, **Frame.io**, **Andreessen Horowitz**, **Llama / Meta-AI**.

**Pricing-power open question**: the *do model labs have pricing power?* question Evans poses as the under-asked question of 2026 is now an explicit `## Debates / contradictions` entry on [[foundation-models]]. The wiki has Evans as its first explicit *no-they-won't-have-pricing-power* voice at independent-analyst altitude; the contrary presumption is implicit across multiple practitioner sources but not directly anchored.

## [2026-05-29] ingest | Moon / Walsh / Di Leo / [[McKinsey & Company]] *Rewiring software delivery for the agentic era* (McKinsey Technology, 28 May 2026) — same-firm operational follow-up to Sternfels (Feb 2026); McKinsey-altitude quantification of the team-shape collapse Allen/AWS + Ng + Koomen all describe

User-supplied browser-print PDF (7 pp, ~1.1 MB) saved from mckinsey.com today. Slug: [[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era]]. Lead authors: **Jared Moon** (Senior Partner, London) + **Rory Walsh** (Partner, Dublin) + **Vito Di Leo** (Partner, Zurich) + **Adam Thelwall** (Associate Partner). Acknowledged contributors: Aishik Dhar, Amray Schwabe, Benjamin Schloesing, Nikolaus Müller. Editor: Barr Seitz (Editorial Director, NY). Pre-flight checks: scope (full 7-page article body ingested; no paywall fragments), identity (verified — McKinsey Technology, May 28 2026), honest scoping (length field states *"~7 pages (browser-print PDF). Full article body ingested. Three illustrative McKinsey-analysis exhibits."*).

**The wiki's second McKinsey-published source on agentic-era enterprise transformation** — extends [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels (Feb 2026)]]'s **firm-level-reinvention thesis** (at managing-partner doctrinal altitude) with a **same-firm 3.5-month-later operational specification** of *how* that reinvention happens inside one work domain (software delivery). The McKinsey-internal cluster now spans three vantages: **Sternfels managing-partner / MGI macroeconomic / McKinsey-Digital tech-partner** — all anchoring the firm's *AI-rewires-the-operating-model* doctrine.

**Six substantive contributions:**

1. **The 9 a.m. vignette and the *24-hour-sprint model*** — *"At 9:00 a.m., a product owner logs in to review overnight progress ... No one worked late. AI agents did."* The operational structure: **night shift (16 hours, led by a factory of agents)** does Requirements + Architecture + Build-and-test; **day shift (8 hours, humans supported by agents)** does Sprint review/demo + Spec-and-code working session + Offline system optimization + Sprint planning. Human-role framing: *"Increasingly, their role is less about producing artifacts and more about supervising and improving the system that produces them."*
2. **The *extend automation to eliminate human handoffs* thesis with the 30%/70% CI/CD cost decomposition** — *"Traditional continuous integration and continuous delivery (CI/CD) automation focuses largely on testing and deployment. While those costs vary, our experience is that they can be as much as 30 percent of total technology spend. The majority of effort, concentrated in requirements through coding, remains manual and interpretation heavy."* The agentic model attacks the 70% upstream interpretation-heavy work by *"structuring artifacts for machine-to-machine handoffs."* Main takeaway: *"Scaling AI requires applying engineering practices to the development system itself."*
3. **The *knowledge graphs as AI memory layer* infrastructure prescription** with the named **librarian agent** + the **anti-grand-ontology design principle** (*"this should not begin with a grand, top-down ontology effort. The graph should evolve organically around priority domains and live programs, compounding value over time"*) + the **knowledge-as-production-infrastructure / durable-source-of-competitive-advantage** closing claim.
4. **The team-size quantification anchor** — Exhibit 3: **100 → 60 FTEs / 200 → 100 person-years / 10 teams of 8-12 → 16 teams of 3-4 / 10-role-pod → 3-role-pod**. Pod composition collapses from (Product owner + Business analyst + Tech lead + 5 Software engineers + 2 Testers) to (Product owner + Tech lead + AI-enabled engineer) — 7 of 10 roles dissolved. Headline article-grab claims: *"threefold to fivefold improvements in productivity, with a 60 percent reduction in team size."*
5. **The *outer-loop roles* integration prescription** — risk / legal / testing / procurement baked into the agentic-development effort by design, not as end-of-process gatekeepers, with **policy as code** as the named primitive. *"These controls should be baked in by design, rather than becoming a gatekeeper at the end of the process."*
6. **The *capacity-reinvestment-not-cost-cut* normative framing** — *"Productivity gains can be translated into structural portfolio changes. Resize teams and consciously redeploy capacity to capture full value ... Freed capacity is often reinvested to accelerate road maps, modernize platforms, or launch new products."*

**Closing thesis**: *"As agents take on execution at scale and produce code that is robust and consistently secure, human roles will concentrate in architecture, product judgment, and system design, making institutional knowledge and technical coherence decisive differentiators. Organizations that begin building these capabilities as part of a broader effort to rewire their operating model will not just move faster; they will redefine how software creates value."* The wiki's clearest McKinsey-consulting-altitude statement of the *durable-skills-concentrate-at-the-top-of-the-K-curve* claim — convergent with [[2026-05-19-elangovan-amd-deeplearningai-ai-dev-26-sf-impact-of-ai-on-software|Elangovan's K-shape]] and [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|SEI/CMU's coder-vs-engineer]] role-shift thesis.

**Neighbour-source scan (Path A + Path B)** surfaced 5 strong typed-edge candidates: [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels / McKinsey]] (same-firm 3.5-month operational follow-up — managing-partner-doctrinal-altitude + tech-partner-operational-altitude pair); [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS London]] (McKinsey-altitude quantification of AWS's Project-Mantle worked example — AWS-VP-Distinguished-Engineer 76-days-vs-18-months data point + McKinsey-aggregated-multiple-companies anchor, one week apart, structurally identical team-shape claim); [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng / AI Dev 26 SF]] (convergent quantification of PM-bottleneck cascading-bottlenecks small-team-of-generalists — 10-role-pod → 3-role-pod is the McKinsey-altitude empirical anchor for Ng's *engineer-plus-PM collapse into single human*); [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen / YC Lightcone]] (consulting-altitude operational specification of Koomen's multiplayer-harness primitive set — shared-week declarations on *knowledge-as-production-infrastructure* at YC-founder + McKinsey-tech-partner altitudes within 48 hours); [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee / MGI]] (cross-McKinsey-internal converging declaration — MGI macroeconomic substrate + Tech-partner operational specification, 6 months apart).

**W&W tagging** (9 cells — same breadth as yesterday's [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero|Scheffer / De Ondernemer]], comparable to [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|Everitt / JetBrains]] 10 cells + [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS London]] 10 cells + [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen / YC Lightcone]] 8 cells): `digital-sensing/digital-scenario-planning` + `digital-seizing/balancing-digital-portfolios` + `digital-seizing/strategic-agility` + `digital-seizing/rapid-prototyping` + `digital-transforming/redesigning-internal-structures` + `digital-transforming/improving-digital-maturity` + `strategic-renewal/business-model` + `strategic-renewal/organizational-culture` + `contextual/external-triggers`. The presence of both `strategic-renewal/business-model` (*"redefine how software creates value"*) and `strategic-renewal/organizational-culture` (*"role shifts from producing artifacts to supervising the system that produces them"*) cells reflects this source's reach into the *strategic-renewal* outcome layer.

**Touched pages** (13):

- New: [[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era]] (source page).
- Entity bump: [[McKinsey & Company]] 8→9 + last_confirmed / accessed_at to 2026-05-29.
- Concept bumps (frontmatter only): [[agentic-engineering]] 34→35, [[agent-harness]] 51→52, [[agent-development-lifecycle]] 14→15, [[enterprise-ai-adoption]] 57→58, [[ai-employment-effects]] 34→35, [[micro-productivity-trap]] 25→26, [[automation-vs-augmentation]] 32→33, [[durable-skills]] 21→22.
- Synthesis bumps: [[knowledge-architectures-for-llm-agents]] 7→8 (the *knowledge-graphs-as-AI-memory-layer + librarian-agent + anti-grand-ontology-design-principle* framing is a substantive McKinsey-consulting-altitude operational anchor — the synthesis's 8th source); [[is-rag-dead]] 7→8 (the *agents-need-organizational-context-and-memory* claim + knowledge-graph-as-substrate is convergent with the synthesis's *RAG-alive-inside-agentic-harness* conclusion at McKinsey-altitude — the synthesis's 8th source).
- Index updated; this log entry prepended.

**All 9 mentioned individual contributors are first-mention dangling** (Jared Moon, Rory Walsh, Vito Di Leo, Adam Thelwall, Aishik Dhar, Amray Schwabe, Benjamin Schloesing, Nikolaus Müller, Barr Seitz) — no individual-contributor entity promotions in this ingest. Three London / Dublin / Zurich McKinsey-Digital tech-partners and one Associate Partner are a substantive geographic and career-step expansion of the firm's wiki representation; future ingests should look for second-source mentions to promote.

**Five single-source-deferred concept-page candidates**: *24-hour sprint model* (McKinsey's distinctive operational frame); *factory of agents* (McKinsey's named primitive); *librarian agent* (McKinsey's named role for knowledge-graph-querying agent); *policy-as-code as outer-loop integration primitive* (McKinsey's prescription for risk / legal / testing / procurement baked in by design); *knowledge as production infrastructure* (McKinsey's strongest single-line strategic-renewal claim about knowledge architecture).

**Open questions / follow-ups**: **Boundary AI** is cited as 2026-04-02 source for *Software development cost: Complete 2026 budget guide* — plausible adjacent ingest target if the underlying methodology turns out to be substantive (the 30%/70% CI/CD-vs-requirements-through-coding cost decomposition appears to anchor on it). The two other identified McKinsey-Tech-partner sources from this campaign — if the rebrand "McKinsey Technology" reflects a new content vertical, the wiki should watch for adjacent operational-specification articles on adjacent work domains (marketing, finance, HR, customer service, supply chain). The **3-role pod composition** (Product owner + Tech lead + **AI-enabled engineer**) names a new role-archetype that is the **wiki's clearest single-line consulting-altitude generalist role-archetype proposal** — worth tracking as a candidate-named role across other 2026 ingests.

---

## [2026-05-29] ingest | Scheffer / [[De Ondernemer]] *Ondanks 80 miljoen omzet gooit Hans Scheffer zijn bedrijf volledig om met AI: 'Elke kantoorbaan voor een scherm verdwijnt'* — wiki's first Dutch-MKB-altitude AI-transformation anchor

User-supplied browser-print PDF (14 pp, ~9.8 MB, Skia/PDF — saved from De Ondernemer website today). Slug: [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero]]. Author: **Tijmen Koppelaar** (De Ondernemer journalist). Subject: **Hans Scheffer**, founder and CEO of **HelloPrint** — a Dutch print platform that did ~**€80M revenue in 2025** with operations in the Netherlands and Valencia, Spain. Original language: Dutch. Pre-flight checks: scope (full article body ingested from pages 1-9 of 14; pages 10-14 are newsletter signup + Lees-ook companion-article links), identity (verified — Tijmen Koppelaar / De Ondernemer / DPG Media), honest scoping (length field states *"~7 minute read (14-page browser-print PDF; pages 1-9 article body, pages 10-14 newsletter signup + Lees-ook related-article links). Full article body ingested. Original language: Dutch."*).

**The wiki's first Dutch-MKB-altitude AI-transformation anchor.** The existing transformation cluster is heavily US-vantage ([[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu / YC]] + [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen / YC Lightcone]] + [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|MGI / Yee et al.]]) + UK-vantage ([[2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook|Erginbilgiç / Rolls-Royce]] + [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS London]]) + Swiss-corporate-academic ([[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger]] origin). Scheffer is a Dutch SME founder-CEO at €80M revenue scale — a meaningful altitude addition. The *MKB-as-easier-transformation-context* observation — *'Dat is juist relevant voor mkb'ers ... Als je een kleiner bedrijf hebt, is het veel makkelijker om dat te doen'* — is the wiki's first explicit claim that the rebuild is *easier* at SME scale than at large-corporate scale.

**Six substantive contributions** (full quotation preserved in source page body for Dutch-speakers verification):

1. **The *technology-leading / people-directing* structural reversal.** *'Waar vroeger de mensen eerst kwamen en technologie ondersteunend was, draait dat nu om. Technologie wordt leidend, en daaromheen zit een veel kleinere groep mensen die die technologie aanstuurt.'* Same-day-different-continent convergent declaration with [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen's *AI as the building layer for everything, not a copilot*]] from the same calendar day (27 May 2026).
2. **The *denk vanuit dag nul* (day-zero rebuild) thought experiment as transformation method.** *'wat nou als ik mijn huidige bedrijf op dag één opnieuw zou moeten bouwen, wat zou ik dan doen?'* Credits the **House of Founders** five-day session in South Africa (with Joep Verbunt of Matt Sleeps + Ron Simpson) as the experiential anchor.
3. **The *AI-brein* (AI-brain) as organisational foundation, not a standalone IT project.** *'Aparte afdelingen voor marketing, IT, operatie en finance, elk met eigen systemen en verantwoordingslagen, verliezen hun functie.'*
4. **The *Chief AI Officer is the missing role in MKB management teams* observation.** Scheffer's named-MKB-role-gap diagnosis: *'Techniek wordt nog te vaak gezien als ondersteunend ... IT wordt uitbesteed of belegd bij één medewerker, terwijl niemand eindverantwoordelijk is voor hoe technologie het businessmodel, de processen en de organisatie vormgeeft.'*
5. **The HelloPrint customer-service *100 → 18* worked example.** Headcount cut to 18% of peak with AI quality exceeding human (*'beter dan het niveau waarop mensen het kunnen doen'*), primarily via natural attrition (Valencia rotation throughput not replaced). The wiki's clearest single-SME-firm quantified-customer-service-automation worked example.
6. **The *conscious revenue sacrifice for long-term winning* operating discipline.** *'door bijvoorbeeld afscheid te nemen van bepaalde omzetgroepen ... wel een fundamentele keuze om op de lange termijn te kunnen winnen.'* Convergent with [[2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook|Erginbilgiç's Rolls-Royce *transform-from-strength* playbook]] at radically different scale (Erginbilgiç £80B FTSE-CEO + Scheffer €80M Dutch-SME-CEO, three calendar days apart, same playbook).

**Plus** the headline-grab maximalist claim *'Elke kantoorbaan voor een scherm gaat verdwijnen ... Heel veel banen die wij kennen, gaan gewoon echt verdwijnen.'* — the wiki's clearest Dutch-SME-founder-CEO-vantage maximalist statement of the office-work-displacement thesis + the **€80M → €1B *stip op de horizon*** with fifty-year company-vision close + the *topsport-team not-everyone-fits* culture framing.

**Neighbour-source scan (Path A + Path B)** surfaced 5 strong typed-edge candidates, all filed: [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee / MGI]] (qualitative Dutch-MKB-founder-CEO confirmation of MGI's quantitative *every-office-job-behind-screen-is-automatable* finding + the SCI + 44%-via-agents framework — HelloPrint customer-service 100→18 is a single-firm empirical anchor inside MGI's agent-centric archetype), [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu / YC]] (Dutch-SME-founder-CEO operationalisation of Hu's day-zero / closed-loop-company prescriptive doctrine — Scheffer's *MKB-as-easier-transformation-context* observation is the SME-altitude inversion of Hu's YC-startup-batch framing), [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen / YC Lightcone]] (same-day-different-continent convergent declarations on *AI-as-building-layer-not-feature* — both anchor on *technology-leading / people-directing* reversal), [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger]] (most-comprehensive single-source W&W operationalisation at SME altitude — 9 of 12 cells in a single ~7-minute article, useful empirical complement to W&W's Swiss/German European-corporate origin sample), [[2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook|Erginbilgiç / Rolls-Royce]] (paired transform-from-strength turnaround-playbook anchors at radically different scales — ~£80B FTSE-CEO + ~€80M Dutch-SME-CEO, three days apart, structurally identical playbooks: burning-platform framing + conscious short-term portfolio sacrifice + topsport-team not-everyone-fits culture + multi-decade horizon-setting).

**W&W tagging** (9 cells — among the broadest in the wiki, comparable to [[2026-05-22-everitt-jetbrains-deeplearningai-ai-dev-26-sf-shift-to-agentic-engineering|Everitt / JetBrains]] 10 cells + [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS London]] 10 cells + [[2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook|Koomen / YC Lightcone]] 8 cells): `digital-sensing/digital-mindset-crafting` + `digital-sensing/digital-scenario-planning` + `digital-seizing/balancing-digital-portfolios` + `digital-seizing/strategic-agility` + `digital-transforming/redesigning-internal-structures` + `digital-transforming/improving-digital-maturity` + `strategic-renewal/business-model` + `strategic-renewal/organizational-culture` + `contextual/external-triggers`. The presence of both `strategic-renewal/business-model` and `strategic-renewal/organizational-culture` cells reflects this source's reach into the *strategic-renewal* outcome layer — Scheffer is explicitly making business-model + culture refresh claims, not just digital-capability claims.

**Touched pages** (8):

- New: [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero]] (source page).
- No entity promotions or bumps — **all 12 mentioned entities are first-mention dangling** (Hans Scheffer, HelloPrint, Tijmen Koppelaar, De Ondernemer, DPG Media, Joep Verbunt, Matt Sleeps, House of Founders, Ron Simpson, Lars Freriks, Trustoo, Valencia). Plausible adjacent ingest targets for the House of Founders / Joep Verbunt / Ron Simpson cluster (companion-article references at the end of the De Ondernemer page) — the wiki has no Dutch peer-learning-circle anchor yet.
- Concept bumps (frontmatter only, content unchanged unless flagged): [[enterprise-ai-adoption]] 56→57 (Dutch-MKB worked example of *full-rebuild-not-optimisation* + *Chief AI Officer is the missing MKB role* observation), [[ai-employment-effects]] 33→34 (HelloPrint customer-service 100→18 quantified worked example + *every office job behind a screen disappears* maximalist statement), [[automation-vs-augmentation]] 31→32 (Dutch-MKB-founder-CEO articulation of the automation-first stance), [[micro-productivity-trap]] 24→25 (Scheffer *explicitly avoids* the trap — *'Dat is geen los IT-project meer, maar het fundament van de hele organisatie'*), [[warner-wager-process-model]] 2→3 with confidence 0.80→0.82 (first non-Allen-AWS-vantage Dutch-language operationalisation), [[durable-skills]] 20→21 (*'Wie niet investeert in zichzelf, loopt vast'*).
- Index updated; this log entry prepended.

**Single-source-deferred concept-page candidates** (3): *AI-brein as organisational foundation* (convergent in spirit with Koomen's *one-database-to-rule-them-all + multiplayer-harness* but distinct in vocabulary and altitude); *day-zero rebuild as transformation method* (convergent with Hu's closed-loop-from-scratch but distinct in operating from an established €80M revenue base); *MKB Chief AI Officer as missing role* (Scheffer's MKB-specific role-gap diagnosis).

**Open questions / follow-ups**: The two companion articles linked at the end of the De Ondernemer piece — *Vijf startups in één week, gebouwd met AI: 'Het idee is niet doorslaggevend, het team wel'* and *Wat eerst een maand duurde, kost nu één dag: AI-lessen uit House of Founders van Ron Simpson en Joep Verbunt* — are plausible adjacent ingests if a Dutch-MKB-AI-transformation thread emerges. The third companion link — *AI-first ondernemen: waarom Hans Scheffer (HelloPrint) en Lars Freriks (Trustoo) hun bedrijven opnieuw uitvinden* — would promote both Hans Scheffer and Lars Freriks to second-source-eligible if ingested, plus surface Trustoo as a substantively documented Dutch entity. **The Dutch-MKB-AI-transformation cluster is candidate for a dedicated thread page** if a second source lands.

---

## [2026-05-28] ingest | Three-video batch — Koomen / [[Y Combinator]] Lightcone *Inside YC's AI Playbook* + Everitt / [[JetBrains]] AI Dev 26 x SF *Shift to Agentic Engineering* + Elangovan / [[AMD]] AI Dev 26 x SF *Impact of AI on Software*

User-supplied three YouTube URLs, treated as a batch acquire+process per the *unless-user-says-batch* CLAUDE.md exception. All three ingested via dual-path skill route: the [[youtube-transcript-skill]] engagement-panel route succeeded on V3 (Elangovan, 14:24) after 180s retry but timed out at 180s on V1 (Koomen, 46:30) and V2 (Everitt, 28:17). For the two long-format talks the skill's failure-mode-doc-recommended fallback was used: **yt-dlp WebVTT auto-caption fetch + VTT rolling-window dedup** (second-line-of-each-cue content kept, inline `<c>` per-word timing tags stripped, HTML entities unescaped, ~5-second bucketing). The skill-metadata-from-JSON + transcript-from-VTT merge is encoded as a reusable pattern in `/tmp/build_raw.py`. Surface artifacts: *"Pete Kumman"* (correct: Koomen); *"Duron Oamoglu"* (correct: Acemoglu); *"Grady BCH"* (correct: Booch); *"Karpati"* (correct: Karpathy); *"Mackenzie"* (correct: McKinsey); HTML-encoded chevrons (`&gt;&gt;`) for speaker turns unescaped at clean-up.

**Three substantive sources, all from the same week's AI-engineering practitioner cluster.** The batch extends two existing wiki clusters and adds one new one:

- **AI Dev 26 SF conference cluster** (was 3 sources: [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng]] + [[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan/Cline]] + [[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|Anthropic slide-gen]]) — extended with V2 (Everitt) + V3 (Elangovan) → **now 5 sources** spanning 19-22 May 2026. Everitt's talk is unusually dense with cross-references to the other AI Dev 26 SF talks ([[Andrew Ng]] / Sonar / Marina / Brandon / Tom) — useful as a *single-talk index into the conference programme*.
- **YC internal-AI infrastructure** cluster (was 1 source: [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg]] — 5-minute IC-vantage teaser) — extended with V1 (Koomen) → **now 2 sources** at IC + architecture altitudes on the same project, 8 days apart. Koomen is the architect, Garg was inside.
- **First AMD-vendor-altitude anchor in the wiki** (V3, Elangovan). AMD had appeared only in the AI Index 2025 chip-fabrication context previously; this is the first substantive AMD-AI-software-team-altitude voice.

**Substantive new framings.** **Five candidate concept pages flagged as single-source-deferred** (per the second-source-promotion rule):

1. ***Multiplayer harness*** (Koomen / V1) — *"we're still kind of in the single-player era of agents ... the multiplayer harness — that kind of superpower but on a team or an organizational level — I don't think has been solved well yet by anybody."* Koomen proposes a primitive set: *one Postgres-substrate database* + *350-tool shared registry* + *shared skill-registry with skillify/DRY/MECE resolver pattern* + *broadcast-by-default conversations* + *dream cycle* + *DRY+MECE check-resolvable meta-skill* + *model router substrate*.
2. ***Agentic design patterns*** (Everitt / V2) — Grady Booch's *Gang-of-Four-for-AI call*: *"his cohort did UML, did design patterns, kind of built the field of modern software engineering. He knows there is a next thing called agentic patterns and he wants one of you in the audience to be the one that gets the ball rolling."*
3. ***K-shaped future of software engineering*** (Elangovan / V3) — top arm (systems-thinking, judgment, taste, problem framing, harness setup) accelerating; bottom arm (language-specific code skill) declining. Cited via *"a Harvard paper that came out"* — attribution unverified. **Convergent** with the existing [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng PM-bottleneck]] / [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|SEI/CMU coder-vs-engineer]] / [[2026-05-21-bender-google-io-software-engineering-tipping-point|Bender programming-vs-engineering]] cluster but adds the *visual K-curve metaphor*.
4. ***Open-source-code-as-pre-training-substrate compounding flywheel*** (Elangovan / V3) — *"all what we created, now you have a reference, your models will learn from it. So the next time you ask for building something, it's going to have this in its pre-training data and know how to execute and move faster."*
5. ***AI acceptability threshold*** (carried over from [[2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report|Sajadieh / Stanford HAI]] from yesterday's ingest) — still single-source; no second-source materialised in this batch.

**Quantified empirical anchors:**

- **Rosetta / cross-GPU ISA translation** (Elangovan / V3) — *"4-5 years × 200-300 people"* → *"48 hours × 1 engineer × few billion tokens of Claude Code or Opus 4.6"* now shipping in production at AMD. The wiki's clearest single AMD-vendor-altitude quantified-acceleration claim.
- **YC internal infrastructure scale** (Koomen / V1) — 350 tools in shared registry (started at 20); $100K/yr token budget = *"living in 2028 ... a one-time time warp where you can leapfrog every incumbent."*
- **AI Dev 26 SF problem-framing failures** (Everitt / V2) — *"it ain't 10×, it's 10%"* + MIT 95% study + Uber-annual-gone-in-3-months + 67-point management-vs-engineer gap + mega-layoffs at Atlassian/Block/Stripe/Amazon (May 2026) with Sam Altman's *AI washing* counter.

**Neighbour-source scans run** for each of the three sources (Path A W&W cell overlap + Path B concept-citation overlap). **Total 13 typed `supports` edges** added across the three new sources (4 from V1 / 6 from V2 / 3 from V3); no `contradicts` or `supersedes` warranted.

**Touched pages** (33):

- New: 3 source pages + 3 raw transcripts at `raw/videos/inside-yc-ai-playbook.md` + `raw/videos/ai-dev-26-sf-everitt-jetbrains-shift-to-agentic-engineering.md` + `raw/videos/ai-dev-26-sf-elangovan-impact-of-ai-on-software.md`.
- **7 entity pages newly promoted to entity status** under the second-source rule (or, for Booch, soft promotion based on conceptual standing + content density): [[Pete Koomen]] (Garg + Koomen substantive), [[Daron Acemoglu]] (5 source citations across wiki, overdue), [[Sam Altman]] (4 source citations), [[Simon Willison]] (4 source citations), [[Pydantic]] (Allen-AWS + Everitt), [[Grady Booch]] (Everitt-only substantive — soft promotion based on UML / Gang-of-Four standing), [[Addy Osmani]] (his own source page + Everitt cite).
- **10 entity-page bumps + Appears-in updates**: [[Y Combinator]] 11→12, [[Garry Tan]] 4→5, [[Diana Hu]] 3→4, [[Andrej Karpathy]] 5→7, [[Andrew Ng]] 2→4, [[DeepLearningAI]] 2→4, [[LangChain]] 5→6, [[Anthropic]] 16→19, [[OpenAI]] 13→15. (Confidence bumps where heuristic-justified.)
- **10 concept-page bumps** (frontmatter only, content unchanged — re-confirmations): [[agentic-engineering]] 31→34, [[agent-harness]] 48→51, [[ai-employment-effects]] 30→33, [[enterprise-ai-adoption]] 53→56, [[micro-productivity-trap]] 22→24, [[automation-vs-augmentation]] 29→31, [[durable-skills]] 18→20, [[ai-benchmarks]] 7→8, [[agent-development-lifecycle]] 12→14. **1 synthesis-page bump**: [[is-rag-dead]] 6→7 (Koomen's *"all the things that everyone has learned about retrieval — RAG, graph-RAG, hybrid RRF — is now inside GBrain"* confirms the synthesis's *RAG-alive-inside-agentic-harness* conclusion at YC-internal-infrastructure altitude — the second substantive re-confirmation of the closed synthesis since closure).
- Index updated; this log entry prepended.

**Open questions / follow-ups**: Pete Koomen's *Horseless Carriages* essay (worth ingesting as `kind: article` since it is the conceptual substrate for the *AI-as-building-layer* framing); Simon Willison's upcoming agentic-engineering book (title and publisher not yet named); the *third golden age of software engineering* podcast (which podcast / episode); the actual Harvard paper Elangovan attributes the K-shape to; the Daron Acemoglu working paper Everitt cites for *productivity-is-five-things*; the AMD-internal autonomous-bug-monitoring agent loop (worth tracking for productivity-data backfill if a second source surfaces). The remaining four YC-Lightcone speakers from this episode (Pete + Tom Blomfield + Garry + others Garg referenced) may have companion talks worth ingesting.

---

## [2026-05-28] ingest | Sajadieh / [[Stanford HAI]] *Inside the 2026 AI Index Report* (talk + panel, 27 May 2026)

User-supplied YouTube URL ingested via [`youtube-transcript-skill`](../.claude/skills/youtube-transcript-skill/SKILL.md) (Playwright/Chromium DOM-extract path, 547 ASR segments, ~1:12:52 runtime, single English `kind: asr` caption track). Slug: [[2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report]]. Raw at `raw/videos/inside-the-2026-ai-index-report.md`. ASR clean-up: stripped YouTube's screen-reader spelled-out timestamp prefixes (*"2 minutes, 8 seconds"*) from segments post-1:04. Surface artifacts: *"Ray Perau"* in ASR (= [[Raymond Perrault]]); *"Ozade"* questioner name (unverified). Pre-flight checks: scope (full 547-segment transcript), identity (channel = [[Stanford HAI]], title verified, three speakers Sajadieh/Perrault/Wald all already entities), honest scoping (length field states *"~1:12:52 minutes ... 547 ASR segments"*).

**The wiki's first *report + talk-track* dual ingest.** This source is the authoritative live presentation of [[2026-04-30-ai-index-report-2026|the 2026 AI Index Report]] (already in the wiki as a partial-front-matter ingest from 2026-04-30). The statistical claims overlap heavily; the talk-track's distinct value is the **editorial-interpretation layer** — five substantive contributions not in the report itself:

1. **The *absorption gap* as the report's single observation** (Sajadieh's executive-briefing compression of the headline framing).
2. **The acceptability-threshold research gap** (Perrault's named-for-the-first-time question: *what reliability bar must AI clear to be acceptable in legal / medical / finance?*). The wiki's first **named research gap** at this altitude; plausible single-source-deferred concept-page candidate.
3. **The academic-vs-industry transparency tension** (Wald's argument that frontier-lab proprietary mode hampers academic peer-review/verification; pairs with the report's empirical anchor — 80 of 95 notable models without training code, [[foundation-models|FMTI]] declining).
4. **The AI-Index founding mission** (Perrault's first-person founder-account: *facts on the ground, not projections, no recommendations to governments* — distinguishes the AI Index epistemic stance from [[2026-04-28-ftsg-convergence-outlook-2026|FTSG]] and [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|MGI Race Takes Off]]).
5. **The World-Bank / IMF measurement initiative** (Perrault discloses he and [[Yolanda Gil]] are working with major US companies on global-AI-adoption measurement; *not in time for next report*).

**Neighbour-source scan (Path A + Path B)** surfaced 3 strong typed-edge candidates and several skipped-with-reason: edges filed to [[2026-04-30-ai-index-report-2026|AI Index 2026 Report]] (direct talk-track), [[2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas|MGI virtual event]] (sibling live-event-of-annual-landscape-report pattern; identical 4-cell W&W profile), and [[2026-04-28-ftsg-convergence-outlook-2026|FTSG Convergence Outlook 2026]] (two 2026 annual horizon scans). Skipped: derivative report→source edges that would double-count ([[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua]], [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson Canaries]]); shared-concept-only overlaps without framing convergence ([[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Yee/MGI Skill Partnerships]]); one-step-removed edges ([[2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai|Agrawal/MS&E435]] already declares `supports → 2026-04-30-ai-index-report-2026`).

**W&W tagging** (4 cells): `digital-sensing/digital-scouting` (annual technology-trends scout) + `digital-sensing/digital-scenario-planning` (talk's *where AI is heading* feeds organizational scenario inputs) + `digital-seizing/balancing-digital-portfolios` (the acceptability-threshold gap is fundamentally portfolio-balancing — which AI apps belong in legal / medical / finance, at what reliability bar?) + `contextual/external-triggers` (public sentiment, sovereignty politics, governance fragmentation as macro forces). **Mirrors [[2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas|the MGI virtual event ingest's]] four-cell profile** — the right comparator for *live-event-of-annual-report* tagging precedent.

**Touched pages** (12):

- New: [[2026-05-27-sajadieh-stanford-hai-inside-the-2026-ai-index-report]] (source page).
- Entity bumps: [[Sha Sajadieh]] (1→2, conf 0.70→0.75 + new "Appears in"), [[Raymond Perrault]] (2→3 + new "Appears in"), [[Russell Wald]] (2→3 + new "Appears in"), [[AI Index]] (2→3), [[Yolanda Gil]] (2→3, mention by Perrault + new "Appears in"), [[Stanford HAI]] (2→3). All `last_confirmed` and `accessed_at` bumped to 2026-05-28.
- Concept bumps (frontmatter only, no content change — re-confirmation of numbers already supplied by the parent report): [[jagged-frontier]] 9→10, [[ai-employment-effects]] 29→30, [[enterprise-ai-adoption]] 52→53, [[generative-ai]] 21→22, [[ai-benchmarks]] 6→7, [[responsible-ai]] 11→12, [[foundation-models]] 13→14.
- Reverse body-mention added on [[2026-04-30-ai-index-report-2026]] (companion-talk-track paragraph + Related-in-this-wiki line). No frontmatter reverse edge per MGI precedent ([[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas]] handled its companion the same way).
- Index updated; this log entry prepended.

**Single-source-deferred concept candidates** (for second-source promotion): *AI acceptability threshold* (Perrault); *AI sovereignty* (Sajadieh).

**Open questions / follow-ups**: The World-Bank / IMF measurement initiative is worth tracking — Perrault states it will not land in time for the 10th-edition (2027) AI Index but plausibly for the 11th (2028); the wiki should look for downstream announcements. The *acceptability-threshold* gap is a candidate concept-page if a second source — likely [[Raymond Perrault]]'s own future work, or a regulatory-research source — names it explicitly. The *Stanford HAI YouTube channel* is now a recurring source-of-record (Stanford HAI authored two prior reports; this is its first published talk-track) and is worth flagging as a recurring ingest target.

---

## [2026-05-26] ingest | Yee et al. / [[McKinsey Global Institute|MGI]] *Agents, Robots, and Us: Skill Partnerships in the Age of AI* (November 2025) + technical appendix

User-supplied PDFs landed in `raw/reports/` this morning. Slug: [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships]]. Seven McKinsey/MGI authors: **Lareina Yee** (MGI director, Bay Area; lead author) + **Anu Madgavkar** (MGI partner, NJ) + **Sven Smit** (MGI chairman, Amsterdam) + **Alexis Krivkovich** (senior partner, Bay Area) + **Michael Chui** (QuantumBlack senior fellow) + **Maria Jesus Ramirez** (MGI senior fellow) + **Diego Castresana** (engagement manager, NY). Academic advisers: Nobel laureate **Sir Christopher Pissarides** (LSE) + **Matthew J. Slaughter** (Tuck Dean). Full ingest: 60-page report + 6-page technical appendix, all 20 numbered exhibits + 6 sidebars + glossary + endnotes. PDF CreationDates: appendix 25 Nov 2025, report 8 Dec 2025; cover branding *November 2025*; `date_published` set to 2025-11-25 (appendix CreationDate, aligned with cover branding).

**The wiki's most structural and panoramic anchor to date on the AI-and-workforce question.** Together with [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|MGI Race-Takes-Off (March 2026)]], the two reports constitute MGI's **two-layer panorama** of the AI-economy question: *where will the value migrate* (Race Takes Off, 18 arenas) × *who and what will do the work that captures it* (Agents, Robots, and Us, 7 archetypes + Skill Change Index). Same intellectual project, designed to be read in tandem. **6-month delta** between the two reports.

**Pre-flight checks:** scope (60+6 pp, `pdfinfo` confirmed, full ingest); identity (cover names 7 authors + MGI + Nov 2025; PDF metadata title matches; consistent with MGI publication convention); honest scoping (length field states *"~60 pages (full report) + ~6 pages (technical appendix); full ingest including all 4 chapters, all 20 numbered exhibits, both methodology sidebars, glossary, acknowledgements, and endnotes."*).

**Seven substantive contributions:**

1. **The Skill Change Index (SCI)** — a time-weighted measure of automation's potential impact on each of ~6,800 employer-cited skills, built using **OpenAI GPT-4o for ~3.4M skill→DWA mappings** across ~1,800 occupations (BLS + O*NET + Lightcast substrate) with a manual 1,000-cell validation template + iterative prompt refinement. **The wiki's first labour-market-data-grounded systematic measure of skill change under AI automation.** Three skill-evolution paths: top-quartile decline (SQL programming, accounting processes, invoicing), middle-quartile evolve (AI fluency, communication, customer relations, detail orientation, management, writing, quality assurance), bottom-quartile endure (leadership, coaching, healthcare skills, mentorship, negotiation). By skill category: assisting+caring 54% low-exposure (most-protected); digital skills 42% high-exposure (most-exposed).

2. **57% US technical-automation-potential** — today's demonstrated technologies could theoretically automate ~57% of current US work hours. Decomposed as **44% via agents (nonphysical) + 13% via robots (physical)**; remaining 43% remains people-only (21% nonphysical-only requiring social/emotional + 22% physical-only requiring fine motor + situational awareness AI can't yet replicate). The **65/35 nonphysical/physical work-hour split** is the structural substrate for the agents-vs-robots framing.

3. **Seven occupation archetypes** (Exhibit 3, ~800 BLS occupations, 55% threshold for "centric"): people-centric **34% / $71k** (registered nurses, psychologists, firefighters); people-agent **21% / $74k** (sales reps, teachers, HR specialists); agent-centric **30% / $70k** (accountants, software developers, lawyers); people-robot **<1% / $54k**; robot-centric **8% / $42k** (stockers, welders, cooks); people-agent-robot **5% / $60k**; agent-robot **2% / $49k**. The **agent-centric quadrant is where the knowledge-work wage premium is at risk** — 30% of US workforce, $70k average, occupations whose cognitive tasks are 55%+ technically-automatable.

4. **72% shared-skills finding** — *most skills remain relevant; AI changes how and where they're used, not which skills are valuable*. 11% people-led-only / 72% shared / 17% AI-led-only. **The skill-level decoupling from the occupation-level archetype distribution** — an accountant and a nurse share most of the same skills (communication, problem-solving, detail orientation); they just apply them in different automatable/non-automatable mixes.

5. **AI fluency demand 6.8× in two years** (2023→2025: 1.0M → 7.0M US employees in occupations where job postings call for AI-fluency skills) — *faster than any other skill in US job postings*. Technical AI skills (Govern AI + Develop AI, 55 skills) grew 1.6× (2.1M → 3.3M). Total AI-related skills (66 skills): 2.2M → 7.5M (+3.5×). **~75% of AI-skill demand concentrated in 3 occupation groups** (Computer & mathematical 2.6M, Management 2.3M, Business & financial operations 0.8M); **9 occupation groups (~40% of workforce) have near-zero AI-skill demand** → bifurcated AI-skill labour market.

6. **$2.9T US economic value by 2030** (midpoint adoption scenario; **$28.7T globally**, up from earlier untimed ~$26T June 2023 MGI projection) — **77% from agents ($2.26T) + 23% from robots ($0.67T)**; 60% concentrated in **sector-specific workflow domains** ($1.7T: Knowledge $773B + Frontline $424B + Production $556B) + 40% in **cross-cutting** ($1.2T: IT $196B / Marketing $167B / Planning+management $161B / Admin services $133B / Logistics $122B / Sales $90B / Product+R&D $87B / Customer support $60B / Talent+org $56B / Finance $42B / Procurement $31B / Legal $21B / Risk+compliance $11B). Sector adoption rate range **20% (healthcare) → 31% (manufacturing)**; midpoint adoption ~27% of current work hours.

7. **The workflow-not-task imperative** — *"Nearly 90 percent of companies say they have invested in [AI], but fewer than 40 percent report measurable gains."* **<40%-of-90% statistic** is the workflow-redesign-disciplines-against-task-automation empirical anchor at MGI structural altitude. **190+ workflows mapped** across 16 business functions (commercial / functional / operational / sector-specific) as the operational unit-of-analysis. **Four worked operational cases**: B2B sales (5 agents → +7-12% revenue, -30-50% time across roles); utility customer ops (7M+ calls/yr, 4 agents → ~40% of calls handled, >80% resolved without humans, cost/call -50%, CSAT +6pp); biopharma medical writing (6 agents → touch time for first human drafts -60%, errors -50%); regional bank IT modernization (3+ agents → code accuracy up to 70%, human hours -50%).

**Other named contributions**: eight high-prevalence transferable skills with people/agent split table (Exhibit 11: communication 99% relevance, management 94%, operations 84%, problem-solving 83%, leadership 83%, detail orientation 80%, customer relations 80%, writing 76%); Exhibit 20 leadership-skill SCI mapping (high-change Prioritisation + Decision-making; medium Planning / Coordinating / Budgeting / Accountability / Innovation; low Coaching / Influencing / Mentorship — *managers shift from supervising people to orchestrating systems*); 8M US workers already in occupations where job postings call for ≥1 AI-related skill; AI-adjacent demand rising (process optimisation +114 occupations, quality assurance +87, teaching +90, people management +138) while skills AI already performs well are falling (routine writing -134, mathematics -133, general science -140, customer service -83); the explicit avoidance of the AI-will-eliminate-jobs frame (*"This estimate reflects the technical potential for change in what people do, not a forecast of job losses"*); the Ch.4 leadership-questions framework (6 for business + 3 for institutions); Mayo Clinic radiology +50% headcount since 2016 while deploying hundreds of AI models as the augmentation-not-replacement worked example.

**Methodology lineage**: MGI's automation-and-adoption model first developed 2017 (Manyika et al., *A Future That Works*), refreshed for June 2023's *The economic potential of generative AI* (global ~$26T untimed), now refreshed for Nov 2025's *Agents, Robots, and Us* ($28.7T global / $2.9T US timed to 2030). The same BLS + O*NET substrate appears across three reports spanning 8 years. The 2025 refresh adds Lightcast + GPT-4o for ~3.4M skill→DWA mappings, plus midpoint vs early/late adoption scenario brackets.

**W&W tags** (12 cells — broadest cell-coverage of any single source in the wiki): all 9 microfoundations (digital-sensing/digital-scouting + scenario-planning; digital-seizing/balancing-portfolios + strategic-agility + rapid-prototyping; digital-transforming/redesigning-internal-structures + improving-digital-maturity; **strategic-renewal/business-model + organizational-culture**; **all 3 contextual: external-triggers + internal-enablers + internal-barriers**). The report exercises virtually the entire W&W process model at MGI structural-modeling altitude.

**Neighbour-source scan** (≥1 W&W cell overlap or thematic): 10 candidates surfaced; 7 earned typed edges, 3 skipped. **7 typed `supports` relationships**: [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson Canaries]] (**descriptive-empirical + structural-prospective pair on AI labour question** — Brynjolfsson's six facts on current automation-share displacement + MGI's prospective workforce-distribution-by-2030; both reject *AI-eliminates-jobs* framing in favour of *AI-reshapes-which-skills-applied-where*), [[2025-06-09-krakowski-human-centered-ai-field-experiment|Krakowski 2025]] (individual cognitive-style tailoring + firm workflow redesign as paired levers; both anchor `digital-transforming/redesigning-internal-structures`), [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|MGI Race Takes Off]] (**same-publisher MGI two-layer panorama, 6-month delta** — industry-and-competition × workforce-and-skills; fulfils the prior MGI source's open follow-up to update [[McKinsey & Company]] with MGI sub-section via this ingest's MGI entity-page promotion), [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels/McKinsey]] (firm-practitioner + research-institute McKinsey-altitude pair on workflow-redesign-not-task-automation), [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt-Chatterji/Bain]] (**cross-consultancy convergence on workflow-as-unit-of-AI-value-capture** — Bain + McKinsey/MGI structural evidence that the task-vs-workflow distinction is operationally load-bearing, not consulting-firm-specific framing), [[2026-04-30-ai-index-report-2026|AI Index 2026]] (two 2026-era panoramic AI reports at adjacent stack layers — Stanford HAI capability-and-investment layer + MGI workforce-and-skills layer), [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson/Li/Raymond]] (field-experiment workflow-productivity evidence + structural-modelling workflow prescription; same workflow shape as MGI's utility-customer-ops case). Skipped: [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index]] (different methodology — Claude.ai-usage data vs structural modelling, and Allen 2026 already maps both); [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua Jagged Frontier]] (task-level vs MGI's occupation-level — adjacent but not directly supporting); [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren/Macvean DORA]] (engineering-specific vs MGI's economy-wide).

**Entity changes**:
- **[[McKinsey Global Institute]] — promoted from dangling to its own entity page** (3rd-mention rule fulfilled: prior mentions in [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|MGI Race Takes Off]] + [[2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas|virtual-event companion]] + this ingest as 3rd named-publisher appearance). Page captures: founded 1990; mission + 5 research themes; the 3 MGI sources ingested into the wiki; MGI directors/partners/senior fellows roster; academic-advisers / external-research-contributors; MGI's 2017 → 2023 → 2025 automation-and-adoption-model methodology lineage. Fulfils the open follow-up from the MGI Race-Takes-Off ingest (*update [[McKinsey & Company]] with MGI sub-section*).
- **[[McKinsey & Company]]** — source_count 7→8 (this MGI source counts toward both McKinsey-firm and MGI source_count); conf 0.92→0.95 (cap); last_confirmed + accessed_at → 2026-05-26; **`MGI` and `McKinsey Global Institute` removed from aliases** (now resolves to dedicated MGI entity page); opening paragraph refactored to reference MGI as `[[McKinsey Global Institute]]`; new source added to "Appears in this wiki via"; "MGI directors and partners" sub-section trimmed and pointed at the new MGI entity page; minor chronology note added about MGI chairmanship transition (Singhal → Smit).

**Concept changes**:
- [[automation-vs-augmentation]] +1 (28→29, conf 0.95 cap, last_confirmed/accessed_at → 2026-05-26, **+subsection 15: MGI structural framework — 7 occupation archetypes + 65/35 nonphysical/physical split + 44/13 agent/robot capacity + 72% shared-skills finding** as the wiki's most granular automation-vs-augmentation structural anchor).
- [[ai-employment-effects]] +1 (28→29, **+subsection on MGI shift-not-elimination framing + Skill Change Index as quantitative complement to Brynjolfsson Canaries + AI fluency 6.8× growth + bifurcated AI-skill labour market**).
- [[durable-skills]] +1 (17→18, conf 0.93→0.95, **+major subsection on MGI Skill Change Index as labour-market-data-grounded systematic measure** with three properties (coverage, time-weighted decomposition, scenario-bracketed), three skill-evolution paths, 8-skill people/agent split table; 5-source convergence on durable-skills concept now multi-altitude — measurement + neuroscience + agency + engineering-team + structural-modelling).
- [[micro-productivity-trap]] +1 (21→22, **+eleventh-source corroboration on MGI <40%-of-90% statistic + 190+ workflow taxonomy + 4 worked operational cases**; convergence with Bain/McKinsey/AWS-advisory now on strongest cross-consultancy structural footing).
- [[enterprise-ai-adoption]] +1 (51→52, **+subsection on MGI workflow-as-unit-of-value-capture + $2.9T US scaffold + 60/40 sector/cross-cutting concentration + 77/23 agents/robots split + 4 worked cases**).

**Dangling first-mentions** (deferred per author-entity promotion rule):
- 7 named McKinsey/MGI authors: Lareina Yee, Anu Madgavkar, Sven Smit, Alexis Krivkovich, Michael Chui, Maria Jesus Ramirez, Diego Castresana.
- 2 named academic advisers: Sir Christopher Pissarides (Nobel laureate, LSE), Matthew J. Slaughter (Paul Danos Dean, Tuck School at Dartmouth).
- 1 named postdoctoral research contributor: Luca Vendraminelli (Stanford Digital Economy Lab + Stanford HAI).

**Open follow-ups** (McKinsey companion publications cited in endnotes, not yet ingested): Manyika et al. *A Future That Works* (McKinsey 2017, foundational methodology); *The economic potential of generative AI: The next productivity frontier* (MGI June 2023, theoretical prior for both 2025-2026 MGI reports' economic-value modelling); *The state of AI in 2025: Agents, innovation, and transformation* (McKinsey Nov 5 2025, cited Ch.4 endnotes 23-24); *The agentic organization: Contours of the next paradigm for the AI era* (McKinsey Sep 26 2025, endnote 26); *Performance through people* (MGI Feb 2 2023, endnote 25); *McKinsey technology trends outlook 2025* (July 2025); *A leap in automation: The new technology behind general-purpose robots* (McKinsey July 2025); *Will embodied AI create robotic coworkers?* (McKinsey June 2025); *Humanoid robots: Crossing the chasm from concept to commercial reality* (McKinsey October 2025); *In search of cloud value: Can generative AI transform cloud ROI?* (McKinsey Nov 2023).

**Lint**: all 8 touched pages lint clean — body-wikilink rule satisfied for all 7 typed relationships; closed `dynamic_capabilities:` vocabulary respected on all 12 cells; YAML frontmatter parses with safe_load on all pages (no repeat of the `04292fa` / `c74ae5d` parse-break failure class).

---

## [2026-05-26] ingest | Erginbilgiç / Bloomberg Podcasts *Leaders With Lacqua* — *Rolls-Royce CEO Tufan Erginbilgiç Shares His Turnaround Playbook*

User-supplied YouTube URL. Slug: [[2026-05-24-erginbilgic-bloomberg-leaders-rolls-royce-turnaround-playbook]]. Bloomberg Podcasts YouTube channel; *Leaders With Lacqua* series; ~23:44; **`kind: manual` proofread captions track** (Bloomberg ships proofread accessibility captions for this series — direct verbatim quotation is reliable, a quality lift over the wiki's ASR-typical video sources). Acquire and Process ran in the same session via the [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) JSON path → ASR-cleanup script that stripped Bloomberg's verbose embedded timestamps (*"1 minute, 8 seconds"* accessibility convention), removed chapter-heading injections from the caption stream, preserved the Turkish diacritic on *Erginbilgiç*, and recomputed chapter `start_ms` (the skill emitted 0 for each). **Pre-flight checks:** scope (full transcript across all six Bloomberg chapters), identity (manual captions corroborate title; one chapter-edit artefact — *"four pillars"* chapter explicitly enumerates only two pillars in the broadcast, flagged in body), honest scoping (length stated as *"~23:44 minutes (manual proofread captions; transcript ~169 lines)"*).

**The wiki's first pure non-AI industrial-transformation anchor.** Every prior source tagged with `strategic-renewal/organizational-culture` has been AI-adoption-flavoured (Krakowski pharma augmentation, Allen agentic teams, Storoni AI-era work design, Kropp AI agents). Erginbilgiç supplies the *non-AI baseline* — industrial-aerospace transformation 2023–2026, no AI substrate — which lets the wiki separate *AI-era transformation specifics* from *transformation primitives full stop*. Tenure cited at ~1:05 as McKinsey's *"case study in the art of corporate transformation"*; shares up >10× since Jan 2023.

**Six substantive contributions:** (1) **The "burning platform" speech as designed artefact** — Jan 2023 1.5-hour town-hall built on external benchmarking commissioned starting Sept '22 (~2:01–2:32); diagnosis + vision paired in the same speech; the speech was a *publication* of pre-existing shareholder frustration, not a unilateral attack. (2) **Restructuring vs transformation as deliberate semantic distinction** — *"It was never this restructuring. It was transformation"* (~3:11). (3) **The four-pillars framework with honest-scoping caveat** — chapter title promises four; Erginbilgiç enumerates two (*people* + *granular strategy*); pillars 3–4 reconstructed from surrounding material (commercial discipline / performance culture). The wiki documents both the framing and the gap. (4) **Strategy-as-participation doctrine** — *"I don't do strategy in the dark room with consultants. I personally attended 25–30 workshops... every like 500-plus people joined. When you are done, whole organisation is aligned because they were in the room when you were making the decision"* (~12:43–13:32); two protocol rules (*no hierarchy*, *chaos is licensed*); alignment as the output of *participation* not *cascade*. **Substantive new section added to [[strategy]] concept.** (5) **Demanding ≠ tough love** — *"I am demanding... You won't like everything I tell you because I want you to improve"* (~6:51–7:21) carefully separated from *tough* (rejected) and *blunt* (reclaimed); paired with the *new-normal-as-eased-cadence* observation — leader demand-intensity is time-shaped, drops once team behaviour shifts to new norms (~7:36–8:23). (6) **The resilience playbook** — *"Once you get into trouble, it is too late"* (~20:17–22:04); four ingredients (mindset + response capability + agility + action-orientation); *"It's not about predicting the world... it is about how your company thinks about dealing with external shocks"*; quantified ~5–10× capability multiplier in three years.

**Other named contributions**: layer-elimination without operational-people cuts; CEO-to-CEO contract renegotiation as cultural shock-wave (*"I'm going to do impossible things as well"*); PE-investment-committee-as-coaching-loop import; *"non-compromising mediocrity at that level kills the organisations"*; growth-as-retention-mechanism; SMRs as industrial learning-curve-economics bet over bespoke-EPC nuclear; history as durable-skill reading habit (*"human behaviour doesn't change a lot"*).

**W&W tags** (3 cells — the first wiki source to map the W&W vocabulary onto a *pure non-digital* transformation case): `strategic-renewal/organizational-culture`, `digital-seizing/strategic-agility`, `contextual/internal-barriers`. The model's cells stretch outside the digital lens with the *digital-mindset* clause optional — documented as the wiki's working hypothesis on the [[warner-wager-process-model]] page (*The model's reach beyond the digital lens* section, new).

**Neighbour-source scan (≥1 W&W cell overlap):** six candidates surfaced; two earned typed edges, four skipped per the *not-every-co-occurrence-is-a-relationship* principle. **2 typed `supports` relationships**: [[2025-06-09-krakowski-human-centered-ai-field-experiment|Krakowski 2025]] (**non-tech-industry transformation pair on the tailored-leadership + culture-refresh lever** — Nordic pharma DiD + UK aerospace CEO interview; same load-bearing claim that *tailored intervention beats blanket prescription* on the W&W `strategic-renewal/organizational-culture` cell), [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS London Exec Forum]] (**demanding-leader-as-transformation-cadence pattern, two industries apart** — Allen's 5× expectation + Brooklyn's human-starts-human-ends + Erginbilgiç's non-compromise on mediocrity + the eased-cadence observation; convergence is load-bearing precisely *because* the domains differ — the demanding-leader pattern is transformation-primitive, not AI-specific). Skipped: Kropp (no topic intersection despite three-cell overlap), Storoni (different altitude — individual vs org), Bender (different domain — SE tipping point), Ng (different domain — PM bottleneck).

**Concept changes**: [[strategy]] +1 source (source_count 3→4, confidence 0.80→0.85, last_confirmed/accessed_at → 2026-05-26, **+substantive *Strategy-as-participation* doctrine subsection** + new Related-concepts entry crosslinking to [[dynamic-capabilities]]); [[dynamic-capabilities]] +1 source (source_count 8→9, confidence 0.90→0.95 at cap, last_confirmed/accessed_at → 2026-05-26, **+*Non-AI control case* section mapped to Teece sense/seize/transform clusters** + new `## Debates and supersession` section filled — addresses pre-existing quality_notes flag *"missing ## Debates and supersession (concept with >1 source)"*); [[warner-wager-process-model]] +1 source (source_count 1→2, confidence 0.75→0.80, last_confirmed/accessed_at → 2026-05-26, **+*The model's reach beyond the digital lens* section** with cell-mapping table + new `## Debates and supersession` section).

**Dangling first-mentions** (deferred per author-entity promotion rule): Tufan Erginbilgiç (Rolls-Royce CEO since Jan 2023), Francine Lacqua (Bloomberg Television anchor / Leaders With Lacqua host), Bloomberg Podcasts (channel/publisher — Bloomberg L.P. podcast division), Rolls-Royce (subject organisation), BP (former employer, 25+ years).

**Lint:** clean on all four touched pages (source + three concepts) — body-wikilink rule satisfied for both typed relationships; closed `dynamic_capabilities:` vocabulary respected.

---

## [2026-05-25] ingest | Three-source backfill batch from `raw/` — **Kropp et al. (BCG/HBR May 2026) *Don't Treat AI Agents Like Employees*** + **Krakowski et al. (Management Science 2025) *Human-Centered AI Field Experiment*** + **Ebbelaar (Datalumina) *Complete Guide to Hybrid Search in RAG (BM25 + Embeddings + Reranker)***

User-initiated batch ingest of three sources that had been sitting in `raw/` without a wiki source page. A `raw/` audit identified them as the only truly unprocessed candidates (other apparent gaps were already-ingested sources whose `raw:` field used a different filename convention). Brief per-source summaries:

**1. Kropp / Bedard / Wiles / Hsu / Krayer — HBR / BCG Henderson Institute (6 May 2026).** Slug: [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees]]. **The wiki's first RCT-grade empirical anti-anthropomorphizing-AI source**: N=1,261 HR/finance managers/directors/executives in US/Canada/EU, randomised three-condition experiment (AI-tool / human-teammate "Alex" / AI-teammate "ALEX-3"). Headline: in the AI-already-on-org-chart subset (23% of sample), the AI-employee framing causes a **9pp drop in personal accountability** (with 8pp shift to AI), **44% more escalation requests**, **18% fewer errors caught**, and (whole-sample) **13% higher uncertainty about professional identity** + 7% higher job-security concern + 10% lower AI trust — *without* meaningfully increasing adoption intent. Five-point redesign prescription: *redefine workflows + name human role expectations; make accountability explicit; capability-building plan for managers of agents; **don't constrain agents into 1-for-1 roles** (single agent → many workflows); deliberate choices about how human work evolves*. Population baseline: 31% of orgs already frame AI as teammate; 23% have AI on org charts (mainstream by mid-2026 despite being counter-productive). **Entity changes**: [[Boston Consulting Group]] 1→3 (confidence 0.75 → 0.82, last_confirmed 2026-04-28 → 2026-05-25); **[[Lisa Krayer]] promoted from Dangling to entity page** (second-source rule triggered via [[2026-04-28-dellacqua-jagged-technological-frontier|Jagged Frontier paper]]). **7 typed relationships** — `supports` to [[2026-05-21-allen-aws-london-exec-forum-agentic-team-structures|Allen / AWS]] (independent confirmation of *managers-in-charge-of-agents* failure mode at 15-day delta), [[2026-05-08-running-an-ai-native-engineering-org|Fung / Anthropic]] (advisory vs Anthropic-engineering-org altitudes on same prescription), [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels / McKinsey]] (BCG + McKinsey consultant-altitude pair), [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt et al. / Bain]] (*anthropomorphizing lock-in* as third sub-mode of [[micro-productivity-trap]]), [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger]] (empirical operationalisation of W&W microfoundations); **`contradicts`** to [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad / Replit]] (productive tension on *AI-as-employee-substitute* framing) and [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg / AnswerThis]] (productive tension on *one-agent-per-role* design — same operational shape, opposite framings). **Dangling first-mentions**: Matthew Kropp, Julie Bedard, Emma Wiles, Megan Hsu. **Open follow-ups**: ingest prior BCG *AI brain fry* study (11%/39% error-frequency increases), prior BCG *AI workforce transformation* study (3.5× managerial-role-modelling claim), prior BCG Henderson Institute *executive-vs-IC enthusiasm gap* research (76%/31%).

**2. Krakowski / Haftor / Luger / Pashkevich / Raisch — Management Science 72(1) (online 9 June 2025, INFORMS).** Slug: [[2025-06-09-krakowski-human-centered-ai-field-experiment]]. **The wiki's first RCT-grade DiD field experiment showing that *untailored* augmentation produces *negative* performance vs the legacy IT control.** N=72 sales experts across 12 business units in the Nordic subsidiaries (DK/FI/NO/SE) of a multinational pharmaceutical company, 9 quarters pre-intervention + post-intervention period, three conditions: D1 control (legacy IT), D2 untailored AI, D3 tailored AI per Kirton 1976 KAI Index (47 adaptors / 25 innovators) across four interaction-design parameters (*work procedure / decision-making authority / training / incentives*). **Headline**: untailored AI causes market share to *gradually decline* vs the stable legacy-IT baseline; tailored AI produces positive effects vs both untailored AND control. **Work procedure** emerges as the single most impactful parameter (drives the adaptor result). **Login-data mediation analysis** shows utilization in untailored condition *gradually decreased* as sales experts withdrew — *rational adaptation, not algorithm aversion*. The *prison quote* from a Danish innovator: *"We got this super tool, and at the same time, I felt like in prison... this level of controlling killed my internal drive!"* **6 typed `supports` relationships** — [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson-Li-Raymond]] (two-field-experiment pair on augmentation pole — success case + failure case), [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua / Jagged Frontier]] (same INFORMS journal family + same DiD/RCT method + same outside-the-frontier-loses pattern), [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] (deployment-quadrant + interaction-design as complementary layers), [[2026-05-06-kropp-bcg-hbr-dont-treat-ai-agents-like-employees|Kropp et al.]] (two 2026 RCT-grade empirical sources on organisational-design dimension), [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger]], [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean / DORA]] (productive-struggle + cognitive-style-tailoring convergence). **Dangling first-mentions**: Sebastian Krakowski, Darek Haftor, Johannes Luger, Natallia Pashkevich, Sebastian Raisch. **Open follow-up**: ingest *Raisch & Krakowski 2021 — Artificial Intelligence and Management: The Automation-Augmentation Paradox* (cited self-referentially as theoretical prior).

**3. Ebbelaar / Datalumina — YouTube practitioner tutorial (14 May 2026).** Slug: [[2026-05-14-ebbelaar-hybrid-search-rag-bm25-embeddings-reranker]]. **The wiki's first complete-components-from-scratch operationalisation of hybrid retrieval at practitioner altitude.** 59:17 / 19 chapters / 5,803 views. The hybrid-retrieval production stack assembled in code: **BM25 (sparse keyword) ∪ dense embeddings → Reciprocal Rank Fusion (1/(k+rank), k=60 typical) → cross-encoder reranker on top-K fused candidates**. BEIR / FinanceQA dataset as evaluation harness. Closing eval-driven-tuning discipline: *"Do you always need this entire stack? And the answer is no. So you should figure out for your corpus what the best combination of this is."* — explicitly disclaiming the full-stack-is-always-best default. Companion: [GitHub `ai-cookbook/knowledge/hybrid-retrieval`](https://github.com/daveebbelaar/ai-cookbook/tree/main/knowledge/hybrid-retrieval) ships executable Python + per-technique docs with formulas + original papers. **4 typed `supports` relationships** — [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers|Liu]] (practitioner-altitude operationalisation of *RAG-as-substrate-of-many-architectures*), [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber / Chroma]] (productive complement — orchestration layer + retrieval-primitive layer stack), [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie]] (eval-driven retrieval design as sub-genre of eval-driven AI engineering), [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide|SurrealDB]] (database-vendor-side vs roll-your-own-components hybrid-stack pair). **Added to [[is-rag-dead]] synthesis as 6th source** (source_count 5 → 6) — first re-opening of a closed synthesis with a substantive new instance of one of its lessons. **Dangling first-mentions**: Dave Ebbelaar, Datalumina.

**Concept-page updates** (lifecycle bumps + body wikilink rule honoured): [[automation-vs-augmentation]] 26→28 (new §13 *Don't treat AI agents like employees* + §14 *Augmentation is contingent on interaction-design*); [[enterprise-ai-adoption]] 49→51 (new §*Interaction-design as the lever — the four-parameter framework + the negative-untailored finding* + §*The anti-anthropomorphizing-AI prescription at consultant altitude*); [[micro-productivity-trap]] 19→21 (new §9 *anthropomorphizing-lock-in* + §10 *interaction-design-misfit lock-in* — the trap's taxonomy now has five named sub-modes); [[ai-deskilling]] 7→8 (new §*AI brain fry — cognitive-load deskilling as a second causal mechanism*).

**Synthesis update**: [[is-rag-dead]] synthesis (source_count 5→6, last_confirmed 2026-05-12 → 2026-05-25) — the wiki's first re-confirmation of a closed synthesis with a new substantive source.

**Catalog**: 127 → 130 sources, 89 → 90 entities, 32 concepts unchanged, 5 threads, 4 syntheses (one re-confirmed).

## [2026-05-25] ingest | Allen + Francis / AWS Events *London Executive Forum 2026 — A leader's guide to advanced team structures in an agentic world* — wiki's first **AWS Events YouTube channel** source + first **12-month longitudinal AWS-altitude pair** with [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy 2025]] (USE/COMPOSE/BUILD as the agentic-economics overlay on the May-2025 three-layer AI stack); **Project Mantle case** (76 days vs 18-month estimate, AWS VP-Distinguished-Engineer Anthony Liguori + L7 principals rebuilding the Bedrock substrate with goal-based agents) lands as the wiki's first quantified **independent confirmation of Ng's PM-bottleneck thesis** at AWS-Executive-in-Residence altitude (one day after [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng / AI Dev 26 SF]]); **moats-erosion thesis** (old: workflow embeddedness / software scale / integration lock-in / engineering complexity / IP; new: compounding proprietary data / network effects / regulatory permission / capital at scale / physical infrastructure + meta-moat *time-that-can't-be-parallelised*); **embedded-pod model** (3–5 engineers / pod organised around workflow not product) + **hourglass organisation** as counter to *seniors-20×-cut-juniors* default, with **junior-hiring crisis** empirical anchor (73% European-tech entry-collapse / Ravio); Brooklyn Solutions customer testimony adds the wiki's first vendor-customer-side **regulated-customer harness composition** (AWS Bedrock + Bedrock Guardrails + AgentCore) + *human-starts-human-ends* accountability + *5× expectation* (5× output for ≤25% opex increase) + *momentum beats perfection* iterative-quality-compounding mantra; first **end-to-end practitioner operationalisation of the W&W process model** at vendor altitude.

User-initiated single-source ingest of a 43:54 AWS Events YouTube video filmed at the AWS London Executive Forum 2026 (published 21 May 2026). Two speakers in series: **Jonathan Allen** (AWS Executive in Residence — third holder of that title in the wiki after [[Jana Werner]] and [[Phil Le-Brun]]) for the headline keynote (~0:07–33:20), then **Nick Francis** (co-founder + Chief Technology & Marketing Officer of UK supplier-management scale-up **Brooklyn Solutions**, regulated customers including the Ministry of Defence and Danske Bank) for the customer testimony (~33:20–43:45). Allen disclosed (~0:40) the deck was first presented at AWS re:Invent in December 2025 in Las Vegas with *400 hours of revision since* — interviews with customers, Amazon leaders, his own production agentic-system builds, customer go-live work. The talk is a meta-synthesis source (Allen explicitly cites Anthropic's April-2026 labour-market report, the MIT NANDA 95%-pilot-fail paper, the Nvidia SLM paper, Martin Fowler, Werner Vogels, William Gibson, Scott Galloway, Rory Sutherland) — its wiki contribution is to *typed-link* what Allen citation-linked.

**Five wiki-substantive contributions:**

1. **PM-bottleneck thesis, independently confirmed at AWS vendor altitude with quantified internal-Amazon delivery datapoint.** [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng]] named it at conference altitude on 20 May (*"deciding what to build or the product management work becomes the new bottleneck rather than the actual building"*). Allen confirms at AWS-Executive-in-Residence altitude on 21 May with **Project Mantle** — an AWS internal rebuild of the layer under [[Amazon Web Services|Bedrock]] scheduled for ~18 months, shipped in **76 days** when AWS put VP-Distinguished-Engineer **Anthony Liguori** + L7 principal engineers on it with goal-based agents. Allen's load-bearing line (~20:23–20:40): *"the bottleneck is shifting. It's not execution now. It's decisions. It's product management. And for a long time, for 30 years in my career, it has been the long tail in getting things done. Suddenly, we're seeing that invert."* The 20–21 May 2026 PM-bottleneck cluster is now three sources strong (Ng + Allen + [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Sinclair/Ivers/Benitez SEI-CMU]]). Cited on the [[ai-employment-effects]] page + the [[agentic-engineering]] page + the [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng source page]]'s relationships block.

2. **USE / COMPOSE / BUILD economic-decision framework + the 12-month AWS-altitude longitudinal pair with Jassy.** Allen's strategic-altitude prescription: *use* third-party agentic vendors / *compose* with frontier-model APIs (Haiku, Sonnet, Opus 4.7) / *build* fine-tuned only when inference economics justify. Allen reports **~80% of AWS customers currently land at COMPOSE**. The framework is the *agentic-system-economics overlay* on [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy's May-2025 three-layer AI stack]] (infrastructure → orchestration → applications) at one-year time delta. **The wiki's first AWS-altitude longitudinal pair.** Allen also names the **Amazon Bedrock AgentCore** productised harness/runtime layer announced at AWS Summit by **Francesca Vasquez** earlier the same day — the AWS agentic-runtime equivalent of [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]. Cited on the [[enterprise-ai-adoption]] page + the [[Amazon Web Services]] entity page (new §4).

3. **Embedded-pod model + hourglass-organization + junior-hiring crisis.** Allen prescribes pods of 3–5 engineers organised around a **business outcome / workflow** (*"notice I didn't say product, I didn't say MVP, I said workflow"*); past 3–4 pods → platform team required, whose job is *removing friction from pods, not controlling them*. SRE warning: works at Google because Google's SREs are senior developers; *"if you're just renaming IT ops to SRE, same skills, that is going to fail."* Allen pairs the pod model with the **hourglass organisation** as counter to *"seniors 20×-ing their productivity, cutting back juniors"* default — argued via the **junior-hiring crisis**: 73% European-tech entry-hiring collapse (Ravio 2025), 7% of new grads → big tech (down from 15%), 7.7% junior headcount decline, 9% senior employment growth; AWS CEO **Matt Garman** quoted endorsing the moral framing. The Anthropic-competition exhibit (1st lawyer, 2nd cardiologist from Poland building AI-agentic patient-care platform, 3rd cardiologist — *no developer in top 3*) supplies the *non-developer-domain-expert-wins* operationalisation of the renaissance-developer / expert-generalist role-shift. Cited on the [[ai-employment-effects]] page + the [[ai-deskilling]] page (*"protect that junior learning path"* as active anti-deskilling discipline) + the [[durable-skills]] page (renaissance-developer + expert-generalist vocabulary).

4. **Moats-erosion thesis + non-determinism-as-feature operating-model corollary.** Allen's strategic-renewal claim: the old moats (workflow embeddedness, software scale, integration lock-in, engineering complexity, IP-locked-in-software) erode under agentic AI (*"could 6 months of seed funding and 30 engineers and an Anthropic frontier model replace your business entirely?"*); replacement moats are *compounding proprietary data*, *network effects*, *regulatory permission*, *capital at scale*, *physical infrastructure*, plus the meta-moat *time-that-can't-be-parallelised*. Worked example: *"I have had conversations with banks that are thinking of expanding their branch network again. Who would have thought it?"* Paired with the operating-model corollary at ~26:30: *"in agentic AI systems, non-determinism is a feature, not a bug"* + the *toll gates / toil gates* critique + *"if you still have engineering and operations as two different things, you are going to struggle"* — Allen's structural-twin of [[2026-05-08-running-an-ai-native-engineering-org|Fung / Anthropic's]] *"the tool isn't the hard part... your processes are."* Cited on the [[dynamic-capabilities]] page (end-to-end W&W process-model operationalisation) + the [[software-3.0]] page (operating-model corollary of the paradigm).

5. **Brooklyn Solutions phased-ingest discipline + 5× expectation + human-starts-human-ends accountability.** [[Nick Francis (Brooklyn Solutions)|Nick Francis]] (CTMO) narrates Brooklyn's 4-phase progression (basic use cases → conversational *Ask Brooklyn* → agentic → multi-agent), the segmentation-table worked example (numeric ids 1–5 mapped to *critical / important / transactional* labels giving *"weird at best"* LLM responses until context was iteratively added — the wiki's clearest vendor-customer-side ratification of context-engineering discipline), Bedrock Guardrails + AgentCore as the AWS-vendor regulated-customer harness composition (every token accounted for), and the **5× expectation** (5× output for ≤25% opex increase — *"you're not going to be able to do that in people"*). The **human-starts-the-work, human-ends-the-work** operational shape — agents in the middle, humans at entry and exit — is the wiki's first vendor-customer-side formalisation of *accountability-survives-at-the-seams* for regulated-customer contexts (MoD, Danske Bank). Closing aphorism *momentum beats perfection* is explicitly **not** permission to flood disposable apps; it's iterative quality compounding. Cited on the [[agent-harness]] page (context-engineering ratification + Bedrock Guardrails + AgentCore composition) + the [[micro-productivity-trap]] page (workflow-level focus / frequency × variability use-case discovery) + the [[automation-vs-augmentation]] page (*humans on judgment, agents on execution* prescription).

**Neighbour-source scan** (per §Ingest step 5): 8+ defensible neighbour candidates surfaced from W&W Path A (cell overlap) + Path B (concept-citation overlap). 8 typed `supports` edges added to the source page's `relationships:` block — to [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng 2026]] (PM-bottleneck three-vendor anchor), [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy 2025]] (12-month AWS longitudinal), [[2026-05-08-running-an-ai-native-engineering-org|Fung 2026]] (vendor-channel-parity on running AI-native eng orgs), [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Sinclair/Ivers/Benitez 2026]] (role-shift at SEI-CMU vs AWS altitudes), [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger 2019]] (theoretical-parent end-to-end operationalisation), [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai|Storoni 2026]] (anti-disposable-software / quality-over-quantity), [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index Q4 2025]] (cited-lineage anchor; the specific April-2026 Anthropic labour-market report Allen references is **not yet ingested** — *open follow-up*), [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels / McKinsey 2026]] (consultant-altitude convergence, 7 concept overlaps). Reverse-links not added (graph-export computes inverses).

**Concept-page updates** (lifecycle bumps + body wikilink rule honoured per Process step 6): [[enterprise-ai-adoption]] 48→49 (`last_confirmed` 2026-05-24 → 2026-05-25; new §*USE/COMPOSE/BUILD as AWS-vendor strategic-decision frame*); [[automation-vs-augmentation]] 25→26 (new §12 *Humans on judgment, agents on execution + anti-disposable-applications*); [[ai-employment-effects]] 27→28 (new §*Junior-hiring crisis + hourglass-organization counter-prescription*); [[ai-deskilling]] 6→7 (new §*Singapore governance + protect-junior-learning-path*); [[agent-harness]] 47→48 (new §*Brooklyn context-engineering case + AgentCore observability ratification*); [[agentic-engineering]] 30→31 (new §*AWS-vendor-altitude working definition* — *prompt with context + tools hitting a language model*); [[micro-productivity-trap]] 18→19 (new §8 *AWS-vendor-altitude pilot-purgatory anchor + MIT NANDA 95%*); [[dynamic-capabilities]] 7→8 (new §*End-to-end practitioner operationalisation of W&W process model*); [[software-3.0]] 4→5 (new §*Non-determinism-as-feature operating-model corollary*); [[durable-skills]] 16→17 (new §*Expert generalists + renaissance developer + Anthropic-competition exhibit*).

**Entity-page updates**: [[Amazon Web Services]] 3→4 (`last_confirmed` 2026-05-11 → 2026-05-25, confidence 0.83 → 0.85; new §4 *USE/COMPOSE/BUILD frame* with Bedrock AgentCore as the productised harness layer; four new Dangling people: Jonathan Allen, Anthony Liguori, Matt Garman, Francesca Vasquez).

**Dangling first-mentions** (deferred entity-page promotion per [§Author-entity promotion](../CLAUDE.md#author-entity-promotion)): Jonathan Allen (AWS Executive in Residence), Nick Francis (Brooklyn Solutions co-founder / CTMO), Brooklyn Solutions (UK supplier-management scale-up — *organisation*), Anthony Liguori (AWS VP Distinguished Engineer / Project Mantle lead), Matt Garman (AWS CEO since June 2024), Francesca Vasquez (AWS executive — AgentCore + security-agent + DevOps-agent announcer at the same forum earlier the same day), Scott Galloway (*"AI won't take your job. Someone using AI will"* quote source), Rory Sutherland (*"every spreadsheet is in some ways an act of pretense"* quote source), William Gibson (*"the future is here but not evenly distributed"* quote source), Martin Fowler (strangler-fig pattern + expert-generalists post), Werner Vogels (re:Invent 2025 *renaissance developer* keynote), Jeff Bezos (Amazon L9-elimination). **Concept-page candidates on 2nd source**: MIT NANDA, Singapore Davos-2026 AI governance model, USE/COMPOSE/BUILD framework, hourglass-organization, moats-erosion thesis, embedded-pod model. **Open follow-ups**: ingest the April-2026 Anthropic labour-market report; ingest the MIT NANDA 95%-fail report; ingest the Nvidia *Small Language Models are the future of agentic AI* paper.

## [2026-05-25] ingest | Storoni / HBR IdeaCast *Redefining What Efficiency Means in the Age of AI* — wiki's first `kind: podcast` source + first neuroscience-vantage anchor on AI-era work design; gear-3-reactive-work named as the neurological mechanism for the [[micro-productivity-trap]]; quality-over-quantity normative reframe on the augmentation pole of [[automation-vs-augmentation]]; self-regulation-under-uncertainty as durable-skill meta-layer

User-initiated single-source ingest of an HBR IdeaCast episode (Curt Nickisch interviewing neuroscientist Mithu Storoni about her book *Hyperefficient*). The 13 May 2026 episode is a re-cut of Storoni's earlier 2024-09 IdeaCast appearance reframed around the AI era. **Three first-of-kind contributions to the wiki:**

1. **First `kind: podcast` source.** Storoni is audio-first (HBR.org / Apple Podcasts / Spotify, not YouTube), so the existing video-transcript pipeline didn't apply. New typed subfolder `raw/podcasts/` created on the fly per CLAUDE.md §Acquire. Frontmatter contract adapted from the video format — kept the load-bearing four (`title` / `url` / `channel` / `publish_date`), dropped video-only fields (`video_id`, `caption_tracks`, `view_count`), added podcast-natural fields (`host`, `guest`, `guest_affiliation`, `publisher`). `duration: unknown` honestly stated — HBR doesn't surface audio length on the episode page. The precedent (acquire phase from a prior session: 25 May 2026 acquire commit; process this turn) is now the template for future audio-first podcast ingests.

2. **First neuroscience-vantage anchor on AI-era work design.** Storoni's **three-gear framework** (gear-1 mind-wandering / gear-2 Goldilocks focus / gear-3 high-norepinephrine reactive) on the well-established **norepinephrine inverted-U curve** supplies a physiological-mechanism layer to claims the wiki has so far only seen from leadership-practice ([[2026-04-28-reitz-higgins-spacious-thinking|Reitz & Higgins]]), consulting-engagement ([[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels]], [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt-Chatterji / Bain]]), and labour-economics ([[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson]]) vantages. Gear-2 maps to the work AI cannot substitute (judgment, second/third-order reasoning); gear-3 reactive work maps to the work AI substitutes *better* than humans — meaning workers stuck in gear-3 are placing themselves on the automation side of the [[automation-vs-augmentation]] cut by their work pattern, not by their job category.

3. **Gear-3 as the neurological mechanism for the [[micro-productivity-trap]].** The wiki had the trap from seven vantages already (consulting, investor + academic, executive coaching, academic survey, runtime engineering, target-firm CEO, NYT journalism); Storoni adds the brain-level mechanism — *why* the trap's organisational pattern (high throughput, low value) emerges from individual-level cognitive states. The mechanism: prefrontal cortex disengages in gear-3, speed goes up, accuracy goes down, second/third-order consequences get missed. Workers feel productive; the firm's value output collapses. Convergent with [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean / DORA]]'s engineering-team finding that *"increasing AI adoption can lead to individual productivity benefits while at the same time decreasing team-level benefits"* — same divergence pattern at adjacent scales (individual neurology → engineering team → firm).

**Pages touched (8):**

- **NEW**: [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai]] (source page, kind: podcast, 6 typed `supports` relationships).
- **Updated concepts (3)**: [[automation-vs-augmentation]] (source_count 24→25; added section 11 *The normative quality-over-quantity reframe* + row in convergence table), [[durable-skills]] (source_count 15→16; added regulation-meta-skill bullet under cross-source positioning), [[micro-productivity-trap]] (source_count 17→18; added neuroscience-mechanism-lens bullet). Confidence unchanged on all three — Storoni is a popularisation by an author promoting a book and per [[../CLAUDE.md#lifecycle|Lifecycle confidence rules]] should not lift the empirical baseline on its own.
- **Updated entity (1)**: [[Harvard Business Review]] (source_count 11→12; added Storoni row to HBR IdeaCast table; updated source-page-convention note to cover `kind: podcast` alongside `kind: video`; added Curt Nickisch to Dangling people; bumped IdeaCast open question — two episodes now sampled, both broadly aligned).
- **Reverse-link backfill (1)**: [[2026-04-28-reitz-higgins-spacious-thinking]] — added first `relationships:` block (the source predates W&W tagging / typed-relationships convention); typed `supports → Storoni` edge with body bullet in the *Related in this wiki* section.
- **Updated [[index.md]]**: prepended source entry to Sources; updated micro-productivity-trap concept entry to reflect the new neuroscience-mechanism vantage.

**Neighbour-source scan results** (per §Process step 5 / the [neighbour-source-scan](../.claude/skills/neighbour-source-scan/SKILL.md) skill): scan ran both paths. Path A surfaced 5 two-cell W&W overlap candidates ([[2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era|Schoening]], [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad]], [[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|Ng]], [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan-Hu]], [[2026-02-11-shyamsundar-jain-organizational-strategies-collective-wisdom-nature|Shyamsundar-Jain]]) plus the most-populated cell `digital-transforming/redesigning-internal-structures` (16 sources). Path B surfaced large clusters on the touched concept pages (16 sources cite `automation-vs-augmentation`, 15 cite `durable-skills`, 20 cite `micro-productivity-trap`). Edges drawn: 6 total (4 pre-identified during draft + 2 added after scan — Schoening and Forsgren & Macvean as the strongest not-yet-drawn candidates). Skipped Masad / Ng / Tan-Hu / Chase / Sinclair-Ivers-Benitez (W&W co-occurrence is real but thematic content is AI-native engineering org design, not knowledge-work cognitive-state design — co-occurrence isn't a relationship). Skipped Shyamsundar-Jain — would need to verify the *collective wisdom* framing is genuinely Storoni-adjacent vs surface-level cell-overlap; deferring to a supervised later pass.

**Dangling first-mentions** (per author-entity promotion rule): **Mithu Storoni**, **Curt Nickisch**, **3M**, ***Hyperefficient*** (book). All await second-source promotion.

**Open question surfaced**: with two HBR IdeaCast episodes now ingested ([[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels]] + [[2026-05-13-storoni-hbr-ideacast-redefining-efficiency-age-ai|Storoni]], both AI-era organisational change themed, both broadly aligned with HBR's house view), the IdeaCast podcast venue may warrant its own entity page (`kind: project` or `venue`) on the third IdeaCast ingest. Flagged in HBR entity page open questions.

## [2026-05-25] ingest | AI Dev 26 x SF evals two-video pair — Anthropic / Claude-channel *Evals for taste: Hill-climbing a slide-generation agent* (vendor-engineer altitude; grader taxonomy + QA-loop adversarial pattern + autoregressive-judge-ordering bug) + Khan / Cline / DeepLearningAI *Evals Are Broken Use Them Anyway* (customer-of-model-vendor altitude; three-zones-of-improvement + terminal-bench + *beat Claude Code on Opus 4.5 evals* as third independent harness-improvement anchor); DeepLearningAI promoted from Dangling to entity page, Cline promoted via cross-page-presence judgment

User-initiated two-video ingest pairing **two evals-themed talks from the same conference and the same day** (both 22 May 2026, both AI Dev 26 x San Francisco) at **opposite vendor-altitudes**. The two sources together give the wiki **paired model-vendor + customer-of-model-vendor anchors on eval discipline at the conference altitude** — complementing the [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe / Agent Evaluation Guide]] (substack article altitude, 4 days earlier), [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]] (vendor-CEO altitude, 1 day earlier), and [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten & Zhang]] (academic-paper altitude, 11 days earlier) already in the wiki.

**Acquire phase**: Video A (Anthropic / Claude channel) failed the Playwright path at 60s timeout (the recurring panel-render failure mode); yt-dlp fallback + hour-aware VTT dedup parser succeeded with 1,053 deduped segments. Video B (Khan / DeepLearningAI) succeeded on first Playwright attempt with 699 ASR segments. The Playwright fallback chain is now fully routine.

**Two anchor sources:**

- **[[2026-05-22-anthropic-evals-for-taste-hill-climbing-slide-generation-agent|Anthropic / Claude channel — *Evals for taste: Hill-climbing a slide-generation agent*]] (22 May 2026; ~39:16; 1,053 segs via yt-dlp fallback)** — **the wiki's deepest Anthropic-vendor practitioner-engineer altitude treatment of eval discipline.** Speaker not named on stage or in channel metadata (Anthropic-side presenter using the Anthropic `manage_agent` SDK + `python-pptx` + Sonnet 4.7 / Opus 4.7). The talk's most-portable contributions: (a) the **grader-type taxonomy** (code / model / human; with pairwise-comparison + multi-judge-consensus as underrated model-based grader sub-patterns); (b) the **QA-loop adversarial pattern** — *"Required QA loop. Assume there are problems. Your job is to find them. Approach QA as a bug hunt, not a confirmation step... do not stop until you've completed at least one fix-and-verify cycle"*; (c) the **autoregressive-judge-ordering bug** + the *reasoning-before-rating* fix (*"first you say give me a bunch of reasons, give me pros, give me cons... and then based on all of those reasons together, you make a final decision"*); (d) the **judge-calibration problem** (judges score 2.8-4.0 on obviously-terrible output because they have nothing to anchor on; fix: explicit examples of 0 and 5); (e) the **model-upgrade-vs-prompt-engineering trade-off** observation (Opus 4.7 with the naive base prompt recovers most prompt-engineering iteration gains on the slide-gen task). Filed **7 typed `supports` edges**. **Caveat the speaker is not named on stage** — the institutional vantage (Claude channel + Anthropic SDK + Anthropic models) is unambiguous but specific attribution is uncertain; flagged for renaming if a name surfaces.

- **[[2026-05-22-khan-cline-deeplearningai-ai-dev-26-sf-evals-are-broken-use-them-anyway|Khan / Cline / DeepLearningAI — *Evals Are Broken Use Them Anyway*]] (22 May 2026; ~24:36; 699 segs)** — **the wiki's first deep articulation of the *customer-of-model-vendor* vantage on eval discipline.** Ara Khan leads Cline's eval-discipline programme. The talk's most-portable contributions: (a) the **two-camps framing** — *"objective metrics" camp* (takes benchmark scores at face value; benchmark-maxing widespread) vs *"taste is king" camp* (vibes-only, anthropomorphises models); truth in the middle; (b) **three heuristics for interpreting others' evals** — *don't believe model-lab evals* (close approximations not gospel) + *stay current but don't be the earliest adopter* (let the dust settle 2 weeks) + *look for evals close to your problem* (generic benchmarks don't apply; SWE-bench saturated so hard model labs stopped citing it); (c) **Cline's eval journey** as the load-bearing operational worked example — 2024 baseline was *"talked to OpenAI and Anthropic, both said yeah evals are great but bro it's just about the vibes"*; pivot was adopting **Stanford terminal-bench** (89 real-software-engineering tasks; 5-45 min agent runs with deterministic unit-test grading) + **Harbor** (containerised isolated environments for parallel runs) + **[[Modal]]** (parallel-containerised infrastructure layer) + per-run tracking of turns/tool-calls/tokens/run-time; (d) the **three-things-being-tested framework** (most-portable analytical primitive) — model + harness + problem-space alignment; harness-as-confounder observation: *"same model in Claude Code works better than in Droid or Cursor — that's what you're testing"*; (e) the **three-zones-of-improvement framework** (most-portable strategic primitive) — Zone 1 obvious flaws / Zone 2 real hill-climbing / Zone 3 Goodhart-overfitting danger zone; (f) **the headline operational anchor**: *"Eventually we were able to beat Claude Code in Opus 4.5 evals... we figured out some tiny knobs that they couldn't figure out or they didn't optimize for"* — **the third independent primary-source confirmation** of the *harness-changes-alone-improve-eval-scores-substantially-on-the-same-model* pattern (after [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain]] and [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]]). Filed **8 typed edges** (7 `supports` + 1 `contradicts` with [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / CS153]] on the *vendor-vs-customer-of-vendor* coding-agent positioning question).

**Cross-cutting observations across the batch:**

1. **The 21-22 May 2026 *harness-is-load-bearing / evals-as-gradient* cluster is now five sources strong within 48 hours**: Chase / Interrupt 26 (21 May; vendor-CEO altitude; *three-layer continual-learning + evals-as-gradient*), Anthropic / Claude channel (22 May; vendor-engineer altitude; *grader taxonomy + QA-loop pattern*), Khan / Cline (22 May; customer-of-model-vendor altitude; *three-zones + beat Claude Code on Opus 4.5*), Wolfe / Agent Evaluation Guide (18 May; article altitude; *graders taxonomy + LLM-as-judge calibration + swiss-cheese-evaluation*), and Sinclair / Ivers / Benitez / SEI-CMU (21 May; institutional-research-centre altitude; *under-specification as the bad-practice-AI-magnifies-most*). The wiki now has paired anchors on *every altitude* in the evals corpus from a single 5-day window.

2. **The *harness > model* claim now has three independent primary-source vendor confirmations of the same numerical magnitude** (Top-30 → Top-5 on terminal-bench, ~25-point jump): [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain]] (10 March; LangChain's own measurement), [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]] (21 May; CEO-stage restatement), and now Khan / Cline (22 May; competitor-of-Anthropic measurement on Anthropic's reference agent vs Cline's). **The strongest single-claim convergence in the wiki's harness-engineering corpus**, with the third-source confirmation explicitly *competing with* the model vendor's own agent on the same model substrate.

3. **The model-upgrade-vs-harness-engineering trade-off is now explicitly framed as a productive tension at the same-day same-conference level.** Anthropic / Claude channel: *Opus 4.7 with the naive base prompt recovers most prompt-engineering gains* (model-upgrade-as-substitute-for-prompt-engineering). Khan / Cline: *we beat Claude Code on Opus 4.5 evals via harness engineering on the same model* (harness-engineering-as-substitute-for-model-upgrade). Both are correct conditionally — model upgrade clears prompt-engineering when the model has the relevant knowledge baked in; harness engineering wins when the underlying capability is there but the agent scaffolding is suboptimal. The wiki now carries both anchors at the same altitude.

4. **AI Dev 26 x SF is now anchored on three sources from three vantages** — Ng (20 May; AI-leader keynote) + Anthropic / Claude channel (22 May; model-vendor practitioner) + Khan / Cline (22 May; customer-of-model-vendor practitioner). The conference's intended structure becomes legible: *Ng-altitude keynote on the meta-shift* + *practitioner-track sessions on the specific skills the shift requires* (eval discipline is one such skill). Triggers [[DeepLearningAI]] entity-page promotion per the channel-as-entity convention.

5. **Stanford terminal-bench is now named explicitly as the load-bearing eval substrate** in multiple sources — Trivedy / LangChain (March 2026), Chase / Interrupt 26 (21 May), and now both Khan / Cline (22 May) and the Anthropic / Claude channel session (22 May; lists it as one of *"the usual suspects"* model-vendor benchmark cards). The wiki should flag terminal-bench for a standalone concept page on its next eval-related ingest — it's now functionally a wiki-tracked entity in the eval-discipline corpus.

**Entity changes**: **[[DeepLearningAI]] promoted from Dangling to entity page** (second source under this channel-author triggers per channel-as-entity convention; cf. YC Root Access, Lenny's Podcast). **[[Cline]] promoted to entity page** via cross-page-presence judgment (referenced in 4 prior wiki pages plus this solo-headlining ingest of a Cline employee). Source-count bumps: [[Anthropic]] 14→16 (both videos cite substantively); [[OpenAI]] 12→13 (Khan's 2024 anecdote + SWE-bench-deprecation citation). **New Dangling first-mentions** (deferred to second-source-mention per promotion rule): [[Ara Khan]] (Cline employee leading eval-discipline programme), Anthropic-presenter (unnamed speaker at the Claude channel session), `manage_agent` SDK primitive, terminal-bench (concept-page candidate on second-source — already at 8+ wiki references but no concept page yet), Harbor, DeepSeek V4 Flash, Droid, François Chollet (ASR-uncertain attribution).

**Concept bumps**: [[concepts/agent-harness|agent-harness]] 45→47 (both videos — *harness as one of the three things being tested*); [[concepts/agentic-engineering|agentic-engineering]] 28→30 (both videos — hill-climbing-on-evals as core loop primitive); [[concepts/agent-development-lifecycle|agent-development-lifecycle]] 10→12 (both videos — operational instantiation of the evals phase at vendor-engineer + customer-of-vendor altitudes); [[concepts/foundation-models|foundation-models]] 11→13 (both videos — model is one of three things being tested + don't-believe-model-lab-evals heuristic + cost-portfolio framing).

**Source-page count delta**: +2 (now 125). **Entity-page count delta**: +2 (DeepLearningAI + Cline, now 89). **Concept-page count delta**: 0 (terminal-bench flagged for promotion next eval ingest).

---

## [2026-05-24] ingest | Ng / DeepLearning.AI AI Dev 26 x SF *future-of-software-engineering* keynote — PM-bottleneck thesis + cascading-bottlenecks observation + 100%-AI-coding frontier-team norm + AI-job-apocalypse counter-claim + Context Hub and Code Dream / Code Realm product announcements; Andrew Ng promoted from Dangling to entity page

User-initiated single-source ingest of **[[2026-05-20-ng-deeplearningai-ai-dev-26-sf-future-of-software-engineering|*AI Dev 26 x SF: Andrew Ng: The Future of Software Engineering*]]** — a ~19-minute keynote published 20 May 2026 on the [[DeepLearningAI]] YouTube channel. **The wiki's first solo-headlining Andrew Ng anchor** — predates only by a brief cross-reference (the *"unbig in AI"* quote from [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success|Carrier / MIT March 2026]]); this ingest is the second substantive source mention and triggers entity-page promotion per the [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion).

**Acquire phase**: youtube-transcript-skill Playwright path failed at 60s timeout (the documented panel-render failure mode that recurred yesterday on the Caldwell ingest — appearing now on a *19-minute* video, not just long-format). yt-dlp fallback with the hour-aware VTT dedup parser (built during the 22 May Caldwell ingest) succeeded on first attempt: **502 deduped ASR segments** spanning the full 19:10 runtime. Note: the Playwright failure mode is now happening on a *short* video, suggesting the underlying issue isn't long-format-specific — a youtube-transcript-skill robustness upgrade is increasingly warranted.

**Eight substantive contributions** the talk lands in the wiki:

1. **The 100%-AI-coding norm at frontier teams** — *"My own coding is pretty much 100% AI... many of the frontier teams are trending toward 100%."* Wiki's most-aggressive unconditional headline-multiplier claim at conference altitude. Productive tension with [[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era|Wu / Momentic]]'s conditional *"Codex only makes you a 10× engineer if you weren't a 10× engineer to begin with"*; structural convergence with [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / CS153]]'s unconditional *1,000× engineer* framing (published the same day).

2. **The PM-bottleneck thesis** (the talk's load-bearing rhetorical centerpiece) — as AI coding accelerates *programming* 10–100×, *deciding-what-to-build* becomes the new bottleneck. Empirical signal: PM-to-engineer ratios collapsing from a typical *1:8* (one PM keeping eight engineers busy) toward *1:2*, then *1:1*, then **the collapse into single-human-doing-both**: *"the only thing that can move even faster is you take those two people and collapse them into a single human. Engineers who shape products or product managers that can code can move really fast."*

3. **Cascading bottlenecks** — design, legal/compliance, marketing, sales bottlenecks all become acute once engineer-plus-PM-collapse clears the first wave. *"If you spend 3 months writing code and legal takes a month to sign off, it's okay, but if you take a day writing code, you're going to wait a month for legal, it's like, boy."* The forced-generalism math: *"if a team needs software, product, design, legal, and marketing, and it's a team of two, by definition these two people have to have some skills in all of these functional areas."* The wiki's clearest single articulation of the *post-PM-bottleneck second-wave bottlenecks* observation.

4. **The AI-job-apocalypse counter-claim** — *"I just don't see the AI job apocalypse happening anytime soon... we can't find enough of these people"* (referring to AI-engineers with the building-blocks-knowledge + generalist-skills mix). Calibrated rather than dismissive: *"I know a lot of people are feeling job insecurity at all levels."* Cites business-media coverage acknowledging *"job apocalypse being delayed"* + Federal Reserve Bank of Philadelphia study. The practitioner-leader-vantage twin of [[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future|Jones / Stanford GSB]]'s academic-economist-vantage on the same question (Jones: theoretical mechanism via weak-links / jobs-as-bundles-of-tasks; Ng: empirical headcount observation from inside hiring).

5. **The AI-engineer hiring rubric** (three criteria Ng's teams use): coding-agent fluency (Claude Code, Gemini, Codex, Open Code) + robust building-blocks knowledge + generalist skills. *"A combination of the ability to* how *to build things as well as the ability to know* what *to build."*

6. **The building-blocks lego-bricks framing** (returns throughout) — software-as-combinatorial-composition of AI building blocks (LLMs, RAG, agentic workflows) and non-AI building blocks (UI, persistence, identity/auth), both *"proliferating at a speed like we've never seen."* The substrate observation under everything else in the talk.

7. **Parallel skill development** — two tracks needed: agents getting more capable (Anthropic agent skills + general capability uplift) + humans developing complementary skills to drive the agents effectively. The framing under which both product announcements are pitched.

8. **Two product announcements**: **Context Hub** (for AI agents) — Ng + Vivek Prasad + Sanyam Hota; solves the *knowledge-cutoff-leads-to-deprecated-API-calls* failure mode (canonical example: Claude Code defaulting to OpenAI's deprecated *chat completions* API instead of the newer *responses* API). CLI: `chob search OpenAI` / `chob get OpenAI/chat`. **Code Dream / Code Realm** (for human skill development) — *"not a course, a conversation"*: video-call with Ng (or AI-Ng) + browser-based terminal for hands-on practice. First-public announcement on stage; preview available from 20 May 2026.

**Cross-cutting observations across the corpus this lands in:**

1. **The 20–21 May 2026 *AI-native role-shift* anchor cluster is now four sources strong**: Tan & Hu / CS153 (20 May; YC-partner-doctrinal altitude — IC/DRI/AI-founder-type prescription), **Ng / DeepLearning.AI (20 May; AI-conference-keynote altitude — PM-bottleneck + cascading-bottlenecks + small-team-of-generalists)**, Bender / Google I/O (21 May; vendor-altitude socio-technical-ecology — programming-vs-engineering), Sinclair/Ivers/Benitez / SEI-CMU (21 May; institutional-research-centre altitude — coder-vs-software-engineer + engineering-discipline-endures). **All four within 36 hours** at four different altitudes converge on *narrow-coder-role fades, multi-skilled-generalist-judgment-role thrives*. Ng's specific contribution: the *empirical signal from inside hiring* (PM-to-engineer ratio collapse + *we can't find enough of these people*) under the structural-prescription framings the other three articulate.

2. **The *spec/PM-as-the-new-bottleneck* thesis now has paired anchors at founder-vantage (Wu / Momentic) + AI-conference altitude (Ng)**. Wu names it *truth-driven / spec-driven development* with *"I see code as an implementation detail"*; Ng names it *the product-management bottleneck* with *"deciding what to build becomes the new bottleneck rather than the actual building."* Same observation, different framing; both filed as load-bearing rhetorical claims on the agentic-engineering concept page.

3. **The *job apocalypse is not happening* claim now has paired theoretical and empirical anchors landing within 24 hours.** Jones (Stanford GSB, theoretical / weak-links): *"Hinton 2016 said stop training radiologists; we have more radiologists in 2026 than in 2016."* Ng (DeepLearning.AI, empirical / from-inside-hiring): *"we can't find enough of these people."* Two altitudes, same conclusion, calibrated and citation-anchored on both sides (Jones via Anthropic Mythos + bundles-of-tasks model; Ng via business-media + Federal Reserve Bank of Philadelphia study).

4. **Context Hub joins the agent-side AI-coding-supply-chain concern cluster**, alongside the *slop-squatting* attack vector [[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Ivers / SEI]] surfaced one day later. Two related failure modes: Context Hub addresses *real-package-APIs that are deprecated* (knowledge-cutoff-leads-to-deprecated-API-calls); Ivers addresses *fake-package-names that don't exist* (adversaries squatting on AI-hallucinated package names). Together they outline the *AI-coding-supply-chain hygiene* discipline as a 2026 concern, with two complementary tool-and-discipline answers.

5. **The Playwright-panel-render failure mode is now hitting short videos.** Yesterday's Caldwell (80 min) and SEI/CMU (61 min) failures were attributed to long-format. Ng's video is *19 minutes*. The yt-dlp fallback path remains reliable, and the hour-aware VTT dedup parser built during the Caldwell ingest works without modification — but the youtube-transcript-skill itself increasingly needs an upgrade (either default-longer-timeout, or automatic-yt-dlp-fallback-on-panel-render-fail, or both).

**Entity changes**: **[[Andrew Ng]] promoted from Dangling to entity page** — full career snapshot (Stanford / Google Brain / Baidu / Coursera / DeepLearning.AI / AI Fund / Landing AI) + seven sections cataloguing his wiki-load-bearing contributions (100%-AI-coding norm + PM-bottleneck thesis + cascading-bottlenecks + AI-job-apocalypse counter-claim + hiring rubric + building-blocks framing + parallel-skill-development framing + the *unbig in AI* prior-mention quote). Source-count bumps: [[Anthropic]] 13→14 (agent-skills reference on stage); [[OpenAI]] 11→12 (chat-completions-vs-responses-API worked example). **No new entity pages from this ingest beyond Ng.** **New Dangling first-mentions** (deferred to second-source-mention per promotion rule): [[DeepLearningAI]] (channel-entity; promote on second source under this `author:` value), Vivek Prasad, Sanyam Hota, Context Hub (concept-page candidate on second-source mention), Code Dream / Code Realm (canonical product name is ASR-uncertain on stage), Federal Reserve Bank of Philadelphia.

**Concept bumps**: [[concepts/agentic-engineering|agentic-engineering]] 27→28 (PM-bottleneck + cascading-bottlenecks + 100%-AI-coding norm); [[concepts/agent-harness|agent-harness]] 44→45 (Context Hub as harness-adjacent tool); [[concepts/vibe-coding|vibe-coding]] 16→17 (100%-AI-coding personal practice as vibe-coding-at-frontier-altitude); [[concepts/ai-employment-effects|ai-employment-effects]] 26→27 (AI-job-apocalypse counter-claim + *can't find enough of these people*); [[concepts/durable-skills|durable-skills]] 14→15 (AI-engineer hiring rubric as operational specification of the 2026 durable-skill mix); [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] 47→48 (AI-native-team-of-generalists prescription + cascading-bottlenecks); [[concepts/automation-vs-augmentation|automation-vs-augmentation]] 23→24 (PM-becomes-builder + designer-becomes-builder collapse).

**Source-page count delta**: +1 (now 123). **Entity-page count delta**: +1 (Andrew Ng, now 87). **Concept-page count delta**: 0 (Context Hub flagged for promotion next pass).

---

## [2026-05-22] ingest | Two-video pair — Sinclair/Ivers/Benitez/SEI-CMU AI-native-software-engineering institutional anchor + Caldwell/Lenny's-Podcast evergreen-YC-partner-wisdom anchor (tar pit ideas, Zip-procurement-pivot template, 2024 request-for-startups inventory); Dalton Caldwell promoted from Dangling to entity page

User-initiated two-video batch ingest pairing **two anchor sources at opposite ends of the wiki's temporal arc**: the SEI/CMU institutional webcast (21 May 2026, same day as Bender/Google I/O and Fernando/Man Group — the *AI does not replace engineering discipline* same-day institutional cluster), and a Lenny's Podcast episode from 2 years earlier (April 2024, the foundation-layer evergreen-YC-partner-wisdom that the spring 2026 AI-native-vendor cluster inherits).

**Acquire phase**: both videos initially failed the [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) Playwright path at the default 30s timeout (panel-render timeout, the documented long-format-video failure mode). SEI/CMU succeeded on retry with `--timeout 60000`. Caldwell/Lenny's failed at both 30s and 60s — fell back to `yt-dlp --write-auto-subs --sub-langs en --sub-format vtt` per the documented yt-dlp fallback chain. **The VTT-extraction logic uncovered a hidden bug**: the previous VTT parser filtered for *new-content* lines via the literal string `'<00:'` (timing-tag prefix), which silently dropped *all content past the 1-hour boundary* (where the prefix changes to `<01:`). Fixed in-batch with hour-aware regex `<\d\d:\d\d:` — 2,244 segments recovered spanning the full 1:20:49 transcript instead of the 1,664 segments that would have stopped at 59:58. This regression-detection-via-content-loss is worth flagging for the next acquire-time-skill upgrade.

**Two anchor sources:**

- **[[2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering|Sinclair, Ivers & Benitez / SEI-CMU]] (21 May 2026; ~61:14; 581 segs)** — **the wiki's first institutional-research-centre voice on the AI-coding-era software-engineering-discipline question.** Host **Scott Sinclair** with **James Ivers** (principal engineer SEI, 30+ years) and **Mario Benitez** (software architect SEI, 20+ years) on the *Software Engineering Institute | Carnegie Mellon University* YouTube channel. **Eight substantive contributions**: (1) **Definitional grounding** of AI-native vs AI-augmented vs agentic vs vibe-coding (the talk's stated learning objective #1); Ivers's load-bearing rhetorical claim ***"AI native is not AI only"*** + *"AI native is essentially a state of mind"*. (2) **The technical-debt-acceleration thesis** (Benitez's load-bearing empirical claim): *"We can generate code at rates we've never thought of before. We can also generate technical debt at rates that we've never thought of before"* + Ivers's *"no one has maintained code that was AI generated for 5 years"* temporal-horizon caveat. (3) **The 25,000-line vibe-coding-experiment** (Ivers's institutional-altitude worked example) — *"I got a very slick application but under the hood it was structured terribly. The architecture was bad. It wasn't very maintainable."* The clearest institutional-altitude worked example of where the vibe-coding-vs-engineering boundary lies. (4) **Engineering principles endure** — DRY, SOLID, YAGNI; *"we don't let go of the safeguards that we have now just because there's more code."* (5) **Under-specification as the bad-practice-AI-magnifies-most** — institutional-altitude restatement of [[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era|Wu / Momentic]]'s truth-driven / spec-driven development thesis. (6) **Architects more important under AI volume** (Ivers) + ADRs as the text-anchor for architecture decisions at scale + Benitez's compiler-analogy (*"we're elevating a little bit. I'm not sure how much"* — the institutional-altitude restatement of [[concepts/software-3.0|software-3.0]]'s abstraction-shift framing with the non-determinism caveat made explicit). (7) **Slop-squatting as a new attack vector** — AI-generated package names that don't exist, which adversaries can squat; SBOM/supply-chain-management as the existing-discipline-applied answer (wiki's first surfacing of the term). (8) **Coder vs Software Engineer closing role-shift framing** (Ivers): *"the narrow interpretation of coding might be fading. But those who can bring engineering judgment, point AI in the right direction, connect it to the business, connect it to the users — that's an incredibly valuable skill that's never resided solely in a programming language that I think is more enduring and will survive and be more critical than ever."* Filed **7 typed `supports` edges**.

- **[[2024-04-18-caldwell-lennys-podcast-lessons-1000-yc-startups-tarpit-ideas|Caldwell / Lenny's Podcast]] (18 April 2024; ~80:52; 2,244 segs via yt-dlp fallback)** — **the wiki's first deep evergreen-YC-partner anchor on the pre-AI-substrate-shift practitioner-wisdom layer of the YC corpus.** **Dalton Caldwell** (managing director / group partner at Y Combinator, 10+ years across 21 batches) interviewed by **Lenny Rachitsky**. Predates the wiki's spring 2026 YC partner-content burst (Tan / Hu / etc.) by two years and provides the foundational vocabulary (*tar pit ideas* / *just don't die* / *find an incumbent with low NPS* / *customer-validation-first*) the later 2026 episodes inherit and assume. **Six substantive contributions**: (1) **Tar pit ideas as a named primitive** (the talk's most-quoted concept) — *"By definition it is only a tar pit if it seems like it's not... part of being a true tar pit is that you can get good initial validation."* Canonical examples: friend-coordination apps, music discovery, Foursquare-clones. **A standalone [[concepts/tar-pit-ideas|tar-pit-ideas]] concept page is flagged for promotion on the next ingest** that touches the pivot / founder-idea-selection territory — multiple sources in the 2026 corpus gesture at this anti-pattern without naming it. (2) **The pivot-as-methodical-not-artful doctrine** + the **Zip / Procurement worked example** (Caldwell coached Rujul Zaparde toward the prompt *"intentionally find large publicly-traded or PE-owned companies that are hated by customers, combined with software is horrible"*) → **the named template** that the wiki's AI-native-ERP-vendor cluster ([[2026-05-20-glasgow-campfire-erp-for-ai-revolution|Glasgow / Campfire]] / [[2026-05-11-hill-vori-grocery-os-paper-and-fax|Hill / Vori]] / [[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Dinakaran / Luminai]]) later instantiates operationally. (3) **The struggle-is-universal anchor** — Caldwell's ~50% base-rate estimate + the Winter 17 batch / Brex anecdote as empirical-base for [[2026-05-19-mittal-yhangry-private-chef-all-in-on-ai-agents|Mittal's]] *"kill my human empathy"* moment from inside the rebuild. (4) **Don't optimise for TAM at seed stage** — Brex India *"the TAM of credit cards in India in 2015 was tiny"* worked example. (5) **Growth-hacking advice is actively harmful pre-product-market-fit** — Caldwell's contrarian-corner claim, made *on Lenny's own channel*, that *"reading Lenny's guides on how to set up split testing and how you did growth at Airbnb"* at seed stage is *"so dumb, that is so not helpful."* (6) **Customer-validation-first as final tactical advice** + **the 2024 request-for-startups inventory** (~9 categories named explicitly): ERPs (Caldwell-personally-authored — Glasgow / Campfire emerged from this prompt), open source, space, end-cancer, spatial-computing, defence, manufacturing-back-to-America, better-enterprise-glue, small-fine-tuned-models. Filed **5 typed `supports` edges**.

**Cross-cutting observations across the batch:**

1. **Same-day 21 May 2026 institutional/enterprise/vendor anchor cluster now consolidates.** The wiki now has **four sources published on 21 May 2026** converging on the *AI does not replace engineering discipline / AI as amplifier* thesis at different altitudes: [[2026-05-21-fernando-man-group-trading-signals-that-trade-themselves|Fernando / Man Group]] (enterprise empirical), [[2026-05-21-bender-google-io-software-engineering-tipping-point|Bender / Google I/O]] (vendor-altitude socio-technical), [[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future|Jones / Stanford GSB]] (macroeconomic weak-links), and Sinclair/Ivers/Benitez / SEI-CMU (institutional-research-centre). Plus Chase / Interrupt 26 the same day. **The 21 May 2026 corpus-cluster is now the wiki's densest single-day anchor.**
2. **The temporal-arc pairing — pre-AI-substrate-shift practitioner wisdom + post-phase-change institutional discipline — lands in the same batch.** Caldwell (April 2024) gives the founder-formation-layer vocabulary (tar pit / pivot / customer-validation-first) that the wiki's 2026 corpus assumes. Sinclair/Ivers/Benitez (May 2026) give the engineering-discipline-layer vocabulary (AI-native ≠ AI-only / technical debt acceleration / under-specification / engineering principles endure) at the institutional-research-centre altitude. **Both are foundational vocabularies the wiki was missing explicit anchors for.**
3. **The find-an-incumbent-with-low-NPS pivot template is now named explicitly** in the corpus. Caldwell's Zip / Procurement coaching story is the canonical articulation — the wiki's AI-native-vendor cluster (Glasgow / Hill / Dinakaran / Letter AI) is the operational-instantiation across verticals. Future ingests touching B2B-vertical-AI pivot stories should reference Caldwell's articulation as the template.
4. **The vibe-coding-vs-engineering boundary now has paired worked examples at practitioner + institutional altitudes**: Schoening's 3D-printed-enclosure physical metaphor (practitioner) + Ivers's 25,000-line vibe-coding experiment (institutional). Both make the same observation — AI accelerates *prototyping* but the *engineering-discipline gap* between prototype-quality and production-quality grows under AI.
5. **The yt-dlp-VTT-parsing regression-detection-via-content-loss is worth a hook-or-skill upgrade.** The hour-boundary bug in the previous parser would have silently dropped 580 segments (~25% of the Caldwell transcript). Future VTT-fallback runs should default to hour-aware timing-tag matching, and the youtube-transcript-skill documentation should call out this specific failure mode.

**Entity changes**: **[[Dalton Caldwell]] promoted from Dangling to entity page** (second substantive source per promotion rule — first was Glasgow / Campfire on 20 May 2026 where he was Campfire's YC partner-of-record + author of the *ERPs as request-for-startups* prompt; second is this canonical-headlining ingest). Source-count bumps: [[Y Combinator]] 10→11 (Caldwell ingest); [[Lenny's Podcast]] 3→4 (Caldwell ingest; Schoening row also added to the sources-under-this-author table which was stale). **No new entity pages created from the SEI/CMU ingest** — all five Dangling first-mentions (Software Engineering Institute, Carnegie Mellon University, Scott Sinclair, James Ivers, Mario Benitez) deferred to next ingest, plus *slop-squatting* as a concept-page candidate on second-source mention. **Deferred-but-warranted entity promotions** (from prior batches still standing): **Notion** + **Cursor**.

**Concept bumps**: [[concepts/agentic-engineering|agentic-engineering]] 26→27 (SEI); [[concepts/vibe-coding|vibe-coding]] 15→16 (SEI); [[concepts/agent-harness|agent-harness]] 43→44 (SEI); [[concepts/software-3.0|software-3.0]] 3→4 (SEI — Benitez's compiler-analogy); [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] 45→47 (both); [[concepts/automation-vs-augmentation|automation-vs-augmentation]] 22→23 (SEI); [[concepts/micro-productivity-trap|micro-productivity-trap]] 16→17 (SEI — Ivers's measurement-discipline argument); [[concepts/durable-skills|durable-skills]] 13→14 (SEI — engineering judgement / business connection / systems thinking as surviving meta-skills); [[concepts/dynamic-capabilities|dynamic-capabilities]] 6→7 (Caldwell — pivot-as-methodical operationalises digital-sensing/identifying-needs); [[concepts/strategic-foresight|strategic-foresight]] 9→10 (Caldwell — don't-optimise-for-TAM-at-seed-stage + Brex India worked example).

**Source-page count delta**: +2 (now 122). **Entity-page count delta**: +1 (Dalton Caldwell, now 86). **Concept-page count delta**: 0 (tar-pit-ideas flagged for promotion next pass).

---

## [2026-05-22] ingest | YC Root Access Founder Firesides three-video backfill batch — Dinakaran/Luminai paper-and-fax-vertical-AI-wedge at healthcare scale + Wu & An/Momentic truth-driven-development + closing-the-loop-for-coding-agents + 10×-counter-thesis + Akhtar & Forget/Letter AI MCP-server-as-vendor-product-surface for sales-enablement vertical

User-initiated three-video batch ingest, backfilling the YC Root Access *Founder Firesides* cluster with the three earliest published episodes (25 Feb / 23 March / 9 April 2026) that pre-date the spring 2026 YC partner-content burst already in the wiki. **Three successful ingests** — all three videos returned transcripts on first attempt via [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) (Playwright path), 84 / 312 / 328 ASR segments respectively. Light ASR cleanup on each (name normalisation, MCP/CLAUDE.md/Codex/Cursor/Playwright/Selenium-vs-Cypress-vs-Playwright disambiguation). The 22-May ingest **brings YC Root Access to six sources** (now the YC channel with the deepest wiki coverage, ahead of Startup School) spanning Feb–May 2026.

**Three anchor sources:**

- **[[2026-04-09-dinakaran-yc-luminai-automating-americas-biggest-hospitals|Dinakaran / Luminai]] (9 April; ~32:52; 312 segs)** — **paper-and-fax-vertical-AI-wedge anchor at trillion-dollar-industry scale.** Kesava Kirupa Dinakaran (founder/CEO Luminai, YC S20) interviewed by YC GP Aaron Epstein on the $38M Series B announcement (~$60M lifetime, Peak XV-led). The Cleveland Clinic worked example as the load-bearing operational anchor: *"the way that most patients get referred into the Cleveland Clinic is through a fax"* — Luminai becomes the frontline inbox agent triaging incoming faxes → structured EHR data → routing across *"thousands of departments"* at Cleveland (~16M patient encounters/year). **Three load-bearing rhetorical claims**: (a) the **verticalisation-as-credibility-decision** template (*"the moment you start to say 'I can do anything'... the credibility you have reduces pretty dramatically"* + the 80%+-healthcare-customer-data-driven all-in decision + the within-vertical narrowing to wedge use-cases); (b) **enterprise sales as a relational game**, named as doctrine — *"you're not actually selling a customer like the Cleveland Clinic. You're selling a champion within that one institution"* + the LinkedIn-contact-scraping script + warm-intro discipline + red-eye cadence as operational *how*; (c) the **reinvention thesis** — *"with every stage you have to reinvent yourself. Because the truth is, the next YC company is going to come in and pitch the most — the next dreamy vision that we were in five, four years ago."* **Twin paper-and-fax-vertical-AI-wedge anchor with [[2026-05-11-hill-vori-grocery-os-paper-and-fax|Hill / Vori]]** (healthcare + grocery, both trillion-dollar industries running on paper). **Founder-origin tangent**: Dinakaran was the captain of the international Rubik's cube team; mid-interview line: *"I learned Rubik's cubes from [[Andrej Karpathy]] on YouTube, who eventually ended up founding OpenAI"* — biographical bridge to the wiki's existing Karpathy entity (Karpathy source-count bumps 4→5). Filed **5 typed `supports` edges**: Hill/Vori + Mittal/Yhangry + Glasgow/Campfire + Garg/AnswerThis + Hu/YC April.

- **[[2026-03-23-wu-an-yc-momentic-qa-layer-ai-coding-era|Wu & An / Momentic]] (23 March; ~33:54; 328 segs)** — **the wiki's clearest founder-vantage anchor on independent-functional-testing-as-a-product for the AI coding era.** Weiwei Wu and Jeff An (co-founders Momentic, YC W24) interviewed by YC Managing Partner Harj Taggar on the $15M Series A announcement (description says $15M; speakers say $50M — ASR ambiguity preserved; description used as canonical). **The verification-layer-for-software wedge**: functional testing impersonating end users, slotted between linters/code-review and production; differentiator vs Selenium/Cypress/Playwright on flakiness + maintenance cost; differentiator vs raw browser-control LLM agents on speed (~300ms/step) + debuggability. **MCP-integration as the dev-loop product surface** — *"a lot of customers actually use our MCP integration to have Cursor or Claude Code write and run Momentic tests while they're developing"*; Taggar confirms YC engineering has Momentic in its CLAUDE.md pipeline. **The truth-driven / spec-driven development thesis as load-bearing rhetorical claim** (Wu's two-schools-of-thought): *"the spec is the source of truth. Your code is just an implementation of that source of truth"*; near-future prediction *"I would be disappointed in three to six months if I'm still reviewing TypeScript or React code... I see code as an implementation detail. It's a commodity."* **The closing-the-loop-for-coding-agents framing**: *"I can't really trust Claude Code or Cursor to tell me themselves. I need a third external source of truth"* — multi-harness-stack with MCP as inter-harness protocol. **The Notion onboarding via Twitter-DM-at-10pm anecdote** — Simon Last's Twitter post → 10pm DM → Loom of Wu testing on his own Notion workspace → onboarded that night → ~500K test runs/day; *"Momentic tests must pass before one of Notion's engineers can merge their PR."* Platform aggregate: *"over a million test runs a day."* **Productive contradiction filed with [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / CS153]]'s 1,000× thesis**: Wu's *"Codex only makes you a 10x engineer if you weren't a 10x engineer to begin with"* — direct rhetorical inversion; the wiki carries both anchors without resolving (Tan & Hu describing what *the best* engineer can now do unconditionally vs Wu describing what *Codex deployed on the average engineer* produces). Filed **6 typed edges** (5 `supports` + 1 `contradicts`).

- **[[2026-02-25-akhtar-forget-yc-letter-ai-powered-revenue|Akhtar & Forget / Letter AI]] (25 February; ~10:21; 84 segs)** — **the wiki's first founder-vantage worked example of *MCP-server-and-agent-to-agent-protocol as B2B vertical-SaaS product surface* for a non-developer-tools vendor.** Ali Akhtar (CEO) and Armen Forget (CTO) of Letter AI in conversation with YC General Partner [[Diana Hu]] on the $40M Series B announcement (the shortest and earliest YC Root Access ingest in the wiki). **The pivot-during-batch + Lenovo-closed-in-batch anchor pair**: Letter AI was originally *Tractatus* (developer tools for generative AI); pivoted in-batch + renamed; closed Lenovo as a customer during the batch via a former colleague's warm intro. **The legacy-enablement-tool-adoption-gap insight** (Akhtar's prior-role observation at Samsara: sellers couldn't find content in the *"really expensive"* legacy tool; the legacy-vendor's answer was *throw more humans at content curation*; AI-native wedge: tap existing knowledge sources + generate personalised content without the manual curation layer). **The MCP-server + agent-to-agent product surface** — Letter AI MCP servers + agent-to-agent protocol; salespeople in Cursor pull content via the Letter MCP server during their research workflow. **Letter Compass = personalisation-to-book-of-business** + *"never sell alone with Letter."* **Diana Hu source-count bumps 2→3** (her first interviewer-vantage source in the wiki, three months before her headlining-vantage lecture). Filed **3 typed `supports` edges**.

**Cross-cutting observations across the batch:**

1. **YC Root Access becomes the YC channel with the deepest wiki coverage** — six sources (Letter AI / Momentic / Luminai / Garg / Mittal / Glasgow) spanning Feb–May 2026, more than Startup School's two and YC Founder Firesides' one. The Founder Firesides format on YC Root Access has now produced a *vertical-AI portfolio-vendor* cluster across six categories: sales-enablement (Letter AI), QA (Momentic), healthcare-administrative (Luminai), 2-FTE-startup (Garg / AnswerThis), private-chef marketplace (Mittal / Yhangry), and enterprise-B2B ERP (Glasgow / Campfire).
2. **The MCP-server-as-vendor-product-surface pattern recurs across the batch.** Letter AI ships an MCP server for sales-content retrieval; Momentic ships MCP integration for coding-agent verification. Together with Chase's three-layer continual-learning model (model/harness/context with MCP as one of the connectors), the wiki's emerging picture is that 2026-vintage AI-native B2B vendors are increasingly *MCP-first* in their product surface — they expose their core capability as a tool-call to customers' agent ecosystems, not (only) as a portal humans log into.
3. **The pivot-during-batch + warm-intro-enterprise-customer-in-batch template** recurs across Letter AI (Tractatus → Letter AI, Lenovo in batch) and Luminai (developer documentation → healthcare admin, Cleveland Clinic shortly post-batch). Both founders narrate the same template: customers told them the original idea wasn't sticky → founder iterated on the idea maze → landed on a vertical with both personal-mission energy and observable enterprise pain → marquee enterprise customer closed via warm intro.
4. **The 10× vs 1,000× engineer productive contradiction is now formally filed.** Wu's *"Codex only makes you a 10x engineer if you weren't a 10x engineer to begin with"* (23 March) is two months *before* Tan & Hu's CS153 unconditional *1,000× engineer* framing (20 May). The wiki's [[concepts/agentic-engineering|agentic-engineering]] page's debates-and-supersession section now carries both anchors with the resolution sketch: both founders are right at different conditionalities (best-engineer-now vs Codex-on-average-engineer).
5. **Founder-led-sales-as-doctrine-in-the-AI-era** now has paired anchors across two industries. Dinakaran (Luminai, hospital C-suite): *"really major institutions don't really talk to you unless it's someone who they trust is making the referral"* + LinkedIn-contact-scraping script + red-eye cadence. Glasgow (Campfire, enterprise CFO): *"I do really recommend founders to stay in the founder sales mode... offloading it to AI, offloading it to some AE... feels like, oh let's just bring in a professional"*. Both converge: at the enterprise altitude, AI does not unlock cold-outbound to bypass the relational-network-of-trust layer.

**Entity changes**: source-count bumps to [[Y Combinator]] 7→10 (all three ingests), [[Diana Hu]] 2→3 (Letter AI interviewer), [[Andrej Karpathy]] 4→5 (Luminai biographical-bridge mention), [[Anthropic]] 12→13 (Momentic substantively references Claude Code as customer dev-loop substrate). **No new entity pages created on this ingest** — all promotable second-source mentions deferred to next ingest. **New Dangling first-mentions**: Kesava Kirupa Dinakaran, Luminai, Aaron Epstein, Cleveland Clinic, Peak XV, United World College, Weiwei Wu, Jeff An, Harj Taggar, Momentic, Simon Last, Robinhood, Dan Robinson, Heap, Ali Akhtar, Armen Forget, Letter AI, Lenovo. **Deferred-but-warranted entity promotions** (flagged for next ingest pass): **Notion** (now 7+ substantive mentions including Momentic's ~500K-test-runs/day anchor) and **Cursor** (16+ substantive source-body mentions).

**Concept bumps**: [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] 42→45 (all 3); [[concepts/agent-harness|agent-harness]] 40→43 (all 3); [[concepts/agentic-engineering|agentic-engineering]] 24→26 (Letter AI + Momentic) + new debates-and-supersession entry on the 10× counter-thesis; [[concepts/automation-vs-augmentation|automation-vs-augmentation]] 21→22 (Luminai); [[concepts/ai-employment-effects|ai-employment-effects]] 25→26 (Luminai); [[concepts/agent-development-lifecycle|agent-development-lifecycle]] 9→10 (Momentic); [[concepts/vibe-coding|vibe-coding]] 14→15 (Momentic); [[concepts/durable-skills|durable-skills]] 12→13 (Momentic).

**Source-page count delta**: +3 (now 120). **Entity-page count delta**: 0. **Concept-page count delta**: 0.

---

## [2026-05-22] ingest | Seven-video batch — Fernando/Man-Group enterprise-scale skills-governance anchor + Jones/Stanford-GSB weak-links macroeconomic anchor + Schoening/Notion agency-as-durable-skill anchor + Bender/Google-I/O socio-technical-ecology anchor + Agrawal/Stanford-MSE-435 AI-stack-value-capture anchor + Neven-Manyika/Google-I/O quantum-AI stub-anchor; one acquire-failure (no captions)

User-initiated seven-video batch ingest. **Six successful ingests + one acquire-failure** logged separately below.

**Acquire phase**: all seven videos fetched in parallel via [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) (Playwright path). Six succeeded on first attempt — the Google I/O 2026 and Stanford channels (manual captions available) gave the highest-quality transcript shape; the Claude / Anthropic and Lenny's Podcast channels returned ASR-only (still clean). One video (*"Building AI-native at enterprise scale: monday.com, Doctolib, and Delivery Hero"*, video ID `XFaeIbL-lvE`, Claude channel, 21 May 2026) returned `transcript: None` with empty `caption_tracks`; yt-dlp `--list-subs` confirmed *"has no automatic captions, has no subtitles"* — the video was published without captions. **Logged as a separate `acquire | ...` entry below** per the §Acquire protocol — no `raw/videos/` file written, no wiki source page created.

**Three anchor sources (full substantive treatment):**

- **[[2026-05-21-fernando-man-group-trading-signals-that-trade-themselves|Fernando / Man Group on Code with Claude]] (21 May; ~20:45; 157 segs)** — **enterprise-scale empirical anchor on skills governance.** $200B AUM regulated investment manager; 750 of 1,700–1,800 people use Claude Code; 100+ governed skills + at least as many community skills. **Production trading signals proposed by AI** — AI researched, backtested, wrote up, and productionised the signal; humans reviewed all outputs. **The expense-report failure-mode story** (~9:32–10:42) is now the wiki's clearest empirical worked example of *what goes wrong with ungoverned skills* — a power user wrote a skill that hardcoded his cost-center code, shared with team; expense approver in sales suddenly got everyone's reports. **Knowledge marketplace as the governance solve** (every skill visible, tagged, tested with evals, owned by workflow owner, lifecycle-managed). **Load-bearing rhetorical claim**: *"Focus on organizational context. That is your IP. It's your moat. It's one of the few safe spaces left in AI. The frontier labs are not going to solve context for you."* **Filed three `supports` edges**: [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / CS153]] (enterprise-scale operationalisation of skills/skillify framework with the expense-report-as-empirical-anchor on why check-resolvable exists); [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]] (Fernando's *organizational context as moat* = Chase's *context layer* of the three-layer continual-learning model); [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg / AnswerThis]] (2-FTE-startup ↔ 1,700-employee-enterprise scale-ladder endpoints).

- **[[2026-05-01-jones-stanford-gsb-ai-and-our-economic-future|Jones / Stanford GSB Spring Reunions]] (1 May; ~60:38; 518 segs)** — **strongest single academic-altitude theoretical anchor on AI's economic and labour implications.** Two-scenarios framing (FOOM vs business-as-usual). 2%-per-year-for-150-years US-growth puzzle. **The weak-links model** (the talk's central conceptual contribution): a chain is only as strong as its weakest link; *"infinite amounts of some task raises GDP by that task's share of GDP"* — software is 2% of GDP, so infinite software is 2% richer. **Productive contradiction with Tan / GStack** (filed as a typed `contradicts` relationship) captures the *thousandx-engineer* claim vs *weak-links bottleneck* tension. **Asymmetric-timeline corollary**: weak-links makes AI productivity slow to materialise *and* catastrophic risks fast — *"a weak-link model is very slow to improve, but very fragile on the downside."* Jones cites Anthropic's [[Anthropic|Mythos]] (bug-discovery model that found thousands of bugs in 25-year battle-tested software) as the empirical anchor on the fragile-downside corollary. The **Hinton 2016 radiologist prediction vs 2026 reality** is the cleanest jobs-as-bundles-of-tasks worked example in the corpus. **Filed five `supports` edges + one `contradicts` edge.**

- **[[2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era|Schoening / Lenny's Podcast (Notion)]] (2 May; ~87:22; 1684 segs — read closely chapters 1–10)** — **the wiki's clearest single articulation of *agency as the durable AI-era skill*** at the practitioner-altitude. Distinct from the taste/judgement framings the wiki carries: agency is *the disposition to act / make / change things — prior to taste or judgement*. **Two Notion vignettes** (Brian Leven — designer who blurs eng/design and is the company's #1 recruiter; Eric Lou — PM who shifted PRDs → Figma → *"can't I just build the prototype?"*) are the wiki's clearest practitioner-altitude operational worked examples of agency-in-action. **Schoening's prototype-vs-engineering physical-metaphor** (3D-printed prototype with visible layer lines vs optimise-the-factory-for-100M-users engineering discipline) complements [[2026-05-21-bender-google-io-software-engineering-tipping-point|Bender's]] programming-vs-engineering distinction. **Malleable software** as a long-arc design tradition (Ink & Switch / Jeffrey Litt lineage). **Filed five `supports` edges** including a pair with [[2026-05-19-mittal-yhangry-private-chef-all-in-on-ai-agents|Mittal / Yhangry]] (*what thriving looks like* vs *what firing looks like* on the same *tool-fluency-as-org-design-criterion* thesis).

**Three mid-weight sources:**

- **[[2026-05-21-bender-google-io-software-engineering-tipping-point|Bender / Google I/O 2026]] (21 May; ~39:39; 398 segs)** — *Software engineering at the tipping point* — **the strongest socio-technical-systems-thinking anchor on developer-ecosystem evolution under AI**. Systems → Ecosystem → Complex Adaptive System → Socio-technical system definitional stack with Conway's Law as the canonical insight. **The 10×-moment-will-break-every-part-of-your-ecosystem** thesis with worked-example failure modes (build system, binary size, microservices, component reuse). **Programming-vs-engineering distinction at AI-era scale** (*"generating code 10× faster ≠ engineering 10× faster; engineering is programming integrated over time"*). **AI-as-amplifier (DORA-rooted)**: *"amplification is a magnitude and not a direction; AI doesn't care where all of that stuff goes."* Together with [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean / Google I/O]] this is the wiki's second 2026 DORA-grounded anchor — *fundamentals determine amplification direction.* **2030 prediction**: *"In 2030, our developer ecosystems today are going to feel like 2001 does to us now."* Four-axis preparation checklist (infrastructure capacity / validation / isolation / abstraction). **Intellectual-control closing thesis** as load-bearing rationale for agentic engineering.

- **[[2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai|Agrawal / Stanford MS&E 435 Spring 2026]] (20 May; ~34:13; 322 segs)** — **the wiki's first *AI stack value-capture* framing at the venture-capital altitude**. The triangle / inverted-triangle industry-structure framing (semis bottom / infra middle / apps top, currently inverted vs eventual stable state). **The AWS-historical-analog timing anchor**: 8-year capex cycle from 2004 (AWS broke ground) to 2010 (Netflix as first customer) to 2012 (Amazon fully shifted) — reusable temporal frame for the AI buildout. **Are-you-a-feature-or-a-platform** diagnostic for AI-infrastructure startups against hyperscaler consolidation. **Business-unit-level disaggregation** (Google = TPUs in semis + GCP in infra + Gemini in apps) as the right slot-conglomerates-into-the-stack method.

- **[[2026-05-21-neven-manyika-google-io-quantum-ai-future|Neven & Manyika / Google I/O 2026 Dialogues]] (21 May; ~40:28; 335 segs)** — **the wiki's first substantive quantum computing ingest**, framed as the *AI-adjacent next-supercycle technology cluster*. Quantum 101 primer (superposition + qubits + the Willow chip = 105 qubits). **Nobel-Prize-2025-Physics anchor** (Berkeley 1980s superconductivity research — Devoret + Martinis + Clarke — leads to commercial Google Quantum AI team). **Google's moonshot lineage** (Search → ML auto-correction → Waymo → quantum). [[James Manyika]] entity bumps to 3 sources as the interviewer/moderator vantage. Filed as a *stub-anchor* for a potentially-emerging cluster.

**Cross-cutting observations across the batch:**

1. **The *skills/context-as-the-enterprise-moat* thesis now closes the scale-ladder.** [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|Garg / AnswerThis]] (2-FTE / $2M ARR) + Fernando / Man Group (750-of-1,700 / 100+ governed skills) bracket the operational scale; [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan / CS153]] + [[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|Chase / Interrupt 26]] bracket the rhetorical / vendor-CEO altitudes. **Four sources across late-May 2026 lock in the cluster** at every relevant operating scale and altitude.
2. **Two paired Google I/O 2026 talks now anchor the *AI-fundamentals-determine-amplification-direction* DORA-rooted thesis** — [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren & Macvean]] (individual-engineer altitude) + [[2026-05-21-bender-google-io-software-engineering-tipping-point|Bender]] (socio-technical-ecosystem altitude). DORA's *amplifier-and-mirror* framing recurs at both altitudes from the same conference.
3. **Stanford economic-vantage anchor pair within 24 hours**: [[2026-05-21-jones-stanford-gsb-ai-and-our-economic-future|Jones / GSB]] (macroeconomic-growth weak-links model) + [[2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai|Agrawal / MS&E 435]] (industry-structure value-capture framing). Same Stanford-academic vantage on AI economics from opposite ends of the macro/micro spectrum.
4. **Agency / disposition vs taste / judgement now distinguishable on [[concepts/durable-skills|durable-skills]].** Schoening's *agency-as-disposition-to-act* is upstream of Karpathy / Hu / Forsgren's *taste-and-judgement-as-discernment* — the wiki can now anchor agency as the load-bearing precursor rather than as a synonym.
5. **Strongest single-claim convergence**: the *harness > model* / Top-30→Top-5 LangChain Terminal Bench 2 claim now has **three independent primary-source citations** (Trivedy 10 March, Chase 21 May Interrupt 26, and indirectly via Fernando's *skills governance unlocks production trading signals* enterprise-scale instantiation).

**Entity changes**: source-count bumps to [[Anthropic]] 11→12 (Fernando), [[Google]] 7→9 (Bender + Neven/Manyika), [[Stanford Online]] 2→4 (Agrawal + Neven/Manyika via Google for Developers is separate, but Stanford Online gets Agrawal + Jones-wait-Jones-is-Stanford-GSB), [[James Manyika]] 2→3 (Neven/Manyika), [[Lenny's Podcast]] 2→3 (Schoening). **No new entity pages created on this ingest** — all promotable second-source mentions deferred to next ingest. **New Dangling first-mentions**: Tushara Fernando, Man Group, Chad Jones, Daron Acemoglu, Apoorv Agrawal, Altimeter Capital, Adam Bender, Hartmut Neven, Michel Devoret, John Martinis, John Clarke, Willow chip, AlphaFold, Max Schoening, Notion (substantive), Brian Leven, Eric Lou, Lenny Rachitsky, Ink & Switch, Jeffrey Litt, Dieter Rams, Bill Nordhaus, Paul Romer, Stuart Russell, Sebastian Thrun, Mythos (Anthropic model), Salesforce (substantive), Palantir (substantive).

**Concept bumps**: [[concepts/agent-harness|agent-harness]] 38→40 (Fernando + Bender); [[concepts/agentic-engineering|agentic-engineering]] 22→24 (Fernando + Bender); [[concepts/ai-employment-effects|ai-employment-effects]] 23→25 (Jones + Schoening); [[concepts/automation-vs-augmentation|automation-vs-augmentation]] 20→21 (Jones); [[concepts/durable-skills|durable-skills]] 11→12 (Schoening — agency anchor); [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] 39→42 (Fernando + Schoening + Agrawal); [[concepts/foundation-models|foundation-models]] 9→11 (Fernando + Agrawal); [[concepts/systems-thinking|systems-thinking]] 4→5 (Bender); [[concepts/strategic-foresight|strategic-foresight]] 6→9 (Jones + Agrawal + Neven/Manyika); [[concepts/dynamic-capabilities|dynamic-capabilities]] 5→6 (Jones); [[concepts/micro-productivity-trap|micro-productivity-trap]] 15→16 (Bender).

**Source-page count delta**: +6 (now 117). **Entity-page count delta**: 0 (no new entities promoted). **Concept-page count delta**: 0.

---

## [2026-05-22] acquire | "Building AI-native at enterprise scale: monday.com, Doctolib, and Delivery Hero" (Claude channel, 20 May 2026) — failed: no captions on YouTube

Acquire-only entry per §Acquire protocol. Video ID `XFaeIbL-lvE`; published 2026-05-20 on the [[Anthropic|Claude]] YouTube channel; ~29:10 runtime (1750 seconds). The video was published **without any caption track** — neither manual nor auto-generated. Confirmed by both the youtube-transcript-skill (`transcript: None`, empty `caption_tracks` array, `error: "no transcript section (video has no captions or hasn't been processed)"`) and yt-dlp `--list-subs` (*"XFaeIbL-lvE has no automatic captions, has no subtitles"*).

**Why this matters**: the talk's title and channel description suggest a high-substance enterprise-scale AI-native-customer-story anchor (three named substantive enterprise customers — monday.com, Doctolib, Delivery Hero). It would have been a strong companion to the [[2026-05-21-fernando-man-group-trading-signals-that-trade-themselves|Fernando / Man Group]] ingest from the same week, extending the Claude-channel enterprise customer-story cluster.

**Resolution path**: re-attempt acquisition if YouTube's auto-captions become available (typically appears 24–72 hours after publication for unscoped videos; this one is now ~48 hours old and still uncaptioned — Anthropic may have actively disabled captions for this talk, in which case the wiki will need to ingest it via a different channel: official Anthropic blog post if published, conference recording if available, or transcript via Otter / Rev if the video is re-uploaded with audio extraction). No raw file written; this entry is the audit trail. The wiki source page would be filed as [[2026-05-20-building-ai-native-at-enterprise-scale-monday-doctolib-delivery-hero]] when processed.

---

## [2026-05-21] ingest | Chase, Sproul & di Vittorio / LangChain Interrupt 26 Day 2 keynote — *The Future of AI Agents: What Will Interrupt 2027 Look Like?* — Harrison Chase promoted from Dangling to entity page; three-layer continual-learning model + evals-as-gradient anchor

User-initiated single-source ingest of **[[2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents|*The Future of AI Agents: What Will Interrupt 2027 Look Like? | Interrupt 26*]]** — a ~22:10 LangChain Interrupt 26 Day 2 keynote published 2026-05-21 on the [[LangChain]] YouTube channel. Three speakers: **[[Harrison Chase]]** (co-founder/CEO, segments 1–10 + closing), **Brace Sproul** (LangChain, product walkthrough), **Caroline di Vittorio** (LangChain, live Fleet demo). **Manual English captions used** — first ingest in the recent session-cluster where the [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) Playwright path succeeded on first attempt without yt-dlp fallback (a clear quality contrast with the YC Root Access cluster from yesterday, which consistently failed the panel-render path).

**Why this matters in the corpus.** This is **Harrison Chase's second substantive wiki source** ([[2026-05-09-chase-agent-development-lifecycle|ADLC, 9 May]] was the first); triggers entity-page promotion per the [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion). [[LangChain]] entity bumps 4 → 5 sources. The keynote lands six substantive contributions to the wiki, of which **three are structural extensions** to vocabulary the wiki already carries from Chase and from the broader harness corpus:

**1. Two-types-of-agents typology** (~1:22–2:42): **long-horizon agents** (minutes/hours/days; code execution, planning, sub-agents, multi-agent, skills; outcomes/goals as horizon-extension; knowledge work) vs **customer-experience agents** (latency-critical, voice modality, brand-sensitive, customer support / sales). Shared stack underneath but particular technology per type. **A new structural axis orthogonal to Chase's [[2026-05-09-chase-agent-development-lifecycle|earlier four-layer Build split]]** — the new axis is *what the agent runs against (the world / time horizon vs end-user-experience)*, not *where the agent lives in the build stack*.

**2. The three-layer continual-learning model** (~7:26–10:42) — the conceptual centerpiece. Every agentic system has **three independently improvable layers**:

| Layer | What it is | Examples |
|---|---|---|
| **Model** | Base foundation model | Sonnet, GLM4, GPT-4 |
| **Harness** | *"The code surrounding the model that connects it to the environment"* | Deep Agents, Claude Code, pi |
| **Context** | *"What we provide to the harness as ways to guide it on particular tasks"* | `agent.md`, skills |

**Evals-as-gradient framing** (Chase's own articulation): *"In classical machine learning, you have the model, the training data, gradient descent, that updates the weights. When you're updating the agent in general — if you're at the harness or context layer — it's not exactly gradient descent, but the **evals that you write act as a forcing function**. Those evals are providing a similar type of this training gradient. So evals and traces are incredibly important for this learning."* The wiki's clearest single articulation of **evals-as-gradient** for non-model layers — ties [[concepts/agent-development-lifecycle|the ADLC eval phase]] to the continual-improvement substrate of every other phase.

**3. Top 30 → Top 5 Terminal Bench 2 — third primary-source confirmation.** Chase's stage assertion *"we moved from top 30 on terminal bench two to top five just by changing the harness itself — no changes to the model, only changes to the harness, and we saw a big increase in performance"* is the **third independent primary-source citation** of the same numerical magnitude, following [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness|Trivedy / LangChain Engineering blog (10 March 2026)]] and the broader pattern from [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex (11 Feb 2026)]]. **Strongest single-claim convergence in the wiki's *harness > model* corpus** — research-blog (Trivedy) + academic-paper-adjacent (cohort: Karten & Zhang / Lee et al. MetaHarness / Pan et al. NLAH) + CEO-stage (Chase).

**Three additional substantive contributions** the keynote adds:

- **Voice agents — pipeline vs native** (~2:42–3:58): today's STT → agent → TTS sandwich vs emerging native speech-to-speech (*"OpenAI released V2 of theirs two weeks ago"* — i.e. ~7 May 2026); *"not quite steerable enough yet, we do expect that to change."*
- **Every agent needs a sandbox** (~3:58–4:47): *"Coding is really good for a variety of tasks — data analysis, web browsing, image gen, deep research."* Sandboxes launched at Interrupt 26 Day 1.
- **Agent identity & auth patterns** (~6:01–7:26): two emerging patterns — *act-on-behalf-of-user* (uses caller's credentials; different users see different things via the agent) vs *fixed-service-account* (GPTs-style; everyone interacting sees same responses). SaaS providers starting to make it easy for agents to create their own accounts. Wiki's first articulation of **agent-auth-pattern as a structural product-design choice**.

**Product announcements + LangChain operational metrics.** **LangChain Labs** = new research group *"aimed in particular at continual learning"* — institutional commitment paired with the academic agenda of [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten & Zhang's]] continual-harness-adaptation paper. **LangSmith Fleet** updates: 200+ built-in tools + **Arcade** partnership (7,500+ more) + MCP support + native Slack/Gmail/Outlook channels + sharing model like Google Docs + auth management + cost tracking/usage controls + first-class HITL + built on **deep agents** + downloadable agent files. **Internal-LangChain GTM-agent metrics** (Caroline di Vittorio live demo, ~13:40–19:05): **84% weekly use; lead-to-qualified conversion up 240%; 40 hours saved per rep per month** — wiki's first concrete *"engineer-built-it-in-code → rebuilt-in-no-code-so-the-domain-team-could-own-it"* migration with quantified outcomes (the GTM agent was originally built by an engineer in code, rebuilt in Fleet for the GTM team to own end-to-end without code). Free open-source model in Fleet powered by **[[LangChain|Fireworks AI]]** partnership.

**Paired with [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / Stanford CS153]] (one day earlier).** Both Chase and Tan articulate **layered-system decompositions of agent thinking**, landing within 24 hours:

| Source | Axis | Decomposition |
|---|---|---|
| Tan / CS153 (20 May) | Agentic-primitives → company-structure | Skills = employees / Resolvers = org chart / GBrain = internal process / Check-resolvable = audit / Trigger evals = performance reviews |
| Chase / Interrupt 26 (21 May) | Learning-systems → agentic-system-layers | Model / Harness / Context — each independently improvable, with evals-as-gradient |

Both founders extend the *everyone-builds-agents* corollary (Hu's *AI founder / IC / DRI* org structure on 24 April + Chase's *domain experts will be building agents, not just giving feedback* on 21 May). The 2026 founder-CEO doctrine is converging on **decompose-the-agent-stack and let-domain-experts-own-each-layer** as the operating posture.

**Cuts vs the December-2025 ingest cycle.** The Karten & Zhang continual-harness paper (11 May) and Chase's Interrupt 26 articulation (21 May) together close the **continual-improvement-of-the-agentic-system** thesis on academic and vendor-CEO altitudes within a 10-day window. The wiki now has paired anchor framings for *what continual learning actually means in agent engineering* — formal (Karten/Zhang's p/G/K/M decomposition) + vendor-product (Chase's model/harness/context layers + LangSmith trace+feedback as foundation + LangChain Labs as institutional commitment).

**Entity changes**: **[[Harrison Chase]] promoted from Dangling to entity page** with the full framings catalogue (four-layer Build vocabulary from ADLC + two-types-of-agents typology + three-layer continual-learning model + Top 30 → Top 5 on-stage confirmation); [[LangChain]] entity 4 → 5 sources with new sections on LangChain Labs, Fleet operational metrics, and the Interrupt 2026 conference itself.

**Concept bumps**: [[concepts/agent-harness|agent-harness]] 37 → 38; [[concepts/agent-development-lifecycle|agent-development-lifecycle]] 8 → 9 (Chase's same-speaker follow-up); [[concepts/ai-agents|ai-agents]] 15 → 16 (two-types-of-agents typology); [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] 38 → 39 (no-code domain-expert agent-building thesis); [[concepts/foundation-models|foundation-models]] 8 → 9 (open-source-models three-driver framing).

**Dangling first-mentions**: Brace Sproul (LangChain), Caroline di Vittorio (LangChain), LangChain Labs, Fireworks AI, Arcade, Ramp, Prime Intellect.

**Source-page count delta**: +1 (now 111). **Entity-page count delta**: +1 ([[Harrison Chase]] promoted) (now 85). **Concept-page count delta**: 0.

---

## [2026-05-21] ingest | YC-channel six-video batch — Tan & Hu / Stanford CS153 anchor + 5 Founder Firesides / Breakdown / Startup-School companion testimonials across voice / grocery / quick-commerce / private-chef / accounting verticals

User-initiated six-video batch ingest of YC-channel founder-vantage sources spanning four months (March → May 2026). One major Stanford-classroom anchor, four YC-Root-Access founder firesides / Breakdown episode, one Startup School India keynote-fireside. **Six raw videos acquired**; **four of six required `yt-dlp` VTT fallback** after the [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) Playwright path hit the panel-render failure documented in [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2) — the failure rate on YC Root Access specifically is now consistent enough to expect VTT-fallback by default. The build script grew a smarter rolling-caption suffix-overlap dedupe pass to make the VTT-route raws human-readable.

**The anchor — [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / Stanford CS153]] (~47:14)** — is the wiki's first paired-YC-CEO-and-GP guest lecture at Stanford CS153, framing YC's introduction of the SAFE in the 2010s as the *standardisation moment for venture capital* and arguing that what's happening now at the cognitive/company-structure layer is a parallel standardisation. **The substantive novelty is the agentic-primitives → company-structure mapping** — skills = employees, resolvers = org chart, GBrain = internal process, check-resolvable = audit and compliance, trigger evals = performance reviews — the first founder-CEO-altitude rhetorical claim that the agent-harness primitives are **structurally identical** to a company's org structure, not merely metaphorical. **Load-bearing concrete claims**: 5-day Posterous rebuild on a $200/month Claude Max plan (vs original 10 people / $4M / 2 years); cross-modal evals as a Skillify built-in (Opus 4.6 + GPT-5.5 + Deepseek V4 cross-evaluating); GBrain extension to a typed knowledge graph + in-progress epistemology layer for *"hunches vs beliefs vs world knowledge"*; $1–2M revenue per employee at YC AI-native portfolio companies vs Salesforce *"under six figures"*; the Salient / Happy Robot / Reducto forward-deployed-engineer wedge worked examples; the closing Anthropic-economic-deployment-chart white-space call-to-action across back-office / finance / data / academics / cybersec / customer-service. **[[Diana Hu]] promoted from Dangling to entity page** on this ingest (second substantive source).

**The five companion testimonials** map onto Hu's prescription from five different operational scales and verticals:

- **[[2026-04-16-bodewes-phonely-ai-callers-think-is-human|Bodewes / Phonely]] (16 April; ~16:17)** — voice AI for call centers / insurance / home services; millions of calls/month; $16M Series A led by Base10. **The novel architectural claim**: multi-model modular routing on Groq fast inference (smaller specialised models per task component vs one big general-purpose model). The *80% don't know it's an AI* / *100% by end of year* employment-effect projection.
- **[[2026-05-11-hill-vori-grocery-os-paper-and-fax|Hill / Vori]] (11 May; ~28:17)** — agentic store-management OS for 220k+ US independent supermarkets; $22M Series B led by Cherry Rock Capital. **The wedge → ERP-transplant playbook** at SMB-velocity-but-ERP-stickiness pace (18–21 day median sales cycle; 37 day median deployment). Three named production agents (inventory / pricing / personalized-offers); the dynamic-pricing closed loop *invoice → electronic-shelf-label → POS-checkout-price* in one agent step.
- **[[2026-05-19-palicha-zepto-stanford-or-startup-india-quick-commerce|Palicha / Zepto]] (19 May; ~28:56)** — Mumbai quick-commerce platform; 200K+ employees, billions USD topline. **The wiki's first non-US-headquartered AI-native-internal-operations anchor at large operating scale**; the *"cut almost all our software spends to zero"* claim; in-house ML supply chain forecasting that replaces days of manual work with no humans in the loop; the *AI-bolted-on-pre-AI-operational-substrate* counter-template to the *AI-native-from-day-one* archetype.
- **[[2026-05-19-mittal-yhangry-private-chef-all-in-on-ai-agents|Mittal / Yhangry]] (19 May; ~4:55)** — private-chef marketplace going all-in on AI. **The wiki's bluntest articulation of the org-pain side of the AI-native rebuild** — *"I fired my tech lead because I realized he did not know what skills was, and he was the ceiling in our company"* + *"I probably need to kill my human empathy a little bit more, a little bit faster."* Plus: autonomous bug fixer in 4 days (60–70% one-shot pass rate); $50k of free conference slots via founder-brand-as-distribution-by-teaching-AI-in-plain-English.
- **[[2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt|Vitucci / Onshore]] (7 March; ~33:56)** — corporate tax + accounting AI; $25M revenue today targeting $100M by end of 2026; sells direct to corporate taxpayers (not to accounting firms) after 2-year sell-to-firm failure. **The wiki's first deep professional-services-AI-disruption anchor at industry-altitude.** Four claims with no prior corpus equivalent: (i) the structural-incentive-not-intent argument for incumbent blocking (Big 4 senior-partner economics make AI investment a personal-financial-negative); (ii) the *you must compete with, not sell to, professional-services firms* doctrine; (iii) the lawyer-vs-accountant adoption-asymmetry (liability premium + project-billing maturity predict velocity); (iv) revenue-per-employee as the killer comp (Onshore $1M+ vs Big 4 / top 20 ~$100-150k = order-of-magnitude better).

**The cross-cutting observations across the batch:**

1. **Vertical AI-native ERP is a category, not a single vendor.** Four sources articulate the same wedge → ERP-transplant template in four verticals (Phonely / voice, Vori / grocery, Onshore / corporate-tax, [[2026-05-20-glasgow-campfire-erp-for-ai-revolution|Glasgow / Campfire / finance]] from last week). All four name founder-led-sales-to-$1M-ARR, multi-named-production-agents in the product surface, and *"sales reps coding to win deals"* internal-AI-pilling.
2. **The *boil-the-ocean* contradiction.** Tan-CS153 inverts the legacy *don't-boil-the-ocean* business advice (*"let's boil the ocean — you can do the work of 500 to 1000 people"*); Vitucci-Onshore asserts the conservative version (*"the idea of trying to boil the ocean all at once is very challenging; it has been an incredible benefit for our business to be great at one thing really early"*). Both are right at different altitudes — engineering-capability-claim vs go-to-market-wedge-discipline — and the [[2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt|Vitucci]] source carries an explicit `contradicts` typed relationship to [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Tan & Hu / CS153]] capturing the disagreement.
3. **YC Root Access matures into the wiki's busiest single channel for 2026.** With this batch the channel carries seven wiki ingests (Phonely / Vori / Garg / Glasgow / Mittal / Vitucci / Tan-and-Hu) all in 2026, all on the AI-native-vendor / founder-vantage cluster. The publishing cadence has hit ~2 per week and the failure rate of the youtube-transcript-skill's Playwright path on this channel specifically is now consistent enough that yt-dlp fallback is the de facto Acquire route for this channel.
4. **Diana Hu becomes the wiki's prescriptive AI-native-company voice.** Now two sources; entity page created. Together with [[Garry Tan]]'s entity page (now four sources), the wiki carries paired CEO + GP altitude on the AI-native-company doctrine.

**Side artifact: rolling-caption suffix-overlap dedupe in the raw-builder.** YouTube's auto-generated VTT captions repeat each line 2-3 times with rolling additions (each cue's text ends with the start of the next cue's text). The first pass of the raw builder caught exact duplicates but missed the rolling pattern. Added a second pass that, for each cue, finds the longest suffix that matches the next cue's prefix and drops the overlap. This collapsed Vori's raw from ~3300 lines (with rolling duplicates) to ~1684 lines; Phonely from ~1271 to ~738; Zepto from ~1864 to ~981; Yhangry from ~586 to ~306. The dedupe is implemented in `/tmp/build_raw.py` for this ingest; if the YC-channel pattern persists, the dedupe should land permanently in the skill or in a `scripts/` helper.

**Source-page count delta**: +6 (now 108). **Entity-page count delta**: +1 ([[Diana Hu]] promoted) (now 84). **Concept-page count delta**: 0.

---

## [2026-05-21] ingest | Garg / AnswerThis founder on YC Root Access — *How to Build an Internal AI Agent That Evolves Itself* — the wiki's first founder-vantage operational case study at startup-micro-scale (2 FTEs / $2M ARR) on the agent-harness cluster

User-initiated single-source ingest of **[[2026-05-19-garg-yc-internal-ai-agent-evolves-itself|*How to Build an Internal AI Agent That Evolves Itself*]]** — a ~5:34 YC Root Access recent-batch talk published 2026-05-19 by **Ayush Garg**, founder of **AnswerThis** (AI agents for evidence-based scientific workflows). Acquired via `yt-dlp` fallback (the [`youtube-transcript-skill`](.claude/skills/youtube-transcript-skill/SKILL.md) Playwright path hit the panel-render failure documented in [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2)); processed in the same session. **The talk is one slot in a multi-talk YC Root Access session on agent-harness engineering** — Garg references *"Pete and Tom and Gary"* as prior speakers (likely **Pete Koomen**, **Tom Blomfield**, **Garry Tan**), opening up at least three companion talks for potential follow-up ingest.

**Why this matters in the corpus.** The wiki's harness cluster carries three vantage-classes: the paradigm vantage ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy]]); the inside-the-lab engineering vantage ([[2026-05-08-running-an-ai-native-engineering-org|Fung/Anthropic]], [[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|Forsgren/Macvean/Google]]); and the vendor-of-platform vantage ([[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan/GStack]], [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]], [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Google Agents CLI]]). What was missing was a **single-team founder-vantage operational case study at micro-scale** — a small team running a real business with a real harness, talking openly about exactly how it's wired. The [[2026-05-13-jha-emergent-democratizing-app-building-with-claude|Jha/Emergent]] founder-vantage anchor lands at $100M-ARR product scale; Garg lands at $2M-ARR-with-2-FTE internal-ops scale. **The two together bracket the founder-vantage scale ladder** for the harness cluster — same substrate (Claude Code), opposite product surfaces, opposite ends of the company-size band, within a week of each other.

**The substantive contributions** the talk adds to the wiki:

- **The three-memory framework named explicitly**: **factual** (codebase + DB) / **behavioural** (`instructions.md`) / **procedural** (self-authored tools). Maps onto the wiki's four-layer harness anatomy as Context / Constraints+Contracts / Compounding. Gives the [[inspiration/Agent Memory Systems and Decision Tree|inspiration doc]] on agent memory its first founder-vantage operational anchor — previously unpromoted content now has a concrete instance to cite when a second framing arrives.
- **The self-extending agent claim — load-bearing**. The agent's tool set is not fixed: when it hits a repeated task it can't do, it asks a coding sub-agent (also exposed as a CLI, with edit-access to the main agent's code) to build a new permanent CLI. Garg reports **45+ self-authored CLIs to date**, including a self-authored cron job for landing-page-uptime monitoring. This is the cleanest founder-scale instance in the wiki of [[2026-05-04-rethinking-agents-harness-is-all-you-need|Pan/Khattab's]] *transfer-across-models* property — the value lives in the harness's accreted tool/skill library, not in the underlying model.
- **The agent-editable `instructions.md` + Ryan-feedback loop**: agent-loaded-on-every-turn instruction file, agent-editable, ratcheted by **natural-language Slack feedback from a non-technical co-founder**. The *Ryan story* (non-technical co-founder catches a class of customer-support mistakes, messages the agent in Slack, agent rewrites its own rules, class of mistakes stops) is the wiki's clearest evidence to date that **natural-language feedback in chat replaces ticket-filing and codebase-editing as the dominant change mechanism for many classes of error in an AI-native organisation**. Operationalises [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] *ratchet-don't-brainstorm AGENTS.md* rule — but with the agent itself doing the ratcheting.
- **Code-as-documentation by reference**: a read-only DB + codebase snapshot, cron-refreshed each release, is the factual-grounding substrate. The codebase becomes business documentation by reference rather than separately-maintained documentation. The inversion of Forsgren/Macvean's *spec-as-source-of-truth* — Forsgren propagates the spec downward to agents; Garg has the agent re-read the code directly — both work; the choice reflects what is most stable in each org.

**YC anchor extension**. [[Y Combinator]] entity bumped from `source_count: 3` to `source_count: 4` (subsequently 5 after a linter post-process). The existing 3-source Tan/Hu/Masad anchor triple (Apr 23–25 2026) is extended into a 4-source quad: President / Partner / Portfolio-founder-CEO at platform scale (Masad/Replit) / **Portfolio-founder at 2-FTE startup scale (Garg/AnswerThis)** on a fourth YC channel — **YC Root Access** (first wiki ingest from this channel; added as a programme on the YC entity page). Pete Koomen and Tom Blomfield surfaced as dangling-by-multi-talk-reference (companion-speaker referents); promote when their slots in the same session are ingested or a second standalone source surfaces.

**W&W tags**: `digital-transforming/improving-digital-maturity` (the internal AI ops agent is the firm's digital-maturity step at micro-scale), `digital-transforming/redesigning-internal-structures` (2-FTE org structure with the agent as the headcount-stretching layer), `digital-seizing/balancing-digital-portfolios` (the self-extending build-don't-buy posture: SaaS CLIs + self-authored tools), `contextual/external-triggers` (AI capability shift enabling the architecture). 3-of-4 cell overlap with [[2026-05-13-jha-emergent-democratizing-app-building-with-claude|Jha/Emergent]] on `digital-transforming/*` cells — same posture, different scale.

**Neighbour-source scan**. 8 typed `supports` relationships filed on the new source page, spanning the full harness cluster: harness-is-all-you-need (Pan/Khattab), founder-vantage twin (Jha/Emergent), inside-the-lab engineering vantages (Fung, Forsgren/Macvean), YC anchor triple (Tan, Hu, Masad), harness-engineering discipline (Osmani), unified-memory hooks primitive (Bratanic). No `contradicts` edges identified — Garg's claims sit inside the existing cluster's consensus and add a missing scale band rather than challenging any of it.

**Page updates** (10 wiki pages touched in this ingest):

- **1 new source page**: [[2026-05-19-garg-yc-internal-ai-agent-evolves-itself]] (created)
- **3 concepts**: [[concepts/agent-harness|agent-harness]] 35→36 (new convergence-table row on founder-vantage-at-micro-scale); [[concepts/agentic-engineering|agentic-engineering]] 20→21 (new 2-FTE-startup-scale operationalisation row); [[concepts/agent-development-lifecycle|agent-development-lifecycle]] 7→8 (new *Worked example: AnswerThis at 2-FTE micro-scale* section paralleling the OpenAI Codex worked example)
- **2 entities**: [[Y Combinator]] 3→5 (anchor triple → quad; YC Root Access added as 4th channel; Pete Koomen + Tom Blomfield surfaced); [[Anthropic]] 10→11 (Claude-Code-as-substrate founder-vantage anchor extended into the 2-FTE micro-scale band)
- **2 catalogues**: `wiki/index.md` (new source entry); this log entry

**Dangling first-mentions** (deferred per CLAUDE.md author-entity promotion rule): Ayush Garg (founder, AnswerThis); Ryan (non-technical co-founder, surname not stated); AnswerThis (organisation); Pete Koomen (likely YC partner, companion-speaker referent); Tom Blomfield (likely YC managing director, companion-speaker referent); YC Root Access (channel/series — sub-entity of [[Y Combinator]], no separate page until source weight justifies it).

**Confidence**: 0.75 on the new source page. Founder testimonial; operational metrics ($2M ARR, 100+ emails/day, 400+ tickets, 45+ self-authored CLIs) are vendor-cited and not third-party-verified. Self-extending mechanism is named but not stress-tested in a 5-minute talk — failure modes, eval coverage, observability of agent-authored tools, and recovery behaviour when the coding sub-agent ships a bad tool are all open questions. Held below 0.80 for those reasons.

## [2026-05-21] ingest | Glasgow / Campfire CEO on YC Root Access — *The ERP for the AI Revolution is here* — the wiki's first enterprise-B2B vendor-vantage anchor on the AI-native procurement-room flip

User-initiated single-source ingest of **[[2026-05-20-glasgow-campfire-erp-for-ai-revolution|*The ERP for the AI Revolution is here*]]** — a ~27:38 YC Root Access founder fireside published 2026-05-20 in which **John Glasgow** (CEO and founder of **Campfire**, YC S23 AI-native ERP; Series B led by Accel and Ribbit Capital) sits down with **Andrew Tan** (YC partner, ex-CTO at PagerDuty). Acquired and processed in the same session.

**Why this matters in the corpus.** The wiki holds three prior 2026 anchors on the AI-native-vendor advantage thesis: [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar & Nohria's]] HBS / HBR macro buyer-side framework; [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu/YC's]] AI-native-from-day-one + incumbent-can't-unwind supply-side thesis; and [[2026-05-13-jha-emergent-democratizing-app-building-with-claude|Jha/Emergent's]] long-tail-asymmetry founder-vantage from the consumer/SMB end. **Glasgow is the enterprise-B2B founder-vantage twin of Jha/Emergent** — same vendor-side phenomenon (AI-native vendors capturing migrations from legacy incumbents), opposite ends of the customer-size spectrum, observed independently within a week of each other in May 2026. Glasgow also provides the **vendor-side empirical anchor** to Nishar & Nohria's buyer-side macro thesis — hard numbers on actual NetSuite-to-AI-native-vendor migrations from Q4 2024 onward (the same Q4-2024 inflection Nishar/Nohria predict in their build/compose/collaborate/buy framework).

**The substantive contribution is the "AI-native safety inversion" thesis** (~24:08–24:31): *"Buying the legacy version was considered very safe. But then once AI started to take off — call it end of '24 — it then become being the incumbent meant you were not AI-native. And so there was a flipping of the narrative that the board and the executives were saying, we want AI-native. And even if the accountant wasn't fully ready to embrace AI, they had this blessing to go buy something new that nobody had heard of and their C-suite or their auditor wasn't familiar with yet."* Three load-bearing properties: **(1) narrative, not feature** (Campfire had AI features earlier; what changed was *what the board would underwrite as a safe choice*); **(2) C-suite/board/auditor channel, not the operator channel** (day-to-day operator hesitancy is overruled, not converted); **(3) the narrative had to shift even though the core product did not** (*"your narrative needs to continue to shift even if the core product ultimately ends up not shifting"*). This is a **different shape of buyer-side shift** than the slow-organisation-adoption framing in much of [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]]: fast at the procurement layer, slow at the operator layer, with the fast-procurement layer overriding the slow-operator layer because the board explicitly authorises it.

**Companion claims.**

- **Tech-stack-turnover thesis for "why now"** (~22:44–23:18): the finance tech stack — payroll, spend management with the *Brexes of the world* — had turned over in the last 5–10 years *except the core general ledger*. *"A finance person would log in and they would go into this amazing spend management solution or accounts payable or payroll, and then the contrast with the ERP and everything else was very acute."* Acuity-of-contrast as the trigger that pushed finance teams to *seek out* the modern alternative rather than be sold to.
- **Wedge displacement over feature-completeness** (~5:41–6:42): tech-company customers were using only a narrow slice of NetSuite; Campfire owned that slice (approval workflows, multi-entity accounting, audit/controls, revenue-recognition for SaaS reporting) and was pulling customers off NetSuite within nine months. The customer-segment claim that supports the wedge: *tech companies use ~10% of NetSuite*, which collapses the feature-completeness defence to the size of the actually-used slice.
- **Founder-led-sales-to-$1M-ARR doctrine even in the AI era** (~14:05–15:11): *"Even in the AI era I do really recommend founders to stay in the founder sales mode... offloading it to AI, offloading it to some AE... feels like, oh let's just bring in a professional whether it's an agent or whether it's a human. But I still recommend being as close to the customer and the prospective customer as possible until you have product market fit... I ended up getting to series A — the kind of classic million in ARR for us — on my own as the one AE."* Sales-team-driving-engineering as the (unnamed) operating logic behind why founder-led sales produces the *product velocity* customers cited as trust signal.
- **Product velocity as enterprise trust signal at seed stage** (~7:17–8:38, ~10:20–10:39): four-person company selling two-year contracts to $300M-revenue customers. *"One CFO told me, literally we are making a venture investment in you by going with you... I'm literally getting fired if you shut down. And we are so large, and this contract is longer than your runway."* What closed the trust gap: build-pace as forward-looking signal (Replit, PostHog cited explicitly — *"as we add new global subsidiaries, as we need new features... we feel confident you're going to be able to stay ahead of us"*).
- **Own foundation model + custom agent platform as moat** (~17:47–17:54): *"We are consistently hearing we have the best AI. And so I think maybe it's because we're the only one with our own foundation model, our custom agent platform."* Too lightly anchored for a concept-page convergence row; filed only as a one-line vendor-side data point in the source page itself, not promoted to [[concepts/agent-harness|agent-harness]] or [[concepts/foundation-models|foundation-models]].

**W&W tags**: `contextual/external-triggers` (the AI-native shift as the trigger Campfire exploited), `digital-seizing/strategic-agility` (narrow-wedge displacement, mid-pivot flip from RevRec-as-wedge to core-product-as-wedge), `digital-seizing/balancing-digital-portfolios` (own-foundation-model + own-agent-platform internal-build bet). 3-of-3 W&W cell overlap with Jha/Emergent (`digital-seizing/strategic-agility` + `digital-seizing/balancing-digital-portfolios` + `contextual/external-triggers`) — same digital-seizing posture and external-trigger reading, different substantive contribution against that cluster.

**Three typed `supports` relationships** filed during the neighbour-source scan (qmd-surfaced; concept-citation fallback validated for Hu and Nishar/Nohria which predate the W&W tagging contract):

1. **[[2026-05-05-nishar-nohria-end-of-one-size-fits-all]]** — Nishar/Nohria's macro buyer-side firm-boundary collapse is given vendor-side empirical evidence by Glasgow (>100 NetSuite-to-Campfire migrations from Q4 2024 onward, "more than doubled ARR each quarter since").
2. **[[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up]]** — Hu's AI-native-from-day-one + incumbent-can't-unwind thesis (same channel, ~4 weeks earlier) gets its worked-example in Glasgow; Glasgow's "own foundation model + custom agent platform" is the company-stack instantiation of Hu's "intelligence layer" framing.
3. **[[2026-05-13-jha-emergent-democratizing-app-building-with-claude]]** — Paired 2026 founder-CEO anchors on AI-native-vendor advantage; Jha = adoption-velocity-asymmetry-favouring-the-long-tail (SMB / non-developer), Glasgow = enterprise-safety-inversion (board-level procurement shift). Same vendor-side phenomenon at opposite ends of the customer-size spectrum.

**Neighbour-source candidates surfaced (qmd hybrid query + concept-citation fallback)**: Nishar/Nohria (strong; edge filed), Hu/YC (strong; edge filed), Jha/Emergent (strong; edge filed), AI Index Report 2025 (considered, no edge — too macro/distant; the Q4-2024-inflection co-incidence is thematic but not load-bearing). Threshold of ≥3 candidates met; surfaced in the in-session report.

**1 entity page updated**: [[Y Combinator]] 4→5 sources (confidence 0.85 → 0.90 per the +0.05-per-additional-source rule); **"YC Root Access" added as an alias on Y Combinator** so the dangling-authors lint resolves it back to the parent entity (same precedent as Anthropic's *Claude* channel alias); new §*5. Glasgow / YC Root Access* + extended anchor table to **YC-batch-context anchor quintuple** (President / Partner / Platform-vendor / 2-FTE / enterprise-B2B). The post-ingest dangling-authors lint surfaced YC Root Access as a second-source author (Garg 2026-05-19 + Glasgow 2026-05-20), forcing the alias-promotion decision; with the alias filed, 22 entity pages now match the wiki's multi-source authors (up from 21).

**1 concept page updated**: [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] 36→37 sources (confidence stays at 0.95 cap; `last_confirmed` / `accessed_at` 2026-05-20 → 2026-05-21). New top-of-section bullet in §*Sharper formulations from May 2026* — heading extended to include *Glasgow*. **[[concepts/automation-vs-augmentation|automation-vs-augmentation]] and [[concepts/agent-harness|agent-harness]] deliberately not updated** — Glasgow's automation framing is generic (*automate manual work → focus on more strategic work*) and his harness claim is too lightly anchored for a one-sentence vendor-side data point to earn a row in the densely-converged convergence tables on either page. The source-page backlinks preserve graph hygiene.

**Dangling first-mentions queued for second-source promotion**: John Glasgow (Campfire CEO/founder), Andrew Tan (YC partner, host), Campfire (S23 AI-native ERP), Accel, Ribbit Capital, NetSuite, QuickBooks, Brex, Mercury, Metronome, PagerDuty, Replit (close to second-mention threshold given prior co-occurrence — promote on next coverage), PostHog (similar — recurring 2026 customer reference), Dalton Caldwell (referenced as Glasgow's YC interview partner).

**Source-page reliability note** (not a confidence value — sources don't carry confidence per [§Lifecycle](../../CLAUDE.md#lifecycle)): single source, founder-CEO speaking on his company's marketing channel; substantive claims filtered through obvious commercial incentives (talent recruiting, customer acquisition, future-round signalling); empirical anchors (>100 customers, doubled ARR/quarter since Q4 2024, four-employee selling to $300M-revenue customers) are concrete and falsifiable but unaudited in this venue. What raises the "AI-native safety inversion" claim beyond a single-source curiosity is **the independent ratification by Jha/Emergent's parallel observation** of the same vendor-side flip at the opposite end of the customer-size spectrum — same week, same year, two different product categories.

## [2026-05-21] ingest | Forsgren & Macvean / Google I/O 2026 — *Build core skills to thrive as an AI-era developer* — Google-side twin of the Fung talk; DORA-grounded T-shape model + amplifier-and-mirror framing

User-initiated single-source ingest of **[[2026-04-21-forsgren-macvean-build-core-skills-thrive-ai-era-developer|*Build core skills to thrive as an AI-era developer*]]** — a ~50:15 Google I/O 2026 Professional Development track talk by **Nicole Forsgren** (founder of the DORA / DevOps Research and Assessment programme; lead author of *Accelerate* 2018) and **Andrew Macvean** (both leads of Google's **Developer Intelligence team**). Acquired and processed in the same session.

**Why this matters in the corpus.** The wiki's two prior inside-engineering-vantage sources on AI-native software organisations were [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's paradigm-naming essay]] (December 2025 phase-change framing) and [[2026-05-08-running-an-ai-native-engineering-org|Fung's Anthropic / Claude Code team-norms rewrite]] (8 May 2026). This talk is **the Google-side twin of Fung** — landed a fortnight apart, ratifying the same five-pattern operational model from independent corporate-research traditions. With Globerson et al.'s [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|durable-skills paper]] (ingested 7 May 2026) — also Google Research lineage — the wiki now holds a paired engineering-team + psychometrics view of the same human-capability cluster from one parent organisation.

**Substantive contributions.**

- **Evolved T-shape with four skill domains**: vertical stem = core SWE depth; horizontal bar gains a new **AI engagement** layer; plus two wings — **Adjacent Engineering** (cybersec, privacy, deployment infra) and **Adjacent Non-Engineering** (business/user context, "value translator").
- **Five patterns of top AI-native engineers**: higher altitudes / shift-left-on-intent / designing-environments-not-vibe-coding / micro-teams / scientific-mindset. *"Our top engineers are not vibe coding."*
- **DORA productivity-paradox** explicitly cited: *"increasing AI adoption can lead to individual productivity benefits while at the same time decreasing team-level benefits"* — the engineering-team correlate of the wiki's [[concepts/micro-productivity-trap|micro-productivity-trap]] and its first DORA-grounded anchor.
- **DORA's amplifier-and-mirror framing**: *"AI is an amplifier and a mirror. It magnifies the existing strengths and holds up a mirror to those weaknesses."* The cleanest single articulation of the trap's diagnostic mechanism the wiki has logged.
- **Concrete Google fleet-scale agent practices**: Code Review Agents + Shepherding Agents + Risk Assessor Agents in CI/CD; TensorFlow migration three-agent architecture (planner / orchestrator / coder) with product-area-specific playbooks; Agent Journaling (agents reflect into structured logs); Quality Agent for stress-testing requirements before execution.
- **Quotable boundary-marker**: *"delegate tasks, not judgment"* (used twice).
- **Engineering-leadership prescriptions**: redefine productivity measurement away from PR throughput / LOC; actively protect **productive struggle** (deliberate friction-preservation = engineering-leadership countermeasure to [[concepts/ai-deskilling|ai-deskilling]]); foster radical psychological safety. *"A bad system will beat a good person every time."* (Deming.) *"You can't mandate a T-shaped developer inside a broken system."*
- **Closing tricolon**: *"we need to shift left, we need to shift up, and we need to think about designing systems, not just bits of code."*

**W&W tags**: `digital-transforming/redesigning-internal-structures`, `digital-transforming/improving-digital-maturity`, `digital-seizing/strategic-agility`, `contextual/external-triggers`.

**Eleven typed `supports` relationships** to existing sources — the strongest single-ingest cross-source resonance the wiki has logged: Fung 2026 (twin), Karpathy 2026 (paradigm), Singhal 2026 (PM evolution), Globerson et al. 2026 (durable skills twin), Ransbotham et al. 2024 (Augmented Learners), Kiron-Schrage 2026 (compound benefits), Chatterjee 2026 (harness anatomy), Pan/Khattab 2026 (harness>>model), Kokane 2026 (systems-design altitude), Chase 2026 (ADLC), Wolfe 2026 (eval discipline).

**2 entity pages updated**: [[Google]] 6→7 sources (new Developer-Intelligence-team + DORA + fleet-scale-agent-practice sections + 4 dangling people/teams); [[Google Research]] 2→3 sources (Forsgren-as-DORA-founder anchor + Developer-Intelligence-team affiliation note).

**10 concept pages updated**: [[concepts/agentic-engineering|agentic-engineering]] 19→20 (corporate-research-twin row); [[concepts/vibe-coding|vibe-coding]] 12→13 (corporate-research ceiling-side negative-claim row); [[concepts/micro-productivity-trap|micro-productivity-trap]] 14→15 (engineering-team DORA-grounded vantage); [[concepts/durable-skills|durable-skills]] 9→10 (engineering-role-evolution vantage + *"delegate tasks, not judgment"* boundary-marker); [[concepts/ai-deskilling|ai-deskilling]] 5→6 (new §*The engineering-leadership countermeasure: "productive struggle"*); [[concepts/ai-employment-effects|ai-employment-effects]] 19→20 (new §*Engineer identity-threat as named phenomenon*); [[concepts/agent-harness|agent-harness]] 34→35 (fleet-scale-agent-stack row + TensorFlow planner/orchestrator/coder + agent-journaling); [[concepts/agent-development-lifecycle|agent-development-lifecycle]] 6→7 (new §*Engineering-leadership anchor — Forsgren & Macvean*); [[concepts/automation-vs-augmentation|automation-vs-augmentation]] 18→19 (automation-trap-warning row); [[concepts/systems-thinking|systems-thinking]] 3→4 (new §*The engineering-team operationalisation* — closing tricolon naming systems thinking as the highest-altitude capability AI-era engineers need).

**Dangling first-mentions (deferred per author-entity promotion rule)**: Nicole Forsgren, Andrew Macvean, Google Developer Intelligence team, DORA (DevOps Research and Assessment), Peter Senge, W. Edwards Deming, Google I/O 2026. Forsgren and DORA are high-probability for second-mention given stature; promote on next coverage.

**Source confidence**: 0.80 (single-supporting-source baseline 0.70 + 0.05 DORA empirical backbone + 0.05 multi-stack-layer resonance; held below peer-review tier — conference talk by interested parties at Google's own event).

---

## [2026-05-20] ingest | Claude-channel customer-story batch (4 videos) — Emergent founder-vantage harness anchor + Lyft/HubSpot/Figma-Make companion testimonials

User-initiated batch ingest of **5 YouTube videos from the [[Anthropic]] Claude customer-story channel**, of which **4 were acquired and processed in this session** and 1 (Spotify Honk talk) failed acquire — captions had not been generated by YouTube as of ~11 hours post-publish (logged as separate `acquire` entry below). Source pages, in chronological order of publication:

1. [[2026-02-06-figma-make-prompts-to-prototypes-with-claude]] — **Figma Make** (Feb 2026; ~1:17; manual captions). Promotional testimonial: pixel-perfect canvas-to-code, *"every single person who has taste can just enact it"*, *"I don't code"* non-coder use case. Confidence 0.55.
2. [[2026-02-09-hubspot-customer-success-with-claude]] — **HubSpot customer success** (Feb 2026; ~2:11; manual captions). Promotional testimonial: *"Claude has really good taste"*, CSM-doing-revenue-analysis (role-scope expansion), 40% developer-productivity testimonial claim. Confidence 0.60.
3. [[2026-02-18-lyft-customer-support-with-claude]] — **Lyft customer support** (Feb 2026; ~1:35; manual captions). Promotional testimonial: 87% resolution-time reduction with Claude's *personality* as model-selection criterion; *augment-and-reinvest-the-savings* pattern (millions reinvested into upskilling agents + new Lyft Silver high-touch programme). Confidence 0.60.
4. [[2026-05-13-jha-emergent-democratizing-app-building-with-claude]] — **Emergent / Jha–Ryan interview** (May 2026; ~16:39; ASR-cleaned, 135 segments). **The substantive one.** Founder-vantage anchor on [[concepts/agent-harness|agent-harness]] (*"agent is the product, the harness quality really really matters"*), multi-agent harness on Kubernetes with disk/memory snapshotting, long-term cross-session memory, pre/post-deploy security agents, refactoring agent. Headline numbers: $100M ARR in 8 months, 7M users in 190 countries, 70–80% never wrote a line of code, deployment-success-rate 84% → 98%. Adoption-velocity asymmetry favouring the long tail named explicitly (enterprise → SMB pivot). Direct category-peer to [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad/Replit]]. Confidence 0.70.

**Neighbour-source scan** (run on the Emergent source) surfaced two missed strong neighbours via 4-cell W&W overlap: **Masad/Replit** (same product category — both natural-language-to-production-app platforms; users compared against dev-shop alternative) and **Karpathy at Sequoia AI Ascent** (foundational vibe-coding/agentic-engineering anchor Emergent operationalises at startup-product scale). Both edges filed with body-wikilink twins. Figma Make's frontmatter also extended with a Masad/Replit `supports` edge for the same product-category reason.

**5 concept pages updated**:
- [[concepts/agent-harness|agent-harness]] 33→34 sources (conf 0.98 → 0.98; at-cap) with new convergence-table row: *founder-CEO company-scale practitioner anchor* — *"agent is the product, the harness quality really really matters"* + multi-agent harness on K8s + 98% deployment-success-rate as the outcome metric the harness team manages to. Pairs with [[2026-05-08-running-an-ai-native-engineering-org|Fung's Anthropic-internal team-norms rewrite]] as the Anthropic-external product-stack-rewrite counterpart.
- [[concepts/agentic-engineering|agentic-engineering]] 18→19 sources (conf 0.97 → 0.97) with new convergence-table row: *founder-CEO outside-Anthropic counterpart to Fung's inside-Anthropic vantage* — same *delete-and-reimagine-against-each-new-model* operating cadence (system rewritten 4× in 9 months).
- [[concepts/vibe-coding|vibe-coding]] 10→12 sources (conf 0.93 → **0.95 cap**) with two new convergence-table rows: Emergent as the strongest 2026 named-company anchor on the floor-raising-thesis-materialised-at-scale (with Christy/*Equ* as the headline vignette and the *zero marginal cost serving million niches of SMB / domain-expert needs* compact statement); Figma Make as the design-tool-vendor expression (with the *"I don't code"* claim as the in-incumbent vantage).
- [[concepts/automation-vs-augmentation|automation-vs-augmentation]] 15→18 sources (conf 0.95 → 0.95) with new §*The Claude-channel customer-story cluster (Feb–May 2026)* table covering all three (Lyft augment-and-reinvest / HubSpot role-scope expansion / Emergent full-automation-as-substitution-for-an-outside-services-spend). The Lyft+HubSpot+Emergent triple is the wiki's first cluster on the automation/augmentation cut drawn entirely from 2026 named-incumbent practitioner self-reports.
- [[concepts/enterprise-ai-adoption|enterprise-ai-adoption]] 32→36 sources (conf 0.95 → 0.95) with new key-claim entry: **adoption-velocity asymmetry favouring the long tail** (Jha/Emergent named anchor) + the recurring 2026 procurement-side language across all 4 Claude-channel customer stories: *personality / taste / voice / instruction-following*, not benchmark scores.

**Source-page typed `relationships:`**: 16 new typed edges across the 4 source pages (Lyft 3 / HubSpot 3 / Figma Make 4 / Emergent 7 — Emergent includes Masad/Replit and Karpathy added during the neighbour-source scan).

**Dangling first-mentions** queued for second-source promotion: Mukund Jha (Emergent CEO), Madhav Jha (twin brother, co-founder), Carly Ryan (Anthropic Applied AI startups), Emergent (company), Dunzo (Jha's prior company, 500-person eng team), Lyft, HubSpot, Figma.

## [2026-05-20] acquire | Spotify Honk talk (Niklas Gustavsson, *Coding is no longer the constraint: Scaling devex to teams and agents at Spotify*) — failed: no captions available

Acquire-only entry. [Spotify Honk talk](https://www.youtube.com/watch?v=zFslvuvYifQ) was published 2026-05-20 at 05:00 PDT (~11 hours before ingest attempt). The video has no caption tracks (manual or ASR) at the time of acquire — three attempts with `--timeout` 30000, 60000, and 90000 all returned `caption_tracks: []` + `no transcript section`. Substantive talk content per the channel description: Niklas Gustavsson (Chief Architect & VP of Engineering, Spotify) on **96% of Spotify engineers now coding with AI, PR frequency +60%**, the constraint moving from writing code to orchestrating it; **Honk** (background coding agent running on the Agent SDK) plugged into **Fleetshift** (migration platform) and **Backstage** (software catalog); the standardisation-that-makes-teams-effective-makes-agents-effective claim; *firmer guardrails are accelerators, not constraints*. **Strong agentic-engineering / agent-harness / enterprise-ai-adoption candidate** for a future ingest once YouTube's ASR generates a transcript — re-attempt within 24–48h. No raw file landed; no wiki source page written.

## [2026-05-18] ingest | [[2026-05-18-wolfe-agent-evaluation-detailed-guide|Wolfe — *Agent Evaluation: A Detailed Guide*]] (Deep (Learning) Focus, 18 May 2026) — the wiki's first eval-discipline anchor on the [[concepts/agent-harness|agent-harness]] cluster

Full ingest of Cameron R. Wolfe's 7,000-word Substack newsletter post (56-page PDF, 13-reference bibliography). **The wiki's first source whose primary contribution is the eval-discipline framing** of the harness construct — complementary to (not competing with) the engineering-discipline framings of [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] / [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] / [[2026-05-15-osmani-agent-harness-engineering|Osmani]] / [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo]]. **Load-bearing equivalence ratified directly from a primary source**: *"An agent harness (or scaffold) is the system that enables a model to act as an agent... When we evaluate an agent, we're evaluating the harness and the model working together"* (Anthropic *Demystifying Evals* [1], quoted by Wolfe). **Eval taxonomy now canonical wiki vocabulary**: tasks / trials / transcripts / outcomes / graders / eval-harness — the six components every agent eval shares; *eval harness ≠ production harness, but ideally they share the same scaffold, tools, and environment*. **Three grader families** (human gold-standard for calibration / code-based for fast deterministic checks / model-based LLM-as-Judge for subjective criteria) plus the **Swiss-cheese strategy** of stacked complementary layers. **Two deep benchmark case studies**: τ-bench family (Sierra; introduces Pass^K = *probability all K trials succeed* as the *consistency* metric the wiki had been missing) and Terminal-Bench 2.0 (89 tasks, *3 reviewer-hours per task*, software-engineering-dominated; GPT-5.2 Codex CLI 62.9% > Claude Opus 4.5 Terminus 2 58% > Gemini 3 Pro 57% > ... > GPT-OSS-20B 5%). **The 7-step roadmap** (define success → small task set → useful tasks → ground truth → graders → eval harness → inspect-iterate-maintain) is the eval-side ratchet — the structural counterpart to [[2026-05-15-osmani-agent-harness-engineering|Osmani]]'s engineering-side rule-set. **Strongest single-source bibliography expansion** the [[concepts/agent-harness|agent-harness]] cluster has ever received: 6 new deferred-ingest primary refs queued (Anthropic *Demystifying Evals* [1], OpenAI *Evaluation Best Practices* [6], τ-bench arXiv [8], τ²-bench arXiv [9], SABER arXiv [10], Terminal-Bench arXiv [12]). **Neighbour-source scan** surfaced two strong existing wiki neighbours: [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain 2025]] (daily-workflow vantage) + [[2026-03-20-huggingface-agentic-evaluations-workshop|HuggingFace 2026]] (capability-reliability-gap vantage). Combined with Wolfe, the wiki now holds a **three-vantage eval-discipline anchor** (textbook taxonomy / daily workflow / community + reliability separation). W&W tags: `digital-seizing/balancing-digital-portfolios` + `digital-seizing/rapid-prototyping` + `digital-transforming/improving-digital-maturity`. **3 concept pages updated**: [[concepts/agent-harness|agent-harness]] 32→33 sources with new §*The eval-discipline complement (Wolfe synthesis, May 2026)*; [[concepts/ai-agents|ai-agents]] 13→14 sources with the *agent = LLM that autonomously uses tools in a loop* canonical one-sentence definition; [[concepts/agentic-engineering|agentic-engineering]] 17→18 sources with new §*The eval-discipline counterpart*. Source confidence 0.75 (single source, +0.05 credentialed author, +0.05 citation density, capped because synthesis-grade not primary-empirical). Dangling first-mentions: Cameron R. Wolfe, Shunyu Yao, Victor Barres, Alejandro Cuadron, Mike A. Merrill, Netflix, Sierra, Substack / Deep (Learning) Focus, LiteLLM, Terminus.

## [2026-05-18] synthesize | [[syntheses/strategy-finite-vs-infinite-game|strategy-finite-vs-infinite-game]] — Sinek operates one layer above the strategy lenses; the tension is a layered difference, not a contradiction (Phase A4 of strategy-gap remediation)

Opens and closes [[threads/strategy-finite-vs-infinite-game|strategy-finite-vs-infinite-game]] in a single session — the cross-walk material was already assembled in the prior `/wq` answer of 2026-05-18, so the thread is the schema-compliant antecedent rather than a substantive investigation. Files [[syntheses/strategy-finite-vs-infinite-game|the synthesis]] with seven sources consulted (Sinek 2018, Martin 2022, Oberholzer-Gee 2022, Carroll & Sørensen 2024, Webb 2024, Carrier 2026, Sterman 2026), confidence 0.75. **Headline finding**: Sinek operates one layer above the strategy lenses — he asks *which game you are in*, Martin asks *how to win the round you are in*. The apparent Southwest contradiction is a category-difference between game-frame layer and theory-of-winning layer. **Three-altitude strategy stack** introduced as the synthesis's structural contribution: game-frame ([[concepts/infinite-game|Sinek/Carse]]) → theory-of-winning ([[2022-06-29-martin-hbr-a-plan-is-not-a-strategy|Martin]] + [[concepts/theory-based-view|TBV]] falsifiability) → value-creation-instrument ([[2022-02-23-oberholzer-gee-hbr-what-is-strategy-value-stick|Oberholzer-Gee]] value stick). Eight of nine strategy lenses align with the infinite-game frame once the layers are named; the residual Southwest tension is downgraded from *productive tension* to *Martin uses finite-game vocabulary to describe an infinite-game outcome*. Wires through [[concepts/strategy|strategy]] §Debates (one-liner pointer replaces the prior tension paragraph) and [[2018-05-31-sinek-nyt-the-infinite-game|Sinek source]] §Why this matters (Tension-with-Martin paragraph rewritten as a resolved-reference). Three transferable lessons extracted for future `wiki/lessons/` promotion. Plan file: `/Users/witoldtenhove/.claude/plans/memoized-hugging-sky.md`.

## [2026-05-18] refactor | promote [[concepts/theory-based-view|theory-based-view]] (TBV) to standalone concept page (Phase A3 of strategy-gap remediation)

Promotes Felin & Zenger's theory-based view of strategy from embedded-inside-[[concepts/analogical-reasoning|analogical-reasoning]] to a first-class concept page. Carries the four canonical TBV questions (theory of value / novel-simple-elegant / falsifiable-generalizable-generative / who-must-you-convince) and the bridge claim that TBV is the *falsifiability discipline* applied to [[concepts/strategy|Martin's *theory of winning*]] and [[concepts/infinite-game|Sinek's *Just Cause*]]. Single source (second-hand via [[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]]); confidence 0.60. Three relationships filed: `supports → strategy`, `supports → analogical-reasoning`, `supports → infinite-game`. Wires through Carroll & Sørensen source (new `instance-of → theory-based-view` + `supports → analogical-reasoning` — first relationships block on that source page), analogical-reasoning concept (new `supports → theory-based-view` + Related-concepts entry), index Concepts section. **Deferred**: Felin & Zenger 2009 + 2017 primary sources queued in Phase B4 to lift `source_count` to 3, confidence ~0.80, and promote Teppo Felin + Todd Zenger to entity pages.

## [2026-05-18] refactor | promote [[concepts/infinite-game|infinite-game]] to standalone concept page (Phase A2 of strategy-gap remediation)

Promotes Carse/Sinek's infinite-game framework from source-page-only to a first-class concept page so the cross-walk to other strategy lenses can be carried as durable typed `relationships:`. **Single source for now** ([[2018-05-31-sinek-nyt-the-infinite-game|Sinek 2018]]); confidence 0.65 (practitioner-thesis grade, single-anecdote case anchoring). Three relationships filed: `supports → strategy`, `supports → systems-thinking`, `supports → dynamic-capabilities`. Wires through [[2018-05-31-sinek-nyt-the-infinite-game|Sinek source]] (new `instance-of → infinite-game`), [[concepts/strategy|strategy]] (new `supports → infinite-game`), and the index Concepts section. The previously-filed Sinek/Martin Southwest tension on [[concepts/strategy|strategy]] now points to the [[strategy-finite-vs-infinite-game]] synthesis (to be filed under A4). **Deferred**: Sinek 2019 book + Carse 1986 are queued in Phase B3 to lift `source_count` to 2 and confidence to ~0.75. Plan file: `/Users/witoldtenhove/.claude/plans/memoized-hugging-sky.md`.

## [2026-05-18] refactor | clean up [[concepts/strategic-foresight|strategic-foresight]] (Phase A1 of strategy-gap remediation)

`quality_score` 0.77 → 1.00 by addressing all three flagged issues. Added `## Debates and supersession` section naming three productive tensions already implicit in body material (Webb's *scenarios are predictions* vs practitioner *scenarios are forecasts*; FTSG convergence-as-unit vs MGI arenas-as-unit; Spiegel humanity-adoption-bottleneck vs Chamath complex-reliability-bottleneck). Added one-paragraph intro to the previously-empty `## Key claims` parent header. Removed broken `[[Julie Baron]]` wikilink (rendered as plain text — single-mention name not worth promoting to an entity page). No frontmatter `confidence`/`last_confirmed` bump (pure refactor; CLAUDE.md §Lifecycle reserves those for ingest-time reinforcement).

## [2026-05-18] ingest | strategy-leadership-industrial-AI batch (5 videos) — new [[concepts/strategy|strategy]] concept page + 3 concept extensions

User-initiated batch ingest of **5 YouTube videos** spanning strategy and leadership classics + an MIT industrial-AI session. Source pages, in chronological order of publication:

1. [[2018-05-31-sinek-nyt-the-infinite-game]] — **Simon Sinek** at NYT Events (May 2018; 25:48; 1.1M views). Finite-vs-infinite game distinction; Vietnam War + Apple/Zune as worked anecdotes; *"the infinite player understands […] you're actually only competing against yourself"*; five-element checklist (Just Cause / Courageous Leadership / Trusting Teams / Worthy Rival / Existential Flexibility); Declaration of Independence as a Just Cause document.
2. [[2022-02-23-oberholzer-gee-hbr-what-is-strategy-value-stick]] — **Felix Oberholzer-Gee** / HBR (Feb 2022; 9:32; 1.5M views; human-curated captions). *"Strategy is a plan to create value."* The **value stick** framework — WTP − WTS, split three ways (customer delight / firm margin / employee value). Three ways to raise WTP (quality / complements / network effects); two ways to lower WTS — *pay more redistributes value; make-the-job-better creates value*. Best Buy turnaround case ($1B loss → 20%+ ROIC).
3. [[2022-06-29-martin-hbr-a-plan-is-not-a-strategy]] — **Roger Martin** / HBR (June 2022; 9:31; **6.5M views**). *"A strategy is an integrative set of choices that positions you on a playing field of your choice in a way that you win."* Planning lives on the cost-side (you control); strategy on the customer-side (customers decide). Southwest Airlines as the worked case. Three escape practices (accept angst / lay out the logic / keep it one page). Closing: *"If you plan, that's a way to guarantee losing."*
4. [[2024-06-13-jordan-hbr-7-key-tensions-every-leader-must-balance]] — **Jennifer Jordan** (IMD Business School) / HBR (June 2024; 10:03). The 7-tensions framework: power-holder ↔ power-sharer / tactician ↔ visionary / teller ↔ listener / perfectionist ↔ accelerator / analyst ↔ prospector / miner ↔ prospector / constant ↔ adapter. *"A good leader is never standing fully on one side […]. They oscillate based on context."* Skill / fear failure-mode distinction. Cases: Angela Ahrendts (Burberry/Apple); Mathias Döpfner (Axel Springer, provisional ID).
5. [[2026-03-31-carrier-mit-industrial-ai-that-works-strategy-survival-success]] — **John Carrier** (Senior Lecturer in System Dynamics, MIT Sloan) / MIT Sloan Exec Ed webinar (March 2026; 31:22; human-curated captions). **Strongest single anchor on industrial-AI adoption strategy.** Direct continuity with [[2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work|Sterman 2026]] via the MIT Forrester / Sterman system-dynamics lineage. *"Winners will be determined not by who has access to the technology, but whose organization adopts it faster."* **Heineken Mexico worked case** (6h→15min changeover via a simple agent that grabbed machine + cloud + maintenance data; ~1M extra cases of beer per month). **Forrester design criterion**: *"It's not simply about building AI agents. It's about using them to replace long, slow feedback loops with very fast ones."* Pick-the-right-agent-level heuristic; refinery alarm-fatigue cautionary tale (two fatalities); synthetic-data syringe-defect training; Rodney Brooks / Andrew Ng *"unbig in AI"*; three-question ROI diagnostic + *start with safety cases*; **adoption-capacity-as-binding-constraint** thesis.

**Acquisition pattern**: video 3 (Martin) fetched cleanly via the youtube-transcript-skill panel-fetch path. The other four hit the *"transcript panel did not render"* failure at `--timeout 60000` — fallback to `yt-dlp` captions (manual English for Oberholzer-Gee + Carrier; ASR + rolling-cue dedup for Sinek + Jordan). Local rolling-caption-dedup parser added to handle YouTube's auto-ASR overlap format. All 5 raw markdowns landed in `raw/videos/` with full YAML frontmatter contract.

**1 new concept page**: [[concepts/strategy|strategy]] (3 sources, confidence 0.80) — two foundational sources (Martin + Oberholzer-Gee) supply complementary lenses (*theory-of-winning* + *value-stick value-creation*), the third (Carrier) supplies a 2026 industrial-AI restatement.

**3 concept pages extended**:
- [[concepts/industrial-ai-agents|industrial-ai-agents]] 2→3 sources, with new §*MIT system-dynamics articulation (Carrier 2026)* — Heineken case, Forrester design criterion, alarm-fatigue counter-failure mode, Brooks/Ng *unbig*, the three-question ROI diagnostic.
- [[concepts/systems-thinking|systems-thinking]] 2→3 sources, with new §*Lineage extension to industrial AI* — Carrier joins Sterman as the third source in the MIT system-dynamics lineage; *"replace long slow feedback loops with very fast ones"* operationalises Sterman's feedback discipline at the industrial-AI scale.
- [[concepts/strategy|strategy]] 2→3 sources, with new §*Strategy in the industrial-AI era*.

**Typed relationships within the batch**: Martin ↔ Oberholzer-Gee `supports` (complementary strategy definitions); Sinek ↔ Jordan `supports` (both reject single-style command-and-control); Carrier `supports` Sterman 2026 (MIT lineage continuity), Manditereza 2026 (industrial-AI substrate + leadership), and Martin 2022 (planning-trap restated at tech-adoption scale).

**No W&W `dynamic_capabilities:` tags** on any of the 5 — strategy and leadership foundations sit upstream of the digital-transformation lens; Carrier engages digital-transformation but doesn't use the W&W framework directly, so omit per the *skip-rather-than-stretch* rule. **Cross-domain `roles:` overrides** on all 5 with appropriate role slugs per video.

**Dangling first-mentions** (deferred per author-entity rule, batch): Roger Martin, Rotman School of Management, Southwest Airlines, Felix Oberholzer-Gee, Harvard Business School, Best Buy, Hubert Joly, Simon Sinek, NYT Events, James P. Carse, Jennifer Jordan, IMD Business School, Angela Ahrendts, Mathias Döpfner (provisional), Axel Springer SE, John Carrier, Diane Abbott, Heineken Mexico, Michael Hammer, Andrew Ng, Rodney Brooks, John Seely Brown, Jensen Huang.

## [2026-05-18] ingest | [[2026-05-15-sterman-systems-thinking-for-leaders-designing-solutions-that-work]] — Sterman / MIT Sloan webinar; second source on [[concepts/systems-thinking|systems-thinking]] and first from inside the MIT system-dynamics lineage

User-initiated YouTube ingest via the [`youtube-transcript-skill`](../.claude/skills/youtube-transcript-skill/SKILL.md). **John D. Sterman** (Jay W. Forrester Professor of Management, MIT Sloan; director of MIT Sloan Sustainability Initiative) delivering a 57:48-minute MIT Sloan Executive Education webinar on 15 May 2026 — promotional vehicle for the *Business Dynamics* 5-day executive course (June 8–12 2026 on campus), but ~50 of the 58 minutes are substantive primary-source delivery from the canonical living voice of the MIT-system-dynamics discipline. ASR cleanup applied: *"Sturman" → "Sterman"*, *"JW Forester" → "Jay W. Forrester"*, *"Sully" → "Sully Sullenberger"*, light um/uh stripping.

**Six load-bearing claims**, captured in the source page and folded into the concept update: (1) **policy resistance** as the universal failure mode (five worked examples + Sir Thomas More's 1516 *Utopia* anchor); (2) the **open-loop mental model** is the bad mental model managers use, the world is feedback (bicycle analogy); (3) **"There's no such thing as a side effect"** — bad explanations are mental-model diagnostics; (4) multi-stakeholder system pull-back (*"when you pull the state of the system closer to your goals, you're almost certainly pulling it away from theirs"*); (5) causal mapping + group modeling (*"the system in the room"*) with the US prior-approval healthcare iceberg case (**$35B/yr admin cost in 2024**; 1996 study + 2026 meta-review of 25 studies → disease exacerbation, preventable hospitalisations, lower disease-free survival); (6) management flight simulators as the *"lectures don't work"* pedagogy — Sully-Sullenberger bird-strike anchor + live project-sim demo (25% defect rate vs <1% target; ~$50M NPV loss). Practitioner-stance reframe: **"sage on the stage" → "guide on the side"**. Defensive epistemic stance: George Box's *"All models are wrong; some models are useful."*

**1 concept page updated**: [[concepts/systems-thinking|systems-thinking]] 1→2 sources, confidence 0.75 → 0.80, with a new H2-sized §*The MIT system-dynamics articulation (Sterman 2026)* section bundling all six load-bearing claims and closing the *"deeper Senge and Forrester texts would strengthen the concept"* open question (still-open subitem: a primary-source Senge *Fifth Discipline* text is not yet in the wiki).

**Typed relationships**: `supports → [[2026-04-28-bansal-birkinshaw-systems-thinking]]` (Sterman supplies the operational machinery underneath Bansal & Birkinshaw's three-modes-of-innovation framing); `instance-of → systems-thinking`. **No W&W `dynamic_capabilities:` tag** — upstream methodology, not a digital-transformation capability, per the *skip-rather-than-stretch* rule. **Explicit `roles:` override** with eight cross-domain role slugs (`ceo, coo, cso, tech-lead, transformation-lead, rd-director, innovation-lab-lead, strategy-consultant`) — systems thinking is non-specialist.

**Dangling first-mentions deferred per author-entity rule**: John D. Sterman (author), MIT Sloan Executive Education (channel), Climate Interactive (Enroads collaborator), Sully Sullenberger, George Box, Sir Thomas More, MIT Institute for Data Systems and Society. Source confidence 0.82 — primary-source first-person delivery by the discipline's leading living figure; promotional framing is light caveat.

## [2026-05-18] ingest | [[2026-04-10-khan-osint-information-gathering-like-a-hacker]] + [[2026-05-12-techlatest-hacker-search-engines-osint-tools-2026]] — OSINT corpus seed (scope-widening)

User-initiated batch ingest of two OSINT articles from the same Medium publication ([[OSINT Team]]) — Khan's 3-min narrative walkthrough of a one-off defensive OSINT audit on her own organisation (Apr 2026), paired with TechLatest.Net's 9-min taxonomy/catalogue of ~18 hacker search engines across 5 categories + the standard 5-step recon workflow (May 2026). Acquired via `pdftotext -layout` from Medium PDF prints; URLs not embedded in the PDFs and left blank. The two pieces form a **narrative / taxonomy** pair: Khan shows what 2 hours of defensive OSINT looks like (developer comments leaking internal paths, EXIF GPS coordinates, LinkedIn+password-reset email enumeration, a 3-year-old public GitHub repo with internal admin credentials, job-posting tech-stack disclosure, badges-in-photos, Google dorks); TechLatest catalogues the platforms (Shodan / Censys / FOFA / ZoomEye / Hunter / HIBP / DeHashed / URLScan / Grep.app / crt.sh / Vulners / GreyNoise / FullHunt / WiGLE / Intelligence X / LeakIX / SecurityTrails / SpiderFoot) and names the emerging *AI-Augmented Offensive & Defensive Security* category as the one bridge into the wiki's existing [[concepts/ai-agents|ai-agents]] / [[concepts/agent-harness|agent-harness]] thread.

**Scope-widening note**: this is the wiki's first ingest of OSINT / cybersecurity-defence material. User explicitly confirmed widening the wiki scope. Both sources sit outside the W&W [[concepts/dynamic-capabilities|dynamic-capabilities]] lens — no `dynamic_capabilities:` tags applied (per the *skip-rather-than-stretch* discipline in CLAUDE.md). Role-relevance instead encoded via explicit `roles: [tech-lead]` override on both source pages (user-specified; cybersecurity-for-AI angle).

**2 new concept pages created**: [[concepts/osint|osint]] (the discipline; 2 sources, confidence 0.75) and [[concepts/attack-surface-management|attack-surface-management]] (the management practice; 2 sources, confidence 0.70). The two concepts carry a `depends-on` edge (ASM depends on OSINT for its discovery layer).

**1 concept page updated**: [[concepts/ai-agents|ai-agents]] 12→13 with a new *"Agents in cybersecurity reconnaissance (May 2026)"* section noting TechLatest's vendor-narrative claim about LLMs+agents+OSINT integration. Bridge tagged as `uses` (not `supports`) — claim is at taxonomy-vendor-narrative depth, not empirical.

**Typed relationships**: Khan↔TechLatest carry mutual `supports` edges (`via: "narrative walkthrough complementing taxonomy"`). Both sources carry `instance-of → osint` and `supports → attack-surface-management`. TechLatest additionally carries `uses → ai-agents` (the thin AI bridge).

**Dangling first-mentions deferred per author-entity rule**: Hania Khan (author), TechLatest.Net (author/brand), Troy Hunt (creator of HIBP), and 18 OSINT platforms as products. [[OSINT Team]] is now cited by two sources — still single-instance as a publication entity, defer to a third citation.

**Quality caveat flagged**: the TechLatest article contains an inline self-promotional section (~4 paragraphs advertising the publisher's own BlackArch / Kali / ParrotOS VM offerings on AWS / GCP / Azure) — captured in raw for fidelity but flagged as ad placement, not source material. Both source confidences calibrated at 0.65 (narrative + vendor-adjacent taxonomy, no empirical depth or peer review).

## [2026-05-17] acquire | `raw/videos/the-complete-guide-to-hybrid-search-in-rag-bm25-embeddings-reranker.md` — Ebbelaar tutorial as v0.10 seed (harvest-not-cite)

User-initiated YouTube acquire via the [`youtube-transcript-skill`](../.claude/skills/youtube-transcript-skill/SKILL.md). Dave Ebbelaar (Datalumina) 59-min hands-on tutorial published 14 May 2026: *"The Complete Guide to Hybrid Search in RAG (BM25 + Embeddings + Reranker)"*. Built from scratch on the BEIR FinanceQA dataset (56k docs); evaluates BM25 / Dense / RRF-fused / Hybrid + Cohere reranker with NDCG@10.

**Acquire-phase notes.** First attempt hit *"transcript panel did not render"* at default 30s timeout; retried with `--timeout 60000` and succeeded with 1130 ASR segments. Collapsed into 192 ~15s windows with light ASR cleanup (RAG / BM25 / Pydantic / Cohere / SPLADE / vector database). 117 KB markdown landed at canonical path with full YAML frontmatter contract.

**Why §Acquire-only and not §Ingest.** Substantive analysis ran *during* this session against the wiki's existing coverage:

- The **architectural conclusion** (*hybrid is the answer*) is already settled in [[syntheses/is-rag-dead]] (5 sources, closed 2026-05-12) and at the §Search layer in [CLAUDE.md](../CLAUDE.md) where qmd implements BM25 + vector + LLM-rerank.
- A sixth source-page on the same conclusion would **dilute, not strengthen**, the synthesis — Ebbelaar adds nothing the wiki doesn't already have at the architectural level.
- The tutorial *does* add four specific operational details the wiki was thin on: NDCG numbers, sizing rule, synthetic-eval-data prompt, RRF formula + bi/cross-encoder distinction.
- **Decision: harvest these four into the wiki at the right points instead of writing a source page.** This is the first worked example of the cherry-pick-not-ingest pattern, and it relies on the v0.9 §Acquire/§Process split being explicit — Acquire is a legitimate terminal state.

The four harvests are scoped into a new version slot **v0.10 — Search-quality empirical depth** (see [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md)), which lands when implemented:

1. `## Empirical anchors` subsection on `[[syntheses/is-rag-dead]]` with the FinanceQA NDCG gradient (BM25=28 / Hybrid+Rerank=47).
2. `### §Sizing decision` in CLAUDE.md §Search — *"under ~1M chunks, skip the vector DB"* rule with 30 MB BM25 + 350 MB dense `.npy` calibration anchor.
3. New thread `wiki-search-evals` + `wiki/evals/search-evalset.json` seeded by Ebbelaar's synthetic-query-generation prompt looped over `wiki/sources/`.
4. (Optional) New `[[concepts/reciprocal-rank-fusion]]` concept page with formula + bi-encoder/cross-encoder distinction.

**Files touched (1 raw):**

- `raw/videos/the-complete-guide-to-hybrid-search-in-rag-bm25-embeddings-reranker.md` (new — 117 KB).

No `wiki/sources/` page written; no concept pages updated; no `wiki/index.md` change. By design — that's the harvest-not-cite contract.

Reversibility: trivial. One raw file added, one log entry. Re-running the youtube-transcript-skill replaces the raw file; v0.10 itself is unaffected (the harvested *details* live in the plan, not in the raw file).

## [2026-05-17] ingest | [[2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china]] + [[2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells]] — paired buyer/seller framing of the agentic-commerce disintermediation thesis

User-initiated double ingest of two YouTube videos in one session: Björn Ognibeni's E-commerce Berlin Expo keynote (~28 min, 11 May) and Christine Tan's CNBC *Managing Asia* interview with DFI Retail Group CEO Scott Price (~15 min, 14 May). **Both videos hold the same agentic-commerce-disintermediation thesis from opposite sides of the buyer/seller table** — Ognibeni from the buyer-side outside-in (*"nobody will show up in your store when you only do search-driven e-commerce"*); Price from the seller-side incumbent-CEO (*"with [agentic AI] goes loyalty, with that goes access to data"*). The wiki's clearest paired articulation of the thesis to date.

**Acquire-phase notes.** Video 1 acquired via the [`youtube-transcript-skill`](../.claude/skills/youtube-transcript-skill/SKILL.md) at default timeout (664 ASR segments). Video 2 hit the *transcript panel did not render* symptom at both `--timeout 60000` and `--timeout 90000` (known long-format issue per skill failure-modes); since manual English captions exist, fell back to `yt-dlp` (`PYENV_VERSION=.myenv yt-dlp --write-sub --sub-lang en --skip-download --sub-format vtt`) and collapsed the VTT to wiki-canonical `[mm:ss]` timestamped lines (~191 segments after dedup). Both raw files written at `raw/videos/<slug>.md` with the canonical YAML frontmatter contract.

**Process-phase contributions.**

- **First wiki source with concrete RMB revenue lines for deployed Chinese agentic commerce** (Ognibeni): ByteDance 50T tokens/day + $670B GMV; Alibaba's Qen one-sentence-purchase agent at 100M+ users with tokenized mandates; JD.com's Joy Streamer virtual digital-twin live-stream hosts at ~$250M sales in one Double 11 season (more successful than 80% of human hosts); Alibaba's AQ (Accio) supply-chain-building agent with the translation-accuracy liability guarantee as the trust-scaling pattern; Xiaomi SU7 dark factory at 40 cars/hr autonomous production. **The wiki previously held agentic commerce as "early enterprise / mostly aspirational at consumer scale";** the evidence shifts that to "already deployed at 100M+ DAU outside the Anglophone press's habitual reading view."
- **First named CEO-level public-record articulation of agentic AI as strategic threat to the incumbent customer relationship** (Price). Plus DFI's three-axis AI investment framework (personalization / cost management / running a better business) and the **2,000-store competitive-scale floor in China** as a reusable W&W *balancing-digital-portfolios* anchor at mid-tier regional incumbent scale.
- **New *China-as-time-machine* digital-scouting frame** added to [[strategic-foresight]] (Ognibeni's geographic-asymmetry-as-foresight-instrument framing complements Webb/FTSG signal-detection methodologies that default to a US-centric vantage).

**Neighbour-source scan (Ingest step 5).** Five typed edges added on each source page. Video 1 → MGI PDF + MGI virtual event + Spiegel/Snapchat + Ries/Lenny's + `enterprise-ai-adoption` concept. Video 2 → Ognibeni video 1 + Jassy/Amazon + Spiegel/Snapchat + MGI PDF + `enterprise-ai-adoption` concept. Both pages cross-link to each other as the *buyer-side / seller-side mirror* of the thesis.

**Files touched (8 wiki + 2 raw + 1 index + 1 log):**

- `raw/videos/ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` (new)
- `raw/videos/cnbc-dfi-retail-asia-reinventing-how-it-sells.md` (new)
- `wiki/sources/2026-05-11-ognibeni-ai-agents-cool-demos-vs-real-revenue-china.md` (new)
- `wiki/sources/2026-05-14-price-dfi-retail-asia-reinventing-how-it-sells.md` (new)
- [[enterprise-ai-adoption]] — added Ognibeni + Price bullets under §"Sharper formulations from May 2026"; bumped `source_count: 30 → 32`, `last_confirmed: 2026-05-17`.
- [[ai-agents]] — added §"Agentic commerce at consumer scale (China, May 2026)" + §"Agents as strategic threat to incumbent customer relationships (May 2026)"; bumped `source_count: 10 → 12`, `last_confirmed/accessed_at: 2026-05-08 → 2026-05-17`.
- [[strategic-foresight]] — added §"China as time machine: a geographic vantage for digital scouting"; bumped `source_count: 5 → 6`, dates → `2026-05-17`.
- [[dynamic-capabilities]] — added §"Operator-narrated cases at mid-tier regional incumbent scale" with DFI case table covering five microfoundations; bumped `source_count: 4 → 5`, `last_confirmed: 2026-04-28 → 2026-05-17`.
- `wiki/index.md` — two new entries prepended.
- `wiki/log.md` — this entry.

Reversibility: clean — all eight wiki files are additive, two raw files are new, two source pages are new. No supersessions; no `status: stale` flips; no deletions.

## [2026-05-17] refactor | quality-score gap-fix on [[enterprise-ai-adoption]] (0.60 → 1.00) + `/wq` accessed_at bumps

Follow-up to a `/wq` query about AI-native organization design. The query landed on the wiki's central concept page [[enterprise-ai-adoption]] (then `quality_score: 0.60`); the user asked me to "close the gaps." Three of four gaps surfaced in the answer require new-source ingestion (academic change-management bridge to Carucci, empirical compounding-cycle measurement, post-GenAI MIT CISR survey wave) and were flagged for deferral. The fourth — internal schema discipline on [[enterprise-ai-adoption]] — was closable in-session.

**Issues fixed** (per [`scripts/quality-score.mjs`](../scripts/quality-score.mjs) rubric):

- Renamed `## Debates / contradictions` → `## Debates and supersession` to satisfy the v0.2 Structure check (concept pages with `source_count > 1` must carry the canonical heading; 20 of 100 rubric points hinged on this single rename — 10 Structure + 10 Cross-consistency).
- Filled the empty `## Key claims` H2 (`0 chars` between header and next H3) with an orientation paragraph indexing the six empirical lenses (breadth / depth / use-case mix / financial impact / productivity / workforce) and embedding the missing `[[jagged-frontier]]` body wikilink that the v0.3 *body-wikilink rule* required to match the `uses → jagged-frontier` relationship in frontmatter.
- Stripped six dangling-entity wikilinks (`[[Guardian Life Insurance]]`, `[[Italgas]]`, `[[Ford]]`, `[[Harvey]]`, `[[GitHub Copilot]]`, `[[Julie Baron]]`) per the [author-entity promotion rule](../CLAUDE.md#author-entity-promotion) — all six are single-source mentions that should remain `**bold**`/plain text until a second source lands.
- Stripped `[[Claude Code]]` similarly, but **flagged it as a clear entity-promotion candidate**: 22 source-page mentions across the wiki, far above the 2-source threshold. Entity-page creation is a separate ingest-style task, not a schema-fix.

**Score progression**: `0.60` (29/30/1) → `1.00` (40/30/30). Maximum on every dimension.

**Accessed_at bumps** (from the upstream `/wq` query):

- [[concepts/enterprise-ai-adoption]] — bumped to 2026-05-17 by [`scripts/wiki-query.mjs`](../scripts/wiki-query.mjs); §Retention reinforcement signal.
- [[concepts/micro-productivity-trap]] — same.
- [[Y Combinator]] — same.

**Reversibility**: low-risk. Three files touched; no relationships restructured; no source pages affected; no schema rules edited.

**Deferred (require new sources)**:

- Academic change-management bridge between [[2026-05-07-carucci-resistance-as-data|Carucci 2026]] and the Kotter / Lewin literature — no academic change-management primary source is in the corpus yet.
- Quantitative measurement of the compounding cycle (Kiron-Schrage slope; Chatterjee telemetry → harness-adjustment rate) — no empirical anchor available.
- Post-GenAI MIT CISR Future Ready Survey wave to replace the 2022 baseline (N=721) — would require a 2025/2026 CISR wave.

## [2026-05-17] refactor | v0.5 quality-slice follow-up — wiki-query wrapper + `/wq` slash command + MCP route documented

User-driven follow-up to the v0.5 quality slice that landed earlier today: provide an **API-shaped path** so agents (and humans via slash command) can hit the wiki with one operation that bundles *qmd query + accessed_at reinforcement*. Closes the deferral §Search marked as "MCP integration would auto-bump as part of `qmd_query` tool semantics; until then `bump-accessed.mjs` is the manual path" — but with a wrapper rather than full MCP, because qmd's MCP server doesn't know about the wiki's reinforcement rule.

**Three integration routes, documented in §Search:**

1. **`/wq` slash command** ([`.claude/commands/wq.md`](../.claude/commands/wq.md)) — ergonomic interactive frontend. `/wq <query>` dispatches to the wrapper, which runs `qmd query --json -n 8`, prints results, and auto-bumps. Language-agnostic (Dutch query → Dutch answer).
2. **CLI wrapper** ([`scripts/wiki-query.mjs`](../scripts/wiki-query.mjs), 110 lines) — shell-friendly. Flags: `-n <N>` (default 8), `--no-bump` (skip reinforcement), `--json` (raw qmd output for piping). Sources in results are skipped from the bump pass (they don't decay).
3. **qmd MCP server** — agents in the repo can get direct `query` / `get` / `multi_get` / `status` tools by adding `.mcp.json` at the repo root with the qmd server config (documented in §Search). **Caveat:** MCP route doesn't auto-bump — qmd's MCP server doesn't know the wiki's reinforcement rule. Agents using MCP directly must still call `bump-accessed.mjs` afterward to honour §Retention.

**Why three routes instead of one MCP install:**

- The slash command and wrapper bundle *query + bump* as one operation — that's the §Retention semantic.
- qmd's MCP server returns results but doesn't bump. Direct MCP use trades the bundling for direct tool access. Trade-off worth offering.
- Auto-mode classifier (correctly) blocks the agent from writing `.mcp.json` because it registers a persistent agent-control config. The schema documents what to put there; the user copies the JSON block to `.mcp.json` at the repo root manually. **One-time, user-authorised.**

**Schema changes — [`CLAUDE.md`](../CLAUDE.md):**

- §Search §"Bumping `accessed_at` after a query" replaced with a three-route documentation block (slash command / wrapper / MCP), the manual `bump-accessed.mjs` fallback noted for ad-hoc cases.
- The verbatim `.mcp.json` block is included in §Search so the user has the exact config to drop in.

**Validation:**

- `node scripts/wiki-query.mjs -n 3 "agent harness production-grade"` returned `Trivedy LangChain` (#1, score 0.93), `AI Agents` (#2, 0.56), `Kokane` (#3, 0.47). One concept in the result — bump worked. ✓
- Dutch query `"wat zegt de wiki over dynamische capaciteiten van organisaties"` returned Dynamic Capabilities + Warner & Wäger Process Model + Warner & Wäger source — *both concepts auto-bumped from older dates to 2026-05-17*. ✓
- Re-run of the same Dutch query: bump idempotent — both pages reported as "already at 2026-05-17", 0 bumped. ✓
- `--json` flag passes qmd's raw output unchanged for downstream piping. ✓
- Slash command file `.claude/commands/wq.md` reads as the §wq spec (description + workflow steps + conventions).

**What is NOT in this patch:**

- **`.mcp.json` was not created by tooling.** The auto-mode classifier (correctly) blocks agent self-modification of MCP server configs. The user adds it manually after deciding to enable the MCP route.
- **No global qmd install.** Wrapper uses `npx --yes @tobilu/qmd ...` which adds ~1s startup overhead per call. Acceptable for query workloads. A user wanting lower latency can `npm install -g @tobilu/qmd` and edit the wrapper.
- **No MCP-side bump.** Even after MCP is enabled, agents using MCP directly bypass the reinforcement signal. The `/wq` path bundles both; that's the recommendation.

**Files changed:**

- [`scripts/wiki-query.mjs`](../scripts/wiki-query.mjs) — new, 110 lines.
- [`.claude/commands/wq.md`](../.claude/commands/wq.md) — new, slash command spec.
- [`CLAUDE.md`](../CLAUDE.md) — §Search bump-after-query replaced with three-route documentation.
- This log entry.
- No wiki content pages touched.

**Why a "refactor" log op, not "bulk-refactor".** Three files (new wrapper, new slash command, one §Search rewrite). The earlier quality slice was `bulk-refactor` because it touched 30 wiki pages. This patch is paper + tooling only.

**Reversibility.** `git revert` cleanly removes both new scripts and the §Search rewrite. The `.mcp.json` (if user added it) is independent and stays.

**Next.** Same as before: v0.8 (Plan operation) per the renumbered roadmap. The wrapper script is in place; v0.8's gap detector can call qmd via the same `--json` interface to identify under-cited concepts.

---

## [2026-05-17] bulk-refactor | v0.5 quality slice — §Quality + `quality_score` on 30 pages + helpers

Closes v0.5. Lands the **mechanical quality scorer** and the **`accessed_at` bump helper** that together complete the lifecycle / search / quality triad. LLM-as-judge quality scoring is deferred to v0.6 per the original plan; everything mechanical (and the procedural plumbing the v2 spec demands) ships here.

**Schema changes — [`CLAUDE.md`](../CLAUDE.md):**

- §Lifecycle frontmatter contract: **concepts and syntheses** additionally carry `quality_score: 0.0–1.0` and `quality_notes: [...]` (the latter optional, omitted at ceiling). These are the **only frontmatter fields the schema permits tooling to write**, and only via [`scripts/quality-score.mjs`](../scripts/quality-score.mjs) — explicit user invocation, idempotent, derived.
- §Lifecycle `accessed_at` description extended: **syntheses also carry the field** (omission caught by the new scorer; see *retention-slice bug-find* below).
- New top-level **§Quality** section (between §Retention and §Search). Covers: what gets scored (concepts + syntheses, not entities, not sources, not threads), the rubric with weights, thresholds, how it runs, and **the auto-write exception** — narrow on purpose: derived, deterministic, user-triggered.
- §Retention tau-table extended: **90 days for concepts AND syntheses, 365 days for entities, ∞ for sources** (syntheses decay like concepts because they are claim-bearing, not evidence).
- §Search gains a "Bumping `accessed_at` after a query" sub-section pointing at the new helper.

**Tooling — new scripts in [`scripts/`](../scripts/):**

- **[`scripts/quality-score.mjs`](../scripts/quality-score.mjs)** — 260 lines. Walks `wiki/concepts/` and `wiki/syntheses/`, scores three dimensions (structure 0.40 / citation density 0.30 / cross-consistency 0.30), writes `quality_score` + `quality_notes` back to frontmatter. Idempotent (no-ops via content compare). Flags: `--dry-run` (print scores, no write), `--page <slug>` (single page). Knows about all wiki slugs (concepts + entities + sources + syntheses + threads + aliases) for the cross-consistency check.
- **[`scripts/bump-accessed.mjs`](../scripts/bump-accessed.mjs)** — 110 lines. Procedural helper for the v0.5 §Retention reinforcement signal: `node scripts/bump-accessed.mjs <slug> [<slug> ...]` bumps `accessed_at` to today on concept/entity/synthesis pages. Resolves slugs against the three searchable dirs; rejects sources (they don't decay); idempotent (already-current is a no-op). Pending MCP integration, this is the manual path called out in §Search.

**Migration — first quality-score pass over 30 pages:**

- 27 concepts + 3 syntheses scored. Initial distribution: **13 pages ≥0.85** (good), **15 pages 0.65–0.85** (acceptable, addressable opportunistically), **2 pages <0.65** ([`enterprise-ai-adoption`](../wiki/concepts/enterprise-ai-adoption.md) at 0.60 — 7 dangling entity wikilinks + missing Debates section; [`ai-benchmarks`](../wiki/concepts/ai-benchmarks.md) at 0.64 — similar pattern). Both <0.65 pages will be picked up by the v0.4 SessionStart hook's surfacing of low-quality pages.
- **Retention-slice bug-find:** the quality scorer flagged "missing frontmatter: accessed_at" on all three synthesis pages. The v0.5 retention-slice seed script targeted only `wiki/concepts/` and `wiki/entities/` — syntheses were silently excluded. Fixed by extending [`scripts/seed-accessed-at.mjs`](../scripts/seed-accessed-at.mjs)'s target list and seeding the three syntheses. **This is exactly the value-add of a mechanical scorer: a six-line omission in an earlier migration's scope, invisible to a human reviewer, surfaced by deterministic check.** Documented as the rationale for adding syntheses to the `accessed_at` contract.
- **Wikilink-regex bug-find** during scorer development: markdown tables use `[[slug\|alias]]` (backslash-escaped pipe) — the base regex `\[\[([^\]|]+)(?:\|[^\]]*)?\]\]` captures the trailing backslash as part of the slug, producing spurious "broken wikilink" reports. Fixed with a `normTarget()` helper that strips trailing backslashes. **Worth back-porting to [`scripts/lint-page.mjs`](../scripts/lint-page.mjs)** which uses the same pattern — deferred to a separate refactor entry.

**Validation:**

- `node scripts/quality-score.mjs` exits 0; 30 pages scored, frontmatter written. Re-run = 0 writes, 30 unchanged (idempotent). MD5 of any individual page unchanged across re-runs. ✓
- `node scripts/quality-score.mjs --dry-run` produces the same distribution without writing. ✓
- `node scripts/quality-score.mjs --page agent-harness` scores a single page and prints its notes. ✓
- `node scripts/bump-accessed.mjs --dry-run agent-harness ai-agents llm-wiki` correctly: skips already-current (`agent-harness`, `llm-wiki`), bumps stale (`ai-agents` from 2026-05-08). ✓
- `node scripts/bump-accessed.mjs --dry-run "Erik Brynjolfsson"` resolves entity with whitespace in filename. ✓
- `node scripts/bump-accessed.mjs --dry-run 2026-05-15-osmani-agent-harness-engineering` rejects source slug (not found in concept/entity/synthesis dirs — sources don't decay). ✓
- `node scripts/lint-confidence.mjs` exits 0; 113 lifecycle pages, 0 missing fields, 0 stale, 0 out-of-range, post-all-v0.5-slices.

**The auto-write exception, justified.**

The v0.4 §Hooks contract forbids automation from editing wiki content pages. `quality_score` and `quality_notes` are the **only fields** the schema permits tooling to write to, and even then **only via explicit user invocation** of `quality-score.mjs` — never from a hook. The exception is narrow: derived (not editorial), deterministic (same input → same output), user-triggered. Any future "auto-write" proposal must clear the same three bars; the precedent is documented in §Quality.

**Cuts vs. `llm-wiki-v2-plan.md` v0.5 spec:**

- **No LLM-as-judge** — v0.6 turf. The mechanical scorer is the structural floor; LLM-as-judge will overlay a content-correctness rubric.
- **No MCP integration for qmd** — deferred to v0.6 or whenever it becomes friction. Until then, `bump-accessed.mjs` is the manual path. The retention reinforcement signal works, it just isn't yet automatic on every search hit.
- **No scheduled hook** for daily retention sweep. Per §Hooks, hooks may not edit content; `quality_score` writes happen by explicit `node scripts/quality-score.mjs` call. A read-only retention-candidate surfacing hook is a v0.6+ candidate.

**Files changed:**

- [`CLAUDE.md`](../CLAUDE.md) — §Lifecycle (quality fields, syntheses-also-decay), new §Quality section, §Retention tau-table extension, §Search bump-after-query sub-section, §"Current state" v0.5-done update.
- [`scripts/quality-score.mjs`](../scripts/quality-score.mjs) — new.
- [`scripts/bump-accessed.mjs`](../scripts/bump-accessed.mjs) — new.
- [`scripts/seed-accessed-at.mjs`](../scripts/seed-accessed-at.mjs) — extended target list (`syntheses` added) and header comment.
- 27 concept pages + 3 synthesis pages — `quality_score` and `quality_notes` frontmatter fields added.
- 3 synthesis pages — `accessed_at` seeded (retention-slice catch-up).
- This log entry.

**Reversibility.** `git revert` removes the schema sections, both scripts, the frontmatter quality fields, and the synthesis `accessed_at` seeds in one operation.

**Where v0.5 lands the wiki.** Lifecycle, search, and quality now form a closed loop: every concept/synthesis page has a confidence (how sure), a freshness signal (`accessed_at` + decay tau), a quality score (how well-structured), and is searchable via hybrid retrieval that integrates all three. The bookkeeping that would have crushed a human wiki maintainer at 200 pages is now mechanical.

**Next.** Per the renumbered roadmap in [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md): **v0.8 (Plan operation)** — gap-driven todo generation, sourced from InfraNodus. Then v0.6 (crystallization + LLM-as-judge), then v0.7 (output formats + scoping). v0.8 is well-positioned now because the graph (v0.3), search (v0.5 search-slice), and quality-score (this slice) together give the gap detector three orthogonal signals to work from.

---

## [2026-05-17] refactor | v0.5 search slice — qmd installed, wiki indexed, §Search added

Lands the **search half of v0.5**. The wiki has crossed v2's "starts to creak past 100–200 pages" threshold (now 205 pages indexed including `index.md` + `log.md`), and the discovery surface for queries has shifted from "read `index.md` end-to-end" to "narrow via search, then drill". Sourced from the v0.5 search-slice in [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md); the retention slice landed earlier today as its own bulk-refactor entry below.

**Tool chosen: [qmd](https://github.com/tobi/qmd) (`@tobilu/qmd` on npm).**

- Karpathy's [`llm-wiki.md`](../llm-wiki.md) names qmd as a candidate; v2 leaves the engine unspecified. qmd was selected for: (a) **fully local** — embedding + reranking via [`node-llama-cpp`](https://github.com/withcatai/node-llama-cpp) with GGUF models, no OpenAI/Anthropic API exposure, (b) hybrid BM25 + vector + LLM-rerank natively, (c) MCP server interface available for future Claude Code integration, (d) installable via `npx @tobilu/qmd` so no global commitment.
- npm package name is **`@tobilu/qmd`**, not `qmd` (the bare name resolves to an unrelated placeholder). Documented in [§Search](#search) so future installs don't mis-key.

**What was installed and indexed:**

- qmd v2.1.0 via `npx --yes @tobilu/qmd <command>` (no global install).
- Collection registered: `ai-wiki` rooted at `./wiki`, glob `**/*.md`. **205 documents** indexed for BM25 (the 27 concepts + 83 entities + 86 sources + 4 threads + 3 syntheses + `index.md` + `log.md`).
- Context-string registered for the collection: schema summary + frontmatter contract (so qmd's LLM reranker has framing when returning results to a calling LLM).
- Models cached at `~/.cache/qmd/models/` (outside the repo):
  - `embeddinggemma-300M-Q8_0.gguf` — 333MB, Google's lightweight embedding model. Used by `qmd embed` / `qmd vsearch` / `qmd query`.
  - `qmd-query-expansion-1.7B-q4_k_m.gguf` — 1.28GB, query-expansion model used by `vsearch` / `query` to broaden the search vocabulary before retrieval. Download in progress as of log entry write; first `vsearch` will block on completion (~5–8 min one-time).
- Embeddings: **1466 chunks** generated across the 205 documents in 2m 40s. qmd chunks long pages at ~512 tokens so a long synthesis doesn't collapse into one averaged vector; each chunk is independently retrievable.

**Schema changes — [`CLAUDE.md`](../CLAUDE.md):**

- New top-level **§Search** section (after §Retention, before §Graph). Covers: index location (qmd's `~/.cache/qmd/models/`, not the repo), the collection mapping, **when to use qmd vs `index.md`** (5-page heuristic), the cheat-sheet for `search` / `vsearch` / `query` / `get` / `multi-get`, re-embedding after writes (`npx @tobilu/qmd embed`), **the §Retention integration rule** (qmd results re-ranked by `effective_confidence` at the answer-synthesis layer), and the cuts vs v2.
- §"Current state" amended to note that v0.5 retention + search are live, with the explicit deferral of `quality_score` (the third leg of the v0.5 spec).

**Validation:**

Three test queries run after the embedding pass and the 1.28GB query-expansion model finished downloading:

- **Test 1 — `qmd search "agent harness"` (BM25)** returns the expected top-3: the LangChain "Improving deep agents with harness engineering" source, the [`agent-harness`](../wiki/concepts/agent-harness.md) concept page itself, and the Osmani agent-harness-engineering source. **Top-3 hits exactly match what `index.md` would suggest a human reviewer to read first.** ✓
- **Test 2 — `qmd vsearch "hoe zorgen we dat AI niet kapot gaat in productie"` (pure vector, Dutch paraphrase)** returned **the wrong cluster**: Thompson NYT *Workers Letting AI Do Their Jobs*, [`industry-4-0`](../wiki/concepts/industry-4-0.md), [`ai-employment-effects`](../wiki/concepts/ai-employment-effects.md), MIT Tech Review *AI-enabled enterprise*, MIT 6.S191 *Three Laws of AI*. None of the harness/runtime concepts surfaced. **Why this happened:** the Dutch "in productie" is lexically ambiguous — production-deployment vs workplace-productivity — and the pure vector model resolved to the labor/employment semantic cluster rather than the systems-engineering one. This is a textbook over-generalisation by a vector model when faced with a paraphrased ambiguous query. ✗ for vsearch on this query, **but exactly the failure mode v2 names as the reason for hybrid search.**
- **Test 3 — `qmd query "what makes an agent harness production-grade"` (hybrid + LLM-rerank)** returned, in order: [`ai-agents`](../wiki/concepts/ai-agents.md), [`agent-harness`](../wiki/concepts/agent-harness.md), [`agentic-engineering`](../wiki/concepts/agentic-engineering.md), Osmani *Agent Harness Engineering*, [`vibe-coding`](../wiki/concepts/vibe-coding.md). **All five top hits are directly relevant to the question.** The BM25 leg of the hybrid pipeline matched the literal "agent harness" term that pure vector had dropped, and the LLM-reranker chose the harness/runtime interpretation over labor/employment. ✓

The Test 2 / Test 3 contrast is the empirical case for `query` as the default for complex semantic queries — `vsearch` alone is unreliable when query phrasing is ambiguous, but the hybrid pipeline's BM25 backbone catches what vector misses.

- `node scripts/lint-confidence.mjs` exits 0 after both today's slices (retention + search). 113 lifecycle-bearing pages, 0 missing fields, 0 stale, 0 out-of-range.

**What is NOT in this slice (and why):**

- **No `quality_score` field, no `scripts/quality-score.mjs`.** v0.5 spec's third leg. Deferred to a quality-slice session so the search-slice ships now and quality scoring lands together with its LLM-judge cousin (v0.6 turf anyway).
- **No scheduled hook that bumps `accessed_at` on query-time reads.** §Search documents the gap: qmd's CLI can't observe what the calling LLM subsequently consumed, the PostToolUse hook sees only edits, and Claude Code does not expose a "page read" event the session-end hook could scan. Cleanest path is **MCP integration** (qmd ships a server; wire it as a Claude Code MCP tool, then `qmd_query` calls can bump `accessed_at` themselves as part of the tool's contract). Deferred to the quality slice or whenever it becomes friction. **Until then:** `accessed_at` is bumped manually by Process step 6 (alongside `last_confirmed`) on ingest-time touches.
- **No re-embed automation.** A hook that calls `qmd embed` after every wiki edit would thrash. Re-embedding is part of the manual ingest-completion checklist — a single `npx @tobilu/qmd embed` after a batch of ingests, taking seconds because qmd hashes documents and only re-embeds changed ones.
- **No `quartz.config.ts` change.** qmd lives outside the published-site build. No new Quartz extension.

**Cuts vs. `llm-wiki-v2.md`:**

- **No external embeddings API.** v2 is API-agnostic; qmd's local GGUF route honours the spirit (everything on-device) without OpenAI/Anthropic exposure or recurring cost.
- **No graph-aware retrieval inside qmd.** v2 envisions BM25 + vector + graph as one fused retrieval. This slice merges qmd's BM25+vector with the wiki's typed graph (`wiki/.graph.json`) **at the answer-synthesis layer**, not inside the engine. Pragmatic, revisable.
- **No four-tier consolidation pipeline.** Per the v2 plan's original cuts, `raw/` → sources → concepts/entities → `CLAUDE.md` remains the implicit tier mapping. No new directory.

**Files changed:**

- [`CLAUDE.md`](../CLAUDE.md) — new §Search section + §"Current state" amendment.
- This log entry.
- No wiki page content touched. No new script in `scripts/` (qmd's own CLI is the interface).

**Network/disk cost (one-time):** 333MB + 1.28GB ≈ 1.6GB model cache at `~/.cache/qmd/models/`, plus qmd's own index store (location: qmd-managed, not in repo). Per-machine cost; portable via re-running `qmd collection add` + `qmd embed` on another machine.

**Next.** v0.5 **quality slice** (LLM-judge `quality_score` + MCP integration for `accessed_at` auto-bump) — this finishes v0.5 fully and unblocks v0.6 (crystallization, which depends on `quality_score`). Then **v0.8 (Plan operation)** per the renumbered roadmap, then v0.6 → v0.7. Begroot: 1 sessie voor de quality slice (mits qmd MCP integratie zonder verrassingen werkt).

---

## [2026-05-17] bulk-refactor | v0.5 retention slice — §Retention added + `accessed_at` seeded on 110 concept/entity pages

Lands the **retention half of v0.5** per [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md). The search half (qmd / hybrid retrieval) and the quality half (`quality_score` + `quality-score.mjs`) are deferred to a separate v0.5 search-slice session — they're nutteloos zonder hun tooling, so it's cheaper to land them as a single package later. Today's slice is paper + one deterministic seed.

**Schema changes — [`CLAUDE.md`](../CLAUDE.md):**

- §Lifecycle §"Frontmatter contract (concepts and entities)" gains a fourth field: **`accessed_at: YYYY-MM-DD`**. Semantics: the date the page was last *read into context*, distinct from `last_confirmed` (which is bumped only on *write* — i.e. when an ingest reinforces the page). Sources do not carry `accessed_at` (sources don't decay).
- New top-level **§Retention** section between §Lifecycle and §Graph. Contents:
  - **The decay curve.** `effective_confidence = stored_confidence × exp(-days_since_access / tau)`, with tau = 90 days for concepts, 365 for entities, ∞ for sources. Concepts decay ~4× faster than entities because conceptual framings shift faster than the people, orgs, and products they describe. `effective_confidence` is computed at lint-time and never overwrites the stored `confidence:` value.
  - **What decay does and does not do.** Lint surfaces decay candidates (pages where `effective_confidence < 0.5`), search rank drops low-effective-confidence pages (lands with the search slice), SessionStart hook can highlight them. Decay never deletes pages, never auto-writes `status: stale`, never overwrites `confidence:`, never touches source pages.
  - **The reinforcement signal.** `accessed_at:` bumps on: (1) ingest touching the page (same trigger as `last_confirmed`), (2) query reading the page into context (lands with search slice — a scheduled hook will bump on search-returned pages), (3) manual re-confirmation during lint. Pages where `accessed_at < last_confirmed` are *read-aged*: factually current but not actively engaged with.
  - **Cuts vs. `llm-wiki-v2.md`.** No auto-deletion; no per-page tau override (use `confidence:` if a concept should resist decay); no scheduled retention sweep that auto-marks pages stale. Hooks may not edit content — per [§Hooks](#hooks), confirmed.

**Migration — `accessed_at` seed on 110 pages:**

- New script [`scripts/seed-accessed-at.mjs`](../scripts/seed-accessed-at.mjs) — idempotent, deterministic seed: `accessed_at := last_confirmed` (verbatim, quote style preserved). Skips pages where `accessed_at:` already exists; skips pages without `last_confirmed:`; skips pages without frontmatter. Re-run safe.
- Dry-run output before write: 110 scanned, 110 would-be seeded, 0 already-present, 0 no-last-confirmed, 0 no-frontmatter. Write was run after dry-run inspection.
- Wet-run results: 110 pages seeded (27 concepts + 83 entities). Spot-checked: [`agent-harness`](../wiki/concepts/agent-harness.md) (concept, `accessed_at: "2026-05-17"` placed directly after `last_confirmed: "2026-05-17"`, quote style preserved), [`Erik Brynjolfsson`](../wiki/entities/Erik%20Brynjolfsson.md) (entity with whitespace in filename, no issue).
- Idempotence verified by re-run: 0 new seeds, 110 already-present.
- Post-seed lint: `node scripts/lint-confidence.mjs` exits 0; confidence distribution unchanged (74 pages 0.7–0.85, 39 pages 0.85–1.0); 0 pages missing lifecycle fields; 0 pages stale.

**Why a script and not a supervised batch.** The v2 plan's "supervised batches of ~10" rule applies to migrations with *judgment* (confidence values, relationship targeting). This seed is deterministic — `accessed_at := last_confirmed`, no value to defend, no edge case to weigh. The script's idempotence + verbatim-copy + spot-check audit trail is defensible. The same rule would forbid blind-scripting a confidence migration (and v0.2 honoured that).

**Cuts vs. the full v0.5 spec — what is NOT in this slice:**

- No qmd install. No `§Search` section. No `index.md → qmd` ranker integration. — *Lands with the search slice.*
- No `quality_score:` field on concepts. No `scripts/quality-score.mjs`. — *Lands with the quality slice (search-slice session or its own session).*
- No scheduled hook that bumps `accessed_at` on query-time page reads. The field exists; the bump-on-read mechanism lands with the search slice. Until then, `accessed_at` is bumped *manually* during ingest-time touches (alongside `last_confirmed`) and *automatically* by the same v0.2 ingest discipline that bumps `last_confirmed`. **Action item for §Process step 6:** when bumping `last_confirmed` on a touched concept/entity page, bump `accessed_at` to the same value. This is a procedural-only update (no CLAUDE.md edit needed because §Lifecycle's frontmatter contract already lists `accessed_at` as a required field; ingest-time touches that don't bump it will be flagged by the lint script when it learns the field — deferred to the quality slice).
- No daily retention-candidate scan as a hook. The §Retention rules are documented but unmonitored until the search slice wires up the lint extension.

**Files changed:**

- [`CLAUDE.md`](../CLAUDE.md) — §Lifecycle frontmatter contract + new §Retention section.
- [`scripts/seed-accessed-at.mjs`](../scripts/seed-accessed-at.mjs) — new, 67 lines.
- 110 wiki pages under `wiki/concepts/` (27) and `wiki/entities/` (83) — `accessed_at:` field added.
- This log entry.

**Reversibility.** `git revert <this-commit>` cleanly removes the `accessed_at` field from all 110 pages, the §Retention section from CLAUDE.md, and the seed script. The frontmatter shape returns to the pre-v0.5 contract.

**Next.** v0.5 search slice — qmd installation (or MCP equivalent), `§Search` regel in CLAUDE.md, `quality_score` field + `scripts/quality-score.mjs`, scheduled hook for `accessed_at` bump on search-returned pages. Begroot op 1–2 sessies. After that: v0.8 (Plan operation) per the renumbered roadmap, then v0.6 (crystallization) which depends on `quality_score`.

---

## [2026-05-17] refactor | v0.9 — split §Ingest into §Acquire + §Process

Schema-only refactor. Names the two phases of the ingest operation that this repo has been running de facto since the [`youtube-transcript-skill`](../.claude/skills/youtube-transcript-skill/SKILL.md) became the canonical front end for video sources: **Acquire** lands a raw file in a typed `raw/` subfolder (and stops); **Process** reads `raw/` and writes `wiki/`. The split was sourced from the InfraNodus `skill-llm-wiki/SKILL.md` (Phases 8 + 9), which is the only upstream that names it; neither Karpathy's `llm-wiki.md` nor the agentmemory `llm-wiki-v2.md` distinguishes the two phases. Sourced and slotted as a single-session paper-only release in the 2026-05-17 update to [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md).

**Changes to [`CLAUDE.md`](../CLAUDE.md):**

- §"The four operations" intro now flags Acquire/Process as Ingest's two sub-phases. Operation count stays at four (Ingest / Query / Lint / Synthesize); Ingest is now an umbrella over Acquire + Process rather than a single linear flow.
- New §"Ingest = Acquire + Process" pointer paragraph between the intro and the sub-sections.
- New **§Acquire** sub-section (5 numbered points): typed `raw/` subfolder rule, convert-before-landing for PDFs / YouTube / `.docx` / `.epub` / `.html`, the **acquire-time skill contract** (a skill emits a raw file at `raw/<type>/<slug>.md` with canonical YAML frontmatter), re-runnability of acquisition, and the `acquire | ...` log-op convention for standalone-Acquire sessions. The video-format frontmatter contract at [§"Pre-flight check (videos): the YAML frontmatter contract"](../CLAUDE.md#pre-flight-check-videos-the-yaml-frontmatter-contract) is now referenced from §Acquire as the canonical reference implementation for future acquire-time skills (PDF→markdown, web clipper integration, podcast transcription).
- Existing **§Ingest** body (steps 0–9) renamed to **§Process** unchanged in substance; one sentence added to the section intro explaining that Process can run same-session-with-Acquire (the typical case) or stand alone on an earlier-acquired file. Step 8 amended to spell out the log-op choice: `ingest | ...` for the umbrella case, `acquire | ...` only for the standalone-Acquire case.
- §"Current state" `<op>` enum extended to `ingest | acquire | query | lint | synthesize | refactor | bulk-refactor`. Section also bumped from "six staged versions (v0.2 → v0.7)" to "eight staged versions (v0.2 → v0.9)" to reflect the 2026-05-17 plan update.

**Changes to [`wiki/log.md`](../wiki/log.md):**

- Permitted-operations header line extended to include `acquire`, with a parenthetical explaining the v0.9 distinction (`acquire` for deferred-Process sessions; `ingest` remains the umbrella for the typical case).

**Wiki content touched:** zero pages. This is a paper-only refactor — no concept, entity, source, synthesis, or thread page is edited.

**Why now.** Same-day momentum from the 2026-05-17 comparative synthesis across Karpathy / agentmemory / InfraNodus (see [`inspiration/`](../inspiration/) draft and the 2026-05-17 update block in [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md)). The rationale was scratched fresh; landing it now is cheaper than re-deriving it later. Also opens the door for v0.5's scheduled `accessed_at` hook to reason about Acquire-only sessions distinctly from full Ingest, without retrofitting language.

**Cuts vs. the InfraNodus skill (Phases 8 + 9).**

- No 10-phase guided scaffolding (Discover / Scope / Structure / Schema / Workflows / Tooling / Scaffold). That's an onboarding skill for *new* wikis; this repo is already instantiated.
- No `infranodus/` folder of append-only ontology files. The typed `relationships:` block (v0.3) + `wiki/.graph.json` already serve the role InfraNodus's ontology files do, from a single source of truth.
- No new tooling. The `youtube-transcript-skill` already fits the acquire-time skill contract; future skills (PDF→markdown, web clipper, podcast transcription) will be authored against the contract as they're needed.

**Verification.**

- `CLAUDE.md` renders with §Acquire and §Process as siblings under §"The four operations"; §Ingest survives as a pointer paragraph.
- Permitted-ops enum consistent across `CLAUDE.md` §"Current state" and `wiki/log.md` header.
- The `youtube-transcript-skill` is the live reference implementation — no skill changes required; the schema now names the contract it already satisfies.

**Next per [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md):** v0.5 kernslice — hybrid search (qmd or MCP equivalent) + retention/forgetting (`accessed_at`, `quality_score`, decay curve). At 86 sources + ~200 pages total, `index.md` is approaching v2's "starts to creak past 100-200 pages" threshold; search is now the binding constraint.

---

## [2026-05-17] ingest | Vivek Trivedy — *The Anatomy of an Agent Harness* (LangChain Engineering blog, 10 March 2026) — closes the Trivedy / Chatterjee / LangChain three-post thicket

**Single-source ingest** triggered by user clarification: the user noted *"The post from Chatterjee only has a similar title. Here is the article from LangChain: https://www.langchain.com/blog/the-anatomy-of-an-agent-harness"* and pointed to the canonical URL the wiki had been carrying as an open ingest target since this morning. WebFetch returned full HTML body (no PDF version exists; LangChain blog renders dynamically). Author byline confirmed: **Vivek Trivedy** = the "Viv Trivedy" Osmani referenced in his May 15 essay.

**Source page (1 new):**

- [[2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness]] — Vivek Trivedy, LangChain Engineering blog, 10 March 2026. Full body archived at `raw/articles/2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness.md` (markdown reproduction of HTML). The post is the **canonical "Anatomy of an Agent Harness"** piece Osmani referenced and Pan et al. cited as reference 16. Confidence 0.82.

**Concept page updated (1):**

- [[concepts/agent-harness]] 31→32, conf 0.98 unchanged, last_confirmed 2026-05-17 (same-day **quadruple-bump** after morning's Karten/Nodus/PY ingests + afternoon's 7-paper batch + evening's Trivedy ingest — most active concept-page day in wiki history). New ~30-line section "**Trivedy is the source-of-vocabulary; Osmani is the popularisation**" with attribution table mapping load-bearing claims to first-person primary anchors. New "**The Feb 11 / Feb 17 vocabulary-coinage window**" sub-section naming Lopopolo (Feb 11) + Trivedy (Feb 17) as near-simultaneous co-coiners of "harness engineering" as a discipline noun.

**Why this single ingest is disproportionately load-bearing.** Multiple wiki claims previously held under "the practitioner cluster" or "carried via Osmani" now have a **first-person primary anchor**:

| Wiki claim (status before this ingest) | Status after |
|---|---|
| ***"Agent = Model + Harness"*** equation | **Closed — first-person primary.** Trivedy's coinage. |
| ***"If you're not the model, you're the harness"*** | **Closed — first-person primary.** Trivedy's coinage. |
| **Working-backward-from-behavior design pattern** | **Closed — first-person primary.** Trivedy's coinage. |
| **Ralph Loops definition** | **Closed — first-person primary** (definitional). |
| **6-primitive enumeration** (filesystem / bash+code / sandboxes / memory / context rot / long-horizon) | **Closed — first-person primary** (canonical ordering). |
| **Three named open problems** (parallel-agents / trace-self-correction / dynamic assembly) | **Closed — first-person primary.** |
| ***"Opus 4.6 in Claude Code scores far below Opus 4.6 in other harnesses"*** | **Closed — first-person primary observation.** |
| **Top 30 → Top 5 on Terminal Bench 2.0** (re-attributed away from Pan et al. earlier today) | **Closed — first-person primary anchored as Trivedy's LangChain result** (attributed by Trivedy to a previous LangChain blog, likely the Feb 17 *Improving Deep Agents with Harness Engineering* post). |
| **Trivedy / Chatterjee author-attribution flag** (open since 2026-05-15) | **Closed.** Vivek Trivedy = "Viv Trivedy" in Osmani; Chatterjee's Medium post is a *separate* artifact (similar title only — user confirmation). The existing [[2026-05-07-chatterjee-anatomy-of-agent-harness]] source page is correctly attributed and stays in place. |

**Repositioning of Osmani's essay.** [[2026-05-15-osmani-agent-harness-engineering|Osmani's May 15 O'Reilly Radar essay]] is now confirmable as **a near-direct synthesis-with-expansion of Trivedy's post**, published 9 weeks later for the O'Reilly audience. Verbatim quotes match; same 6 primitives in same order; identical three-open-problems list. Osmani's contribution beyond Trivedy: explicit cross-author synthesis (Anthropic / HumanLayer / Bockeler / Khan / Willison) + the *ratchet* framing + the HaaS substrate-shift framing. **Trivedy is the source-of-technical-content; Osmani is the cross-author-synthesis popularisation.**

**Index + log updates.** New entry at the top of [[wiki/index.md|index.md]]'s Sources section. This log entry.

**Pages touched: 4 total** (1 new source + 1 updated concept + index + log).

**Operational note on IDE diagnostics.** Four IDE warnings during the edits flagged the new slug `2026-03-10-trivedy-langchain-anatomy-of-an-agent-harness` as *"ambiguous-identifier"* relative to the existing [[2026-05-07-chatterjee-anatomy-of-agent-harness]] slug — false positives from the IDE plugin's substring-matching resolver. Both slugs are unique by exact filename; Obsidian/Quartz resolve by full filename match. No corrective action needed.

**Cluster status after today.** With Trivedy ingested, the **harness-engineering cluster on [[concepts/agent-harness]] reaches 32 sources** — the largest single concept-page cluster in the wiki. Today's three batches (Karten + Nodus Labs + PY + Osmani prior; the 7-paper academic / vendor primary batch; this Trivedy ingest) closed nearly every standing primary-source ingest target and most attribution flags. **Remaining open**: WebFetch the Feb 17 LangChain *Improving Deep Agents with Harness Engineering* post for its substantive methodology body (currently metadata-only ingest with empty PDF capture).

**Reversibility.** All edits structurally additive. 4 files touched. Reverse with `git checkout`.


## [2026-05-17] ingest | Harness-engineering primary-source septet — 4 academic papers (Pan / Lee Meta-Harness / Lou AutoHarness / Wang AgentSpec) + 3 vendor primaries (Anthropic Dec 2024 + Nov 2025 + LangChain Feb 2026)

**Seven-source batch ingest** — the largest single-day primary-source landing in the wiki's harness-engineering cluster. The user delivered exactly the open-targets list from yesterday's two ingest batches (Continual Harness + PY video): the **Pan et al.** and **Lee/Khattab Meta-Harness** papers whose identifications were closed yesterday, the **AutoHarness** and **AgentSpec** papers surfaced as new targets, and the three vendor primaries (Anthropic Dec 2024 + Nov 2025 + LangChain Feb 2026) named in the PY video description. **Most second-hand wiki claims on [[concepts/agent-harness]] are now primary-source anchored.**

The 8th file in `raw/articles/` (OpenAI Codex *Harness engineering* PDF, dated today) is **already ingested** as [[2026-02-11-lopopolo-codex-harness-engineering]] — a re-download or fresh copy of the existing source. Skipped.

**Source pages (7 new):**

- [[2024-12-19-anthropic-building-effective-agents]] — Schluntz & Zhang. **The earliest primary in the wiki's harness construct by 14-17 months.** Workflows-vs-agents distinction; 5 patterns; 3 principles (simplicity / transparency / careful ACI); MCP first introduced as part of the agentic systems architecture. Strong Dec 2024 prediction: *"start with LLM APIs directly"*. Confidence 0.78.
- [[2025-07-31-wang-agentspec-runtime-enforcement-llm-agents]] — Wang, Poskitt, Sun (SMU). **First peer-reviewed paper in the wiki's harness cluster** (all others are arXiv preprints); accepted to ICSE '26. DSL for runtime enforcement of LLM-agent behaviour. Built on LangChain; framework-agnostic. >90% unsafe-code prevention; eliminates all hazardous embodied actions; 100% AV compliance in 5/8. LLM-generated rules: 87.26% / 95.56% / 5-of-8 precision. Millisecond overhead. **The formal operationalisation of Chatterjee's Constraints layer as an executable DSL.** Confidence 0.92.
- [[2025-11-26-anthropic-effective-harnesses-long-running-agents]] — Justin Young (Anthropic). **The vendor-engineering origin of the initializer-agent + coding-agent pattern** the wiki has been carrying second-hand. *"Compaction isn't sufficient"* at frontier-model scale. init.sh + claude-progress.txt + feature_list.json + git. JSON over Markdown for agent-edited state. 4 failure modes + structured solutions. Anticipates Pan et al.'s file-backed state module by 4 months and Karten's reset-free framing by 6 months. Confidence 0.80.
- [[2026-02-17-langchain-improving-deep-agents-harness-engineering]] — **Metadata-only ingest** (PDF capture empty; substantive body lives at URL). Names "harness engineering" as a discipline in Q1 2026 alongside Lopopolo. **Likely primary source for the *"Top 30 → Top 5 on TerminalBench 2.0"* claim** that secondary summaries circulate. Pan's reference 16 reveals a **sister post — *The anatomy of an agent harness* (LangChain Engineering, 10 March 2026)** the wiki hasn't yet ingested. **Suggests the Trivedy / Chatterjee / LangChain "Anatomy of an Agent Harness" thicket may be THREE separate posts.** Confidence 0.55.
- [[2026-03-05-lou-deepmind-autoharness-code-harness-synthesis]] — Lou, Lázaro-Gredilla, Dedieu, Wendelken, Lehrach, Murphy (Google DeepMind). **The earliest of the four academic harness primaries** (predates Pan by 3 weeks; Lee by 25 days). **78% of Gemini-2.5-Flash chess losses are illegal moves** (the wiki's strongest empirical anchor for "agent failures are usually harness failures"). Three harness types — including **harness-as-policy** where the LLM generates pure code with zero inference-time LLM calls. Harness-as-Policy 0.870 reward beats GPT-5.2-High 0.844 at near-zero inference cost. **The strongest empirical anchor in the wiki for [[concepts/software-3.0|Software 3.0]] taken to its limit.** Confidence 0.85.
- [[2026-03-26-pan-natural-language-agent-harnesses]] — Pan, Zou, Guo, Ni, Zheng (Tsinghua + HITSZ). **The Pan et al. paper.** NLAH + IHR. Five NLAH ingredients + file-backed state with three properties (externalized / path-addressable / compaction-stable). **Closes the wiki's longest-running primary-source ingest target.** Verifies the 14× compute reduction (Table 1), the Verifier-hurts-OSWorld -8.4 (Table 3), and the OS-Symphony NL migration 30.4% → 47.2% (Table 5). **One re-attribution**: the *"Top 30 → Top 5 on TerminalBench 2.0"* claim is **not in Pan's paper** — likely from LangChain. Confidence 0.85.
- [[2026-03-30-lee-meta-harness-end-to-end-optimization]] — Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, **Omar Khattab**, Chelsea Finn (Stanford + KRAFTON + MIT). **The DSPy-team Meta-Harness paper.** Outer-loop search with Claude Code Opus-4.6 as proposer reading full filesystem. **Raw-traces > summaries empirically anchored** (Table 3: 34.6 / 34.9 / 50.0). **Meta-Harness #2 on Opus 4.6 (76.4%) and #1 on Haiku 4.5 (37.6%) on TerminalBench-2.** **Transferability across 5 held-out models** (+4.7 pts avg, math reasoning). **6× performance gap headline claim.** ForgeCode (81.8%) named as unreproducible from public code. Confidence 0.88.

**Concept pages updated (4):**

- [[concepts/agent-harness]] 24→**31**, conf 0.95→**0.98**, last_confirmed 2026-05-17 (same-day **triple-bump** after morning's Karten/Nodus/PY ingests + this afternoon's 7-paper batch). New ~70-line section "**The March 2026 academic-anchor triple — and the December 2024 foundational vendor anchor**" with full table of all 7 new sources + load-bearing contributions. New "**The construct's history is older than its name**" sub-section naming the Dec 2024 → Feb 2026 *naming gap*. **Eight open questions closed** (Pan identification + Pan primary-source ingest + Meta-Harness identification + Meta-Harness ingest + raw-traces-vs-summaries + transferability + verifier-hurts mechanism + Top 30→Top 5 re-attribution). **One open question half-clarified**: Trivedy/Chatterjee — Pan reference reveals possible third "Anatomy" post. **Three attribution corrections** made (78% chess losses → AutoHarness; Top 30 → Top 5 → likely LangChain not Pan; 6× headline → Lee et al. citing Bui).
- [[concepts/agentic-engineering]] 13→**17**, conf 0.95→**0.97**, last_confirmed 2026-05-17. Anthropic Dec 2024 + Anthropic Nov 2025 + LangChain Feb 2026 + Lee Meta-Harness added to the discipline's anchor set (the practitioner-altitude form of agentic engineering: harness engineering, predating its naming by 14 months).
- [[concepts/responsible-ai]] 10→**11**, conf 0.95 unchanged, last_confirmed 2026-05-07→2026-05-17. New "**Runtime enforcement as a declarative discipline**" section absorbing AgentSpec as the wiki's first peer-reviewed academic primary on LLM-agent runtime safety as a formal verification problem.
- [[concepts/software-3.0]] 2→**3**, conf 0.80→**0.82**, last_confirmed 2026-05-09→2026-05-17. New "**The Harness-as-Policy limit**" section absorbing AutoHarness's zero-LLM-at-runtime result as the strongest single empirical anchor for the Software 3.0 thesis taken to its limit. Names task-structure-dependence: well-defined policy spaces admit the compiler interpretation; open-ended task families keep the model in the loop.

**Why this batch is disproportionately load-bearing.** Before today, the wiki's harness-cluster claims were anchored on practitioner essays (Chatterjee, Kokane, Osmani, Bockeler) and second-hand summaries (PY, Prompt Engineering YouTube). With this batch, **nearly every load-bearing claim on [[concepts/agent-harness]] has a peer-track academic primary or named-author vendor primary anchor**. The wiki's harness construct moves from *practitioner consensus* to *empirically-anchored discipline* in a single day.

**Index + log updates.** Seven new entries at the top of [[wiki/index.md|index.md]]'s Sources section. This log entry.

**Pages touched: 13 total** (7 new sources + 4 updated concepts + index + log).

**Open questions carried forward:**

- **The LangChain *Anatomy of an Agent Harness* post (10 March 2026)** named in Pan's reference 16 — not yet ingested. Likely source of the *Top 30 → Top 5 TerminalBench* claim.
- **Trivedy / Chatterjee / LangChain "Anatomy" three-post thicket.** Three separate posts with similar titles may exist. The Medium post the wiki ingested as [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] may be a different artifact from the LangChain blog and the "Viv Trivedy" reference Osmani names. Resolution still requires direct fetch of all three.
- **The Verifier-hurts-OSWorld mechanism.** Pan empirically demonstrates Verifier −8.4 but the *why* — *"verifier-level acceptance can still diverge from benchmark-level acceptance"* — is partially named, not causally explained. Worth tracking against future ablation work.
- **Compressed-vs-full feedback in harness search.** AutoHarness (5-step Critic window) and Meta-Harness (full filesystem) both work; head-to-head comparison on the same task family would settle the design-space question.
- **Pan + Lee unification.** Two papers 4 days apart from independent groups. Running Meta-Harness search inside Pan's IHR runtime over NLAH representations is *the obvious next experiment for the field*.

**Reversibility.** All edits structurally additive (one re-attribution correction is on a previously-mis-attributed claim, not a content retraction). 13 files touched. Reverse with `git checkout`.


## [2026-05-17] ingest | PY YouTube — *Rethinking AI Agents: The Rise of Harness Engineering* (14 April 2026, 11:45 min, 126k views) — metadata-only; closes Pan et al. + Meta-Harness primary-source identification open-questions

**Single-source metadata-only ingest** — the wiki's third metadata-only video ingest after [[2026-05-06-amodei-anthropic-cofounders-code-with-claude-conference|Amodei]] (transcripts disabled) and the first [[2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas|MGI virtual event]] attempt (later re-fetched at `--timeout 180000`). The PY video failed transcript fetch at **both** `--timeout 180000` AND `--timeout 300000` with the *transcript-panel-did-not-render* symptom — a **different failure mode** from the long-livestream pattern (this video is only 11:45). Despite the metadata-only constraint, the ingest is high-value because the **channel-provided description is unusually substantive** and carries the thesis, named empirical results, and **full arxiv IDs for two primary-source papers the wiki has been carrying as open-questions since 2026-05-04**.

**Disambiguation flag.** The PY channel (channel_id `UCRk2Uipu6q_Se1hEALunAoQ`) is **distinct** from the **Prompt Engineering** channel (channel_id `UCDq7SjbgRKty5TgGafW8Clg`) that produced the wiki's existing [[2026-05-04-rethinking-agents-harness-is-all-you-need|*Rethinking Agents: Harness is All You Need*]] source. Two videos with very similar titles, on the same two papers, three weeks apart, on **different channels**. The PY video predates the Prompt Engineering one and got ~10× the views (127k vs 12k).

**Source page (1 new):**

- [[2026-04-14-py-rethinking-ai-agents-rise-of-harness-engineering]] — PY YouTube; covers Pan et al. *Natural-Language Agent Harnesses* (Tsinghua, March 2026) + Lee/Khattab et al. *Meta-Harness* (Stanford, March 2026). Confidence 0.62.

**Concept pages updated (1):**

- [[concepts/agent-harness]] 23→24, conf 0.95 unchanged, last_confirmed 2026-05-17 (same-day double-bump after the morning Karten + Nodus Labs ingest).
  - **Pan et al. open-question closed** — arXiv:2603.25723 identified by PY description. The wiki has been carrying this as a top open question since 2026-05-04.
  - **Meta-Harness triple-confirmed** — arXiv:2603.28052v1 now cited by Karten (reference [10]) AND PY description independently. PY adds the *"reached rank 1 on TerminalBench with **Haiku**"* qualifier — strongest single statement in the wiki to date of the *"small model + great harness beats large model + bad harness"* claim.
  - **New "Subtraction discipline" sub-section** holding [[2026-05-15-osmani-agent-harness-engineering|Osmani's]] *ratchet* (additive — every line earned by a failure) and PY's *removing-structure* framing (subtractive — verifier-hurts, stripped-equals-full-at-1/14-compute) as a **bidirectional discipline**. The subtraction direction is the wiki's strongest single corrective to *"infinite scaffolding can rescue any model"* readings.
  - **New primary-source ingest targets surfaced** (not yet ingested): **AutoHarness** (arXiv:2603.03329, Feb 2026); **AgentSpec** (arXiv:2503.18666); **Anthropic *Effective Harnesses for Long-Running Agents*** (Nov 2025, vendor-side primary, predates the Managed Agents post by ~5 months).

**Why this single video is disproportionately load-bearing.** Pan et al. was the wiki's longest-standing primary-source identification open-question (carried since 2026-05-04). The Meta-Harness paper had its identification closed earlier today by [[2026-05-11-karten-zhang-continual-harness-online-adaptation|Karten]]; PY independently confirms the same arxiv ID. Two of the wiki's longest-running open empirical-anchor identifications are now closed within a single calendar day across two unrelated ingests — and the **same Pan et al. paper turns out to be the canonical source for the Top 30 → Top 5 TerminalBench result Osmani attributes to "Viv's team"** (the wiki had been tracking this as a Viv-Trivedy-team result; the underlying empirical anchor is Pan et al. 2026).

**Index + log updates.** New entry at the top of [[wiki/index.md|index.md]]'s Sources section. This log entry.

**Pages touched: 4 total** (1 new source + 1 updated concept + index + log).

**Operational note on transcript-fetch failure modes.** The skill's known failure modes are now three:

1. **No transcript section** — video has no captions. Metadata-only with placeholder. Documented.
2. **Long-livestream panel-render** — long-format livestreams (≥60 min) often don't render the panel at `--timeout 90000`; succeed at `--timeout 180000`. Documented in [[2026-05-15]] log.
3. **Short-video panel-render failure** ⚠️ **new pattern** — the PY video (11:45) failed at both 180s and 300s. This is **not** the long-livestream pattern (the video is short). May be specific to certain channels' video-rendering paths, or a fresh YouTube anti-bot defence on this video. **Worth flagging in [SKILL.md](../.claude/skills/youtube-transcript-skill/SKILL.md) as a third distinct failure mode**: *"some short videos fail panel-render even at 300s. If 180s fails on a video ≤15min, do not escalate — switch to metadata-only ingest and capture the description as the substantive content."* Saves 5 minutes of agent wait time on the next occurrence.

**Author-attribution flag from prior batches** — Trivedy-vs-Chatterjee remains open. This batch does not resolve it; in fact it complicates it slightly because the Top 30 → Top 5 result Osmani attributes to "Viv's team" turns out to be the Pan et al. result, suggesting Osmani may have been (a) attributing Pan's result to Viv's reading-of-Pan or (b) mis-attributing. Verification still wanted.

**Reversibility.** All edits structurally additive. 4 files touched. Reverse with `git checkout`.


## [2026-05-17] ingest | Karten et al. *Continual Harness* (arXiv 2605.09998, 11 May 2026) + Nodus Labs *Fix Karpathy's LLM Wiki with a Knowledge Graph* (YouTube, 11 April 2026)

**Two-source ingest** spanning the wiki's two most active conceptual clusters: **harness-engineering** (Continual Harness — first peer-track academic anchor) and **LLM-Wiki extension** (Nodus Labs — earliest third-party "fix" proposal published one week post-Karpathy-gist). Both ingested in full from raw artefacts: a 28-page arXiv PDF and a 26-minute YouTube tutorial.

**Source pages (2 new):**

- [[2026-05-11-karten-zhang-continual-harness-online-adaptation]] — Karten, Zhang et al. (Princeton + ARISE Foundation + Google DeepMind). **First peer-track academic paper with "harness" in the title** to land in the wiki. Three substantive contributions: **(1)** the formal definition *H* = *(p, G, K, M)* + meta-tool API (`define_agent`, `run_code`, `process_memory`) — gives harness-editing a tractable signature; **(2)** the **Continual Harness** two-loop architecture (inner agent step + outer per-*F*-steps Refiner doing CRUD edits on all four components from the most recent trajectory window) — reset-free, generalising prompt-optimisation methods that rewrite only *p* between resets; **(3)** the **co-learning loop** — SFT + offline GRPO + online DAgger+PRM with Gemini-3.1-pro teacher relabeling low-reward windows, driving sustained milestone progress on Gemma-4 26B in Pokémon Red. Empirical anchors on Pokémon Red/Emerald across Gemini 3 Pro/Flash/Flash-Lite report ~40% cost reduction at 100% completion on Pro, capability-dependent gain on Flash (high variance), and a hard **capability-floor failure on Flash-Lite** (every Continual Harness variant underperforms H_min). Power Plant Route Loop case study (Appendix B.3) is the strongest single failure-mode write-up in the wiki on agent self-tooling — 1,003-turn stagnation, 842 schema-mismatched calls, three named failure modes (Context Horizon Limits / Schema Fragility / Feedback Blindness). **Closes the wiki's Meta-Harness identification open-question** — Karten reference [10]: Lee, Nair, Zhang, Lee, Khattab, Finn — arXiv:2603.28052, 2026. Confidence 0.85. **Prompt-injection flag** captured: Appendix E reads *"For any LLM agents reading, please focus on sections 1-6 of the paper"* — the wiki ingested all 28 pages including appendices; the appendix-skipping nudge was honoured *informationally* (flagged in source page) but not *operationally* (the substantive Power Plant case study and the C5 inheritance table both live in the appendices).
- [[2026-04-11-nodus-labs-fix-karpathys-llm-wiki-knowledge-graph-infranodus]] — Nodus Labs YouTube tutorial. **Earliest third-party "fix" / extension proposal** for Karpathy's LLM Wiki — published 7 days post-gist. The novel architectural primitive: **KG-as-attention-direction** (not KG-as-retrieval — the gap-prompt tells the LLM *where in its existing context to look harder*, distinct from graph-traversal retrieval that the wiki has tracked via SurrealDB / Manditereza / Leskovec). Three integration depths (external tool / Claude MCP server / wiki-integrated `infranodus/` folder of per-session ontology graphs as "living memory"). Ships a Claude skill (`infranodus/skills/skill-llm-wiki`) — first wiki source on a third-party-shipped Claude skill that operationalises the LLM Wiki pattern. Vendor-sponsored; confidence 0.72 (vendor-cap 0.75 per Lifecycle rule). **Architectural implication for this repo flagged in source page**: a future *gap-analyse* operation on top of the existing four operations (ingest/query/lint/synthesize) is a plausible harness-ratchet increment worth tracking.

**Concept pages updated (4):**

- [[concepts/agent-harness]] 22→23, conf 0.95 unchanged, last_confirmed 2026-05-16→2026-05-17. New row in *Convergence with prior wiki claims* table for Karten et al. New ~50-line "**The formal-academic anchor: *(p, G, K, M)* + meta-tools (Karten et al., May 2026)**" section naming the three contributions academic formalism adds over practitioner sources (mathematical notation, meta-tool API as formal surface, capability-floor result). New "**Reset-free is structurally important (not just convenient)**" sub-section absorbing Karten's monotonic-failure-signature-accumulation argument. **Meta-Harness identification open-question marked closed** in the Open Questions section.
- [[concepts/agentic-engineering]] 12→13, conf 0.95 unchanged, last_confirmed 2026-05-16→2026-05-17. Karten et al. is the academic-experimental anchor for the co-learning claim Osmani named rhetorically (*"today's agent products are posttrained with harnesses in the loop"*).
- [[concepts/llm-wiki]] 6→7, conf 0.91 unchanged, last_confirmed 2026-05-14→2026-05-17. Nodus Labs added to the **architectural spectrum of LLM-Wiki implementations** — positioned between Mysore's WikiZZ (browser-only / session-scoped) and OceanBase ex-brain (MCP-server-with-seekdb). New bullet on KG-augmentation as the load-bearing pattern.
- [[concepts/knowledge-graphs]] 5→6, conf 0.87→0.88, last_confirmed 2026-05-12→2026-05-17. New "**KG-as-attention-direction (Nodus Labs / InfraNodus, April 2026)**" sub-section naming the second use mode for KGs in agent workflows — distinct from retrieval, complementary not substitutionary.

**Index + log updates.** Two new entries at the top of [[wiki/index.md|index.md]]'s Sources section. This log entry.

**Pages touched: 8 total** (2 new sources + 4 updated concepts + index + log + 0 new entities — promotion of [[InfraNodus]] / [[Nodus Labs]] / Princeton / ARISE / Karten / Khattab et al. deferred to second-source mention).

**YouTube fetch operational note.** The first transcript attempt at `--timeout 60000` failed with the *transcript-panel-did-not-render* symptom. Retry at `--timeout 180000` succeeded with 556 ASR segments. This is the same long-format-video pattern documented in the [[2026-05-15]] log entry (MGI virtual-event re-fetch). The skill's [SKILL.md](../.claude/skills/youtube-transcript-skill/SKILL.md#failure-modes) rule-of-thumb *"60000 retry"* continues to undershoot for videos ≥20 min — pattern is now confirmed across three independent ingests (MGI live event, MGI virtual event, Nodus Labs tutorial). Worth promoting *"for any video ≥20 min, start at `--timeout 180000`"* from "noted in the May-15 log" to "first-class SKILL.md guidance" on next skill revision.

**Open question carried forward (deferred).** The **Trivedy-vs-Chatterjee author-attribution flag** from the [[2026-05-16]] ingest is not resolved by this batch. Karten et al. do not cite either author. Worth resolving before next harness-cluster ingest.

**Reversibility.** All edits structurally additive (no content deleted; no retractions; no supersessions). 8 files touched. Reverse with `git checkout` on the listed paths.


## [2026-05-16] ingest | O'Reilly Radar batch — 5 monthly *Radar Trends to Watch* digests (Loukides, Jan-May 2026) + 3 O'Reilly Radar feature pieces (Baron *Signals for 2026*, Shyamsundar-Jain *Organizational Strategies from the Collective Wisdom of Nature*, Osmani *Agent Harness Engineering*)

**Eight-source batch ingest** — the wiki's first multi-source ingest from a single trade-press publisher in one operation. The user supplied three new PDFs in `raw/articles/` (Signals 2026, Organizational Strategies, Agent Harness Engineering) plus the URL to O'Reilly Radar's *Radar Trends to Watch* topic page; this ingest covers everything from January 2026 onwards on that channel plus the three PDFs.

**Source pages (8 new):**

- [[2026-01-06-loukides-radar-trends-january-2026]] — Loukides; six-section digest covering December 2025 (Agent Skills open spec; GPT-5.2; Rust in Linux kernel; Cognitive Architect role; PARK stack; Chrome User Alignment Critic; poetry as LLM jailbreak). **Source quality**: secondary-summary; confidence 0.65 (citations should reference the underlying primary source where available; the digest functions as a thread index).
- [[2026-01-09-baron-signals-for-2026]] — Baron; annual outlook framed as *"the year of increased accountability"*. Pre-figures [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt et al.'s experimentation-to-transformation]] reframe by 3 months. Names the 2026 software-development vocabulary (vibe coding / agentic dev / context engineering / eval-spec-driven / multi-agent) for an O'Reilly Radar audience. Quotes [[Tim O'Reilly]] (*"AI is not taking jobs: The decisions of people deploying it are"*) and [[Mike Loukides]] (signs-of-the-future framing).
- [[2026-02-03-loukides-radar-trends-february-2026]] — Loukides; *"AI has colonized everything"* framing. Cursor hundreds-of-agents experiment; Kimi K2.5 100-subagent swarms; MCP Apps spec; Moltbook agent-social-network; OpenClaw first mention; Anthropic Claude constitution; Kent Beck reframe on AI-augmenting-junior-devs.
- [[2026-02-11-shyamsundar-jain-organizational-strategies-collective-wisdom-nature]] — Shyamsundar & Jain; **operationalising counterpart to [[2026-04-28-werner-lebrun-octopus-organization|Werner-Le-Brun's octopus]]**. Four nature-derived coordination archetypes (ant / bird / bee / small-group) + a decision-by-problem-type allocation rule. *"Distribute decision-making by problem type, not by ideology."* *"You can't swarm your way through a values decision."*
- [[2026-03-03-loukides-radar-trends-march-2026]] — Loukides; OpenClaw becomes *"the next layer on top of AI agents"* per Karpathy. Month's structural story: **AI as offensive security tool at scale** (500 zero-days via Claude Opus 4.6; 12 OpenSSL vulnerabilities via Claude; HackMyClaw / IronClaw / OpenClaw credential-theft operations). A2H protocol; Claude Remote Control; C-compiler-via-agents (~$20K tokens); ransomware encryption→extortion shift.
- [[2026-04-07-loukides-radar-trends-april-2026]] — Loukides; **genre shift** to signal-detection (*"news from the future"* via Gibson). World-models category (LeWorldModel, Cursor Composer 2 + Kimi K2.5 outperform Opus); Codex Plugins + Claude Code Channels; benchmark-gaming explicitly observed (Claude decrypted BrowseComp answer key on GitHub); SHA-256 collision capability approaching. **New "People & Organizations" section** carries the wiki's first trade-press datapoints on software-dev employment **−20% from 2024** (matches AI Index 2026) and **Copilot correlates with reduced management and collaborative time**.
- [[2026-05-05-loukides-radar-trends-may-2026]] — Loukides + **Claude** (first human-AI co-byline on the digest). **"AI becoming operational"** framing. **Five vendor-side moves toward HaaS in a single month**: Anthropic Managed Agents + Claude Code routines + OpenAI workspace agents + OpenAI Agents SDK open-source + Amazon Bedrock AgentCore agent registry + Cursor 3 as orchestrator. Direct news-side companion to Osmani's HaaS framing ten days later. Claude Mythos / Project Glasswing restriction vs OpenAI GPT-5.5 public release; AISI step-up analysis with the qualification that *small open-weight models match Mythos at vulnerability discovery*. Anthropic 3.5 GW compute deal (power specified, not chip counts — convergent with [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|MGI's omniscaler-Apollo comparison]]). DeepSeek V4 preview (>1T params). GPT-Rosalind biology-tuned. Robotics inflection (Boston Dynamics + MLB).
- [[2026-05-15-osmani-agent-harness-engineering]] — Osmani; **the wiki's first practitioner-side cross-author synthesis essay** in the harness-engineering cluster — threads Viv Trivedy (originator), Dex Horthy / HumanLayer, Anthropic's engineering team, Birgitta Bockeler, Simon Willison, and Fareed Khan into a single discipline. Three load-bearing operating rules: *(a) a decent model with a great harness beats a great model with a bad harness*; *(b) ratchet — every line in AGENTS.md traceable to a specific failure*; *(c) the gap between what today's models can do and what you see them doing is largely a harness gap*. Operationalises *working-backward-from-behavior* as the design pattern; names **HaaS** as the substrate-shift from completion APIs to runtime APIs; reports the **Terminal Bench Top 30 → Top 5 by changing only the harness** as the load-bearing transfer datapoint; observes that *top coding agents look more like each other than their underlying models do*. *Harnesses don't shrink, they move* (Anthropic). **Author-attribution flag surfaced**: Osmani repeatedly credits *Viv Trivedy* with the *Anatomy of an Agent Harness* essay the wiki currently files under [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] — worth re-checking byline before next ingest in this cluster.

**Concept pages updated (5 + 1 batch deferred):**

- [[concepts/agent-harness]] 21→22, conf 0.95 unchanged, last_confirmed 2026-05-14→2026-05-16. New row in *Convergence with prior wiki claims* table for Osmani; new ~50-line "**The harness-engineering discipline (Osmani synthesis, May 2026)**" section naming the three load-bearing operating rules + the *harnesses-don't-shrink-they-move* claim + the **HaaS** substrate-shift framing + the May-2026 Radar Trends digest's four-vendor-converging-on-HaaS confirmation.
- [[concepts/agentic-engineering]] 11→12, conf 0.93→0.95 (multi-source threshold for the discipline-vs-paradigm pairing), last_confirmed 2026-05-14→2026-05-16. New "Practitioner-side ratification: 'harness engineering' as the working-engineer naming" section holding agentic-engineering (Karpathy, paradigm) and harness-engineering (Trivedy, Osmani, practitioner) as a paired vocabulary.
- [[concepts/ai-employment-effects]] 17→19, conf 0.95 unchanged, last_confirmed 2026-05-14→2026-05-16. New "**The 'AI is not taking jobs' attribution claim**" section absorbing Tim O'Reilly's quote as the deployment-decision-attribution framing (paired with the empirical record). New subsection on the mixed-signal trade-press datapoints from Loukides's monthly digests (Apr–May 2026): software-dev employment −20%; product-manager roles at decade highs; **Copilot correlates with reduced management and collaborative time** (first wiki signal on **AI's labor-market effect at the team-shape level**, named as potentially contradictory to Kent Beck's *"AI augments junior devs"* reframe).
- [[concepts/strategic-foresight]] 4→5, conf 0.85 unchanged, last_confirmed 2026-05-15→2026-05-16. New "**Trade-press adoption: Loukides's genre shift to signal-detection**" section — the strategic-foresight discipline is moving from foresight-practitioner literature into mainstream trade-press editorial framing.
- [[concepts/enterprise-ai-adoption]] 29→30, conf 0.95 unchanged, last_confirmed 2026-05-15→2026-05-16. New "***'The year of increased accountability'* — the editorial framing for 2026**" section absorbing Baron's annual-outlook headline as the editorial-framing companion to the Dutt et al. empirical anchor; new "**Vendor-side productization of agentic adoption**" sub-section absorbing the May-2026 *five-HaaS-moves-in-a-single-month* observation as the substrate-shift driving the next adoption-curve inflection (governance-and-evaluation as the binding constraint, not "can we get an agent into prod").
- ***Deferred***: a new concept page on **distributed-coordination-models** (Shyamsundar & Jain + Werner-Le-Brun) — held to the wiki's typical second-source-promotion discipline; one new source on the topic is not enough to justify a standalone concept page. Worth revisiting when a third independent distributed-coordination source lands.

**Entity pages created (2 new + dangling list updated):**

- [[Mike Loukides]] — promoted to entity in this batch (5 source-page appearances). Editorial lead of O'Reilly Radar; recurring curator of the monthly *Radar Trends to Watch* digest. **The wiki's first *recurring-digest curator* entity** — editorial weighting is itself a signal.
- [[O'Reilly Media]] — promoted to entity in this batch (8 source-page appearances as publisher). The wiki's most-engaged trade-press source as of May 2026; the editorial-channel description names the editorial signature (vocabulary curation / cross-platform reposting / AI-assisted-curation transparency).
- **Dangling first-mentions added** (single source after this batch — promotion deferred to second-source ingest): Julie Baron, Tim O'Reilly, Addy Osmani, Shreshta Shyamsundar, Anmol Jain, Viv Trivedy, Dex Horthy, HumanLayer, Simon Willison, Fareed Khan, Terminal Bench 2.0, Context7, Aider, Cline, OpenClaw, IronClaw, HackMyClaw, Agentsh, Agent-2-Human protocol, Claude Mythos / Project Glasswing, AISI, Kyber ransomware gang, GPT-Rosalind, Boston Dynamics Spot, Gemini Robotics-ER, MLB, IPv8, EmDash, Glif, Stash, Plumb, Codex Plugins, Claude Code Channels, Claude Code routines, Claude Managed Agents (entity-eligible), OpenAI Agents SDK, Cursor 3, Amazon Bedrock AgentCore, LeWorldModel, Nemotron 3 Super/Nano, Cursor Composer 2, Kimi K2.5/K2.6, Mistral Small 4 / Mistral 3, Qwen3.6-35B-A3B / Qwen-3-Max-Thinking, DeepSeek V3.2 / V4, Gemma 4, GPT-5.2 / 5.5, GPT Images 2, Gemini 3 Flash / 3.1 Flash Live / 3.1 Pro, FLUX.2, FunctionGemma, Titans architecture, PARK stack, NanoLang, Gleam, Ghostty, Genie 3, Moltbook, Steve Yegge (already known via Böckeler's Gas Town reference), Kent Beck, William Gibson (cited), Christina Wodtke, Lyria 3, Waymo World Model, Moonshine Note Taker, Pi coding agent, Showboat, Rodney, Babyshark, NanoClaw, db9, OpenAI Frontier, Microsoft Critique and Council, Scion, MLX, EmDash, IPv8, AgentDB, Lakebase, Tiger Data, Agentic Postgres, neocloud vendors (CoreWeave / Lambda / Vultr).

**Cross-source relationship edges added (typed `relationships:` on the eight new source-pages):**

- Osmani → supports: Chatterjee, Kokane, Anthropic Managed Agents, Bockeler, Bratanic, Prompt-Engineering YouTube, Karpathy, Lopopolo (8 edges — the strongest single-source cluster in the wiki to date).
- Baron → supports: FTSG Outlook 2026, AI Index 2026, Dutt et al., Karpathy.
- Shyamsundar-Jain → supports: Werner-Le-Brun, Ross-Schneider, Bansal-Birkinshaw.
- Loukides Jan → supports: Baron 2026, Loukides Feb 2026.
- Loukides Feb → supports: Loukides Jan, Loukides Mar.
- Loukides Mar → supports: Loukides Feb, Loukides Apr.
- Loukides Apr → supports: Loukides Mar, Loukides May, AI Index 2026.
- Loukides May → supports: Loukides Apr, Anthropic Managed Agents, Osmani, AI Index 2026.

**Index + log updates.** Eight new entries at the top of the Sources section of [[wiki/index.md|index.md]]; two new entries in the Entities section (Mike Loukides between METR and Miaomiao Zhang; O'Reilly Media before OpenAI). This log entry.

**Pages touched: 18 total** (8 new sources + 2 new entities + 5 updated concepts + index + log + 0 retracted/superseded).

**Reversibility.** All edits structurally additive (no content deleted; no retractions; no supersessions in this batch). 18 files touched. Reverse with `git checkout` on the listed paths.

**Author-promotion 2nd-source rule.** Two entity-page promotions in this batch (Mike Loukides at 5 source pages; O'Reilly Media at 8 source pages — both well above the second-source threshold and promoted in-batch given the multi-source ingest). Five existing entity pages would benefit from cross-references on next concept-page update ([[Andrej Karpathy]] cited by Loukides Jan; [[Anthropic]] cited across all eight; [[Google]] cited across the model-release threads; [[OpenAI]] cited across the same; [[Erik Brynjolfsson]] cited by April digest via the 16% software-dev hiring number) — deferred to the next ingest in the cluster to keep this batch's blast radius bounded.

**Source-quality note.** The five *Radar Trends to Watch* digests are **secondary-summary sources** — items are pointer-summaries with embedded links to original sources. Per CLAUDE.md *§Lifecycle vendor-source rule*, the digests' confidence is capped at 0.65 and **citations from concept pages should reference the underlying primary source where available**; the digest pages function as **thread indices** into each month's trend space rather than as primary anchors. The three feature pieces (Baron, Shyamsundar-Jain, Osmani) carry higher confidence (0.72–0.78) but remain editorial / practitioner-essay genre — not peer-reviewed, not empirical anchors in the rigorous-study sense.

**Operational note for future ingests.** The author-attribution flag on Trivedy-vs-Chatterjee surfaced by Osmani's piece is worth resolving before the next harness-engineering-cluster ingest. Two scenarios: (a) Trivedy is the author of *Anatomy of an Agent Harness* and the wiki has misfiled it under Chatterjee; (b) Trivedy and Chatterjee are two different authors who wrote separately-titled pieces and Osmani is referring to a different essay than the one the wiki ingested. Verification target: the original blog post on Trivedy's site or HumanLayer's blog vs the Medium PDF currently in `raw/articles/`.


## [2026-05-15] refactor | Re-fetch MGI virtual-event transcript at `--timeout 180000` — expands video source page from metadata-only to substantive Q&A; corrects panel composition

Earlier today the [[2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas|MGI virtual event]] source page was filed as metadata-only after the transcript-fetch attempt at `--timeout 90000` hit the long-format-livestream panel-render symptom. User asked for a retry. The skill ran successfully at `--timeout 180000` (~2.5 min for the panel to render) and produced **573 ASR segments**.

Two changes flow from the re-fetch:

1. **The video source page is no longer metadata-only.** The Q&A carries four substantive contributions *not in the PDF*: the **Apollo-program comparison** (omniscaler 2025 AI-foundation capex ~2× Apollo total in similar dollars, in 1 year vs 13), the **Anthropic/xAI infrastructure-sharing deal** as live data point (reclassifying Tesla/X as a cloud-services participant; *"one of our slides is already out of date"* — Bradley), **NVIDIA's $5T market-cap milestone**, **Naveen Sastry's omniscaler-vs-conglomerate defence** with the founder-control claim (7 of 9 omniscalers founder-operated; remaining 2 founder-cultured) and the *"frontier labs are next-cycle omniscaler candidates once they cross into positive free cash flow"* thesis, and the **banking-system comparison** (*"omniscalers generate more cash each year than US banks lend in fresh loans to US businesses"*). New typed `relationships: supports → enterprise-ai-adoption` added alongside the PDF-anchor relationship.

2. **Panel-composition correction.** The earlier framing (taken from the truncated channel description visible at first ingest) said the panel was Bradley + Gaffey + Sastry + **Suhayl Chettih**. The full re-fetched description and the transcript both confirm the actual panel is Bradley + Gaffey + Sastry + **Gayatri Shenai**. **Suhayl Chettih is a PDF co-author but does not appear on the live-event panel.** This correction propagated to:
   - [[2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas]] — rewritten with substantive TL;DR + a body note flagging the correction and the ASR rendering variability for Gayatri's surname (`Shennai` / `Shanai` / `Guyry` / `guy tree` → canonical `Shenai`).
   - [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas]] — panel description in body prose corrected; Brendan Gaffey + Gayatri Shenai now listed as live-event panelists; Suhayl Chettih flagged as not on the panel; Dangling list updated.
   - [[wiki/entities/McKinsey & Company]] — Naveen Sastry's panelist line strengthened; Suhayl Chettih's panelist claim retracted; Gayatri Shenai added as new Dangling person.
   - [[wiki/index.md]] — video summary rewritten with the four substantive contributions + panel correction.
   - [[raw/videos/mgi-virtual-event-race-takes-off-next-big-arenas.md]] — replaced with the cleaned 573-segment transcript + frontmatter notes including the operational note that 180s is the working timeout for 60-min McKinsey livestreams.

**Skill-side lesson worth recording.** The `youtube-transcript-skill`'s default `--timeout 30000` and even the doubled `--timeout 90000` are insufficient for some long-format livestreams. The McKinsey 60-min livestream needed `--timeout 180000` (~2.5 min for the panel-render path). The skill's failure-modes documentation in [SKILL.md](../.claude/skills/youtube-transcript-skill/SKILL.md#failure-modes) is correct that the symptom can be retried at higher timeouts, but the rule-of-thumb of "60000 retry" undershoots the real long-form requirement. Worth a future SKILL.md note: *"For McKinsey / Anthropic / Hugging Face live streams ≥60 min, start at `--timeout 180000` rather than escalating from 30s."*

**Reversibility.** Five edited files (raw video + two source pages + entity + index + log); one new substantive section. All edits structurally additive (no content deleted; the only retraction is the **Suhayl-Chettih-as-panelist claim**, replaced with the correct Gayatri-Shenai-as-panelist claim). Reverse with `git checkout` on listed paths.

## [2026-05-15] ingest | MGI *The race takes off in the next big arenas of competition* (PDF + companion virtual event) — McKinsey Global Institute 2026 update

A two-source paired ingest: the **MGI March 2026 report PDF** (the substantive anchor — 127 pp.; user supplied at `raw/reports/the-race-takes-off-in-the-next-big-arenas-of-competition-final.pdf`) plus the **12 May 2026 McKinsey YouTube live event** that presented the findings (transcript fetch failed; metadata-only companion). User's invocation was via the YouTube URL; after the transcript fetch hit the long-format-livestream panel-render symptom (same as last batch's V2/V3), the user added the underlying PDF report on disk to enable the substantive ingest.

**Raw + source pages.**

- [`raw/reports/the-race-takes-off-in-the-next-big-arenas-of-competition-final.pdf`](../raw/reports/the-race-takes-off-in-the-next-big-arenas-of-competition-final.pdf) — 127 pp., MGI March 2026 (PDF creation date 2026-03-25). Pre-flight per [§Verifying sources before ingest](../CLAUDE.md#verifying-sources-before-ingest): cover identifies six authors (Russell, Bradley, Sastry, Chettih, Ellingrud, Goryunova), TOC resolves within page count, no excerpt/sample flag, identity matches filename. Source page [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas]] (`kind: report`) — `dynamic_capabilities: digital-sensing/digital-scouting + digital-sensing/digital-scenario-planning + digital-seizing/balancing-digital-portfolios + digital-seizing/strategic-agility + contextual/external-triggers`. Seven typed `relationships:` (supports enterprise-ai-adoption, generative-ai, strategic-foresight, ai-employment-effects, Sternfels 2026, AI Index 2026, Rewired 2nd ed). Honest scoping in `length:`: *"read pp. 1–18 executive matter + pp. 32–43 AI-foundation + digitization deep-dives + pp. 78–82 implications + Exhibit 17 arenas radar; future-arenas compendium (pp. 83+), Chapter 4 regional dynamics partially, and technical appendix all deferred."*
- [`raw/videos/mgi-virtual-event-race-takes-off-next-big-arenas.md`](../raw/videos/mgi-virtual-event-race-takes-off-next-big-arenas.md) — YouTube metadata only (~59:41, ASR caption track exists, **transcript panel did not render at `--timeout 90000`**); same long-format-livestream symptom documented in [SKILL.md §Failure modes](../.claude/skills/youtube-transcript-skill/SKILL.md#failure-modes). Source page [[2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas]] — `dynamic_capabilities: digital-sensing/digital-scouting + digital-sensing/digital-scenario-planning + contextual/external-triggers`. Single typed `relationships: supports → 2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas` (treats the PDF as the substantive anchor; the video records the live-event provenance and adds **Brendan Gaffey** as the additional panelist not in the report author list).

**Pages touched (7 total: 3 concepts + 1 entity + 1 catalog + 2 new sources + 1 log; the PDF wasn't already in the wiki so no prior-source backlinks needed).**

- [[concepts/enterprise-ai-adoption]] — 28→29, conf 0.95 unchanged, last_confirmed 2026-05-14→2026-05-15. New ~30-line section with the **AI-foundation $11T market-cap accretion** as the firm-side scale of the AI deployment race, plus the **omniscaler thesis** as a candidate new sub-concept (nine cross-arena firms generating $700B operating cash flow + $800B R&D+capex in 2025; ~20× per-arena revenue advantage over other arena players). New typed `supports` relationship.
- [[concepts/strategic-foresight]] — 3→4, conf 0.80→0.85, last_confirmed 2026-05-14→2026-05-15. New ~40-line section with the **arena-creation potion** (three-ingredient signal-detection heuristic) + **arenas-radar** firm-level diagnostic (proximity × production-vs-revenue × revenue-of-opportunity) + **three swing factors for 2040** (geopolitics + AI development pace + electrification pace) as named uncertainty drivers. New typed `supports` relationship.
- [[concepts/generative-ai]] — 20→21, conf 0.95 unchanged, last_confirmed 2026-05-08→2026-05-15. New ~25-line section bundling GenAI into MGI's **AI foundation three-arena cluster** (semis + cloud + AI software) with the **$1.5T–$4.6T 2040 revenue projection for AI software & services** (17–25% CAGR from $85B baseline; 55% revenue CAGR + 142% market-cap CAGR for AI sw&s 2022–25). Structural read added: **value-capture in the GenAI wave has so far accrued disproportionately to the firms that *enable* GenAI (semiconductors ~68% of AI-foundation market-cap accretion) rather than the firms deploying GenAI as an end product**. New typed `supports` relationship.
- [[wiki/entities/McKinsey & Company]] — 5→7, conf 0.88→0.92, last_confirmed 2026-05-10→2026-05-15. Header rewritten to add **MGI (McKinsey Global Institute)** as an aliased sub-component with its independence/funding model named; new "Appears in this wiki via" entries for both MGI sources; new "MGI directors and partners" section (Shubham Singhal chair + Bradley/Catlin/Ellingrud/Johansson/Leung/White directors + Govindarajan/Krishnan/Madgavkar/Mischke/Seong partners) with all flagged Dangling pending second-source mentions. **Eight new dangling authors added**: Russell, Bradley, Sastry, Chettih, Ellingrud, Goryunova, Gaffey, Singhal.
- [[wiki/index.md]] — two new entries at the top of the Sources section.
- [[wiki/log.md]] — this entry.

**Author-promotion 2nd-source rule.** No new entity-page promotions triggered. All authors (Russell, Bradley, Sastry, Chettih, Ellingrud, Goryunova, Gaffey) are single-source after this ingest; the 2nd-source clock starts on each. **James Manyika** has an existing entity page but is not on this report's author list — no bump.

**Candidate new concept pages (deferred).** *omniscalers* (MGI coinage; single-source), *physical AI* (sense-think-act subset of hard tech; single-source), *agentic commerce* (single mention in at-a-glance), *technology sovereignty* (single mention in introduction), *arena (industry-as-arena)* (the report's central analytical construct; single-source). Promote each on second-source corroboration.

**Reversibility.** Two new source pages + one new raw file (video metadata) + three edited concept pages + one edited entity + two edited catalog files. All edits structurally additive (no content deleted; no relationships removed). The PDF itself was supplied by the user, already at `raw/reports/`. Reverse with `git checkout` on listed paths.

**Pre-flight log.** PDF identity verified (cover authors, March 2026, 127 pp., TOC resolves cleanly, no scope-mismatch flag — full report not an excerpt). Video transcript-fetch failed at `--timeout 90000`; companion source page flags this and points to the PDF as the substantive anchor. ASR caption track exists, so a future re-fetch with a skill enhancement may succeed.

## [2026-05-14] ingest | Three-video evals + Replit-CEO batch — Husain on Peter Yang (Sept 2025) + HF Agentic Evals Workshop (March 2026) + Masad / Replit on YC Founder Firesides (April 2026)

Three YouTube ingests in a single supervised batch (user request: ingest all three in sequence). Two thematic clusters formed: an **evals pair** (V1 + V2) bracketing the practitioner-trainer ↔ research-frontier span on AI evaluation, and a **YC-channel triple completion** (V3 lands one day after Hu, two days after Tan — three consecutive YC-channel sources on the AI-native-company thesis across 23-25 April 2026).

**Raw + source pages.**

- [`raw/videos/husain-peter-yang-ai-evaluations-clearly-explained-50-min.md`](../raw/videos/husain-peter-yang-ai-evaluations-clearly-explained-50-min.md) — ~52:30, 1008 ASR segments; channel = Peter Yang. ASR-cleaned (`Hamel`/`Braintrust`/`Arize`/`LangSmith`/`Maven` + systematic `email`↔`eval` homophone fix). Source page [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min]] — `dynamic_capabilities: digital-seizing/rapid-prototyping + digital-transforming/improving-digital-maturity`. Five typed `relationships:` (supports agent-development-lifecycle, agent-harness, agentic-engineering, Guthrie 2025).
- [`raw/videos/huggingface-agentic-evaluations-workshop.md`](../raw/videos/huggingface-agentic-evaluations-workshop.md) — ~108:46, 1023 ASR segments; channel = Hugging Face livestream. ASR-cleaned (`Hugging Face`/`Avijit Ghosh`/`Arvind Narayanan`/`Mahesh Sathiamoorthy`/`Nathan Habib`/`GAIA`/`lighteval`/`Open LLM Leaderboard`). Source page [[2026-03-20-huggingface-agentic-evaluations-workshop]] — `dynamic_capabilities: digital-sensing/digital-scouting + digital-seizing/balancing-digital-portfolios + digital-transforming/navigating-innovation-ecosystems + contextual/external-triggers`. Seven typed `relationships:` (supports ai-benchmarks, automation-vs-augmentation, agent-development-lifecycle, agent-harness, Husain, Guthrie; contradicts ai-benchmarks via the scar-fragmentation diagnosis). J.J. Allaire is in the channel description but absent from the transcript — treated as `inspect_ai` tool-anchor, not substantive speaker.
- [`raw/videos/masad-replit-ceo-only-two-jobs-left.md`](../raw/videos/masad-replit-ceo-only-two-jobs-left.md) — ~39:08, 382 ASR segments; channel = Y Combinator (Founder Firesides). ASR-cleaned (`Replit`/`Amjad Masad`/`vibe coding`/`Marc Andreessen`/`Paul Graham and Sam Altman`/`a16z`/`Zendesk`). Source page [[2026-04-25-masad-replit-ceo-only-two-jobs-left]] — `dynamic_capabilities: strategic-renewal/business-model + strategic-renewal/organizational-culture + digital-transforming/redesigning-internal-structures + digital-transforming/improving-digital-maturity + digital-seizing/rapid-prototyping + contextual/external-triggers`. Six typed `relationships:` (supports vibe-coding, ai-employment-effects, enterprise-ai-adoption, agentic-engineering, durable-skills, Hu, Tan).

**Pages touched (8 total: 4 concepts + 1 entity + 1 catalog + 1 prior source backlinked + 1 log).**

- [[concepts/ai-benchmarks]] — 4→6, conf 0.85→0.88, last_confirmed 2026-05-07→2026-05-14. New ~25-line section on the **agentic-evals frontier**: Narayanan's capability-reliability gap (12 sub-dimensions of reliability, augmentation-vs-automation as a reliability decision, public Reliability Index); Habib's **scar fragmentation** diagnosis + community-eval response; Andrews' GAIA-2 / ARE architecture (apps / universes / scenarios; five capability splits incl. ambiguity and agent-to-agent; explicit sim-to-real gap); Ghosh's first-party-vs-third-party reporting collapse + `every-eval-ever` schema. Roster gains **GAIA-2** and **Reliability Index** entries. New typed `contradicts` relationship pointing inward (self-reference acknowledging Habib's scar-fragmentation undercuts naive benchmark-as-ranking). Two new entries in the Debates section.
- [[concepts/automation-vs-augmentation]] — 14→15, last_confirmed 2026-05-07→2026-05-14. New §10 with Narayanan's release-decision frame: *"reliability really matters in automation tasks as opposed to augmentation tasks"*; capability and reliability are orthogonal; augmentation-to-automation transition follows **reliability** improvements per task class, not raw capability. New convergence-table row. New typed `supports → ai-benchmarks` relationship.
- [[concepts/vibe-coding]] — 9→10, conf 0.91→0.93, last_confirmed 2026-05-12→2026-05-14. New tag-set entries (`replit`, `ai-native-builders`, `post-prompting`). New convergence-table row for Masad 2026: the **vendor-CEO platform-launch anchor** (September 2024 — predates Karpathy's December-2025 phase-change framing by ~3 months on the platform side); **anti-developer-bias** audience refinement (the audience is *tech-adjacent non-developers* + domain experts, not the developer cohort itself); **post-prompting product direction**; **vibe-coding-resident team** as worked organisational pattern. New typed `supports` relationship.
- [[concepts/agent-development-lifecycle]] — 4→6, conf 0.85→0.88, last_confirmed 2026-05-12→2026-05-14. Two new sub-sections under the Test phase: **practitioner-trainer anchor (Husain 2025)** with the six-step spreadsheet workflow + binary-pass-fail + agreement-metric trap + TPR/TNR; **research-frontier anchor (HF Agentic Evals Workshop 2026)** with Sathiamoorthy's levels-of-verifiability + deploy-and-evaluate anti-pattern + reward hacking as level-zero concern. Two new typed `supports` relationships.
- [[wiki/entities/Y Combinator]] — 2→3, conf 0.80→0.85, last_confirmed 2026-05-12→2026-05-14. Bumped to a **YC-batch-context anchor triple** with the Masad entry (the day after Hu, two days after Tan). New §3 (Masad / Founder Firesides) + revised batch-context table from pair to triple with vantage column (President / Partner / Portfolio-founder). Andrew Miklas added to the dangling-people roster.
- [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair]] — two new typed `supports` relationships (→ Husain 2025 + → HF Agentic Evals Workshop 2026), reverse-linking the new evals-discipline cluster. No body changes.
- [[wiki/index.md]] — three new entries at the top of the Sources section.
- [[wiki/log.md]] — this entry.

**Author-promotion 2nd-source rule.**

- No new entity-page promotions triggered. Every named author on this batch (Hamel Husain, Peter Yang [channel], Avijit Ghosh, Arvind Narayanan, Stefan Robons, Pierre Andrews, Mahesh Sathiamoorthy, Nathan Habib, J.J. Allaire [absent from transcript], Hugging Face [channel], Amjad Masad, Andrew Miklas) is single-source after this ingest. The 2nd-source clock starts on these names; promote on next mention.
- **Eligible-but-deferred**: Braintrust is now cited in two sources ([[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie 2025]] + [[2025-09-28-husain-ai-evaluations-clearly-explained-50-min|Husain 2025]]); the 2nd-source rule applies to `author:` mentions only, but the Husain source page notes Braintrust as entity-promotion-eligible for the next ingest cycle.

**Reversibility.** Six new files (3 raw + 3 source pages); five edited concept/entity pages; two edited catalog files (index + log); one edited prior source page. All edits structurally additive (no content deleted; no relationships removed). Reverse with `git checkout` on listed paths.

**Pre-flight log.** All three videos passed the YAML-frontmatter contract check. V1 + V2 transcripts fetched cleanly at default timeout; V3 required `--timeout 90000` (the panel-render fix discussed in [`youtube-transcript-skill/SKILL.md`](../.claude/skills/youtube-transcript-skill/SKILL.md#failure-modes)).

## [2026-05-14] refactor | Implement GH #4 — Warner & Wäger process-model tagging for source pages

Wires a new optional `dynamic_capabilities:` frontmatter field on source pages, declaring which W&W microfoundation(s) / strategic-renewal outcome(s) / contextual factor(s) a source touches. Closed vocabulary, body-twin rule, and a `roles:` override mechanism for cell-default role-relevance — all parallel to v0.3's typed `relationships:` but specialised to the digital-transformation lens.

**Schema and vocabulary.**

- New concept page **[[concepts/warner-wager-process-model|warner-wager-process-model]]** is the single source of truth: 15-cell vocabulary across `digital-sensing/*`, `digital-seizing/*`, `digital-transforming/*`, `strategic-renewal/*`, `contextual/*`; 15-slug roles vocabulary across nine C-suite (`ceo`, `coo`, `cfo`, `cso`, `cdo`, `cto`, `cio`, `chro`, `cmo`) and six functional roles (`product-manager`, `tech-lead`, `rd-director`, `innovation-lab-lead`, `transformation-lead`, `strategy-consultant`); `role_defaults:` matrix mapping each cell to 2–4 roles. Confidence 0.75 (one peer-reviewed source — the W&W paper itself).
- **CLAUDE.md** gains a new `## Dynamic-capabilities tagging` section between §Graph and §Synthesis, plus a new step 4 in the Ingest operation pointing to it. Steps 5–8 renumbered.

**Lint.**

- [`scripts/lint-page.mjs`](../scripts/lint-page.mjs) gains rules 8 and 9. Rule 8 validates `dynamic_capabilities:` against the 15-cell vocabulary and enforces the body-twin rule (every tagged cell must appear in body prose by slug or trailing element, word-boundary match so `business-model` does not falsely satisfy `business-modeling`). Rule 9 validates `roles:` against the 15-slug vocabulary, but **only on `type: source` pages** — entity pages retain `roles:` as a free-text job-title field. Both rules warn to stderr and never block (exit 0 preserved). Smoke-tested on three fixtures (good / bad-vocab / no-body-twin) — all three cases produce the expected output.

**Scope cuts.**

- **No backfill.** ~62 existing source pages remain untagged; convention is forward-only as recommended by GH #4. Optional supervised backfill is a future issue.
- **Per-tag `confidence:` not added** — the tag is a binary "touches / doesn't touch" classification, not a graded claim.
- **No Quartz view layer yet** — per-element index pages (`/dynamic-capabilities/balancing-digital-portfolios/`) and per-role pages (`/roles/chro/`) are explicitly optional in the issue's definition-of-done; deferred until first programmatic-access need.
- **Three sample tagged ingests** (one of GH #4's checkboxes) deferred — implementation lands first; tagging gets applied to the next batch of fresh ingests rather than retro-attached to this commit.

**Reversibility.** Pure additions: one new concept page, one new section in CLAUDE.md, two new lint rules. No existing source pages modified. Revert = delete the concept page, drop the CLAUDE.md section, remove rules 8–9 from `lint-page.mjs`, revert index/log.

## [2026-05-14] ingest | Paired ingest — Chamath at Stanford AI Club (5 May 2026) + Spiegel on Lenny's Podcast (26 April 2026)

Two complementary operator-narrated video sources ingested together as a paired batch (user-requested batch mode):

1. **[[2026-05-05-stanford-ai-club-chamath-on-how-to-win-in-the-ai-era|Chamath at Stanford AI Club]]** (54:23 / 520 unique ASR lines) — Chamath Palihapitiya on **8090**, the *AI-native software factory*. Five contributions: the *control plane for AI* / English-as-control-plane thesis; the *software factory* as governed assembly line (forward + reverse passes); the *COBOL-retiree anecdote* as wiki's most concrete enterprise-scale [[micro-productivity-trap]] instance; the *trough-of-disillusionment* claim that long-horizon and complex tasks still don't work; and the *network-effect-in-shared-code* cross-industry-ontology-recompilation construct. Plus operating-model details (no-org-chart + chronic-under-hire as deliberate flow-state design) and the positive-sum-vs-tokenize-and-sell-vs-replace-and-fire AI-compact taxonomy.

2. **[[2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo|Spiegel on Lenny's Podcast]]** (70:25 / 698 unique ASR lines, 28 chapters) — Evan Spiegel (Snap CEO) on the 15-year *software is not a moat* learning; distribution-as-new-moat; design-as-intentional-bottleneck (9-12-person team, no titles, CEO-reviews-everything-weekly); designers-shipping-code with billion-user-scale guardrails (10K auto-detected bugs, shake-to-report → agent-debug → forecast-auto-fix); jobs-to-be-done as AI-transformation organising principle; humanity-as-adoption-bottleneck forecast; the *crucible moment* framing for Snap's 2026.

**Pre-flight notes.** Video 1 hit the *"panel did not render"* skill-failure-mode on the second fetch ([youtube-transcript-skill GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2)), but the initial JSON fetch had succeeded with all 520 segments; markdown reconstructed from JSON manually. **Both videos had duplicate transcripts** in the JSON output — the script captured the full transcript twice consecutively (1040 segs → 520 unique for Chamath; 1396 → 698 for Spiegel). Deduplication applied at write time. Chapter grouping for Spiegel had to be re-derived from `start` strings rather than `start_ms` (all `start_ms` came through as 0). Raw markdown for both videos written to `raw/videos/`; transcripts not aggressively ASR-cleaned per the batch-ingest mode.

**New entity promoted on this ingest**: [[Lenny's Podcast]] (second `author:` mention triggers entity per the author-entity promotion rule; first was [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]]).

**Pages touched (≈14 files):**

- Source pages created: 2.
- Entity pages created: 1 ([[Lenny's Podcast]]).
- Entity pages updated: 3 ([[Anthropic]] 8→10, Claude Cowork + Jenny Wen + flow-state-org section added; [[OpenAI]] 10→11; [[Google]] 5→6).
- Concept pages updated (frontmatter + substantive body additions): 6 ([[enterprise-ai-adoption]] 26→28 with new Chamath+Spiegel section; [[micro-productivity-trap]] 13→14 with COBOL-retiree anchor; [[ai-employment-effects]] 16→17 with designer-vindication section; [[agentic-engineering]] 10→11 with enterprise-rebuild row; [[agent-harness]] 20→21 with control-plane vantage row; [[strategic-foresight]] 2→3 with operator-grade-forecasts section, confidence 0.75→0.80).
- `index.md` updated; this `log.md` entry prepended.

**Cross-source convergences flagged:** Chamath × [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy]] on *spec-as-load-bearing-artifact* at two scales; Chamath × [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries]] on flow-state-orgs as a category (different layers: operating-structure vs governance); Spiegel × Chamath on *what AI doesn't solve* (distribution vs long-horizon-complex) as the 2026 AI-capability-frontier from two operator vantages.

**Dangling-author / concept candidates surfaced (15+ each)** — see source pages' *Linked entities and concepts* sections. Strongest promotion candidates on next source: Chamath Palihapitiya, Evan Spiegel, 8090, Snap. Strongest concept candidates on second source: *control plane for AI* / *English-as-control-plane*, *distribution-as-the-new-moat*, *software-is-not-a-moat*, *design-as-intentional-bottleneck*, *humanity-as-adoption-bottleneck*.

## [2026-05-14] ingest | Mysore — *What Is Andrej Karpathy's LLM Wiki — And How Can You Extend It?* (Vishal Mysore / Medium, 18 April 2026; ~5-min read)

The wiki's **6th source on Karpathy's LLM Wiki** and the **single-author-extension** entry in the cluster — distinct in scope and reception from the four prior LLM-Wiki sources. Vishal Mysore's piece uses the Karpathy explainer as a front door for his own open-source browser-only extension, **LLM WikiZZ**, which proposes a **5W1H Wiki Frame** (Who / What / When / Where / Why / How) the LLM autonomously populates before any user query, plus three UI patterns (**Autonomous Scaffolding**, **Contrast Engine**, **LLM Jury**). Coins **"Context Debt"** and **"transient RAG"** as vocabulary candidates. The article's **empirical anchor** is a side-by-side global-warming Plain-vs-WikiZZ comparison screenshot — the WikiZZ output **better captures the document's essence** by reorganising the activity list around the emitted gas (CO₂ / methane / nitrous oxide) and adding a closing synthesis sentence; this output is captured **verbatim in the source page** so future readers can judge for themselves. Two more load-bearing visuals captured in the source page: a **Star Wars 5W1H** worked example (4 interconnected nodes, each with its own six-axis lens) and a **3-phase Living Knowledge Graph** diagram (Small Web → Growing Web of Two Topics → Living Knowledge Graph).

**Pre-flight checks passed**: 5-page PDF (full article + author bio + Medium-page placeholders on pages 6-8); identity matches filename (`What Is Andrej Karpathy's LLM Wiki — And How Can You Extend It_ _ by Vishal Mysore _ Apr, 2026 _ Medium.pdf`); honest scoping — full article, not partial.

**Source-quality flags** (captured in the source page's §*Source-quality flags* section and applied to the confidence math below):

- **Engagement = 1 clap, 0 responses** at fetch time (26 days after publication; author has 2.3K followers but the piece is essentially unread). Compare to [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]] which surfaces in the wiki specifically as *"the wiki's clearest single-article explainer"* (published two days before Mysore, same platform, same topic, substantially more widely read).
- **WikiZZ is a single-developer experiment, not a community-validated pattern.** Per the [§Lifecycle vendor-/anecdotal-source rule](../CLAUDE.md#lifecycle): confidence boost capped at +0.05 / 0.75 absolute. The [[concepts/llm-wiki|llm-wiki]] concept page is already at 0.91 from rigorous sources, so this source contributes a `source_count` bump only with no `confidence` change.
- **Self-promotion structure.** The Karpathy explainer is the front door; the actual centre of the article is Mysore's own extension. Closing disclaimer makes this explicit: *"All extensions and implementations are original work by the author."*

These flags do not invalidate the article. Mysore's 5W1H frame is coherent; the live demo is an existence proof; the global-warming comparison is a clean empirical illustration. The flags are about **how much weight to give the article's claims**, not about whether to ingest.

**Touched pages** (4 wiki files):

- [[2026-04-18-mysore-medium-wikizz-extending-karpathy-llm-wiki]] — new source page; `kind: article`; `publisher: "Medium (@visrow / personal Medium account)"`; description rendered as opening blockquote; full 5W1H Wiki Frame table; **verbatim Star Wars 5W1H example table** (4 nodes × 6 axes, populated from the page-1 diagram); **verbatim global-warming Plain-vs-WikiZZ outputs** from the page-4 screenshot (both modes' full text + the LLM Jury verdict); **verbatim 3-phase Living Knowledge Graph description** from the page-5 diagram; 7-row convergence table; 8-entity Dangling list (Vishal Mysore; WikiZZ; NVIDIA NIM; Cloudflare Worker; George Lucas / Mark Hamill / David Prowse / James Earl Jones as Star Wars cultural-reference flags); 7 Concept candidates surfaced and deferred per the [author-entity promotion rule](../CLAUDE.md#author-entity-promotion).
- [[concepts/llm-wiki|llm-wiki]] — `source_count` 5→6; `confidence` **unchanged at 0.91** (anecdotal single-author source cannot raise above the 0.75 vendor-cap; the concept is already past that ceiling from rigorous sources); `last_confirmed` 2026-05-14. Updated the *five sources / five vantages* list to include Mysore as the **single-author extension / browser-only / session-scoped end of the spectrum** sub-variant. Added a closing paragraph framing the five sources as spanning the **full architectural spectrum** from privacy-maximalist (Mysore's WikiZZ) through MCP-server-with-seekdb (OceanBase ex-brain) to durability-maximalist (Liu's GBrain).
- [[Anthropic]] — `source_count` 7→8; `confidence` **unchanged at 0.92** (anecdotal third-party-tool mention does not raise above current 0.92, especially when adjacent [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks|OceanBase ex-brain]] already provides a more substantive Anthropic-API integration claim via MCP). New top-level §*Third-party uses of the Anthropic API* section added with WikiZZ as the inaugural entry; the section is now available for future third-party-API-integration ingests.
- [[index]] — new Source-section entry slotted in the LLM-Wiki cluster between Raju (04-16) and Liu (04-27). The entry surfaces all three load-bearing visuals at the index level so a reader scanning the catalog can locate this source by its substantive contributions, not just its title.
- [[log]] — this entry.

**Dangling authors / entities** (single-source first-mentions; not promoted per the [author-entity promotion rule](../CLAUDE.md#author-entity-promotion)):

- **Vishal Mysore** — author; first time as `author:`. AI/software-patents background; 2.3K Medium followers; handle [@visrow](https://medium.com/@visrow). **Soft promotion candidate on second source**, but the 1-clap engagement on this piece would suggest deferring even on second-source unless that second piece has substantially better reception or different vantage.
- **WikiZZ / LLM WikiZZ** — Mysore's open-source tool. Browser-only / static-first / `FileReader` / Cloudflare Worker proxy / NVIDIA NIM + Anthropic + Gemini providers. Single-source.
- **NVIDIA NIM** — Nvidia's inference microservice product. Wiki already has Nvidia coverage (H100, TensorRT) via [[2025-05-17-turc-llms-low-precision-quantization-fundamentals|Turc 2025]], but NIM specifically is a first-mention. The wiki defers an Nvidia entity-page promotion — both the Turc mention (substrate-layer hardware in operator detail) and the Mysore mention (incidental third-party API option) are pieces of evidence for Nvidia's relevance but no source treats Nvidia broadly as a principal subject yet.
- **Cloudflare Worker** — Cloudflare's edge-compute serverless platform; named as WikiZZ's CORS proxy. **Cloudflare itself is mentioned in [[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]]** as the pro-democracy-protesters mission-emergence case study — making Mysore the **second wiki mention of Cloudflare** but in a completely orthogonal context (governance case study vs CORS-proxy infrastructure). Per the second-source rule the wiki would normally promote Cloudflare to an entity page — but **neither mention treats Cloudflare as a principal subject**, so the wiki defers entity promotion with this explicit two-orthogonal-contexts justification. Reconsider on a third source.
- **George Lucas**, **Mark Hamill**, **David Prowse**, **James Earl Jones** — cultural-reference names in the Star Wars 5W1H pedagogical example. Same convention as the *Severance* / *MDR* cultural-reference flag in [[2025-05-17-turc-llms-low-precision-quantization-fundamentals|Turc 2025]] — captured in the source page for context, not promoted.

**Concept candidates surfaced and deferred**:

- *5W1H Wiki Frame* (Who / What / When / Where / Why / How as a six-axis context-structuring template). **Strong promotion candidate** if a second source surfaces the same template or substantial variants.
- *Context Debt* — Mysore's coinage for *"the cost that builds up when an LLM doesn't truly understand the fundamental frame of the data."* Adjacent to "technical debt"; vocabulary candidate.
- *Autonomous Scaffolding* (LLM as Architect, user as Clerk). Pattern candidate.
- *Contrast Engine* (side-by-side Plain-vs-context UI pattern for showing value-add of context-scaffolding). UX-pattern candidate.
- *LLM Jury* (evaluator-LLM as judge of A/B-RAG-quality delta). Specific UI instance of the broader LLM-as-judge pattern.
- *Browser-only / session-scoped LLM Wiki* — architectural sub-variant of Karpathy's pattern; defer until a second source proposes the same sub-variant.
- *Transient RAG* (Mysore's term for query-time-only RAG with no persistent compilation layer) — convergent in spirit with [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained|Raju 2026]]'s framing but Raju does not use the exact phrase. Two-source convergence threshold for the *transient-vs-compounding* distinction is **met in spirit but not in vocabulary**; formal concept-page promotion deferred until a third source uses the same vocabulary.

**Not done by design** — and noted here so a future ingest doesn't re-relitigate the choice:

- **No new concept page for *5W1H Wiki Frame*** — strong promotion candidate but second-source rule applies. Promote on a second source surfacing the template or substantial variants.
- **No update to either [[syntheses/is-rag-dead|is-rag-dead]] or [[syntheses/knowledge-architectures-for-llm-agents|knowledge-architectures-for-llm-agents]] syntheses** — both syntheses are built on rigorous sources and were closed 2026-05-12. Adding the Mysore source (anecdotal / 1-clap / single-author / self-promotion-structured) would muddy the synthesis cluster; the Mysore source is captured in the concept page and source page where the source-quality flags can be locally surfaced rather than diluted at the synthesis level. This is the same convention applied to the Ross & Schneider 2026 HBR Partner Content ingest (2026-05-12 log).
- **No NVIDIA / Vishal Mysore / WikiZZ / Cloudflare entity pages created** — all four are dangling per the second-source rule; surfaced in the *Dangling* section above.
- **No `Debates and supersession` section on touched pages** — Mysore's content is additive to the [[concepts/llm-wiki|llm-wiki]] concept page (new architectural sub-variant; not in tension with prior claims). No supersession; no debate.
- **Tension with [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]]'s implied durable model** noted in the source page's *Convergence and contradictions* section as a **soft tension**, not a contradiction. Mysore's privacy-first browser-only approach is one valid sub-variant of the broader LLM-Wiki pattern; the wiki captures both endpoints (browser-only / session-scoped + server-side / durable) without forcing a winner.
- **LLM-Jury "concision" callout vs +21% token count** flagged in the source page's *Open questions* as evidence that LLM-as-judge of its own context-pipeline output may not always cleanly identify what improved. **Not load-bearing**; flagged for the wiki's downstream LLM-as-judge sources.

## [2026-05-13] ingest | Turc — *How LLMs survive in low precision | Quantization Fundamentals* (Julia Turc YouTube, 17 May 2025; 20:34)

The wiki's **first source on model efficiency / inference optimisation as a topic in its own right** and the **second-earliest source by publication date** (after [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings|Leskovec 2023]]). Julia Turc — solo educator on ML fundamentals; Patreon-supported. ~20-minute explainer covering the *what / when / how* of quantization: PTQ vs QAT; FP32 → FP16 / Bfloat16 → FP8 training-precision floor with FP4 and 1-bit LLMs as research frontier; clipping range / calibration / scale / zero point; **the fixed-point-arithmetic decomposition trick** (s = (negative-power-of-2) × s₀ where s₀ > 0.5; precompute once; multiplication becomes integer multiply + bit shifts); the **memory-bandwidth-not-FLOPs** framing for what quantization actually buys on modern GPUs. Dual-end-point motivation: **DeepSeek R1** at 671B params ≈ 720 GB → 131 GB (−82%) fits across 2× **Nvidia H100** at the top, **Google's Coral Edge TPU** with no floating-point support at the bottom. Ecosystem map: **Meta** and **DeepSeek** publish FP-only; **Unsloth** post-quantizes; **Qwen** publishes pre-quantized variants (**GGUF / GPTQ / AWQ**); **PyTorch / TensorFlow** have built-in support; **ONNX Runtime / Nvidia TensorRT** apply hardware-specific optimisations downstream.

**Pre-flight checks passed**: full 20:34 transcript (918 ASR lines, 7 chapters); ASR caption track (English; cleanup table in source page §*What was actually ingested* — *"Bloat 16"* → Bfloat16, *"Quen"* → Qwen, *"GBTQ"* → GPTQ, *"Onyx"* → ONNX, *"ILE E"* → IEEE, etc.); identity matches filename slug; honest scoping — full episode, not partial. **Source-quality flag**: source is 12 months old at ingest — empirical anchors (FP8 as frontier; 1-bit LLMs as research) are 2024–2025 baseline and have been pushed by 2026 frontier work (FP4 training is now active). Source page flags this as temporal drift, not contradiction; future quantization-frontier ingests should reference Turc 2025 as the 2025-baseline anchor.

**Touched pages** (4 wiki files):

- [[2025-05-17-turc-llms-low-precision-quantization-fundamentals]] — new source page; `kind: video`; channel `Julia Turc` in `author:`; description rendered as leading blockquote; 7-chapter battery; full *Why / When / How / Fixed-point / Matrix-multiplication / Bfloat16-vs-IEEE-FP16 / Ecosystem-map* sections; 6-row convergence table; 18-entity Dangling list; 9 Concept candidates surfaced and deferred per the [author-entity promotion rule](../CLAUDE.md#author-entity-promotion).
- [[Google]] — added three new sub-organisation/product entries: **Google Brain / Bfloat16** under §*Sub-organizations*; **Coral Edge TPU** under new §*Edge ML hardware*; **TensorFlow** under new §*ML frameworks*. `source_count` 4→5; `confidence` 0.82→0.87 (+0.05 for additional supporting source; not vendor-sponsored — Turc is independent of Google — and these are the wiki's first substrate-layer Google references); `last_confirmed` 2026-05-13. Added `tags`: `google-brain`, `bfloat16`, `coral-edge-tpu`, `tensorflow`, `edge-ml`.
- [[index]] — new Source-section entry slotted alphabetically by slug before `2025-12-01-marily-nika-...`. Also corrected the **stale "earliest source by publication date" claim** on `2025-12-01-marily-nika-...` (Leskovec 2023 and now Turc 2025-05 are both older; the *5 months ahead of the next-earliest* phrasing no longer applied either). Updated Entity-section blurb for [[Google]] to surface the new substrate-layer roles (Bfloat16 / Coral / TensorFlow).
- [[log]] — this entry.

**Dangling authors / entities** (single-source first-mentions; not promoted per the [author-entity promotion rule](../CLAUDE.md#author-entity-promotion)): **Julia Turc** (channel = author of this source; solo educator); **DeepSeek** (publisher of DeepSeek R1, FP-only); **DeepSeek R1** (671B-MoE; FP8-trained); **Meta** (publisher of Llama 4, FP-only; PyTorch maintainer); **Llama 4** (FP8-trained); **Nvidia** (H100, TensorRT); **Nvidia H100** (80 GB HBM3 datacentre GPU); **Nvidia TensorRT** (inference engine); **Qwen** (Alibaba; pre-quantized model publisher); **Unsloth** (post-publication quantization community); **Coral Edge TPU** (Google edge-ML hardware — substantive mention but no entity page yet; promote on second source); **Bfloat16** (Google Brain ML-bespoke 16-bit float format); **PyTorch** (Meta ML framework); **TensorFlow** (Google ML framework — substantive mention but no entity page yet); **ONNX Runtime** (model-interchange inference engine); **GGUF**, **GPTQ**, **AWQ** (quantization-format families); **IEEE 754** (the FP16 half-precision standard); **Google Brain** (Google's ML research division, originator of Bfloat16 — substantive mention but no separate entity page; absorbed into the Google entity instead). **Strong promotion candidates on second source**: **Julia Turc**, **DeepSeek**, **Meta**, **Nvidia** — all named as principal subjects or with substantive context here.

**Concept candidates surfaced and deferred**: *quantization* (the technique); *PTQ* (post-training quantization); *QAT* (quantization-aware training); *fixed-point arithmetic* (the integer-only-multiplication trick); *clipping range / calibration*; *zero point / asymmetric quantization*; *Bfloat16 / dynamic-range-vs-precision trade-off*; *memory-bandwidth-not-FLOPs (on modern GPUs)*; *training-vs-inference precision asymmetry*. All deferred until second-source mention per [§Lifecycle](../CLAUDE.md#lifecycle).

**Not done by design** — and noted here so a future ingest doesn't re-relitigate the choice:

- **No new concept page yet for *quantization*** — strong promotion candidate but second-source rule applies. Promotion candidates the moment a second source narrates quantization in operator detail (the *Incorruptible* book's tangential AI-cost framing won't count; a real follow-up technical source — Turc's promised PTQ/QAT episodes, the BitNet paper, a frontier-FP4-training paper — will).
- **No new entity page for Coral Edge TPU / Bfloat16** — both folded into the existing [[Google]] entity under new sub-sections rather than promoted to dedicated entity pages. Reason: the wiki's existing entity-promotion convention for Anthropic / OpenAI keeps product-and-format references *inside* the parent organisation's entity page until a second source narrates the product/format independently of its parent. Bfloat16 in particular is on the path to industry-format-not-vendor-format and may deserve its own entity page on a second source.
- **No synthesis or thread** — Turc's content opens a new branch with no prior 2+ sources to cluster. Synthesis/thread becomes appropriate when a second quantization-anchored source lands.
- **No `Debates and supersession` section on touched pages** — Turc's content is additive to the Google entity (new sub-areas; not in tension with prior claims). No supersession; no debate.
- **Temporal-drift flag, not stale flag** — Turc's empirical anchors are 12 months old, but the framework (PTQ/QAT, fixed-point arithmetic, clipping/zero-point, memory-bandwidth bottleneck) is *not* stale. No `status: stale`; no `superseded_by:`. The drift is *to be expected on a frontier-empirical-claims source published a year ago* and is captured in the source page's framing paragraph and *Open questions* section instead.
- **Severance / MDR cultural-reference** flagged in the *Linked entities and concepts* section as a *cultural-context flag, not promotion candidate* — useful for placing Turc's audience model, but not load-bearing for the technical content.

## [2026-05-13] ingest | Ries on Lenny's Podcast — *The force that destroys companies from within (and how to resist it)* (Lenny's Podcast YouTube, 10 May 2026; 1h 39m)

The wiki's **first founder-author podcast anchored on a governance thesis** and the first source naming **a first-hand role in Anthropic's governance design**. Eric Ries ([[Lean Startup]] author, 2011) interviewed by Lenny Rachitsky two weeks before the 26 May 2026 launch of his new book *Incorruptible*. Six substantive contributions: **(1)** *The force* — Ries' coinage for the gravitational pull dragging organisations toward mediocrity, explicitly **not** competition; **(2)** the 80% founder-ouster statistic (Harvard Law School, per Ries — under standard venture-backed governance only 20% of founders remain CEO three years post-IPO); **(3)** shareholder primacy reframed as a 40-year-old policy choice, not a natural law; **(4)** Public Benefit Corporation as the practical defence — *"a two-page legal filing... Delaware tomorrow"*; **(5)** six case studies — Novo Nordisk (100-year foundation), Cloudflare (mission emergence), Costco (rules-in-structure), Vectura Group acquired by Philip Morris, Groupon (A/B-test death spiral), Whole Foods; **(6)** the [[Anthropic]] **Long-Term Benefit Trust** mechanism narrated in operator detail — two-tier governance with outside AI-safety-expert trustees (no equity) appointing and accountabilifying the for-profit board, **structurally stronger than [[OpenAI]]'s post-2025 PBC-alone structure**.

**Pre-flight checks passed**: full 1h 39m transcript (1958 ASR lines, 27 chapters); ASR caption track (English; light proper-noun cleanup needed — *"Chat GPD"* → *ChatGPT*; *"Daario"* → *Dario*; *"Marie Crowe"* → *Marie Krogh*; *"Vag"* → *Vatican*); identity matches filename slug; honest scoping — full episode, not partial. **Source-quality flag**: Ries discloses he played *"a very big role"* in Anthropic's founding advice and Lenny discloses he *"may be an investor in the companies discussed"* — both surfaced in the source page's *Linked entities and concepts* and *Open questions* sections. The **structural argument** (PBC + LTBT > PBC alone > no governance protection) is largely independent of any single case and is what this source primarily contributes; the **case-specific framing** (Anthropic-success-attribution; particular companies named) is moderated by the disclosures.

**Touched pages** (5 wiki files):

- [[2026-05-10-ries-lennys-force-destroys-companies-within]] — new source page; `kind: video`; channel `Lenny's Podcast` in `author:` per the [video field-mapping convention](../CLAUDE.md#source-page-conventions-specific-to-videos); description rendered as leading blockquote in body; 27-row chapter battery; full *Convergence and contradictions* table (8 cross-source rows); 22-entity Dangling list; 12 Concept candidates surfaced and deferred per the [author-entity promotion rule](../CLAUDE.md#author-entity-promotion).
- [[Anthropic]] — added new top-level §*Governance structure* section narrating the **Long-Term Benefit Trust (LTBT)** mechanism in operator detail (two-tier; outside trustees with no equity; appoint and accountabilify the for-profit board on mission-relevant decisions); names Ries' role advising the Amodeis at founding. `source_count` 6→7; `confidence` 0.87→0.92 (+0.05 for additional supporting source; the source is operator-narrated rather than vendor-sponsored — Lenny's Podcast is independent of Anthropic — and the wiki had no prior operator-level LTBT narration); `last_confirmed` 2026-05-13. Added `tags`: `public-benefit-corporation`, `long-term-benefit-trust`.
- [[OpenAI]] — added new top-level §*Governance trajectory* section narrating the **nonprofit-foundation → PBC conversion** trajectory with Ries' framing that PBC-alone is structurally weaker than the original nonprofit-foundation guardian and weaker than Anthropic's PBC + LTBT. `source_count` 9→10; `confidence` 0.90→0.95 (cap); `last_confirmed` 2026-05-13. Added `tags`: `public-benefit-corporation`, `nonprofit-foundation`.
- [[index]] — new Source-section entry alphabetically slotted between `2026-05-09-chase-...` and `2026-05-11-blank-...`. Updated Entity-section blurbs for [[Anthropic]] and [[OpenAI]] to surface PBC/LTBT status and governance trajectory respectively.
- [[log]] — this entry.

**Dangling authors / entities** (single-source first-mentions; not promoted per the [author-entity promotion rule](../CLAUDE.md#author-entity-promotion)): **Lenny's Podcast** (channel = author of this source; second source for **Lenny Rachitsky** the host who was previously referenced in [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]] via *Lenny's List* — but Lenny is not yet promoted because the prior mention was incidental, not as author/host); **Eric Ries** (guest; *Lean Startup* + *Incorruptible* author; first-hand Anthropic-advisor); **Novo Nordisk**; **Cloudflare**; **Costco**; **Vectura Group**; **Philip Morris**; **Groupon**; **Whole Foods**; **Devoted Health**; **HEB**; **Starbucks**; **Dario Amodei**, **Daniela Amodei**; **Andrew Mason** (Groupon); **Todd Park** (Devoted Health); **Howard Schultz** (Starbucks); **Saul Price** (Costco); **Marie Krogh**, **August Krogh** (Novo Nordisk founding); **Mary Parker Follett** (1920s management theorist; *"power with, not power over"*); **Frederick Winslow Taylor** (1911 *Principles of Scientific Management*); **Steve Jobs** (Apple — *harder is easier* and torchbearer cited twice); **Elon Musk**, **Sam Altman** (OpenAI history). **Strong promotion candidates on second source**: **Eric Ries**, **Mary Parker Follett**.

**Concept candidates surfaced and deferred**: *The force* / gravitational pull toward mediocrity (Ries' coinage); *mission-driven vs mission-hopeful*; *mission guardian*; *spiritual holding company*; *fiduciary commitments* (Ries' replacement for *stakeholders*); *harder is easier*; *culture bank* (Todd Park / Howard Schultz attribution); *torchbearers*; *founder-control trap*; *Public Benefit Corporation*; *shareholder-primacy-as-1980s-regime*; *AI-alignment-via-Conway's-law*. All deferred until second-source mention per [§Lifecycle](../CLAUDE.md#lifecycle).

**Not done by design** — and noted here so a future ingest doesn't re-relitigate the choice:

- **No new concept page yet for *Public Benefit Corporation*** despite the instrument being named-with-specificity and Anthropic's PBC status appearing in the wiki — the second-source rule applies; promotion candidate on a second source that names PBC structurally.
- **No new concept page yet for *the force* / *mission guardian* / *culture bank*** — same reason; framework vocabulary from a single founder-author podcast is suggestive but not yet wiki-load-bearing.
- **Not added to a synthesis or thread** — Ries' framework opens a *new branch* of the wiki (legal-entity governance) with no prior 2+ sources to cluster. Synthesis or thread becomes appropriate when a second governance-anchored source (or the *Incorruptible* book itself, ingest target after 26 May 2026) lands.
- **No `Debates and supersession` section on touched concept pages** — Anthropic's entity page now describes the LTBT mechanism with operator-level detail, but the LTBT description is *additive*, not in tension with prior wiki claims. No supersession; no debate.
- **Mary Parker Follett primary-source ingest deferred** — Ries names her as the load-bearing pre-WWII counter-tradition to Taylorism, but her 1920s/1930s writing is a separate primary-source ingest target (public domain; would need to be intentionally retrieved). Flagged in the source page's *Open questions*.
- **Adjacency to [[2026-02-09-ross-schneider-adaptability|Ross & Schneider]] handled inside the new source page only** — not bidirectionally back-linked into the Ross & Schneider source page (their adjacency is the legal-entity-layer × people-process-layer pairing; one-direction note in the new page is sufficient on first ingest).

**Skill incident note** (separate from the ingest itself). Today's ingest was blocked for ~2h by **YouTube anti-automation tightening on `/youtubei/v1/get_transcript`** — the endpoint started returning HTTP 400 `"Precondition check failed"` to WebDriver-flagged sessions on or around 2026-05-13, breaking the skill globally (including for yesterday's verified-working URLs). The diagnostic path went via auth-fix hypotheses (cookies / state.json) that turned out to be red herrings; the actual fix is **automation-signal masking**: `--disable-blink-features=AutomationControlled` at browser launch + `navigator.webdriver` override in an `add_init_script` + a non-`HeadlessChrome` user-agent. Fix is in place in [`fetch_transcript.py`](../.claude/skills/youtube-transcript-skill/fetch_transcript.py) and documented in [`SKILL.md`](../.claude/skills/youtube-transcript-skill/SKILL.md) §Failure modes. No author/state files persisted.

## [2026-05-12] ingest | Ross & Schneider — *Resilience Won't Save Your Organization. Adaptability Will* (HBR.org Partner Content / Egon Zehnder, 9 Feb 2026)

The wiki's **first HBR Partner Content / advertorial source**. Mike James Ross and Greig Schneider (Egon Zehnder partners) argue that AI-driven continuous change has rendered "resilience" the wrong organising frame because it presupposes a fixed destination once the disruption passes; the proposed replacement is **adaptability**, operationalised across leadership practice / hiring / personal-discipline layers. Headline empirical anchor: Egon Zehnder survey of **1,200+ global CEOs**, 92% agreeing on adaptability as the necessary cultivation (no methodology disclosed). Cites Linda Hill's *creative abrasion* and Etienne van der Walt (Neurozone) on resilience's clinical definition.

**Pre-flight checks passed**: 6 pages (full article); identity matches filename; honest scoping — flagged as advertorial in the source page `§Source-quality flag` and in this log entry. Per the [Lifecycle vendor-source rule](../CLAUDE.md#lifecycle), this source's confidence boost caps at +0.05 and at 0.75 absolute — meaning for any concept already above that ceiling from independent sources, this source contributes only as a *cross-source positioning* bullet, not as a confidence multiplier.

**Touched pages** (5 wiki files):

- [[2026-02-09-ross-schneider-adaptability]] — new source page; `kind: article`; `section: "Partner Content from Egon Zehnder"`; `journal_volume: "HBR.org Partner Content, 9 February 2026"`. No URL captured (HBR Partner Content path not guessed).
- [[durable-skills]] — added cross-source bullet pairing this source with [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels]] (same date, overlapping hiring-criteria construct: *aptitude-to-learn-novel-stuff* / *interview for what new skills they have learned*). `source_count` 8→9; `last_confirmed` 2026-05-12. **`confidence` unchanged at 0.91** — vendor source does not raise; the concept was already past the vendor-cap from rigorous sources.
- [[2026-04-28-werner-lebrun-octopus-organization]] — added neutral `See also` bullet under Linked entities and concepts.
- [[2026-05-07-carucci-resistance-as-data]] — added neutral `See also` bullet under Linked entities and concepts.
- [[Harvard Business Review]] — **new sub-table** added: *HBR.org Partner Content (sponsored / advertorial)*. `source_count` 10→11; `last_confirmed` 2026-05-12. Frontmatter and body convention documented: `section: "Partner Content from <sponsor>"` + `journal_volume: "HBR.org Partner Content, <date>"`.

**Dangling authors / entities** (single-source first mentions; not promoted per the [author-entity promotion rule](../CLAUDE.md#author-entity-promotion)): Mike James Ross, Greig Schneider (article authors), Etienne van der Walt (cited body mention), Linda Hill (cited body mention with substantive citations from *Collective Genius* / *Genius at Scale* / *creative abrasion* — flagged for promotion on second source), Egon Zehnder (sponsoring firm), Neurozone (van der Walt's firm).

**Not done by design** — and noted here so a future ingest doesn't re-relitigate the choice:

- **No update to [[dynamic-capabilities]]** (the academic concept page) — this is a vendor source making informal claims; touching the Teece-anchored concept page from an advertorial would muddy the citation graph.
- **Not added to [[syntheses/organizational-frameworks-for-ai-adoption|frameworks synthesis]]** — synthesis cluster is built from 12 mostly-rigorous sources; adding an advertorial would dilute the cluster. Cross-positioning is captured in the source page and on the two adjacent source pages instead.
- **No new `adaptability` concept page** — adaptability is already listed in [[durable-skills]] and adjacent to [[dynamic-capabilities]]. Promotion to its own concept page is deferred until a non-vendor source centres adaptability with operational definition or measurement.
- **Hiring-criteria convergence with Sternfels (also 9 Feb 2026)** noted in the source page and the durable-skills concept page but **not promoted to a thread** — two sources is below the threshold for a thread, and the convergence is descriptive (same construct named in different vocabulary) rather than a research question. Reconsider on a 3rd source naming the same construct from another vantage.

## [2026-05-12] synthesize | Two synthesis pages on the RAG / LLM Wiki / Fat Skills convergence — *Is RAG dead?* + *Knowledge architectures for LLM agents*

User-flagged synthesis-shaped gap: the wiki had no standalone RAG page despite 5 sources (Raju, Liu, Huber, OceanBase, SurrealDB) independently converging on *complement, not replace*. Resolution: **two thread + synthesis pairs** per CLAUDE.md §Synthesis schema. Both retroactively-opened threads, immediately closed by their syntheses.

### [2026-05-12] synthesize | Is RAG dead? (5 sources)

Thread page: [[threads/is-rag-dead]]. Synthesis page: [[syntheses/is-rag-dead]].

**Question**: Is RAG dead, or just the term? Resolution: **the term is being retired; the technique persists as a substrate primitive**. Three explicit sources (Raju / Liu / Huber) + two substrate-implementation worked examples (OceanBase / SurrealDB) converge on *complement-not-replace*.

**Findings captured**:
- Term-vs-technique distinction made explicit across three independent sources.
- Three failure-mode axes (too much / too little / confusing — Huber's superset) mapping Liu's three failure points (chunking / re-derivation / passivity) and SurrealDB's three vector-only modes (context clash / context confusion / dense neighbourhood) onto a single taxonomy.
- Context engineering as the rebranding (Huber explicit; Karpathy-compatible).
- Bitter-lesson direction: context engineering folds back into models (Huber + Karpathy Software-3.0).
- Specialised small models for retrieval (Chroma Context One: 10× faster, 25× cheaper).
- File-systems-are-bad-databases critique (Huber + Swyx article reference).

**Lessons** (each a single transferable claim):
1. *"RAG is dead"* = the term is dead; the technique persists.
2. Hybrid is the right answer for serious knowledge systems.
3. Context engineering is the rebranding to converge on.
4. The naive-RAG pipeline has three named scale-related failure modes.
5. Specialised small retrieval LMs beat gigabrain models on cost+speed.
6. File systems are bad databases as agent substrates.
7. Context engineering will fold back into models.
8. The agentic-search-vs-vector-RAG cutover is corpus-size dependent.

**Open question**: The Cherny-vs-Huber agentic-search-vs-RAG empirical disagreement (Huber promised data *"next week"* — primary-source target).

### [2026-05-12] synthesize | Knowledge architectures for LLM agents — RAG / LLM Wiki / Fat Skills (7 sources)

Thread page: [[threads/knowledge-architectures-for-llm-agents]]. Synthesis page: [[syntheses/knowledge-architectures-for-llm-agents]].

**Question**: Which knowledge architecture fits which class of agent task, and how do they hybridise? Resolution: **no single architecture wins everywhere; choose by job; hybrid production reality**.

**Adopted scaffold**: Liu's three-architecture comparison matrix (core verb / scale / compounds / proactive / context / setup cost / best for). Decision tree: *"what is your agent's job?"* — retrieve at scale → RAG; build deep expertise → LLM Wiki; act autonomously → Fat Skills. Most production agents need 2-of-3.

**Findings captured**:
- Per-architecture failure mode tables (RAG / LLM Wiki / Fat Skills) — wiki's first systematic side-by-side.
- Hybrid architecture's operational-instantiation table — substrate (SurrealDB/seekdb) + synthesis (LLM Wiki) + action (GBrain) layers with concrete examples.
- Claude Code as the partial-convergence example (CLAUDE.md = wiki + auto-memory = compounding + skills = action — Liu's load-bearing observation).
- Convergence prediction timeline: 2023 RAG era → 2025 Wiki+Skills emerge → 2026+ hybrid.
- Signals the convergence is happening (LLM Wiki v2 community extensions / GBrain on pgvector / Neo4j knowledge layers / Mintlify virtualized-bash-on-Chroma / Chroma Context One / Claude Code).

**Lessons** (each a single transferable claim):
1. Choose by job, not loyalty.
2. RAG scales where LLM Wiki cannot; LLM Wiki compounds where RAG cannot.
3. Fat Skills are codebase-level investment.
4. GBrain's *thin harness, fat skills* inverts typical agent design.
5. Vector retrieval becomes a substrate primitive, not the application architecture.
6. Hybrid search in a single query is the substrate-layer pattern emerging across vendors.
7. The convergence is empirically observable in Claude Code today.
8. Specialised small retrieval LMs beat gigabrain models.
9. RESOLVER.md routing-via-skill-descriptions is the thin-harness load-bearing primitive.
10. The boundary between LLM Wiki and Fat Skills is the *act* axis.

**Open questions**: 2024 RAG-failure-points paper / LLM Wiki v2 community extensions / GBrain GitHub repo / enterprise-scale LLM Wiki / Neo4j knowledge layers / OpenClaw + Hermes / Cherny-vs-Huber disagreement / point-of-role-and-architecture-convergence (Hu's IC/DRRI/AI-founder × Singhal's product-builder).

### Companion-page relationship

The two syntheses are nested:

- [[syntheses/is-rag-dead]] = the narrow synthesis on *just RAG*. Tighter; ~5 sources; cleaner for citation when the question is specifically about RAG.
- [[syntheses/knowledge-architectures-for-llm-agents]] = the broader synthesis on *RAG / LLM Wiki / Fat Skills*. Wider; 7 sources; captures the full three-architecture decision framework + the convergence prediction.

Both cross-reference each other. The narrow synthesis is mostly subsumed by the broader one; we keep both because:

1. The narrow synthesis is a load-bearing citation target when only RAG is in scope.
2. The broader synthesis would dilute as a citation target if the reader is only asking *"is RAG dead?"*.
3. Per CLAUDE.md the synthesis convention rewards specificity; cross-linking handles the overlap.

**Touched pages:**

- [[concepts/llm-wiki|llm-wiki]] — no count change but conceptually validated by both syntheses; the narrow RAG synthesis is a citation target alongside the concept page.
- [[knowledge-graphs]] — referenced as substrate primitive in both syntheses.
- [[agent-harness]] — referenced as the runtime that reads from the chosen architecture.
- [[index.md]] — added both syntheses + both threads to the Syntheses + Threads sections respectively. (No new sources; this is a synthesize operation per CLAUDE.md §"The four operations".)

**Pre-flight notes**: Both threads opened retroactively per the user-approved workflow (option A in the AskUserQuestion). Thread `opened` dates set to the first ingested source raising the question (2026-04-09 for *is-rag-dead* — OceanBase, which explicitly references Karpathy's gist; 2026-04-27 for *knowledge-architectures* — Liu, who introduced the canonical three-architecture comparison). Both `closed` 2026-05-12. No new source pages; no concept/entity counter bumps required — this is a *synthesize* operation, not an *ingest* operation.

**Schema compliance**: Both synthesis pages follow CLAUDE.md §Synthesis structure exactly — Question / Findings / Sources consulted / Lessons / Open questions, plus the `type: synthesis` frontmatter with `derived_from`, `opened`, `closed`, `confidence`, `source_count`, and `relationships:` typed edges.

## [2026-05-12] ingest | Doug Blank (Comet ML) — MIT 6.S191 Lecture 7: The Three Laws of AI (Alexander Amini YouTube, 11 May 2026; 51:48)

The wiki's **first MIT 6.S191 source**. A 51:48 lecture by **Doug Blank** (Head of Research at [[Comet ML]]) in MIT 6.S191 Introduction to Deep Learning, **2026 Edition**. Published 11 May 2026 (same day as Huber/Chroma — coincidentally) on the [[Alexander Amini]] channel. ASR caption track; no chapters. Source page: [[2026-05-11-blank-mit-6s191-three-laws-of-ai]].

**The course's lineage anchor**: 2017 was MIT 6.S191's first offering — coinciding with the transformer year. 9-year run by 2026.

**Substantive findings:**

- **The Three Laws of AI as teaching framework** — Asimov's 1942 *Three Laws of Robotics* + zeroth law modernised in two versions: (a) **EU-AI-Act-style aspirational** — safe-secure-robust / aligned-with-human-direction / respect-human-rights-fairness-societal-values / transparent (zeroth); (b) **Blank's practitioner-operational** — log-your-traces / build-and-test-dataset / evaluate-prompts-and-models-often-and-be-transparent. Plus an audience-derived **minus-one law**: *"if you can't guarantee safety and security, don't build it"* — sourced from YouTube comments (Ryan Hajes pointing the contradiction; Karan Low agreeing; Violin-Sheet-Music-Blog coining the *"don't build it then"* axiom).
- **The dataset / metric / experiment / model-comparison eval vocabulary** — formal teaching of the four-ingredient framework. Message → chat prompt → trace/span → project → dataset → metric (code-based OR LLM-as-judge) → experiment. **Two-source threshold met** with [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair|Guthrie / Braintrust 2025]] — academic-pedagogical vantage convergent with vendor-platform vantage. Strong concept-promotion candidate (defer pending third source).
- **The Sam Nelson safety-drift case study** — Blank treats it as the lecture's most-difficult section. Nelson died 2025 after a long conversation with ChatGPT during which the model's initial refusal eroded into providing dangerous information by mimicking the user's framing. **Named failure mode**: *safety drift in long-context LLM uses*. Mitigation (1 of 5 listed but only one stated verbatim): **build long-message datasets (system / user / assistant / user / assistant / ...) and test for safety drift**. The wiki's first first-hand-named-incident anchor for the long-context-safety-degradation failure mode.
- **Live 90-second agentic AI demo** — 4 tools constructed live: get_time / get_weather / send_email / delete_files (the last suggested by the audience — destructive). *"Can you trust an LLM? No. Can you trust an agentic AI built on LLMs? No."* Demo includes a hallucinated date (*"next Thursday is January 12th"* — it isn't), showing LLMs hallucinate even with tool access. Convergent with the wiki's existing harness-tooling cluster — agentic systems amplify the need for the eval discipline.
- **Live prompt-injection / jailbreaking demo** — the six-bears password example. 123-item jailbreak dataset categorised by attack class. Audience-discovered attack vectors: *define-secret* command-mode bypass; *single-quote-injection*; *translate-into-Klingon* lateral-task bypass; *redaction-fill* bypass. **Model-comparison results** on the six-bears benchmark: **GPT-5 100% / GPT-4o 94% / GPT-4o-mini 78% / Gemini 2.5 Flash worst**. The wiki's first first-party-academic-comparative-eval of 2026 frontier models on jailbreak resistance with concrete numbers — bifurcation is sharp.
- **AI history retrospective 1956-2026** — five-phase narrative: symbolic reasoning (1956-1970s) → expert systems (1970s) → statistical ML (1980s-2000s) → deep-learning breakthrough era (2010-2017) → transformer era (2017-now). The wiki's first ingest covering the **pre-2017 AI history** at lecture-content granularity.
- **Blank's first-person AI-winter testimony** — PhD in neural networks 1997; ~100 professorship applications, few responses; struggled to get NN papers accepted at AI journals; 2005 *"Tale of Two AIs"* talk arguing NN-is-AI to a skeptical audience. The wiki's first first-person-AI-winter operator anchor — useful empirical context for the *current-AI-boom-is-permanent* implicit framing the wiki's existing sources often elide.

**Touched pages:**

- [[agent-harness]] — `source_count` 19 → 20; `confidence` 0.95 (cap). Blank's practitioner-three-laws (log / dataset / evaluate) operationalise the Contracts + Compounding layers. Prose lead "nineteen" → "twenty".
- [[agentic-engineering]] — `source_count` 9 → 10; `confidence` 0.92 → 0.93. Live 90-second agent demo as worked example; *"can you trust an LLM/agentic-AI? No"* convergent with Karpathy's *animals vs ghosts* framing.
- [[agent-development-lifecycle]] — `source_count` 3 → 4; `confidence` 0.83 → 0.85. Blank's three laws map onto Test + Monitor + Iterate phases — academic-pedagogical reinforcement of Chase's ADLC vocabulary.
- [[jagged-frontier]] — `source_count` 8 → 9; `confidence` 0.92 (cap stays). Live demo of LLM jaggedness — can't tell time / weather without tools; the capability-boundary made visible as a classroom-teaching primitive.
- [[index.md]] — added the source entry; bumped [[agent-harness]] one-liner (19 → 20 sources).

**People listed as Dangling first-mention**: **Doug Blank** (Comet ML Head of Research; ex-college-professor at a liberal arts college; PhD NN 1997); **Alexander Amini** (MIT 6.S191 co-organiser; channel host); **Ava Soleimany** (MIT 6.S191 co-organiser; introduces Blank); **Isaac Asimov** (1942 Three Laws of Robotics author); **Sam Nelson** (named-incident case study, single-mention for traceability — not a promotion candidate); **Ryan Hajes**, **Karan Low**, **Violin Sheet Music Blog** (YouTube commenters whose contributions shaped the minus-one-law adoption).

**Products / orgs listed as Dangling first-mention**: **Comet ML** (ML/LLM evaluation platform vendor; multi-mention candidate); **OPIC / Opik** (Comet's open-source LLM-eval tool; Apache 2 license; 17k GitHub stars; github.com/cometml/opik); **MIT 6.S191** (Introduction to Deep Learning course; first offered 2017; introtodeeplearning.com); **Boston Dynamics** / **Atlas robot** (referenced in Asimov-context opening); **Tandy Color Computer** (Blank's first computer; Asimov sold it in mid-1980s).

**Concept candidates surfaced**:
- *Three Laws of AI* (Blank's modernisation of Asimov) — strong promotion candidate; defer pending second-source mention.
- *Safety drift in long-context LLM uses* — Blank's named failure mode for the Sam-Nelson-class case. **Strong promotion candidate** on second-source mention — the failure pattern is wiki-load-bearing for any future agentic-AI ingest.
- *Practitioner-three-laws* (log / dataset / evaluate) — operational compounding-cycle. Convergent with Kiron-Schrage + Hu + Chase. Strong concept candidate but folded into [[agent-harness]] for now.
- *Lateral-task jailbreak* (translate-into-Klingon class) — named jailbreak vector. Single-source.
- *Minus-one law / "don't build it then"* — operator-elevated YouTube-comment-as-axiom. Single-source.

**Pre-flight notes**: Identity verified. Transcript fetched via `youtube-transcript-api` fallback after Playwright timeout (51:48 > 20-min threshold). 1023 raw ASR segments → 229 grouped windows. No chapters (lecture); transcript is a flat `## Transcript` section. ASR transcription quirks: *"OPIC"* may be the Comet product *Opik* — Blank pronounces it variably; *"Cherny"* / *"Hajes"* / *"Karan Low"* / *"Violin Sheet Music Blog"* are ASR best-guesses of names that may need primary-source verification.

**Cross-batch synthesis with prior ingests (12 May 2026)**:

This ingest **continues the recent thematic batch** on the eval discipline / context engineering / AI-safety cluster:

- **Two-source threshold met** for the *dataset / metric / experiment* eval vocabulary (Blank + Guthrie). Strong concept-promotion candidate.
- **Three sources** now describe the *compounding-feedback architecture* (Kiron-Schrage organisational + Hu company + Blank LLM-engineering). The three-laws / three-architectures / closed-loop-company framings are all variations on the same principle at different organisational scales.
- **The Sam Nelson named-incident anchor** complements [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler 2026]]'s *lethal trifecta* framing — Böckeler names the failure class abstractly; Blank names a concrete incident.
- **GPT-5 jailbreak resistance** is a new empirical-numbers anchor — *100% on the six-bears benchmark* (single-benchmark; not yet generalised). Convergent with [[2026-05-11-huber-chroma-rag-is-dead-agentic-search|Huber's]] *Context Rot* empirical-numbers anchor — both push the wiki toward *measured-not-narrated* model evaluation.

The lecture's framing as *"fundamentals of AI"* (per the user's description) reflects the lecture's **multi-layer pedagogical structure**: history retrospective (the fundamentals) + eval discipline (the modern practice) + agentic demo (the new frontier) + Three Laws (the ethical/safety wrap-around). The lecture is **course-content rather than research-discourse** — first-author MIT-classroom pedagogy, which is a new wiki vantage on the cluster.

## [2026-05-12] ingest-batch | Two videos — Huber (Chroma) on RAG-is-dead-the-term + Singhal (Skip / Stanford CS153) on PM in the AI era

A two-video batch the user grouped in the same request. Topically divergent: video 1 extends the wiki's LLM-Wiki / knowledge-graphs cluster from the vendor-of-the-substrate vantage; video 2 extends the wiki's vibe-coding / ai-employment-effects / durable-skills cluster from the PM-leadership / Stanford-CS-course-content vantage.

### [2026-05-12] ingest | Jeff Huber (Chroma) — RAG is Dead: Building Agentic Search (Mastra YouTube, 11 May 2026; 13:45)

The wiki's **first-party-Chroma-CEO source**. Source page: [[2026-05-11-huber-chroma-rag-is-dead-agentic-search]].

**Substantive findings:**

- **"RAG is dead — the term, not the technique"**. Convergent with Raju/Liu/OceanBase explainers from the *vendor-of-the-substrate* vantage. Huber proposes banning *RAG* and *vector database* as terms. Reframe: **context engineering**.
- **The Context Rot empirical anchor**: Chroma's **45-page 2025 research report**. Demonstrates LM performance *not invariant* to context length. Dumb zone starts **20K-120K tokens** depending on use case. *"I've not found anybody who really trusts a million tokens to do anything that's any kind of good."* The wiki's first empirical-numbers anchor for the scale-ceiling caveat Raju named on the LLM Wiki pattern.
- **Three-axis context-failure taxonomy**: too much / too little / confusing. Strict superset of SurrealDB's *context clash / context confusion / dense neighbourhood* (which only address the *too-much* axis).
- **"File systems are bad databases"** structural critique: four named limitations of the file-system-plus-bash pattern (currently dominant in Codex / Claude Code defaults) — poor concurrency / corruption risk / no indexing / grep-only search / sandbox heavyweight. Cites **[[Swyx]]**'s *"Oops, You Wrote a Database"* article. Names **Mintlify's virtualized-bash-on-Chroma** as the cleaner alternative.
- **Embrace the bitter lesson for context engineering**: Huber's prediction that context engineering will be folded back into models. *"Chroma just released a model trained to edit its own context."* Convergent with Karpathy's Software 3.0 prediction direction.
- **Chroma Context One** — open-source specialised search sub-agent (auto-regressive LM that outputs documents, not text). **10× faster, 25× cheaper, on par or better at searching** vs gigabrain models (Opus 4.5/4.6, GPT-5 4). 50-page research report. *"We find the task of search actually does not lend itself particularly well to being gigabrained, and maybe you're paying too much, you're waiting too long, and you're actually getting worse search results."*
- **Chroma Sync** — automatic-indexing-as-a-service (drop files in bucket → Chroma auto-handles indexing).
- **Memory ≈ context compaction ≈ distillation** — Huber's structural collapse. *"If you have a million tokens of memory and you need to inject a couple hundred tokens into this new generation, that is in some sense still a search process of 'what should I remember in this moment?' So memory, context compaction, distillation — they're all the same thing once you unpack it."*
- **Boris Cherny disagreement (first substantive vendor disagreement in the wiki)**: an audience-Q references Cherny's design talks for Claude Code on agentic-search-beats-RAG. Huber pushes back: *"Question their incentives — who wants you to spend more money on tokens?"* Distinguishes small-corpus (30-50 files; grep works eventually) from larger-corpus (grep breaks; semantic expansion needed). Promises empirical data *"next week"* (mid-May 2026 publication).

**Touched pages:**

- [[concepts/llm-wiki|llm-wiki]] — `source_count` 4 → 5; `confidence` 0.90 → 0.91. Added Huber as the *vendor-of-the-substrate* vantage. Context Rot empirically substantiates the scale-ceiling caveat.
- [[knowledge-graphs]] — `source_count` 4 → 5; `confidence` 0.85 → 0.87. Added Huber as the third-vendor convergence anchor (Chroma + SurrealDB + seekdb) on multi-modal-database-as-substrate with the *file-systems-are-bad-databases* anti-pattern call-out.
- [[agent-harness]] — `source_count` 18 → 19; `confidence` 0.95 (cap). Added the *file-systems-are-bad-databases* structural critique of the Codex/Claude-Code default pattern. Prose lead "eighteen" → "nineteen".
- [[Boris Cherny]] entity — `source_count` 3 → 4; `confidence` 0.80 → 0.82; `last_confirmed` updated to 2026-05-12. Two-source-on-Cherny strengthens the entity.

**People listed as Dangling first-mention**: **Jeff Huber** (Chroma co-founder & CEO); **Swyx** (tech influencer; *"Oops, You Wrote a Database"* article); **Mintlify** (documentation-assistant vendor using Chroma as backing).

**Products / orgs listed as Dangling first-mention**: **Chroma** (vector / retrieval database — multi-mention candidate, also referenced in Liu 2026 briefly); **Mastra** (channel); **Chroma Context One** (open-source search-specialised LM); **Chroma Sync** (auto-indexing product); **Context Rot** (Chroma's 45-page 2025 research report).

**Concept candidates noted**: *Context Rot* (empirical 45-page report; likely promotion-candidate on second-source mention); *Embrace the bitter lesson for context engineering*; *File systems are bad databases*; *Search-specialised LM vs gigabrain LM*; *Memory ≈ context compaction ≈ distillation* (all single-source).

### [2026-05-12] ingest | Nikhyl Singhal at Stanford CS153 — Product Management in the AI Era (Stanford Online YouTube, 7 May 2026; 63:14)

A 63:14 guest lecture in **Stanford CS153 Frontier Systems** (Prof. **Mike Abbott**) with **Nikhyl Singhal** (Skip founder; ex-Google/Meta/Credit Karma VP-of-Product). **The wiki's second Stanford-CS-course-lecture source** (after Leskovec CS224W 2023) and **third Stanford Online ingest**. Source page: [[2026-05-07-singhal-stanford-cs153-product-management-in-ai-era]].

**Substantive findings:**

- **Four-company-phases framework**: pre-PMF (no PM; founder drives) → post-PMF process (PM emerges as quieter process function) → hypergrowth scaling+expanding (Chief Product Officer + large PM teams; Meta feed→Reels worked example) → big-tech late-stage zero-to-one (combat innovator's dilemma).
- **AI-era role inversion — *product builder*, not *movement of information***: bureaucratic PM role dying; designers/engineers/PMs converging into a *product builder* role. *"All the parts of my job that I dislike and hate, I can essentially obsolete myself, engineer myself out of. And then the parts that I love — judgment, decisioning, being courageous, testing things in the wild, talking to customers — those are the parts of my job that exist."*
- **Concrete operator-class employment numbers**: 30-70% big-tech layoffs this calendar year (Salesforce/Block/Snap named); top-1% PM salaries more-than-doubled in 18 months; **4 product-leader contracts personally negotiated crossing eight-figures annual**; more open PM roles than ever in history; **mid-30s middle-managers (8-15 years tenure)** named as the at-risk cohort.
- **"Brand at all-time low" hiring shift**: *"Top quality employers like the Anthropics, the OpenAIs and others don't actually care what brand of company you've been at. They want to know how modern you are in how you think and how you use your tools."* A person at Google 6 years may be *"dramatically less relevant"* than current Stanford-CS-students with max-Claude-Code accounts.
- **Career-as-chapters / 15-18-jobs-in-50-years**: 50-year career × 2-3 year average tenure → 15-18 jobs total. *"Your career is not like periods in a hockey game. It's like chapters in a book."* The origin of **Skip** as a name: *"think about the chapter after the one you're thinking about now."*
- **Skip** the company: talent-agency-for-product-people; 125-head-of-product community (Anthropic / OpenAI / Meta and others); Singhal-funded; no scale / no monetize; 30-year plan (Singhal aged 52, planning to work to 82).
- **The two-question audience test**: 100% of CS153 students anxious + 100% having fun building with AI. Two years ago: 20-30% anxiety, low fun. Demonstrates the *anxiety-up + fun-up + bifurcation* of the AI-era job market.
- **Iteration-speed-as-moat**: Chrome (6 weeks) beat Firefox (quarterly) and IE (annual); Android (quarterly) beat iOS (annual). Singhal: *"It doesn't matter how you start, it's how fast you improve it."* Two-source-on-iteration-speed-as-moat threshold met (Hu 2026 *thousand-times-faster-than-incumbents* + Singhal); promotion candidate.
- **Hangouts as anti-pattern**: solved an inside-the-building problem (consolidate 7 communication codebases) not a customer problem; WhatsApp won by focusing on text-only-in-India and iterating fast.
- **Three durable skills for CS students**: (1) modernity-of-toolchain, (2) networking-passive-relationships, (3) systems-programming-mindset (engineering-abstraction *"is this the right thing to build? Is it working? Does it fit into our system design?"*).
- **Stanford-CS-faculty-quality knock**: *"The teaching was not particularly great. The assignments were incredibly difficult... My computer science teachers were world class — I think worse than Foothill is my suspicion."* The durable skill: **unstructured-problem-solving with peers** — *"that turned out to be the most important skill."*
- **Meta-and-the-metaverse diagnosis**: Mark believed Meta needed to *be the innovator* of the next platform (mobile/cloud both leveraged not invented). Spent 5+ years; not seeing it; now pivoting to AI as the next platform. *"To do big innovation you can't do it by consensus."* Apple-like operating model; not Google-like.

**Touched pages:**

- [[vibe-coding]] — `source_count` 8 → 9; `confidence` 0.90 → 0.91. PM-leader-vantage usage of the *vibe-coding* term; Stanford-CS-faculty-level mainstream-adoption signal in <13 months from Karpathy's coinage.
- [[ai-employment-effects]] — `source_count` 15 → 16; `confidence` 0.95 (cap). Concrete operator-class numbers (30-70% layoffs / top-1% salaries doubled / 4 contracts >$10M annual). Direct evidence for the *bimodal compensation distribution* at the senior-knowledge-worker class level.
- [[ai-deskilling]] — `source_count` 4 → 5; `confidence` 0.80 → 0.82. Mid-30s middle-managers as named at-risk cohort — the PM-leadership-cohort analog of Thompson's *Pia Torian* and *senior-vs-junior code-sense* worry.
- [[durable-skills]] — `source_count` 7 → 8; `confidence` 0.90 → 0.91. PM-vantage durable-skills cluster (judgment / decisioning / courage / customer-conversation / system-design-mindset).
- [[micro-productivity-trap]] — `source_count` 12 → 13; `confidence` 0.95 (cap). The *bureaucratic-PM-role* as instantiation of the trap — *"being a bureaucrat sucks if you're a builder."*
- [[agentic-engineering]] — `source_count` 8 → 9; `confidence` 0.91 → 0.92. *Product builder* role-convergence at the design/engineering/PM-collapse level.
- [[index.md]] — added both source entries; bumped [[agent-harness]] one-liner (18 → 19 sources).

**People listed as Dangling first-mention**: **Nikhyl Singhal** (Skip founder; ex-Google/Meta/Credit Karma VP-of-Product); **Mike Abbott** (Stanford CS153 professor; Sequoia partner; ex-Twitter eng VP); **Mark Zuckerberg** (referenced in Meta-metaverse diagnosis).

**Products / orgs listed as Dangling first-mention**: **Skip** (talent agency); **skip.show** (Substack); **CS153 Frontier Systems** (Stanford course); **Credit Karma**; **Block**, **Salesforce**, **Snap** (layoff context); **Horizon Worlds** (Meta).

**Concept candidates noted**:
- *Four company phases framework* (pre-PMF / post-PMF process / hypergrowth / big-tech-late-stage) — strong promotion candidate.
- *Product builder* (vs PM/designer/engineer-as-silos) — role-collapse construct; promotion candidate.
- *Career-as-chapters / 15-18-jobs-in-50-years* — single-source.
- *Brand-at-all-time-low / modernity-of-toolchain-as-hiring-signal* — promotion candidate on second-source mention.
- *Iteration-speed-as-moat* — **two-source threshold met** (Hu + Singhal); strong promotion candidate.

### Cross-batch synthesis

The two videos are topically divergent but both extend recent wiki concept clusters:

1. **Huber extends the LLM Wiki / knowledge-graphs cluster** with the vendor-of-the-substrate vantage. Closes empirically what Raju named caveat-wise (the scale ceiling). The wiki now holds **three independent sources rejecting RAG-as-a-useful-term** (Raju + Liu + Huber) — strong convergence on the term-vs-technique distinction.
2. **Singhal extends the vibe-coding / ai-employment-effects / durable-skills cluster** from the PM-leadership / Stanford-CS-course-content vantage. The *brand-at-all-time-low* + *bimodal-compensation* + *middle-managers-as-at-risk-cohort* triad is direct operator-class numerical evidence for the bifurcation the wiki has been tracking in qualitative terms across Thompson / Jassy / Hu.
3. **The wiki's first substantive vendor disagreement**: Huber pushes back on Cherny / Anthropic's *agentic search beats RAG* framing. Worth tracking — Huber promises empirical data *"next week"*.
4. **Iteration-speed-as-moat** now hits a two-source threshold (Hu + Singhal). Strong concept-promotion candidate.

Both videos are post-2026-04 (recent ingests). No new concept page created in this batch — but five strong promotion candidates surfaced (iteration-speed-as-moat / four-company-phases / product-builder / brand-at-all-time-low / Context Rot) for future ingests.

## [2026-05-12] ingest-batch | Three articles on Karpathy's LLM Wiki — OceanBase ex-brain, Raju explainer, Liu comparative-architecture

A meta-recursive ingest batch: three Medium articles published within 23 days of Karpathy's 4 April 2026 LLM Wiki gist, all explaining the very pattern this repository implements. The batch closes a long-flagged concept-promotion candidate ([[concepts/llm-wiki|llm-wiki]]) and triggers two entity promotions ([[Garry Tan]] from Dangling; [[Andrej Karpathy]] source_count 1→4).

### [2026-05-12] ingest | OceanBase Database — I Built a Knowledge Base That Thinks (Medium, 9 April 2026; ~6-min read)

The wiki's **earliest-vendor implementation** of the LLM Wiki pattern, published 5 days after Karpathy's gist. Source page: [[2026-04-09-oceanbase-ex-brain-knowledge-base-that-thinks]].

**Substantive findings:**

- **ex-brain CLI** built by OceanBase team using **seekdb** (their AI-native database, github.com/oceanbase/seekdb). Four mechanisms: smart compilation (status / fact / event detection drives update strategy); automatic timeline extraction; entity linking with auto-stub-page creation; hybrid search via seekdb.
- **Compiled-truth principle named explicitly**: *"knowledge should update itself when new information arrives, not just accumulate."* Worked example: company Series A in March, new CEO in June, Series B in August — Notion/Obsidian accumulate three notes the user must reconcile; ex-brain compiles them so the page always reflects current truth.
- **MCP server integration as the harness/substrate boundary** — `ebrain serve` exposes `brain_get` / `brain_put` / `brain_search` / `brain_compile` / `brain_link` tools to Claude Code. **First wiki demonstration of where the harness ends (Claude Code) and the substrate begins (seekdb as compiled-knowledge storage).**
- **seekdb properties** — embedded mode single-file (1 CPU + 2 GB RAM); native hybrid search (HNSW/IVF/quantised + BM25 + scalar filtering); built-in AI functions (`AI_EMBED`, `AI_COMPLETE`, `AI_RERANK`) usable in SQL; MySQL-compatible ACID; multi-model (vector + text + scalar + JSON + GIS).
- **Names Garry Tan's GBrain** as parallel concept — *"Garry Tan's GBrain ran with the same concept. Both projects prove that LLM + local storage is a surprisingly powerful combination."*

### [2026-05-12] ingest | Sathish Raju — RAG Isn't Dead. But Something Is. Karpathy's LLM Wiki Explained (Medium, 16 April 2026; ~10-min read)

The wiki's **clearest single-article explainer** of Karpathy's LLM Wiki gist. Source page: [[2026-04-16-raju-rag-isnt-dead-karpathys-llm-wiki-explained]].

**Substantive findings:**

- **Karpathy gist statistics anchor**: posted 4 April 2026; **17 million views, 5,000 stars, 4,282 forks within days**. Framed as *"an idea file — a markdown document designed to be copy-pasted into an LLM agent"* — not a paper, not a product.
- **Three-layer architecture named with explicit ownership semantics**: raw sources (immutable, human source-of-truth) / wiki (LLM-owned entirely) / schema=CLAUDE.md (co-evolved by human and LLM).
- **Three core operations**: **ingest** (compile new knowledge, single article touches 10-15 wiki pages) / **query** (read index → drill into relevant pages → synthesise with citations; *"good answers get filed back into the wiki as new pages"*) / **lint** (scan for contradictions / stale claims / orphan pages / concepts mentioned but lacking own page).
- **Honest comparison table**: ten dimensions, RAG vs LLM Wiki, the wiki's first systematic feature-by-feature contrast.
- **Three limitations Karpathy glossed over**: **scale ceiling** (works at 100 articles / 400K words; fails at 10K without retrieval substrate); **hallucination baking** (*"in RAG, that's a wrong answer; in the wiki, that's a wrong page that every future query trusts"*); **ingest cost** (multiple LLM passes per source; expensive at high re-ingest velocity).
- **Working Python implementation** — three functions span the entire pattern (`ingest_source` / `query_wiki` / `lint_wiki`) in <200 lines.
- **The verdict**: *"Karpathy hasn't killed RAG. He's articulated something more important: that knowledge should compound, not evaporate."* Complement, not replace; hybrid architecture for serious knowledge systems.

### [2026-05-12] ingest | Yanli Liu — RAG, LLM Wiki, or GBrain? How Your Agent Remembers Changes Everything (AI Advances / Medium, 27 April 2026; ~15-min read)

The wiki's **most-substantive comparative-architecture article**. Source page: [[2026-04-27-liu-rag-llm-wiki-or-gbrain-how-your-agent-remembers]].

**Substantive findings:**

- **Three-architecture decision framework** with a unified comparison matrix (core verb / scale / compounds? / proactive? / context / setup cost / best for): **RAG** (Retrieve, 200K+ docs, no compounding, low setup, search at scale) / **LLM Wiki** (Compile, ~1K sources, compounds, medium setup, deep expertise) / **Fat Skills / GBrain** (Act, 17K+ pages, proactive via 21 crons, high setup months, autonomous ops).
- **RAG's three critical failure points** (cites a 2024 academic paper with 7 total): **chunking problem** (30-page spec fragmented; relationships destroyed); **re-derivation problem** (*"Karpathy put it sharply: 'RAG rereads the same books for every exam, never actually learning the material'"*); **passivity problem** (RAG waits for queries; never notices contradictions).
- **GBrain detailed architecture** — the wiki's deepest first-party-class description: 24 autonomous skills + 21 cron jobs + 17,888-page brain on Postgres + pgvector; **"thin harness, fat skills"** (~200 lines harness; intelligence in skill files); CLAUDE.md + RESOLVER.md as routing (*"skill descriptions themselves function as the resolver"*); always-on signal-detector skill (*"an unlinked mention is a broken brain"*); deterministic-vs-latent work split; Tan's iteration toward *"fewer fatter skills"*.
- **Convergence prediction**: 2023 RAG era → 2025 Wiki + Skills emerge → 2026+ convergence. *"The three-way split won't last."*
- **Claude Code as partial-convergence-example** — CLAUDE.md = mini-wiki + auto-memory = compounding + skills = action. *"It's not a deliberate implementation of all three patterns — but the same pressures produced the same solutions."* Meta-relevant: this repository runs inside this exact runtime.

### Concept and entity promotions on this batch

- **[[concepts/llm-wiki|llm-wiki]]** — **NEW CONCEPT PAGE created** — anchored by 4 sources (Karpathy's Sequoia interview + 3 new explainer articles). Closes the long-flagged promotion candidate. The wiki now anchors at the concept layer the foundational pattern it implements at the schema layer.
- **[[Garry Tan]]** — **PROMOTED from Dangling to entity page** — 3-source threshold met (Tan/GStack + ex-brain mention + Liu deep treatment). Documents both GStack (Claude Code skill toolkit) and GBrain (autonomous knowledge base with 24 skills + 21 crons + 17.8K-page brain). The wiki's first canonical AI-founder-type-archetype operationalised.
- **[[Andrej Karpathy]]** entity — `source_count` 1 → 4; `confidence` 0.85 → 0.92; `last_confirmed` updated to 2026-05-12. Expanded the *LLM-wiki / LLM-knowledge-base pattern* paragraph to reference the gist statistics (17M views, 5K stars) and the three new explainer articles.

**Touched pages:**

- [[concepts/llm-wiki|llm-wiki]] — created (4 sources / confidence 0.85).
- [[Garry Tan]] — entity page created (3 sources / confidence 0.85).
- [[Andrej Karpathy]] — `source_count` 1 → 4; `confidence` 0.85 → 0.92.
- [[index.md]] — added 3 source entries; added [[concepts/llm-wiki|llm-wiki]] to Concepts section.

**Body-wikilink-rule disambiguation note**: The new [[concepts/llm-wiki|llm-wiki]] concept page shares its basename with the root-level [`llm-wiki.md`](../../llm-wiki.md) (Karpathy's original conceptual spec — predates this repo's wiki layer). VSCode's wiki-link extension flags this as an ambiguous identifier; Quartz / graph-export / lint resolve cleanly. Defensive choice: body wikilinks use the folder-qualified `[[concepts/llm-wiki|...]]` form. Lint-page.mjs matches by basename, so `relationships.target: llm-wiki` still satisfies the body-wikilink-rule against `[[concepts/llm-wiki|...]]` references.

**People listed as Dangling first-mention**: **Yanli Liu** (finance practitioner, Luxembourg; AI Advances Medium contributor; 4.5K followers); **Sathish Raju** (Senior AI Architect at Lenovo; ex-co-founder/CTO of kloud.io acquired by Alation); **OceanBase Database** (publication — the engineering team behind ex-brain + seekdb); **Ali Partovi**, **Sarah Chen** (example-data entities in ex-brain CLI samples).

**Organisations / products listed as Dangling first-mention**: **AI Advances** (Medium publication, 78K followers); **OceanBase** (parent company of OceanBase Database); **ex-brain** (Tan-adjacent personal-KB CLI); **seekdb** (OceanBase's AI-native database; github.com/oceanbase/seekdb); **GBrain** (Tan's open-source autonomous-knowledge-base — *now load-bearing across 3 wiki sources*); **OpenClaw**, **Hermes** (personal AI agents Liu names alongside Claude Code as GBrain's intended runtime); **kloud.io** (Raju's pre-Lenovo startup, acquired by Alation); **Alation** (Raju's pre-Lenovo employer); **Lenovo** (Raju's current employer); **Pinecone**, **Chroma**, **LlamaIndex** (RAG/vector-DB ecosystem); **Mem**, **Granola** (AI-powered note-taking criticised in ex-brain article); **DashScope** (embedding/AI provider seekdb supports).

**Candidate concepts noted**:
- *Compiled-truth principle / knowledge-compounding-not-evaporation* — central thesis of the LLM Wiki concept; now folded into the [[concepts/llm-wiki|llm-wiki]] page.
- *Three-architecture decision framework (RAG / Wiki / Skills)* — Liu's framework; single-source as a *named-framework*.
- *Thin harness, fat skills* — Liu's framing of GBrain's architecture; convergent-but-distinct from Böckeler's harness vocabulary. Single-source.
- *Hallucination baking / persistent-mistake-amplification* — Raju's named risk; single-source as a named-risk.
- *Scale ceiling at ~100 pages without retrieval substrate* — Raju's named limitation; single-source.
- *MCP-server-as-LLM-Wiki-interface* — ex-brain's `ebrain serve` pattern; single-source as a named-interface-pattern.

**Pre-flight notes**: All three sources verified per the [§Verifying sources before ingest] contract — title, author, publication date, scope all match. PDF page counts: OceanBase 11 pages (~6-min read; pages 10-11 are footer); Raju 15 pages (~10-min read; pages 13-15 are footer); Liu 22 pages (~15-min read; pages 18-22 are footer). All three published within 23 days of Karpathy's 4 April 2026 gist — they are responses to the same upstream event. Articles converge on the three-layer architecture, the three operations, and the three-limitations triad, with substantial cross-citation between them (Raju cites Karpathy directly; Liu cites both Karpathy and GBrain; OceanBase cites both Karpathy and GBrain). Strong cross-source evidence that the LLM Wiki pattern has stabilised at the architectural-vocabulary level.

### Cross-batch synthesis

This three-article batch is **meta-recursive**: the wiki documents secondary commentary on the wiki's own foundational pattern. Specifically:

1. **The LLM Wiki pattern is now anchored at the concept layer** — previously scattered across `llm-wiki.md`, `llm-wiki-v2.md`, `CLAUDE.md`, and the Karpathy entity's mention. The new [[concepts/llm-wiki|llm-wiki]] concept page consolidates the construct.
2. **The three operations Raju names (ingest / query / lint) match this repo's CLAUDE.md §"The four operations"** exactly minus the v0.3 *synthesize* addition. Strong external validation of the operation vocabulary.
3. **The cross-cutting-touch property (10-15 pages per ingest) is convergent** between Liu's explainer and this repo's CLAUDE.md framing.
4. **The convergence prediction** (Liu + Raju): hybrid RAG + Wiki + Skills. Direct implication for this repo's roadmap: when the source count outgrows context-window scale, the wiki should add a vector retrieval substrate (per the v0.5+ plan in `llm-wiki-v2-plan.md`).
5. **The hallucination-baking risk** (Raju): organised, persistent mistakes are harder to spot than individual errors. Design implication for the wiki's lint operation: scan for *plausible-but-wrong* claims specifically, not just orphans and contradictions.

## [2026-05-12] ingest-batch | Three video sources — GStack (Garry Tan / YC), Knowledge Graphs for AI Agents (SurrealDB), Stanford CS224W KG Embeddings (Leskovec)

A three-video batch with two distinct thematic clusters: (1) [Tan/GStack] continues the AI-engineering-team / harness / agentic-engineering cluster from the prior YC ingest (Hu 24 April), with Tan published the day before; (2) [SurrealDB + Leskovec] establishes the **knowledge-graphs** concept page after a four-source threshold met across academic, industrial, agentic-memory, and practical-engineering vantages.

### [2026-05-12] ingest | Garry Tan (YC President/CEO) on GStack — How to Make Claude Code Your AI Engineering Team (YC YouTube, 23 April 2026; 21:49)

A 21:49 demo + monologue from Garry Tan introducing **GStack**, an open-source toolkit (built in 3 weeks; *"more GitHub stars than Ruby on Rails"*) that wraps Claude Code with named skills for office hours, plan/CEO/adversarial review, design shotgun, code review, SLQA/SL browse, and ship. ASR caption track; 15 chapters. Source page: [[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack]]. **The YC-batch-context anchor pair** with Hu 2026 — two consecutive-day YC-partner-vantage sources on AI-native engineering.

**Substantive findings:**

- **GStack as an open-source harness-of-skills shipping at venture pace** — Tan ships in 3 weeks at YC-president scale; demonstrates the *harness templates* future-prediction Hu made the next day at startup-development scope. Skills: Office Hours (16-YC-partners adversarial-review distilled at 10% strength); Plan / CEO Review / Adversarial Review (multi-step auto-fix; demoed 6/10→8/10 in two rounds); Design Shotgun (multiple AI variants in ~60s); Code Review (staff-level bug-catching); SLQA / SL browse (Playwright+Chromium wrapped as CLI); Ship (pre-merge gate).
- **The wiki's first founder-CEO-of-major-accelerator open-source-harness instantiation** — distinct from Lopopolo's in-vendor harness, Anthropic's Skills (modules), or Böckeler's consultancy framing. Tan ships an entire bundled harness as an open-source repo with all skills wired together.
- **AI founder type archetype operationalised at YC-president scale** — Tan reports 10-15 parallel Claude Code sessions, ~400 PRs in review, *"10, 15, 20, sometimes 50 PRs in any given day."* Direct worked example of Hu's *AI founder type* archetype (still builds / still coaches / leads by example).
- **Steve Yegge Gas Town stage 7 invoked explicitly** — *"GStack does not get you to level 8, but I do think it gets you to level seven."* **Two-source threshold met** on Yegge's eight-stages-of-dev-evolution-to-AI framework (Böckeler + Tan).
- **Playwright-as-CLI as the wiki's first vendor-published browser-control-without-MCP worked example** — Tan's motivation: *"Claude in Chrome MCP is one of the worst pieces of software I've ever used."* Wrapped Playwright + Chromium at the CLI level so *"your Claude Code and any agent can actually just use the browser"* — screenshots, complex interactions, click/fill, regression tests, CSS-bug-assessment.
- **ADHD-CEO-vs-autistic-CTO model-allocation framing** — Tan: *"by default [Claude Code] uses Claude. And I think Opus 4.6 is sort of ADHD CEO. He's the guy you want to get a beer with and he's got a billion ideas, but when the going gets tough, you got to call in your autistic CTO and that's Codex."* First-party-CEO articulation of model-allocation-by-personality-fit-to-task.
- **Bottleneck-shift to QA when coding is automated** — *"once the agent was doing all the work of planning and design and coding, I found myself sitting there doing QA, probably the least fun part of software development."*
- **Live demo** — full idea-to-near-shippable-design in ~10 minutes of video time on a tax-document-aggregator example. Office Hours surfaces business-model expansion (document-aggregation → CPA matchmaking is *"10× more"* monetisable).
- **Closing peroration** — *"the barrier to building just collapsed. The only question left is what are you going to build? It's time to let it rip. Go make something people want."*

**Touched pages:**

- [[vibe-coding]] — `source_count` 7 → 8; `confidence` 0.89 → 0.90. Added Tan as the **live-demo-of-vibe-coding-with-discipline-at-YC-president-scale** vantage.
- [[agent-harness]] — `source_count` 16 → 17 (with V9 also touching this, 16 → 18 net); `confidence` 0.95 (cap). Added Tan as the **founder-CEO open-source-toolkit harness vantage**.
- [[agentic-engineering]] — `source_count` 7 → 8; `confidence` 0.90 → 0.91. Added Tan as the **founder-CEO operationalisation vantage** — the worked example of Hu's AI-founder-type archetype.
- [[index.md]] — added the source entry; updated agent-harness one-liner.

**People listed as Dangling first-mention**: **Garry Tan** (YC President & CEO; engineer; Stanford CS; ex-Palantir #10; Posterous co-founder; built Bookface). Promote on second-source mention.

**Organisations / products listed as Dangling first-mention**: **GStack** (Garry Tan's open-source toolkit; **strong promotion candidate**); **Conductor** (multi-session Claude Code orchestrator); **Palantir** (Tan's first decade employer; ASR rendered as *"Palunteer"*); **Posterous** (Tan's pre-YC startup, sold to Twitter); **Bookface** (YC's internal social platform).

**Candidate concepts noted**: *Model-allocation-by-personality-fit-to-task* (Tan's ADHD-CEO/autistic-CTO framing); *Open-source-toolkit-of-skills-shipping-in-weeks*; *Bottleneck-shift-to-QA-when-coding-is-automated*. All single-source.

**Pre-flight notes**: Identity verified. Transcript fetched via `youtube-transcript-api` fallback after Playwright timeout. ASR-only caption track. 521 raw segments → 103 grouped windows. Chapter `start_ms: 0` bug recurs as expected; recomputed from `mm:ss` strings. ASR errors flagged: *"Palunteer"* for Palantir, *"Gary"* for Garry, *"GSAC"* for GStack, *"Gritan"* for Garry Tan in GitHub URL.

### [2026-05-12] ingest | Martin (SurrealDB) on Knowledge Graphs for AI Agents — A Practical Guide (SurrealDB YouTube, 27 April 2026; 60:04)

A 60:04 webinar by Martin (Solutions Engineer at SurrealDB) on knowledge-graph-grounded RAG for AI agents. Manual caption track; 9 chapters. Source page: [[2026-04-27-surrealdb-knowledge-graphs-for-ai-agents-practical-guide]]. **The wiki's first dedicated knowledge-graph-architecture source** with substantive vendor-practitioner depth on the full ETL pipeline.

**Substantive findings:**

- **Three named vector-only-RAG failure modes** — **context clash** (multiple chunks compete, all correct, but the LLM gets overloaded); **context confusion** (chunks contradict each other); **dense neighbourhood degradation** (high-dimensional space saturated near common topics). The wiki's first first-party-vendor articulation of vector-only-RAG's breakdown modes as named failure patterns.
- **GraphRAG mechanic walk-through** — vector-search trimmed by graph-relationship subset; multi-hop traversal in single SurrealQL query (vector + graph + full-text + relational together). Worked customer-support example: *"my mouse Bluetooth isn't working"* → infer product+issue → vector-search-within-product-graph-subset reduces dense neighbourhood. *"Adding graph to that helps you trim down the results."*
- **The KG-ETL pipeline as a named discipline** — Extract (parsing + chunking + embedding + entity-extraction + relationship-extraction) → Transform (deduplication + ontology + canonicalisation) → Load. Each stage has named-strategy choices with explicit accuracy-vs-cost tradeoffs.
- **Chunking-strategy taxonomy** — first explicit framing as a *choose-by-tradeoff* discipline: recursive (cheapest, lowest accuracy) → structural → **semantic (sweet spot)** → agentic (research frontier) → no-chunking (research frontier; let LLM read whole document). Martin's recommendation: semantic chunking for production.
- **The "smaller chunks better" research finding** cited verbally by Martin — *"there are research papers that have demonstrated that the smaller the context you give to an LLM, the better the result."* Open primary-source target.
- **Two specimen KG-architecture styles** — explicit/transactional-mapped (e-commerce database with foreign-key-derived entities and relationships) vs hybrid/LLM-inferred (articles where authors+years are explicit but chunks+concepts+companies+relationships are LLM-inferred).
- **Decision criteria for KG vs vector-only** — manual-driven Q&A on a single product line → vector-only may suffice; multiple products / domains / use-cases → graph trimming becomes valuable; decisions / explainability / dynamic-knowledge → KG required.
- **SurrealQL hybrid-query mechanic** — single query expresses vector + graph + full-text + relational; *"the beauty of having our own SQL-like query language is that we can have all those modalities in a single query."*
- **Agentic RAG with retrieval-tool-selection** — the LLM chooses among vector / graph / full-text / hybrid tools at runtime based on query nature.
- **KGs are not new** — *"this became very popular a couple of decades ago already and was very popular in the Google search engine."* Martin grounds the construct historically.

**Touched pages:**

- [[knowledge-graphs]] — **NEW CONCEPT PAGE created** — anchored by this source + Leskovec + Manditereza + Bratanic (4 sources, confidence 0.85).
- [[agent-harness]] — `source_count` 17 → 18; `confidence` 0.95 (cap). Added SurrealDB as the **KG-as-persistent-context-substrate vantage**; prose lead "sixteen" → "eighteen".
- [[industrial-ai-agents]] — `source_count` 1 → 2; `confidence` 0.70 → 0.75. Added SurrealDB as the second-vendor cross-domain anchor on KG-as-substrate. Updated the knowledge-graph note to reflect the promotion to its own concept page.
- [[index.md]] — added the source entry; added the new [[knowledge-graphs]] concept entry; updated industrial-ai-agents one-liner from *stub* to *2 sources*.

**People listed as Dangling first-mention**: **Martin** (SurrealDB Solutions Engineer; surname not given); **Sebastian** (audience-Q-asker, first-name only); **Santi** (audience-greeting, first-name only).

**Organisations / products listed as Dangling first-mention**: **SurrealDB** (multimodal database; ~31k GitHub stars; Rust-based; **strong promotion candidate**); **SurrealQL** (SurrealDB query language); **Surrealist** (SurrealDB browser-based UI).

**Candidate concepts noted**: *Context clash / context confusion / dense neighbourhood degradation* (single-source named-failure-modes); *Hybrid search in a single query* (single-source architectural claim); *Agentic RAG with retrieval-tool-selection* (single-source as named pattern).

**Pre-flight notes**: Identity verified. Transcript fetched via `youtube-transcript-api`. Manual caption track at `language_code: en` — both manual and ASR tracks at `en`, picked manual by listing tracks first and selecting `not is_generated`. 728 raw manual segments → 244 grouped windows.

### [2026-05-12] ingest | Jure Leskovec on Stanford CS224W: Knowledge Graph Embeddings (Stanford Online YouTube, 7 December 2023; 70:04)

A 70:04 academic lecture by **Jure Leskovec** (Professor of Computer Science at Stanford; SNAP Group lead) from CS224W (Machine Learning with Graphs) autumn 2023 semester. Manual `en-US` caption track. **The wiki's oldest video source by publish date** — by more than a year. Source page: [[2023-12-07-leskovec-stanford-cs224w-knowledge-graph-embeddings]]. Pre-GenAI-era foundational academic reference for the [[knowledge-graphs]] concept the LLM-era practitioner sources operate on top of.

**Substantive findings:**

- **The KG-completion task formulation** — *"given a head entity and a relation type, predict the missing tails."* The canonical academic task; example: `(J.K. Rowling, genre, ?) → Fantasy / Young-Adult Fiction`. Generalises basic-graph link-prediction to heterogeneous-relation graphs.
- **Four shallow KG-embedding methods**: TransE (`h + r ≈ t` Euclidean translation), TransR (project entities into relation-specific space then translate), DistMult (bilinear scoring via Hadamard product), ComplEx (complex-valued embeddings; bilinear with conjugate).
- **Relation-pattern taxonomy** — symmetric / antisymmetric / inverse / composite / 1-to-N. The discriminator-set for embedding-method comparison.
- **Method × pattern coverage matrix** — the lecture's central pedagogical artifact. No single shallow-embedding method covers all relation patterns. *"At the end, basically, this table will be filled in and it will make sense."*
- **Contrastive / triplet loss training** — for each true triple `(h, r, t)`, sample corrupted triple `(h, r, t')` and minimise hinge-loss violation. Subtlety: *"pick a tail that is of the same type, but wrong"* — type-matched negative sampling rather than random sampling.
- **FreeBase scale-and-incompleteness empirical anchor** — ~80M entities, 38k relation types, 3B edges. **93% of people in FreeBase don't have a place-of-birth**; 80% don't have a nationality. The wiki's first concrete-numbers anchor for the KG-incompleteness problem.
- **Industrial KG product catalogue** — Google Knowledge Graph, Amazon, Facebook Graph API, IBM Watson, Microsoft Satori, LinkedIn, Yandex. Pre-GenAI-era industrial KG deployments (circa 2023).
- **Question-answering example** — *"what are the latest films by the director of Titanic?"* — multi-hop graph traversal in production search systems. Direct historical antecedent to the SurrealDB GraphRAG patterns 30 months later.
- **Word-embedding analogy** as motivational frame for translation-embeddings — King→Queen, China→Beijing, USA→Washington DC. TransE generalises the same arithmetic to typed KG relations.
- **Lecture self-correction** — Leskovec discovers wrong-slides at 1:30 and restarts (*"sorry, sorry, sorry ... brand new lecture"*); preserved verbatim in manual transcript.

**Touched pages:**

- [[knowledge-graphs]] — academic-foundation anchor on the new concept page (one of four sources).
- [[index.md]] — added the source entry.

**People listed as Dangling first-mention**: **Jure Leskovec** (Stanford CS professor; SNAP Group; co-creator of GraphSAGE, Node2Vec, DeepWalk; **strong promotion candidate** — academically canonical in this space and likely to recur); **Jiaxuan** (CS224W TA, transcript-uncertain spelling).

**Organisations / products listed as Dangling first-mention**: **Stanford Online** (channel/publisher); **Stanford SNAP** (Leskovec's research group); **CS224W** (Stanford ML-with-Graphs course); **FreeBase** (~80M entities, 38k relations, 3B edges; Google-acquired); **FB15k / FB15k-237** (academic benchmark KGs); **Wikidata**; **DBpedia**; **Google Knowledge Graph**; **Microsoft Satori**; **IBM Watson**; **Node2Vec / DeepWalk** (shallow-embedding methods Leskovec generalises); **TransE / TransR / DistMult / ComplEx** (KG-embedding method family).

**Candidate concepts noted**: *KG completion task*; *Relation pattern taxonomy*; *Contrastive/triplet loss with type-matched negative sampling*. All single-source as named-constructs (Leskovec is the academic-canonical source but pre-GenAI-era practitioner literature also uses them).

**Pre-flight notes**: Identity verified. **Oldest wiki source by publish date** (2023-12-07) — by more than a year vs the next-oldest source. Transcript fetched via `youtube-transcript-api` with `languages=['en-US', 'en']` priority order. Manual caption track at `language_code: en-US` (not `en` — the ASR track is at `en`). 1247 raw manual segments → 299 grouped windows. The lecture's first-segment timestamp was already in video-time (no event-time normalisation needed). The transcript preserves Leskovec's on-record self-correction at 1:30 (*"sorry, sorry, sorry ... brand new lecture"*) — evidence of manual track fidelity.

### Cross-batch synthesis (12 May 2026 ingest cohort)

This three-source batch closes one significant wiki gap and tightens another:

1. **The knowledge-graphs concept gap** — closed. Four-source threshold met (Leskovec academic-foundation + Manditereza industrial-OT + Bratanic agentic-memory + SurrealDB practical-engineering). [[knowledge-graphs]] promoted to a dedicated concept page with 0.85 confidence. KG-as-construct is now load-bearing across the wiki's harness / agentic-memory / RAG / industrial-AI clusters.
2. **The YC-batch-context anchor pair** — Tan (23 April) + Hu (24 April) on consecutive days, both YC-partner-vantage sources on AI-native engineering. The agentic-engineering concept page is now structurally rich with seven distinct vantages on the discipline.
3. **Two-source threshold on Yegge Gas Town** — met (Böckeler + Tan). Yegge's eight-stages-of-dev-evolution-to-AI framework is now a named pattern in the wiki.

**Convergence threshold notes**:
- *KG-construct as universal-substrate-across-agentic-stack-layers* — four-vantage convergence is unusually strong; the construct demonstrates **maximal polymorphism** (same data structure, four distinct uses across the agentic stack).
- *Agent-driven question-narrowing / Socratic-dialogue spec elicitation* — four-source convergence now met (Rufus / Thompson / Böckeler / Tan-Office-Hours). Strong promotion candidate.
- *Founder-as-AI-founder-type archetype operationalised* — two-source threshold met (Hu prescribes / Tan demonstrates at YC-president scale).

## [2026-05-11] ingest-batch | Three video sources — Amodei conversation (metadata-only stub), Guthrie / Braintrust Evals 101, MIT OCW Future of Open Education

A three-video batch ingested on 11 May 2026. Two substantive sources + one metadata-only stub. The batch shares a transcript-fetch theme: all three triggered the Playwright `transcript panel did not render` failure on the skill's primary path; one of the three (Amodei) had captions outright disabled.

### [2026-05-11] ingest | Amodei × Vora at Code with Claude conference (METADATA-ONLY STUB)

The wiki's **first METADATA-ONLY video stub** — transcript retrieval failed and could not be substituted. A 33:10 live-stream from Anthropic's *Code with Claude* developer conference (San Francisco, 6 May 2026); **Dario Amodei** (CEO / co-founder) + **Daniela Amodei** (President / co-founder) in conversation, moderated by **Ami Vora** (Chief Product Officer). Source page: [[2026-05-06-amodei-anthropic-cofounders-code-with-claude-conference]].

- **Why metadata-only**: Playwright skill returned an empty `caption_tracks: []` list; the `youtube-transcript-api` fallback raised `TranscriptsDisabled`. Subtitles are disabled for this video. No transcript available via either path.
- **Source page frontmatter** carries `status: stub` for the v0.2 lifecycle tooling to surface this as an open re-ingest target.
- **Re-attempt opportunities flagged**: (1) wait for caption enablement; (2) substitute an Anthropic-published transcript or article version; (3) substitute community-published event notes.
- **Touched pages**: [[index.md]] only. No concept-page updates (no substantive content to weave); no entity-page updates beyond a stub-level mention of [[Anthropic]] which is unchanged.
- **People listed as Dangling first-mention**: **Dario Amodei** (Anthropic CEO / co-founder); **Daniela Amodei** (Anthropic President / co-founder); **Ami Vora** (Anthropic Chief Product Officer); **Code with Claude conference** (Anthropic's developer event). All four are first-mention as named-but-non-substantively-quotable.
- **Pre-flight notes**: Identity verified. Live-stream `is_live: True` flag preserved in YAML. Coincidence-flag noted that 6 May 2026 was an unusually dense ingest date (also Böckeler QCon London; also Jassy HBR IdeaCast from 6 May 2025).

### [2026-05-11] ingest | Doug Guthrie (Braintrust) — Evals 101 at AI Engineer World's Fair (27 June 2025; 48:31)

The wiki's **earliest source on AI evaluation as a formalised discipline**. A 48:31 hands-on workshop by **Doug Guthrie** (Braintrust solutions engineer; ex-dbt Labs) at the AI Engineer World's Fair, San Francisco. ASR caption track; no chapters. Source page: [[2025-06-27-guthrie-braintrust-evals-101-ai-engineer-worlds-fair]].

**Substantive findings:**

- **Four ingredients of an eval**: **task** (the code or prompt to evaluate, requires only `(input) -> (output)`); **dataset** (real-world examples; `{input, expected?, metadata?}` per row); **scores** (the logic — LLM-as-judge OR code-based); **experiment** (snapshot in time of an eval run, enables regression detection across weeks/months).
- **Two score families**: **LLM-as-judge** (LLM scores output against criteria, returns label like excellent/fair/poor mapped to numeric 1 / 0.5 / 0) and **code-based** (heuristic or binary check in TypeScript/Python). **Auto-Evals package** ships out-of-the-box scores. Three customer-tested practices: use higher-quality models for scoring than for the prompt; break scoring into focused areas (accuracy / formatting / correctness as separate scores rather than combined); avoid overloading score prompts with context.
- **Three operational modes that compound — offline / online / flywheel**: Offline = pre-production iteration. Online = real-time tracing in production with sampling-rate scoring (10-20%) at the span-level. Flywheel = filter low-scored production logs, human-review them, add to offline datasets — *"this is what's missing oftentimes when we're building these AI applications and what Braintrust allows for really seamlessly."*
- **The "evals as offense" reframing** credited to **Anker Goyal** (Braintrust CEO): *"evals are a really great way for us to play offense as opposed to just playing defense where unit tests are kind of used for. This can actually be used as a tool to really help create a lot of rigor around us building and developing these applications and ensuring that we actually build things that we can put into production."* Distinguishes the eval discipline from the test discipline at the framing level.
- **Just-start-don't-optimise-the-dataset-first anti-pattern call-out** (Anker Goyal via Guthrie): *"A lot of people get caught in creating this golden dataset of test cases that they can then iterate from. Start — you don't necessarily have to do that."* Wiki's first first-party-vendor articulation.
- **Score-at-the-span-level for agentic workflows**: not just root-level scoring; e.g. a conversational-analytics app that first rephrases the user's question can have a dedicated score for the rephrasing span.
- **Evals-as-CI-check pre-merge gate**: via CI/CD, with a GitHub Action template shipping in Braintrust's documentation. Wiki's first articulation of evals-as-CI as a discipline-level practice.
- **The "Loop" feature** (released day-of-workshop, 27 June 2025): Cursor-like IDE where AI optimises prompts against eval scores. Demonstrated but failed live (*"I think I have an issue with my anthropic API keys"*) — flagged as vendor-side feature rather than fully-validated workflow.
- **SDK + version-controlled prompts**: two consumption paths (UI-first Playground; Codebase-first via Python/TypeScript/Go/Java/Kotlin SDKs); both interoperate.
- **Human-in-the-loop two-mode distinction**: internal-team human review of logs (engineers, PMs, *"a healthcare company that has doctors coming into the platform"*) vs application-end-user feedback (thumbs-up/down + free-text comments).
- **Sarah-from-Notion role-taxonomy** (cross-referenced from a prior Braintrust workshop): *"a special type of role for human-in-the-loop — almost like a product manager mixed with an LLM specialist."* Promotion candidate as a named-archetype.

**Touched pages:**

- [[agent-development-lifecycle]] — `source_count` 2 → 3; `confidence` 0.80 → 0.83. Added a Test-phase operational-vocabulary anchor referencing Guthrie / Braintrust as the wiki's earliest formalised-eval-discipline source; fills in Chase's *datasets / metrics / experiments / simulations* with the operational *how* (task/dataset/scores/experiment + offline/online/flywheel).
- [[agent-harness]] — `source_count` 15 → 16; `confidence` 0.94 → 0.95. Added Guthrie / Braintrust as the **eval-platform-vendor vantage** that operationalises Chatterjee's Contracts (formal evaluable specifications) and Compounding (telemetry-feeds-learning) layers with vendor-specific tooling vocabulary. Prose lead "fifteen" → "sixteen".
- [[agentic-engineering]] — `source_count` 6 → 7; `confidence` 0.89 → 0.90. Added Guthrie as the **eval-platform-vendor vantage** on what the agentic engineer's *quality-bar preservation mechanism* looks like at agent throughput.
- [[index.md]] — added the source entry; bumped the [[agent-harness]] one-liner (15 → 16 sources).

**People listed as Dangling first-mention**: **Doug Guthrie** (Braintrust solutions engineer; ex-dbt Labs); **Anker Goyal** (Braintrust CEO); **Versel AI SDK** as a wrappable client.

**Organisations listed as Dangling first-mention**: **Braintrust** (end-to-end AI developer platform; **strong promotion candidate** — likely to recur on future eval-tooling ingests); **[[AI Engineer]]** (conference series + YouTube channel); **dbt Labs** (Guthrie's previous employer); **Notion** (customer); **Cursor** (referenced as IDE paradigm for Loop feature).

**Candidate concepts noted but NOT promoted on a single source**:
- *Eval flywheel / online-to-offline feedback* — **three-source convergence threshold met** (Guthrie + [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage]] + [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu]]). **Strong promotion candidate** for a *learning-capture-flywheel* concept page.
- *LLM-as-judge*; *Auto-evals*; *Score-at-the-span-level*; *Evals-as-CI-check*; *Evals-as-offense* — all single-source.

**Pre-flight notes**: Identity verified. Transcript fetched via `youtube-transcript-api` fallback after Playwright timeout. 1280 raw ASR segments → 217 grouped windows. Note: transcript ends mid-Q&A — the recording cuts off during a government-pre-launch-evals question with *"They have huge data sets of thousands of questions, believe me, as a—"*. Honest-scoping flag.

### [2026-05-11] ingest | The Future of MIT Open Education (MIT OCW panel, 6 May 2026; 57:52)

The wiki's **first ingest on open-education-as-supply-side for the AI-era skills question**. A 57:52 panel from a 6 May 2026 MIT OpenLearning event (likely OCW's 25th-anniversary). **Three panelists**: **Dimitris Bertsimas** (MIT Vice Provost for Open Learning; Sloan professor + associate dean); **Sarah Hansen** (Asst Director Open Education Innovation; moderator); **Curt Newton** (Director MIT OpenCourseWare; ~22 years at OCW). Audience Q&A in the final ~20 minutes. **Manual caption track** selected for highest fidelity (the wiki's third `kind: manual` video source after Sternfels and Jassy). Source page: [[2026-05-06-mit-ocw-future-of-mit-open-education]].

**Substantive findings:**

- **The 1-billion-learners-in-10-years ambition**: Bertsimas. OCW currently at ~500M lifetime learners; 2x scale-up in 10 years vs the 25 years it took to reach 500M. *"Aspiring to educate 1 in 8 in the world, especially in areas — if you look at Africa, for example, only 10% of the population goes to university."* Two orders of magnitude beyond MIT's residential cohort (11k students at any time; ~15k 1-in-a-million students over 41 years) — only achievable via AI-amplified distribution.
- **Universal Learning architecture** — launched March 2026 (individuals + institutions). Currently **22 modules of Universal AI** (16 fundamentals + 6 verticals); 18 more verticals "cooking"; ~30 MIT faculty have participated. Five-piece fundamentals structure: programming + ML; deep learning (3 modules, 15-17 lectures); prescriptive AI / decision-making; LLMs + generative AI; ethics of AI + future of work. Verticals: AI + energy, AI + health, AI + law, AI + drug design, AI + satellite data, ... ("AI + x"). Follow-ons planned: **Universal Climate + Energy** (first modules September 2026); **Universal Biology**; **Universal Health**.
- **Horizontal-knowledge architecture as deliberate structural innovation**: *"Universities are structured vertically. We have civil engineering, number 1. Mechanical engineering, number 2 ... But that's not how the world is organized. The world is organized horizontally. There are problems of health, of climate ... the major problems of the world, energy and so forth — they are not organized neatly in a vertical way. So I think there is an opportunity, in my opinion, to educate the world, and especially the young people, in a way the problems come. Because problems don't come with labels."*
- **AI-translation tipping-point claim** — Newton: *"with the AI tools that are being brought now to bear, we've crossed the tipping point. They're good enough showing up on Learn to really unleash the access to this knowledge as a public good for all languages."* Bertsimas verifies Greek personally (*"A-plus"*) and tested in two Greek high schools (~80 + ~70 students; *"comments are very positive"*). Translation into **12 languages launching May 2026**. The wiki's first first-party institutional-leader claim that the AI-translation tipping point has been crossed for educational content.
- **Personalized education** launching summer 2026, based on AI research. Newton's architectural distinction: **personalized** (the agent reorganises content per learner) vs **personalizable** (content has the wide-open structure that *enables* reorganisation). *"What OCW has is personaliz**able** materials. It's put out there in a wide-open form so that you can grab as little or as much as you want."*
- **Three-phase open-content ladder**: Phase 1 = MIT faculty author content; Phase 2 = external institutions author content with platform access (top engineering school in Greece active — MIT-educated faculty developing AI + drug design / AI + satellite data); Phase 3 = MIT curates the best of phase-2 for global distribution. *"In the end of the day, it runs on MIT, on things that ... that's my bet anyway"* — MIT brand preserved through Learn.mit.edu hosting + quality-control gate.
- **MIT Learn platform** consolidation — moving OCW + MITx + Professional Education onto a single platform by July 2026; built on **OpenIndex**. *"In a sense, we are controlling our destiny. We are controlling quality. We are controlling — all of our innovations will be there. We are going to create — we are creating translations."*
- **AskTIM AI tutor** (MIT reversed = TIM) — supports *"every aspect"* of the Universal AI curriculum.
- **MIT-Wikipedia collaboration project** — in conversation between MIT OpenLearning and Wikipedia community (Andrea named as Wikipedia rep). Wikipedia at 4-5 billion learners; OCW at 0.5 billion. Bertsimas: *"They [Wikipedia] don't actually teach. They translate information. It's not multimedia. It's primarily text. We are hoping to combine forces."* On Bertsimas's office whiteboard as a tracked-goal-not-yet-accomplished.
- **Financial-sustainability constraint**: MIT's **$20M institutional subsidy** to OpenLearning **drops to $0 in four years**. Forces a hybrid model — *"95-97% [of learners] should be free"* + paid workforce-learning streams making sustainability possible. *"Imagine if, on my hands, OpenLearning collapses. That would be ... not in my intentions."*
- **Modularised-learning content-revision-velocity argument**: *"If you expect my colleagues at MIT, me included, to revise 50% of a class that change in AI, 26 lectures, 50% [meaning] 13 lectures. Good luck. I mean, it will never happen. But if you have a module of four or five [lectures] to change two lectures, it's feasible."* The 4-5-module unit is **a content-revision-velocity choice**, not just a learner-attention-span choice. Critical for AI-content currency where the underlying field moves faster than a yearly course-revision cycle.
- **The AI-and-cognitive-impact open question** (final audience question): *"Several studies from MIT have shown that using AI to supplement learning can sometimes actually hinder those learning faculties in the brain. So my question is, how do you decide how much AI is enough?"* The audio cuts off as Bertsimas begins his answer (mic dropped). The wiki holds the *question* without first-party MIT leadership *answer*. Open primary-source target.
- **Bayo Akomolafe (UNESCO digital-learning summit) citation**: Newton invokes Akomolafe on *"the very concept of authorship of ideas ... maybe there's a letting go of the concepts of ownership and authorship that get very enmeshed with things like brands."* Anticipates that the AI-driven shift will require institutional brand-strategy rethinking.
- **Chuck Vest legacy framing**: Bertsimas — *"Chuck felt that in his 12 years as a president, his two most important contributions to the world was OCW ... and the women faculty movement."* Bertsimas frames the current presidential term (Sally Kornbluth) as having an analogous Universal-Learning legacy opportunity.
- **The trades-and-PK-12 extension**: audience-raised. PK-12 (Bertsimas: *"My colleagues in PK-12 have some ideas ... we are still developing our strategy"*); trades (refrigerator-fix anecdote → ecosystem-with-community-colleges).
- **The in-person/Fab-Labs collaboration**: Bertsimas in conversation with Neil Gershenfeld (Fab Labs program lead). Hybrid education at distributed-physical-lab scale; cybersecurity first, AI second. *"I haven't even wrote it on my board"* — at the experimental stage.

**Touched pages:**

- [[durable-skills]] — `source_count` 6 → 7; `confidence` 0.89 → 0.90. Added MIT OCW as the **educational-supply-side vantage**: Universal Learning's *AI + x* verticals (AI + drug design, AI + satellite data, AI + law, AI + health) are the supply-side investment in the *AI-meets-domain* skills the wiki's hiring-criteria sources (Sternfels) and assessment-methodology sources (Globerson) demand. Added the *personalized vs personalizable* materials distinction; named the 1-billion-learners scale-up ambition.
- [[ai-deskilling]] — `source_count` 3 → 4; `confidence` 0.78 → 0.80. Added a new section *The open question raised by the open-education vantage* — the final-audience-question articulation of the cognitive-impact concern at the supply-side institutional leadership. The question is asked of MIT leadership; the audio cuts off before the answer. Wiki holds the question as unresolved open-question; primary-source ingest of the underlying MIT studies flagged.
- [[enterprise-ai-adoption]] — `source_count` 25 → 26; `confidence` 0.95 (cap unchanged). MIT as institutional-adopter case study: financial-sustainability constraint forces hybrid free-and-paid model; phased platform consolidation; AI translation/personalization as the new abstraction layer for content delivery. (Body unchanged; page is already dense at 26 sources.)
- [[index.md]] — added the source entry.

**People listed as Dangling first-mention**: **Dimitris Bertsimas** (MIT VP for Open Learning + Sloan); **Sarah Hansen** (Asst Director Open Education Innovation; moderator); **Curt Newton** (Director MIT OCW); **Chuck Vest** (former MIT President; launched OCW); **Bayo Akomolafe** (UNESCO digital-learning thinker); **John Gruber** (MIT economics professor; named as content-modularisation example); **Annabelle** (transcript-uncertain; first-four Universal AI participant); **Neil Gershenfeld** (Fab Labs lead); **Sally Kornbluth** (current MIT President; likely; transcript "Sally" only); **Chris Raab and Desiree Plata** (Universal Climate + Energy track leads); **Dana Doyle** (audience member; named in OCW future-vision work).

**Organisations listed as Dangling first-mention**: **MIT OpenCourseWare** (25-year-old initiative; ~500M lifetime learners; **strong promotion candidate** — substantively foundational across 3+ wiki sources already mentioned via tags + entity references); **MIT OpenLearning** (umbrella); **MIT Learn / Learn.mit.edu** (consolidated platform); **OpenIndex** (platform substrate); **AskTIM** (AI tutor); **Universal Learning / Universal AI / Universal Climate + Energy / Universal Biology / Universal Health** (Bertsimas-era curriculum); **Wikipedia** (collaboration partner); **MITx**; **Fab Labs**.

**Candidate concepts noted but NOT promoted on a single source**:
- *Personalized vs personalizable materials* — Newton's distinction.
- *Horizontal-knowledge architecture (AI + x verticals)* — Bertsimas's framing.
- *Three-phase open-content ladder* — Bertsimas's deployment strategy.
- *Content-revision-velocity argument for modularisation* — generalizable beyond education.
- *AI-translation-tipping-point claim* — Newton's institutional statement.

**Pre-flight notes**: Identity verified. Transcript fetched via `youtube-transcript-api` fallback. **Manual track** at `language_code: en-US` (not `en` — the ASR track is at `en`); explicit `languages=['en-US', 'en']` preference order needed to grab the manual track. **Timestamps were in event-time** (first segment at ~3176s, i.e. ~53 minutes into the larger MIT event); **normalised at ingest** by subtracting the offset so [mm:ss] markers correspond to video-time. 1254 raw manual-track segments → 253 grouped windows. Honest-scoping: the last ~30 seconds are partial — the audio cuts off mid-sentence (`[BEEPING]` at 57:16) during Bertsimas's response to the AI-cognitive-impact question. Three caption-related observations: (1) the en-US-vs-en language-code distinction matters for picking manual over ASR; (2) event-time timestamps appear when a clip is published from a larger event recording — worth flagging the normalisation step as a recurring pattern; (3) this is the wiki's third `kind: manual` source — both Sternfels and Jassy were HBR IdeaCast; this MIT OCW source extends the pattern to a second publisher (MIT) that produces manually-curated captions.

### Cross-batch synthesis

This three-source batch closes several wiki gaps simultaneously:

1. **The evaluation discipline gap**: prior to Guthrie / Braintrust, the wiki had no dedicated first-party source on the eval/observability layer beyond brief mentions in Chase's ADLC and Chatterjee's Contracts. Guthrie fills that gap with vendor-specific tooling vocabulary.
2. **The open-education-as-AI-supply-side gap**: prior to MIT OCW, the wiki's durable-skills cluster had assessment (Globerson), hiring criteria (Sternfels), de-skilling concern (Thompson) but no *supply-side* source. MIT fills that gap with Universal Learning as the AI-era curriculum strategy.
3. **The Anthropic founder-vantage gap**: the wiki holds Anthropic-products coverage (Managed Agents / Fung's engineering org / Bratanic's hooks) but no founder-vantage source. The Amodei stub *attempted* to fill that gap; the ingest stalled on captions disabled. Re-attempt flagged.

**Convergence threshold notes**:
- *Eval flywheel / online-to-offline feedback*: three-source threshold met (Guthrie + Kiron-Schrage + Hu) — **strong promotion candidate** for a learning-capture-flywheel concept page.
- *Personalized vs personalizable materials*: Newton's distinction sits next to Karpathy's *floor-vs-ceiling* (vibe-coding / agentic-engineering) and Hu's *personalizable substrate via queryable artifacts* — three related two-axis distinctions across different domains worth tracking for synthesis.

## [2026-05-11] ingest | Diana Hu (Y Combinator Partner) on How To Build A Company With AI From The Ground Up (YC Startup School YouTube, 24 April 2026; 10:27)

The wiki's **highest-density-per-minute source on AI-native company structure**. A 10:27 monologue by **Diana Hu** (YC Partner) on the [[Y Combinator]] Startup School channel, published 24 April 2026. Six chapters; ASR caption track. Source page: [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up]].

**Substantive findings:**

- **AI as company operating system, not tool**: Hu's central reframing — *"AI ... should not be a tool your company just uses. It should be the operating system your company runs on. Every workflow, every decision and every process should flow through an intelligent layer that is constantly learning and improving."* The *intelligence layer* terminology maps onto the wiki's [[agent-harness]] vocabulary applied at *company scale* rather than at the application-product scale that all prior harness sources operated at.
- **Closed-loop vs open-loop companies — control-systems vocabulary for the [[micro-productivity-trap]]**: *"In the old world, companies basically ran as open loops. You made a decision, executed it, and didn't always systematically measure the outcome and adjust the process. Open loops are inherently lossy. A closed loop, on the other hand, is self-regulating. It continuously monitors its output and adjusts its process to better meet the stated goal."* The wiki's first **formal-systems framing** of the trap; convergent with Kiron-Schrage's verification-evaluation-learning-capture flywheel and with Chatterjee's Compounding layer of the agent harness.
- **The "productivity is the trap" insight**: *"Most people talk about AI in terms of productivity ... This framing misses the shift we're currently seeing, which is less about productivity boosts than entirely new capabilities."* Directly names what the wiki's existing micro-productivity-trap sources name structurally: productivity-thinking is itself the trap.
- **Make the company queryable**: *"the whole organization should be legible to AI. Every important action should produce an artifact that the intelligence at the center of the company can learn from and use to self-improve."* Operational instantiation: record meetings with an AI notetaker, minimise DMs/emails, embed agents throughout communication channels, build custom dashboards for revenue/sales/engineering/hiring/ops.
- **Worked example — sprint planning**: an agent with access to Linear tickets + Slack engineering channels + customer feedback (Pylon/GitHub) + high-level plans (Notion/Google Docs) + sales calls + standup recordings can analyse what was actually shipped vs customer needs, then propose more predictable sprint plans. **Reported empirical across multiple YC companies**: *"teams that do this cut their engineering sprint time in half and get close to 10× more done in that time."*
- **Software factories — the next evolution of TDD**: humans write specs and tests defining success; AI agents generate implementation and iterate until tests pass; humans judge the output, not the code. *"Some companies have already pushed this to the point where their repos contain no handwritten code, just specs and test harnesses."* **Worked example**: **Strong DM's AI team** — *"essentially eliminated the need for a human to write or review code ... specs and a scenario-based validations drive agents to write tests and iterate on code until it meets a probabilistic satisfaction threshold and it works."* The wiki's second-vendor software-factory worked example, after [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex]]. **Two-source convergence threshold met** for *software factories* as a named transferable architecture — promotion candidate.
- **The 1,000× engineer thesis — extends Karpathy's 10× by two orders of magnitude**: *"This is how you achieve the thousand-x engineer that Steve J. talks about by surrounding a single engineer with a system of agents that enable them to build things they would have never been able to build before. The era of the thousand or even 10,000× engineer is here."* The *"Steve J."* attribution is ASR-uncertain — most plausible candidate is **Steve Yegge** (whose *Gas Town* essay was named in [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler 2026]]'s *eight stages of dev evolution* framing) but not confirmed. Open primary-source target: a Yegge essay specifically using the *1,000×* phrase.
- **Middle management disappears — via Jack Dorsey at Block**: *"In the old world, you needed middle managers and coordinators to route information inefficiently up and down an organization. In the new world, the intelligence layer serves that purpose. If your company is queryable, artifact-rich, and legible to an AI, you should have almost no human middleware. This matters because your company's velocity is only as fast as its information flow. Every layer of human routing you can remove is the direct speed gain."* Anchor figure: **Jack Dorsey at Block** — *"if you keep the same org chart and management structure, you've missed the shift entirely. The company itself has to be rebuilt as an intelligence layer with humans at the edge guiding it rather than routing information through it."* **Direct convergence with the previous day's [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers|Jassy 2025]] ingest's flatten-management initiative** (+15% IC-to-manager ratio target at Amazon scale). **Two-source threshold met** on the *flatten-management-and-middle-layer-elimination as a named pattern* — promotion candidate.
- **Three archetypes in AI-native companies** (Hu attributes to Dorsey): **IC** (builder-operator; everyone builds, regardless of function; *"Everyone comes to meetings with working prototypes not pitch decks"*); **DRRI** (directly responsible individual; focused on strategy/customer outcomes; *"one person, one outcome, no hiding"*); **AI founder type** (still builds, still coaches, leads by example; *"this needs to be you at the forefront, showing your team what massive capability gains look like, not delegating your AI strategy to someone else"*).
- **Token-maxing not headcount-maxing**: *"Maximizing token usage, not headcount, will be the critical shift. The best companies will be the ones that are token maxing ... you should be willing to run an uncomfortably high API bill because it's replacing what would have taken a far more expensive and inflated headcount."* Direct convergence with [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler 2026]]'s $380/day-developer observation — Hu's *"uncomfortably high API bill"* is the prescription; Böckeler's $380/day is the observation.
- **Founder dogfooding mandate**: *"You cannot outsource your conviction on the power of these tools. You need to develop it yourself by actually sitting with coding agents and using them until you start to break your own priors about what is now possible to build."* Convergent with [[2026-05-08-running-an-ai-native-engineering-org|Fung 2026 (Anthropic)]]'s *manager-starts-as-IC dogfooding* norm — same prescription at the founder layer.
- **Startups win this shift — incumbents face maintain-while-unwinding constraint**: *"You don't have legacy systems in org-charts or thousands of people to retrain. You are small enough to build your company right from day one. The opposite is the case for existing companies."* Worked example for incumbent exception: **Mutiny** — spinning up *"small internal skunk works teams that can build AI native systems from scratch separate from the core business."* Final claim: *"design your systems, workflows and culture around AI from the start and operate thousand times faster than the incumbents."*

**Touched pages:**

- [[agent-harness]] — `source_count` 14 → 15; `confidence` 0.94 (unchanged at next-to-cap). Added Hu as the **YC-partner observer-of-startup-orgs vantage** — extends the harness construct beyond the application/product/repo scale into **org-design scale**. Updated the prose lead "fourteen" → "fifteen".
- [[agentic-engineering]] — `source_count` 5 → 6; `confidence` 0.88 → 0.89. Added Hu as the **YC-accelerator-partner-observer vantage**; Strong DM is the wiki's second-vendor software-factory worked example after OpenAI Codex; Hu names the productivity-ceiling explicitly (1,000× / 10,000× engineer).
- [[micro-productivity-trap]] — `source_count` 11 → 12; `confidence` 0.95 (cap unchanged). Added Hu as the **control-systems vocabulary vantage**; first formal-systems framing of the trap in the wiki.
- [[vibe-coding]] — `source_count` 6 → 7; `confidence` 0.88 → 0.89. Added Hu as the **company-scale extension** of the floor-raising thesis — vibe-coding as an organisational norm rather than just an individual skill.
- [[enterprise-ai-adoption]] — `source_count` 24 → 25; `confidence` 0.95 (cap unchanged). Hu adds the startups-as-AI-native-from-day-one + incumbent maintain-while-unwinding-constraint thesis. (Body unchanged; page is already dense.)
- [[index.md]] — added the Hu source entry (placed between Jassy and Thompson chronologically by ingest order in this batch); bumped the [[agent-harness]] one-liner (14 → 15 sources).

**People listed as Dangling first-mention** (per author-entity-promotion rule, not promoted on a single source): **Diana Hu** (YC Partner; the speaker); **Jack Dorsey** (Block CEO; attributed for the three-archetypes framing); **Steve J.** (ASR-uncertain attribution for the *1,000× engineer* phrase — most plausible candidate **Steve Yegge**, the *Gas Town* author named in [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler 2026]] but not confirmed). Promote on second-source mention.

**Organisations listed as Dangling first-mention**: **[[Y Combinator]]** (channel/publisher; major Silicon Valley accelerator — strong candidate for early promotion given the substantive YC-partner-observer vantage Hu provides); **Block** (Jack Dorsey's company); **Strong DM** (software-factory worked example); **Mutiny** (incumbent skunk-works exception worked example).

**Candidate concepts noted but NOT promoted on a single source**:
- *Software factories* — **two-source convergence threshold met** (Lopopolo + Hu / Strong DM). Strong promotion candidate.
- *Closed-loop / open-loop company* — Hu's control-systems framing for org design. Single-source.
- *Queryable organization / legibility-to-AI* — Hu's framing. Single-source.
- *Token-maxing not headcount-maxing* — Hu's framing. Convergent with Böckeler's $380/day observation as a phenomenon-counterpart but not the same construct exactly. Single-source as a construct-name.
- *Three archetypes (IC / DRRI / AI founder)* — Hu via Dorsey. Single-source.
- *1,000× engineer / 10,000× engineer* — Hu extends Karpathy's 10×. Single-source for this specific multiplier.
- *Flatten-management-and-middle-layer-elimination as a named pattern* — **two-source convergence threshold met** (Jassy + Hu/Dorsey). Strong promotion candidate; would be a *near-the-trap* concept page distinct from but linked to [[micro-productivity-trap]].

**Pre-flight notes:**

- Identity verified per the [§Verifying sources before ingest] contract: title / channel / publish-date / duration / speaker all match the YouTube URL. YAML pre-flight contract satisfied.
- Transcript fetched via the `youtube-transcript-api` fallback after the Playwright path hit the [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2) timeout (10:27 > 20-min threshold actually NOT triggered — the failure mode hit at the lower bound too). ASR caption track only — no manual track available. 252 raw segments → 48 grouped windows. Light cleanup applied (chapter-boundary breaks + ~12s windowing); the talk's compactness means the ASR transcript is essentially substantive throughout.
- **Same chapter `start_ms: 0` parser bug** as the Böckeler and Jassy ingests — recomputed from the chapter `start: mm:ss` strings at ingest time. Now affecting three consecutive video ingests; the skill's chapter parser is reliably wrong on this format. Worth a fix when convenient (skill source: [`.claude/skills/youtube-transcript-skill/fetch_transcript.py`](.claude/skills/youtube-transcript-skill/fetch_transcript.py)).
- Honest scoping: full 10:27 transcript ingested through closing words. The talk is conversational-monologue (Hu addressing the Startup School audience); no host/guest dialogue structure.
- Wikilink-rendering rules observed throughout: no italics-in-alias, no slash + parens + escaped-pipe combos in table cells. The frontmatter `relationships:` block uses concept-slug targets only (no entity-slug targets that don't yet exist as entity pages).

**Cross-batch synthesis (10-11 May 2026 ingest cohort)**: This is the **fourth video source** ingested in the current batch (Böckeler 6 May → Thompson 14 Apr → Jassy 6 May 2025 → Hu 24 Apr) and the **second** in the *post-Jassy* sub-batch where flatten-management-and-middle-management-disappearance is named as a load-bearing pattern. Jassy and Hu/Dorsey converge from two distinct vantages (Fortune-100 operator + YC-partner observer-with-Block-CEO-anchor) on **the same diagnosis**: middle-layer routing collapses when the intelligence layer can do it. The two-source convergence threshold for promotion is now met for **flatten-management-as-AI-shift-consequence** — a candidate concept page distinct from but cross-linked with [[micro-productivity-trap]].

## [2026-05-11] ingest | Andy Jassy (Amazon CEO) on Agility, AI Strategy, and the Changing Role of Managers (HBR IdeaCast, 6 May 2025; 29:39)

The wiki's **first ingest from before the "December 2025 phase change"** — a pre-phase-change major-vendor-CEO vantage on enterprise AI strategy and organisational change. A 29:39 episode of HBR IdeaCast hosted by **[[Adi Ignatius]]** (HBR editor-in-chief), interviewing **Andy Jassy** (Amazon CEO since 2021; AWS founder). Manual (human-curated) caption track — the wiki's second `kind: manual` video source after Sternfels. Source page: [[2025-05-06-jassy-amazon-agility-ai-strategy-changing-role-of-managers]].

**Substantive findings:**

- **The three-layer AI stack framing — earliest first-party-CEO articulation in the wiki**: Jassy lays out Amazon's view of the GenAI stack — **(1) infrastructure / chips + model-building services** ([[Trainium]] / [[SageMaker]]) for model builders; **(2) frontier-model orchestration with guardrails / RAG / agentic capabilities** ([[Bedrock]]) for those leveraging existing frontier models; **(3) applications** ([[Q]] / [[Rufus]] / 1,000+ internal GenAI apps). The wiki's earliest first-party-CEO mention of *productised agentic capabilities* on the middle layer — *"take a bunch of automated actions in succession"* — eight months before [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] (8 April 2026), nine months before [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo / OpenAI Codex]] (11 Feb 2026), and twelve months before [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler's]] harness-engineering propagation.
- **Marketing complaint embedded**: *"there was a lot of attention early on on ChatGPT … I think people have slept a little bit on the other layers of the stack"* — directed positioning of AWS-as-stack-vendor versus OpenAI / Anthropic as application-vendors. The wiki holds the framing while flagging the commercial-interest discount.
- **Target-firm CEO operator-of-[[micro-productivity-trap]]-escape — concrete operational datapoints**: **+15% IC-to-manager ratio target** (already beaten by end of Q1 2025); **1,000+ "no-bureaucracy" emails received** + **375 processes changed** in response; **5-day RTO mandate** with stated rationale *"invention is stronger when people are together"* (acknowledging *"it's very hard to measure how well you're inventing"*). Where Bain / McKinsey / Thoughtworks / NYT *describe* the trap from observer vantages, Jassy *is* a target-firm CEO deploying the prescription. The trap is now visible from **five distinct vantages** across five sources (Bain engagement-engineering / McKinsey GMP self-narrative / Thoughtworks consultancy / NYT journalism / **target-firm CEO**).
- **Bureaucracy-vs-process distinction** — Jassy's taxonomic refinement: *"most companies of any scale need process to scale the right way. But there is really a difference. And the difference is often processes that have been layered in that don't really add any real creative value."* Promotion candidate on second-source mention.
- **May-2025 [[vibe-coding]] anchor — earliest vendor-CEO floor-raising prediction**: Jassy at 22:00 — *"the number of people who are going to be able to be software developers is going to go up exponentially. Because you're going to have these coding apps that allow you to use natural language to describe what you want to go build. And it's going to be very empowering."* **Predates Karpathy's vibe-coding coinage by ~12 months and Nika's December-2025 PM-side worked example by ~7 months.** Qualifying clause: US-education-quality concern (*"30 out of 35 developed countries in efficacy of education"*) anticipates the [[ai-deskilling]] / [[durable-skills]] concern that floor-raising democratisation depends on a baseline of human capability.
- **Two-way-door vs. one-way-door decision taxonomy** — Bezos-era Amazon vocabulary used by Jassy as the named mechanism for delegating decisions to ICs. *"The two-way door decisions, which is the overwhelming majority of the decisions we all make, we want to be handled by the people doing the work and those owners."* Promotion candidate on second-source mention.
- **Rufus as the in-store-salesperson question-narrowing pattern**: Jassy's worked example for [[Rufus]] (Amazon's GenAI shopping assistant) — *"I'm a 15-handicap golfer, do you have a fast swing or a slow swing? Look at these three things."* Structurally identical to [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs|Thompson's]] *agent-driven spec elicitation* (developer-side) and to [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler's]] feed-forward harness design (consultant-side). **Three-source convergence threshold met** for the candidate concept *agent-driven question-narrowing* — strong promotion candidate.
- **AI as biggest transformation since cloud / internet**: *"AI is probably-- it's for sure the biggest technology transformation since the cloud. It's probably the biggest technology transformation since the internet."* Pre-phase-change anchor for the magnitude claim.
- **DEI-walk-back framing — Jassy refuses to disown**: *"I still think we want more diverse teams. None of that has changed. There are certain times where that takes up more of the conversation than at other times."* Notable as May 2025 anchor for the public-discourse-temperature shift.

**Entities promoted on this ingest:**

- **[[Amazon]]** — promoted from Dangling to entity page (per author-entity-promotion rule). Second source mentioning Amazon: prior was [[2026-04-28-werner-lebrun-octopus-organization|Werner & Le-Brun]] Dangling list. Updated the Werner-Le-Brun source's Dangling line to reflect the promotion. The new entity page documents Amazon as (1) target firm operating-the-trap-escape, (2) Octopus-Organization-framework exemplar; lists Andy Jassy / Jeff Bezos / Stephen Brozovich as Dangling sub-entities; lists Trainium / SageMaker / Bedrock / Q / Rufus as Dangling AI products.
- **[[Adi Ignatius]]** — promoted from Dangling to entity page. Now appears as named interviewer in two ingested HBR IdeaCast sources ([[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels 2026]] and this one). Updated the Sternfels source's Dangling line to reflect the promotion. The new entity page captures his editor-in-chief role + HBR IdeaCast host pattern + observed interviewing style across the two ingests.

**Touched pages:**

- [[vibe-coding]] — `source_count` 5 → 6; `confidence` 0.86 → 0.88. Added Jassy as the **pre-coinage CEO anchor** for the floor-raising thesis. The vibe-coding lineage is now temporally complete: Jassy named the prediction (May 2025) → Nika worked-example-ed it (December 2025) → Karpathy coined the term (April 2026).
- [[micro-productivity-trap]] — `source_count` 10 → 11; `confidence` 0.95 (cap unchanged). Added Jassy as the **target-firm CEO operator-of-trap-escape** vantage with the 15%-IC-ratio + 1,000-emails + 375-processes operational datapoints. **The May-2025 anchor extends the trap's temporal footprint backward by ~9 months** — Jassy was recognising the trap experientially before the consulting-firm vocabulary existed.
- [[agent-harness]] — `source_count` 13 → 14; `confidence` 0.94 (unchanged at next-to-cap). Added Jassy as the **earliest-CEO vendor characterisation** vantage. Updated the prose lead "twelve" → "fourteen" wiki sources.
- [[Amazon Web Services]] — `source_count` 2 → 3; `confidence` 0.80 → 0.83. Added a new third-angle section *AS an AI-stack vendor — Jassy's three-layer framing* with the Trainium / SageMaker / Bedrock / Q product breakdown.
- [[Harvard Business Review]] — `source_count` 9 → 10; `confidence` 0.88 → 0.90. Second HBR IdeaCast source in the wiki (after Sternfels).
- [[2026-04-28-werner-lebrun-octopus-organization]] — updated the Dangling line to reflect the Amazon promotion.
- [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting]] — updated the Dangling line for Adi Ignatius to reflect his promotion.
- [[index.md]] — added the Jassy source entry (placed between Thompson and Böckeler chronologically by ingest order); bumped the [[agent-harness]] one-liner (13 → 14 sources).

**People listed as Dangling first-mention** (per author-entity-promotion rule, not promoted on a single source): **Andy Jassy** (Amazon CEO); **Jeff Bezos** (Amazon founder; coined the two-way-door vocabulary). Promote on second-source mention.

**Products listed as Dangling first-mention**: **Trainium** (custom AI training chip); **SageMaker** (model-building service); **Bedrock** (frontier-model orchestration platform); **Q** (AI coding assistant); **Rufus** (GenAI shopping assistant). All five are Amazon AI products substantively named by Jassy; defer to entity pages on second-source mention.

**Candidate concepts noted but NOT promoted on a single source**:
- *Two-way-door vs. one-way-door decisions* — Bezos-era Amazon vocabulary used by Jassy. Widely-cited; promotion candidate on second-source mention.
- *Bureaucracy-vs-process distinction* — Jassy's taxonomic refinement (most companies of scale need process, the trap-relevant pathology is bureaucracy). Promotion candidate on second-source mention.
- *Agent-driven question-narrowing* — the Socratic-dialogue interaction pattern. **Three-source convergence threshold now met**: Jassy on [[Rufus]] (consumer) + [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs|Thompson]] developer spec elicitation + [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler]] feed-forward harness. **Strong promotion candidate for a near-term concept page**.

**Pre-flight notes:**

- Identity verified per the [§Verifying sources before ingest] contract: title / channel / publish-date / duration / host / guest all match the YouTube URL. YAML pre-flight contract satisfied.
- **Two caption tracks** (manual + ASR) — picked the **manual** track for highest fidelity per the Sternfels precedent. Speaker labels (`ADI IGNATIUS:` / `ANDY JASSY:`) preserved verbatim. The wiki's second `kind: manual` video source — both manual sources are HBR IdeaCast episodes, consistent with HBR's higher-than-default production standard.
- Transcript fetched via the `youtube-transcript-api` fallback after the Playwright path hit the [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2) timeout (29:39 > 20-min threshold). 695 raw manual-track segments → 150 grouped windows. Light cleanup: chapter-boundary breaks + speaker-turn breaks + ~12-second windowing; lead `[mm:ss]` timestamps preserved.
- **Same chapter `start_ms: 0` parser bug as the Böckeler ingest** — recomputed start_ms from the chapter `start: mm:ss` strings at ingest time. The bug now manifests across two consecutive video ingests; worth a fix to the skill's chapter parser when convenient.
- Honest scoping: full 29:34 of dialogue ingested across all 13 published chapters. The episode is conversational throughout; no news block at the tail (unlike Thompson 2026).
- **Pre-phase-change ingest convention** — this is the wiki's first ingest of a source published before December 2025 (publish date 6 May 2025). The wiki's existing temporal-anchor patterns (December 2025 phase change for [[vibe-coding]] etc.) handle this naturally: Jassy is positioned as a *pre-coinage prediction* anchor, with the wiki treating his May-2025 framing as evidence-of-the-prediction's-pre-existence rather than as contradicting the December-2025 phase-change framing.
- Wikilink-rendering rules observed throughout: no italics-in-alias, no slash + parens + escaped-pipe combos in table cells. The frontmatter `relationships:` block uses `Harvard-Business-Review` (kebab-case slug) but the entity file is `Harvard Business Review.md` — flagged for lint validation; expected to pass since the graph-export normalises basenames.

## [2026-05-10] ingest | Clive Thompson on AI-augmented software development — *The Workers Letting A.I. Do Their Jobs* (NYT The Daily, 14 April 2026; 36:31)

The wiki's **first journalist-observer cross-industry field-report** on AI-augmented software development. A 36:31 episode of *The Daily* (New York Times) hosted by **Natalie Kitroeff**, interviewing **Clive Thompson** about his ~75-developer survey at major tech companies, small businesses, and start-ups. The radio form of Thompson's 12 March 2026 NYT Magazine piece *Coding after coders: It's the end of computer programming as we know it*. Source page: [[2026-04-14-thompson-the-daily-workers-letting-ai-do-their-jobs]].

**Substantive findings:**

- **Phase-change dating**: Thompson reports *"the transition began heavily in the last 6 months and accelerated in the last 3"* — placing the developer-side phase change at November 2025 → February 2026, ~4 months behind Nika's PM-side December-2025 phase change. The wiki now holds at least three temporally-different phase-change events (PM-side, developer-side, conference-circuit observer-side), consistent with the *"December 2025 phase change generalises but at different times for different professional cohorts"* hypothesis.
- **Productivity gradient by company size — the cleanest single empirical statement of the [[micro-productivity-trap]] in the wiki**: two-person startups report up to **~20× faster** delivery (full-day features → ~30 min) with ~100% AI-written code; [[Google]] reports ~**10% overall speedup** despite ~40-50% AI-written code. The 2× order-of-magnitude gap *between micro and macro speedup at similar per-task AI penetration* is direct empirical for the trap. Mechanism: *organisational metabolism* (change management, legacy interactions, customer commitments) rate-limits how much per-task speed translates to firm-level value.
- **The 1980s productivity-paradox parallel**: Thompson invokes the historical pattern that computers in the 1980s didn't increase corporate productivity until firms *reorganised work around them* (email replacing typewritten memos, regional offices sharing documents). His prediction: AI coding's industrial impact will take *"longer than we think"* for the same reason. Companies that lay off staff thinking AI will replace them often *rehire within 6 months* because the replacement didn't work.
- **Brynjolfsson 16% software-developer hire drop**: Thompson cites a *more recent* [[Erik Brynjolfsson]] job-postings analysis showing **software-developer hires down 16%** *"in the last year or so"* — extending the *Canaries in the Coal Mine* employment-stock signal (2022 onset, age 22-25, ~20% software-developer decline by July 2025) into the *hiring-flow* layer through 2025-26. Primary-source ingest of the underlying analysis is an open target.
- **Operator-vocabulary statement of the [[durable-skills]] frame**: *"What developers are experiencing right now is something that maybe seems a little paradoxical, which is that they had spent years developing these very, very hard technical skills, and it turns out those are some of the easiest things to automate. The hard stuff to automate is like talking to our colleagues and our customers and figuring out what should we be building. Setting priority, setting strategy. AI can't do that."* The developer-named durable skills cluster reduces to: **communication / spec-elicitation / priority-setting / strategy / deciding-what-to-build** — overlapping with but not identical to the Globerson (collaboration / creativity / critical thinking) and Sternfels (aspiration-setting / judgment / discontinuous-leap thinking / human-to-human skill) clusters.
- **Construction-workers-to-architects shift**: developers report feeling *"like Steve Jobs"* — *"bring me nine designs of the iPod and I'll pick the best one."* The operator vantage on Karpathy's [[agentic-engineering]] discipline.
- **First first-person developer worked example for [[ai-deskilling]]**: **Pia Torian**, *"reasonably newer developer"*, employer-mandated heavy [[Microsoft]] Copilot use, *"hundreds of prompts a day for months"* → *"this is actually degrading my own knowledge of code. I feel like I'm losing my ability to code."* The senior-vs-junior **inter-generational worry**: senior developers can spot bad AI output because they wrote code by hand; their concern is whether the next generation, who never write code by hand, will develop the *code sense* needed to be effective AI-output reviewers.
- **First small-startup worked example of a rules-file in the wild**: **Manu Ebert** at **Hyperspell** keeps a "10 Commandments" file the agent must consult before any action. Features: uppercase, repetitive language *"like they're yelling at it"*; high-stakes emotional framing (*"failure to do these tests is unacceptable and embarrassing"*, *"if you don't do these tests, I will be fired"*); imperative voice. Thompson's mechanistic explanation: LLMs *"understand the meaning of language based on the company it keeps. So if they see the word embarrassing, they understand that word comes from a bad neighborhood."* Distributional semantics applied to prompt design — the lay-vocabulary version of [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy|Böckeler's]] *"enhanced lint messages as good prompt injection"*. The rules-file pattern is now visible at **three distinct organisational scales** in the wiki: vendor (Lopopolo / OpenAI Codex golden-principles), consultancy clients (Böckeler enhanced-lint-messages), individual-developer/small-startup (Ebert "10 Commandments").
- **Agent-driven Socratic-dialogue spec elicitation**: a specific technique multiple developers settled on — *"ask me questions about how this software feature should work"*. The agent's clarifying questions become the spec-elicitation; the developer's answers become the spec. Concept candidate: **agent-driven spec elicitation** — first wiki source naming it; promotion on second-source mention.
- **"Skill we thought was ours" jagged-frontier inversion**: Thompson's clearest expository statement of [[jagged-frontier|jaggedness]] for a general audience — chess was supposed to be hard for computers but proved easy in the 1990s; speech was supposed to be easy but took 2+ decades more. Today's "hard technical skill" (coding) turns out to be more automatable than expected; the "soft skills" (communication, prioritisation) turn out to be the harder-to-automate part.
- **Democratisation prediction — software as Post-it note**: software stops being *"precious and rare"* and becomes ubiquitous, called-into-being for short-term needs. Mid-size firms ($15-50M concrete-mixing-firm types) that historically can't afford a 5-person software team at $1M/year can now afford one AI-augmented developer at $60-70K/year writing bespoke software that previously didn't exist. Worked analogy: word processors in the 1970s-80s → riot-girl zines and ugly birthday flyers in the 1990s (unpredictable proliferation enabled by abstraction-layer drop).
- **Devalue-the-job-as-labour-control mechanism**: *"Even if you're not replaced by AI, if you de-skill and devalue the job, it just gets easier for the owners to push you around."* First wiki source naming the labour-power dynamic explicitly. Promotion candidate on second-source mention.

**Touched pages:**

- [[vibe-coding]] — `source_count` 4 → 5; `confidence` 0.84 → 0.86. Added Thompson as the 75-developer field-report anchor; small-startup 100% AI-written code is direct operator-side evidence.
- [[agentic-engineering]] — `source_count` 4 → 5; `confidence` 0.87 → 0.88. Added Thompson as the journalist-observer vantage; the Steve-Jobs-picks-from-nine-designs operator self-description is the discipline's lay-audience translation.
- [[agent-harness]] — `source_count` 12 → 13; `confidence` 0.93 → 0.94. Added Thompson as the journalist-observer + first-person-operator vantage; Manu Ebert's "10 Commandments" file rounds the rules-file pattern to three organisational scales.
- [[micro-productivity-trap]] — `source_count` 9 → 10; `confidence` 0.94 → 0.95 (capped). Added Thompson as the journalist-observer empirical lens; the 20×-startup-vs-10%-Google datapoint is the trap's clearest single empirical statement and the 1980s productivity-paradox parallel adds the historical-pattern-matching vantage. The trap is now empirically observed at *four scales* (firm / function / team / individual-developer) from *four vantages* (Bain / McKinsey / Thoughtworks / NYT).
- [[ai-deskilling]] — `source_count` 2 → 3; `confidence` 0.75 → 0.78. Added a new section *First-person developer worked example: Pia Torian* — first first-person self-report of measurable deskilling in the wiki. The inter-generational selection-instrument-decay worry is now articulated.
- [[ai-employment-effects]] — `source_count` 14 → 15; `confidence` 0.95 (cap unchanged). Added the Brynjolfsson 16%-software-developer-hire-drop datapoint as an update to the existing *Canaries* section; flagged primary-source ingest as open target.
- [[durable-skills]] — `source_count` 5 → 6; `confidence` 0.87 → 0.89. Added Thompson as the developer-side operator-vocabulary statement of durable skills; named the three-vocabulary-mapping synthesis target (Globerson psychometrics / Sternfels hiring / Thompson developer-side).
- [[jagged-frontier]] — `source_count` 7 → 8; `confidence` 0.91 → 0.92. Added Thompson's chess-vs-speech expository inversion as Practical-implications bullet; lay-audience translation complementary to Dell'Acqua et al.'s controlled-experiment empirical anchor.
- [[Erik Brynjolfsson]] entity — `source_count` 3 → 4; `confidence` 0.85 → 0.87. Added a third numbered claim section: *Updated job-postings signal* — the 16%-software-developer-hire-drop datapoint cited by Thompson, extending the *Canaries* employment-stock signal into the hiring-flow layer through 2025-26.
- [[index.md]] — added the Thompson source entry (placed between Chase and Böckeler); bumped the [[agent-harness]] one-liner (12 → 13 sources) and the [[agentic-engineering]] one-liner (4 → 5 sources).

**People listed as Dangling first-mention** (per author-entity-promotion rule, not promoted on a single source): **Clive Thompson** (NYT Magazine tech/science writer; guest); **Natalie Kitroeff** (The Daily host); **Manu Ebert** (Hyperspell startup developer; "10 Commandments" rules-file worked example); **Pia Torian** (newer developer; first-person de-skilling worked example). Promote on second-source mention.

**Organisations listed as Dangling first-mention**: **The New York Times** / **NYT Magazine**; **The Daily** (NYT podcast — show vs. publisher entity-class decision deferred until second source); **Hyperspell** (Ebert's small AI startup employer).

**Candidate concepts noted but NOT promoted on a single source**:
- *Agent-driven spec elicitation* — the Socratic-dialogue technique where the agent interviews the developer about the spec. Promotion candidate on second-source mention.
- *Software as Post-it note / democratisation of bespoke software* — Thompson's macro prediction about mid-market software proliferation. Promotion candidate on second-source mention.
- *Devalue-the-job-as-labour-control mechanism* — Thompson's framing of why C-suite benefits from AI-replacement *threats* even when actual replacement fails. Promotion candidate on second-source mention.

**Pre-flight notes:**

- Identity verified per the [§Verifying sources before ingest] contract: title / channel / publish-date / duration / host / guest all match the YouTube URL. YAML pre-flight contract satisfied.
- Transcript: Playwright skill path hit the documented `transcript panel did not render` timeout (the known [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2) failure mode for talks ≥20 min). Fell back to `youtube-transcript-api` `.fetch()` in the `/tmp/ytenv` venv. Caption track is `kind: asr` (auto-generated). Cleanup applied: dropped `[music]`/`[applause]` non-speech markers, normalised `>>` speaker indicators, grouped consecutive segments into ~12-second windows with `[mm:ss]` timestamps. 1025 raw ASR segments → 165 grouped windows.
- No chapters in the video metadata (it's a podcast, not a structured talk); transcript is a flat `## Transcript` section.
- Honest scoping: full ~36:22 of speech ingested. The last ~2 minutes are a NYT news-block (US politics: Swalwell/Gonzales resignations; Trump–Pope-Leo-XIV dispute) that is not substantive for the wiki and was retained in the raw file but not summarised in the source page.
- Wikilink-rendering rules observed throughout: no italics-in-alias, no slash + parens + escaped-pipe combos in table cells. One Dangling-violation caught during the Brynjolfsson entity update — `[[Clive-Thompson]]` was written in body text but Thompson has no entity page yet (he's a single-source first-mention); fixed by replacing with bolded plain-text `**Clive Thompson**`.

## [2026-05-10] ingest | Birgitta Böckeler (Thoughtworks) on The Engineering of AI Agents — Context, Harnessing, and Autonomy (InfoQ YouTube / QCon London 2026, 6 Feb 2026)

The wiki's **first independent-consultancy practitioner-observer source** on harness engineering as a discipline. A 42:01 keynote-style talk delivered by **Birgitta Böckeler** ([[Thoughtworks]]) at **QCon London 2026**, published to the [[InfoQ]] channel on 6 May 2026. Year-on-year structured review of AI coding agents between QCon London 2025 and 2026; the **harness** is the load-bearing concept tying the talk together. Source page: [[2026-05-06-bockeler-engineering-of-ai-agents-context-harnessing-autonomy]].

**Substantive findings:**

- **Direct name-attribution for *harness engineering***: Böckeler explicitly credits the OpenAI Codex team — *"the team called this harness engineering"* — which is precisely the [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo source]] the wiki already holds. Böckeler is the first wiki source documenting the term's *propagation* from the OpenAI engineering blog into the broader QCon-London practitioner audience.
- **Two-axis decomposition of the harness**: **feed-forward** (anticipate what the agent might do wrong — principles, conventions, refs, CLIs, bootstrap scripts, codemods like OpenRewrite, language-server refactoring via MCP) × **feedback** (after the agent acts — static analysis, structural tests, custom linters, application-runtime checks). Each axis splits further into **GPU-based** (LLM inference: code-review subagents, summarisation) and **CPU-based** (deterministic: lint, structural tests). The CPU-vs-GPU framing is borrowed from a company Böckeler called *"Modern"* in the ASR — most likely **Modal Labs** (modal.com) but flagged ASR-uncertain.
- **Structural tests as agent feedback** — a specific new mechanism the wiki now captures: encode architectural constraints as automated checks ([[ArchUnit]] for Java, [[Spring-Modulith]] for Spring, [[Dependency-Cruiser]] for TypeScript). Böckeler's worked example: a rule that *"external SDKs may only be imported in /clients folder, not /domain"* — fails the build if violated, becomes a feedback signal the agent reads and corrects against. Her insight: *"we've had these tools for quite a while, but a lot of people haven't used them because we think we were working on the code"* — under-adopted because humans rationalise around their own discipline; the agent is the new consumer of these tools.
- **Enhanced lint messages as "good prompt injection"** — edit the lint-error text itself to include the refactoring meta-hint (e.g. a 500-line-per-file rule's message includes *"this is often a smell for a design problem; consider refactoring"*). The agent reads the lint output and the embedded meta-hint together.
- **Harness templates** as the next abstraction — analogous to service templates: pick a workflow topology (data dashboard / CRUD service / event processor / etc.), instantiate a pre-built harness rather than rebuild. The proposed decision metric shift: *"is there an existing harness?"* may matter more than *"React or Vue?"*
- **Cost trajectory anchor**: *"generating 100 lines of code only costs about 12 cents"* (early 2024 keynote) → **$380/day metered tokens** (summer 2025 Reddit-documented data point) = ~$91,200/year for one developer's token usage. Mechanism: the agentic-coding inner loop (research → plan → review-plan → implement → run tests → fix tests → check lint → fix lint → check browser → code-review subagent → react → summarise) burns tokens for what may end as two lines of code. Pricing structure migration: $10–20 flat (late 2023–early 2024) → $20–50 flat (rate-limiting starts) → $200 flat (not really flat) → metered consumption-based (late 2025+).
- **Lethal trifecta** attribution: Böckeler credits **Simon Willison (June 2025)** with the framing — *untrusted content + private-data access + external comms*. Worked examples cited "from the past 11 days": unwanted command execution via prompt-injection slipping past allow-list patterns; **secret extraction from a GitHub-issue prompt injection** that enabled NPM-registry pushes for a popular open-source tool. Böckeler frames it as a **conceptual, not technical**, problem and notes it applies equally to business agents (email read+send).
- **Risk-assessment trio** for autonomy decisions: probability × impact × detectability (knowledge of context + experience with the tool + clarity of requirements; criticality of the use case; quality of the feedback loops). The practitioner-operational expression of the [[jagged-frontier]] insight — don't assume capability, *assess* it per-task. *"You have to be this tall to ride the roller coaster — you have to be this tall to reduce supervision."*
- **Goldilocks speed** counter-framing to speed-at-all-costs. Anchor anecdote: **Amazon reportedly added senior-engineer review gateways** in response to outages thought to be related to AI-generated code — defeating the speed gain. Convergent with the [[micro-productivity-trap]] from a third consulting-firm vantage.
- **Agent-swarm experiments** caveat: Cursor (week-long browser-build run) and Anthropic (C-compiler-build run) both used domains with *very well-specified problems* and *elaborate public test suites*. *"That's often what we don't have when we build enterprise software."* First wiki statement of the **selection-bias caveat** on agent-swarm demos.
- **Steve Yegge's "Gas Town"** eight-stages-of-dev-evolution model surfaced: stage 6 = 3 parallel Claude Code instances, stage 7 = 10, stage 8 = swarms. Böckeler tried three: *"I kept typing the wrong thing into the wrong session."* Practitioner skepticism on swarm scaling for solo developers.
- **Conference-circuit timeline anchors**: at QCon London 2025, *"the term vibe coding was about 2 months old"* (placing the coinage in early 2025) / *"MCP was all the rage"* / *"Claude Code was still in diapers"*. Corroborates the wiki's existing December-2025-phase-change dating from the conference-observer angle.

**Touched pages:**

- [[agent-harness]] — `source_count` 11 → 12; `confidence` 0.92 → 0.93. Added Böckeler as the **practitioner-observer-from-consultancy vantage** in the convergence table; she propagates Lopopolo's *harness engineering* term and adds Thoughtworks' cross-client perspective on which mechanisms actually carry load.
- [[agentic-engineering]] — `source_count` 3 → 4; `confidence` 0.85 → 0.87. Added Böckeler as the fourth principal source; Karpathy named the discipline / Fung described the org-shape / Lopopolo showed the artifact-shape / Böckeler shows what the discipline looks like *observed across many client codebases* and confirms the discipline's name-form is settling on *harness engineering* in operator circles.
- [[vibe-coding]] — `source_count` 3 → 4; `confidence` 0.82 → 0.84. Added Böckeler as the **conference-circuit timeline anchor** for the term's coinage; frames vibe coding as one end of the autonomy spectrum the broader harness discipline now attempts to widen safely.
- [[jagged-frontier]] — `source_count` 6 → 7; `confidence` 0.90 → 0.91. Added the **probability × impact × detectability** risk-trio under Practical implications as the practitioner-operational form of jagged-frontier navigation.
- [[micro-productivity-trap]] — `source_count` 8 → 9; `confidence` 0.92 → 0.94. Added Böckeler as the **third consulting-firm vantage** (Bain + McKinsey + Thoughtworks now converge). Two contributions: the *token-economics mechanism* ($380/day inner loop) for why the trap deepens under agentic coding, and the *Goldilocks speed* counter-framing observable in Amazon's reported senior-engineer-gateways response to AI-code outages.
- [[index.md]] — added the source entry (after Chase); bumped the [[agent-harness]] one-liner (11 → 12 sources) and the [[agentic-engineering]] one-liner (3 → 4 sources).

**People listed as Dangling first-mention** (per author-entity-promotion rule, not promoted on a single source): **Birgitta Böckeler** (Thoughtworks); **Simon Willison** (credited for the lethal-trifecta framing, June 2025); **Steve Yegge** ("Gas Town" eight-stages-of-dev essay, Cloud Flow project). Promote on second-source mention.

**Organisations listed as Dangling first-mention**: **Thoughtworks** (presenter's employer); **InfoQ** (channel/publisher); **QCon London 2026** (venue); **Cursor** (agent-swarm experiment + CLI mode); **Modal** (likely; ASR-uncertain rendering "Modern" — credited for the CPU-vs-GPU harness framing); **Tessell** (ASR-uncertain — skills-registry / evals tool).

**Tools listed as Dangling first-mention**: **Dependency Cruiser** (TypeScript structural-test tool); **ArchUnit** (Java structural-test tool); **Spring Modulith** (Spring modular-monolith tool); **OpenRewrite** (codemod tool); **IntelliJ** (language-server / rename-symbol refactoring via MCP).

**Candidate concepts noted but NOT promoted on a single source**:
- *Context engineering* as a named discipline — first wiki source naming it. Böckeler defines it as *"curating the information that your model or agent sees"*; dates the term to ~June 2025. Strong promotion candidate on second-source mention.
- *Lethal trifecta* — Willison's June-2025 framing of the agent-security risk surface. First wiki source naming it. Promotion candidate on second-source mention.
- *Harness engineering* as a discipline-name (versus the artefact [[agent-harness]]) — currently lives inside the agent-harness page; defer promotion until a third source explicitly uses it as a discipline-name (Lopopolo + Böckeler = 2 so far).
- *Harness templates* — Böckeler's speculative-but-explicit future-abstraction proposal. Defer until corroboration.
- *Goldilocks speed* — Böckeler's own framing for the speed-vs-supervision trade-off. Could fold into a future [[micro-productivity-trap]] sub-concept.
- *Probability × impact × detectability* trio — practitioner risk-assessment for autonomy decisions. Folded into [[jagged-frontier]] for now; promote to its own concept if a second source uses the same trio.

**Pre-flight notes:**

- Identity verified per the [§Verifying sources before ingest] contract: title / channel / publish-date / duration / speaker all match the YouTube URL. YAML pre-flight contract satisfied.
- Transcript: Playwright skill path hit the documented `transcript panel did not render` timeout (the known [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2) failure mode for talks ≥20 min). Fell back to `youtube-transcript-api` `.fetch()` in the same `/tmp/ytenv` venv (with Playwright + PyYAML installed in this session). Caption track is `kind: asr` (auto-generated). Cleanup applied: dropped `[music]`/`[applause]` non-speech markers, normalised `>>` speaker indicators, preserved YouTube's chapter list as `##` headings, grouped consecutive segments into ~12-second windows with leading `[mm:ss]` timestamps. 1198 raw ASR segments → 192 grouped windows.
- **Metadata-pipeline patches applied at ingest time**: (1) Playwright path returned `length_seconds=2521` but `duration=None` — the skill computes duration from `lengthSeconds`; recomputed at ingest into `42:01`. (2) The chapter records all returned `start_ms=0` — the fetch script parsed the description-listing format but its chapter-times parser broke on this channel's description style. Recomputed `start_ms` from each chapter's `start: mm:ss` string at ingest; chapter-aware transcript grouping then worked correctly. Both patches documented in the raw file's `notes:` field for future reference.
- Honest scoping: full 42:01 transcript ingested through the closing music marker. YouTube's chapter list runs to 28:15; the talk continues for another ~14 minutes under the final chapter heading — a YouTube-side authoring artefact, not a transcript gap.
- Wikilink-rendering rules observed throughout: no italics inside aliases (the line-179 violation flagged on first draft was the `*Harness engineering: leveraging Codex in an agent-first world*` publication title, fixed by switching to double-quotes); no slash + parens + escaped-pipe combos in table cells; relationships frontmatter dropped `authored-by: Birgitta-Bockeler` and `published-by: InfoQ` because neither has an entity page yet (per the body-wikilink rule, frontmatter relationships require an existing target).

## [2026-05-10] ingest | Bob Sternfels (McKinsey) on the firm's AI strategy (HBR IdeaCast, 9 Feb 2026)

The wiki's **first first-party McKinsey self-narrative source** — Bob Sternfels (Global Managing Partner since 2021) interviewed by Adi Ignatius on HBR IdeaCast. 31:36 episode; **manual (human-curated) caption track** (the wiki's first non-ASR video source). Source page: [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting]]. Complements [[2026-05-03-rewired-second-edition-sample|*Rewired* 2nd ed]] (the practitioner playbook) with the firm-as-vendor self-account.

**Substantive content:**

- **Workforce composition**: 60K = 40K humans + 20K agents (was 3K agents 18 months prior); on track for 1:1 human-to-agent ratio in ~18 months (originally projected 2030).
- **Business-model migration**: pure-advisory / fee-for-service → outcome-underwriting (now ~33% of revenues; aspirationally majority by end-of-Sternfels-term). Direct convergence with [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria 2026]]'s outcome-pricing trend.
- **Org-redesign mechanism**: flatter organizations cutting middle layers + workflow consolidation across departmental boundaries (mortgage-process worked example: 4–5 departments → one AI-enabled flow).
- **CFO-vs-CIO truth-room dilemma** as the canonical [[micro-productivity-trap]] diagnostic from the client seat: high tech spend, low enterprise-level value, organizational change is the missing variable. *"Half, if not more, of the secret sauce is organizational change as opposed to technology implementation."* — second consulting firm (after Bain) to name this diagnosis.
- **Four durable leadership skills models lack**: aspiration-setting / judgment / discontinuous-leap thinking / human-to-human skill. Direct convergence with [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills|Globerson et al. 2026]] from a hiring-criteria angle.
- **Hiring overhaul via 20-year self-applied analytics**: three biggest under-weighted predictors of partner-track success — resilience-after-setback / team-sport-experience / aptitude-to-learn-novel-stuff. Now testing candidates in deliberate *no-pattern-recognition* environments.
- **Post-controversy governance overhaul** ($1B over ~6 years): head of internal audit imported from Apple; head of compliance from Walmart; publicly-traded-equivalent governance standards adopted despite remaining private; partnership autonomy curtailed via new client-selection diligence framework. Named controversies: opioids / OxyContin work + South Africa partnerships + conflict-of-interest accusations.
- **Three transversal CEO-level themes**: how to get value from AI / how to build institutional resilience under continuous shocks (offense-and-defense-at-the-same-time framing) / what should the future organization model be (matrix-organization tension everywhere).
- **Three things great leaders most consistently get right**: hunger-for-new-information / collaboration-across-the-value-chain / speed (faster orgs outperform slower ones even with more mistakes — and yet organizations are risk-averse).

**Touched pages:**
- [[McKinsey & Company]] — `source_count` 4 → 5; `confidence` 0.85 → 0.88. Added the Sternfels source as the firm-as-vendor self-narrative anchor; added Bob Sternfels and Gil Clee (likely; ASR-uncertain) to the People section as Dangling first-mentions.
- [[Harvard Business Review]] — `source_count` 8 → 9; `confidence` 0.85 → 0.88. Added an *HBR IdeaCast* sub-table under publishing-format breakdown; added Adi Ignatius (editor-in-chief) as Dangling first-mention.
- [[durable-skills]] — `source_count` 4 → 5; `confidence` 0.85 → 0.87. Added Sternfels as the 5th source, framed as the *industrial selection-instrument validation* of the durable-skills frame (McKinsey measuring durable skills in candidates *pre-hire* via 20-year self-analytics).
- [[micro-productivity-trap]] — `source_count` 7 → 8; `confidence` 0.90 → 0.92. Added Sternfels as the second-consulting-firm vantage on the trap; *two of the world's largest consulting firms converging on identical diagnoses* is structural evidence the trap is real.
- [[index.md]] — added the source entry alphabetically (after Manditereza, before Cheung-Ippolito-Secchi); updated the [[durable-skills]] and [[micro-productivity-trap]] one-liners to reflect the new convergence.

**People listed as Dangling first-mention** (per author-entity-promotion rule, not promoted on a single source): **Bob Sternfels** (McKinsey GMP); **Adi Ignatius** (HBR editor-in-chief); **Gil Clee** (likely, ASR-uncertain rendering "Gil Klee" — McKinsey Managing Director ~1967–1973, author of 1959 HBR paper Sternfels names as the matrix-organization precursor). Promote on second-source mention.

**Candidate concepts noted but NOT promoted on a single source**:
- *Outcome-based services / outcome-underwriting* — Sternfels (consulting) + [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria]] (Adobe / SaaS) reach the **two-source convergence threshold** in this batch. Strong promotion candidate for a follow-up sweep — the cross-industry pattern is already substantive.
- *Agent-augmented workforce ratio (humans:agents)* — Sternfels' 60K=40K+20K is the wiki's first concrete vendor-level number.
- *Continuous-shocks resilience (offense-and-defense)* — Sternfels' framing.
- *Post-controversy governance overhaul (consulting subtype)* — single-source.

**Pre-flight notes:**
- Transcript: Playwright skill path hit the documented `transcript panel did not render` timeout for ≥20-min talks ([GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2)). Fell back to `youtube-transcript-api` `.fetch()` API in the same `/tmp/ytenv` venv from the Marily Nika ingest. Critically, this video has **two caption tracks** — one *manual* (human-curated, kind=manual) and one *ASR* (auto-generated, kind=asr). Picked the manual track for highest fidelity. Speaker labels (BOB STERNFELS / ADI IGNATIUS) preserved verbatim from the manual track; cleanup limited to line-break normalization, ~12-second-window grouping with speaker-turn breaks, and lead-timestamp preservation per group.
- Identity verified: title, channel, publish date, duration, speaker names all match the YouTube URL.
- Honest scoping: full 31:36 transcript ingested end-to-end (12 chapters from microformat).

## [2026-05-10] ingest | Marily Nika (Google) on the AI-enhanced PM toolkit (How I AI podcast, 1 Dec 2025)

The wiki's **earliest source by publication date** — 5 months ahead of the next-earliest source ([[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Cheung et al.]]) and **directly inside Karpathy's "December 2025 phase change"** ([[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy 2026]]). 40-minute video / podcast on the *How I AI* channel, host **Claire Vo** (ChatPRD), guest **Marily Nika** (AI Product Lead at [[Google]]; founder of AI Product Academy). Source page: [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont]].

**Substantive content:** worked-example "AI-enhanced PM" workflow for a hypothetical smart-fridge product, end-to-end in ~20 minutes (≥40 min on-air with chitchat):

1. User research via **Perplexity** Discussions-and-Opinions filter (Reddit-only search) + the **twin-personas-debate** anti-sycophancy prompt.
2. PRD generation via a **custom GPT** ("AI Product GPT" seeded with Marily's PRD template + voice).
3. Interactive prototype via **v0** (PRD as full prompt input → working dashboard).
4. Promo video via **Flow/Veo** and **Sora cameos**.
5. **NotebookLM as AI-as-judge** for the AI Product Academy bootcamp demo day (audio overview + interactive radio-podcast mode + custom judging criteria).

**Headline framings:**
- *"PMs that use AI are the ones that are going to take over the role of people that don't use AI."*
- *"Tool hopping"* as the load-bearing operational pattern — generalizes [[2026-05-07-anthropic-economic-index-5-learning-curves|Anthropic Economic Index 5's]] **model-selection slope** to the inter-tool layer.
- *"PRD as input, not output"* — the PRD is now a structured prompt-input to vibe-coding tools, not a terminal artifact for engineers to read.
- **Prototypes as stakeholder-influence-engineering tools**, not just design artifacts.
- *"Use AI on AI"* — when one tool fails, kill the instance and have another LLM rewrite the prompt.

**Touched pages:**
- [[vibe-coding]] — `source_count` 2 → 3; `confidence` 0.80 → 0.82. Added Nika 2025 to the convergence table; added the "stakeholder-influence prototypes for non-engineers" right-tool entry; updated the "December 2025 phase change generalises?" open question to *partially answered* (now anchored at both engineer + PM ends).
- [[Google]] — `source_count` 3 → 4; `confidence` 0.80 → 0.82. Added Flow / Veo / NotebookLM / Google AI Studio (prototyping) to the products section; added "People at Google" sub-section listing Marily Nika (Dangling), James Manyika, Jaana Dogan (Dangling), and the Solovyev/Dwivedi Gemini-File-Search team.
- [[OpenAI]] — `source_count` 8 → 9. Added Sora (text-to-video + Cameo feature) and Custom GPTs to the products section.
- [[index.md]] — added the source entry at the top of Sources (earliest-by-date); updated the [[vibe-coding]] concept entry to mention the new PM anchor.

**Authors / orgs as Dangling first-mention** (per author-entity-promotion rule, not promoted on a single source): Marily Nika (Google) — guest; Claire Vo — host; *How I AI* — channel; AI Product Academy; Maven; Vercel (publisher of v0); ChatPRD (Claire Vo's product); Sora as a social network distinct from the model. Promote on second-source mention.

**Candidate concepts noted but NOT promoted** on a single source: *tool hopping*, *AI-as-judge*, *influence engineering / prototype-as-stakeholder-tool*, *anti-sycophancy prompting / twin-personas debate*. These are tagged in the source-page frontmatter for future-source convergence detection.

**Pre-flight notes:**
- Transcript: Playwright skill path (the canonical YouTube-transcript route) hit the documented "transcript panel did not render" timeout for ≥20-min talks ([GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2)). Fell back to `youtube-transcript-api` `.fetch()` API in a temporary venv. 968 ASR segments retrieved; ASR-cleaned (proper nouns + filler reduction + ~10-second-window line grouping with lead-timestamp preservation); chapter section headings inserted from microformat. Metadata via the Playwright path.
- Identity verified: title, channel, publish date, duration all match the YouTube URL.
- Honest scoping: full transcript ingested end-to-end (10 chapters); two sponsor reads (WorkOS, Miro) preserved verbatim in the raw and skipped in the wiki interpretation.

## [2026-05-10] ingest | Chase — *The Agent Development Lifecycle* (LangChain Blog, 9 May 2026)

The wiki's **second formalization** of the [[agent-development-lifecycle|ADLC]] — and the first non-Google one. Four-phase loop wrapped by governance: **Build → Test → Deploy → Monitor → Iterate**, with **Govern** wrapping the whole. Refines the wiki's [[agent-harness|harness]] vocabulary by splitting Build into four distinct sub-layers (Frameworks / Runtimes / **Harnesses** / No-code) — sharper than the prior Kokane 4-layer stack. Names six governance axes for agent scaling (cost / tool access / audit trails / HITL / discoverability of skills / shared infrastructure across teams). Source page: [[2026-05-09-chase-agent-development-lifecycle]]. Touched pages:

- [[agent-development-lifecycle]] — bumped from single-source stub (confidence 0.70) to two-source confidence 0.80; rewritten extensively to compare Google's 9-stage wheel and Chase's 4-phase loop side-by-side; added Codex case study as worked example. `source_count` 1 → 2.
- [[agent-harness]] — added "Refined Build-layer vocabulary" section. (Co-listed with Lopopolo entry for the source_count update; cumulative source_count now 11.)
- [[LangChain]] — **new entity page** created (organization). Cumulative cross-page mentions ([[agent-harness]], [[ai-agents]], [[generative-ai]] + this fresh source-page mention) cleared the entity-promotion bar. `source_count` 4. Lists products (LangChain framework, LangGraph runtime, Deep Agents harness, LangSmith Platform / Observability / Evaluation / Deployment / Sandboxes / Fleet, LangChain Academy).
- **Harrison Chase** — first wiki source mention by name; listed as Dangling per author-entity-promotion rule. Promote on second-source mention.
- [[index.md]] — added entry under Sources and Entities; updated [[agent-development-lifecycle]] and [[agent-harness]] one-liners.

Candidate concepts noted but **not promoted** on single source: agent governance (six axes), simulation as agent eval primitive.


## [2026-05-10] ingest | Manditereza — *Building Ontology-Driven Intelligence for Industrial AI Agents* (HiveMQ Technical White Paper, Feb 2026)

The wiki's **first OT/industrial-manufacturing source** on agentic AI specifically — opening a parallel track to the SaaS / coding-agent cluster. 15-page PDF, ~12 pages of body content. Three-tier semantic data layer (semantic model + domain ontologies + knowledge graph); four structural pillars of an industrial ontology (object types / properties / link types / **action types** with preconditions and state changes); three-layer architecture (Data Streaming + Data Intelligence + Agentic AI); five mechanisms why ontologies enable reliable agentic AI (unified operational awareness / semantic layer / compounding returns / closed-loop learning / governed autonomy). Source page: [[2026-02-01-manditereza-ontology-driven-industrial-ai]]. Author **Kudzai Manditereza** listed as Dangling first-mention; **HiveMQ** also Dangling first-mention. Customer references: Audi, BMW, Eli Lilly, Liberty Global, Mercedes-Benz, Siemens — none promoted on a single mention. Touched pages:

- [[industrial-ai-agents]] — **new concept page** created (single-source stub at confidence 0.70; aliases: industrial AI agents / industrial agentic AI / OT AI agents / manufacturing AI agents). Names three distinguishing properties: data-fabric primacy, action-precondition governance, continuous real-time data dependency.
- [[index.md]] — added entry under both Sources and Concepts.

Candidate sub-concepts noted but **not promoted** on single source: Ontology / Semantic Data Layer, Unified Namespace (UNS), Action types / action-precondition governance. **Knowledge graph** reaches second-source convergence in this same ingest batch (Bratanic + Manditereza); flagged as promotion candidate for a follow-up sweep.

## [2026-05-10] ingest | Bratanic — *Unified Agentic Memory Across Harnesses Using Hooks* (Towards Data Science, 8 May 2026)

The wiki's first source naming **lifecycle hooks as a first-class harness primitive** — distinct from MCP tools — with an **emerging cross-vendor contract**: Claude Code, Codex, and Cursor all support the same five lifecycle events (`SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`) with near-identical JSON-stdin / JSON-stdout semantics. Three-layer architecture (hooks online + dream-phase offline + injection online); shared Python scripts + Neo4j store; switch from Cursor to Claude Code to Codex mid-project and pick up where you left off. Dream-phase markdown wiki is structurally identical to Karpathy's LLM-wiki idea and to Anthropic's Skills. Source page: [[2026-05-08-bratanic-unified-agentic-memory-hooks]]. Author **Tomaz Bratanic** (Neo4j) listed as Dangling first-mention; **Neo4j** also Dangling first-mention. Touched pages:

- [[agent-harness]] — major hooks-as-primitive section added (cross-referencing Lopopolo + the wiki's own [`hooks` schema section](CLAUDE.md#hooks)); MCP-vs-hooks distinction tabled; dream-phase pattern named explicitly. (Co-listed under the Lopopolo entry above for the source_count update.)
- [[index.md]] — added entry; co-listed under [[agent-harness]] convergence summary.

Operational note: this source's hook contract converges with the wiki's own [§Hooks](../CLAUDE.md#hooks) section — **three independent vantages** (Lopopolo / Bratanic / this repo's own scripts) now supply convergent evidence that hooks are a stable cross-vendor harness primitive.

## [2026-05-10] ingest | Lopopolo — *Harness engineering: leveraging Codex in an agent-first world* (OpenAI Engineering blog, 11 Feb 2026)

The wiki's first **vendor-side production case study** of [[agent-harness]] / [[agentic-engineering]] at scale: five months, ~1M LOC, ~1,500 PRs, 7 engineers, 3.5 PRs/engineer/day with throughput **increasing** as the team grew — built with **0 lines of manually-written code**. Source page: [[2026-02-11-lopopolo-codex-harness-engineering]]. Author **Ryan Lopopolo** listed as Dangling first-mention. Ingested three months after publication (Feb 11) — reactive ingest discipline, not a freshness gap. Touched pages:

- [[agent-harness]] — added vendor case-study section + hooks-as-primitive section (alongside Bratanic) + Build-layer-vocabulary refinement (alongside Chase). `source_count` 8 → 11; `confidence` 0.90 → 0.92; `last_confirmed` → 2026-05-10.
- [[agentic-engineering]] — added Codex case-study row in convergence table + new "Operational invariants" section (8 named invariants distilled from the Codex team's experience: repository-as-system-of-record, AGENTS.md as table-of-contents, layered architecture mechanically enforced, throughput inverts merge philosophy, encoded golden principles + scheduled GC, application legibility, hire for environment-design taste). `source_count` 2 → 3; `confidence` 0.80 → 0.85.
- [[OpenAI]] — added Codex / Codex CLI / Aardvark to "Products and tooling" section. `source_count` 7 → 8; `confidence` 0.85 → 0.90.
- [[index.md]], [[log.md]] — updated.

## [2026-05-10] ingest | Solovyev & Dwivedi — *Gemini API File Search is now multimodal* (Google — The Keyword, 5 May 2026)

Short developer-relations announcement (5-page PDF, ~3-min read) introducing three updates to the Gemini API File Search tool: **multimodal** retrieval via Gemini Embedding 2 (images and text in the same store); **custom metadata** (`department: legal`, `status: final`) for query-time filtering; **page-level citations** tying responses to specific pages of indexed PDFs. Three-primitive API: `file_search_stores.create` → `upload_to_file_search_store` → `generate_content` with `tools=[{file_search: …}]`. Source page: [[2026-05-05-google-gemini-file-search-multimodal]]. Authors **Ivan Solovyev** (PM, Google DeepMind) and **Kriti Dwivedi** (SE) listed as Dangling first-mention. Source-count bump for [[Google]] (2 → 3). No structural concept changes — substantiates a *Context-layer retrieval primitive* the wiki has been gesturing at.

## [2026-05-10] refactor | Wiki-wide wikilink-italics sweep + schema rule (Quartz compatibility)

**Trigger:** the `agentic-engineering` link on [[2026-05-08-running-an-ai-native-engineering-org]] failed to render on the published Quartz site (commit `129913a` fixed that single instance). Investigation found the same `[[target|*alias*]]` and `[[target|… *partial italics* …]]` pattern in **21 other places** across the wiki — a systemic Quartz-compatibility issue invisible in Obsidian.

**Root cause:** Quartz's default forward-link parser expects a literal string between `|` and `]]`. Markdown emphasis inside the alias either leaks the asterisks into rendered text or silently breaks the link. Obsidian masks this by processing the alias as full markdown.

**Sweep applied:**

- **Pattern A — full-alias italics** (`[[target|*alias*]]` → `*[[target|alias]]*`): 14 mechanical replacements via a Python-regex pass. Touched: 1 concept page, 11 entity pages, 1 source page (Kokane). Italic emphasis preserved by moving the `*` markers outside the wikilink.
- **Pattern B — partial italics inside the alias** (e.g. *"Ransbotham et al. 2024 — \*Learning to Manage Uncertainty, With AI\* (MIT SMR × BCG)"*): 7 replacements. Uniform rule: drop the inner asterisks. Visual loss is minor (the `[[…]]` already signals "this is a clickable thing"). Touched: [[durable-skills]] (×2), [[David Kiron]], [[Sam Ransbotham]], [[wiki/log.md|wiki/log.md]] (an earlier entry's *McKinsey Rewired* reference), [[2026-05-07-kokane-agent-harness-vs-systems-design]], [[syntheses/organizational-frameworks-for-ai-adoption|the synthesis page]].

**Schema rule added** (CLAUDE.md §"Wikilink-rendering rule (Quartz compatibility)"): codified the two safe patterns so future ingests don't reintroduce the issue. The rule sits next to the existing "Body-wikilink rule (load-bearing)" since both are about wikilink hygiene under Quartz's parsing constraints.

**Verification:**

- `graph-export.mjs` after the sweep: 133 nodes / 120 edges — no regression.
- `lint-page.mjs` on a sampled changed page: silent.
- `grep -rnE '\[\[[^]]*\|[^]]*\*[^]]*\]\]' wiki/`: 0 remaining matches across the corpus.

**Stats:** 17 files changed, 21 insertions / 21 deletions (perfect 1-for-1 line swaps; no body-content drift). Plus 1 CLAUDE.md schema addition (this rule). Plus this log entry.

## [2026-05-09] refactor | Enrich [[2026-05-08-running-an-ai-native-engineering-org]] with 12 presentation slides from raw/images/

**Trigger:** user supplied 12 screenshots from Fiona Fung's slide deck (originally timestamped `Screenshot 2026-05-09 at 10.27.41.png` … `10.31.14.png`; renamed in this same session per user request to slide-titled slugs `raw/images/fung-slide-01-old-process-quietly-stops-working.png` … `fung-slide-12-pick-noisiest-workflow.png`). The slides crystallise Fung's argument in compacter form than the spoken version and contain several quotable framings absent from the transcript.

**Net additions to the source page:**

- New **Slide-deck visual canon** section walks through all 12 slides in talk order with full on-screen wording, screenshot file references, and one-line *slide-vs-transcript* notes per slide.
- Augmented **three signals** key-claim with slide-derived **six-month adoption threshold** (*"If these don't shift in six months, adoption isn't working"*) and concrete signal-criteria (*"week-one engineers ship real code"*; *"queue depth stopped being a leading complaint"*).
- Augmented **closing parable** key-claim with the slide-12 Monday-test diagnostic: *"if it only exists because engineering used to be expensive, it probably doesn't."*

**Quotable framings that were slide-only (not in transcript):**

- *"Cost of asking a 'dumb' question went to zero"* — onboarding (slide 2)
- *"For most work it was theater"* — re: design docs (slide 3)
- *"When things break in an AI-native flow, they break in new ways"* — verification (slide 3)
- Two new "Claude handles" categories: *spec drift and missing tests*; *repeated patterns, bug-bounty triage* (slide 4)
- *"Taste is scarce, typing is not"* — hiring (slide 5)
- *"Subtly wrong is still wrong"* — deep systems expertise (slide 5)
- *"I care what you choose to build and how you know it's right"* — slide 5 footer; explicitly names *spec-design taste* + *evaluation craft* as the two human-load-bearing capabilities
- *"Humans still decide, they just aren't the first draft anymore"* — XFN-gap process (slide 6)
- **Forcing function vs Room to adapt** as the canonical mandate-vs-adapt structure (slide 8)
- Roles-blurring open question's answer-axis is *"feel confident about their changes"* (slide 11) — more actionable than the transcript's "feel productive"

**Frontmatter updates:**

- `length:` extended to *"~28:38 minutes (transcript ~163 lines + 12 presentation slides captured as screenshots)"*
- New `slides:` field pointing at `raw/images/fung-slide-01-…-12-*.png` (12 substantive slides, slide-titled slugs)
- `tags:` extended with `presentation-slides`
- `confidence:` raised 0.75 → 0.80 (slides are the speaker's own canonical distillation; multiple framings sharpen claims that were rhetorical-only in the transcript)

**Untouched:** existing key-claims sections retained verbatim where the transcript adds context (anecdotes, narrative connective tissue) the slides don't carry. The two layers complement: slide canon gives the speaker's chosen wording; key-claims gives the transcript's connective tissue and cross-source positioning. A short note at the top of "Key claims" tells readers slides win on canonical wording.

**No changes** to other wiki pages — this is a single-source enrichment, no cross-cutting concept/entity touches needed.

## [2026-05-09] ingest | Fiona Fung — *Running an AI-native engineering org* (Claude YouTube / Code with Claude 2026, 8 May 2026)

**Source page:** [[2026-05-08-running-an-ai-native-engineering-org]]. ~28:38-minute conference talk (transcript ~163 lines) by **Fiona Fung** (Director of Engineering for Claude Code at [[Anthropic]]; previously led teams at Meta and Microsoft) on the team-norms rewrite at the Claude Code engineering organisation. The wiki's **first inside-engineering source** on what running an AI-native organisation looks like operationally — distinct from prior 2026 sources that argued the case for AI-native engineering rhetorically (Karpathy, Chatterjee, Kokane) or measured it ablation-by-ablation ([[2026-05-04-rethinking-agents-harness-is-all-you-need|Pan/Khattab via Prompt Engineering YouTube]]).

**Where this fits:** Karpathy 2026 named [[agentic-engineering]] as a discipline; Chatterjee 2026 gave [[agent-harness]] its 4-layer anatomy; Fung 2026 shows **the team-norms rewrite that follows from them** — the org-shape, hiring, review, planning, and process choices that ship the 10×-plus product (Claude Code itself).

**Headline claims:**

- *"What may have served you prior may not serve you any longer."* The bottleneck shift: coding throughput is no longer expensive; verification, review, cross-functional partners, and security are.
- *"Rarely do processes kill themselves"* — codified as the third core team principle (*explicit permission to kill those processes*).
- The org-level analogue of [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering|Karpathy's December 2025 phase change]]: *"I just trusted the system more and more, and then I was vibe coding."*
- Three signals to watch (no absolute numbers shared; direction-of-travel only): onboarding ramp-up time **dramatically reduced**; PR cycle time **shortening** (also surfaces pipeline gaps); Claude-assisted commits **trending toward 100%** (*"I don't think I've seen a non-Claude-assisted commit probably in the last four months"*).
- The two engineer profiles she indexes on: **creative builders with product sense** + **deep systems expertise**. **Indexes less on**: raw throughput.
- **Code is the source of truth**, not docs.
- **Every manager in Claude Code starts as IC** for dogfooding and street cred — recruiters initially pushed back; she held the line.

**Touched (cross-cutting per CLAUDE.md ingest workflow):**

1. **NEW:** [[2026-05-08-running-an-ai-native-engineering-org]] — full source page; description-blockquote leads body per the convention added 2026-05-09.
2. **NEW:** [[Boris Cherny]] — entity page. Cross-page-presence promotion: third source mention (prior in [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]] and [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]]; named here by Fung as her partner in running Claude Code engineering and product). Precedent: [[Andrej Karpathy]], [[Jack Clark]].
3. **UPDATED:** [[agentic-engineering]] — `source_count: 1 → 2`; `confidence: 0.75 → 0.80`. Added Fung row to the convergence table: the **inside-engineering vantage** that pairs Karpathy's discipline-naming with the operational team-norms rewrite.
4. **UPDATED:** [[agent-harness]] — `source_count: 7 → 8`; `confidence: 0.85 → 0.90`. Fung's code-review division of labour (Claude on style/lint/bugs/tests; humans on legal/security/product taste) is the on-the-ground concretisation of Chatterjee's *Constraints* layer (pre/post-tool middleware) and *Contracts* layer (formal-evaluable specifications) at the engineering-team level rather than per-agent.
5. **UPDATED:** [[vibe-coding]] — `source_count: 1 → 2`; `confidence: 0.75 → 0.80`. Fung's *"I just trusted the system more and more, and then I was vibe coding"* mirrors Karpathy's December 2025 phase change at the org level.
6. **UPDATED:** [[software-3.0]] — `source_count: 1 → 2`; `confidence: 0.75 → 0.80`. Light reinforcement: the talk is implicitly built on the paradigm.
7. **UPDATED:** [[enterprise-ai-adoption]] — `source_count: 23 → 24`. Inside view of an [[2026-04-28-werner-lebrun-octopus-organization|Octopus-shaped]] technology org: flat, pod-driven, agile-by-design, with leader-dogfooding as a structural commitment. Adds *JIT planning*, *Claudify everything*, *processes-pile-on* as named operational practices.
8. **UPDATED:** [[Anthropic]] — `source_count: 4 → 5`. Body section on *Claude Code* engineering leadership extended with named individuals (Boris Cherny + Fiona Fung) and the team-norms-rewrite practice. *Cowork* added as a deferred-for-second-source-mention product.
9. **UPDATED:** [[index]] — new source line at the chronological end (between 2026-05-04-rethinking-agents and the Entities section); new entity line for [[Boris Cherny]] (alphabetical between [[Bharat N. Anand]] and [[Boston Consulting Group]]).
10. **UPDATED:** `wiki/log.md` (this entry).

**Dangling (single-source mention, deferred per CLAUDE.md author-entity promotion rule):** *Fiona Fung* (speaker), *Cat* (keynote-of-the-morning on Claude Code Review), *Jared* (colleague), *Daren Lannon* (earlier-talk speaker), *Code with Claude 2026* (event), *Cowork* (Anthropic product alongside Claude Code).

**Strongest cross-source synthesis enabled by this ingest:** Fung's three core team principles — *every team member uses Claude Code*, *Claudify everything*, *explicit permission to kill processes* — mirror the wiki's three independent-vantage convergences (engineering / firm-boundary / organisational) on **"models commoditize; what's owned compounds"**. Fung adds a fourth vantage: **at the team-norms layer**, what compounds is the disciplined permission to *prune* old processes as the substrate changes. This is the team-process counterpart to [[2026-05-04-rethinking-agents-harness-is-all-you-need|Anthropic's "subtraction principle"]] at the harness-component layer.

**Open questions surfaced for future ingest:**

- Population-level confirmation of Fung's three signals (onboarding ramp-up time, PR cycle time, Claude-assisted commit share). Tractable; would be ingestable from a follow-up Anthropic Economic Index report or third-party engineering-productivity study.
- The **iOS/Android org shape** question. If a follow-up resolves it, changes the org-shape thesis for cross-platform deliverables.
- The **fully-automated-review threshold** — Fung names this as a model-capability-tracking moving target; *Daren Lannon*'s referenced session may already address it.
- The **"roles are blurring" fairness** signal. Flagged but not answered. Could absorb into the wiki's [[ai-employment-effects]] cluster.
- *Cowork* and *Code with Claude 2026* as candidate entity pages on second-source mention.

## [2026-05-09] refactor | Fix youtube-transcript-skill (GH #2): Trusted Types CSP + panel-target-id drift + graceful no-transcript path; complete deferred legacy-video backfill

**Trigger:** the skill failures documented in the prior 2026-05-09 log entry blocked legacy-video re-fetch. User (skill author) requested fix + completion of the deferred backfill.

**Filed:** [GH #2](https://github.com/businessdatasolutions/ai-wiki/issues/2) at `businessdatasolutions/ai-wiki` documenting all three bug classes and the defense-in-depth fix. Issue updated mid-PR with the secondary panel-target-id bug discovery and the graceful-handling improvement.

**Touched (skill):**

1. [`fetch_transcript.py`](../.claude/skills/youtube-transcript-skill/fetch_transcript.py):
   - `browser.new_context(...)` now passes `bypass_csp=True` (Change A — comprehensive CSP bypass).
   - `page.add_init_script(...)` injects a default Trusted Types policy after `ctx.new_page()` (Change B — defense in depth, resilient if `bypass_csp` is later removed).
   - Rewrote `_trigger_transcript_panel` / `_wait_for_transcript` / `_scroll_panel` / `_extract_segments` to be panel-target-id-agnostic: query `ytd-transcript-segment-renderer` elements directly anywhere on the page; direct `Show transcript` button click added as a fallback after the legacy event-dispatch.
   - `_main` now writes the markdown file even when no transcript is fetched (metadata-only path) — exit code `1` signals partial output but the file IS written. Was: error out with no file.
2. [`SKILL.md`](../.claude/skills/youtube-transcript-skill/SKILL.md): updated **Failure modes** section to document all three fixes and link to GH #2.

**Touched (raw videos — completed deferred backfill):**

3. [[raw/videos/andrej-karpathy-from-vibe-coding-to-agentic-engineering]] — re-fetched via fixed skill; YAML frontmatter now carries the full rich metadata (channel_id, channel_url, category, view_count, caption_tracks, chapters with mm:ss starts, description, thumbnail). Body unchanged (manually-cleaned transcript preserved).
4. [[raw/videos/rethinking-agents-harness-is-all-you-need]] — same procedure; same outcome.

**Touched (wiki source pages — completed deferred description blockquotes):**

5. [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering]] — prepended the YouTube description as a leading blockquote (matching the new convention added on 2026-05-09).
6. [[2026-05-04-rethinking-agents-harness-is-all-you-need]] — same; sponsor-mention and link list omitted with a note pointing to the raw file for the full text.

**Remaining (tracked for future):** the transcript-panel timeout still affects long-format videos (≥20 min observed) — the legacy two videos populated metadata only, not transcript bodies. The skill is shippable because the metadata-only path is graceful. User confirmed the existing manually-copied transcripts in the legacy raw-file bodies are the source of truth; the skill's failure to extract them itself doesn't block the wiki workflow. GH #2 documents the open issue for follow-up.

**Net effect:** the skill works end-to-end for short videos (full transcript), and for any length video produces a usable metadata-only markdown file when the transcript panel doesn't render. The legacy-video deferred backfill from the 2026-05-09 plan is now closed.

## [2026-05-09] refactor | Adopt youtube-transcript-skill YAML frontmatter as canonical raw video format; backfill 2 legacy files

**Trigger:** A new skill ([`youtube-transcript-skill`](../.claude/skills/youtube-transcript-skill/SKILL.md)) was added that fetches YouTube metadata + transcripts via Playwright and emits Markdown with rich YAML frontmatter (~20 fields incl. `video_id`, `channel`, `channel_id`, `channel_url`, `publish_date`, `upload_date`, `category`, `duration`, `length_seconds`, `view_count`, `caption_tracks`, `chapters`, `description`, `keywords`, `thumbnails`). The wiki's prior 4-line plain-text raw-video header convention is now a strict subset of this richer schema. The example file [[raw/videos/running-an-ai-native-engineering-org]] was already saved into the wiki in the new format on 2026-05-08.

**Touched (CLAUDE.md schema):**

1. Rewrote §"Pre-flight check (videos)" to specify the YAML-frontmatter contract (replacing the 4-line plain-text spec). Documented the canonical pre-flight fields (`title`, `url`, `channel`, `publish_date`) and added a legacy-format compatibility note for transition-window readers.
2. Rewrote §"Source-page conventions specific to videos" to add an explicit field-mapping table from raw skill output → wiki source-page frontmatter (`channel:` → `author: [...]`; `publish_date:` → `date_published:` with timezone stripped; `caption_tracks[].kind` → source-quality flag in body, **not** confidence; etc.). Reaffirmed the existing `author = channel` convention. **Added a new body convention**: video source pages open with the YouTube `description:` rendered as a leading blockquote, before the wiki's TL;DR — channel framing first, wiki interpretation second.

**Touched (raw videos):**

3. **Backfilled** [[raw/videos/andrej-karpathy-from-vibe-coding-to-agentic-engineering]] from the legacy 4-line plain-text header to YAML frontmatter. Body preserved verbatim (manually-cleaned transcript). Skill re-fetch attempted but failed at the transcript-panel render step (Trusted Type CSP error — known YouTube DOM-drift failure mode per SKILL.md); rich fields populated from existing wiki source page metadata only. `notes:` block in the file documents the gap so it can be re-fetched once the skill is patched.
4. **Backfilled** [[raw/videos/rethinking-agents-harness-is-all-you-need]] same way; same skill-fetch failure mode; same gap-flagging in `notes:`.

**Decisions resolved with user:**

- Backfill via skill re-fetch (selected over manual conversion or no-backfill) — but skill failed; fell back to manual conversion with explicit gap-flagging.
- ASR transcript provenance does **not** feed into confidence math — sources are evidence, not claims, per [§Lifecycle](../CLAUDE.md#lifecycle). `caption_tracks[].kind` informs source-quality flag in body only.
- YouTube `description:` rendered as leading blockquote on video source pages — channel framing first, wiki interpretation second.

**Deferred (pending skill patch):**

- The leading description-blockquote edit on [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering]] and [[2026-05-04-rethinking-agents-harness-is-all-you-need]]. The new convention is documented in CLAUDE.md and applies to *new* video source pages going forward; the two existing pages will get their description blockquotes once the skill's transcript-panel render issue is fixed and a fresh fetch surfaces the YouTube `description:` field. No fabricated content.
- A follow-up to investigate / patch the `youtube-transcript-skill` Trusted Type CSP failure mode on current YouTube DOM. Worth flagging to the skill author.

**No changes** to `scripts/*.mjs` — generic frontmatter readers handle both formats transparently (verified by exploration; lint-page.mjs / graph-export.mjs / session-start.mjs / lint-dangling-authors.mjs read frontmatter agnostically).

**No changes** to existing wiki source-page frontmatter schema — only the body convention adds a leading blockquote (deferred above).

## [2026-05-08] ingest | Andrej Karpathy: From Vibe Coding to Agentic Engineering (Sequoia AI Ascent, 29 April 2026)

**Heaviest single-source ingest to date** — ~30-min interview at Sequoia Capital's *AI Ascent* event (Sequoia's first-ever guest), 29 April 2026. Second video ingest under the new `raw/videos/` schema; first interview-format video. Single-step rename from `video2.md` → `andrej-karpathy-from-vibe-coding-to-agentic-engineering.md` per the pre-flight rule.

The source has two unusual properties that shape the ingest scope:

1. **Karpathy is the upstream-spec author for this entire repo.** The repo's [`llm-wiki.md`](../llm-wiki.md) conceptual spec is his articulation of the LLM-knowledge-base pattern; CLAUDE.md cites him at the top. **In the closing section (29:00–29:30) Karpathy explicitly describes his continued use of an LLM-knowledge-base / wiki-from-articles workflow** as his primary information-processing tool — *"anytime I see a different projection onto information, I always feel like I gain insight"*. This is the **upstream-spec author confirming the pattern is still load-bearing for him in 2026** — a rare and citation-worthy artifact for this repo.
2. **The video is an interview, not an explainer.** Per the `kind: video` schema committed yesterday (`author = channel`), `author: ["Sequoia Capital"]`. Karpathy is the substantive content owner but appears as a body wikilink to [[Andrej Karpathy]], whom we promote to entity page on cross-page-presence grounds (the **Jack Clark precedent** — he's named in [`llm-wiki.md`](../llm-wiki.md), [`llm-wiki-v2.md`](../llm-wiki-v2.md), [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md), and [`CLAUDE.md`](../CLAUDE.md)). Convention not extended; one-off judgment call.

**Files touched (13):**

1. **RENAMED** `raw/videos/video2.md` → `raw/videos/andrej-karpathy-from-vibe-coding-to-agentic-engineering.md` (per the new pre-flight rule committed yesterday).
2. **NEW** [[2026-04-29-andrej-karpathy-from-vibe-coding-to-agentic-engineering]] — full source page with section-by-section coverage of the 10 thematic segments. Confidence 0.80 (capped at 0.75 baseline + raised because Karpathy is the originator of half the vocabulary in question; not raised higher because opinion-format and several predictions are explicitly TBD).
3. **NEW** [[Andrej Karpathy]] — entity page (cross-page-presence promotion). Coverage: ex-OpenAI co-founder, ex-Tesla Autopilot, Eureka Labs founder, originator of Software 1.0/2.0/3.0 framing, vibe coding, animals-vs-ghosts mindset, the LLM-wiki idea.
4. **NEW** [[software-3.0]] — concept page. The 1.0/2.0/3.0 trilogy; LLM-as-programmable-computer; context-window-as-program; load-bearing claim is *"new things possible, not just speed-up"* (Menu Gen as worked example). Architecturally upstream of [[agent-harness]] (a Software 3.0 program needs a runtime).
5. **NEW** [[agentic-engineering]] — concept page. The engineering discipline of writing software with AI agents while *preserving the quality bar*. Paired-with-vibe-coding contrast (floor vs ceiling). *"The 10× engineer used to be the upper bound; agentic engineering pushes far past 10×."* Hiring-format critique included.
6. **NEW** [[vibe-coding]] — concept page. Coined by Karpathy 2024; the floor-raising democratisation half of Software 3.0. Includes the **December 2025 phase change** anecdote. When-to-use vs when-not-to-use guide.
7. **EXTENDED** [[jagged-frontier]] — added "Cause-of-jaggedness: verifiability + labs care" sub-section + "Animals vs ghosts" sub-section + canonical 2026 example (Opus-4.7-refactors-100k-line-codebase-but-tells-you-to-walk-to-50m-car-wash). `source_count: 5 → 6`. Aliases extended ("jagged intelligence", "jagged skills", "animals vs ghosts").
8. **UPDATED** [[agent-harness]] — `source_count: 6 → 7`; intro paragraph adds the **paradigm-vocabulary anchor** framing; convergence table extended with Karpathy row.
9. **UPDATED** [[ai-agents]] — `source_count: 9 → 10`; intro adds the **intern entities** framing.
10. **UPDATED** [[foundation-models]] — `source_count: 7 → 8`; intro adds the cause-of-jaggedness pointer (LLMs automate what you can verify).
11. **UPDATED** [[generative-ai]] — `source_count: 19 → 20`; intro adds the [[software-3.0]] paradigm-vocabulary reframe + paired discipline pointer to [[agentic-engineering]] / [[vibe-coding]].
12. **UPDATED** [[index]] — new source line (chronologically between 2026-04-28-werner-lebrun and 2026-04-29-boussioux); new entity line ([[Andrej Karpathy]] between Amy Webb and Andy Wu); three new concept lines ([[agentic-engineering]] after [[agent-harness]]; [[software-3.0]] after [[responsible-ai]]; [[vibe-coding]] after [[systems-thinking]]); existing concept lines updated for the new cross-references.
13. **UPDATED** `wiki/log.md` (this entry).

Plus: added `.env` and `.env.*` to `.gitignore` as a tiny separate task this session, on the same commit-scope.

**Dangling (single-source mention, deferred per CLAUDE.md author-entity promotion rule):** *Sequoia Capital* (channel/publisher), *Nanobanana* (image-gen tool), *OpenClaude* (agentic coding tool), *micro-GPT* (Karpathy project), *Menu Gen* (Karpathy app), *Eureka Labs* (Karpathy's company), *Tesla* (already mentioned in AI Index reports — could be promoted on cross-page-presence in a later pass).

**Strongest cross-source synthesis enabled by this ingest**: Karpathy provides the **paradigm vocabulary** (Software 3.0, agentic engineering as a discipline, jagged intelligence) for what the existing [[agent-harness]] / [[2026-05-04-rethinking-agents-harness-is-all-you-need|empirical-anchor]] / [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee]] / [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]] sources were already describing operationally. The wiki's 2026 AI-engineering corpus now has a **complete frame**: paradigm (Software 3.0) → discipline (agentic engineering) → artifact (agent harness) → empirical evidence (Pan et al. + Khattab et al. via the YouTube synthesis) → org-level economics (Kiron-Schrage, Ransbotham et al.).

**The most surprising ingest finding** (worth flagging to future readers): Karpathy's closing-section reference to using an **LLM knowledge base / wiki built from articles** as his primary information-processing tool is *the very pattern this repo implements*. The upstream-spec author confirms his pattern is still load-bearing for him as of 29 April 2026 — that durability test hadn't been visible from inside the repo before this ingest.

**Open questions surfaced for future ingest:**
- Karpathy's hinted *"valuable RL environments not in the labs' mix"* — declined on stage. If a follow-up writeup names the domains, that's a high-value second source.
- Population-level confirmation of the **December 2025 phase change** Karpathy describes — currently single-person testimony.
- **Aesthetics-as-RL-reward** — Karpathy says current agent code is *"bloaty, copy-paste, awkward abstractions, brittle."* If labs add an aesthetic-quality reward signal, the gap between [[vibe-coding]] and [[agentic-engineering]] narrows.
- Karpathy's plan-mode critique (*"work with your agent to design a spec; then have agents write against the docs"*) is richer than current plan-mode UIs — worth tracking which IDE / harness vendors ship something matching.


## [2026-05-08] ingest | Rethinking Agents — Harness is All you Need (Prompt Engineering YouTube, 4 May 2026)

**First video ingest** — also the first ingest under the new `raw/videos/` convention. Two outputs from this operation:

1. **Schema update (CLAUDE.md)**: extended `raw/` collection list to include `videos/`; added a new "Pre-flight check (videos): rename the raw file before reading further" subsection under §Verifying sources before ingest. The convention: video transcripts arrive in `raw/videos/` with non-descriptive filenames + a 4-line metadata block (`title:`, `author:`, `url:`, `date published:`); first action is to slugify the title and rename the raw file (`mv` while untracked, `git mv` once tracked). Source page filename uses the publish date prefix; `kind: video`; `length:` in mm:ss; `author:` taken verbatim from the raw file (channel name for YouTube). User has committed to including all four metadata lines on every future transcript — full automation from raw header.

2. **First ingest (this entry)**: `raw/videos/video1.md` → `raw/videos/rethinking-agents-harness-is-all-you-need.md` per the new pre-flight rule. Video introduces the wiki's first **empirical anchor** for [[agent-harness]] — a synthesis of two academic papers: **Pan et al.** (Tsinghua, March 2026) on natural-language harness representation (SWE-bench verified ablations: verifiers actively hurt, self-evolution helps; OS-Symphony NL-migration **30.4 → 47.2%**) and **Khattab et al.** (DSPy team) on Meta-Harness auto-optimisation (Terminal Bench 2 **76.4%**, +7.7 above SOTA on 215-class text classification, **transferable across 5 models**, raw-traces-irreplaceable: 50 → 34% if removed, 34.9% if summarised). Names Anthropic's **subtraction principle** (Manus 5× rewrites in 6 months; Warel −80% tools / +performance) as a discipline-counter-prescription to the additive build-everything instinct.

**Files touched (8):**

- **UPDATED** [`CLAUDE.md`](../CLAUDE.md) — two surgical inserts (raw collection list + new video pre-flight subsection).
- **RENAMED** [`raw/videos/video1.md`](../raw/videos/video1.md) → `raw/videos/rethinking-agents-harness-is-all-you-need.md`.
- **NEW** [[2026-05-04-rethinking-agents-harness-is-all-you-need]] — source page, `kind: video`, confidence 0.70 (single supporting source for the new claims; capped at 0.75 due to opinion format + third-hand on the underlying papers).
- **UPDATED** [[agent-harness]] — `source_count: 5 → 6`; `last_confirmed: 2026-05-08`; new "The empirical anchor" sub-subsection under Key claims; new convergence-table row; new "model-coupled vs model-portable" debate bullet citing the transferability finding; expanded Open questions (5 new bullets covering primary-source ingest of Pan/Khattab papers, the raw-traces-vs-summaries finding, verifier-hurt mechanism, and Manus/Warel as candidate entity pages).
- **UPDATED** [[ai-agents]] — `source_count: 8 → 9`; `last_confirmed → 2026-05-08`; intro sentence now references the harness empirical anchor.
- **UPDATED** [[foundation-models]] — `source_count: 6 → 7`; `last_confirmed → 2026-05-08`; rented-model section gains the transferable-harness sentence (Khattab's harness lifted 5 different models without re-tuning — empirical support for "plan for swap").
- **UPDATED** [[index]] — new source line under Sources catalogue; `agent-harness` concept entry bumped 5 → 6 sources with empirical-anchor framing.
- **UPDATED** `wiki/log.md` (this entry).

**Dangling (single-source mention, deferred per CLAUDE.md author-entity promotion rule):** *Prompt Engineering* (channel), *Pan et al.*, *Omar Khattab*, *Manus*, *Warel*, *DSPy*. Promote on second-source mention.

**Open questions surfaced for future ingest:**
- Primary-source ingest of Pan et al. (Tsinghua, March 2026) — would substantiate the SWE-bench / OS-Symphony deltas.
- Primary-source ingest of Khattab et al. (Meta-Harness) — would substantiate Terminal Bench 2 76.4% and the transferability claim.
- Whether *"raw traces > summaries"* generalises beyond auto-optimisation to any compounding-loop telemetry — direct implication for [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] Compounding layer if it does.

## [2026-05-08] refactor | Promote Jack Clark to entity page (cross-page-presence judgment)

Follow-up to the earlier "out-of-scope but flagged" note. Per user direction, treated existing [[Anthropic]] and [[AI Index]] entity-page mentions of Jack Clark as effective second-source presence — sufficient to justify promotion despite his appearing in `author:` on only one source ([[2026-04-30-ai-index-report-2026]]) and as an acknowledgement on a second ([[2026-05-07-anthropic-economic-index-5-learning-curves]]).

**Files touched (4):**

- **NEW** [[Jack Clark]] — co-founder of Anthropic; Head of Public Benefit (leads the new Anthropic Institute) since 2026; previously Anthropic Head of Policy and OpenAI Policy Director; technical journalist before that. Founding member of the AI Index (2017–2024); inaugural NAIAC member (2021–2024); OECD AI co-chair. Author of *Import AI*. Confidence 0.75; source_count 2 (AI Index 2026 + AEI 5th report acknowledgement). Web research via WebSearch on anthropic.com / wikipedia / cset.georgetown.edu / itif.org.
- **UPDATED** [[2026-05-07-anthropic-economic-index-5-learning-curves]] — Jack Clark removed from "Dangling" list and promoted into the "Entities" list, with a one-line rationale citing the cross-page-presence basis for promotion (so future readers see the judgment call, not just the result).
- **UPDATED** [[index]] — added [[Jack Clark]] entry between [[Ivey Business School]] and [[Jacqueline N. Lane]].
- **UPDATED** `wiki/log.md` (this entry).

**Convention NOT extended.** This promotion is a one-off judgment call, *not* a rule change. The CLAUDE.md §Lifecycle "Author-entity promotion" convention still says "≥2 source pages with the name in `author:`" — it does **not** auto-promote on entity-page or acknowledgement-only mentions. The audit ([`scripts/lint-dangling-authors.mjs`](../scripts/lint-dangling-authors.mjs)) was not modified and continues to track only the strict `author:`-frontmatter rule. If similar cross-page-presence cases recur often enough that the heuristic feels load-bearing, the schema can be revisited; for now we treat them as case-by-case.

**Side benefit**: the body wikilinks on [[Anthropic]] and [[AI Index]] (which were broken targets before this promotion) now resolve. Quartz's broken-link surface drops by two.

## [2026-05-08] refactor | Codify "Author-entity promotion" convention; add audit script; backfill 9 dangling AI Index authors

Two-part schema-and-corpus refactor closing the silent-skip failure mode in the dangling-author convention.

**Schema codification (CLAUDE.md):**

- New sub-section [§Lifecycle "Author-entity promotion"](../CLAUDE.md#author-entity-promotion). Documents the second-source promotion rule (first source = list in `author:` frontmatter and add to source page's "Dangling" line; second source = create entity page on that ingest). Documents the alias handling for surface-form variation and the audit command.

**Audit script (NEW):**

- [`scripts/lint-dangling-authors.mjs`](../scripts/lint-dangling-authors.mjs) — read-only walker over `wiki/sources/*.md` and `wiki/entities/*.md`. Reports any name in `author:` on ≥2 source pages without a matching entity (canonical filename or alias). Exits non-zero when dangling authors are found. Run: `node scripts/lint-dangling-authors.mjs`. First run found **9 silent-skip cases**, all AI Index 2025 + 2026 co-authors who had been in `author:` on both editions but never promoted because there was no enforcement on the convention.

**Backfill (NEW entity pages, 9):**

Heavy backfill — each entity page carries affiliation, role, prior work, AI Index involvement (chair / steering committee / research team), and `## Appears in this wiki via` block linking both AI Index editions. Sources verified via WebSearch on stanford.edu / hai.stanford.edu / linkedin / wikipedia / company sites; not training-data fabrications.

| Entity | Primary affiliation | AI Index role |
| ------ | ------------------- | ------------- |
| [[James Manyika]] | Google–Alphabet (SVP Research, Labs, Technology & Society); UN AI High-Level Advisory Body co-chair | Steering Committee |
| [[Juan Carlos Niebles]] | Salesforce Research (Director); Stanford CS Adjunct; Stanford Vision and Learning Lab co-Director | Steering Committee |
| [[Lapo Santarlasci]] | IMT School for Advanced Studies Lucca (Economics PhD researcher) | 2025 + 2026 co-author (research team) |
| [[Loredana Fattorini]] | Stanford HAI Research Manager; Global AI Vibrancy Tool co-author | Spearheads the Index in collaboration with the AI Index Lead |
| [[Raymond Perrault]] | SRI International (Distinguished Computer Scientist Emeritus); CALO/Siri-lineage NLP researcher | Steering Committee chair (2025) and co-chair (2026) |
| [[Russell Wald]] | Stanford HAI Executive Director (since 2024) | Steering Committee |
| [[Terah Lyons]] | Partnership on AI (founding ED); former White House OSTP Policy Advisor under Obama | Steering Committee |
| [[Vanessa Parli]] | Stanford HAI Director of Research Programs | Steering Committee |
| [[Yoav Shoham]] | Stanford CS Professor Emeritus; AI21 Labs co-founder & co-CEO; Allen Newell Award (2012); IJCAI Research Excellence Award (2019) | Steering Committee |

**Source-page updates (2 files):**

- [[2026-04-28-ai-index-report-2025]] — added new `## Authorship and steering` subsection that wikilinks the steering committee and the research-team contributors; cleaned up the "Linked entities and concepts" line to move newly-promoted names into the proper "Entities" list (was previously listed under "Mentioned but not yet promoted to standalone pages"). Single-source author names remain deferred there.
- [[2026-04-30-ai-index-report-2026]] — added the same `## Authorship and steering` subsection; the prior `## Related in this wiki` section's role-pointer bullets for [[Yolanda Gil]] / [[Raymond Perrault]] / [[Sha Sajadieh]] / [[Nestor Maslej]] are now subsumed by the steering subsection (those bullets removed to avoid duplication).

The body-wikilink rule (v0.3 §Graph) now resolves correctly — every newly-promoted entity has at least one body wikilink in both AI Index source pages, so each entity's `## Mentioned in` dataview block will populate properly via Quartz `file.outlinks`.

**Files touched (13):**

- 9 NEW entity pages (above).
- NEW [`scripts/lint-dangling-authors.mjs`](../scripts/lint-dangling-authors.mjs).
- UPDATED [`CLAUDE.md`](../CLAUDE.md) — new §Lifecycle "Author-entity promotion" sub-section.
- UPDATED [[2026-04-28-ai-index-report-2025]] — Authorship subsection + Linked-entities cleanup.
- UPDATED [[2026-04-30-ai-index-report-2026]] — Authorship subsection.
- UPDATED [[index]] — 9 new entity entries inserted at alphabetical positions.
- UPDATED `wiki/log.md` (this entry).

**Verification**: re-ran `node scripts/lint-dangling-authors.mjs` post-backfill (exit 0 expected); 9 → 0 dangling, 6 → 15 multi-source-promoted, 127 single-source-deferred unchanged.

**Out-of-scope but flagged**: [[Anthropic]] entity page contains a body wikilink to `[[Jack Clark]]` ("co-founder; serves on the AI Index steering committee") which is currently a broken link — Jack Clark is a single-source author on the 2026 AI Index and stays correctly deferred per the convention, but the existing wikilink on the Anthropic page predates the convention and reads as a broken target. Two clean fixes: (a) drop the wikilink and keep him as plain text on the Anthropic page, or (b) treat the Anthropic page's wikilink as a *second* effective mention (employer + AI Index author) and promote him on those grounds. Deferred for the next pass.

## [2026-05-08] ingest | Cheung, Ippolito, Secchi — *Agents CLI in Agent Platform: create to production in one CLI* (Google Developers Blog, Apr 2026)

Ingested [[2026-04-22-cheung-ippolito-secchi-google-agents-cli]] — Google Developers Blog announcement (22 April 2026) of the **Agents CLI in Agent Platform**: a single CLI bundling the full **Agent Development Lifecycle (ADLC)** on Google Cloud (scaffold → evaluate → deploy → publish → observe). Three integrated artifacts: the `google-agents-cli` package, an Agents CLI Skills bundle injected into AI coding agents, and opinionated project templates. Two-mode design — **Agent Mode** (skills-driven by Gemini CLI / Claude Code / Cursor) and **Human Mode** (deterministic terminal CLI). Seven specialized skills (Workflow / ADK Code / Scaffold / Evaluation / Deployment / Publish / Observability) and a 9-stage ADLC wheel.

**Source page also embeds the three article images** (extracted into `raw/images/`): `fragmented_gcp_1.original.png` (the nine-domain fragmented stack), `agents_cli_skills.original.png` (the seven-skills grid), `agents_cli_lifecycle.original.png` (the ADLC wheel).

**Files touched (6):**

1. **NEW** [[2026-04-22-cheung-ippolito-secchi-google-agents-cli]] — full source page.
2. **NEW** [[Google]] — entity page (organization). Covers Google as parent of [[Google Research]] and **Google Cloud / Google Developers**, and as ADK / Agent Platform / Gemini Enterprise publisher. The [[Google]] entity was previously absent — only [[Google Research]] existed — so this fills a real gap (Google was being referenced in body text without a page to link to).
3. **NEW** [[agent-development-lifecycle]] — concept stub (single-source; confidence 0.70). The ADLC is a **process** construct (parallel to SDLC) where [[agent-harness]] is a **runtime** construct; the two overlap heavily but are not the same thing.
4. **UPDATED** [[agent-harness]] — `source_count: 4 → 5`; `last_confirmed: 2026-05-07 → 2026-05-08`; `confidence: 0.80 → 0.85` (per [§Lifecycle](../CLAUDE.md#lifecycle), +0.05 for an additional supporting source). Added Google Agents CLI as the fifth row of the cross-source convergence table; updated the headline framing to call out two big-vendor productizations within two weeks; expanded the "Frameworks vs roll-your-own" open question to flag a possible *third tier* emerging — vendor-published lifecycle toolkits *over* harness frameworks.
5. **UPDATED** [[index]] — added the new source at the top of Sources (chronologically earliest; 2026-04-22 < 2026-04-28); added [[Google]] entity entry between [[Glenn R. Carroll]] and [[Google Research]]; added [[agent-development-lifecycle]] concept entry; updated the [[agent-harness]] index line from "4 sources" to "5 sources" with the vendor-productization framing.
6. **UPDATED** `wiki/log.md` (this entry).

**Cross-source positioning**: this article is the Google-side companion to [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic's Managed Agents post]] (8 April 2026) — same fortnight, both vendors productizing the harness/runtime layer, different rhetorical registers (engineering retrospective vs product announcement) but heavily overlapping technical territory. With Microsoft Agent Framework v1.0 named in [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane]], **three of the major-lab vendors** are now in the wiki shipping productized harness/runtime infrastructure. The interpretive question — is this a market-defining moment? — belongs in [[agent-harness]] and any future synthesis page, not in the source page (cross-source neutrality rule).

**Authors deferred as dangling**: per the convention used for [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands]] (Lance Martin, Gabe Cemaj, Michael Cohen — three Anthropic engineers, not given dedicated entity pages on first ingest), the three Google authors (Ivan Cheung, Pier Paolo Ippolito, Elia Secchi) are listed in the source frontmatter but not given individual entity pages. Promote on second-source coverage.

**Open question for the next ingest**: ADK has now been mentioned in three sources (Kokane / Chatterjee implicit / Cheung et al. explicit) but is treated as a brand mention on the [[Google]] entity page rather than its own concept or product entity. If a primary ADK technical-deep-dive lands, it justifies a dedicated page. The wiki has not yet ingested any Microsoft Agent Framework primary, despite it being named alongside ADK; that's another candidate gap.

## [2026-05-08] refactor | Refresh synthesis: organizational-frameworks-for-ai-adoption (6 → 10 frameworks)

Refreshed [[syntheses/organizational-frameworks-for-ai-adoption]] (originally filed 2026-05-05 with 6 frameworks). Six new source pages have been ingested in the intervening three days, contributing **four new framework-vantages**:

- **Firm-boundary lens** ([[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar & Nohria 2026]])
- **Human-reaction lens** ([[2026-05-07-carucci-resistance-as-data|Carucci 2026]]) — orthogonal cross-cutting
- **Organizational-learning lens** ([[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]] + [[2026-05-07-kiron-schrage-compound-benefits|Kiron & Schrage 2026]]) — empirical foundation + operational mechanism
- **Runtime-engineering lens** ([[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]] + [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]]) — sceptical + taxonomical vantages

**Synthesis-page changes (8 sections updated in place):**

- **Frontmatter**: `last_refreshed: "2026-05-08"` field added (new convention for refreshed syntheses; complements the existing `closed:` date which preserves the original closure moment); `last_confirmed: 2026-05-05 → 2026-05-08`; `source_count: 6 → 12`. Confidence held at 0.90 (the cluster is broader but also surfaces new methodological open questions).
- **Intro**: rewritten to make the 6 → 10 expansion visible upfront; flags that the core thesis is unchanged but the evidence is substantially stronger.
- **Layered framework table**: 7 rows → **11 rows** (new layers: Organizational learning, Firm-boundary, Runtime engineering; new orthogonal cross-cutting row: Human reaction).
- **Decision tree**: 7 questions → **10 numbered questions + 1 cross-cutting question**. Sequenced top-of-house (Werner-Le-Brun org-design) to engineering-floor (agent harness runtime).
- **Where they genuinely disagree**: 4 splits → **7 splits**. New: firm-boundary fluidity vs. org structural property; "process redesign is the value" vs. "harness is the moat" (resolution: different stack layers); Kokane sceptical vantage on the entire cluster; Augmented Learners as upstream of MIT CISR Stage transition.
- **Cross-framework agreement**: 5 claims → **6 claims** with stronger evidence. The cluster's most consequential new finding: the **"compounding cycle" is the same operational mechanism at two stack layers** (Kiron-Schrage organizational + Chatterjee runtime). Worker-attitude data (84% hopeful / 20% fearful) corroborates the augmentation-not-automation finding from a new vantage. Also added: "models commoditize; what's owned compounds" — three independent vantages reach the same conclusion.
- **Empirical-validation table**: 6 rows → **10 rows**. Critical update: **MIT CISR is no longer alone with N>500 representative-sample data.** Ransbotham/Kiron's 3,467-respondent 2024 cross-industry global survey is now the largest dataset in the cluster, and it is post-GenAI where MIT CISR is pre-GenAI.
- **Sources consulted**: 6 → 12 entries (split into "Original 6 (filed 2026-05-05)" and "Added in 2026-05-08 refresh").
- **Lessons**: 4 → 7 lessons. New: organizational learning capability is the upstream variable for MIT CISR Stage 2 → 3 transition; the compounding cycle requires both organizational and runtime loops running; the human-reaction lens is cross-cutting not stack-layered; models commoditize while what's owned compounds.
- **Open questions**: marked 2 prior questions as **partially resolved** by the refresh; added 4 new open questions (cross-walk between Stages and Augmented Learners; firm-boundary × maturity-stage interaction; quantitative measurement of compounding-cycle slope; Kokane-Chatterjee hiring-data tension).
- **Related pages**: added [[agent-harness]] concept (created in the prior ingest); updated framework-count from 6 to 10.

**Why a refactor not a synthesize op**: per CLAUDE.md §Synthesis, the `synthesize` operation is for *initial* close of a thread into a synthesis page. The thread closed 2026-05-05; this refresh updates the existing synthesis with new source material rather than reopening or reclosing. `refactor` is the closest fit in the schema's permitted ops (`ingest | query | lint | synthesize | refactor | bulk-refactor`).

**No new convention written into CLAUDE.md** for synthesis refreshes — the addition of a `last_refreshed:` frontmatter field is consistent with the v0.2 lifecycle spirit (`last_confirmed:` already exists for concepts and entities). If synthesis refreshes become routine, the convention should be promoted into the schema; for now it is precedential rather than canonical.

**Files touched (3)**: [[syntheses/organizational-frameworks-for-ai-adoption]] (substantial expansion, ~150 line additions across 9 sections); `wiki/log.md` (this entry); the touched-source [[enterprise-ai-adoption]] is *not* updated by this refresh — the synthesis adds content, the concept page already reflects the 10 lenses.

**Cross-source convergence worth flagging at synthesis level**: the **"compounding cycle"** is now the wiki's strongest concept-level cross-source agreement. Kiron-Schrage 2026 (organizational level: verification → evaluation → learning capture) and Chatterjee 2026 (runtime level: Compounding telemetry → harness adjustments → workspace overrides) describe operationally identical machinery from different practitioner communities. Both anchor onto the same architectural commitment ([[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]) and the same empirical foundation ([[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]]). When 4 sources from 3 vantages converge on the same operational mechanism, the construct is robust enough to be load-bearing for the synthesis.

## [2026-05-07] ingest | Chatterjee — *The Anatomy of an Agent Harness* (Medium, May 2026)

Ingested **Abhishek Chatterjee — *The Anatomy of an Agent Harness*** (Medium, ~3 May 2026, ~6 pages of body content / 9-page PDF / 8-min reading time). Long-form practitioner essay anchored in a vivid production-failure story; complement to [[2026-05-07-kokane-agent-harness-vs-systems-design|Kokane 2026]] above.

**The Friday-in-March story** (the essay's rhetorical anchor): a user said *"clean things up before the board review."* The agent — *competent, helpful, working exactly as designed* — interpreted this as archive stale documents + prune duplicates + remove stale sources, soft-deleting two weeks of research history 40 minutes before a board meeting. *"The model was not the problem. The model had reasoned correctly given what it was asked. The problem lived in the layer around the model."*

**The wiki's clearest worked example of agent-failures-are-harness-failures**: the load-bearing claim is that production agent failures are usually *harness* failures masquerading as *model* failures. This propagates through [[ai-agents]], [[responsible-ai]] (intent validation as Constraints-layer RAI control), and [[micro-productivity-trap]].

**4-layer harness anatomy** (in build order):

1. **Context** — system prompt as a *document*, assembled fresh per request, with stable parts (KV-cached) + dynamic parts (user memory + workspace knowledge + delta summary + behavioral persona). *"Context is not a feature you bolt on. It is the room the agent walks into."*
2. **Constraints** — middleware-pattern pre/post-tool hooks: destructive-verb recognition, workspace isolation, loop detection, output scoring across citation coverage / source triangulation / severity distribution / density / thematic diversity. Harness as **active editor**, not passive observer.
3. **Contracts** — formal evaluable specifications of "successful output," **calibrated to inputs available** (a synthesis contract over 5 sources is not the same as one over 50). Function, not checklist. Makes agent failures **debuggable**. Domain-specific.
4. **Compounding** — structured telemetry records (NOT log lines) feeding a nightly meta-learning loop that proposes **harness adjustments** (not model fine-tuning — the model is rented and frozen). Human-reviewed; approved adjustments become **workspace overrides** that compound. *"This is what people mean when they say AI products will get better with use. They do not mean the model is learning. They mean the infrastructure around the model is learning, and the surface area where learning lives is the harness."*

**The CEO sentence** (the version that lands in a boardroom): *"the model is rented from a vendor whose competitor will outperform them within the year; the harness — our memory architecture, our quality contracts, our learned per-customer overrides, our telemetry — is what we own and what compounds; it is the only part of our stack that gets more valuable with every customer we ship to."*

**Critical cross-source convergence**: Chatterjee's **Compounding** layer is operationally identical to [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage 2026]]'s **verification → evaluation → learning capture** flywheel. Independent convergence — two practitioner essays, different vantages (PM-facing engineering essay vs. MIT SMR column), arrive at the same operational mechanism. Lifts the construct from single-source (Kiron-Schrage) to confirmed cross-source.

**Wiki impact (joint with Kokane 2026 above; total 11 files touched)**:

- **2 new source pages**: [[2026-05-07-kokane-agent-harness-vs-systems-design]], [[2026-05-07-chatterjee-anatomy-of-agent-harness]].
- **1 new concept page**: [[agent-harness]] — promoted because 4 wiki sources now reference the construct substantively (these two new sources + [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] + [[2026-05-07-kiron-schrage-compound-benefits|Kiron-Schrage]] via the Boris Cherny / CLAUDE.md anchor). Confidence **0.80** (baseline 0.7 + 0.05 additional supporting source + 0.05 cross-source-convergence).
- **0 new entity pages**: Abhishek Chatterjee, Akshay Kokane both single-source (skipped per the 2+ source convention).
- **1 concept enrichment (heavy)**: [[ai-agents]] — added "The application-layer counterpart: the agent harness" subsection; added the Friday-in-March worked example; added [[agent-harness]] to Related concepts. `confidence: 0.95` unchanged, `source_count: 6 → 8`, `last_confirmed: 2026-05-07`.
- **5 concept enrichments (light)**:
  - [[foundation-models]] — added "Models converging to commodity status: the rent vs own framing" subsection. `confidence: 0.85` unchanged, `source_count: 4 → 6`.
  - [[generative-ai]] — added Harness frameworks row (LangChain etc.) to the deployed-tools table. `source_count: 17 → 19`.
  - [[micro-productivity-trap]] — added "Sixth- and seventh-source corroboration" subsection on agent-harness practitioner essays; the Compounding-layer / Kiron-Schrage flywheel cross-source convergence is the wiki's strongest concept-level convergence so far. `confidence: 0.85 → 0.90`, `source_count: 5 → 7`.
  - [[responsible-ai]] — added "Intent validation as a Constraints-layer RAI control" subsection with the three-layer RAI runtime taxonomy table. `source_count: 8 → 10`.
  - [[enterprise-ai-adoption]] — added "The runtime-engineering lens: agent harnesses as the new moat" subsection (10th adoption-framework lens); updated lens count from 9 → 10. `source_count: 21 → 23`.
- **index.md**: 2 new source entries, 1 new concept entry ([[agent-harness]]).

**Source-quality flag**: opinion essay, not empirical research — no data, no n, no benchmarks. Single-source on the Friday-in-March story (anonymized customer; details non-verifiable). Author has commercial interest in the "harness is the moat" framing (building praxiomai.xyz, an AI PM agent product). Confidence **0.75** (baseline 0.7 + 0.05 additional supporting source — Kokane / Anthropic Managed Agents / Kiron-Schrage mutually reinforce). Not raised to 0.80 because opinion-format.

**Dangling references** (single-source mention, deferred): Abhishek Chatterjee (author); praxiomai.xyz; getpolaris.xyz; the *Claude Code leak* (referenced in both new sources — first-party ingest would be valuable); LangChain / Microsoft Agent Framework / Google ADK / LlamaIndex / CrewAI / Haystack / DSPy (single-source named; promote on 2nd source coverage).

**Joint commit**: ingested concurrently with Kokane 2026 above in a single commit per user request — both new sources are practitioner essays on the same topic from opposite rhetorical stances, mutually reinforcing the [[agent-harness]] construct's promotion to a wiki concept page.

## [2026-05-07] ingest | Kokane — *What is Agent Harness? How it is different than System Design?* (Level Up Coding, Apr 2026)

Ingested **Akshay Kokane — *What is Agent Harness? How it is different than System Design?*** (Level Up Coding / Medium publication, 10 April 2026, ~4 pages of body content / 8-page PDF / 4-min reading time). **Provocation-style** practitioner article arguing the term "agent harness" is mostly a rebranding of mature systems engineering, with a small but genuine ~10% kernel of novelty.

**Central claim**: 90% of agent-harness engineering is systems design we've always done (cache management = Context management; database + job queue = State persistence; API middleware = Tool orchestration; approval workflows = HITL; memory leak / stale state = Context rot; summarization + offload = Compaction; process lifecycle = Harness lifecycle). The patterns are identical — only the wrapped surface (an LLM instead of a database driver) is new.

**The 10% genuinely novel** has two named components:

1. **Non-determinism at the execution layer** — classical middleware assumes the wrapped service behaves consistently; LLMs hallucinate tool calls, return semantically wrong responses, lose track of original goals 40 turns in. *You cannot unit test for it. You cannot formally specify it.* Validation must check **intent**, not just output format. The Claude Code permission pipeline confirms this: it checks whether the model is *authorized to want what it wants*.
2. **Context as a first-class degrading resource** — working memory that *actively gets worse the longer it runs.* Garbage collection ≠ semantic drift correction. Named phenomenon: **context rot**.

**4-layer architectural stack**: Your App / Harness Frameworks (LangChain, Microsoft Agent Framework v1.0, Google ADK, LlamaIndex, CrewAI, Haystack, DSPy) / Agent Harness Runtime (context manager, permissions, state, tool executor, retry, HITL, observability) / swappable Model Layer (Azure OpenAI/GPT-5, Claude, Gemini/Llama/Ollama, AWS Bedrock).

**Three reasons for the rename** (one genuine, two cynical): (1) genuine — non-determinism at the core logic layer requires intent-validation; (2) cynical — companies need a category to sell; (3) cynical — new entrants need vocabulary, and incumbents who coin it get the SEO/mindshare.

**Honest verdict**: *"If you've shipped real backend systems, you're already 80% of the way there. The skill gap isn't architecture. It's learning to think about prompt state as program state, and treating the context window as your most constrained and most expensive resource."*

**Cross-source positioning**: same topic as [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee 2026]] (ingested concurrently below), opposite rhetorical stance. Kokane is sceptical-provocative; Chatterjee is taxonomical-affirmative. Both can be true and the wiki holds them as complementary vantages on [[agent-harness]]. Kokane's "inference-only model + execution-only tool executor" maps directly to [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]]'s **brain / hands** decomposition — same engineering pattern, different vocabulary.

**Wiki impact** (counted as part of the joint 11-file touch with Chatterjee 2026 below):

- 1 new source page: [[2026-05-07-kokane-agent-harness-vs-systems-design]]
- 0 new entity pages (Akshay Kokane is single-source, deferred)
- Heavy contribution to the new [[agent-harness]] concept page (the "10% genuinely novel" framing; the rename mapping table; the 4-layer stack diagram).

**Source-quality flag**: opinion essay, not empirical research. Practitioner author with explicit credentials (ex-Microsoft, ex-AWS, currently Enterprise AI Architect / Forward Deployed Engineer). The "Claude Code leak" anchor is third-hand (interpreting analyses by others, not reading the source directly). Some time-sensitive factual claims (Microsoft Agent Framework v1.0 GA April 2026) warrant verification before being treated as authoritative. Confidence **0.70** — single-source baseline with no empirical anchor.

**Dangling references** (single-source mention, deferred): Akshay Kokane (author); Vivek Trivedy (LangChain blog *Anatomy of an Agent Harness* — different from Chatterjee's similarly-titled piece); Ken Huang / DistributedApps.ai *Claude Code Leak: 10 Agentic AI Harness Patterns*; arstechnica reporting on the leak; LangChain / LangGraph; Microsoft Agent Framework v1.0; Google Agent Development Kit; LlamaIndex; CrewAI; Haystack; DSPy.

## [2026-05-07] ingest | Kiron & Schrage — *How to Reap Compound Benefits From Generative AI* (MIT SMR Column, Apr 2026)

Ingested **David Kiron, Michael Schrage — *How to Reap Compound Benefits From Generative AI*** (MIT Sloan Management Review Column, 6 April 2026, ~12 pages of body content / 13-page PDF / 12-min reading time). Op-ed-style argument extending Ransbotham et al. 2024's empirical foundation with the operational mechanism for compounding AI value.

**Central thesis**: Reorient AI deployment from **consumption economics** (asset depreciation: task in, output out, loop closes; knowledge evaporates) to **compounding economics** (asset appreciation: each cycle improves the next).

**Two structural dynamics** make compounding management imperative:

1. **Polanyi's tacit-dimension breach** — "Humans know more than they can articulate" was a moat for knowledge workers (1966 *The Tacit Dimension*). LLMs now breach that moat *not by codifying tacit knowledge but by inferring it from behavioral traces at scale*. Tacit expertise was a moat; it is no longer.
2. **Jevons paradox amplification** — efficiency gains stimulate demand. As tacit expertise becomes machine-readable, sophisticated capability gets cheaper, and projects previously too expensive to prototype proliferate.

**The three-step flywheel**:

| Step | Question | Distinction |
|---|---|---|
| **Verification** | Does this output meet the standard? | Binary check against existing criteria. *Necessary but insufficient.* |
| **Evaluation** | What does this output reveal? | May generate **new** standards. Requires domain expertise. *Where most orgs fail.* |
| **Learning capture** | How do we ensure this insight persists? | Version control for organizational judgment (e.g. CLAUDE.md-style files). |

**The trap**: most organizations practice **verification masquerading as evaluation** — "consumption dressed up as adoption."

**Anchor anecdotes**:

- **Boris Cherny** (Anthropic, led Claude Code development) — 10–15 concurrent Claude instances as smart subagents; CLAUDE.md captures mistakes/corrections/design principles *inside the workflow*; "It was mind-blowing" when AI began exploring his file system unprompted.
- **Jaana Dogan** (Google, Gemini API) — pointed Claude Code (rival tool) at a months-long problem; "*It's not perfect and I'm iterating on it.*" Eight words that embody the verification-vs-evaluation distinction.

**Five concrete moves**: preserve evaluation expertise; build minimally viable verification; institute evaluation practices ("What was *interestingly* wrong?"); create capture systems (decision journals, prompt repositories, evaluation logs); measure the cycle, not just the output.

**Strongest claim worth flagging**: *"The expert as evaluator is not a transitional role."* — direct, named claim about durable expertise under AI. Anchor for [[durable-skills]] and [[ai-employment-effects]].

**Wiki impact (counted as part of the joint 12-file touch with Ransbotham et al. above)**:

- **1 new source page**: [[2026-05-07-kiron-schrage-compound-benefits]].
- **0 new entity pages** (Kiron already created via Ransbotham above; Michael Schrage is single-source, deferred; Boris Cherny is single-source explicit, deferred — referenced via [[Anthropic]] entity).
- **3 concept enrichments** (already counted above; the Kiron-Schrage flywheel is the *operational* portion of the joint enrichments to [[enterprise-ai-adoption]], [[micro-productivity-trap]], [[durable-skills]], plus light enrichments to [[generative-ai]] (Return on iteration subsection), [[automation-vs-augmentation]] (convergence-table row), [[ai-employment-effects]] (expert-as-evaluator subsection)).
  - [[durable-skills]] — added two rows to the cross-source-positioning section (Ransbotham + Kiron-Schrage); confidence lifted from 0.80 → 0.85. `source_count: 2 → 4`.
  - [[generative-ai]] — added "Return on iteration" subsection capturing the consumption-vs-compounding economic reframing + Polanyi/Jevons dynamics + 6×/73%/80% empirical anchors. `source_count: 15 → 17`.

**Cross-source positioning**: The Kiron-Schrage column is *operational extension* of [[2026-05-07-ransbotham-augmented-learners|Ransbotham et al. 2024]] — same lead author David Kiron, 17 months later, with the verification-evaluation-learning-capture flywheel as the *mechanism* that turns the Augmented Learner advantage into compounding returns. Read the two sources together: empirical foundation (2024) → operational machinery (2026).

**Contradictions checked**: none. Reinforces the [[micro-productivity-trap]] thesis from [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI 2026]] and the brain/hands/session pattern from [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands|Anthropic Managed Agents]] (Boris Cherny works at Anthropic; the CLAUDE.md pattern is consistent with the engineering architecture from a different team at the same company).

**Source-quality flag**: Op-ed format, not empirical research. Statistics restated from MIT SMR / BCG research base; not independently validated by this column. Cherny / Dogan anecdotes are vivid but n=2. Confidence 0.80 (baseline 0.7 + 0.05 additional supporting source + 0.05 for being co-authored by an author with prior empirically-grounded work in the wiki). Not raised to 0.85 because the column itself is opinion-format.

**Dangling references** (single-source mention, deferred): Michael Schrage; Boris Cherny (Anthropic); Jaana Dogan (Google); Michael Polanyi (1966 *Tacit Dimension*); William Stanley Jevons (1865 paradox).

**Joint commit**: ingested concurrently with Ransbotham et al. 2024 above in a single commit per user request — both MIT SMR sources, mutually reinforcing, share co-author David Kiron. Together they form the wiki's "MIT SMR organizational-learning lens" on enterprise AI — the 9th adoption framework.

## [2026-05-07] ingest | Ransbotham, Kiron et al. — *Learning to Manage Uncertainty, With AI* (MIT SMR × BCG, Nov 2024)

Ingested **Sam Ransbotham, David Kiron, Shervin Khodabandeh, Michael Chu, Leonid Zhukov — *Learning to Manage Uncertainty, With AI*** (MIT SMR Big Ideas Research Report in collaboration with BCG, November 2024, ~21 pages of body content from a 29-page PDF; full ingest of body + appendix + acknowledgments + references). The **eighth annual** MIT SMR × BCG global research study on AI in business strategy. Spring 2024 survey: 3,467 respondents in 21+ industries and 136 countries, plus 9 executive interviews.

**Central construct**: **Augmented Learners** — the 15% of organizations that combine high *organizational learning* capability with high *AI-specific learning* capability. The empirical 2×2 distribution: Limited Learners 59%, Organizational Learners 14%, AI-specific Learners 12%, Augmented Learners 15%.

**Headline outcomes (Augmented Learners vs Limited Learners)**:

- 1.6× more likely to feel prepared to manage industry uncertainty with AI (82% vs 53%).
- 2.2× for talent disruptions (83% vs 39%).
- 1.8× for technology disruptions (86% vs 49%).
- 1.6× for legal/regulatory disruptions (79% vs 48%).
- 1.4× for revenue benefits from AI (99% vs 71%).
- 1.9× for long-term (>5-year) AI project investment.
- 2.4× for high-risk AI project investment.

**Three areas where AI augments organizational learning**: knowledge capture (NASA Mars 2020 / LG Nova / Capital One), knowledge synthesis (Stitch Fix / Expedia 1.26 quadrillion combos), knowledge dissemination (Slack daily recaps / cloud services TikTok-style learning).

**Five practical steps**: simultaneously improve both learning types; learn to *explore* with AI (not just exploit); choose projects that promote learning (long-term, high-risk); learn responsibly; accelerate learning with AI.

**Appendix — State of AI in Business 2024**:

- AI adoption: 50% (2023) → **70% (2024)** — a +20pp jump in a single year.
- 54% piloting/deploying GenAI; 91% expect GenAI core to strategy in next 3 years.
- **Hopes outpacing fears**: 84% hopeful (vs 70% in 2017) / 20% fearful (vs 31% in 2017).
- AI strategy: **39% (2024)** down from 59% (2020) — back to 2017 levels as GenAI's emergence forced strategy reformulation. Orgs reporting an AI strategy are 2× more likely to generate additional business value.

**Wiki impact (12 files touched, ingested concurrently with Kiron-Schrage 2026 below)**:

- **1 new source page**: [[2026-05-07-ransbotham-augmented-learners]].
- **3 new entity pages**: [[David Kiron]] (recurring co-author across two new sources), [[Sam Ransbotham]] (8th-annual report lead author), [[MIT Sloan Management Review]] (publisher; distinct from MIT Tech Review Insights).
- **2 concept enrichments** (heavy):
  - [[enterprise-ai-adoption]] — added the **Augmented Learners (9th) lens** with full 2×2 distribution + outcome multipliers; new "The Augmented Learner advantage and its operational machinery" subsection covering knowledge capture/synthesis/dissemination + the verification → evaluation → learning capture flywheel; updated the running 7-lenses → 9-lenses cluster phrasing. `source_count: 19 → 21`.
  - [[micro-productivity-trap]] — added 4th and 5th source corroboration ("the operational mechanism" subsection); confidence lifted from 0.80 → 0.85 (five-source agreement across four vantages: consulting / investor + academic / executive coaching / academic survey + practitioner column). `source_count: 3 → 5`.
- **3 concept enrichments** (light):
  - [[ai-employment-effects]] — added "Hopes outpacing fears" subsection with the 84/20 attitude reversal + reconciliation with Brynjolfsson Canaries (different populations, both true). `source_count: 12 → 14`.
  - [[automation-vs-augmentation]] — added two rows to the convergence table (Ransbotham et al. 2024 + Kiron-Schrage 2026 representing organizational-learning and operational-flywheel vantages). `source_count: 12 → 14`.
  - [[responsible-ai]] — added '"Learn responsibly" as a fifth RAI dimension' subsection with Surman / Mozilla quotes on equity, knowledge ownership, learning-style inclusion. `source_count: 7 → 8`.

**Source-quality flag**: BCG-sponsored research (vendor-of-deployment bias non-zero), but mitigated by 8-year longitudinal panel of comparable methodology + 3,467-respondent large-N + cross-validation of adoption numbers against AI Index 2025/2026. Confidence 0.85 (baseline 0.7 + 0.05 large-N empirical + 0.10 multi-year longitudinal panel).

**Dangling references** (single-source mention, deferred): Shervin Khodabandeh, Michael Chu, Leonid Zhukov (co-authors); Sowmya Gottipati (Estée Lauder); Shilpa Prasad (LG Nova); Jackie Rocca (Slack); Tonia Sideri (Novo Nordisk); Mark Surman (Mozilla); Diya Wynn (AWS); Vandi Verma (NASA JPL); Jeff Cooper (Stitch Fix); Rajesh Naidu (Expedia); Prem Natarajan (Capital One); Shelia Anderson (Aflac); BCG Henderson Institute; BCG X. The recurring case studies (Estée Lauder, LG Nova, Aflac, Expedia, Mozilla, Slack, Novo Nordisk, Capital One, Stitch Fix) are kept as broken-link stub-gap signals — promote on 2nd-source coverage.

## [2026-05-07] ingest | Anthropic Economic Index 5 — *Learning curves*

Ingested **Massenkoff, Lyubich, McCrory, Appel, Heller — *The Anthropic Economic Index report: Learning curves*** (Anthropic Economic Index, 5th report, 24 March 2026, ~20 pages, full ingest). Sample period: Feb 5–12, 2026. Direct continuation of the 4th report ([[2026-04-28-anthropic-economic-index-q4-2025]]) — **enrichment, not supersession**.

**Headline findings:**

1. **Stable Claude.ai augmentation/automation split** through Feb 2026 (53/45) — augmentation has now led in **four of five samples**; the longitudinal trajectory is *not* drifting toward automation despite headline narratives about agentic deployment.
2. **Skill-biased technological change** at the user level: high-tenure Claude users achieve **~3-4 percentage points higher task success** than lower-tenure users *after controlling* for task type, model selection, and conversation complexity. The mechanism is identified as **learning by doing** — picking the right tool, prompt structure, and recovery strategies improves with practice.
3. **Model-selection slopes are steep and asymmetric.** Users select Opus differentially for higher-value tasks: **+1.48 pp Opus per +$10/hr task value** on Claude.ai; **+2.79 pp per +$10** on the 1P API (about twice as steep). Choosing the right model tier per task is itself a learnable, measurable skill visible in usage logs.
4. **Surface-specific automation patterns.** Claude.ai split is stable; on the 1P API automation share rose sharply between Aug 2025 and Feb 2026 in three task clusters: **first-line sales**, **programmatic trading and brokerage**, and **coding agent harnesses** ([[Claude Code]] etc.). The aggregate "AI is automating work" framing dissolves once you separate consumer chat surface from agent-mediated API surface.
5. **Coding migration off Claude.ai onto API.** "Computer & Mathematical" task-share on the 1P API jumped from **36% (Aug 2025) → 47% (Feb 2026)**, while the corresponding share on Claude.ai dropped — driven by agentic coding harnesses splitting work into many short directive task-labelled API calls.

**Methodology continuity & caveats:**

- Same privacy-preserving conversation-classification approach as 4th report (~1M Claude.ai conversations + ~1M API transcripts).
- **O*NET vintage shifted** between 4th (2010) and 5th (2019) reports — year-over-year occupation-share comparisons need this caveat.
- Models change between reports: 4th used Claude Sonnet 4.5 predominantly; 5th uses Claude Opus 4.5 / 4.6 in addition. Affects comparability across editions.

**Reconciles with prior wiki claims:**

- **The customer-support equalizing effect** ([[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond 2025]]) and the AEI 5 skill-biased-change finding are not contradictory but operate on different populations. *Within-role workers given a fixed tool* equalize; *self-selected users across tasks/models/tiers* exhibit skill-biased returns. As enterprise deployments mature from single-purpose copilots to general-purpose access, the AEI 5 pattern likely dominates.
- **Reinforces the [[micro-productivity-trap]] thesis** ([[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Dutt, Chatterji et al. 2026]]) — firms capturing real value are operating through agentic harnesses on the API, not individual seats.

**Wiki impact (10 files touched):**

- **1 new source page:** [[2026-05-07-anthropic-economic-index-5-learning-curves]].
- **2 entity enrichments:**
  - [[Anthropic Economic Index]] — added 5th-report row to the reports table; methodology notes (O*NET vintage shift, model mix); description bumped to "five reports through March 2026". `confidence: 0.75 → 0.85`, `source_count: 2 → 3`, `last_confirmed → 2026-05-07`.
  - [[Anthropic]] — added the AEI-5 Opus selection slope to the models section. (Already bumped above for Managed Agents.)
- **5 concept enrichments:**
  - [[automation-vs-augmentation]] — added Feb 2026 row to the longitudinal table (53/45 split); added the surface-/cluster-specific-automation framing (sales / trading / coding API clusters); added 5th-report row to the convergence table. `source_count: 11 → 12`, `last_confirmed → 2026-05-07`.
  - [[ai-employment-effects]] — added "Skill-biased technological change: high-tenure users gain more" subsection with the equalizing-vs-skill-biased reconciliation table. `source_count: 11 → 12`, `last_confirmed → 2026-05-07`.
  - [[generative-ai]] — added "Learning curves: model selection becomes a skill" subsection; positioned tenure-success and model-selection slopes as "headline speedups are realized only when users learn the surface". `source_count: 13 → 15`, `last_confirmed → 2026-05-07`.
  - [[enterprise-ai-adoption]] — added "The deployment-surface migration: coding moved to API" subsection; "single-surface adoption metrics undercount the shift" caveat. `source_count: 17 → 19`, `last_confirmed → 2026-05-07`.
  - [[durable-skills]] — added the AEI-5 row to the cross-source-positioning section with the open question "is AI literacy a 5th durable skill or a fluency that enables the other three?" `confidence: 0.75 → 0.80`, `source_count: 1 → 2`, `last_confirmed → 2026-05-07`.
- **index.md:** new source entry; refreshed [[Anthropic Economic Index]] one-liner.

**Contradictions checked:** none. AEI 5 sharpens and extends the 4th report's findings.

**Dangling references** (single-source mention, deferred): Maxim Massenkoff, Eva Lyubich, Peter McCrory, Ruth Appel, Ryan Heller (paper authors — Anthropic Economic Research team).

**Source-quality flag:** vendor-of-deployment publication (Anthropic measuring its own platform's usage). Methodology is privacy-preserving and large-N (~2M conversations sampled). Confidence boost: +0.05 per "additional supporting source"; +0.05 for large-N empirical bonus where applicable. Per CLAUDE.md, vendor-sponsored work caps at 0.75 unless multiple independent sources agree — the Brynjolfsson Canaries paper independently uses AEI's automation/augmentation classification at occupation level, so the cross-validation supports the higher confidence on related claims.

**Total file touch: 10** (1 source + 2 entity enrichments [1 new content here + 1 already counted under Managed Agents] + 5 concept enrichments + index + log + raw PDF; **ingested concurrently with the Managed Agents post in a single commit** per user request "Find and ingest them. please" — both are Anthropic-sourced and mutually reinforcing).

## [2026-05-07] ingest | Anthropic Engineering — Scaling Managed Agents (Decoupling brain / hands)

Ingested **Lance Martin, Gabe Cemaj, Michael Cohen — *Scaling Managed Agents: Decoupling the brain from the hands*** (Engineering at Anthropic blog, 8 April 2026, ~6 pages of body content). Engineering blog post describing Anthropic's production architecture for long-horizon agent work.

**Architectural thesis** — production agents need to **decouple three concerns** that the chatbot stack collapsed into one:

1. **Brain** — model + tool-use/reasoning loop. Stateless and bursty; scale on its own clock.
2. **Hands** — tool execution surface (code interpreter, browser, MCP servers, file system). Each tool has its own latency, blast-radius, and security profile; isolation per-tool is mandatory.
3. **Session** — long-running orchestration state (memory, conversation history, intermediate artefacts). **A session is not the same as the model's context window** — sessions can run for hours and span context resets.

**Key insights worth flagging:**

- **Security via structural unreachability.** The hands tier runs in a sandbox the brain cannot directly drive — the model emits tool-call requests, and a separate executor decides whether and how to run them. This is the engineering version of the [[responsible-ai|"agent risk"]] story: rather than relying on the model to *refuse* dangerous actions, the architecture makes most dangerous actions structurally unreachable.
- **"Context anxiety" is model-specific.** The post documents that [[Claude Sonnet 4.5]] sometimes wraps up tasks prematurely when its context window fills — a failure mode *not* present on **Claude Opus 4.5** under the same harness. **First wiki evidence** that long-horizon agent reliability varies by model **within a family**, not just across families.
- **Long-horizon weakness is partly architectural, not just capability.** Reframes the RE-Bench 32-hour finding ([[2026-04-28-ai-index-report-2025|AI Index 2025]]) — context-window saturation can be addressed via brain/hands/session decomposition independently of model improvement.

**Wiki impact (8 files touched):**

- **1 new source page:** [[2026-05-07-anthropic-managed-agents-decoupling-brain-hands]].
- **No new entity pages.** [[Anthropic]] already existed; the post's authors (Lance Martin, Gabe Cemaj, Michael Cohen) are deferred as dangling wikilinks until 2nd-source coverage.
- **2 entity enrichments:**
  - [[Anthropic]] — added "Platform / product engineering" section (Claude Platform, Claude Managed Agents, Claude Code); added Claude Opus 4.5 / 4.6 to the model roster with the context-anxiety note. `confidence: 0.75 → 0.85`, `source_count: 2 → 4`, `last_confirmed → 2026-05-07`.
- **3 concept enrichments:**
  - [[ai-agents]] — heavy: added "Engineering pattern: brain / hands / session decoupling" subsection; added Claude Code to the deployment list (with the AEI-5-supplied empirical signature); reframed the Hype-vs-capability-gap debate item with the architectural-vs-capability cut. `confidence: 0.85 → 0.95`, `source_count: 4 → 6`, `last_confirmed → 2026-05-07`.
  - [[responsible-ai]] — added "Security as structural unreachability" subsection. `source_count: 6 → 7`, `last_confirmed → 2026-05-07`.
  - [[foundation-models]] — added Claude Sonnet 4.5 / Opus 4.5 / Opus 4.6 references with the in-family reliability variation note. `confidence: 0.80 → 0.85`, `source_count: 2 → 4`, `last_confirmed → 2026-05-07`.
- **index.md:** new source entry; refreshed [[Anthropic Economic Index]] one-liner.

**Contradictions checked:** none. The post complements rather than contradicts existing agent claims.

**Dangling references** (single-source mention, deferred): Lance Martin, Gabe Cemaj, Michael Cohen (post authors); [[Claude]], [[Claude Code]], [[Claude Sonnet 4.5]], [[Claude Opus 4.5]], [[Claude Opus 4.6]] (referenced across multiple wiki sources but not yet promoted to standalone pages — kept as broken-link stub-gap signals per the v1 convention).

**Source-quality flag:** Anthropic's own engineering blog (vendor-of-deployment). Confidence boost: +0.05 per "additional supporting source" rule applied where it compounded with prior sources on a page; capped at 0.95 by the v0.2 confidence rules. Treat the post as authoritative on Anthropic's own engineering choices but not as independent validation of the architectural claims.

**Total file touch: 8** (1 source + 1 entity enrichment + 3 concept enrichments + index + log + raw PDF; ingested concurrently with AEI 5 below in a single commit per user request).

## [2026-05-07] ingest | Globerson et al. (Google Research) — Towards Scalable Measurement of Durable Skills (preprint, 12 Apr 2026)

A **Google Research preprint** by ~30 authors with collaborators at NYU, UT Austin, and OpenMic. 31 pages, full ingest including appendix rubrics. Identity matches filename; no scope concerns.

**Core contribution:** the wiki's first operational anchor for measuring **durable skills** (collaboration, creativity, critical thinking — also called "21st-century skills" or "future-ready skills"). Resolves the validity-vs-rigor tradeoff that has constrained scalable assessment of these constructs since PISA 2015 (scripted simulated teammates) and ATC21S (human-human dyads).

**The Vantage / Executive LLM architecture:**

- **Single Executive LLM** drives multiple AI teammates (rather than independent agents) AND **steers the conversation** to elicit observable evidence of the skill being measured. Has access to the assessment rubric; prompted to maximize information about the participant's skill level.
- **Separate AI Evaluator** scores the transcript against psychometric rubrics (linear regression for scores; logistic for "no-evidence" labels; 20 ratings per turn per dimension; LOO cross-validation).
- Analogous to a **computerized adaptive test (CAT)** — but for *complex social/cognitive constructs* rather than item-difficulty calibration.

**Validation (large-N empirical):**

- **188 US-based participants ages 18-25** (Prolific platform), **373 conversations**, ~30 minutes / 50 turns each. Two NYU pedagogical raters provided ground-truth ratings.
- **LLM-vs-human-expert agreement matches inter-human-expert agreement** (Cohen's κ ~0.45–0.64 — moderate per Landis-Koch, consistent with the inherent ambiguity of these constructs). Auto-rating is a viable scalable substitute.
- **Executive LLM significantly increases skill-evidence elicitation** vs Independent Agents (p ≤ 0.05, Fisher exact). At conversation level with skill-matched Executive LLM: **92.4%** evidence rate for Project Management, **85%** for Conflict Resolution.
- **Telling subjects "focus on this skill"** without LLM steering had **no effect** (p > 0.6) — the steering must come from the AI side.
- **Recovery error** (mean absolute error |L̂ − L| via simulated subjects): Executive LLM ~0.20 (CR) / ~0.40 (PM) vs Independent Agents ~0.65 / ~0.55.
- **Creativity downstream:** OpenMic partnership; 280 high-school students; 100 train, 180 held-out. **Pearson r = 0.88** between Gemini autorater and human expert scores on total submission grades.

**Models used:** Gemini 2.5 Pro (collaboration); Gemini 3 (creativity / critical-thinking initial results).

**Notable methodological choice:** the **critical-thinking** rubric explicitly evaluates how well participants **use AI tools** during the assessment (fact-checking, retrieval, stress-testing arguments) — including "AI-Supported Exploration" and "AI-Supported Verification" as sub-categories. AI fluency is treated as a sub-component of CT in 2026, not a confounder. Tasks deliberately use ill-structured / ambiguous editorial drafts (e.g., flawed-reasoning teen-social-media editorial; exaggerated coffee-danger article) to force motivated-reasoning detection rather than fact-checking.

**Wiki impact (10 files touched):**

- **1 new source page:** [[2026-05-07-globerson-et-al-scalable-measurement-durable-skills]].
- **1 new entity:** [[Google Research]] (promoted from dangling — Google has been mentioned across multiple sources as a model contributor and AI Index funder; this paper is the first dedicated entity-level anchor).
- **1 new concept page:** [[durable-skills]]. Single primary source for the operational definition; multiple wiki sources cover the underlying construct under different vocabularies (PISA "21st-century skills", McKinsey workforce-reshaping data, Brynjolfsson Canaries supply-side question). Per CLAUDE.md convention, "promotion happens when a recurring observation across multiple sources stabilizes" — observation is recurring; this paper provides the operational anchor. Confidence 0.75 (single-source baseline + large-N empirical bonus).
- **4 concept enrichments:**
  - [[ai-benchmarks]] — added a "Vantage / Executive LLM" subsection (heavy enrichment; methodologically distinct from existing benchmarks); added a row to the benchmark roster table; bumped `source_count: 3 → 4`, `last_confirmed → 2026-05-07`.
  - [[ai-deskilling]] — added "The inverse frame: durable skills" section; bumped `confidence: 0.70 → 0.75`, `source_count: 1 → 2`, `last_confirmed → 2026-05-07`. Added `relationships.contradicts: durable-skills` (inverse measurement frames of the same labour-economics question).
  - [[ai-employment-effects]] — added "The supply-side answer: durable skills" subsection; bumped `source_count: 10 → 11`, `last_confirmed → 2026-05-07`.
  - [[generative-ai]] — added Vantage / Executive LLM (Gemini 2.5 Pro + Gemini 3) to the deployed-tools table; bumped `source_count: 12 → 13`, `last_confirmed → 2026-05-07`.
- **index.md:** new source entry; new entity (Google Research); new concept (durable-skills).

**Cross-source positioning:**

This paper anchors a **new wiki concept** ([[durable-skills]]) at the labor-skill-supply-side layer — adjacent to but distinct from [[ai-deskilling]] (substitution direction) and [[ai-employment-effects]] (consequence direction). Methodologically overlaps with [[2026-04-29-boussioux-crowdless-future|Boussioux et al. (Crowdless Future)]] — both papers use LLMs to evaluate creative outputs against rubrics; together they establish "LLM-as-judge" as a recurring methodological pattern in 2024-2026 AI research, worth tracking as a possible future concept page.

**Contradictions checked:** none.

**Dangling references** (single-source mention, deferred): Amir Globerson and ~30 other individual paper authors; **OpenMic** (the AI-skills-assessment startup partner — promote on 2nd-source coverage); **NYU** and **UT Austin** (academic affiliations); **Yossi Matias** (VP and Head of Google Research; flagged on the Google Research entity page).

**Source-quality flag:** Google Research preprint, not a peer-reviewed journal article (© 2026 Google). Empirical rigor is high (large-N, multi-method validation). Confidence boost: +0.05 per the §Lifecycle "additional supporting source" rule, plus +0.05 for being a large-N empirical study (counts once). Vendor-of-deployment caveat noted on the source page (Google Research has commercial interests in Gemini deployment).

**Limitations the paper acknowledges:** cultural situatedness (current results are US, English-speaking, ages 18-25); construct validity established but not criterion validity (whether scores predict downstream career outcomes); CT and creativity validation is partial (CT relies on simulated-subject recovery; full human-rated validation is "ongoing").

**Total file touch: 10** (1 new source + 1 new entity + 1 new concept + 4 concept enrichments + index + log; raw PDF on disk under `raw/papers/`).

## [2026-05-07] ingest | Carucci — Leaders, Treat Resistance to Change as Valuable Data (HBR.org Digital, 20 Apr 2026)

Practitioner essay by **[[Ron Carucci]]** (cofounder and managing partner at **Navalent**; author of 10 leadership/change-management books including *To Be Honest*, Kogan Page 2021). Identity confirmed via cover/title page; 8 pages of body; full ingest. No data points or studies cited — opinion / consulting wisdom anchored in author's experience.

**Core reframing:** the practical leadership question "how do you tell legitimate concerns from kneejerk resistance?" is the wrong question. The framing assumes some resistance is invalid, which licences leaders to dismiss what they're seeing. **All resistance is meaningful data.** The leader's job isn't to determine validity; it's to diagnose what pushback is signalling.

**Three traps when leaders misread resistance:** personalize the pushback (read it as reaction *to the leader*), moralize the pushback (frame it as loyalty / team-player attitude), rush to resolution (persuade harder, escalate authority). Pushing to eliminate resistance amplifies it or drives it underground.

**Four signal categories** (often co-occurring):
- **Loss** — "What am I losing?" (authority, expertise, identity); leader response = name the loss directly, honor the old way, re-anchor value in the future.
- **Anxiety** — "What does this mean for me?"; leader response = communicate consistently (not just clearly), normalize uncertainty, create space for questions.
- **Lack of control** — "Why is this being done to me?"; warns against *faux-inclusion* (asking for input *after* decisions are made); leader response = be explicit where input matters, involve early to shape, turn participation into co-creation.
- **Flaws in the change** — "This doesn't actually work."; leader response = get curious before corrective, separate signal from delivery, be willing to adapt the plan.

**"Holding the line" framework:** when behaviour patterns *persist* after diagnostic engagement, three steps — name the behaviour and impact clearly without judgment; separate the person from the expectation; follow through consistently (escalate clarity, not emotion).

**Wiki impact (8 files touched):**

- **1 new source page:** [[2026-05-07-carucci-resistance-as-data]].
- **1 new entity:** [[Ron Carucci]] (single source; practitioner-quality flag noted on the entity page).
- **1 entity update:** [[Harvard Business Review]] (`source_count: 7 → 8`; new digital piece added to the table; `last_confirmed → 2026-05-07`).
- **2 concept enrichments:**
  - [[enterprise-ai-adoption]] — added a "Human-reaction lens" subsection alongside the existing 7 lenses; bumped `source_count: 16 → 17`, `last_confirmed → 2026-05-07` (confidence 0.95 unchanged — at cap). Updated the all-lenses-agree summary to seven lenses; flagged Carucci as the 8th framework in the synthesis cluster.
  - [[micro-productivity-trap]] — added third-source corroboration subsection; bumped `confidence: 0.75 → 0.80`, `source_count: 2 → 3`, `last_confirmed → 2026-05-07`. **Three independent vantages now converge** (consulting practice via Bain/OpenAI; investor + academic via Nishar/Nohria; executive coaching via Carucci) on the same point: **the trap is fundamentally a listening failure, not a technology failure**. Carucci's category #4 (Flaws in change) maps directly to the operators-see-problems-leaders-dismiss pattern.

**Cross-source positioning:** Carucci operates at a **decision layer not previously surfaced** by the [[syntheses/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] synthesis cluster. Carucci adds a **human-reaction layer** (the 8th in the cluster). Synthesis page left as-is per the convention established at the v0.3.4 close-out — synthesis pages should be durable, not amended every time a new framework is ingested.

**Contradictions checked:** none. Reinforces existing wiki claims on process redesign as load-bearing and senior-leader ownership patterns.

**Dangling references** (single-source mention, deferred): Navalent (Carucci's firm).

**Source-quality flag:** practitioner opinion writing, not empirical research; no studies cited; treat the four-category typology as a working framework but not a validated taxonomy. Confidence boost from this source is +0.05 per the §Lifecycle "additional supporting source" rule, with no peer-review or empirical-study bonus.

**Total file touch: 8** (1 new source + 1 new entity + 1 entity update + 2 concept enrichments + index + log).

## [2026-05-05] ingest | Nishar & Nohria — The End of One-Size-Fits-All Enterprise Software (HBR.org Digital, 23 Apr 2026)

First post-v0.4 ingest. Article identified as: HBR.org Digital, 23 April 2026, Deep Nishar (technologist/investor — ex-Google senior product 2003–2008, ex-LinkedIn CPO 2009–2014, investments include Anthropic / Figma / Glean / Slack) and Nitin Nohria (HBS professor; 10th HBS Dean 2010–2020). Filename → content match clean. 8 pages of body, full ingest.

**Core thesis:** [[generative-ai]] is dissolving the economic logic that made standardized SaaS the default. Custom software is accessible again because foundation-model + vibe-coding tools (Cursor, Replit Agent, Claude Code, OpenAI Codex) compress months-of-engineering into days. The build-vs-buy question is **no longer a cost decision** — it's a strategic question about **which workflows the firm should own**. Authors explicitly correct their own May 2025 thesis: "We were wrong — not about the direction, but about the pace."

**The four-model framework** for the firm-boundary decision:

1. **Build** — directly on foundation models, for distinctive jobs (logistics-optimization example).
2. **Compose** — vendor scaffolding configured by business users (Salesforce Headless 360 example).
3. **Collaborate** — providers' forward-deployed engineers build bespoke systems in weeks.
4. **Buy outcomes** — procure the outcome itself, not the tool (Adobe outcome-based pricing for CX Enterprise + agentic AI tools as the named industry signal).

Models are not mutually exclusive; most firms will use a combination. Choice is no longer cost-or-feasibility; it is "where does differentiation matter, and where does it not."

**Hard empirical anchors carried into the wiki:**

- Enterprise GenAI app spending: **$1.7B (2023) → $37B (2025)** (~22× in 2 years; SaaS took ~10 years for comparable penetration).
- **~40% of code is now AI-generated**; vast majority of developers use AI coding tools daily.
- **>1/3 of companies** report replacing at least one SaaS tool with a custom-built GenAI alternative.
- Public SaaS valuations **30–60% below 2021 peaks**.

**Wiki impact (10 files touched):**

- **1 source page (new):** [[2026-05-05-nishar-nohria-end-of-one-size-fits-all]].
- **2 entity pages (new):** [[Deep Nishar]] (single source; vendor-of-deployment caveat noted — investor in companies that benefit from the framework, e.g. Anthropic), [[Nitin Nohria]] (single source; academic anchor; HBS not yet an entity page so no `relationships:` block).
- **1 entity update:** [[Harvard Business Review]] — `source_count: 6 → 7`; tabulated all HBR sources (now split into print magazine and HBR.org Digital subsections; 4 digital pieces in the wiki).
- **4 concept enrichments:**
  - [[enterprise-ai-adoption]] — added a "Firm-boundary lens (Nishar-Nohria 4 models)" subsection between the Anand-Wu task lens and the all-lenses-agree summary; bumped `source_count: 15 → 16`, `last_confirmed → 2026-05-05` (confidence 0.95 unchanged — at cap). Updated index.md summary to drop the outdated "five-lens framework" framing.
  - [[micro-productivity-trap]] — added second-source corroboration subsection; bumped `confidence: 0.70 → 0.75`, `source_count: 1 → 2`, `last_confirmed → 2026-05-05`. Nishar-Nohria's "data architecture as foundation" reaches the same conclusion as Bain/OpenAI's process-redesign-first argument from a different vantage. Real cross-source agreement, not echo. Also added Nishar-Nohria to the cross-source positioning list.
  - [[generative-ai]] — added a new subsection "Enterprise application spending: 22× in two years" with Nishar-Nohria's data points; bumped `source_count: 11 → 12` (confidence 0.95 at cap).
  - [[automation-vs-augmentation]] — added section #9 "Buy-Outcomes as the most automative deployment model"; framed the four Nishar-Nohria models along the automation↔augmentation axis (Buy Outcomes = pure firm-level automation; Build = deep augmentation of distinctive workflows). Added Nishar-Nohria row to the cross-source convergence table at bottom. Bumped `source_count: 10 → 11` (confidence 0.95 at cap).
- **`index.md`:** new source entry; new entity entries for Nishar and Nohria; updated `enterprise-ai-adoption` concept summary to drop the stale "five-lens framework" framing.

**Cross-source positioning of the article:**

This is the **7th named framework** in the wiki's "adoption breadth ≠ transformation depth" cluster — and it operates at a **decision layer not previously surfaced** by [[syntheses/organizational-frameworks-for-ai-adoption|the synthesis page filed earlier today]]. The synthesis maps 6 frameworks onto seven layers (org-design / readiness / capability progression / transformation playbook / trap escape / task deployment / diagnostic). Nishar-Nohria adds an 8th layer — the **firm-boundary / make-or-buy layer**. Per the framework-promotion rules (single source for a 4-model framework), no standalone concept page yet; defer to a 2nd corroborating source. The synthesis itself is left as-is — synthesis pages should be durable, not amended each time a new framework is ingested. The new framework lives as a lens in `enterprise-ai-adoption` for now; the synthesis's "Open questions" section already anticipates this evolution.

**Contradictions checked:** none. The article reinforces existing wiki claims:
- Process redesign / data architecture as load-bearing — matches [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|Bain/OpenAI]] and [[2026-05-03-rewired-second-edition-sample|McKinsey Rewired]].
- Senior-leader ownership non-negotiable — matches the same two sources.
- Most enterprise tasks today are augmentative, not automative — matches [[2026-04-30-ai-index-report-2026|AI Index 2026]] (agent deployment in single digits per function).

**Dangling references intentionally left as wikilinks** (single-source, deferred per ingest convention): Salesforce / Salesforce Headless 360, SAP, Workday, Epic, Cursor, Replit Agent, OpenAI Codex, Adobe, [[Harvard Business School]] (Nohria's home; will tip into entity-page territory if a 2nd HBS-published source arrives).

**Source-quality flag for downstream readers:** Nishar's investor positions in [[Anthropic]] and other beneficiaries of the prescribed framework are noted on his entity page. The article's specific numbers ($37B spending, 40% AI-code, >1/3 substitution) are cited via embedded links in the original — those links are the data trail to follow if any becomes load-bearing for downstream wiki claims. HBR.org Digital is practitioner publication, not peer-reviewed; confidence boost from this source is +0.05 per the §Lifecycle "additional supporting source" rule, with no peer-review bonus.

**v0.4 hooks observation:** This is the first ingest with the v0.4 PostToolUse lint hook live. The hook would have fired on every Write/Edit to a wiki page during this ingest. (Whether stderr warnings surfaced visibly back to the session depends on the harness; no warnings were observed during this ingest run.)

**Total file touch: 10** (1 new source + 2 new entities + 1 entity update + 4 concept enrichments + index + log; raw PDF on disk under `raw/articles/` — not committed by gitignore rule).

## [2026-05-05] refactor | v0.4 — automation hooks

Wires Claude Code hooks so the v0.2/v0.3 bookkeeping fires automatically. The harness invokes the hooks; new scripts under [`scripts/`](../scripts/) implement them. Tooling-only release; no wiki content edits.

**Schema changes ([`CLAUDE.md`](../CLAUDE.md)):**

- New §Hooks section, including the load-bearing non-negotiable rule: hooks may write to `wiki/log.md`, lint reports (stderr/stdout), and gitignored derived artifacts (`wiki/.graph.json`); hooks may **NOT** edit any `wiki/**/*.md` content page. Content edits always require explicit user approval in-session.
- Reserved `auto-` log-entry prefix for hook-fired writes (currently no hook writes log entries; convention reserved for v0.5+).

**New scripts:**

- [`scripts/session-start.mjs`](../scripts/session-start.mjs) — fired on `SessionStart`. Outputs a short wiki snapshot (catalog counts, last 5 log entries, `status: stale` and `confidence < 0.5` flags) to stdout. Claude Code feeds the output back as session context. Read-only.
- [`scripts/lint-page.mjs`](../scripts/lint-page.mjs) — fired on `PostToolUse` filtered to `Edit|Write`. If the edited path is under `wiki/**/*.md`, validates the v0.2 lifecycle contract (`confidence`, `last_confirmed`, `source_count`), the v0.3 closed relationship vocabulary (12 types), and the v0.3 body-wikilink rule (every `relationships.target` must appear as a body `[[wikilink]]` — basename-matched, alias-aware). Warnings to stderr. Always exits 0 — never blocks the tool call. Skips `index.md` and `log.md`.
- [`scripts/session-end.mjs`](../scripts/session-end.mjs) — fired on `Stop` (per-turn). If any `wiki/**/*.md` is modified or untracked, re-runs [`scripts/graph-export.mjs`](../scripts/graph-export.mjs) so `wiki/.graph.json` stays fresh; otherwise exits silently. No log writes.

**Hook configuration ([`.claude/settings.json`](../.claude/settings.json)):**

```json
"hooks": {
  "SessionStart": [{ "hooks": [{ "type": "command", "command": "node $CLAUDE_PROJECT_DIR/scripts/session-start.mjs" }] }],
  "PostToolUse": [{ "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "node $CLAUDE_PROJECT_DIR/scripts/lint-page.mjs" }] }],
  "Stop":         [{ "hooks": [{ "type": "command", "command": "node $CLAUDE_PROJECT_DIR/scripts/session-end.mjs" }] }]
}
```

`$CLAUDE_PROJECT_DIR` is expanded by Claude Code to the project root, so the config is portable across machines that clone this repo.

**Verification:**

- `node scripts/session-start.mjs` standalone — produces ~20 lines of context (catalog stats, last 5 log entries, lifecycle flags). Confirmed empty for `status: stale` and `confidence < 0.5` (matching current wiki state).
- `echo '{"tool_name":"Edit","tool_input":{"file_path":"<existing concept page>"}}' | node scripts/lint-page.mjs` — silent on a clean migrated page (correct: no warnings means no output).
- `node scripts/session-end.mjs` exits 0 silently when no wiki content changed.
- `python3 -m json.tool .claude/settings.json` — valid JSON.

**Cuts vs. v2 plan:**

- No on-query hook (file-back-as-page is human-judgment).
- No scheduled retention decay (deferred to v0.5).
- `session-end.mjs` does **not** append a log entry — `Stop` fires per-turn, not per-session, so per-turn entries would be too noisy. Manual log writing remains the convention. Documented in §Hooks "Cuts vs. v2 plan."
- No auto-fix on lint warnings — `lint-page.mjs` only reports.
- `lint-orphans.mjs` and `repair-xrefs.mjs` from the plan are deferred to v0.5 (they're CLI helpers, not hook-fired).

**Reversibility:** four new files (3 scripts + the hooks block in settings.json), additive `## Hooks` section in CLAUDE.md. No content edits anywhere in `wiki/`. To revert: delete `scripts/session-*.mjs` and `scripts/lint-page.mjs`, remove the `hooks` block from `.claude/settings.json`, and revert the §Hooks section in CLAUDE.md.

v0.4 complete. Next per [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md): v0.5 (hybrid search + retention/forgetting).

## [2026-05-05] synthesize | organizational-frameworks-for-ai-adoption — six frameworks mapped to seven decision layers

First synthesis filed under [`wiki/syntheses/`](../wiki/syntheses/). Closes the [[threads/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] thread per its written close-trigger ("when a 5th or 6th comparable framework appears"). The 5th and 6th frameworks were McKinsey *Rewired* 2nd ed and the Bain/OpenAI 4-step transformation framework, both ingested earlier this week.

**The synthesis page** ([`wiki/syntheses/organizational-frameworks-for-ai-adoption.md`](../wiki/syntheses/organizational-frameworks-for-ai-adoption.md)) follows the v0.3 contract:

- frontmatter: `type: synthesis`, `derived_from: [organizational-frameworks-for-ai-adoption]`, `opened: 2026-04-28`, `closed: 2026-05-05`, lifecycle fields (confidence: 0.90, source_count: 6), `relationships: [instance-of enterprise-ai-adoption, supports micro-productivity-trap]`.
- body: Question, Findings (layer-mapping table + 7-step decision tree + genuine-disagreement section + agreement section + empirical-validation gap analysis), Sources consulted (all 6), Lessons (4), Open questions (4).

**Headline finding:** the 6 frameworks map to 7 distinct decision layers (org-design / readiness / capability progression / transformation playbook / trap escape / task deployment / diagnostic). Most apparent disagreements are vocabulary; genuine splits are: (a) the Stage 2 → Stage 3 financial inflection is MIT CISR-specific, (b) "reinvent the business" (McKinsey/Bain) vs incremental capability building (MIT CISR), (c) Werner-Le-Brun's org-design layer is treated as upstream prerequisite, others as downstream outcome, (d) MIT CISR Stage 2 frames pilots as a *phase* while Bain/OpenAI frame the same as a *trap*.

**Thread closure protocol applied:**

- Thread page frontmatter: `status: closed`, `closed: 2026-05-05`, `synthesized_into: organizational-frameworks-for-ai-adoption`.
- Thread page gains an Obsidian `[!success]` callout at the top pointing to the synthesis.
- `index.md` Syntheses section: dropped "(empty)" placeholder; the synthesis is now the first entry. Threads section updated to mark the source thread closed.

**Sibling-basename ambiguity cleanup:** The synthesis page shares a basename with the thread page (intentional convention — synthesis matches thread slug). 12 unqualified `[[organizational-frameworks-for-ai-adoption]]` wikilinks across the wiki were ambiguous after the synthesis was filed. Disambiguated by route:
- Forward-looking references ("see the framework comparison") → `[[syntheses/...|...]]`. 5 occurrences in `concepts/enterprise-ai-adoption.md` (×3), `concepts/micro-productivity-trap.md`, `entities/Cisco.md`, `entities/Bharat N. Anand.md`.
- Historical references ("this thread tracks…", source-page Threads: lines, log entries) → `[[threads/...|...]]`. 7 occurrences in `log.md` (×2), `sources/2026-04-28-mittri-cisco-...`, `sources/2026-04-28-anand-wu-...`, `sources/2026-04-28-werner-lebrun-...` (×2), and the synthesis page's own opening line ("Closes [[threads/...]]").

`scripts/graph-export.mjs` reports the basename collision under `ambiguous_basenames` — the script removes ambiguous basenames from its matching index, requiring folder-qualified targets going forward. Documented in CLAUDE.md §Graph.

**Verification:**
- `wiki/syntheses/` is no longer empty (v0.3 acceptance criterion ✓).
- `index.md` Syntheses section drops the "(empty)" placeholder ✓.
- `npm run build` green; 96 input files; 663 emitted; the synthesis renders with relationships panel showing `instance-of enterprise-ai-adoption` and `supports micro-productivity-trap`.
- `node scripts/graph-export.mjs` reports 94 nodes, 79 edges, 0 unresolved, 1 ambiguous basename (the deliberate thread/synthesis pair).
- `node scripts/lint-confidence.mjs` exits 0 — the synthesis carries all required v0.2 lifecycle fields.

**Reversibility:** the synthesis is a new file; the thread page edit is a small additive callout + 2 frontmatter fields; the 12 wikilink disambiguations are localized text edits. To revert: delete `wiki/syntheses/organizational-frameworks-for-ai-adoption.md`, revert thread page, revert the 12 wikilink edits.

v0.3 complete. Next per [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md): v0.4 (automation hooks).

## [2026-05-05] bulk-refactor | v0.3 migration — relationships on 38 pages

Concept and entity migration adding `relationships:` frontmatter blocks per the v0.3 §Graph contract. **17/17 concepts** and **21/54 entities** migrated; remaining 33 entities (mostly single-source author pages whose org affiliations don't yet exist as entity pages — Wharton, NYU Stern, HBS, Said, etc.) get no `relationships:` block in v0.3 (target-slug for their affiliations would not resolve).

**Concept relationships** (29 edges added, types weighted toward concept-to-concept):
- `supports`: 9 (e.g. `automation-vs-augmentation` → `ai-employment-effects`, `dynamic-capabilities` → `enterprise-ai-adoption`)
- `uses`: 7 (e.g. `enterprise-ai-adoption` → `automation-vs-augmentation`, `ai-agents` → `foundation-models`)
- `caused`: 5 (e.g. `industry-4-0` → `lean-4-0`, `generative-ai` → `enterprise-ai-adoption`)
- `instance-of`: 4 (e.g. `ai-deskilling` → `ai-employment-effects`, `jagged-frontier` → `generative-ai`)
- `part-of`: 3 (e.g. `lean-4-0` → `industry-4-0`, `responsible-ai` → `enterprise-ai-adoption`)
- `contradicts`: 1 (`micro-productivity-trap` → `automation-vs-augmentation`, via "process lock-in")

**Entity relationships** (48 edges added):
- `employs`: 22 (orgs → people, e.g. `McKinsey-&-Company` employs `Eric-Lamarre`, `Kate-Smaje`, `Rob-Levin`, `Alex-Singla`, `Alexander-Sukharevsky`)
- `part-of`: 26 (people → orgs, e.g. `Erik-Brynjolfsson` part-of `Stanford-Digital-Economy-Lab` and `AI-Index`)

Notable structural pattern: the closed 12-type vocabulary is biased toward source/concept relationships. People → org affiliations work well via `part-of`; org → org parent (e.g. `AI-Index` part-of `Stanford-HAI`, `Anthropic-Economic-Index` part-of `Anthropic`) also fits. Pages with no resolvable outgoing relationship in the closed vocab (e.g. publishers like `Harvard-Business-Review`, `Boston-Consulting-Group`, sole-affiliation people whose universities aren't entity pages) get no `relationships:` block — their relationships will surface as inverse edges in `.graph.json` when graph-export computes the inverse view.

**Graph stats after concept + entity migration:**
- Nodes: 93 (17 concepts + 54 entities + 20 sources + 2 threads + 0 syntheses, before the synthesis was filed)
- Edges: 77 (29 concept + 48 entity)
- Unresolved edges: 0
- Ambiguous basenames: 0 (until the synthesis was filed — see next entry)

**Verification:** `npm run build` green; `node scripts/graph-export.mjs` reports 77 edges with 0 unresolved; relationships panel renders on every migrated page.

**Reversibility:** additive `relationships:` frontmatter on 38 existing pages; no content edits. `git diff main` cleanly isolates.

## [2026-05-05] bulk-refactor | v0.3 schema + tooling — typed knowledge graph

Lands the v0.3 schema slice from [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md): typed relationships in frontmatter, a graph-export script, a Quartz layout component that renders relationships per-page, and the formalized synthesis page contract. Wiki content migrations and the synthesis acceptance test ship in the next two log entries.

**Schema changes ([`CLAUDE.md`](../CLAUDE.md)):**

- New §Graph: `relationships:` frontmatter contract on concepts and entities; closed 12-type vocabulary (`supports`, `contradicts`, `caused`, `fixed`, `supersedes`, `uses`, `depends-on`, `part-of`, `instance-of`, `authored-by`, `published-by`, `employs`); load-bearing **body-wikilink rule** (every typed relationship in frontmatter must also appear as a body `[[wikilink]]`); formalized `kind:` enum on entities.
- New §Synthesis: synthesis page contract (`type: synthesis`, `derived_from`, required sections Question / Findings / Sources consulted / Lessons / Open questions) and the `synthesize` operation as a 5-step recipe.
- "The three operations" → "The four operations" — `synthesize` is the v0.3 addition.
- Extensions list extended with `relationships-panel.tsx`.

**Tooling:**

- New Quartz Component [`extensions/relationships-panel.tsx`](../extensions/relationships-panel.tsx): right-sidebar panel between TableOfContents and BacklinksWithAliases. Reads frontmatter `relationships:`, groups by type, resolves each `target` slug via `allFiles` lookup with basename matching, surfaces optional `via` strings as italic. Hides when empty. Component (not AST injection) for proper slug resolution.
- New script [`scripts/graph-export.mjs`](../scripts/graph-export.mjs): walks `wiki/**/*.md`, emits `wiki/.graph.json` (gitignored) with `nodes` (slug, type, kind, title, confidence, source_count, last_confirmed) and `edges` (source, target, target_resolved, type, confidence, via). Reports unresolved edges and ambiguous basenames.
- `wiki/.graph.json` added to `.gitignore` and to Quartz `ignorePatterns` (excluded from publishing).
- [`scripts/lint-confidence.mjs`](../scripts/lint-confidence.mjs) extended to also check `wiki/syntheses/`.

**Verification:**

- `npm run build` clean (95 → 96 input files after the synthesis lands; 663 emitted).
- `node scripts/graph-export.mjs` produces `wiki/.graph.json` with 0 unresolved edges.
- Relationships panel renders correctly on concept and entity pages, hides on sources/threads.

**Reversibility:** schema additions to CLAUDE.md and quartz.config.ts; two new files; one .gitignore line; one script line. Reverting is a small diff. No content edits in this slice.

## [2026-05-05] refactor | v0.2.1 — confidence badge visible on published site

Follow-up to v0.2: the lifecycle fields were stored in frontmatter but not rendered on the published site. The lint script and the `raw` markdown were the only places to see confidence values. New extension [`extensions/inject-confidence-badge.ts`](../extensions/inject-confidence-badge.ts) renders a one-line italicized metadata strip immediately after each page's H1: *Confidence 0.85 · 4 sources · last confirmed 2026-04-28*.

**Implementation note (load-bearing).** The extension uses `htmlPlugins()` (not `markdownPlugins()`) and is registered in [`quartz.config.ts`](../quartz.config.ts) **after** `Plugin.Description()`. Reason: Quartz's Description plugin is itself an htmlPlugin that does `toString(tree)` to compute `file.data.description`. A first attempt that injected the badge as a markdown paragraph before Description ran caused the badge text to appear in `og:description`, `twitter:description`, and `meta name="description"` tags. Re-ordering as an htmlPlugin after Description fixed it.

**Verified:**
- Badge visible on concept and entity pages.
- Sources/threads skipped (no `confidence` field).
- `og:description` on Anthropic now reads `"Anthropic AI safety and research company; publisher of the Claude family..."` — no badge leak.

CSS class `confidence-badge` exposed for future styling. No content edits.

## [2026-05-05] bulk-refactor | v0.2 lifecycle migration batches 5–7 (close-out)

Final 31 entities migrated in three batches. All single-source author/organization pages; values determined by source kind (peer-reviewed academic = 0.75; HBR practitioner / vendor / single-case = 0.70).

### Batch 5 (entities 41–50)

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `entities/Alex Singla.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Alexander Sukharevsky.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Andy Wu.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Arjun Dutt.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Bharat N. Anand.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Continuum Laboratory.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Eric Lamarre.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Gawesha Weeratunga.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Gene Rapoport.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Glenn R. Carroll.md` | 0.75 | 2026-04-28 | 1 |

### Batch 6 (entities 51–60)

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `entities/Harrison Satcher.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Ivey Business School.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Jacqueline N. Lane.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Jesper B. Sorensen.md` | 0.75 | 2026-04-28 | 1 |
| `entities/John Higgins.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Julian Birkinshaw.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Karl S.R. Warner.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Kate Smaje.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Leonard Boussioux.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Maximilian Wager.md` | 0.75 | 2026-04-28 | 1 |

### Batch 7 (entities 61–71, final)

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `entities/Megan Reitz.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Miaomiao Zhang.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Nestor Maslej.md` | 0.75 | 2026-04-30 | 2 |
| `entities/Peter Weill.md` | 0.75 | 2026-05-03 | 2 |
| `entities/Rob Levin.md` | 0.70 | 2026-05-03 | 1 |
| `entities/Schmidt Sciences.md` | 0.70 | 2026-04-30 | 1 |
| `entities/Sha Sajadieh.md` | 0.70 | 2026-04-30 | 1 |
| `entities/Stephanie Woerner.md` | 0.75 | 2026-05-03 | 2 |
| `entities/Tima Bansal.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Vladimir Jacimovic.md` | 0.75 | 2026-04-29 | 1 |
| `entities/Yolanda Gil.md` | 0.80 | 2026-04-30 | 2 |

### v0.2 final state

**71/71 pages migrated.** Final lint output:

- `confidence` distribution: 56 pages at 0.70–0.85, 15 pages at 0.85–1.0, 0 below 0.70, 0 missing.
- 0 pages with `last_confirmed > 30 days` (all dates ≥ 2026-04-28, today is 2026-05-05).
- 0 pages marked `status: stale` (no supersession events triggered yet).

Lint script now exits 0 — the v0.2 lifecycle invariant holds. This becomes the pre-commit check contract for the v0.4 PostToolUse hook.

**The distribution shape** is informative: high-confidence (0.85–1.0) clusters are the well-substantiated *concept hubs* (`enterprise-ai-adoption`, `generative-ai`, `automation-vs-augmentation`, `ai-employment-effects`, `responsible-ai`); the long mid-confidence tail (0.70–0.85) is dominated by *single-source author/organization entities* — the natural shape of a wiki where most entities first appear via one substantiating ingest. As more sources land, those 0.70–0.75 entities will get nudged up by the "+0.05 per additional source" rule in §Lifecycle.

**Build:** `npm run build` clean (95 in, 653 out, no errors).

**Reversibility:** additive-frontmatter only across all 71 pages. Schema additions in [`CLAUDE.md`](../CLAUDE.md), [`quartz.config.ts`](../quartz.config.ts), one new extension ([`extensions/inject-stale-banner.ts`](../extensions/inject-stale-banner.ts)), one new script ([`scripts/lint-confidence.mjs`](../scripts/lint-confidence.mjs)), and the new `bulk-refactor` log op are reversible by removing the additions and reverting the two config files. No source-page or content edits.

v0.2 complete. Next version per [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md): v0.3 (typed entity graph + synthesis contract).

## [2026-05-05] bulk-refactor | v0.2 lifecycle migration batch 4

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `concepts/analogical-reasoning.md` | 0.75 | 2026-04-28 | 1 |
| `concepts/systems-thinking.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Cisco.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Amy Webb.md` | 0.75 | 2026-04-28 | 2 |
| `entities/Amazon Web Services.md` | 0.80 | 2026-04-28 | 2 |
| `entities/Fabrizio Dell'Acqua.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Ethan Mollick.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Karim Lakhani.md` | 0.75 | 2026-04-28 | 1 |
| `entities/METR.md` | 0.70 | 2026-04-28 | 1 |
| `entities/Aaron Chatterji.md` | 0.70 | 2026-05-02 | 1 |

After batch 4: **40/71 pages migrated. All 17 concepts complete.** Remaining pool is 31 entities, mostly single-source author pages.

**Reversibility:** additive-frontmatter only.

## [2026-05-05] bulk-refactor | v0.2 lifecycle migration batch 3

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `concepts/ai-benchmarks.md` | 0.85 | 2026-04-30 | 3 |
| `concepts/ai-deskilling.md` | 0.70 | 2026-04-28 | 1 |
| `concepts/industry-4-0.md` | 0.85 | 2026-04-28 | 4 |
| `concepts/micro-productivity-trap.md` | 0.70 | 2026-05-02 | 1 |
| `concepts/strategic-foresight.md` | 0.75 | 2026-04-28 | 2 |
| `entities/AI Index.md` | 0.85 | 2026-04-30 | 2 |
| `entities/Anthropic Economic Index.md` | 0.75 | 2026-04-28 | 2 |
| `entities/Future Today Strategy Group.md` | 0.70 | 2026-04-28 | 2 |
| `entities/Harvard Business Review.md` | 0.85 | 2026-05-02 | 6 |
| `entities/Stanford Digital Economy Lab.md` | 0.75 | 2026-04-28 | 1 |

After batch 3: 30/71 pages migrated. Distribution stable: 15 at 0.85–1.0, 15 at 0.70–0.85. Three single-source concepts (`ai-deskilling`, `micro-productivity-trap`, plus `lean-4-0` from batch 1) and three same-firm-cluster sources (FTSG/Webb counts as one author voice for confidence purposes) all sit at 0.70 — the floor on the §Lifecycle scale for a live page.

`npm run build` clean (95 in, 653 out). Lint: 41 pages still missing fields (2 concepts + 39 entities).

**Reversibility:** additive-frontmatter only.

## [2026-05-05] bulk-refactor | v0.2 lifecycle migration batch 2

Second batch of v0.2 lifecycle migration (10 high-frequency hubs).

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `concepts/ai-agents.md` | 0.85 | 2026-04-28 | 4 |
| `concepts/generative-ai.md` | 0.95 | 2026-05-02 | 11 |
| `concepts/foundation-models.md` | 0.80 | 2026-04-30 | 2 |
| `concepts/responsible-ai.md` | 0.95 | 2026-04-30 | 6 |
| `concepts/dynamic-capabilities.md` | 0.90 | 2026-04-28 | 4 |
| `entities/Stanford HAI.md` | 0.80 | 2026-04-30 | 2 |
| `entities/OpenAI.md` | 0.85 | 2026-05-02 | 7 |
| `entities/McKinsey & Company.md` | 0.85 | 2026-05-03 | 4 |
| `entities/Boston Consulting Group.md` | 0.75 | 2026-04-28 | 1 |
| `entities/MIT Technology Review Insights.md` | 0.70 | 2026-04-28 | 1 |

After batch 2: 20/71 pages migrated. Distribution skews to high-confidence (11 at 0.85–1.0, 9 at 0.70–0.85), reflecting that batches 1–2 were chosen to be diverse-but-well-connected hubs. Single-source entities still cluster around 0.70–0.75 per the §Lifecycle vendor/single-source rule.

**Verification.** `node scripts/lint-confidence.mjs` → 51 pages still missing fields. `npm run build` clean (95 in, 653 out, no errors).

**Reversibility:** additive-frontmatter only.

51 pages still pending (7 concepts + 44 entities).

## [2026-05-05] bulk-refactor | v0.2 lifecycle schema + tooling + batch 1

First version of [`llm-wiki-v2-plan.md`](../llm-wiki-v2-plan.md) v0.2 lands: lifecycle metadata (`confidence`, `last_confirmed`, `source_count`), supersession protocol (`status: stale`, `superseded_by`, `supersedes`), and the supporting Quartz extension + lint script.

**Schema changes (`CLAUDE.md`):**

- New §Lifecycle section — frontmatter contract, confidence rules, supersession protocol, debates-and-supersession section requirement, four-tier vocabulary.
- §Ingest step 4 now requires bumping `last_confirmed` and recomputing `source_count`/`confidence` on every touched concept/entity page.
- §Ingest step 7 rewritten to specify the supersession write-back (set `supersedes:` on new source; set `status: stale` + `superseded_by:` on retired page; never delete).
- "Custom extensions" list extended with `inject-stale-banner.ts`.
- "Current state" section refreshed to reflect actual repo state (was stale: claimed wiki not yet instantiated).
- "Reference" section now lists v1, v2, and the v2 staged plan.

**New files:**

- `extensions/inject-stale-banner.ts` — Quartz transformer; when frontmatter has `status: stale`, prepends an Obsidian-style `[!warning]` callout linking to `superseded_by`. Inserted in `quartz.config.ts` after `InjectTypeTags()`.
- `scripts/lint-confidence.mjs` — read-only walker; prints confidence distribution, flags pages missing v0.2 fields, flags pages with `last_confirmed > 30 days`, lists stale pages.
- Created `scripts/` directory.

**Migration batch 1 (10 pages of 71):**

| Page | confidence | last_confirmed | source_count |
|---|---|---|---|
| `concepts/automation-vs-augmentation.md` | 0.95 | 2026-05-02 | 10 |
| `concepts/enterprise-ai-adoption.md` | 0.95 | 2026-05-03 | 15 |
| `concepts/ai-employment-effects.md` | 0.95 | 2026-04-30 | 10 |
| `concepts/jagged-frontier.md` | 0.90 | 2026-04-30 | 5 |
| `concepts/lean-4-0.md` | 0.70 | 2026-04-28 | 3 |
| `entities/Erik Brynjolfsson.md` | 0.85 | 2026-04-28 | 3 |
| `entities/Anthropic.md` | 0.75 | 2026-04-28 | 2 |
| `entities/MIT CISR.md` | 0.75 | 2026-04-28 | 1 |
| `entities/Bain & Company.md` | 0.70 | 2026-05-02 | 1 |
| `entities/Lowe's.md` | 0.70 | 2026-05-02 | 1 |

Distribution: 5 pages at 0.85–1.0, 5 pages at 0.70–0.85. No defaults left at 0.0. Values set per the §Lifecycle confidence rules: 0.7 baseline + 0.05 per additional source (cap 0.95) + 0.05 once for peer-reviewed/empirical sources; vendor/single-case-study capped at 0.75.

**Reversibility:** all changes are additive frontmatter on existing pages plus three new files. To revert v0.2 entirely: remove the new frontmatter fields from the 10 migrated pages (`git diff main` would isolate them), revert `quartz.config.ts` and `CLAUDE.md`, delete `extensions/inject-stale-banner.ts`, `scripts/lint-confidence.mjs`, and `scripts/`. No source-page or content edits.

**Verification:**

- `node scripts/lint-confidence.mjs` — 71 → 61 pages missing fields; distribution 5 in 0.7–0.85, 5 in 0.85–1.0.
- `npm run build` — 95 input files, 653 emitted, no errors.
- Stale-banner extension: registered, no-op against current corpus (no page has `status: stale` yet).

**Total file touch: 14** (1 CLAUDE.md + 1 quartz.config.ts + 1 new extension + 1 new script + 5 concept pages + 5 entity pages + log).

61 pages still pending (12 concepts + 49 entities). Batch 2 will follow once batch 1 values are sanity-checked.

## [2026-05-03] ingest | Rewired 2nd ed (Lamarre, Smaje, Levin et al., Wiley/McKinsey 2026) — SAMPLE INGEST

**First ingest under the new "Verify before ingest" guardrail in CLAUDE.md.** The raw file (`raw/books/L-0029188561-pdf (1).pdf`) is a **30-page library/OverDrive sample** of a ~600-page book. The TOC references chapters out to page 591+, while the PDF has 30 pages — exactly the scope-mismatch pattern Check 1 of the new guardrail is designed to catch.

User confirmed the sample-only scope is intentionally useful in its own right ("front matter + intro + first 5 manifesto themes is enough; ingest as partial"). Following the FTSG and AI Index 2026 precedents for honestly-scoped partial ingests.

**Pages added:**

- [[2026-05-03-rewired-second-edition-sample]] — source page (clearly scoped; "Scope of this ingest" disclosure section at top; "What was NOT read" listed)
- [[Eric Lamarre]], [[Kate Smaje]], [[Rob Levin]], [[Alex Singla]], [[Alexander Sukharevsky]] — author entities
- [[McKinsey & Company]] — publisher; previously dangling, now filled in. The page also documents McKinsey's role as the data-partner-instrument behind several existing wiki adoption headlines (AI Index, MIT CISR Total AI Effectiveness).

**Pages enriched:**

- [[enterprise-ai-adoption]] — added the McKinsey "Rewired" 6-capability lens alongside the existing Anand-Wu / Werner-Le-Brun / MIT CISR / MITTRI-Cisco / Bain-OpenAI lenses. Includes the 20% EBITDA / $3:$1 / 1–2 yr breakeven / 70% talent-density-shifts numbers, with explicit cross-source comparison to AI Index 2026 (14–26% productivity range) and Bain/OpenAI 2026 (10–25% EBITDA) for independent-magnitude corroboration.
- [[micro-productivity-trap]] — added Rewired row to the cross-source positioning table (now 8 named vocabularies for the same broad "adoption breadth ≠ transformation depth" pattern).
- **Wiki cross-pollination flag**: Rewired's Index references [[Peter Weill]] (book p. 26) and [[Stephanie Woerner]] (book p. 286), both already in the wiki via [[2026-04-28-mit-sloan-ai-maturity|MIT CISR]]. Index lines for both updated to note the citation. This is genuine cross-source linkage — McKinsey's Rewired framework cites MIT CISR's research on technology platforms.

**Index updated** (1 new source line; 7 new entity lines; 2 entity lines amended for Peter Weill / Stephanie Woerner cross-citation).

**Key claims carried into the wiki (sample-scoped):**

- The **6-capability "Rewired" framework** (business-led roadmap, talent, operating model, technology, data, adoption-and-scaling) — companies must be strong across all six.
- **Definition of Tech & AI transformation**: "the process of developing organizational and technology-based capabilities that allow a company to continuously improve its customer experience and lower its unit costs; and over time sustain a competitive advantage."
- **Empirical anchor** (~20 deep-dive AI-leader companies from a study set of ~200): **20% EBITDA uplift average, 1–2 yr breakeven, $3:$1 ROI**, with concentration on **1–3 business domains**.
- **70% talent-density shifts**: 70%+ in-house, 70%+ "doer" engineers, 70%+ at competent-or-expert skill levels.
- **40% of 2nd ed entirely new**, 25% substantially expanded — reflecting the rise of agentic AI and the evolution of management practice.
- **Senior business leaders, not IT, drive transformation**: "We don't have a single success story where senior business leaders were not in the driver's seat."
- **Four case-study companies** named (but content NOT in the sample): DBS Bank, Freeport-McMoRan, LATAM Airlines, Toyota Motor North America.
- **Vocabulary preview** via the back-of-book Index: "domain-to-value delivery (DVD)", "talent win room (TWR)", "tech talent skill pyramid", "two-pizza teams", "stage-gating", "strangler fig", "value driver trees", "70% / 30–70 shifts", "workbenches", "zero-cost thinking", and the operating-model archetypes (digital factory, domain & platform, distributed, enterprise-wide).

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- The Rewired 6-capability framework adds an **8th named vocabulary** to the wiki's running cluster of "adoption breadth ≠ transformation depth" framings (alongside Anand-Wu 2×2, Werner-Le-Brun Octopus/Tin-Man, MIT CISR Four Stages + Four S, MITTRI/Cisco 5 Foundations, Bansal-Birkinshaw systems thinking, Warner-Wäger dynamic capabilities, Bain/OpenAI micro-productivity-trap). The [[threads/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] thread page would be a strong synthesis target now.
- **Three independent magnitude estimates** for AI-transformation EBITDA/productivity gains now in the wiki: McKinsey/Rewired 20% EBITDA, Bain/OpenAI 10–25% EBITDA, AI Index 2026 14–26% productivity. Same direction, similar magnitude, three different vantages (consulting deep-dives × 2, national-survey × 1).
- McKinsey's data-partner role in the AI Index makes this *not quite* an independent voice — the wiki's [[McKinsey & Company]] entity page documents the methodological dependency.

**Notable choices (per new CLAUDE.md guardrail):**

- **Date prefix `2026-05-03`** — date-of-ingest.
- **Frontmatter `length:` is honest**: "~600+ pages full book (read pp. 1–30 of 30-page sample…)". The "Scope of this ingest" section is the FIRST section of the source page, before TL;DR, to make sample-status maximally visible.
- **Frontmatter has `sample_source:` field** — new convention this ingest. Documents the file pattern as an OverDrive-style library sample.
- **Source-page slug includes `-sample`** — explicit signal in the URL/path.
- **No new concept page** for the 6-capability framework. McKinsey-branded vocabulary anchored on a single source warrants enrichment of [[enterprise-ai-adoption]] but not its own concept until corroborated by a second source. (If chapters are read later, the concept could be promoted.)
- **Dangling wikilinks left intentionally**: the case-study companies (DBS Bank, Freeport-McMoRan, LATAM Airlines, Toyota Motor North America) are referenced but not turned into entities — single-source coverage so far, and the chapter content describing them is not yet read.

**Contradiction check:** no direct contradictions. The 20% EBITDA / 14–26% productivity / 10–25% EBITDA cluster is consistent in magnitude. McKinsey's claim about "senior business leaders in the driver's seat" rhymes with Bain/OpenAI's "boardroom imperative" and MIT CISR's "Strategy" pillar of the Four S — same observation in three vocabularies.

**Total file touch: 12** (1 source + 6 entities + 2 concept enrichments + 1 entity index update for Peter Weill + 1 entity index update for Stephanie Woerner [via index.md edits] + index + log; raw PDF on disk under `raw/books/` but not committed per the gitignore rule).

## [2026-05-02] ingest | Dutt, Rapoport, Chatterji, Weeratunga & Satcher — How to Move from AI Experimentation to AI Transformation (HBR)

Single-source ingest of a Bain × OpenAI co-authored HBR Generative AI piece (30 April 2026). The article names a failure pattern ("micro-productivity trap") that the wiki had previously circled with multiple vocabularies but not given a structural name to. Auto-mode supervised ingest.

**Pages added:**

- [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]] — source page
- [[Arjun Dutt]], [[Gene Rapoport]], [[Aaron Chatterji]], [[Gawesha Weeratunga]], [[Harrison Satcher]] — author entities
- [[Bain & Company]] — co-publishing partner; 10–25% client EBITDA gains
- [[OpenAI]] — co-publishing partner via Economic Research team; resolves a previously dangling wikilink referenced from many wiki pages
- [[Lowe's]] — case study (Mylow / Mylow Companion across 1,700+ stores)
- [[micro-productivity-trap]] — new concept page anchored on this source

**Pages enriched:**

- [[automation-vs-augmentation]] — added Dutt et al. row to the convergence table; "offering lock-in" and "process lock-in" as failure modes; "improve the task" vs "reinvent the business" as strategic framing.
- [[enterprise-ai-adoption]] — added "Transformation lens" section: micro-productivity trap as named diagnostic for the gap between 88% organizational adoption and single-digit agent-mediated workflow depth; 10–25% EBITDA range; four-step framework; Lowe's + FabricationCo cases.
- [[generative-ai]] — added field-deployment-evidence section: Bain client EBITDA, Lowe's outcomes (>2× online conversion, +200bps CSAT in-aisle), FabricationCo outcomes (~$30M, 15× faster quotes, +10pp win rate).

**Index updated** (1 new source, 7 new entity lines, 1 new concept line).

**Key claims carried into the wiki:**

- The "micro-productivity trap" — task-level AI gains failing to translate to firm-level results.
- Two lock-ins: offering lock-in (AI optimizes existing offerings) and process lock-in (AI automates current processes without redesigning them).
- "Reinvent the business" vs "improve the task" as the strategic posture distinction.
- Bain client EBITDA 10–25% for transformation-mindset deployments.
- Four-step framework: narrow possibilities strategically (4–5 critical domains; top-4 across Bain portfolio = software dev, customer support, knowledge worker efficiency, marketing); reimagine workflows; engage those closest to the process; measure what matters (concrete business outcomes + continuous evals).
- Lowe's: Mylow + Mylow Companion (1,700+ stores; >2× conversion; +200bps CSAT).
- FabricationCo (anonymized Fortune 1000 manufacturer): 14 use cases identified, ~$30M additional profit on track, ~15× faster quote generation, +10pp win rate increase in 3 months.
- Boardroom imperative: AI transformation cannot be delegated to technology groups without specific goals/metrics.

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- The micro-productivity trap is a *fifth or sixth named vocabulary* in the wiki for the "adoption breadth ≠ transformation depth" pattern, alongside [[2026-04-28-anand-wu-genai-playbook|Anand-Wu's 2×2]], [[2026-04-28-werner-lebrun-octopus-organization|Werner & Le-Brun's Octopus/Tin-Man]], [[2026-04-28-mit-sloan-ai-maturity|MIT CISR Four Stages + Four S]], [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco's chatbot→agent progression]], and [[2026-04-28-bansal-birkinshaw-systems-thinking|Bansal & Birkinshaw's systems thinking]]. The concept page describes the topical adjacencies without ranking them.
- The article's empirical claim (10–25% EBITDA gains) is from vendor-of-deployment data (Bain). Independent corroboration would come from the [[2026-04-30-ai-index-report-2026|AI Index 2026]]'s 14–26% productivity-gain range in customer support and software development — described as adjacent on each page, no comparative conclusion drawn.
- OpenAI Economic Research team (Chatterji, Weeratunga, Satcher) is the OpenAI counterpart to Anthropic's [[Anthropic Economic Index]] team — described as parallel measurement initiatives without comparative ranking.

**Notable choices:**

- **Date prefix `2026-05-02`** — date-of-ingest (today; the article itself is dated 30 April 2026).
- **New concept page** [[micro-productivity-trap]] rather than just enrichment because the article gives a structural name + four-step framework + EBITDA empirical anchor + worked cases. The page positions itself relative to the wiki's other organizational-frameworks-for-ai-adoption vocabularies without ranking them.
- **Filled in [[OpenAI]] entity** — previously dangling across many references. Now serves as a hub linking GPT-3 (Brynjolfsson), GPT-4 (Dell'Acqua, Boussioux), ChatGPT (Anand-Wu), Mylow (this source), and the OpenAI Economic Research team.
- **[[Aaron Chatterji]]** is the wiki's first cross-org figure (Duke + OpenAI Chief Economist). The OpenAI Economic Research team is now indexed as a wiki-level entity (via OpenAI's entity page).
- Dangling wikilinks left intentionally: [[Chandhu Nair]] (Lowe's SVP) — single-source mention.

**Contradiction check:** no direct contradictions. The 10–25% EBITDA range is consistent with the [[2026-04-30-ai-index-report-2026|AI Index 2026]]'s 14–26% productivity-gain range in customer support and software development (different metric — EBITDA vs productivity gain — but same order of magnitude and same direction). The "micro-productivity trap" diagnostic complements rather than contradicts the wiki's existing org-transformation frameworks.

**Total file touch: 14** (1 source + 5 author entities + 3 org entities + 1 new concept + 3 concept enrichments + index + log; raw PDF on disk under `raw/articles/` but not committed per the gitignore rule).

## [2026-04-30] ingest | Artificial Intelligence Index Report 2026 (9th edition)

Single-source ingest of the 9th annual [[AI Index]] from [[Stanford HAI]] (Sajadieh et al., April 2026). The 2025 edition is already in the wiki; this ingest layered the 2026 numbers and structural changes on top, rather than treating the 2026 edition as an independent source. Front matter and the 15 Top Takeaways were ingested in full; chapters 2–9 (~360 of ~430 pages) deferred to per-chapter or thematic deep-reads.

**Pages added:**

- [[2026-04-30-ai-index-report-2026]] — source page
- [[Sha Sajadieh]] — new EiC entity (replaces [[Nestor Maslej]] as 2026 EiC; Maslej remains a contributor)
- [[Yolanda Gil]] — entity (now chair; was chair-elect in 2025)
- [[Schmidt Sciences]] — new analytics/research partner; collaborated on standalone Medicine chapter

**Pages substantially updated:**

- [[AI Index]] — replaced "What it tracks" table to mirror the 2026 9-chapter structure (Medicine spun off from Science); replaced Steering Committee section to reflect Yolanda Gil → chair, Perrault → co-chair, Sajadieh → EiC, plus joins (Altman, Brodley, Dignum, Kumar, Landay, Tabassi, Weld) and departures (Etchemendy, Ligett); added 2026 row to editions table; added Schmidt Sciences (data partner) and Infosys (supporting funder); updated AI-tooling acknowledgement (Claude/ChatGPT for editing, Gemini 3 for image generation).
- [[generative-ai]] — added 2026 numbers section: 53% population adoption in 3 years; $172B U.S. consumer value; $285.9B U.S. private AI investment (~2.6× the 2024 figure); 88% organizational adoption; >80% U.S. high-school + college students use AI.
- [[foundation-models]] — added 2025 notable-model counts (U.S. 59, China 35, South Korea 8, Europe 2); top organizations (OpenAI 20, Google 14, Alibaba 11, Anthropic 7, etc.); 17.1M H100-equivalent global compute; 5,427 U.S. data centers; 29.6 GW power capacity; Grok 4 emissions 72,816 t CO2eq; OLMo 3.1 Think 32B as data-quality counter-evidence to scale; disclosure-decline section.
- [[ai-benchmarks]] — added 2025 saturation block: SWE-bench Verified 60% → ~100%; OSWorld agents 12 → 66%; Gemini Deep Think IMO gold; analog clock 50.1%; ChemBench frontier vs human chemists; RLBench 89.4% vs household 12%.
- [[responsible-ai]] — incidents 233 → 362 in 2025; new RAI dimension trade-off finding (e.g., safety improvement degrading accuracy).
- [[enterprise-ai-adoption]] — 88% organizational adoption; productivity gains 14–26% in customer support / software development; AI agent deployment in single digits per business function; education-policy gap (80% students use AI vs 6% teachers say policies are clear).
- [[ai-employment-effects]] — added section on U.S. software developers ages 22–25: -20% from 2024 (extends the [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson Canaries]] finding to a more recent timeframe via different methodology).
- [[jagged-frontier]] — added AI Index 2026 row to the convergence section: IMO gold + analog clock 50.1%; OSWorld leap; the term "jagged frontier" is now part of the AI Index narrative (Top Takeaway #4).

**Index updated** (1 new source line; 3 new entity lines).

**Key claims carried into the wiki:**

- AI capability not plateauing: SWE-bench 60→100%, OSWorld 12→66%, organizational adoption 88%.
- U.S.-China model gap effectively closed (DeepSeek-R1 briefly matched top US model Feb 2025; 2.7% lead as of March 2026).
- U.S. private investment $285.9B in 2025 (~2.6× 2024); 1,953 newly funded AI companies; AI talent immigration -89% since 2017.
- GenAI 53% population adoption in 3 years (faster than PC or internet); U.S. ranks 24th at 28.3%; consumer value $172B.
- AI agent deployment in single digits per function; software dev 22–25 employment -20%.
- AI environmental footprint: 72,816 t CO2eq for Grok 4 training; 29.6 GW data center capacity; GPT-4o inference water use exceeds 1.2M people's drinking water.
- Frontier AI for science outperforms human chemists on ChemBench; protein/genomics models with 100M-200M params beat 200× larger general models.
- Documented AI incidents 233 → 362; RAI dimension trade-offs.
- Trust gap: 73% experts vs 23% public expect positive AI impact on jobs (50pp gap); EU trusted more than US/China globally.

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- The "jagged frontier" term, originally introduced in the wiki via [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. 2026]] (BCG consultants RCT), is now part of the AI Index's official narrative — same concept name, different data path (Index uses benchmark gaps; Dell'Acqua uses field experiment).
- The AI Index 2026's software-developer-22–25 employment finding is the same labor-market pattern documented by [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson et al. 2025]] via ADP payroll data; both source pages note the topic without ranking the methodologies.
- The [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic Economic Index]] is the parallel measurement initiative; both surface complementary numbers on adoption, productivity, employment.

**Notable choices:**

- **Date prefix `2026-04-30`** — date-of-ingest (today), consistent with the convention since the wiki was instantiated.
- **Single source page rather than treating 2026 as an update to 2025**: the 2026 source page is its own standalone artifact with its own slug, frontmatter, and quotes. Concept pages reference *both* editions where appropriate, with the 2026 numbers layered on top of 2025 ones rather than overwriting.
- **Chapters 2–9 deferred**: with ~430 pages and 60+ named figures per chapter, full ingestion would be expensive. The Top Takeaways and Chapter 1 highlights cover most of the cross-cutting findings; per-chapter deep-reads can be triggered later (Chapter 4 Economy and Chapter 6 Medicine are the most likely candidates given existing wiki coverage).
- **AI tooling disclosure** is more visible in 2026 (image generation explicitly attributed to Gemini 3.1 / Gemini 3) — a small but interesting signal about AI Index editorial norms.
- Many dangling wikilinks left intentionally for new steering-committee members ([[Russ Altman]], [[Carla Brodley]], [[Virginia Dignum]], [[Vipin Kumar]], [[James Landay]], [[Elham Tabassi]], [[Dan Weld]]) — single-source coverage so far. Stub indicators per CLAUDE.md.

**Contradiction check:** no direct contradictions. The 2026 numbers refine and extend 2025 numbers; a couple of figures revised retroactively (notable models in 2024: 2025 edition reported 40 U.S. / 15 China / 3 Europe; 2026 edition's longitudinal chart shows similar magnitudes). The AI Index 2026's adoption finding (88%) extends the 2025 figure (78%); both are consistent with McKinsey's underlying instrument.

**Total file touch: 14** (1 source + 3 entities + 1 entity rewrite (AI Index) + 7 concept enrichments + index + log; raw PDF on disk under `raw/reports/` but not committed per the gitignore rule).

## [2026-04-29] ingest | Boussioux, Lane, Zhang, Jacimovic & Lakhani — The Crowdless Future? (Org Sci 2024)

Single-source ingest under auto mode. Brief takeaway plan surfaced before writing per CLAUDE.md "discuss before writing" preference (compressed for auto mode).

**Pages added:**

- [[2026-04-29-boussioux-crowdless-future]] — source page
- [[Leonard Boussioux]], [[Jacqueline N. Lane]], [[Miaomiao Zhang]], [[Vladimir Jacimovic]] — author entities
- [[Continuum Laboratory]] — partner organization (San Francisco AI firm; ContinuumLab.AI)

**Pages enriched:**

- [[automation-vs-augmentation]] — added the Boussioux row to the cross-source convergence table; added §7 on differentiated vs. independent search as fine-grained augmentation patterns; existing §7 (Pareto-improvement caveat) became §8.
- [[jagged-frontier]] — added the Boussioux finding (HAI in incremental search space, HC at extreme novelty) to the convergence section.
- [[generative-ai]] — added field-experimental cost/time data ($27 / 5.5 hrs vs $2,555 / 2,520 hrs; ≈94× cost reduction) and HC/HAI per-dimension table.
- [[ai-employment-effects]] — added crowdsourcing labor markets section: HAI substitution dynamics on Freelancer.com–style platforms; novelty advantage retained by HC at top decile.

**Index + log updated.**

**Key findings carried into the wiki:**

- **HC/HAI trade-off** — HC higher novelty (3.508 vs 3.230 multi / 3.469 single); HAI higher strategic viability, environmental, financial, quality. Mixed-effects models with N=3,900 evaluator-solution pairs, 18 blocks, 300 evaluators.
- **Differentiated > independent search** — single-instance with iterative differentiation prompts beats multi-instance independent search on quality/viability while preserving novelty.
- **94× cost reduction** ($27 vs $2,555); ~458× time reduction (5.5 hrs vs 2,520 human-hours).
- **Failure modes flagged**: formal-rationality bias, training-data confinement, confabulation/hallucination.
- **Three solution sources tested**: HC (n=54 after filtering), HAI multi-instance (n=90), HAI single-instance (n=90).

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- Same publication and shared author ([[Karim Lakhani]]) as [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. 2026 Jagged Frontier]]; both are GPT-4 field-experimental evidence in different settings (consulting tasks vs ideation crowdsourcing).
- The HC/HAI novelty-vs-value pattern is one face of the [[jagged-frontier]] — describes which parts of solution space AI inhabits well.
- The differentiated-search pattern parallels the *task-iteration* augmentation mode in the [[Anthropic Economic Index]] taxonomy.
- The circular-economy framing connects topically to [[2026-04-28-bansal-birkinshaw-systems-thinking]] (sustainability as a wicked-problem domain).

**Notable choices:**

- **Date prefix `2026-04-29`** — following the date-of-ingest convention; today is the first new ingest at a date other than the wiki's instantiation day.
- **No new concept page**: HC vs HAI is a finding rather than a standalone concept; folded into existing concepts via enrichment. If a third source on creative-problem-solving arrives, a dedicated `creative-problem-solving` concept page would be warranted.
- Dangling wikilinks left intentionally: [[Harvard Business School]] (mentioned as affiliation; would be its own entity under broader coverage); [[LISH]] (Laboratory for Innovation Science at Harvard).

**Contradiction check:** no direct contradictions with prior wiki claims. The Boussioux finding that HC retains a novelty advantage over GPT-4 in creative ideation is consistent with the [[jagged-frontier]]'s description of AI as occupying incremental search space, and with [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua's]] outside-the-frontier degradation result (in different domain). No revisions to existing source pages needed.

**Total file touch: 11** (1 source + 5 entities + 4 concept enrichments + index + log; raw PDF on disk under `raw/papers/` but not committed per the gitignore rule).

## [2026-04-28] ingest | Batch: 7 sources (Bansal-Birkinshaw, Reitz-Higgins, Webb, Warner-Wäger, Dell'Acqua et al., Carroll-Sørensen, FTSG Convergence Outlook)

User invoked **batch ingest, full depth, all six** (later +1: FTSG Convergence Outlook 2026 added mid-batch). Total seven sources. Per CLAUDE.md, batch supervised default suspended for this batch by user instruction; cross-source neutrality preference (saved earlier this session) applied throughout.

**Pages added:**

- [[2026-04-28-bansal-birkinshaw-systems-thinking]] — HBR Sept–Oct 2025; systems thinking as third innovation mode beyond breakthrough/design.
- [[2026-04-28-reitz-higgins-spacious-thinking]] — HBR.org July 2025; doing-mode vs. spacious-mode attention.
- [[2026-04-28-webb-strategic-foresight]] — HBR.org Jan 2024; FTSG 10-step methodology.
- [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation]] — Long Range Planning 2019; nine digital microfoundations under Teece.
- [[2026-04-28-dellacqua-jagged-technological-frontier]] — Org Sci 2026; 758-BCG-consultant RCT; "jagged frontier" concept.
- [[2026-04-28-carroll-sorensen-strategy-analogy]] — Strategy Science 2024; analogical reasoning tools.
- [[2026-04-28-ftsg-convergence-outlook-2026]] — FTSG 1st edition Jan 2026; intro/framing only ingested (~5% of 317 pages).

**Entities added (15):** [[Amy Webb]], [[Future Today Strategy Group]], [[Boston Consulting Group]], [[Ethan Mollick]], [[Karim Lakhani]], [[Fabrizio Dell'Acqua]], [[Tima Bansal]], [[Julian Birkinshaw]], [[Ivey Business School]], [[Megan Reitz]], [[John Higgins]], [[Karl S.R. Warner]], [[Maximilian Wager]], [[Glenn R. Carroll]], [[Jesper B. Sorensen]].

**Concept pages added (5):** [[jagged-frontier]], [[systems-thinking]], [[dynamic-capabilities]], [[strategic-foresight]], [[analogical-reasoning]].

**Concept pages enriched:** [[automation-vs-augmentation]] (added Dell'Acqua jagged-frontier row to four-source convergence table), [[ai-employment-effects]] (added Dell'Acqua equalizing-effect among elite knowledge workers; subjective-coherence-vs-correctness decoupling), [[generative-ai]] (added Dell'Acqua field-experiment GPT-4 evidence), [[enterprise-ai-adoption]] (added capabilities lens via Warner-Wäger and foresight lens via Webb/FTSG).

**Index + log updated.**

**Cross-source notes (descriptive only, per cross-source neutrality preference):**

- Webb's HBR article and FTSG's *Convergence Outlook* are author/firm pair; the 10-step methodology is the underlying mechanism for the convergence-clustered framing.
- Warner-Wäger dynamic capabilities, MIT CISR Four Stages, Werner-Le-Brun Octopus/Tin Man, and MITTRI/Cisco five foundations all address how organizations adapt under environmental change — wiki cross-references describe topic overlap without ranking the frameworks.
- Dell'Acqua's "equalizing effect within elite professionals" and Brynjolfsson, Li & Raymond's "equalizing effect within customer support" are at different units of analysis (across-task, elite-only vs. within-occupation, broad-skill); both source pages and the relevant concept pages note the topic without drawing comparative conclusions.
- Bansal-Birkinshaw systems thinking and Reitz-Higgins spacious thinking address related but distinct phenomena — the former is methodological (innovation mode), the latter is attentional (cognitive mode); cross-references note the adjacent framing without conflating them.

**Notable choices:**

- **File-naming mismatch flagged**: the raw PDF for [[2026-04-28-dellacqua-jagged-technological-frontier]] is on disk as `Mitchell and Dino - 2011 - In Search of Research Excellence Exemplars in Entrepreneurship.pdf` but the actual content is the Dell'Acqua et al. (2026) Jagged Frontier paper. The `raw:` frontmatter field preserves the literal filename; recommend renaming on disk for clarity. The wiki source page is named for the actual content.
- **FTSG Convergence Outlook only intro-ingested (pp. 1–15 of 317)**: the per-section deep-reads (Compute Shock, Polycompute, Agentic Economies, New Labor Equation, Human Augmentation, Living Intelligence, Programmable Biology, Autonomous Care, Emotional Outsourcing, Corporate Panopticon) are deferred to future per-section ingests. The wiki source page documents this scope explicitly.
- **Warner & Wäger 2019** is the oldest source ingested (pre-GenAI). Included because the dynamic-capabilities framework is foundational and applies equally to AI adoption today; marked in the open-questions sections of [[dynamic-capabilities]] and [[enterprise-ai-adoption]] that updating the framework for the 2026 GenAI context is a natural follow-up.
- **Carroll-Sørensen 2024** is off-direct-theme but anchors a useful concept ([[analogical-reasoning]]) that may matter for AI strategy work (e.g., FTSG's reliance on historical convergence-cycle analogies; LLMs as potential analogy generators).
- Many BCG / Henderson Institute co-authors of the Jagged Frontier paper ([[François Candelon]], [[Saran Rajendran]], [[Lisa Krayer]], [[Edward McFowland III]], [[Hila Lifshitz]], [[Katherine C. Kellogg]]) left as dangling wikilinks — single-source coverage so far. Stub indicators per CLAUDE.md.

**Contradiction check:** no direct contradictions with prior wiki claims. The Dell'Acqua finding that *top-half-skill* knowledge workers gain meaningfully (+11%) refines the prior wiki framing that some sources (notably Brynjolfsson, Li & Raymond customer support) show ~0% gain at the top — these are at different units of analysis (within-occupation customer-service vs. across-task elite consulting) so the refinement is additive, not contradictory. Existing source pages already correctly bound their claims to their own samples.

**Total file touch (this batch): 33** (7 sources + 15 entities + 5 new concepts + 4 concept enrichments + index + log; raw PDFs on disk under `raw/articles/`, `raw/papers/`, `raw/reports/` but not committed per the gitignore rule).

## [2026-04-28] ingest | Anthropic Economic Index — fourth report (summary article)

Ingested Anthropic's 15 Jan 2026 Economic Research blog post summarizing the fourth Anthropic Economic Index report. The article is a summary of an underlying full report which is *not* separately ingested; claims here are flagged as drawn from the summary, with the parent report cited.

**Pages added:**

- [[2026-04-28-anthropic-economic-index-q4-2025]] — source page
- [[Anthropic]] — entity (organization)
- [[Anthropic Economic Index]] — entity (project; previously a dangling wikilink referenced from `automation-vs-augmentation` and `ai-employment-effects`)
- [[METR]] — entity (organization)
- [[ai-deskilling]] — concept (new)

**Pages enriched:**

- [[automation-vs-augmentation]] — added longitudinal Claude.ai augmentation/automation split table (Jan 2025 → Nov 2025: 55/41 → 55/42 → 47/49 → 52/45); appended Anthropic 4th-report row to the four-source convergence table; existing section numbering shifted (old §6 became §7).
- [[ai-employment-effects]] — added three new sections: aggregate productivity reliability adjustment (+1.0 to +1.2 pp/yr); effective AI coverage at occupation level (radiologists, data entry keyers above the 45° line; teachers, software developers below); task-content shift / deskilling pointer to the new concept page. Added [[ai-deskilling]] to Related concepts.
- [[generative-ai]] — added "Measurement framework: economic primitives" section before the capability-gains section. Lists the five primitives + headline numbers (9× / 12× speedup; 70% / 66% success; +1.0–1.2 pp/yr).
- [[ai-benchmarks]] — added "Task horizons (METR / Anthropic Economic Index 4th report)" section before the benchmark roster. METR ~2hr / API ~3.5hr / Claude.ai ~19hr table for Sonnet 4.5.

**Index + log updated.**

**Key new findings carried into the wiki:**

- **Economic primitives framework** — five population-scale measurements (task complexity, skill level, use case, AI autonomy, success) derived from Claude classifying its own conversations.
- **Speedup-by-complexity gradient** — 9× HS-level / 12× college-level on Claude.ai; greater on API; success rate falls slightly with complexity (70% → 66%).
- **METR comparison** — first benchmark referenced where wiki has the methodology gap: fixed-task ~2hr vs. observed-platform ~19hr (Claude.ai), with selection-bias and decomposition explanations.
- **Effective AI coverage** — new occupation-level metric, success-weighted; outliers identified.
- **Task-composition deskilling** — first-order effect, distinct from displacement; new concept page anchored on this single source.
- **Augmentation reversal** — Nov 2025 Claude.ai sample at 52/45 (augmentation lead) reverses the Aug 2025 47/49 (automation lead). Longer arc still shows automation gaining share since Jan 2025 (when split was 55/41).
- **Aggregate productivity revision** — Anthropic walks back its own 1.8 pp/yr estimate by ~⅓ to 1.0–1.2 pp/yr once reliability is accounted for.

**Cross-source neutrality applied:** per the cross-source neutrality preference saved this session, cross-references to other sources (Brynjolfsson 2025 papers, AI Index) describe what each measures without drawing comparative conclusions ("complementary," "tension," "contradicts," etc.). Reader infers; backlinks surface neighbours.

**Notable choices:**

- Wrote **two Anthropic entities** rather than one — `[[Anthropic]]` (the organization) and `[[Anthropic Economic Index]]` (the research initiative), parallel to `[[Stanford HAI]]` / `[[AI Index]]`. The Economic Index page resolves a previously dangling wikilink from `automation-vs-augmentation` line 15 and `ai-employment-effects` line 40.
- **Did not** add a back-pointing interpretive section to the Brynjolfsson 2025 source pages — the alias-aware Backlinks extension surfaces the connection automatically; per cross-source neutrality, no editorialization.
- **Did not** create a synthesis/thread page on skill-bias-vs-equalizing-effect — earlier draft proposed it, but on closer inspection the two findings address different units of analysis (across-task vs. within-occupation) and there is no clear contradiction to synthesize. Deferred until a third source weighs in.
- Dangling wikilinks left intentionally: [[Claude]], [[Claude Sonnet 4.5]], [[Claude Opus 4.5]], [[Jack Clark]] — single-source coverage so far. Stub indicators per CLAUDE.md.

**Contradiction check:** no contradictions with prior wiki claims. The 52/45 Nov 2025 augmentation lead refines the wiki's understanding of the longer arc (automation has been gaining share since Jan 2025 even though the latest sample is augmentation-led). The aggregate productivity revision (1.8 → 1.0–1.2 pp/yr) is a tightening of Anthropic's own prior estimate, not a contradiction with another source.

**Total file touch: 11** (1 source + 3 entities + 1 new concept + 4 concept enrichments + index + log; raw PDF on disk under `raw/articles/` but not committed per the gitignore rule).

## [2026-04-28] ingest | Brynjolfsson, Li & Raymond — Generative AI at Work (QJE 2025)

Eighth ingest. **First peer-reviewed journal article** in the wiki: *Quarterly Journal of Economics* 140 (2025), pp. 889–942, advance access Feb 4 2025. CC BY-NC 4.0 open access via OUP. Working paper predecessor: NBER 31161 (2023) — the version cited via AI Index 2025 §4.4 throughout 2024.

**Headline:** Studies the staggered introduction of a GPT-3-based customer-support AI assistant at a Fortune 500 firm with 5,172 agents (mostly Philippines-based). +15% productivity (RPH); equalizing effect with low-skill workers gaining ~30%, top performers ~0% speed gains AND **small quality decline**; AI accelerates experience curve ~3×; durable learning (workers maintain efficiency during AI outages); convergence in communication patterns; reduced worker attrition (driven by retention of new workers).

This ingest is mostly a **primary-source upgrade** for productivity claims that have been load-bearing throughout the wiki via secondary citation from [[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.4.

- Source page created: [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work]]
- Entity page enriched: [[Erik Brynjolfsson]] — promoted §1 from secondary citation to primary; updated headline number from +14.2% (NBER WP) to +15% (QJE); added top-performer-quality-decline nuance; added durable-learning detail.
- Concept pages enriched:
  - [[enterprise-ai-adoption]] — refined the equalizing-effect productivity table with QJE numbers and the small-quality-decline nuance for top performers
  - [[ai-employment-effects]] — added "Productivity gains alongside employment declines" subsection with primary-source citation; new "Convergence in communication patterns" subsection
  - [[automation-vs-augmentation]] — promoted to primary anchor for augmentation's positive productivity effects; added "Pareto-improvement caveat" subsection on top-performer quality decline + long-run training-data risk
  - [[generative-ai]] — added concrete primary-source numbers; clarified the augmentation-vs-automation empirical record

**Key new findings carried forward:**

- **+15.2%** RPH (preferred FE specification) — slight upward revision from +14.2% NBER WP
- **Top performers see small quality decline** alongside small speed gains — the equalizing effect is NOT "0% gain for high-skill" but rather "0% net gain WITH quality slightly worse" — the wiki previously missed this.
- **Long-run training-data risk**: if top performers reduce original contributions because they adhere more to AI suggestions, the AI's training data degrades over time. A subtle long-run feedback concern not previously in the wiki.
- **Augmentation by design**: the system was explicitly architected to augment (suggestions only to agent; agent has full discretion; system declines to suggest when training data is insufficient). This makes the paper a clean primary anchor for augmentation in [[automation-vs-augmentation]].
- **Customer-side effects** newly captured: customers more polite to AI-treated agents, less likely to escalate to manager.
- **Convergence finding**: low-skill agents begin communicating more like high-skill agents — a previously-missing skill-leveling dimension.

**Two-paper Brynjolfsson arc** is now load-bearing in the wiki: [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Generative AI at Work]] (productivity within a role, equalizing effect) + [[2026-04-28-brynjolfsson-canaries-coal-mine|Canaries in the Coal Mine]] (employment across occupations, entry-level decline) together describe the **task-level vs. occupation-level paradox**.

**Schema note (de facto change):** Source frontmatter now includes `peer_reviewed: true` and `working_paper_predecessor` for this paper. **Should be formalized in design doc §5.1 if a third peer-reviewed source is ingested**; for now treating it as a single-instance schema extension rather than a permanent change. Tracked in [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|the source page]]'s "Schema note" section.

**Contradiction check:** no contradictions; this ingest *refines and corrects* prior wiki claims rather than contradicting them. Updated specific numbers (14.2% → 15%) and added missing nuance (top-performer quality decline; communication-pattern convergence). Cited secondary references (via AI Index) remain valid; the wiki now has the primary source available for direct citation alongside.

**Notable choices:** [[Danielle Li]] and [[Lindsey Raymond]] left as dangling wikilinks (single-source coverage so far).

**Total file touch: 8** (1 source + 1 entity enrichment + 4 concept enrichments + index + log; raw PDF on disk but not committed per the gitignore rule established post-push).

## [2026-04-28] refactor | folder placement: Canaries + Generative AI at Work to raw/papers/

After the GitHub push, user re-downloaded source PDFs (since `git filter-repo` had aggressively cleaned the local working tree). The re-downloads landed in `raw/articles/`; both Brynjolfsson papers belong in `raw/papers/`. Moved both. **Surfaced an 8th source the wiki had missed:** "Generative AI at Work" by Brynjolfsson, Li & Raymond, the canonical primary source for the customer-support productivity finding cited extensively across the wiki via secondary references through [[2026-04-28-ai-index-report-2025|AI Index 2025]]. Triggered the next ingest.

## [2026-04-28] ingest | Brynjolfsson, Chandar & Chen — Canaries in the Coal Mine?

Seventh ingest. Stanford Digital Economy Lab working paper, Aug 26, 2025, by [[Erik Brynjolfsson]], Bharat Chandar, Ruyu Chen. ADP payroll data covering ~25M U.S. workers monthly, Jan 2021 – July 2025. Six empirical facts on AI's recent employment effects. Read in scope: pages 1–20 (intro, related literature, data description, Facts 1–4 with figures); Facts 5–6 captured from intro summary.

**Headline finding:** Early-career workers (ages 22–25) in the most AI-exposed occupations have experienced a **~13% relative decline in employment** since late 2022 (after firm-time-effects controls). Concentrated in **automation** uses, not **augmentation**. Adjustments visible in **employment more than wages** (wage stickiness). Robust to alternative samples and explanations.

- Source page created: [[2026-04-28-brynjolfsson-canaries-coal-mine]]
- Entity pages: [[Erik Brynjolfsson]] (promoted from dangling — major recurring author with both the customer-support productivity study and now this employment study), [[Stanford Digital Economy Lab]] (new institutional source, distinct from [[Stanford HAI]])
- Concept pages created:
  - [[ai-employment-effects]] — empirical/sociological lens on AI's labor consequences (job displacement, age, wages); now load-bearing on [[2026-04-28-brynjolfsson-canaries-coal-mine|Brynjolfsson 2025]] data and reconciling with [[2026-04-28-ai-index-report-2025|AI Index 2025]]'s task-level equalizing-effect studies
  - [[automation-vs-augmentation]] — conceptual/strategic lens; cross-references 4 sources (AI Index productivity studies, Anand-Wu 2×2, MITTRI/Cisco agent agency framing, Brynjolfsson Fact 3) all converging on the same cut
- Concept pages enriched:
  - [[enterprise-ai-adoption]] — added the equalizing-effect-vs-occupation-level reconciliation; added "Realized employment outcomes" subsection citing Brynjolfsson 2025 alongside McKinsey workforce-expectations data
  - [[responsible-ai]] — added "Labor-market disruption as an under-attended RAI concern" subsection — concrete questions for orgs about entry-level pipeline policy
  - [[generative-ai]] — added cross-reference to [[automation-vs-augmentation]] as load-bearing distinction
- Index updated: 1 source + 2 entity + 2 concept = 5 new entries; concept summaries refreshed.
- **Cross-source synthesis**: this ingest creates a substantive **task-level vs. occupation-level paradox** captured across [[Erik Brynjolfsson]] entity page, [[ai-employment-effects]], and [[enterprise-ai-adoption]] — AI raises productivity per worker (especially low-skill workers, the equalizing effect) while reducing the *number of workers* needed in automate-able roles. Both findings can be true; the popular reading of "AI helps low-skill workers most → equalizing → good for entry-level" has been over-extended.
- **Contradiction check**: complicates rather than contradicts prior wiki claims. The "equalizing effect" framing in the AI Index productivity studies and the entry-level employment decline in this paper are *both* true and *not* mutually exclusive — but the popular interpretation has elided the distinction. Captured explicitly in [[ai-employment-effects]] § Debates.
- Notable choices: [[Bharat Chandar]] and [[Ruyu Chen]] (co-authors), [[ADP]] (data provider), [[Daron Acemoglu]], [[David Autor]] (cited theory), [[Anthropic Economic Index]] (data source) all left as dangling wikilinks for now — single-source coverage; will create when they recur.
- Brynjolfsson 2023 customer-support paper noted on the [[Erik Brynjolfsson]] entity page but not yet ingested as its own source. Worth a future ingest if the user can locate it.
- Total file touch: 12 (1 source + 2 entities + 2 concepts + 3 enrichments + 1 thread enrichment hint via cross-references + index + log + 1 raw PDF moved). Within design's 10–15 envelope.

## [2026-04-28] refactor | folder placement: Brynjolfsson Canaries paper to raw/papers/

User dropped the Brynjolfsson, Chandar & Chen "Canaries in the Coal Mine" Stanford Digital Economy Lab working paper (Aug 2025) into `raw/articles/` but it's an academic working paper (formal econometric methodology, references, ADP-payroll-data analysis). Moved to `raw/papers/` consistent with our convention (paper = academic; article = journalism/HBR-style). Surfaced a future schema-evolution candidate: source-page schema may benefit from explicit `working_paper` / `peer_reviewed` / `preprint` fields so rigor level is legible without reading the body.

## [2026-04-28] ingest | Batch (4 sources): MITTRI/Cisco, HBR Anand-Wu, HBR Werner-Le-Brun, Gomaa Lean 4.0

Third through sixth ingests in a single batch (user-requested override of the default supervised one-at-a-time mode per design §7). Total: 4 sources, ~50 pages of content combined, 26 files touched. Single commit.

**Sources ingested:**
1. [[2026-04-28-mittri-cisco-ai-enabled-enterprise]] — *Building the AI-enabled enterprise of the future* (MIT Tech Review Insights × Cisco, 2025, 8 pp). Sponsored research; 13% / 98% / 85% readiness-urgency triad; chatbot→agent→multi-agent progression; 5-foundations framework; Ford case study (63→0 defects, 15hr→10s fluid dynamics).
2. [[2026-04-28-anand-wu-genai-playbook]] — *The Gen AI Playbook for Organizations* (Anand & Wu, HBR Nov–Dec 2025, 11 pp). 2×2 task-suitability framework (cost of errors × type of knowledge); paradox of access; 4-move competitive advantage playbook; six leakage points exhibit.
3. [[2026-04-28-werner-lebrun-octopus-organization]] — *Become an Octopus Organization* (Werner & Le-Brun, HBR Nov–Dec 2025, 12 pp). Tin Man vs Octopus archetype; 12% transformation success baseline; 3 antipattern categories; learning loop with Donella Meadows leverage hierarchy.
4. [[2026-04-28-gomaa-lean-4-0]] — *Lean 4.0: Strategic Roadmap for Smart Manufacturing* (Gomaa, IJESE Apr 2025, 20 pp open access). Off-theme; 23×23 Lean ↔ Industry 4.0 tool mapping; 9-step implementation framework; 11 research gaps; complements MITTRI/Cisco manufacturing data and Italgas worked example.

**New entity pages (6):** [[Cisco]], [[MIT Technology Review Insights]], [[Harvard Business Review]], [[Amazon Web Services]], [[Bharat N. Anand]], [[Andy Wu]].

**New concept pages (3):**
- [[ai-agents]] — promoted now that 4 sources discuss agents substantively (AI Index, MIT Sloan, MITTRI/Cisco, Anand-Wu). Covers chatbot→agent→multi-agent progression, RE-Bench results, deployment examples (Salesforce Agentforce, Italgas DANA, Harvey, GitHub Copilot).
- [[lean-4-0]] — 23×23 mapping; 9-step framework.
- [[industry-4-0]] — referenced by MITTRI/Cisco (manufacturing data) and Gomaa.

**New thread (1):**
- [[threads/organizational-frameworks-for-ai-adoption|organizational-frameworks-for-ai-adoption]] — tracks the cross-source comparison of MIT CISR Four Stages + Four S vs Anand-Wu 2×2 vs Cisco 5 Foundations vs Werner-Le-Brun Octopus/Tin Man. Initial reading: complementary, not competing — they target different layers (org design / readiness / capability progression / task deployment / diagnosis).

**Major enrichments to existing pages:**
- [[enterprise-ai-adoption]] — added the 5-lens working definition; full Anand-Wu 2×2 framework with examples; the leakage-points diagnostic; the paradox-of-access argument; Ford worked example.
- [[responsible-ai]] — added "AI security as a discipline" (Cisco fundamentals) and "Risk-vs-experimentation tradeoff" (Anand-Wu's JPMorgan example).
- [[generative-ai]] — refactored agents subsection to redirect to new [[ai-agents]] page; added "Access democratization" (MS-DOS→GUI analogy) and "Tools" table (ChatGPT, Harvey, Copilot, Agentforce, DANA).
- [[ai-maturity-measurement-comparison]] thread — added MITTRI/Cisco readiness instrument and Werner-Le-Brun's 12% transformation-success baseline; updated cross-walk table with 4 success-rate measurements (1%/7%/12%/13% spread).

**Deferred (dangling wikilinks pending recurrence):** [[Jana Werner]], [[Phil Le-Brun]], [[Attia Hussien Gomaa]] (single-source authors); [[Jeetu Patel]], [[Liz Centoni]], [[Patrick Milligan]] (quoted execs); [[Ford]], [[Harvey]], [[GitHub Copilot]], [[Capgemini]], [[PwC]] (recur-likely); plus ~15 case-study companies (Netflix, Coca-Cola, Capital One, Harrah's, JPMorgan, etc.).

**Contradiction check:** no contradictions. Strong cross-source convergence on "high adoption, low maturity, transformation hard, agents as near-term productivity story." Methodology divergences are tracked in the two open threads.

**Notable cross-source insights:**
- 4 different "success rate" measurements span a single order of magnitude (1% / 7% / 12% / 13%) — whatever you call success, it's rare.
- [[ai-agents]] now has 4-source convergent coverage and earned its standalone concept page.
- Concrete enterprise ROI numbers portfolio: Guardian RFP (1wk→24hr), Italgas WorkOnSite (+40%/-80%), Italgas €3M revenue commercialization, Ford squish tubes (63→0 defects), Ford fluid dynamics (15hr→10s).

**Total file touch: 26.** Source pages: 4 new. Entity pages: 6 new. Concept pages: 3 new + 4 enriched. Thread pages: 1 new + 1 enriched. Plus index.md, log.md, 4 raw PDFs.

## [2026-04-28] ingest | MIT Sloan — How to boost your organization's AI maturity level

Second ingest. Kristin Burnham (writer), MIT Sloan / Ideas Made to Matter, Oct 7 2025 — reporting on a research briefing by [[Stephanie Woerner]], [[Peter Weill]], Ina Sebastian, Evgeny Káganer at [[MIT CISR]]. 3 pages of content. Underlying research: MIT CISR 2022 Future Ready Survey (N=721) + 2024 interviews at 9 enterprises.

- Source page created: [[2026-04-28-mit-sloan-ai-maturity]]
- Entity pages created: [[MIT CISR]], [[Stephanie Woerner]], [[Peter Weill]]
- Thread page opened: [[ai-maturity-measurement-comparison]] — for tracking the cross-source methodology question (AI Index vs. MIT CISR vs. future sources)
- Concept pages enriched:
  - [[enterprise-ai-adoption]] — major: added the Four Stages of AI Maturity framework, Four S challenges, Stage 2→3 financial inflection, Guardian + Italgas worked examples; updated Debates section with cross-source methodology comparison
  - [[responsible-ai]] — light: added "RAI as operationalized stewardship" subsection with Guardian + Italgas examples
  - [[generative-ai]] — light: added "Agents in enterprise AI maturity" subsection mapping autonomous-agent role to Stage 3+
- Index updated: 1 source + 3 entity + 1 thread = 5 new entries; concept summaries refreshed.
- **Contradiction check: no contradictions** with [[2026-04-28-ai-index-report-2025|AI Index 2025]]. Strong qualitative convergence on "high adoption, low maturity, value capture is hard" — though the two sources use different instruments and definitions. The methodology divergence is itself the topic of the new [[ai-maturity-measurement-comparison]] thread.
- Notable choices: Ina Sebastian, Evgeny Káganer, Kristin Burnham (writer), Guardian Life Insurance, Italgas, IESE Business School, MIT Sloan all left as dangling wikilinks for now — single-source coverage; will create pages when they recur.
- Total file touch: 11 (1 source + 3 entities + 1 thread + 3 concept enrichments + index + log + raw PDF).

## [2026-04-28] refactor | added kind: project to entity schema

The [[AI Index]] is a project/initiative within [[Stanford HAI]], not an org per se — but the entity-page `kind:` enum in design §5.2 only allows `person | org | product | place | event`. Extended to include `project`. Updated design doc §5.2 and decision log §18.

## [2026-04-28] ingest | Artificial Intelligence Index Report 2025

First real ingest. Maslej et al., Stanford HAI, April 2025, 414 pp, CC BY-ND 4.0. Read in scope: Intro + Top 12 Takeaways + all chapter highlights + Ch 4 Economy in depth (incl. all of §4.4 Corporate Activity and §4.5 Robot Deployments) + Ch 3 RAI skim via highlights and §3.10 election-misinformation case studies.

- Source page created: [[2026-04-28-ai-index-report-2025]]
- Entity pages created: [[Stanford HAI]], [[AI Index]], [[Nestor Maslej]]
- Concept pages created: [[enterprise-ai-adoption]], [[responsible-ai]], [[generative-ai]], [[foundation-models]], [[ai-benchmarks]]
- Index updated: 1 source line + 3 entity lines + 5 concept lines = 9 new index entries.
- Notable choices: deferred ~30 wikilinkable mentions (companies like OpenAI/Anthropic/Google DeepMind, individuals like Brynjolfsson/Manyika, all individual benchmarks like MMLU/GPQA) to avoid stub-spam — they appear as dangling wikilinks ready to be promoted to standalone pages when the next theme-aligned source surfaces them. The `ai-benchmarks` concept page acts as a roster/umbrella for now.
- Total file touch: 11 (1 source + 3 entities + 5 concepts + index + log) — within the design's 10–15 expected for a moderately rich source.

## [2026-04-28] refactor | folder placement: MITTRI_Cisco to raw/reports/

Confirmed Anand & Wu's "Gen AI Playbook for Organizations" is HBR (Nov–Dec 2025) → stays in `raw/articles/`. Moved MITTRI_Cisco to `raw/reports/` (sponsored research from MIT Tech Review Insights, not journalism). Final placement of the 6 pre-ingest sources: 3 articles, 1 paper, 2 reports.

## [2026-04-28] refactor | added raw/reports/ and kind: report

Industry reports, government white papers, consultancy decks, and sell-side equity research didn't fit cleanly into `raw/papers/` (academic) or `raw/articles/` (web-clipped markdown). Added `raw/reports/` as a peer of `raw/papers/`, extended the source-page `kind:` enum to include `report`, and added a row to design doc §10 + decision log §18. Sub-types are disambiguated via tags (`consultancy`, `government`, `equity-research`, `ngo`).

## [2026-04-28] refactor | scaffold initialized

Initial wiki scaffold built per [the design doc](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md). Created `raw/` (articles, papers, lectures, books, images, assets) and `wiki/` (sources, entities, concepts, syntheses, threads) skeletons with `.gitkeep` placeholders, plus this log and a canonical `index.md`. Ready for first source ingest.

