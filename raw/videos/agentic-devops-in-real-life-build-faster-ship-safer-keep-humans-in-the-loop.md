---
title: "Agentic DevOps in Real Life – Build Faster, Ship Safer, Keep Humans in the Loop"
video_id: MtzTpoots-A
url: https://www.youtube.com/watch?v=MtzTpoots-A
channel: Microsoft Visual Studio
channel_id: UChqrDOwARrxdJF-ykAptc7w
channel_url: https://www.youtube.com/channel/UChqrDOwARrxdJF-ykAptc7w
publish_date: '2025-12-22T07:00:56-08:00'
upload_date: '2025-12-22T07:00:56-08:00'
category: Science & Technology
duration: '58:00'
length_seconds: 3480
view_count: 2445
default_language: en
is_live: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi/MtzTpoots-A/maxresdefault.jpg
caption_tracks:
  - language_code: en
    name: English (auto-generated)
    kind: asr
    is_translatable: true
chapters:
  - {start: '0:00', title: "Introductions & the evolution of DevOps"}
  - {start: '3:26', title: "What “agentic DevOps” means"}
  - {start: '6:20', title: "Demo: GitHub Copilot Agents in action"}
  - {start: '9:10', title: "Agent HQ: monitoring and steering agents"}
  - {start: '12:30', title: "Copilot + Azure DevOps workflows"}
  - {start: '18:00', title: "AI models, trust, and human-in-the-loop practices"}
  - {start: '23:30', title: "What’s new in VS Code for agentic development"}
  - {start: '30:20', title: "Demo: reviewing AI-generated PRs"}
  - {start: '35:51', title: "Security: code scanning, secret scanning & autofix"}
  - {start: '40:00', title: "Real-world pitfalls & responsible AI"}
  - {start: '48:48', title: "The productivity paradox & adoption challenges"}
  - {start: '51:32', title: "30/60/90-day rollout plan"}
  - {start: '53:05', title: "Azure’s autonomous agent for cloud monitoring"}
  - {start: '56:11', title: "Final takeaways"}
description: |
  In this Live! 360 keynote, Brian Randell and Mickey Gousset unpack how agentic AI is reshaping DevOps—from coding and code review to automation, security, and incident response. You’ll see how GitHub Copilot, agent workflows, and new Azure capabilities let teams automate the repetitive work, keep humans in the loop where it matters, and accelerate delivery without sacrificing safety.
  
  Through real demos in GitHub, Azure DevOps, Visual Studio Code, and Azure’s new “agent” preview, you’ll learn how agents collaborate with developers and IT pros, where they excel, where they fail, and how to build a practical 30/60/90-day adoption plan for rolling this out in your own organization without losing control, quality, or security.
  
  🔑 What You’ll Learn
  • What “agentic DevOps” means and how AI agents collaborate with humans
  • How GitHub Copilot Agents handle issues, PRs, refactoring, and multi-step workflows
  • Using Agent HQ to monitor, steer, and audit active agent sessions
  • How Copilot integrates with Azure DevOps for pull requests and automation
  • Security essentials: code scanning, secret scanning, and AI-powered autofixes
  • Responsible AI practices & the importance of keeping humans in the loop
  • How Visual Studio Code’s agent modes (Ask, Edit, Plan, Agent) improve developer workflows
  • Azure’s new autonomous agent for monitoring & incident response
  • A 30/60/90-day roadmap for bringing agentic workflows into your organization
  
  ⏱️ Chapters
  00:00 Introductions & the evolution of DevOps
  03:26 What “agentic DevOps” means
  06:20 Demo: GitHub Copilot Agents in action
  09:10 Agent HQ: monitoring and steering agents
  12:30 Copilot + Azure DevOps workflows
  18:00 AI models, trust, and human-in-the-loop practices
  23:30 What’s new in VS Code for agentic development
  30:20 Demo: reviewing AI-generated PRs
  35:51 Security: code scanning, secret scanning & autofix
  40:00 Real-world pitfalls & responsible AI
  48:48 The productivity paradox & adoption challenges
  51:32 30/60/90-day rollout plan
  53:05 Azure’s autonomous agent for cloud monitoring
  56:11 Final takeaways
  
  🔗 Links
  • Explore more Live! 360 sessions: https://aka.ms/L360Orlando25
  • Join us at upcoming VS Live! events: https://aka.ms/VSLiveEvents
  
  👤 Speakers: Brian Randell & Mickey Gousset
  
  #devops #githubcopilot #agenticAI #azure #vscode
notes: |
  ASR-cleaned auto-generated transcript (transcript looped; trimmed to the unique 0:00-57:43 content, 553 segments). Speakers: Brian Randell (MCW Technologies; ex-GitHub; Microsoft MVP; *Essential DevOps* co-author) and Mickey Gousset (Staff DevOps Architect, GitHub). ASR fixes: speaker names normalised (Randall->Randell; Gusay/Guousay/Vicki/Miggy->Gousset); "Aentic/Gentech"->"agentic"; "Zevos"->"DevOps"; "C-pilot/Copot/copile"->"Copilot"; "cloud sonnet 45"->"Claude Sonnet 4.5"; "codeex"->"Codex"; "Olama"->"Ollama"; "Octiverse"->"Octoverse"; "meter study"->"METR study"; "autobond"->"Autobahn"; "S sur/S um agent"->"SRE Agent". Section headings are the creator-supplied YouTube chapters. Live! 360 keynote (Orlando 2025).
---

# Agentic DevOps in Real Life – Build Faster, Ship Safer, Keep Humans in the Loop


## [0:00] Introductions & the evolution of DevOps


[0:00] Our first speaker is Brian Randell. Um he's a partner for MCW Technologies. Uh

[0:05] he was a Microsoft MVP for over 17 years before joining GitHub for a multi-year stint. Today he's a consultant working

[0:11] for Microsoft and other companies small and large. He's co-authored a few books, most recently Essential DevOps. Um and

[0:18] then our second speaker today is Mickey Gousset, staff DevOps architect for GitHub.

[0:24] He is passionate about DevOps and helping developers achieve their goals. He speaks on DevOps and cloud topics.

[0:29] And if you don't follow him on LinkedIn, you should because he's always posting these really great short little snippet

[0:35] videos of how to do things you might not have known how to do. So free high quality learning right there for Mr.

[0:42] Gousset. So thank you. And with no further ado,

[0:47] commence with your keynote. Thank you very much. [applause]

[0:55] As Angela said, I'm Brian Randell and this is my very good friend Mickey Gousset. We have a lot to cover and the

[1:01] key thing we want to cover here is we're gonna have a lot of concepts and stuff because it's keynote, but Mickey and I

[1:06] are developers first and so we are going to do a couple demos if that's okay with you. Uh that said, the slide deck has a

[1:13] lot of data in it. I will be posting the deck and I will be giving you a list to the resources where I got the numbers

[1:19] from. So there's going to be a lot of numbers and I do mention one study in

[1:24] particular on there that you can quickly Google for or or Bing it. In addition, I have a quote from Microsoft, but

[1:30] otherwise there's a lot of numbers on there that don't have attribution because you wouldn't be able to read it on the slides anyway. Those will be

[1:37] included. So please check the conference website at the end of the week. There'll be a PDF with all that there because

[1:42] part of the goal here as we talk about agentic DevOps and what that means and how it fits in is for you to go back to

[1:48] your organizations and be successful. That's our goal here. So to get started, what's our agenda? We got kind of four

[1:54] themes we want to cover. First is the arrival of the agentic into DevOps. What does that mean? Then we're going to go

[2:00] in and talk about how you integrate AI agents into your workflow. Talk about keeping humans in the loop. And finally,

[2:07] how do you level up your team in a 30, 60, 90day plan? So without further ado,

[2:12] let's get started and talk about the arrival of agentic AI and DevOps. And whenever you talk about this, you first

[2:18] got a level set on what is DevOps. This is my favorite definition that DevOps is

[2:24] the union of people, process, and products. And it's all about enabling continuous delivery of value to your end

[2:30] users. Everything you do in building a software solution. And I know this is a

[2:36] mixed audience. You're not all developers. We got some IT pros in here. We may have some data scientists. This whole keynote is for everybody. There is

[2:43] going to be a heavier developer focus because that's where we're seeing some of the core initial innovation in AI for

[2:50] DevOps. But DevOps is something that belongs to everybody. as part of the

[2:55] process of both building and delivery, but also

[3:02] deploying and managing and monitoring a software

[3:07] solution. So, literally from idea to a system being torn down, DevOps

[3:12] encompasses that. No offense to anybody in the room, but I really dislike organizations that have a I'm the DevOps

[3:18] engineer. No, DevOps is everyone's responsibility. It is an organizational

[3:24] transformation first. Now so how do we fit aentic into this Mickey? Well


## [3:26] What “agentic DevOps” means


[3:31] well that's a very good question there Brian. So we've come up with or we've found this definition of agentic devops

[3:37] right the next evolution of DevOps reimagined for a world where intelligent agents collaborate with you. And that

[3:44] collaborate word I find is very important because it's not just they're just going to go do it. They're going to collaborate with you and with each other

[3:50] and to optimize and automate every stage of the software life cycle. And when we think about this, the idea

[3:56] is that you're going to extend the people on your team through these agents. And the key is both from a

[4:04] interactive experience of the agent, but also the term you're going to hear is autonomous where you can have them do

[4:10] things automatically on their behalf. So, one of the demos we're going to do at the end for more of the IT pros is

[4:16] Microsoft has them preview what's called the SRE Agent for Azure and it has autonomy based upon your desires and

[4:24] what you want to give it to do things on your behalf on a regular basis and I'm going to demonstrate something that I

[4:29] set up yesterday and how that got here today. So, the whole point is you to focus on the work that matters and we're

[4:35] going to talk about some different situations where this plays out. Understand that we're just like you. I

[4:42] like to stay employed. I've got a 22-year-old and a 19-year-old who are at probably one of the most expensive

[4:48] stages in my life, especially because my mother's no longer around to buy them toys, clothes, um, and pay for the car

[4:54] insurance. So, fundamentally, I want to stay employed, too. Okay. So I am looking at

[5:01] how that I enable people like you and I'm basically anyone in the technology field to embrace AI safely and yes stay

[5:08] employed so you can pay the mortgage, buy food and you know like a lot of us being an indoor enthusiast although I

[5:14] know some of you are more fit than that. All right. So, we start looking at how AI is going to be shaping development,

[5:21] right? We've been seeing a lot of major milestones. Now, we have a bias, right? Mickey works at GitHub. I used to work in

[5:27] GitHub. I have a former Microsoft MVP. This is a Microsoft ccentric conference.

[5:32] So, obviously, there's a ton of things going on in AI every day. We're going to kind of highlight some things related to

[5:38] the major milestones and how they have affected what we're doing. And one of those is this evolution of agent AI in

[5:46] Copilot itself. So if we look at what happened at GitHub Universe just a few weeks ago, they announced something

[5:52] called Agent HQ. And the idea behind Agent HQ is that you will be able to use

[5:58] agents from everyone to do things on your behalf. And we're going to demonstrate that in just a second. In

[6:05] fact, you know what I realized, Mickey? What did you realize, Brian? These agents,

[6:11] they're indoor enthusiasts as well. So, they don't just know how to run, you know, a flat, you know, 60 really quick.

[6:18] We might want to get an agent started so we can prove to this is actually real and not smoking mirror. That's a great idea. Let's do it.


## [6:20] Demo: GitHub Copilot Agents in action


[6:23] So, if you don't mind, we're going to stop with the slides and Mickey's going to show you how you use GitHub Copilot

[6:29] in agent mode from the web. Okay. So we've got this application that we've

[6:35] written that's int net 8. And unfortunately if you look at how we did a lot of our naming in this application

[6:41] we actually put the version of net in the name of the files and the name of the folders and all kind of places.

[6:47] My bad. Brian did that. So we want to fix this right. And I could go in there and fix

[6:53] it manually. I could tell Brian to fix it manually but that's I mean that's going to take a while and it's very much drudgery work. So

[7:00] instead, we're going to make use of Copilot coding agent to help us out with this. And there's multiple ways that we

[7:06] could ask copilot coding agent to do this. And one of them is simply to create an issue, a work item in the

[7:13] repository. So here I have created an issue and I've given it a title, you know, prepared net 10 upgrade and I've

[7:20] given some basic instructions of what I want it to do. Find all the places it finds eight and just remove it so that

[7:26] we're no longer being tied to a specific version of net. And then all I do is come over here to assign assignees and

[7:33] assign it to copilot. And by assigning it to copilot, it then prompts me with a couple of pieces of

[7:39] information. Make sure I'm in the the right repository where I want it to create a pull request. What branch? I

[7:44] could have other custom agents that I also use for this. I don't have any right now, but I could. And I could also

[7:50] provide other prompt instructions. And then I simply click assign.

[7:56] And then finally, we create the issue. And by creating the issue

[8:02] in just a moment here, Copilot's actually going to should pop up some little eyeballs here for us to show us that it's actually picking this up.

[8:10] Are you using Cloudflare on your phone? I'm not on my not on my phone right now. There you go. Oh, there you go.

[8:16] There we go. Okay, I'm off. Oh, Copilot's unavailable. Service is temporarily unavailable. Please try

[8:21] again. Did it really say that? That's exactly what it says. average.

[8:27] Well, then guess what? We plan for these things. So, by planning for these

[8:33] things, what you actually end up getting. So, let me go to the other end and we will open up and see the lovely turkey

[8:39] that I met by being Julia Child's is you end up with, like I said,

[8:44] Copilot comes out here and it's going to throw some eyeballs at it. And then it starts it will go and create a pull

[8:51] request where then that pull request is it's going to start grinding in the background. It's going to start

[8:56] evaluating the instructions I gave it and start looking at the files, start looking at the folder, start making those changes,

[9:02] make doing tests, trying to verify everything works and then it finally comes back with a pull request where I

[9:08] can review those changes. Why don't you show them go to Agent HQ? So go to the hamburger menu and then go


## [9:10] Agent HQ: monitoring and steering agents


[9:14] over to agents and go to your past runs. And what it can show you is that

[9:20] you can get this breakdown of what's going on. First of all, you could interact with it in real time,

[9:26] but also you have the history of what happened in that session. Um, and so one of the things about interaction in real

[9:31] time, you can actually steer it. You if you see it doing something, you go, "Oh, wait, wait, wait. I want to have you do this." You can actually interact in a

[9:37] conversational fashion in that session. So you could let it be autonomous. just go do the work and then have the reveal

[9:43] when it's done or you can actually be a part of it. It's really up to you. Um any love there?

[9:49] Oh, look at that. Oh, wait. Yeah, there we go. Oh, is it running? It's it's starting. Okay, it came back. So, he is actually

[9:56] going to run that there. Now, this is a feature that is part of GitHub Copilot when using um GitHub with your code.

[10:04] Anybody use Azure DevOps? All right. Who loves you? I love you.

[10:11] So, let me come over here and I'm going to go to my browser and sure we got

[10:17] GitHub, but I've also got Azure DevOps and it turns out that

[10:22] Microsoft is bringing Copilot agents to Azure DevOps. Now, yeah, I think now a

[10:29] couple things about it. It is in preview and it's what they call private preview. They did a kind of hey, who wants to try

[10:35] it? And they got guess what? Enormous response from customers like you. So,

[10:40] you can't get it right now today. That said, it's Ignite week. Maybe it'll open

[10:45] it up further. We'll see. But the bottom line is once it's available, what you'll be able to do is you go into your team

[10:51] project in Azure DevOps. And let's make the font a little bigger. There we go. And what you do is you come over here

[10:58] and yes, there is a GitHub component because it is GitHub copilot. GitHub is the the center of the universe

[11:05] for Microsoft's developer agentic tooling. Um and while it integrates with

[11:10] different places like Azure and in this case Azure DevOps, you still have to link it up to GitHub. So that is one of

[11:16] the things to be aware of. And what you do is in the world of GitHub, we manage

[11:21] Copilot agents access on a repository basis. In Azure DevOps, you can have a

[11:27] team project which has multiple repositories. So you have to decide how you want to link things. You'll see I've

[11:33] already done that. I've linked a specific repo on the GitHub side that has Copilot enabled just like Mickey

[11:40] did. But now I can come over here and just like if I was in GitHub, but now with Azure DevOps, I can say let's

[11:46] create a new work item and let's say add Aspire

[11:56] to reading time.

[12:01] And we're going to come over here and make sure I'm logged on as the right version of Brian. I am good. And we'll

[12:09] come over here and we will save. And we'll be committed.

[12:18] Do lots of magic. Okay. And then what I'll do is I'll come over

[12:24] here and we'll go back to work items and we'll add a new task. Now again you


## [12:30] Copilot + Azure DevOps workflows


[12:31] could do this with the PBI. I just defends my sensibility to actually have the work associated there. And we'll say

[12:37] add the latest compatible version of Net Aspire. Even

[12:45] though they renamed it to Aspire, I'm still going to call it Net Aspire. SP uh spelling's hard

[12:53] to the web app. If you'll notice right there, all of a

[12:58] sudden I have a Copilot. And so I will come over and click the dropdown and say create poll requests with GitHub Copilot.

[13:06] Now it's going to say no work on data available for show the work on content. Try again. Oh, you mean you want me to

[13:12] tell you what to do? Oh, all right. Please add Net Aspire

[13:22] support to the web app and all its goodness.

[13:32] And of course, the world's not complete without emoji.

[13:37] Save. And now the pull request picks the GitHub repository because your

[13:44] team project can point to repositories. You can change it if you've picked the wrong one. And then finally, special

[13:50] instructions. Make it simple, make it fast,

[13:55] keep it safe, keep it secret. So, what's happening behind the scenes?

[14:02] It is talking to GitHub and it is spinning up an agent. You'll see it's

[14:08] right there spinning. What we're going to do is we'll come back and check on this in a little bit. But these are both

[14:14] real-time things. We're both working on the same repo, but it's git. So we've got branches and we've got two agents

[14:22] working on our behalf while we sit stand here and pontificate about the good end of AI. Switch back.

[14:27] Switch back to me just a second. are you I just want to show yeah I just want to show something which is so here we are in what we're calling

[14:34] Agent HQ where we've got a centralized location where we can see when we kick off all these different Copilot coding

[14:40] agents what's going on but what I want to show you is you can see here that it's you know going through doing all

[14:45] this stuff uh reading running tests running bash scripts but you have the ability right here steer active session

[14:51] while Copilot is working so as you're reading through this as this as this is running and doing something if you

[14:57] realize oh I forgot to tell it something or oh, I see I saw it do something. I needed to do something a little bit different. You can add those

[15:03] instructions while it's running. It will pick those up and incorporate those into what it's doing. Fantastic. And because he showed it, I

[15:10] now have to do it there. Here's Agent HQ for my account and it's doing my work on

[15:16] my behalf. So whether you're in GitHub as your day-to-day hosting experience or if you primarily want to use Azure

[15:22] DevOps as long as you put your code over in GitHub, you can get the same Agentics

[15:28] AI experience that we have in GitHub. And this includes all the new stuff, which means for example, I can have the

[15:34] copilot agent, but I also can use the Codex agent. That's a new enhancement I'll show you a bit later. So let's let

[15:40] this run for a bit and we will come back to the story we need to tell on how you're going to do this in your job. So

[15:47] GitHub universe was a big step because that's where it introduced this Agent HQ this extension of the the Copilot uh

[15:53] agent experience Claude Sonnet 4.5 that was a big thing right when you are

[15:58] looking for agents and you're looking for a way to have these team members be

[16:06] intelligent they're intelligence is driven two ways number one it's driven by the foundation of the model it's

[16:13] using also refer to the big models as frontier models And Sonnet is definitely one of the better ones out there. I am a huge fan

[16:19] of this. I use a lot. That's my personal bias. As I told some people in the previous talk, uh I hang out on Reddit a

[16:26] little bit. And if you hang out on Reddit, you will find people every day who hate a particular model and who love a model. Now, sometimes the people who

[16:33] love it feel like they're astroturfy. Uh but the reality is that it's a personal choice. It really is. You're going to

[16:39] have to use the models with your code and figure out what works best. Okay? Most of the models work really well with

[16:46] a lot of the most popular languages. Right in the state of the Octoverse report for 2025, the most popular

[16:53] programming language in the world right now is Typescript, which is the compiled version of JavaScript that Microsoft

[16:59] puts out. That's pretty impressive. Python, I believe, is still number two. Um, and then beyond that, it gets

[17:05] there's always a fight going on. Uh, the year before it was really weird. Terraform's language, uh, HCL was just

[17:11] hugely popular. And believe it or not, Bash scripts are amazingly popular. So, take that for what it is. Um, and the

[17:18] bottom line is developers were seeing this explosion in adoption.

[17:23] However, not all is rosy because when we start thinking about this, there's some job displacement. And there are some

[17:30] myths here. Now, let's be clear. This is looking at the data we have today. In five years, it could all be different.

[17:36] We're trying to look at a crystal ball. We know how well it could be because if it was that good, I wouldn't be on stage here. I'd be sipping a pinina colada on

[17:44] vacation because I would have all this money from knowing how to bet the stock market. Okay, but this is the data we

[17:50] have today. Yes, there will be displacement. I had a a a young lady I

[17:55] dated in high school and her first job was working at Wells Fargo in their


## [18:00] AI models, trust, and human-in-the-loop practices


[18:01] typing pool. Yes, this is still in the 80s, but they had a typing pool where they got documents that they would sit

[18:07] there and type up. She doesn't do that anymore, thank goodness, because I'm obviously a little older than in my 20s.

[18:14] But what I'm getting at is that this is a continuous process where jobs come and go. That said, AI has been a little

[18:20] scary because it's been so fast, right? It's been kind of freaking people up. Anything you want to say about this

[18:26] before I go on? Just the fact that you can is the the fears there, right? We've seen jobs that have been been let go

[18:33] based off of the fact people saying it was related to AI, but then there's also the World Economic Forum is anticipating

[18:40] 78 million new jobs net by the 2030. So, it's not about it's about using these

[18:46] agents and this agentic devops process to work collaboratively with the with the agents to get stuff done. So, you're

[18:54] not going to go away. Now we start thinking about starting an agentic mindset, right? You really got to shift

[19:01] from that very traditional view of writing every line of code yourself, right? And you focus on the more

[19:08] critical things. So a good example is I was doing some code writing which is one of the great things about my job. I get

[19:13] to write code every day and we were making some changes to their website and

[19:18] the website is already in existence. It uses ASP uh ASP.NET

[19:23] uh core um and currently it's on 8.0 0 it uses an SQL server database. So we

[19:29] have some very standard patterns on what we do right we display data they can edit the data we talk to the database we

[19:35] have transactions etc that is the kind of code that once you lay the foundation the way you want you can guide the agent

[19:43] to do a new screen and you can say I need a new screen with these type of data elements etc and it will follow the

[19:50] patterns and you can even use in the case of Copilot what's called an instructions file you can give it

[19:56] explicit rules around how you want to do things. You can even give it specific subset files based on the data types. So

[20:03] for example for SQL I have some compulsions about how I like my DDL and

[20:08] my DML code to look. For example, I'll give you a simple one. When I have a create statement, say a create table,

[20:15] create table books. And after that, you have a choice where that parenthesis goes. You can put it right after it or

[20:22] you can put on a new line. I'm a new line kind of guy. And so that goes into my instructions. That way when any code

[20:29] is written for me on my behalf by Copilot or any other agent, it will follow those rules. So you can steer it

[20:36] either in real time like Mickey was doing or you can actually do it um as part of an instructions file. And so

[20:41] what happens is you start looking at that bottom at the developer workflow. What you're seeing there is define a

[20:46] goal. That sounds like something we do right now, right? Hopefully you don't just sit down, come to work every day and go, "Hey yolo, I'm going to write

[20:53] some code. Uh, what do I feel like doing? I don't know. I think I'm going to write a WPF app. No, you're probably

[20:59] going to have some type of backlog of work that you're doing. Maybe you're old school and you've got post-it notes

[21:05] on the board, right? Maybe using Azure DevOps, so you go in and look at something there. The bottom line is you

[21:12] probably have a work list that tells you what to do. The difference is you're

[21:17] going to maybe be able to do what we just did. take that issue, take that work item and hand it to an agent. Then

[21:26] you review the output. Maybe while it's working on something, you work on something new. Again, this notion of the

[21:33] exemplar, here's how we do something in our application becomes critical to

[21:39] providing that baseline for the application. When we talk about AI and agents and you start implementing AI in

[21:45] your app, we have to talk about different patterns for injecting our well-known data into the equation into

[21:51] the data pipeline. Rag retrieval augmented generation. This is a way to do that by providing these examplers to

[21:58] your app. So then you keep going. You provide feedback. Ah, you didn't do it exactly the way I wanted. Now you can

[22:04] have a choice. Sometimes they'll go, "Oh, I asked you to do this and you didn't do it." Or, "Oops, I screwed up.

[22:09] I didn't tell you explicitly that I wanted you to use this version. Well, it's just going to modify code in

[22:16] a branch, make the changes yourself. You can be a part of it or you can have it do it if it's a bigger change. Then you

[22:22] go through agent refineses, human approves, right? Everything that's out here is

[22:30] designed to have you in the loop. So now in the last 90 days, we've had a lot of changes. Um, for those of you living the

[22:38] lifestyle in the Microsoft ecosystem, they have this little tool called Visual Studio Code. Few of you maybe use it.

[22:43] Now, the great thing about Visual Studio Code is it is for developers, but it's also for IT pros. It's also a great tool

[22:51] for data scientists, people using Python, people using Jupyter notebooks. It is an all-in-one crossplatform

[22:59] developer and code editing machine that allows you to create and configure

[23:05] things that are going on. Last Thursday, they released the latest version of Visual Studio Code Regular. There's also

[23:12] what's called Visual Studio Code Insiders, which gets updated almost every night and is where you can live

[23:18] for the uh paid sorry for the the coolest features out there, bleeding edge, um that's going on. And so what

[23:25] they did was they shipped that. Now are you doing okay? Did you want to show something? It is still running. Okay. So still thinking


## [23:30] What’s new in VS Code for agentic development


[23:31] I'm going to pause here and show you a couple things that changed in Visual Studio Code. And again,

[23:37] while it is primary for developers, it's for all of you if you're in it. It's a great place to write Markdown. In fact,

[23:43] it turns out that a lot of people don't realize they have this thing called profile. So I'm going to come over here to Visual Studio Code. And right now, if

[23:49] you look over here, I have the squirrel profile. Now, it's not really the squirrel profile. You get to choose the

[23:56] icon. I've called this my modern base one, which is basically it has all the

[24:01] extensions I use to build a modern.net application with .NET 8 or later.

[24:08] It turns out that you can have multiple profiles. So, you'll see I have C for video. This was something I used a lot

[24:14] when I was at GitHub and I wanted to record a video. So, I'd had it set up a certain way, certain extensions. I have

[24:20] one here called Dockriter. Let's just pick this one. Now watch what happens when I choose it.

[24:25] My profile color changed. My tools changed. If we go to the

[24:31] extension, you're going to see a bunch of tools relating to working with markdown. Okay, let's click over here again and

[24:39] let's go to another profile. How about Ollama with C? Ollama is a local engine

[24:45] allows you to run LMS on your machine. When I do that, I for example have an

[24:50] extension called continue. This basically is an agent kind of like Copilot that runs all locally and talks

[24:57] to a llama locally, which means I can work with an AI agent on a plane without internet or anything else. So you can

[25:04] have these different setups. And if you're an IT pro and you're focused on infrastructure code, maybe you have to

[25:09] write bicep. Well, there's a bicep extension. You're a data scientist, you can pick the data scientist profile. So,

[25:14] if I pick one of these profiles like modern bass, it'll show you the extensions I need. And then if we come

[25:21] over here to the other side, what you're going to see is nothing because it turned it off. So, we'll come over and

[25:26] open it up. You have Copilot. And when you work with Copilot, you'll see there's a few different things going on.

[25:32] Number one, generate agent instructions. when you open it up with some code or

[25:37] some other type of textbased artifact that it doesn't know about, it'll say, "Hey, do you want to tell me anything

[25:43] about this project? Do you want to tell me anything about the way you work?" By default, we store those in the repo, and

[25:48] that's how we can use it. But then, if you come down here, you get that familiar interface. Now, let me just zoom out so you can just see it, right?

[25:54] It's the typical chat interface. You'll notice that we have a couple things that

[26:00] have changed. First of all, we now have four modes when interacting with it. The existing ask mode is the

[26:08] traditional I'm going to ask a question. I'm going to get a response back. There's edit mode, which was introduced over a year ago, which was their first

[26:15] attempt in having Copilot make changes to the code for you instead of you doing

[26:20] the typing. Then they introduced agent mode. in agent mode runs locally inside

[26:27] the Visual Studio context and will modify the files.

[26:33] But the problem we've realized is developers want more.

[26:38] You want to be able to say go do these 10 things and come back.

[26:46] And in order to do that, we realize that if we give the agent too much autonomy,

[26:52] sometimes bad things happen. It implements things not the way you want it. So what we found was instruction

[27:00] files. And then we found that how about you create a plan? I'll give you some

[27:06] information and you tell me how you're going to implement it beforehand. And so this this is new addition of planning

[27:12] mode. It'll do explicit steps about what is going on. Okay. Now, couple other

[27:19] things that you can do. Configure custom agents. Well, if you take a look over here, we have this new feature called

[27:27] agent sessions. And you'll notice you have your local chat agent, the Copilot cloud agent. So now you saw Mickey and I

[27:35] both kick off work via a work item, an issue. We define some stuff, fed it to

[27:42] the agent, and it's up running in the cloud. If I use agent mode and VS Code, by default, it runs locally. It uses my

[27:49] CPU GPU combination. Maybe I've got a big task that I want some power. Well, it turns out that I

[27:56] can come over here and I can either do it from this screen on this side or I can zoom over here. See that little

[28:02] button down there? I can take the command and it will actually spin it up in GitHub for me. So you have lots of

[28:09] flexibility about where the code runs and how it works. Now going back over here though, I want to show you this

[28:16] other piece of the new announcement. Copilot works particular way. It has a data pipeline where it takes the

[28:22] request, feeds it up into the Azure backend and it runs through the Microsoft responsible AI pipeline where

[28:28] they look at the input parameters. They then feed it down into the coding model of choice. If it's one of our hosted

[28:35] models, it's all processed in our data centers. If on the other hand, you have chosen for example Anthropics model or

[28:42] say Gemini as an example, it takes enough of the information, sends it out across the wire to their particular

[28:49] endpoint and brings back the results. Regardless, it takes a look at the response before it goes back to you and

[28:55] it checks it for things like, is this code going to introduce a security vulnerability? Is this going to introduce some not safe

[29:01] for work content? It will do all that validation as part of the responsible AI pipeline and bring that back through the

[29:08] proxy into Copilot and it does this often in milliseconds.

[29:13] Some people aren't always happy though with the way it's processed. They

[29:18] perceive that for example using OpenAI directly with their agent which is called Codex is better. Or maybe they

[29:27] prefer Claude. They've tested and found it gives them better results with their codebase.

[29:32] GitHub and Microsoft said that's great. We're going to give you that choice. And through this new open Agent HQ

[29:38] architecture and in this first release with Visual Studio Code, I can now use

[29:43] the OpenAI Codex agent right here from within Visual Studio Code without

[29:51] signing up for an account with OpenAI. This is included in the box with your Copilot license and other partners like

[29:59] Anthropic and Google etc. are on tap to bring them there and you'll be able to

[30:04] do this both the Visual Studio Code and sooner Visual Studio proper as well as

[30:09] in the GitHub cloud and again it's all about giving you the choice you need to bring this aentic workflow into your

[30:19] environment. So again, we want to show you some results that this actually does do something. So here we are back in


## [30:20] Demo: reviewing AI-generated PRs


[30:26] Agent HQ looking at the agent session and everything that happened. And you can see we've got a lot of details of

[30:31] all the different stuff that it's done. Here's where it was doing different renames. It shows you the commands that it's running. And we can actually see it

[30:38] created a draft pull request for us. And we don't have to necessarily leave Agent HQ to be able to see the change the

[30:44] files that are being changed in that draft pull request. But at the same token, we can go view that pull request.

[30:50] Now, here's the thing I want to point out that goes back to your um agents do humans approve it. It as sorry, it put

[31:00] me as a reviewer on this pull request. So, since I asked this agent to go do all those things that we saw in the in

[31:07] the Agent HQ, then it comes back and it says, "Okay, now it's your turn to actually verify this. Make sure the file

[31:14] ch Wow, 77 file changes, Brian. That would have taken you a while. Yes, it would have. Um it's but it's up to me now to say,

[31:21] "Okay, this looks good to review this and then be able to take it from a draft to a full pull request and take it

[31:27] through our process where then it might have um checks that run against it to make sure that it builds and tests pass,

[31:32] etc. This is what we want, right? Do things that yes, I can do. I'm qualified, but I do I really want to do

[31:39] it, right? I mean, no offense to anybody in the audience, but for the developers in the room, you're inherently lazy. I

[31:46] mean, who else embraces inheritance, right? Ry once, reuse.

[31:51] And so, having agents be able to do those things that are repetitive that have to be done for the applications we

[31:56] build because we really haven't hit that nirvana of the 4GL, 5G where you can just write something and it builds it

[32:02] completely correctly without code. We're still building solutions today with

[32:08] code. Now, Mickey did it. Mine is still running. And what I want to show you when you're in a Oh, it just finished.

[32:13] Look at that. I just got the green check mark there. And I want to show you that

[32:19] you can see how long it took. So, it took 17 minutes and 55 seconds to do what was going on. I will tell you as

[32:26] someone who has played with Aspire. I haven't used it in much anger, but it would not have taken me that long. It

[32:32] would taken me much longer to get that set up. Now, Mickey looked at his poll request and say, "Hey, looks good." What

[32:38] you really should do with any poll request, and you have to review the code, is I should pull it down. and I should try and run it and test it. But

[32:45] you'll notice it even ran my unit test. It did some checks and all those things. And when I come back up here to the top

[32:51] and go to Azure DevOps, you'll see that no longer does it say Copilot is

[32:57] working, but it tells me my poll request is ready for review right there in Azure DevOps. I don't have to sit there and

[33:03] monitor an Agent HQ if I don't want to. I can see it there. My team can see it and I can assign other reviewers. They

[33:09] can go through it. By default, the way GitHub copilot works when it's doing work on your behalf, whether it's from

[33:15] GitHub issues or from Azure DevOps or any of the other mechanisms is that the

[33:20] person who started the request cannot do the final approver to merge into your

[33:25] parent branch. Obviously, we want that extra safety balance with the human in the loop. So, that is pretty darn cool.

[33:34] So, again, lots of changes, Visual Studio Code, really impressive what's there today. And again, I encourage the

[33:41] non-developers to take a look as well. It's a powerful tool that you can configure for your subset of work that

[33:48] you do even if you don't write code on a regular basis. Now, integrating AI agents into your workflow means thinking

[33:53] about different tools. So, definitely Microsoft and GitHub are focused on how do they bring it to you first in the

[33:59] developer experience, but also in other environments outside there um like the

[34:05] Azure cloud. And this is where we get into this notion of how can the IT pros in life do this. Right? For years, we've

[34:11] been trying to get IT pros to embrace automation, to embrace the motto of

[34:18] cattle, not pets. Now, what do I mean by that? Mickey and

[34:24] I, we like food. You might be able to figure that out by our body shapes. Um,

[34:29] so cow is something we both like. Oh, you're going to suck it in. Nice. Yeah, I like that. Can you hold that the whole

[34:35] time? Nope. The idea is simple, right? Particularly in the 90s when I got started and doing

[34:43] stuff for for pay and work and even into the odds. If you set up a Windows server, you had to give it a name. And

[34:49] people often had very thoughtful names. Maybe this was the Froto server or it was the Ferrari server, right? You had

[34:56] car names, you had various science fiction fantasy names. And so when people said, "Well, where's the files?"

[35:02] Oh well, you know, go over to the Bezabub server and pull down the files. Okay, the problem with that is that

[35:08] you've now given it a name. Now you have to care for it. You have to feed it. You have to love it. We don't want to do

[35:14] that. We want to do it through things like PowerShell and other technologies like infrastructure as code. And this is

[35:19] an example where aic technologies can really help you. Who likes writing YAML? Anybody? Buler, Ferris,

[35:27] JSON, ARM files, ARM files, who likes that? HCL? No, you don't. Right. You

[35:33] want the results. You want the new server stood up the way you want it. You want your cloud deployment to be

[35:38] repeatable. These tools can help you. Now, security posture is another big

[35:45] one. The reality is that we're not doing enough and we're trying, but it's hard.

[35:50] And so, at GitHub, we have something called GitHub advanced security. And what's really nice about this is that


## [35:51] Security: code scanning, secret scanning & autofix


[35:56] not only does it help you do the right thing, it stops you from doing the wrong

[36:02] thing. Mickey, you want to tell them anything about this? So, yeah. So, with get the two main areas that you should

[36:09] be doing, whether you're using honestly advanced security or some other tool is secret scanning and code scanning. You should be checking to make sure you're

[36:15] not putting secrets in your code. You should be scanning your code to make sure that you're writing good quality code and not doing things like SQL

[36:21] injections, stuff like that. Now, we've had secret scanning and code scanning for a while, but now we started adding

[36:27] Copilot on top of it. So, now we're doing things such as allowing Copilot to

[36:32] actually tell you how to fix the problem that it finds automatically. So, you

[36:37] want to get ready for that. Yep. So, the key thing to put in context and again this is package as a developer feature

[36:43] because it's GitHub. But remember, if you're an IT pro or a data scientist, you should be using version control as

[36:49] well. And all of us are guilty of doing this. We're going to need to connect to

[36:55] something. A data scientist wants to connect to some data store. In order to do that, you have to provide information

[37:01] about where it's at, the connection string. And then there's that dreaded piece of, well, how do I authenticate?

[37:08] And we've all been lazy and said, I'm not going to build the OOTH 2 interactive login experience. I'm going

[37:14] to use a PAT or I'm going to use a password. and you say to yourself, I'm only going to put it in this source

[37:20] file, in this Excel configuration, in this Python file for just a minute. I

[37:26] just want to see if it works. And then a week later,

[37:35] yeah, what's up, boss? Can you explain this $100,000 AWS bill for our S3

[37:41] buckets? Looks like we're using 22 terabytes of storage for

[37:48] I don't want to say this out loud. My mama taught me better. No, you don't

[37:53] want that. The number of keys that get out there for AWS, for Azure, the

[37:58] passwords is ridiculous. Real quick. Oh, yeah. In 2024,

[38:05] GitHub advanced security secret protection prevented over 4.4 4 million

[38:12] credential leaks. You folks are still doing it. Okay. No,

[38:17] no, not you. I know none of you were doing that because there are 180 million developers on GitHub. Um, but you're not

[38:24] doing it. So, Mickey's going to show you one of the great features that's facilated to the agentic part, which is Copilot autofix.

[38:30] Exactly. So, we have a little saying at GitHub is found means fixed. So if we're

[38:36] able to find a problem in your code, we should also be able to help you fix that problem in your code. So here I've got

[38:42] an alert that we have found with our code scanning, which is database query being built from user controlled sources. And there's lots of information

[38:49] here, and we actually give you a lot of details on how you could go fix this yourself. But let's face it, it'd be a

[38:55] lot easier if somebody would fix it for me. Well, it would because you know, your developer skills are sometimes questionable.

[39:01] That is very true. But what we've got is a generate fix button and we simply

[39:06] click that generate fix button and give it. You'll see it's AI is

[39:12] generating fix suggestion. Copilot's now taking the issue that was found looking

[39:17] at the code and trying to come back and tell us how it would potentially solve this problem. And here you can see it's

[39:24] already come back in the alert itself. It's showed us this is what the problem is. This is how I would fix it. And down

[39:30] here, I even have the ability to go ahead and commit that to a new branch or to an existing branch and then create a

[39:35] pull request and start going through whatever my process is to be able to get that fix pushed off into deployment. And

[39:43] this is a really compelling feature because it's something that you can put into your workflow so that when

[39:49] developers bring code to the server environment, right, when they bring it to the repo and push it up into a pull

[39:56] request, it can run automatically. I've been playing around with vibe coding and vibe coding is one of those


## [40:00] Real-world pitfalls & responsible AI


[40:02] things that you know makes a lot of professional developers kind of get nauseous in their mouth and in looking

[40:09] at this because we know that building things is hard. The idea that you're going to sit down and yolo stuff and ship something for production, you know,

[40:15] you can vibe code, but can you vibe debug it? Well, I've been having fun with it because I wanted an extension to

[40:21] help me manage my URLs. My name is Brian and I have a bookmark problem. Um, I am

[40:27] one of those people that will have multiple browser sessions each with 30 tabs open and you know there's some good

[40:34] stuff. I really will get back to read it and so I thought it'd be great. Hey, let's learn how to write a extension. So

[40:40] I thought I'd do it in Chrome and of course that means JavaScript and while semicolons are there for my C bias, it's

[40:46] not the same. So I said I'm going to vibe code it and I started doing it. I was using Cloud and Cloud's really good.

[40:52] I even had Codex review the code that claude wrote looked good. I pushed

[41:00] it up to GitHub. I have advanced security turn on which by the way GitHub advanced security is a

[41:06] paid product for private repos. But if you do public, so you want to just do it for fun or you're doing open source, you

[41:13] get it for free. I have it turned on. Guess what it did? It found a URL

[41:19] injection attack in my code. multiple times.

[41:24] So, I used two different smart AI agents and they still screwed up and GitHub had my back. So, this is something that is

[41:31] super compelling to help you not only prevent secrets from getting in, but preventing bad code from getting into

[41:38] your application. So, this is really great stuff. 4.4 million, that's a huge number. I can't wait to see the figures

[41:44] for 2025. I pray they go down. I don't think it will. In fact, I think it's going to go up in the name of vibe

[41:51] coding. Um, reduction of security review times. If you save half your time on security review, that means you're

[41:57] shipping faster, means you're delivering value faster. Um, and of course, faster

[42:02] vulnerability fixes. If we find a pattern, we can help you fix that. All

[42:08] this means that we need to have humans in the loop, though, because even though the AI is really smart, it's far from

[42:14] perfect. And we are the ones that know our application domain the best, right?

[42:20] We know how our application is used. We know the critical aspects and we also know when not to goldplate. One of the

[42:26] downsides to AI sometimes it's like, oh, you've asked me to do that. Sure, I'll do. And you're like, I asked you to

[42:32] change one file, dude. Um, so we really got to make sure the human's in the loop. And so we think about this

[42:37] starting with security first. And so this idea that you're going to generate code, but you're going to go through this multiplestep process of taking that

[42:45] idea and that code and getting it all the way to step 10 where you can do that continuous monitoring. When we think

[42:52] about security best practices and warning signs, we've got kind of a list for you here. And it looks like I got a

[42:58] little wrap there. U but the bottom line is we see some warning signs, right?

[43:03] Ignoring the happy green check boxes, as assisted commits are merged four times faster bypassing reviews.

[43:12] That means people are trying to look more productive. And one way they do that is they use AI and then they just

[43:19] say, well, I'm sure it's awesome, right? Because this is the latest and greatest model.

[43:24] [clears throat] Okay, the next one freaks me out. 322% more

[43:33] privilege escalation paths in AI code. Again,

[43:39] here's the internet. Rainbows, unicorns, kittens, puppy dogs.

[43:45] Over here, things we don't talk about imply company. The frontier models are often trained on

[43:51] all of that. And when they're even distilled down to be focused on code, there is code that has been trained on

[43:58] that isn't necessarily always the best. Okay. Now, that's why Copilot works really hard to look at the inbound and

[44:05] outbound that's going on. You don't necessarily have that guarantee with every IDE and every a enabled tool out

[44:10] there in the industry. So, be aware of that. More design flaws and 40% increase in CRI secrets exposure risk. I can tell

[44:19] you from experience multiple times as I've been working with the various agents to test things out, I have had it

[44:25] more often than not offer the cheap and easy way of authentication passwords and pats

[44:32] over the more complicated but safer ooth or other type of authentication

[44:37] format. Be aware you have to have your your uh eyes wide open. So start with

[44:44] logging and this is beyond the normal application logging but you got to think about AI enabled logging. When you start

[44:51] thinking about what to log we've got some categories for you in some different areas. Again you'll get the slides you can go through the details

[44:56] but ultimately you need to be tracking and monitoring what's going on. YOLO is

[45:03] not going to cut it in production and real applications. No I've got nothing to add to that. That's 100% correct.

[45:08] Okay. There's various tools. For example, GitHub has very rich audit logging. Um, you go the other extreme,

[45:15] there's tools like Splunk, um, and, uh, Permit.io and all these tools that are

[45:20] designed to help you data mind your logging information. Um, and this is

[45:26] going to go across the board and this has to be part of a cohesive strategy as you roll out AI into your organization.

[45:32] You got to think about the various compliance frameworks as well, right? This is a place where for example picking a company like say Microsoft or

[45:39] Amazon might be better than the latest startup who isn't necessarily at that point where they're investing in

[45:45] compliance and this might be anything from soft compliance to HIPPA right the

[45:50] number of bad things I've seen in organizations without AI related to HIPPA freaks me out to think of what

[45:55] they'll do once they add AI to the puzzle right because AI is driven by data it's ultimately a data problem now

[46:03] we start looking at AI versus human control, right? We want to have the appropriate automation, but make sure

[46:09] that the human maintains control where necessary and there's a lot of different places you're going to look in there.

[46:15] When we get to this on the data, right, we have some interesting numbers, right? They don't plan to use II for deployment

[46:22] and monitoring, right? This is a lot of stuff I've heard for years in the IT Pro community when

[46:28] it came to doing things like automated database deployments, right? I know lots of DBAs, the deeders, the debies of the

[46:35] world that will not let developers use automated deployment tools. They require that you provide them with the SQL

[46:41] scripts and they will look at and they will manually deploy them themselves. We're going to run into the same

[46:46] friction with using AI for some of this stuff, right? Uh project planning, uh

[46:51] preserve mental energy during repetitive tasks. There's some good and there's some bad. The key thing is coding is not

[46:58] typing, right? It's much more than just that. And so as we embrace AI, we have

[47:04] to be careful that we don't bring the AI slop to our application process. Here's a set of essential human

[47:11] controls, right? Performance optimization, security, threat modeling. You really need to be actively a part of

[47:17] this situation. Now, where is AIXL? Right? Here's some stuff we found in

[47:22] 2025. This is based on the data. Again, I will give you links to the resources. Everything from 30% average code

[47:28] acceptance rate, 84% increase in successful builds. AI is really good at

[47:34] some of those things where it can find syntax errors. Oh, you forgot the slash. You left out a colon, right? These are

[47:41] the little pieces. It's good at that. Right? Concepts and architecture, it might need some help. In fact, when we

[47:47] start looking at where it struggles, right? those complex architectural decisions, it doesn't always know

[47:52] because the way it's trained, it's looking at the results of what someone or some set of people did. You start

[47:58] looking at things like edge cases for handling training data. Uh thinking about what is considered responsible AI

[48:06] for your organization, right? When I work at GitHub and Mickey works at GitHub, GitHub in certain parts

[48:11] of the company, you know, people don't care if you use a little not safe for work language, right? In other

[48:17] companies, that's just not done. When you build a system for your customers, you have to understand what their

[48:22] tolerance is to that experience, right? You have the extremes where Elon Musk and what he's offering through X AI and

[48:28] and and Grock and stuff is, hey, we have these, you know, more adult modes,

[48:33] whereas, you know, if you're enabling AI for your local church, you may really want to make sure it's it's well behaved

[48:40] vocally as well as other formats, right? So again all these things require you

[48:45] the human to be invested in the experience. This is where we get into this METR study which talks about the


## [48:48] The productivity paradox & adoption challenges


[48:51] productivity paradox. We have the expectation that AI is going to help us go faster.

[48:58] But sometimes you have to go slower to go faster because you have to do it safely. Right? The Germans have

[49:05] something called the Autobahn. The Autobahn is well known because there are parts of it that do not have speed

[49:12] limits, which makes people think, "Oh, all right. I want to go there and drive as fast as I can." But every German who

[49:20] holds a driver's license knows that speed is only a partial component of being prepared to use the Autobahn

[49:27] effectively. And one of the thing is recognizing your skills.

[49:32] How fast can you drive based upon your experience? based upon your tolerance for pain and

[49:39] suffering if you screw up and understanding the law. For example,

[49:45] you're not allowed to drive in the fast lane unless you are going fast. And the

[49:51] expectation is you're only there to pass. Those are rules that have to be respected by every driver. And so when

[49:58] we think about how we're going to work with AI, you're going to have to find out what your tolerance and trust is.

[50:03] And so therefore, we're finding people are slower on average. They think they're faster because they see things

[50:09] spinning out. They see more files generated. It's that feeling of paper pushing where I'm really busy. I'm

[50:15] really busy. I move the paper on this side of the desk over here, this paper over here. Right?

[50:21] And some people are saying, "Yeah, I'm using AI, but it's not having a real effect on my ability to ship the

[50:26] features I want with the quality and what I want." So, it's not all roses. There is some data out there that says

[50:32] we need to think about this. And so we're really seeing this trust gap and

[50:37] having to really deal with the fact that we need to build up the trust based upon working with it on a regular basis in

[50:43] our domain. You don't have to be on the latest piece of AI technology to be using AI. Just because a new frontier

[50:51] model comes out doesn't mean that that's the one you all switch to. Because anytime you adopt a new tool means you

[50:58] have to spend time learning how to use the tool, right? You might see the latest and greatest uh you know kitchen

[51:05] tool and so you go spend all the money because some chef like Emerald says, "Oh, it's going to help you make this

[51:10] great meal." And you realize you can't make the meal with 10 of the greatest tools because you don't have the skills.

[51:17] So be aware of that. So the bottom line, our key insight is AI is powerful but not magic, right? you're really going to

[51:24] have to invest in how you bring it onto your team just like you would invest in

[51:29] bringing another human onto your team. Now, as we start thinking about 11 up to success, we start running into this 30


## [51:32] 30/60/90-day rollout plan


[51:36] 60day, sorry, 30, 60, 90day playbook. And so, we've written down some ideas on

[51:41] how you can approach your first one to 30 days, how you can go on to the next level of 31 to 60, and how you can do it

[51:48] on 61 to 90 where you really get into the optimization. And the idea is that you're looking for these metrics. You

[51:54] want to look at progressive success where you're seeing real return on investment but not necessarily boiling

[52:01] the ocean. Right? That's one of the big problems I've seen with people when they approach an agent. They give it too much at once. Break down the work very much

[52:07] like you would as a human. Now, when we start thinking about adopting AI, we

[52:12] start looking at how do we upskill in our different roles. And so, again, we've got some different breakdowns on what you can do as developers. One of

[52:19] the first things is learn how to write good prompts. The number of people that will write one sentence and expect magic

[52:24] from AI don't get the results they're looking for. You need to think about being articulate. And in fact, when you

[52:31] are articulating what you want in a question, this is where actually having decent language skills works out. You

[52:36] know, the joke is, you know, I'm a developer. I'm not an English major. Well, it turns out the better you can

[52:42] write, the better results you're going to get from your AI, your code review skills, security awareness, all these

[52:48] things matter. DevOps engineers, I don't like the term, but the reality is that I know it exists in organizations, the

[52:54] people that focus on really building the pipelines, maybe under the ones that understand infrastructure as code, etc.

[53:00] There's a lot of different things you can do there. security teams, threat modeling, incident response, and in


## [53:05] Azure’s autonomous agent for cloud monitoring


[53:06] fact, let's talk about instance incident response and how you might be able to monitor your code. So, for this last

[53:11] thing before we get wrapped up here, we're going to go over here to Azure.

[53:19] And Azure has this new feature called the SRE Agent. And this agent is in preview.

[53:26] And what you'll see here is once you configure it, you specify what you want to monitor. So you can come in and you

[53:33] pick what's called a resource group. And a resource group is a container in Azure that you use to bring things together.

[53:40] Web services, containers, databases. So you'll see I have a couple available.

[53:45] I'm already monitoring one. So I could add another one. And you'll see that over here I have activities. The one

[53:51] thing is I can chat with it. But more importantly, it'll go through and do things like incident management. when it

[53:57] finds something happened, it can actually be given the permission to be autonomous and try and fix it. It also

[54:03] can come through here and provide me with reports. So you see I have a report from yesterday. What this is telling me

[54:09] is that it went through and did not find any security issues or incidents and that my current app group that's

[54:15] monitoring is healthy and it provides me with all this data on a regular basis. So, I now have this site reliability

[54:22] engineer that is on my team that I've given autonomous ability to monitor and

[54:28] alert me when something goes on. So, rather than me having to look for an email notification or god forbid the old

[54:34] pager or my phone, I have this rich report and this tool that's constantly

[54:39] checking on behalf and I can give it the rights to fix certain conditions. This

[54:45] is available in preview. If you're using Azure, you should take a look at it. It's easy to set up and play with. And so we start thinking about how these

[54:51] agents come in. We start looking at how we find the drudgery. We find the things

[54:57] that take a lot of time but have to be done. And instance response is an example. Better yet, get your sea levels

[55:03] to upscale, right? They need to understand that AI isn't just about saving money and about replacing the

[55:09] humans because this whole idea of keeping the human in the loop means they need to use AI effectively and you need

[55:14] to be trained. So we've got this idea behind learning resources. everything from Microsoft learn certification

[55:19] programs the community and things like LinkedIn learning and coserup then we have these patterns that we've got for

[55:25] you the interrupt and resume pattern the human as a tool pattern it's not as bad as it sounds uh an approval flow pattern

[55:33] and then a fallback escalation pattern these are different ways to inject AI agents and agentic workflows into your

[55:40] DevOps platforms we have a bunch of critical decision points and approval requirements that are also relevant and

[55:46] when we think about collaboration. There's these big three here. Human in the loop, human on the loop, and human

[55:52] out of the loop. Let's be honest, the first two are where you're going to be actively involved in a part of the

[55:57] process. Human out of the loop means you have established a workflow where you trust

[56:03] the AI to do the right thing on a consistent basis. I currently have

[56:08] nothing that I use that is human out of the loop. Five key takeaways. Number one, start Monday with an action plan.


## [56:11] Final takeaways


[56:16] go back to work and think about how you're going to do it. Security comes first. We cannot increase that number

[56:23] every year with the number of uh secrets that we find in things like GitHub advanced security. Keep the human in the

[56:30] loop. AI suggests humans decide. Measure everything. Right? This is a

[56:36] critical point in the transformation of how we build and deliver solutions and

[56:42] monitor and maintain them for our customers. It's how we deliver value as

[56:48] developers, as IT pros, as data scientists, as DBAs. Focus on value. It's that continuous

[56:55] delivery of value that's going to keep us all employed, not how many lines of code we can generate with AI.

[57:02] So, you got your next steps, your final thoughts, right? It's a transformation. It really is. You can be a part of it or

[57:09] you can stick your head in the sand and say, "I ain't doing AI." You're probably not going to do very well with that.

[57:14] You're going to find on the slides our contact information. Like I said, I have a free copy of the book to give away. You can harass Mickey, especially if you

[57:20] need some help with GitHub. Thank you so much for attending this keynote.

[57:26] Be good humans. We'll talk to you later.

[57:31] Heat.

[57:37] [music]

[57:43] [music] Heat.
