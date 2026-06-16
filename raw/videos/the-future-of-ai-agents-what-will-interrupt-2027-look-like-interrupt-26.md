---
title: 'The Future of AI Agents: What Will Interrupt 2027 Look Like? | Interrupt 26'
video_id: R9K2574YEAg
url: https://www.youtube.com/watch?v=R9K2574YEAg
channel: LangChain
channel_id: UCC-lyoTfSrcJzA1ab3APAgw
channel_url: https://www.youtube.com/channel/UCC-lyoTfSrcJzA1ab3APAgw
publish_date: '2026-05-21T07:26:45-07:00'
upload_date: '2026-05-21T07:26:45-07:00'
category: Science & Technology
duration: '22:10'
length_seconds: 1330
view_count: 554
is_live: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi_webp/R9K2574YEAg/maxresdefault.webp
keywords:
- LangChain
- Interrupt 2026
- AI agents
- LangSmith
- LangSmith Fleets
- Harrison Chase
- agentic AI
- AI keynote
- no-code agents
- multi-agent systems
- open source LLMs
- continual learning
- voice agents
- AI sandboxes
- long-horizon agents
- agent identity
- LLM ops
- LangGraph
- deep agents
- AI conference 2026
- AI in the enterprise
- go-to-market AI
- sales AI
- human in the loop
- agent harness
- fine-tuning
- open models
- Fireworks AI
- AI automation
caption_tracks:
- language_code: en
  name: English
  kind: manual
  is_translatable: true
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
chapters:
- title: Welcome & Shoutouts
  start: 0:00
  start_ms: 0
- title: 'Setting the Stage: Imagining Interrupt 2027'
  start: 0:29
  start_ms: 0
- title: 'Two Types of Agents: Long-Horizon vs. Customer Experience'
  start: '1:22'
  start_ms: 0
- title: The Future of Voice Agents
  start: '2:42'
  start_ms: 0
- title: Why Every Agent Needs a Sandbox
  start: '3:58'
  start_ms: 0
- title: The Rise of Open-Source Models
  start: '4:47'
  start_ms: 0
- title: Agent Identity & Auth Patterns
  start: '6:01'
  start_ms: 0
- title: 'Continual Learning: Model, Harness & Context Layers'
  start: '7:26'
  start_ms: 0
- title: Announcing LangChain Labs
  start: '10:42'
  start_ms: 0
- title: Updates to LangSmith Fleet
  start: '11:00'
  start_ms: 0
- title: How LangChain Builds Agents Internally
  start: '12:39'
  start_ms: 0
- title: 'Fleet Demo: Go-to-Market Agent'
  start: '13:40'
  start_ms: 0
- title: 'Fleet Features: Tools, Channels, Governance'
  start: '19:05'
  start_ms: 0
- title: Closing
  start: '21:28'
  start_ms: 0
description: "Harrison Chase, Brace Sproul, and Caroline di Vittorio kicked off Day 2 of Interrupt 26 with an inside look at where AI agents are headed, the unveiling of LangChain Labs, as well as the latest features in LangSmith Fleet. \n\n0:00 Welcome & Shoutouts\n0:29 Setting the Stage: Imagining Interrupt 2027\n1:22 Two Types of Agents: Long-Horizon vs. Customer Experience\n2:42 The Future of Voice Agents\n3:58 Why Every Agent Needs a Sandbox\n4:47 The Rise of Open-Source Models\n6:01 Agent Identity & Auth Patterns\n7:26 Continual Learning: Model, Harness & Context Layers\n10:42 Announcing LangChain Labs\n11:00 Updates to LangSmith Fleet\n12:39 How LangChain Builds Agents Internally\n13:40 Fleet Demo: Go-to-Market Agent\n19:05 Fleet Features: Tools, Channels, Governance\n21:28 Closing\n\nExtra resources:\n• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview\n• Meet LangSmith Engine: https://www.langchain.com/blog/introducing-langsmith-engine\n• About LangChain: https://www.langchain.com/"
notes: Transcript fetched via youtube-transcript-skill (Playwright path); manual English captions used where available.
---

## [0:00] Welcome & Shoutouts
[0:06] I don't know about you guys, but this is the coolest tech conference I've ever been to. And I have had nothing to do with it.
[0:12] So before we get started, I do want to shout out everyone who's working behind the scenes, in particular, Jess, Julia, Jacob, and Brianna for making this event fantastic.
[0:21] So let's give them a big round of applause. Chapter 2: Setting the Stage: Imagining Interrupt 2027

## [0:29] Setting the Stage: Imagining Interrupt 2027
[0:29] Now yesterday, we talked a lot about what building agents today looks like and how a lot of the most successful teams are bringing agents into production.
[0:37] And so for today, I want to talk a little bit about the future.
[0:41] One of the things that we think a lot about at LinkedIn-- it's actually in our mission and vision statement-- is what do the agents of the future look like?
[0:50] And so for the rest of this talk, I want to pretend like we're a year in the future. It's interrupt 2027.
[0:57] And what are the topics that we're going to be talking about? What are the topics we're going to be discussing? And I'm going to be wrong in a lot of these. This is going to look really silly and really stupid.
[1:05] 1 minute, 5 seconds But hopefully this gives you a glimpse into where we think that the space in the industry is going.
[1:14] 1 minute, 14 seconds One thing that I think will start to happen is there will be a divergence in the types of agents that people are building.
[1:21] 1 minute, 21 seconds So I think there will be two types of agents, and we're already starting to see some of this emerge. Chapter 3: Two Types of Agents: Long-Horizon vs. Customer Experience

## [1:22] Two Types of Agents: Long-Horizon vs. Customer Experience
[1:26] 1 minute, 26 seconds So one of the types I think will be these long horizon style agents.
[1:30] 1 minute, 30 seconds So these are agents that run for minutes and hours and maybe even in the future days. They do code execution. They do planning. They use subagents.
[1:38] 1 minute, 38 seconds They maybe use multi-agent systems. They use skills. And they operate over longer and longer time horizons.
[1:44] 1 minute, 44 seconds Things like outcomes and goals are starting to become ways to increase the horizons at which these can operate.
[1:52] 1 minute, 52 seconds And so I think we'll see a big push in these is they do more and more valuable knowledge work.
[1:57] 1 minute, 57 seconds At the same time, there's a completely different set of agents that latency is a huge factor for.
[2:04] 2 minutes, 4 seconds And these often end up looking like customer experience agents. So this could be customer support. This could be sales. This is places when you're talking to an end user.
[2:12] 2 minutes, 12 seconds Brand is really important here. Voice becomes a really interesting modality. Maybe video will in the future as well.
[2:19] 2 minutes, 19 seconds And so I think these are these two directions that agents are going in. There is a shared stack underneath.
[2:26] 2 minutes, 26 seconds There are also differences in terms of the technology.
[2:29] 2 minutes, 29 seconds And I think one of the big questions that we'll be thinking about over the next year is how common is this shared stack versus how particular are the technology pieces that you need for each? Chapter 4: The Future of Voice Agents

## [2:42] The Future of Voice Agents
[2:42] 2 minutes, 42 seconds Speaking of voice, I think we'll be talking a lot more about voice in a year. This is a place where we're starting to invest more and more.
[2:49] 2 minutes, 49 seconds We see this be particularly relevant for these customer experience style agents. voice is a great modality. The typical voice pipeline today looks something like this.
[2:59] 2 minutes, 59 seconds There's this speech to text, text to speech, kind of like sandwich.
[3:03] 3 minutes, 3 seconds So the user speaks, that's transcribed into text, that's passed to an agent.
[3:08] 3 minutes, 8 seconds The agent operates in kind of like the text space, output some text, and then that text is transformed back into speech, which is the audio that you hear from the agent as you're talking to it.
[3:19] 3 minutes, 19 seconds And so this is the pipeline that we see today, But there are these native speech-to-speech native voice models that are coming out.
[3:26] 3 minutes, 26 seconds So OpenAI released V2 of theirs, I think, two weeks ago.
[3:30] 3 minutes, 30 seconds And while I would say the consensus today seems to be for applications where you really care
[3:38] 3 minutes, 38 seconds about having control, they're not quite steerable enough yet, we do expect that to change.
[3:42] 3 minutes, 42 seconds And so I think one of the big things that we're looking at in the future for voice agents is which will it be? Will it be this pipeline approach? Will it be this native voice-to-voice approach?
[3:50] 3 minutes, 50 seconds Will it be a combination? What are the pros? What are the cons?
[3:53] 3 minutes, 53 seconds I think we'll be talking a lot more about voice in the next year or so. Chapter 5: Why Every Agent Needs a Sandbox

## [3:58] Why Every Agent Needs a Sandbox
[3:58] 3 minutes, 58 seconds We think all agents will need a sandbox, especially these long horizon style agents. So coding is really good for a variety of tasks.
[4:05] 4 minutes, 5 seconds It's not just writing software, it's for data analysis, it's for web browsing, it's for image gen, for deep research.
[4:11] 4 minutes, 11 seconds I was talking to someone yesterday who said that when they think about building agents for their marketing team, one of the ways that they think about it is they think about giving that marketing team a software engineer.
[4:21] 4 minutes, 21 seconds What would that software engineer build?
[4:23] 4 minutes, 23 seconds What apps would it build to make the marketing team's job easier?
[4:27] 4 minutes, 27 seconds That's what giving an agent the ability to write and execute code is.
[4:30] 4 minutes, 30 seconds That's why we think sandboxes are really important, and that's why we launched sandboxes yesterday. So I actually think agents are very early on.
[4:38] 4 minutes, 38 seconds Sandboxes are very, very early on. It's still just the dawn of those. I think we'll be talking a lot about them over the next year. Chapter 6: The Rise of Open-Source Models

## [4:47] The Rise of Open-Source Models
[4:47] 4 minutes, 47 seconds Open models are a place that we expect to see significant increase in over the next year.
[4:52] 4 minutes, 52 seconds So the performance of these base open models without any type of post training for particular tasks is already approaching that of frontier models.
[5:00] So this is some benchmarking that we did on deep agents comparing closed frontier models to open models.
[5:06] 5 minutes, 6 seconds And you can see that it does lag in some places, but it's starting to get really, really close to that frontier.
[5:13] 5 minutes, 13 seconds The other big thing that is happening is cost is starting to become more and more of an issue.
[5:19] 5 minutes, 19 seconds So there are multiple cases where, in particular for coding agents, these agents are burning through a ton of tokens really, really fast.
[5:27] 5 minutes, 27 seconds I think open models offer a cheap alternative to these, and we expect that to be a big driver of open models.
[5:34] 5 minutes, 34 seconds A third reason that we think open models are really interesting is because they can be trained for your particular domain.
[5:40] 5 minutes, 40 seconds And so I think that's yet another reason As companies build up a lot of these traces, a lot of these agent runs, how can you use those?
[5:48] 5 minutes, 48 seconds How can you use those to improve the model over time? I'll talk a little bit more about that in a second.
[5:52] 5 minutes, 52 seconds But this type of post-training is something that you can do with open models. And so we expect a big rise in interest in open models. Agent identity is really, really interesting to us. Chapter 7: Agent Identity & Auth Patterns

## [6:01] Agent Identity & Auth Patterns
[6:03] 6 minutes, 3 seconds So as agents start to do more work in the real world, they take actions. How do they take those actions? On whose behalf do they take those actions?
[6:11] 6 minutes, 11 seconds I think it's still early here. We see two emerging trends. One is when the agents act on behalf of individual users.
[6:18] 6 minutes, 18 seconds So if I'm accessing an agent and that agent has access to Slack and I tell it to look up something in Slack, it will use my credentials and it'll have access to whatever I see in Slack.
[6:27] 6 minutes, 27 seconds And so if Julia or a colleague uses it, they might get a different answer because it might see different things.
[6:34] 6 minutes, 34 seconds Another type of auth is when they have a fixed set of credentials, usually a service account or something like that.
[6:39] 6 minutes, 39 seconds And then whoever is interacting with that agent, they will always use that fixed set of credentials. So they'll see the same responses.
[6:46] 6 minutes, 46 seconds This, I think, started to get really, really popular with things like OpenAI, where you had this concept of an agent that was its own thing, and it had its own fixed set of credentials,
[6:54] 6 minutes, 54 seconds and you'd expose it through separate channels, and you'd interact with it.
[6:57] 6 minutes, 57 seconds And we started to see actually some SAS providers make it really easy for agents to create their own accounts so that they could have their own fixed set of credentials.
[7:06] 7 minutes, 6 seconds And so I think this will be an interesting trend to watch. I actually think we'll see both of these in the future.
[7:11] 7 minutes, 11 seconds I think we'll have agents that act on behalf of users, but also agents with their own fixed set of credentials.
[7:16] 7 minutes, 16 seconds And I think being really, really precise about when to use which one and which one which one is, and making that clear to users will be important. Chapter 8: Continual Learning: Model, Harness & Context Layers

## [7:26] Continual Learning: Model, Harness & Context Layers
[7:26] 7 minutes, 26 seconds Continual learning is maybe one of the areas that we're most excited about as a company.
[7:32] 7 minutes, 32 seconds So when we think about continual learning, we think about improving the agentic system over time.
[7:38] 7 minutes, 38 seconds And there's three layers to this agentic system, and all of them can be improved.
[7:41] 7 minutes, 41 seconds There's the model layer, there's the harness layer, and there's the context layer.
[7:45] 7 minutes, 45 seconds So the model, I mean things like Sonnet, GLM4, GPT-4, harness, this is the code surrounding the model that connects it to the environment.
[7:52] 7 minutes, 52 seconds This is deep agents, Claude Code, pi.
[7:55] 7 minutes, 55 seconds And then context might be what we provide to the harness as ways to guide it on particular tasks. So agent.md, skills.
[8:03] 8 minutes, 3 seconds You can't edit Claude Code directly, but you can give it skills and give it an agent.md that tunes it for your particular task.
[8:11] 8 minutes, 11 seconds And so these are three different layers of the agentic system, and we think all of them are involved in continual learning.
[8:19] 8 minutes, 19 seconds So maybe starting at the model layer first, this is taken from research done by Ramp and Prime Intellect that came out last week, where they fine-tuned a model to be really good at Ramp sheets.
[8:28] 8 minutes, 28 seconds And you can see here that the latency is very, very low and the accuracy is very, very high.
[8:33] 8 minutes, 33 seconds And this is an advantage of using an open source model, Qwen 3.5, and fine-tuning it for their particular domain.
[8:41] 8 minutes, 41 seconds And so this is an example of continual learning at the model level. You can also learn at the harness level.
[8:48] 8 minutes, 48 seconds So there's a great paper out of MIT and Stanford called MetaHarness, where they used an agent to optimize a coding harness.
[8:56] 8 minutes, 56 seconds They optimized it on terminal bench 2.
[8:58] 8 minutes, 58 seconds And you can see that it outperforms human-written harnesses.
[9:02] 9 minutes, 2 seconds And so this is an example where they used the feedback from the environment, the feedback from running it on terminal bench.
[9:07] 9 minutes, 7 seconds They took that feedback, they passed it to an agentic system itself that would make edits to the harness.
[9:12] 9 minutes, 12 seconds So it wasn't changing the model at all, it was just editing the harness. And they got a really good score there.
[9:20] 9 minutes, 20 seconds My backgrounds in classical machine learning, then there are a lot of similarities between how you use data there and how you use it in this new world of agent development.
[9:30] 9 minutes, 30 seconds And so in classical machine learning, You have the model, you have the training data, you do some gradient descents, and that updates the weights of the model.
[9:38] 9 minutes, 38 seconds When you're updating the agent in general, depending on the layer you're at, if you're working at the harness or context layer, it's not exactly gradient descents, but the evals that you write act as a forcing function.
[9:49] 9 minutes, 49 seconds So in the example of the meta-harness that I just gave, you have these evaluations, terminal bench two, you run the agent on terminal bench, you get some feedback, you then pass that into the agentic system and updates it.
[10:01] 10 minutes, 1 second So those evals are providing a similar type of this training gradient.
[10:06] 10 minutes, 6 seconds And so evals and traces are incredibly important for this learning.
[10:12] 10 minutes, 12 seconds We did this ourselves, and so this is a few months old at this point, and so all of these, you know, the leaderboard no longer looks like this because the space moves really fast,
[10:21] 10 minutes, 21 seconds but we moved from top 30 on terminal bench two to top five just by changing the harness itself.
[10:26] 10 minutes, 26 seconds So no changes to the model, only changes to the harness, and we saw a big increase in performance.
[10:32] 10 minutes, 32 seconds And so we think that more and more companies will be doing this type of continual learning, whether it's at the model layer, the harness layer, or the context layer, for their particular use cases. Chapter 9: Announcing LangChain Labs

## [10:42] Announcing LangChain Labs
[10:42] 10 minutes, 42 seconds We wanna help people do this.
[10:43] 10 minutes, 43 seconds And so one of the things that we're announcing today is LangChain Labs, which will be a research group inside of LangChain aimed in particular at continual learning.
[10:54] 10 minutes, 54 seconds We think that, yeah.
[10:55] 10 minutes, 55 seconds (audience applauding) (audience applauding) We think that LangSmith, with all these traces already Chapter 10: Updates to LangSmith Fleet

## [11:00] Updates to LangSmith Fleet
[11:03] 11 minutes, 3 seconds in there and all the feedback associated with it, this is a really, really solid foundation for doing this type of continual learning, whether it's at the model layer or the harness layer or the context layer.
[11:13] 11 minutes, 13 seconds And so we're excited to work with a bunch of our customers going forward in this direction.
[11:18] 11 minutes, 18 seconds The last thing that I'll say is we think that everyone will help build agents in the future. And we already see this today.
[11:25] 11 minutes, 25 seconds So we already see that everyone in an org is involved in improving the agent with feedback.
[11:30] 11 minutes, 30 seconds So you've got UX research, there's domain specialists, customer support pokes, product people, engineers, they're all giving feedback in some form,
[11:38] 11 minutes, 38 seconds whether direct feedback or by tweaking the prompts or by just debugging in Slack, they're all giving feedback that improves these agents.
[11:44] 11 minutes, 44 seconds And oftentimes it's the domain experts themselves who have the best type of feedback and know how the agent should perform best.
[11:51] 11 minutes, 51 seconds And so we think in the future, they'll be even more involved in creating these agents. we think they're actually going to be building their agents.
[11:57] 11 minutes, 57 seconds They're not just going to be giving feedback on them and handing that off to a separate team, they're actually going to be involved in building these agents.
[12:05] 12 minutes, 5 seconds We've started to see a glimpse of this at LangChain, where we have a bunch of agents created by people in all different domains and expertise.
[12:14] 12 minutes, 14 seconds And we've seen them build these over the past few months.
[12:16] 12 minutes, 16 seconds And so to talk more about what that future looks like, I want to welcome onto the stage Caroline di Vittorio.
[12:23] 12 minutes, 23 seconds (audience applauding) All right, all right, how's everyone doing? Chapter 11: How LangChain Builds Agents Internally

## [12:39] How LangChain Builds Agents Internally
[12:41] 12 minutes, 41 seconds (audience cheering) Good, good. Anyone else get sunburned yesterday or was that just me?
[12:47] 12 minutes, 47 seconds All right, Harrison painted a picture of what the future of agents in the workforce will look like.
[12:52] 12 minutes, 52 seconds I'm excited to tell you all how we're actually doing that at Langchain today. First, I'm going to start with a few use cases.
[12:59] 12 minutes, 59 seconds Our talent acquisition team sources candidates using our sourcing agent.
[13:04] 13 minutes, 4 seconds Our sales team automates outbound and account intelligence with our go-to-market agent.
[13:09] 13 minutes, 9 seconds Our marketing team researches the competitive landscape with our Intel bot.
[13:14] 13 minutes, 14 seconds And our engineering teams triage and fix incidents automatically with OpenSuite.
[13:20] 13 minutes, 20 seconds Across the company, agents are constantly running, monitoring the business, and providing real-time updates and Slack. What do all these agents have in common?
[13:30] 13 minutes, 30 seconds Well, they were all built by the LangChain team members who actually use them without having to write a single line of code. How do we do that?
[13:39] 13 minutes, 39 seconds I'm glad you asked. Chapter 12: Fleet Demo: Go-to-Market Agent

## [13:40] Fleet Demo: Go-to-Market Agent
[13:40] 13 minutes, 40 seconds They use LangSmith Fleet, our managed agent builder, which allows anyone to build agents with just natural language. They don't have to write any code.
[13:50] 13 minutes, 50 seconds Over the last three years of building agents, we've learned three main things.
[13:55] 13 minutes, 55 seconds One, the best people to build the agents are the ones who actually do the job.
[14:01] 14 minutes, 1 second Two, agents need to work where you work and have access to the same systems you use.
[14:08] 14 minutes, 8 seconds And three, as your agent scale, governance can become a bottleneck.
[14:14] 14 minutes, 14 seconds So why is it that the best people to build the agents are the ones who actually do the job?
[14:19] 14 minutes, 19 seconds Well, at the end of the day, agents are just a collection of instructions, skills, and tools.
[14:26] 14 minutes, 26 seconds And who best to codify that than the people actually doing the jobs?
[14:30] 14 minutes, 30 seconds Also, just like how all of us improve over time, fleet agents do as well. They have memory built directly into them.
[14:38] 14 minutes, 38 seconds So the more you use them, the better they become.
[14:42] 14 minutes, 42 seconds Now, in order to work in conjunction these agents, they need to have access to all the systems you use. We solve that through tools and channels.
[14:51] 14 minutes, 51 seconds We have over 200 tools built directly into fleets that cover the most common integrations that companies require.
[14:59] 14 minutes, 59 seconds We also have a first-class partnership with Arcade, allowing you to access an extra 7,500 tools out of the box to cover the long tail of your integration requirements.
[15:09] 15 minutes, 9 seconds And of course, we support everyone's favorite tool framework, MCP.
[15:13] 15 minutes, 13 seconds means you can connect your custom tools and proprietary data sources directly to Fleet.
[15:20] 15 minutes, 20 seconds Now, in order to use them easily, Fleet agents are integrated natively into Slack, Gmail, Outlook, and more.
[15:29] 15 minutes, 29 seconds So you can utilize the full power of Fleet without having to learn a new workflow.
[15:34] 15 minutes, 34 seconds We also have a comprehensive user interface, which you can use to build, manage, and run your agents directly within our app.
[15:43] 15 minutes, 43 seconds And of course, I haven't forgotten about you developers out there. We're opening up the fleet APIs.
[15:48] 15 minutes, 48 seconds So you can use them directly within your own production applications and harness all of the incredible features we've built.
[15:57] 15 minutes, 57 seconds So people working teams, these agents need to be able to work seamlessly alongside you. How do we handle that? Sharing, of course.
[16:05] 16 minutes, 5 seconds You can share and collaborate on your agents and skills directly in fleet, just as easy as sharing a Google Doc with your team.
[16:14] 16 minutes, 14 seconds When you actually go to use these agents, you need credentials and authentication management so they can connect to all your different services. And this can be really tricky.
[16:23] 16 minutes, 23 seconds Trust me.
[16:24] 16 minutes, 24 seconds Luckily, we've solved this for you in fleet, meaning you can connect all your accounts and pick which agents use which accounts depending on which user is using it.
[16:34] 16 minutes, 34 seconds Everyone still with me? We've also seen how cost can skyrocket as your agents are adopted internally.
[16:42] 16 minutes, 42 seconds So for that, we've built cost tracking and usage controls directly into the app.
[16:48] 16 minutes, 48 seconds So you can inspect exactly how much your agents and users are spending and set spend limits on them.
[16:56] 16 minutes, 56 seconds Human in the Loop is also a first class feature in Fleet.
[16:59] 16 minutes, 59 seconds So you can give your agents access to powerful tools without having to worry.
[17:04] 17 minutes, 4 seconds And of course, Fleet integrates natively with the rest of the LangSmith platform.
[17:09] 17 minutes, 9 seconds So you can look at your agent traces and see exactly how your fleet agents are operating under the hood. Finally, fleet's open.
[17:18] 17 minutes, 18 seconds It's model agnostic. So you can use your favorite open or closed source models.
[17:23] 17 minutes, 23 seconds It's built on top of everyone's favorite open source agent harness. You guessed it, deep agents.
[17:29] 17 minutes, 29 seconds And we make it easy for you to download your agent files directly into your code so you can make whatever modifications you would like.
[17:38] 17 minutes, 38 seconds Now, I'm going to hand it off to Caroline, who's going to give us a live demo. Yeah, you heard that right. Live demo of fleet. >> Thanks, Brace.
[17:46] 17 minutes, 46 seconds So we've talked--
[17:48] 17 minutes, 48 seconds [APPLAUSE]
[17:53] 17 minutes, 53 seconds So we've talked about why we built fleet and some of its capabilities. And I'm excited to show you what that looks like in practice.
[18:01] 18 minutes, 1 second So here we have our go-to-market agent.
[18:04] 18 minutes, 4 seconds This agent can surface account intelligence based on data from your CRM, your call recording platform, and your data warehouse.
[18:11] 18 minutes, 11 seconds It can research accounts and contacts, and it can draft personalized outbound emails.
[18:17] 18 minutes, 17 seconds In order to do that, we've connected it to the tools that we use here at Langchain.
[18:22] 18 minutes, 22 seconds So in our case, that's Salesforce, BigQuery, Slack, Gmail, et cetera.
[18:27] 18 minutes, 27 seconds We've written certain subagents for common research tasks that we wanted to perform.
[18:33] 18 minutes, 33 seconds And we've given it a long list of skills for step-by-step instructions of common tasks that we wanted to get right every time.
[18:42] 18 minutes, 42 seconds We've also connected the Slack channel.
[18:44] 18 minutes, 44 seconds So instead of having to come into the UI here in order to use the agent, you can use it directly in Slack by tagging @gtmagent.
[18:54] 18 minutes, 54 seconds Okay, enough said, let's run it. Here we go. Where did we leave things off with a Pied Piper account? What should our next steps be? Chapter 13: Fleet Features: Tools, Channels, Governance

## [19:05] Fleet Features: Tools, Channels, Governance
[19:05] 19 minutes, 5 seconds As it runs, this go-to-market agent has been a game changer for our team. The go-to-market team, 84% of the go-to-market team uses it weekly.
[19:14] 19 minutes, 14 seconds Lead to qualified conversion is up 240%, and it has saved on average 40 hours per month per rep.
[19:23] 19 minutes, 23 seconds Originally, an engineer had built this agent directly in code.
[19:28] 19 minutes, 28 seconds But when we built Fleet, we rebuilt this agent directly in Fleet so that the go-to-market team could own this agent's implementation entirely end-to-end without having to write a single line of code.
[19:41] 19 minutes, 41 seconds Okay. So, the agent has wrapped up. We're seeing an at-risk account. That's not great.
[19:47] 19 minutes, 47 seconds We're seeing some hesitation around pricing and recommended next steps to reengage Jared by email.
[19:55] 19 minutes, 55 seconds So let's do that. Great. Get an email to Jared, please. As Brace mentioned, human in the loop is first class in fleet.
[20:07] 20 minutes, 7 seconds So before we just send off an email to a potential future customer, this agent is going to check in with us so that we can double check the copy, make sure everything looks good before we send.
[20:17] 20 minutes, 17 seconds So let's take a look here. Let's capitalize, LangGraph. Correctly. Everything looks good.
[20:26] 20 minutes, 26 seconds pretty cool, right? Okay. Many of the agents, thank you.
[20:33] 20 minutes, 33 seconds [applause]
[20:39] 20 minutes, 39 seconds Many of the agents that we use every day here at Langchain are available as pre-built agents
[20:45] 20 minutes, 45 seconds directly in fleet. So there's a go-to-market agent, which you just saw, but also our software
[20:51] 20 minutes, 51 seconds software engineer agent, which allows you to fully own an agent that you can tag and Slack, have it write code in a sandbox, and then put up a PR for you to merge.
[21:01] 21 minutes, 1 second All you have to do to use it is create the agent, connect it to the tools that your organization uses, and then go through a short onboarding flow so it gets to know your company, and then you're good to go.
[21:12] 21 minutes, 12 seconds And with that, I'm going to hand it back over to Harrison.
[21:19] 21 minutes, 19 seconds [APPLAUSE] Chapter 14: Closing

## [21:28] Closing
[21:28] 21 minutes, 28 seconds So you guys can try out Fleet today. I use it myself for a variety of tasks. We actually added a free model in there.
[21:37] 21 minutes, 37 seconds So for a limited time, there'll be a free model.
[21:39] 21 minutes, 39 seconds And backing up what we were talking about earlier, it's an open source model powered by Fireworks, one of our fantastic partners here.
[21:47] 21 minutes, 47 seconds So we try to live what we preach in terms of open source models and also trying to have the best partners here.
[21:53] 21 minutes, 53 seconds There's a fantastic ecosystem of folks out there at the booth. And so I'd encourage you to go talk to them. So that's going to wrap it up for the keynote today.
[22:29] 22 minutes, 29 seconds [BLANK_AUDIO]
