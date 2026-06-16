# Plan: Did we ingest https://youtu.be/X1NXnLRNIfM?

## Context

User asked whether the wiki has already ingested the YouTube video at https://youtu.be/X1NXnLRNIfM.

## Finding: **Yes, already ingested.**

The video ID `X1NXnLRNIfM` matches exactly the URL recorded on:

- **Wiki source page**: [`wiki/sources/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md`](../../Projects/ai-wiki/wiki/sources/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md)
- **Raw transcript**: [`raw/videos/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md`](../../Projects/ai-wiki/raw/videos/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md)
- **Source frontmatter** `url:` field reads `https://www.youtube.com/watch?v=X1NXnLRNIfM` (verbatim match — same video).

## Source details

- **Title**: *The ERP for the AI Revolution is here*
- **Channel**: [[Y Combinator]] (YC Root Access channel — founder fireside)
- **Interviewer**: Andrew Tan (YC partner, ex-CTO at PagerDuty)
- **Speaker**: John Glasgow — founder/CEO of Campfire (YC S23, AI-native ERP)
- **Published**: 2026-05-20
- **Ingested**: 2026-05-21
- **Length**: ~27:38 minutes; ASR-cleaned, 221 segments
- **Wiki position**: the wiki's first enterprise-B2B vendor-vantage anchor on the **AI-native safety inversion** thesis

## Log entry

The dedicated ingest entry is at [`wiki/log.md`](../../Projects/ai-wiki/wiki/log.md) under `## [2026-05-21] ingest | Glasgow / Campfire CEO on YC Root Access — The ERP for the AI Revolution is here — the wiki's first enterprise-B2B vendor-vantage anchor on the AI-native procurement-room flip`. The source has since been re-cited in three later batch ingests (the 6-video YC batch on 21 May, the Chase/LangChain Interrupt 26 ingest on 21 May, and the 7-video batch on 22 May including Fernando/Man Group and Vitucci/Onshore as paired AI-native-vendor-disrupting-incumbent anchors).

## Recommendation

**No action needed.** The ingest is complete; the source is fully integrated into the existing AI-native-vendor / wedge-to-ERP-transplant / safety-inversion clusters.

If the user wanted any follow-up — e.g., re-process the source with deeper treatment, file an additional typed relationship, refresh `accessed_at`, or extract a specific claim into a synthesis page — they should specify the follow-up; otherwise the answer to the question is *yes, this video is in the wiki under the Glasgow / Campfire ingest*.

## Verification

To re-confirm the answer:

```bash
cd /Users/witoldtenhove/Projects/ai-wiki
grep -rl "X1NXnLRNIfM" wiki/ raw/
# Expected:
#   wiki/sources/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md
#   raw/videos/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md
```

---

## Follow-up: Lessons for building an accountancy app

The user shared they are building an accountancy app and asked what they can learn from "this founder." Two founders in the wiki are highly relevant — Glasgow / Campfire (the video the user just asked about — AI-native ERP with accounting + financial reporting workflows; sells to growing tech companies) and Vitucci / Onshore (the most directly accountancy-domain founder in the wiki — AI corporate tax + accounting; sells to corporate taxpayers competing with Big 4). Together they cover the buyer-side and the supply-side of AI-native accountancy. Fernando / Man Group adds the regulated-finance skills-governance discipline.

### Primary anchor: Vitucci / Onshore — [[2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt]]

**Lesson 1 — Do not sell to accounting firms. Compete with them.** Vitucci spent 2 years (2020–2022) selling AI tooling to top-20 / top-50 firms, reached *"eight customers, mid-six-figures revenue,"* hit a wall. Two structural reasons firms don't internally adopt AI: (a) **value-perception inversion** — they bill hourly so anything that diminishes hours diminishes their pricing power; (b) **asymmetric senior-partner incentives** — partners 3–5 years from retirement won't plow money into something they'll never reap the benefits from. Summer 2022 he **fired all customers and pivoted to direct-to-corporate-taxpayer**. Cold-DM'd 1,000 people on LinkedIn; closed a Miami customer; got into YC on the flight. For your accountancy-app: if your customer is an accountancy firm, you are selling to the least-motivated buyer on the planet. The right customer is the *corporate taxpayer* / SMB / scale-up the firm currently serves.

**Lesson 2 — Pick a single workflow that's the wedge. Don't try to "do accounting."** Vitucci's wedge was *R&D tax credits*. Glasgow's wedge was *approval workflows + multi-entity accounting + audit/controls + revenue-recognition for tech-company SaaS*. *"Tech companies use ~10% of NetSuite — narrowly focus on the slice that triggers the migration."* For an accountancy app: pick **the one workflow** where (a) the customer's pain is acute and quantifiable, (b) the data sits in places the customer can give you access to, (c) you can show *"hey, we can do an R&D tax credit better, faster, more affordably with better traceability"* against a specific incumbent practice. Land that, then expand.

**Lesson 3 — Industry-pick carefully: liability premium + billing-model maturity predict adoption velocity.** Vitucci explains why Harvey / Lora cracked legal but accounting AI hasn't yet: (a) **liability premium** — lawyer mistakes carry jail/large-fine consequences, so the perceived premium-for-human-judgement is durable; accounting mistakes are mostly business-inefficiency. (b) **Industry forward-thinking-ness** — *"Lawyers are forward thinking. That might be the hottest take."* (c) **Project-based billing maturity** — law has been moving to project pricing for a decade; accounting still bills hourly. *"Once you are billing by project, you have price competition and then people have a lot more incentive to reduce their cost."* The implication: if your accountancy app targets a sub-segment that has *already moved off hourly billing* (e.g., fixed-fee R&D credits, fixed-fee bookkeeping, fixed-fee SaaS-recognition), the adoption curve will be faster.

**Lesson 4 — Get senior credibility into the building, especially when you're young.** Vitucci's co-founder *Mark* was his *"boss's boss's boss at Grant Thornton"* — a senior partner near retirement who co-signed the innovation. *"Senior partner Grant Thornton comes over and co-signs this innovation, becomes somewhat more palatable than like junior guy that started doing this — and a wealth of expertise and knowledge."* Vitucci's reflection: *"It's possible we could have gotten it done [without Mark] — Lora is a great example. I think it would have been appreciably more difficult."* For an accountancy app: a former-partner / former-Big-4-director as co-founder, advisor, or first-five-hire is a force-multiplier at the procurement-conversation level. The accountancy buyer's first instinct is *"are you serious people who understand my world?"* — pre-emptively answer that.

**Lesson 5 — Revenue-per-employee is the killer comp; target it explicitly from day one.** Vitucci: Onshore is on track for **$1M+ revenue per employee** ($25M revenue / ~50 people today, targeting $100M / 60–100 by end of 2026). Big 4 / top-20 firms run at **$100–150K revenue per employee** = order-of-magnitude better. *"They will only get worse, especially now that we see instead of investing into technology, we see a lot of these big companies investing into overseas operations."* For an accountancy app: this is the killer enterprise-buyer pitch. CFO asks *"why should I switch?"*; you say *"because your current accountancy provider is doing this on $100K/employee economics, and we are doing it on $1M/employee economics, and that difference is going to grow."* Make the unit-economic comparison your default opening.

**Lesson 6 — The future-shape of the surviving accountancy firm.** Vitucci predicts: industry revenue *up*, headcount roughly *flat*; small senior-partner layer for sales + a regulatory-compliance/expertise layer + some software-engineering — *"I don't think you'll have the very fat bottom layer because I think you'll have AI agents doing it."* For an accountancy app: this is the org shape *your accountancy-firm customer* will look like in 10 years if they survive — design your product so it gives them that shape. If your product reinforces the fat-bottom-of-juniors org structure, you are building for the wrong end of the curve.

### Secondary anchor: Glasgow / Campfire — [[2026-05-20-glasgow-campfire-erp-for-ai-revolution]]

**Lesson 7 — The AI-native safety inversion.** The most distinctive Glasgow contribution: from end-of-2024 onward, the buyer-side procurement narrative on enterprise finance/accounting software *flipped* — *being the incumbent meant you were not AI-native*. Boards and executives now explicitly authorise buying AI-native vendors *"even if the accountant wasn't fully ready to embrace AI — they had this blessing to go buy something new that nobody had heard of and their C-suite or their auditor wasn't familiar with yet."* For an accountancy app: your pitch is no longer to the day-to-day accountant. It is to **the CFO / board / auditor channel** that overrules the day-to-day operator's hesitancy. Your sales material should target the procurement-decision-maker, not the user.

**Lesson 8 — The tech-stack-turnover argument for "why now."** Glasgow: *"Everything in the finance tech stack — payroll, spend management with the Brexes of the world — had all turned over in the last 5–10 years except the core general ledger. A finance person would log into this amazing spend management solution and then the contrast with the ERP was very acute."* For an accountancy app: name the adjacent-tools-already-modern *contrast* explicitly in your pitch. The buyer is *already* using modern tools next to your category; their current pain is the *acuity-of-contrast* between modern adjacent tools and the legacy category you're displacing.

**Lesson 9 — Founder-led sales to $1M ARR, even in the AI era.** Glasgow's strongest counter-claim against agents-everywhere narratives: *"I do really recommend founders to stay in the founder sales mode. Offloading it to AI, offloading it to some AE — feels like, oh let's just bring in a professional whether it's an agent or whether it's a human. But I still recommend being as close to the customer and the prospective customer as possible until you have product market fit. I'm in every Slack channel with every customer... I ended up getting to series A on my own as the one AE."* For an accountancy app: do not outsource sales to AI or AEs in the wedge phase. The *sales-team-driving-engineering* feedback loop is the (un-named) operating logic behind why founder-led sales produces the product velocity that closes the next round.

**Lesson 10 — Velocity as the procurement-side substitute for present feature parity.** A $300M-revenue customer signed Campfire when Campfire had four employees. The CFO's exact concern: *"I'm literally getting fired if you shut down... this contract is longer than your runway."* What closed the gap: peer-customers explicitly told Glasgow *"you guys are building so fast. As we add new global subsidiaries, as we need new features, we feel confident you're going to be able to stay ahead of us."* For an accountancy app: when enterprise buyers ask *"how do I know you'll still be here in 5 years"* (they will), the answer is not roadmap-promises; it is **observable build-pace right now**, ideally with named peer-customers willing to vouch.

### Tertiary anchor (regulated-finance compliance angle): Fernando / Man Group — [[2026-05-21-fernando-man-group-trading-signals-that-trade-themselves]]

**Lesson 11 — Skills governance is what unlocks compliance.** Fernando is head of data + AI at Man Group ($200B AUM, regulated investment firm). 750 of 1,700 employees use Claude Code; 100+ governed skills; production trading signals proposed by AI on real capital. The expense-report failure-mode story is the wiki's clearest empirical worked example of why governance matters: a power user wrote a skill that hardcoded his cost-center; expense approver in sales suddenly got everyone's reports because *"nobody had reviewed that skill — it worked for him, it worked for his team, so it was going to work for everybody. And he wasn't accountable."* Fernando's solve: a **knowledge marketplace** where every skill is visible, tagged, tested with evals, owned by the *workflow owner* (not the *power user who wrote it*), lifecycle-managed. For an accountancy app: bake **skill / workflow governance** into the product as a first-class concern. *"Plan governance before rollout (who owns / reviews / retires / tests — before shipping the first skill, not after the hundredth like us)."* This is what lets your compliance officer / audit team say *yes* to AI on load-bearing accounting workflows.

**Lesson 12 — Organisational context is the moat.** Fernando: *"That is your IP. It's your moat. It's one of the few safe spaces left in AI. The frontier labs are not going to solve context for you. It's not on the internet. They don't know your workflows."* For an accountancy app: the value layer is not the model. It is the **encoded workflows, the data pipelines, the compliance rules, the accounting policies that the customer organisation has built up over decades**. Build a product that **exposes and operationalises that context** rather than trying to replicate it from scratch.

### What the wiki does NOT yet have

These are gaps in the wiki's accountancy-app coverage that future ingests could address:

- A **UK-specific** AI-native accountancy founder (all current sources are US-headquartered — Vitucci/Onshore Chicago, Glasgow/Campfire SF).
- A **SMB / bookkeeping-tier** accountancy AI founder (current sources are mid-market or enterprise — there is no wiki anchor on the QuickBooks-replacement tier).
- An **AI-native sole-practitioner-CPA** founder (the *one-person frontier company* archetype from Tan/CS153 applied to accountancy specifically).
- Quantified data on AI's effects on the *accountancy-firm-customer-side* — most wiki anchors are vendor-CEO self-reports, not buyer-side audited outcomes.

### Companion concept pages worth reading

- [[concepts/ai-employment-effects]] — Chad Jones's *jobs-as-bundles-of-tasks* / *radiologist worked example* framing, applied to professional services.
- [[concepts/enterprise-ai-adoption]] — the *no-code-domain-experts-build-their-own-tools* trajectory at the customer-side.
- [[concepts/agent-harness]] — skills governance + the harness layer.
- [[concepts/durable-skills]] — Schoening's *agency, not skills* framing applied to which accountancy-side roles will compound vs decay.

### Optional follow-up actions the user could approve

1. **Formalise this synthesis as a wiki page** at [`wiki/syntheses/lessons-for-an-ai-native-accountancy-app-founder.md`](../../Projects/ai-wiki/wiki/syntheses/) — links to Vitucci + Glasgow + Fernando, ratchets the new framing onto the wiki for future re-citation. Would require exiting plan mode.
2. **Open a thread page** at [`wiki/threads/`](../../Projects/ai-wiki/wiki/threads/) — for collecting future accountancy-vertical ingests (UK-specific, SMB-tier, sole-practitioner) before synthesising.
3. **No formal artifact** — keep the synthesis as a working note in this plan file only.

These three options diverge enough that I should ask before acting.
