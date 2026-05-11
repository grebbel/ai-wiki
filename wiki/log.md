# Log

Append-only chronological record of wiki operations. Strict prefix format so `grep "^## \[" wiki/log.md | tail -10` works as a CLI. Format (indented to keep grep clean):

    ## [YYYY-MM-DD] <op> | <title>

Permitted operations: `ingest`, `query`, `lint`, `synthesize`, `refactor`, `bulk-refactor` (added v0.2 — for any operation touching >10 wiki pages, with affected slug list and reversibility note). See [the design doc, §9.2](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md#92-wikilogmd) for details.

---

## [2026-04-28] refactor | scaffold initialized

Initial wiki scaffold built per [the design doc](../docs/superpowers/specs/2026-04-28-llm-wiki-design.md). Created `raw/` (articles, papers, lectures, books, images, assets) and `wiki/` (sources, entities, concepts, syntheses, threads) skeletons with `.gitkeep` placeholders, plus this log and a canonical `index.md`. Ready for first source ingest.

## [2026-04-28] refactor | added raw/reports/ and kind: report

Industry reports, government white papers, consultancy decks, and sell-side equity research didn't fit cleanly into `raw/papers/` (academic) or `raw/articles/` (web-clipped markdown). Added `raw/reports/` as a peer of `raw/papers/`, extended the source-page `kind:` enum to include `report`, and added a row to design doc §10 + decision log §18. Sub-types are disambiguated via tags (`consultancy`, `government`, `equity-research`, `ngo`).

## [2026-04-28] refactor | folder placement: MITTRI_Cisco to raw/reports/

Confirmed Anand & Wu's "Gen AI Playbook for Organizations" is HBR (Nov–Dec 2025) → stays in `raw/articles/`. Moved MITTRI_Cisco to `raw/reports/` (sponsored research from MIT Tech Review Insights, not journalism). Final placement of the 6 pre-ingest sources: 3 articles, 1 paper, 2 reports.

## [2026-04-28] ingest | Artificial Intelligence Index Report 2025

First real ingest. Maslej et al., Stanford HAI, April 2025, 414 pp, CC BY-ND 4.0. Read in scope: Intro + Top 12 Takeaways + all chapter highlights + Ch 4 Economy in depth (incl. all of §4.4 Corporate Activity and §4.5 Robot Deployments) + Ch 3 RAI skim via highlights and §3.10 election-misinformation case studies.

- Source page created: [[2026-04-28-ai-index-report-2025]]
- Entity pages created: [[Stanford HAI]], [[AI Index]], [[Nestor Maslej]]
- Concept pages created: [[enterprise-ai-adoption]], [[responsible-ai]], [[generative-ai]], [[foundation-models]], [[ai-benchmarks]]
- Index updated: 1 source line + 3 entity lines + 5 concept lines = 9 new index entries.
- Notable choices: deferred ~30 wikilinkable mentions (companies like OpenAI/Anthropic/Google DeepMind, individuals like Brynjolfsson/Manyika, all individual benchmarks like MMLU/GPQA) to avoid stub-spam — they appear as dangling wikilinks ready to be promoted to standalone pages when the next theme-aligned source surfaces them. The `ai-benchmarks` concept page acts as a roster/umbrella for now.
- Total file touch: 11 (1 source + 3 entities + 5 concepts + index + log) — within the design's 10–15 expected for a moderately rich source.

## [2026-04-28] refactor | added kind: project to entity schema

The [[AI Index]] is a project/initiative within [[Stanford HAI]], not an org per se — but the entity-page `kind:` enum in design §5.2 only allows `person | org | product | place | event`. Extended to include `project`. Updated design doc §5.2 and decision log §18.

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

## [2026-04-28] refactor | folder placement: Brynjolfsson Canaries paper to raw/papers/

User dropped the Brynjolfsson, Chandar & Chen "Canaries in the Coal Mine" Stanford Digital Economy Lab working paper (Aug 2025) into `raw/articles/` but it's an academic working paper (formal econometric methodology, references, ADP-payroll-data analysis). Moved to `raw/papers/` consistent with our convention (paper = academic; article = journalism/HBR-style). Surfaced a future schema-evolution candidate: source-page schema may benefit from explicit `working_paper` / `peer_reviewed` / `preprint` fields so rigor level is legible without reading the body.

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

## [2026-04-28] refactor | folder placement: Canaries + Generative AI at Work to raw/papers/

After the GitHub push, user re-downloaded source PDFs (since `git filter-repo` had aggressively cleaned the local working tree). The re-downloads landed in `raw/articles/`; both Brynjolfsson papers belong in `raw/papers/`. Moved both. **Surfaced an 8th source the wiki had missed:** "Generative AI at Work" by Brynjolfsson, Li & Raymond, the canonical primary source for the customer-support productivity finding cited extensively across the wiki via secondary references through [[2026-04-28-ai-index-report-2025|AI Index 2025]]. Triggered the next ingest.

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

## [2026-05-05] refactor | v0.2.1 — confidence badge visible on published site

Follow-up to v0.2: the lifecycle fields were stored in frontmatter but not rendered on the published site. The lint script and the `raw` markdown were the only places to see confidence values. New extension [`extensions/inject-confidence-badge.ts`](../extensions/inject-confidence-badge.ts) renders a one-line italicized metadata strip immediately after each page's H1: *Confidence 0.85 · 4 sources · last confirmed 2026-04-28*.

**Implementation note (load-bearing).** The extension uses `htmlPlugins()` (not `markdownPlugins()`) and is registered in [`quartz.config.ts`](../quartz.config.ts) **after** `Plugin.Description()`. Reason: Quartz's Description plugin is itself an htmlPlugin that does `toString(tree)` to compute `file.data.description`. A first attempt that injected the badge as a markdown paragraph before Description ran caused the badge text to appear in `og:description`, `twitter:description`, and `meta name="description"` tags. Re-ordering as an htmlPlugin after Description fixed it.

**Verified:**
- Badge visible on concept and entity pages.
- Sources/threads skipped (no `confidence` field).
- `og:description` on Anthropic now reads `"Anthropic AI safety and research company; publisher of the Claude family..."` — no badge leak.

CSS class `confidence-badge` exposed for future styling. No content edits.

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

## [2026-05-08] refactor | Promote Jack Clark to entity page (cross-page-presence judgment)

Follow-up to the earlier "out-of-scope but flagged" note. Per user direction, treated existing [[Anthropic]] and [[AI Index]] entity-page mentions of Jack Clark as effective second-source presence — sufficient to justify promotion despite his appearing in `author:` on only one source ([[2026-04-30-ai-index-report-2026]]) and as an acknowledgement on a second ([[2026-05-07-anthropic-economic-index-5-learning-curves]]).

**Files touched (4):**

- **NEW** [[Jack Clark]] — co-founder of Anthropic; Head of Public Benefit (leads the new Anthropic Institute) since 2026; previously Anthropic Head of Policy and OpenAI Policy Director; technical journalist before that. Founding member of the AI Index (2017–2024); inaugural NAIAC member (2021–2024); OECD AI co-chair. Author of *Import AI*. Confidence 0.75; source_count 2 (AI Index 2026 + AEI 5th report acknowledgement). Web research via WebSearch on anthropic.com / wikipedia / cset.georgetown.edu / itif.org.
- **UPDATED** [[2026-05-07-anthropic-economic-index-5-learning-curves]] — Jack Clark removed from "Dangling" list and promoted into the "Entities" list, with a one-line rationale citing the cross-page-presence basis for promotion (so future readers see the judgment call, not just the result).
- **UPDATED** [[index]] — added [[Jack Clark]] entry between [[Ivey Business School]] and [[Jacqueline N. Lane]].
- **UPDATED** `wiki/log.md` (this entry).

**Convention NOT extended.** This promotion is a one-off judgment call, *not* a rule change. The CLAUDE.md §Lifecycle "Author-entity promotion" convention still says "≥2 source pages with the name in `author:`" — it does **not** auto-promote on entity-page or acknowledgement-only mentions. The audit ([`scripts/lint-dangling-authors.mjs`](../scripts/lint-dangling-authors.mjs)) was not modified and continues to track only the strict `author:`-frontmatter rule. If similar cross-page-presence cases recur often enough that the heuristic feels load-bearing, the schema can be revisited; for now we treat them as case-by-case.

**Side benefit**: the body wikilinks on [[Anthropic]] and [[AI Index]] (which were broken targets before this promotion) now resolve. Quartz's broken-link surface drops by two.

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

## [2026-05-10] ingest | Solovyev & Dwivedi — *Gemini API File Search is now multimodal* (Google — The Keyword, 5 May 2026)

Short developer-relations announcement (5-page PDF, ~3-min read) introducing three updates to the Gemini API File Search tool: **multimodal** retrieval via Gemini Embedding 2 (images and text in the same store); **custom metadata** (`department: legal`, `status: final`) for query-time filtering; **page-level citations** tying responses to specific pages of indexed PDFs. Three-primitive API: `file_search_stores.create` → `upload_to_file_search_store` → `generate_content` with `tools=[{file_search: …}]`. Source page: [[2026-05-05-google-gemini-file-search-multimodal]]. Authors **Ivan Solovyev** (PM, Google DeepMind) and **Kriti Dwivedi** (SE) listed as Dangling first-mention. Source-count bump for [[Google]] (2 → 3). No structural concept changes — substantiates a *Context-layer retrieval primitive* the wiki has been gesturing at.

## [2026-05-10] ingest | Lopopolo — *Harness engineering: leveraging Codex in an agent-first world* (OpenAI Engineering blog, 11 Feb 2026)

The wiki's first **vendor-side production case study** of [[agent-harness]] / [[agentic-engineering]] at scale: five months, ~1M LOC, ~1,500 PRs, 7 engineers, 3.5 PRs/engineer/day with throughput **increasing** as the team grew — built with **0 lines of manually-written code**. Source page: [[2026-02-11-lopopolo-codex-harness-engineering]]. Author **Ryan Lopopolo** listed as Dangling first-mention. Ingested three months after publication (Feb 11) — reactive ingest discipline, not a freshness gap. Touched pages:

- [[agent-harness]] — added vendor case-study section + hooks-as-primitive section (alongside Bratanic) + Build-layer-vocabulary refinement (alongside Chase). `source_count` 8 → 11; `confidence` 0.90 → 0.92; `last_confirmed` → 2026-05-10.
- [[agentic-engineering]] — added Codex case-study row in convergence table + new "Operational invariants" section (8 named invariants distilled from the Codex team's experience: repository-as-system-of-record, AGENTS.md as table-of-contents, layered architecture mechanically enforced, throughput inverts merge philosophy, encoded golden principles + scheduled GC, application legibility, hire for environment-design taste). `source_count` 2 → 3; `confidence` 0.80 → 0.85.
- [[OpenAI]] — added Codex / Codex CLI / Aardvark to "Products and tooling" section. `source_count` 7 → 8; `confidence` 0.85 → 0.90.
- [[index.md]], [[log.md]] — updated.

## [2026-05-10] ingest | Bratanic — *Unified Agentic Memory Across Harnesses Using Hooks* (Towards Data Science, 8 May 2026)

The wiki's first source naming **lifecycle hooks as a first-class harness primitive** — distinct from MCP tools — with an **emerging cross-vendor contract**: Claude Code, Codex, and Cursor all support the same five lifecycle events (`SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`) with near-identical JSON-stdin / JSON-stdout semantics. Three-layer architecture (hooks online + dream-phase offline + injection online); shared Python scripts + Neo4j store; switch from Cursor to Claude Code to Codex mid-project and pick up where you left off. Dream-phase markdown wiki is structurally identical to Karpathy's LLM-wiki idea and to Anthropic's Skills. Source page: [[2026-05-08-bratanic-unified-agentic-memory-hooks]]. Author **Tomaz Bratanic** (Neo4j) listed as Dangling first-mention; **Neo4j** also Dangling first-mention. Touched pages:

- [[agent-harness]] — major hooks-as-primitive section added (cross-referencing Lopopolo + the wiki's own [`hooks` schema section](CLAUDE.md#hooks)); MCP-vs-hooks distinction tabled; dream-phase pattern named explicitly. (Co-listed under the Lopopolo entry above for the source_count update.)
- [[index.md]] — added entry; co-listed under [[agent-harness]] convergence summary.

Operational note: this source's hook contract converges with the wiki's own [§Hooks](../CLAUDE.md#hooks) section — **three independent vantages** (Lopopolo / Bratanic / this repo's own scripts) now supply convergent evidence that hooks are a stable cross-vendor harness primitive.

## [2026-05-10] ingest | Manditereza — *Building Ontology-Driven Intelligence for Industrial AI Agents* (HiveMQ Technical White Paper, Feb 2026)

The wiki's **first OT/industrial-manufacturing source** on agentic AI specifically — opening a parallel track to the SaaS / coding-agent cluster. 15-page PDF, ~12 pages of body content. Three-tier semantic data layer (semantic model + domain ontologies + knowledge graph); four structural pillars of an industrial ontology (object types / properties / link types / **action types** with preconditions and state changes); three-layer architecture (Data Streaming + Data Intelligence + Agentic AI); five mechanisms why ontologies enable reliable agentic AI (unified operational awareness / semantic layer / compounding returns / closed-loop learning / governed autonomy). Source page: [[2026-02-01-manditereza-ontology-driven-industrial-ai]]. Author **Kudzai Manditereza** listed as Dangling first-mention; **HiveMQ** also Dangling first-mention. Customer references: Audi, BMW, Eli Lilly, Liberty Global, Mercedes-Benz, Siemens — none promoted on a single mention. Touched pages:

- [[industrial-ai-agents]] — **new concept page** created (single-source stub at confidence 0.70; aliases: industrial AI agents / industrial agentic AI / OT AI agents / manufacturing AI agents). Names three distinguishing properties: data-fabric primacy, action-precondition governance, continuous real-time data dependency.
- [[index.md]] — added entry under both Sources and Concepts.

Candidate sub-concepts noted but **not promoted** on single source: Ontology / Semantic Data Layer, Unified Namespace (UNS), Action types / action-precondition governance. **Knowledge graph** reaches second-source convergence in this same ingest batch (Bratanic + Manditereza); flagged as promotion candidate for a follow-up sweep.

## [2026-05-10] ingest | Chase — *The Agent Development Lifecycle* (LangChain Blog, 9 May 2026)

The wiki's **second formalization** of the [[agent-development-lifecycle|ADLC]] — and the first non-Google one. Four-phase loop wrapped by governance: **Build → Test → Deploy → Monitor → Iterate**, with **Govern** wrapping the whole. Refines the wiki's [[agent-harness|harness]] vocabulary by splitting Build into four distinct sub-layers (Frameworks / Runtimes / **Harnesses** / No-code) — sharper than the prior Kokane 4-layer stack. Names six governance axes for agent scaling (cost / tool access / audit trails / HITL / discoverability of skills / shared infrastructure across teams). Source page: [[2026-05-09-chase-agent-development-lifecycle]]. Touched pages:

- [[agent-development-lifecycle]] — bumped from single-source stub (confidence 0.70) to two-source confidence 0.80; rewritten extensively to compare Google's 9-stage wheel and Chase's 4-phase loop side-by-side; added Codex case study as worked example. `source_count` 1 → 2.
- [[agent-harness]] — added "Refined Build-layer vocabulary" section. (Co-listed with Lopopolo entry for the source_count update; cumulative source_count now 11.)
- [[LangChain]] — **new entity page** created (organization). Cumulative cross-page mentions ([[agent-harness]], [[ai-agents]], [[generative-ai]] + this fresh source-page mention) cleared the entity-promotion bar. `source_count` 4. Lists products (LangChain framework, LangGraph runtime, Deep Agents harness, LangSmith Platform / Observability / Evaluation / Deployment / Sandboxes / Fleet, LangChain Academy).
- **Harrison Chase** — first wiki source mention by name; listed as Dangling per author-entity-promotion rule. Promote on second-source mention.
- [[index.md]] — added entry under Sources and Entities; updated [[agent-development-lifecycle]] and [[agent-harness]] one-liners.

Candidate concepts noted but **not promoted** on single source: agent governance (six axes), simulation as agent eval primitive.


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
