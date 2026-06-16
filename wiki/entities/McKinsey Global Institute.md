---
type: entity
kind: organization
aliases: ["MGI", "McKinsey Global Institute", "MGI (McKinsey)"]
tags: [mckinsey, mgi, research-institute, economics, productivity, business-research, future-of-work, ai-economics]
website: "https://www.mckinsey.com/mgi"
founded: 1990
parent: "[[McKinsey & Company]]"
confidence: 0.85
last_confirmed: "2026-05-26"
accessed_at: "2026-05-26"
source_count: 3
relationships:
  - type: part-of
    target: McKinsey & Company
    via: "the research arm of McKinsey & Company; editorially independent (no client-commissioned work) but operationally + financially within the McKinsey partnership"
---

# McKinsey Global Institute

The **McKinsey Global Institute** is the business and economics research arm of [[McKinsey & Company]]. Founded **1990**. Mission per its own framing: *"to provide a fact base to aid decision making on the economic and business issues most critical to the world's companies and policy leaders."* Editorially independent — *"none of our work is commissioned or funded by any business, government, or other institution; we share our results publicly free of charge; and we are entirely funded by the partners of McKinsey"* — but operationally + financially within the McKinsey partnership.

## Role in the AI ecosystem

MGI is one of the wiki's **highest-source-reliability tier** publishers on structural AI-and-economy questions — comparable to [[Stanford HAI]] (publisher of the [[AI Index]]) at the academic-institute altitude. Three properties make MGI publications load-bearing for the wiki:

1. **Independence from client work**: MGI publications are not commissioned by clients; they're cross-firm research priorities set by the MGI directors-and-partners group.
2. **Multi-author + academic-adviser sign-off**: flagship reports are co-authored by 4-7+ MGI partners with named external academic advisers (Nobel laureates, deans of Tuck / LSE / Wharton).
3. **Methodological transparency**: technical appendices accompany major reports; methodologies are publicly documented (automation model, occupation taxonomies, economic value models, etc.).

## Five research themes (current)

Per the [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|MGI directors' framing]] in *Agents, Robots, and Us* (Nov 2025):

1. **Productivity and prosperity** — creating and harnessing the world's assets most productively.
2. **Resources of the world** — building, powering, and feeding the world sustainably.
3. **Human potential** — maximising and achieving the potential of human talent.
4. **Global connections** — exploring how flows of goods, services, people, capital, and ideas shape economies.
5. **Technologies and markets of the future** — discussing the next big arenas of value and competition.

## Sources from MGI ingested into this wiki

| Source | Theme | Date | Authors |
| --- | --- | --- | --- |
| [[2025-11-25-yee-mgi-agents-robots-and-us-skill-partnerships|Agents, Robots, and Us]] | Human potential + Productivity (workforce-skills layer) | Nov 2025 | Yee, Madgavkar, Smit, Krivkovich, Chui, Ramirez, Castresana |
| [[2026-03-25-russell-bradley-mgi-race-takes-off-next-big-arenas|The Race Takes Off in the Next Big Arenas of Competition]] | Technologies and markets of the future (industry layer) | Mar 2026 | Russell, Bradley, Sastry, Chettih, Ellingrud, Goryunova |
| [[2026-05-12-mgi-virtual-event-race-takes-off-next-big-arenas|MGI Virtual Event: Race Takes Off]] | Same as above (event presentation of report) | May 2026 | Ellingrud + Russell (panelists), Bradley (moderator), Gaffey + Sastry + Shenai (panel) |

The two flagship reports (*Race Takes Off* + *Agents, Robots, and Us*) constitute MGI's **two-layer panorama** on the AI-and-economy question — *where will the value migrate* (Race Takes Off, 18 arenas) × *who and what will do the work that captures it* (Agents, Robots, and Us, 7 archetypes + Skill Change Index). Same intellectual project, designed to be read in tandem.

## Notable people (mentioned in this wiki)

**MGI directors** (per Nov 2025 acknowledgements; chair listed first):
- **Sven Smit** *(MGI chairman; senior partner, Amsterdam office)* — co-author of *Agents, Robots, and Us*. Promoted from dangling: 2nd-source author appearance.
- **Chris Bradley** *(director; co-author of Race Takes Off)*.
- **Kweilin Ellingrud** *(director; co-author of Race Takes Off)*.
- **Sylvain Johansson** *(director)*.
- **Nick Leung** *(director)*.
- **Olivia White** *(director)*.
- **Lareina Yee** *(director; senior partner, Bay Area; lead author of Agents, Robots, and Us)*.

**MGI partners** (per Nov 2025 acknowledgements):
- **Mekala Krishnan**.
- **Anu Madgavkar** *(partner, New Jersey office; second author of Agents, Robots, and Us)*.
- **Jan Mischke**.
- **Jeongmin Seong**.

**MGI senior fellows / engagement managers** (per Nov 2025 acknowledgements):
- **Maria Jesus Ramirez** *(senior fellow, Bay Area)* — sixth author of *Agents, Robots, and Us*.
- **Michael Chui** *(QuantumBlack senior fellow, Bay Area)* — fifth author of *Agents, Robots, and Us*; widely-cited McKinsey AI thought leader.
- **Alexis Krivkovich** *(senior partner, Bay Area)* — fourth author of *Agents, Robots, and Us*.
- **Diego Castresana** *(engagement manager, New York)* — seventh author of *Agents, Robots, and Us*.

**Academic advisers and named external contributors to MGI flagships**:
- **Sir Christopher Pissarides** *(Regius Professor of Economics, LSE; Nobel laureate Economics 2010)* — MGI academic adviser, *Agents, Robots, and Us*.
- **Matthew J. Slaughter** *(Paul Danos Dean, Tuck School of Business at Dartmouth)* — MGI academic adviser, *Agents, Robots, and Us*.
- **Luca Vendraminelli** *(postdoctoral researcher, Stanford Digital Economy Lab + Stanford HAI)* — named research contributor, *Agents, Robots, and Us*.

## MGI research methodology lineage (AI/automation strand)

MGI's automation-and-adoption modelling stack — used in *Agents, Robots, and Us* — was first developed in **2017** (Manyika et al., *A Future That Works*, McKinsey 2017) and refreshed for each subsequent major report:
- **2017** baseline — BLS 800 occupations × O*NET 2,000 detailed work activities × 18 human capabilities; expert-survey current/future performance estimates; sigmoidal S-curve adoption modelling.
- **June 2023** — *The economic potential of generative AI: The next productivity frontier* — added GenAI as a new capability layer; global potential ~$26T (untimed).
- **November 2025** — *Agents, Robots, and Us* — refreshed BLS + O*NET + Lightcast data; new AI-expert capability survey; new **Skill Change Index (SCI)** computed via OpenAI GPT-4o for ~3.4M skill→DWA mappings with manual 1,000-cell validation; midpoint + early/late scenario brackets; $2.9T US / $28.7T global by 2030 (now timed).

The lineage is a useful indicator of MGI methodology continuity: the same BLS + O*NET substrate appears in three reports spanning eight years, with progressive additions (GenAI capability layer in 2023; Lightcast + GPT-4o skill-mapping in 2025).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "mckinsey-global-institute") OR contains(tags, "mgi")
SORT file.name ASC
```

## Open questions

- **Continuity of the MGI two-layer panorama**: will the next flagship MGI report extend the AI-and-economy frame (technology layer, geopolitical layer, capital-flows layer), or pivot to a different theme cluster from MGI's five research themes?
- **MGI's GenAI June 2023 paper** (*The economic potential of generative AI: The next productivity frontier*) — cited as the theoretical prior for both 2025-2026 MGI reports' economic-value modelling. Open ingest target.
- **MGI's 2017 baseline paper** (Manyika et al., *A Future That Works*) — the foundational methodology paper for the automation-and-adoption model used throughout subsequent reports. Open ingest target.
- **Relationship to QuantumBlack** — Michael Chui is a *QuantumBlack senior fellow* on this Nov 2025 report; the boundary between QuantumBlack (McKinsey's AI-and-analytics arm) and MGI deserves a body note when a QuantumBlack-specific source is ingested.
