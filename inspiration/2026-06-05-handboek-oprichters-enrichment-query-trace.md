---
type: query-trace
question: "What can be added from the wiki to enrich the Founders' Handbook (Dutch BDS edition)?"
date: 2026-06-05
language: en
trace: 2026-06-05-handboek-oprichters-enrichment-query-trace.json
enrichment_target: "/Users/witoldtenhove/Projects/brand-project/ideation/2026-05-22-handboek-voor-oprichters.html"
pages_used: 6
pages_ignored: 97
---

# Query trace — enriching the Founders' Handbook (Dutch BDS edition)

## 1. Question

- **Original:** "See ideation/2026-05-22-handboek-voor-oprichters.html — What can be added from the Wiki to enrich this handbook?"
- **Resolved target:** `brand-project/ideation/2026-05-22-handboek-voor-oprichters.html` — *Handboek voor startende AI-ondernemers* (BDS-branded Dutch edition of the 14-chapter Founders' Handbook; published to `businessdatasolutions.github.io/ai-wiki`). Confirmed a faithful translation of the English edition, citing the **same ~24 wiki pages, frozen at 2026-05-22**, same accountancy-app callouts.
- **Restated:** Which wiki material added *since* 22 May 2026 (today is 5 June) can deepen the handbook — and which conceptual gaps does it leave?
- **Facets:** 1) new GTM / business-model material · 2) new org-shape & future-of-firm material · 3) new vertical worked examples · 4) a native Dutch-market anchor · 5) conceptual gaps the handbook never names.

This is an **enrichment query** (the inspiration doc's hardest case): the goal is material that *extends or challenges* the handbook, not material that echoes what it already cites. The triage filter was therefore explicit: a candidate enriches only if it is **not already in the handbook's Bronnenkaart** *and* is either a source dated ≥ 2026-05-22 or a concept/synthesis adding a missing dimension.

## 2. Paths explored

Three facet queries via `node scripts/wiki-retrieve.mjs --json -n 12` (qmd ∪ graph, RRF-fused, decay-ranked), unioned to **103 candidates**. `graph_available: true`.

**Enrichment candidates kept (USE) — where they live**

| Anchor | Page | type | fused | dated | verdict |
|---|---|---|---|---|---|
| W1 | `wiki/sources/2026-06-03-warren-yc-how-to-build-an-ai-native-services-company.md` | source | 0.82 | 3 Jun | **USE** |
| W2 | `wiki/sources/2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero.md` | source | 0.27 | 27 May | **USE** |
| W3 | `wiki/sources/2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era.md` | source | 0.26 | 28 May | **USE** |
| W4 | `wiki/sources/2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs.md` | source | 0.26 | 28 May | **USE** |
| W5 | `wiki/sources/2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care.md` | source | 0.33 | 31 May | **USE** |
| W6 | `wiki/concepts/micro-productivity-trap.md` | concept | 0.94 | 28 src | **USE** |

**Notable candidates explored and ignored** (full 97-row list in the JSON trace)

| Page | reached via | verdict | class |
|---|---|---|---|
| `concepts/agent-harness`, `concepts/enterprise-ai-adoption`, `concepts/dynamic-capabilities`, `concepts/ai-employment-effects`, `concepts/durable-skills` | qmd | IGNORE | redundant (already in the handbook's Verder-lezen) |
| `sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook` | qmd | IGNORE | redundant (build-layer thesis already carried by Tan/Hu + W1) |
| `sources/2026-05-31-benedict-evans-...` | qmd | IGNORE | redundant (noted only as Giles's counter-voice) |
| `sources/2026-05-24-erginbilgic-...-rolls-royce-turnaround` | qmd | IGNORE | off-facet (incumbent, not a founder vantage) |
| `concepts/ai-agents` (0.91), `syntheses/organizational-frameworks-for-ai-adoption` | qmd/graph | IGNORE | off-facet (foundational / pointer-only) |
| ~85 further graph + qmd tail | graph | IGNORE | below-threshold |

**index.md / gap-expansion (Step 5):** none — all five facets were covered by the USE set.

## 3. Ignore policy applied

- `redundant` — the dominant class here, *by design*: the handbook already cites the wiki's core concepts and the strongest YC/McKinsey doctrine, so anything restating them is not enrichment. The five "Verder lezen" concepts and the Koomen/Evans pieces fall here.
- `off-facet` — adjacent but not founder-actionable for *this* handbook (Rolls-Royce incumbent turnaround; the generic `ai-agents` concept).
- `below-threshold` — the long graph-only tail; no enrichment facet needs it.

The unusually high ignore rate (97/103) is the correct shape for an enrichment query against an already-well-sourced document: most of what the wiki returns is what the handbook *already* knows.

## 4. Information ignored

| Page | reason-class | reason |
|---|---|---|
| `concepts/agent-harness`, `…/enterprise-ai-adoption`, `…/dynamic-capabilities`, `…/ai-employment-effects`, `…/durable-skills` | redundant | already in the handbook's Appendix C (Verder lezen) |
| `sources/2026-05-27-koomen-yc-lightcone-inside-yc-ai-playbook` | redundant | "AI-as-building-layer" thesis already reaches the handbook via Tan/Hu and (newly) Warren [W1] |
| `sources/2026-05-31-benedict-evans-rational-conversation-…` | redundant | only valuable as the counter-voice to Giles [W4]; surfaced in-answer, not separately evidenced |
| `sources/2026-05-24-erginbilgic-bloomberg-…-rolls-royce` | off-facet | FTSE-incumbent turnaround, not a founder vantage; "transform-from-strength" already reaches the handbook via Scheffer [W2] |
| `concepts/ai-agents` (fused 0.91) | off-facet | foundational agent-internals; handbook is GTM/operating-doctrine |
| `syntheses/organizational-frameworks-for-ai-adoption` | off-facet | a good Further-Reading pointer, but not deep-read this run; `micro-productivity-trap` [W6] already maps the cluster |
| ~85 further graph/qmd tail candidates | below-threshold | no enrichment facet needs them |

## 5. Information used

| Page | type | effConf | what it contributes that the handbook lacks |
|---|---|---|---|
| [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company\|Warren / YC]] | source | — | a whole YC anchor purpose-built for the handbook's thesis: the *services-company* (not software-product) playbook |
| [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero\|Scheffer / De Ondernemer]] | source | — | the missing **native-Dutch €80M founder-CEO** worked example for a Dutch-branded handbook |
| [[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era\|Moon et al. / McKinsey]] | source | — | consulting-altitude **numbers** for the team-shape / future-firm chapters (currently only qualitative) |
| [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs\|Giles / WP Intelligence]] | source | — | recent employment **empirics** + the chatbot-vs-deeper-agent productivity split |
| [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care\|Peron / Philips]] | source | — | the **healthcare** vertical the preface names but never anchors |
| [[concepts/micro-productivity-trap\|micro-productivity-trap]] | concept | 0.94 | the demand-side concept the handbook's product-design chapters implicitly defend against but never name |

## 6. Answer-element map

| Anchor | Enrichment element | Wiki page | Lands in handbook chapter(s) |
|---|---|---|---|
| [W1] | outcome-vs-co-pilot; 4 market traits (low trust / low task-judgment / high intelligence threshold / regulation-as-moat); Sam Altman Test; variance-is-existential; P&L math (30%→50%+ margin, TAM 2-3×); pricing GO/AVOID; don't-buy-your-way-in; early-demand-trap | [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company\|Warren / YC]] | Ch 1, 2, 3, 10, 13; Appendix A |
| [W2] | day-zero rebuild; CS 100→18 via natural attrition; technology-leading/people-directing reversal; CAIO as missing MKB role; conscious revenue sacrifice; *"elke kantoorbaan voor een scherm verdwijnt"* | [[2026-05-27-scheffer-de-ondernemer-helloprint-ai-rebuild-from-day-zero\|Scheffer]] | Preface (anchors), Ch 1, 6, 14 |
| [W3] | 100→60 FTE / 10-role→3-role pod / ~60% team cut / 3-5× productivity; outer-loop roles + policy-as-code; knowledge-graph memory layer + librarian agent | [[2026-05-28-moon-mckinsey-rewiring-software-delivery-for-the-agentic-era\|McKinsey]] | Ch 6, 10, 11, 12, 14 |
| [W4] | AI #1 cited layoff reason Mar+Apr 2026; chatbot 2-3% vs deeper-agent 30-60% split; Frey "no automobile industry"; IBM tripling entry-level; "if you work like a robot…" | [[2026-05-28-giles-wp-intelligence-new-human-machine-workforce-agentic-ai-jobs\|Giles]] | Ch 2, 14 |
| [W5] | SmartArt cardiac-MRI 15min→30s, ~4× throughput; augmentation in a structurally-undersupplied vertical; AI-as-clinical-bias-auditor; interoperability/reimbursement/regulation barriers | [[2026-05-31-peron-mit-smr-me-myself-and-ai-philips-interoperability-health-care\|Peron]] | Ch 2 (a new supply-side axis); vertical-example anchors; Ch 8 |
| [W6] | the trap (offering/process/anthropomorphizing lock-in); escape = workflow redesign + verify→evaluate→capture flywheel; 10-25% EBITDA for the transformation mindset | [[concepts/micro-productivity-trap\|micro-productivity-trap]] | Ch 12, 13; Appendix A; Appendix C |

## 7. Final answer

The handbook is internally complete and well-sourced, but its citation set is **frozen at 22 May 2026**. In the two weeks since, the wiki has ingested exactly the material that the handbook's own thesis was reaching for. Six additions, in priority order:

**1. Add a dedicated treatment of the *AI-native services company* (Warren / YC, 3 June). [W1]** This is the single highest-value addition — a YC anchor published *after* the handbook that is purpose-built for its thesis. The handbook's nine YC sources all sit on the *AI-software-product* side; Warren names the *services-company* side explicitly, which is precisely the "compete with the firm by selling the outcome" move Vitucci makes in Chapter 1. Concretely: the **outcome-as-product vs co-pilot-as-product** distinction (Ch 1); the **four market-selection traits** — low trust, low task-level judgment, high intelligence threshold, *regulation-as-moat* — which sharpen Chapter 2's vertical diagnostic and Chapter 3's wedge test; **variance is the existential problem** (*"customers will fire you for variance faster than … for being a bit slower or more expensive"*) as a Chapter 10 counterpoint to velocity; and a full **P&L section** for Chapter 13 — traditional services ~30% margins → AI-leveraged 50%+ on a TAM "two to three times bigger than software," with **per-unit and outcome-based pricing as GO, cost-plus and straight-line-undercutting as AVOID**, plus the **don't-buy-your-way-in** rule and the **early-demand trap** (two new Appendix A anti-patterns). [W1]

**2. Add the native-Dutch founder-CEO anchor the BDS edition is missing (Scheffer / HelloPrint, 27 May). [W2]** Every anchor in this Dutch-branded handbook is US/UK. Scheffer is a **Dutch €80M founder-CEO** rebuilding HelloPrint AI-first — the worked example a Dutch reader will recognise. He supplies: the **day-zero rebuild** thought experiment (*"wat nou als ik mijn huidige bedrijf op dag één opnieuw zou moeten bouwen?"*); the **customer-service 100→18** quantified reduction via natural attrition, with AI *"beter dan het niveau waarop mensen het kunnen doen"* (Ch 14); the **technology-leading / people-directing reversal**; the **"Chief AI Officer is the missing role in MKB management teams"** observation (a Dutch-specific sharpening of Chapter 6); and **conscious revenue sacrifice for long-term winning** (Ch 1/transform-from-strength). His headline — *"elke kantoorbaan voor een scherm gaat verdwijnen"* — is a Dutch-voice restatement of Chapter 14's future-shape thesis and would make a strong native-language callout to sit alongside (or replace) the accountancy-app callouts. [W2]

**3. Give the team-shape and future-firm chapters hard numbers (McKinsey, 28 May). [W3]** Chapters 6 and 14 currently rest on qualitative founder doctrine (Tan/Hu) plus the revenue-per-employee comp. McKinsey adds a **consulting-aggregated quantification**: 100→60 FTEs, **10-role pods collapsing to 3-role pods** (Product owner / Tech lead / AI-enabled engineer), ~60% team-size reduction, 3-5× productivity. It also strengthens Chapter 11 (governance) with **outer-loop roles baked in by design + policy-as-code**, and Chapter 12 (context-is-the-moat) with **knowledge graphs as an AI memory layer** and the **librarian agent** — a concrete mechanism for the "context the customer accumulates" moat. [W3]

**4. Refresh the employment empirics in Chapters 2 and 14 (Giles / WP Intelligence, 28 May). [W4]** The handbook leans on Jones's weak-links theory; Giles adds 2026 *data*: AI as the **#1 cited reason for US layoffs in both March and April 2026**; the **chatbot 2-3% vs deeper-agent 30-60%** productivity split (the empirical floor/ceiling that *is* the micro-productivity-trap, see W6); **IBM tripling entry-level hiring** as a counter-trend; and the durable-skill line *"if you are working like a robot, your job will be taken by a robot."* It also introduces a **productive tension** worth surfacing in Chapter 14: Frey's *"hard to see [AI] creating something like the automobile industry"* counters the lump-of-labor optimism — and the wiki records Giles and Benedict Evans explicitly disagreeing on the aggregate-employment trajectory. The handbook currently presents the future-shape forecast without that debate. [W4]

**5. Anchor the healthcare vertical the preface promises (Peron / Philips, 31 May). [W5]** The preface scopes "healthcare ops" but the handbook has no healthcare worked example. Peron supplies one — Philips **SmartArt cardiac-MRI: 15 minutes of expert setup → 30 seconds, ~4× throughput** — plus a vertical-selection insight Chapter 2 lacks: in healthcare the adoption driver is **structural undersupply ("do more with the same"), not billing-model maturity**, which is a *different axis* than the handbook's liability/forward-thinking/project-billing triad. Her **AI-as-clinical-bias-auditor** examples and the **interoperability / reimbursement / regulation** barrier list also enrich Chapter 8's procurement-reality discussion for regulated verticals. [W5]

**6. Name the trap the product-design chapters are silently fighting (micro-productivity-trap, 28 sources). [W6]** This is the biggest *conceptual* gap. The handbook's Chapters 11-13 (governance, context-is-moat, unit economics) are, in effect, advice for building products that escape a failure mode it never names: the **micro-productivity-trap** — task-level AI gains that fail to become firm-level value, via *offering / process / anthropomorphizing lock-in*. It is the wiki's most strongly corroborated concept (28 sources, confidence 0.95). Adding it gives the handbook the **demand-side rationale** for its own advice: founders should "sell outcomes" and "build for the future org" precisely because their *customers* fail when they bolt AI onto unredesigned workflows. The escape mechanism — **workflow redesign + a verification→evaluation→learning-capture flywheel**, with **10-25% EBITDA gains** for the transformation mindset — belongs in Chapter 12/13, and *"AI bolted on is going to fail"* is a natural ninth Appendix A anti-pattern (the buyer-side mirror of the handbook's vendor-side set). It should also join Appendix C (Verder lezen) as a companion concept page. [W6]

*Scope note:* this enriches the **content**; it does not touch the handbook's HTML/design. If you want, the next step is to draft the specific insertions (callout blocks + Bronnenkaart entries, in Dutch) for chapters 1, 2, 6, 12, 13, 14 and Appendices A/C. *Currency:* all six additions are fresh (the concept page is at full confidence; the five sources are days old), so no decay discount applies.

## 8. Trace artifact

Machine-readable provenance (103-candidate ledger with verdicts, scores, and the answer-element map): [`2026-06-05-handboek-oprichters-enrichment-query-trace.json`](2026-06-05-handboek-oprichters-enrichment-query-trace.json).
