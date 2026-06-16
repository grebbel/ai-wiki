---
type: source
kind: video
title: "Why Zepto's Aadit Palicha Turned Down Stanford to Deliver Groceries"
author: ["Y Combinator"]
publisher: "Y Combinator (Startup School India — Jared Friedman interviewing Aadit Palicha / Zepto)"
url: "https://www.youtube.com/watch?v=YKZCU0ynEbs"
date_published: 2026-05-19
date_ingested: 2026-05-21
length: "~28:56 minutes (auto-generated English captions; ASR-cleaned, 888 segments)"
raw: "../../raw/videos/why-zeptos-aadit-palicha-turned-down-stanford-to-deliver-groceries.md"
tags: [zepto, aadit-palicha, kaivalya-vohra, jared-friedman, quick-commerce, dark-stores, 10-minute-delivery, india, mumbai, urban-grocery, supply-chain-ml, in-house-ml-forecasting, search-ads-genai, software-spend-elimination, customer-first-principles, brian-chesky-7-star, y-combinator, customer-story]
dynamic_capabilities:
  - contextual/external-triggers
  - digital-sensing/digital-scouting
  - digital-seizing/rapid-prototyping
  - digital-seizing/strategic-agility
  - digital-transforming/improving-digital-maturity
  - strategic-renewal/business-model
relationships:
  - type: supports
    target: 2026-05-11-hill-vori-grocery-os-paper-and-fax
    via: "Twin **grocery-vertical founder-fireside** ingests in the same week. Vori (US) builds the **store-operating-system layer for independent supermarkets** (POS + payments + electronic shelf labels + three production agents); Zepto (India) builds the **end-to-end dark-store urban grocery platform** that owns the supply chain end-to-end (dark stores + in-house fruits-and-vegetables sourcing + ML supply chain forecasting + industrial robotics). Geographic-and-format-contrast worked examples of the same broad thesis: *legacy grocery is the largest undigitised retail category on the planet, and 2026's AI tooling makes it tractable from two different angles* (tooling-layer / Vori; full-stack / Zepto). The Vori interviewer (Aaron Epstein) and the Zepto interviewer (Jared Friedman) are both YC partners; same accelerator vantage."
  - type: supports
    target: 2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer
    via: "Zepto is a YC portfolio company with deep AI-internal-tooling adoption that matches Hu's CS153 framing — Palicha names *cut SaaS spend to nearly zero* internally, in-house ML supply chain forecasting that replaces days of manual work with no humans in the loop, GenAI-driven search-ads keyword prediction now grossing hundreds-of-millions-ARR. Zepto is the wiki's first **non-US-headquartered YC-portfolio anchor on the same AI-native-internal-operations thesis** Hu prescribes — substantiating the framework's reach beyond the Silicon Valley accelerator-batch context."
  - type: supports
    target: 2026-05-13-jha-emergent-democratizing-app-building-with-claude
    via: "Both founders ratify the 2026 **AI-native-internal-tooling-cuts-headcount-and-SaaS-spend** thesis from opposite vantages. Jha (Emergent) ratifies it from the *platform-vendor enabling SMB-AI-adoption* side ($100M ARR / 8 months / serving 7M users with most never coding); Palicha (Zepto) ratifies it from the *enterprise-scale-operational-business* side — 200,000+ employees, millions of deliveries/day, *'we've cut almost all our software spends to zero'* enabled by an AI-fluent ~650-person tech-and-data org. Same observation — *AI tooling restructures what 'enough engineering' looks like at every operating scale* — observed independently at platform-vendor and operational-customer ends of the spectrum."
---

# Palicha — Why Zepto's Aadit Palicha Turned Down Stanford to Deliver Groceries (Startup School India)

> Aadit Palicha is the co-founder and CEO of Zepto, one of India's largest quick-commerce grocery platforms. What began as a WhatsApp group delivering groceries to neighbors in Mumbai during COVID has grown into a company employing over 200,000 people, processing millions of deliveries per day and operating one of India's largest fruits and vegetables supply chains — all built around a 10-minute delivery model powered by a network of dark stores.
>
> At Startup School India, Aadit sat down with YC's Jared Friedman to talk about the scrappy origins of Zepto, the pivot from a doorstep delivery model to owning their own dark store infrastructure and how the company is now using AI and robotics to drive supply chain efficiency and grow a fast-scaling advertising business.
>
> — channel description, Y Combinator

## TL;DR

A ~28:56 [[Y Combinator]] *Startup School India* fireside (published 2026-05-19). Interviewer **Jared Friedman** (YC managing director); founder **Aadit Palicha**, co-founder and CEO of **Zepto**. Aadit and co-founder **Kaivalya Vohra** ("KB" / "Kavali" in the ASR) started Zepto at 17 during the COVID lockdowns, deliberately turning down Stanford admissions to pursue it. Today: tens of thousands of crores of topline (billions of dollars), customer base in the crores, *largest fruits-and-vegetables seller in India*, 200,000+ employees, ~650-person tech and data team (500 engineers, ~150 data science / analytics / PM / design), hundreds-of-millions ARR in ads revenue.

**The substantive contributions are four:**

**1. The COVID-lockdown-WhatsApp-to-dark-store pivot (~0:17–10:30).** Originally called **Coronicart** during YC. *"We never started with a thought process of building a company; we started from a thought process of just solving a problem for the 30 aunties in our neighborhood."* The first iteration was a WhatsApp group delivering from existing mom-and-pop stores. *"In early 2021... if you're just doing doorstep delivery from a mom-and-pop shop to the customer, you've got no control on the customer experience, no control on the delivery times."* The pivot: KB's apartment as the first mini-warehouse → a cardboard-mini-warehouse in Juhu → a proper warehouse. Volume in the one dark-store neighborhood was 3-4× the rest of the city; that signal drove the name change to Zepto and the 10-minute-delivery vision.

**2. The Brian-Chesky-7-star customer-first-principles framing (~10:30–12:04).** Palicha cites Brian Chesky's *five-star, seven-star* framing as the architectural pattern: *"remove all constraints, remove all the laws of physics, think from first principles, what's the most extreme positive customer experience you can give... start from there and then work backwards from how can I make that possible at scale, that is a better way from starting saying that what is possible for me, that's the best I'm going to give the customer."* Operationalised as 10-minute delivery — *"a crazy idea at the time"* — which then drove higher dark-store throughput and per-unit cost compression nobody forecasted. Closing line of the segment: *"Customer delight is where financial value starts."*

**3. The AI-and-ML internal operations sweep (~22:44–25:35).** Three angles:

- **Supply chain ML (no-humans-in-the-loop forecasting).** *"It used to take a team of people days to manually forecast the entire supply chain. But now we've built out a machine learning algorithm that runs millions of units per day and doing forecasts without any humans in the loop. That's made my supply chain more agile — I'm able to dispatch faster, do more throughput in the same place because my forecast accuracy is so high."* In-house, not vendor.
- **Search-ads GenAI for brands.** Coca-Cola, Pepsi, Nestle bidding on search keywords on the Zepto app. *"We give them a model that helps you accurately predict what keyword is going to give you the best return on ad spend... once brands see that their marketing dollars are getting put to use in the most optimal way, it's been a huge bump in advertising revenue."* Ad revenue: hundreds-of-millions-ARR today, up from *"very small / inconsequential two years ago."*
- **The SaaS-spend-cut-to-zero claim.** *"Internally, we've been able to achieve a lot more with less headcount... we've cut almost all our software spends to zero. We've cut a lot of managed services spends. We've been able to reduce a lot of inefficiencies and manual tasks in the system... if you walk into the Zepto office, there's so many more tools that are automated and there's no outsource tools at all. We're saving literally hundreds, huge amounts of costs on that side."* The most consequential AI-internal-tooling claim in this fireside — Zepto is a ~650-person tech-and-data org reportedly running on AI-native-internal-tooling replacing the typical enterprise SaaS stack.

**4. The industrial-supply-chain-robotics layer.** Palicha names *"industrial-grade automation on the backend supply chain... a decent part of our tech team now works on hardware."* Robotic sortation at the dark-store-replenishment layer; in-house fruits-and-vegetables sourcing from farmers across India (Mahabaleshwar strawberries, Karnataka outskirts). The thesis: *"every rupee of cost you save across the supply chain by becoming more efficient is a rupee you've saved the customer or a rupee that you can invest in better selection, better delivery times."*

**Founder-development line.** Palicha's closing answer on how he kept levelling up at 17–23 years old: *"surround yourself with people that are smarter than you and learn from them shamelessly... we've also looked very stupid a lot internally, but then that's been good because we shamelessly ask questions."* Names his CFO, COO, CTO, head of growth and marketing, chief business officer, and product leader — all senior-tenure professionals who joined early.

**Caveats.** YC channel founder fireside on the YC main channel (not Root Access). Every empirical claim is unaudited and presented through obvious commercial motive (recruiting from Startup School India). The *"cut almost all our software spends to zero"* claim is the most consequential and the most-likely-to-be-rhetorical-exaggeration — Palicha hedges *"a lot of managed services spends"* in the same sentence. Numbers are stated in crores ("tens of thousands of crores of topline") — at the 2026 USD-INR rate, ~$2.4B (10,000 crore = ~$1.2B; the *"tens of thousands"* phrasing suggests $2–5B topline, but Palicha leaves the exact figure intentionally vague).

## Why this matters in the corpus

Zepto is the wiki's first **non-US-headquartered AI-native-internal-operations anchor** at large operating scale (200K+ employees, billions USD topline). The wiki's prior AI-native-company corpus is almost entirely YC-Silicon-Valley-vantage; the Palicha ingest substantiates that the [[2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer|Hu/CS153]] / [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|Hu/YC]] thesis on *AI-native internal tooling cuts SaaS spend and lets a smaller team carry more workload* has reach into a logistics-and-physical-operations operating context, not just digital-first SaaS startups.

Two adjacent observations worth flagging:

- **The "company started in 2020, AI bolted on after" pattern.** Zepto pre-dates the LLM/ChatGPT wave; the supply-chain-ML and search-ads-GenAI layers were added at scale. This is a useful counterpoint to the [[2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up|AI-native-from-day-one]] doctrine — Zepto did not start AI-native, but **the operational substrate (logistics + supply chain) was the AI-receptive surface**, and the company was able to AI-pill its internal tooling and ads layers after-the-fact. The wiki's framing should be careful not to insist on AI-native-from-day-one as the only viable form-factor.
- **The customer-first → financial-value direction.** Palicha's *"customer delight is where financial value starts"* is the wiki's first explicit founder-altitude articulation that runs counter to *"financial-engineering-first growth"* — the canonical Silicon Valley alternative would be *"unit economics first, customer-experience second."* Both are valid in different contexts; Palicha is unambiguous about which one he picks.

## What was actually ingested

The full ~28:56 transcript was read end-to-end with focus on the *Stanford or Startup*, *Pivot to dark stores*, *10-minute delivery vision*, *Hidden supply chain*, *Scale*, *Long-term vision*, and *How Zepto Uses AI* chapters. Earlier sections on founding-history-and-WhatsApp-iteration provide colour and confirm Palicha's *first-principles + obsess over the customer + don't trust the pundits* posture.

The transcript renders **Aadit** as *"Audit"* / *"Adit"* (ASR), **Kaivalya** as *"Kavali"* / *"KB"*, **Coronicart** as *"Coronicart"*, **Bangalore** as *"Bangalore"*, and a few city / supplier names with minor mis-spellings. Numbers in crores are kept as Palicha states them; not converted to USD in the body.

## Linked entities and concepts

**Entities promoted by this source:**

- [[Y Combinator]] — channel; already entity. Bumps source-count.

**Dangling — single-source mention, deferred:**

- **Zepto** — Indian quick-commerce platform; YC alum. First wiki mention; promote on second source.
- **Aadit Palicha** — co-founder and CEO, Zepto; turned down Stanford; 23 years old at filming. First wiki mention.
- **Kaivalya Vohra** ("KB" / "Kavali") — co-founder, Zepto. First wiki mention.
- **Jared Friedman** — YC partner / managing director; interviewer. First wiki mention.
- **Brian Chesky** — Airbnb CEO; cited by Palicha for the *five-star, seven-star* customer-experience framing. First wiki mention (in passing context).
- **Justin Khan** ("Justin Khan") — likely *Justin Kan* (YC partner / Twitch co-founder); cited by Palicha for the *naivety of knowing how to build a company* advantage. First wiki mention.

**Concept pages touched:**

- [[concepts/ai-employment-effects]] — adds the *AI-internal-tooling reduces SaaS spend and outsource-tool spend* anchor at large enterprise operating scale (Zepto's claim of *"cut almost all our software spends to zero"* with ~650-person tech-and-data org operating a 200K-employee field workforce). The mechanism named is **substitution of vendored software by in-house AI-driven automation**, not headcount reduction; this is a useful distinction from the *"AI replaces humans"* default framing.
- [[concepts/enterprise-ai-adoption]] — adds the *AI bolted onto a pre-AI operational substrate* counter-template to the *AI-native-from-day-one* archetype. Zepto's pre-2020 founding does not preclude AI-native internal tooling; the operational substrate (logistics + supply chain) was the AI-receptive surface and the layer most amenable to ML forecasting + GenAI-search-keyword tooling.
- [[concepts/dynamic-capabilities]] / [[concepts/warner-wager-process-model]] — the **Coronicart → Zepto pivot** is a worked example of Warner & Wäger's `digital-seizing/strategic-agility` cell (rapid resource reallocation, pacing strategic responses); the **10-minute-delivery vision** is a worked example of `digital-sensing/digital-scouting` (sensing customer-centric trends).

## Source quality

- **Channel**: [[Y Combinator]] main channel — *Startup School India* sub-series. YC's official channel; higher reach than YC Root Access.
- **Format**: ~28-minute stage-fireside conversation, two cameras, no slides referenced (a few dark-store walkthrough videos shown during the AI section but not captured in the transcript).
- **Empirical anchors**: 200K+ employees, ~650-person tech-and-data team, tens-of-thousands-of-crores topline, hundreds-of-millions ARR ad revenue, millions of deliveries/day. All founder self-reports; Zepto's financial disclosures (public Series filings in India) are the falsifier.
- **Bias / motive**: Founder-marketing in a Startup-School-India context; treat numerical claims as motivated-but-falsifiable.
- **Transcript provenance**: yt-dlp VTT fallback after the youtube-transcript-skill's Playwright path failed to render the engagement panel within 90 seconds — the fourth of four YC-channel videos in this ingest batch to require fallback. Rolling-caption duplicates de-duplicated by the build script's suffix-overlap collapse pass; ASR mis-spellings (Audit / Kavali / Skenctity / Vory) preserved in raw, corrected against the channel description in attribution.
