---
type: concept
aliases: ["dynamic capabilities", "dynamic-capabilities", "Teece dynamic capabilities", "sense seize transform"]
tags: [dynamic-capabilities, teece, strategic-renewal, digital-transformation, microfoundations]
confidence: 0.90
last_confirmed: "2026-04-28"
accessed_at: "2026-05-17"
source_count: 4
relationships:
  - type: supports
    target: enterprise-ai-adoption
    via: "AI adoption requires dynamic-capability microfoundations to scale"
quality_score: 0.79
quality_notes: ['missing ## Debates and supersession (concept with >1 source)', '1 near-empty section(s)']
---

# Dynamic Capabilities

A firm-level capability for **sensing opportunities and threats, seizing them, and transforming the firm's resource base** in response to changing environments. Distinguished from **ordinary capabilities** (doing things right; replicable; outsourceable) by their role in *governing the rate of change* of ordinary capabilities. Origin: David Teece (1997, 2007).

## Working definition

Per Teece (2007, as quoted in [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger 2019]]):

> Dynamic capabilities = "a company's capacity to (a) sense and shape opportunities and threats, (b) seize opportunities, and (c) maintain competitiveness through enhancing, combining, protecting, and, when necessary, reconfiguring the business enterprise's intangible and tangible assets."

> "Dynamic capabilities are about doing the right things, whereas ordinary capabilities are about doing things right." (Teece & Leih 2016)

## Key claims

### The three-cluster framework (Teece 2007)

| Cluster | Function |
|---|---|
| **Sensing** | Scanning the external environment for trends/threats; opportunity identification |
| **Seizing** | Mobilizing resources to capture opportunities; new business model design |
| **Transforming** | Reconfiguring the firm's asset base; renewal of structures and culture |

### Microfoundations for digital transformation ([[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|Warner & Wäger 2019]])

Empirically identified across 7 incumbent German MNCs and 18 strategy-consultant interviews — **nine subcapabilities** organized under the three clusters:

| Cluster | Microfoundation | What it does |
|---|---|---|
| **Digital Sensing** | Digital scouting | Tech trends; competitor screening; customer-centric trend sensing |
| | Digital scenario planning | Signal analysis; future-scenario interpretation; digital-strategy formulation |
| | Digital mindset crafting | Long-term vision; entrepreneurial mindset; cultural promotion |
| **Digital Seizing** | Rapid prototyping | MVPs; lean startup; digital innovation lab |
| | Balancing digital portfolios | Internal/external option balance; scaling new BMs |
| | Strategic agility | Rapid resource reallocation; redirection acceptance; strategic pacing |
| **Digital Transforming** | Navigating innovation ecosystems | Partner interaction; co-creation; ecosystem capabilities |
| | Redesigning internal structures | CDO appointment; team-based structures; BM digitalization |
| | Improving digital maturity | Workforce maturity; digital natives; internal knowledge leverage |

### Three forms of strategic renewal that result

- **Business model renewal** — replacing transactional product logics with relational/multi-sided value propositions.
- **Collaborative-approach renewal** — replacing siloed, internal-only collaboration with cross-functional and external-ecosystem collaboration.
- **Cultural renewal** — refreshing or replacing legacy cultures with digital-mindset / entrepreneurial cultures.

### Contextual factors

| External triggers | Internal enablers | Internal barriers |
|---|---|---|
| Disruptive digital competitors | Cross-functional teams | Rigid strategic planning |
| Changing consumer behaviors | Fast decision making | Change resistances |
| Disruptive digital technologies | Executive support | High level of hierarchy |

### Why digital transformation requires *new* dynamic capabilities

- New digital technologies (AI, cloud, IoT, blockchain) change the *nature and purpose* of dynamic capabilities — not merely their content.
- Organizations can now scale up/down at speed, ease, and cost not previously possible.
- The convergence and generativity of digital technologies forces incumbents to behave entrepreneurially even when entering competitively *established* markets.

## Related concepts

- [[enterprise-ai-adoption]] — AI adoption is a contemporary instantiation of digital transformation; the same sensing/seizing/transforming logic applies, with AI-specific subcapabilities.
- [[generative-ai]] — extends the digital-transformation context; GenAI is a current sensing/seizing target for incumbents.
- [[automation-vs-augmentation]] — a strategic-deployment choice that lives within seizing capabilities.
- [[strategic-foresight]] — sensing-cluster microfoundation; FTSG-style methods are sensing tools.
- [[systems-thinking]] — adjacent lens for transforming-cluster decisions about flows and ecosystem boundaries.
- [[2026-04-28-mit-sloan-ai-maturity|MIT CISR Four Stages]] — staged-maturity view of digital/AI transformation; complementary to the dynamic-capabilities lens.
- [[2026-04-28-werner-lebrun-octopus-organization|Octopus / Tin Man]] — adjacent framing of org design under environmental change.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "dynamic-capabilities")
SORT file.name ASC
```

## Open questions

- The Warner & Wäger study is from 2019, pre-GenAI. How do the nine microfoundations need to be updated for the [[2026-04-28-anthropic-economic-index-q4-2025|2026 GenAI context]]? (Open question; possible synthesis topic.)
- Cross-source mapping: MIT CISR's Four S (Strategy/Systems/Synchronization/Stewardship) and the dynamic-capabilities framework appear to overlap substantially in scope but use different vocabularies. Would benefit from a future synthesis page.
