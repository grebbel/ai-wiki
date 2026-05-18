---
type: concept
aliases: ["analogical reasoning", "analogical-reasoning", "strategy by analogy", "predictive analogy"]
tags: [analogical-reasoning, strategy-theory, theory-based-view, carroll, sorensen]
confidence: 0.75
last_confirmed: "2026-04-28"
accessed_at: "2026-05-18"
source_count: 1
relationships:
  - type: supports
    target: strategic-foresight
    via: "disciplined analogies are a sensing/scenario tool"
  - type: supports
    target: theory-based-view
    via: "[[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]] position disciplined analogy as the practical methodology for [[theory-based-view]] (TBV) theory-discovery — analogies aid theory discovery, wider-team theory engagement, identifying unique aspects, and communication"
quality_score: 0.99
quality_notes: ['1 near-empty section(s)']
---

# Analogical Reasoning (in Strategy)

The use of **analogies between a known source case and an unknown target case** to inform strategy formulation, communication, or evaluation. Logicians regard analogy as a weak inductive form, yet practitioners use it pervasively. The wiki's anchor source ([[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]]) argues analogies should be *disciplined*, not banished.

## Working definition

Two roles of analogy in strategy discourse (Gentner 1982):

| Role | Use |
|---|---|
| **Rhetorical / persuasive** | Vivid metaphor for stakeholders ("Glassdoor is Tripadvisor for jobs") |
| **Generative / problem-solving** | Surface candidate causal mechanisms; develop firm-specific theory of value |

A **predictive analogy** has the structure: source A has features a₁, a₂, … and outcome a_c; target B has features b₁, b₂, … (where b_n is similar to a_n); therefore the unknown b_c is *plausibly* similar to a_c.

## Key claims

### Why analogies dominate strategy discourse despite weak logical foundations

1. **Efficient communication** — a one-phrase analogy carries vast detail.
2. **Concrete and memorable** — material analogies vivid; abstract theories aren't.
3. **Predictive even when conceptual understanding is limited**.
4. **Generative problem-solving tool** — best solutions often generalize from familiar puzzles.
5. **Intermediate-level abstraction** — neither too specific nor too abstract; matches how busy executives reason.
6. **Success-story anchoring** — the source firm worked, providing existence proof.

### Practical tools for disciplining strategy analogies ([[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]])

1. **Decompose** the global analogy into atomic feature premises.
2. **Add negative analogies** (where source and target *differ*).
3. **Distinguish horizontal vs. vertical relations** (Hesse 1966):
   - Horizontal = surface similarity between source and target features.
   - Vertical = causal relationships within source that produced its outcome.
4. **Test the vertical relations** — does the source's success theory plausibly transfer?
5. **Build multiple analogies in parallel** — increases predictive ability.

### Connection to the theory-based view of strategy

The **theory-based view (TBV)** of strategy (Felin & Zenger 2009, 2017) asks executives to develop firm-specific theories of value:

1. What is your firm's theory of value?
2. Is your theory novel, simple, elegant?
3. Is it falsifiable / generalizable / generative?
4. Who must you convince for your theory to be realized?

Analogies aid TBV in **theory discovery**, **wider-team theory engagement**, **identifying unique aspects**, and **communication**.

### Worked example: Glassdoor / Tripadvisor

| Tripadvisor (source) | Glassdoor (target) |
|---|---|
| experiential-good info (hotels) | experiential-good info (jobs) |
| free + open access | free + open access |
| user-generated content | user-generated content |
| five-star ratings + detailed reviews | same |
| collects data → reports + trend prediction | same |
| ad/referral revenue | same |
| **market success** | **plausibly similar** |

Negative premises (where the analogy *fails* or weakens): travel events vs. ongoing employment; willingness to disclose negative experiences; user registration requirements.

### AI-related analogy noted in passing

The paper's footnote-level example: a leaked Google memo (Patel & Ahmad 2023) characterized the open-source AI threat to GPT-4 as *"if GPT-4 is the Walmart you go to for apples, what happens when a fruit stand opens in the parking lot?"* — illustrating the analogy form in a current AI strategy debate.

## Related concepts

- [[theory-based-view]] — the framework analogical reasoning supports in [[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]]'s framing. Disciplined analogy is the practical methodology for TBV theory-discovery; TBV is the falsifiability layer that disciplines what counts as a *good* analogy.
- [[strategic-foresight]] — analogies between historical convergence cycles and the current period are explicitly invoked in [[2026-04-28-ftsg-convergence-outlook-2026|FTSG 2026]] (industrial revolution, post-WWII, late-1990s).
- [[dynamic-capabilities]] — sensing involves analogizing across industries, contexts, time periods.
- [[2026-04-28-anand-wu-genai-playbook|Anand-Wu's 2×2]] — itself a kind of generative analogical structure for matching deployment context to AI use case.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "analogical-reasoning")
SORT file.name ASC
```

## Open questions

- Single-source coverage at present ([[2026-04-28-carroll-sorensen-strategy-analogy]]); related Gavetti & Rivkin work (2005, 2014) and Felin & Zenger TBV writings would deepen the page.
- Open question whether LLMs can serve as effective analogy-generation tools for strategy work — the [[jagged-frontier]] suggests they may be especially good at the *rhetorical* role and potentially weaker at the *generative/causal* role.
