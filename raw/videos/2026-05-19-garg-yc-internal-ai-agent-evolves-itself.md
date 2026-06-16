---
title: "How to Build an Internal AI Agent That Evolves Itself"
video_id: DGD9b8K42lk
url: https://www.youtube.com/watch?v=DGD9b8K42lk
channel: YC Root Access
channel_id: UCxIJaCMEptJjxmmQgGFsnCg
channel_url: https://www.youtube.com/channel/UCxIJaCMEptJjxmmQgGFsnCg
publish_date: '2026-05-19T11:22:57-07:00'
upload_date: '2026-05-19T11:22:57-07:00'
category: Entertainment
duration: '05:34'
length_seconds: 334
view_count: 6606
default_language: en
is_live: false
is_family_safe: true
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
description: |
  AnswerThis builds AI agents for evidence-based scientific workflows and has scaled past $2 million in ARR with just two full-time employees — largely because they built an internal AI ops agent that processes over 100 emails a day, closes support tickets, and updates their CRM automatically. In this recent batch talk, founder Ayush Garg breaks down the architecture of a self-extending agent that builds its own tools when it encounters tasks it can't handle yet, how his non-technical co-founder trains the agent by giving it feedback in Slack, and the three types of memory — factual, behavioral, and procedural — that any founder can copy to build an internal agent for their own business.
notes: |
  Acquired via yt-dlp fallback (auto-captions) on 2026-05-21; the youtube-transcript-skill
  Playwright path hit the panel-render failure documented in GH #2 (Page.wait_for_function
  timeout). Light ASR cleanup: VTT rolling-overlap deduplicated; segments regrouped into
  ~3–4-sentence paragraphs with timestamp anchors at each paragraph boundary. Original VTT
  preserved at /tmp during ingest.
---

## Transcript

[00:03] Hello everyone. My name is Ayush. I'm the founder of Answer This. We build AI agents for evidence-based scientific workflows, and today I'm going to be sharing about how we're using AI agents internally and how you can replicate our setup.

[00:13] So, we've been able to do over $2 million in ARR largely being two full-time employees, which is myself and my co-founder. Do have two or three contractors for things like design and outbound, but a large reason for why we've been able to do this is because we have an internal AI ops agent that handles a lot of the work that would normally consume founder time. So, this AI agent is processing more than 100 emails a day for us, has closed over 400 customer support tickets. It handles CRM updates after meetings.

[00:45] It collects user feedback across channels, helps with things like customer support, but more importantly, as Pete and Tom and Gary mentioned, it also lets us ask questions about our business at any time. Things like, "What's the status of a lead?" or "What are the open issues for a customer?" This has become instantly queryable for us, whereas previously, you know, we had to operate a bunch of different apps to get answers to our question. Now, the most important part of this is not that the agent can do a fixed set of tasks, is that the agent is self-extending. When it runs into a repeated task it cannot do yet, it asks a coding sub-agent to build a tool for it, and this tool becomes permanent and is available in future sessions.

[01:33] So, let me talk through the architecture for how you can set this up. The first thing you should do is have a Claude code CLI wrapped in Python, where new messages from Slack, email, and other channels go into a task queue. The agent picks up these tasks and then works through them iteratively. Now, Pete, Gary, and Tom have already mentioned why you need a thin harness, so I'm not going to repeat it, but Cloud Code works exceptionally well because it already knows how to inspect files, run commands, and use CLIs.

[02:05] Which brings me to my second point. How do you tell it business logic that only you know of? A great way that we've found to be able to do this is by giving the agent a read-only copy of both our database as well as our code base, where it has a cron job that basically gives it an updated version every time we do a release. And whenever a customer support query comes now and they ask some question about the business, the agent can just read our code base to be able to figure that out, including things like what our subscription logic is and where things inside of our app are located.

[02:39] Now, what actually makes it self-evolve? There's two very important components here. First is all the tools that we use as a startup, things like, you know, Intercom, Fathom, Stripe. We have given all of those as CLIs to our main agent.

[02:55] But at the same time, it has a general coding agent also as a CLI, which can edit the agent code itself. And what this means is that whenever we ask it to do a task it cannot do yet, it is simply able to just code that tool into existence and handle the task. To us it's magical because we only ask it to do things, but it's able to self-author tools and has gone from just being a skeleton to being this full-blown tool with over 45 CLIs that it has made itself. A cool example for this is also when we just wanted to monitor our landing pages to make sure they're always up for ads, and we just sort of told it and it created a cron job into existence that does this.

[03:35] Now, moving slightly further, there's one very important thing that also this agent needs to have, which is an editable personality or memory. We do this by an instructions.md file that is loaded on every agent turn, and the agent is able to edit this. This is how we are able to self-evolve the agent because we can give it feedback like we would give feedback to an employee and it just updates this instruction.md file which then gets appended to the next run. The best example for this is customer support.

[04:06] When we had just rolled out this agent to start doing customer support, my co-founder Ryan, who's non-technical, noticed a class of support mistakes. Instead of opening the code base or telling me or filing a ticket, he just messaged the agent in Slack and told it what was wrong. The agent updated its own instruction set and tool link and then that entire class of mistakes stopped happening again. So, the broader lesson here is that uh an internal agent needs sort of three sorts of memories.

[04:36] It needs factual memories, which is your code base and your database, things how they work operationally within your startup. It needs behavioral memories. This is what you teach the agent. It's things like instruction and feedback.

[04:49] That is what we have the instructions.md file for. And it needs procedural memory, regular tasks that you're doing. This is what we encode into the tools that the agent is able to create itself. So, if you want to copy this entire agent, just take a picture of this and give it to your cloud code and just use cloud code or any other coding capable CLI as the main agent harness.

[05:12] Give the agent read-only access to your code base. Give it some basic CLIs and then give it a coding agent as a CLI as well. Finally, load an instruction file that gets edited on every turn. You know, you can just connect it to Slack or email through SSH and you will have this agent ready for your business as well.
