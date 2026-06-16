---
title: Building the quantum-AI future with Hartmut Neven and James Manyika
video_id: yQPnb4gxKRc
url: https://www.youtube.com/watch?v=yQPnb4gxKRc
channel: Google for Developers
channel_id: UC_x5XG1OV2P6uZZ5FSM9Ttw
channel_url: https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw
publish_date: '2026-05-21T16:54:06-07:00'
upload_date: '2026-05-21T16:54:06-07:00'
category: Science & Technology
duration: '40:28'
length_seconds: 2428
view_count: 345
is_live: false
is_family_safe: true
thumbnail: https://i.ytimg.com/vi_webp/yQPnb4gxKRc/maxresdefault.webp
keywords:
- Google
- developers
- 'pr_pr: Google I/O;'
- ct:Event - Dialogues;
- ct:Event - AI PA Keynote;
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
- language_code: en
  name: English - CC (English)
  kind: manual
  is_translatable: true
chapters: []
description: "Join Hartmut Neven and James Manyika to explore the intersection of quantum computing and AI. Discover how AI is helping to build and operate quantum computers, while quantum unlocks new ways for AI models to train, learn from complex data, and accelerate scientific discovery, making quantum a key part of Google’s innovation strategy.\n\nSpeakers: Jeff Dean, Hartmut Neven\n\nWatch the AI sessions from Google I/O 2026 → https://goo.gle/AI-at-IO26\nWatch the Dialogues sessions from Google I/O 2026 → https://goo.gle/Dialogues-at-IO26\n\nSubscribe to Google for Developers → https://goo.gle/developers \n\n#GoogleIO\n\nEvent: Google I/O 2026\n\nProducts Mentioned: AI/Machine Learning, Design"
notes: Transcript fetched via youtube-transcript-skill (Playwright path); manual English captions preferred where available.
---

## Transcript
[0:00] [MUSIC PLAYING]
[0:05] [WAVES CRASHING]
[0:11] [ANIMAL CRIES]
[1:17] 1 minute, 17 seconds [APPLAUSE]
[1:20] 1 minute, 20 seconds JAMES MANYIKA: Good morning and thank you for coming to this session this morning.
[1:28] 1 minute, 28 seconds My name is James Manyika.
[1:29] 1 minute, 29 seconds I'm the President for Research Labs, Technology & Society at Google and Alphabet.
[1:35] 1 minute, 35 seconds And, Google has an incredible track record in history of pursuing very ambitious problems and challenges and moonshots.
[1:45] 1 minute, 45 seconds Some could argue that, in fact, Search itself is a moonshot, has been a moonshot. The work in AI arguably has been a moonshot.
[1:54] 1 minute, 54 seconds Some of the earliest examples of this at Google were back in 2001, when Google started to do things like auto correction using machine learning.
[2:03] 2 minutes, 3 seconds And then you could also think about the work on Waymo, driverless cars, has been a moonshot that's now turned to reality as we start to ride Waymos.
[2:13] 2 minutes, 13 seconds Hopefully, you've all done that. And then quantum is one of those too.
[2:19] 2 minutes, 19 seconds We've focused on trying to build the idea of quantum computers for quite a long time.
[2:24] 2 minutes, 24 seconds And that's what we're going to spend time talking about this morning.
[2:28] 2 minutes, 28 seconds I should say that the foundations on which we're building quantum computers go all the way back
[2:33] 2 minutes, 33 seconds to the 1980s, when researchers at Berkeley, Michel Devoret,
[2:39] 2 minutes, 39 seconds John Martinis, and John Clarke started to work on this idea of how do you do superconductivity?
[2:46] 2 minutes, 46 seconds Because up until that time, the understanding was that quantum phenomena was only observable at the micro level.
[2:53] 2 minutes, 53 seconds And so the question is, could you ever make observations at the macro level?
[2:58] 2 minutes, 58 seconds So they made these incredible experiments and breakthroughs that led to the idea of circuits you could actually build at the macroscopic scale.
[3:07] 3 minutes, 7 seconds And that's been the foundation of how we think about building quantum computers.
[3:11] 3 minutes, 11 seconds I should say those three individuals, Michel Devoret, John Martinis and John Clarke, were awarded the Nobel Prize in physics last year,
[3:20] 3 minutes, 20 seconds and I'm actually glad to say two of them, Michel Devoret and John Martinis, have actually been part of our quantum team at Google.
[3:27] 3 minutes, 27 seconds Well, John Martinis is no longer with us at the quantum team, but Michel Devoret is actually our Chief Hardware Scientist on the quantum computing team at Google.
[3:39] 3 minutes, 39 seconds I'm going to be joined in this conversation by Hartmut Neven. Hartmut is the leader and founder of our Quantum AI team.
[3:49] 3 minutes, 49 seconds [APPLAUSE]
[3:52] 3 minutes, 52 seconds Take a seat. HARTMUT NEVEN: Hey.
[3:54] 3 minutes, 54 seconds JAMES MANYIKA: Hartmut founded this team back in 2012, the idea how can we build and achieve this moonshot of building quantum computers.
[4:04] 4 minutes, 4 seconds So he and I are going to have a conversation. We work together. So this is always a pleasure for me to chat with Hartmut.
[4:11] 4 minutes, 11 seconds And we'll talk about first of what quantum computing is; where we are, what progress are we making; and what are some of the challenges,
[4:20] 4 minutes, 20 seconds opportunities, and things that we're excited about; and what can we look forward to. So Hartmut, thanks for joining me. HARTMUT NEVEN: Oh, a pleasure.
[4:27] 4 minutes, 27 seconds Thanks, everyone, for coming. JAMES MANYIKA: Well let's start.
[4:31] 4 minutes, 31 seconds Quantum computing or quantum mechanics is one of these very complex topics.
[4:38] 4 minutes, 38 seconds How would you describe quantum computing? Give us some basics.
[4:41] 4 minutes, 41 seconds What are some of the basic things that one would have to understand about quantum computing?
[4:46] 4 minutes, 46 seconds HARTMUT NEVEN: So if you want to understand where the superpower of quantum computers comes from, the one concept we need to grasp is the concept of superposition.
[4:58] 4 minutes, 58 seconds So let me give you a quick quantum computing 101 and explain to you what superposition is.
[5:05] 5 minutes, 5 seconds Essentially, quantum physics states that any system can simultaneously exist in many configurations.
[5:16] 5 minutes, 16 seconds That's what is called a superposition. So to help you visualize it as the following.
[5:20] 5 minutes, 20 seconds Let's look at the system we are forming here right now in the room. And we are sitting here in one specific configuration.
[5:29] 5 minutes, 29 seconds But you can easily envision another one, like the two of you could switch seats. You, James and I, we could switch seats.
[5:38] 5 minutes, 38 seconds So there are other configurations.
[5:40] 5 minutes, 40 seconds But a reading of quantum physics would suggest that all these or many of these constellations,
[5:47] 5 minutes, 47 seconds configurations, are realized right now, and they evolve together in time.
[5:54] 5 minutes, 54 seconds And that is what we take advantage of in our chips.
[5:59] 5 minutes, 59 seconds JAMES MANYIKA: But I think one of the things that often, so how would you describe because we go from-- we can try to build physical qubits and then logical qubits.
[6:09] 6 minutes, 9 seconds Explain the idea of qubits, and how should we think about that, what that is? HARTMUT NEVEN: So a qubit is short for quantum bit.
[6:16] 6 minutes, 16 seconds And it's essentially a bit or qubits are a number of bits that I can put into superposition.
[6:23] 6 minutes, 23 seconds So I will later show you, or maybe we do this right now. I show you a chip that contains qubits.
[6:30] 6 minutes, 30 seconds I'm not sure the camera can see this. So this is a Willow chip, one of our more recent chips.
[6:37] 6 minutes, 37 seconds And it has 105 qubits in there.
[6:41] 6 minutes, 41 seconds And now that you know what a superposition is, you can envision the following. Those qubits can be in a superposition state.
[6:51] 6 minutes, 51 seconds So a single configuration for 105 qubits it's just a string of zeros and ones.
[6:57] 6 minutes, 57 seconds We call it a bit string of length 105.
[7:01] 7 minutes, 1 second But similar, as we envisioned before, you can just flip a few qubits and you get a different bit string.
[7:08] 7 minutes, 8 seconds You flip a few more, you get a different bit string. How many bit strings can there be?
[7:13] 7 minutes, 13 seconds I say 105 quantum bits in this chip is 2 to the power of 105.
[7:20] 7 minutes, 20 seconds And then, as amazing as this may sound, in just one clock cycle of this chip, we can touch 2 to the 105 different objects, 2 to the 105 different strings.
[7:34] 7 minutes, 34 seconds That is an enormous number.
[7:36] 7 minutes, 36 seconds And therefore, you arrive at these situations where this tiny chip can do certain computations
[7:44] 7 minutes, 44 seconds that the largest factory-sized data center would need an inordinate amount of time, 10 septillion years, in a recent demonstration.
[7:54] 7 minutes, 54 seconds JAMES MANYIKA: In my opening--
[7:56] 7 minutes, 56 seconds [APPLAUSE]
[7:57] 7 minutes, 57 seconds Thank you.
[7:59] 7 minutes, 59 seconds In my opening remarks, I mentioned the idea that we're building on breakthroughs that our colleagues, Michel Devoret and others made in the 1980s.
[8:08] 8 minutes, 8 seconds And one of the key things that they worked on was this idea of superconductivity as a way with the ideas of how do you do,
[8:15] 8 minutes, 15 seconds if you like, quantum tunneling with Josephson circuits, to be able to do superconductivity.
[8:20] 8 minutes, 20 seconds That often requires that we actually cool these things down to a few degrees above Kelvin.
[8:27] 8 minutes, 27 seconds And so in the lab, describe the fact that you're actually building these extraordinary fridges so you can cool things down to a few degrees above 0 Kelvin.
[8:37] 8 minutes, 37 seconds Why are we building it that way? How does that work?
[8:41] 8 minutes, 41 seconds HARTMUT NEVEN: So the different ways how you can make qubits, in quantum mechanics, famously, you
[8:48] 8 minutes, 48 seconds might think of quantum mechanics as a physics of the very small, the thing that describes electrons, atoms.
[8:55] 8 minutes, 55 seconds But this is actually incorrect.
[8:58] 8 minutes, 58 seconds Quantum physics is the law of the land at all scales, at the microscopic, all the way to the universe as a whole.
[9:05] 9 minutes, 5 seconds It just happens to be the case that quantum effects can easily be controlled, managed, and observed on microscopic scales.
[9:14] 9 minutes, 14 seconds So a natural choice to build a qubit, therefore, would be to just use an atom, to use, let's say, the states of a spin of an electron or of a nucleus.
[9:28] 9 minutes, 28 seconds But these things are tiny and hard to engineer with.
[9:32] 9 minutes, 32 seconds So the ingenious inventions that got the Nobel Prize, as you explained, was to essentially make macroscopic qubits.
[9:39] 9 minutes, 39 seconds So using a loop of superconducting wires, you can have the same property of quantized energy levels and other hallmark features of atoms.
[9:51] 9 minutes, 51 seconds You can have this at a macroscopic scale, much easier to put into a chip and work with.
[9:57] 9 minutes, 57 seconds JAMES MANYIKA: Yeah, and in fact, one of the things that you always like to say, Hartmut, is that your lab is probably the coldest place in our galaxy.
[10:05] 10 minutes, 5 seconds Can you explain that? HARTMUT NEVEN: Yeah so to work with these artificial atoms that
[10:12] 10 minutes, 12 seconds are made out of superconducting material, and many of you may know that right now, to get superconductivity, a macroscopic quantum effect,
[10:20] 10 minutes, 20 seconds you have to cool down the metals or the materials to a very low degree. So we work currently with aluminum qubits.
[10:29] 10 minutes, 29 seconds You could have used niobium, tantalum. There are some choices. But all of them have to go down to about 1 Kelvin.
[10:37] 10 minutes, 37 seconds So that's pretty cool. But we don't stop there.
[10:42] 10 minutes, 42 seconds We go even further down to just 10 millikelvin because temperature is really the physicists' term for noise.
[10:50] 10 minutes, 50 seconds And we don't want to have noise in our chips, so the colder we can make it, the better.
[10:55] 10 minutes, 55 seconds JAMES MANYIKA: So talk a little bit about what's difficult about building quantum computers.
[11:01] 11 minutes, 1 second What are some of the key challenges you have to solve if you're trying to build these systems?
[11:06] 11 minutes, 6 seconds HARTMUT NEVEN: So in the very beginning, I explained to you that the key ingredients, a key resource is superposition states.
[11:14] 11 minutes, 14 seconds And we need to keep these superpositions of different constellations alive.
[11:22] 11 minutes, 22 seconds And the times that measured, there's an important time. We call it the coherence time of a quantum computer.
[11:29] 11 minutes, 29 seconds It essentially measures how long these superpositions survive. And you want to make this the longer the better.
[11:36] 11 minutes, 36 seconds And initially, we all thought, oh, this is a key battle to fight, the key engineering challenge to get right.
[11:44] 11 minutes, 44 seconds But it turned out in this area we made rapid progress.
[11:47] 11 minutes, 47 seconds We went from 20 microsecond coherence time to 10 times more, now over 250 microseconds, pretty much enough for what we need for use for quantum computing.
[11:58] 11 minutes, 58 seconds So it's not the key physics challenge anymore. It's more mundane system-level issues that hold us back.
[12:05] 12 minutes, 5 seconds JAMES MANYIKA: So why would anybody want to build a quantum computer?
[12:10] 12 minutes, 10 seconds What are some of the useful applications, assuming we get there? We'll talk a little bit in a little while about where we are. But why would you want a quantum computer?
[12:19] 12 minutes, 19 seconds HARTMUT NEVEN: Yeah, so on the application side, there are various areas.
[12:24] 12 minutes, 24 seconds One thing that's important for the audience to understand, quantum computers, as far as we know, will always be a specialist tool.
[12:33] 12 minutes, 33 seconds It will be very good for certain applications, not so useful for others. So what are some of the useful applications we can think of?
[12:43] 12 minutes, 43 seconds The first one is we call it Richard Feynman's killer app.
[12:49] 12 minutes, 49 seconds Feynman was the first one to realize that if you want to simulate a system where quantum effects are important, you run against this combinatorial challenge.
[12:59] 12 minutes, 59 seconds That is you have to consider all these different constellations, and that's just impossibly hard for classical computers to do.
[13:06] 13 minutes, 6 seconds So he coined, you saw it in the initial video, that if you want to make a faithful simulation of nature, you better make it quantum mechanical.
[13:16] 13 minutes, 16 seconds JAMES MANYIKA: But I think often when people think about quantum computers, we often think about the speed-up benefits, that it will be able to run things much faster.
[13:27] 13 minutes, 27 seconds But also there are some problems that are inherently quantum that you can only work on.
[13:33] 13 minutes, 33 seconds So can you make a distinction between where are we mostly capsulizing just on speed-ups versus when we're actually working on things that can only be worked on with quantum computers?
[13:43] 13 minutes, 43 seconds HARTMUT NEVEN: Yeah. Let's say a few examples.
[13:46] 13 minutes, 46 seconds I just gave you this general overview, Richard Feynman's killer app, the simulation of quantum systems.
[13:53] 13 minutes, 53 seconds That is actually a task that is necessary more often than you might think. Let's pick a nice one.
[14:01] 14 minutes, 1 second Batteries, sounds a little bit boring, but we would all feel so much better if we could fly in an airplane that is powered by batteries, not by kerosene when we do vacation.
[14:13] 14 minutes, 13 seconds So now there are things like lithium air batteries, which, they have a higher energy density than kerosene.
[14:22] 14 minutes, 22 seconds So you could perfectly do that. Unfortunately, they are very brittle. They have various material science issues. So that's why we don't use them today.
[14:30] 14 minutes, 30 seconds But a quantum computer would be a marvelous tool to simulate various designs for lithium air batteries.
[14:37] 14 minutes, 37 seconds And then we can have some not just in cars, but in airplanes too. JAMES MANYIKA: Right, yeah.
[14:42] 14 minutes, 42 seconds Maybe you can correct me, I think there's currently something like 70-plus kind of algorithms and problems that people in the community have actually identified as things
[14:51] 14 minutes, 51 seconds where a quantum computer would be the most useful way to tackle those problems. Is this still 70, or is that list growing? HARTMUT NEVEN: Yeah.
[14:59] 14 minutes, 59 seconds Thank you for mentioning this number.
[15:01] 15 minutes, 1 second I should have checked up on the website because when we started talking it was like 60. Now it's 70.
[15:07] 15 minutes, 7 seconds And I hope that in a few years, there will be 600 or 700 important, 10 times more, important algorithms where quantum computers give you a decisive advantage.
[15:20] 15 minutes, 20 seconds JAMES MANYIKA: Right. So Hartmut, let's talk about where we are at this stage.
[15:24] 15 minutes, 24 seconds I mean, I remember when you and I first started working together, I guess five years ago, you had a roadmap which had six milestones.
[15:33] 15 minutes, 33 seconds First of all, can you describe the roadmap you've had for progress towards building a quantum computer, and where are we on that roadmap?
[15:41] 15 minutes, 41 seconds What progress are we making?
[15:43] 15 minutes, 43 seconds HARTMUT NEVEN: So originally, and if anybody has watched the work of the Google Quantum AI team, you may have seen we typically show it first thing whenever
[15:52] 15 minutes, 52 seconds we give a talk or presentation is our mission is to build a useful quantum computer for otherwise unsolvable problems.
[16:02] 16 minutes, 2 seconds To get to that, we had set out a roadmap with six milestones to build such a machine.
[16:09] 16 minutes, 9 seconds And the first two milestones we cleared a few years ago.
[16:14] 16 minutes, 14 seconds So our very first one was in 2019, where we showed for the first time that a quantum computer could compute something quickly
[16:21] 16 minutes, 21 seconds in minutes that would have taken many, many years on a classical supercomputer to do. So that was milestone one.
[16:29] 16 minutes, 29 seconds And milestone two was there is a technique called quantum error correction.
[16:35] 16 minutes, 35 seconds That is essentially the technology you need to keep those superposition states alive. And that was understood in theory well since the '90s.
[16:45] 16 minutes, 45 seconds But then, in '22, for the first time, we reduced this to practice and built a machine
[16:53] 16 minutes, 53 seconds where quantum error correction successfully reduced the errors in a machine in practice.
[17:00] And we are now ahead of, hopefully fingers crossed, we solve it later this year as milestone three.
[17:09] 17 minutes, 9 seconds This would be one very good module out of which you can build a large modular quantum computer.
[17:18] 17 minutes, 18 seconds JAMES MANYIKA: And so by the time we get to hopefully milestone five or six, hopefully we'll have useful applications.
[17:26] 17 minutes, 26 seconds But let's talk a little bit about some of the recent breakthroughs. I mean you showed the Willow chip.
[17:31] 17 minutes, 31 seconds This is a chip we showed the world back in 2024.
[17:36] 17 minutes, 36 seconds And I think there are two key breakthroughs associated with that.
[17:40] 17 minutes, 40 seconds One is the fact that it was able to do in a few minutes what would take the world's fastest supercomputer 10 septillion years.
[17:48] 17 minutes, 48 seconds That's 1 with 25 zeros next to which is extraordinary.
[17:52] 17 minutes, 52 seconds But the other one, in some ways more important demonstration, was this idea of below threshold error correction.
[17:59] 17 minutes, 59 seconds Can you explain what that is and why that matters so much?
[18:03] 18 minutes, 3 seconds HARTMUT NEVEN: Yeah, so quantum error correction is a technology you need to keep the important superposition states alive.
[18:12] 18 minutes, 12 seconds And for the very first time, as I said, we cleared that hurdle in '22.
[18:16] 18 minutes, 16 seconds But the community wasn't too impressed because the errors just came down by a few percent.
[18:23] 18 minutes, 23 seconds And people said, well, even though before-- so how do you do error correction? Typically, you use redundancy.
[18:32] 18 minutes, 32 seconds That's what we use in engineering to make things safer.
[18:36] 18 minutes, 36 seconds So you take a number of physical qubits, as we call them, to orchestrate them into one more stable logical qubit.
[18:45] 18 minutes, 45 seconds That is what error correction does.
[18:47] 18 minutes, 47 seconds And then when we try-- before when people tried it they introduced more redundancy.
[18:55] 18 minutes, 55 seconds But there was more stuff. Now more qubits, more wires, more measurement devices.
[19:00] So the error always came down, or sorry the opposite, the error went up.
[19:07] 19 minutes, 7 seconds And then in '22, we made it come down for the first time, but an unimpressive few percent. And then with Willow, we just redid this.
[19:16] 19 minutes, 16 seconds And in '24, we basically did the same experiment again. But now it was already much higher quality chip. And the error came down by a factor of 2.
[19:25] 19 minutes, 25 seconds And then the field for the first time was, oh, this seems to really work for good. JAMES MANYIKA: Right. So that was an important breakthrough.
[19:33] 19 minutes, 33 seconds And then last year, we had another big breakthrough.
[19:36] 19 minutes, 36 seconds But maybe to set up that breakthrough, all these typical benchmarks we've been using, such as the 10 septillion years and so forth, we're
[19:45] 19 minutes, 45 seconds talking about using a particular benchmark mechanism called random circuit sampling as a way to measure, but it's not a very useful computation.
[19:54] 19 minutes, 54 seconds But it's useful to measure progress.
[19:56] 19 minutes, 56 seconds But the breakthrough last year with Quantum Echoes was actually the first time anybody, I think, had shown a useful algorithm.
[20:04] 20 minutes, 4 seconds Can you talk about Quantum Echoes and why that breakthrough was important? HARTMUT NEVEN: Yes. So you said it nicely.
[20:12] 20 minutes, 12 seconds So the initial demonstrations that quantum chips can do something impressive was done
[20:18] 20 minutes, 18 seconds on exotic mathematical benchmarks where essentially problems that you or people in the real world don't have, good for benchmarking.
[20:28] 20 minutes, 28 seconds And then the criticism was show us something that I would care for. And Quantum Echoes was the answer to this.
[20:37] 20 minutes, 37 seconds It was the first quantum algorithm that can do a useful task. JAMES MANYIKA: Talk about the task.
[20:44] 20 minutes, 44 seconds Because we had a demonstration where we worked with researchers at Berkeley and others to actually show a useful use of Quantum Echoes.
[20:53] 20 minutes, 53 seconds Can you describe that work?
[20:54] 20 minutes, 54 seconds HARTMUT NEVEN: Yeah, so Quantum Echoes is essentially the quintessential quantum machine learning algorithm.
[21:01] 21 minutes, 1 second It allows you to learn from readily available data.
[21:05] 21 minutes, 5 seconds It's data that comes from nuclear magnetic resonance imaging, so in NMR machines that pharmaceutical companies use.
[21:12] 21 minutes, 12 seconds Or if you go to a hospital and do an MRI scan, that's also nuclear magnetic resonance imaging.
[21:19] 21 minutes, 19 seconds So to get out of these devices more information, that's where the Quantum Echoes algorithm applies.
[21:27] 21 minutes, 27 seconds JAMES MANYIKA: And I think in that example, what you were able to observe was to show that, for the first time, you were able to measure these kind of dihedral angles of these very hard to understand molecules.
[21:39] 21 minutes, 39 seconds I think, was it a benzene, a couple benzene molecules?
[21:41] 21 minutes, 41 seconds Can you-- HARTMUT NEVEN: Yeah, we then-- and typically when you have such new algorithms, there are a few steps to really lodge it in practice.
[21:51] 21 minutes, 51 seconds So initially, we showed it on some proof of principle problems. And then you go closer to what chemists care for.
[21:59] 21 minutes, 59 seconds So there was it's called a diphenyl. It has two benzene rings.
[22:03] 22 minutes, 3 seconds And chemists didn't know how are these two rings rotated relative to each other. So we computed this angle using Quantum Echoes.
[22:12] 22 minutes, 12 seconds And showed, look, you can answer real open questions in chemistry with that algorithm.
[22:18] 22 minutes, 18 seconds JAMES MANYIKA: One of the things, I mean so the quantum team at Google is actually called Quantum AI.
[22:26] 22 minutes, 26 seconds And we should talk about that, why that name.
[22:29] 22 minutes, 29 seconds And there's always a question about, so do these two things need each other.
[22:34] 22 minutes, 34 seconds Does quantum computing need AI and does AI need quantum computer?
[22:38] 22 minutes, 38 seconds Can you explain the origin of the name Quantum AI for the team?
[22:42] 22 minutes, 42 seconds And then I'd love to maybe debate you a little bit on this question of AI and quantum. Why that name? HARTMUT NEVEN: So yeah, why is our team called Quantum AI?
[22:51] 22 minutes, 51 seconds And that was-- actually I worked in AI for most of my career. I actually here is self-driving cars.
[22:59] 22 minutes, 59 seconds My PhD was on self-driving cars. I joined Google doing computer vision, visual search.
[23:06] 23 minutes, 6 seconds But at the time, it dawned on me that real, powerful future AI
[23:13] 23 minutes, 13 seconds wants to have access to the most potent, capable computational substrate we can think of, and currently that is quantum computing.
[23:25] 23 minutes, 25 seconds So I thought quantum AI should be able to do tasks that AI running on classical machines will never be able to do.
[23:32] 23 minutes, 32 seconds And then in 2012, we set out, based on the thesis, to show that this is really true.
[23:39] 23 minutes, 39 seconds JAMES MANYIKA: And I think one of the reasons, one of the contributions that quantum computing can make to AI is in particular data sets.
[23:48] 23 minutes, 48 seconds HARTMUT NEVEN: Yeah. So maybe we should advertise this, James.
[23:52] 23 minutes, 52 seconds So for those of you who want to know more details, there will be a special issue of "Daedalus" coming out.
[23:59] 23 minutes, 59 seconds You're the editor.
[24:01] 24 minutes, 1 second And there we put an essay that is called "Quantum Plus AI Equals Quantum AI," and it speaks about this bidirectional acceleration.
[24:11] 24 minutes, 11 seconds How do we use AI today to accelerate progress in quantum computing, and how starting now, and even more so in the future, quantum resources will help solve novel tasks?
[24:23] 24 minutes, 23 seconds JAMES MANYIKA: Yeah and I think one of those examples, which is incredible to see was how there was a deep collaboration between the DeepMind team
[24:32] 24 minutes, 32 seconds and the quantum team around this idea of alpha qubits as a way to think about how to use AI and machine learning
[24:40] 24 minutes, 40 seconds techniques to actually help the progress we've been making on error correction. There was one example where AI was actually benefiting quantum.
[24:50] 24 minutes, 50 seconds Have there been other examples like that?
[24:52] 24 minutes, 52 seconds HARTMUT NEVEN: Yeah, let me give you also your previous question I haven't properly answered yet. So how can quantum help AI?
[25:00] There are probably a dozen different ways. Let me give you one or two examples.
[25:05] 25 minutes, 5 seconds So AlphaFold, a resounding success, used in labs all over the world.
[25:13] 25 minutes, 13 seconds To train AlphaFold, we needed data sets that started to be collected in the 1970s.
[25:19] 25 minutes, 19 seconds It took 50 years to make things like the protein database to train AlphaFold, very painstaking work by many PhDs, lots of government grants.
[25:33] 25 minutes, 33 seconds So a quantum computer would be able to produce very valuable training sets in many settings where it's difficult to make those training sets otherwise.
[25:44] 25 minutes, 44 seconds So we expect this to be the very first contribution of quantum to AI that we say, look, here's a great data set that you should use.
[25:54] 25 minutes, 54 seconds And actually, as a late-breaking piece of news, just last week, we had first data sets relevant to material science where we thought, oh wow, they have the quality good enough.
[26:04] 26 minutes, 4 seconds We should ship them to our colleagues at DeepMind. JAMES MANYIKA: That's fantastic.
[26:08] 26 minutes, 8 seconds One of the things that I find pretty exciting about, even though, of course, we're on this moonshot journey
[26:14] 26 minutes, 14 seconds to build a fully error-corrected quantum computer, there's a lot of great science and discovery that's actually happening along the way.
[26:24] 26 minutes, 24 seconds Can you give a couple of examples?
[26:26] 26 minutes, 26 seconds I mean, one of my favorite ones was the holographic effect, which goes back to something, a conjecture that Einstein had.
[26:32] 26 minutes, 32 seconds But talk a little bit about some of the examples of the incredible science you and the team are able to do along the way.
[26:40] 26 minutes, 40 seconds HARTMUT NEVEN: So now that we have chips with a few hundred qubits, we can make good on Richard Feynman's dream
[26:47] 26 minutes, 47 seconds and simulate quantum systems and study their properties and learn new things.
[26:54] 26 minutes, 54 seconds And you mentioned already a few.
[26:57] 26 minutes, 57 seconds There is one very exotic one which created quite the firestorm in the scientific community.
[27:05] 27 minutes, 5 seconds And it will be hard to explain fully the science behind it.
[27:11] 27 minutes, 11 seconds You might have heard of the effect of quantum entanglement that two quantum particles can be correlated at long distances.
[27:20] 27 minutes, 20 seconds You may also have heard about wormholes, which is a connection through space between two distant space points.
[27:28] 27 minutes, 28 seconds And there is a field in physics.
[27:31] 27 minutes, 31 seconds It's called holographic duality that claims that these two processes are the same.
[27:36] 27 minutes, 36 seconds So if that is really true, then we can use entangled qubits, which we can produce on our chip to make wormholes.
[27:44] 27 minutes, 44 seconds And we essentially created a wormhole. And I use the word created not simulated.
[27:50] 27 minutes, 50 seconds Because strictly speaking, if the holograph, if the string theorists are right and this duality exists, then it was actually a tiny--
[27:58] 27 minutes, 58 seconds don't worry, you wouldn't have fallen in-- but a tiny wormhole was actually created.
[28:03] 28 minutes, 3 seconds JAMES MANYIKA: Yeah, I mean, this gets very exotic pretty quickly.
[28:06] 28 minutes, 6 seconds I mean, you've also been doing experiments on quantum gravity as well.
[28:10] 28 minutes, 10 seconds And you've also been doing even understanding deeper questions about electromagnetism that we didn't fully understand before.
[28:18] 28 minutes, 18 seconds So there's a lot of incredible science going on along the way.
[28:22] 28 minutes, 22 seconds HARTMUT NEVEN: Yeah, so one thing we are proud of is that there is our team produces this string,
[28:29] 28 minutes, 29 seconds dense string of high-impact publications that discusses exactly that, that discoveries made
[28:39] 28 minutes, 39 seconds through this process, quantum simulation of interesting systems.
[28:43] 28 minutes, 43 seconds And others, just the names, we won't explain, but time crystals. We made time crystals.
[28:48] 28 minutes, 48 seconds That's the closest you get, that physics lets you get to perpetual mobile.
[28:53] 28 minutes, 53 seconds It's essentially a system that stays in periodic motion forever, without needing to exchange any energy with the environment.
[29:02] 29 minutes, 2 seconds Or another exotic thing was non-abelian anyons. I know that's a mouthful. What is that?
[29:08] 29 minutes, 8 seconds But it's something also goes seemingly against common sense.
[29:14] 29 minutes, 14 seconds It's essentially the situation, imagine you build a little house out of LEGO blocks.
[29:19] 29 minutes, 19 seconds And there are, let's say, two bricks that look the same, and you switch them out and you look again at your house, because they were the same, nothing should have changed.
[29:31] 29 minutes, 31 seconds But in quantum physics, there was a prediction that this may be different.
[29:35] 29 minutes, 35 seconds That even though you swap two identical particles, the overall system changes properties.
[29:42] 29 minutes, 42 seconds And that we showed in practice that really, yes, that exists.
[29:47] 29 minutes, 47 seconds JAMES MANYIKA: Often when people think a lot about quantum computing, I mean, you and I can talk about all these extraordinary applications in biology and chemistry, in materials and so forth.
[29:59] 29 minutes, 59 seconds But I think the one application or use that most people think about is encryption.
[30:05] 30 minutes, 5 seconds Ever since, for example, Shor's algorithm, the idea that most of our cryptographic encryption systems
[30:13] 30 minutes, 13 seconds rely on the fact that these are incredibly hard problems for classical computers to solve.
[30:20] 30 minutes, 20 seconds And so therefore, we rely on the difficulty of those computations as a way to think about our encryption systems.
[30:26] 30 minutes, 26 seconds But if you had a quantum computer, you probably could crack those systems.
[30:30] 30 minutes, 30 seconds And so recently, you made and the team made some news recently, to suggest that, in fact, the ability
[30:39] 30 minutes, 39 seconds to build systems that can crack RSA encryption and also elliptic curve cryptography systems is not that far away.
[30:48] 30 minutes, 48 seconds Can you talk a little bit about what the news was and what the progress has been on building those kinds of systems?
[30:55] 30 minutes, 55 seconds HARTMUT NEVEN: Yeah so fortunately, many of the natural applications for quantum computers are these very human-kind friendly things,
[31:02] 31 minutes, 2 seconds like design drugs quicker, better batteries, fusion reactors, and many important humankind challenges.
[31:13] 31 minutes, 13 seconds But one of the more problematic applications of quantum computing is it can be very powerful for crypto analysis.
[31:23] 31 minutes, 23 seconds And indeed, in quantum computing, it's not just that the hardware has made progress.
[31:30] 31 minutes, 30 seconds It's also the algorithms have made progress.
[31:33] 31 minutes, 33 seconds So we were able to show that you need less and less resources to do the simulations, but also cryptoanalysis, and therefore indeed the timelines are moving inward.
[31:46] 31 minutes, 46 seconds It's not that you can wait till late 2030s before you have to worry about it.
[31:52] 31 minutes, 52 seconds Actually, Google put a blog post out saying, hey, we need to move to more powerful post-quantum crypto schemes already by 2029.
[32:02] 32 minutes, 2 seconds JAMES MANYIKA: Yeah, maybe to put this in concrete terms, I think back in 2019, I think the view in the field was that
[32:10] 32 minutes, 10 seconds if you wanted a quantum system that was capable of cracking RSA 256 encryption, you'd need at least a 20-million qubit system.
[32:21] 32 minutes, 21 seconds And then we showed about a year ago that threshold had actually come down because of the progress to where you'd need perhaps about a million qubits.
[32:31] 32 minutes, 31 seconds And then two months ago, we showed that in particular with the elliptic curve cryptography systems, which are mostly used for cryptocurrencies
[32:40] 32 minutes, 40 seconds and other things, the threshold that had come down even further, which suggests that the day in which we
[32:49] 32 minutes, 49 seconds have to move to a post-quantum cryptography system is not that far away. It's not that far away.
[32:55] 32 minutes, 55 seconds I mean, talk about how you think about our responsibilities when it comes to making sure the world is ready for the arrival of quantum computer systems.
[33:06] 33 minutes, 6 seconds HARTMUT NEVEN: Yeah, you're exactly right.
[33:09] 33 minutes, 9 seconds So last year, we have a very gifted quantum algorithm design on our team. His name is Craig Gidney.
[33:15] 33 minutes, 15 seconds And last year he showed, oh, you can do cryptanalysis on RSA 2,048 with just a million physical qubits.
[33:23] 33 minutes, 23 seconds And then he went on to show ECC-256, which is important for digital signatures. You need only a few hundred thousand physical qubits.
[33:33] 33 minutes, 33 seconds By the way, earlier when we described the roadmap, I should have added this. I said our roadmap had six milestones.
[33:40] 33 minutes, 40 seconds And number six was essentially build a physical chip or a set of physical chips with a million physical qubits.
[33:49] 33 minutes, 49 seconds But because of these advances in algorithms, we now think that a commercially relevant machine would only need about 100,000 physical qubits.
[34:01] 34 minutes, 1 second So our meme there is milestone five is the new milestone six. That one, we really would see commercial impact.
[34:10] 34 minutes, 10 seconds JAMES MANYIKA: So Hartmut, as you look ahead, what are you most excited about and what are you most concerned about with quantum computing?
[34:21] 34 minutes, 21 seconds HARTMUT NEVEN: What I'm most excited about is that right now for many algorithms,
[34:30] 34 minutes, 30 seconds to quantum algorithms, to argue that they are useful in real life, you have
[34:37] 34 minutes, 37 seconds to prove it by pencil and paper because you can't run the algorithm yet. At the end of the decade, we won't have to do this anymore.
[34:46] 34 minutes, 46 seconds There's a cool quantum machine learning algorithm.
[34:49] 34 minutes, 49 seconds And rather than painstakingly trying to prove it, and we can't prove these things typically for classical neural networks either.
[34:59] 34 minutes, 59 seconds But then you would just demonstrate by running it.
[35:02] 35 minutes, 2 seconds So that will be a so much more fun period, when empirically, heuristically, you can test out and develop new algorithms.
[35:11] 35 minutes, 11 seconds JAMES MANYIKA: But I do know you're excited about a few other things too. Maybe I can draw you out on this.
[35:15] 35 minutes, 15 seconds I mean, you've been thinking about the intersection of quantum computing and creativity, for example. Can you talk about some of the experiments you've been running?
[35:24] 35 minutes, 24 seconds HARTMUT NEVEN: Yeah, we recently did some very fun experiments.
[35:28] 35 minutes, 28 seconds Many of you may know that a key tool to generate nice images, audio, video, is with diffusion neural networks.
[35:40] 35 minutes, 40 seconds They essentially take a noise tensor and then have been trained to sculpt a nice image out of this noise.
[35:49] 35 minutes, 49 seconds And one of the things we can do today is we can represent noise distribution or probability
[35:57] 35 minutes, 57 seconds distributions, I should say, on our chips that are outside of the reach of classical computers.
[36:04] 36 minutes, 4 seconds So we asked, hey, if we use our chip to make the noise tensor, will this make a more vibrant, better-looking image?
[36:13] 36 minutes, 13 seconds And we produced those images. And actually, you're going to see them.
[36:17] 36 minutes, 17 seconds We try to find ways to release this tool so you can play with it and judge for yourself whether this hypothesis is correct.
[36:23] 36 minutes, 23 seconds JAMES MANYIKA: But you actually showed some of this in some exhibitions in Europe recently, I think. Right?
[36:29] 36 minutes, 29 seconds HARTMUT NEVEN: Yeah, we had collaborations with known artists.
[36:34] 36 minutes, 34 seconds So the earliest was with Refik Anadol where in 2020, we did the same process.
[36:41] 36 minutes, 41 seconds We used output from a quantum processor, quantum noise tensor to build this artwork.
[36:48] 36 minutes, 48 seconds It was called "Quantum Memories." And it was actually that successful, it was seen by 1.3 million viewers, but not clicking on YouTube.
[36:58] 36 minutes, 58 seconds Physical people came into the museum, so very successful.
[37:02] 37 minutes, 2 seconds There were two other shows in Berlin and one I was a bit proud of. There was a show that drew a crowd that long.
[37:12] 37 minutes, 12 seconds There was a one or two mile long line in Berlin in the middle of the winter, to get into the Kraftwerk
[37:19] 37 minutes, 19 seconds exhibition to see this quantum art show, so that was very nice to see.
[37:24] 37 minutes, 24 seconds JAMES MANYIKA: So Hartmut, as we wrap up, because I know we're at the end of our time, if we're having this conversation a couple years
[37:31] 37 minutes, 31 seconds from now, what kinds of things do you hope we'll have achieved and what new results will you be able to show?
[37:39] 37 minutes, 39 seconds HARTMUT NEVEN: Yeah, I hope to show and of course our team is very motivated by this,
[37:45] 37 minutes, 45 seconds to demonstrate that this basic thesis is correct, that quantum AI is a more powerful form of AI.
[37:55] 37 minutes, 55 seconds JAMES MANYIKA: Yeah, well, actually, maybe I can sneak in one other question.
[37:58] 37 minutes, 58 seconds I think at the very beginning of this conversation, we very much obviously focused on the fact that you've been pursuing superconductivity and superconducting qubits as a way to build quantum computers.
[38:12] 38 minutes, 12 seconds But that is clearly not the only way to build quantum computers. There are other mechanisms.
[38:16] 38 minutes, 16 seconds People are talking about neutral atoms, talking about if you like, topological qubits, and a whole range of possibilities.
[38:25] 38 minutes, 25 seconds You recently started a new team focused on neutral atoms.
[38:29] 38 minutes, 29 seconds Can you describe that as a different alternative way to build these systems?
[38:34] 38 minutes, 34 seconds HARTMUT NEVEN: So there are five, six, seven ways that are being explored to represent quantum bits, qubits.
[38:45] 38 minutes, 45 seconds And I earlier explained to you how superconducting is a very good strategy to do this because you have these macroscopic atoms easy to deal with.
[38:54] 38 minutes, 54 seconds Now it turns out that people who work with the natural atoms, they also made nice progress to the point where we thought,
[39:03] 39 minutes, 3 seconds maybe they might get to certain applications earlier than the superconducting path.
[39:08] 39 minutes, 8 seconds So we added a second thread, and we have now an emerging lab in Boulder, Colorado, where
[39:16] 39 minutes, 16 seconds we pursue a second thread called neutral atom approach to quantum computing. And we will see how this goes.
[39:24] 39 minutes, 24 seconds And of course, both threads can benefit tremendously from the common expertise we have in algorithms, error correction, control, electronics, and others.
[39:34] 39 minutes, 34 seconds JAMES MANYIKA: And they both have very different properties. That's why they're very complementary, I think, right? HARTMUT NEVEN: Yeah, they have both their pluses and minuses.
[39:43] 39 minutes, 43 seconds Superconducting will always be much quicker.
[39:47] 39 minutes, 47 seconds Neutral atom systems have maybe an easier way to be connected to sensors. That's something we haven't talked about.
[39:55] 39 minutes, 55 seconds And quantum enhanced sensing literally gives humanity new eyes to see features of the universe we so far were blind to.
[40:06] 40 minutes, 6 seconds JAMES MANYIKA: I think we're being told we should wrap this up, but thank you for the conversation.
[40:11] 40 minutes, 11 seconds I hope this was useful and informative to everybody, but good to see you, Hartmut, as always. HARTMUT NEVEN: Yeah, it was a fun conversation. Thank you.
[40:18] 40 minutes, 18 seconds [APPLAUSE]
[40:19] 40 minutes, 19 seconds [MUSIC PLAYING]
[40:23] 40 minutes, 23 seconds
