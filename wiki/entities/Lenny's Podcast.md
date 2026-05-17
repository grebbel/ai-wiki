---
type: entity
kind: venue
aliases: ["Lenny's Podcast", "Lennys Podcast", "lennypodcast", "Lenny Rachitsky's podcast"]
tags: [lenny-podcast, podcast, product-management, consumer-tech, ai-era-strategy, founder-interviews, lenny-rachitsky]
since: 2022
confidence: 0.75
last_confirmed: "2026-05-14"
accessed_at: "2026-05-14"
source_count: 2
relationships:
  - type: published-by
    target: 2026-05-10-ries-lennys-force-destroys-companies-within
    via: "Eric Ries on Incorruptible — governance, mission, and the force that destroys companies (10 May 2026)"
  - type: published-by
    target: 2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo
    via: "Evan Spiegel (Snap CEO) on distribution as the new moat, software not being a moat, and Snap's design-led operating model (26 April 2026)"
---

# Lenny's Podcast

Long-form interview podcast hosted by **Lenny Rachitsky** (ex-Airbnb PM; founder of *Lenny's Newsletter* and the *How I AI* companion show). The podcast publishes ~1–2 episodes per week, primarily interview-format with product leaders, founders, and operators in consumer-tech, B2B SaaS, and AI. The wiki has, as of May 2026, **two sources under this `author:` value** — the second of which triggered this entity page per the [author-entity promotion rule](../../CLAUDE.md#author-entity-promotion).

Lenny Rachitsky himself is not (yet) given his own entity page because he does not appear as a *first author* in the wiki's `author:` frontmatter — he is the host of *Lenny's Podcast* (this entity) and of the *How I AI* companion show, which appears in the wiki via [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]] under `author: ["How I AI"]`. The two channels are operationally distinct.

## Sources under this author

| Source | Guest | Topic anchor |
|---|---|---|
| [[2026-04-26-how-to-win-when-software-is-not-a-moat-evan-spiegel-snapchat-ceo\|Spiegel 2026]] | **Evan Spiegel** (Snap CEO) | Software-is-not-a-moat learned over 15 years; distribution-as-new-moat; design-as-intentional-bottleneck; JTBD-as-AI-sequencing |
| [[2026-05-10-ries-lennys-force-destroys-companies-within\|Ries 2026]] | **Eric Ries** (Lean Startup; *Incorruptible*) | Governance as the unit of mission protection; PBC + LTBT as defensive structure; Conway's law applied to AI alignment |

Both episodes are operator-narrated and run ~70 minutes to ~100 minutes. Both lean into structural arguments about *durability under change* rather than tactical product advice. The pairing is mutually-reinforcing: Ries on the **legal-entity layer**, Spiegel on the **operating-model layer** — see the *Convergence and contradictions* sections of the respective source pages for the cross-link analysis.

## Disclosure flag

Both episodes carry the same standing disclosure: *"Lenny may be an investor in the companies discussed."* Lenny does not enumerate his portfolio per episode. Source-quality consequence: confidence in framing of *specific named companies* is slightly attenuated where Lenny's framing matters; the *structural-argument* contributions of each episode are largely independent of any specific portfolio holding.

## Related entities and threads

- [[Anthropic]] — referenced approvingly in both episodes (Ries on the LTBT structure; Spiegel on Claude Cowork and Jenny Wen).
- [[OpenAI]] — referenced in Ries 2026 as the structural foil to Anthropic; passing references in Spiegel 2026.
- *How I AI* (Lenny Rachitsky's companion show, separate `author:` value) — appears via [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]].

## Open candidates for ingest

The episode-archive at lennysnewsletter.com (cited in the Spiegel transcript) lists prior episodes referenced by Spiegel that may be worth ingesting:

- **Keith Rabois (Khosla Ventures) — "Hard truths about building in the AI era"** — referenced in Spiegel 2026.
- **Marc Andreessen — "The real AI boom hasn't even started yet"** — referenced in Spiegel 2026; also the source of the *designer-PM-engineer triad* framing Spiegel critiques.
- **Jenny Wen (head of design at Claude) — "The design process is dead. Here's what's replacing it."** — referenced in Spiegel 2026; would substantiate the *designers-shipping-code* construct directly from a designer-side operator.
- **Rahul Vohra (Superhuman) — secret-to-success interview** — referenced in Spiegel 2026.

None are claims about Lenny's Podcast itself; they are dangling forward-references this entity page captures so future ingests have a head-start.
