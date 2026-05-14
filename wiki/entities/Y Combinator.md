---
type: entity
kind: organization
aliases: ["Y Combinator", "YC"]
tags: [accelerator, venture-capital, silicon-valley, startup-school, ai-native-companies, founder-firesides]
since: 2005
website: "https://www.ycombinator.com"
confidence: 0.85
last_confirmed: "2026-05-14"
source_count: 3
---

# Y Combinator

**Y Combinator** is a Silicon Valley startup accelerator founded in 2005. **President & CEO: Garry Tan** (since 2023). Operates the Startup School educational programme + biannual accelerator batches + Bookface internal social platform.

Promoted to a wiki entity page on 12 May 2026 after appearing as `author:` (channel) on two ingested videos in two consecutive days (Tan 23 April + Hu 24 April). **Bumped to source_count: 3 on 14 May 2026** with the addition of [[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad / Replit on Founder Firesides]], landing one day after Hu and forming a three-day YC-channel cluster on the AI-native-company thesis from three distinct vantages (President / Partner / Portfolio-founder).

## Role in the wiki

YC is the **AI-native-startup-formation vantage** the wiki tracks across three distinct 2026-batch-contemporaneous sources:

### 1. Tan / GStack ([[2026-04-23-tan-yc-how-to-make-claude-code-your-ai-engineering-team-gstack|Tan 2026]])

YC President & CEO Garry Tan publicly shipping **GStack** — an open-source toolkit of skills wrapping Claude Code with named primitives (Office Hours / Adversarial Review / Design Shotgun / Code Review / SLQA / Ship). 3-week build velocity; *"more GitHub stars than Ruby on Rails"* by ingest time. The **Office Hours** skill is *"the distilled version of what is thousands and tens of thousands of hours that the 16 YC partners have spent many many years honing and perfecting"* — a 10% strength version of YC's real partner-mediated adversarial review of startup ideas.

### 2. Hu / Startup School ([[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu 2026]])

YC Partner Diana Hu (published 24 April 2026, the day after Tan) presents the prescriptive framework for AI-native company structure: AI-as-operating-system; closed-loop vs open-loop companies; software factories; the **1,000× engineer** thesis; three archetypes (IC / DRRI / AI founder type) via Jack Dorsey at Block; token-maxing not headcount-maxing.

### 3. Masad / Founder Firesides ([[2026-04-25-masad-replit-ceo-only-two-jobs-left|Masad 2026]])

Replit CEO **Amjad Masad** in conversation with YC's **Andrew Miklas** (published 25 April 2026, the day after Hu). Masad gives the **portfolio-founder-vantage worked example** of the YC-batch thesis: the *company-of-the-future* is built of *builders + salespeople*; Replit's internal **vibe-coding-resident team** (a generalist team with vague mission *"go around the company and make it better"*) is the *closed-loop company* pattern in operation; the **skills-call revolution** at the Replit-platform layer parallels Tan's GStack-style packaging.

### The YC-batch-context anchor triple

The three sources together form a **YC-batch-context anchor triple** spanning 23–25 April 2026:

| Vantage | Source | Contribution |
|---|---|---|
| President / platform-toolkit | Tan / GStack | The packaged-toolkit-ship-at-venture-pace worked example |
| Partner / prescription | Hu / Startup School | The framework — closed-loop companies + software factories + 1,000× engineer |
| Portfolio-founder / platform-vendor | Masad / Founder Firesides | The vendor-CEO worked example — Replit as the floor-raising infrastructure + post-prompting trajectory |

All three align on the same diagnosis: AI-native companies need **fewer humans + queryable artifacts + software factories + a packaged harness of skills**. Same diagnosis from three distinct vantages (President / Partner / Portfolio-founder-CEO).

## People at Y Combinator (referenced across the wiki)

- **Garry Tan** — President & CEO since 2023; engineer (Stanford CS); ex-Palantir #10; Posterous co-founder; built first version of Bookface. **The AI founder type archetype operationalised** at YC-president scale — runs 10-15 parallel Claude Code sessions, ~400 PRs in review. Currently Dangling; promote on second-source mention.
- **Diana Hu** — YC Partner; speaker at YC Startup School on AI-native company construction. Currently Dangling; promote on second-source mention.
- **Andrew Miklas** — YC, interviewer on Founder Firesides (Masad / 2026-04-25). Currently Dangling; promote on second-source mention.

## Operational practices observed across both ingests

- **YC partners as adversarial-review-as-a-service** — Hu's *queryable organization* framing operates on the same partnerships YC has long offered to portfolio companies; Tan's Office Hours skill is *"the 10% strength version of what we do at YC every day."* Both sources reference YC partner sessions as the human-mediated baseline.
- **AI-as-default-tooling-recommendation** — both Tan and Hu prescribe Claude Code (or Codex or Cursor) as the agent-runtime; software factories as the architectural pattern; token-maxing as the resource-allocation discipline.
- **Open-source-toolkit-ship-at-venture-pace** — Tan's GStack ships in 3 weeks to more-stars-than-Ruby-on-Rails. YC's institutional preference for shipping-and-iterating is operationalised at the accelerator-president scale.
- **The accelerator-batch-context as a wiki-relevant temporal anchor** — both sources land in late April 2026, mid-batch for YC's spring cohort. The accelerator's *partner-public-content cadence* now produces wiki-load-bearing sources at scale.

## Notable products / programmes

- **Startup School** — YC's free online programme + content channel; Hu 2026 published there.
- **Bookface** — YC's internal social platform + portfolio knowledge base (Tan built v1).
- **GStack** — open-source Claude Code harness toolkit; Tan's recent project (Dangling first-mention).

## Mentioned in

```dataview
LIST
FROM "wiki/sources"
WHERE contains(file.outlinks, this.file.link) OR contains(tags, "y-combinator") OR contains(tags, "yc") OR contains(tags, "startup-school")
SORT file.name ASC
```

## Open questions

- **YC AI-batch composition** — what fraction of YC's W26 / S26 batch is AI-native by default? First-party YC disclosure would substantiate the *"this is the AI batch"* implicit framing in both Tan and Hu.
- **YC-portfolio adoption of GStack** — Tan ships GStack; how many YC portfolio companies adopt it? First-party data.
- **The 1-billion-startups-in-10-years analog** — Hu's *1,000× engineer* thesis suggests dramatic founder-leverage shifts. Does YC's accelerator throughput change in response?
- **YC-partner-content cadence as a wiki source** — if Tan + Hu are representative of YC's content velocity, the wiki should expect to ingest more YC-partner-public-content sources at rate-of-batch-cycle (every ~3 months).
