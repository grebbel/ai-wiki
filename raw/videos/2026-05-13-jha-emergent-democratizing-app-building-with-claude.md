---
title: How Emergent is making app building more accessible with Claude
video_id: IGAVa4uyo2w
url: https://www.youtube.com/watch?v=IGAVa4uyo2w
channel: Claude
channel_id: UCV03SRZXJEz-hchIAogeJOg
channel_url: https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg
publish_date: '2026-05-13T09:53:20-07:00'
upload_date: '2026-05-13T09:53:20-07:00'
category: Science & Technology
length_seconds: 999
view_count: 10995
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
description: 'Emergent reached $100M ARR in eight months, with 70–80% of users having never written a line of code. In this
  conversation, Co-founder and CEO Mukund Jha sits down with Anthropic''s Carly Ryan to talk about the technical decisions
  behind building on Claude and how Emergent thinks about durability in a category moving this fast.


  Read the full story: claude.com/customers/emergent'
keywords: []
chapters: []
---

## Transcript

[0:00] We are building for like small businesses today, right? Small businesses globally account for 70% of employment, accounts for like 50% of GDP of the world, right? But they've never
[0:07] had the tools to sort of really express themselves because like there are million niches in small businesses. But for the first time with AI, you can actually serve all of these million
[0:14] niches at zero marginal cost. And that's what we're trying to enable.
[0:20] Hi, my name is Karly and I'm on the applied AI team here at Anthropics, specifically working with startups.
[0:26] Today, Mukund has joined me. He is the CEO and co-founder of Emergent. So, Mukund, let's bring it back to the beginning. Emergent's growth has been
[0:34] one of the standout stories of this year. Why don't you walk me through your journey with YC, some of your pivots, and how you landed on the product that you have today?
[0:42] Thank you for having me here. Super excited to be here. So, I'm doing this startup with my twin brother, Madhav, and I actually started programming at age 12.
[0:49] Love it. We love We love sibling founders here.
[0:51] Totally. Then we actually like have been obsessed with this problem of automating software engineering from the beginning.
[0:57] Before this I was running a startup called Dunzo where I had a 500 people engineering team. And when we entered YC our first sort of insight was to automate software testing because I had
[1:06] seen in in at Dunzo that how software testing was the bottleneck for shipping software fast. And we started with this problem of like how hey how do we
[1:14] automate all of the software testing including mobile apps, web apps. And when we sort of started building that out, we realized that to automate
[1:21] testing, we had to build, you know, our own container technology, our own coding agents. And we stumbled upon this insight that if you can actually solve for the verification loop, you can actually make agents run longer. On the
[1:30] day one, we told our YC partners that, hey, like testing is great, but you know, we want to now build general coding agents. We were like almost like
[1:37] a applied research lab working just building, you know, high production grade quality agents. invented a bunch of things like test time compute. How do
[1:45] we sort of scale the memory across agents? How do we solve for agent to agent communication? We were one of the first team to productionize multi- agent
[1:52] systems. When we launched our first approach was to go to enterprise. We had an enterprise customer started working with them but realized that the adoption
[2:00] in enterprise is going to be slow. At the same time we started using these internal coding agents to build everything internally. In fact like there were like few nontechnical people in the team who were using it more than
[2:08] developers were at that point. And we truly realized that the power is actually to democratize software engineering for everyone. And that's when we in June
[2:16] launched this almost like a research preview. And that time agentic coding was not that popular. And when we launched it just took off and you know
[2:24] we were actually surprised you know everybody else at that time was building for front-end heavy applications. They were building for more demo kind of things. And B fundamentally approached
[2:32] the problem thinking that what would it take for actually anybody to ship production ready software that will actually have real use cases we'll have
[2:40] business critical apps running and our insight was to sort of automate all of this testing linting deployment security
[2:48] how do you solve for like code reviews and that actually like really really resonated with users because most of the users that who are coming to Emergent today are serious builders these are
[2:56] small businesses entrepreneurs who actually want to see an economic value from these software getting built.
[3:02] Yeah, that's awesome. So, it's like basically democratizing. It's taking natural language. It's for non-s software engineers, but it's also building durable products. It's not just
[3:10] for prototyping. It's really cool. So, you've been building on Claude since the really early days. We met about a year ago. What made that the default choice
[3:18] and what's kept that all the way through? Why have you stayed on cloud?
[3:21] Yeah, I mean I think we were almost lucky to get started when Sonnet came out and um and I think in AI I think every everybody needs to sort of imagine
[3:28] the world six months ahead and build for that versus building for what's available today. Imagine the world from the lens of what is available and what what's going to come next, right? So
[3:37] people who would have started with the previous generation of models would be solving a different problem versus us because for the first time like I think set
[3:45] instruction following so that you could actually really imagine what longunning agents would look like. It was really good at programming. it was really good at front end as well. Um, and so that
[3:53] actually like really gave us, you know, a little bit of futuristic view of what the world of programming could look like and what could agentic programming look like and our users are actually like comparing us against a dev shop, right?
[4:03] So they're not comparing us against like an IDE or a tool and to them outcome matters a lot, right? And so we are really really focused on what would give
[4:11] us the highest quality, what would give us the highest probability of getting to the right outcome versus a speed. Most of the other players who are focused on front end or design to them speed
[4:20] matters a lot but for us and our users what is important is that that are they able to reach the outcome that they want and that's why like opus has been sort of you know our our workhorse and and
[4:28] it's really great at instruction following and if you have the right tight feedback loops that we have been able to build using our multi- agent systems you can actually keep them
[4:36] running for a much longer time. Today our agents can run for hours trying to build the software and we we run like very tight evals internally and and of
[4:44] course like you've been really helpful in helping us. I know about your emails. For sure.
[4:47] Yeah. And I remember like, you know, when we were about to launch, we had this like 2 a.m. meeting just to get started on things.
[4:53] Totally. Well, I mean, so so a lot of your engineers are in India. So, one day when I was like, it was like Friday at 2 p.m. for for us and it was the middle of the night for you guys. And I was like,
[5:01] "Oh, of course they're going to answer the next day." And then one of your engineers was like, "Oh, yeah. Let's like let's get on a call in 15." And I was like, "Is it not the middle of the night?"
[5:08] So, your team during YC built this internal coding agent. Maybe you didn't know what it would become. What did you learn from that? and like what shows up today in the product and then maybe what
[5:17] are learnings that like you really scrapped. Yeah, I think our first insight was to, you know, to really really build an automated software engineering platform, you will have to
[5:25] own every layer of the stack, right? And you have to almost co- build the infrastructure to support your agent and an agent to sort of support the infrastructure.
[5:32] And at that time, everybody took the shortcut, you know, hey, what is the third party that is available? Let's use that. Uh when we started like there were no good container technologies. We had
[5:40] to actually invent and build sort of our own container technology on top of Kubernetes which does disc snapshotting, memory snapshotting. So you could actually save the states and run
[5:48] parallel agents. And for us what's been sort of really really insightful has been that agent is the product right in many ways and and like the harness
[5:55] quality really really matters and we sort of build this multi- agent system.
[6:00] We were one of the first teams to productionize it and many learnings including like how do you sort of save for memory? How do you do agent to agent communication? How do you do better
[6:08] context management? How do you effectively use caching to keep the cost down? Um, and tightening all the feedback loops from the container and all of the infrastructure that you have
[6:16] built like is really important. The other thing that really was important to us from day one was to own the entire stack because the last mile is where
[6:24] like most solutions trip. We spend a lot of time just to make sure that our production quality is really high and what you can see in the development environment is something that replicates
[6:31] in the production and today I think I think we're probably one of the deepest logs in app building space and that allows us to sort of compound our learning. for example, like a lot of the
[6:39] errors actually don't show up in the dev side. Like they'll only show when your app is live and real users are using it.
[6:44] We're able to pipe all of that back to our development environment and allow our agents to learn. We also have built this um what we internally call long-term memory where an agent is not
[6:52] just learning from within the user session, but is learning across all of the apps that are getting built. So first time it sees an error, a new error or a new library upgrade, it's able to
[7:00] learn that and and sort of, you know, do that in the next iteration in much less tokens with much more accuracy. So I think like building this co-agent and
[7:07] instructor together like has been really really helpful for us and I guess because you own the whole stack like up to the hosting as well that gives you kind of all this
[7:15] proprietary data that you can feed into the next parts of the agent and the future of the agent.
[7:19] How do you think about model selection especially when your users can't debug the output? I mean a lot of the burden lies on us today right like to make our users successful and we take that very
[7:27] very seriously and and that's what we are sort of like extremely obsessed about like how do we get users success couple months back our like you know deployment rates were 84% now it's it's
[7:35] closer to 98%. So 98% people on the platform were able to build something are able to deploy to production. That's that's been amazing and that that's just tightening all of these feedback loops
[7:44] making sure that you know your agents are extremely reliable and self-learning. In terms of model like the way we think about it, we are getting compared to a dev shop, right?
[7:52] So when a user comes to us they're comparing us to like a $250,000 price point uh that they would have paid if they had gone and and hired a dev shop.
[8:00] So they're not price sensitive. They're also not like latency sensitive that much because they're comparing us to a 3 months project that would have been executed outside. Uh so we are very very
[8:07] obsessed on the quality of the product and not so much about the cost as much.
[8:11] And so for us like being on the frontier the the highest reasoning possible is is something that we sort of index a lot on internally. We index a lot on like just
[8:18] highest quality output versus you know the fastest output.
[8:21] And we're not not trying to oneshot a solution. We're trying to you know build really really reliable production ready system that can be iterated upon.
[8:27] instruction following should be really good because the error sort of compounds and even small sort of errors as you run 10,000 steps like they they compound very quickly. Totally
[8:35] and because the outcome matters the most, right? So we sort of you know rely on the best possible models for reasoning and coding abilities.
[8:42] Yeah. Yeah. I think that's been a through line that I've observed with you guys where it's like you really put accuracy top and like that's why you've
[8:49] had so much success. So this is a question we ask our founders often. The AI builder space has gotten a bit crowded. So curious to hear from you.
[8:58] What has Emergent built that's genuinely hard to replicate?
[9:00] Yeah, I mean I think first of all like I I think we're beginning of a very very large market that's opening up, right? I think the market is actually growing faster than all of us can serve right
[9:09] now, right? And pie is getting bigger, way bigger, way faster than all of us can serve right now. So we are actually not so so much worried about like hey what is competition doing? You know what
[9:17] are labs doing? I we just generally think that the market is so big and it it's growing so fast that us being able to serve the customer that we want to serve is is generally sort of you know
[9:25] really really important for us on the technical side. I think like you know our approach has always been to sort of really really build very closely with the customer. So we understand our customer really really well you know
[9:33] what their needs are. For example they really don't care about you know demos front end prototypes. They care about like real production use cases. They care about third party integrations
[9:41] working. They care about payments getting through. They care about like you know authentication working. A lot of our users you know early on started uploading like really large files. So we
[9:49] had to sort of think about like hey how do we support large file systems on our production systems. They care about scalability. So when we write code we
[9:56] make sure that these code are written in a horizontally scalable manner. So as traffic grows the infrastructure sort of grows with them right for us like I think the technical motives one our sort
[10:04] of agent quality the harness quality is really really strong and it's continuously evolving. Second is all of the provided data that we are collecting right now, right? I think all of that
[10:12] feeds into our long-term memory, feeds into, you know, like our self-learning agents, feeds into our RL systems and because we are solving only for one
[10:19] stack, we are almost like a vertical agent for coding because our users don't really care about what technical choices is being made. So they leave that onus on us and we make the right choice for
[10:28] them and we are solving for just one kind of tech stack. So that allows us to sort of really really accelerate our sort of learnings on that tech stack.
[10:35] And lastly, I think the code generation is only 20% of the problem, right? Like the the 80% of the problem is actually how do you take it to the uh deployment?
[10:41] How do you make sure it's maintained in production? How do you make sure that security is really really high? And we are solving for all of those deep infrastructure problem where you know
[10:49] not only your code is written but does it work in the dev environment when it works in dev? Does it replicate in the production? Do you have the feedback loop? And solving for the full stack is like really really important for us.
[10:58] Yeah. Really cool. Yeah. Yeah, I think one of the like early differentiators I saw from you guys is kind of that third point, building durable, reliable apps
[11:06] that can be built on later. It's for actual like business owners and not necessarily just people prototyping. And so I remember in one of our early calls you were talking about you have your
[11:15] agent that initially builds the prototype or or the product, but then you later have another agent that comes back and cleans up the code and makes it such that people can build on it later.
[11:24] I mean we we take like code quality very seriously. So we have like refactoring agent that'll come and refactor your app. We have a post- deployment agent and a pre-eployment agent that'll check
[11:33] for all security flaws. They'll sort of make sure that there are no key leakages bunch of those things and sort of approaching the problem from you know the outcome first perspective right like
[11:41] allows us to sort of really design the system for that. What do you think are most defensible mode how like you know what what are you seeing you guys?
[11:47] Yeah this has always been true for startups. It's like deeply understanding your users and deeply like building a product that you can iterate on quickly
[11:54] that really captures your users's needs and problems. And then kind of related to that is like building a brand and a go to market strategy and a user
[12:02] experience like around those people that you understand so well. The second thing is like moats that intelligence alone can't overcome. And so that's like
[12:11] proprietary data or infrastructure building in a highly regulated space.
[12:15] That's like something that like AI is not going to automate you know compliance regulation fully soon. The final one is like human trust and so
[12:23] like this is also in regulated spaces but anywhere like human trust is not something that's going to be automated soon. So kind of these moats that model intelligence can't bridge that gap yet.
[12:32] And then the final thing which I see you guys doing it's the most exciting for me to see a customer do is build a beautiful product right now but then also build a product that's looking
[12:40] towards the future. We are seeing models consistently get better at longer horizon tasks, more autonomous tasks and you know a year and a half ago someone
[12:50] probably didn't think emergence product could exist. you know text to app builder truly democratizing software and then continuing to push that forward of
[12:57] like okay today we know a product like emergent can exist what's the next thing ahead of the frontier for the models right I mean internally we have actually
[13:05] rewritten our systems like four times over 9 months right and we almost feel that with every new model launch we have to sort of delete everything that we've learned so far reimagine the world
[13:13] and I work with you on it yeah I mean for example opus like really feels like a different class of model and much more capable of longer horizon task especially like now we can multiple agents coordinating on the same task.
[13:24] Totally.
[13:24] My belief has always been that okay, every time like a new class model shows up, let's delete everything we have done. Let's reimagine the world from this lens of the new model. So, I think I think that's been really really helpful.
[13:32] I'm curious to transition into like your users. So, we've talked about how most of them have never written code. Who are these people and like what are they building? I'd love to hear some like user stories too.
[13:42] Yeah, I mean when we started like you know like I we thought that we were building um for mostly like semi-technical users, right? It's going to be mostly program managers, you know,
[13:50] product managers, designers who are going to use us initially. But we were surprised to see when we launched that like a lot of our users were actually business operators who were using us to
[13:58] build serious applications. And essentially we're actually built for like domain experts. People who really really understand their domain really well and but never had the tools to
[14:05] express themselves can now just come in and describe the problem in depth and like agents will go and build the application for them. the gap between
[14:13] communication has been reduced and build out and and have the site feedback loop to sort of you know iterate on the software themselves and we have users across the globe 190 countries almost 7
[14:22] million users my favorite example is uh this user Christy she's in Alaska and she is a clinical psychologist and also
[14:30] an equestrian coach and she had been waiting for 10 years to sort of marry these two fields and she had gone to you know a dev shop in Nova Scotia and got a
[14:39] code of $50,000 to build this app and tried it with them but it didn't sort of work out discovered emergent started building on it has her app live on the
[14:46] app store today it's called Equ for the first time she was able to marry these two fields of psychology and her sports coaching has hundreds of us are using it
[14:54] right now and she was telling me that like you know like I've been waiting for 10 years for this opportunity to sort of really really build something so we are building for like small businesses today right small businesses globally account
[15:02] for 70% of employment accounts for like 50% of GDP of the world right but they've never had the tools to sort of really express themselves because like there are million niches in small
[15:11] businesses right and tradition Traditionally when you had SAS world they were forced to move up market for economic reason but for the first time with AI actually you can actually serve
[15:19] all of these million niches at zero marginal cost and that's what we're trying to enable like you know really empower these small businesses to sort of accelerate their businesses.
[15:26] What do you think emergent looks like a year from now? What are you most excited to build next?
[15:31] Yeah I think a year is a long time in this world.
[15:34] Yeah. Yeah. I think all of us have seen that meter chart where you know the long horizon agents are going to be for us the market segment is like really clear.
[15:41] We want to serve these small medium businesses. We want to serve new entrepreneurs. So we are very very focused on making them successful. We're coming out with a new agent which we
[15:49] think is significantly better than existing ones. One of the other things that we are really really excited about is with especially long horizon agents coming online. We especially think that
[15:57] there's a way for us to automate all of the businesses operations for small businesses. We want to move from software to sort of actually automating
[16:04] their entire business and allow for this autonomous businesses to happen on the platform. So we are very soon launching a new product. We're very excited about it. It's called Wingman. It's kind of
[16:13] agents for businesses and it's going to automate all of your business processes including finances, including operations, sales, marketing.
[16:19] 2026 is going to be year where people start automating large part of their businesses and emergent wants to be the platform for businesses to come and automate all of their businesses on top of us.
[16:28] Well, thank you for being here today, Mukund. It's been such a pleasure having you.
[16:31] Thanks for having me. It's been a great chat. Thank you so much.
