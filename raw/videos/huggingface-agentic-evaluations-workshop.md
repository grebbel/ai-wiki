---
title: Agentic Evaluations Workshop - Deep Dive on the Future on Evals for Agents.
video_id: UxMZfbWI3LY
url: https://www.youtube.com/watch?v=UxMZfbWI3LY
channel: Hugging Face
channel_id: UCHlNU7kIZhRgSbhHvFoy72w
channel_url: https://www.youtube.com/channel/UCHlNU7kIZhRgSbhHvFoy72w
publish_date: '2026-03-20T01:06:58-07:00'
upload_date: '2026-03-20T01:06:58-07:00'
category: Science & Technology
length_seconds: 6526
view_count: 21949
is_live: true
is_upcoming: false
is_private: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi/UxMZfbWI3LY/maxresdefault.jpg?v=69af3ce9
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
description: "As agents evolve from text conversations to autonomous agents capable of multi-step reasoning, tool use, and real-world task completion, evaluation methodologies must evolve to keep up. We will discuss topics related to questions such as:\n\n- Where is the state of the art in evaluating agentic systems?\n- Why are agentics systems’ performance on benchmarks not reflected in usage?\n- How can we evaluate the agentic systems and language models that we use? \n\nThis workshop brings together diverse perspectives from academia, industry, and policy to explore the frontier of agentic evaluation.\n\nIncluding: \n\nAvijit Ghosh,  Hugging Face \nArvind Narayanan, Princeton University \nPierre Andrews, Meta\nJ.J. Allaire,  UK AI Security Institute \nMahesh Sathiamoorthy,  Bespoke Labs \nNathan Habib,  Hugging Face"
notes: Fetched via youtube-transcript-skill; ASR caption track (auto-generated); ingest-time line grouping preserved verbatim from skill output.
---

## Transcript

[0:25] Hi everyone. Welcome to the agentic evals workshop organized by hugging face. I'm Ben and I take responsibility
[0:33] for the community education at Hugging Face and I organize programs like our courses and
[0:40] workshops like this. This is the first time that we've organized a workshop and
[0:46] uh we're really excited about it and it's a new kind of new format for Hugging Face where we're going to tackle more
[0:52] nuanced and complicated topics that we can't necessarily put into courses or educational material things that we
[0:58] don't necessarily fully understand and we think that we need to take the time to bring experts in and and work
[1:03] through. Today we're going to focus on agentic evals which is a particularly
[1:09] challenging problem to some extent. We figured out how to evaluate LLMs on on
[1:14] text tasks. There are still limitations there. And as we move into agentic domains and agents start to work on long
[1:21] running tasks. Evaluating those over time becomes exceptionally difficult as
[1:26] we're going to hear today. We have a a broad selection of of
[1:31] speakers from industry, research, policy and open source and we're going to work
[1:38] through those. So first we have Avijit Ghosh from hugging face and also from
[1:43] eval evals and Avijit is going to introduce the problem and then we're
[1:48] going to move to Arvind Narayanan from Princeton who's going to talk about
[1:55] further and then we're going to go through the program to
[2:02] and um from Neta who will talk about GAIA too
[2:07] the identic benchmark paper and then we'll hear from Mahesh from bespoke
[2:14] labs who will talk about how they're evaluating agents of Bespoke Labs in industry and then we're going to hear
[2:21] from Nathan also from hugging face a maintainer of the Open LLM Leaderboard and now future
[2:29] I don't want to take up too much time I'm going to give as much time as possible to the speakers so if you do
[2:34] have questions just raise those in the chat and I'll raise them to to the speakers and we'll try to keep tempo
[2:40] quite high and move from one to the next. So without further ado, I pass over to
[2:50] Thanks Ben. Um let me try to share my screen.
[2:55] [snorts] Great. You should be able to get your slides up right now. Great.
[3:03] Cool. Are you able to see my screen?
[3:14] Okay. Um, hello everyone. Um, I'm Avijit Ghosh. Um, I'm a technical AI policy
[3:20] researcher at Hugging Face. And today I'm going to be talking about my talk today is called evaluation reporting in
[3:26] the age of agentic AI. Um, as Ben mentioned, I also lead a group of 400
[3:31] plus researchers called eval. um a big focus of that has been looking to eval documentation. So this talk is
[3:38] going to look at uh what's currently missing in the field of evals, how specifically it relates to agentic evals
[3:44] and what we're doing to uh fix that problem.
[3:49] So we have moved on from LLMs that generate
[3:54] text to now more agentic systems that plan, decide and act. So in terms of
[4:00] that we have examples like open computer use uh uh claude's computer use Gemini
[4:06] now has agent mode we all uh really enjoyed manis um and we have also heard
[4:11] about open cloth so it's it's everywhere um but before we dive deep into agentic
[4:17] evals um I wanted to talk about the state of eval generally speaking and
[4:23] what the missing part parts are in terms of honest and transparent eval reporting.
[4:30] So a lot of eval nuances are actually hidden in the small print. So this
[4:35] screenshot is from um OpenAI's uh system card for GPD 5.2 and it was criticized
[4:43] heavily by anthropic and also just by other eval folks because um they reported a very high SWE score but then
[4:50] in a very tiny fine print um they basically said that they had omitted 40
[4:56] out of the 237 problems. Um this is not immediately apparent if you are trying
[5:01] to consume evals very very quickly and you look at just the table and move on with your lives. Um there are other
[5:07] similar issues. When Llama 4 was released, um it came out that Meta had
[5:14] used um different versions of Llama 4 to uh score different benchmarks which just
[5:21] uh sounded like not the best eval practice and um their reports were also criticized for similar reasons. Um
[5:28] essentially benchmark maxing. Um we also have seen problems in the
[5:34] community uh basically chart crisis or misrepresentation of data using weird
[5:40] graphics. So a couple of those examples are currently on the screen. Um for
[5:46] instance um the sweep score of openi was reported in a very weird way like you
[5:52] can see that um 69.1 and 30.8 data shown as similarly tall histograms uh which is
[5:59] not scaled to anything based in reality. Um similarly people often don't report
[6:06] um error bars um which is another problem in terms of eval rigor
[6:13] um and that's just talking about um regular capability eval when it comes to
[6:19] social impact eval uh the situation is far worse. So the evalu coalition that I
[6:25] mentioned that that I co-lead um we have a paper out called who evaluates AI
[6:30] social impacts mapping coverage and gaps in first and third party valuations. Um so that paper looks at the state of
[6:37] reporting of social impact eval. And by social impact I specifically mean things like environmental impacts, financial um
[6:44] such uh stuff and so on bias um and so on. Um we looked at uh social impact
[6:51] eval by foundation model developers over time. Um specifically we looked at 171
[6:57] model release documents. Um we see a lot of uh interesting
[7:02] things. We first of all observed that model developers have become less transparent about their eval results
[7:08] over time. So for instance environmental cost reporting in firstparty reports. So
[7:14] uh essentially this chart is showing the things that model developers report themselves. Um that has become
[7:21] um less transparent over time. In fact less than 15% mention labor and environmental effects. This this used to
[7:28] be not the case back in 2022 like most orgs were reporting um almost everything about their models. Um but then as time
[7:36] has passed u model developers have become less transparent for a host of different reasons. Um so we look at
[7:43] specific examples. Um for instance, Google and Meta used to report a lot more back in 2022 and 2023 and they
[7:50] don't report um these social impact evals anymore. Um first party reports in general are
[7:58] not transparent and are of lower quality. We also therefore did interviews of eval practitioners. We
[8:04] asked like okay why are you not reporting these things over time? What happened? Um we were told that companies
[8:10] have either broken up or reassigned teams dedicated to documentation or social impact evaluation. We also heard
[8:17] that um because of the changing political climate or legal liabilities
[8:22] companies are told to focus more on capability reporting over risk measurement.
[8:29] Um at the same time in terms of positive news we find that um third-party
[8:34] reporting meaning third party orcs like meter and Apollo um uh Meror and so on
[8:41] um eval reported by them have gone up both in terms of quality and in terms of
[8:47] raw quantity over time. Um which only strengthens the position that good
[8:52] quality independent third party valuations are paramount for holistic AI safety. Um given that observation um how
[9:00] do we see all of these third party evaluations for a model in one single place because these evaluations are not
[9:07] really always published in the same format. Somebody produces a leaderboard, somebody else produces a report,
[9:12] somebody else produces I don't know blog post. Um so to centralize that information we created uh a project
[9:20] called every eval ever. Um so we launched this project last month with a
[9:27] host of different organizations. Uh some of the logos are on the screen. Um so what is every valver? Every is a a
[9:36] unified open data format or schema and then b a public data set of every
[9:41] possible first and third party evaluations on hugging face with these results. Um we are actively collecting
[9:48] these um evaluation results in that schema. So very briefly the schema um h
[9:55] supports both aggregate results. So you are required to report things [snorts]
[10:00] like source provenence um specification about the model and not just the model but also what quantization you used,
[10:07] what version of the model you used and so on, what evaluation library you used. Um we also support the instance schema
[10:14] meaning that if your eval result uh is not just reporting an aggregate score but also line by line results we support
[10:21] that as well and eventually the hope is that um with all this data we will be
[10:28] able to build something that we're calling eval cards. So a dummy um screenshot is currently on the screen.
[10:35] Um the hope is that you'll be able to go to the Eval Cards website, click on
[10:40] whatever model you want to look at, say um Quen 72 billion, and you get to see
[10:46] all of these um first and third party evals organized under categories and get
[10:51] a very quick sense of what's going on for their model. Um
[10:56] so um that's where we are in terms of building infrastructure to centralize and report eval in ways that cannot be
[11:05] gamified as easily because um this type of filtering allows you to hold all of
[11:11] these confounding variables constant and then see the exact scores between models. And um Nathan will get into uh
[11:19] other uh infrastructure issues later in in the talk. We'll hear from him later. Uh but I think this is extremely
[11:25] important for honest and non-gamified eval reporting. Um and now given that situation of uh
[11:33] requirement of centralized eval documentation, we get to the state of agentic eval. So what's going on in
[11:39] agentic eval specifically? Um agent eval
[11:45] beyond LLM eval because they are more complex systems. So on the screen you
[11:50] see an example of two agents that score that score pass on an eval um but
[11:58] they're actually completely two different stories. So the first one like takes less number of steps is cheaper,
[12:04] it takes less time and does not crash or has zero errors. Uh meaning that the
[12:10] metrics for agents generally look different and so the evaluations need to be more robust.
[12:16] Um, current agentic benchmarks are still mutually incompatible. They look at
[12:22] different things and it's really hard to um sort of generalize results uh between
[12:29] different things over time. So for instance, Taobench um specifically measures user messaging um which is not
[12:37] really something you can then also use to measure um computer performance on the web. So therefore it's not
[12:44] compatible with web arena and and not compatible with terminal bench. Um so
[12:50] more um generalized performance is required. Um specifically agent eval
[12:56] need to capture sequence of actions meaning uh are you measuring what's
[13:02] happening in the chain of thought are you measuring what tools are being called? Um what is the context of the
[13:08] action? What was the user input? What environment was it? what was the noise? Um also uh I think uh human interaction
[13:18] is undermeasured in the current landscape of agent eval. Um so people
[13:23] can interact in different levels of the agent workflow. Um are we measuring the
[13:28] impact of or the noise produced by the human input? Um there's a paper out um where I was
[13:37] one of the co co-authors um saying agent systems should be general. Um specifically in that paper
[13:44] we claim that we should build the protocols, evaluation frameworks and development practices needed to support
[13:51] um adaptable agents. Um general purpose agents are probably the future that we
[13:57] are all moving towards. So our evaluation framework should look the same. So what is concretely missing across uh
[14:05] agent evals? Um a lot of evals don't report um session level um reporting
[14:14] meaning that you can have completely different results between two sessions
[14:21] um even though you might have two identical scores um as I showed in the example above. So having session level
[14:28] information is important for reproducibility. Um [snorts] agent identity is a black hole. Um right now most agent valals are
[14:37] tagged with a model name. Um the model is not necessarily the agent. Um so we
[14:42] would also like information about the sub agent list um MCP servers memory config and so on. Um benchmark specific
[14:50] protocols block block generalist agents. Um so if you have designed a benchmark that requires a very specific setup that
[14:58] does not work very well with generalist agents um robustness measurements are
[15:03] not standardized. Um people are not reporting seeds prompt perturbations passet K and so on. Um we need better
[15:11] standardization around those. Um cost reporting is inconsistent or absent. Um
[15:18] some evalu cost but not uh others. Um also benchmarks are currently lacking in
[15:25] the feature set that they're not simultaneously cross model cross environment cross agent cross protocol
[15:31] and agent agnostic. Um so working towards generality is something that we have waited for.
[15:38] So how does that relate to documentation? So bringing it back to every um the team that wrote that paper
[15:45] they have proposed some agentic extensions. So in terms of standardized eval reporting we can extend that for
[15:51] also agents by additionally submitting system composition. So what are the
[15:56] models inside the system? What are their roles? What are the sub aents? What are the MCP servers and so on. Um session
[16:02] semantics. So we need to very clearly add fields for what defines a particular
[16:08] run or a particular session of an agent. Um interaction accounting. Um so again
[16:14] all of these additional measurements that measure an interaction and finally eval conditions. So what are the
[16:20] conditions required to reproduce that agent action that can be evaluated by somebody else cleanly by specifically by
[16:27] a third party. Um as Ben mentioned at the top of the talk there still remains technical
[16:34] challenges. Um I still would like to see more human AI interaction measurement or
[16:41] human agent interaction measurement. Um specifically in systems um we are also
[16:47] starting to see emergent multi- aent effects now with open clock people have claws um we ourselves have been noticing
[16:54] at hanging face that we get a lot more pull requests by people's clause um and
[17:01] it is not very clear to us how to sort of do that kind of monitoring cleanly
[17:08] um uh and then uh we also So we meaning the
[17:13] community is also working towards better measurement of long horizon tasks because that is not yet clearly defined.
[17:19] Um meter has a long horizon benchmark. Um but again that is people mean
[17:24] different things when they mean long horizons. Um what are the policy implications of
[17:31] this uh this sort of need for standardization of reporting? So um
[17:37] governance requires session data. So we in terms of actually holding people
[17:42] liable or their agents liable, we need uh clear session information otherwise
[17:48] you cannot um clean the audit agent behavior. Just giving a score is not enough. Um you also need white box
[17:54] system records. So just saying the model data is insufficient. You need to see which actor was responsible for a harm.
[18:00] This already happens in AI. So when you look at an AI life cycle, you have the data collector, you have the model
[18:06] trainer, you have the um system designer, you have the person who was responsible for making you interact with
[18:13] the system. So if you're in a professional scenario, um somebody was responsible for uh whitelisting some AI
[18:20] systems and not allowing others. And then you have the end user um agents make that problem uh worse by multiple
[18:28] orders of magnitude. So having infrastructure that sort of allows you
[18:33] to measure accountability cleanly is needed. Um shared schemas are great for
[18:39] independent evaluation. You can both see all of the evaluations for an agent or a
[18:44] system or an LLM in one single place and you can um reproduce them with the
[18:49] technical parameters that we are requiring for uh the schema. Um finally
[18:56] um safety oversight is undermined by benchmark gaming. So we need we as a community need to continuously talk
[19:02] about malpractices in eval reporting um so that we move away from benchmark gaming and actually move towards
[19:08] holistic AI safety reporting. So in terms of my closing thoughts the call to
[19:13] actions I have for the community are we should build evals in the open. We should have compatible open reporting
[19:19] frameworks. We should stop benchmark chasing and look at the aggregate picture. Look at what happens beyond
[19:24] just getting a particular score. Um we need better scalable oversight. So we can't just have the world have 1 million
[19:31] open claws. We also need to make sure that it is monitorable by humans. And finally, eval policy should move beyond
[19:38] capability measurements and also keep humans and societal impacts in mind.
[19:44] With that, I'm at the end of my talk. Um, thank you so much for listening and I'm open to questions and feedback.
[19:53] Thanks. Yeah, that was a really cool talk and it really set the stage for for the the rest of the workshop. Uh we had
[20:00] a couple of we actually had a number of questions coming in and one that I think
[20:05] um was repeated a few times was really about the relationship between the model
[20:12] and its harness or or its implementation like the agent's implementation. Um, one question was how much of the
[20:20] safety concerns come from the the underlying LLM and how much come from the agent. Uh, and another question
[20:26] which which I kind of want to myself was really how would we evaluate
[20:31] harnesses agnostically? Would we have like a single harness that we say this is our eval harness or would we just
[20:37] need to kind of take every major harness and and evaluate them? Which strategy do you suggest? So um so there is a paper
[20:45] uh follow-up paper to the paper I shared about agent system should be general called exgenic um by the IBM team. Um so
[20:53] they really go really deep into this meaning that there is a way to create uh
[20:59] agentic evaluations that are harness agnostic. Um to get to your first question though is um some errors do
[21:06] come from LLM underlying LLMs and some errors come from the tool itself. Um
[21:11] there is a ton of work uh pre-agentic work on cascading biases for instance like I come from a fact background. Um
[21:19] uh so I I just generally think that we should look at
[21:24] agents as a white box fashion meaning that you look at the whole system you not only see what the failure modes of
[21:31] the underlying LLM are but also what are the failure modes of the tools that are used. Um was a particular tool called
[21:38] correctly during the agent run. uh was there is the chain of thought inconsistent um and so on. So it's it's
[21:46] more holistic than that. So like I personally favor reporting all possible information um for maximum
[21:53] reproducibility and then we go from there.
[21:59] [snorts] I think you're muted.
[22:06] Great. Thank you. We're gonna keep the train moving and move on to Arvin Naran
[22:12] now and uh is going to give a presentation on uh towards a science of
[22:18] AI agent reliability in
[22:25] great thank you Ben uh hi everybody I hope you can all hear me uh Aviji really nicely set up a lot of the problems with
[22:32] AI agent evaluation and I would like to tell you about my team's recent work taking a big swing at one set of those
[22:39] problems, those related to agent reliability, which we think is a kind of a separate orthogonal component from
[22:45] capability. And until this work, we're not really aware of any serious efforts to even define what reliability is,
[22:51] figure out what are the different components of reliability and try to measure them and see whether reliability
[22:56] is improving over time. And so that's what we've done in this paper. I want to give a shout out to the team in particular Stefan Robons, the first
[23:02] author who's put an incredible amount of work into this. uh and some of the slides are also from him. Okay. So to
[23:09] motivate this, let me start with a paradox that many people have been noticing uh which is that AI agents have
[23:15] been basically crushing all kinds of capability benchmarks. And if you believe this hype, companies should be
[23:21] replacing people with agents left and right. That doesn't seem to be happening. There's no measurable impact
[23:27] on let's say the GDP yet. What could be the reasons for this? One possible reason is that it's just going to take
[23:33] time. Many companies, people might not even be aware of these capabilities yet.
[23:38] So maybe we just have to wait a while. That is a plausible explanation. We think there is another plausible
[23:44] explanation which is that these capability benchmarks are looking at only one component of what it takes to
[23:50] make an AI agent useful. And these agents are actually not useful enough yet to be sort of drop and replacements
[23:56] for almost any kind of uh uh human worker. Uh and we think this is a big gap. this is a capability reliability
[24:03] gap. And so that's the hypothesis we explore in this paper. Now, uh we've
[24:08] kind of known this for a while. There have been some notable failures of consumer products. We'll talk about
[24:14] enterprise in a second. Consumer products that uh were highly capable but were not reliable enough and so no one
[24:19] wanted them. So here's one example that many people might have seen. This is was called the Rabbit R1. I think again this
[24:26] was from almost two years ago. You could just talk to it. It didn't have a screen, but you could just talk to it
[24:31] and could order products for you online. That's an incredible capability, right? People were just building these rappers
[24:36] on top of LLMs uh and trying to make these kind of aentic hardware products. But people quickly noticed when they
[24:44] tried these that there were reliability problems. Uh so in this example, it delivered food to the incorrect address.
[24:51] And also something with the tip you can see at the bottom. Now, even with pre-Lolm Aentic systems like Alexa and
[24:58] Siri, we've had reliability problems. But if Alexa or Siri plays the wrong song 10% of the time, that's merely an
[25:05] annoyance. But if uh an Aentic product, you know, uses your credit card and does the wrong order 10% of the time, that's
[25:12] dead on arrival, right? So, this is a really serious issue. And so, we I've been ranting about this on social media
[25:18] for two years, but six months ago, we started to really try to define and measure the problem. uh and I want to
[25:24] tell you about some of those results. But let me give you some more examples. While we were doing this research, we
[25:29] noticed many many other examples of reliability failures of deployed agents.
[25:34] Whether it's sorry uh skipped a slide there, whether it's OpenAI's operator again with incorrect purchases or on the
[25:41] right here, you can see an agentic coding system deleting a production database. You've probably seen many
[25:46] horror stories like that. Even governments which are usually pretty slow to move are not immune from the
[25:53] reliability failures of these systems. Now if you look at the attitude in the
[25:59] AI industry compared to other traditional industries where safety is important like aviation or nuclear power
[26:05] it's just such a different approach to things right so if you think about it in terms of pure capability you know ever
[26:11] since uh the Wright brothers we've had demonstrations that planes can fly but getting them to the point where it's one
[26:17] error every trillion miles or whatever that standard is that level of reliability took most of a century and I
[26:23] think that is u you know maybe it won't take most of a century but there's a
[26:29] long way to go I think for AI agents to be able to be used in high stakes environments uh in order to reach those
[26:36] levels of reliability. Okay so with that let's get into some details here. So
[26:41] when we looked at all of these domains, we found that there are four different dimensions of reliability that emerged.
[26:47] Consistency. Um so a 70% accuracy might mean that uh there are 70% of tasks that
[26:55] the agents can perform consistently and the other 30% where it will consistently fail. Or it could mean that on any given
[27:02] task unpredictably it'll work 70% of the time and fail 30% of the time. Uh robustness. What happens if you slightly
[27:08] change the prompt or environment or whatever? predictability. Can it look back at an agentic trace and figure out
[27:14] if it has performed the task correctly or not? And then when failures do happen, is the severity high or low? So
[27:21] again, these are from traditional systems, but we were also able to adapt them to AI agents. And so here's our key
[27:28] finding. So we looked at uh 14 different frontier models and we used a scaffold.
[27:34] You can see the details of the scaffolds and harnesses in the paper. But the critical finding is that over the last
[27:41] 18 months, a period when accuracy on different benchmarks has been improving dramatically, when you look at these
[27:48] four dimensions of reliability, uh, and you have a composite score based on those different dimensions, reliability
[27:54] has only been going up very gradually. And um, you know, if um, if you think
[28:00] that AI Asian capability is improving exponentially, this should be a bit of a sobering finding. Yes, capability is
[28:06] going up, but capability doesn't fully measure usefulness. And there is this other dimension we should care about.
[28:12] And so this was on uh GAIA uh and the Towbench airline uh uh benchmark. Uh
[28:18] we've started with two, but we're gradually working to add more benchmarks to this. So I'm going to show some more
[28:24] charts that go into this in a bit more detail. Um
[28:30] so there's going to be a lot on this slide. I apologize. So let's start with the middle. So in the middle here you
[28:36] see the two uh uh charts uh the two benchmarks GAIA and TaBench broken down
[28:42] separately. So especially on GAIA but on Ta bbench as well the reliability
[28:48] progress has been slow. Uh on the other hand accuracy progress as you can see on the left has been much more rapid. The
[28:53] slope is much higher. Uh and then on the right hand side you see accuracy versus reliability. It's a remarkably straight
[29:00] plot. Uh so there seems to be a very strong linear relationship. Uh so
[29:05] reliability does go up as accuracy goes up but much much slower and this is across a whole bunch of different
[29:11] frontier models. So that is the key finding. Okay. So what I want to do in the rest
[29:18] of the time in you know in the next uh 5 to 10 minutes is to look in a little bit
[29:23] more detail at what these different dimensions are and what they're capturing. So if we look at the
[29:29] consistency dimension that actually further splits into three different metrics. We look at uh you know is it is
[29:36] it the same pass fail result each time for any given task or is it kind of stochastic even within a particular
[29:42] task. So that's outcome consistency and then trajectory consistency is is it taking the same set of actions in the
[29:49] same sequence each time or is it you know uh exploring different ways of doing the task. Um, that kind of
[29:55] creativity can be actually helpful in certain scenarios, but if you have like a customer service agent for instance,
[30:02] you really wanted to have the same predictable behavior for each customer. Otherwise, it's hard to have quality
[30:07] assurance over how it's going to work on a scale of millions of customers. Uh, and then cost and other resources. How
[30:14] stable are they across different ones? Uh, and then we have different kinds of robustness, fault robustness. we uh
[30:21] specifically inject faults into the environment because of course when agents are deployed there are going to be you know API timeouts and various
[30:28] other kinds of errors. How good are they at dealing with these things? Another one is prompt robustness. We use an LLM
[30:35] to automatically reword the prompt in a way that preserves the semantics but changes you know the style or tone or
[30:42] something like that. So in this example, you might see an informal style of prompt might lead to one answer compared
[30:48] to a more formal style of prompt. So this is a hypothetical example, but I'll show you uh some some uh real insights
[30:55] from agent traces as well. Uh calibration. So this is really important.
[31:01] You know, if um if an agent is not calibrated, typically non-calibrated
[31:06] agents tend to be overconfident rather than underconfident, then you elicit its confidence score. how likely is it that
[31:13] you got the correct answer? Uh if it says 60% then you know you expect that
[31:18] to actually be true 60% of the time but um in the case of an overconfident agent
[31:23] it's going to be giving scores like 1.0 but in fact only half of those cases did it actually succeed. Now one good news
[31:30] is that calibration has been improving because of issues like zopency. We suspect that's the reason why companies
[31:36] have been really careful about fixing this because they've gotten into trouble for overconfident chatbots and agents.
[31:42] But the downside has has been that discrimination has been getting worse over time. So, uh you want good
[31:49] discrimination, which means that the agent doesn't always say 50% or something close to that when asked how
[31:54] likely it is that it succeeded. You want it to be able to separate its successes from its failures. Okay. And then
[32:01] finally, safety. This is something we measure but we don't aggregate into our overall index. We look at the severity
[32:07] of failures. Is it something minor like a formatting error or is it something major like data deletion? All right. So
[32:13] uh here I want to give you some insights from uh automatic as well as manual analysis of agent traces on the GAIA
[32:21] benchmark which we found to be a very interesting benchmark for this purpose and I believe we'll hear a GAIA 2 talk
[32:27] later. One thing we found is that on the calibration problem specifically models
[32:33] tend to uh get to get confused when they
[32:38] have a very clean process versus a messy process if there were some tool calling failures that sort of thing the model
[32:44] thinks oh maybe the answer is wrong when in fact that actually has nothing to do with the correctness of the answer. So
[32:49] that was one kind of failure mode. Uh another one is many of the questions in
[32:54] GAIA were ambiguous. Um, and that's really interesting from the perspective of eliciting capability. You might think
[33:00] this is a bad thing. It's under eliciting capability because models are getting confused by ambiguous questions.
[33:05] But from a reliability perspective, that's very helpful for us. We can examine what happens when these models
[33:11] are faced with ambiguous questions because in real world deployment, of course, there will be ambiguous tasks all the time and they don't handle it
[33:18] that well. uh and then I won't go through all of these but you know we did find many cases of hallucinations when
[33:24] for instance we inject false which means that some of the data that they need to download to complete the task becomes
[33:30] inaccessible. So even if by default the model might not hallucinate much when we put it in this situation uh then it
[33:36] might do so. Okay. So what are some lessons from
[33:42] this? So we do think that uh companies that are deploying agents have to make a critical
[33:48] distinction between whether the agent is meant to augment uh human productivity.
[33:53] So for example in a coding agent you know many of these errors are maybe not too not too bad because the the
[34:00] programmer is still in the loop and they're reviewing the code uh and so forth. But in a customer service agent,
[34:06] you want the agent to autonomously handle customers. These are much worse
[34:12] uh errors, right? So reliability really matters in automation tasks as opposed to augmentation tasks.
[34:20] Okay. Uh and so maybe you know for release decisions, it's not just capability that matters. It's also some
[34:26] reliability threshold that needs to be met before you decide to deploy an agent. And for researchers and
[34:31] developers, we think it really should be the norm that for every benchmark uh you
[34:36] know this is not some reliability specific benchmark. I want to I want to clarify that you can take any benchmark
[34:42] and measure all of our reliability metrics on it. So maybe that should become the norm. Uh and then uh we've
[34:47] seen many uh researchers say oh you know as models get smarter in general the reliability issues will get solved.
[34:54] Maybe but I think we should also prepare for the possibility that maybe that won't happen and we have to specifically
[34:59] work towards optimizing reliability. Okay. Um so I do want to clarify that so
[35:05] far our findings are tentative. uh we're you know uh reviewing our uh runs for
[35:11] for any bugs. We know there are many limitations only two benchmarks um not too many scaffolds etc. So we're working
[35:18] on all of those uh and we're hoping to launch a reliability index which will be a one-stop shop for tracking how
[35:24] reliability is changing over time in the community. Um and then uh just some last
[35:30] thoughts on some big picture implications. uh one thing I wanted to mention is that if you look at to the
[35:38] extent that you're interested in you know the grand ambition of the AI community to achieve AGI I think our
[35:44] work has some implications for that. So the UK AC AI safety institute recent or
[35:49] security institute recently put out a nice report listing six barriers to AGI
[35:55] right and what our work did is to drill down into reliability and identify these 12 different metrics and most of these
[36:02] metrics aren't solved. Two of them are more or less solved but the other ones still remain barriers. So we think that
[36:09] if other researchers were to drill down into each of these other barriers and identify those subdimensions, we're
[36:15] going to identify lots more barriers that need to be solved before we can get to some notion of AGI AI that can
[36:21] replace you know almost any human worker. Um and then one final thought uh
[36:27] this is on long horizon tasks. You already heard a little bit from JJ about long horizon tasks. Now meter famously
[36:33] recently said, "Oh, you know, our task suite is starting to get saturated." Well, maybe. But what if what's getting
[36:41] saturated is not the task suite. The tasks are fine, but the metric is saturated. It's not enough to look at
[36:48] capability. You have to look at, you know, 12 different dimensions of reliability, various other things. Maybe collaboration ability, cost, latency, so
[36:55] many other metrics you might want to want to look at. So that is a provocation that I want to end on. Our
[37:01] evaluations for agents need to be much more multi-dimensional. If everybody is just focusing on capability, we're
[37:07] really missing many questions about what makes agents useful in the economy. Okay, thank you very much.
[37:15] Thank you Alvin. That was a really cool talk and and and we went even deeper. That was great. Yeah, we had once again
[37:21] questions firing in um and kind of also about the implementation again. people
[37:27] were interested specifically in a kind of React paradigm or even in um yeah in
[37:33] kind of other implementations of agents, how what it would look like practically and and how if I was building an agent
[37:41] in a research or or industry context, how I would measure reliability
[37:47] like like for example, if I was working on an open-ended task and agents could achieve that task in in many different
[37:53] ways over different numbers of turns, how I measure that in my system and kind of
[37:59] act based on on what I found. Yeah, definitely. So, in terms of, you know, reproducing our results and um
[38:05] doing these same measurements for different tasks or different benchmarks, our code is available. You know, please
[38:11] feel free to reach out. We're happy to help with that. Um, what I take from the question is that if you had, you know, a
[38:17] kind of more open-ended task, what does it mean to to look at the consistency of the agents performance? I want to
[38:23] clarify that on many kinds of tasks the reliability metrics that we measure might not be desirable things. Uh in
[38:31] some cases for instance if you want let's say you just to take an extreme example if you want an agent that writes
[38:37] poetry if it does the same thing every time if it produces the same poem on any on a given topic every time that would
[38:44] be a very bad thing. You want the agent to be creative. You want it to be very stochastic. And so it really depends on
[38:49] the task whether it actually makes sense to measure what we're measuring or not.
[38:55] Great. Thanks for that. Um we'll keep on going on to Pierre Andrew. Thanks Ain.
[39:02] Okay so Pier Andrew ready to go. I'll just get your slides ready. There you go. So you can take it away Pierre.
[39:09] Hey thank you Ben. Um hey I'm Pierre. I'm a research engineer at MEA. Um, and
[39:15] I'm going to talk about GAIA 2, which is uh a new benchmark for agents that we've been developing um with people from the
[39:22] GAIA original team and and a bunch of other people you can see on this slide. Um, a lot of the previous speakers have
[39:30] talked about the challenges of evaluating agents and here I'm going to dig into one possible benchmark. It's
[39:38] not the full benchmark for everything. Um but I'll talk about the challenges
[39:43] we're trying to solve. Um and one core thing we're trying to work on is agents
[39:49] when you look at open flow are vice they need to work on a word that keeps
[39:55] changing. So, previous evaluations of LLMs would get a prompt input and look
[40:02] at the output of the LLM and say this is the correct or the wrong answer. And that that was um the evaluation. Um, for
[40:10] three agent evaluations, you put your agent in a sandbox and you let let it
[40:16] work on a bunch of code files and check that they compile um and pass the test
[40:22] you want, but they don't have any input from the outside world. Um, [clears throat] but in real consumer
[40:28] agents um the outside world changes. You get new evals. Um, the news changes,
[40:34] the internet changes. You have to be able to adapt to this. Um so we need evaluation frameworks that let us do
[40:41] this. Um an example and it's really tiny I'm sorry. Um is this task that you might
[40:49] give to someone to an agent which is um organize a one tasting with some
[40:54] colleagues. Um the agent has to um eval the colleagues, wait for their eval
[41:00] responses, um book a bunch of things and adjust to the environment sending um
[41:06] inputs to the agent, not just the user talking to the agent.
[41:11] So we're trying to solve this with simulation um in GAIA 2. Um and there are a few other environment that do
[41:18] dynamic environments like this. So Arvin mentioned T square earlier that does
[41:25] user simulation. So the agent sends a message and the user responds to the
[41:30] message in the in the benchmark. Um the vending bench benchmark does some
[41:37] environment simulation by changing the cost and the sales and the demand um of
[41:42] the vending machine. Um but we're trying to focus on what we call multi app
[41:49] simulation. So think of it as um trying to simulate what you would have on a
[41:55] mobile phone where you would have a bunch of apps. Some of them are connected to external services like your
[42:00] eval or your messenger apps. Some of them are purely local stuff like your file system. Um but they all interact
[42:07] and they might change with what the s the agent does, what the user does or
[42:13] some external um environment he builds. Um the GAIA to benchmark has been built
[42:19] on top of uh the ma agent research environment which is a platform or
[42:26] framework where you can build um use this simulation and build evaluations um
[42:31] for agents. So it's not specific to GA 2 and if you want to contribute other um
[42:38] kind of task uh feel free to to try [snorts] um [cough] and the concept [clears throat] in um are four main
[42:46] concepts. Uh first we have the apps. So again it's like an app on your phone. It keeps some state um about the word and
[42:54] the the app and it exposes some tools or some API surface then the agent can
[43:00] interact with um the environment can interact with and the user can interact with either through um API calls through
[43:07] Python through MCP or even through CLI if we want for more modern um
[43:13] orchestration frameworks. Um then we have a concept of universe which is your simulated environment and the initial
[43:20] state of your environment. So it's a bunch of apps um and all their initial states. So past evals you've received
[43:27] your current calendar um events, message conversation with other personas in the
[43:33] in the universe. All this is simulated. Um and then on top of this we can inject
[43:39] events either from the user, the agent or again the environment. Um and then
[43:44] from all of this we can build uh tasks that we call scenarios because they're not a simple prompt like you would have
[43:50] in other uh frameworks in benchmarks. Uh but there are prompt that is the task
[43:57] sequence of events that we expect from the agent and events that might happen
[44:02] in the environment during this task. Um we want to be doing this in a simulation
[44:08] and not in the real world. Um so we can have reproducible um and observable
[44:13] evaluation like Avijit was asking for um where we
[44:18] can also test robustness um like we discussed earlier
[44:24] uh we want to be able to do this in a safe environment. So we want to take destructive actions. We want to ask the
[44:30] agent to remove all my evals, cancel calendar events. Um so we don't want to
[44:35] test this on the open web. Um and we want it to be cheap. So it's reproducible again. So don't want to
[44:42] depend on external bandwidths and APIs. Um so GIA 2 was built on AR. Um we
[44:51] published a benchmark with a thousand scenarios. Um over 10 different
[44:56] universes and [snorts] all of them use around 11 apps. Um all these apps all
[45:03] are within all these 11 apps are in the 10 universes. Um each universe was
[45:08] automatically generated from a database of personas um in a hierarchical way um
[45:15] using an LLM to generate conversations, evals, calendar um data to set up the
[45:21] initial state of our environment and then we add um human annotators create tasks and events um scenarios on top of
[45:30] this. Um GAIA 2 is uh split in five different
[45:36] capabilities. Um the first one is execution which um is when you ask your
[45:43] agent to do a task that require a bunch of tool calls um that will change the
[45:49] environment. So cancel all my meetings um respond to
[45:54] that eval. So the agent has to take a bunch of ris of actions but will do this within one turn of the of the agent.
[46:04] um search which is very similar to the first GAIA um benchmark but this one
[46:09] instead of testing search on the open web um tests search within our set of
[46:14] apps so within our universe um and the agent has to find the information across
[46:20] different API surfaces and not just keyword searches. [snorts] So a good
[46:26] example here is um I forgot my Netflix password but I remember sharing it with my parents. app, can you retrieve it?
[46:34] The agent has to figure out who your parents are um and search in a bunch of communication apps for messages that
[46:41] might contain this Netflix password and return the password. Um [clears throat] the next one is
[46:47] adaptability which is um in a way an ext an extension to the execution
[46:53] capability. Um in adaptability you have multiple turns. So the agent takes some
[46:58] actions in the first turn uh but the environment messes up at some point with
[47:03] this action. So maybe it has booked a bunch of uh meetings but the other
[47:09] attendees cancel this meeting. So the agent has to react to this um and adapt to the the environment changing and
[47:17] reschedule or take new actions based on that. Um the next one is time which is similar
[47:24] to adaptability but instead of adapting to events of the environment coming after its action um the events come
[47:31] based on time. So you can think of you know asking the agent to book a flight
[47:37] when it's under a particular uh price. So you have to wait for the flight price
[47:42] to lower in the in the flight app um and
[47:47] react to to timely events like this. Um time is interesting because
[47:53] when we run the evaluation benchmark and we have a scenario that has events
[47:58] happening over two or 3 weeks, we don't want to wait for 3 weeks for um that
[48:04] task to be performed. So we have to simulate the time fast forward or jump
[48:09] in time in the simulation and make the agent aware of this as if it was in the real world.
[48:16] Um and finally we have ambiguity um which I think have been talked about from the original GAA um where we have
[48:25] tasks which are ambiguous. So the agent cannot resolve the task without asking
[48:30] follow-up questions to the user. Um so it's going to start doing search doing actions on the environments and then
[48:36] figure out it has to stop and ask the user before doing something wrong.
[48:42] Um [cough] and to do stress testing and robustness testing like Arvin was
[48:48] suggesting um we have a way to in introduce noise into the simulation. Um
[48:54] so we can introduce tool failures on all the apps um in different forms. Um we
[49:00] can uh vary the the API of the apps. So
[49:05] change the names and the API signatures of all the tools so that we can make sure the agent is not overfeitting over
[49:13] um some specific signatures. And we can introduce what we call the environment
[49:19] noise which sorry lets us introduce external events in the simulation that
[49:25] are not related to the task but will add extra noise um to the input to the
[49:30] context. So we can check that the agent is robus to actual real world um noise
[49:37] happening. Um and finally another implementation is agent to agent um
[49:42] where the agent instead of being able to directly call the tool has to talk to a sub agent with natural language um and
[49:50] the sub agent is the expert that will be able to call the tool. So this test uh being able to solve a task without any
[49:56] tools just talking to to sub aents. So GAIA 2 is quite different from GAIA
[50:03] version one. Um it's not limited to web browsing anymore. It's on a bunch of
[50:08] apps. It's dynamic with real-time events. [cough] Um it's [clears throat] not read only anymore. Um it requires a
[50:16] lot of write actions. Um and we can do verification at the action level. Um and
[50:23] the way we do verification is we moved away from rubric judging which was very
[50:29] dependent on LLMs and their capability um and very [clears throat] expensive in a way to even verification.
[50:38] Um so if you think of a diag of events like I showed in some of the scenarios earlier um we have annotations for each
[50:46] scenarios of the expected set of actions of right actions we want the um the
[50:51] agent to take and we can compare this expected DA of actions to the actual DAG
[50:58] of action the agent took during the evaluation um and check event to event that they happened in the right order um
[51:05] and they happened with the correct uh parameters [cough and clears throat] [laughter]
[51:10] and we [snorts] do this thanks to a hard verifier. So this is a lot cheaper than
[51:16] calling an LLM and a a lot more reliable to reproduce results because there's a
[51:22] lot of parameters to the tool calls like did I send it to the right eval? Did I did the agent send it at the right time
[51:28] that we can check with pure equality or simple algorithmic uh code. Um and then
[51:35] we have soft verifiers. So if the eval if the agent has to send an eval um we
[51:40] can use an LM to check that the content of the eval generated by the agent is the one that we expected. It doesn't
[51:47] have to match entirely. We can use the LLM language capabilities for that.
[51:53] Um the key findings we published last year. So this table is a bit outdated. [cough] Um but
[51:59] [clears throat and snorts] we can see a lot of agents um and models already performed quite well in search and
[52:06] execution but time they are terrible they are around 0% all of them um even
[52:12] the top models um adaptability so adapting to the environment changing
[52:17] during the action they're not super good either and ambiguity also um what we've
[52:23] seen is that these numbers change very quickly with um new models coming out so
[52:29] often. Um, so we need to adjust and make tasks more complicated. But with the
[52:35] framework, it's easy to to add more turns and more expectations to to the scenarios. Um, we also need to adjust
[52:42] how the judges work um for comparing events because we see that the style um
[52:48] that we expected from models last year is actually very different from the output style of model this year.
[52:56] So yeah, this is um two things we've open sourced last year. Um there's a paper coming up at ICLR this year. Um
[53:05] the AR framework lets you write um new scenarios, new task and even new apps.
[53:10] So you can create your own benchmark on top of this framework. Um and you can
[53:16] use the GAIA 2 benchmark which was um human annotated and curated um for for
[53:22] creating uh good results. Thank you.
[53:29] [snorts] Great. Thanks for that, Pierre. That was another great presentation. Um, one
[53:34] question that came to my mind and and maybe it's because of my bias of working on um environments, RL environments. Um,
[53:44] the question is what does like reward hacking or or what does hacking GIA from
[53:49] an agent look like? Like how would they do that? um how did you anticipate that
[53:54] they would do that and kind of what did you build into GAIA to prevent them kind of hacking the the environment?
[54:02] Mhm. Um so in GAIA 2 um the the way we
[54:07] do this is we have a quite strict checkers. So um in the way we check the
[54:13] the results um we make sure we don't see hacking patterns in there. Um and also
[54:19] we can increase noise um if we want. So we can make sure uh the agents don't
[54:25] overfitit and and and guess what the tools look like or should do. Uh because
[54:31] we can increase failure rates and change the signatures of the tools while keeping the same tasks.
[54:40] Okay, cool. Um thanks for that. I'm going to move on to Mahesh now.
[54:47] Cool. Great. Mahesh, there's your slide. So you're ready to go. Yes. Um, thank you Ben for the
[54:54] invitation and uh lots of great talks so far and I feel like uh you guys have
[54:59] done excellent job of setting up the stage for me to talk about uh environments and why environments are
[55:05] actually critical to uh do evaluations and uh my name is Mahesh uh I'm
[55:11] co-founder and CEO at Bespoke Labs and for those who don't know Bespoke Labs is
[55:16] like an AI applied AI research lab that focuses a lot on doing research as well
[55:22] as shipping RL environments and so we have a lot of experience working on environments uh thinking about how to
[55:29] build them as well as how to use them for evaluations and also previously we
[55:34] uh we we uh um created open thoughts and worked on it. It was a community effort.
[55:40] It's one of the best open reasoning data sets uh that we did uh last year. So
[55:46] with that I want to kind of dive into environments but before that I want to introduce here hiccup uh whose uh you
[55:55] know goal in life is to train his dragon toothless and he tries for a while but
[56:01] that real transition happens when he actually starts to observe his dragon and truly understands it. I feel that's
[56:08] a great metaphor for us also where lot of us are either training I when I say
[56:13] train some of us are you know uh post- training agents using SFTDRL but also
[56:19] just building agents out right so um and I' and also we speak to a lot to
[56:26] different enterprises where they are starting to or setting things up but one
[56:32] of the things that happens is like they don't u you know have this uh eval first
[56:37] mentality. So that's kind of what I'm uh kind of advocating for is like you first
[56:43] start to understand and in our parlance evaluate your agents and get the setup
[56:49] done, get the metrics uh defined and then you start improving your uh agents,
[56:54] right? So I want to kind of uh keep this talk simple where I I will first talk
[57:00] about you know how not to evaluate and why agent evals are hard and in fact some of this I feel like has been
[57:06] covered in the previous set of slides and um after there's two main things I
[57:13] want to say okay how do we set things up especially around environments and then what what what do we evaluate how do we
[57:19] evaluate so that's kind of going to be uh what I will uh be talking work. So
[57:25] how not to evaluate uh you know why be val right side right side right side right side right side right side right side right side right side right side so a lot of times uh what's happening is
[57:31] like people build agents again this talk is a bit more on the practical side uh where people are deploying agents so as
[57:39] I was saying previously people you know um are looking at what's happening to the output a bit more on the web side it
[57:46] just is it's fine for easier or smaller agents but quickly you run into issues
[57:52] where you change something and you you kind of don't figure you don't understand what has failed or you don't
[57:58] catch them on time. Right? So this is again a lot of this stuff has been standard for uh software engineering
[58:04] where we have to write all these unit tests, regression tests and whatnot. So some of that I feel we should be uh
[58:11] incorporating or sometimes the other thing uh that happens is like there is a incorrect initial level of focus where
[58:18] people are starting to actually initially like identify oh here is my
[58:24] agent where there's a planner okay is this doing the right thing that that that's something that you have to do
[58:30] eventually but that's not where you kind of start uh or thinking into too many of
[58:35] these granular details about okay is this the right function call to be done and things like that. Um and of course
[58:42] one of the traps to watch out and avoid is to deploy to production and evaluate which again happens a lot. Um
[58:51] and briefly I want to talk about why agents u evaluations are hard because
[58:57] agents are very much stoastic like two different runs can produce very different results. uh which you know I
[59:04] think uh Arvind was also talking about consistency um many steps to get to the progress to
[59:10] to get to the final outcome right so that also introduces lot of complexity
[59:15] uh the other important thing is that it agents can interact with real world and
[59:20] tools the world underneath can change so you your agent can do something which
[59:26] you know um can change the world so that can make evaluations hard and not so
[59:32] reproducible and also sometimes real world interactions can be expensive. You don't want to delete all your data or
[59:39] you don't want to send incorrect messages to your uh user.
[59:44] And so let's get into how do we set things up for evaluations. I'm going to kind of talk about this in a bit of okay
[59:52] different levels of complexity. So level zero is like thinking about
[59:58] verifiable setups, right? Soam easy example here is like coding agents where
[1:00:05] is the agent actually uh fixing the bug or not? Did the unit test pass? So things are a lot more verifiable. Uh
[1:00:13] maybe in the context of math you can check if the you know value is correct or not. So th this is kind of the first
[1:00:21] set of things that you can think of about is like okay is the final answer correct or not in in the in the case of
[1:00:28] verifiable domains and even here there are some gotchas for example u you know
[1:00:35] if you are building a coding agent if you have a number of unit tests do do you give equal weightage to all the
[1:00:42] tests for example many unit tests could be pretty simple and there could be some
[1:00:47] important tests which uh that may be few in number and you may think okay most of
[1:00:53] the tests are passing but you know ultimately the agent is still not getting the real work done right so so
[1:01:00] thinking about some of this and then reward hacking is uh uh something that
[1:01:06] can happen for example we see agent goes and uh makes instead of fixing the bug
[1:01:12] it just fixes the unit test so that just they artificially pass right So things
[1:01:17] like that are something to watch out for. Uh and then the other level to it
[1:01:24] is like when you have cases where the output is not verifiable. So as an
[1:01:29] example, you are trying to build a deeper search agent and the output is a paragraph or few pages in length. How do
[1:01:37] you even evaluate it? There is no single right or wrong answer. So rubrics kind
[1:01:42] of come to the rescue there, right? So what you can do is you can define various rubrics to evaluate whether the
[1:01:50] um outcome looks reasonable. Um and and in fact what happens in many situations
[1:01:56] is like you define a bunch of tasks u or or questions that you you you define
[1:02:03] them and then you can also write corresponding rubrics for them. So here is an example where somebody uh there is
[1:02:11] a question around uh I think kidney stone and you can define a bunch of rubrics around the correctness of the
[1:02:17] answer accuracy and and there are more here that you can define along with that you can also define some numbers. The
[1:02:25] critical point, the main point here is that you have your question and you are able to use this with LLM as a judge get
[1:02:33] get this each of these can be zero and one right and then you are applying uh weights and ultimately you end up with a
[1:02:40] score. So this gives you a nice nice methodology where you have your
[1:02:45] questions and you get a final answer and you are either updating the uh you know agent harnessers or you are changing the
[1:02:52] model or whatever and then you are able to measure and see whether the uh number
[1:02:58] is going up or not. Right? So that that is level one of thinking um going from
[1:03:04] verifiable to non-verifiable. And the other thing now uh I I want to kind of
[1:03:09] talk about is the concept of this environment. Uh again we have talked about this uh before in the previous
[1:03:16] slides um uh pre previous talks here but what's essentially happening is the
[1:03:22] agent gets a task and it interacts with an environment and and it produces an
[1:03:28] output or sometimes the output is like underneath the environment right so like for example code was the the bug was
[1:03:35] fixed um and and you you have to have a grader which is checking whether the
[1:03:40] output whether whether the agent did the right thing or not. So, as I was saying previously, this grader can be unit
[1:03:47] tests. Did they pass or not? Um or or you can have a bunch of rubrics to
[1:03:52] measure whether the output looks uh you know reasonable, right? And then here I
[1:03:59] have these two arrows where the agent is interacting with the environment. So, this is kind of also uh um stuff around
[1:04:08] how the harness behaves, right? So what are the what's the set of uh uh how is
[1:04:14] the agent planning things and so on. So so this is u the the high level of how
[1:04:20] things can be thought about when defining these agents u uh defining
[1:04:25] environments and isolating and creating an environment is actually very useful
[1:04:32] because it can help you do repeatable and reproducible evaluations and also
[1:04:38] it's isolated and safe. So one of the things again I want to mention is this environment could actually be real world
[1:04:44] or you can kind of encapsulate into a sandbox. So that's uh actually the
[1:04:50] definition we are going for here when I when we say environment is like a sandbox. So um let me actually move to
[1:04:58] the next slide. There are a bunch of uh formats here to define your environment.
[1:05:03] So basically it has to at the end of the day what it is it's a sandbox uh uh
[1:05:09] which is containing the required dependencies required you know state of
[1:05:15] the world required tools um and and and uh data and so on and uh harbor is one
[1:05:23] of the popular uh formats. There is also open end um and uh uh the the
[1:05:31] along with the environment you have these uh tasks that are defined and then ways of grading right so uh it's it's
[1:05:38] yeah grading so some of the key design decisions when
[1:05:44] when it comes to using environments for evaluations is maybe you have one or
[1:05:49] more environments right so maybe you are trying to evaluate uh um um agent for
[1:05:56] the legal domain. So you can have different environments where they they all have different data and again
[1:06:02] associated with all of them there can be uh tasks right and you want to make
[1:06:08] these environments as similar to production as possible. And the other thing to kind of take care of which
[1:06:14] harbor uh at least you know um uh gives this natively is the agent should not
[1:06:20] have access to the grader or the solution otherwise it can reward hack.
[1:06:25] And the other thing to think through is like what are the tasks that you are defining uh for what the agents are
[1:06:31] going to try and do right again as much as possible having something similar to
[1:06:36] what you get in production. Um and and sometimes you can keep it very well defined open-ended and whatnot. And
[1:06:44] grader is uh as we were talking about it can be a way of verifiably uh grading
[1:06:50] things or uh there can be rubrics uh which convert the non-verifiable to in
[1:06:57] some sense the verifiable uh numbers and lot of thought has to be given uh to
[1:07:03] make sure you are kind of actually grading for the right thing for the right outcome and also making sure
[1:07:10] everything you asked for in the task is graded otherwise is it can uh you know
[1:07:15] cost reward hacking for example um um if you have asked for three different
[1:07:21] things but you're grading only two things the agent can see that oh um I I don't need to work on the third thing
[1:07:28] right so things like that uh which connects back to reward hacking where you you want to kind of you know as an
[1:07:35] example add fingerprint to unit test to make sure the agent doesn't muck around
[1:07:40] uh unit tests so this is kind of talking about how to set things up for
[1:07:45] evaluation. So thinking about the rubrics and thinking about setting up the environments. Now what do you
[1:07:51] actually measure? There are many many numbers uh many many different things but u in fact Arvin was
[1:07:58] talking about some of these but you know um some of the primary metrics is you
[1:08:05] can start with something like success rate where given again the agent given
[1:08:11] the environment given a task you try end rollouts try the let the agent uh you
[1:08:17] know attempt the task end times and then you measure the success rate how how often did it succeed So the grading you
[1:08:24] you just uh get an average uh of the grades from for all these rollouts or
[1:08:31] you can also measure something called pass at K. This is um you know basically
[1:08:37] of the K rollouts at least one did at least one succeed and if you have many many tasks then you can kind of get a um
[1:08:44] sense of the average pass at K. Now once you have these metrics I I'm kind of
[1:08:50] showing this as an example where you can now compare and contrast different
[1:08:55] models or even different harnesses to see okay what's happening with passet K
[1:09:00] what's happening with success rate across these uh models. This is a very specific example we had uh for a
[1:09:07] specific domain where you can see how the different models are uh you know
[1:09:13] performing differently and of course there are many other in
[1:09:18] addition to like thinking about the success alone there are many other uh things right so as an example efficiency
[1:09:25] like how many steps did it take to uh get to the final outcome it could have
[1:09:32] succeeded or failed but it could have taken like know um hundreds of steps to get there. So kind of getting a sense of
[1:09:38] that. Uh very related is the token count. How how much tokens uh how many tokens are getting used latency like how
[1:09:47] long did it take to get the uh u answer and also cost. Cost matters right. So as
[1:09:53] we are getting into you know uh the models are expensive but also we are
[1:09:59] using this uh in many different situations and the rollouts are also expensive.
[1:10:04] So these are some of the factors but there can be many others that depend on that that is that are specific to your
[1:10:11] uh application or your domain right and not not to um ignore there are many
[1:10:18] other factors as well. For example you want to also understand the role of harness. So given a agent the if you put
[1:10:25] it in different harness it can actually the success rate can actually drastically vary. So as an example if
[1:10:31] you go to terminal bench dashboard you can see that the same model on different harnesses has different uh metrics right
[1:10:39] and safety is another u interesting aspect to uh verify. This is in fact a
[1:10:45] article from today. um you know you you want to make sure your agent didn't delete all the data or is not using your
[1:10:52] credit card uh you know and maxing out on it. So you can kind of this is why
[1:10:58] it's also useful to uh you know encapsulate things in an environment and
[1:11:04] then you can also maybe incorporate some of these as tasks uh and and the graders
[1:11:10] for example you can have a specific grade or you basically you can penalize the model if it deletes uh data right
[1:11:18] and again reward hacking we we see this often so this is something to kind of
[1:11:23] think about and try to incorporate as much as possible. when you're getting the when you're setting up your
[1:11:29] evaluations to make sure the agents are um you know not taking shortcuts.
[1:11:37] Um the other thing to do is uh looking at the traces. So this is kind of the
[1:11:43] flow of things right. So you start with the success metrics and all these other um additional metrics and then you also
[1:11:50] kind of want to read your traces to some extent and and and that gives you a sense of how the agent is behaving
[1:11:58] and also in addition to that you can do a lot of automated and deeper analysis. For example uh it can surface you lots
[1:12:07] of interesting um you know um uh insights. So maybe the agent is
[1:12:13] generally good but when you when you dig deeper you see that oh in this specific
[1:12:18] uh kind of scenarios the success rate drops right things like that is very useful when you uh you you can basically
[1:12:25] do lots of these u you know automated failure analysis on the trajectories as
[1:12:31] well and then uh uh going forward uh what what I'm kind of trying to tell here is
[1:12:38] in order to do these uh evaluations Think about uh being in environment
[1:12:43] first. So think about how to set up the environment where you can do these evaluations.
[1:12:49] Uh think about what the tasks are going to be. Think about how to grade these things properly. So these are three
[1:12:56] specific things you can kind of incorporate and think about. Um and and
[1:13:01] uh uh and also of course the harness. And it's not just for evaluations, but you
[1:13:07] can once you have this nailed down, you can run something like the Japa algorithm or other ways of optimizing
[1:13:14] these agents so that you can get a better sense of how to improve these agents given these environments, right?
[1:13:21] So you do that you you measure the improvements on your system and then you
[1:13:26] can deploy to production and not to mention there are many new challenges like long horizon, right? So this is a
[1:13:33] general issue like when when the tasks are taking like many many hours maybe even days to finish how do you do these
[1:13:40] evaluations it gets quite you know obviously it takes a while for us to wait and get these uh response but also
[1:13:48] it's uh expensive um how do we think about multi- aent systems or multi-users or you know
[1:13:56] things like that um and then yeah I think the main point here is you want to you know just like
[1:14:03] uh what hiccup was doing you want to observe understand and evaluate your agent before you actually start you know
[1:14:10] train or build it. So I think with that I I conclude my talk.
[1:14:16] Great. Thanks Mahesh. That was a really practical talk which I think will be uh useful to to people listening. One thing
[1:14:23] that came to my mind over the last few months we've started to see more environments land on the hugging face
[1:14:29] hub right um in openend format but also some in harbor terminal benches on the
[1:14:35] hub now. And um so you see a lot of people building environments for for
[1:14:40] training and for evaluation but but also for um for production or or for usage,
[1:14:45] right? And so the question came up during your talk is h how do you make or
[1:14:51] in kind of general terms like how would one make a real world environment,
[1:14:56] right? So you have this um training environment where you obviously don't have a an active Slack channel running,
[1:15:04] right? So, so what what does that look like in in kind of simple terms if I wanted to push like a a Slack
[1:15:10] environment to the hub or or a startup environment where I have like a Slack and and a GitHub and other kind of
[1:15:16] things like how how do I create that real world environment for for these training for training and evaluation?
[1:15:23] Yeah, that's a great question. So, this is where the SIM to real gap comes in, right? So
[1:15:29] all these environments uh we we want to build them so that they are isolated sandboxes but but then the real world is
[1:15:37] lot more complex. It's a it's a challenge. uh what what ends up happening is you kind of try to u there
[1:15:45] are lots of uh you you can basically also wipe code some of these things and
[1:15:51] uh maybe if you have slack you kind of wipe code slack uh and then incorporate
[1:15:56] as many relevant stuff as is needed for your real world into these uh uh
[1:16:02] environments. So yeah that there is like this uh game of how do we make the
[1:16:08] environment as realistic as possible so that it mimics the um real world. So
[1:16:16] cool. Okay. Thanks for answering that question. We'll now go over to Nathan. You can come right up and I get your
[1:16:22] slides ready. Thanks Mahesh.
[1:16:28] Everything is good. Everyone can hear me I think. Yeah perfectly. Yeah,
[1:16:34] sure. Well, thanks Ben for the introduction on this and
[1:16:39] welcome everyone to the last talk of this agentic evaluation workshop. I'm
[1:16:45] Nathan an ML engineer at Hugging Face and the co- maintainer of lighteval the
[1:16:50] open LLM leaderboard and community eval as of very recently
[1:16:55] uh which is what we're going to talk about today. So the subject of this talk
[1:17:00] is going to be defining living benchmarks with community-eval
[1:17:08] like maintaining the Open LLM Leaderboard like back in the days led us to
[1:17:13] introducing this new feature on the hub and how you can use it to share your
[1:17:19] benchmark, make it a living benchmark, how to get the community involved and basically how to maintain your uh uh
[1:17:27] benchmark like through time. So let's start by the state of eval 2026
[1:17:34] and as a like for the first talk very well said like it was a very nice
[1:17:40] introduction to my talk. There is quite a few issues with evaluation now. So one
[1:17:47] of them being like scar fragmentation. So different sources usually report very
[1:17:53] different results. So what you see like for example every time there's a new model coming out you look at the
[1:18:00] evaluation page evaluation results and you see they evaluated a bunch of models
[1:18:06] but it does not match previous reported scores on those models and
[1:18:12] probably the next release is not going to match it either. So we've been thinking on how to solve this. There is
[1:18:19] also a maintenance burden. So I maintained a few leaderboards and I
[1:18:25] can tell you and I'm I'm probably sure a lot of you listening have tried to maintain leaderboard. It is quite
[1:18:31] painful to maintain especially if you try to update it manually and it's also quite painful to maintain
[1:18:39] um what is it called like evaluation frameworks that you use for your benchmarks. uh especially if you're
[1:18:45] doing custom evaluation frameworks for your benchmark specifically, it can be a bit hard and a pain to maintain.
[1:18:54] There is also right now not really a single source of truth even though a few labs are trying to evaluate as many
[1:19:02] models as they can and as to and to present themselves as the one source of
[1:19:08] unbiased evaluation. It's still not really working and I feel like we need a
[1:19:13] lot more of community involvement in the eval space. What does it mean is that we
[1:19:18] can get truth in numbers by making the community more involved and evaluating
[1:19:24] uh models and building benchmarks with a greater number of people where each
[1:19:31] people is going to be able to say with with my agent uh with this agent
[1:19:36] framework that I just did that I just vibe coded for example this is the result and with a few people like a lot
[1:19:44] of people doing this we maybe get uh closer to an actual evaluation space.
[1:19:50] Obviously with all the um what do we say how do you say all the um
[1:19:58] specificity that JJ talked about in his talk. Also last one benchmarks right now
[1:20:04] are kind of scattered sorry across like repos on GitHub making it quite hard to find and when you find it how to run it
[1:20:11] on your custom model uh if you have like any any custom evaluation task for
[1:20:17] example. So that's what okay that's what we are trying to solve with what we call
[1:20:22] community evolves on the hub. So community evolves is basically hiding
[1:20:29] face data sets that you can turn into benchmarks. So here's a a screenshot.
[1:20:34] For example, we have as of now 13 benchmarks on the hub like this uh going
[1:20:39] from OCR bench, JSMK, uh MTBench, uh not MTBench, sorry, MTB,
[1:20:48] uh Sweet Bench Pro and SWEBench verified as well as the math arena folks with AM
[1:20:54] 2026 and uh more of interest of you guys for agentic evaluation. We have terminal
[1:21:01] bench from the harbor framework. Uh folks,
[1:21:07] how do we think community eval are going to fix our issue into the evaluation space? Well, first of all, it's
[1:21:12] decentralized, which means that uh every data set on the hub has um way an eval
[1:21:20] yamo file that makes it very easy to run for everyone. And all the data is
[1:21:26] public, even though gated, but we'll get into this later. And every results and
[1:21:32] leaderboard, every results that's going to show up in the leaderboard is and can
[1:21:38] be opened by a community member. And we'll get into this later. So the
[1:21:44] decentralized aspect is very important for us. It's also very easy access. It's basically just a hinged leaderboard. So
[1:21:50] again very easy to find and it's community first. As I said everyone currents
[1:21:57] uh and it displays the leaderboards on the data set display any sources.
[1:22:02] As an example here we have HLE which stands for humanity last exam that you
[1:22:08] guys might be familiar with. It's by the center of AIT that we talked about in the previous talk. And now you can see
[1:22:15] it's a data set page, but there is a leaderboard. And the leaderboard displays results for open source models.
[1:22:23] And you can see the scores for each of them with a little note that I can't access now, but which a little note
[1:22:29] about how the model was run, what agent was used for this model, etc. For
[1:22:34] example, if it's five shot, two shots, no shots and all
[1:22:40] like anything that could be of use to specify how the model was run can be can
[1:22:46] be added to the result. Now let's go into like how do we define
[1:22:53] this evaluation humanity sorry last exam on the hub. So as I said we have an eval
[1:23:00] yaml sorry that defines the name of the task a small description and most
[1:23:06] importantly an evaluation framework here we use inspect AI for hle and then for
[1:23:13] each task in the benchmark because humanity's last exam is the benchmark and defines possibly multiple task here
[1:23:21] there's only one where the ID is hle and you have a field spec that's not really
[1:23:27] like we won't go into details from it. But here in the same files we have also
[1:23:33] solvers uh that just here define like how am I going to prompt my model? How I
[1:23:39] going am I going to build a framework and a scaffolding
[1:23:44] around my model. So here it's a very simple system message and a generate call to the model. But it can be uh way
[1:23:53] more complex than this for you can do very big agentic evaluation uh using
[1:23:58] this file uh especially using inspect AI. Then you have your scorer which basically just is
[1:24:06] how am I grading the model answer and here is the model graded fact. It's basically just LLM as a judge using 03
[1:24:13] mini from OpenAI as the judge.
[1:24:18] The evaluation framework that we use here is is inspect AI but it can be pretty much anything else uh on the hub
[1:24:26] and why is it important and why do we recommend using in existing sorry
[1:24:32] evaluation framework it's because we see quite a lot of evaluation of benchmarks
[1:24:38] sorry uh that redefineses their evaluation framework because it's quite easy to
[1:24:44] vibe code now I guess but it's quite It's first of all it's way harder to
[1:24:50] maintain your own like evaluation framework. Having done it myself there is a lot of you know very pecular issues
[1:24:58] that come with it. So using a existing one really reduces maintenance override. For example inspect AI as we'll see
[1:25:05] later once you define your re.l you have nothing to do like the the model code is
[1:25:10] going to take it get take care of the tooling is going to take care of too.
[1:25:16] The publishing of results is going to take care of basically the only thing you want when you're defining an evaluation agentic or LLM
[1:25:24] vanilla LLM is defining your evaluation. It makes your benchmark more accessible
[1:25:31] because if one or just a few evaluation framework are defining pretty much every
[1:25:36] benchmarks then it's very easy to jump from one to it to to the other and it's standardized tooling and separate
[1:25:43] benchmark as I said from your evaluation logic.
[1:25:49] Now that you've done this how do you actually run the benchmark that you've defined agentic or not? You can use
[1:25:56] obviously what we did for the open LLM leaderboard back in the days is that we had a local cluster and it's fine but
[1:26:03] it's quite hard to maintain and you have to take care of like GPU GPU usage and
[1:26:11] all of this when there is more than only your team on the on the cluster and
[1:26:16] usually just a local just one GPU or local small cluster is not going to cut
[1:26:21] it for bigger models. You can use also cloud compute uh any cloud compute that you have that is available for you. Uh
[1:26:29] but recently more in like what we wish we had for for example the openm
[1:26:35] leaderboard is HF jobs. HF jobs basically you can just um it's cloud
[1:26:42] compute but like you can ask what hardware do you want and it can it is
[1:26:47] very reproducible and it's a oneliner to run your evaluation. So these are your
[1:26:54] option. But another option that I see a lot of people using and I don't really
[1:26:59] uh like we are quite against using it I
[1:27:05] guess but it's inference providers of any sort because what we saw when evaluating a lot of models with
[1:27:11] evaluation with inference providers is that in reality you are evaluating the
[1:27:16] provider which can be a good thing but maybe not what you want and you're not
[1:27:22] ev evaluating the model. What this mean is that
[1:27:27] uh inference provider usually you don't know how the model is called in the back end. You don't know if it's prompt in
[1:27:34] exactly the way you want it to be prompt and this can cause a lot of issue. First of all, it's not reproducible.
[1:27:40] You don't really know what's happening with the model. So we would say that to you need to use local inference or at
[1:27:46] least control environments like HF jobs. Once you defined your model with uh on
[1:27:54] the hub, it's very simple to run it using here inspect AI. So you just use
[1:27:59] UV here UVX for tooling. So you use UV call inspect AI. Um
[1:28:06] say that the the benchmark is from HF. Give it the benchmark.
[1:28:12] Give it your model here. It's going to use OpenAI GPOSS 20B running with VLM.
[1:28:18] So this oneliner you can just use HF jobs to run it and it's going to run and
[1:28:24] publish your results. How does it publish the results? Uh it
[1:28:29] creates here it's HF space but it can be a website it can be anything. It's very easy to publish. It's going to create
[1:28:36] logs very detailed logs about what temperature was used how the model was
[1:28:41] how VLM server was spin up how many tries. If you use the metric for example
[1:28:46] pass K it's going to be detailed also here. It's also computing the standard
[1:28:52] error of the evaluation and you have pretty much all the metrics
[1:28:57] that you needed and we talked about in previous talks how important it was to have very like detailed logging during
[1:29:05] your evaluation just to be able to share it. And when you are building your model, you also want detailed logging to
[1:29:11] be able to build on top of it to get better results. After this,
[1:29:18] um, here we also saw, it's not a very good screenshot, sorry, but it's a PR in
[1:29:24] model uh repository and it's this PR that is
[1:29:30] going to be used to display on the leaderboard. So once you've done your evaluation result your evaluation run
[1:29:37] how do you share results dynamically and to make a live leaderboard is that you simply have to open a PR on the model
[1:29:45] repository on face and it's automatically going to show up with all all the info that you want on the
[1:29:51] leaderboard data set on the data set leaderboard sorry
[1:29:57] talking about the leaderboard so as I said it's something that auto updates
[1:30:02] which is great. Like when we are running the OpenLM leaderboard, we had quite a few of issues with with pipelines. It
[1:30:09] breaks it. It used to breaks like quite a lot. And uh now the leaderboards live
[1:30:16] directly on your data set page. You have nothing to do, no infra to set up, nothing. And yeah, it shows latest
[1:30:23] results in real time. And it's very easy easy to share with the community. And also on it because each result is a PR
[1:30:30] the community can discuss it on the PR itself. If for example it does not agree
[1:30:35] with one of the results if one of the results seem a bit low or a bit high it
[1:30:40] can just discuss it in the PR. Uh as I said community engagement for
[1:30:47] the for the leaderboard not the leaderboard the evaluation and benchmarking is very important.
[1:30:54] Oh yeah, and also I forgot to say that model author can close or hide uh disputed scores like scores that they do
[1:31:01] not agree with. They can discuss it and if it's really bad like you can hide the the result obviously
[1:31:09] and uh yes that was it for presenting the the community eval feature. I was I
[1:31:16] wanted to do a small demo but uh I can't share my screen unfortunately. So yeah,
[1:31:22] thank you. Cool. Thanks, Nathan. Thanks for sharing that feature that we've been building over the last few months.
[1:31:27] That's really useful. A quick question that came to my mind. um was that if I
[1:31:34] like let's say I'm evaluating uh models that I'm using not not
[1:31:40] exhaustively and maybe in some ways I am evaluating the provider like I'm using
[1:31:45] one or two models and I'm evaluating across providers and maybe quantizations
[1:31:50] and and I have these results and and they're important to like me or or my domain or or my language or something
[1:31:56] like that and I want to get them out into the community like like what would
[1:32:02] that look like? Like h how would I do that basically? Uh sure. I mean that's a great question.
[1:32:08] The the what would look like is that you would probably want to sort the results in a certain way. So to have a
[1:32:15] leaderboard and if you build your evaluation, you probably have a data set
[1:32:20] on a on hugging face to be able to run your evaluations. And so the way you would do it is that you could just
[1:32:27] define your data set as a benchmark your models. You're going to just open a
[1:32:33] PR with the results on uh the model repo. It's going to show up and then when people want to see your evaluation
[1:32:40] results and you want to share your leaderboard, you can just share the data set page.
[1:32:47] Cool. And I guess from that the advantage is then other people could go and and evaluate like other models that
[1:32:53] I hadn't I hadn't got around to. Absolutely. It makes it super open to see like blind spot to evaluate on your
[1:33:00] model specifically. It makes it makes it very community based. Cool. Okay. With that, thanks Nathan.
[1:33:07] That was really cool. I'm now going to bring uh everyone else back on and we're going to have a kind of short panel uh
[1:33:14] just to close. Uh yeah. So, so thanks again everyone for your for your talks. Uh in my
[1:33:21] opinion that that was really cool like that was really wellrounded and uh and it was amazing. So yeah, once again
[1:33:28] thanks. I prepared a few sort of questions, but maybe if I do like a
[1:33:33] quick round table and and someone can just kind of mention any any sort of topic that was of particular interest to
[1:33:40] them and and any kind of like quick takeaway that they had from it or um it doesn't necessarily need to be super
[1:33:47] articulated, but just a kind of yeah short takeaway. Uh maybe uh Abashit.
[1:33:57] Um I mean I think I think what I'm realizing from this entire discussion is
[1:34:03] we still don't know what we don't know. Like I would say if you had asked me last year what I think about agents I
[1:34:11] would say that oh agents um agents are just with tools and we don't need to
[1:34:17] build further scaffolding. We can just move on with our lives. uh access to tools and so on. But then people are
[1:34:23] doing so many more interesting cool things um with agents especially the human behavior aspect of it like I as a
[1:34:31] person would not probably give an agent access to my entire computer and and
[1:34:36] allow it to delete my WhatsApp messages but then somebody working in machine learning safety at a big company
[1:34:42] apparently think that's okay. So when we add that additional real life noise to
[1:34:48] agentic evaluations, I think the error landscape uh meaningfully changes and
[1:34:54] I'll be curious to see what comes up in the following year. Cool. Thank you. Um Pierre.
[1:35:04] Yeah, I think like JJ said, there's a lot of things we need to evaluate for
[1:35:10] agents which are not just like tokens in tokens out, right? there's a lot of higher level behaviors
[1:35:17] um we want to evaluate and a lot of this doesn't just go through one score as I
[1:35:23] think I have been saying like it's good to collect robustness and all the things um there's all a lot of safety evolves
[1:35:30] to do on agents like if you give it access to a lot of stuff like how how are you sure it's going to do the right
[1:35:37] thing how do you know it's not open to um prompt injection and this kind of
[1:35:43] things. Um, and one thing we've we're seeing now is with things like, uh, open
[1:35:49] code that people just drop in Telegram conversations is, um, a lot of current
[1:35:55] devolves are just one user, one agent. Um, and then, you know, in GAIA 2, we
[1:36:02] have some environment stuff happening. But what happens when you have multiple actors like how do you evaluate this? Um
[1:36:10] the the agent behavior who it's supposed to align with um like very complicated
[1:36:17] questions on behavior more than just token in token out again.
[1:36:24] Um Mahesh. Sure. Sure. Yeah. So I think the the the
[1:36:30] AR work and GIA 2 they are quite interesting. They kind of show us how to push the frontier on building these
[1:36:37] complex environments which are very useful to you know understand these frontier models frontier agents but how
[1:36:44] can we democratize something like that for enterprises right so they for
[1:36:50] example is is a complex environment which is very specific to some use cases but many many others are building agents
[1:36:57] for their use cases how can we build something like u so that they can start evaluating
[1:37:03] ating very safely on their uh you know enterprise setting right so things like that that that's I think we are just
[1:37:10] scratching the surface here of in fact you know building these environments building uh doing evaluations so I feel
[1:37:17] there is a lot of interesting work ahead of us
[1:37:22] cool and Nathan sure something that I I find very interesting
[1:37:29] and that actually came out like in almost every presentation today is long
[1:37:35] context uh long horizon sorry evaluation and I think that's one of the next
[1:37:41] challenge of Agentic AI and I found it's a very interesting subject especially
[1:37:46] right now like in the last for example week or two weeks a few benchmarks started coming out already for example
[1:37:53] you have Swissi which is like the next not the next but like the the
[1:37:59] the the followup to SW bench where it's going evaluate how the model does not
[1:38:05] only codes but like how does it maintain on the longer on the long run a code
[1:38:11] base and there is a few it's going to be very interesting to see how benchmarks adapt to longer horizon evaluation
[1:38:21] cool yeah so those are some really interesting takeaways I've kind of got some questions um yeah but based on
[1:38:27] those and also ones that came in uh in the chat one thing that I I think kind of came out of um Nathan's uh
[1:38:34] presentation, but maybe a question addressed to a is is there a like a
[1:38:40] tension between open open evaluations and and preventing benchmark gaming and
[1:38:46] and how do we implement that um within the community like how do we make open
[1:38:51] environments and open data sets but not just allow them to be gained basically.
[1:38:57] I think I think like disclosure plays a huge role. Like there are some common misconceptions that have not been
[1:39:02] verified. For instance, um most people you talk to will say benchmarks get
[1:39:07] saturated when they're public, but that has not been like massively tested. So at Eval, we had a or have a benchmark
[1:39:15] saturation paper. Um it's currently submitted to ICML. So we will talk about it more when the results are out. And we
[1:39:22] find that um whether a benchmark is public or or private or partially
[1:39:27] private does not have a strong correlation with how quickly the benchmark saturates.
[1:39:33] But on the flip side, when you don't have a public benchmark data set, um it allows for this lack of transparency and
[1:39:40] other people cannot verify what's going on. So even if you game something, if you were doing it in a way that is
[1:39:46] reproducible, other people could then check um whether you were doing that. Uh
[1:39:51] so that's why I'm like a big fan of disclosure. So public benchmarks um open
[1:39:57] standards and the bare minimum amount of information necessary for somebody else
[1:40:02] to validate your evaluation. Um those are things we are definitely
[1:40:08] cool. So yeah I mean does anyone else want to go into that just if you do um
[1:40:15] say otherwise I had a question. Oh go ahead. you know, [snorts] you can
[1:40:20] have open evaluations and check that they're game um only if you have access
[1:40:25] to the models, right? Like if if the models are closed, like even if they are evaluated on open evaluations, you don't
[1:40:32] know um how they were evaluated, right?
[1:40:37] Was it the same model that was run? Um so it's going to be very hard to check.
[1:40:46] Cool. So a question that I had for Mahesh was what's the so so thinking
[1:40:52] about closed and open environments really and and that we want open environments so that agents can perform
[1:40:59] well on on tasks and applications that we want to use but there's a kind of
[1:41:05] growing evaluation environments industry right like um and building specific
[1:41:11] environments for for labs and and these kinds of things. um what's the tension
[1:41:16] there and and how do we navigate that in the open source like like how do we get
[1:41:22] environments that we can use to evaluate models um yeah great great point I think uh
[1:41:32] this tension exists between even even for models right there is there are closed models always more more powerful
[1:41:39] than the open ones uh but of course the open you know open source community
[1:41:44] keeps uh surprising us. So uh we we did open thoughts which was the
[1:41:50] reasoning data and now there is actually open thoughts agents which is actually working on how do we create these
[1:41:57] environments in the open uh community. So that that work is going on. There are
[1:42:03] various ways of uh creating these that that we are kind of you know working on. So that is happening. Um but also you
[1:42:11] know there is I think the tension between closed versus open
[1:42:19] it's there but ultimately what also matters for many people in the enterprise is like okay are they able to
[1:42:25] build uh environments that are very suitable or very specific to their their
[1:42:32] internal use cases. Right. Right? So as long as we are able to
[1:42:37] work on methodologies and publish them and have good tooling, maybe it doesn't
[1:42:44] matter if the labs have access to very good environments and open source has uh
[1:42:49] you know not as many environments. But as long as there are these tooling that
[1:42:54] allows people to build their environments for their enterprises, then maybe that that that solves you know at
[1:43:00] least one part of the issue. Obviously researchers do want to have access to environments. The other interesting
[1:43:06] aspect is like the environments are typically calibrated to the models. So
[1:43:12] for uh very strong models you get to kind of build very complex environments.
[1:43:18] Um whereas for open models if they are not as strong you can kind of have some
[1:43:24] uh slightly uh weaker environments which are maybe still useful for doing
[1:43:29] research. Great. Yeah, I mean it it also made me think about OpenM and a number of the
[1:43:36] environments that have come out in for OpenM have been um like
[1:43:41] reimplementations and standardizations of of environments that were previously closed where like the rubrics and and
[1:43:48] the the rewards have been open but like the the source kind of seed data has not
[1:43:54] been which yeah bridges that gap for the for open right. Um, I I I guess Pierre,
[1:44:02] I've got a question for you that kind of comes really just from from your closing point there about multi- aent setups and
[1:44:08] and and what would that look like? Um, obviously in a kind of guy 2 setting
[1:44:14] like you couldn't necessarily do that or or could you would you have an a sub
[1:44:19] agent that acted in a verifiable way or or would you evaluate um teams? like do
[1:44:25] you have any intuitions there about what multi- aent evaluation would look like?
[1:44:32] Yeah, it's a good question. Um, you [clears throat] know, in GIA 2 we have this agent to agent mode where we have
[1:44:38] this sub agent and one sub agent is responsible for one app like one set of
[1:44:44] tools basically. So it can be very specialized to this. Um but what we see
[1:44:50] in open close for instance you could have two open close plus a bunch of humans in the same chat right or like
[1:44:56] how do you deal with this like this not specialized agent like you have to simulate the full separate agent with
[1:45:04] its own memory with memory you know it and soul files if we take the the
[1:45:10] openflow um terminology that come from a different user right from a different
[1:45:15] persona that initialized it slightly different. It has access to slightly different tools. We could do it in um we
[1:45:24] haven't tried yet. Um don't think it's it's very complicated, but then you get
[1:45:30] to one level of complication in in your parameter parameterization of your eval,
[1:45:38] right? Because like Nathan was saying, we want to document all the parameters. There's already a judge model. There's
[1:45:44] the model you're evaluating. there's like what agent orchestration you're
[1:45:49] using. But if you add more agents like there's the model of that agents like how it was set up is it a different
[1:45:56] orchestration. Again you have this explosion of ways of evaluating
[1:46:01] um simple task right and if you want to cover all of this then you have to have even more annotations
[1:46:09] like possible task and possible things to reproduce through there. So that I don't know how to manage this
[1:46:17] complexity yet, but we'll have to get there. Cool. Yeah, thanks for those intuitions.
[1:46:23] That that's really insightful. I I guess my my kind of finishing individual question would be to to Nathan and about
[1:46:29] community evals and and like the it's a really optimistic project, right? Like
[1:46:36] uh that's like kind of in its origins and it's not necessarily like dictating
[1:46:41] a standard and saying like this is the way to do things. It's kind of just like opening up the data layer to the
[1:46:46] community. Where do you see it like uh like you know if it everything uh worked as
[1:46:54] planned like six months a year from now like like what do you see that community looking like and and how do you see
[1:47:00] evaluations kind of living on the hub and how do you see it? Sure. I [clears throat] mean as you said
[1:47:06] it's not we are not trying to define anything with this feature. We're just trying exactly as what you said open up
[1:47:13] the possibility for the community to define their own not way of doing thing
[1:47:19] because they I guess someone the the way of doing thing would be defined but like by like bigger like
[1:47:27] labs or agencies but to have a say in how model results
[1:47:34] are reported and how benchmarks are created. If you make it easy for everyone to build bench benchmarks and
[1:47:41] to report the results. The hope for example in six months or in a year is is
[1:47:47] to have on the hub many many people just like you see today with models every
[1:47:53] time a model come out there is a lot of people fine-tuning their to their own data set and to opening it on the hub.
[1:48:00] The idea would be to have the same with evaluation data set and benchmarks.
[1:48:06] everyone a benchmark comes out for example every time a benchmark comes out you can just use this run your own
[1:48:12] models on it do small changes maybe to the to the data set and to this and have
[1:48:19] people build build on top of each other that would be the idea
[1:48:24] cool yeah that's that that's a a great vision um and I think a really nice point to close I just say thanks again
[1:48:31] to all the speakers it fell together really nicely and I'm looking forward to doing another kind of talk like this and
[1:48:37] and maybe inviting you all back uh one day but probably not next time. Thank you. Thank you for organizing.
[1:48:43] Thank you. This is amazing. Yeah.
