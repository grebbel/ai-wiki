---
type: source
kind: report
title: "Artificial Intelligence Index Report 2025"
author: ["Nestor Maslej", "Loredana Fattorini", "Raymond Perrault", "Yolanda Gil", "Vanessa Parli", "Njenga Kariuki", "Emily Capstick", "Anka Reuel", "Erik Brynjolfsson", "John Etchemendy", "Katrina Ligett", "Terah Lyons", "James Manyika", "Juan Carlos Niebles", "Yoav Shoham", "Russell Wald", "Tobi Walsh", "Armin Hamrah", "Lapo Santarlasci", "Julia Betts Lotufo", "Alexandra Rome", "Andrew Shi", "Sukrut Oak"]
publisher: "Stanford Institute for Human-Centered Artificial Intelligence (HAI)"
url: "https://hai.stanford.edu/ai-index/2025-ai-index-report"
raw: "../../raw/reports/Maslej - 2025 - Artificial Intelligence Index Report 2025.pdf"
date_published: 2025-04
date_ingested: 2026-04-28
tags: [ai-index, stanford-hai, ai-adoption, generative-ai, responsible-ai, ai-investment, ai-policy, ai-productivity, ai-benchmarks, sponsored-research]
license: "CC BY-ND 4.0"
pages: 414
---

# AI Index Report 2025

## TL;DR

The 8th annual Stanford HAI AI Index. **Business has gone all-in on AI in 2024**: 78% of organizations use AI (up from 55%); 71% use generative AI (up from 33%); $109.1B U.S. private investment. The frontier is tightening (top-2 model gap now 0.7%), inference cost cratered 280-fold in 18 months, and China is closing the U.S. quality gap. **But financial impact remains modest** (most cost savings <10%, revenue gains <5%) and **only 1% of C-suite executives describe their GenAI rollouts as "mature."**

## Key claims

### Enterprise adoption (the headline story)

- **78% of orgs use AI** in at least one business function in 2024 (vs. 55% in 2023, ~50% during 2017–2022). McKinsey survey, n=2,854. §4.4.1.
- **71% of orgs use [[generative-ai|generative AI]]** in at least one function (vs. 33% in 2023). The "use gap" between any-AI and GenAI shrunk from 22pp to 7pp in a single year. §4.4.7.
- Regional adoption: North America 82% (+21pp YoY), Europe 80% (+23pp), Greater China 75% (+27pp — largest jump), Developing markets 77% (+28pp), Asia-Pacific 72% (+14pp). §4.4.4.
- High-use industries: Technology (IT 48%, marketing 47%, product 47%, software 45%); Media/telecom; Financial services. Lower-use: Consumer goods, Advanced industries, Business services. §4.4.2.
- Top GenAI use cases: marketing strategy content (27%), knowledge management (19%), personalization (19%), design (14%), code creation (13%). §4.4.5.
- **Only 1% of C-suite executives describe their GenAI rollouts as "mature."** Most companies are still capturing value at small scale.

### Financial impact (real but modest)

- The dominant pattern is **cost savings <10% per function and revenue gains <5%**. §4.4.3 / 4.4.6.
- Functions reporting cost savings (analytical AI / GenAI): service ops (49% / 58%), supply chain (43% / 61%), software engineering (41% / 52%), strategy & finance (—/56%).
- Functions reporting revenue gains (analytical AI / GenAI): marketing/sales (71% / 66%), supply chain (63% / 67%), service ops (57% / 63%), strategy & finance (—/70%).

### Productivity (consistent equalizing effect)

Five rigorous empirical studies (n>200,000 across customer support, software, materials science, knowledge work) converge on **AI productivity gains in the 10–45% range**. §4.4.

- Customer support: +14.2% issues/hour ([[Erik Brynjolfsson]] et al. 2023, NBER 31161, Q.J. Econ 2025). Gains emerged quickly; AI-exposed workers maintained efficiency during AI outages.
- Microsoft workplace study: doc editing +10–13%, email time -11%, security +23% faster +7% accuracy, sales 39% faster.
- Materials science: +44.1% materials discovery, +39.4% patent filings, +17.2% prototypes (Toner-Rodgers 2025, n=1,018 scientists).
- Software (Cui et al. 2024): +26.08% task completion. (Hoffman et al. 2024): +12.4% coding, -24.9% PM time.

**Equalizing effect — robust across studies:** low-skill workers gain disproportionately more.

| Study | Task | Low-skill gain | High-skill gain |
|---|---|---|---|
| Brynjolfsson et al. 2023 | Customer support | 34% | ~0% |
| Dell'Acqua et al. 2023 | Consulting | 43.0% | 16.5% |
| Cui et al. 2024 | Software eng | 21–40% | 7–16% |
| Hoffman et al. 2024 | Software eng | 12–27% | 5–10% |

### The frontier (tightening)

- **Top-2 model Elo gap on Chatbot Arena: 4.9% (2023) → 0.7% (2024). Top-10 gap: 11.9% → 5.4%.**
- **U.S.-China model performance gap closing:** end-2023 gaps on MMLU/MMMU/MATH/HumanEval were 17.5/13.5/24.3/31.6pp. End-2024: 0.3/8.1/1.6/3.7pp.
- **90% of notable AI models in 2024 came from industry** (vs. 60% in 2023). Training compute doubles every ~5 months; dataset size every ~8 months; power demand annually.
- **Inference cost cratered 280-fold** in 18 months for GPT-3.5-equivalent quality (Nov 2022: $20/M tokens → Oct 2024: $0.07/M tokens via Gemini-1.5-Flash-8B). HW costs falling 30%/year, energy efficiency improving 40%/year.
- **Test-time compute** (o1, o3) lifted reasoning sharply: o1 = 74.4% on IMO qualifier vs. GPT-4o's 9.3% — but at ~6× the cost and 30× the latency.
- **Smaller models matching big ones**: Phi-3-mini (3.8B) matches PaLM (540B) on 60%+ MMLU — 142× reduction in two years.

### Responsible AI (acknowledged but undermitigated)

- **AI incidents +56.4% YoY: 233 reported in 2024** (record high). Source: AI Incidents Database. §3.
- McKinsey RAI survey: orgs identify risks but most don't actively address them. Top concerns: inaccuracy 64%, regulatory compliance 63%, cybersecurity 60% — all <70%.
- **The data commons is shrinking:** restrictions on actively maintained C4 domains went from **5–7% (2023) to 20–33% (2024)**. Implications for data diversity, alignment, and scalability.
- New RAI benchmarks: **HELM Safety, AIR-Bench, FACTS, SimpleQA, Hughes Hallucination Evaluation**. Older ones (HaluEval, TruthfulQA) failed to gain traction.
- **Foundation Model Transparency Index** (CRFM): avg score among major developers **37% (Oct 2023) → 58% (May 2024)**.
- LLMs trained against explicit bias continue to exhibit **implicit** bias (race, gender) on standard probes — including GPT-4 and Claude 3 Sonnet.
- Global RAI governance intensified: OECD, EU, UN, African Union frameworks.
- 2024 election misinformation case studies: Pakistan deepfakes, "spamouflage" U.S. campaign, South Africa AI-generated infrastructure-decay images, Uruguay AI hologram debate. Spread broadly across >12 countries; measurable impact remained unclear.

### Policy (governments scaling up)

- **U.S. federal AI regulations: 59 introduced in 2024** — 2× the 2023 rate, from 2× as many agencies.
- Globally: legislative mentions of AI rose **21.3% across 75 countries**; 9-fold increase since 2016.
- Major national investments: Saudi Arabia $100B (Project Transcendence), France €109B, China $47.5B (semiconductor fund), Canada $2.4B, India $1.25B.

### Infrastructure and energy

- **Nuclear partnerships for AI:** Microsoft $1.6B Three Mile Island deal (Sep 2024); Google ↔ Kairos Power (small modular reactors); Amazon ↔ Energy Northwest / X-energy / Dominion (SMRs).
- Training carbon emissions trajectory: AlexNet 2012 (0.01 tons) → GPT-3 (588) → GPT-4 (5,184) → Llama 3.1 405B (8,930). Reference: average American = 18 tons/year.

### Robotics

- **China dominates industrial robot installations**: 51.1% of global (276,300 in 2023, vs. Japan 46.1k, U.S. 37.6k, S Korea 31.4k, Germany 28.4k). Has installed more than the rest of the world combined since 2021.
- Collaborative robots ("cobots") rose from 2.8% (2017) to 10.5% (2023) of new industrial installs.
- Operational stock: 4.28M industrial robots globally in 2023.

### 2024 milestones (selected from §4.1 timeline)

OpenAI raises $6.6B at $157B valuation; Anthropic ↔ AWS partnership reaches $8B; xAI raises $6B at $40B+; Databricks $10B at $62B; Salesforce launches Agentforce (autonomous agents); Microsoft hires Inflection AI's team for $650M; Google hires Character.AI's cofounders ($2.5B deal); Nvidia acquires Run:ai ($700M); Mistral AI $640M at $6B; Cohere $500M at $5.5B; Perplexity $500M at $9B; Safe Superintelligence $1B; Figure AI (humanoid robots) $675M at $2.6B; AMD acquires Silo AI ($665M); Synopsys/Ansys $35B (chip-design AI).

## Notable quotes

> "AI is no longer just a story of what's possible — it's a story of what's happening now and how we are collectively shaping the future of humanity." — Yolanda Gil and Raymond Perrault, Co-directors

> "Most companies that report financial impacts from using AI within a business function estimate the benefits as being at low levels."

> "Industry's lead in notable model development, highlighted in the two previous AI Index reports, has only grown more pronounced, with nearly 90% of notable models in 2024 (compared to 60% in 2023) originating from industry."

> "Companies across sectors and geographical regions are moving beyond experimental AI adoption toward systematic integration."

## My take

This is the most authoritative single-source baseline of where AI stood at end-of-2024 / early-2025. The most informative tension in the data: **adoption is exploding while value capture is still modest and concentrated.** 78% of orgs use AI but only 1% of executive leaders describe their GenAI rollouts as "mature"; revenue gains are real but mostly under 5%; the equalizing effect on labor is robust but workforce-impact expectations remain mixed.

For this wiki's theme (AI in organizations), the load-bearing data is in §4.4 (Corporate Activity, McKinsey-derived). When [[2026-04-28-ai-index-report-2025|other sources in this corpus]] (HBR Anand-Wu, MIT Sloan, MITTRI/Cisco) make claims about adoption levels, productivity, or organizational change, this report is the right baseline to compare them against.

The non-obvious story: the **data-commons shrinkage** (5–7% → 20–33% restricted in one year) is a slow-burn structural change that probably matters more for the long-run trajectory of model quality and openness than the headline benchmark numbers. Worth a thread page once another source touches it.

The other unexamined-in-the-report assumption I want to flag: **the equalizing effect studies are all on tasks where AI augments existing human work**. Whether the equalizing effect persists when AI restructures the *task itself* (e.g., agent workflows replacing entire workstreams) is an open question that 2024 data can't yet answer.

## Authorship and steering

The full author list is recorded in the source frontmatter and the citation block below. Promoted-to-entity contributors with steering or research-management roles on this edition:

- **Lead author** — [[Nestor Maslej]] (then-EiC of the AI Index).
- **Co-chairs of the Steering Committee** — [[Raymond Perrault]] (chair, SRI International) and [[Yolanda Gil]] (chair-elect, USC ISI).
- **Steering Committee members** — [[Erik Brynjolfsson]] (Stanford Digital Economy Lab), [[James Manyika]] (Google / UN High-Level Advisory Body on AI), [[Yoav Shoham]] (Stanford CS / AI21 Labs), [[Russell Wald]] (Stanford HAI), [[Terah Lyons]] (Partnership on AI), [[Juan Carlos Niebles]] (Salesforce / Stanford), [[Vanessa Parli]] (Stanford HAI Director of Research Programs).
- **Research team contributors** — [[Loredana Fattorini]] (Stanford HAI Research Manager), [[Lapo Santarlasci]] (IMT School for Advanced Studies Lucca).

Additional named co-authors on the 2025 edition (single-source mentions, deferred per [§Lifecycle "Author-entity promotion"](../../CLAUDE.md#author-entity-promotion)): Njenga Kariuki, Emily Capstick, Anka Reuel, John Etchemendy, Katrina Ligett, Tobi Walsh, Armin Hamrah, Julia Betts Lotufo, Alexandra Rome, Andrew Shi, Sukrut Oak.

## Linked entities and concepts

**Entities (promoted):** [[Stanford HAI]], [[AI Index]], [[Nestor Maslej]], [[Yolanda Gil]], [[Raymond Perrault]], [[Erik Brynjolfsson]], [[James Manyika]], [[Yoav Shoham]], [[Juan Carlos Niebles]], [[Russell Wald]], [[Vanessa Parli]], [[Terah Lyons]], [[Loredana Fattorini]], [[Lapo Santarlasci]], [[McKinsey & Company]], [[OpenAI]], [[Anthropic]].

**Mentioned but not yet promoted to standalone pages:** International Federation of Robotics, Center for Research on Foundation Models, Epoch AI, Lightcast, Quid, Google DeepMind, Microsoft, Meta, Mistral AI, xAI, NVIDIA, Databricks, Salesforce, Perplexity, Cohere, Figure AI, Safe Superintelligence.

**Concepts:** [[enterprise-ai-adoption]], [[responsible-ai]], [[generative-ai]], [[foundation-models]], [[ai-benchmarks]].

## Source

- **Raw PDF (414 pp):** [report file](../../raw/reports/Maslej%20-%202025%20-%20Artificial%20Intelligence%20Index%20Report%202025.pdf)
- **Public release:** [hai.stanford.edu/ai-index/2025-ai-index-report](https://hai.stanford.edu/ai-index/2025-ai-index-report)
- **License:** CC BY-ND 4.0
- **Citation (per the report):** Nestor Maslej, Loredana Fattorini, Raymond Perrault, Yolanda Gil, Vanessa Parli, Njenga Kariuki, Emily Capstick, Anka Reuel, Erik Brynjolfsson, John Etchemendy, Katrina Ligett, Terah Lyons, James Manyika, Juan Carlos Niebles, Yoav Shoham, Russell Wald, Tobi Walsh, Armin Hamrah, Lapo Santarlasci, Julia Betts Lotufo, Alexandra Rome, Andrew Shi, Sukrut Oak. *"The AI Index 2025 Annual Report,"* AI Index Steering Committee, Institute for Human-Centered AI, Stanford University, Stanford, CA, April 2025.

## Reading scope

For this ingest I read: Introduction (pp. 1–10) + TOC + Top 12 Takeaways (pp. 3–5) + all Chapter Highlights (pp. 12–23, all 8 chapters) + Chapter 4 Economy in depth (pp. 214–278: Overview, 2024 timeline, Jobs, Investment focus areas, Corporate Activity in full, AI's Labor Impact / productivity studies, Robot Deployments). Skimmed: Chapter 3 RAI via highlights and the §3.10 election-misinformation case studies. **Not read in detail:** Chapters 1, 2, 5, 6, 7, 8 — the chapter highlights from the front matter were sufficient for entity/concept seeding. Future ingests of theme-aligned sources may pull more depth from these chapters.
