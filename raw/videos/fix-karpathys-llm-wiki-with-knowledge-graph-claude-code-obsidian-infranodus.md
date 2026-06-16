---
title: Fix Karpathy’s LLM Wiki with a Knowledge Graph | Claude Code + Obsidian + InfraNodus
video_id: yYSTsKo8moU
url: https://www.youtube.com/watch?v=yYSTsKo8moU
channel: Nodus Labs
channel_id: UCK2IvRB36OUwXwMRD1iDmvg
channel_url: https://www.youtube.com/channel/UCK2IvRB36OUwXwMRD1iDmvg
publish_date: '2026-04-11T07:01:35-07:00'
upload_date: '2026-04-11T07:01:35-07:00'
category: Science & Technology
duration: '26:09'
length_seconds: 1569
view_count: 31144
caption_tracks:
- language_code: en
  name: English
  kind: manual
  is_translatable: true
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
thumbnail: https://i.ytimg.com/vi_webp/yYSTsKo8moU/maxresdefault.webp
keywords:
- obsidian for beginners
- how to use obsidian app
- second brain
- knowledge management software
- llm wiki
- infranodus
- andrej karpathy
- productivity system
- obsidian plugins
chapters:
- title: LLM Wiki — organise your knowledge
  start: 0:00
  start_ms: 0
- title: The problem with LLM Wiki
  start: '1:12'
  start_ms: 0
- title: Real-life demo
  start: '2:12'
  start_ms: 0
- title: Knowledge graphs help visualise and optimize the structure of the LLM wiki
  start: '3:41'
  start_ms: 0
- title: Obsidian InfraNodus graph view
  start: '5:00'
  start_ms: 0
- title: MCP server to create graphs
  start: '5:36'
  start_ms: 0
- title: Adding knowledge graphs into LLM wiki
  start: '6:53'
  start_ms: 0
- title: “You generate a living memory of what’s happening in the system”
  start: '8:23'
  start_ms: 0
- title: 'DEMO: SETTING UP YOUR LLM WIKI with our skill'
  start: '8:57'
  start_ms: 0
- title: Ingesting sources into LLM Wiki
  start: '13:10'
  start_ms: 0
- title: Organising ideas into the internal wiki
  start: '15:21'
  start_ms: 0
- title: Exploring and optimising the content of Wiki with InfraNodus graph
  start: '15:39'
  start_ms: 0
- title: Using the knowledge graph to bridge a content gap in your wiki
  start: '18:05'
  start_ms: 0
- title: Adding a plan to your research
  start: '20:22'
  start_ms: 0
- title: Final overview of the stack to use - Obsidian + Claude + Cursor + InfraNodus graph / MCP server
  start: '22:23'
  start_ms: 0
- title: Running gap analysis on LLM Wiki using the MCP server - without using the graph interface
  start: '23:15'
  start_ms: 0
description: "In this video, I'm going to show how Andrej Karpathy's LLM wiki setup can be improved using https://infranodus.com — using knowledge graphs to discover topical clusters and content gaps between your ideas in order to generate better insights. \n\nThe easiest way to use it is to install the InfraNodus extension to your favorite IDE where you use Claude Code, for instance, for Cursor or Antigravity — https://infranodus.com/vscode-extension \n\nYou can also use InfraNodus inside Obsidian if you prefer it for visualizing your wiki: https://infranodus.com/obsidian-plugin\n\nTo set up your own LLM wiki, you can use our Claude skill that will take you through the process: https://github.com/infranodus/skills/blob/master/skill-llm-wiki/SKILL.md \n\nTimestamps:\n0:00 LLM Wiki — organise your knowledge\n1:12 The problem with LLM Wiki\n2:12 Real-life demo\n3:41 Knowledge graphs help visualise and optimize the structure of the LLM wiki\n5:00 Obsidian InfraNodus graph view \n5:36 MCP server to create graphs\n6:53 Adding knowledge graphs into LLM wiki\n8:23 “You generate a living memory of what’s happening in the system”\n8:57 DEMO: SETTING UP YOUR LLM WIKI with our skill\n13:10 Ingesting sources into LLM Wiki\n15:21 Organising ideas into the internal wiki\n15:39 Exploring and optimising the content of Wiki with InfraNodus graph\n18:05 Using the knowledge graph to bridge a content gap in your wiki\n20:22 Adding a plan to your research\n22:23 Final overview of the stack to use - Obsidian + Claude + Cursor + InfraNodus graph / MCP server\n23:15 Running gap analysis on LLM Wiki using the MCP server - without using the graph interface"
notes: ASR caption track; transcript fetched 2026-05-17 at --timeout 180000 (60s attempt failed with panel-render symptom). 556 segments. No manual cleaning applied to the body — proper nouns may be ASR-spelled (Andrej Karpathy / InfraNodus / Karpathy's gist URL etc. confirmed correct on spot-check).
---

## Transcript


## [0:00] Adding a plan to your research


## [0:00] Adding knowledge graphs into LLM wiki


## [0:00] DEMO: SETTING UP YOUR LLM WIKI with our skill


## [0:00] Exploring and optimising the content of Wiki with InfraNodus graph


## [0:00] Final overview of the stack to use - Obsidian + Claude + Cursor + InfraNodus graph / MCP server


## [0:00] Ingesting sources into LLM Wiki


## [0:00] Knowledge graphs help visualise and optimize the structure of the LLM wiki


## [0:00] LLM Wiki — organise your knowledge


## [0:00] MCP server to create graphs


## [0:00] Obsidian InfraNodus graph view


## [0:00] Organising ideas into the internal wiki


## [0:00] Real-life demo


## [0:00] Running gap analysis on LLM Wiki using the MCP server - without using the graph interface


## [0:00] The problem with LLM Wiki


## [0:00] Using the knowledge graph to bridge a content gap in your wiki


## [0:00] “You generate a living memory of what’s happening in the system”

[0:00] Last week, Andrej Karpathy, a prominent AI  researcher, released a super useful framework
[0:06] called LLM Wiki that uses LLM to supercharge your  research. It's a really good framework. However,
[0:13] there's a critical piece missing. It's not  aware of itself. The problem that Karpati
[0:18] himself pointed out is that when you interact  with your standard AI and you upload some files
[0:23] and you want to get a result, what happens is  that it retrieves uh some chunks of text using
[0:29] rag retrieval augmented generation and gives you  the result and then every time you interact with
[0:34] this system, it's always going to do the same  thing and forget what it's done in the past. So
[0:39] you don't have a knowledge base that is evolving  with you. Andrej Karpathy proposed to resolve this
[0:45] problem by building so-called LLM wiki which you  can open in any IDE or Obsidian that basically
[0:51] retrieves all your raw papers or notes organizes  them in a folder which we call raw folder here
[0:58] and then it generates a wiki where it lists all  the concepts and the connections between them
[1:03] the main ideas. So it creates an organization  for your knowledge and then you can use this
[1:09] structure to then interact with it and to generate  insight. The problem with the system however is
[1:14] that even though you have the structure you  still need something to navigate through it
[1:19] because if you just ask your LLM to produce the  results it's going to extract the concepts that
[1:23] you have listed the questions the data but then  it's going to produce the most probable outcome
[1:29] because that's what LLMs are trained to do. This  is where knowledge graphs can be very useful.
[1:35] For the last 10 years, I've been working on  InfraNodus, a knowledge graph visualization tool
[1:41] that represents ideas as network and then applies  graph science metrics to identify the main ideas
[1:47] and clusters of them inside, but most importantly  identify the gaps in your knowledge which you can
[1:53] then use to generate new ideas. So, I'm going  to show you how you can augment this LLM wiki
[1:59] with knowledge graphs so that you can generate  much more pertinent insights and so that you can
[2:05] direct your LLM's thinking through that structure  that it created. I'll just show you a couple of
[2:11] things it can do and then I'm going to demonstrate  how you can set the whole system up from zero. So,
[2:17] let me show you here. I have an already prepared  wiki that I made from my documents on a research
[2:22] topic I'm working on. And uh what I did first is  that I ingested all my papers into the raw folder
[2:29] here uh which you can see some papers here,  some notes that I have on different topics
[2:33] and so on. And then I ran the skill that I'm  going to also make available to you for free
[2:38] uh through my GitHub repo. I'm going to leave the  link in the description to the video below that
[2:43] basically ingests all this raw material and then  generates structured representation of the main
[2:48] concepts in those research papers, how they're  connected to one another. So the main connections,
[2:54] some sources that it uses so that you can always  get back to those sources or add more interesting
[3:00] research papers and then systems that it's talking  about. Okay. So normally what happens here is that
[3:05] once you have that wiki created here which is  a structured representation of your knowledge,
[3:10] you could launch claude code inside that folder  and then start asking questions about it. But when
[3:17] you ask questions, what it's going to do is that  it's going to scan through your wiki, extract some
[3:21] concepts, and then produce the most plausible  response that kind of connects everything
[3:26] together. It can be good for some use cases, but  when you want to generate new ideas, is not so
[3:31] interesting because the results are going to be  quite generic. What I need first, and this is
[3:35] where knowledge graphs are very useful, is to get  an understanding of the structure of this wiki.
[3:41] And so for this you can actually use knowledge  graph of InfraNodus which you can use both from
[3:48] your favorite IDE like in this case I use cursor  maybe you're using anti-gravity you can install
[3:53] the extension of InfraNodus here and then when you  have that folder of concepts for example where I
[3:59] have the most important concepts listed that were  extracted from the research papers I right click
[4:03] on it then I click InfraNodus visualize as a  graph and then the extension which is opened
[4:08] in the side bar here is going to visualize to me  what are the main topics in my research and this
[4:14] is very useful because first of all it reminds me  what are the main ideas inside network theory you
[4:20] know then phase dynamics fractal structure but  also shows me the smaller clusters that I want
[4:26] to develop in order to make this whole discourse  much more coherent so I will focus on the smaller
[4:32] ideas like power mechanisms here for example and  explore them further or frequency modulation and
[4:38] so on right so this helps me see what are the  topics that I need to develop further. But then
[4:43] I can also go into gaps and ask it to show me  some clusters that could be better connected
[4:48] and then focus on the connections between those  clusters to generate new ideas. You can also use
[4:54] this plug-in inside Obsidian itself. So here  for example I have Obsidian and in Obsidian we
[4:59] have the InfraNodus plugin. So then I would open  that same folder concepts and visualize it as an
[5:05] InfraNodus graph and then it would show me the  connections between the ideas that exist in this
[5:10] folder give me the same topical overview and also  I could identify the gaps and then by bridging the
[5:16] gaps and using AI to generate research questions  I can then generate new ideas that bridge those
[5:22] different clusters together. So this would be one  approach that you can use it visually like this or
[5:28] you can also go back to cloud and actually use  the InfraNodus mcp server which is basically a
[5:34] connector for your llm to think in terms of these  graphs so that it would create that same graph
[5:41] representation of your content. So I could ask  okay use InfraNodus generate graph tool to analyze
[5:47] the concepts in the wiki concepts folder. Okay. So  then it would connect to the InfraNodus MCP tool
[5:54] which is basically an like an API that connects  uh this whole content to Infronotus and then it
[6:01] extracts the list of the concepts that we have  listed here as markdown files. Then you see it
[6:06] uses the InfraNodus generate knowledge graph tools  and it's going to give me a similar insight to
[6:11] what I visually see. So here again I can generate  an overview and then I can use InfraNodus to
[6:17] identify the main clusters and then ask InfraNodus  to generate insights based on the gaps between
[6:21] these clusters. So that would be one approach  to use this. You see it runs the tool then it
[6:27] generates the analysis and then it will generate  a response. As you can see here it provides me
[6:31] information about the graph structure main topical  clusters fractal dynamics critical transitions
[6:36] process coupling and also information about the  gaps. So you can use the graphs if you want or
[6:42] you can also use the MCP server inside cloud code  itself. However, an even more advanced approach
[6:48] is to add knowledge graphs into the structure of  this LLM wiki so that instead of just analyzing
[6:55] the folders with the external tool, you actually  integrate knowledge graphs into the process of
[7:01] structuring your knowledge. So that skill that  I made available actually allows you to do that.
[7:06] And what it does is that once your wiki is created  and you generate some ideas from it, then it will
[7:14] create a folder InfraNodus where it's going to  save so-called ontology graphs that I was talking
[7:19] about before on my channel which describe the main  concepts and relations between them. So then later
[7:25] if you say want to analyze what's happening in  this repository in this wiki you can go back to
[7:32] Obsidian for instance and then you can open that  folder InfraNodus and for example if you want to
[7:37] see a graph of all the concepts you have here then  you just click on this and Obsidian InfraNodus
[7:43] plug-in shows you what are the main concepts you  have here and also which of them are disconnected.
[7:49] So that can also give you information how you can  connect them better. So for example, you can see
[7:54] like okay, you have synchronization patterns here,  but they're not so connected to, for example,
[8:00] fractal networks. So you select these two and  then you generate an interesting question that
[8:04] can link them together. And this will give you an  idea for how you can link disconnected clusters
[8:10] of your knowledge and make your whole research  much more coherent and interconnected which can
[8:16] be very useful for improving its structure. Okay,  so this would be another approach how you could
[8:20] use it. You generate InfraNodus ontology graphs  for everything that it does. So it's some kind
[8:27] of living memory of what's happening in the system  and then every time you come back to it claude or
[8:32] whatever system you use will have access to this  system of rules of of how the concepts connect in
[8:38] your wiki and then it will be able to extract them  and generate some interesting ideas from them. So
[8:43] that would be another deeper approach where you  integrate knowledge graphs into the actual LLM
[8:48] wiki. Now that I showed you how all of this looks  like, let me show you how you would actually set
[8:54] something like this up. So first I would create  a new folder on my computer and I would give it
[8:59] the name of the research I'm working on. So for  example, I want to make another one on finance.
[9:04] I click create and then I go inside and I simply  open the empty folder in my favorite programming
[9:10] development environment which is cursor in this  way. All right. So now it's completely empty.
[9:16] Then what I do, I open terminal inside here.  And by the way, you could also do it directly
[9:21] through terminal. But what I like is that in  something like Corsor or if you like anti-gravity,
[9:25] you can use anti-gravity. I can actually see the  file structure on the left. That helps. Then I
[9:29] open cloud and because I already installed that  LLM wiki skill that I'm going to link to in the
[9:35] description to the video below, I can then um ask  it okay use LLM wiki skill to create a repository
[9:45] of knowledge on finance that I have. And you can  even make a general query like that and see how
[9:53] it does. Sometimes you will need to tell it where  it should take the data. Let's see if the skill
[9:57] will actually pick it up because I structured it  in a way where it will ask you questions for how
[10:02] to proceed. Here it's asking us shall I use the  skill lm wiki we say yes. Okay let's use the skill
[10:07] and then see what it does. So first of all it's  asking me okay you want to explore finance that
[10:12] this wiki is for just explain to me what you want  to work on personal investing microeconomics and
[10:18] market personal finance trading and strategy. So  I would say that I would like to work on personal
[10:24] investing. I think that will be interesting for  me. And also trading and strategy. Okay. So then
[10:29] let's click next. And you see everything that it's  going to do. It's going to ask me a question about
[10:33] it. And then it tells me, okay, so what kind of  sources you want to feed? Articles? Yes. Books
[10:38] and papers? Videos and podcasts? No. But personal  notes and data? Yes. Okay. And then it's telling
[10:44] me, okay, so what's your end goal for this finance  week? So I think I want to track and learn. I want
[10:51] to support my decisions. And I want to also have a  living reference. Submit. You see, it provided me
[10:58] um with some questions. I answered them. Now I  click submit answers. It's going to now use the
[11:04] skill to structure my knowledge in the best way  possible. So now while all this is happening,
[11:10] it's basically building something from it. And  here it's telling me, okay, so how many sources
[11:14] you want to have? Um let's say 20 to 100 medium.  Do we need entity pages for individual stocks,
[11:20] funds, or companies or people? Yes, let's do  that. Uh, do you track your own portfolio data?
[11:26] Occasionally, and we submit the answers. So, you  see, every time it's going to build something,
[11:31] this skill, it's going to ask you a few  questions so it can structure its work
[11:36] properly just for your particular use case. So,  here it asks us a few more questions about what
[11:43] kind of structure we want and what kind  of trading strategies we want to have.
[11:49] We say that we want to provide some sources to it.
[11:55] And as you can see, it generated a really nice  structure where we have the raw folder where we
[12:02] will ingest all the relevant articles, notes,  data and books. Then we have the folder where
[12:07] this knowledge will be structured. That's what  I showed you at the beginning with the concepts,
[12:11] connections, data, entries and so on. And then  uh it will have a folder with the output where
[12:16] it will generate interesting ideas and even a  to-do folder so that you can keep track of the
[12:21] things that you need to do to this repository. And  because it's using infronotus under the hood then
[12:26] it's going to also have a hidden folder InfraNodus  where it's going to store knowledge graphs that
[12:32] will keep record of all the important connections  and concepts that you have in this repository of
[12:38] knowledge. Now, as you can see, it also generated  the cloud MD file and agents MD file that's for
[12:44] Codex with a description of what this project is  about and what we want to achieve with it. So,
[12:49] that will really help the agents later to generate  some interesting ideas from it. And also it added
[12:55] some technical files to make sure that we can  uh track the changes that we do to this and
[13:01] uh save intermediary versions as well. Now,  we say okay, we're ready to ingest a source.
[13:07] So let's say that we have a source already.  So I'm going to say yes. Let's let's do the
[13:13] source. And then it's going to tell me okay. So  where do you want to take the source? And I can
[13:17] tell it okay I have all my research papers on the  Dropbox research papers folder. Find everything
[13:24] relevant to finance and economics there. And you  see the claude is very clever in this case because
[13:30] it's basically going to search that folder and  extract the most interesting papers and images
[13:36] and other assets I have on the topic of finance,  money, and economics. As you can see, it says it
[13:43] found a lot of material. Now, it's going to sort  it into tiers of relevance and organize it. So,
[13:48] here it's asking us what it should actually  extract. Core finance, finance and market dynamics
[13:54] or everything potentially interesting. I think  maybe not everything but let's say that we want
[13:59] finance and market dynamics around 30 papers. What  clo is going to do now is going to extract the
[14:06] content from those papers extract the content from  PDFs and transform it into markdown files which is
[14:12] very good because then you would be able to open  it using any text editor and also they would be
[14:20] accessible to your LLM because it will basically  be like plain text. Now it's copying the files to
[14:26] my raw folder that all the books are copied here.  And then like it says here, it's going to create
[14:32] wiki pages for these papers in parallel. If we go  into wiki, we see that now it has the folder with
[14:38] sources and it's adding paper by paper into that  folder. And here we have a summary of the paper.
[14:45] We have some key takeaways from each paper,  some data and evidence and also relevance,
[14:51] quotes and links to important concepts and ideas  that are present in this paper. So it's creating
[14:57] an interconnected structure of the main ideas  that relate to this project which is really
[15:03] great and it would take you hours or even days  to do that manually. Our end goal here is to
[15:09] extract some interesting insight. So this is why  having this structure is going to be very useful.
[15:14] What happened now here is that from these papers  that it found were relevant, it extracted a list
[15:19] of concepts and also a list of connections and  uh that already creates a really nice structure
[15:27] for our LLMs to use inside cloud in order to  generate some interesting insights for us.
[15:32] While it's doing this job, we can actually use the  InfraNodus extension that I have installed into
[15:38] my cursor in order to see the content of every  page that we have generated here. So for example,
[15:45] here I have a page on balance of payments. If I  want to see what it's about, I can rightclick then
[15:51] click in front of this visualize as a graph and  then it will generate for me a really nice visual
[15:56] overview of the main ideas in this summary  of the concept of balance of pay payments.
[16:02] It's about capital dynamics, exchange flow,  investment trends, market insight, and so on. If I
[16:07] open the bond one, then if I right click on that,  I can then visualize the main concepts there. So,
[16:14] as you can see, you're actually creating really  nice visual representation of the main ideas.
[16:20] And if I want to see how all of my concepts  connect, while of course, Claude will create some
[16:26] connections for me. If I don't want to rely on AI  to do that, I can right click on the whole folder,
[16:31] then click visualize as a graph. And what's going  to happen here is that InfraNodus will visualize
[16:37] uh all the concepts from all these different files  and show me what are the most important topics. So
[16:42] I can see there's a lot of on bond returns and  financial flows, but for example, very little
[16:48] on equity analysis or regression analysis. And if  I decide that maybe regression analysis is quite
[16:54] important because it will provide me a framework  through which I can analyze financial data then
[16:59] it's going to be quite important and I should  develop this cluster more. So you see already just
[17:03] from this visualization that is happening live as  LLM is building that knowledge base I can already
[17:10] optimize it by understanding which topics I should  develop more what kind of sources I should seek to
[17:17] make that more coherent and interconnected.  And if I go into the gaps analysis here,
[17:22] I can also see which topics are not so well  connected. And then using this AI advice button,
[17:28] I can generate a question which is like an  advanced prompt that I can feed back to my
[17:33] claude by selecting it and pasting it here.  That will enable clot to understand a little
[17:38] bit better how it can develop ideas further. So,  it's pretty interesting because not only you get a
[17:43] really nice visual overview of what's happening  in your folders as LLM is building this wiki,
[17:48] but you can already optimize it by identifying  the clusters that are underdeveloped and that
[17:53] you want to develop further or finding the gaps  that you want to bridge with new ideas. Actually,
[17:59] let me show you how that would work in practice.  So here I have a gap identified in the folder on
[18:05] concepts and if notice shows me that there is  a cluster on financial flows and on regression
[18:10] analysis there is a gap between them. So what I  can do is I can click on the question here and
[18:15] then it's going to find me the statements from the  folder of concepts that could be better connected
[18:20] and here it provides these two statements to  me. But then there is also the InfraNodus log
[18:26] which is basically a prompt that uses the  underlying graph that I can use to generate
[18:31] some interesting insight. So I'm going to copy  that prompt with the underlying graph structure
[18:35] that shows the two clusters and the possible  connections between them. Then I'm going to
[18:39] go to terminal and open another terminal window.  So the second one launch clo there and say okay
[18:46] based on what you see in the concepts folder  try to think of the connection between these
[18:55] clusters and then I paste this structure which I  copied from the InfraNodus log with the underlying
[19:01] graph structure that represents these clusters.  Then I provide it here and I can also use this
[19:07] as inspiration. These are the actual extracts from  the concept documents that uh contain uh the most
[19:15] dense representation of those clusters. And then  I can also say to claude uh also take this into
[19:22] account. Okay. Then I provide the statements  and then you see now it's going to basically
[19:27] use this structural information. So I point LLM's  attention to the gap that exists. I provided the
[19:33] underlying structure. I give it some context and  then I say okay use the documents in the concepts
[19:38] folder in order to generate an interesting idea  that would connect these ideas together. How does
[19:43] regression analysis connect to financial flow? And  you see it's doing the work. It's extracting some
[19:48] relevant concepts from our wiki from the concepts  themselves analyzing all these documents taking
[19:55] this graph structure that uh we we identified  into account and then now it's going to generate
[20:00] an insight for us. Let's see what it generates.  So as you can see here based on this gap after
[20:06] doing some research it identifies a potential  research question how the critical transitions
[20:11] and systemic fragility affect the bop a fix  models reliability and it tells us do you want
[20:17] me to create a connection page or question page  to capture any of these insights. Yes. Let's add
[20:23] the question and add it into to-do list because  we want to research it further later. Right. So
[20:30] now it will use that question that it extracted  that found the gap identified the gap generated
[20:35] an interesting research question and then it's  going to add that question into our to-dos list
[20:40] so that we can later explore it either manually  or automatically using AI and kind of like focus
[20:46] on something which is not yet explored in the  literature but that touches upon the topics
[20:53] that the literature is talking about. So we  know that we will have uh good quality source
[20:58] material to work with but we will actually come  up with something new and that can be interesting
[21:02] for us because we will link these ideas in new  ways. So here it added this into to-do and if
[21:07] we look at the wiki we now see that we have the  concepts we have connections between some of the
[21:12] concepts. We have also important entities and we  have some research questions that we are adding
[21:18] that will enable us to then guide our research  and explore the connections between the topics
[21:23] that are not connected yet. So then we will be  sure to generate new insights this way. So this
[21:29] is how the system works in a nutshell. I know it's  a lot to ingest, but what I recommend you to do is
[21:36] just to install the skill and to try it for one  of the projects you have so you can test run it
[21:40] yourself with your own data and see what kind of  insights it can generate for you. And if you see
[21:45] that you want this model to work differently, you  can always modify that skill and add some changes
[21:51] into it that will suit your workflow better.  And once you have something like this generated,
[21:56] you can interact with it using cloud code  using your favorite IDE or you can even go
[22:01] back inside Obsidian and you will have that  structure presented here. So you can use the
[22:06] more traditional Obsidian structure to navigate  through this data, visualize the connections
[22:11] between different ideas and see how you can link  them together in new ways. So you have Obsidian
[22:17] as a viewer of this information including the  InfraNodus graph view plug-in or you have a more
[22:23] low-level representation here where you use claude  or your favorite AI in order to interact with this
[22:29] data and to generate new ideas from it and you  have the graph available here which you can use to
[22:35] also visualize this knowledge to find gaps inside  and to see what the main concepts are and how they
[22:39] relate to one another and finally you can use the  InfraNodus MCP server inside cloud code itself in
[22:45] order to generate knowledge graphs and to save  them into the InfraNodus folder so that you have
[22:49] an ongoing memory of the conversations you're  having. So here if I want to create such graph
[22:54] I can go back to the first discussion we had where  it ingested 20 papers on the topic. It says the
[23:01] wiki is ready to use open the finance folder as of  old and then when you start quering it ingesting
[23:06] new sources or gap analysis if you like. So for  example now I can say okay now that this whole
[23:11] wiki is ready run gap analysis on it and then  look what happens here it's basically going to
[23:17] do the same thing that I do in the graph when I  choose gaps but now it's going to read through
[23:22] the main concepts that it ingested and then it's  going to launch the InfraNodus gap analysis tool
[23:29] in order to generate uh the clusters that could  be better connected and then help us generate new
[23:35] ideas from them. So you see here it says let me  run the InfraNodus analysis directly on the wiki
[23:39] content to identify structural gaps. So it first  gathers all the wiki content from all the files
[23:44] that it saved into the wiki here. It will then  create a query for them. Now as you can see it
[23:50] created the full wiki text and then it's going to  use the InfraNodus generate content gaps tool via
[23:56] the MCP server that is connected to my cloud code  and then it's going to generate content gaps based
[24:02] on this content and deliver me similar insights  that I can get also through this visual interface
[24:09] either inside the cursor or anti-gravity or  inside Obsidian as well if I'm using the AI
[24:15] questions here that identifies the gaps and then  generates questions based on those gaps. But here
[24:20] the difference is that I don't actually need to  use the graph. So if I feel uncomfortable using
[24:26] the graph interface, I can just delegate all this  responsibility to my LLM to the MCP server and
[24:32] then I'll just have the readym made insights. But  I find it's important to also demonstrate to you
[24:37] how this whole thing works even if it makes it  a bit more complicated because you know what's
[24:41] happening under the hood that it's not going to be  some hallucination but we're actually performing
[24:46] structural analysis here where we identify  the main topical clusters find the gaps then
[24:52] feed those gaps to the model with the underlying  graph structure and steer its attention to the
[24:57] parts that should be better connected so that the  quality of insights we get are much less generic
[25:02] and much more original. So as you can see here, it  provided me the final outcome of the research it
[25:08] made, identified some of the priorities, added  them into to-do list. So that's the stuff that
[25:13] I should be working on to explore these ideas  further. And then it even created an ontology,
[25:18] an InfraNodus graph with all the main ideas inside  that show how the different concepts that I have
[25:25] in this whole wiki relate to one another in  relation to this particular exploration. So
[25:30] that next time when I will be talking to this  folder through clot code or through any other
[25:35] tool uh LLM will have access not only to the whole  wiki structure but also to all the relations and
[25:42] ideas inside and it will have a much more precise  understanding of how all of these concepts relate
[25:47] and also what questions I should be working on  to have this knowledge evolve further. So let
[25:52] me know how this works for you. If you have any  questions, please ask them in the comments below
[25:56] the video. And I hope you find this demo useful  and I encourage you to try it on your own notes,
[26:02] ideas, research papers, books. I think you will  get really interesting results. I did. Thank you.
[0:00] Last week, Andrej Karpathy, a prominent AI 
researcher, released a super useful framework
[0:06] called LLM Wiki that uses LLM to supercharge your 
research. It's a really good framework. However,
[0:13] there's a critical piece missing. It's not 
aware of itself. The problem that Karpati
[0:18] himself pointed out is that when you interact 
with your standard AI and you upload some files
[0:23] and you want to get a result, what happens is 
that it retrieves uh some chunks of text using
[0:29] rag retrieval augmented generation and gives you 
the result and then every time you interact with
[0:34] this system, it's always going to do the same 
thing and forget what it's done in the past. So
[0:39] you don't have a knowledge base that is evolving 
with you. Andrej Karpathy proposed to resolve this
[0:45] problem by building so-called LLM wiki which you 
can open in any IDE or Obsidian that basically
[0:51] retrieves all your raw papers or notes organizes 
them in a folder which we call raw folder here
[0:58] and then it generates a wiki where it lists all 
the concepts and the connections between them
[1:03] the main ideas. So it creates an organization 
for your knowledge and then you can use this
[1:09] structure to then interact with it and to generate 
insight. The problem with the system however is
[1:14] that even though you have the structure you 
still need something to navigate through it
[1:19] because if you just ask your LLM to produce the 
results it's going to extract the concepts that
[1:23] you have listed the questions the data but then 
it's going to produce the most probable outcome
[1:29] because that's what LLMs are trained to do. This 
is where knowledge graphs can be very useful.
[1:35] For the last 10 years, I've been working on 
InfraNodus, a knowledge graph visualization tool
[1:41] that represents ideas as network and then applies 
graph science metrics to identify the main ideas
[1:47] and clusters of them inside, but most importantly 
identify the gaps in your knowledge which you can
[1:53] then use to generate new ideas. So, I'm going 
to show you how you can augment this LLM wiki
[1:59] with knowledge graphs so that you can generate 
much more pertinent insights and so that you can
[2:05] direct your LLM's thinking through that structure 
that it created. I'll just show you a couple of
[2:11] things it can do and then I'm going to demonstrate 
how you can set the whole system up from zero. So,
[2:17] let me show you here. I have an already prepared 
wiki that I made from my documents on a research
[2:22] topic I'm working on. And uh what I did first is 
that I ingested all my papers into the raw folder
[2:29] here uh which you can see some papers here, 
some notes that I have on different topics
[2:33] and so on. And then I ran the skill that I'm 
going to also make available to you for free
[2:38] uh through my GitHub repo. I'm going to leave the 
link in the description to the video below that
[2:43] basically ingests all this raw material and then 
generates structured representation of the main
[2:48] concepts in those research papers, how they're 
connected to one another. So the main connections,
[2:54] some sources that it uses so that you can always 
get back to those sources or add more interesting
[3:00] research papers and then systems that it's talking 
about. Okay. So normally what happens here is that
[3:05] once you have that wiki created here which is 
a structured representation of your knowledge,
[3:10] you could launch claude code inside that folder 
and then start asking questions about it. But when
[3:17] you ask questions, what it's going to do is that 
it's going to scan through your wiki, extract some
[3:21] concepts, and then produce the most plausible 
response that kind of connects everything
[3:26] together. It can be good for some use cases, but 
when you want to generate new ideas, is not so
[3:31] interesting because the results are going to be 
quite generic. What I need first, and this is
[3:35] where knowledge graphs are very useful, is to get 
an understanding of the structure of this wiki.
[3:41] And so for this you can actually use knowledge 
graph of InfraNodus which you can use both from
[3:48] your favorite IDE like in this case I use cursor 
maybe you're using anti-gravity you can install
[3:53] the extension of InfraNodus here and then when you 
have that folder of concepts for example where I
[3:59] have the most important concepts listed that were 
extracted from the research papers I right click
[4:03] on it then I click InfraNodus visualize as a 
graph and then the extension which is opened
[4:08] in the side bar here is going to visualize to me 
what are the main topics in my research and this
[4:14] is very useful because first of all it reminds me 
what are the main ideas inside network theory you
[4:20] know then phase dynamics fractal structure but 
also shows me the smaller clusters that I want
[4:26] to develop in order to make this whole discourse 
much more coherent so I will focus on the smaller
[4:32] ideas like power mechanisms here for example and 
explore them further or frequency modulation and
[4:38] so on right so this helps me see what are the 
topics that I need to develop further. But then
[4:43] I can also go into gaps and ask it to show me 
some clusters that could be better connected
[4:48] and then focus on the connections between those 
clusters to generate new ideas. You can also use
[4:54] this plug-in inside Obsidian itself. So here 
for example I have Obsidian and in Obsidian we
[4:59] have the InfraNodus plugin. So then I would open 
that same folder concepts and visualize it as an
[5:05] InfraNodus graph and then it would show me the 
connections between the ideas that exist in this
[5:10] folder give me the same topical overview and also 
I could identify the gaps and then by bridging the
[5:16] gaps and using AI to generate research questions 
I can then generate new ideas that bridge those
[5:22] different clusters together. So this would be one 
approach that you can use it visually like this or
[5:28] you can also go back to cloud and actually use 
the InfraNodus mcp server which is basically a
[5:34] connector for your llm to think in terms of these 
graphs so that it would create that same graph
[5:41] representation of your content. So I could ask 
okay use InfraNodus generate graph tool to analyze
[5:47] the concepts in the wiki concepts folder. Okay. So 
then it would connect to the InfraNodus MCP tool
[5:54] which is basically an like an API that connects 
uh this whole content to Infronotus and then it
[6:01] extracts the list of the concepts that we have 
listed here as markdown files. Then you see it
[6:06] uses the InfraNodus generate knowledge graph tools 
and it's going to give me a similar insight to
[6:11] what I visually see. So here again I can generate 
an overview and then I can use InfraNodus to
[6:17] identify the main clusters and then ask InfraNodus 
to generate insights based on the gaps between
[6:21] these clusters. So that would be one approach 
to use this. You see it runs the tool then it
[6:27] generates the analysis and then it will generate 
a response. As you can see here it provides me
[6:31] information about the graph structure main topical 
clusters fractal dynamics critical transitions
[6:36] process coupling and also information about the 
gaps. So you can use the graphs if you want or
[6:42] you can also use the MCP server inside cloud code 
itself. However, an even more advanced approach
[6:48] is to add knowledge graphs into the structure of 
this LLM wiki so that instead of just analyzing
[6:55] the folders with the external tool, you actually 
integrate knowledge graphs into the process of
[7:01] structuring your knowledge. So that skill that 
I made available actually allows you to do that.
[7:06] And what it does is that once your wiki is created 
and you generate some ideas from it, then it will
[7:14] create a folder InfraNodus where it's going to 
save so-called ontology graphs that I was talking
[7:19] about before on my channel which describe the main 
concepts and relations between them. So then later
[7:25] if you say want to analyze what's happening in 
this repository in this wiki you can go back to
[7:32] Obsidian for instance and then you can open that 
folder InfraNodus and for example if you want to
[7:37] see a graph of all the concepts you have here then 
you just click on this and Obsidian InfraNodus
[7:43] plug-in shows you what are the main concepts you 
have here and also which of them are disconnected.
[7:49] So that can also give you information how you can 
connect them better. So for example, you can see
[7:54] like okay, you have synchronization patterns here, 
but they're not so connected to, for example,
[8:00] fractal networks. So you select these two and 
then you generate an interesting question that
[8:04] can link them together. And this will give you an 
idea for how you can link disconnected clusters
[8:10] of your knowledge and make your whole research 
much more coherent and interconnected which can
[8:16] be very useful for improving its structure. Okay, 
so this would be another approach how you could
[8:20] use it. You generate InfraNodus ontology graphs 
for everything that it does. So it's some kind
[8:27] of living memory of what's happening in the system 
and then every time you come back to it claude or
[8:32] whatever system you use will have access to this 
system of rules of of how the concepts connect in
[8:38] your wiki and then it will be able to extract them 
and generate some interesting ideas from them. So
[8:43] that would be another deeper approach where you 
integrate knowledge graphs into the actual LLM
[8:48] wiki. Now that I showed you how all of this looks 
like, let me show you how you would actually set
[8:54] something like this up. So first I would create 
a new folder on my computer and I would give it
[8:59] the name of the research I'm working on. So for 
example, I want to make another one on finance.
[9:04] I click create and then I go inside and I simply 
open the empty folder in my favorite programming
[9:10] development environment which is cursor in this 
way. All right. So now it's completely empty.
[9:16] Then what I do, I open terminal inside here. 
And by the way, you could also do it directly
[9:21] through terminal. But what I like is that in 
something like Corsor or if you like anti-gravity,
[9:25] you can use anti-gravity. I can actually see the 
file structure on the left. That helps. Then I
[9:29] open cloud and because I already installed that 
LLM wiki skill that I'm going to link to in the
[9:35] description to the video below, I can then um ask 
it okay use LLM wiki skill to create a repository
[9:45] of knowledge on finance that I have. And you can 
even make a general query like that and see how
[9:53] it does. Sometimes you will need to tell it where 
it should take the data. Let's see if the skill
[9:57] will actually pick it up because I structured it 
in a way where it will ask you questions for how
[10:02] to proceed. Here it's asking us shall I use the 
skill lm wiki we say yes. Okay let's use the skill
[10:07] and then see what it does. So first of all it's 
asking me okay you want to explore finance that
[10:12] this wiki is for just explain to me what you want 
to work on personal investing microeconomics and
[10:18] market personal finance trading and strategy. So 
I would say that I would like to work on personal
[10:24] investing. I think that will be interesting for 
me. And also trading and strategy. Okay. So then
[10:29] let's click next. And you see everything that it's 
going to do. It's going to ask me a question about
[10:33] it. And then it tells me, okay, so what kind of 
sources you want to feed? Articles? Yes. Books
[10:38] and papers? Videos and podcasts? No. But personal 
notes and data? Yes. Okay. And then it's telling
[10:44] me, okay, so what's your end goal for this finance 
week? So I think I want to track and learn. I want
[10:51] to support my decisions. And I want to also have a 
living reference. Submit. You see, it provided me
[10:58] um with some questions. I answered them. Now I 
click submit answers. It's going to now use the
[11:04] skill to structure my knowledge in the best way 
possible. So now while all this is happening,
[11:10] it's basically building something from it. And 
here it's telling me, okay, so how many sources
[11:14] you want to have? Um let's say 20 to 100 medium. 
Do we need entity pages for individual stocks,
[11:20] funds, or companies or people? Yes, let's do 
that. Uh, do you track your own portfolio data?
[11:26] Occasionally, and we submit the answers. So, you 
see, every time it's going to build something,
[11:31] this skill, it's going to ask you a few 
questions so it can structure its work
[11:36] properly just for your particular use case. So, 
here it asks us a few more questions about what
[11:43] kind of structure we want and what kind 
of trading strategies we want to have.
[11:49] We say that we want to provide some sources to it.
[11:55] And as you can see, it generated a really nice 
structure where we have the raw folder where we
[12:02] will ingest all the relevant articles, notes, 
data and books. Then we have the folder where
[12:07] this knowledge will be structured. That's what 
I showed you at the beginning with the concepts,
[12:11] connections, data, entries and so on. And then 
uh it will have a folder with the output where
[12:16] it will generate interesting ideas and even a 
to-do folder so that you can keep track of the
[12:21] things that you need to do to this repository. And 
because it's using infronotus under the hood then
[12:26] it's going to also have a hidden folder InfraNodus 
where it's going to store knowledge graphs that
[12:32] will keep record of all the important connections 
and concepts that you have in this repository of
[12:38] knowledge. Now, as you can see, it also generated 
the cloud MD file and agents MD file that's for
[12:44] Codex with a description of what this project is 
about and what we want to achieve with it. So,
[12:49] that will really help the agents later to generate 
some interesting ideas from it. And also it added
[12:55] some technical files to make sure that we can 
uh track the changes that we do to this and
[13:01] uh save intermediary versions as well. Now, 
we say okay, we're ready to ingest a source.
[13:07] So let's say that we have a source already. 
So I'm going to say yes. Let's let's do the
[13:13] source. And then it's going to tell me okay. So 
where do you want to take the source? And I can
[13:17] tell it okay I have all my research papers on the 
Dropbox research papers folder. Find everything
[13:24] relevant to finance and economics there. And you 
see the claude is very clever in this case because
[13:30] it's basically going to search that folder and 
extract the most interesting papers and images
[13:36] and other assets I have on the topic of finance, 
money, and economics. As you can see, it says it
[13:43] found a lot of material. Now, it's going to sort 
it into tiers of relevance and organize it. So,
[13:48] here it's asking us what it should actually 
extract. Core finance, finance and market dynamics
[13:54] or everything potentially interesting. I think 
maybe not everything but let's say that we want
[13:59] finance and market dynamics around 30 papers. What 
clo is going to do now is going to extract the
[14:06] content from those papers extract the content from 
PDFs and transform it into markdown files which is
[14:12] very good because then you would be able to open 
it using any text editor and also they would be
[14:20] accessible to your LLM because it will basically 
be like plain text. Now it's copying the files to
[14:26] my raw folder that all the books are copied here. 
And then like it says here, it's going to create
[14:32] wiki pages for these papers in parallel. If we go 
into wiki, we see that now it has the folder with
[14:38] sources and it's adding paper by paper into that 
folder. And here we have a summary of the paper.
[14:45] We have some key takeaways from each paper, 
some data and evidence and also relevance,
[14:51] quotes and links to important concepts and ideas 
that are present in this paper. So it's creating
[14:57] an interconnected structure of the main ideas 
that relate to this project which is really
[15:03] great and it would take you hours or even days 
to do that manually. Our end goal here is to
[15:09] extract some interesting insight. So this is why 
having this structure is going to be very useful.
[15:14] What happened now here is that from these papers 
that it found were relevant, it extracted a list
[15:19] of concepts and also a list of connections and 
uh that already creates a really nice structure
[15:27] for our LLMs to use inside cloud in order to 
generate some interesting insights for us.
[15:32] While it's doing this job, we can actually use the 
InfraNodus extension that I have installed into
[15:38] my cursor in order to see the content of every 
page that we have generated here. So for example,
[15:45] here I have a page on balance of payments. If I 
want to see what it's about, I can rightclick then
[15:51] click in front of this visualize as a graph and 
then it will generate for me a really nice visual
[15:56] overview of the main ideas in this summary 
of the concept of balance of pay payments.
[16:02] It's about capital dynamics, exchange flow, 
investment trends, market insight, and so on. If I
[16:07] open the bond one, then if I right click on that, 
I can then visualize the main concepts there. So,
[16:14] as you can see, you're actually creating really 
nice visual representation of the main ideas.
[16:20] And if I want to see how all of my concepts 
connect, while of course, Claude will create some
[16:26] connections for me. If I don't want to rely on AI 
to do that, I can right click on the whole folder,
[16:31] then click visualize as a graph. And what's going 
to happen here is that InfraNodus will visualize
[16:37] uh all the concepts from all these different files 
and show me what are the most important topics. So
[16:42] I can see there's a lot of on bond returns and 
financial flows, but for example, very little
[16:48] on equity analysis or regression analysis. And if 
I decide that maybe regression analysis is quite
[16:54] important because it will provide me a framework 
through which I can analyze financial data then
[16:59] it's going to be quite important and I should 
develop this cluster more. So you see already just
[17:03] from this visualization that is happening live as 
LLM is building that knowledge base I can already
[17:10] optimize it by understanding which topics I should 
develop more what kind of sources I should seek to
[17:17] make that more coherent and interconnected. 
And if I go into the gaps analysis here,
[17:22] I can also see which topics are not so well 
connected. And then using this AI advice button,
[17:28] I can generate a question which is like an 
advanced prompt that I can feed back to my
[17:33] claude by selecting it and pasting it here. 
That will enable clot to understand a little
[17:38] bit better how it can develop ideas further. So, 
it's pretty interesting because not only you get a
[17:43] really nice visual overview of what's happening 
in your folders as LLM is building this wiki,
[17:48] but you can already optimize it by identifying 
the clusters that are underdeveloped and that
[17:53] you want to develop further or finding the gaps 
that you want to bridge with new ideas. Actually,
[17:59] let me show you how that would work in practice. 
So here I have a gap identified in the folder on
[18:05] concepts and if notice shows me that there is 
a cluster on financial flows and on regression
[18:10] analysis there is a gap between them. So what I 
can do is I can click on the question here and
[18:15] then it's going to find me the statements from the 
folder of concepts that could be better connected
[18:20] and here it provides these two statements to 
me. But then there is also the InfraNodus log
[18:26] which is basically a prompt that uses the 
underlying graph that I can use to generate
[18:31] some interesting insight. So I'm going to copy 
that prompt with the underlying graph structure
[18:35] that shows the two clusters and the possible 
connections between them. Then I'm going to
[18:39] go to terminal and open another terminal window. 
So the second one launch clo there and say okay
[18:46] based on what you see in the concepts folder 
try to think of the connection between these
[18:55] clusters and then I paste this structure which I 
copied from the InfraNodus log with the underlying
[19:01] graph structure that represents these clusters. 
Then I provide it here and I can also use this
[19:07] as inspiration. These are the actual extracts from 
the concept documents that uh contain uh the most
[19:15] dense representation of those clusters. And then 
I can also say to claude uh also take this into
[19:22] account. Okay. Then I provide the statements 
and then you see now it's going to basically
[19:27] use this structural information. So I point LLM's 
attention to the gap that exists. I provided the
[19:33] underlying structure. I give it some context and 
then I say okay use the documents in the concepts
[19:38] folder in order to generate an interesting idea 
that would connect these ideas together. How does
[19:43] regression analysis connect to financial flow? And 
you see it's doing the work. It's extracting some
[19:48] relevant concepts from our wiki from the concepts 
themselves analyzing all these documents taking
[19:55] this graph structure that uh we we identified 
into account and then now it's going to generate
[20:00] an insight for us. Let's see what it generates. 
So as you can see here based on this gap after
[20:06] doing some research it identifies a potential 
research question how the critical transitions
[20:11] and systemic fragility affect the bop a fix 
models reliability and it tells us do you want
[20:17] me to create a connection page or question page 
to capture any of these insights. Yes. Let's add
[20:23] the question and add it into to-do list because 
we want to research it further later. Right. So
[20:30] now it will use that question that it extracted 
that found the gap identified the gap generated
[20:35] an interesting research question and then it's 
going to add that question into our to-dos list
[20:40] so that we can later explore it either manually 
or automatically using AI and kind of like focus
[20:46] on something which is not yet explored in the 
literature but that touches upon the topics
[20:53] that the literature is talking about. So we 
know that we will have uh good quality source
[20:58] material to work with but we will actually come 
up with something new and that can be interesting
[21:02] for us because we will link these ideas in new 
ways. So here it added this into to-do and if
[21:07] we look at the wiki we now see that we have the 
concepts we have connections between some of the
[21:12] concepts. We have also important entities and we 
have some research questions that we are adding
[21:18] that will enable us to then guide our research 
and explore the connections between the topics
[21:23] that are not connected yet. So then we will be 
sure to generate new insights this way. So this
[21:29] is how the system works in a nutshell. I know it's 
a lot to ingest, but what I recommend you to do is
[21:36] just to install the skill and to try it for one 
of the projects you have so you can test run it
[21:40] yourself with your own data and see what kind of 
insights it can generate for you. And if you see
[21:45] that you want this model to work differently, you 
can always modify that skill and add some changes
[21:51] into it that will suit your workflow better. 
And once you have something like this generated,
[21:56] you can interact with it using cloud code 
using your favorite IDE or you can even go
[22:01] back inside Obsidian and you will have that 
structure presented here. So you can use the
[22:06] more traditional Obsidian structure to navigate 
through this data, visualize the connections
[22:11] between different ideas and see how you can link 
them together in new ways. So you have Obsidian
[22:17] as a viewer of this information including the 
InfraNodus graph view plug-in or you have a more
[22:23] low-level representation here where you use claude 
or your favorite AI in order to interact with this
[22:29] data and to generate new ideas from it and you 
have the graph available here which you can use to
[22:35] also visualize this knowledge to find gaps inside 
and to see what the main concepts are and how they
[22:39] relate to one another and finally you can use the 
InfraNodus MCP server inside cloud code itself in
[22:45] order to generate knowledge graphs and to save 
them into the InfraNodus folder so that you have
[22:49] an ongoing memory of the conversations you're 
having. So here if I want to create such graph
[22:54] I can go back to the first discussion we had where 
it ingested 20 papers on the topic. It says the
[23:01] wiki is ready to use open the finance folder as of 
old and then when you start quering it ingesting
[23:06] new sources or gap analysis if you like. So for 
example now I can say okay now that this whole
[23:11] wiki is ready run gap analysis on it and then 
look what happens here it's basically going to
[23:17] do the same thing that I do in the graph when I 
choose gaps but now it's going to read through
[23:22] the main concepts that it ingested and then it's 
going to launch the InfraNodus gap analysis tool
[23:29] in order to generate uh the clusters that could 
be better connected and then help us generate new
[23:35] ideas from them. So you see here it says let me 
run the InfraNodus analysis directly on the wiki
[23:39] content to identify structural gaps. So it first 
gathers all the wiki content from all the files
[23:44] that it saved into the wiki here. It will then 
create a query for them. Now as you can see it
[23:50] created the full wiki text and then it's going to 
use the InfraNodus generate content gaps tool via
[23:56] the MCP server that is connected to my cloud code 
and then it's going to generate content gaps based
[24:02] on this content and deliver me similar insights 
that I can get also through this visual interface
[24:09] either inside the cursor or anti-gravity or 
inside Obsidian as well if I'm using the AI
[24:15] questions here that identifies the gaps and then 
generates questions based on those gaps. But here
[24:20] the difference is that I don't actually need to 
use the graph. So if I feel uncomfortable using
[24:26] the graph interface, I can just delegate all this 
responsibility to my LLM to the MCP server and
[24:32] then I'll just have the readym made insights. But 
I find it's important to also demonstrate to you
[24:37] how this whole thing works even if it makes it 
a bit more complicated because you know what's
[24:41] happening under the hood that it's not going to be 
some hallucination but we're actually performing
[24:46] structural analysis here where we identify 
the main topical clusters find the gaps then
[24:52] feed those gaps to the model with the underlying 
graph structure and steer its attention to the
[24:57] parts that should be better connected so that the 
quality of insights we get are much less generic
[25:02] and much more original. So as you can see here, it 
provided me the final outcome of the research it
[25:08] made, identified some of the priorities, added 
them into to-do list. So that's the stuff that
[25:13] I should be working on to explore these ideas 
further. And then it even created an ontology,
[25:18] an InfraNodus graph with all the main ideas inside 
that show how the different concepts that I have
[25:25] in this whole wiki relate to one another in 
relation to this particular exploration. So
[25:30] that next time when I will be talking to this 
folder through clot code or through any other
[25:35] tool uh LLM will have access not only to the whole 
wiki structure but also to all the relations and
[25:42] ideas inside and it will have a much more precise 
understanding of how all of these concepts relate
[25:47] and also what questions I should be working on 
to have this knowledge evolve further. So let
[25:52] me know how this works for you. If you have any 
questions, please ask them in the comments below
[25:56] the video. And I hope you find this demo useful 
and I encourage you to try it on your own notes,
[26:02] ideas, research papers, books. I think you will 
get really interesting results. I did. Thank you.
