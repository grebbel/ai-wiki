---
title: "A leader’s guide to advanced team structures in an agentic world | AWS Events"
video_id: O7u6myBRsns
url: https://www.youtube.com/watch?v=O7u6myBRsns
channel: AWS Events
channel_id: UCdoadna9HFHsxXWhafhNvKw
channel_url: https://www.youtube.com/channel/UCdoadna9HFHsxXWhafhNvKw
publish_date: '2026-06-12T16:32:26-07:00'
upload_date: '2026-06-12T16:32:26-07:00'
category: Science & Technology
duration: '31:36'
length_seconds: 1896
view_count: 7592
keywords:
  - AWS
  - Amazon Web Services
  - AWS Cloud
  - Amazon Cloud
  - AWS Summit
  - AWS Events
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
description: |
  As AI agents transform the workplace, organizations must adapt their structures and methodologies to harness new opportunities. The probabilistic nature of AI requires continuous iteration and intelligent oversight, creating new ways of working across business functions. To thrive, organizations must combine clear capability assessment with agile planning while leveraging their unique domain expertise and data assets. This keynote explores how leadership is evolving to meet these needs, covering new organizational models and roles that coordinate human-AI hybrid teams. Leaders will learn strategies for balancing rapid decision-making with strategic oversight, finding the optimal mix of centralized guidance and decentralized innovation.
  
  Learn more about AWS events: https://go.aws/events
   
  Subscribe: 
  More AWS videos: http://bit.ly/2O3zS75 
  More AWS events videos: http://bit.ly/316g9t4
  
  ABOUT AWS
  Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts. AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.
  
  #AWSEvents
notes: |
  Auto-generated ASR transcript (no manual track), light cleanup of proper nouns
  (Werner Vogels, Josephine Teo, Eloundou, O*NET, McKinsey, Claude, agentic, SREs).
  No YouTube chapters; flat transcript. AWS Summit executive-forum keynote.
---

## Transcript

[0:05] Well, good afternoon. It's a real privilege and an honor to be able to be with you this afternoon. My name is
[0:10] Steven Brovich. Um, I joined Amazon in August of 1999, almost 27 years ago, and a lot of the
[0:17] world has changed. I spent the first half of my career on the technology side of the business, but the latter half has
[0:24] been focused on people and culture because it turns out organizational culture is one of the primary reasons
[0:31] why organizations are successful beyond technology. I've spent the last two
[0:36] years had the privilege of working alongside Tom and a group of peers who are all former sea level executives
[0:43] leading large organizations through massive transformation. And our job is not sales. Our job is to come alongside
[0:50] customers and partners in their journey. Not because we think we have the answers, but as my boss likes to say, we
[0:56] really want our customers to make their own mistakes, not somebody else's. So today, I'm excited to share with you
[1:03] some of the insights that we've gained because over the last year, this conversation has shifted as I sit down
[1:09] with customers. They're no longer asking, should I be doing AI? The question now is how do we actually build
[1:16] teams that work in this new world? How do we organize? How do we govern? How do
[1:22] we protect what we've got while embracing what's coming? What I'm going to share with you today is a
[1:28] framework. There's four questions we're going to look at in order. Economics, talent, structure, and governance. The
[1:35] research that sits behind this is a combination of about a hundred executive conversations like the ones I have every
[1:40] week along with an Harvard Business study review sponsored by AWS on AI
[1:46] readiness and some internal conversations we've been having at Amazon as we work through AI across the
[1:52] breadth of the full stack. But before we get to that framework, I want to ground us in current reality. AI won't take
[1:59] your job. Someone using AI will. Now whether or not Scott Galloway is the
[2:04] person who originated this quote, it's stuck with Scott. And I think the reason it's stuck is because it's true.
[2:11] A lot of companies worry about AI as a threat. But the threat isn't the technology. The threat is the colleague,
[2:19] the competitor, that younger version of you that learned how to use this stuff six months before you did. Because
[2:25] here's the uncomfortable bit. AI doesn't have ambition. AI doesn't have a P&L
[2:31] target. that AI doesn't want your job. People want your job. Those people that
[2:36] are coming for your job, your team's job, or your company's competitive margin. Those are the ones who are
[2:42] successful are the ones who are already integrated into these tools into how they think and how they work. So the
[2:48] question isn't will AI replace me. It's am I moving fast enough to stay ahead of
[2:53] the people who are using it. Now I know that sounds dramatic. So, let me bring
[2:59] it back down to earth with a slightly less serious version of the same point.
[3:05] Look, every wave of technology has had a conversation similar to this one. When
[3:12] the tractor arrived on the farm, it didn't kill farming, but it changed who was useful on the farm. The same thing
[3:20] is happening to us now. AI isn't taking your job, it's changing what it means to
[3:25] do your job. And the people who figure out how to work with it, the horses who learn how to drive, they're the ones who
[3:32] get to stay in the barn. And by the way, I'm calling all of us horses in this metaphor, just to be really clear. Now,
[3:37] this is the joke, but let's look at the data because there's actually serious research right now that is coming out to
[3:42] tell us what is really happening in the labor market. Not what the headlines say, but what's actually happening. So,
[3:50] this is from Anthropic from March of this year. It's the first serious empirical study of what AI is actually
[3:57] doing to jobs. And what they found is going to surprise you. A lot of what
[4:03] gets written about AI taking jobs is based on theoretical exposure. What an LLM could do. Anthropic did something a
[4:11] little different. They combined three things. The O*NET database of 800 US job occupations, actual their own clawed
[4:19] usage data, and the Eloundou MIT exposure scores. And then they asked of all the
[4:24] tasks AI could do, which ones is it actually doing in work at scale. They
[4:32] call that observed exposure. The blue is the theoretical ceiling. The red is
[4:38] what's actually happening. And the gap is huge. Computer and math jobs where you'd expect AI to be furthest along,
[4:44] Claude just 33% of the tasks it could theoretically do. In office and admin
[4:50] the theoretical exposure is 90% but observed exposure is a fraction of that.
[4:55] Now the chart on the right is the one that matters for our conversation today. Since chat GPT launch in 2022 there has
[5:03] been no systematic increase in unemployment for the most exposed workers. None. What they did find, and
[5:11] this is the interesting bit, is that the hiring of younger talent into those exposed occupations has slowed by about
[5:18] 14%. Not a collapse, a slowdown. And it's the juniors who are feeling it
[5:24] first. So, who are the most exposed workers? Computer programmers top that list, then customer service, then data
[5:31] entry. And here's the surprising part. The most exposed workers are disproportionately older, more educated,
[5:38] and better paid than the average worker. The old narrative was that AI would come and replace the lower talent first. But
[5:45] the reality and the data says the opposite. This pattern is what we're going to unpack during the rest of this
[5:51] session. It's not mass unemployment. It's a reshaping. An entry level is
[5:57] where that reshaping is happening first. Now remember this slide when we talk about the hourglass organization.
[6:03] But let's shift focus to look at how agentic AI is impacting business strategy.
[6:08] Timelines are compressing. Tasks that would have required dozens of developers and a multi-year budget are now being
[6:15] replicated by a motivated engineer over a weekend. This
[6:22] is the scary slide. This is the question your competitors are asking right now.
[6:28] Somewhere a well-funded team of 30 engineers with access to a frontier model is looking at one of your product
[6:34] lines and asking could we do this at a tenth of the cost a tenth of the
[6:39] headcount and a fraction of the time and the honest answer for most of in this room is maybe possibly we don't actually
[6:48] know because we haven't done the work to find out now I can use AI to generate a product
[6:55] but a successful business is built on more than the product itself. The top row of this slide, those are the moats we
[7:02] spent the last 20 years building. AI is eroding all of them fast.
[7:08] The bottom row, those are hard to get. AI makes those more valuable, not less.
[7:15] Because the easier it gets to build software, the more value concentrates in the things that software cannot
[7:22] replicate. years of operations, decades of trust, things that cannot be parallelized, things AI can't speed up.
[7:29] So if the old moats no longer provide protection, then how should we be investing? Now there was a period of
[7:36] time where we thought the answer as we started and look at economics as part of our model. We thought part of the answer
[7:42] was small language models. It seemed that the idea was if you could leverage my proprietary data to build your own
[7:49] set of small language models that becomes your new moat. Now, Anthropic's research paper on the topic is a really
[7:55] good read. But when you b weigh the benefits of operating a small language
[8:00] model against the cost of building one, the economics paint the different picture. Training costs are rising 2.4x
[8:09] per year. At the same time, inference costs are falling 10x per year. The gap
[8:15] between those two curves, the pricing scissors is opening by 12 to 24x per
[8:21] year. What does that mean practically? It means that the cost to create a frontier model is now approaching the
[8:27] billions. Only a handful of companies can afford it, but the cost to use one is collapsing towards zero.
[8:35] So, is the answer never build? Well, not quite. We see three worlds emerging each
[8:42] with a different level of cost and differentiation. World one is use the
[8:47] endto-end managed solution. Somebody else operates the AI, you consume it. Highest leverage, lowest
[8:53] differentiation. World two is compose. This is where you leverage frontier APIs
[8:59] stitching together in your specific context. You bring the workflow, they bring the intelligence. It's medium
[9:06] leverage and medium differentiation. World three is build. You train or
[9:12] fine-tune your models. It's the highest control, the highest cost, and the lowest speed. Build is still a valid
[9:20] option, but it should only be used in the places that truly differentiate your business. So, we've looked a little bit
[9:26] at this model so far, and what we see is actually these workflows cut across the
[9:33] worlds. Don't try to live in one world. Let economics and your actual
[9:39] differentiation drive which world each part of your workflow lives in and you'll naturally evolve. Day one, maybe
[9:46] the frontier model does everything. Month six, you learn the economics. You move some shifts to use and some to
[9:53] compose. By year two, the high volume, high differentiation stuff moves to build. This is the healthy path. The
[10:00] unhealthy path is the one where a leader says, "We're a build shop on day one and burns the company trying to train models
[10:07] before they understand their own workflow." So that's the economics that can guide our decisions in our strategy.
[10:13] Let's take a look then at the impact on talent because that world is changing as well.
[10:19] For 30 years, being valuable in tech meant being able to build the thing,
[10:25] write the code, design the schema, ship the feature. That was the craft. That was the career ladder. The craft is
[10:32] changing. The people who will be most valuable in the next 5 years aren't the ones who build the fastest. They are the
[10:38] ones who orchestrate the fastest, who can point an agent at a problem, evaluate the output, steer the next
[10:44] iteration, and know when to overrule. That is a different skill set. And most
[10:50] of us, including me, haven't retained for this new world. This shift is
[10:55] exactly the shift that Martin Fowler and his colleagues at ThoughtWorks talked about in their July 2025 article. He
[11:01] calls that orchestrator archetype the expert generalist and identified seven key characteristics including curiosity,
[11:09] collaboriveness, customer focus, and understanding of first principles. Why does this matter? Because these seven
[11:15] characteristics are exactly what agentic AI amplifies. An agent multiplies a curious person. It
[11:23] doesn't multiply someone who only knows one framework. An agent rewards deep fundamentals, not surface level
[11:30] certification collecting. So when you're hiring in the new world, and this is important, hire for these seven,
[11:38] not for the framework of the year because that framework will change three times before this person's first
[11:44] performance review. What this is doing as AI then enters the team, the specialist, your deep domain expert gets
[11:52] pushed to broaden because their specialty isn't enough anymore. They need to understand adjacent domains.
[11:58] They need to explain their work across boundaries. They need to orchestrate. Your generalist, your breadth player,
[12:05] they get pulled inward because AI gives them the superpower of specialist level depth on demand. They can ship domain
[12:12] specific work they couldn't ship before. They meet in the middle and what emerges
[12:18] is what Werner Vogels called the Renaissance developer. Whether it's Werner Vogels, Martin Fowler, Jurgen or PWC,
[12:26] everyone's converging on the same answer. The valuable human in the loop is the polymath with steering hands. And
[12:34] that's the opposite of what we have hired for for the last 20 years. And let's make this concrete. This is from
[12:40] Anthropics Build with Claude hackathon from February of this year. 13,000 applications from around the world. 500
[12:47] of those were accepted. 277 shipped production code. 21 million lines of
[12:53] code were generated in here. Third place. Third place. Dr. Mikall Nettoko,
[12:59] interventional cardiologist, MD, PhD, not a professional developer. He built
[13:04] an AI platform for post-appoint patient care in 7 days. coded it in the hospital
[13:10] between patients and in the cloud flying from Brussels to San Francisco. First
[13:15] place a lawyer built a permitting tool for California called Crossbeam. Also
[13:21] not a professional developer. Now stop and think about that. The top three finishers in Anthropic's own flagship
[13:29] hackathon were not professional developers. They were domain experts and they beat
[13:36] 13,000 other people, many of whom had been coding professionally for years.
[13:43] The lesson here isn't developers are dead. The lesson is domain expertise plus AI beats coding skills alone. And
[13:52] the implication to your hiring strategy, especially for the next two years, is profound.
[13:58] The person who understands your customer, your regulation, your product
[14:04] nuance, who can now build because AI fills the gap. That person is gold. So
[14:10] what does this mean for how we staff our teams? The old world called for a team
[14:16] of specialists. Each one owns a lane. You got handoffs between them. There's coordination overhead. Classic
[14:21] enterprise team structure. The new world is calling for two or three expert
[14:27] generalists plus agents to fill the gaps. Each generalist doesn't own a lane. They own
[14:34] a workflow. They orchestrate a workflow end to end. Agents fill the gaps where specialist depth is needed. The
[14:41] coordination overhead collapses. The handoffs disappear. This is what I mean by hypercon convergence. And I'm not
[14:47] saying the eightp person teams die tomorrow. What I am saying is that the
[14:53] teams you build for new work will look like this. If your team still looks like
[14:59] the side on the left for new AI work, you are building yesterday's team. Now,
[15:04] let's test that ideal structure against four realities because there are four forces that are happening at once and
[15:10] they're not all pointing in the same direction. Force one, expert multiplier. Those of you that haven't heard about
[15:15] Project Mantle, go look it up. It's astonishing what a group of senior knowledgeable people can do with AI at
[15:21] their disposal. An order of magnitude increase in speed. Force two, the
[15:27] bottleneck shifts. The question is no longer can we build it. It's do we have the data and can we
[15:34] decide fast enough to keep up with what we can build. Force three, the
[15:39] verification tax. AI generates code 10 times faster, but it's three times
[15:46] harder to validate. The reviewing bottleneck eats the velocity if you're not careful. Force four, the deskilling
[15:54] trap. Juniors using AI can ship about 17% more code, but they understand 17%
[16:01] less of what they've actually shipped. The people coming through your pipeline are getting faster and less grounded at
[16:09] the same time. All four are true simultaneously. The leader's job, your job in this room
[16:16] is to hold the tension. Which leads us to talk about how we think about team shape and the talent pipeline. Let's
[16:22] look at four models for team structure. Pyramid. This is most of your organizations today. Lots of juniors at
[16:28] the base, pyramid levels, fewer seniors directing the work.
[16:34] Diamond. This is what happens when you overreact. You cut the juniors. We don't
[16:40] need them. AI can do the work. You bulk up the middle with more managers because we need someone to oversee the AI. You
[16:47] have a thin base, a thin top, and a flat middle. This is the trap. The inverted
[16:52] pyramid is what the new pod is emerging. Three to five senior engineers, each
[16:59] full stack, each with AI doing execution. The pod shape, and it works well for execution, but it's missing the
[17:06] learning path. The last shape is the hourglass and that's the learning organization.
[17:14] We have execution at the top, lean middle, and importantly
[17:20] juniors learning the craft on the way up. This is what I want you to walk around out remembering. The inverted
[17:25] pyramid is the pod that senior team with AI doing execution. The organization that houses them is the hourglass
[17:32] keeping the junior pipeline alive. Both are true at different levels of altitude. And this is why the hourglass
[17:39] matters because right now most organizations are heading toward the diamond. They're cutting the base and
[17:44] the data on that is brutal. Companies see reducing junior talent as
[17:49] the quickest path to ROI targets their boards are mandating from their AI investments.
[17:55] And the inverse is happening as well because the jobs aren't disappearing, they're bifurcating. Those same
[18:02] companies are frantically paying top dollar for senior talent and anyone with ERA AI in their job resume. Put the last
[18:08] two slides together and you start to see the emerging shape. The middle is hollowing out. The top is exploding.
[18:16] That's not a healthy economy. That's not a healthy talent pipeline. Which is why the hourglass matters. You have to be
[18:21] rebuilding the bottom deliberately. No one else will. Which brings us back to
[18:26] the central question. If you stop training your juniors, where do your seniors come from? In five to 10 years,
[18:33] the seniority pyramid inverts. AI absorbs the execution layer. What
[18:39] remains is judgment. But judgment only exists because somewhere someone spent
[18:45] 10 years doing the execution and learning from the mistakes. If we skip that entirely, we don't just have a
[18:52] talent pipeline problem. We have an expertise pipeline problem. and expertise takes a generation to build.
[18:58] Matt Garmin, CEO of AWS, put it plainly in a 2025 interview. He asked, "How's
[19:04] that going to work when 10 years in the future you have no one that has learned anything? My view is you absolutely want
[19:10] to keep hiring kids out of college." He's right. The companies who stop training juniors today don't have a
[19:16] talent shortage today. They have one in 2034, which is four CEO cycles from now.
[19:22] So, no current CEO has to worry about it. which is why this is going to be a massive problem and exactly why your job
[19:29] as a leader is to resist the short-term temptation to cut the base. Your competitive advantage in 2034 is the
[19:36] juniors you're hiring today, not the ones you're laying off.
[19:42] This is the tension we talked about earlier, and this is why holding the tension is the leader's job. So, we've
[19:48] talked about economics, we've talked about talent. Let's take a look at structure.
[19:54] And I'm going to start with the uncomfortable bit. What got you here is not going to get
[19:59] you there like at all. Look, this org structure was already cumbersome in the
[20:05] age of cloud. It fundamentally breaks in an agentic world. Not because any of the functions disappear, but because the
[20:12] boundaries between them dissolve. Security isn't a department with review gates. It's code running at the gateway.
[20:20] Architecture isn't a whiteboard exercise. It's the policies your agents respect at runtime. Foundation services
[20:27] isn't provisioning. It's defining the operating envelope for the autonomous systems. The CIO role itself is shifting
[20:35] from being owner of the stack to being conductor of the stack. And the people who can make that shift will run the
[20:42] next decade. But that shift comes with a challenge because today everything in
[20:47] our operating model optimizes for determinism, runbooks, change advisory boards, SLAs's with 59s, predictable
[20:55] outputs for predictable inputs. Our whole discipline is built around the
[21:00] idea that the system should do the same thing every time. And for 30 years, that was the right bet. But it's no longer
[21:07] the right bet because non-determinism is a feature,
[21:13] not a bug. Think about what you're actually asking an agent to do. You're asking it to handle cases you didn't
[21:19] anticipate, to adapt, to reason about the goal, not just follow the steps.
[21:26] That requires non-determinism. A deterministic agent is a runbook. We
[21:32] already have runbooks. We don't need AI for that. So the operating model has to
[21:38] shift and you have to become tolerant of variance in execution and strict about
[21:44] variance in outcome. It's a different thing. This is the single hardest mental
[21:49] model shift for the CIO in the room because your whole career has been about
[21:54] tightening execution. And now the discipline becomes relax execution,
[21:59] tighten outcome measurement and build guard rails around the things you actually care about, not the steps, the
[22:07] outcomes. Set the outcome, give the team the means, and resist the urge to manage
[22:13] the how. Because just like rivers, agents find their own path. If you tried
[22:18] to build a toll gate in the middle of a river, the river would find another way around. Your job is not to prescribe the
[22:26] route. Your job is to define the riverbank, what the outcome has to be, and let the water find its way. This is
[22:33] the mental model shift. And the practical implication is the organizational models we'll explore
[22:38] next. Model A, traditional IT ops. What worked for 20 years is now the
[22:45] antiattern. This is the model most organizations in this room are operating today. Engineering builds then throws it over
[22:52] the wall for IT operations to run. Two separate teams, separate objectives, separate performance metric. This model
[22:57] was already less effective with cloud. It fundamentally breaks in an agentic world. And here's the evidence. Six
[23:05] stats all from real research. One, runbooks are deterministic. Agents are not. Two, ticket culture kills context.
[23:12] A quarter of your incident time isn't debugging, it's assembling the humans who understand what happened. Three,
[23:18] your operators have no authority over the model. Most enterprises can't see what their agents are actually doing.
[23:25] Four, operators have no authority over the data. Threearters of the failure moats bypass your current telemetry.
[23:32] Five, 91% of ML models degrade over time. You deploy, it gets quietly worse.
[23:38] and six ITIL can't keep up. These six failure moats stacked are why 95% of AI
[23:46] pilots fail to achieve meaningful impact. Your operators cannot debug what
[23:51] they cannot see and they cannot see what they were never trained to reason about. Most organizations are sitting here
[23:59] right now. The first step is admitting it because you cannot fix model A by
[24:05] adding more SREs, more runbooks or more monitoring. You have to change the model and that's what models B and C are
[24:11] all about. Model B is embedded. You build it, you run it. The same three to five senior
[24:17] engineers build and operate the pod. Same team, same people, full stack
[24:24] ownership. And the results, multi-eployments per day, subhour recovery, 0 to 15% change
[24:31] failure rate. This is Dora Elite territory. Why does it work? Because the
[24:36] people who wrote the agents system prompt are the same ones debugging it at 3:00 a.m. No context gap, no handoff.
[24:44] They are production. But model B breaks at scale. And here's why.
[24:50] At two or three pods, you survive without a platform. Each pod makes its own choices. Each pod build its own
[24:55] guardrails. It's messy, but it's survivable. At 10 plus pods, the duplication kills you. Each pod builds a
[25:03] slightly different off layer, a slightly different observability stack, differently, badly, repeatedly, and the
[25:09] cost of that inconsistency, security holes, compliance gaps, a
[25:14] spiraling AI budget you can't get insight into, that outweighs the cost
[25:19] you were trying to avoid by building a platform. So model C is model B plus platform platform provides everything
[25:26] you need for agent infrastructure runtime memory identity observability
[25:32] it's consistent it's governed and it's shared but the key to getting C right
[25:38] is this the platform doesn't constrain the platform enables pods choose what to
[25:46] build which models to use and how to structure their agents and how to use their data full autonomy full accountability but the road they build
[25:52] on is the platform. So this is the structural decision distilled. Model A is dead. Full stop. If you're operating
[25:59] model A today, you have a transition plan to execute, not a strategy to debate.
[26:05] Choose between model B embedded pods with AI agents as first class platform citizens and model C pods plus a
[26:14] platform providing the shared infrastructure. At small scale, B alone is fine. at medium and large scales. B
[26:20] plus C. Model A is dead. That's the banner. Go back and tell the people who aren't in this room. We've talked about
[26:27] economics, talent, and structure. Let's wrap this up by looking at governance. And for that, I'm going to point to
[26:34] Singapore's model of AI governance framework for agentic AI. In January 2026 at Davos, Minister Josephine Teo of
[26:42] Singapore launched model AI governance framework for agentic AI version one from Singapore's IMDA. It's the first
[26:49] statebacked governance framework specifically designed for autonomous AI agents. Not a general AI governance
[26:56] framework, but specifically agentic. They published the first comprehensive model back in 2019. This 2026 version
[27:03] extends that to agents, and it's worth reading cover to cover if you're a CIO
[27:08] in a regulated space. Singapore's framework distills to four dimensions. Risk assessment upfront, structured
[27:16] before deployment. Two, human accountability chains. Every agent action is traced to a named human.
[27:23] Three, technical guardrails throughout the life cycle. And four, enduser transparency. Users have to know that
[27:31] they are interacting with an agent and they have to know the bounds of what that agent can do on their behalf. There
[27:37] are five things that make this framework stand out as distinct. One, it's the first framework to mandate agent
[27:44] identity management. Every agent has a verifiable identity before it can act,
[27:50] not a nice to have a prerequisite. Two, it integrates concrete testing
[27:55] frameworks along five risk categories building on the AI verify and global AI assurance pilot from 2025. It's not
[28:02] aspirational, it's operational today. Three, it explicitly addresses multi-
[28:08] agent coordination risk. When agents talk to other agents, and they will, what happens when they disagree, escalate, or
[28:16] find emergent behavior none of us planned for? Singapore has thought through this. No other framework has
[28:21] yet. Four, it's voluntary but directional. Singapore doesn't compel
[28:26] compliance, but if you want to do business with the Singapore government or in regulated sectors, this is the de facto standard. And last, it addresses
[28:35] the deskilling trap headon. We have to be able to show not just that we're using agents, but that we are using
[28:41] approaches that are continuing to train the people who will take over for us in the future. And this is the beautiful
[28:48] part. Singapore landed on four governance dimensions. Amazon building agent core launched on the same four.
[28:53] Convergent evolution, different teams, different continents, same answer. Four questions we have to answer before the
[28:59] agent acts. Who's the agent? Who authorized it? Two, what is the agent allowed to do? Three, is the agent
[29:06] performing as expected? And four, can we audit what it did?
[29:11] This is policy enforcement that's happening outside the LLM loop. That's the critical architectural point. You
[29:17] don't ask the agent nicely not to do something. You stop it at the gateway before the LLM ever sees the request.
[29:23] This separates who writes the policy from who writes the agent. Your security team owns the policies. Your engineering
[29:29] team owns the agents. Each one of them places a strength. This is what governance as infrastructure looks like.
[29:35] Not a policy document, not a compliance checklist. Running code enforcing rules
[29:41] every request every time. Remember, agents find their own path like a river.
[29:46] Policy is code is the riverbank. The agent can meander, but it can't cross the bank. So, what do you do Monday
[29:52] morning? What do you actually do? Six steps in order. Don't jump ahead. One, economics. Pick one workflow in your
[29:59] organization, not one AI strategy, one workflow, and answer, does this workflow
[30:05] live in use, compose, or build? Two, talent. Decide who's on the pod. Three
[30:12] to five engineers maximum. If you can't staff a senior only pod, you're not
[30:18] ready to build. You should either use or compose. Three, structure. Are you model
[30:24] A, B, or C? Answer honestly. If you're in model A and calling it DevOps,
[30:32] acknowledge what it really is. Escape. Four, governance.
[30:37] Five, people. Invest in your senior domain experts. Double down on that
[30:44] person who understands your customer, your regulation, and your product nuance, the things AI can't compress.
[30:50] And six, pipeline. Protect the juniors. Do not cut entrylevel hiring to pay for
[30:58] senior AI talent. Both are true at the same time. Seniors are more valuable.
[31:03] And juniors are your 2034 pipeline. You need both. Economics, talent, structure,
[31:10] governance, people, pipeline. Six steps. Answer in order. The whole deck depends
[31:15] on that single economics question. But the answer is per workflow. You'll use this framework many times, but it's the
[31:21] steps that will keep you sane. The companies that win in the next decade aren't the ones with the best AI.
[31:27] They're the ones with the best operating model around the AI.
