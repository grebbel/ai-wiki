---
type: concept
aliases: ["agent development lifecycle", "ADLC", "agent SDLC", "agent lifecycle"]
tags: [agent-development-lifecycle, adlc, ai-agents, agent-engineering, lifecycle-frameworks, sdlc-parallel]
confidence: 0.70
last_confirmed: "2026-05-08"
source_count: 1
relationships:
  - type: part-of
    target: ai-agents
    via: "the SDLC-parallel process construct for agent engineering — design, evaluate, deploy, publish, observe"
  - type: uses
    target: agent-harness
    via: "stages 4–7 of the lifecycle (implement tools / context engineering / evaluate / UAT) are mostly harness-construction work"
---

# Agent Development Lifecycle (ADLC)

A **process** construct — analogous to the Software Development Lifecycle (SDLC) for traditional software — naming the recurring stages of building, validating, deploying, distributing, and operating an [[ai-agents|AI agent]]. The vocabulary entered the wiki via Google's [[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Agents CLI announcement]] (22 April 2026), which positioned the CLI as "the unified programmatic backbone for the ADLC on Google Cloud."

This page is a **stub** on a single source. Confidence is set defensively at `0.70`. Future ingests describing parallel lifecycles (whether by Anthropic, Microsoft, or non-vendor practitioners) will substantiate or reshape it.

## Working definition

An **agent development lifecycle** is the ordered (but iterating) set of stages a team works through to take an agent from idea to production and onward to maintenance. It is distinct from but tightly entangled with [[agent-harness]] — the harness is the *runtime layer* the lifecycle constructs, validates, and operates.

## Google's nine-stage wheel ([[2026-04-22-cheung-ippolito-secchi-google-agents-cli|Cheung, Ippolito, Secchi 2026]])

The article presents an ADLC wheel with nine numbered stages, traced clockwise:

1. *(implicit start: idea / requirement)*
2. **Capability & Tool Exploration** — what does the agent need to do; what tools exist
3. **Design Cognitive Architecture** — agent topology, model selection, orchestration shape
4. **Implement Tools** — actual tool/function code
5. **Context Engineering** — system prompt assembly, retrieval, state shape
6. **Evaluate** — evalsets, trajectory scoring, contract checks
7. **User Acceptance Testing** — human-in-the-loop validation
8. **Deploy Infrastructure** — provision Agent Runtime / Cloud Run / GKE
9. **CI/CD & Production** — release pipeline, secrets, observability

with an inner arrow labelled **"Iterate on approach"** running back from late stages into Design Cognitive Architecture — the wheel is explicitly non-linear.

## Mapping to wiki vocabulary

| ADLC stage | Closest existing wiki concept | Notes |
| ---------- | ----------------------------- | ----- |
| Capability & Tool Exploration | (none yet) | discovery / scoping work; pre-engineering |
| Design Cognitive Architecture | [[ai-agents]] (chatbot → agent → multi-agent progression) | topology choice |
| Implement Tools | [[agent-harness]] — Layer 2/3 plumbing | tool execution + retry + permission middleware |
| Context Engineering | [[agent-harness]] — Context layer (Chatterjee) | system prompt as document, KV-cached stable parts + dynamic |
| Evaluate | [[agent-harness]] — Contracts layer (Chatterjee) | formal evaluable specifications of "done" |
| User Acceptance Testing | (analog: HITL middleware in [[agent-harness]] — Constraints layer) | human checkpoint before production traffic |
| Deploy Infrastructure | (Google Cloud / hyperscaler substrate) | Agent Runtime / Cloud Run / GKE in the Google flavour |
| CI/CD & Production | (standard SRE) | pipeline, secrets, observability |

The lifecycle's **Stages 4–6** are precisely where the harness lives. The ADLC and the harness are not competing constructs — the ADLC is the *process* through which the harness gets built, while the harness is the *artifact* the process produces and operates.

## Open questions

- **Vendor-specificity.** Google's ADLC is the only formalization the wiki has seen so far. Whether it is generic (other vendors converge on similar wheels) or Google-specific (e.g., *Deploy Infrastructure* assumes Cloud Run / GKE / Agent Runtime as the only substrate options) is unresolved on a single source.
- **Pre-stage work.** The Google wheel has an implicit "idea / requirement" pre-stage but no formalization of *deciding to build an agent at all* — i.e., a build-vs-buy or build-vs-compose-vs-buy-outcomes step (cf. [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria's]] firm-boundary framework). Worth tracking whether other lifecycle formalizations include this.
- **Compounding loop.** Chatterjee's Compounding layer (telemetry-as-training-data, harness self-tuning) does not appear as an explicit stage in Google's wheel — it would sit between Stage 9 (CI/CD & Production) and the wheel's "Iterate on approach" return arrow, but is not named separately. Worth watching whether more mature vendor / practitioner formalizations name the compounding loop explicitly.
- **Promote or fold.** If subsequent sources keep reaching for "lifecycle" vocabulary as their primary frame, this page will substantiate. If not, it may eventually fold into [[agent-harness]] as a sub-section.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "agent-development-lifecycle") OR contains(tags, "adlc")
SORT file.name ASC
```
