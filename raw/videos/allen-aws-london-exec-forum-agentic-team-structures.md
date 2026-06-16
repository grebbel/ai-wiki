---
title: "London Executive Forum 2026 - A leader's guide to advanced team structures in an agentic world"
video_id: ECLHOG3uYzk
url: https://www.youtube.com/watch?v=ECLHOG3uYzk
channel: AWS Events
channel_id: UCdoadna9HFHsxXWhafhNvKw
channel_url: https://www.youtube.com/channel/UCdoadna9HFHsxXWhafhNvKw
publish_date: '2026-05-21T11:26:36-07:00'
upload_date: '2026-05-21T11:26:36-07:00'
category: Science & Technology
duration: '43:54'
length_seconds: 2634
view_count: 1862
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
keywords:
  - AWS
  - Amazon Web Services
  - AWS Cloud
  - Amazon Cloud
  - AWS re:Invent
  - AWS Summit
  - AWS re:Inforce
  - AWS reInforce
description: |
  As AI agents transform the workplace, organizations must adapt their structures and methodologies to harness new opportunities. The probabilistic nature of AI requires continuous iteration and intelligent oversight, creating new ways of working across business functions. To thrive, organizations must combine clear capability assessment with agile planning while leveraging their unique domain expertise and data assets. This keynote explores how leadership is evolving to meet these needs, covering new organizational models and roles that coordinate human-AI hybrid teams. Leaders will learn strategies for balancing rapid decision-making with strategic oversight, finding the optimal mix of centralized guidance and decentralized innovation.

  Speaker: Jonathan Allen, AWS Executive in Residence & Nick Francis, Chief Technology & Marketing Officer, Brooklyn Solutions

  Learn more about AWS events: https://go.aws/events
notes: |
  ASR-cleaned: "Verer Vogles"→"Werner Vogels", "Anthony Lrini"→"Anthony Liguori",
  "Martin Fowl"→"Martin Fowler", "shrumpian"/"Schrumpian"→"Schumpeterian",
  "Nandanda"/"Nanda"→"NANDA", "podantic"→"Pydantic", "Sonet"→"Sonnet",
  "Opus 47"→"Opus 4.7", "GPC"→"GPT", "S sur"/"SRRES"→"SRE"/"SREs",
  "agent encore"/"encore"→"AgentCore", "gold-based"→"goal-based",
  "Martin Fowl"→"Martin Fowler", "Matt Garmin"→"Matt Garman",
  "Franchesca"→"Francesca", "deskkilling"→"deskilling",
  "MTR"→"MTTR", "Danska Bank"→"Danske Bank", "Jevans"→"Jevons".
  Speaker switch from Jonathan Allen to Nick Francis at ~33:20.
---

## Transcript

[0:07] Thank you to Yanna and Phil. Always insightful. Many of you may have seen this Scott
[0:13] Galloway quote: "AI won't take your job. Someone using AI will." Everyone heard
[0:19] this, seen this — a few of us. Yeah. What about this one?
[0:28] That uncomfortable moment. Am I the horse in what's going on right now? We don't want to be the horse, right? We
[0:34] want to be in charge. But this is actually the conversation that's going on. Now, this presentation
[0:40] I actually created originally at the AWS re:Invent conference that I presented in in December in Las Vegas last year.
[0:47] Since then, between then and now, I spent about 400 hours updating this presentation.
[0:52] And it's interesting what's going on. I've interviewed many of you. I've interviewed many of the Amazon leaders.
[0:58] I've built my own production products. I've helped customers get into production with their agentic systems.
[1:03] And although this is slightly amusing, the concern that we feel — the concern as
[1:10] employers, employees, as leaders — is very real. So let's ground it in a little bit
[1:15] of data. This report came out from Anthropic just last month: labor
[1:21] market impacts of artificial intelligence. And it's really only just started if you
[1:27] actually look at the data in here. So this blue on the spider diagram you're seeing is the potential disruption right
[1:34] now of these frontier models. The red is where it's actually started.
[1:42] So this is really early days still. And then when you look at the effect on
[1:49] unemployment and the unemployment rate, least exposed, most exposed —
[1:55] interesting data point again. And then when you look here at the exposure, the
[2:01] projected employment change, you can start to plot this out in your own mind.
[2:07] So this is real. But before we go on, let's just ground ourselves in what an
[2:12] agent really means. When we look at the spectrum, when we look at automation,
[2:18] all of us have looked at automation for years — even a cron job if you're looking at a Unix-based system executing code,
[2:26] still heavily used in agentic systems by the way — through to AI assistants. We've all used ChatGPT in this room or
[2:32] Claude. My personal favorite is Anthropic. Through to these goal-based agents, which I call them on here.
[2:38] You'll probably know them better as the coding assistants — the Claude Codes, the Codex from OpenAI, the Amazon Kiro from
[2:46] Amazon. These goal-based agents, which really only started in legitimacy
[2:52] October last year, have fundamentally changed the game.
[2:57] The ability to drive a goal, to instantiate code, has fundamentally changed the game — all the way through to
[3:03] an agentic system. And let's not overthink what an agentic system is. By the way, an agentic system is
[3:09] fundamentally a prompt with context or the ability to pull tools in that's hitting a language
[3:16] model. And in my experience right now, 80% of the use cases that customers are hitting is actually one of the frontier
[3:22] models — one of the frontier models when they're building these systems.
[3:28] So these goal-based agents have changed the game because not only can they take
[3:33] on a goal, they can instantiate that infrastructure. My personal projects which I've built at
[3:39] home, the ability to then take them to the cloud, a reasonably complex multi-agent system with a few gigabytes of
[3:45] data — suddenly to build that and have the goal-based agent build this and instantiate my entire AWS environment
[3:52] securely in 45 minutes with all the CloudFormation code required, blows my mind.
[3:59] So what's going on when you actually look at it is the ability to write software. There was a fascinating stat
[4:05] that I briefly saw this morning where I was talking about the amount of code contributions to GitHub have gone up by
[4:11] an inordinate amount just in the last 6 months. So you've actually got to think about this not from a job threat point
[4:17] of view but from a Jevons paradox point of view. And we've seen this every time
[4:23] a general-purpose technology has come out in human history. All the way back, by the way, 5,000 years ago, from the
[4:28] emergence of the bronze chisel, which allows us to defeat friction by creating a wheel and an axle, through to
[4:34] electricity and the discovery of electricity, through to the silicon discoveries, through to cloud, now
[4:40] through to AI. Let's look at this first point. Anyone remember incandescent light bulbs? Of course we do, right? We
[4:46] all had them. Terribly inefficient, weren't they? So, what do we do? Replace for an LED light bulb. Watch our
[4:52] electricity bills go down. Anyone feeling their electricity bills gone down right now? No. Because what do we
[4:58] do? We put these things everywhere. LED lights everywhere. And guess what? Your electricity bill goes back to where
[5:04] it was. This is Jevons paradox. Whether it's the price of electricity, whether
[5:10] it's the usage of coal, whether it's the usage of factories — every single time we've seen this play out, the explosion
[5:17] coming out the back of it is dramatic. So don't for a second think that software is set at this level. Oh no, no,
[5:24] software is going through the roof and beyond. We are getting to disposable applications.
[5:30] We do not want this as leaders, right? We do not want this — control
[5:37] is still important. We're accountable for what our teams are doing. But — and this is the conversation, the
[5:44] real fear conversation I've had in the last five or 6 months since these goal-based agents come out — could 6
[5:50] months of seed funding and 30 engineers and an Anthropic frontier model replace your business entirely?
[5:57] Because if you look at it, these moats that we previously had — workflow embeddedness, software scale,
[6:03] integration lock-in, engineering complexity — I have hid behind decades of technology that I've built before going,
[6:09] "you're not going to be able to come after me. I have a lot of IP locked in the software I've built." Wow, that just
[6:15] changed, didn't it? What truly matters now? Compounding
[6:20] proprietary data. Network effects, regulatory permission,
[6:26] capital at scale, physical infrastructure for your team. The meta-moats the same: time that can't be
[6:33] parallelized. I have had conversations with banks that are thinking of
[6:38] expanding their branch network again. Who would have thought it? Because that
[6:43] suddenly differentiates their business. So for you as business leaders, those
[6:49] five things are really going to matter. And by the way, if you want to take pictures, some of these slides are dense. I've tried to simplify them. So
[6:56] have your camera phones ready if you want to take pictures as you go. So this reality check, this quote from William
[7:02] Gibson — "the future is here, but it's not evenly distributed" — has never been more true to me.
[7:07] Never been more true. And then many of you may have seen this report that came out from MIT NANDA, and you can argue
[7:14] about the statistical breadth which they took on, but still look at this
[7:20] title that sort of grabs your attention: "Despite 30 to 40 billion in enterprise investment to GenAI, this report uncovers
[7:27] a surprising result, and that 95% of organizations are getting zero return."
[7:33] Ouch. So when you actually look at why 95% of
[7:38] AI pilots fail — lack of workflow alignment, and I'm going to talk about the ability to focus at a workflow
[7:44] level being the difference between success and failure. AI bolted on is
[7:50] going to fail, and Phil talks a little about that. Wrong targets: companies aiming at sales
[7:56] and marketing high visibility instead of back-office operations where there's higher ROI are going to struggle. And
[8:03] then missing integration: pilots stay as demoed, never connected to actual business decision flows. Pilot purgatory,
[8:08] for goodness sake. And this is why you get some of these shocking stats at the bottom of the slide here. And yes,
[8:17] proof of concept almost four weeks. But hey, do you know what? Works on my laptop.
[8:24] This is not where you want to be. So what do the 5% do differently? They're picking one point and executing
[8:30] well — implementations that adapt, involved, customized, and specialized for critical
[8:36] tasks. Right team composition — and I'm going to go deeper on that — and
[8:42] integrated into real business decision flows from day one. It's got to matter. Nobody cares about a proof of concept on your executive committee.
[8:48] They care about a business outcome. We always have.
[8:53] And then this paper came along from Nvidia, and this drove a lot of people to think, "hmm, small language models are the
[9:00] future of agentic AI." I don't expect you to be able to read the subtext. So surely I need to go and create my own
[9:05] models to do generative AI or agentic systems? And the answer is yes and no.
[9:11] Yes, if you have specific tasks — and we're absolutely ready to help you with that with SageMaker AI and Amazon Nova
[9:16] and the Forge, very happy to help you do with that. But this has sent some people to an interesting place and not
[9:23] always the right one, because you've actually got to put the economics first. The economics first. So let's have a
[9:30] little look at what's going on. This shows you the cost to train a frontier model going back the last few years all
[9:36] the way from a transformer back in 2017 costing $900 all the way to those frontier models we suspect costing that
[9:43] much money to train them. That's a lot of money, and this requires a big team of
[9:49] data scientists, data experts, model enthusiasts, fine-training. You're taking on a lot of responsibility when
[9:55] you train a model. You're creating that model for a long time. It's a bit like a puppy at Christmas.
[10:01] It's for life, not just for Christmas. And then conversely, the cost of
[10:07] inference to access these frontier models has dropped, dropped.
[10:13] So the decision that you have to start with when you're looking at workflows is economic.
[10:19] And interestingly, think of it like this — and this is a new mental model —
[10:24] you are going to have to use some things. Of course, you're using a sundry of software solutions right now, and I'm
[10:30] sure all of those software vendors are rightly coming to you going, "we have the answer to your agentic AI woes, just use X,
[10:37] Y, and Z," and there's going to be an absolute legitimate case for you to do
[10:42] in scenarios. So this *use* is really important. But conversely, you are a
[10:48] specific business that has a specific unique selling point. You're going to want to *compose* agentic solutions.
[10:54] You're going to want to use those frontier APIs — the OpenAIs, the Anthropics, the AWS. Of course you are.
[11:02] Absolutely. And actually, this is where I see around 80% of my customers choosing to build the agentic solutions
[11:08] right now. They don't want to train those models. They just want to hit the frontier model. And whether they're
[11:13] using Haiku, the small model, or Sonnet or Opus 4.7, available just this last few
[11:18] days, that's what they're choosing to do. And then if you need to build —
[11:24] if you have an edge case where you need special latency, special knowledge to be fine-tuned into
[11:30] a model — absolutely, fill your boots. And as Francesca talked about this morning,
[11:36] Amazon Bedrock AgentCore we believe is there to help you achieve your goals in
[11:43] regards of the containment, the simplicity, the security, the observability that you're looking for.
[11:49] But day one, we're seeing that that frontier model does a lot of things. And
[11:54] the risk of building your own with that training curve still going up is: have you built something where a frontier model can actually give you an inference
[12:01] cost which is cheaper than you maintaining that model. That's why it's an economic decision first and foremost, and the team
[12:07] to go and build is very different to the team to compose, that's very different to the team to use.
[12:14] Let me show you an example of three customers I've worked with: a recruitment platform. They are using orchestration
[12:21] and comms from their existing vendors for both email and phone. Absolutely they're happy with the agentic solution, but they
[12:27] also use the frontier models to do application matching. Now this has been done for a long time with machine learning, but they wanted to move to an
[12:33] agentic system. So they used resume-to-job matching. The
[12:39] frontier model returns a pass or fail of 90%. Haiku really good at this. But at scale they realized they could do it
[12:45] cheaper by taking those results and building their own. So that's what they did. Customer service: queueing, Connect,
[12:51] amazing agentic AI solutions. But again, this customer wanted the hard stuff to go to a frontier model, and then
[12:58] eventually wanted to do sentiment analysis at scale across all of them. And for cost-effective service, they built their own model.
[13:05] Supply chain optimization — you get the idea. So optimizing the economics and
[13:11] understanding that as a leader is really, really important, really important. One of my personal agentic
[13:18] AI systems, by the way — I used 12 Opus agents, did a run, it consumed 2.1 million tokens, cost me 45 quid, one
[13:26] run. That isn't going to scale when you've got millions of customers. So things
[13:31] like batch optimization, caching, really important here. So the economics is a
[13:37] good thing to answer first. And then we're seeing a huge change in
[13:43] the data space across this. So where data engineers used to build integration
[13:48] pipelines, they're now ensuring source systems are clean. Because if your data is not clean — and a
[13:56] lot of data systems are now being built in Python — if you're not building a Pydantic layer to make sure that data going into the agent's correct, expect
[14:03] problems. Data going in, you're going to get a bad call. You're going to get an agent echo. Bad things happen.
[14:09] So yeah, your data's got to be clean and curated. Under *compose*, data engineers were building RAG pipelines and vector
[14:16] databases. Well, that goal-based agent can now write that better than they can.
[14:22] Now, context is king — or queen, depending on who you are.
[14:28] That is important. The ability to help an agentic system understand the relationships with the data in my
[14:34] experience is everything. Moment you've got a problem, you've not given the context. One really simple answer for you here. I
[14:40] was working with a financial customer building an agentic system. They assumed that an ETF that tracks the price of
[14:45] silver would understand the price of silver. No, not unless you put that into context. The agent won't, and it will
[14:52] get really confused on the two prices. All the way through to *build*, where data engineers create training sets — they're
[14:58] now composing data to help you train data automatically from whatever that frontier model has done. So this is
[15:04] changing across the board, but the lessons for us in data are still consistent. Every data should have a
[15:10] business owner. Clean unique data advantage is your competitive advantage.
[15:16] Data engineers are becoming context architects, and monitor data quality, not just data flow. Put the controls in for
[15:23] it. This is not just a case of connecting it to a SQL database. And this slide is important. I hear
[15:29] somebody on the previous question asked about pricing. There is no credible model that I have been able to find
[15:36] right now for monitoring and measuring NPV or ROI prior to going into this,
[15:41] because the simple fact is you cannot at the front end understand where you're
[15:47] going to save the cost, how the data is. You can't verify that at the start of a project. You would spend three or four
[15:52] years trying to evaluate that and get nowhere. And without a reliable framework, things aren't being approved.
[15:59] What I have seen work, both at Amazon and with my customers, is working closely with the CFO office. Embed a financial
[16:06] analyst with that team. Have them understand what the opportunity cost is with time saved, with data sets, with
[16:14] decisions, with outputs. Hour by hour, the scope is now incredibly flexible on
[16:21] what value can be achieved. And for us as leaders, we've got to know then — are we pivoting or persevering an idea
[16:27] really, really quickly? Because the truth is, as it's been
[16:33] mentioned already, we're moving from builders to orchestrators — not just for our team, but for ourselves.
[16:40] This goal-based agent has really disrupted things. And the Schumpeterian
[16:47] disruption cycle does not stop for anybody. So, what's happening in the
[16:53] world of talent right now? Well, Martin Fowler, a big fan of mine, he coined the term "strangler fig" pattern, for
[17:00] those of us that deconstructed monolithic applications before. He has a really interesting post on expert
[17:06] generalists, which I love. Now, all of us in the room have tenure and experience, otherwise we wouldn't be
[17:12] in this room. We've stepped on those mistakes. We've learned from those things. It actually makes us pretty
[17:18] powerful domain experts in knowing what a secure, available system is. We
[17:23] actually make pretty good builders. It was interesting on the panel this morning — that individual that built his own home control system. I guarantee he
[17:28] learned a lot doing that with one of those building agents. And this is what's happening. So domain
[17:36] experts are pushing outward. Generalists are deepening their domain
[17:42] expertise. This is leading towards this "renaissance developer" as Werner Vogels talked about
[17:49] it in his final keynote at re:Invent last year. And you see this playing out. Anthropic
[17:57] had a competition in this last few months. Look who won.
[18:04] The second place person was a cardiologist from Poland who built an AI agentic care platform that guides
[18:11] patients after they leave the doctor's office. He built that. He knew
[18:17] what was wrong. He had the insightfulness to use a goal-based agent
[18:22] while he was flying around the world with just Wi-Fi to build this. Look at the first place — a lawyer. Look at the third place, a cardiologist. Look who
[18:29] wasn't on there: a developer. Wow. So think in your business — who has
[18:37] the domain knowledge? Who has the domain knowledge?
[18:45] We're moving from a world where we had specialist squads that we used to put together based on the business outcome
[18:52] we're trying to achieve, with a diversity of skill sets,
[18:57] to a world that is starting to look a little bit like this.
[19:03] Generalists, often software engineers who now have a deep understanding of a business outcome, a process, or domain
[19:09] experts reflecting inwardly to now look at orchestrating that entire workflow.
[19:16] Not *own* — orchestrate alongside business process experts.
[19:22] Often I see lawyers dropping into these teams when they're doing it alongside
[19:28] those tenured software architects that have guided you, and becoming a team in their own right to instantiate this — make
[19:35] it real. But before you rush here, there's another reality that's occurring.
[19:43] Some really interesting patterns. Let's start on the left here. This was a team called Project Mantle in Amazon Web
[19:49] Services where we wanted to fundamentally rearchitect the layer underneath Amazon Bedrock.
[19:56] We thought this was going to take us a long time, maybe even a year and a half. And Anthony Liguori, one of our VP distinguished engineers — we have
[20:03] only a few of these folks in AWS, of course, our most tenured engineers — along with what we call level seven principal
[20:10] engineers, again some of our most senior engineers who have proven sign code, came together and shipped it in 76
[20:16] days. These are people that know what exceptional quality of code looks like. They do the code reviews. Look how it
[20:23] supercharged them in their delivery time cycle. But the bottleneck is shifting.
[20:28] It's not execution now. It's decisions. It's product management. And for a long time, for 30 years in my
[20:36] career, it has been the long tail in getting things done. Suddenly, we're seeing that invert. So our domain
[20:42] experts and our business-leader colleagues aren't ready to make decisions. If you don't know what you're doing, and
[20:49] you're just arbitrarily accepting code, then we're starting to see more vulnerabilities creep into it if you've not got the right support around it. And
[20:56] for those newer folks, they don't understand what they're shipping. And that is why, when you heard
[21:01] Francesca in the keynote this morning talk about security agent and DevOps
[21:06] agent — these are the companions which are going to go into those teams to remove that heavy lifting so they can
[21:13] focus on the domain expertise. They can continue to accelerate their
[21:18] static and dynamic security code reviews. They can accelerate their pen testing. They can accelerate their MTTR
[21:24] to finding out the skills, because for all of us who looked at that two-person team, they recognized a huge problem and I did straight away — on-call.
[21:33] Now I've looked after many on-call teams in my career, and when a team used to get to four people for on-call, I used
[21:39] to really start to worry, because you get one person ill, one person off on holiday, maybe another person off on holiday —
[21:44] that one person left isn't having a fun time. We haven't fully thought this out or
[21:50] solved this yet. I don't have all the answers. I just want to share the trends. But we are seeing a dramatic log
[21:57] analysis improvement in Amazon. You know, detecting that signal from the noise. I mean, just look at some of
[22:02] these — SecOps engineers used to spend 6 hours analyzing logs, now only 7 minutes.
[22:10] 50x productivity lets them detect and respond to threats faster than ever. We
[22:16] monitor 400 trillion network flows per day, looking for those patterns. So for us,
[22:24] extracting that signal from the noise from the humans — and by the way, that's only going to grow — is really important.
[22:31] So when we think about jobs declining, bear all of this in context. We still know that P0, P1, P2, P4, P5 — humans
[22:39] are going to be involved in those higher incident limits than they still are right now. The human in the loop is as important as ever.
[22:48] But we do see this changing the operating model. We've gone from this pyramid that we've all seen for years
[22:54] through to people trying to put managers or people in charge of agents. I haven't
[22:59] seen this working really well, because those domain experts need to understand
[23:04] that orchestration flow of what's going on. I do see this occurring.
[23:10] These seniors are 20x-ing their productivity, and we're
[23:15] cutting back on the juniors. I would fight this. I would say here is
[23:21] where we're actually going — where we've got to actually look towards the hourglass organization. We have to keep
[23:29] looking at bringing in the juniors,
[23:36] because sadly right now we do have a bit of a junior hiring crisis.
[23:41] 73% entry hiring level collapse in European tech according to Ravio last
[23:46] year's study. The 7% by the way of new grads entering big tech has dropped from 15%.
[23:54] 7.7% junior headcount decline, 9% employment growth
[24:00] in those senior roles. Now, I'm proud that Matt Garman said this statement, because all of us in this
[24:07] room, I think, remember the moment we got our first job opportunity — that first official "you've got the job." How
[24:12] good was that feeling when we got that? Would we deny that to the next
[24:18] generation? We've got to solve this. And I think we are and will, because we've
[24:24] got to — because every single revolution, by the way, in human history has shown us that jobs explode.
[24:31] Now all of us are going, "yeah, but this time it's different." Really? Is the data
[24:36] really showing that? Because actually when you look at us, suddenly you see the senior people's
[24:44] comp rising. The fastest-growing US top job title: AI engineer. 1.3 million
[24:51] new AI roles created according to the web. 67,000 open software engineer roles
[24:58] opened, and virtually 52,000 layoffs. So we are going through a job-family
[25:03] change. There is no doubt about it. Now I put this leveling on the board
[25:08] because I wanted to give you a little bit of an insight into how Amazon does this really quickly. So a level 4 engineer is typically a graduate-level
[25:15] engineer for us. Through to level 5, 6, 7, 8. There is no level 9 in Amazon.
[25:20] Jeff Bezos has eliminated it. Through to level 11. That's it, by the way. That's it.
[25:27] We have a responsibility to understand
[25:35] how to help those juniors go from here to here, and understanding — as that
[25:42] person asked the question in the previous session — how do we help them go through understanding those failure patterns, the responsibilities in their
[25:48] code? And we're trying in Amazon to figure that out, because if you stop training the juniors, where on earth do
[25:54] your seniors come from in 5 to 10 [years]?
[26:01] Now moving on to the organization. I've got some news for you here and you might have a complete health reaction to this,
[26:08] and that's fine. I'm just sharing what I'm seeing. If your organization looks like this, you're going to have a hard
[26:14] time with agentic systems. I'm sorry to say. Because the challenge here — the
[26:19] challenge here is that we're now bringing in line systems that aren't
[26:25] deterministic, and we have optimized for determinism.
[26:30] But in agentic AI systems, non-determinism is a feature, not a bug.
[26:36] And this path to high agency — we all understand what managing a high-agency individual looks like. This requires a
[26:41] leadership shift. And we've spent years building these
[26:46] toll gates — or should it be toil gates — to help these deterministic systems find
[26:52] their own path. But really, when you look at an agentic system, much like a river busting its banks, agents do find their
[26:59] own path. You've got to watch them, what they're doing. And I love this quote from Rory [Sutherland]: "Most business is
[27:05] probabilistic, but everyone in business wants to prove and pretend that it's deterministic. So every spreadsheet is in some ways an act of pretense, because
[27:12] it's past information which you pretend has wonderful predictive value."
[27:17] Nobody's been there, right? Have they? I have. So some principles before we move on to
[27:24] the penultimate section. Match your operating model to your growth stage.
[27:30] Put humans on judgment work, agents on execution work. And I'm sorry to say, if you still have
[27:38] engineering and operations as two different things, you are going to struggle with agentic systems.
[27:47] And here's why. Runbooks are deterministic. Agents are
[27:54] not. Ticket culture kills the context.
[28:00] No authority over the model. No ability to change anything. No authority over the data — feedback loop of death — leads to
[28:07] that statistic from the MIT NANDA report first of all.
[28:12] So what model does work? What model does work?
[28:18] What I'm seeing is this embedded pod model does work. So how it works: three
[28:24] to five engineers per pod. What is the business outcome? They're solving — workflow. Notice I didn't say product. I
[28:31] didn't say MVP. I said workflow. The hourglass strengthens it. Seniors
[28:37] already understand production. Agents are absorbing some of that junior work, but we've got to help those juniors now
[28:43] get to that senior level much faster. Understanding what the responsibility of security, durability, availability,
[28:49] regulatory looks like is really important, and we are only just now starting to solve that. By the way, I
[28:56] don't have the immediate answers for you. So yeah, some interesting different dynamics I'm seeing play out here,
[29:02] depending on the skill sets, depending on the country, depending on the workflow around the world that you're looking at.
[29:09] And that 3 to 5 million by the way is for the extreme end of building some models that I've seen some customers do.
[29:15] So yes, this model — looking at a business outcome — is where I see success working,
[29:23] and this team is now going to create that moving forward. They're going to use other agents to manage the on-call
[29:29] workload and assist them, relieving that burden. But here's the question. Once you get
[29:35] beyond three or four pods, then the real decision to allow this empowerment-in-action to actually take place is going
[29:42] to be on the platform that helps them across these dimensions. If you're any
[29:50] scale of 10 teams or beyond, because without a platform team you're going to have inconsistency of build. You're not
[29:56] going to have the observability which is crucial in any sort of regulated environment, or not even regulated.
[30:03] You need to know what is going on with these agents — with a platform team. Yeah, I'm getting
[30:09] one paved road. I'm still giving the empowered, and those platform teams have got to have absolutely really good
[30:14] emotional intelligence to empower those pod teams, not hold them back. So this
[30:20] is the model I'm working now. Many customers I've seen have gone, "well it's all right, we have site reliability
[30:25] engineering, we have SRE." Here's the problem with SRE: by the way, it works very well for Google, who
[30:32] are an exceptional company. They're a competitor, but they're an exceptional company because their SREs are the most
[30:39] senior developers that exist in Google. SREs are software engineers. They have
[30:46] really interesting responsibilities. But if you're just renaming IT ops to SRE,
[30:51] same skills, that is going to fail. And I have seen it fail with customers.
[31:00] So an embedded team model with the right platform supporting them — and that's not
[31:06] necessarily the platforms you have right now; in fact, it isn't. You're going to need supplementary ones. You're removing
[31:11] the friction from those pods. That's your focus. Not controlling the pods — removing the friction from those pods is crucial.
[31:19] And finally, governance. Governance. Everyone's asking me about it quite rightly. So, Tunisia touched on
[31:25] it with ethics. When we look at governance models around the world, there's only really one that I've seen a
[31:31] government produce right now which for me stands out, and that's the Singaporean model they announced this
[31:36] year at Davos. Simply four things: assess and bound
[31:42] risks up front, human accountability, technical controls across lifecycle, end-user responsibility. Pretty clear.
[31:49] And then when you start to look at how the different components actually map to that, whether it's identity management,
[31:55] deskilling prevention — it's not legally binding yet — multi-agent risk, and some
[32:00] of those five risk categories, we can start to map this to how actually businesses think.
[32:07] And when I looked at actually the Amazon tooling to actually overlay into that, I was pretty happy. I was pretty happy,
[32:14] because this is now actionable for our customers to overlay into it. And the
[32:21] final element when you really want to lock this down is policy-as-
[32:27] code. And as much as we've become experts at policy-as-code in CloudFormation and your controls and control
[32:33] objectives, we also see it utterly, utterly crucial in agentic systems.
[32:39] So to take it away — because I'm one minute over time — when we look at the economics, map your
[32:46] workflows to the tiers. Discipline. Measure the verification tax,
[32:52] because you do not want 2.74 times more vulnerabilities coming in to you. You want to get them down. You want to
[32:59] escape Model A. And for those of you that are still running in it, I'm sorry — it won't work for agentic systems.
[33:06] Implement that governance that's appropriate for you. Audit your seniority mix. Be prepared to bridge the
[33:12] gap from juniors to seniors, and protect that junior learning path.
[33:20] Now, I'd like to invite a customer to stage now who's going to share their journey, and then I'm going to open it
[33:26] up to some brief Q&A. And one of these customers who's been dealing with these challenges for real is Brooklyn
[33:33] Solutions, a UK scaleup that's been quietly building AI-powered supplier management for some of the most
[33:39] regulated organizations in the country, including the Ministry of Defence, Danske Bank in Europe. The kind of
[33:45] customers who do not accept "it'll probably work." Here to walk us through their agentic AI journey — what worked, what
[33:52] didn't — I'm happy to announce the chief technology and marketing officer to stage, Nick Francis. Nick.

## [33:52] Nick Francis (Brooklyn Solutions)

[34:10] Thank you, Jonathan. And good afternoon to you all. As Jonathan said, I'm Nick Francis. I'm a co-founder and
[34:17] chief technology and marketing officer at Brooklyn Solutions. Brooklyn is a supplier management platform. We focus
[34:24] on helping organizations deal with their commercial agreements and all the risks
[34:29] and delivery that goes along with that at scale. We work in financial services,
[34:34] across defense and energy sectors, to name but a few. Prior to Brooklyn, I
[34:39] spent 20-plus years working in organizations similar to Jonathan — Barclays, Lloyd's, Commerce Bank. So
[34:46] I've been on both sides of the fence as a buyer and a product builder.
[34:52] Our journey with AWS started eight years ago when Brooklyn was born, but our journey with AI started around 3 years
[34:59] ago, and we went through a number of phases in looking at what it could do for us and our customers. We started
[35:05] with basic use cases such as, as you'd expect, document summarization, formatting, extracting key points from
[35:12] larger texts, essentially making our application smarter. Phase two, we went on to looking at
[35:19] agentic AI from a conversational perspective, and we gave birth to something called Ask Brooklyn, which
[35:25] essentially is putting a bunch of bots in our application that's backed off to a number of large language models so
[35:31] they could be naturally language-queried by the users. Phase three moved us into agentic AI
[35:38] where we started coupling up that intelligence with the capabilities of the platform,
[35:45] and the agents being able to actually execute within the software. And phase four is where we're heading, which
[35:51] is on to a multi-agent agentic AI solution. By doing the previous steps,
[35:57] what we were able to do is come up with a rich set of use cases that really lend themselves to agentic AI — from contract
[36:04] intelligence, risk, supply management, coordinating together. We never had a
[36:09] grand plan. Each phase found its way with the previous one, finding out
[36:14] things for us and use cases that could work better. What we had initially was — we moved from
[36:20] the old way, which is the first two steps and phases we were in where we used to push information into what was effectively a steel box into an
[36:26] intelligence to get output out and use that across the application. But the new
[36:32] agentic way we're leaning into is actually teaching what was in the box — how to use our application for us —
[36:38] through APIs, endpoints, to actually shift and do a step change from advising
[36:43] into the agents being able to act on behalf of the users.
[36:49] Jonathan spoke about data and context, and we learned that lesson the hard way. We assumed naively out the gate that we
[36:56] could hook up the AI and the large language models of all sorts to our
[37:01] standard SQL database in the application. How wrong we were. That database was built for development. It
[37:09] was built for an application that has a lot of overlay and UX and information for the user to use it. So the large
[37:14] language model couldn't make a lot of sense out of it. And the responses it gave were weird at best.
[37:20] As an example, we have a segmentation system in Brooklyn which essentially just buckets suppliers from critical to
[37:26] non-critical. In that table in the database, it essentially says numbers 1 to 5: critical, important,
[37:33] transactional, etc. What we've had to do now, as we've learned the hard way, is add context to all parts of the database
[37:39] as to what constitutes a critical supplier, what governance a critical supplier is expected to go through. And
[37:46] by doing that on an iterative basis across the database when delivering our use cases, we get much better results
[37:51] from the AI — to the point that AI started giving us things that we didn't even expect. They started to combine tools
[37:58] and use things across the platform that we had no idea they would do. I think the rule here is: don't wait for perfect
[38:04] data. Start with what you've got. Start with a use case and iterate on top of your data on those use cases to get to
[38:11] where you need to do to know. From a team perspective — building the solution, we've had to
[38:18] adapt. Traditional development was: we'd spec something out and then work on it for 3 to 6 months, knowing exactly where
[38:24] we'd end up. Now we've got a partner in the AI and the large language models.
[38:31] You can't have that kind of determined outcome when the models themselves are evolving outside your team's remit. So
[38:38] what we have to do is more sandboxing, piloting, more experimentation, more feedback loops, more iteration within
[38:44] the development cycles to play for that unknown. And sometimes, like I said, it surprises us — it goes both ways. It has
[38:51] the ability to do things we didn't expect at a benefit level, but also sometimes to things we didn't want it to
[38:57] do. And then we have to tune it. We have to manage that through things like Bedrock Guardrails. We define
[39:03] boundaries which the agents operate in through the prompts as well. We ground our data in reality,
[39:13] and we make sure that's effective. What we've gone from is builders to orchestrators. So everyone in Brooklyn
[39:21] that's a developer, and in all other teams, have been asked to work with agents and build their personal team and
[39:28] functions with including AI as a resource in that team. We look at it at a task level, not
[39:36] a whole process level. Does AI genuinely improve the situation, or is it AI for
[39:41] AI's sake? And then we right-size it to the agent. We build for reuse, using the
[39:48] same pattern over and over again. So we have examples of agents that review and recommend and work across different
[39:55] context as the data changes. This mental model leads to mixed teams
[40:00] where we're pairing people with agents. The same principle in building effective
[40:06] human teams is applied, but including the AI.
[40:13] From a product perspective and what we do with our customers — we work in a regulated environment. We make sure that human-in-the-loop is very much a reality of
[40:20] what we have in the platform, and Jonathan mentioned it. We essentially always have a human start the work and a
[40:28] human end the work. But we may have agents of all different sorts in between that taking place doing steps that are
[40:35] now highly automated that weren't to begin with. But what that makes sure is the human themselves are still
[40:42] accountable for the work that gets done. We work with regulated clients. They need that accountability. So we make
[40:47] sure that's a deliberate design choice that we don't automate everything end to end. The benefit is though now with
[40:54] AgentCore, we start getting observability — the ability for what agents do is logged,
[41:01] triggered, looked at from a curation perspective, a cost — and every
[41:06] token is accounted for. Within Brooklyn we have a concept of the
[41:13] 5x expectation. We're not holding managers and teams to this as such, but the 5x expectation is
[41:21] for them to get five times the output for as little as 25% increase
[41:27] in opex. Now, you're not going to be able to do that in people. So we're asking them to fundamentally look at the
[41:32] way that they're doing things and increase that output to 5x where possible by using a series of tools and
[41:38] agents, rather than getting in people and personnel and how they'd scale a business. In that regard,
[41:47] we keep it honest. So we have quarterly executive reviews where we look at what we delivered, what we learned — back to
[41:54] the point of regularly getting together, regularly testing, regularly iterating
[42:02] internally. And the way we work with our customers at workshops is to help them find their initial use cases. And we do
[42:08] that on a way of looking at a combination of frequency and variability — where we find tasks that are in
[42:16] processes that happen a lot that aren't really that variable. So they have a
[42:22] known output and a known format. We mark them as something that AI is
[42:27] perspectively good to do or good to look at. How we do that is we sit down with
[42:33] subject matter experts from all departments and all divisions, and typically within your businesses you'll find these people as well that just
[42:40] through conversation they'll tell you these things that are mundane, high-frequency, not that variable, that happen
[42:47] day in, day out. That starts you identifying your use cases that you can
[42:52] go after on a volumetric basis, and where your biggest benefits will be.
[43:00] So in closing — momentum beats perfection. In Brooklyn, we had no grand
[43:05] strategy, just a basic use case that we learned from, and we built from there.
[43:11] We've got a backlog of over a hundred now, but each phase revealed itself as the next one closed off.
[43:18] The mantra, as it says on the slide: momentum beats perfection. Don't over-plan it. Don't wait for perfect data.
[43:25] Don't wait for the technology to settle, otherwise you'll miss the opportunity. So for you guys in the room, if you
[43:32] don't know what AI can do for your business, start to find out.
[43:39] And the only way you do that is get started in a small part of the business at the right level with the right level
[43:45] of detail in the lines that I just mentioned. Thank you.
