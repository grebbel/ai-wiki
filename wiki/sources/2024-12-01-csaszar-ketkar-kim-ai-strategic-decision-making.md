---
type: source
kind: paper
title: "Artificial Intelligence and Strategic Decision-Making: Evidence from Entrepreneurs and Investors"
author: ["Felipe A. Csaszar", "Harsh Ketkar", "Hyunjin Kim"]
publisher: "INFORMS — Strategy Science 9(4):322–345 (Special Issue on the Theory-Based View)"
url: "https://doi.org/10.1287/stsc.2024.0190"
date_published: 2024-12-01
date_ingested: 2026-06-08
length: "~24 pages (Strategy Science vol. 9 no. 4, pp. 322–345; full article incl. two empirical studies + references)"
raw: "../../raw/papers/Csaszar et al. - 2024 - Artificial Intelligence and Strategic Decision-Making Evidence from Entrepreneurs and Investors.pdf"
tags: [strategy, theory-based-view, strategic-decision-making, large-language-models, ai-augmentation, search-representation-aggregation, competitive-advantage, entrepreneurship, venture-capital, peer-reviewed, csaszar, felin-zenger]
confidence: 0.78
last_confirmed: "2026-06-08"
dynamic_capabilities:
  - digital-sensing/digital-scenario-planning
relationships:
  - type: supports
    target: 2026-04-28-dellacqua-jagged-technological-frontier
    via: "extends the AI-augments-knowledge-work evidence (Dell'Acqua's consulting-task RCT) into strategic decision-making; both find a capability frontier where LLMs match/surpass humans on some tasks"
    confidence: 0.72
  - type: supports
    target: 2026-04-29-boussioux-crowdless-future
    via: "both find LLMs generate and evaluate ideas at human-comparable levels — Boussioux on innovation crowdsourcing, Csaszar on entrepreneurial strategy generation/evaluation"
    confidence: 0.72
  - type: supports
    target: 2026-04-28-carroll-sorensen-strategy-analogy
    via: "shared theory-based-view-of-strategy lens (Felin & Zenger); AI's effect on the causal-theory / analogical reasoning that strategy-as-theory depends on"
    confidence: 0.7
---

# Artificial Intelligence and Strategic Decision-Making: Evidence from Entrepreneurs and Investors

A **peer-reviewed paper** by **Felipe A. Csaszar** (Ross School of Business, University of Michigan), **Harsh Ketkar** (McCombs School of Business, UT Austin), and **Hyunjin Kim** (INSEAD), published in *Strategy Science* 9(4):322–345 (December 2024), in the journal's **Special Issue on the Theory-Based View**. It is the wiki's first **academic-strategy** treatment of how large language models change the *strategic decision-making* (SDM) process — distinct from the wiki's many practitioner/consultancy sources on AI adoption, and the first to engage the [[theory-based-view]] of strategy ([[2026-04-28-carroll-sorensen-strategy-analogy|Felin & Zenger]]) head-on.

The paper's vantage is **strategy-as-discipline**: not "should firms adopt AI" but "what happens to the cognitive machinery of strategy — search, representation, aggregation — when LLMs can generate and evaluate strategies." It supplies the wiki's first **controlled empirical evidence that LLMs perform at a level comparable to entrepreneurs and investors** on realistic, forward-looking strategy tasks.

## TL;DR

- **Three questions**: (1) How might AI-augmented SDM *look*? (2) How *effective* are current LLMs at strategic decisions? (3) What are the *implications* of AI in SDM?
- **Method 1 — vignettes**: AI-augmented reimaginings of classic SDM tools (Porter's Five Forces, Devil's Advocate, etc.) demonstrating the *feasibility* of automating commonly used strategy tools with current LLMs.
- **Method 2 — two empirical studies**: (a) with a **start-up accelerator**, an experiment comparing **LLM-generated business plans** against those of entrepreneurs seeking VC; (b) using a **start-up competition**, comparing **LLM evaluations** of business plans against those of **VC and angel investors**. Finding: **LLMs generate and evaluate entrepreneurial strategies at a level comparable to humans** in realistic, high-uncertainty contexts.
- **Method 3 — cognitive-process framework**: SDM rests on three processes — **search, representation, aggregation** (Csaszar & Steinberger 2022) — and the paper theorises how AI affects each, linking the SDM *outcomes* it changes (generation + evaluation of strategies) to **competitive advantage**.
- **Competitive-advantage futures**: depending on how AI capability progresses, advantage could **stay Ricardian** (rooted in unique resources), **become Schumpeterian** (innovation-driven), or **erode entirely** if everyone can generate comparable strategies cheaply.
- **Theory-Based-View tension**: AI both *supports* and *challenges* the TBV. Challenges — LLMs are next-word predictors, which may limit **forward-looking causal theory** creation (Zellweger & Zenger 2023); they rely on past data, risking **reproduction of conventional strategies** and reduced novelty (Felin & Holweg 2024); their generality may miss firm-specific context. Support — AI could expand the reach of theory-based strategising (e.g. **virtual strategy simulations**).
- **New approaches enabled**: AI can enhance the **speed, quality, and scale** of strategic analysis and enable novel methods like virtual strategy simulations — but *ultimate firm-performance impact depends on competitive dynamics*, not the tool alone (a strategy-theoretic restatement of the wiki's [[micro-productivity-trap]] / paradox-of-access pattern).

## What was actually ingested

Full article (pp. 322–345, ~24 pages incl. both empirical studies, the cognitive-process framework, discussion, and references; converted from the INFORMS PDF via `pdftotext`). Identity verified against the cover/title page — authors, *Strategy Science* vol. 9 no. 4, DOI 10.1287/stsc.2024.0190, CC-BY-NC-ND. **Note on dating**: the wiki uses the journal issue date (December 2024) for the slug/`date_published`; the paper was accepted Sept 2024 and published online in advance Nov 18, 2024.

## Key claims, with detail

### The financial-trading analogy bounds the claim

Algorithmic trading now accounts for **>78% of trading decisions** (SEC 2020) because trading reduces to quantitative, rule-based inputs. SDM is different: it depends on **open-ended, qualitative textual inputs and outputs** (news, user stories, market reports → strategic plans, memos). Computers historically couldn't handle this — until LLMs. The paper's wager is that LLMs cross the threshold that kept SDM "largely inaccessible to AI," for three reasons: LLMs handle strategy's textual data; they match/surpass humans on reasoning-heavy professional exams (medicine, law); and their training corpora encode strategy-relevant knowledge (consumer preferences, competitor info).

### Empirical: LLMs are human-comparable at *generating* and *evaluating* strategy

The two studies are the load-bearing contribution — they move the claim from speculation to evidence in *realistic* strategy environments (actual accelerator applicants; actual VC/angel evaluations), complementing prior LLM-business studies that examined either non-SDM tasks (writing, creativity — [[2026-04-29-boussioux-crowdless-future|Boussioux]], Girotra, Noy & Zhang) or stylised SDM (internal-consulting tasks — [[2026-04-28-dellacqua-jagged-technological-frontier|Dell'Acqua et al.]]; small-business mentoring — Otis et al.). Csaszar et al. push into *forward-looking entrepreneurial strategy* under genuine uncertainty.

### The search / representation / aggregation framework

The paper's general contribution is a framework tying AI use in SDM to firm outcomes via the three cognitive processes it changes:
- **Search** — generating the candidate set of strategies (AI widens or narrows it);
- **Representation** — how the strategic problem is framed/modelled (AI can increase or flatten representational complexity);
- **Aggregation** — combining judgments into a decision (AI changes who/what aggregates).

These map onto the **quality and heterogeneity** of firms' strategies, the **complexity of strategic representations**, the role of **business experiments**, and the **importance of theories** in strategy — the bridge to the TBV.

### Competitive advantage: Ricardian → Schumpeterian → or gone

A sharp, quotable claim for the [[strategy]] page: as AI capability progresses, the *nature* of competitive advantage may change — it "could remain Ricardian (based on unique resources), become Schumpeterian (driven by innovation), or potentially cease to exist altogether." If AI commoditises strategy generation, advantage migrates to **complementary assets** (proprietary data, unique execution) — convergent with the *paradox of access* the wiki holds via [[2026-04-28-anand-wu-genai-playbook|Anand-Wu]] ("because everyone can use it, it becomes harder to capture value with it").

## Dynamic-capabilities reading (Warner & Wäger)

Lightly within the W&W lens: this paper touches **`digital-sensing/digital-scenario-planning`** — AI-augmented SDM is precisely "analyzing scouted signals; interpreting digital future scenarios; formulating digital strategies," and the paper's **virtual strategy simulations** are a direct instance of AI-enabled scenario planning. (Roles inherited: `cso, cdo, strategy-consultant`.) The paper sits mostly *outside* the transformation-process cells — it is a strategy-theory contribution about AI as a decision tool, not an org-transformation case — so it carries a single, defensible tag rather than being stretched across the vocabulary.

## Cross-source positioning

| Source | Construct | What Csaszar et al. adds |
|---|---|---|
| [[2026-04-28-dellacqua-jagged-technological-frontier\|Dell'Acqua et al.]] | Jagged frontier of AI in knowledge work (consulting RCT) | Extends the augmentation evidence into **strategic decision-making** under genuine uncertainty, not stylised consulting tasks. |
| [[2026-04-29-boussioux-crowdless-future\|Boussioux et al.]] | LLMs generate/evaluate ideas vs crowds | Parallel finding in a **strategy** setting: LLM-vs-entrepreneur generation and LLM-vs-investor evaluation. |
| [[2026-04-28-carroll-sorensen-strategy-analogy\|Carroll & Sørensen]] / [[theory-based-view]] | Strategy-as-theory; analogical reasoning | The TBV-special-issue companion: how AI **supports and challenges** the theory-based view (causal-theory creation vs past-data conventionalism). |
| [[automation-vs-augmentation]] | Augment vs automate | SDM as an **augmentation** frontier — AI augments the strategist's search/representation/aggregation rather than replacing the decision. |
| [[micro-productivity-trap]] / [[2026-04-28-anand-wu-genai-playbook\|Anand-Wu paradox of access]] | Task gains ≠ firm value; access erodes advantage | "Ultimate impact on firm performance will depend on competitive dynamics" — the strategy-theoretic version of the same caution. |

## Linked entities and concepts

**Existing pages (touched or referenced):**

- [[theory-based-view]] — heavy: the paper is in the TBV special issue and engages Felin & Zenger directly.
- [[strategy]] — heavy: AI in SDM; the Ricardian/Schumpeterian/erased competitive-advantage futures.
- [[automation-vs-augmentation]] — moderate: AI-augmented SDM as an augmentation frontier.
- [[analogical-reasoning]] — light: search/representation as the cognitive substrate strategy reasoning draws on.
- [[enterprise-ai-adoption]] — light: a strategy-discipline complement to the adoption literature.

**Dangling (single-source mention, deferred per CLAUDE.md author-entity promotion rule):**

- *Felipe A. Csaszar* — lead author (Professor of Strategy, Michigan Ross). Promote on second-source mention.
- *Harsh Ketkar* — co-author (Assistant Professor, UT Austin McCombs).
- *Hyunjin Kim* — co-author (Assistant Professor of Strategy, INSEAD).
- *Felin & Zenger*, *Zellweger*, *Felin & Holweg* — cited theory-based-view scholars (not authors here).

## Source-quality flag

- **Strengths**: peer-reviewed (*Strategy Science*, INFORMS); **two empirical studies in realistic strategy settings** (accelerator + competition) rather than toy tasks; a clean cognitive-process framework; the wiki's first academic-strategy anchor on AI + SDM and first to engage the theory-based view directly. Open-access (CC-BY-NC-ND).
- **Caveats**: studies use 2023–24-vintage LLMs (capability has since advanced — both raising and complicating the findings); "comparable to entrepreneurs and investors" is a level-of-performance claim, not a firm-performance claim (the authors are explicit that firm impact depends on competitive dynamics); generalisability beyond entrepreneurial/VC settings is untested.
- **Per CLAUDE.md §Lifecycle**: baseline 0.70 + 0.05 (peer-reviewed) + dual-study empirical strength → **confidence 0.78**.

## Open questions for the wiki

- **Re-test with frontier models.** The empirical comparisons predate 2025–26 frontier models; a replication would sharpen the "comparable to humans" claim.
- **Does the Ricardian→Schumpeterian→erased trichotomy get a concept-page home?** It is a candidate addition to [[strategy]] / [[theory-based-view]] as AI-era competitive-advantage scenarios.
- **Second Csaszar / Kim source** would promote the authors from dangling to entities and strengthen the wiki's academic-strategy spine.
