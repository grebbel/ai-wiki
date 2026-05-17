---
type: concept
aliases: ["systems thinking", "systems-thinking"]
tags: [systems-thinking, innovation, sustainability, design-thinking, breakthrough-thinking, wicked-problems]
confidence: 0.75
last_confirmed: "2026-04-28"
accessed_at: "2026-04-28"
source_count: 1
relationships:
  - type: supports
    target: enterprise-ai-adoption
    via: "workflow redesign in the micro-productivity-trap escape is systems-thinking applied to AI"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Systems Thinking

A mode of reasoning and innovation that **focuses on flows, relationships, feedback loops, and unintended consequences across an interconnected ecosystem**, rather than on a bounded product, service, or user. Distinguished from **breakthrough thinking** (Silicon-Valley "move fast and break things") and **design thinking** (IDEO-style user-centric iteration).

## Working definition

Per [[2026-04-28-bansal-birkinshaw-systems-thinking|Bansal & Birkinshaw (2025)]], building on Bertalanffy's general-systems theory, Jay Forrester's system dynamics, and Peter Senge's *The Fifth Discipline* (1990):

- **Systems thinking** = recognizing that the modern economy is a network of people, products, finances, and data; changes in one node have side effects in others; innovation must be designed with these flows in mind.
- The aim is to make entire systems more sustainable and resilient, accepting that benefits in one part of the system may be outweighed by harm done elsewhere if the cross-effects aren't traced.

## Key claims

### Three modes of innovation ([[2026-04-28-bansal-birkinshaw-systems-thinking|Bansal & Birkinshaw 2025]])

| Mode | Method | Strengths | Side effects |
|---|---|---|---|
| **Breakthrough thinking** | Slice the Gordian knot; "10× / winner-take-all"; Zuckerberg's "move fast and break things" | Speed; dramatic progress on bounded problems | Knock-on damage; well-suited only to clearly bounded problems (rocketry) |
| **Design thinking** | Empathy-driven iteration on user need; IDEO/Senge popularization | User-centric clarity; cuts through complexity | Obsession with the user creates problems for non-users (e.g., Airbnb solving for hosts/travelers but harming local housing) |
| **Systems thinking** | Map flows + relationships; iterate problem framings | Avoids unintended consequences; embraces complexity | Slower; harder; "least common mode of innovation" |

### Why systems thinking is rare in practice

- Traditional approach demands modeling all flows, interactions, feedback loops — daunting in fast-changing worlds where models can't reflect reality.
- Systems thinkers spend time figuring out exactly how the Gordian knot is tied — almost guaranteed to be overtaken by a design thinker (slicing) or a breakthrough thinker (single-strand focus).

### Streamlined four-principle approach (Innovation North initiative, [[Ivey Business School]])

1. **Define your desired future state** — articulate a *North Star* for the firm's role in the future system. Example: Maple Leaf Foods' shift from "meat processor" to "the most sustainable protein company on Earth" (CEO Michael McCain).
2. **Frame the problem, reframe it, and repeat** — wicked problems lack a single definition; iterating reframings engages stakeholders who experience the system's dysfunctions differently. Example: U of Guelph reframing climate change → soil health for farmer engagement.
3. **Focus on flows and relationships, not products or services** — Co-operators insurance introduced "drying in place" and "soft contents" cleaning to redirect the flow of damaged materials away from landfills, without launching a new product.
4. **Nudge your way forward** — pursue an "ecology of actions" rather than a moonshot/silver bullet. Example: CSA Group's circular built environment program — small actions across architects, engineers, developers, owners, plus a "coalition of the willing."

### Wicked problems (Rittel & Webber, 1973 — implicit reference)

- Constantly changing, hard to define, multiple stakeholders with divergent experiences of the system's dysfunctions.
- Solutions involve difficult trade-offs.
- Systems thinking is best suited here; breakthrough/design thinking misfit.

### Examples cited in the wiki

- **Maple Leaf Foods** — repositioning meat processor → "sustainable protein company" → tens of millions in new value, partnership with Meat Institute on Protein PACT.
- **University of Guelph regenerative agriculture program** — climate change reframed as soil health.
- **Co-operators (Canadian insurance)** — "drying in place" + "soft contents" cleaning to disrupt the flow of damaged materials to landfills.
- **CSA Group circular built environment** — UN Environment Programme cites ~37% of global carbon emissions from built environment, ~38% reducible through circular design.

## Related concepts

- [[enterprise-ai-adoption]] — AI deployment decisions are often systems-thinking problems (knock-on effects across users, communities, supply chains).
- [[automation-vs-augmentation]] — strategic deployment choices have systemic consequences beyond the deploying firm.
- [[dynamic-capabilities]] — systems thinking informs sensing/seizing/transforming under interconnected change.
- [[strategic-foresight]] — both approaches treat the firm as embedded in a larger interacting system.
- [[ai-deskilling]] — task-composition shifts within retained jobs are a systems-level effect of AI adoption.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "systems-thinking")
SORT file.name ASC
```

## Open questions

- Single primary source in the wiki so far ([[2026-04-28-bansal-birkinshaw-systems-thinking|Bansal & Birkinshaw]]); deeper Senge and Forrester texts would strengthen the concept.
- How does systems thinking interact with AI tooling? Specifically: AI systems excel at slicing the Gordian knot (breakthrough mode) and at user-centric iteration (design mode); whether they can support genuinely systems-level analysis is open.
