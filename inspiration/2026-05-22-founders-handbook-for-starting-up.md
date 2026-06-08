# Founders' Handbook for Starting Up

*An AI-native vertical-vendor app: how to choose your battlefield, find your wedge, build the team, sell to win, scale safely, and play the long game.*

---

## Preface

This handbook is for founders building **AI-native applications in incumbent-dominated verticals** — accounting, law, insurance, healthcare ops, engineering services, real-estate ops, finance — where a slow-moving incumbent professional-services firm or enterprise-software vendor sits between the technology and the end-buyer who actually benefits from your work.

It is not for founders building horizontal developer infrastructure, foundation models, consumer apps, or generic productivity SaaS. The patterns in those categories are different.

The handbook is built around a **12-lesson spine** drawn from three primary anchor founders the wiki has captured in deep detail in 2026:

- **Dominic Vitucci**, founder/CEO of **Onshore** (YC W23) — AI corporate tax and accounting, displacing the Big 4. The most directly accountancy-domain founder in the wiki's corpus. *Started by trying to sell to firms; spent two years failing; pivoted to direct-to-corporate-taxpayer.*
- **John Glasgow**, founder/CEO of **Campfire** (YC S23) — AI-native ERP for tech companies, pulling enterprise customers off NetSuite from Q4 2024 onward. The wiki's first anchor on the **AI-native safety inversion** thesis at procurement-room altitude.
- **Tushara Fernando**, head of data and AI at **Man Group** ($200B AUM regulated investment firm) — runs 750 of 1,700 employees on Claude Code with 100+ governed skills, including AI-proposed production trading signals. The wiki's strongest empirical anchor on **skills governance at enterprise scale**.

Secondary anchors weave across the chapters: **Garry Tan + Diana Hu** (Y Combinator) at the founder-doctrine altitude; **Dalton Caldwell** (Y Combinator) as the pre-AI-substrate-shift YC-partner doctrinal voice on tar pit ideas, pivots, and customer-validation-first; **Harrison Chase** (LangChain) on the vendor-CEO three-layer continual-learning model; **Max Schoening** (Notion) on agency-as-the-durable-AI-era-skill; **Sinclair / Ivers / Benitez** (SEI / Carnegie Mellon University) as the institutional-research-centre voice on *engineering-discipline-endures* under AI volume; **Chad Jones** (Stanford GSB) on the weak-links macroeconomic theory; **Adam Bender** (Google) on socio-technical ecology of developer ecosystems; **Brandon Hill** (Vori), **Will Bodewes** (Phonely), **Ayush Garg** (AnswerThis), **Siddhi Mittal** (Yhangry), **Mukund Jha** (Emergent), **Amjad Masad** (Replit), **Apoorv Agrawal** (Altimeter) for vertical worked examples and counter-points.

**What this handbook does not cover.** Capital-raising mechanics (term sheets, SAFE structuring, dilution calculations, board management). Employment law, immigration, equity-vesting. Founder-conflict resolution and co-founder breakups. Crisis management. The handbook assumes you already have, or can find, the standard playbooks for those topics.

> 📒 **Use-case callout — accountancy app.** Throughout the handbook, callouts like this one render the chapter's general lesson into a concrete *if you are building an AI-native accountancy app, then…* action. Skip them if your vertical is different; the chapter prose remains generic.

## How to use this handbook

**Linear** — read front-to-back for a complete operating doctrine. Roughly 90 minutes at reading pace.

**Reference** — jump to the chapter for your current decision. The 6-part / 14-chapter structure maps to the founder's calendar in roughly the order you face the decisions:

| Part | When you face this |
|---|---|
| **I — Choose Your Battlefield** | Before founding; or in the first 90 days. |
| **II — Find Your Wedge** | First 6 months. |
| **III — Build the Founding Team** | First 12 months; reviewed at every funding round. |
| **IV — Sell to Win** | $0 → $1M ARR. |
| **V — Build for Compliance and Compounding** | $1M → $10M ARR; or earlier if you sell to regulated buyers. |
| **VI — The Long Game** | At every fundraise; whenever the pitch needs sharpening. |

**Go deeper** — every claim in the handbook is backed by at least one wiki source. **Appendix B** maps each cited source to a one-line summary and a direct link.

---

## Part I — Choose Your Battlefield

*Where you compete is the most consequential decision you will make. Most "bad startup ideas" are not bad ideas; they are good ideas pointed at the wrong customer or the wrong industry sub-segment.*

### Chapter 1: The Customer Choice — Don't sell to firms, compete with them

The single most-load-bearing lesson in this handbook is **counter-intuitive**: when an incumbent professional-services firm sits between the technology and the end-buyer, **do not sell the technology to the firm. Compete with the firm by selling the outcome to the firm's customer.**

Vitucci spent **two years** (2020–2022) trying to sell AI tooling to top-20 / top-50 accounting firms. He reached *"eight customers, mid-six-figures revenue,"* and then hit a wall. Two structural reasons:

1. **Value-perception inversion.** *"They bill for hours of expertise, and as soon as the hour becomes a diminished unit of value, you no longer really have a whole lot of ground to stand on when you say 'certainly pay me $1,000, $1,500, $2,000 an hour.'"* Any tool that automates the work *erodes the seller's pricing model*. The firm's incentive is to slow-walk adoption.
2. **Asymmetric senior-partner incentives.** *"You have to then as a senior partner — a guy who maybe has three to five years left in his career — plow a ton of money into something I will never reap the benefits from… some older guys 63, 64 years old say 'I'm going to retire in 24 months, I don't care about this — I'm not going to see the value here in 5, 6, 10, 15 years.' And so quickly the guys who make the decisions, the senior partnerships, say 'well, what if we just don't do that?'"*

The pattern is **structural, not bad-management**. It will not be fixed by Big-4 *AI strategy days* or *$1B AI investment* press releases — Vitucci observed firsthand that those translate into purchasing *$3–4M of Copilot licences* and nothing else: *"What do you guys do with that? Nothing. It's horrible. It doesn't work."*

In summer 2022, Vitucci **fired all of his accounting-firm customers** and rebuilt the software for corporate taxpayers directly. He cold-DMed 1,000 people on LinkedIn. *"Hey my name's Dominic. I can do your R&D tax credit better because I use AI."* He closed a Miami customer; got into YC on the flight back to Chicago.

The buyer-side mirror, from John Glasgow at Campfire: once you pivot to direct, the **AI-native safety inversion** (Chapter 8) becomes your tailwind — boards and CFOs now explicitly authorise buying AI-native vendors over incumbents. The two halves of the lesson reinforce each other.

A parallel doctrine from **Amjad Masad** (Replit) on the same wiki cluster: *"The only two jobs left are builder and salesperson."* If your customer is an incumbent firm and you cannot find a builder-or-salesperson on the other side of the table who actually wants what you sell, you are in the wrong room.

**The upstream YC-partner doctrine.** Vitucci's pivot is not an emergent observation — it is the operational instantiation of a YC-coached prompt **Dalton Caldwell** has been giving founders for years: *"intentionally find where there's a knowable big market with an incumbent, combined with the software is horrible."* Caldwell's canonical worked example is the **Zip / Procurement** pivot (~19:20–22:00 of his April 2024 Lenny's Podcast episode): Caldwell coached Rujul Zaparde at Zip through six pivots before they landed on procurement using exactly this prompt — *"look at what companies are publicly traded and/or owned by private equity that are large and that also are hated by customers."* Zip found procurement; built a billion-dollar business off it. The structural template predates the AI-substrate shift; what the AI-substrate shift adds is the wedge mechanism (Chapter 3) and the procurement-narrative cover that the *AI-native safety inversion* (Chapter 8) provides. Caldwell named the template; Vitucci, Glasgow, Hill, Dinakaran, and the Letter AI founders are the AI-era cohort instantiating it across verticals.

> 📒 **Accountancy-app callout.** If you have been pitching to Big 4 / top-20 firms, stop this week. Identify *the corporate taxpayer or SMB scale-up* the firm currently serves. The first customer you should approach is a 100–500-employee company whose CFO is paying $X00K/year in fees to a firm that is delivering a workflow you can automate. Lead the conversation with that CFO, not with the firm's audit partner. (See Chapter 7 for how to actually run that first sales conversation.)

**Action item.** Make a list of 20 candidate customers. For each, write down (a) what they currently pay the incumbent firm, (b) which named individual signs the cheque, (c) what specific workflow you are replacing. If you cannot answer (a), (b), and (c) for at least 5 of the 20, you have not yet identified your real customer.

**Anti-pattern.** *"We will sell to firms because they have the customer relationships and will be our distribution channel."* Vitucci spent two years on this exact theory. The firm's distribution-channel value is dwarfed by the firm's incentive to slow-walk you. (See Appendix A.)

---

### Chapter 2: The Vertical Choice — Liability premium + billing-model maturity predict velocity

Not every incumbent-dominated vertical is equally tractable. Vitucci offers a clean three-variable diagnostic for *why-Harvey-and-Lora-cracked-legal-but-accounting-is-harder*:

1. **Liability premium.** *"Lawyers' mistakes carry jail / large-fine consequences; accountants' usually only inefficiency consequences."* The perceived premium-for-human-judgement is more durable in high-liability verticals — which sounds like an obstacle for AI adoption but is actually a *tailwind*: when the lawyer customer concludes that AI saves them billable hours without changing their liability exposure, they adopt. When the accounting customer concludes that AI saves them billable hours but also weakens their pricing power, they resist.
2. **Industry forward-thinking-ness.** *"Lawyers are forward thinking. That might be the hottest take."* Cultural openness to new tooling varies enormously by vertical. Construction, accounting, and healthcare ops adopt slowly; legal, finance-tech, and creative services adopt faster.
3. **Project-based billing maturity.** Law has been moving to project pricing for over a decade. Accounting still bills hourly. *"Once you are billing by project, you have price competition and then people have a lot more incentive to reduce their cost."* Sub-segments that have already moved off hourly billing — *fixed-fee R&D credits, fixed-fee bookkeeping, fixed-fee SaaS-revenue-recognition* — adopt AI 5–10× faster than the same vertical's hourly-billed segments.

The theoretical mechanism behind these empirical observations is **Chad Jones's weak-links model** (Stanford GSB, May 2026): jobs are bundles of tasks; AI automates the codified tasks first; the tacit tasks become the new weak links and capture all the rents. *"Geoff Hinton in 2016 said 'We should stop training radiologists.' We have more radiologists in 2026 than in 2016, and they're paid more."* The same mechanism applies at the *vertical* level: AI does not eliminate the vertical; it eliminates the *junior-time-billed tasks* in the vertical and re-concentrates value at the tasks AI cannot do.

**The diagnostic, applied:** rank your candidate verticals on the three axes above. Pick the **highest-fit sub-segment** — usually a project-billed niche inside an otherwise hourly-billed vertical, where the buyer already accepts that price competition is normal. This is where adoption velocity will reward you for being first.

> 📒 **Accountancy-app callout.** Within accounting, the highest-velocity sub-segments in 2026 are: **R&D tax credits** (project-billed, fixed-fee, niche-expert-driven — Vitucci's wedge), **fixed-fee bookkeeping for tech companies** (Glasgow's adjacent terrain), **SaaS revenue recognition** (technically complex, audit-relevant, increasingly project-billed), **transfer pricing** (high-liability, increasingly project-billed). The lowest-velocity sub-segments: general audit (still hourly, high-liability, partnership-economics), forensic accounting (hourly, expert-witness-dependent), tax for high-net-worth individuals (relationship-driven). Start where the velocity is.

**Action item.** For each candidate vertical, score 0–3 on each of the three axes. Total possible 9; ignore anything that scores ≤4. For your shortlist, talk to 5 buyers in each before committing.

**Sidebar — Beware tar-pit verticals.** The vertical-choice diagnostic above tells you what to *pick*. Caldwell's **tar-pit-ideas** primitive tells you what to *avoid* — and the avoid case is harder to recognise because tar pits, by construction, present as good ideas. *"By definition it is only a tar pit if it seems like it's not. The weird aspect of what we call a tar pit idea is an idea that a lot of people come up with and that it seems like an unsolved problem and you get lots of positive feedback for. And you have a really good set of arguments that it's a really good startup idea — and that's different than a bad startup idea. Part of being a true tar pit is that you can get good initial validation."* The canonical consumer-tar-pit example is *friend-coordination apps* (*"people have been starting that startup since the '90s"*). The B2B parallels at the vertical-choice layer: **"sell to firms"** (Vitucci's two-year tar pit; Chapter 1) and **"we'll be the AI-native CRM / ERP / [category]"** (the category-is-the-wedge anti-pattern from Chapter 3 — verticals masquerading as wedges). Tar pits don't fail the obvious tests; they fail the retention test. If your candidate vertical produces enthusiastic initial buyer reactions but you cannot point to a second-month-retention signal from at least 3 of your 5 buyer conversations, treat the validation as positive-but-insufficient and re-run the three-axis diagnostic before committing.

**Anti-pattern.** *"Big market = good market."* Total addressable market is the wrong primary filter at vertical-choice stage; *adoption velocity* is the right primary filter. A $10B market that adopts in 24 months beats a $200B market that adopts in 8 years.

---

## Part II — Find Your Wedge

*Once you know where you compete, the next question is what you build first. The answer is almost never the full product. The answer is the single workflow that triggers the customer's migration.*

### Chapter 3: The Workflow Choice — Pick one workflow as the wedge

The classical incumbent-defence in enterprise software is *"you can't disrupt this category until you're feature-complete."* Both Glasgow (Campfire) and Vitucci (Onshore) refute this empirically. The right wedge is **the single workflow that gives the buyer permission to switch.**

Glasgow's framing (~5:41 in the Campfire fireside):

> *"Within our initial market of tech companies, they're actually not using a lot of NetSuite — most of NetSuite they're actually not using. So we very narrowly focused on a certain segment which was like tech companies that had outgrown QuickBooks, that needed something more powerful or more mature for certain specific features… approval workflows doesn't sound sexy at all but it's a key reason that folks need it for audit and QuickBooks doesn't have that. Multi-entity accounting where you have a subsidiary — particularly in the AI-native world folks are going multi-entity very quickly… we narrowly focus on those few features and then folks are saying we actually don't have a lot but within nine months we were moving people off of NetSuite because we actually narrowly focused on being the best for a very specific profile of the customer base."*

The supporting claim — *"tech companies use ~10% of NetSuite"* — collapses the feature-completeness defence to the size of the actually-used slice.

Worked examples of single-workflow wedges across the wiki:

- **Vitucci / Onshore**: R&D tax credits.
- **Glasgow / Campfire**: approval workflows + multi-entity accounting + audit/controls + revenue-recognition.
- **Hill / Vori**: inventory-reorder mobile app for independent supermarkets ("a couple of weeks" to build; one store door-knocked into during YC; hundreds of stores in year one).
- **Bodewes / Phonely**: voice AI receptionist for small business → enterprise call-center optimization.

Diana Hu (Y Combinator, Stanford CS153) names the general pattern as the **forward-deployed-engineer wedge**: *"Pick a painful workflow, go inside deep into the customers, and you basically become the forward-deploy engineer."* The recipe: *"The founders of Salient or Happy Robot did not come from a finance background or logistics — not in the training set. The way they became experts is they actually shadowed or took a job and learned the depths of everything that had to be done with it."*

**The three properties of a good wedge:**

1. The customer's **pain is acute and quantifiable**. *"How many hours per month do you spend on this?"* should produce a number the customer can name in 5 seconds. If they hesitate, the pain is not acute enough.
2. The **data sits in places the customer can give you access to**. If the data lives only in the firm's heads, or in a system the customer cannot release, the wedge is dead on arrival.
3. You can show *"we can do this better, faster, more affordably, with better traceability"* against a **named incumbent practice**. The comparison should be specific and demonstrable in a 30-minute demo.

**The upstream wedge-discovery method.** The three properties tell you *what makes a wedge good*; **Dalton Caldwell** (YC) names the *how-to-find-it* method, the same one he has been giving founders since well before the AI-substrate shift: *"My tactical advice is start doing customer validation first versus building a PowerPoint deck versus trying to raise money. If you find people that are really excited and you do line up customers, that is a great green light that it is time to do a startup. Build it once you have some conviction that you're like — oh, I think I would have a customer. At least one."* The handbook's 2026 founder-anchors (Vitucci's 1,000 cold DMs; Dinakaran's LinkedIn-contact-scraping + warm-intro discipline) are the post-AI-wave operational instantiations of Caldwell's customer-validation-first prescription. The substrate changed; the method did not.

> 📒 **Accountancy-app callout.** Candidate wedges that pass the three-property test for accountancy: **R&D tax credits** (acute pain — every CFO knows the time spent; data in get/Jira/payroll; clear incumbent comparison). **Sales-tax nexus and filings** for multi-state SaaS (acute pain; data in Stripe + ERP; clear incumbent comparison). **Revenue recognition for usage-based-billing SaaS** (acute pain; data in invoicing system; ASC-606-compliance incumbent comparison). Less obviously wedge-worthy: *"a better Xero"* (no specific acute pain). *"AI-powered audit"* (data not releasable in early sales motion; incumbent comparison opaque).

**Action item.** Write down your candidate wedge on one line. Then write down (a) the named workflow, (b) the customer-quantifiable pain, (c) the data-access path, (d) the incumbent practice you are replacing. If you cannot write the four lines in 5 minutes, your wedge is too vague.

**Anti-pattern.** *"We will be the AI-native [X]"* — where [X] is the category name. The category name is too big to be a wedge. *"We will be the AI-native ERP"* is a wedge if and only if you can name the specific *first* feature that triggers the migration (Glasgow: approval workflows).

---

### Chapter 4: The Build-Order Choice — From wedge to platform without losing focus

Once your wedge is landed, the next question is *what do you build second?* The wiki carries two empirical answers, both anchored to **compound startup** founders who built hardware + software + services stacks over 3–5 years.

**Glasgow's expansion arc** (Campfire): approval workflows → multi-entity accounting → audit/controls → revenue-recognition → eventually the full general ledger. The order is determined by *which adjacent workflow the existing customer pulls you into*. *"Sales-team-driving-engineering"* (Chapter 7) is how this discipline stays anchored to real demand.

**Hill's expansion arc** (Vori): mobile inventory-reorder app → POS → payment processing → electronic shelf labels → three production agents (inventory / pricing / personalized-offers) → full store operating system. The lever: a Michael Seibel prompt early at YC — *"Where in the grocery store is your customer spending the most money on technology? On the point of sale, on payment processing, on the store operating system. So build that."* The order is determined by *the size of the budget you are displacing*.

**Vitucci's expansion arc** (Onshore): R&D tax credits → corporate accounting → audit. The order is determined by *the customer-trust ladder* — each subsequent service is one that the customer would not have trusted you for at the start but does now.

The three orders look different, but they share a **single discipline**: **the customer tells you what to build next, not your roadmap document.** Your job is to (a) keep founder-led sales going (Chapter 7) so you actually hear the request, (b) build fast enough that the customer believes you can ship before they need it (Chapter 10), and (c) refuse to build things the customer has not asked for, even when they sound strategically obvious.

There is a productive tension in the wiki on this point. **Garry Tan** at Stanford CS153 (May 2026) explicitly inverts the legacy *"don't boil the ocean"* business advice: *"My response to that, based on my experience with coding agents, is actually let's boil the ocean. You can do the work of about 500 to 1,000 people. And if that's true, then all of the expectations that we currently have in society around what a founder can do, what a company can do, what a small team can do — they're actually a thousandx wrong."*

Vitucci asserts the opposite at the go-to-market layer: *"The idea of trying to boil the ocean all at once is very challenging. It has been an incredible benefit for our business to be great at one thing really early."*

Both are correct at different operating altitudes. Tan describes what *one founder-engineer with current tooling can build*; Vitucci describes what *one CFO will buy from a startup they have not heard of before*. **Engineering capacity can boil the ocean; procurement trust cannot.** Build like Tan; sell like Vitucci.

> 📒 **Accountancy-app callout.** A typical expansion arc for an accountancy app: Year 1 — wedge (e.g., R&D tax credits) plus the **minimum surrounding workflows the buyer cannot do without** (data ingestion from get / Jira / payroll; output format the buyer's existing audit firm will accept; an audit-trail document). Year 2 — adjacent compliance workflow that uses the same data ingestion (e.g., state R&D credit equivalents; jobs-tax credits; cost-segregation). Year 3 — the corporate-tax adjacency that uses the same audit-trail discipline. The order is *which adjacency uses the same data pipeline you have already built*.

**Action item.** Maintain a list of *adjacent workflows your customers have asked for in the past 60 days*. Sort by frequency-of-ask. The top item is your next build, regardless of what the roadmap document says.

**Anti-pattern.** *"We are building the operating system for [X]."* This framing is a roadmap retrofit, not a build-order. The operating-system framing belongs in the pitch deck after year 3, not in the year-1 backlog.

---

## Part III — Build the Founding Team

*Who you start with determines what conversations you can credibly have, and therefore which doors open. In incumbent-dominated verticals, credibility is currency.*

### Chapter 5: The Credibility Question — Senior co-founder as procurement-force-multiplier

Vitucci's most strategically-loaded decision was hiring his former boss-of-his-boss-of-his-boss at Grant Thornton — **Mark**, a senior partner near retirement — as co-founder. *"Senior partner Grant Thornton comes over and co-signs this innovation, becomes somewhat more palatable than like a junior guy that started doing this — and a wealth of expertise and knowledge."*

Vitucci's later reflection on whether Mark was load-bearing: *"It's possible we could have gotten it done [without Mark] — Lora is a great example. I think it would have been appreciably more difficult."* The honest answer is *we cannot run the counterfactual, but every accountancy buyer's first instinct is 'are you serious people who understand my world,' and Mark answered that question pre-emptively.*

The wiki carries an interesting variant of the same lesson: **Ayush Garg** at AnswerThis (YC, Spring 2026) achieved the same effect at micro-scale with a *non-technical co-founder* (Ryan) providing **workflow-ownership credibility** rather than industry-prestige credibility. Ryan was the daily user; he wrote the agent's `instructions.md` updates by messaging the Slack channel in natural language; the agent edited its own rules in response. The credibility Ryan provided was *"this product is used by a real workflow-owner on day one, not just a founder demo."*

A third variant from **John Glasgow** (Campfire): Glasgow's YC interviewer was **Andrew Tan** (YC partner, ex-CTO at PagerDuty). The credibility lineage shows up at the cap table — *"a four-employee seed-stage vendor pulling >100 customers off NetSuite from Q4 2024 onward"* required something more than a clever pitch deck. Investor-side credibility is real and observable to procurement buyers who do reference checks.

**The three credibility variants:**

| Variant | Provider | Best when… |
|---|---|---|
| **Industry-prestige** | Former senior partner / Big-4 director / industry-association president | Selling to procurement-cautious enterprise buyers in regulated verticals |
| **Workflow-ownership** | Daily user of the workflow / former practitioner at the level of the buyer's team | Selling to SMB or mid-market where the buyer wants peer-credibility, not authority-credibility |
| **Investor-side** | Top-tier accelerator / lead investor with vertical reputation | Selling to enterprise buyers who do investor reference checks |

You do not need all three. Most successful founders in this wiki have one strong source of credibility plus an absence of obvious red flags on the other two.

> 📒 **Accountancy-app callout.** The single highest-leverage hire for an accountancy app in 2026 is a **recently-retired Big-4 / top-20 partner** who is bored, professionally restless, financially independent, and willing to take a senior-advisor role for equity. They open procurement doors that no amount of cold outreach will. If you cannot find that person in your network, second-best is a **former Director of Tax / Director of Finance at a 500–5,000-employee company in your target customer segment** — they are the buyer's peer, which is procurement-credible for the *workflow-ownership* variant.

**Action item.** Make a list of 10 candidate senior advisors / co-founders. For each, write down (a) which credibility variant they would provide, (b) what specific procurement door they would open, (c) what equity / advisory-shares package would secure them. Have the conversation with the top 3 within the next 30 days.

**Anti-pattern.** *"We are two technical co-founders and we will figure out the industry as we go."* This works in some categories but is extremely hard in regulated incumbent-dominated verticals. The wiki has zero successful accountancy / law / healthcare AI startups led by two technical co-founders with no industry credibility hire.

---

### Chapter 6: The Roles You Need from Day One

Diana Hu (Y Combinator, Stanford CS153 lecture, May 2026) articulates a **three-role org structure** for AI-native companies that compresses what was previously 8–12 roles into 3:

1. **IC (Individual Contributor)** — *everyone* ships. Including non-technical staff. The salesperson builds their own pipeline-automation. The customer-success rep builds their own onboarding-flow. *"Everyone in an org is involved in improving the agent with feedback."*
2. **DRI (Direct Responsible Individual)** — Apple's *Direct Responsible Individual* convention, applied at the outcome level. *"Tends to oftentimes be the founder."* The DRI orchestrates ICs around a specific business outcome (e.g., *"we need to increase the revenue by 3× by the end of the week"*).
3. **AI founder type** — operates *at the edge of the tools*. Hu names Garry Tan as the embodiment: *"If you hear Gary, he really embodies this — you're living at the edge of the future with all the tools in order to get your company to run fast."* The AI founder type is who tries the new tooling first, brings it into the company, and rewrites the team's working norms as new tooling arrives.

In a sub-10-person AI-native startup, **all three roles can sit on the founder team**. Two co-founders cover IC + DRI; one of the two is also the AI founder type. The crucial property is that **none of the roles can be the "manager who does not ship."**

Max Schoening (Notion, May 2026) provides the practitioner-altitude lens: **agency, not skills, separates the people who thrive from the people who fall behind.**

> *"Even if you have the skills at your fingertips because now an AGI-adjacent model helps you, the thing that matters is agency. People who have true agency and understand that the world around them is malleable will do great. The folks who stick to 'what does it mean to be a PM, what does it mean to be a designer, what's my job as an engineer' — that will be much harder."*

Two Notion vignettes Schoening offers as worked examples:

- **Brian Leven** — a Notion designer who *"blurs engineering and design, but he also is probably our number one recruiter."* Agency vignette: contributing to org outcomes *outside* the day-to-day role.
- **Eric Lou** — a Notion PM who asked Schoening *"if you started a startup would you hire me?"*, was told *"not in the first 10 — I don't need a product manager,"* and replied *"oh, okay — I'm going to work on the skills so that you would hire me in the first five."* He progressively shifted from PRDs to Figma to *"why do I have to do the Figma thing — can't I just build the prototype and at least show you what I think?"* The narrative arc of **PM evolving into builder via agency**.

The negative case: **Siddhi Mittal** at Yhangry (May 2026) on what *firing* looks like when an existing team member does not have agency: *"I fired my tech lead because I realized he did not know what skills was, and he was the ceiling in our company. And I re-hired our new head of engineering all within a week. In March, we are really all in. I probably need to kill my human empathy a little bit more, a little bit faster."*

Hire for **agency over credentials, and tool-fluency over job-title-fit.** A senior engineer who insists on writing every line by hand is a worse hire in 2026 than a junior who has shipped three side projects with Claude Code in the past month.

> 📒 **Accountancy-app callout.** Your founder team in months 1–12 should be: (a) a founder who *does the IC accounting work daily* — actually opens the customer's books, runs the workflow, files the form; (b) a founder who is the *AI founder type* — runs every model release, writes the skills, rewrites the team's working norms as Claude Code / Codex / Cursor evolves; (c) a *senior advisor* (Chapter 5) who opens doors. Your first three hires after the founders are *more ICs who can do (a)* — preferably former-firm-associates who left the firm because they wanted to ship.

**Action item.** Score your current team on the three roles. If any of the three is absent or weak, that is your most urgent hire. If you have a "manager who does not ship," you have a problem.

**Anti-pattern.** *"We will hire a Head of Sales / Head of Marketing / Head of People before we hit $1M ARR."* Glasgow explicitly counsels against this in Chapter 7. Hire ICs and DRIs; the heads-of-function come after product-market-fit.

---

## Part IV — Sell to Win

*The four chapters in this part are the most operationally-dense in the handbook because the $0 → $1M ARR motion is where founders most often fail.*

### Chapter 7: Founder-led Sales to $1M ARR

The strongest counter-claim against the most-aggressive *agents-everywhere* narratives in the wiki comes from Glasgow (~14:05 in the Campfire fireside):

> *"Even in the AI era, I do really recommend founders to stay in the founder sales mode. I think offloading it to AI, offloading it to some AE — I think it feels like, oh let's just bring in a professional whether it's an agent or whether it's a human. But I still recommend being as close to the customer and the prospective customer as possible until you have product market fit. I'm in every Slack channel with every customer. I'm trying to listen to as many sales meetings as I can to really hear, because then you're the best person in the company to actually impact change on what is happening — the sales team driving engineering. I ended up getting to series A — the kind of classic million in ARR for us — on my own as the one AE."*

Two things to internalise:

1. **Do not outsource sales to an AI or an AE before $1M ARR.** The output of sales is not just revenue; it is the **feedback loop that drives engineering**. If the founder is not in every sales call and every customer Slack channel, that feedback loop breaks.
2. **The sales motion is itself a discovery process.** Vitucci's first 1,000 cold DMs taught him which talking points worked, which buyer titles converted, which competitors mattered. He did not pay an AE to make those discoveries on his behalf.

**The YC-partner doctrinal anchor.** Both points above are downstream of a discipline **Dalton Caldwell** has been coaching at YC for years. Caldwell's tactical-advice closing on Lenny's Podcast (April 2024): *"Start doing customer validation first versus building a PowerPoint deck versus trying to raise money. If you find people that are really excited and you do line up customers, that is a great green light."* And on the cold-DM-to-real-customer template: *"Get permission to talk to potential customers and try to pre-sell something before you write code."* Glasgow, Vitucci, and Mittal are not three independent founders converging on the same conclusion in 2026; they are three founders applying a YC-partner-coached doctrine that predates the AI substrate by years. The doctrine is older than this handbook's source corpus; the AI substrate just sharpened its consequences.

Mittal's *founder-brand-as-distribution* variant (Yhangry, May 2026) is worth knowing as an adjacent pattern. Mittal turned *teaching AI agents in plain English* into a sales channel: she pitched *"instead of pitching Yhangry, I'm going to teach everyone how to build AI agents in 30 minutes,"* got **$50K worth of conference slots for free**, and embedded the Yhangry AI product demo inside the teaching deck. *"It's like win, win, win, win, win."* This is founder-led sales executed as **content-as-product-distribution**, not direct-cold-outreach.

The discipline both variants share: **the founder is the sales channel.** Whether the channel takes the form of cold DMs (Vitucci), in-every-Slack-channel (Glasgow), or teaching-as-pitching (Mittal), it is the founder running it.

The third wiki anchor: **Garry Tan's office-hours skill** — Tan codified the YC-partner office-hours sales-and-product-feedback session as a Claude Code skill that delivers *"the 10% strength version of what we do at YC every day."* The skill is open-source. Run it on your own pitch and your own demo, weekly, with Claude or Codex playing the role of the YC partner.

> 📒 **Accountancy-app callout.** Concrete first 30 days of founder-led sales for an accountancy app: (1) Compile a list of 200 CFOs / heads-of-tax at companies in your target segment. (2) Cold-DM 20/day on LinkedIn for the first two weeks with the specific *"I can do your [wedge workflow] better, faster, more affordably with better traceability — 30 minutes, here's a calendar link"* message. (3) Take every meeting yourself; do not delegate. (4) For every meeting, record (with consent), transcribe with Claude, extract the three things the buyer said that did not match your pitch deck, and update the pitch deck within 48 hours. (5) Do this until you have closed three paying customers (mid-five-figures each is fine) or done 100 calls — whichever comes first. The 100-call benchmark is Vitucci's own discipline.

**Action item.** Block 4 hours every weekday for sales calls until $1M ARR. Anything that competes for that block — including engineering meetings, hiring, fundraising — yields. This is the single highest-leverage time-allocation discipline a founder can practise in this phase.

**Anti-pattern.** *"We hired a Head of Sales in month 6."* The handbook's strongest red flag. If you cannot answer *"why is the founder still selling at $500K ARR?"* with *"because that is how we hear the customer,"* you do not yet have product-market fit.

**Anti-pattern (companion).** *"We're applying [Lenny's / a16z's / SaaStr's] late-stage growth playbook at seed."* Caldwell's sharpest *contrarian-corner* claim, made *on Lenny's own channel*: *"Growth and growth hacking and doing all this analytics AB testing stuff is a total waste of time for very early startups. A lot of the advice was catered towards later-stage companies… you see this inclination away from getting a first customer, getting one customer and talking to that person, and instead they have like all this really complex growth-hacking theory."* The cross-channel meta-comment — Caldwell criticising premature application of Lenny's own content *on Lenny's own podcast* — is a small but pointed *information-diet* worked example: even the highest-quality late-stage operating advice is harmful at seed when it displaces customer conversations. The pre-PMF founder's reading list should be 90% customer-discovery / sales / wedge-validation and 10% everything else, not the inverse.

---

### Chapter 8: The AI-Native Safety Inversion

The most distinctive contribution John Glasgow brings to the wiki is the **AI-native safety inversion** thesis (~24:08–24:31 of the Campfire fireside):

> *"Buying the legacy version was considered very safe. But then once AI started to take off — call it in the finance category, call it like a year and a half ago, call it, you know, end of '24 — it then become being the incumbent meant you were not AI-native. And so there was a flipping of the narrative that the board and the executives were saying, we want AI-native. And even if the accountant wasn't fully ready to embrace AI, they had this blessing to go buy something new that nobody had heard of and their C-suite or their auditor wasn't familiar with yet."*

Three details that make this load-bearing:

1. **It is a narrative flip, not a feature flip.** Glasgow's product had AI features for years; what changed at end of 2024 was *what the board would underwrite as a safe choice*. The shift is on the procurement-decision-maker's side, not on the product side.
2. **The shift moves through the C-suite / board / auditor channel, not the day-to-day operator channel.** *"Even if the accountant wasn't fully ready to embrace AI, they had this blessing"* — the day-to-day operator's hesitancy is overruled by the procurement-level decision-maker, not converted.
3. **The narrative had to shift even though the core product didn't.** *"Your narrative needs to continue to shift even if the core product ultimately, you know, ends up not shifting."*

**The implication for your sales motion:** the buyer is no longer the day-to-day operator. The buyer is the **CFO / board / auditor** who provides the *air cover* for the operator to use your tool. Your sales material, your pitch deck, your case studies, and your reference-customer calls should all be designed for that procurement-level audience.

The SMB-vantage parallel: **Mukund Jha** at Emergent (May 2026) reports $100M ARR in 8 months, 7M users in 190 countries, *"70–80% have never written a line of code."* The same procurement-narrative flip — *being AI-native is no longer the disadvantage it was; being legacy is now the disadvantage* — operating at the long-tail SMB / non-coder end of the spectrum.

A complementary observation from Diana Hu (Stanford CS153): *"There are people who are still operating like co-pilot level from last year, and it's like — not going to make it, bro. They're not going to make it."* Hu's framing is about *engineering teams* not embracing agentic-coding; the parallel buyer-side observation is that *companies* still buying legacy software *because it's safe* are starting to look risky to their own boards.

> 📒 **Accountancy-app callout.** Re-write your sales deck for the CFO / audit-committee audience. The day-to-day accountant who actually uses your tool is your *user* but not your *buyer*. The pitch slides that work in 2026: (1) the *adjacent-categories-already-modernised* contrast (Chapter 9); (2) the *revenue-per-employee* unit-economic comparison (Chapter 13); (3) the *board-asked-us-to-find-AI-native-options* permission-giving framing — confirm with the CFO that this is the directive they have received, then position your product as the answer; (4) auditor-friendly artefacts: SOC 2 Type II, evidence of data residency, named human-in-the-loop on every consequential output.

**Action item.** Audit your existing sales deck against the CFO / audit-committee audience. If more than 30% of the slides speak to the day-to-day user rather than the procurement-decision-maker, rewrite.

**Anti-pattern.** *"Our product is so good the user will champion it from below."* Bottom-up motion works in horizontal SaaS (Slack, Figma, Notion); it does not work in regulated incumbent-dominated verticals where procurement is a board-level decision.

---

### Chapter 9: The Tech-Stack-Turnover Pitch — Name the *acuity-of-contrast*

When investors at seed asked Glasgow *"why now? This is a very established market, mission-critical software,"* his answer was operational rather than macro (~22:44–23:18 of the Campfire fireside):

> *"Everything in the finance tech stack — like payroll, spend management with the Brexes of the world — had all turned over in the last 5 to 10 years except the core general ledger. And so there was, you know, a finance person would log in and they would go into this amazing spend management solution or accounts payable or payroll, and then the contrast with the ERP and everything else was very acute."*

**The mechanism:** every adjacent tool in the customer's daily workflow has already received its modern-SaaS rewrite; your category is the last domino. Finance teams *experiencing the contrast daily* are the ones reaching out, not the ones being sold to.

This is the wiki's strongest *why-now* diagnostic. Apply it to your own category by asking:

1. Which **adjacent tools** does your customer use daily, immediately before or after your category?
2. Which of those adjacent tools have been **rewritten in the past 5–10 years**?
3. What does the *acuity-of-contrast* look like in your customer's daily UX — the moment they log out of the modern tool and into your category?

If you can answer those three questions with specific named tools and a specific *moment-of-contrast*, you have a *why-now* pitch that is concrete and testable. If you cannot, your *why-now* is too abstract.

**The macro complement:** Apoorv Agrawal (Stanford MS&E 435, May 2026) hands the wiki the **AWS 8-year capex-cycle historical analog** as the broader temporal frame: *"AWS started in the year 2004. AWS had its first customer in Netflix in 2010. Ultimately Amazon shifted fully to AWS in 2012. 8 years from breaking ground."* The implication: the AI buildout we are watching today is structurally analogous to AWS 2004–2012; the value-capture pattern will not fully resolve for years; the right way to time your category is *capex-cycle timing + which-layer-wins resolution*.

A second supporting anchor: **Brandon Hill** at Vori names the same *category-not-yet-digitised* observation in grocery — *"the largest undigitised retail format in the world, the most-frequent consumer shopping behaviour on the planet, running on paper, pencil, fax machines, and paper clips."* The acuity-of-contrast in grocery is *between the SpaceX-grade tech across the street and the clipboard at the supermarket*. Vitucci's accounting parallel: *"In 2020, my parents showed me a stack of paper invoices and I assumed it was from when they were my age — they told me it was from last week."*

> 📒 **Accountancy-app callout.** The *acuity-of-contrast* slide for an accountancy app should literally show side-by-side screenshots. Left: the modern tools the customer's finance team uses daily — **Brex** (spend management), **Ramp** (corporate card + AP), **Rippling** (payroll), **Stripe** (billing). Right: the screen the customer sees when they need to file an R&D credit / reconcile a multi-entity consolidation / produce ASC-606-compliant revenue recognition. The visual asymmetry is the pitch. Then narrate the *why now*: every adjacent finance tool has been modernised in the past 5–10 years; the workflow you serve is the last domino.

**Action item.** Build the side-by-side screenshot slide. Show it to 5 prospective customers in the next two weeks. If they do not react with *"yes, that is exactly what I experience every day,"* either the contrast is not acute enough or you are talking to the wrong segment.

**Anti-pattern.** *"AI is happening and we should ride the wave."* Too abstract. The *why-now* that lands is operational and category-specific, not macro.

---

### Chapter 10: Velocity as the Procurement-Side Substitute for Feature Parity

A $300M-revenue customer signed Campfire when Campfire had **four employees**. The CFO's exact concern (~7:57–8:30 of the Campfire fireside):

> *"One CFO told me, literally we are making a venture investment in you by going with you because you can only be in one ERP really at a time. And so he was like, I'm literally getting fired if you shut down. And we are so large, and this contract is longer than your runway."*

What closed the gap was not feature parity. What closed the gap was **observable build pace**. Peer customers told Glasgow (~10:20–10:36): *"You guys are building so fast. As we add new global subsidiaries, as we need new features, as our usage-based revenue gets more complex, we feel confident you're going to be able to stay ahead of us."*

The wiki-relevant pattern: **forward-looking build-pace is the procurement-side substitute for present feature parity.** When the enterprise buyer asks *"how do I know you'll still be here in 5 years?"* (they will), the answer is not roadmap-promises; it is *here is what we built last week, here is what we built last month, here is what we shipped in the past quarter, and here are three named peer-customers willing to vouch for our pace.*

Two adjacent worked examples in the wiki:

- **Mukund Jha / Emergent**: $100M ARR in 8 months. The platform-vendor velocity instance. Customer-side reports framed Emergent's velocity itself as the feature (*"every model release we delete the system and reimagine it"* — system rewritten 4× in 9 months).
- **Ayush Garg / AnswerThis**: 45+ self-authored CLIs by the agent's coding sub-agent. The micro-scale velocity instance — $2M ARR with 2 full-time employees, where build-pace per FTE is the headline metric.

**Schoening provides the necessary caveat** (Notion): velocity is not the same as engineering quality. *"If you and I were to build a hardware startup, we would make the first enclosures with 3D printing — and you would see all the layer lines. It would be very obvious that this is not a thing you should give to people to pay for. Then there's a long windy road all the way to where, if you're very lucky, you get to manufacture that product for 100 million people."* Schoening's *prototype-vs-engineering* physical-metaphor: AI-generated code is the 3D-printed-prototype-with-visible-layer-lines; the engineering work is *optimise-the-factory-for-100M-users*. The current discourse over-weights how fast prototypes can be built; the under-discussed half is the engineering work that converts the prototype into a manufactured product.

**Adam Bender** (Google I/O 2026) names the same distinction at the ecosystem altitude: *"There's a big difference between generating code 10× faster and engineering 10× faster. At Google, we often say that engineering is programming integrated over time."*

**James Ivers** (Software Engineering Institute / Carnegie Mellon University, May 2026) lands the same caveat at the institutional-research-centre altitude with a specific worked example: *"I did a vibe-coding experiment. I produced an application soup-to-nuts, 25,000 lines of code in language I never written before. I got a very slick application but under the hood it was structured terribly. The architecture was bad. It wasn't very maintainable."* Paired with the temporal-horizon claim Ivers attributes to a prior talk: *"No one has maintained code that was AI generated for 5 years. It hasn't been around that long. We don't know what it's going to be to maintain this code in five years."* The handbook now has a **three-altitude triangulation** on the same engineering-discipline caveat: practitioner (Schoening at Notion), vendor-ecosystem (Bender at Google), and institutional-research-centre (Ivers at SEI). All three say the same thing — *velocity is a sales signal, but engineering discipline is what survives the 5-year maintenance horizon* — at the three altitudes the procurement buyer cross-references when doing a real reference check.

The implication for your build-pace narrative: lead with *programming* speed (visible, demoable, customer-facing), but back it with *engineering* discipline (uptime SLAs, error rates, audit trails, change-management). The procurement buyer evaluates *programming-speed-as-trust-signal* but reserves the right to look at *engineering-quality* once they care.

> 📒 **Accountancy-app callout.** Your build-pace narrative for an accountancy app should include: (a) a *changelog* on your public website with weekly updates including specific customer-requested features; (b) at least 3 named peer-customers willing to do a reference call on a specific *"in the past 6 months, this is what they shipped for us"* story; (c) a *roadmap-with-confidence-intervals* — *"these three things this quarter (high confidence), these three things in the next quarter (medium confidence), this is what we are exploring (low confidence)"*. Procurement-side trust is built by *showing your work*, not by promising the moon.

**Action item.** Publish a public changelog. Update it weekly. Build the muscle of *making your build-pace observable* before you need it as a sales tool.

**Anti-pattern.** *"We will show velocity through our roadmap deck."* Roadmap decks are promises. Procurement buyers discount promises. Changelogs are receipts. Changelogs are *forward-looking trust signals because they are backward-looking truth signals*.

---

## Part V — Build for Compliance and Compounding

*The next two chapters cover the discipline that separates the AI-native vendors that survive 5 years from the ones that get displaced. The discipline matters most in regulated verticals — accounting, law, healthcare, finance — where compliance is not optional.*

### Chapter 11: Skills Governance from Day One

The wiki's strongest empirical anchor on what goes wrong without skills governance comes from **Tushara Fernando** at Man Group (~$200B AUM regulated investment manager, May 2026). After Anthropic-led skills workshops drove enthusiastic adoption across the firm:

> *"We started to see cracks in our approach. It was really the power users that were building the skills. It wasn't the process owners. There was a guy who used to travel a lot at Man Group and he had loads of expenses to do. He wrote a skill for it. He gave lots of pictures of receipts to Claude and it would do the expense report for him. He brought this to the show-and-tell session and even shared it with a few people in his team. A few days later, the expense approver came to us and was like, 'Why is Claude creating so many expense reports for my cost center? People from technology, people from the people team. Why do I have to approve all of them? I'm in sales. I don't want to approve everybody else's expense reports.' And we dug into it and it was just because the cost-center code was hardcoded. Nobody had reviewed that skill. It worked for him, it worked for his team, so it was going to work for everybody. And he wasn't accountable for that. He kind of thought it was quite funny. And I mean, so did I, to be honest."*

The expense-report failure-mode is the wiki's clearest empirical worked example of why **skills governance is not optional once you scale to a real organisation**.

**The institutional-research-centre articulation of the same discipline.** **James Ivers** (Software Engineering Institute / Carnegie Mellon University, May 2026) names the discipline from the *broader software-supply-chain* altitude rather than from inside one firm: *"We don't let go of the safeguards that we have now just because there's more code. We might scale it differently."* Ivers's three concrete extensions of the discipline that matter directly for your product surface:

1. **Under-specification as the bad-practice-AI-magnifies-most.** *"If I gave [Cursor] a loose requirement, fine. It would just go generate code and it would fill in all the blanks. It would decide what corner cases worth handling, what weren't, what I really meant by that requirement. Terrible idea."* The spec, not the code, is the source-of-record. (Wu & An at Momentic make the same point from the founder-vantage; the SEI version is the institutional restatement.)
2. **Slop-squatting as a new attack vector.** *"Generative AI generates code for us. Sometimes it'll generate an include or a `with` of a package that doesn't really exist. The name sounds good but doesn't really exist. This has actually become an attack vector where adversaries can create a dummy repository with that bogus name."* The defence is the existing-discipline-applied: SBOMs, supply-chain management, third-party-code review. Your product surface needs to expose the package-and-dependency manifest of every skill the customer runs, not just the skill's behaviour.
3. **The 5-year-maintenance-horizon caveat.** *"No one has maintained code that was AI generated for 5 years. It hasn't been around that long. We don't know what it's going to be to maintain this code in five years."* This is why retire-by dates (below) are not optional bureaucracy; they are the operational answer to a horizon we cannot empirically calibrate yet.

The bridge to Fernando's solve: governance is not a vendor-side discipline you build for compliance officers to tick boxes. It is the **operational answer to a class of failure modes — expense-report-cost-center-hardcoding (Fernando), slop-squatting (Ivers), under-specified-skill-fills-in-the-blanks (both)** — that recur predictably at scale.

Fernando's solve — the **knowledge marketplace**:

- **Every skill is visible, tagged, tested with evals.**
- **The skill is owned by the workflow owner**, not the power user who wrote it.
- **Usage is tracked. Skills are reviewed. They have a lifecycle. They are visible to everybody to install.**
- **Plugins as groups of skills** (e.g., a *data plugin* gives access to Man Group's datasets).

The framework underneath is Garry Tan's **skillify protocol** from the same May 2026 cluster (Stanford CS153): unit tests + LLM evals + integration test + resolver entry + trigger eval + **check-resolvable** + smoke test + schema. Tan and Fernando are saying the same thing from opposite altitudes — Tan as the upstream rhetorical articulation (skills = employees, resolvers = org chart, check-resolvable = audit, trigger evals = performance reviews); Fernando as the empirical worked example of *what happens to a regulated firm when the protocol is not followed*.

A third anchor: **Harrison Chase** (LangChain, Interrupt 26, May 2026) names the same architecture as **three-layer continual learning**: model (Sonnet, GLM4, GPT-4) + harness (Deep Agents, Claude Code) + context (`agent.md`, skills). *"Evals act as a forcing function… those evals are providing a similar type of this training gradient."*

For your accountancy app, **skills governance is not just a vendor-side discipline. It is the customer-side product surface that lets compliance say yes.**

Fernando's lessons-to-past-me, delivered as a checklist:

1. *Focus on organisational context — that is your IP, your moat.* (Chapter 12.)
2. *Treat skills like production code* — version control, code review, deployment process, monitoring.
3. *Plan governance before rollout — who owns / reviews / retires / tests. **Before shipping the first skill, not after the hundredth like us.***
4. *Adoption is a people problem, not a licensing problem.*

> 📒 **Accountancy-app callout.** Bake **skill governance** into your product surface as a first-class feature, not a back-office concern. Concrete deliverables: (a) every skill / workflow your product runs is **owned by a named workflow-owner** in the customer's org (not by the user who first invoked it); (b) every skill has a **version history**, a **review trail**, and a **retire-by date**; (c) every skill produces a **machine-readable audit trail** (who invoked it, what data it touched, what output it produced, who reviewed the output); (d) your enterprise pitch deck has a slide titled *"How your compliance officer says yes"* that walks through (a)–(c).

**Action item.** Identify the *named compliance role* at three prospective customers. Build a 30-minute walkthrough of your governance surface specifically for that role. Schedule the three walkthroughs in the next 60 days.

**Anti-pattern.** *"We will build governance once we have customers asking for it."* Fernando's *before-the-first-skill-not-after-the-hundredth* lesson is the strongest single anti-pattern signal in the handbook. Governance built after the fact requires retroactive ownership-assignment and retroactive audit-trail reconstruction; both are nearly impossible at scale.

---

### Chapter 12: Context Is the Moat

The most directly-quotable wiki claim on where competitive defensibility sits in 2026 also comes from Fernando (~16:47):

> *"Focus on that organizational context. **That is your IP. It's your moat. It's one of the few safe spaces left in AI.** The frontier labs are not going to solve context for you. It's not on the internet. They don't know your workflows. And you already have that context. You have decades of it. The work is on exposing it, not reinventing it. And skills are how those decades of institutional knowledge become leverage."*

Harrison Chase (LangChain) provides the matching vendor-CEO articulation: in his **three-layer continual-learning model** (model / harness / context), the **context layer is where customer-specific value compounds**. The model is rented (and your competitors will outperform you within the year on any given model); the harness is yours; the context is *the customer's*. The product wraps the customer's context and exposes it for AI to operate on.

The architectural implication: **build the product so that the customer's encoded workflows, data pipelines, compliance rules, and accounting policies are the substrate** — not the model, not your application code. A model upgrade should improve your product without you having to migrate the customer's context. A customer who has built up 18 months of context on your product should find that context impossible to extract and replicate on a competitor.

Three companion framings from the wiki:

- **Garry Tan** (Stanford CS153): *"Organizational context is what you cannot fake. The frontier labs cannot give it to you. It is your moat."* Tan's articulation is shorter but the same.
- **Carly Ryan** (Anthropic, interviewing Mukund Jha of Emergent): a reusable triplet of *moats that intelligence alone cannot overcome* — *(1) deep user understanding; (2) proprietary infrastructure + regulated-space barriers; (3) human trust*. The triplet is the consumer-vendor angle on the same Fernando observation.
- **The wiki's [[concepts/foundation-models]] page**, citing Chatterjee 2026: *"Models are converging toward commodity status. They are rented from vendors whose competitors will outperform them within the year. They are swapped between, routed across, replaced quarterly… The model is what you rent. The harness is what you own."* In your version of that aphorism, **the context is what your customer brings, and your job is to make it impossible for the customer to extract.**
- **Mario Benitez** (SEI / Carnegie Mellon, May 2026) provides the abstraction-layer corollary: *"Before, we used to write assembly code and then compilers came along and you no longer needed to do that. I know this is still non-deterministic… but we're elevating a little bit. I'm not sure how much."* The model is the new compiler; *non-determinism is the new property of the abstraction-shift*. Your product's job is to absorb the non-determinism into a deterministic customer-facing experience — the context layer is what makes that absorption possible, and the moat is everything the customer has accumulated that the next-quarter's-better-compiler cannot rewrite for them.

The product-design corollary: **switching costs are determined by how much customer-specific context you have accumulated**. If your competitor can write a 50-line import script that pulls all the customer's data out of your product into theirs, you have no moat. If migrating off your product requires the customer to rebuild 200 governed skills, 1,000 reviewed workflow updates, and a multi-year audit trail, you have a deep moat.

> 📒 **Accountancy-app callout.** The context your accountancy app should accumulate per customer: (a) **encoded firm-specific accounting policies** (revenue-recognition rules, chart-of-accounts mappings, intercompany elimination rules, transfer-pricing assumptions); (b) **historical journal-entry traces** with reviewer annotations (which entries were challenged in audit, which were waved through, which were re-classified); (c) **per-customer skill library** for repetitive workflows (e.g., a *"close the books for May"* skill that encodes the firm's specific close-checklist); (d) **regulatory-jurisdiction context** (state-specific tax treatment, industry-specific accounting standards). All four are *impossible to replicate from scratch on a competitor's product* — which is your moat.

**Action item.** Map your current product's *context surface*. For each customer, can you list the named pieces of customer-specific context your product has accumulated? If the list is short or vague, your moat is shallow. Make accumulating context an explicit product-roadmap priority.

**Anti-pattern.** *"Our moat is the model — we fine-tuned it on accountancy-specific data."* The model is rented. The fine-tuning is replicable. The moat is the customer's accumulated context that your product wraps, not the model your product runs on.

---

## Part VI — The Long Game

*The final two chapters are the unit-economic comparison you use to win enterprise pitches, and the future-shape of the customer firm that should guide your 5-year product strategy.*

### Chapter 13: Revenue-Per-Employee as the Killer Comp

Vitucci's most memorable enterprise-pitch slide is a single number comparison (~25:35 of the Onshore Breakdown episode):

> *"This year in 2026 we're targeting getting to $100 million in revenue. By end of year, we'll have somewhere between 60 and 100 employees. Let's call it 100. So we'll make a million dollars of revenue per employee at least. And what is that number for someone like Grant Thornton or Deloitte or KPMG? My estimation would be probably $100,000, maybe $150,000. You're an order of magnitude better. And you will only get better going forward because you're software-based whereas they can't really change. And they will only get worse, especially now that we see instead of investing into technology, we see a lot of these big companies investing into overseas operations."*

The comparison is the killer pitch slide because it answers the CFO's first question — *"why should I switch?"* — with a single arithmetic claim the CFO can verify in 30 seconds. **Onshore: ~$1M revenue per employee. Big 4 / top-20: ~$100–150K revenue per employee. Order of magnitude.**

The wiki carries reinforcement of the *$1–2M revenue-per-employee* benchmark from multiple vantages:

- **Diana Hu** (YC, Stanford CS153): the YC AI-native portfolio benchmark — *$1–2M revenue per employee* — vs Salesforce comps at *"under six figures."*
- **Ayush Garg** (AnswerThis): $2M ARR with **2 full-time employees** + 2–3 contractors. The micro-scale instance.
- **Mukund Jha** (Emergent): $100M ARR in 8 months with a small founding team. The platform-vendor scale instance.
- **Tushara Fernando** (Man Group): 750 of 1,700 employees running Claude Code is the *enterprise-incumbent* comparison number — Man Group's 44% Claude-Code-adoption is what *good* looks like on the incumbent side, and even that is well short of $1M+ per employee economics.

Lead the enterprise pitch with the comparison and *make the CFO do the arithmetic*. The conversation that follows is no longer *"are you better?"* — it is *"can I trust the number?"* That is a much shorter conversation, and a winning one.

> 📒 **Accountancy-app callout.** Your enterprise pitch deck for an accountancy app should open with one slide: *"Big 4 / top-20: ~$100–150K revenue/employee. Us: target $1M+ revenue/employee. Order of magnitude. Here is why."* The *"here is why"* paragraph should reference Vitucci's structural reasons: (a) software-based vs hours-billed; (b) AI agents replacing the fat-bottom-of-juniors; (c) the incumbent is investing in overseas operations not in technology, so the gap will widen. Then transition to your *which-workflow* slides (Chapter 3) — but always anchor on the unit-economic comparison first.

**Action item.** Build the unit-economic comparison slide. Have it reviewed by a CFO of a target customer before your next 5 sales calls. If the CFO says *"that arithmetic doesn't work for [reason]"*, fix the arithmetic until the CFO says *"that's interesting."*

**Anti-pattern.** *"We'll show ROI through productivity gains."* Productivity-gain pitches are slow and squishy. Unit-economic comparisons are fast and crisp. The unit-economic comparison is what the CFO will repeat to the board on your behalf when you are not in the room.

---

### Chapter 14: The Future-Shape of the Customer Firm

Vitucci's 10-year forecast for the surviving accountancy firm (~22:02–24:25 of the Onshore episode):

> *"I don't think you'll have the very fat bottom layer because I think you'll have AI agents doing it. And I think the people at the top are mostly there for sales. Industry revenue will go up. Headcount will stay roughly flat. **Revenue-per-employee will go through the roof.**"*

The shape of the firm:

- **Small senior-partner layer** — for sales and rainmaking.
- **A regulatory-compliance / expertise layer** — for the situations AI cannot handle alone (novel regulatory interpretations, audit-defence, complex multi-jurisdiction matters).
- **A software-engineering layer** — to build and govern the AI infrastructure.
- **AI agents** doing what the fat bottom of juniors used to do.

Tom Blomfield (YC managing director, interviewing Vitucci) extends the thesis past accounting: *"The contention that software programmers will no longer write code sounded crazy nine months ago and now is like orthodoxy almost. My contention is the same thing is going to happen to accounting and law and audit. By the end of this year, I can see mass realization that the AI can do these knowledge-work jobs just as well or better than humans, and yet still not that big a change in employment rate — that might be five or six or seven years to come."*

The Tan & Hu (Stanford CS153) **primitives-as-company-structure** mapping is the higher-altitude version of the same observation:

| Tan's agentic primitive | Corresponds to (in the surviving firm) |
|---|---|
| **Skill** | Employee with a particular capability |
| **Resolver** | Org chart |
| **GBrain / memory** | Internal process / where information lives |
| **Check-resolvable** | Audit / compliance |
| **Trigger eval** | Performance review |
| **Skillify protocol** | The 10-step compliance discipline for codifying a workflow |

The wiki's most theoretically-grounded counter-point to *full junior automation* comes from **Chad Jones** (Stanford GSB, May 2026) — the **radiologist worked example**. Hinton predicted no radiologists in 5 years (in 2016). In 2026, there are *more* radiologists than in 2016, and they are paid *more*. *"Jobs are bundles of tasks. When the AI automates 75 of them, the weak links are the things that are now scarce and get the high return."* Augmentation persists at the senior tier *because the senior tier owns the weak-link tasks*; automation collapses the junior tier *because the junior tier owns the codified tasks*.

The product-design implication: **build for the org-shape your customer will become, not the one they are today.**

- If your product reinforces the fat-bottom-of-juniors org structure (e.g., a tool that needs an army of junior analysts to operate), you are building for the wrong end of the curve.
- If your product **collapses the junior tier into the senior-partner-plus-AI-agents structure**, you are building for the surviving firm.
- The intermediate-success scenario: your product is **the regulatory-compliance-and-expertise-layer enabler** — it gives senior partners the AI infrastructure they need to deliver the work that previously required 8 juniors.

> 📒 **Accountancy-app callout.** Five years from now, the firms your accountancy app sells to will look like: 4 senior partners; 6 regulatory-compliance-and-expertise specialists; 4 software-engineers / AI-infrastructure folks; 100+ AI agents doing what 80 juniors used to do. Design your product for *that* customer org, not the current one. Concrete implications: (a) your UI should be designed for senior-partner-level users who need to *audit* AI outputs, not junior analysts who need to *produce* them; (b) your audit-trail surface (Chapter 11) should be designed for the regulatory-compliance specialist's daily review; (c) your skills-marketplace (Chapter 11) should be designed for the software-engineer-on-the-firm-side to extend; (d) your pricing should assume the customer's headcount stays flat or shrinks while their revenue grows — i.e., per-output pricing, not per-seat pricing.

**Action item.** Sketch the org chart of your largest customer five years from now. Compare to their org chart today. Identify the three product features that are essential for the *future* org chart but irrelevant to the *current* one. Move those features up your roadmap.

**Anti-pattern.** *"We'll add seats and SKUs as the customer grows."* If your business model depends on selling more seats per customer, you are betting against the future-shape forecast. Per-output / per-outcome pricing is the right model for an industry that is collapsing its junior tier.

---

## Appendix A — Anti-patterns

The six most common failure modes derived from the same source set:

1. **Sell-to-firm-anyway.** *"The firm's distribution channel value is dwarfed by the firm's incentive to slow-walk you."* If you find yourself in month 18 of selling to the firm with eight customers and stalling, fire all eight and pivot to direct. (Vitucci.)
2. **Fat-bottom-of-juniors product-design.** Products that assume the customer's org has lots of junior analysts to operate the tool are building for the org structure that is going away. Design for the surviving structure. (Vitucci + Tan & Hu + Jones.)
3. **Skills-without-governance.** Enthusiastic skill-creation without ownership, review, lifecycle, and audit-trail discipline produces the *expense-report-failure-mode* at scale. Build governance before adoption, not after. (Fernando.)
4. **Outsource-sales-too-early.** Hiring a Head of Sales / AEs / AI sales agents before $1M ARR breaks the *sales-team-driving-engineering* feedback loop. Founder-led sales is not a phase to graduate from; it is a discipline to maintain until product-market fit. (Glasgow.)
5. **Feature-parity-first.** Trying to be feature-complete before going to market against an incumbent is a 10-year project. The wedge is the only feature you need to land the customer. Be the best at one thing, not adequate at everything. (Glasgow + Vitucci.)
6. **Model-as-moat.** Believing the fine-tuned model is your defensibility is a deep misunderstanding of the 2026 stack. The model is rented; competitors will catch up within the year. The moat is the harness you own and the context the customer accumulates inside your product. (Fernando + Chase + the [[concepts/foundation-models]] page.)
7. **Tar-pit-as-vertical / tar-pit-as-wedge.** *"By definition it is only a tar pit if it seems like it's not."* Verticals and wedges that produce strong initial validation but fail the retention test are the most expensive failure mode in this handbook — they cost *years* to recognise, not months, because the early signal looks positive. Apply Caldwell's *can-you-get-good-initial-validation-but-it-still-fails* diagnostic at every level: customer choice (Chapter 1), vertical choice (Chapter 2), wedge choice (Chapter 3). If your buyer is enthusiastic on the first call but you cannot point to a second-month-retention signal, treat the validation as positive-but-insufficient. (Caldwell.)
8. **Engineering-principles-can-be-abandoned-under-AI-volume.** AI-generated code at 10× pace without DRY / SOLID / YAGNI discipline produces 10× technical debt — and *"no one has maintained AI-generated code for 5 years yet"* (Ivers). Engineering principles do not get cheaper under AI; they get *more important* because more decisions are being made faster. The handbook's three-altitude triangulation on this caveat (Schoening / Bender / SEI) is in Chapter 10; the operational consequence is that **velocity is a sales signal but engineering discipline is what survives the 5-year maintenance horizon** — and procurement-side reference checks ask about both. (Sinclair / Ivers / Benitez / SEI.)

---

## Appendix B — Wiki Source Map

**Primary anchors:**

- [`2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt`](../wiki/sources/2026-03-07-vitucci-onshore-next-industry-ai-will-disrupt.md) — Dominic Vitucci, founder/CEO Onshore (YC W23), AI corporate tax + accounting. The wiki's deepest professional-services-AI-disruption anchor.
- [`2026-05-20-glasgow-campfire-erp-for-ai-revolution`](../wiki/sources/2026-05-20-glasgow-campfire-erp-for-ai-revolution.md) — John Glasgow, founder/CEO Campfire (YC S23), AI-native ERP. First wiki anchor on the AI-native safety inversion thesis at procurement-room altitude.
- [`2026-05-21-fernando-man-group-trading-signals-that-trade-themselves`](../wiki/sources/2026-05-21-fernando-man-group-trading-signals-that-trade-themselves.md) — Tushara Fernando, head of data + AI at Man Group ($200B AUM). The wiki's strongest empirical anchor on enterprise-scale skills governance.

**Founder-doctrine anchors:**

- [`2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer`](../wiki/sources/2026-05-20-tan-hu-stanford-cs153-ai-native-company-1000x-engineer.md) — Garry Tan + Diana Hu (Y Combinator) at Stanford CS153. AI-native company architecture; primitives-as-company-structure mapping; IC / DRI / AI-founder-type org model; $1–2M revenue/employee benchmark.
- [`2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents`](../wiki/sources/2026-05-21-chase-langchain-interrupt-26-future-of-ai-agents.md) — Harrison Chase, LangChain CEO, Interrupt 26 keynote. Three-layer continual-learning model (model / harness / context); evals-as-gradient.
- [`2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up`](../wiki/sources/2026-04-24-hu-yc-how-to-build-a-company-with-ai-from-the-ground-up.md) — Hu's earlier full articulation of the AI-native-company doctrine.
- [`2024-04-18-caldwell-lennys-podcast-lessons-1000-yc-startups-tarpit-ideas`](../wiki/sources/2024-04-18-caldwell-lennys-podcast-lessons-1000-yc-startups-tarpit-ideas.md) — Dalton Caldwell (YC managing director / group partner, 21 batches). The pre-AI-substrate-shift YC-partner doctrine: tar pit ideas; pivot-as-methodical (the Zip / Procurement worked example as the *find-an-incumbent-with-low-NPS* template Caldwell coached); customer-validation-first; growth-hacking-is-premature-for-seed contrarian; 2024 request-for-startups inventory (Caldwell-personally-authored ERPs prompt → Glasgow / Campfire's downstream worked example).

**Practitioner-vantage anchors:**

- [`2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era`](../wiki/sources/2026-05-02-schoening-lennys-podcast-cultivating-agency-ai-era.md) — Max Schoening (Notion). Agency-as-durable-AI-era-skill; Brian Leven + Eric Lou vignettes; prototype-vs-engineering metaphor.
- [`2026-05-19-mittal-yhangry-private-chef-all-in-on-ai-agents`](../wiki/sources/2026-05-19-mittal-yhangry-private-chef-all-in-on-ai-agents.md) — Siddhi Mittal (Yhangry). The *fired tech lead in a week* vignette as the bluntest articulation of org-design urgency.
- [`2026-05-19-garg-yc-internal-ai-agent-evolves-itself`](../wiki/sources/2026-05-19-garg-yc-internal-ai-agent-evolves-itself.md) — Ayush Garg (AnswerThis). $2M ARR / 2 FTE; self-extending Claude Code harness; Ryan as workflow-ownership credibility variant.

**Vertical-worked-example anchors:**

- [`2026-05-11-hill-vori-grocery-os-paper-and-fax`](../wiki/sources/2026-05-11-hill-vori-grocery-os-paper-and-fax.md) — Brandon Hill (Vori). Inventory-app-as-wedge → 4-year compound-startup expansion.
- [`2026-04-16-bodewes-phonely-ai-callers-think-is-human`](../wiki/sources/2026-04-16-bodewes-phonely-ai-callers-think-is-human.md) — Will Bodewes (Phonely). Voice-AI-for-call-centers wedge.
- [`2026-05-13-jha-emergent-democratizing-app-building-with-claude`](../wiki/sources/2026-05-13-jha-emergent-democratizing-app-building-with-claude.md) — Mukund Jha (Emergent). $100M ARR / 8 months; adoption-velocity-asymmetry-favouring-the-long-tail; *moats that intelligence alone cannot overcome* triplet.
- [`2026-04-25-masad-replit-ceo-only-two-jobs-left`](../wiki/sources/2026-04-25-masad-replit-ceo-only-two-jobs-left.md) — Amjad Masad (Replit). *Only two jobs left: builder + salesperson.*

**Theoretical / academic anchors:**

- [`2026-05-21-jones-stanford-gsb-ai-and-our-economic-future`](../wiki/sources/2026-05-21-jones-stanford-gsb-ai-and-our-economic-future.md) — Chad Jones (Stanford GSB). Weak-links macroeconomic model; jobs-as-bundles-of-tasks; Hinton-radiologist worked example.
- [`2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai`](../wiki/sources/2026-05-20-agrawal-stanford-mse435-economics-of-generative-ai.md) — Apoorv Agrawal (Altimeter / Stanford MS&E 435). AWS-8-year-capex-cycle historical analog; are-you-a-feature-or-a-platform diagnostic.
- [`2026-05-21-bender-google-io-software-engineering-tipping-point`](../wiki/sources/2026-05-21-bender-google-io-software-engineering-tipping-point.md) — Adam Bender (Google). Socio-technical ecology; programming-vs-engineering distinction at AI-era scale; DORA-rooted *AI as amplifier* framing.
- [`2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering`](../wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md) — Scott Sinclair / James Ivers / Mario Benitez (Software Engineering Institute, Carnegie Mellon University). The institutional-research-centre voice on AI-native software engineering discipline. *"AI native is not AI only"* (Ivers); engineering principles endure (DRY / SOLID / YAGNI); the 25,000-line vibe-coding-experiment worked example; under-specification as the bad-practice-AI-magnifies-most; *no one has maintained AI-generated code for 5 years yet*; slop-squatting as a new attack vector; coder-vs-software-engineer role-shift framing; Benitez's compiler-analogy on the non-determinism property of the new abstraction-shift.

---

## Appendix C — Further Reading

Companion concept pages on the wiki that go deeper than this handbook on specific topics:

- [`concepts/agent-harness`](../wiki/concepts/agent-harness.md) — the technical-architecture layer Chapters 11 + 12 build on. 40 source-anchors, the wiki's largest cluster.
- [`concepts/enterprise-ai-adoption`](../wiki/concepts/enterprise-ai-adoption.md) — the *wedge → ERP-transplant* + *no-code-domain-experts-build-their-own-tools* customer-side trajectory referenced in Chapters 1, 3, 4. 42 source-anchors.
- [`concepts/durable-skills`](../wiki/concepts/durable-skills.md) — Schoening's *agency-as-disposition-to-act* framing; Chapter 6's roles-you-need backdrop.
- [`concepts/ai-employment-effects`](../wiki/concepts/ai-employment-effects.md) — Jones's weak-links model; Chapter 2's vertical-pick framing and Chapter 14's future-shape forecast.
- [`concepts/dynamic-capabilities`](../wiki/concepts/dynamic-capabilities.md) — Warner & Wäger lens on what enterprise buyers are trying to build, which is the demand-side mirror of what your product supplies.
- [`syntheses/strategy-finite-vs-infinite-game`](../wiki/syntheses/strategy-finite-vs-infinite-game.md) — Sinek's layered framing of finite vs infinite games. The closing-philosophy frame for *why you are doing this for the next 10 years, not the next 18 months*.

---

*This handbook is a working note in `inspiration/`. The 12-lesson source synthesis it builds on is at [`inspiration/2026-05-22-lessons-for-ai-native-accountancy-app-founder.md`](2026-05-22-lessons-for-ai-native-accountancy-app-founder.md). If a future iteration formalises this handbook as a wiki page, it would land at `wiki/syntheses/founders-handbook-ai-native-vertical-startup.md` with full frontmatter, typed `supports` edges to the primary anchors, and a `derived_from:` link to the 12-lesson thread.*

*Updated 2026-05-22 with the day's two-video ingest — [Caldwell / Lenny's Podcast](../wiki/sources/2024-04-18-caldwell-lennys-podcast-lessons-1000-yc-startups-tarpit-ideas.md) as the pre-AI-substrate-shift YC-partner doctrinal anchor (additions in Preface, Chapters 1, 2, 3, 7; Appendix A item 7; Appendix B founder-doctrine anchors) and [Sinclair / Ivers / Benitez / SEI-CMU](../wiki/sources/2026-05-21-sinclair-ivers-benitez-sei-cmu-ai-native-software-engineering.md) as the institutional-research-centre voice on engineering-discipline-endures (additions in Preface, Chapters 10, 11, 12; Appendix A item 8; Appendix B theoretical / academic anchors).*
