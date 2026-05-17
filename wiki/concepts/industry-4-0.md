---
type: concept
aliases: ["Industry 4.0", "I4.0", "industry-4-0", "Fourth Industrial Revolution"]
tags: [industry-4-0, smart-manufacturing, iot, cyber-physical-systems, digital-transformation]
confidence: 0.85
last_confirmed: "2026-04-28"
accessed_at: "2026-04-28"
source_count: 4
relationships:
  - type: caused
    target: lean-4-0
    via: "Industry 4.0 technologies enabled the Lean Manufacturing + digital synergy"
  - type: uses
    target: ai-agents
    via: "autonomous monitoring (Jidoka + AI-powered) is an Industry 4.0 deployment of agents"
quality_score: 0.75
quality_notes: ['missing ## Debates and supersession (concept with >1 source)', '1 near-empty section(s)', '2 broken body wikilink(s)']
---

# Industry 4.0

The framing of a **fourth industrial revolution** characterized by hyperconnected, intelligent production ecosystems built on cyber-physical systems, the Internet of Things (IoT), AI/ML, big data analytics, robotics, and cloud computing. Introduced by the **German government in 2011** as part of its high-tech strategy. Now a standard reference frame in manufacturing, supply chain, and operations literature globally.

## Working definition

The four "industrial revolutions" framing:
- **1st** (~1780s): mechanization (water/steam power)
- **2nd** (~1880s): electrification, mass production
- **3rd** (~1970s): computerization, automation, IT
- **4th** (~2010s onward): cyber-physical systems — physical processes monitored and controlled by intelligent, networked digital systems

The Industry 4.0 toolkit (per [[2026-04-28-gomaa-lean-4-0|Gomaa 2025]] Table II — 23 essential technologies):
Digital Twin, IoT Sensors, Workflow Automation Software, Big Data Analytics, Collaborative Platforms, Process Mapping Software, Automated Inventory Systems, Digital Kanban Boards, Sensor-Based Error Detection, AI-Powered Monitoring Systems, Machine Learning Algorithms, Simulation/Modeling Tools, Predictive Maintenance Tools, Production Planning Tools, Real-Time Alert Systems, Automated Inspection Systems, Smart Manufacturing Cells, Smart Conveyor Systems, AR Displays, IoT Tool Tracking, Decision Support Systems, ERP Systems, Cloud-Based Maintenance Platforms.

## Key claims

### As empirical reality

- **AI use in manufacturing functions, 2025** (per National Association of Manufacturers data via [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]]): manufacturing & production 39%; inventory management 33%; quality operations 24%; R&D 24%; IT/OT 21%; equipment maintenance 17%.
- **72% of manufacturers** report AI has reduced costs and improved operational efficiency (NAM data via MITTRI/Cisco).
- Industrial robotics ([[2026-04-28-ai-index-report-2025|AI Index 2025]] §4.5):
  - **541,000** industrial robots installed worldwide in 2023 (slight YoY decrease, first since 2019).
  - Operational stock: **4.28M** robots globally in 2023.
  - **China dominates: 51.1% of global installations** (276,300 in 2023, more than rest of world combined since 2021).
  - Top 5 countries: China > Japan (46.1k) > U.S. (37.6k) > S. Korea (31.4k) > Germany (28.4k).
  - Collaborative robots ("cobots") rose from **2.8% (2017) to 10.5% (2023)** of new installs — an emphasis on human-facing roles.

### As conceptual frame

- **Industry 4.0 is the umbrella term for the digital side** of the [[lean-4-0|Lean 4.0]] synergy. Gomaa pairs each Lean tool with an Industry 4.0 technology that operationalizes it.
- The pattern generalizes beyond manufacturing — [[Italgas]]'s 300TB data platform, IoT-enabled gas distribution, 23 AI models, and DANA (GenAI network control) are Industry 4.0 in a non-manufacturing sector. Source: [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan]].

## Connection to the rest of the wiki

Industry 4.0 sits at the **intersection of manufacturing/operations work and the broader [[generative-ai|GenAI]] / [[ai-agents]] story** unfolding in white-collar work:

- The **predictive maintenance** strand of Industry 4.0 (TPM + Predictive Maintenance Tools, in Gomaa's mapping) is a domain where AI agents operate today with measurable ROI.
- The **digital twin** technology — virtual replicas of physical assets — is a recurring concept in industrial AI; relevant to [[Italgas]]'s 300TB platform and Ford's computational fluid dynamic test (15 hr → 10 sec, per [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]]).
- **Industrial robotics** (China's 51.1% global share) is the physical-world counterpart to the knowledge-work agent story.

## Debates / contradictions

- **"Beyond Industry 4.0" / "Industry 5.0".** Some literature (cited in [[2026-04-28-gomaa-lean-4-0|Gomaa]]) is already pushing toward "Industry 5.0" or "Beyond Industry 4.0" framings emphasizing human-centric and sustainable manufacturing. The wiki has only Industry 4.0 sources for now; track the 5.0 framing if it appears in future ingests.
- **Energy and sustainability.** Industrial AI is energy-intensive (data centers + cyber-physical systems). The [[2026-04-28-ai-index-report-2025|AI Index 2025]] reports **carbon emissions from training rising** (Llama 3.1 405B at 8,930 tons), and Microsoft/Google/Amazon are signing nuclear-energy deals to power AI infrastructure. Industry 4.0's sustainability claims need to be evaluated against the rising energy footprint.
- **SME viability.** Industry 4.0 technologies are written for and adopted by large manufacturers. [[2026-04-28-gomaa-lean-4-0|Gomaa]] flags SME scalability as a research gap.

## Related concepts

- [[lean-4-0]] — the Lean + Industry 4.0 synergy framework
- [[ai-agents]] — autonomous monitoring/control systems are Industry 4.0 agents
- [[generative-ai]] — increasingly entering industrial control loops (DANA at Italgas)
- [[enterprise-ai-adoption]] — manufacturing-specific lens

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "industry-4-0") OR contains(tags, "smart-manufacturing")
SORT file.name ASC
```
