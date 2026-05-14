---
title: AI Evaluations Clearly Explained in 50 Minutes (Real Example) | Hamel Husain
video_id: uiza7wp1KrE
url: https://www.youtube.com/watch?v=uiza7wp1KrE
channel: Peter Yang
channel_id: UCnpBg7yqNauHtlNSpOl5-cg
channel_url: https://www.youtube.com/channel/UCnpBg7yqNauHtlNSpOl5-cg
publish_date: '2025-09-28T06:01:58-07:00'
upload_date: '2025-09-28T06:01:58-07:00'
category: Science & Technology
length_seconds: 3150
view_count: 12145
is_live: false
is_upcoming: false
is_private: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi_webp/uiza7wp1KrE/maxresdefault.webp
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
chapters:
- title: What the most valuable part of evals is
  start: 0:00
  start_ms: 0
- title: 'Live walkthrough: Analyzing 100 real production traces'
  start: '1:25'
  start_ms: 0
- title: Creating the eval criteria using a simple spreadsheet
  start: '9:50'
  start_ms: 0
- title: Why binary pass/fail ratings beat 1-5 scores every time
  start: '24:44'
  start_ms: 0
- title: The agreement metric trap that fools most PMs
  start: '28:52'
  start_ms: 0
- title: True positive and negative rates explained
  start: '30:08'
  start_ms: 0
- title: How to set up continuous evals in production
  start: '36:00'
  start_ms: 0
description: 'Today, I want to share a new episode with Hamel Husain.


  Hamel has trained 2,000+ PMs and engineers from companies like OpenAI, Anthropic, and Google on how to run AI evals. In my new episode, he shares a free master class on how to build evals for a real AI agent in just 50 minutes using a simple spreadsheet. I learned a lot from Hamel and I think you will too.


  Hamel and I talked about:

  (00:00) What the most valuable part of evals is

  (01:25) Live walkthrough: Analyzing 100 real production traces

  (09:50) Creating the eval criteria using a simple spreadsheet

  (24:44) Why binary pass/fail ratings beat 1-5 scores every time

  (28:52) The agreement metric trap that fools most PMs

  (30:08) True positive and negative rates explained

  (36:00) How to set up continuous evals in production


  Get the takeaways: https://creatoreconomy.so/p/ai-evaluations-crash-course-in-50-minutes-hamel-husain


  Where to find Hamel:

  X: https://x.com/HamelHusain

  Website: https://hamel.dev/


  📌 Subscribe to this channel – more interviews coming soon!'
notes: Fetched via youtube-transcript-skill; ASR caption track (auto-generated); ingest-time line grouping preserved verbatim from skill output.
---

## Transcript

[0:00] this looking at data accounting. You can get insane value by just doing that. And that's the one part that everyone skips.
[0:07] I'm going to use a spreadsheet to drive home the fact that this process can be dead simple and you can get immense
[0:13] value out of it. When you see an average score of 3.2 versus 3.7, no one really
[0:18] knows what the hell that means. It's not really actionable, honestly. They're like, "Oh, it's like getting better."
[0:23] Honestly, like nobody really knows whether it's getting better or not. So, as a product manager, if you ever see the word agreement, you need to pause
[0:30] and be like, hm, let me dig into this, please. If people don't trust your evals, they won't even trust you. You're
[0:37] done. Okay, welcome everyone. My guest today is uh Hamel. Hamel has trained over
[0:43] 2,000 PMs and engineers from companies like OpenAI, Anthropic, and Google on how to run AI evaluations. He teaches
[0:50] the most popular course on this topic at Maven. So really excited to dig into
[0:55] these best practices and I feel like I made a lot of mistakes that you know and have a lot of assumptions that Hamel can
[1:01] help. So welcome. Really happy to be here. Excited to talk about evals.
[1:07] All right. So you know there's been a lot of like online debate about like you know are evaluable or not like blah blah
[1:12] blah on Twitter and and um let's just make this really practical. Um like let
[1:18] us talk about evals for like a real product like like do you have a do you have a product example that you want to talk about throughout? I do. Yes. So
[1:25] there's a company that I've been working with. Let me share my screen. Sure. So just to set the stage, Nurture Boss
[1:32] is a AI powered property management assistant. And so it's a really
[1:37] interesting use case because it's actually one of the best teaching examples and I love using it because
[1:43] it's messy and there's enough complexity to where it's realistic. And so the
[1:49] question comes like oh okay like how do you do evals? So like lot a lot of times when we talk about evals you know
[1:55] we can show toy examples but sometimes those are oversimplified and it's hard for people to generalize that like how
[2:01] is how am I going to do that for my app? my app is complex, you know, I have other things going on. Well, that's what
[2:07] we're going to show today is actually we're going to look at Nurture Boss's data together and we're going to do like
[2:13] a minimal set of evals and we're going to do that very quickly. Yeah, that'll be awesome. So, I know on your podcast
[2:18] you had Aman on already. He may have talked about Arize. There's a lot of different solutions out there. The ones
[2:24] that I come across the most in practice are Arize, Braintrust, LangSmith. Those
[2:29] are like kind of three popular ones. Mhm. One of the observability platforms that nurture boss used in the beginning was
[2:36] Braintrust. They actually like created their own but for but I'm going to show you their data in Braintrust cuz that's
[2:42] where we have it anonymized. Traces is basically like the chat conversations right with nerbos.
[2:48] Okay. I'll show you what a trace is. The best way is just to look at it rather than me trying to define it. So I'm just going to open one. So trace is a log of
[2:57] all of the history of a particular interaction that your user might be
[3:02] having with an AI including all of the internal things that might be going on that the user doesn't see. Okay. So this
[3:08] is example of a trace. And so what we see here is we have the system message.
[3:15] So you are an AI assistant working work as a leasing team member at the arrow and you have different instructions on
[3:22] how to interact with the res the resident or the prospective resident.
[3:27] You know for example how to deal with maintenance requests or um you know what
[3:34] to do with prospective residents and tour scheduling and all kinds of things like applications.
[3:39] Yep. And you know you can there's a lot of instructions here. We don't need to read all of them. We can scroll down
[3:46] and we see here where is the building located is one of the questions the user
[3:52] is asking. Mhm. And so there's a tool call made. Get communities information. We can expand
[3:58] it and it's pulling back some information. It's making a tool call. The tool call returns with some
[4:03] information which we can see here. Um and then the assistant is is giving an
[4:08] answer. you know this the arrow is located at this address and then it's
[4:14] the user is saying I'm interested in a two-bedroom what's available and actually then it stops
[4:20] um it just dead ends and um there there is a failure of some kind it just wasn't
[4:27] surfaced to the user so this is not like necessarily the most interesting error um
[4:33] this is just like you know something that you would see in the real world now this is example of a trace so So when
[4:39] Jacob came to me, I said, "Okay, Jacob, this is what we're going to do. We're going to look at traces." And he's like,
[4:45] he's like, "What do you mean we're going to look at traces? This seems like we're going in the wrong direction." Like, "This is going to take forever, Hamel.
[4:51] Like, this must be like what what are you like, what are you doing?" He said, "Just trust me. We're going to look at
[4:58] about 100 traces and just we're just going to write notes about what is going wrong. The first one may be painful, but
[5:03] we're going to get really good at it. By the time we get to the 10th one, we're going to be really fast." So, we got to this one. We're like, "Oh, like
[5:09] something happened here." Um, the conversation got cut off. Um, it failed. We had to do some investigation to
[5:16] figure out like what's happened. But we just wrote a note. And so, in this case, um, we can make an annotation. So, I
[5:23] would write a note saying like, hey, there was an error
[5:30] that was not surfaced to the user. Okay? Just write a note. um
[5:38] you know, end the conversation deadended. The point is not to do a full root cause analysis. Just observe what's
[5:45] wrong. Okay? And that's all you got to do is do this. Do it like 100 times.
[5:50] Yeah. Do this 100 times. Now, Jacob's like, "What the hell are we doing? Why are we doing this?" Like, I hired you,
[5:56] Hamel, for evals, and you are like a monkey looking at this data, and like I don't understand what is going on. Like,
[6:02] what is the purpose of this Hamel? this is a very expensive consulting engagement and we are looking at data. I
[6:08] said no trust me we are going to this is going to lead somewhere.
[6:13] Well I mean you're basically human labeling this data right? You're basically saying I'm basically human labeling this data. So let's look at a couple of more like
[6:21] um I think it will become clear why this is valuable really fast. Okay. So this is another trace. You are leasing team
[6:27] member at the Meadow Brick Gardens and your name is Taylor. So giving it a name. uh your goals are to answer
[6:33] questions. Okay, so it's really the same thing. You have, you know, uh you're fielding calls from from residents um
[6:41] actually prospective residents because this looks like it's like a salesfunnel type of mode where you're like
[6:47] encouraging customers to schedule tours. Um so let's go to the first user
[6:52] message. So we got the system message out of the way. The assistant says this call, so this is over voice now. Okay, this call may be
[6:59] recorded blah blah blah. And the the only thing the user says is preview program. I have no idea what that is.
[7:06] Maybe it's something in the system prompt, but I personally don't recall necessarily what that is. The assistant
[7:12] says, "It looks like you might be interested in learning more about community and possibly scheduling a tour. Would you like to schedule a
[7:18] tour?" User says, "No." The assistant says, "Seems like you might have a specific question or need assistance
[7:23] with something related to the our apartment. How can I assist you? Can I tell to a representative?" Obviously,
[7:30] they're trying to talk to a person. Uh, sure. I can connect you to representative. Um, would you like me to
[7:35] do that now? Yes, great. I'll connect you to representative. One moment. Would you like me to connect you? I'm already
[7:42] frustrated. Like, yeah, it's the person to a human being already like so many questions like, "Are you sure? Are you
[7:48] sure? Blah blah." Uh, so okay, like ADU, he wants to talk about ADU. It sounds like you might be interested. Yes. Could
[7:55] you clarify your query? I just want to talk. We've all had this experience at one point in other in our lives.
[8:01] Yeah. Every time, man, I call. Yeah. Yeah. This is not, you know, I want to
[8:06] throw my phone out the window whenever I have this interaction with an AI. Um, so, okay, I understand. I'll connect
[8:13] you. And finally, a tool call is made. We're transferring the call. Okay. So, we feel the pain of the user. We we do
[8:20] honestly. Um, and it's pretty clear like, hey, we So, this this is an this
[8:25] is a clear error in this case. I'll write the the note here just like it to the other one. And you're not trying to like write
[8:31] solutions. You're just trying to write like the note of the problem. Yeah. I'm not trying to debug it. I'm not trying to say like why it happened.
[8:37] I'm not trying to root cause a solution. I'm just journaling why it happens. So you do this. It took us frankly it took
[8:44] us like an hour to do 100 traces. Didn't take us long at all. Okay. But by the end of it, we knew a
[8:51] lot. Like we learned a lot and we learned way more than you could possibly
[8:58] learn by trying to throw any kind of automated solution at this problem. So
[9:03] if you tried to come at nurture boss and put a hallucination score, toxicity score, coherence score, whatever you
[9:10] want to call it, it would not have given us anywhere close to this insight that we had right now. You know, we
[9:16] identified very specific failures and things that are painful, right? By looking at the data we immediately could
[9:23] like see that did you uh use some AI to like summarize the trace data that you labeled or
[9:29] Aha very good question. So while you shouldn't use AI to like do the you
[9:35] should definitely look at the data put your hands on the data you can use AI to help you do the analysis of it. So what
[9:43] happens is I exported all of these logs plus the notes into a spreadsheet. Okay.
[9:50] Okay. Um, and you don't have to use a spreadsheet. I'm going to use a spreadsheet to make it to drive home the fact that this process can be dead
[9:57] simple and you can get immense value out of it. So what I did is I exported like
[10:03] all the notes. So in this column, column A, you have all the notes that I took.
[10:08] Yeah. Okay. So like you know, one note is user was probably asking about lease terms or maybe deposit not about specials. And
[10:16] the AI was talking about specials or another one was the AI offered virtual tours but there is no virtual tour.
[10:24] Um, okay. You know, so all these different and there's the disperate messaging one that we just saw. Okay. And so all these
[10:30] different notes that it took. So what you can do is you can take these
[10:35] notes and you can do something really stupid simple is you can dump them into
[10:42] like claude or chat GPT or whatever and I say okay please analyze the following CSV file. There's a metadata field which
[10:49] is nested field called z_note that contains open codes. So this is like some terminology here. Open codes is
[10:55] just a fancy word for those comments that I made. Okay, just the notes for analysis of LLM logs that we are
[11:03] conducting. Please extract all of the different open codes from the z_note field. Propose five to six categories
[11:08] that can we can create axial codes from. So the axial code is another piece of terminology that means we just want to
[11:13] group them into C. We want to group these notes. We want to just classify them. Okay, this like open code axial code
[11:20] thing is actually some really old technique from social sciences and it's been also used in machine learning for
[11:26] decades. And so that's why we're using this terminology as a shortcut to give to the LLM because the LM knows exactly
[11:34] what this means. They're like, "Oh, I know exactly what you're doing. You're trying to do this technique."
[11:39] Got it. Okay. So, it's better than just saying it's better than just saying like categorizes stuff. It's just some shortcut technique. Yeah.
[11:45] Yeah. It know it has like it it gives it some specificity. it like kind of by saying open code axial code it knows
[11:50] like what my goal is because there's a lot of context when I use that terminology in this technique you could
[11:57] also say categorize though I mean there's no you can start wherever you want so if you want to say categorize start with categorize totally fine it's
[12:04] you know the point is make progress and get value as fast as you can I don't
[12:09] want to be too prescriptive but the point is like you can sort of uh so like
[12:14] okay it kind of iterated a lot on how to open the CSV so We can skip that. But it gave me it gave me like um you know some
[12:22] categories and I didn't really like I didn't necessarily like all of them and I could have been you know I kind of
[12:28] went back and forth a little bit to refine the categories that made sense to me. Um and I just like took I wrote down
[12:35] some categories actually. Um and here are some categories here. So I said like okay tour scheduling rescheduling issue,
[12:44] human handoff or transfer issue, formatting error with the output. They had some formatting errors um like
[12:50] putting markdown inside text messages for example. Um conversational flow
[12:56] issues. So that's like the text thing where just abrupt you know the flow. um
[13:02] making up promises not kept like rescheduling and things like that or not rescheduling but other kinds of promises
[13:09] um and then there's another I usually have another field called none of the above but I didn't do that here just out
[13:15] of simplicity okay and so what you can do is then you can kind of go back and forth and what I did
[13:20] is like in the spreadsheet you know you can use AI so there's AI in this Google spreadsheet the Google Google sheets
[13:26] have AI um you can have the AI formula that's very handy to to show you something. So I say, "Okay, categorize
[13:33] the following note into one of the categories." So you're just like c using LM to like categorize it.
[13:39] And you can see I'm just categorizing these notes that I took like the problems that I found. I'm just putting
[13:44] it into categories. Well, I did know that Google Sheets has this AI feature already. Okay. They're usually very slow.
[13:49] It's cool. It's cool. It's can be slightly janky, but it's okay. It's lightweight and you don't have to use any tools and everyone can understand
[13:56] how to do this. is like demystifies the whole process of what I'm doing cuz if I like open some code you might think oh
[14:02] like you need to be like software engineer to do this or something and like no you don't uh we can use English all the way. So now you have categorized
[14:10] all of these things and now we can use one of my favorite tools pivot tables.
[14:15] So pivot tables um you know if you haven't seen them before really handy in spreadsheets so
[14:22] you can just count how many times each of these categories occurred. Okay. And and we can see the just at a high
[14:29] level um hey oh okay we're having like this conversational flow issue is happening quite a bit. Um you know we
[14:36] also have this like human handoff uh transfer issue and you can kind of get a
[14:41] sense like right away uh what the problem is. Now it is likely that before you even get to this count
[14:47] you already know you've looked at 100 traces. you know in your gut you're like okay you know what I'm going to I need
[14:53] to fix this like human transfer thing like right now you're like I don't even need to like do
[14:58] a data analysis but it's like quick this takes like like less than a few minutes
[15:04] honestly and it just gives you some grounding and it's like lets you see you go from this
[15:09] like mess of like I don't know what's going on to okay like I have some idea about the problems that I have
[15:17] and you have some starting point. Does that make sense? Yeah. Yeah. This is brilliant, dude. But
[15:23] but let me ask you this question. Yeah. So, um in this case, the agent was already live in production before you
[15:29] started doing all all this stuff, right? Like like um but that's not the ideal approach, right? Like I ideally you want
[15:35] to do some of this before or maybe dog food with your team first or like get some users try it.
[15:40] Absolutely. How do you Yeah. So the best case scenario is you dog food it with like
[15:47] you know some friendly customers, you dog food it yourself. That's going to be really good. You can also synthetically
[15:53] generate inputs into your system. So basically what you can do is like think about plausible user questions
[16:01] they may have and you know and try to come up with some hypothesis of where your system will break.
[16:07] Yeah. But there's a certain way to do that. You don't want to just ask an LLM, hey,
[16:12] come up with plausible questions for a prospective tenant that might be looking to rent an apartment. The right way to
[16:19] do it is to come up with some categories. So, is to come up with some dimensions. And what I mean by that is
[16:26] let's say um let's let's think about what good dimensions might be for nurture boss. So
[16:33] for nurture boss uh you might have like resident uh you can have okay like type
[16:40] of customer maybe apartment class maybe so like luxury standard
[16:47] something else I don't know what that is I'm not that creative to like think about on the fly but what was the thing
[16:53] you suggested just type of customer right you can you can get the tenant manager versus the actual resident right depending on who
[16:59] you're talking to yeah uh resident uh manager.
[17:05] Yeah. And you can think of put your product hat on. So like by the way this whole
[17:11] process is is very product oriented like so you know when you read the trace it's
[17:18] not so much about engineering it's putting your product kind of hat on and saying is this the experience that you
[17:24] want your user to have? Does this actually make sense? when it comes to like these dimensions I'm talking about,
[17:30] you're kind of putting your product hat on and saying, "Okay, what are the different personas? What are different categories, different dimensions that
[17:36] you may want to consider?" And then what you want to do is like you know you would take um the kind of combination of
[17:42] these um you know so like luxury resident luxury luxury for resident
[17:47] luxury for manager standard for president standard for manager and you would feed those we call it dimensions
[17:54] into an LLM say okay these are the different dimensions for this for every one of these dimensions generate
[17:59] plausible user queries got it that's like way better than just asking an LLM. Yeah, just because um if
[18:08] if you just ask an LLM, it'll be more a lot more homogeneous and you don't want to be homo you don't want to have
[18:14] homogeneous inputs. You want to explore the space of inputs and so these
[18:19] brainstorming dimensions helps you to kind of make sure you're you're exploring the space being thoughtful
[18:26] about exploring the space. Does that make sense? Got it. Yeah. You want to find all the edge cases and like you know Yeah. Got it.
[18:32] And that's just scratching the surface of this. There's a lot more to generating synthetic data that we could probably get into here, but there
[18:38] there's like more advanced ways to generate synthetic data or things to think about in terms of being more adversarial, how to, you know, come up
[18:45] with hypotheses to help you break your system, so on and so forth. But the short answer is use our system and you
[18:51] can use LMS to help you help basically pretend as synthetic users.
[18:57] That makes sense. Okay, let's go back to the categories you have on the left. So uh so now you have these I mean they're
[19:03] not they're basically pro problems right problems with the product and uh now what are we going to do with with this
[19:09] stuff is this is how we come up with our criteria or should we just start fixing the issues or very good question next very good
[19:15] question so um when we first did this what the top
[19:21] issue was date handling it's like and it was very clear uh you know the the user
[19:27] wanted to schedule an appointment Yeah. And it was always getting the date wrong. And it was very clear like,
[19:36] "Oh, this is so dumb." Like the LM doesn't know what today's date is. We just
[19:41] Okay. We just like forgot. They like, "Yeah, they like forgot to put that in the prompt." It's like, "Do you really need
[19:47] an eval for that?" Maybe not. Like, you know, you don't want to eval. You don't like necessarily
[19:54] want to do eval cuz like it feels good. the whole purpose of anything is to make your product better and to and to
[20:00] iterate and you know move fast. Um and so for that one we're like well let's
[20:06] see like let's just give it what today's date is and that problem basically went
[20:11] away unsurprisingly. So we didn't really need an eval from that. Um other things
[20:17] that more subjective or you know so there's a it's a costbenefit tradeoff.
[20:22] So there's two kinds of evals. One is LM as a judge which we are going to build together. Another one is codebased eval
[20:29] where you don't really need an LM as a judge. It's some kind of assertion that you can make and that's very cheap
[20:36] compared to LM as a judge. And so uh for the date one we actually did we did the
[20:42] like a codebased eval which is like we had some test cases and we're able to test like does the date that's coming
[20:48] out equal to the expected date. And that was like very cheap. We didn't have to do LM as a judge. Got it. You know, but
[20:55] that was like really easy to fix. Now something like, hey, you should be handing off to a human
[21:01] like, okay, that one like we don't know exactly like we did have rules for that
[21:06] already, but the LM is struggling and like we don't really know how we're going to do it. That seems like a really
[21:13] good use case for an LLM-as-judge. And also the the eval is going to provide tons of
[21:18] value even though it's expensive more expensive because we're gonna iterate against it a lot to make progress
[21:26] and so we said okay like let's you know okay we need an LLM judge for the human
[21:32] handoff let's go ahead and do it it's an important problem also. Yeah. Yeah. The main problem that people
[21:39] encounter when doing LLM as a judge is they just prompt another LLM to kind of
[21:46] judge what your LM did and they say is it good? Now that should that should be
[21:51] suspicious, right? Like why is that okay? Like why you just going to tell another LM to tell me if it's okay? Like
[21:58] I don't know. And you would be right to be very suspicious of that. And there is
[22:03] an answer to that. And the answer is you can measure the judge. So it's like an it's a meta evaluation problem is like
[22:10] you need to measure if the judge is good. It's very important. You don't want to skip that step because if you
[22:16] have a bunch of judges LM judges floating around and your stakeholders
[22:21] are like you're reporting them on the dashboard your stakeholders looking at them and everyone's like oh the judge
[22:27] you know this no one's going to understand what you're using LLM-as-judge anyways. They're just going to look at your metric and and when there becomes a
[22:34] significant there's enough gap between reality and your metrics, no one's going to trust you anymore. You want to avoid
[22:40] that. You want Y cuz like if people don't trust your evals, they won't even trust you.
[22:46] You're done. Yeah. Exactly. Yeah. You can't you can't make it have like perfect scores for something, but it's actually totally
[22:51] wrong, right? The way you manage it. Yeah. Yeah. And so Okay. So, how do you go about this? Well, thankfully when you're doing
[22:58] this axial coding stuff, right, you actually I've identified really good test cases or some reasonable text uh
[23:05] test cases that you can use that are labeled. You you already labeled them as a human. So, you have some ground truth.
[23:12] And these are things that you can use to calibrate an LLM judge to see if you can
[23:18] create a judge that's good enough. Okay, green enough is just like green up is like how closely does it match to human
[23:24] labels, right? That's kind of what how close does the match to human label? Yeah. So that's what we're going to do next
[23:30] is we are going to think about first we're going to write the prompt and this is like the dumbest prompt. I'm not
[23:37] saying like this is a good prompt. This is just a prompt. And the point is not to like have a
[23:44] prompt recipe or some like magic thing is just to iterate. Okay. And you want to just specify kind of the requirements
[23:51] of like in this case what is a good handoff or when should you be doing a handoff and when should it happen and so
[23:57] you know you are scoring a leasing assistant uh to determine if there was a handoff failure there should be handoff
[24:05] if any of the these things occur um you know or sorry there there is a
[24:11] handoff failure if any of these things occur like if a human requested to be handed off, but you just ignored them or
[24:19] looped through it too many times. That's a failure. Got it? Yeah. And there's a list of these seven failures. You don't have to read all of
[24:25] them, but you get the idea. And we also say when there's not a failure, just out of completeness. And we say we want to
[24:31] return exactly true or false, binary. So, it's worth lingering on this for a
[24:39] moment. So, it's very important for an LLM judge that you output a binary
[24:44] score. 99% of the time you don't want to import uh export like a like art scale
[24:50] or a you know a score of one to five um or some kind of score because that
[24:57] introduces tremendous complexity. Yeah. You know LM's are not good at continuous
[25:04] scores number one. Number two is the output is not going to be clear. When
[25:09] you see an average score of 3.2 two versus 3.7. No one really knows what the
[25:15] hell that means. 3.7. Yeah. Yeah. No one. And it's not really actionable, honestly. They're like, "Oh, it's like
[25:21] getting better." Honestly, like nobody really knows whether it's getting better or not. I found that when you try to
[25:28] hide behind a score, you're not really making a decision. And like what you're trying to the frame here is is this
[25:36] feature good enough to ship? Yes or no? Make a decision. You know what? What is the line? there
[25:41] is a line somewhere and so like there has to be right and so we don't want to score um wherever possible you want to
[25:49] simplify it the score just makes it too complex yeah it's like uh fake science you know
[25:54] it's like you know false precision right like who knows yeah it can be yeah it can be there's some like there's some evals where you
[26:01] want a score when you get when you go very narrowly into certain aspects of things like you know when you try try to
[26:09] have evals for retrieval search and like different components then the scores
[26:14] make sense but for this like as a judge case in the overall sense like no and and why why no explanations though
[26:21] like why why don't you want to explain why I marked so explanations actually usually good um so you do you you know what we teach
[26:29] is you want explanations and then a score but this is like a spreadsheet and so
[26:34] we just want it to be tractable if I try to give an explanation then it would like and you know the model here in the
[26:40] spreadsheet isn't the most powerful one they give you. So, uh it was going all over the place. So,
[26:46] I was just trying to simplify it here. But yeah, explanation can be good. It can help you debug the AI model. And you
[26:52] want to give a structured output. You want like a field. You want to usually output two fields like you want it to
[26:58] output like an explanation and a binary score. And then you can use the explanation to kind of help you debug
[27:05] what went wrong with the LM's thinking. Oh, so you're actually going to do this LM adjusting using the Google sheet
[27:11] model AI model. Yes, I'm gonna stay in the Google sheet because our goal is to demystify
[27:16] everything and to make it very clear like what is actually happening. Okay. By using a spreadsheet all the way down.
[27:23] So, uh, okay. So, we have this element judge prompt and now we can go back to those traces. So, we have like this is
[27:29] the original trace column A. This is just in a JSON format. Um and then we
[27:35] have sort of this LM as a judge. So this is like for one error. So you want them
[27:40] to be scoped usually. So we have this LM as judge just for the handoff error. And we have the formula assess this LM
[27:47] trace according to these rules. Okay. And then it's the LLM-as-judge prompt
[27:52] that I just showed you. That's all it is. And then it's giving us true true or false. Okay. So we have true or false
[27:59] here. And then this is this this column H is the LLM judge
[28:06] handoff uh the like what it said by the binary score true or false is there an error and then this is the human label
[28:14] column G there's an error okay so we have these two labels and we already did column G before that was
[28:20] kind of happened for free because of the axial coding in the in the open coding the process oh so you you have like another AI no
[28:28] the human label is like the notes right so So you have yeah those are like the results of the notes. Um
[28:34] you know like basically I said hey if the axial code is human handoff or transfer issue
[28:39] I just said it's true otherwise it's false. Got it. Got it. Okay. And so you can then see how aligned the
[28:46] LM is to the human. That's the main thing that you want to test. Now one thing you want to stay away from. So a
[28:52] lot of people go to just calculate agreement. intuitively it
[28:57] is makes sense right like let me calculate the agreement between the LM and the human it seems like a it seems
[29:04] like a plausible metric it seems like oh that sounds reasonable okay like agreement sure yeah the problem with agreement is most
[29:12] errors hopefully if your system is not jank most errors are not you know happening
[29:19] kind of at the tail like so this human handoff error is is not happening every single time it's maybe happening 15% of
[29:26] the time or 10% of the time, right? Got it. And so if something is happening 10% of
[29:31] the time, how can you agree with it? So it's like if something if a system is
[29:37] saying something is failing 10% of the time, you can agree with it 90% of the
[29:43] time by just saying it never fails. You'll be in 90% agreement.
[29:50] And 90% agreement seems really good on paper. you go into like a stakeholder meeting like yeah I have a judge you
[29:57] know 90 90% agreement like okay that sounds good no that sounds really bad
[30:02] actually uh potentially you need to like really dig into that so as a product manager
[30:08] if you ever see the word agreement you need to pause and be like hm really
[30:14] let's uh let me dig into this please like and so you need to measure two quantities one is and there's different
[30:22] way there's different uh terms but true positive rate and true negative rate so
[30:29] those are just and there's different words for it sensitivity specificity precision recall there's different words
[30:34] but I'm true positive rate true negative rate and so true positive rate is what is
[30:40] your ability to successfully identify the failures
[30:46] like when the failures actually happen and what's your ability to successfully identify when failures don't happen And
[30:52] that's a better those two quantities are kind of better than agreement because
[30:58] they will show you when something is off like you know and so to make this more concrete because it can be a lot in your
[31:03] head like oh what am I saying right now like why isn't that right and so let's go here to this confusion it's called a confusion matrix
[31:11] it's funny that it's called a confusion matrix sometimes it causes confusion but hopefully today it won't cause confusion
[31:17] what you have here is like okay in this column you have the human label. Okay.
[31:23] True or false? False and true. And then in this going across here, you have the LLM-as-judge label where the green diagonal
[31:31] is where they both agree. Yeah. Okay. Cuz this is like 100 traces. We have 70. So when the human says it's
[31:39] false, the LLM-as-judge agrees with it. Okay. Like out of you know the 73 times,
[31:45] but then when the human says it's false, the LLM-as-judge thinks it's a there is an error 18 times. Interesting.
[31:52] There is a different there's different kinds of errors and this is what I'm talking about here. You don't want to
[31:57] just go in agreement. You want to know what the true positive rate true negative rate is. Now, how do you know what a good true positive true negative
[32:03] rate is? There is no magic bullet there. That's a business decision. Like what
[32:11] what level of judge are you is is like okay for you in in the in the most base
[32:17] case. You just need to do a sanity check. Like does it make sense? Okay. Like you know does it seem okay?
[32:23] Calculate the true positive rate, calculate the true negative rate. Is one of them like really bad? Okay, then
[32:29] maybe you don't want to use that. Um is it really low? Um or you know just look at the confusion matrix do whatever you
[32:35] know and you can use a spreadsheet and say hm is this okay? Like am I okay with this kind of error? Um you know give
[32:42] yourself an intuition. often times you I would say for most people who haven't
[32:48] are not used to true positive rate true negative rate it takes some time for it to click
[32:53] even I have to think about it sometimes honestly even I've been doing this for years just to like ground myself
[32:59] I mean I think the confusion matrix is actually way more clear than the percentages I mean yeah
[33:06] 18 where it's marked as true when it's false yeah right yeah so there's a problem
[33:12] when it's false you like you know where it's false is where there's um you know
[33:17] out of these 91 times you have like 18 of these 91 times it has this specific
[33:22] error is that okay you know so basically so basically 18 times it actually did successfully hand off to the to the human to the human uh sub
[33:30] support but like the LM thinks it did not or like there's too many turns or something yeah yeah the like 18 times it LM thinks
[33:38] there is an error when there's not right is that okay and so like you know different sit situations you might be uh
[33:45] like the the false positives are not as expensive as the false negatives, you
[33:50] know? So like you you might be okay with catching things like catching more errors that
[33:56] don't actually exist. You just want to make sure you do catch all of them. So then what do you do with this 18 like
[34:02] you look back at the traces, see what happened and then you try to modify the prompt. Yeah. Yeah. So what you do is you can look at these like 18
[34:08] um and you can you know you can say okay like what happened here and you can iterate and you keep iterating a bit on
[34:15] the prompt. Yeah. Um and often times it's quite straightforward. Um sometimes not as
[34:21] much but one thing I did leave out here is a lot of times in the LMS judge you
[34:26] want examples. I didn't put examples here because I just wanted to keep it simple. Once you start putting examples
[34:32] in the prompt, you do have to um split the data set a bit. Like you
[34:38] can't just you can start overfitting to your data. So like if I put all of these traces in my
[34:46] prompt, it would get 100%. Because it would know the answer exactly, right? So like you
[34:53] don't want to do that and and so um you want to hold aside some data to make
[34:58] sure you're not cheating yourself and you know so that that's so we don't have to get into all that from a product
[35:05] manager perspective the best thing you can do is like just know just have a trigger in your mind about agreement and
[35:12] just don't just ask some clarifying questions like okay agreement is 90%. What's what is the baseline error rate
[35:19] if they say 10%. Yeah, you know that agreement 90% you're like this this is
[35:24] really bad like something something went wrong here and this is like pretty common right for
[35:29] for teams running evals they they just have a they just have like a agreement store they don't they don't have the TPR thing
[35:34] uh very extremely common is like yeah this is this is a reason I'm making a big deal out of it is uh because we just
[35:42] see it so much that uh it's worth uh calling out. Okay, got it. All right. So now we have
[35:49] some jud judges uh live and um like what what what's the next step? You want to
[35:55] put his judges into production to run all time. So now you have this really uh so let's
[36:01] say you have the judge like this human handoff score judge. That's right. And you like it enough. So now you have
[36:07] this like powerful tool that you can use like number one uh you can you know you can set aside some data. you can uh put
[36:15] it in CI. You can have a test anytime you make a change to code or whatever. You can test what the you know how good
[36:23] you're doing on this human handoff problem. But also you can run your judge in production. You can run it on a
[36:29] sample or a large portion of your production traces and you can see like where this handoff failure is happening
[36:36] and you can debug it even more. You can say I want to find all of the places where handoff failure is happening. I
[36:42] want to find a lot more situations where it's happening. Um and you can put you can do production monitoring of it um of
[36:48] problems. You can see you can use these judges to kind of run on a sample of traffic. You can know like hey are
[36:55] handoff problems happening you know so on and so forth. And you can
[37:00] build this suite of evals over time. Okay. Most of the time people ask me how many
[37:05] evals I have. Usually have under a dozen. I don't really have that many
[37:12] because I'm pretty parsimonious about the evals that I need. It depends like sometimes I have more than that if uh it
[37:18] depends how expensive they are. Um it takes some work to maintain this stuff as well. Um you know for the LLM-as-judge
[37:25] the codebased ones not so much. Uh because you don't have to do all this like you know because I don't have to do
[37:33] too many human this like human label stuff because like in the codebased stuff there's a there is a right and
[37:38] answer. Yeah. Yeah. And that's like that's called a reference based eval. And this
[37:43] is a reference free eval. So depending on what kind of eval it is um it'll you know there's a there's like a total
[37:50] budget sort of roughly in my mind of like okay how many you should have. So let's say you have like uh you know five
[37:56] or six judgy valves in production and and you just like so basically in production just means that like like
[38:02] this um human handoff jud judge like it it just randomly samples like out of 100 conversations it looks like five or
[38:08] something and then it kind of gives a pass fail. Yeah, it depends how many you have. Like
[38:14] it depends how many how what kind of scale you're at. you know, if you're serving like billions of users a day or
[38:20] something, then you probably don't want to run an LLM-as-judge across like everything. Um, you know, it really depends like you can get a lot of data
[38:28] from just sampling. But if you have like very low amount of data, like you're only serving like thousands of users a
[38:35] day, then just run the whole I don't know, just like score the whole Yeah. I mean, it's probably not that
[38:40] expensive. So, it really depends. And then you have a dashboard that has basically like TPR
[38:46] and TNR for each judge or or something. Yeah. And so what you can do is actually
[38:51] like you can bake this into a score. There are ways to like combine these TPR TNR. There's like F1 score and stuff
[38:57] like that that weight them equally or whatever. You can get into this. Usually do a report one score. That's probably
[39:03] beyond the scope of I have to go into a lot of like data science to like talk about how to do that.
[39:08] Yeah. Um but usually there's one score um that report and actually there's like
[39:14] all these evaluators and I try to have like one aggregate score um y
[39:19] that is like aggregated across all of them just to give me a sense and then I can drill in and see okay what's going
[39:25] on and and when do you do like human labels uh like you know because you you did it
[39:31] in the beginning with looking at 100 traces but like when when do you do human labels again? Oh, so always do
[39:37] them all the time. I do it like revisit it. It depends on the dynamics of the system. So depends like anytime there's
[39:44] like big changes, I'll definitely do it again and I'll also do it on a regular cadence. Let's say like once a week,
[39:51] once a month. It depends like how fast the systems are changing and how what the scale of the system is. But I'll do
[39:56] it like on both a cadence and also um and then you get better every time. But
[40:01] also you can build tools that help you do this. So, one of the things that we talk about in our course is okay, we use
[40:08] like Braintrust. We did this here. We did this a spreadsheet or whatever. Um, for nurture boss, what they ended up
[40:15] doing and I took some screenshots and I put it in my blog. So, let me just share that with you.
[40:21] Um, so they actually built their own annotation tool because it's so valuable
[40:26] of a process. Probably the most valuable process of eval is this like is annotation
[40:31] is the annotation and counting. Even if that's all you do, you don't build any judge, you don't do any eval what like
[40:38] you don't do whatever, you can get insane value by just doing that. And that's the one part that everyone skips.
[40:44] They try to like go directly to like whatever. Yeah. Um and so uh you know this is a
[40:52] screenshot of what they like the tool they built for themselves and they built this in less than four hours. Um because
[40:58] this is type of thing that AI is really good at. Yeah. helping you build. So it's like
[41:04] okay, you know, you can see this is a trace viewer. You have these selectors for different channels. You have um this
[41:10] is their interface. The system prompt is hidden by default. They could just create add notes here and then they had
[41:17] they baked it in into their tool where they just did the axial coding for them. You see like it just tried to do it for
[41:23] them and it gave them a count. Got it. They loved it. There's a video in this blog post here. This is Jacob and he's
[41:31] like super happy. Uh yeah, he looks happy now. Yeah, he talks about how like he did this and
[41:38] how like the the impact that it had on on his uh on nurture boss. So,
[41:44] okay. Um yeah, like you can get really fast. So, like you know with these like your own
[41:49] tools it gets ridiculously fast and it's not painful at all. Um, yeah. But basically, yeah,
[41:57] I mean, but basically, you should still like basically manually like before I make a major update to a prompt or something like I should still manually
[42:02] look at the, you know, like the traces and like just make sure like uh everything makes sense, right, before I
[42:07] ship ship anything. Yeah. I mean, you don't have to do it on every single prompt update. You don't have to look at man, you don't have to
[42:13] manually look at traces. You can just you can run your evals that you have um and do that way. Just make sure you're
[42:20] looking at your traces every so often. Yeah. because it's like it might be mysterious like oh like how
[42:26] often and how many traces. So we tell people look at 100 traces minimum.
[42:32] And the reason we say that that is not a magic number. We always find that if we don't give a number, people don't start.
[42:39] And then when we give a number, when people get in to like let's say 20 or 30 traces, they they they keep going uh
[42:47] until they So we tell people like the term is called theoretical saturation
[42:52] and that just means you keep doing the activity until you it's like a dimension
[42:57] returns. Yeah. When Yeah. until you aren't learning anything new. Got it. So we find that people once they
[43:03] start this they kind of get addicted to it and they find it so valuable that they just do it. So just keep in mind
[43:09] like 100 traces as a goal. Okay this is actually a great convers maybe I have to take down the video of
[43:14] Aman because but this is actually a great conversation because um so first of all so TRDR is that the the trace
[43:21] looking at the actual conversations of whatever AI product you have is the most valuable thing and kind of like counting
[43:27] on labling that right. Yes. and like okay so let let let's just
[43:32] wrap up by dispelling some myths okay so so I'm gonna put some I'm gonna put a statement out there and maybe you can
[43:38] tell me why it's is right or wrong okay so uh one thing that I that I thought
[43:44] was right was like you know you know you want to do a eval for a new product and then you get your team together and you be like oh you know like like should we
[43:51] do helpfulness or should we do toxicity or should we do like what should we do like and what what is the right criteria
[43:56] like what what is good toxicity and bad toxicity but that doesn't seem to Right. Based on what we just talked about.
[44:02] Yeah, that's right. So, a lot of people go straight to helpfulness toxicity score.
[44:07] Yeah, it's a very appealing idea. A lot of vendors, they sell that. They're like, "Hey, don't worry about evals. You just
[44:13] plug and play this tool. We got you. You don't have to worry about it. Just like push this button and then we'll give you
[44:20] a dashboard. Don't worry." The fundamental problem is generic prompts in those generic things usually don't
[44:27] match to the most important problems that are actually occurring in your application. They're just like super
[44:33] generic and they lead you astray and they actually waste your time because you
[44:39] spend a lot of mental energy looking at those metrics and looking at the dashboards and talking about the dashboards and having meaning about the
[44:45] dashboard and all of that could have been directed towards real problems that
[44:50] are actually happening. Now there is a right way to use generic metrics. There's like an advanced Jedi trick that
[44:59] you can do once you have learned error analysis. It will make sense. And what you can do
[45:06] is you can take your hallucination score. You can score this generic hallucination score on all your traces
[45:13] and you can sort the traces by the hallucination score. Okay? And you can see you can do error
[45:19] analysis and see does the top hallucination score like okay you can start doing like smart sampling with
[45:26] these different generic scores. You can use the generic these like all these generic scores as like sampling mechanism to see like is there anything
[45:33] interesting there. And what you'll find is sometimes there is interesting stuff. Sometimes it's not quite like
[45:39] hallucination but something else. And you can kind of see if any of these scores are helpful, but you shouldn't
[45:45] just report the scores. Should never report the scores as is. Probably shouldn't use the scores, but you can
[45:50] use them as meta tools. Got it. Okay. But but like it's way more important to identify as problems wrong with your product.
[45:56] Yes. Okay. Then another thing is like uh and maybe this is more a question like how
[46:02] much of the stuff that we just walked through should we do before we even launch the product? you know, like like should we try to have like a bunch of
[46:08] judges set up and like, you know, do a bunch of synthetic stuff like how how much because what once you launch you
[46:14] actually get real signal, right? I mean, yeah. How much of the stuff should we do? Yeah, I wouldn't get carried away with
[46:21] eval especially in the beginning. I would I would definitely look at lots of data. Um, and looking at data includes
[46:29] using it yourself. Okay. I mean if that like it says like if if you're building a tool for yourself like you are n equals one user.
[46:37] So you don't need to like just use it yourself and you know the air you're doing error analysis like just by being
[46:43] alive and using your tool like if you're actually using it that's fine. You don't need to do all this stuff. It's like
[46:48] when it kind of gets beyond the scale of your comprehension when it starts to you
[46:54] know there's like lots of users or lots of things going on different use cases. Yeah. Then you might think about okay
[47:00] that then you can see like where that data might be helpful or maybe you know you can roll out to like 5% of users and you know like maybe
[47:07] they get a shitty experience but then you can start getting real data to improve. Yeah then nothing beats real data.
[47:13] Got it. And like the the liker stuff is just is it just completely you sis or or like do you are you dogmatic about it
[47:19] the one to five stuff should you stay away from it? I would say I haven't seen you have to be extremely disciplined to
[47:27] use it correctly. Okay. Um you have to have very clear rubrics.
[47:33] You have to make sure everyone is calibrated on that rubric. Um and it usually doesn't go well and for most
[47:40] companies it adds tons of complexity. I would say it's exponential complexity on
[47:45] like relative to binary scores. And so I just haven't seen it done in most cases
[47:51] correctly. There's there's some rare exceptions where it does is okay, but
[47:56] it's usually like, you know, and I press teams to say, hey, like can we just make
[48:02] this a binary score? Like is there a point where this is like good enough versus not good enough? We're able to do
[48:09] it. But dude, then where does this stuff come from? Like why do teams keep doing this stuff? Yeah, because it it's a kind of an
[48:15] appealing idea, right? to like we've all been graded on like we have a grading system from school A through F like you
[48:22] know it's not nothing is black or white like we want to like have this like high fidelity sort of assessment but the
[48:31] problem is like what what would what do you even do with this highfidelity assessment like yeah it just makes you feel like false
[48:37] precision right it's like you know I got a three versus a four like what does that even mean like yeah like humans can't even tell a difference between a
[48:42] three and a four yeah yeah yeah most most people can't and it gets just gets lost in the sauce
[48:47] and already, you know, it's just like it's already complicated enough. You need to really reduce complexity in this
[48:54] whole thing and be pragmatic about it. All right, dude. This is this is super awesome conversation. So, so I guess let's go back to the Twitter debate. Do
[48:59] evals matter? It does matter if you do the problem properly, if you're actually solving real problems. Yeah, that's a really good question. Do
[49:05] evals matter? Yeah, I would say so eval don't exist in a silo. If you just try to do if you try to eval and get carried
[49:13] away with evals, it will probably hurt you. What you want to do is definitely ground yourself in the data analysis, in
[49:20] the looking at the data part. And like, you know, everyone says look at your data, but I I think um it's hard
[49:27] to know what that means. What we went through today actually shows you what it means and hopefully demystify what what
[49:34] it is to look at data. But it should be it's like a very tightly coupled with
[49:39] evals and I I say that it is eval like this data this looking at data counting
[49:45] I just say you you because you can't do evals without it. Yeah. It's not like the super sexy part of it but yeah it's the most important
[49:51] part of it. Yes. Yeah. Got it. Makes sense. All right dude. All right man. I I I think you
[49:56] convinced me to take your core course now. So uh can you talk about your course and um when you teach it and if
[50:02] you have a discount for folks? We are teaching a course on evals where we walk you through the end-to-end detailed
[50:08] process on how to do evals correctly. We go into subjects like okay how do you
[50:14] evaluate your rag systems? How do you evaluate retrieval? How do you evaluate agents? Um how do you deal with all
[50:21] kinds of edge cases that you might encounter? How do you do this effectively? Like how do you actually
[50:26] read a trace in you know save yourself from kind of all the complexities that
[50:32] might happen? and how do you get through this effort? And we've been we've taught over 2,000 students including lots of
[50:39] people from Google, open AAI, things like that. Um, you know, the big labs
[50:44] are really interested in this because, you know, they focused on foundation model benchmarks, but we're talking
[50:50] about application specific evals like if you're building an application, what is that? And that eval is very different.
[50:56] Yeah. Yeah. And so, uh, I teach the course of Shrea Shankar. Sha Shankar has been writing
[51:02] about eval as well for years now and been doing a lot of research in the space. So we both have a machine
[51:09] learning and data science background as well as software engineering background. You know in the course is four weeks
[51:15] long. We give students lots of resources. So we have over nine hours of
[51:21] office hours. Yeah. Uh we give students a uh AI evals
[51:26] assistant. So it's like everything that we've ever said about evals publicly in the course, blog posts, talks, papers,
[51:34] you name it. Uh we've put that in an AI and we give that to you as a like an
[51:40] assistant as well. So you know it's a it's a modern course and you got to have evals on top of that too, you know.
[51:46] Yeah. And we're doing evals. Yeah, we are doing evals on top of that. This is the first time this is the first cohort we're doing it for. Uh so this next one
[51:52] coming up in October. And so we also give people a 160 page book on evals
[51:57] that you can take with them. So there's a lot of resources there is a it's a good community and we're offering
[52:03] Peter's community 35% off. Awesome dude. So please see the link in the in the description.
[52:09] Awesome. Yeah, dude. I I personally learn a lot from this. I need to reevaluate how I do evals. So So yeah, I
[52:15] I hope to see uh folks there. Definitely want to take the course in October. Thanks so much Hamel and sharing your
[52:21] knowledge and um keep dropping non knowledge box man like on social media.
[52:26] Yeah, thank you so much. Thanks for having me.
[0:00] this looking at data accounting. You can get insane value by just doing that. And that's the one part that everyone skips.
[0:07] I'm going to use a spreadsheet to drive home the fact that this process can be dead simple and you can get immense
[0:13] value out of it. When you see an average score of 3.2 versus 3.7, no one really
[0:18] knows what the hell that means. It's not really actionable, honestly. They're like, "Oh, it's like getting better."
[0:23] Honestly, like nobody really knows whether it's getting better or not. So, as a product manager, if you ever see the word agreement, you need to pause
[0:30] and be like, hm, let me dig into this, please. If people don't trust your evals, they won't even trust you. You're
[0:37] done. Okay, welcome everyone. My guest today is uh Hamel. Hamel has trained over
[0:43] 2,000 PMs and engineers from companies like OpenAI, Anthropic, and Google on how to run AI evaluations. He teaches
[0:50] the most popular course on this topic at Maven. So really excited to dig into
[0:55] these best practices and I feel like I made a lot of mistakes that you know and have a lot of assumptions that Hamel can
[1:01] help. So welcome. Really happy to be here. Excited to talk about evals.
[1:07] All right. So you know there's been a lot of like online debate about like you know are evaluable or not like blah blah
[1:12] blah on Twitter and and um let's just make this really practical. Um like let
[1:18] us talk about evals for like a real product like like do you have a do you have a product example that you want to talk about throughout? I do. Yes. So
[1:25] there's a company that I've been working with. Let me share my screen. Sure. So just to set the stage, Nurture Boss
[1:32] is a AI powered property management assistant. And so it's a really
[1:37] interesting use case because it's actually one of the best teaching examples and I love using it because
[1:43] it's messy and there's enough complexity to where it's realistic. And so the
[1:49] question comes like oh okay like how do you do evals? So like lot a lot of times when we talk about evals you know
[1:55] we can show toy examples but sometimes those are oversimplified and it's hard for people to generalize that like how
[2:01] is how am I going to do that for my app? my app is complex, you know, I have other things going on. Well, that's what
[2:07] we're going to show today is actually we're going to look at Nurture Boss's data together and we're going to do like
[2:13] a minimal set of evals and we're going to do that very quickly. Yeah, that'll be awesome. So, I know on your podcast
[2:18] you had Aman on already. He may have talked about Arize. There's a lot of different solutions out there. The ones
[2:24] that I come across the most in practice are Arize, Braintrust, LangSmith. Those
[2:29] are like kind of three popular ones. Mhm. One of the observability platforms that nurture boss used in the beginning was
[2:36] Braintrust. They actually like created their own but for but I'm going to show you their data in Braintrust cuz that's
[2:42] where we have it anonymized. Traces is basically like the chat conversations right with nerbos.
[2:48] Okay. I'll show you what a trace is. The best way is just to look at it rather than me trying to define it. So I'm just going to open one. So trace is a log of
[2:57] all of the history of a particular interaction that your user might be
[3:02] having with an AI including all of the internal things that might be going on that the user doesn't see. Okay. So this
[3:08] is example of a trace. And so what we see here is we have the system message.
[3:15] So you are an AI assistant working work as a leasing team member at the arrow and you have different instructions on
[3:22] how to interact with the res the resident or the prospective resident.
[3:27] You know for example how to deal with maintenance requests or um you know what
[3:34] to do with prospective residents and tour scheduling and all kinds of things like applications.
[3:39] Yep. And you know you can there's a lot of instructions here. We don't need to read all of them. We can scroll down
[3:46] and we see here where is the building located is one of the questions the user
[3:52] is asking. Mhm. And so there's a tool call made. Get communities information. We can expand
[3:58] it and it's pulling back some information. It's making a tool call. The tool call returns with some
[4:03] information which we can see here. Um and then the assistant is is giving an
[4:08] answer. you know this the arrow is located at this address and then it's
[4:14] the user is saying I'm interested in a two-bedroom what's available and actually then it stops
[4:20] um it just dead ends and um there there is a failure of some kind it just wasn't
[4:27] surfaced to the user so this is not like necessarily the most interesting error um
[4:33] this is just like you know something that you would see in the real world now this is example of a trace so So when
[4:39] Jacob came to me, I said, "Okay, Jacob, this is what we're going to do. We're going to look at traces." And he's like,
[4:45] he's like, "What do you mean we're going to look at traces? This seems like we're going in the wrong direction." Like, "This is going to take forever, Hamel.
[4:51] Like, this must be like what what are you like, what are you doing?" He said, "Just trust me. We're going to look at
[4:58] about 100 traces and just we're just going to write notes about what is going wrong. The first one may be painful, but
[5:03] we're going to get really good at it. By the time we get to the 10th one, we're going to be really fast." So, we got to this one. We're like, "Oh, like
[5:09] something happened here." Um, the conversation got cut off. Um, it failed. We had to do some investigation to
[5:16] figure out like what's happened. But we just wrote a note. And so, in this case, um, we can make an annotation. So, I
[5:23] would write a note saying like, hey, there was an error
[5:30] that was not surfaced to the user. Okay? Just write a note. um
[5:38] you know, end the conversation deadended. The point is not to do a full root cause analysis. Just observe what's
[5:45] wrong. Okay? And that's all you got to do is do this. Do it like 100 times.
[5:50] Yeah. Do this 100 times. Now, Jacob's like, "What the hell are we doing? Why are we doing this?" Like, I hired you,
[5:56] Hamel, for evals, and you are like a monkey looking at this data, and like I don't understand what is going on. Like,
[6:02] what is the purpose of this Hamel? this is a very expensive consulting engagement and we are looking at data. I
[6:08] said no trust me we are going to this is going to lead somewhere.
[6:13] Well I mean you're basically human labeling this data right? You're basically saying I'm basically human labeling this data. So let's look at a couple of more like
[6:21] um I think it will become clear why this is valuable really fast. Okay. So this is another trace. You are leasing team
[6:27] member at the Meadow Brick Gardens and your name is Taylor. So giving it a name. uh your goals are to answer
[6:33] questions. Okay, so it's really the same thing. You have, you know, uh you're fielding calls from from residents um
[6:41] actually prospective residents because this looks like it's like a salesfunnel type of mode where you're like
[6:47] encouraging customers to schedule tours. Um so let's go to the first user
[6:52] message. So we got the system message out of the way. The assistant says this call, so this is over voice now. Okay, this call may be
[6:59] recorded blah blah blah. And the the only thing the user says is preview program. I have no idea what that is.
[7:06] Maybe it's something in the system prompt, but I personally don't recall necessarily what that is. The assistant
[7:12] says, "It looks like you might be interested in learning more about community and possibly scheduling a tour. Would you like to schedule a
[7:18] tour?" User says, "No." The assistant says, "Seems like you might have a specific question or need assistance
[7:23] with something related to the our apartment. How can I assist you? Can I tell to a representative?" Obviously,
[7:30] they're trying to talk to a person. Uh, sure. I can connect you to representative. Um, would you like me to
[7:35] do that now? Yes, great. I'll connect you to representative. One moment. Would you like me to connect you? I'm already
[7:42] frustrated. Like, yeah, it's the person to a human being already like so many questions like, "Are you sure? Are you
[7:48] sure? Blah blah." Uh, so okay, like ADU, he wants to talk about ADU. It sounds like you might be interested. Yes. Could
[7:55] you clarify your query? I just want to talk. We've all had this experience at one point in other in our lives.
[8:01] Yeah. Every time, man, I call. Yeah. Yeah. This is not, you know, I want to
[8:06] throw my phone out the window whenever I have this interaction with an AI. Um, so, okay, I understand. I'll connect
[8:13] you. And finally, a tool call is made. We're transferring the call. Okay. So, we feel the pain of the user. We we do
[8:20] honestly. Um, and it's pretty clear like, hey, we So, this this is an this
[8:25] is a clear error in this case. I'll write the the note here just like it to the other one. And you're not trying to like write
[8:31] solutions. You're just trying to write like the note of the problem. Yeah. I'm not trying to debug it. I'm not trying to say like why it happened.
[8:37] I'm not trying to root cause a solution. I'm just journaling why it happens. So you do this. It took us frankly it took
[8:44] us like an hour to do 100 traces. Didn't take us long at all. Okay. But by the end of it, we knew a
[8:51] lot. Like we learned a lot and we learned way more than you could possibly
[8:58] learn by trying to throw any kind of automated solution at this problem. So
[9:03] if you tried to come at nurture boss and put a hallucination score, toxicity score, coherence score, whatever you
[9:10] want to call it, it would not have given us anywhere close to this insight that we had right now. You know, we
[9:16] identified very specific failures and things that are painful, right? By looking at the data we immediately could
[9:23] like see that did you uh use some AI to like summarize the trace data that you labeled or
[9:29] Aha very good question. So while you shouldn't use AI to like do the you
[9:35] should definitely look at the data put your hands on the data you can use AI to help you do the analysis of it. So what
[9:43] happens is I exported all of these logs plus the notes into a spreadsheet. Okay.
[9:50] Okay. Um, and you don't have to use a spreadsheet. I'm going to use a spreadsheet to make it to drive home the fact that this process can be dead
[9:57] simple and you can get immense value out of it. So what I did is I exported like
[10:03] all the notes. So in this column, column A, you have all the notes that I took.
[10:08] Yeah. Okay. So like you know, one note is user was probably asking about lease terms or maybe deposit not about specials. And
[10:16] the AI was talking about specials or another one was the AI offered virtual tours but there is no virtual tour.
[10:24] Um, okay. You know, so all these different and there's the disperate messaging one that we just saw. Okay. And so all these
[10:30] different notes that it took. So what you can do is you can take these
[10:35] notes and you can do something really stupid simple is you can dump them into
[10:42] like claude or chat GPT or whatever and I say okay please analyze the following CSV file. There's a metadata field which
[10:49] is nested field called z_note that contains open codes. So this is like some terminology here. Open codes is
[10:55] just a fancy word for those comments that I made. Okay, just the notes for analysis of LLM logs that we are
[11:03] conducting. Please extract all of the different open codes from the z_note field. Propose five to six categories
[11:08] that can we can create axial codes from. So the axial code is another piece of terminology that means we just want to
[11:13] group them into C. We want to group these notes. We want to just classify them. Okay, this like open code axial code
[11:20] thing is actually some really old technique from social sciences and it's been also used in machine learning for
[11:26] decades. And so that's why we're using this terminology as a shortcut to give to the LLM because the LM knows exactly
[11:34] what this means. They're like, "Oh, I know exactly what you're doing. You're trying to do this technique."
[11:39] Got it. Okay. So, it's better than just saying it's better than just saying like categorizes stuff. It's just some shortcut technique. Yeah.
[11:45] Yeah. It know it has like it it gives it some specificity. it like kind of by saying open code axial code it knows
[11:50] like what my goal is because there's a lot of context when I use that terminology in this technique you could
[11:57] also say categorize though I mean there's no you can start wherever you want so if you want to say categorize start with categorize totally fine it's
[12:04] you know the point is make progress and get value as fast as you can I don't
[12:09] want to be too prescriptive but the point is like you can sort of uh so like
[12:14] okay it kind of iterated a lot on how to open the CSV so We can skip that. But it gave me it gave me like um you know some
[12:22] categories and I didn't really like I didn't necessarily like all of them and I could have been you know I kind of
[12:28] went back and forth a little bit to refine the categories that made sense to me. Um and I just like took I wrote down
[12:35] some categories actually. Um and here are some categories here. So I said like okay tour scheduling rescheduling issue,
[12:44] human handoff or transfer issue, formatting error with the output. They had some formatting errors um like
[12:50] putting markdown inside text messages for example. Um conversational flow
[12:56] issues. So that's like the text thing where just abrupt you know the flow. um
[13:02] making up promises not kept like rescheduling and things like that or not rescheduling but other kinds of promises
[13:09] um and then there's another I usually have another field called none of the above but I didn't do that here just out
[13:15] of simplicity okay and so what you can do is then you can kind of go back and forth and what I did
[13:20] is like in the spreadsheet you know you can use AI so there's AI in this Google spreadsheet the Google Google sheets
[13:26] have AI um you can have the AI formula that's very handy to to show you something. So I say, "Okay, categorize
[13:33] the following note into one of the categories." So you're just like c using LM to like categorize it.
[13:39] And you can see I'm just categorizing these notes that I took like the problems that I found. I'm just putting
[13:44] it into categories. Well, I did know that Google Sheets has this AI feature already. Okay. They're usually very slow.
[13:49] It's cool. It's cool. It's can be slightly janky, but it's okay. It's lightweight and you don't have to use any tools and everyone can understand
[13:56] how to do this. is like demystifies the whole process of what I'm doing cuz if I like open some code you might think oh
[14:02] like you need to be like software engineer to do this or something and like no you don't uh we can use English all the way. So now you have categorized
[14:10] all of these things and now we can use one of my favorite tools pivot tables.
[14:15] So pivot tables um you know if you haven't seen them before really handy in spreadsheets so
[14:22] you can just count how many times each of these categories occurred. Okay. And and we can see the just at a high
[14:29] level um hey oh okay we're having like this conversational flow issue is happening quite a bit. Um you know we
[14:36] also have this like human handoff uh transfer issue and you can kind of get a
[14:41] sense like right away uh what the problem is. Now it is likely that before you even get to this count
[14:47] you already know you've looked at 100 traces. you know in your gut you're like okay you know what I'm going to I need
[14:53] to fix this like human transfer thing like right now you're like I don't even need to like do
[14:58] a data analysis but it's like quick this takes like like less than a few minutes
[15:04] honestly and it just gives you some grounding and it's like lets you see you go from this
[15:09] like mess of like I don't know what's going on to okay like I have some idea about the problems that I have
[15:17] and you have some starting point. Does that make sense? Yeah. Yeah. This is brilliant, dude. But
[15:23] but let me ask you this question. Yeah. So, um in this case, the agent was already live in production before you
[15:29] started doing all all this stuff, right? Like like um but that's not the ideal approach, right? Like I ideally you want
[15:35] to do some of this before or maybe dog food with your team first or like get some users try it.
[15:40] Absolutely. How do you Yeah. So the best case scenario is you dog food it with like
[15:47] you know some friendly customers, you dog food it yourself. That's going to be really good. You can also synthetically
[15:53] generate inputs into your system. So basically what you can do is like think about plausible user questions
[16:01] they may have and you know and try to come up with some hypothesis of where your system will break.
[16:07] Yeah. But there's a certain way to do that. You don't want to just ask an LLM, hey,
[16:12] come up with plausible questions for a prospective tenant that might be looking to rent an apartment. The right way to
[16:19] do it is to come up with some categories. So, is to come up with some dimensions. And what I mean by that is
[16:26] let's say um let's let's think about what good dimensions might be for nurture boss. So
[16:33] for nurture boss uh you might have like resident uh you can have okay like type
[16:40] of customer maybe apartment class maybe so like luxury standard
[16:47] something else I don't know what that is I'm not that creative to like think about on the fly but what was the thing
[16:53] you suggested just type of customer right you can you can get the tenant manager versus the actual resident right depending on who
[16:59] you're talking to yeah uh resident uh manager.
[17:05] Yeah. And you can think of put your product hat on. So like by the way this whole
[17:11] process is is very product oriented like so you know when you read the trace it's
[17:18] not so much about engineering it's putting your product kind of hat on and saying is this the experience that you
[17:24] want your user to have? Does this actually make sense? when it comes to like these dimensions I'm talking about,
[17:30] you're kind of putting your product hat on and saying, "Okay, what are the different personas? What are different categories, different dimensions that
[17:36] you may want to consider?" And then what you want to do is like you know you would take um the kind of combination of
[17:42] these um you know so like luxury resident luxury luxury for resident
[17:47] luxury for manager standard for president standard for manager and you would feed those we call it dimensions
[17:54] into an LLM say okay these are the different dimensions for this for every one of these dimensions generate
[17:59] plausible user queries got it that's like way better than just asking an LLM. Yeah, just because um if
[18:08] if you just ask an LLM, it'll be more a lot more homogeneous and you don't want to be homo you don't want to have
[18:14] homogeneous inputs. You want to explore the space of inputs and so these
[18:19] brainstorming dimensions helps you to kind of make sure you're you're exploring the space being thoughtful
[18:26] about exploring the space. Does that make sense? Got it. Yeah. You want to find all the edge cases and like you know Yeah. Got it.
[18:32] And that's just scratching the surface of this. There's a lot more to generating synthetic data that we could probably get into here, but there
[18:38] there's like more advanced ways to generate synthetic data or things to think about in terms of being more adversarial, how to, you know, come up
[18:45] with hypotheses to help you break your system, so on and so forth. But the short answer is use our system and you
[18:51] can use LMS to help you help basically pretend as synthetic users.
[18:57] That makes sense. Okay, let's go back to the categories you have on the left. So uh so now you have these I mean they're
[19:03] not they're basically pro problems right problems with the product and uh now what are we going to do with with this
[19:09] stuff is this is how we come up with our criteria or should we just start fixing the issues or very good question next very good
[19:15] question so um when we first did this what the top
[19:21] issue was date handling it's like and it was very clear uh you know the the user
[19:27] wanted to schedule an appointment Yeah. And it was always getting the date wrong. And it was very clear like,
[19:36] "Oh, this is so dumb." Like the LM doesn't know what today's date is. We just
[19:41] Okay. We just like forgot. They like, "Yeah, they like forgot to put that in the prompt." It's like, "Do you really need
[19:47] an eval for that?" Maybe not. Like, you know, you don't want to eval. You don't like necessarily
[19:54] want to do eval cuz like it feels good. the whole purpose of anything is to make your product better and to and to
[20:00] iterate and you know move fast. Um and so for that one we're like well let's
[20:06] see like let's just give it what today's date is and that problem basically went
[20:11] away unsurprisingly. So we didn't really need an eval from that. Um other things
[20:17] that more subjective or you know so there's a it's a costbenefit tradeoff.
[20:22] So there's two kinds of evals. One is LM as a judge which we are going to build together. Another one is codebased eval
[20:29] where you don't really need an LM as a judge. It's some kind of assertion that you can make and that's very cheap
[20:36] compared to LM as a judge. And so uh for the date one we actually did we did the
[20:42] like a codebased eval which is like we had some test cases and we're able to test like does the date that's coming
[20:48] out equal to the expected date. And that was like very cheap. We didn't have to do LM as a judge. Got it. You know, but
[20:55] that was like really easy to fix. Now something like, hey, you should be handing off to a human
[21:01] like, okay, that one like we don't know exactly like we did have rules for that
[21:06] already, but the LM is struggling and like we don't really know how we're going to do it. That seems like a really
[21:13] good use case for an LLM-as-judge. And also the the eval is going to provide tons of
[21:18] value even though it's expensive more expensive because we're gonna iterate against it a lot to make progress
[21:26] and so we said okay like let's you know okay we need an LLM judge for the human
[21:32] handoff let's go ahead and do it it's an important problem also. Yeah. Yeah. The main problem that people
[21:39] encounter when doing LLM as a judge is they just prompt another LLM to kind of
[21:46] judge what your LM did and they say is it good? Now that should that should be
[21:51] suspicious, right? Like why is that okay? Like why you just going to tell another LM to tell me if it's okay? Like
[21:58] I don't know. And you would be right to be very suspicious of that. And there is
[22:03] an answer to that. And the answer is you can measure the judge. So it's like an it's a meta evaluation problem is like
[22:10] you need to measure if the judge is good. It's very important. You don't want to skip that step because if you
[22:16] have a bunch of judges LM judges floating around and your stakeholders
[22:21] are like you're reporting them on the dashboard your stakeholders looking at them and everyone's like oh the judge
[22:27] you know this no one's going to understand what you're using LLM-as-judge anyways. They're just going to look at your metric and and when there becomes a
[22:34] significant there's enough gap between reality and your metrics, no one's going to trust you anymore. You want to avoid
[22:40] that. You want Y cuz like if people don't trust your evals, they won't even trust you.
[22:46] You're done. Yeah. Exactly. Yeah. You can't you can't make it have like perfect scores for something, but it's actually totally
[22:51] wrong, right? The way you manage it. Yeah. Yeah. And so Okay. So, how do you go about this? Well, thankfully when you're doing
[22:58] this axial coding stuff, right, you actually I've identified really good test cases or some reasonable text uh
[23:05] test cases that you can use that are labeled. You you already labeled them as a human. So, you have some ground truth.
[23:12] And these are things that you can use to calibrate an LLM judge to see if you can
[23:18] create a judge that's good enough. Okay, green enough is just like green up is like how closely does it match to human
[23:24] labels, right? That's kind of what how close does the match to human label? Yeah. So that's what we're going to do next
[23:30] is we are going to think about first we're going to write the prompt and this is like the dumbest prompt. I'm not
[23:37] saying like this is a good prompt. This is just a prompt. And the point is not to like have a
[23:44] prompt recipe or some like magic thing is just to iterate. Okay. And you want to just specify kind of the requirements
[23:51] of like in this case what is a good handoff or when should you be doing a handoff and when should it happen and so
[23:57] you know you are scoring a leasing assistant uh to determine if there was a handoff failure there should be handoff
[24:05] if any of the these things occur um you know or sorry there there is a
[24:11] handoff failure if any of these things occur like if a human requested to be handed off, but you just ignored them or
[24:19] looped through it too many times. That's a failure. Got it? Yeah. And there's a list of these seven failures. You don't have to read all of
[24:25] them, but you get the idea. And we also say when there's not a failure, just out of completeness. And we say we want to
[24:31] return exactly true or false, binary. So, it's worth lingering on this for a
[24:39] moment. So, it's very important for an LLM judge that you output a binary
[24:44] score. 99% of the time you don't want to import uh export like a like art scale
[24:50] or a you know a score of one to five um or some kind of score because that
[24:57] introduces tremendous complexity. Yeah. You know LM's are not good at continuous
[25:04] scores number one. Number two is the output is not going to be clear. When
[25:09] you see an average score of 3.2 two versus 3.7. No one really knows what the
[25:15] hell that means. 3.7. Yeah. Yeah. No one. And it's not really actionable, honestly. They're like, "Oh, it's like
[25:21] getting better." Honestly, like nobody really knows whether it's getting better or not. I found that when you try to
[25:28] hide behind a score, you're not really making a decision. And like what you're trying to the frame here is is this
[25:36] feature good enough to ship? Yes or no? Make a decision. You know what? What is the line? there
[25:41] is a line somewhere and so like there has to be right and so we don't want to score um wherever possible you want to
[25:49] simplify it the score just makes it too complex yeah it's like uh fake science you know
[25:54] it's like you know false precision right like who knows yeah it can be yeah it can be there's some like there's some evals where you
[26:01] want a score when you get when you go very narrowly into certain aspects of things like you know when you try try to
[26:09] have evals for retrieval search and like different components then the scores
[26:14] make sense but for this like as a judge case in the overall sense like no and and why why no explanations though
[26:21] like why why don't you want to explain why I marked so explanations actually usually good um so you do you you know what we teach
[26:29] is you want explanations and then a score but this is like a spreadsheet and so
[26:34] we just want it to be tractable if I try to give an explanation then it would like and you know the model here in the
[26:40] spreadsheet isn't the most powerful one they give you. So, uh it was going all over the place. So,
[26:46] I was just trying to simplify it here. But yeah, explanation can be good. It can help you debug the AI model. And you
[26:52] want to give a structured output. You want like a field. You want to usually output two fields like you want it to
[26:58] output like an explanation and a binary score. And then you can use the explanation to kind of help you debug
[27:05] what went wrong with the LM's thinking. Oh, so you're actually going to do this LM adjusting using the Google sheet
[27:11] model AI model. Yes, I'm gonna stay in the Google sheet because our goal is to demystify
[27:16] everything and to make it very clear like what is actually happening. Okay. By using a spreadsheet all the way down.
[27:23] So, uh, okay. So, we have this element judge prompt and now we can go back to those traces. So, we have like this is
[27:29] the original trace column A. This is just in a JSON format. Um and then we
[27:35] have sort of this LM as a judge. So this is like for one error. So you want them
[27:40] to be scoped usually. So we have this LM as judge just for the handoff error. And we have the formula assess this LM
[27:47] trace according to these rules. Okay. And then it's the LLM-as-judge prompt
[27:52] that I just showed you. That's all it is. And then it's giving us true true or false. Okay. So we have true or false
[27:59] here. And then this is this this column H is the LLM judge
[28:06] handoff uh the like what it said by the binary score true or false is there an error and then this is the human label
[28:14] column G there's an error okay so we have these two labels and we already did column G before that was
[28:20] kind of happened for free because of the axial coding in the in the open coding the process oh so you you have like another AI no
[28:28] the human label is like the notes right so So you have yeah those are like the results of the notes. Um
[28:34] you know like basically I said hey if the axial code is human handoff or transfer issue
[28:39] I just said it's true otherwise it's false. Got it. Got it. Okay. And so you can then see how aligned the
[28:46] LM is to the human. That's the main thing that you want to test. Now one thing you want to stay away from. So a
[28:52] lot of people go to just calculate agreement. intuitively it
[28:57] is makes sense right like let me calculate the agreement between the LM and the human it seems like a it seems
[29:04] like a plausible metric it seems like oh that sounds reasonable okay like agreement sure yeah the problem with agreement is most
[29:12] errors hopefully if your system is not jank most errors are not you know happening
[29:19] kind of at the tail like so this human handoff error is is not happening every single time it's maybe happening 15% of
[29:26] the time or 10% of the time, right? Got it. And so if something is happening 10% of
[29:31] the time, how can you agree with it? So it's like if something if a system is
[29:37] saying something is failing 10% of the time, you can agree with it 90% of the
[29:43] time by just saying it never fails. You'll be in 90% agreement.
[29:50] And 90% agreement seems really good on paper. you go into like a stakeholder meeting like yeah I have a judge you
[29:57] know 90 90% agreement like okay that sounds good no that sounds really bad
[30:02] actually uh potentially you need to like really dig into that so as a product manager
[30:08] if you ever see the word agreement you need to pause and be like hm really
[30:14] let's uh let me dig into this please like and so you need to measure two quantities one is and there's different
[30:22] way there's different uh terms but true positive rate and true negative rate so
[30:29] those are just and there's different words for it sensitivity specificity precision recall there's different words
[30:34] but I'm true positive rate true negative rate and so true positive rate is what is
[30:40] your ability to successfully identify the failures
[30:46] like when the failures actually happen and what's your ability to successfully identify when failures don't happen And
[30:52] that's a better those two quantities are kind of better than agreement because
[30:58] they will show you when something is off like you know and so to make this more concrete because it can be a lot in your
[31:03] head like oh what am I saying right now like why isn't that right and so let's go here to this confusion it's called a confusion matrix
[31:11] it's funny that it's called a confusion matrix sometimes it causes confusion but hopefully today it won't cause confusion
[31:17] what you have here is like okay in this column you have the human label. Okay.
[31:23] True or false? False and true. And then in this going across here, you have the LLM-as-judge label where the green diagonal
[31:31] is where they both agree. Yeah. Okay. Cuz this is like 100 traces. We have 70. So when the human says it's
[31:39] false, the LLM-as-judge agrees with it. Okay. Like out of you know the 73 times,
[31:45] but then when the human says it's false, the LLM-as-judge thinks it's a there is an error 18 times. Interesting.
[31:52] There is a different there's different kinds of errors and this is what I'm talking about here. You don't want to
[31:57] just go in agreement. You want to know what the true positive rate true negative rate is. Now, how do you know what a good true positive true negative
[32:03] rate is? There is no magic bullet there. That's a business decision. Like what
[32:11] what level of judge are you is is like okay for you in in the in the most base
[32:17] case. You just need to do a sanity check. Like does it make sense? Okay. Like you know does it seem okay?
[32:23] Calculate the true positive rate, calculate the true negative rate. Is one of them like really bad? Okay, then
[32:29] maybe you don't want to use that. Um is it really low? Um or you know just look at the confusion matrix do whatever you
[32:35] know and you can use a spreadsheet and say hm is this okay? Like am I okay with this kind of error? Um you know give
[32:42] yourself an intuition. often times you I would say for most people who haven't
[32:48] are not used to true positive rate true negative rate it takes some time for it to click
[32:53] even I have to think about it sometimes honestly even I've been doing this for years just to like ground myself
[32:59] I mean I think the confusion matrix is actually way more clear than the percentages I mean yeah
[33:06] 18 where it's marked as true when it's false yeah right yeah so there's a problem
[33:12] when it's false you like you know where it's false is where there's um you know
[33:17] out of these 91 times you have like 18 of these 91 times it has this specific
[33:22] error is that okay you know so basically so basically 18 times it actually did successfully hand off to the to the human to the human uh sub
[33:30] support but like the LM thinks it did not or like there's too many turns or something yeah yeah the like 18 times it LM thinks
[33:38] there is an error when there's not right is that okay and so like you know different sit situations you might be uh
[33:45] like the the false positives are not as expensive as the false negatives, you
[33:50] know? So like you you might be okay with catching things like catching more errors that
[33:56] don't actually exist. You just want to make sure you do catch all of them. So then what do you do with this 18 like
[34:02] you look back at the traces, see what happened and then you try to modify the prompt. Yeah. Yeah. So what you do is you can look at these like 18
[34:08] um and you can you know you can say okay like what happened here and you can iterate and you keep iterating a bit on
[34:15] the prompt. Yeah. Um and often times it's quite straightforward. Um sometimes not as
[34:21] much but one thing I did leave out here is a lot of times in the LMS judge you
[34:26] want examples. I didn't put examples here because I just wanted to keep it simple. Once you start putting examples
[34:32] in the prompt, you do have to um split the data set a bit. Like you
[34:38] can't just you can start overfitting to your data. So like if I put all of these traces in my
[34:46] prompt, it would get 100%. Because it would know the answer exactly, right? So like you
[34:53] don't want to do that and and so um you want to hold aside some data to make
[34:58] sure you're not cheating yourself and you know so that that's so we don't have to get into all that from a product
[35:05] manager perspective the best thing you can do is like just know just have a trigger in your mind about agreement and
[35:12] just don't just ask some clarifying questions like okay agreement is 90%. What's what is the baseline error rate
[35:19] if they say 10%. Yeah, you know that agreement 90% you're like this this is
[35:24] really bad like something something went wrong here and this is like pretty common right for
[35:29] for teams running evals they they just have a they just have like a agreement store they don't they don't have the TPR thing
[35:34] uh very extremely common is like yeah this is this is a reason I'm making a big deal out of it is uh because we just
[35:42] see it so much that uh it's worth uh calling out. Okay, got it. All right. So now we have
[35:49] some jud judges uh live and um like what what what's the next step? You want to
[35:55] put his judges into production to run all time. So now you have this really uh so let's
[36:01] say you have the judge like this human handoff score judge. That's right. And you like it enough. So now you have
[36:07] this like powerful tool that you can use like number one uh you can you know you can set aside some data. you can uh put
[36:15] it in CI. You can have a test anytime you make a change to code or whatever. You can test what the you know how good
[36:23] you're doing on this human handoff problem. But also you can run your judge in production. You can run it on a
[36:29] sample or a large portion of your production traces and you can see like where this handoff failure is happening
[36:36] and you can debug it even more. You can say I want to find all of the places where handoff failure is happening. I
[36:42] want to find a lot more situations where it's happening. Um and you can put you can do production monitoring of it um of
[36:48] problems. You can see you can use these judges to kind of run on a sample of traffic. You can know like hey are
[36:55] handoff problems happening you know so on and so forth. And you can
[37:00] build this suite of evals over time. Okay. Most of the time people ask me how many
[37:05] evals I have. Usually have under a dozen. I don't really have that many
[37:12] because I'm pretty parsimonious about the evals that I need. It depends like sometimes I have more than that if uh it
[37:18] depends how expensive they are. Um it takes some work to maintain this stuff as well. Um you know for the LLM-as-judge
[37:25] the codebased ones not so much. Uh because you don't have to do all this like you know because I don't have to do
[37:33] too many human this like human label stuff because like in the codebased stuff there's a there is a right and
[37:38] answer. Yeah. Yeah. And that's like that's called a reference based eval. And this
[37:43] is a reference free eval. So depending on what kind of eval it is um it'll you know there's a there's like a total
[37:50] budget sort of roughly in my mind of like okay how many you should have. So let's say you have like uh you know five
[37:56] or six judgy valves in production and and you just like so basically in production just means that like like
[38:02] this um human handoff jud judge like it it just randomly samples like out of 100 conversations it looks like five or
[38:08] something and then it kind of gives a pass fail. Yeah, it depends how many you have. Like
[38:14] it depends how many how what kind of scale you're at. you know, if you're serving like billions of users a day or
[38:20] something, then you probably don't want to run an LLM-as-judge across like everything. Um, you know, it really depends like you can get a lot of data
[38:28] from just sampling. But if you have like very low amount of data, like you're only serving like thousands of users a
[38:35] day, then just run the whole I don't know, just like score the whole Yeah. I mean, it's probably not that
[38:40] expensive. So, it really depends. And then you have a dashboard that has basically like TPR
[38:46] and TNR for each judge or or something. Yeah. And so what you can do is actually
[38:51] like you can bake this into a score. There are ways to like combine these TPR TNR. There's like F1 score and stuff
[38:57] like that that weight them equally or whatever. You can get into this. Usually do a report one score. That's probably
[39:03] beyond the scope of I have to go into a lot of like data science to like talk about how to do that.
[39:08] Yeah. Um but usually there's one score um that report and actually there's like
[39:14] all these evaluators and I try to have like one aggregate score um y
[39:19] that is like aggregated across all of them just to give me a sense and then I can drill in and see okay what's going
[39:25] on and and when do you do like human labels uh like you know because you you did it
[39:31] in the beginning with looking at 100 traces but like when when do you do human labels again? Oh, so always do
[39:37] them all the time. I do it like revisit it. It depends on the dynamics of the system. So depends like anytime there's
[39:44] like big changes, I'll definitely do it again and I'll also do it on a regular cadence. Let's say like once a week,
[39:51] once a month. It depends like how fast the systems are changing and how what the scale of the system is. But I'll do
[39:56] it like on both a cadence and also um and then you get better every time. But
[40:01] also you can build tools that help you do this. So, one of the things that we talk about in our course is okay, we use
[40:08] like Braintrust. We did this here. We did this a spreadsheet or whatever. Um, for nurture boss, what they ended up
[40:15] doing and I took some screenshots and I put it in my blog. So, let me just share that with you.
[40:21] Um, so they actually built their own annotation tool because it's so valuable
[40:26] of a process. Probably the most valuable process of eval is this like is annotation
[40:31] is the annotation and counting. Even if that's all you do, you don't build any judge, you don't do any eval what like
[40:38] you don't do whatever, you can get insane value by just doing that. And that's the one part that everyone skips.
[40:44] They try to like go directly to like whatever. Yeah. Um and so uh you know this is a
[40:52] screenshot of what they like the tool they built for themselves and they built this in less than four hours. Um because
[40:58] this is type of thing that AI is really good at. Yeah. helping you build. So it's like
[41:04] okay, you know, you can see this is a trace viewer. You have these selectors for different channels. You have um this
[41:10] is their interface. The system prompt is hidden by default. They could just create add notes here and then they had
[41:17] they baked it in into their tool where they just did the axial coding for them. You see like it just tried to do it for
[41:23] them and it gave them a count. Got it. They loved it. There's a video in this blog post here. This is Jacob and he's
[41:31] like super happy. Uh yeah, he looks happy now. Yeah, he talks about how like he did this and
[41:38] how like the the impact that it had on on his uh on nurture boss. So,
[41:44] okay. Um yeah, like you can get really fast. So, like you know with these like your own
[41:49] tools it gets ridiculously fast and it's not painful at all. Um, yeah. But basically, yeah,
[41:57] I mean, but basically, you should still like basically manually like before I make a major update to a prompt or something like I should still manually
[42:02] look at the, you know, like the traces and like just make sure like uh everything makes sense, right, before I
[42:07] ship ship anything. Yeah. I mean, you don't have to do it on every single prompt update. You don't have to look at man, you don't have to
[42:13] manually look at traces. You can just you can run your evals that you have um and do that way. Just make sure you're
[42:20] looking at your traces every so often. Yeah. because it's like it might be mysterious like oh like how
[42:26] often and how many traces. So we tell people look at 100 traces minimum.
[42:32] And the reason we say that that is not a magic number. We always find that if we don't give a number, people don't start.
[42:39] And then when we give a number, when people get in to like let's say 20 or 30 traces, they they they keep going uh
[42:47] until they So we tell people like the term is called theoretical saturation
[42:52] and that just means you keep doing the activity until you it's like a dimension
[42:57] returns. Yeah. When Yeah. until you aren't learning anything new. Got it. So we find that people once they
[43:03] start this they kind of get addicted to it and they find it so valuable that they just do it. So just keep in mind
[43:09] like 100 traces as a goal. Okay this is actually a great convers maybe I have to take down the video of
[43:14] Aman because but this is actually a great conversation because um so first of all so TRDR is that the the trace
[43:21] looking at the actual conversations of whatever AI product you have is the most valuable thing and kind of like counting
[43:27] on labling that right. Yes. and like okay so let let let's just
[43:32] wrap up by dispelling some myths okay so so I'm gonna put some I'm gonna put a statement out there and maybe you can
[43:38] tell me why it's is right or wrong okay so uh one thing that I that I thought
[43:44] was right was like you know you know you want to do a eval for a new product and then you get your team together and you be like oh you know like like should we
[43:51] do helpfulness or should we do toxicity or should we do like what should we do like and what what is the right criteria
[43:56] like what what is good toxicity and bad toxicity but that doesn't seem to Right. Based on what we just talked about.
[44:02] Yeah, that's right. So, a lot of people go straight to helpfulness toxicity score.
[44:07] Yeah, it's a very appealing idea. A lot of vendors, they sell that. They're like, "Hey, don't worry about evals. You just
[44:13] plug and play this tool. We got you. You don't have to worry about it. Just like push this button and then we'll give you
[44:20] a dashboard. Don't worry." The fundamental problem is generic prompts in those generic things usually don't
[44:27] match to the most important problems that are actually occurring in your application. They're just like super
[44:33] generic and they lead you astray and they actually waste your time because you
[44:39] spend a lot of mental energy looking at those metrics and looking at the dashboards and talking about the dashboards and having meaning about the
[44:45] dashboard and all of that could have been directed towards real problems that
[44:50] are actually happening. Now there is a right way to use generic metrics. There's like an advanced Jedi trick that
[44:59] you can do once you have learned error analysis. It will make sense. And what you can do
[45:06] is you can take your hallucination score. You can score this generic hallucination score on all your traces
[45:13] and you can sort the traces by the hallucination score. Okay? And you can see you can do error
[45:19] analysis and see does the top hallucination score like okay you can start doing like smart sampling with
[45:26] these different generic scores. You can use the generic these like all these generic scores as like sampling mechanism to see like is there anything
[45:33] interesting there. And what you'll find is sometimes there is interesting stuff. Sometimes it's not quite like
[45:39] hallucination but something else. And you can kind of see if any of these scores are helpful, but you shouldn't
[45:45] just report the scores. Should never report the scores as is. Probably shouldn't use the scores, but you can
[45:50] use them as meta tools. Got it. Okay. But but like it's way more important to identify as problems wrong with your product.
[45:56] Yes. Okay. Then another thing is like uh and maybe this is more a question like how
[46:02] much of the stuff that we just walked through should we do before we even launch the product? you know, like like should we try to have like a bunch of
[46:08] judges set up and like, you know, do a bunch of synthetic stuff like how how much because what once you launch you
[46:14] actually get real signal, right? I mean, yeah. How much of the stuff should we do? Yeah, I wouldn't get carried away with
[46:21] eval especially in the beginning. I would I would definitely look at lots of data. Um, and looking at data includes
[46:29] using it yourself. Okay. I mean if that like it says like if if you're building a tool for yourself like you are n equals one user.
[46:37] So you don't need to like just use it yourself and you know the air you're doing error analysis like just by being
[46:43] alive and using your tool like if you're actually using it that's fine. You don't need to do all this stuff. It's like
[46:48] when it kind of gets beyond the scale of your comprehension when it starts to you
[46:54] know there's like lots of users or lots of things going on different use cases. Yeah. Then you might think about okay
[47:00] that then you can see like where that data might be helpful or maybe you know you can roll out to like 5% of users and you know like maybe
[47:07] they get a shitty experience but then you can start getting real data to improve. Yeah then nothing beats real data.
[47:13] Got it. And like the the liker stuff is just is it just completely you sis or or like do you are you dogmatic about it
[47:19] the one to five stuff should you stay away from it? I would say I haven't seen you have to be extremely disciplined to
[47:27] use it correctly. Okay. Um you have to have very clear rubrics.
[47:33] You have to make sure everyone is calibrated on that rubric. Um and it usually doesn't go well and for most
[47:40] companies it adds tons of complexity. I would say it's exponential complexity on
[47:45] like relative to binary scores. And so I just haven't seen it done in most cases
[47:51] correctly. There's there's some rare exceptions where it does is okay, but
[47:56] it's usually like, you know, and I press teams to say, hey, like can we just make
[48:02] this a binary score? Like is there a point where this is like good enough versus not good enough? We're able to do
[48:09] it. But dude, then where does this stuff come from? Like why do teams keep doing this stuff? Yeah, because it it's a kind of an
[48:15] appealing idea, right? to like we've all been graded on like we have a grading system from school A through F like you
[48:22] know it's not nothing is black or white like we want to like have this like high fidelity sort of assessment but the
[48:31] problem is like what what would what do you even do with this highfidelity assessment like yeah it just makes you feel like false
[48:37] precision right it's like you know I got a three versus a four like what does that even mean like yeah like humans can't even tell a difference between a
[48:42] three and a four yeah yeah yeah most most people can't and it gets just gets lost in the sauce
[48:47] and already, you know, it's just like it's already complicated enough. You need to really reduce complexity in this
[48:54] whole thing and be pragmatic about it. All right, dude. This is this is super awesome conversation. So, so I guess let's go back to the Twitter debate. Do
[48:59] evals matter? It does matter if you do the problem properly, if you're actually solving real problems. Yeah, that's a really good question. Do
[49:05] evals matter? Yeah, I would say so eval don't exist in a silo. If you just try to do if you try to eval and get carried
[49:13] away with evals, it will probably hurt you. What you want to do is definitely ground yourself in the data analysis, in
[49:20] the looking at the data part. And like, you know, everyone says look at your data, but I I think um it's hard
[49:27] to know what that means. What we went through today actually shows you what it means and hopefully demystify what what
[49:34] it is to look at data. But it should be it's like a very tightly coupled with
[49:39] evals and I I say that it is eval like this data this looking at data counting
[49:45] I just say you you because you can't do evals without it. Yeah. It's not like the super sexy part of it but yeah it's the most important
[49:51] part of it. Yes. Yeah. Got it. Makes sense. All right dude. All right man. I I I think you
[49:56] convinced me to take your core course now. So uh can you talk about your course and um when you teach it and if
[50:02] you have a discount for folks? We are teaching a course on evals where we walk you through the end-to-end detailed
[50:08] process on how to do evals correctly. We go into subjects like okay how do you
[50:14] evaluate your rag systems? How do you evaluate retrieval? How do you evaluate agents? Um how do you deal with all
[50:21] kinds of edge cases that you might encounter? How do you do this effectively? Like how do you actually
[50:26] read a trace in you know save yourself from kind of all the complexities that
[50:32] might happen? and how do you get through this effort? And we've been we've taught over 2,000 students including lots of
[50:39] people from Google, open AAI, things like that. Um, you know, the big labs
[50:44] are really interested in this because, you know, they focused on foundation model benchmarks, but we're talking
[50:50] about application specific evals like if you're building an application, what is that? And that eval is very different.
[50:56] Yeah. Yeah. And so, uh, I teach the course of Shrea Shankar. Sha Shankar has been writing
[51:02] about eval as well for years now and been doing a lot of research in the space. So we both have a machine
[51:09] learning and data science background as well as software engineering background. You know in the course is four weeks
[51:15] long. We give students lots of resources. So we have over nine hours of
[51:21] office hours. Yeah. Uh we give students a uh AI evals
[51:26] assistant. So it's like everything that we've ever said about evals publicly in the course, blog posts, talks, papers,
[51:34] you name it. Uh we've put that in an AI and we give that to you as a like an
[51:40] assistant as well. So you know it's a it's a modern course and you got to have evals on top of that too, you know.
[51:46] Yeah. And we're doing evals. Yeah, we are doing evals on top of that. This is the first time this is the first cohort we're doing it for. Uh so this next one
[51:52] coming up in October. And so we also give people a 160 page book on evals
[51:57] that you can take with them. So there's a lot of resources there is a it's a good community and we're offering
[52:03] Peter's community 35% off. Awesome dude. So please see the link in the in the description.
[52:09] Awesome. Yeah, dude. I I personally learn a lot from this. I need to reevaluate how I do evals. So So yeah, I
[52:15] I hope to see uh folks there. Definitely want to take the course in October. Thanks so much Hamel and sharing your
[52:21] knowledge and um keep dropping non knowledge box man like on social media.
[52:26] Yeah, thank you so much. Thanks for having me.
