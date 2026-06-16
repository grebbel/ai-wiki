---
title: "Architecting AI-Native Organizations: How to Redesign Work at Scale - Joe Beutler"
video_id: fFOLWoHyWLE
url: https://www.youtube.com/watch?v=fFOLWoHyWLE
channel: IT Revolution
channel_id: UCkAQCw5_sIZmj2IkSrNy00A
channel_url: https://www.youtube.com/channel/UCkAQCw5_sIZmj2IkSrNy00A
publish_date: '2026-06-02T14:56:58-07:00'
upload_date: '2026-06-02T14:56:58-07:00'
category: Science & Technology
duration: '25:25'
length_seconds: 1525
view_count: 121
default_language: null
is_live: false
is_family_safe: true
keywords:
  - AIStrategy
  - AgenticAI
  - Joe Beutler
  - OrgDesign
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
chapters:
  - {title: Introduction by Gene Kim, start: '0:00'}
  - {title: The Enterprise AI Adoption Gap, start: '1:49'}
  - {title: "OpenAI's Internal AI Wins", start: '3:40'}
  - {title: Business Owners Drive Outcomes, start: '6:13'}
  - {title: Embedding Engineering in Business, start: '9:59'}
  - {title: Ask, Assist, Automate Framework, start: '12:51'}
  - {title: Customer Case Studies, start: '16:44'}
  - {title: Where to Start and Key Takeaways, start: '21:44'}
description: |
  Joe Beutler, Head of Solutions Engineering for Strategics at OpenAI, draws on firsthand experience inside OpenAI and across its largest enterprise customers to explain what structural changes actually enable AI-native organizations. He examines why most companies are stuck between broad workforce tools and a handful of top-down strategic initiatives—and what it takes to unlock automation at the team and department level. In this talk, you'll learn how to separate governance from transformation, why embedding engineering directly inside business functions is the key to scaling AI adoption, and how to use the Ask-Assist-Automate framework to move from early experiments to production-grade agentic workflows responsibly.

  PRESENTED BY
  Joe Beutler — Head of Solutions Engineering, Strategics, OpenAI

  CHAPTERS
  0:00 Introduction by Gene Kim
  1:49 The Enterprise AI Adoption Gap
  3:40 OpenAI's Internal AI Wins
  6:13 Business Owners Drive Outcomes
  9:59 Embedding Engineering in Business
  12:51 Ask, Assist, Automate Framework
  16:44 Customer Case Studies
  21:44 Where to Start and Key Takeaways

  LINKS
  📊 Slides: https://raw.githubusercontent.com/devopsenterprise/2026-spring-eais/main/Beutler%2C%20Joe.pdf
  🎥 Watch in the IT Revolution Video Library: https://videos.itrevolution.com/watch/1183556417

  ABOUT THE EVENT
  Enterprise AI Summit: Spring 2026
  April 9-10, 2026

  ABOUT IT REVOLUTION
  IT Revolution helps technology leaders succeed through books, research, and events.
notes: |
  ASR-cleaned auto-transcript (single caption track, kind: asr). Cleanups applied:
  speaker name "Joe Butler" → "Joe Beutler" (per channel description); "chatbt" /
  "chachib" / "chatt" / "chatg" → "ChatGPT"; "codeex" → "Codex"; "PWC" → "PwC";
  "BBVA" verbatim; obvious stutters and filler ("uh", "um", duplicated words)
  lightly trimmed for readability; timestamps preserved. Section headings follow
  the YouTube chapter markers. The JSON export duplicated the segment list; only one
  copy is retained here. Talk presented by Joe Beutler (OpenAI), introduced by
  Gene Kim, at the IT Revolution Enterprise AI Summit Spring 2026 (9–10 April 2026).
---

## [0:00] Introduction by Gene Kim

[0:00] *(Gene Kim)* To set the stage for the next talk: I had mentioned this morning that we're trying to figure out what are the conditions that must exist to get genuine 10x gains in productivity, as opposed to like 20% gains — which maybe in another generation would have been something to brag about, but it seems like that's just not what the potential really is.

[0:22] And so here to explain what I think a big piece of that puzzle is — Joe Beutler. He is head of solutions engineering for OpenAI's largest enterprise customers. I met him over two years ago and I've learned so much from him. It helps that obviously he's a super switched-on guy, but also the fact that he's in a foundation lab — I think it shows us what is happening within their organization is going to predict what's going to be happening in our organization.

[0:48] So when we last talked, Joe had shared with me a stat that blew me away. PwC benchmarked OpenAI's finance team and noted that it was only 20% of the size it should be. I'm sure they calculated and factored in revenue complexity, transaction volume, entity count, regulatory burden. But there's something interesting about that, and Joe sort of explaining what he thinks the structural reason that enables that is: the CFO has an engineering manager working for her, working on integrating AI and engineering. So does the chief revenue officer. In fact, they've embedded engineering managers throughout the company. And I think this phenomenon is actually going to be replicated across all our organizations. In fact, I think you've even heard hints of that in the presentations over the last two days. So here to talk about what he calls moving centers of excellence to embedded innovation — Joe Beutler.

[1:50] *(Joe Beutler)* You just did my whole talk for me, so I can just go ahead and sit down. Nice to meet you all, those that I haven't met. I'm Joe Beutler. As Gene mentioned, I lead the solutions engineering function at OpenAI. I used to be across all of our strategic accounts, now focusing more on financial services. One of the things I wanted to share today is how we are structurally changing inside OpenAI. A lot of that is what we've learned from working with customers — that's the advantage I have, being across a lot of our largest customers: we're seeing what everyone is trying to do as they adapt to the new realities we have with AI.

## [1:49] The Enterprise AI Adoption Gap

[2:25] To kick off: there have basically been two approaches we've seen for AI adoption. There's a bottoms-up approach, where people are providing workforce tools like ChatGPT to their employees to help them be more productive in their day-to-day work. And then from the top down, there are these large strategic initiatives — maybe one to three initiatives that companies are picking to go after — where they're going to try to build agentic systems that can automate significant workflows. That might be automating your call center or things along those lines.

[2:59] But what's been missing is what's in the middle, which is this concept of **team agents**. We're trying to get to: how can you have more automation at the team and department level, instead of just these major AI initiatives, or "I'll just give everybody these tools and they can figure out how to be more productive themselves." So that's the gap. A lot of the agent products we're seeing come to market, a lot of the stuff we're working on, we're trying to fill that gap and make sure we're able to distribute the benefits of AI through all the different organizations. I'm super excited about this. I think that will address the big enterprise value gap that everyone keeps talking about.

## [3:40] OpenAI's Internal AI Wins

[3:40] We've seen this firsthand inside OpenAI. One example is in our finance team. Here's one specific example where they identified a large opportunity to eliminate manual work across contract workflows. They now use the OpenAI API to extract and structure data and feed it into their downstream systems. The result is they're starting to see millions of dollars of impact across these workflows. And this is just one example from our finance team, which Gene mentioned. Our CFO is probably one of our most AI-forward executives in the company. More recently, she shared with us that her team built a GPT to help with due diligence questions across the massive fundraise we just completed — and that GPT was able to answer thousands of questions we got in from investors.

[4:33] That's how we're starting to see those efficiencies — where, as Gene mentioned, PwC benchmarked that the finance team is only 20% of the size it should be for an org doing the type of business they're doing. And that's not just against legacy finance orgs, that's also against comps in the market that are more digitally native.

[4:48] Another example is from our go-to-market team — that's where I sit, all of our customer-facing employees. We identified a core constraint: our products were outpacing our ability to scale the sales team. The bottleneck was all this top-of-funnel work — qualifying leads, engaging prospects, gathering the information needed to move deals forward. So we redesigned that workflow. This is one of the things I've been most excited about. As you can imagine, everybody wants to talk to us, and that was very difficult to do, especially a couple of years ago when you could kind of count the sales team — the sales team could definitely fit in this room. Now obviously we're scaling that sales team, but part of the way we've been able to scale our business — especially for more scaled parts of the market like SMB — is by building a lot of this automation.

[5:39] We've automated everything from analyzing leads to qualify them, figuring out if they should be routed to a salesperson or if it should be more of a self-service motion, to collecting purchase details to prepare a quote. So for that scaled part of the market that doesn't qualify for talking to a salesperson, can we just automate that entire sales process? That's effectively what we've done — we'll have an agent send back a quote, then they decide whether they want to buy, and it'll route those opportunities to sales if needed.

## [6:13] Business Owners Drive Outcomes

[6:12] We deploy our own technology across every function in the business, and it started with a clear mandate: each functional leader was responsible for identifying the highest-value opportunities to drive cost savings and growth within their organization. What we found is that this can't just be one or two use cases across the whole company, or even per department — it's going to need to be dozens of use cases that people are surfacing as they recognize potential impact for their org. Because the people closest to the work are the best positioned to see where AI creates leverage.

[6:54] Part of that is an enablement problem — people need to know how to use the tools so they can start to recognize how they might automate their own workflows. But then we also need to combine that with domain ownership, where you have the right technical support, so you can unlock better decisions on what to build and where agents can drive value within that org.

[7:14] So what this has led to is three main takeaways. As we've embedded AI into these functions like finance and go-to-market, the lessons have been consistent: the bottleneck is rarely the model capability — we're finding that it's **org design, ownership, and workflow clarity**.

[7:35] If you want to architect an AI-native organization, there are three things you have to get right. First: business leaders need to own the outcomes. Second: engineering needs to sit within that business function, so they're close enough to the people doing the work to understand how to actually automate the workflow. And third is a framework — I shared it in Vegas, I'll share it again, it's evolved a little bit — the idea of an **Ask, Assist, and Automate** framework to decide where to start and how to scale responsibly.

[8:08] To start, one of the clearest lessons we've seen is that you can't have the same person own transformation and governance, because one or the other tends to win out. We've seen department transformation succeed when the business leaders own the outcomes for their own organization, not central IT. If the head of a business unit is not accountable for the result, you probably don't have an agent — you have a demo. Central IT should own the foundations: all the firmwide governance and tooling, and the biggest cross-company initiatives. But the business units need to own the transformation in their own domain, because they know the work, they know the bottlenecks, and they know where AI can create the real value.

[8:57] What we've seen with some of the organizations — like our CRO's and our CFO's orgs (I'm closest to the CRO's work) — is that they've actually started hiring dedicated innovation teams. One thing that's really interesting about how we got here: somebody asked me the other day, "How do you know, as a CFO, how to go out and hire an engineering leader?" It's something that happened a little more organically.

## [9:59] Embedding Engineering in Business

[9:22] I'll speak to what happened in our sales org. We had somebody who was a seller on our sales org who was just obsessed with AI and started building tooling for themselves, and then it started being used by their colleagues. Over time we realized we needed somebody who could actually own that tooling for the job function — because if you're just doing that on the side of your desk, it's not getting the attention it needs if somebody still has a full-time job. So we took that person, who was a domain expert, and started shifting them into a role where they could own these tools full-time.

[9:59] If you follow that pattern, what we really see you need to be successful is different phases:

- A **domain expert** who defines the requirements, the quality, and the edge cases for the agent or workflow automation you're building.
- An **AI expert** who advises on project selection, sets up the evals, and establishes the system behavior. Fortunately for us internally we have a lot of AI experts — but this is where my team spends the most time with our customers, where we step in to fill that role while we enable those customers to build their own AI experts.
- A **software engineer** who can connect the context, the identity, and the telemetry.

[10:51] That's where you go from having the domain expert who knows how to do the job — they figure out how to use different tools, whether that's ChatGPT or Codex or any number of other tools on the market, to start to automate those workflows — but then when you actually want to bring it to something that is production-ready, you end up needing somebody from engineering to step in and help.

[11:14] What we ended up doing internally: our engineering teams were not happy that the CRO or CFO was going to go hire an engineer or engineering leader directly into their organization. So it had to happen a little more organically. When we hired the first engineer into the sales org, they had to be interviewed by our engineering org, so they could make sure that person would be on the same comp ladder as the engineers — they wanted to make sure they were at the same quality bar. So that team started as the domain expert who was tinkering and building tools for the team; then we paired them with an engineer who could perfect those and build real automation; then we brought in a head of innovation — that engineering leader who's now scaling out the team. It's been a really interesting evolution over the last couple of years.

## [12:51] Ask, Assist, Automate Framework

[12:03] So I started by talking about the org and team structure we're seeing take shape to drive this innovation across the business. Now I'll go a little deeper and talk about what it takes to actually build these AI systems or agents once you have those teams in place.

[12:22] When people hear "agents," they usually want to jump straight to automation — that's the big prize, that's where everyone's trying to go. But in my experience, I haven't really seen that work. It's really hard to go from zero to full automation, especially in regulated or enterprise environments where you have all those compliance things to worry about. So you have to start with a strong foundation with evals and governance, and then you can build toward automation.

[12:53] The way we've seen that work is you start with **Ask**: if you're building any kind of agentic system, the first actions you want it to take are to reach into your data and do read-only operations. Have it go out, pull in information, answer questions. Then you'll be able to validate that it's able to answer the questions and find the sources correctly — the way you want it to — before you give it any kind of access to do write actions or anything that could be potentially destructive.

[13:24] Once you get really confident in those Ask-level capabilities, you can move to **Assist**, where users start to complete tasks. You'd have the agent recommend what action it thinks it should take, and then you have the human in the loop to validate — "yes, this is the right thing, go ahead and execute," or "no, this isn't quite right" — and that lets you recognize where the agent's falling short before you actually let it go off and work on its own.

[14:01] Then what happens naturally is you realize there are certain types of things the agent is always getting right — it figures out the right tool to call, the right action to take — and so you can stop putting those in front of humans, and that's where you naturally end up at the **Automate** phase.

[14:15] I learned this framework working with T-Mobile a couple of years ago. They had really big ambitions for AI transformation, and their goal was to automate their entire call center — or at least 75% of it. We got them to come back a little bit. Where they were starting, they had already automated about 60% of those customer interactions, so this was targeting 75% of the remaining 40%. And that was a $3 billion cost center for them — a massive prize. They wanted to go straight to Automate, as everyone does. We walked them through: hey, we have to build foundations, we need to build evals, you're going to need people who are the experts doing the job to validate the output and the next actions. Across all of that, we were able to show them it was actually best to start with Ask, so you could make sure you're pulling from the right data sources, and then have that human in the loop before you start executing any write actions.

[15:26] With this foundation and framework, we've seen success with really any use case where we want to automate critical but defined workflows that are being done by people today. The biggest value is obviously at Automate — but that's also where you have the most integration, the highest quality bar, the strongest evaluations, and the most operational ownership needed from the people doing the job today.

[15:56] Aside from the technical challenges, getting support from the business users so you can start to automate these things happens much more naturally when you start by building tools that help them do their job. When you go back to Ask — if you're creating some kind of co-pilot, whatever you want to call it, an agent that helps them know how to do their job and answers questions for them — then you can start to hill-climb toward full automation. Once they see the value in the tool, they'll provide you feedback on how to improve it. Eventually you get this natural flywheel as you hill-climb toward automation. Plus you start to get value quickly as it grows, and then it grows exponentially as you unlock each new level.

## [16:44] Customer Case Studies

[16:44] I want to make this concrete and share a couple of examples of work we've done. To start, I'll talk about what we did with a **large insurer** to build an auto-claims agent. In the **Ask** phase, they built a read-only chatbot that helps their team answer FAQs and pull together policy information, customer records — basically everything across the firm they'd need to answer questions when evaluating one of these cases. Once this is proven, you can make this chatbot customer-facing: it can start as an internal tool for client-facing teams, and eventually you make it external so it helps people directly.

[17:23] Once you have high confidence in that, you move to **Assist**, where it starts to draft the analyst work — it summarizes issues, flags gaps, and prepares recommendations for each next step, but still requires human approval before taking action. Then in **Automate**, you reach the prize: once the workflow is stable and the quality bar is cleared, it can begin handling low-risk, standard cases end-to-end and is only routing exceptions to humans for review.

[18:01] One more example — here's the same progression with another customer in **wealth management**. There are millions of people going to ChatGPT for financial advice today. These are the clear types of opportunities for businesses that have direct consumer exposure. At **Ask**, the agent helps advisers answer questions quickly — they can pull product details, account history, prior interactions, and even get valuable market research context. This creates real value for the advisers very quickly. At **Assist**, it starts doing real work: it will draft prep notes, create follow-ups, and draft portfolio review materials that the advisers can review and approve before they're sent to clients. Once proven, you get to **Automate**, where you can start to automate a lot of the routine work and client interactions these advisers do today.

[19:08] Obviously we have to be careful with things like actual investment advice — I feel like I need a disclaimer here. But the reality is that millions of consumers are using ChatGPT to do tasks like this today, so there's a real opportunity to push into building products for consumers, even in more sensitive areas like wealth management.

[19:31] If you're still not convinced, we've also done this across many different workflows with **BBVA**. BBVA is one of the fastest-moving financial institutions I've seen — which is obviously very difficult in a regulated industry — and they're building these types of processes across multiple departments in parallel. That's everything from customer service, to sales agents they call their "AI banker," to risk automation and operations automation. And that's all the same pattern, following that Ask, Assist, and Automate framework.

[20:08] Today, building these high-quality agents takes a lot of work. You need that domain expert who knows how to do the job, the AI expert who understands what's possible with the tools today, and the software engineer who can actually build it if it requires tying into backend systems. It's a lot of work and it takes time. As I mentioned earlier, one of the biggest prizes I see right now in enterprise AI is these **no-code agent builders**, where you can type to build agents to automate your own workflows. This is one of our main focus areas right now.

[20:50] The end state we want to get to is: instead of having a software engineer tie into things like APIs and your different data, and build custom evals and guardrails for each of these tools, we want to be able to productize that. That's one of the differences in how we approach a lot of these problems — we don't have a massive professional services business where we're trying to go in and get lucrative contracts that will last 10 years. We're trying to enable each individual to figure out how to use AI on their own and build these things for themselves. That could look like an agent-building platform that's no-code, has continuous evaluation, has all the governance you need to get through your IT security, but also has connectors that tie into the different data sources that matter, and provides skills — repeatable things you can share across the business.

## [21:44] Where to Start and Key Takeaways

[21:43] Now that you've seen some of these examples, the next question is usually: where do you start? This is how we apply the model internally with our own teams and with customers. This is kind of an eyesore — I made it myself. But this is what I did with my team on our solutions engineering function. We went through and identified all the different workflows that make up the job we do today. We tracked: how are we using AI against those? How often are we doing those tasks? How much time are we spending? Where are we using AI today, and where do we think there's an opportunity to get to more assisted AI functions or full automation? That's how we identified which use cases could be most useful.

[22:26] One of the difficult things is you can't build all of these at once, so you have to pick your bets. You start with the experts on your team who are already building and using these agents, and then you identify which of those bets you should elevate — moving from the individuals doing the work to a centralized team that's going to own getting those up to production value.

[22:48] Once the agent is built and clears that performance benchmark, the real fun begins. Everyone in the business functions, or even cross-functional teams, can start using that agent. If I build an agent for my own team — that might be doing a function other people typically reach out to my team to do. One example I like is our security questionnaire agent that someone on my team built. Typically we have salespeople, customers, or customer support reps asking the solutions engineers with security expertise to answer those questionnaires. We now have an agent they can use directly, so they don't have to come to us.

[23:25] But of course, these types of tools need management — we keep introducing new products, there are new security concerns people will have. So we're starting to move toward a world where part of someone's job is as an **AI agent manager**. We could see this becoming a full-time job in the near future. I share that as something a little more forward-looking, but you can imagine that if somebody builds an agent and they're the domain expert, you're then going to need to manage that agent — make sure the output quality is high and that it's staying up to date on the job function, the same way you'd need training and enablement for people on your team.

[24:04] I want to leave you with three key insights to make sure you're set up for success. **First**, keep governance and transformation separate: central IT should own the platform, guardrails, and shared tooling, while business leaders own the outcomes for their own organization. **Second**, scale happens when engineering is embedded directly into the business function — they're close to the experts and the workflows selected for automation. **Third**, every agent needs a domain owner: someone has to be accountable for the quality bar, understand the edge cases, and know when the system is ready to scale.

[24:41] If the last decade was about digitizing workflows, the next one will be about building and managing agentic workflows. And this is the real architecture question that is in front of all enterprises right now.

[24:57] Gene always asks for help requests. These are two areas I'm currently working on a lot and really obsessed with. Obviously the second one — focusing on re-architecting teams — is what we talked about today. I'm also super interested in what's happening in the product development life cycle, outside just the core software development life cycle. If you're already working on that, I'd love to hear what you're doing. If you're interested in experimenting with some of these concepts, I'd love to connect and see how we can collaborate. Thanks, everyone.
