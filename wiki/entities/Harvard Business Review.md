---
type: entity
kind: org
aliases: ["Harvard Business Review", "HBR"]
tags: [publisher, business-magazine, management-research, harvard, hbr-ideacast, podcast]
parent: "[[Harvard Business School]]"
website: "https://hbr.org"
confidence: 0.90
last_confirmed: "2026-05-11"
source_count: 10
---

# Harvard Business Review

**Harvard Business Review** (HBR) is the management magazine published by Harvard Business Publishing, an affiliate of [[Harvard Business School]]. Founded 1922. Long-form articles aimed at executives and managers, blending academic research with practitioner perspectives.

A primary publishing venue for academic strategy and management work intended to reach C-suite readers.

## Role in the wiki

HBR sources span both the print magazine (with `hbr_reprint` codes) and HBR.org Digital pieces. Print articles are tabulated here; digital pieces are listed separately below.

**Print magazine — Nov–Dec 2025 issue:**

| Article | Authors | Reprint | Topic |
|---|---|---|---|
| [[2026-04-28-anand-wu-genai-playbook\|The Gen AI Playbook for Organizations]] | [[Bharat N. Anand]], [[Andy Wu]] | R2506K | Strategy: where to deploy GenAI today |
| [[2026-04-28-werner-lebrun-octopus-organization\|Become an Octopus Organization]] | [[Jana Werner]], [[Phil Le-Brun]] | R2506C | Change management: org adaptability |

**Print magazine — earlier issues:**

| Article | Authors | Issue | Topic |
|---|---|---|---|
| [[2026-04-28-bansal-birkinshaw-systems-thinking\|Why You Need Systems Thinking Now]] | [[Tima Bansal]], [[Julian Birkinshaw]] | Sept–Oct 2025 | Systems thinking for wicked problems |

**HBR.org Digital pieces:**

| Article | Authors | Date | Topic |
|---|---|---|---|
| [[2026-04-28-webb-strategic-foresight\|Reuniting Strategy and Foresight]] | [[Amy Webb]] | Jan 2024 | Strategic foresight methodology |
| [[2026-04-28-reitz-higgins-spacious-thinking\|The Best Leaders Encourage "Spacious Thinking"]] | [[Megan Reitz]], [[John Higgins]] | July 2025 | Leadership attention modes |
| [[2026-05-02-dutt-chatterji-ai-experimentation-to-transformation\|How to Move from AI Experimentation to AI Transformation]] | [[Arjun Dutt]] et al. ([[Bain & Company]] + [[OpenAI]]) | 30 April 2026 | AI transformation framework + [[micro-productivity-trap]] |
| [[2026-05-05-nishar-nohria-end-of-one-size-fits-all\|The End of One-Size-Fits-All Enterprise Software]] | [[Deep Nishar]], [[Nitin Nohria]] | 23 April 2026 | Firm-boundary 4-model framework (Build / Compose / Collaborate / Buy Outcomes) |
| [[2026-05-07-carucci-resistance-as-data\|Leaders, Treat Resistance to Change as Valuable Data]] | [[Ron Carucci]] | 20 April 2026 | Resistance-as-data framework with four signal categories and three leader traps |

**HBR IdeaCast (podcast / video):**

| Episode | Guest | Host | Date | Topic |
|---|---|---|---|---|
| [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting\|How McKinsey Plans to Survive AI (and Reinvent Consulting)]] | Bob Sternfels (Global Managing Partner, [[McKinsey & Company]]) | Adi Ignatius (HBR editor-in-chief) | 9 Feb 2026 | McKinsey 100-yr reflection + AI strategy: 40k humans + 20k agents workforce, outcome-underwriting, post-controversy governance, hiring overhaul, four durable leadership skills |

HBR articles in the wiki use this convention: source `kind: article`. Print pieces include an `hbr_reprint` field; digital pieces use `journal_volume: "HBR.org Digital, <date>"`. **HBR IdeaCast** episodes use source `kind: video` (since the wiki currently ingests them via the video transcript pipeline) with `author: ["Harvard Business Review"]` per the [video source-page convention](../../CLAUDE.md#source-page-conventions-specific-to-videos).

## Article structure (recurring "Idea in Brief")

HBR articles open with a "Idea in Brief" panel: **The Problem / The Solution / The Payoff** (or variants like Problem / Why It Happens / The Solution). Useful when summarizing — the panel often distills the entire argument in 50–100 words.

## Cross-referenced HBR articles (not yet ingested)

The Anand-Wu article cites two earlier HBR pieces worth tracking:
- *"How Generative AI Can Augment Human Creativity"* (HBR Jul–Aug 2023) — relevant to [[generative-ai]] creative-catalyst quadrant.
- *"How Is Your Team Spending the Time Saved by Gen AI?"* (HBR Mar–Apr 2025) — relevant to [[enterprise-ai-adoption]] productivity-redeployment question.

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "hbr")
SORT file.name ASC
```

## People affiliated with HBR

- **Adi Ignatius** — Editor-in-chief; long-time *IdeaCast* host. First wiki source mention by name in [[2026-02-09-sternfels-mckinsey-survive-ai-and-reinvent-consulting|Sternfels 2026]]. Per the [author-entity-promotion rule](../../CLAUDE.md#author-entity-promotion), do not promote on a single source — listed as Dangling. Promote on second-source mention.

## Open questions

- HBR's editorial process for AI-strategy articles (peer review? practitioner review?). Worth investigating once a third HBR source is ingested.
- Distinguishing HBR's flagship articles from HBR Press books and HBR.org "online" pieces — different rigor levels.
- *IdeaCast* curation: does the podcast surface narratives that contradict HBR's print articles, or is it always-aligned? The wiki has only one IdeaCast source so far.
