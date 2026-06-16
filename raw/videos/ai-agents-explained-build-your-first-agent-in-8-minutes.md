---
title: "AI agents explained: Build your first agent in 8 minutes"
video_id: Zqno_vux6d8
url: https://www.youtube.com/watch?v=Zqno_vux6d8
channel: Google Cloud Tech
channel_id: UCJS9pqu9BzkAMNTmzNMNhvg
channel_url: https://www.youtube.com/channel/UCJS9pqu9BzkAMNTmzNMNhvg
publish_date: '2026-06-10T06:00:05-07:00'
upload_date: '2026-06-10T06:00:05-07:00'
category: Science & Technology
duration: '8:29'
length_seconds: 509
view_count: 22160
keywords:
  - AIAgents
  - GoogleADK
  - PythonTutorial
  - SoftwareEngineering
  - MachineLearning
  - LLMs
caption_tracks:
  - language_code: en
    name: English - CC (English)
    kind: manual
    is_translatable: true
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
chapters:
  - {title: "AI Agents Explained", start: '0:00'}
  - {title: "The ReAct Framework Explained", start: '1:05'}
  - {title: "The 3 Types of AI Agents (Sequential, Reactive, Planning)", start: '2:15'}
  - {title: "Project Overview: The Auto-Correcting Blog Writer", start: '3:30'}
  - {title: "Setting Up Google ADK & UV", start: '4:15'}
  - {title: "Coding the Planner Agent", start: '4:50'}
  - {title: "Adding Auto-Correction (Validation Checkers & Loop Agents)", start: '5:40'}
  - {title: "Coding the Blog Writer & Root Agent", start: '6:50'}
  - {title: "Testing the AI in the ADK Web UI", start: '8:20'}
description: |
  Follow the codelab → https://goo.gle/3Q5TSt3
  GitHub repo → https://goo.gle/4fsahT8 
  Google Agent Development Kit (ADK) → https://goo.gle/3Q3enqf
  
  At the simplest level, an AI agent doesn’t just answer—it decides and takes action. In this video, Smitha goes beyond basic chatbots and demonstrates how to build a fully autonomous, self-correcting multi-agent system from scratch using Google’s Google Agent Development Kit (ADK).
  
  
  First, Smitha breaks down the theory behind modern agents: the ReAct Framework (reasoning and acting) and the 3 main agent patterns (sequential, reactive, and planning). Then, she jumps straight into Python to build a practical *Blog Writing Agent*. Watch along and learn how to combine *Planner* and *Writer* agents with validation checkers and loop agents to create an AI that catches its own mistakes and automatically retries until it gets it right.
  
  Chapters:
  00:00 - AI Agents Explained
  01:05 - The ReAct Framework Explained 
  02:15 - The 3 Types of AI Agents (Sequential, Reactive, Planning) 
  03:30 - Project Overview: The Auto-Correcting Blog Writer 
  04:15 - Setting Up Google ADK & UV 
  04:50 - Coding the Planner Agent 
  05:40 - Adding Auto-Correction (Validation Checkers & Loop Agents) 
  06:50 - Coding the Blog Writer & Root Agent 
  08:20 - Testing the AI in the ADK Web UI 
  09:40 - What's Next? (Connecting to MCP Servers)
  
  More resources:
  ReAct Paper → https://goo.gle/4oa1oQ9 
  
  🔗 Connect with Smitha online:
  YouTube → https://goo.gle/Smitha-on-YouTube 
  Linkedin → https://goo.gle/Smitha-on-LinkedIn
  X → https://goo.gle/Smitha-on-X 
  
  #AIAgents #GoogleADK #PythonTutorial #SoftwareEngineering #MachineLearning #LLMs
  
  Watch more Modern AI Agents: From Theory to Production → https://goo.gle/Learn-with-Smitha
  🔔 Subscribe to Google Cloud Tech → https://goo.gle/GoogleCloudTech
  
  #AIAgents #Gemini
  
  Speaker: Smitha Kolan
  Products Mentioned: Agent Development Kit, Gemini
notes: |
  Manual English CC track used (kind: manual), segments 0-182; the fetcher also
  returned a duplicate ASR pass (segments 183-365) which was discarded. Light
  caption cleanups applied (ADK agent categories, in ADK, robust blog, writes will
  be stored). Chapter headings from YouTube macro-markers interleaved over the
  transcript. Presenter named in the video as Smitha (Google Cloud).
---

## Transcript

## [0:00] AI Agents Explained

[0:04] In this video, you're going to learn
[0:06] what AI agents are not just in theory, but in practice.
[0:10] We'll look at the ideas behind modern agents,
[0:12] and then we'll build your very first AI agent step
[0:16] by step using Google's SDK.
[0:18] By the end, you'll understand how agents reason,
[0:21] act and adapt, and you'll have code that you can actually
[0:24] run yourself.
[0:25] So what are AI agents.
[0:27] At the simplest level, an agent is
[0:29] software that doesn't just answer,
[0:31] it can decide and take action.
[0:33] Instead of generating a single response
[0:35] like a traditional chatbot, it looks
[0:37] at your request, figures out what steps need to be taken,
[0:41] maybe calls an API, runs code, looks at the results,
[0:44] and then decides what to do next.
[0:46] One of the clearest explanations comes from the research paper
[0:50] React synergizing reasoning and acting in language models.
[0:55] The idea in that paper was simple but powerful.
[0:58] Language models shouldn't just generate text in one go.
[1:01] They can actually reason step by step.
[1:04] Take an action like calling a tool or API.

## [1:05] The ReAct Framework Explained

[1:06] Observe the results and then decide what to do next.
[1:09] That cycle of reasoning, acting, observing, and adjusting
[1:14] is the foundation of how modern AI agents work, and it
[1:18] lines up with how it's defined.
[1:20] Systems with reasoning, planning, and memory
[1:23] with enough autonomy to adapt and make decisions
[1:27] on behalf of the user.
[1:28] Now, not all agents behave the same way.
[1:31] A useful way to think about them is in three broad patterns.
[1:35] First, we have sequential agents.
[1:37] These run step by step like an assembly line.
[1:40] Step one, then step 2, then step three.
[1:43] They're predictable but rigid.
[1:44] Second, we have reactive agents.
[1:46] These decide in the moment.
[1:48] They look at the current state and ask, what should I do next.
[1:50] Maybe tool a one time tool B the next.
[1:53] They're flexible, but they don't plan ahead.
[1:55] Lastly, we have deliberate or planning agents.
[1:58] These pause to sketch a plan then execute.
[2:02] Think about booking travel.
[2:03] You don't just buy a flight randomly.
[2:05] You pick dates, hotels and then that's the order of steps
[2:08] that you follow through.
[2:09] So which of these is the right one for you.
[2:12] It depends on the problem.
[2:13] For simple, predictable flows, sequential

## [2:15] The 3 Types of AI Agents (Sequential, Reactive, Planning)

[2:16] is fine for dynamic, reactive works better.
[2:19] And for multi-step goals with dependencies
[2:22] you want planning agents.
[2:24] OK, that's the high level view.
[2:25] Now let's actually build an agent.
[2:27] So you can see these ideas in action.
[2:30] We'll build a blog writing agent.
[2:32] You give it a topic, it will generate a structured outline,
[2:35] turn that outline into a full blog post,
[2:38] and then suggest the alternative titles and hooks.
[2:41] This is where ADK's agent categories comes in
[2:43] as we walk through the code, notice how the planner
[2:46] and writer agent are LLM agents which are powered by a model.
[2:51] They are wrapped in loop agents, which
[2:53] are workflow agents in ADK.
[2:55] These handle retries automatically
[2:57] if validation fails, and if we ever wanted something
[3:01] beyond that, ADK would also let us extend a custom agent
[3:05] by subclassing the base agent.
[3:08] So let's set up the environment and then go line by line
[3:10] through the code.
[3:11] First off, you need to install UV.
[3:13] You can do that by running the command right here.
[3:16] Secondly, you need to install Google ADK because we need
[3:19] to obviously use ADK in this.
[3:21] And then let's create a file called agent in your Ide.
[3:26] We need to import these key libraries.
[3:28] And then we can start building out our very first agent.

## [3:30] Project Overview: The Auto-Correcting Blog Writer

[3:32] So the first agent that we're building out
[3:33] is called the blog planner.
[3:36] Its only job is to take a topic and turn it
[3:38] into a structured outline.
[3:40] We give it the name blog planner so it's easy to identify,
[3:44] and we tell it which model to use,
[3:46] which comes from our environment file.
[3:48] The description is just a human readable note.
[3:51] The important part of the introduction is here.
[3:53] We actually tell it what to produce,
[3:55] which is a markdown outline with a title, a short introduction,
[3:59] four to six sections with bullet points, and a conclusion.
[4:02] By spelling that out, we make the output much more reliable.
[4:07] Finally, look at the output key.
[4:09] We set it to blog outline.
[4:11] This means whatever this agent writes
[4:14] writes will be stored in shared state under that name,

## [4:15] Setting Up Google ADK & UV

[4:17] so that the next agent that can pick it up
[4:19] can do it automatically.
[4:21] Next, we add a second agent.
[4:23] The outline validation checker.
[4:25] This one doesn't write anything new.
[4:27] It just checks the outline.
[4:28] Its instruction is strict.
[4:30] If the outline in state has a title, an intro,
[4:33] four to six sections, and a conclusion,
[4:36] it must answer with the word OK.
[4:38] If something is missing, it must answer with the word retry
[4:42] and explain what's wrong.
[4:43] That way, we can automatically decide
[4:45] whether to accept the outline or try again
[4:48] to connect the planner and the checker.

## [4:50] Coding the Planner Agent

[4:50] We've wrapped them inside a loop agent called robust blog
[4:54] planner.
[4:55] The loop first runs the planner, then the checker.
[4:58] If the checker says OK, we're done.
[5:00] If the checker says retry, the loop runs the planner again
[5:04] with the same instructions.
[5:05] It can do this up to three times.
[5:07] This gives us a safety net.
[5:09] So if the model forgets something,
[5:10] it has another chance to get it right.
[5:13] Now we create another agent called blog writer.
[5:16] This one takes the outline we just saved in blog outline
[5:19] and turns it into a full markdown blog post.
[5:22] The instruction tells it how to write.
[5:25] It should assume the audience is software engineers.
[5:28] Skip the basics and focus on practical insights.
[5:31] Explain both how and the why and include short code snippets
[5:36] where helpful.
[5:37] It should also follow the structure of the outline
[5:39] with proper headings.

## [5:40] Adding Auto-Correction (Validation Checkers & Loop Agents)

[5:40] The finished draft is saved under blog post in shared state.
[5:45] Ready for the next step.
[5:46] Next up, we're going to add another checker,
[5:49] this time for the post.
[5:50] It's called blog post validation checker.
[5:53] It looks at blog post and checks if the article has
[5:57] an introduction as sections that match the outline, a conclusion,
[6:01] and clear explanations.
[6:03] If it passes, the checker says OK.
[6:06] If not, it says retry and list the fixes which are needed.
[6:10] Just like with planning, we combine the writer
[6:12] and its checker into a loop agent called robust blog writer.
[6:18] This makes the system automatically
[6:19] retry the writing step until the validation passes.
[6:23] Up to three times.
[6:24] Now we wrap each loop, the robust blog planner
[6:29] and the robust blog writer as tools.
[6:32] This is what lets the root agent call them directly
[6:35] without worrying about what's happening inside.
[6:37] Finally, we put it all together with the root agent
[6:40] called blogger.
[6:41] The instructions for blogger are simple.
[6:44] When a user gives it a topic first
[6:46] it calls the planner tool to make an outline.
[6:49] Then it calls the writer tool to draft the full post.

## [6:50] Coding the Blog Writer & Root Agent

[6:52] And finally it adds three alternative titles
[6:56] and two tweet length hooks.
[6:58] The root agent only has access to the two tools.
[7:02] We exposed the planner and the writer.
[7:05] So its workflow is clear and controlled.
[7:08] You give it a topic, it plans, it writes, it checks,
[7:12] and then it gives you a polished blog post.
[7:15] You've now successfully written your first agent script.
[7:18] The next step is to actually run it.
[7:20] Head into your terminal and launch it using this command
[7:24] with ADK web so you can view everything inside a simple UI.
[7:28] Once that's running, open the local ADK web link
[7:31] in your browser and start interacting with the agent
[7:34] directly.
[7:35] To kick things off, I'm going to ask
[7:37] it to generate a blog on the top 10 use cases for AI agents.
[7:41] Let's see how it plans, writes, and delivers the results.
[7:45] Your subagents will then work together to create a blog post.
[7:49] And that's it.
[7:50] You've built and run your first AI agent with Google's SDK.
[7:54] We've started from the idea of what agents are, then walk
[7:58] through the code step by step and finally saw
[8:01] it come to life in terminal.
[8:02] Thank you for watching.
[8:03] Check out the description box for all the resources and code
[8:06] mentioned in this video.
[8:08] Check out this next video to learn how to connect your AI
[8:11] agent to an MCP server.
