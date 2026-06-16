---
type: entity
kind: organization
aliases: ["OpenAI"]
tags: [openai, ai-lab, foundation-models, chatgpt, gpt-4, gpt-5, codex, agentic-engineering, sora, custom-gpts, public-benefit-corporation, nonprofit-foundation]
since: 2015
confidence: 0.95
last_confirmed: "2026-06-13"
accessed_at: "2026-06-13"
source_count: 17
relationships:
  - type: published-by
    target: 2025-10-05-patwardhan-et-al-openai-gdpval
    via: "OpenAI research paper introducing the GDPval economically-valuable-task benchmark; public grader at evals.openai.com"
  - type: employs
    target: Aaron-Chatterji
    via: "Chief Economist"
  - type: employs
    target: Gawesha-Weeratunga
    via: "Economic Research team"
  - type: employs
    target: Harrison-Satcher
    via: "Economic Research team"
---

# OpenAI

AI research and deployment company. Originator of **ChatGPT** (Nov 2022) and the **GPT-3 / GPT-4 / GPT-5** series. Self-described in [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|the Bain/OpenAI HBR article]] as "an AI provider to over one million businesses."

## Governance trajectory

Originally founded (2015) as a **nonprofit foundation**. **Two or three "OpenAI crises" ago** ([[2026-05-10-ries-lennys-force-destroys-companies-within|Ries 2026]], 1:12:28), Dario and Daniela Amodei left OpenAI to spin out [[Anthropic]] — the moment Ries dates as his own entry into the AI-governance-advice arc. Mid-2025, OpenAI **converted from the nonprofit-foundation governance to Public Benefit Corporation (PBC) structure** (Ries: *"although now they've converted to a public benefit corp structure"*).

Per Ries' framework, **PBC alone** is structurally weaker than the **PBC + Long-Term Benefit Trust** structure adopted by Anthropic — a PBC replaces the *any-lawful-act-or-purpose* clause with a specific declared purpose (making mission-pursuit a fiduciary obligation of the board) but lacks an *outside trustee body* holding the for-profit board accountable to that mission. The implication Ries does not state outright but the structural comparison implies: OpenAI's *original* nonprofit-foundation guardian was **stronger** than the eventual PBC-only structure; the 2025 conversion is a **governance downgrade** by Ries' criteria.

Ries describes the OpenAI history as *"a really hard case study to learn from because it's such a bizarre story and has involves like mega personalities like Elon and Sam like dueling to the death."* The deeper case-study narrative is deferred to *Incorruptible* (book, out 26 May 2026), not given on-air.

## Models referenced in this wiki

- **GPT-3** — substrate of the customer-support augmentation system in [[2026-04-28-brynjolfsson-li-raymond-generative-ai-at-work|Brynjolfsson, Li & Raymond (2025) QJE]].
- **GPT-3.5 / ChatGPT** — the democratization breakthrough cited by [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] and the trigger for the [[generative-ai|GenAI]] adoption wave.
- **GPT-4** — basis of the [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al. 2026 BCG RCT]] and the [[2026-04-29-boussioux-crowdless-future|Boussioux et al. 2024 crowdless-future study]].
- **GPT-5** — used by [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo's Codex team]] (Feb 2026) to generate the initial repository scaffold via Codex CLI.

## Products and tooling referenced in this wiki

- **Codex** — agent-driven software engineering platform documented in [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]]. Five months of internal use produced ~1M LOC and ~1,500 PRs across an internal product, with **0 lines of manually-written code** and throughput averaging 3.5 PRs / engineer / day across 7 engineers (increasing with team size).
- **Codex CLI** — command-line interface for Codex; used (with GPT-5) to generate the initial repository scaffold for Lopopolo's project. The wiki's first concrete operational reference to Codex CLI tooling.
- **Aardvark** — second agent operating on the same Codex-team codebase, named in passing in [[2026-02-11-lopopolo-codex-harness-engineering|Lopopolo 2026]] as a beneficiary of repository legibility investments. Not detailed.
- **Sora** — text-to-video model + social-network app. Surfaces in [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]] as the parallel demo to Google Flow / Veo for PM-side promo videos, with the **Cameo** feature (custom-instruction-shipped — *"always make me look good"*; reportedly Mark Cuban's cameo auto-injects a Cost Plus Drugs ad). Marily / Claire's tentative read: *"the social-network aspect of it is a distribution method for the underlying API models — power users find what's possible, then commercial applications follow."*
- **Custom GPTs** — user-authored, system-prompt-+-knowledge ChatGPT instances. [[2025-12-01-marily-nika-pms-who-use-ai-will-replace-those-who-dont|Nika 2025]] demonstrates a domain-specific custom GPT ("AI Product GPT") seeded with a PRD template and the author's voice, used as a structured prompt-input-to-prototype-tool pipeline component. Operationally a domain-specific *Context-layer artifact* in [[2026-05-07-chatterjee-anatomy-of-agent-harness|Chatterjee's]] vocabulary.

## OpenAI as an AI-native organization (first-party deployment vantage)

The wiki's **first first-party OpenAI source** — [[2026-06-02-architecting-ai-native-organizations-redesign-work-at-scale-joe-beutler|Beutler 2026]], a talk by **Joe Beutler** (Head of Solutions Engineering, Strategics) at IT Revolution's Enterprise AI Summit — reports how OpenAI is restructuring *itself* and what its solutions team sees succeed across its largest enterprise customers:

- **Internal wins**: the finance team uses the OpenAI API to extract and structure contract data for "millions of dollars of impact," and built a GPT that answered "thousands" of investor due-diligence questions during the recent fundraise. The go-to-market team automated top-of-funnel work (lead qualification, quote preparation) for the SMB self-service segment.
- **The PwC benchmark**: PwC benchmarked OpenAI's finance team at **only 20% of the size it should be** for a firm of its revenue complexity / transaction volume / regulatory burden — "not just against legacy finance orgs … also against comps that are more digitally native."
- **Embedded engineering throughout the company**: per Beutler (and Gene Kim's introduction), the CFO and CRO each have an engineering manager working on AI integration; OpenAI has embedded engineering managers across business functions. The pattern emerged organically (domain expert builds tooling → full-time role → paired with an engineer interviewed by and on the same comp ladder as engineering → head of innovation), and OpenAI frames it as "moving centers of excellence to embedded innovation."
- **Vendor strategy — sell the builder, not the outcome**: Beutler explicitly contrasts OpenAI's approach with "a massive professional services business … lucrative contracts that will last 10 years," betting instead on **no-code agent builders** (continuous evals + governance + connectors + shareable skills) so individuals build their own agents. This is the deliberate counter-position to the outcome-as-a-service thesis in [[2026-06-03-warren-yc-how-to-build-an-ai-native-services-company|Warren / YC]] and the buyer-side *Buy Outcomes* model in [[2026-05-05-nishar-nohria-end-of-one-size-fits-all|Nishar-Nohria]].
- **Ask → Assist → Automate**: the deployment-maturity framework OpenAI's solutions team uses with customers (read-only → human-in-the-loop → full automation). See [[automation-vs-augmentation]] and [[enterprise-ai-adoption]].

Note OpenAI's recurring appearance on the *deployment* side of wiki sources (the Bain/OpenAI [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation|HBR article]]; the [[2026-04-28-anand-wu-genai-playbook|ChatGPT access-democratization]] anchor): Beutler's talk is the first where OpenAI describes its *own* organizational redesign rather than a customer's.

## Research initiatives appearing in this wiki

- **Economic Research team** (led by Chief Economist [[Aaron Chatterji]]). Counterpart to Anthropic's [[Anthropic Economic Index]] initiative. Members in this wiki: [[Gawesha Weeratunga]], [[Harrison Satcher]].
- **GDPval** ([[2025-10-05-patwardhan-et-al-openai-gdpval|Patwardhan et al. 2025]]) — OpenAI's benchmark measuring frontier-model performance on real-world economically valuable tasks (1,320 tasks, 44 occupations, top-9 US-GDP sectors), graded by head-to-head win rate vs human experts. Best model at publication: Claude Opus 4.1 (47.6% wins-or-ties). Public automated grader at evals.openai.com. The capability-measurement counterpart to OpenAI's adoption-focused Economic Research; complements [[2026-04-28-anthropic-economic-index-q4-2025|Anthropic's Economic Index]] (usage) and the [[2026-04-30-ai-index-report-2026|AI Index]] (academic benchmarks).
- **Lowe's partnership** ([[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation]]): launched **Mylow** (online customer-facing) and **Mylow Companion** (in-store associate-facing) AI interfaces in March 2025; Mylow Companion deployed across 1,700+ Lowe's stores.

## Other references

- Supporting partner of the [[AI Index]] (annual report from [[Stanford HAI]]).
- Anchor case in the [[2026-04-28-anand-wu-genai-playbook|Anand-Wu GenAI Playbook]] (ChatGPT as the access-democratization breakthrough).
- Subject of the open-source-AI strategic-analogy example (GPT-4 = Walmart, open source = fruit stand) discussed in [[2026-04-28-carroll-sorensen-strategy-analogy|Carroll & Sørensen 2024]].
- Investment-figure context: U.S. private AI investment $285.9B in 2025 ([[2026-04-30-ai-index-report-2026]]).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "openai")
SORT file.name ASC
```

## Open questions

- The wiki has many references to GPT-4 / ChatGPT / OpenAI as substrate but no first-party OpenAI source has been ingested yet. The OpenAI Economic Research team's writing (this article, plus their independent research papers) is a candidate for a deeper deep-read once a primary OpenAI Economic Research publication is added.
