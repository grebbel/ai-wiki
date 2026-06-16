---
title: "Build core skills to thrive as an AI-era developer"
video_id: OJLMClRrUv4
url: https://www.youtube.com/watch?v=OJLMClRrUv4
channel: Google for Developers
channel_id: UC_x5XG1OV2P6uZZ5FSM9Ttw
channel_url: https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw
publish_date: '2026-04-21T22:21:19-07:00'
upload_date: '2026-04-21T22:21:19-07:00'
category: Science & Technology
duration: '50:15'
length_seconds: 3015
view_count: 8408
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
  - language_code: en
    name: English - CC1
    kind: manual
    is_translatable: true
  - language_code: en
    name: English - DTVCC1
    kind: manual
    is_translatable: true
keywords:
  - 'Google'
  - 'developers'
  - 'pr_pr: Google I/O;'
  - 'ct:Event - Professional Development;'
description: |
  Explore the essential skill domains—including core engineering principles and business context—needed to harness the full potential of AI, and unlock massive productivity gains in your daily workflow. Discover how AI is a powerful collaborator that can change and accelerate how you build software. 
  
  Speakers: Nicole Forsgren, Andrew Macvean
  
  Watch the Professional Development sessions from Google I/O 2026 → https://goo.gle/professional-developement-IO26 
  
  Subscribe to Google for Developers → https://goo.gle/developers 
  
  
  #GoogleIO
  
  
  Event: Google I/O 2026
  
  Products Mentioned: AI/Machine Learning
notes: |
  ASR-cleaned: stripped redundant 'N minutes, M seconds' prefix that the YouTube Live caption track prepends to each segment.
  Manual (CC1) caption tracks exist on this video alongside the ASR track; the fetched transcript is ASR-derived.
---

## Transcript

[4:36] >> Hi, everyone! How we doing? [Applause].

[4:42] >> There we go! How are we feeling? Excited? There we go.

[4:49] Maybe a little overwhelmed? Curious? Hopefully curious? Okay. We are Andrew and Nicole, both leads on the Developer

[4:56] Intelligence team here at Google.

[5:01] And together, we've spent our careers studying software engineering, the people, the processes, the tools, the systems, the culture.

[5:07] And we want to start by recognizing this is a big moment for Software engineering.

[5:13] You see quotes like this that really emphasize not just the magnitude of the moment, but the speed at which this is

[5:21] Change happening.

[5:21] Our goal today is to share some of our research, some of our knowledge about what we are seeing inside of Google, and ultimately answer this question:

[5:29] How can we as software engineers continue to thrive in this AI native era.

[5:35] We are going to do that by walking through this T shaped Software Engineering role which we are seeing grow in importance. We will go into detail on some

[5:43] patterns we are seeing in terms of how software engineering is being done, the skills and capabilities we are seeing our

[5:53] top engineers embody, and introduce some practical tips for how you can think about your role.

[5:57] But first, we want to set the scene. We want to make sure we are all on the same page.

[6:03] Like we said, this is a big moment, but what's actually happening? First of all, we are seeing fairly pervasive adoption of AI

[6:11] tools for Software Engineering. Probably not a surprise to anyone here. The Majority of Tech professionals are using AI, and

[6:19] Relying on it, in many cases, a lot. We are also seeing profound impact. So inside of Google, around 3/4 of all code is

[6:26] written by AI. At the same time, people are very reasonably asking, is it

[6:33] actually improving productivity?

[6:41] And if it is, is it 10%? 10X? 100 X? The truth is, in some places, there's even a productivity paradox occurring.

[6:49] There's some evidence that our DORA team found by studying multiple companies, that increasing AI adoption can lead to individual productivity benefits while at the same time

[6:55] decreasing team level benefits. Over the last year inside of Google, we have seen some

[7:03] interesting patterns emerge. First of all, we are seeing a lot of benefits. Not only are we seeing AI generate an increasing amount of

[7:09] code, with more and more

[7:19] autonomy, we are seeing that that code actually lasts. This presentation is about the skills and capabilities that really allow that to happen.

[7:29] Second of all, there is some emergent behaviors on those numbers. For example, we are seeing the engineers who use AI the most,

[7:37] they're actually spending more time coding, identifying and collaborating with their peers.

[7:45] There is counterintuitive. The truth is they are doing more of these activities and the shape looks different.

[7:51] Our top performing engineers are more active, not less, even though they're delegating more

[7:57] and more work to AI.

[8:05] It's important to note, the AI benefits are not necessarily homogenous. We know all about the old adage, garbage in, garbage out. And we've seen lots of research around the need to not only really master working with the AI, but also the domain in which

[8:13] you are applying that AI to.

[8:19] Furthermore, and this is preaching to the choir, but software engineering is so much more than coding, and coding was never really the bottleneck, right?

[8:27] We are talking about a hugely complex system here. To get the true benefits, we need to really recognize two more things.

[8:35] First, we need to think about AI for the entire software

[8:43] development lifecycle and the entire product development lifecycle. We need to think about AI way beyond code generation.

[8:49] Second, this isn't about just applying AI to the old ways of working, the magic actually happens when those traditional

[8:57] Processing are evolved and even transformed.

[8:59] We are going through multiple paradigm shifts. We are seeing totally new processes emerge with totally new people taking

[9:05] on new roles in the software development lifecycle. So I go back to the question that we introduced at the start.

[9:13] This is a lot of change to deal with.

[9:17] Well, hopefully I've got two pieces of good news.

[9:21] The first is, however you are feeling, trust me, you are not alone. There is a lot of research on

[9:29] this, inside and outside of Google, and there are lots of really complex emotions emerging. None of this is surprising given the size and speed of change. The excitement is real, the

[9:37] opportunities are real, but it's a lot. The second piece of good news is that this talk is really about

[9:45] how you can rise above all of this, and continue to thrive in this AI-native era.

[9:53] There are no magic wands. But there are ways to thrive. We are seeing strong evidence that despite the new shape of the software engineering role, when the change is approached

[10:01] intentionally, this can and should be the most exciting time to work in this field.

[10:07] >> Thanks, Andrew. Okay. So let's talk a little bit about the patterns we are seeing in our

[10:13] highest performing AI Native approach. Here we will look at some

[10:21] interesting things that emerge and we will talk about the expanded role of software engineering.

[10:29] As Andrew mentioned, our job is to really study and measure the engineering system and all the pieces within that. We are measuring the end to end time, to go from an initial seed of an idea, all the way through

[10:37] to getting that idea out into a real user's hands. So here we're thinking about not just software engineering, but

[10:45] actually the entire product development process.

[10:49] In that system, our most productive AI Native engineers are doing a few things differently.

[10:57] We will go through five patterns that we're seeing emerge. First,is that they are operating at higher altitudes. They are

[11:07] combining their engineering knowledge, but they are also applying their understanding of business context and user needs.

[11:11] They are thinking deeply about why they are building it, not just what, or how. Now, if we think about this,

[11:19] this is always what's been expected of senior engineers, but with AI accelerating execution, doing it well has never been more important.

[11:27] Second, they are really shifting left on intent. I know some of this heard this

[11:35] at the conference today. Traditionally, "shifting left" meant moving testing or security practices earlier in the software development lifecycle.

[11:43] But today, we have more and more work being done autonomously by agents, we need to shift left on intent. We need to spend more time up

[11:51] front in energy to really plan, get clear on instructions, and provide the right context.

[11:59] What this means is that a fundamental source of truth is moving away from the code itself and it's really shifting toward

[12:07] the structured intent. Our engineers are writing specification files, which are product thinking made explicit.

[12:15] This helps better guide our AI. But it also documents the decisions much more explicitly than some of us have done in the

[12:23] past and this is critical, as agents take on more execution, human context shrinks and the signal-to-noise ratio declines.

[12:31] Just building without capturing intent is incredibly tempting , it's fun to do on a weekend,

[12:39] maybe, but you risk a lot of prototypes that no one understands the rationale for. So when we actively organize this continuously-evolving knowledge

[12:47] That's one strong strategy to prevent severe cognitive overload.

[12:53] Building on the point before I just made, our top engineers are not "vibe coding." They are not prompting for code.

[12:59] What they're doing is designing environments, setting the guardrails, creating the systems So that agents and humans can

[13:07] work together toward a goal and a broader purpose. Think of this like creating a system of reasoning in order to operate at a scale beyond one person can do.

[13:19] So this also includes setting up teams of agents to give them the right skills to act.

[13:27] Our top engineers, I know someone else mentioned this in another session, don't want fast code. They want verified high quality code. So when we are delegating to

[13:35] teams of agents, and outsourcing execution, how do we keep the bar high and how to act and

[13:43] debate each other for better outcomes?

[13:45] That all comes from Pattern two, and the specifications and intent files we just discussed. And even though we're shifting left on intent and capturing

[13:53] this and specifying it early, the feedback loops are really important to this process.

[14:01] Next up, AI is not just changing how people build, but who can build.

[14:05] It is actively decoupling a person's job role from the tasks they perform.

[14:11] We are also seeing the rise of the micro team. Small, agile pods, with less communication overhead and

[14:18] tighter collaboration loops. These teams can execute at

[14:25] really large scale and good velocity, thanks to the agents they are deploying. But going back to our earlier points, all of this is only possible if you actually shift

[14:33] left on intent because that helps us master the delegation to agents. You have to clearly articulate the context, the constraints, the goals, the success criteria,

[14:41] so those agents can execute the "the how" and not keep repeating

[14:49] mistakes and creating things they already learned about. You need to design the system so your agents can access the right tools, navigate your data, and iterate with you.

[14:57] Moving forward. The fifth and final pattern is really about the scientific mindset. And how we all need to continually explore.

[15:05] If we're going to work at the cutting edge, we need to be open to failure. Things are moving so fast, it's rarely right about -- the idea

[15:13] is rarely getting it right the first time, it's to learn what we can as we move and then iterate and turn that into

[15:21] a -- contribute up into a learning organization. Every week, our engineers are experimenting with new approaches and investing in codifying that learning back

[15:28] into the system. Again, Intent and feedback loops are key. It's not a scientific mindset if we are just randomly exploring and not capturing the

[15:37] learnings. So pulling this all together, we are are really talking about shifting left. Shifting up. And System Design.

[15:45] Now, System Design includes the environment, the actors in that environment, including humans, agents and tools, and the

[15:51] culture that ties it together. This let's us focus our efforts on the most important problems, to learn and adapt as quickly as possible,

[15:59] and execute effectively while feeding insights back into the system.

[16:03] Okay. So we've talked about five general patterns we are

[16:11] Seeing during this shift and if we go back and think about the

[16:19] goals together into a way of thinking about the core skill areas required to thrive in this AI era. We may repeat a few ideas, but that's because we want to really land the shift that is happening and the role evolution that we we are seeing in this evolution.

[16:27] As we mentioned, Our top performers are increasingly embodying this T-shaped software engineer profile.

[16:33] The idea of a T shaped developer We've heard of this before, we're familiar with it. We are seeing a few things emerge, though.

[16:40] For those of you who haven't heard of a T-shaped engineer, the horizontal bar of the T, represents a broad foundation of

[16:47] knowledge of the wider software engineering ecosystem. This doesn't necessarily mean expertise in all possible areas, But we have a good understanding

[16:56] how key parts of the system work. And then the vertical stem of the T represents the deep, specialized knowledge and hands on

[17:03] experience, usually within one specific field, like FinTech, or On a particular technology stack

[17:12] or framework but that's our deexpertise. What we are seeing happen though is an interesting evolution of this T-shape.

[17:20] First of all, there is a new layer of horizontal expertise required, and that is focussed on effectively engaging with and

[17:27] -- AI. The AI engineers --

[17:35] engineers are able to understand AI constraints in task specific contexts, assess the outputs, and ultimately steer the AI effectively.

[17:41] We're also seeing some additionals on the wings of the T here. We are seeing some more breadth required.

[17:49] Because AI has lowered the barrier to entry, and increased the throughput of coding, it is more important than ever before To understand this context.

[17:58] On one arm, we have Adjacent Engineering. Because AI is increasingly generating more and more functional code, the

[18:05] key considerations during that

[18:13] -- need to be at the forefront. The second area is in Adjacent Non-Engineering, specifically Business and User Context.

[18:19] Because AI handles the "how" of coding, we need to make sure we are thinking about and understanding the business and

[18:28] contextual needs that we're solving for.

[18:31] I think one thing that's interesting is this is already what's expected of our senior developers, we've talked about this a little bit.

[18:38] But now that our engineers are working at higher and higher altitudes, we can do more with agents.

[18:46] So the difference here is really, A, there's a fundamental assumption about using AI effectively and B, for a lot of the reasons we discussed, AI

[18:55] makes the depth and breadth needs a little more acute. We notice them a little bit more. We need that adjacent knowledge

[19:02] and need the depth of technical noij knowledge, otherwise AI

[19:11] makes us do things faster. >> Thank you, Nicole. Everyone good?

[19:23] We will move through each of the T-shaped skill Domains, and for each we will give you a few stories and anecdotes from inside Google. We want to emphasize real examples of how things are playing out today, what we are learning, and make clear the

[19:31] importance of the entire T-shape.

[19:32] We will then pull it together by sharing some specific practical tips we mentioned to acquire or embody the behaviors and

[19:40] recommended practices.

[19:45] Okay. Let's start with core software Engineering is evolving, I want to share a story from our Search organization.

[19:51] Right now, we have product managers who are shipping features all the way through to live experiments.

[19:59] Now, They aren't writing traditional code, they are using some of our internal platforms that help Translate their intent, that's

[20:08] the business or user needs, into working features on our real production tech stack.

[20:11] From the outside, you could think that if PMs are vibe coding their way to production, what role do traditional core software engineering skills

[20:21] actually play?

[20:22] The reality is, none of this is possible without an incredibly advanced platform.

[20:25] The deep expertise in system architecture, the differing strengths of particular

[20:35] frameworks, they are all baked into the platform. This is a nice example of how the engineer is working higher

[20:42] up the abstraction stack. The engineer isn't hand-crafting those individual features, they are precision engineering the

[20:50] ecosystem that allows the features to exist safely. Now, that requires more engineering depth, not less.

[21:03] So given this trajectory, let's talk about three concrete shifts we are seeing. First, because code generation is happening faster, effective

[21:11] verification becomes the bottleneck. AI can act as a massive force multiplier, but you must possess the deep expertise required to

[21:19] evaluate, integrate, and maintain its output. However, given the scale at

[21:27] which AI can operate, this is not necessarily about manually verifying output line by line. This isn't possible cognitively.

[21:33] It's about setting effective feedback loops, ensuring you catch issues reliably and in low

[21:39] stakes environments, and using that data to ensure that

[21:48] you as an engineer is on the highest value most necessary things. And so our internal platforms, they're really designed to allow

[21:56] us to quickly test out features, gather performance data in a safe way, and use these feedback loops to highlight to our engineers where their particular expertise is most required.

[22:06] That's where they're then brought into the loop. Now, this leads us to our second point and Nicole mentioned this

[22:14] already, our engineers don't vibe code. They control. They are precision engineers. If you lack deep engineering understanding, if you don't

[22:22] understand the systems you're building against, AI can run the risk of generating technical and cognitive debt at an incredibly fast rate.

[22:30] This is why our teams have been working on these internal platforms in which intent is carefully translated into high quality, reliable, and secure

[22:37] code. Our engineers are thinking about setting the boundaries and the

[22:44] guardrails of the system. So, for example, they're specifying the nuanced tile

[22:52] guide conventions to follow, with the checks and balances to detect drift. Now, we know some of these models

[23:00] have a tendency to sound incredibly confident and when they're operating at that when they are operating at

[23:08] scale, it can be easier to accept changes wholesale. There's a saying I like, delegate tasks, not judgement. It is essential that your core engineering skills are what push

[23:16] the models in the right direction. Again, this is about creating the environment. The system where issues can be

[23:24] caught and remediated with minimal risk. What we don't want is intellectual passivity. That's why the feedback loops are so important,

[23:32] not just in getting end-user feedback, performance feedback,

[23:38] and using that to measure the adherence to intent. Observability is critical so we can establish where guardrails may be missing, or agents are making incorrect assumptions.

[23:48] Because they don't have the right context. Okay, it is easy to say maintain your deep expertise, but how do

[23:54] you actually do that when you In this fast-moving environment?

[24:04] Here are a few practical tips we are seeing our top teams embracing.

[24:06] First, we recommend re-implementation as a learning tool. Because AI can generate

[24:14] solutions so quickly, don't just accept the first draft.

[24:22] Instruct the AI to tear it down and reimplement it.

[24:24] Ask it to document its logic for why it approached it differently and what is learned in the process. This is incredibly useful for checking assumptions, seeing where context may be missing and for thinking through the implications of different approaches.

[24:32] Second, we encourage teams to do walkthroughs of "alien code" and

[24:40] system architectures and agent decisions. We have engineers explain the code or the system designs that they did not write themselves in order to help build the shared

[24:48] mental models and the theory of the system we know to be so important. Analog approaches work incredibly well here, and so

[24:56] we've actually seen teams adopt more whiteboarding to help articulate the logic in the system. For us, code is increasingly not the

[25:04] first class outcome, it's adherence to the end user goals

[25:14] and shared understanding which should be a deliberate deliverable. Third, I am sure you have all seen the increasing practice of

[25:22] using skill files and rules files, et cetera, to really explicitly codify team

[25:28] practices, expectations, and institutional knowledge into agents in a consistent way. This is something we have seen

[25:36] become critically important. We are talking about ways to engineer the context provided to

[25:44] agents reliably and at scale. Our best teams don't just use agents out of box, they create, curate, and maintain structured

[25:52] agent roles, profiles, and Giving them very specific behavioral attributes and providing them recipes to work

[26:00] inside our system. Again, being forced to consistently reflect on what What is a good behavior from an agent, that is a good way to

[26:08] remain sharp in your core engineering skills. It ensures you have an up-to-date understanding on the system you're trying to build

[26:16] and creating those feedback loops to know what is working, what's not, and how to make your agents more effective.

[26:26] Importantly, these files, the skills, the rules, the system specifications need to be treated as you would other code files, with appropriate version control, testing and observability practices.

[26:34] >> Thank you. Next, we are going to talk about GenAI Use. We want to share a little more about how our engineers are working with AI, and building the right systems for AI to be effective.

[26:46] Here we are really moving beyond an era of AI Enhancement and into AI Native engineering. This is a big mental model shift from being a Conductor of

[26:54] an individual agent to an Orchestrator of a system.

[27:00] Here we are seeing three principles emerging. Our orchestrators are managing teams of asynchronous AI agents,

[27:06] each with its own context window, each with its own specific area of responsibility, while the human software

[27:14] engineer is the one who sets the environment and directs the flow from above. Our engineers are directly and indirectly teaching these agents

[27:22] by giving them the skills that Andrew mentioned which is essentially giving them the exact recipes and tools and domain knowledge they need to

[27:30] execute their tasks. The shift to orchestration is a new skill, we need to know

[27:38] when to delegate and when not to delegate. Our top teams avoid the automation trap by establishing

[27:46] clear human baselines for their -- for their work and measuring verification overheads. To hill climb towards a win, we run experiments to find the tasks where the probability of success is highest. This allows us to keep human

[27:54] attention on the tasks we know agents can't yet perform, or where taste and judgement is really essential.

[28:02] Because evaluation cost is a new critical bottleneck, our engineers are having to deeply engage with their system thinking skills. Where we don't see enough

[28:10] success, we analyze agent traces to build shared understanding of where our system can improve, be it the usability of tools the

[28:18] agents are using, or the skills agents have been equipped with. One example is

[28:26] Adversarial Review Agents are deployed to push at decisions and push at their edge cases.

[28:34] Traces are documented, and the intent and agent rules are updated Because we've learn of what we've done. None of this is possible without the deep understanding of the underlying software systems

[28:42] while also having the AI skills to understand the strengths and weaknesses of the models and of the agents we're working with. Inside of Google, we are seeing

[28:50] substantial growth in the amount of code to be reviewed. And so we're building code

[28:56] review agents. Their goal is to evaluate functionality, reliability, performance, usability, security, and maintainability.

[29:04] Our goal is not to replace human code reviewers with AI, but rather, create tighter and

[29:12] tighter feedback loops. We want to catch as many issues as early as possible. Feed the issues back into the system, for example, documenting where incorrect assumptions were

[29:20] made, all the while also preserving human cognition for the highest value tasks. So, that's why we started creating Shepherding Agents that guide

[29:28] changes through our CI/CD pipelines, triggering Review Agents multiple times, and Risk Assessor Agents that scan

[29:36] in-flight changes and flags high-risk changes for human reviews.

[29:44] Of course, I come back to the need for Software Engineers to delegate tasks, not judgment. That's our favorite quote.

[29:52] Our Software Engineers are playing a critical role in first, helping define the expectations around topics like usability, maintainability. What do we even mean by these things? How does it differ by

[30:00] team? How is it contextually specific?

[30:06] Second, there tends to be tradeoffs between these constructs. In which situation Do we prioritize performance or usability? Applying this

[30:14] requires human judgement and taste. AI can help inform but

[30:20] In what we're considering but the judgment comes from the human.

[30:26] So how can you upskill yourself to work more effectively with Agents, and maybe more importantly how can you help your organization and your systems be ready to embrace these new ways of working?

[30:34] First, we strongly recommend upskilling on evals.

[30:42] Because verification is such a big bottle neck, you need to be confident in how you evaluate AI output. The whole of the T-shaped engineer is essential here, as

[30:50] this really requires a mix of AI, Software Engineering, User and Business skills, in order to ensure you are developing realistic, grounded, and relevant evals.

[30:58] Our Evals are also a critical artifact to ensure shared team knowledge, and a big part of how intent is captured. They help us define what Good looks like.

[31:06] Second, our top engineers are doing not just personal self-reflection, but forcing their agents to constantly reflect and document.

[31:14] We think about this a little like Agent Journaling. It is fascinating at the end of every

[31:22] day to read how your agent perceives its day. Where it got stuck in your system. Where it got confused about instructions. Where it felt the most productive.

[31:30] These reflection journals give me and all of us insights into how you can improve not just your work with the AI, for example, by giving it clearer instructions on which language

[31:38] or framework to use, but also we can improve the entire ecosystem around the agents. For example, if your agent is

[31:44] consistently having difficulty accessing an internal tool, you may have a tool usability problem worth solving.

[31:52] Third and I know we've said this a couple times already, we want to build teams of agents. Now is the time to really lean

[32:00] into the opportunity to scale beyond a single agent to a balanced team with strict roles and protocols.

[32:06] We are doing this right now inside of Google, for example, with some migrations we have been doing around TensorFlow. This is highly complex, delicate

[32:14] work. Instead of using a single chatbot, our team deployed a strict three-agent architecture:

[32:22] One, a planner agent that generates verifiable migration steps, an Orchestrator agent that groups those steps, and a Coder agent that executes them.

[32:32] Our top performing teams scale beyond single agents by codifying their own best practices, for example around stylistic rules and coding preferences.

[32:40] In the Tensorflow migration example, different playbooks are fed into the agents to ensure a migration in one product area like YouTube uses YouTube

[32:48] specific practices. Another thing to consider here is agent sprawl. For example, some argue that you should stick to three to five

[32:56] agents so you can meaningfully track the work. I think we are generally aligned with this as a sweet spot but we are seeing more and more tools

[33:04] emerging to support the mutli-agent system management, With increasing number of agents

[33:12] and we think some techniques we've discussed so far can help you explore additional scale.

[33:14] This leads us to our final point. We cannot rely on vague prompts and expect high quality outcomes.

[33:20] We need precision engineering. Here is where we are seeing spec driven Development, where product

[33:28] thinking and architectural decision making are made explicitly grow in importance.

[33:36] Goals, Constraints, Rationale become critical context not just for the agents executing tasks, but really for the broader team.

[33:43] The Specs, combined with the agent rules and skills, are the source of truth for what and the why of the system you are building.

[33:50] Here they are documented to guide agents at scale and support system understanding and maintainability.

[33:58] >> All right. So we have really implicitly talked about adjacent skills already, because really all of these capabilities are interacting with each other all the time.

[34:06] Take the Review Agent as a clear example of combining all four domains.

[34:10] But let's now move to the left wing of our T. Adjacent

[34:18] Engineering wing. We are talking about domains like cybersecurity, privacy, industry-specific regulations, and deployment infrastructure becomes so important.

[34:26] If your organization has a high-quality internal platform, strong APIs, and clear well document ed workflows, AI acts as a powerful

[34:34] collaborator. But if you suffer from fragmented tooling, siloed data, or fragile infrastructure, AI

[34:42] won't save you, it will simply help you generate technical debt faster. There's some wonderful research from our DORA team that really speaks to this point.

[34:50] AI is an amplifier and it is a mirror. It magnifies the existing strengths and It holds up a mirror to those weaknesses.

[34:58] This Adjacent Engineering wing is where AI is most likely to introduce quiet, catastrophic debt if left unchecked.

[35:08] And so let's talk about three principles to help mitigate this.

[35:13] First of all, our story of the search PMs is highly relevant here too. Embedding best practices directly into high quality

[35:20] internal platforms allowed us to get features into production without explicitly authoring each line of code.

[35:30] That requires many adjacent skills understanding the deployment environment, the security needs, as well as the deep core software engineering skills.

[35:36] We've already discussed. One of the statistics we are most proud of is that while we have seen increases in the

[35:44] amount of code being written by AI, we have not seen any measurable increase in outages or decrease in system reliability.

[35:50] What we want is 10x the velocity without the 10x the risk. One way that we have achieved

[35:58] this is by creating tiered risk environments. We recognize that different applications require different environments. For example, an internal Google

[36:06] Application doesn't need to scale to a billion users.

[36:08] So our goal is to get from a prototype, to production in a more incremental and iterative

[36:17] fashion. We are moving through different risk profiles, while still

[36:26] achieving faster and faster feedback loops This also speaks to other adjacent software engineering skills, like effective experimentation. When features are moving through

[36:36] your system faster and faster, how do you get them out to users in a way that isolates features appropriately or prevents

[36:44] And understand how they're performing. Thinking through these

[36:48] environments is a critical

[36:56] Architectural and is how our engineers engage in. So how do we actively build these adjacent engineering muscles while keeping up with the pace of change? First, we highly encourage a culture of blame free post-mortems.

[37:04] To build truly resilient systems, you need to make a habit of documenting, reading,

[37:12] and importantly discussing outages and incidents. This builds your intuition for edge cases, scale limitations, and reliability threats. It is also invaluable context as

[37:20] you think about how to steer and guide your agents. For example, triangulating these resources with agents

[37:28] self-reflections and As Nicole discussed and observability traces allows you to see where edge cases may be getting exposed, or system instructions are unclear.

[37:36] Second, don't just use AI to build, use it to stress test. Going back to our points around balanced agent roles, explicitly

[37:44] setting up red team agents allows you to see your system through the eyes of malicious actors. Having your agents explain how

[37:52] it would exploit the system forces you to engage with these exploit mechanisms. Rather than passively accepting

[37:58] solutions, you begin training yourself and your agents to spot the vulnerabilities that your generation agents are missing.

[38:08] Now, we've covered this already is really the interesting rise in analog approaches to system

[38:16] architectures and datamaps. Like previously mentioned, white boards are at a premium, with a real focus on thinking through the initial architectures. By manually tracing pipelines, you can build mental models of

[38:25] things like enterprise compliance before code is actually written. Codifying your intent on a

[38:33] whiteboard is a great way to challenge initial assumptions and ensure your agents have the right context going into execution.

[38:39] Finally, observability is a critical piece of the puzzle. In a world where you are generating

[38:47] features at 10 times the speed, You have to monitor those to understand how things are actually behaving in the wild. We found some of our earlier

[38:55] career developers were getting blocked by opaque performance metrics, like subtle system health regressions. They didn't know how to diagnose the complex, distributed systems

[39:03] they were deploying to. And so what we did is we

[39:11] invested in more observability tools, and unified data agents with access to code, error logs, performance dashboards, stack traces, and more, we were able to empower engineers to better

[39:19] interpret and understand the complicated systems. This to me is another nice example of not just using AI to

[39:25] build but using AI to understand. Okay, this now brings us to our last capability in our T and

[39:33] that is Adjacent Non-Engineering skills. This is in alignment with user and business needs. Now that Agents are able to

[39:41] handle more of the routine task execution our software engineers now have the mandate to focus more heavily on the what and the why.

[39:47] But we want to acknowledge. For many of us, this is an uncomfortable shift. Our DORA research highlights that many developers are

[39:55] currently feeling a very real 'identity threat. Historically, we derived immense intrinsic value just from the sheer craft of writing code.

[40:03] We need to shift how we measure our worth. We have to lean into the broader value of our work, which comes from solving real human problems

[40:09] and real business problems. Our engineers are increasingly acting as value translators and

[40:19] taking the user needs and business needs to precise requirements. They act as Value Translators. While agents can write flawless sorting algorithms they cannot

[40:27] experience your user's frustration. Consider a feature request to improve performance. An AI might be able to find and refactor inefficient loops. But a Value Translator first asks, "Improve performance for whom? Under what conditions?" They might look at metrics and

[40:35] discover the real pain point for a specific user segment to require the change. They then guide the AI to optimize critical code paths affecting that specific scenario.

[40:45] Here's another example of where human taste and judgment are really essential to point the AI resources in the right direction.

[40:53] I really like this quote from Peter Senge "The most effective people are those who can hold their vision while remaining committed to seeing current reality clearly."

[41:01] This perfectly captures what we are talking about with the T-shaped engineer. They have the ability to form

[41:09] that broad vision, thanks to these skills, but who also intimately knows the technical reality thanks to their engineering depth. They use the systems and

[41:17] practices we have discussed today to capture intent, maintain understanding, and ensure we never lose the context of the current reality as we

[41:23] build. Now, of course we're here today to talk about the

[41:31] T-shaped software engineer. Software Engineering isn't the only discipline that is getting more T-shaped. We are seeing this exact same evolution in our product

[41:41] managers, our UX researchers, and more.

[41:43] We shared the story earlier about our Search PMs. While the software engineers are who built the safe, reliable platform, from the PM's side: they are extending their own

[41:49] adjacent skills. They are not waiting on a designer to hand over a static mocks. They are going from an idea directly to a working system.

[41:57] This allows us to create more nimble, and more fluid teams. Now, each discipline, they still have their specific strengths

[42:05] and role to play, but the boundaries are blurring. For example, in one of the internal tools I work on, the

[42:13] Software Engineering, Product, They are all shipping code. But each discipline is leveraging their own unique perspective.

[42:20] The big problems are solved together, but UI paper cuts that maybe stick out more to a UX designer are just as quickly

[42:28] fixed and shipped by that designer. That is the true power of the T-Shaped era.

[42:31] Okay, we could spend a whole hour on this topic, but here's two quick tips we are seeing teams embrace.

[42:39] First, avoid the temptation to have AI synthesize all your user feedback. It is incredibly tempting to dump hundreds of user feedback logs into an LLM and ask for a summary.

[42:47] I think if done properly, there can be space for this. But much like we're seeing an increase in analogue whiteboard sessions, we are also seeing an increase in high touch user

[42:55] feedback sessions, and our engineers are really enjoying being deeply involved.

[43:01] Hearing the actual frustration Or joy in a user's voice builds profound empathy and makes the why more real.

[43:11] Second, and we've mentioned this a few times, is Spec Driven development, really treat your spec as your ultimate product deliverable.

[43:17] Our best teams are fiercely protective of their specifications. A lot of their cognitive energy goes into debating the goals,

[43:25] the business logic, and the edge case constraints. Forcing this clear articulation

[43:31] early and in the open has really ensured teams get aligned on the why and ensuring our agents have access to nuanced institutional knowledge.

[43:39] When everyone can prototype at lightspeed, taking a few minutes

[43:47] to capture intent prevents exploration from turning into chaos.

[43:51] And because they treat these specs like code, tools like our Quality Agent can be used to stress test requirements or look for logical collisions before a

[44:01] Execution has begun. >> Okay, now we're going to pull it all together. When you combine the deep expertise to catch the AI's

[44:09] mistakes, the skills to orchestrate the fleet, the

[44:15] adjacent engineering to keep the -- to understand the system and look at the broader context to know what to build and why you have what it takes

[44:23] to thrive in the AI Era. We are talking about possessing the skills to capture and translate knowledge in a way that preserves signal to noise for both humans and agents, and

[44:33] We can have that creates a virtuous improvement system.

[44:36] Hopefully the framework, the capabilities and the pattens provides a useful way for you to think about your role or gave some inspiration for things you can try.

[44:41] We also want to take a few minutes to speak to the

[44:49] engineering managers and leaders in the room. Engineers do not work outside the org and we don't work alone.

[44:57] You can't mandate a T-shaped developer inside a broken system.

[45:01] As our DORA research shows. AI can be a harsh mirror reflecting existing organizational strengths and weaknesses.

[45:09] If you have well-aligned teams with strong practices, AI accelerates value delivery. But if you have fragmented tooling, siloed data, or a

[45:17] culture of blame, AI won't save you it will simply expose those bottlenecks.

[45:27] I love this quote from Deming: "A bad system will beat a good person every time." We are now asking engineers to

[45:33] really focus their attention on some of the hardest architectural decisions, to verify machine

[45:39] output, and to context-switch between all the time by multiple agents. That has the potential to be

[45:46] cognitively exhausting. 10x output cannot come with 10x

[45:53] cognitive load or that will burn people out.

[45:59] So, as a leader, how do you create an environment where your engineers can safely evolve? To embrace the expanding T-shaped role? We recommend three immediate shifts.

[46:03] First, redefine how you measure productivity. You have to stop measuring your teams by pull request throughput

[46:09] or lines of code accepted. We should reward outcomes and business needs that are met. We should focus on the right

[46:17] outcomes with a balanced understanding of value. For example, if we measure only speed and never quality, your developers won't take the time to

[46:24] rigorously verify the AI's output and then system instability will skyrocket.

[46:30] We strongly recommend a balanced portfolio of metrics, and there's lots of good resources out there to get you started.

[46:35] Second, actively protect the "productive struggle." We have to carve out dedicated time during work hours so our

[46:43] devs can learn these tools and understand the systems they're building. Encourage them to manually do architectural walkthroughs or experiment with a new tool or

[46:53] approach so they can learn how tools handle different problems differently. If you don't give them the space to build shared mental models, your team will drown in cognitive debt.

[47:03] Third, foster radical psychological safety. We are in an era of experimentation. Your teams are going to build agentic

[47:11] workflows that fail. If your culture punishes those failures, developers will

[47:19] rely on the skills that they have in their old safe ways of working. We need to celebrate intelligent failure and create a

[47:25] blameless post-mortem culture where the whole team learns from the mistakes in the system.

[47:31] Now, all of this has always been true, but like we've said all along, AI is a mirror and an

[47:37] amplifier, so we need this focus -- We want to conclude by

[47:45] explicitly acknowledging and Reemphasizing a few things.

[47:51] Managing an agent workforce while architecting complex systems might sound exhausting, especially since it forces us to stay exclusively in that 'high-altitude' decision space. But here is the silver lining: while the nature of our effort

[47:59] is changing, we still have that joy of building. By investing in the expanded T-shaped developer skill set, you get to see your ideas come to life at unprecedented speeds,

[48:07] And they bring you closer to the actual software that you want to create. You aren't leaving the craft of engineering behind; you are

[48:15] simply stepping up to its highest and most impactful level.

[48:19] And most importantly, I know we've said this, but it's worth reiterating, The software engineering role is not vanishing. It is evolving and becoming more important.

[48:27] So we need to shift left. We need to shift up. And we need to think about

[48:35] designing systems, not just bits of code.

[48:37] So, thank you. [Applause].

