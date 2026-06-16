---
type: thread
status: open
opened: 2026-04-28
tags: [ai-maturity, ai-adoption, methodology, cross-source-comparison]
---

# Thread: How do different sources measure AI maturity, and where do they agree or diverge?

## The question

Multiple authoritative sources are publishing **adoption** and **maturity** numbers for enterprise AI, using different instruments, samples, and definitions. Sometimes they appear to converge ("most orgs aren't really mature"); sometimes they appear to diverge (78% adoption vs. 7% Stage 4). Is there a coherent meta-story across these sources, or are they measuring fundamentally different things?

## What we know so far

### From [[2026-04-28-ai-index-report-2025|AI Index 2025]] (citing McKinsey survey, n=2,854)

- **78% of orgs use AI** in at least one business function (vs. 55% in 2023).
- **71% of orgs use [[generative-ai|generative AI]]** in at least one function (vs. 33% in 2023).
- **Only 1% of C-suite executives describe their GenAI rollouts as "mature."**
- Most reported financial impact: cost savings <10%, revenue gains <5%.
- Methodology: McKinsey Global AI Survey instrument; "use" = at least one business function; "mature" = self-reported by C-suite.

### From [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan / MIT CISR]] (Future Ready Survey 2022, n=721, plus 2024 interviews at 9 enterprises)

- **Four-stage AI maturity distribution:** Stage 1 (Experiment) 28%, Stage 2 (Pilots) 34%, Stage 3 (Ways of working) 31%, **Stage 4 (Future-ready) 7%.**
- Stages 1–2 below industry-average financial performance; Stages 3–4 above.
- Maturity score = equally-weighted combination of three measures: AI effectiveness for (i) operations, (ii) customer experience, (iii) ecosystem support.
- **Greatest financial impact in moving Stage 2 → Stage 3.**

### Apparent convergence

| Question | AI Index (McKinsey) | MIT CISR | Convergence |
|---|---|---|---|
| Are most orgs "using AI"? | 78% (any function) | 100% (Stages 1–4 are *all* using AI in some sense) | Both say yes — high adoption breadth |
| Are most orgs *mature*? | 1% mature (C-suite self-report on GenAI) | 7% Stage 4 | Both say no — maturity is rare |
| Is there a clear value gradient? | Cost savings <10%, revenue <5% | Stages 1–2 below avg, Stages 3–4 above | Both say yes — but CISR locates the inflection (Stage 2→3) |

### Apparent divergence (or methodological)

- **Definition of "mature."** AI Index uses C-suite self-report on GenAI specifically. CISR uses a triangulated AI-effectiveness score across operations, CX, and ecosystem support — and mature is Stage 4, the top 7%. These are not the same metric.
- **Sample.** McKinsey n=2,854 global, 2024. CISR Future Ready n=721, **2022** — 2 years older. The 2022 baseline predates the GenAI explosion; current CISR distributions might look quite different.
- **Adoption granularity.** AI Index: binary (used in ≥1 function or not). CISR: 4 stages with explicit progression criteria. The CISR view is *richer* but the AI Index view is *more comparable across years*.

### Two more instruments (added 2026-04-28 batch)

#### From [[2026-04-28-mittri-cisco-ai-enabled-enterprise|MITTRI/Cisco]] (Cisco's 2025 readiness survey)

A **third measurement type** — *readiness and urgency*, distinct from adoption breadth or maturity stage:
- **13%** of companies globally are ready to leverage AI to its full potential.
- **68%** say their infrastructure is at best moderately ready.
- **98%** feel increased urgency over the past year.
- **85%** give themselves <18 months to deploy a strategy or face negative business effects.
- **50%** have already dedicated 10–30% of IT budget to AI.

These numbers are **complementary, not competing** with AI Index/CISR. They describe a **gap analysis** between what orgs are doing (high adoption, low maturity) and what they think they need to do (massive urgency, short deadlines, high IT spend). Caveat: Cisco's survey instrument; Cisco-favorable framing on "infrastructure readiness."

#### From [[2026-04-28-werner-lebrun-octopus-organization|Werner-Le-Brun]] (HBR Nov–Dec 2025)

A **broader org-change baseline**, not AI-specific:
- **Just 12% of transformation efforts** show sustainable performance gains, even after three years.
- Despite trillions in investment over the past 20 years.

This contextualizes the AI maturity numbers. If only 12% of *general* transformations succeed, then **CISR's 7% Stage 4 + AI Index's 1% mature is actually consistent with — possibly even worse than — the broader transformation-success baseline.** AI maturity may be even harder than general transformation, given the speed of capability change and the depth of org-redesign required.

### Updated cross-walk

| Source | What it measures | "Successful" % | Sample / instrument |
|---|---|---|---|
| AI Index 2025 (McKinsey) | GenAI rollout maturity (C-suite self-report) | **1%** mature | n=2,854, 2024, McKinsey instrument |
| MIT CISR (2022 baseline) | Stage 4 "AI future-ready" (triangulated AI-effectiveness score) | **7%** Stage 4 | n=721, 2022, CISR Future Ready Survey |
| Cisco (2025) | "Ready to leverage AI to full potential" | **13%** ready | Cisco's instrument; details thin |
| Werner-Le-Brun (HBR 2025) | Transformation efforts → sustainable performance gains | **12%** | Aggregated from cited research |

The four "success rate" numbers (1% / 7% / 12% / 13%) span a single order of magnitude despite radically different instruments — which is itself useful information: **whatever you call success, it's rare.**

## What's missing / candidate sources to find

- **Updated CISR Future Ready Survey wave** (post-2022, ideally 2024). If it exists in the wiki later, ingest it to see if Stage distributions shifted.
- **Other organizational maturity frameworks** — e.g., Gartner's AI maturity model, Deloitte's State of AI in the Enterprise, McKinsey's own "AI high-performer" framing. As of this thread opening, none have been ingested.
- **A direct MIT Sloan/CISR ↔ AI Index methodology cross-walk** — if anyone has published one. Not yet found.
- **MITTRI_Cisco** (in `raw/reports/`, not yet ingested) is sponsored MIT Tech Review Insights research, likely to introduce a third framing. Will surface in the next ingest.
- **HBR Anand-Wu Gen AI Playbook** (in `raw/articles/`, not yet ingested). Authors are at NYU Stern / HBS — different academic lineage, may have a different framing.

## How this thread should resolve

When at least 3 sources are ingested with explicit adoption/maturity definitions, this thread should resolve into a [[syntheses]] page that:

1. Lists each source's instrument, sample, and definition side-by-side.
2. Maps each source's "mature" / "high-performer" definition to the others.
3. Notes where the numerical claims agree vs. disagree.
4. Identifies what the *practical* implication is for someone trying to assess where their own org stands.

Until then, this thread stays open as a reminder to **always include the instrument when citing an adoption/maturity number** — "78% of orgs use AI" without saying "per McKinsey's at-least-one-function definition" loses important meaning.

## Related pages

- [[enterprise-ai-adoption]] — main concept page
- [[2026-04-28-ai-index-report-2025|AI Index 2025]] — first source
- [[2026-04-28-mit-sloan-ai-maturity|MIT Sloan article]] — second source
- [[MIT CISR]] — institutional source
- [[McKinsey & Company]] (dangling) — instrument source for AI Index adoption data
