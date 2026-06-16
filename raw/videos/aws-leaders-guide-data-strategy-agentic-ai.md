---
title: "A leader's guide to data strategy in the era of agentic AI | AWS Events"
video_id: 3XyNPfWWxiQ
url: https://www.youtube.com/watch?v=3XyNPfWWxiQ
channel: AWS Events
channel_id: UCdoadna9HFHsxXWhafhNvKw
channel_url: https://www.youtube.com/channel/UCdoadna9HFHsxXWhafhNvKw
publish_date: '2026-06-12T16:32:31-07:00'
upload_date: '2026-06-12T16:32:31-07:00'
category: Science & Technology
duration: '33:42'
length_seconds: 2022
view_count: 1400
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
  In Formula 1, victories depend on turning millions of data points into winning decisions. Organizations can apply this same precision to unlock value from underutilized data assets. Drawing from F1's model, we present a three-part framework for data excellence: customer-focused decisions, dynamic people- powered strategies, and market-reive structures. Learn practical approaches to evolve your data strategy into a business advantage in the AI era.
  
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

[0:05] Thank you and hello everyone and welcome to the executive forum at the AWS summit
[0:10] in Sydney. Thank you so much for spending a little bit of time with us. We got a lot to cover. So let's dive in.
[0:19] Seeing that data is foundational to many of our efforts, I think it's only right
[0:24] that we start there. You see, many organizations face huge barriers when
[0:30] adopting agentic AI. In this session, we're going to talk about the importance
[0:35] of a bold data strategy and how we need to reimagine that data strategy in this
[0:42] era of agentic AI. AWS is the title sponsor for Formula 1.
[0:49] And as I spent time with the teams at Formula 1 with Formula 1 talking about their use of data, to me, it is the
[0:56] pinnacle of data. The amount of data that they use is unbelievable. And the ways that they use it is impressive.
[1:03] We're going to use this as a backdrop. To be able to explore a variety of different things. You see, in Formula 1,
[1:11] champions are made by data, not just the drivers. Behind those engines lie a lot of
[1:17] invisible battles. Each car captures over 1 million data points every second.
[1:24] It's a rolling laboratory. Fans see the spectacle, but it's that analytical edge that truly sets everything apart. But
[1:31] unfortunately, unlike Formula 1, most businesses are
[1:36] struggling to extract real value from their data investments. Gartner warns that 80% of data governance initiatives
[1:44] will fail by 2027. Wow. Let that sink in for a moment.
[1:50] Expensive data lake sit is underutilized assets. The reality is many
[1:55] organizations have prioritize data volume over data value.
[2:00] As a former CIO, I can tell you, yeah, I did that. Sorry about that.
[2:09] But what if we've been approaching data the wrong way? You know, we're celebrating collecting
[2:14] those petabytes [snorts] instead of that value. Our massive platforms aren't delivering what we need. So, Formula 1
[2:20] can show us a way. But let me give you one more sobering stat. Harvard Business Reviews say that
[2:27] 99% of organizations invest in data. Now, Harvard's widely regarded being a
[2:33] elite academic institution in the United States. Where's the 1% that aren't investing in data? I mean I partly
[2:41] question their survey but 99% but only 29% are seeing meaningful value out of
[2:48] that data. We're chasing data but we're losing sight of that business value that
[2:53] we need. So the big question is why is the agentic AI changing all this?
[2:58] In 2015 Formula 1 engineers studied the telemetry between sessions. The cars
[3:04] would go out, they gather some and they'd analyze it. Now they analyze that data real time.
[3:10] It's that shift that we need to strive for. But as we've looked at how business
[3:15] has driven new data strategies, it's evolved through four major areas. BI
[3:21] gave us reports. Big data, we built a lot of data lakes. Generative AI, well, it generated content. But the fourth
[3:28] era, the era we're in now changes everything. Humans are no longer the primary data
[3:35] consumer. Machines are. Agents need metadata to reason. They need memory to
[3:41] learn. They need context to be able to act. Your infrastructure stays. The
[3:47] consumer has changed. So in today's session, I'm going to give
[3:53] you a framework for how we look at this. We're going to transform how we think about data governance.
[4:00] So, we'll start by first reimagining, challenging every assumption
[4:05] on what data is worth. Then, we're going to rewire. We're going to look at the business and how the business is
[4:10] structured and operates and look at new ways to do things. And finally,
[4:16] remember, it's about value. We'll talk about what we need to do to turn these ideas into value. Things that you can
[4:24] see, things that you can measure. So how do we actually deliver on these promises? We need a solid foundation.
[4:31] Then we can focus on creating value. That means reimagining everything, every
[4:37] assumption about your data, how you manage it, how you extract value from it, what drives that value. See most
[4:46] companies, we wind up chasing technology instead of business outcomes.
[4:51] all these companies that are launching AI initiatives. Okay, congratulations.
[4:58] Have a business strategy that's informed by your AI, not the other way around. Same thing's true with data.
[5:05] So, as we look at this, let's start with some inspiration from Formula 1. When Formula 1 regulations
[5:14] change, that old car becomes obsolete overnight. teams try to adapt to last
[5:19] year's design, applying those designs to new rules, they're going to lose. The
[5:24] winners recognize and prepare for the shift. They reward the teams that are
[5:31] innovative, that are progressive. So, as we look at our data strategy, the first thing we want to talk about is
[5:38] your data consumers have changed. For decades, we designed data for humans to
[5:44] interpret. dashboards, reports, visualizations, PDF files, document
[5:49] files. That era is ending. Your most demanding data consumer
[5:55] will be an agent. But here's the uncomfortable truth. All
[6:00] that data was designed for humans. It has that structure, that bullet
[6:06] points, the indentation, the bold, the italics. That doesn't matter to the
[6:12] machines. The machines need lower latency, embedded quality signals, context that
[6:19] it can actually parse to be able to execute. You see, most organizations are asking a
[6:25] question. Oh, we need to get a lot of data scientists. How do we get them in? It's the wrong question
[6:31] or maybe the wrong answer. Instead, what we need is we need to enable thousands
[6:36] of business experts to build those agents. That old model was five agents
[6:41] in a year, $500,000 slow. No, the new model I want hundreds of agents built
[6:47] daily, but I need the data in order to do it.
[6:53] But part of our challenge is another uncomfortable truth. We need to bridge
[6:58] these two worlds. Domain experts, data teams, we got to bring them together. But now there's
[7:05] that third party. These machines agents don't understand tribal knowledge or
[7:11] unwritten rules. They can't absorb context the way that a new hire eventually does. That's why metadata and
[7:18] data products matter more than ever before. You see, every data investment, my
[7:25] suggestion is should pass four questions or get rejected outright. One, how will
[7:32] it create value? You'd be surprised at how many projects should stop right there.
[7:39] Two, is this the most direct path? Now maybe your engineering teams are different than mine, but mine loved a
[7:44] good Rube Goldberg solution. Fun to build, complicated. No, no, no. I want
[7:49] the direct path, the fast path. The agents are going to demand it. How quickly can we deliver? And the fourth
[7:55] one, can an agent consume this without a human translating. If a human needs to
[8:01] interpret the data, you have failed the test. So, the second piece of inspiration
[8:08] we're going to look at from Formula 1, you ever wonder what the drivers are staring at in those screens before they
[8:13] leave the garage? They got them up on their car. They're looking at them. It's this.
[8:19] Sorry. It's this. It's a custom lap analysis time. It's showing them where
[8:24] they gained or lost time against a competitor. How's Oscar doing against Charles? Looks
[8:31] like Oscar's not doing well. He's behind by 16,000 of a second. [snorts] Every
[8:38] turn mapped. But the point is we're giving the driver specific information that they need. We're not giving them
[8:45] the whole wealth of information. We're providing that information purposebuilt for that individual.
[8:52] But we've talked about data products for years. Nice idea. It's hard to do. But guess
[8:58] what, guys? Now it's not optional. Agents cannot navigate your data the way
[9:04] humans have. No tribal knowledge, no workarounds. Data products instead give agents what
[9:10] they need. Clear contracts, metadata, and quality signals baked in.
[9:16] This is how we start to make data consumable by machines.
[9:21] But one of the problems that we have with this is data that belongs to everyone.
[9:27] How many organizations where we say, "Ah, well, the owner of the data is the chief data officer." Yeah, fine. I
[9:34] suppose it's terrible place to put ownership. Not because they're not competent, but because it's not where we
[9:40] need it to be. We need to have clear ownership at the most granular level.
[9:46] See, our problem that we get to is when we have shared responsibility, we get shared neglect.
[9:52] And the agents can't navigate this ambiguity.
[9:58] You see that driver gets those eight numbers, but the person sitting on the pit wall gets 200 numbers. The person
[10:04] back at the factory at Ferrari is getting 2,000 numbers. Data products
[10:09] purposebuilt to solve the answers that the people have, but all originating from the same source. Your enterprise
[10:17] should work the same way, shaped for each consumer, not dumped into data
[10:22] lakes where we assume someone will magically come up with value out of
[10:28] it. In today's agentic world, data products need a completely different definition. They need to be
[10:34] purpose-built. They need to be agentready assets
[10:39] enriched with metadata. But what we also need is clear
[10:45] ownership. If we don't have ownership over these data products, someone who comes in to
[10:50] work every day, obsessed with is this data product creating value for the
[10:57] organization? And if not, what do I, as the owner of this data product need to be doing differently?
[11:04] And critically, these data products, well, they need to be accessible and discoverable by agents.
[11:12] You see, open architectures, yeah, they'll free you from those walled gardens, but we need to prioritize with
[11:18] intention. A mistake I see organizations making. If I look back on my history as
[11:23] CIO, I might have made this mistake. You guys are probably wondering, gosh, did this guy get anything right? I I did. I
[11:31] got a few things right. But people I see going out and saying, "First thing I need to do is gather all
[11:37] the data in the enterprise, figure out where it all sits. Then I need to clean it and position it and store it. Then
[11:44] I'm probably going to put it in a data lake." And after five years, $50 million, and the severance of one CIO
[11:51] who got fired for this failed project, you're done. Except for you've created no value.
[11:58] You've just created the opportunity for value. Instead, what you need to do, identify a business problem or a need,
[12:06] determine what data will help you solve that situation and get that data right.
[12:13] And then lather, rinse, repeat. Do it over and over again. Learn as you go. Create value as you go.
[12:20] The engineer inside me's twitching at this because it's not the way an engineer
[12:27] would do it, but it's the way a business person would do it and it's the way that we're seeing
[12:35] organizations that are able to succeed do it. When you start to narrow down on one data product, you disco discover
[12:42] something crucial. Traditional data gives you the what, what happened,
[12:48] volumes, facts, figures. But agentic AI demands the why behind it. The more why
[12:55] that we can give it, the more autonomous we can permit these agents to be. This
[13:02] context provides answers and connections, revealing hidden relationships in the data. Is this the
[13:07] first time this customer has called to complain about this product or the 10th time? Is it always new customers or
[13:14] existing customers? Is it customers in North America or customers in Europe? All of this context,
[13:21] this information matters when we want to train our agents to behave. So, three
[13:26] things your agents need from data. First, machine readable structure.
[13:33] So, agents are able to parse it without guessing. Second, we need the semantics, the relationships between the data. And
[13:40] third, we need memory across those agents, across those interactions. So the agents
[13:47] are able to learn. As humans, we read formatting cues
[13:53] without thinking. We see a PDF document. We see the italics, the bold. It means
[13:58] something to us. Read this. Pay attention to this. This jumps out to you. But to machines that gets lost.
[14:06] It becomes overhead. More tokens to pay for, more tokens to consume.
[14:14] You see, Stripe has gone through and converted human docs into markdown where agents can reason over this. Headers
[14:21] become um hierarchy. Lists become arrays. Links become more navigable.
[14:27] The same content. Now the agent is able to understand it. We need to put
[14:34] the data into machine readable format as well as human readable format.
[14:40] But the clean data stores are just step one. With LLMs, you extract the entities
[14:45] from unstructured data, people, places, time, and then we need to find the associations between them. Think of it
[14:52] as a cube where a cat and dog might sit close together in close proximity with one another.
[14:58] But rotate your perspective for a moment and the picture completely changes. Suddenly AWS and Gartner are connected
[15:06] because they're both talking about cloud strategy and the dogs and cats are split a little bit farther apart. This is
[15:12] vector embedding. We need to begin this vector embedding with our data and have
[15:18] this as a component of our data strategy. And this unlocks something incredibly powerful. Mapping these
[15:24] entity relationships. Gartner publishes a magic quadrant with evaluates vendors like AWS. These
[15:30] connections, well, they're knowledge graphs. They let LLMs traverse cause and
[15:36] effect to solve real problems. It's a new type of data that we must master and
[15:41] we must provide. But the other thing is memory. Goldfish memory is cute for chat bots.
[15:49] It's not really actually, but for agents, it's a deal breakaker. Imagine briefing a change leader in your
[15:56] organization on your business, your system and goals and their next question is um sorry, what does your company do?
[16:04] We can't permit our agents to do the same thing. And we need to do that by providing them memory. We need to
[16:12] address this stateless challenge. Memory makes agents useful over time. Not
[16:17] bigger context windows, more tokens, more money. Now we want memory. Four
[16:23] types. We want that episodic what happened. Semantic and what's true. Priming is who the agent is now. And
[16:31] procedural is how it should act. Every night agents consolidate what matters.
[16:37] Kind of just like your brain does as you sleep. So couple suggestions. One, treat data products not as raw material, but
[16:45] as purposebuilt, purpose-designed solutions. Structure your data so agents
[16:51] are able to parse that data. Embed the semantics and the relationships in them
[16:56] and give your agents memory. Start with one data product. Prove that it works.
[17:03] Lather, rinse, repeat. So, now that we've reset our focus on what matters
[17:09] and have oriented around data products, Formula 1's going to teach us another lesson. The fastest car means nothing
[17:16] without the people supporting it behind it. So let's get into rewire. Like those 1.8
[17:22] second lap times or excuse me pit times that we see dataf flow demands a perfect
[17:28] choreography. Every handoff engineered each person playing the right role. The
[17:34] time to engineer and understand those is becoming more and more crucial.
[17:40] As we look at Formula 1 for a little inspiration here, Ferrari's tire specialist is not back at the factory.
[17:46] She's at the track side where it matters. The fuel strategist hears the
[17:51] driver talking about how the car is behaving right there. Each expert is
[17:57] positioned where their decisions create immediate impact. We've decentralized
[18:04] the organization. But proximity without structure fails like a trackside expert
[18:09] who can't well they can't reach and talk to the pit crew. Success means skilled people
[18:16] putting them where those decisions will happen. Out of almost anything I see
[18:22] organizations do, that decentralizing and empowering of the workforce
[18:29] by far is the greatest predictor of success of
[18:34] organizations. But here's an uncomfortable truth about where a lot of organizations fail. focusing on that
[18:41] technology instead of focusing on the people. To me, it's
[18:47] like this analogy. If you had a Formula 1 car, arguably the most advanced automobile in the world,
[18:54] but if I put it on a dirt track, you're going to get a lot of YouTube views. Now, someone pointed out to me,
[19:01] actually, Daniel Ricardo in Red Bull actually did this here in Australia. Drove a Formula 1 car in a dirt track.
[19:08] It got a lot of YouTube views, but doing that is the same thing of
[19:13] having fantastic technology, but not the people to be able to execute
[19:19] on it. And the research backs this up. For five straight years, culture beats
[19:25] technology as the roadblock in data realization. Leaders preach that
[19:30] datadriven decisions, but often don't model that behavior. We need to fix
[19:36] these cultural barriers first. So where should we think about how to structure
[19:42] these teams? Should we centralize teams or should we decentralize teams? This is
[19:47] one of the most common questions we get on our team. And the answer that I give
[19:52] people is relatively simple. If it speeds your team up, centralize
[19:58] it. Everything else, decentralize it.
[20:04] My centers of excellence were always centered. They were never excellent. This idea
[20:11] that I'm going to be able to build this core centralized team that's going to build a platform that'll be reusable. It sounds great, guys. Maybe your teams are
[20:18] better than mine. I'm not saying don't have a centralized team or a centralized strategy. I'm just
[20:25] saying however big you think it is, it should be smaller than that. I used to tell my centralized team, you had one
[20:32] job every single year. And that job was to put yourself out of business. Now, I
[20:37] never thought that they would get there. And I also told them, trust me, I love you guys. You'll have plenty to do and
[20:42] don't worry. But I wanted them to be so obsessed over how could they enable the rest of the organization that they were
[20:49] no longer needed. But another thing that we see is data hoarding. It kills collaboration.
[20:56] You know, these open standards make communication a lot better, but the
[21:01] barriers are cultural in this. You see, data hoarding isn't malicious.
[21:07] These teams fear misuse, the loss of control, getting blamed for what's going to happen. We need to transform this
[21:14] through four steps. First, you got to understand their concerns. We got to be empathetic with these people. Then, we
[21:21] need to show them why collaboration will win. Then we have to build those secure
[21:27] platforms. I talk a lot about govern by enabling. Make it easy for people to do
[21:32] the right thing and they will make it hard and they will go around you and
[21:38] then [snorts] watch that shift happen. My data becomes our intelligence inside the organization.
[21:44] But we also need to fix that decision distance with that three team structure that puts expertise where those decision
[21:50] happens. We want those platform teams, small team, remember, smaller than however you think it is to build the
[21:57] tools, the standards that enable rather than control. Then we have those data
[22:03] product teams embedded with sales, marketing, operations, building those data products in those
[22:08] domains. And then we have the business consumers that define the needs and apply the insights. Think centralized
[22:17] infrastructure, decentralized consumption. So decentralize your teams
[22:22] by default. Centralize only what speeds you up. Flip the default from data
[22:28] hoarding to automatic sharing with data trails. Move data engineers into your
[22:34] business units where the decisions actually are happening and build those AI data platforms that connects these
[22:42] restructured teams. These cultural changes will take time and they will take repetition and communication to be
[22:49] able to drive through them. But let's go back to Formula 1 here for a minute.
[22:54] Ferrari uses the identical telemetry standards whether the data goes to the pit or the factory. Every team member
[23:01] knows exactly what tire temperature means. There's no confusion. When everyone speaks the same language,
[23:08] decisions happen instantly. This is what enabling governance looks
[23:14] like. Think Formula 1 safety cars. They don't stop the race, they manage the
[23:20] risk. Great governance accelerates value. It doesn't block it. We need real
[23:27] time policy enforcement and audit trails built in, not bolted on to our data.
[23:34] I know data governance, especially in AI, feels like an impossible puzzle, but everyone's struggling with it. 92% of
[23:41] agentic AI users worry about their data quality and governance issues.
[23:48] That'll get your attention. Half of data leaders say poor data quality blocks
[23:54] their AI implementation completely. We have to get this right. You're not
[24:00] behind. Everyone is struggling with this. So what do companies do? Well, they do what I did. You panic. You lock
[24:06] everything down. Got to have control. No hallucinations from my AI.
[24:12] But here's the irony. These strict controls create the problems they were meant to prevent. They force people to go
[24:18] underground, to go around you. Why? Because we're humans. When official channels fail, people
[24:25] build their own. And they build them without safeguards.
[24:31] So we need to build these structures. So let's talk about a better way. Minimum
[24:36] viable governance. Think guardrails, not roadblocks. Accepting some visible risk actually
[24:42] reduces your real risk exposure. By keeping your work visible when teams
[24:48] work within systems, not around them, you maintain control over your data. So
[24:56] like Formula 1 drivers, users should think about their infrastructure. Shouldn't, excuse me, shouldn't think
[25:01] about their infrastructure. Authentication, discovery, queries, all should be invisible.
[25:08] This context engineering becomes even more important for agents. Data assets
[25:14] should carry business meaning. Those trust scores of how good that data is and lineage, not just the schema of that
[25:21] data. And metadata becomes even more crucial in this.
[25:26] And I encourage you to look at a framework like this, be inspired by it.
[25:32] The vast majority of your data should be open, available for everyone.
[25:37] A limited amount of your data, yes, your data, names, addresses, phone number, it's protected.
[25:43] And only a small amount of the data is actually restricted. I want it to be open by default. Open
[25:50] within your organization. You're not giving away your IP.
[25:56] And in order to do this, we've worked with a lot of organizations to establish a series of data tenants. And our
[26:01] approach distills this down to eight essential tenants we think that work well in harmony. A foundation. Customer
[26:08] value should drive all investment. Remember that from earlier. The flow. We want to minimize the distance from
[26:15] decisions and we want to default to open access. For execution, we want clear
[26:21] ownership. We want to trust through monitoring. We want automation. If it's not automated, it is not done. And
[26:28] everything everything everything needs to become real time data. You see
[26:35] that smart classification might unlock lineage as a competitive advantage. But we need to move past those dusty
[26:42] compliance docks. We need to move beyond so we can trust in a different way. You see, agents need
[26:50] trust at speed. You can't audit your way to trust. You need live systems as we
[26:56] heard Werner Vogels talking about before watching. We need guardrails, telemetry.
[27:02] We need agents that are able to make their own judgment. A good way to think of this is well,
[27:09] think of golf versus Formula 1. In golf, you prepare, swing, and trust the
[27:14] outcome. In Formula 1, winning happens during the race. Telemetry, continuous strategy,
[27:21] continuous course correction. You don't send the car and hope, you monitor it
[27:26] every step of the way. We need to move to that same thing. So we need to move
[27:32] from controls to enablement. Traditional governance controls through restriction. Instead, we need to enable
[27:40] people. We need the standards to eliminate the confusion, the guard rails to eliminate the risky work. And we need
[27:46] to default to open with our data. So, we built a solid foundation,
[27:53] but the first two steps mean nothing without measuring the business outcome.
[27:59] So, now it's time to realize the results. We need to dive into a couple strategies to do that. You see, race day
[28:06] is where champions prove themselves, their moment of truth. Let me show you how we start to put this together. Let's
[28:13] go to Formula 1 again. Everyone's fast on Friday practice. Sunday separates those champions from
[28:20] pretenders. Practice laps aren't race wins. The gap is that production
[28:25] readiness that they're able to apply. When conditions change midra, Ferrari
[28:31] adapts in real time. They don't use their original tire strategy. They evolve and they evolve because of
[28:38] that real-time data. You see, the demo is not the destination. Production is where the value lives.
[28:45] We have to move from those proof of concept purgatory into value creation.
[28:52] And the gap between that Friday practice and Sunday wins is that production
[28:58] readiness. And agentic AI demands continuous learning, not periodic
[29:03] refreshes like traditional systems. Real time means capturing every interaction, every customer complaint, every market
[29:10] shift, all of it, all the time. Forget batch processing. Your AI needs to learn
[29:16] instantly. You see, Formula 1 processes a million data points per second. Races won in
[29:22] real time. McKinsey studied over,200 managers.
[29:29] Fast, high decisions, high quality decisions outweighed almost anything else in how they were able to create
[29:35] value. And you can't do that with data that's a minute, an hour, a day, a week,
[29:40] a month old. Your agents will demand the same thing. So, transform your speed to
[29:46] competitive advantage with this three-step plan. First, audit your decision de delays. Precisely. Where
[29:54] does your data bottleneck in your critical choices? Select two or three high impact decisions. Remember, we're
[29:59] not boiling the ocean. Accelerate those. Turn those into real-time data. Replace those batch
[30:06] reports. Fast data without fast decisions. Well, it equals expensive failure.
[30:14] Dynamic data means capturing every customer interaction as it happens.
[30:19] Reducing the time between data creation and data value. Obsess over it. Ask your
[30:26] teams constantly how long it takes to be able to get to that. You see, again, everyone's fast on
[30:33] practice. Sunday's where it separates things. We need to be able to change.
[30:39] And what we see is data strategy needs to become an evolution, not a
[30:44] revolution. You see, strategy isn't a document. It's what you do every day. Just like Ferrari's constant refinement
[30:52] of their strategy. Success comes from continuous testing and learning, not
[30:57] powerpoints or annual planning cycles. These documents might have come from my desk at my last job. Strategy documents
[31:05] might be less important than we've ever been taught to believe. McKinsey found that only 21% of top performers credit
[31:13] their strategy documents for their success.
[31:19] I don't know how many McKinsey wrote, but we can get back to that. The best companies embed strategic thinking in
[31:26] every decision every day. These are not minor in issues you see here. They're
[31:32] existential threats to your data strategy. If you see these signs, pause your new investments until you fix these
[31:40] underlying problems. Shadow data teams mean that centralized strategy is too restriction. When
[31:47] executives rely on their gut instead of using data, you're not creating value with those data products. You see that
[31:54] strategy deck that you built is already dead. Formula 1, they don't plan in
[32:00] those annual cycles. Test, validate, ship, revert. Production is the intent
[32:05] of every sprint. Don't create a proof of concept without the ambition of putting
[32:11] it into production. Everything else is theater. It's dress up. So, we have the
[32:16] playbook. We believe that AWS provides you that data infrastructure that you need that
[32:23] will scale with you without limits. those purpose-built databases and processing engines and an ecosystem to
[32:30] allow you to succeed. So that complete playbook reimagine,
[32:35] rewire and realize the question is not whether or not you need to transform. It's how fast you can.
[32:42] So we started with reimagining the foundation through your customer eyes and treating data as products not raw
[32:49] material and ownership over those data products. We rewired with a peoplep
[32:55] powered culture with those clear tenants and governance that enables people and
[33:00] doesn't restrict and we realize the results through decisions focused in
[33:05] real time data and living strategy documents.
[33:10] So here's the transformative truth. Data is not like oil. It's oxygen for your
[33:17] business and more important than oil could ever be. It doesn't just fuel your
[33:22] operations, it gives life to your organization. And the agentic AI winners
[33:28] will treat data as a vital asset to their organization.
[33:33] So, thank you very much. I appreciate the time. [music]
