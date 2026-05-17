---
type: concept
aliases: ["Warner-Wäger process model", "Warner & Wager process model", "W&W process model", "digital-transformation process model"]
tags: [dynamic-capabilities, digital-transformation, microfoundations, warner-wager, wiki-vocabulary]
confidence: 0.75
last_confirmed: "2026-05-14"
accessed_at: "2026-05-17"
source_count: 1
relationships:
  - type: instance-of
    target: dynamic-capabilities
    via: "the process-model elaboration of Teece's three-cluster framework, specialised for digital transformation"
  - type: authored-by
    target: 2026-04-28-warner-wager-dynamic-capabilities-digital-transformation
quality_score: 0.84
quality_notes: ['citation density 1.5/1000 words (2 source links in 1344 words; target ≥3.0)']
---

# Warner & Wäger Process Model

The process-model elaboration of Teece's [[dynamic-capabilities]] framework, specialised for digital transformation. Warner & Wäger ([[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation|2019]]) decompose **sense → seize → transform** into **nine empirically-grounded microfoundations** plus **three strategic-renewal outcomes** and a contextual triggers/enablers/barriers ring.

This page is **both an explainer and a vocabulary spec**: the slugs below are the closed vocabulary used by the `dynamic_capabilities:` and `roles:` frontmatter fields documented in [`CLAUDE.md` §Dynamic-capabilities tagging](../../CLAUDE.md#dynamic-capabilities-tagging). The matrix at the bottom is the single source of truth for the role-defaults mapping used to compute role-relevance from `dynamic_capabilities:` tags.

## Microfoundations vocabulary (closed)

Tagging is at the **microfoundation level** — twelve cells total: nine microfoundations across three clusters, plus three strategic-renewal outcomes, plus an optional ring of three contextual factors. The bulleted detail under each cell is the **first-order-concept layer** from the paper (Fig. 1 *Data structure*); it is **not** itself part of the slug vocabulary, but reads as the operational definition: *use this slug when the source's content speaks to one or more of these activities.*

### Digital sensing

- **`digital-sensing/digital-scouting`** — scanning for technological trends; screening of digital competitors; sensing customer-centric trends.
- **`digital-sensing/digital-scenario-planning`** — analyzing scouted signals; interpreting digital future scenarios; formulating digital strategies.
- **`digital-sensing/digital-mindset-crafting`** — establishing a long-term digital vision; enabling an entrepreneurial mindset; promoting a digital mindset.

### Digital seizing

- **`digital-seizing/rapid-prototyping`** — creating minimum viable products; considering a lean start-up methodology; using a digital innovation lab.
- **`digital-seizing/balancing-digital-portfolios`** — balancing internal and external options; scaling up innovative business models; setting an appropriate speed of execution.
- **`digital-seizing/strategic-agility`** — rapidly reallocating resources; accepting redirection and change; pacing strategic responses.

### Digital transforming

- **`digital-transforming/navigating-innovation-ecosystems`** — joining a digital ecosystem; interacting with multiple external partners; exploiting new ecosystem capabilities.
- **`digital-transforming/redesigning-internal-structures`** — hiring a chief digital officer; digitalization of business models; designing team-based structures.
- **`digital-transforming/improving-digital-maturity`** — identifying digital workforce maturity; external recruiting of digital natives; leveraging digital knowledge inside the firm.

### Strategic renewal (Fig. 2 outcomes)

W&W's Fig. 2 does not decompose these into first-order-concept bullets the way Fig. 1 does for microfoundations; the operational definitions below are drawn from the cross-case body text (§§ "Strategic renewal of business model / collaborative approach / organizational culture").

- **`strategic-renewal/business-model`** — replacing transactional product logics with relational/multi-sided value propositions; refreshing or replacing the firm's value-creation/value-capture logic.
- **`strategic-renewal/collaborative-approach`** — refreshing or replacing internal R&D / cross-team patterns and external partner ecosystems; opening company boundaries to co-creation.
- **`strategic-renewal/organizational-culture`** — refreshing legacy cultures toward digital-mindset, entrepreneurial, fast-and-flexible cultures; embedding new shared values across the workforce.

### Contextual factors (optional, when load-bearing in the source)

- **`contextual/external-triggers`** — disruptive digital competitors; changing consumer behaviours; disruptive digital technologies.
- **`contextual/internal-enablers`** — cross-functional teams; fast decision making; executive support.
- **`contextual/internal-barriers`** — rigid strategic planning; high level of hierarchy; change resistances.

## Role-relevance inheritance

A second view onto the same vocabulary: each cell carries a **default role profile** — the business roles that would typically care about a source touching that cell. A role-scoped agent ("acting on behalf of a CHRO") can navigate the corpus by org-chart slice without the wiki re-tagging per source.

### Roles vocabulary (closed)

Fifteen slugs, kebab-case:

**C-suite (9):** `ceo`, `coo`, `cfo`, `cso` *(Chief Strategy Officer)*, `cdo` *(Chief Digital Officer)*, `cto`, `cio`, `chro`, `cmo`.

**Functional / operational (6):** `product-manager`, `tech-lead`, `rd-director`, `innovation-lab-lead`, `transformation-lead`, `strategy-consultant`.

The taxonomy is grounded in (a) W&W's interview sample from Table 2 — Director of Digital Transformation, VP of Strategy, Director of Digital Banking, Head of Digital Consulting, Director of Sales, Director of Digital Strategy, Chief Digital Officer; (b) explicit role-mentions in the microfoundations themselves (e.g. "hiring a chief digital officer" appears verbatim in `redesigning-internal-structures`); (c) the functional roles W&W's activities clearly imply (a `digital innovation lab` doing `rapid-prototyping` implies an Innovation Lab Lead and Product Managers; tech leads own architecture calls during MVP work).

### Role-defaults matrix

Each cell maps to 2–4 roles — the **smallest set that captures who owns the activity**, not an exhaustive list. These are starting defaults grounded in W&W's empirical signals, not W&W canon; refinable as the wiki grows.

```yaml
role_defaults:
  digital-sensing/digital-scouting: [cso, cdo, strategy-consultant]
  digital-sensing/digital-scenario-planning: [cso, cdo, strategy-consultant]
  digital-sensing/digital-mindset-crafting: [ceo, chro, transformation-lead]
  digital-seizing/rapid-prototyping: [product-manager, tech-lead, cto, innovation-lab-lead]
  digital-seizing/balancing-digital-portfolios: [cfo, cso, ceo]
  digital-seizing/strategic-agility: [ceo, coo, transformation-lead]
  digital-transforming/navigating-innovation-ecosystems: [cdo, cto, rd-director]
  digital-transforming/redesigning-internal-structures: [cdo, chro, ceo]
  digital-transforming/improving-digital-maturity: [chro, cdo, cio]
  strategic-renewal/business-model: [ceo, cso, cmo]
  strategic-renewal/collaborative-approach: [cio, cdo, rd-director]
  strategic-renewal/organizational-culture: [chro, ceo]
  contextual/external-triggers: [cso, cdo]
  contextual/internal-enablers: [chro, transformation-lead]
  contextual/internal-barriers: [chro, ceo]
```

| Cell | Default roles | Why |
| --- | --- | --- |
| `digital-sensing/digital-scouting` | `cso, cdo, strategy-consultant` | External trend/competitor scanning is owned by strategy; W&W's data is built on senior strategy consultants doing exactly this work. |
| `digital-sensing/digital-scenario-planning` | `cso, cdo, strategy-consultant` | "Formulating digital strategies" is the strategy function's core deliverable. |
| `digital-sensing/digital-mindset-crafting` | `ceo, chro, transformation-lead` | Long-term vision + entrepreneurial-mindset work is leadership + culture; HR owns the workforce side. |
| `digital-seizing/rapid-prototyping` | `product-manager, tech-lead, cto, innovation-lab-lead` | MVPs / lean startup / digital innovation lab is product + engineering; tech leads own architecture calls during MVP work. |
| `digital-seizing/balancing-digital-portfolios` | `cfo, cso, ceo` | Capital allocation across legacy and digital bets is a finance + strategy + top-exec call. |
| `digital-seizing/strategic-agility` | `ceo, coo, transformation-lead` | Rapidly reallocating resources and pacing strategic responses is a top-exec / operations decision. |
| `digital-transforming/navigating-innovation-ecosystems` | `cdo, cto, rd-director` | Partner ecosystems, co-creation, joint R&D. |
| `digital-transforming/redesigning-internal-structures` | `cdo, chro, ceo` | W&W names "hiring a chief digital officer" as the canonical activity; team-based structures are HR + CEO. |
| `digital-transforming/improving-digital-maturity` | `chro, cdo, cio` | Digital workforce maturity, recruiting digital natives, leveraging digital knowledge = HR + IT + CDO. |
| `strategic-renewal/business-model` | `ceo, cso, cmo` | Value-creation/value-capture logic is a top-exec + commercial decision. |
| `strategic-renewal/collaborative-approach` | `cio, cdo, rd-director` | R&D collaboration patterns and external partner ecosystems. |
| `strategic-renewal/organizational-culture` | `chro, ceo` | Culture refresh is HR-led, CEO-sponsored. |
| `contextual/external-triggers` | `cso, cdo` | Market-sensing. |
| `contextual/internal-enablers` | `chro, transformation-lead` | Cross-functional teams, fast decision-making, executive support all live with HR + transformation. |
| `contextual/internal-barriers` | `chro, ceo` | Rigid planning, hierarchy, change resistance — culture and leadership levers. |

### Per-source override semantics

Sources may add a `roles:` frontmatter list when their emphasis diverges from the cell default. When `roles:` is present, it **replaces** the inherited defaults for that source. Half-overrides ("add this role, keep the others") are not supported — the override case is rare enough that "write the full list you mean" is fine.

```yaml
# Implicit: roles inherited from the dynamic_capabilities tag
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
# (computed roles: cdo, chro, ceo)

# Explicit override: source emphasises one role specifically
dynamic_capabilities:
  - digital-transforming/redesigning-internal-structures
roles: [chro]
```

The field is `roles:` (not `audience:` or `personas:`) to mirror the existing person-entity convention. On a source page it's a **list of role slugs** drawn from the closed vocabulary above; on a person-entity page `roles:` (if used) remains a **free-text job title**. Lint distinguishes by `type:`.

**The body-twin rule does NOT extend to roles.** The body sentence describing how the source touches a W&W cell already implies the relevant roles; restating "and a CHRO would care because…" would be padding. Role-relevance is a *derived* view, not an independent claim.

## Related concepts

- [[dynamic-capabilities]] — the broader Teece framework that W&W specialise for digital transformation.
- [[2026-04-28-warner-wager-dynamic-capabilities-digital-transformation]] — the source paper that supplies this vocabulary.
- [[enterprise-ai-adoption]] — current-instantiation lens; AI adoption sits inside `digital-seizing` (rapid prototyping, balancing portfolios) and `digital-transforming` (redesigning internal structures, improving digital maturity).

## Open questions

- Should `dynamic_capabilities:` tags carry an optional `confidence:` like typed relationships? Deferred — the tag is currently a binary "touches / doesn't touch" classification.
- Should the role taxonomy be extracted into `wiki/.vocab/roles.yaml` so lint and future Quartz views can read it programmatically? Deferred to whichever issue first needs programmatic access; for now the vocabulary lives here.
- Backfill of pre-2026-05-14 source pages is forward-only by default. A supervised backfill pass is a candidate follow-up issue.
