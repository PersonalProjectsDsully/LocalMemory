---
type: youtube
title: How to build the world's fastest voice bot: Kwindla Hultman Kramer
author: AI Engineer
video_id: dRQHikOrH2A
video_url: https://www.youtube.com/watch?v=dRQHikOrH2A
thumbnail_url: https://img.youtube.com/vi/dRQHikOrH2A/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: ['Conversational AI', 'LLM Integration', 'Healthcare Automation', 'Real-Time Systems', 'Latency Optimization', 'Tool Calling', 'Generative AI', 'User Experience Design']
entities: ['Tri County health services', 'Gaba Penton', 'LLM', 'electronic health record systems', 'webRTC', 'conversational AI', 'Gen Frontier', 'healthcare automation']
concepts: ['conversational AI', 'LLM integration', 'healthcare automation', 'real-time systems', 'latency optimization', 'tool calling', 'generative AI', 'user experience design']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['knowledge of LLMs', 'understanding of healthcare systems', 'experience with real-time data processing']
related_topics: ['Conversational AI', 'LLM applications', 'Healthcare technology', 'Real-time systems', 'Latency optimization', 'Tool integration', 'Generative AI', 'User experience design']
authority_signals: ['we built this is an example of something we built for a Healthcare customer that solved a real pain point', "it's not actually a real electronic health record systems on the back end but it's they're they real tool calling"]
confidence_score: 0.7
---

# How to build the world's fastest voice bot: Kwindla Hultman Kramer

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=dRQHikOrH2A)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai development, voice bot, gpt-4, real-time audio, cloud computing, multimodal ai, deep learning  

## Summary

```markdown
# Summary of "How to Build the World's Fastest Voice Bot" by Kwindla Hultman Kramer

## Overview
Kwindla Hultman Kramer, a developer at Daily (a company specializing in real-time audio/video infrastructure), discusses the challenges and strategies for building a fast, reliable voice bot using advanced tools like GPT-4. The talk emphasizes the importance of **architectural flexibility** and **low-latency processing** to create seamless conversational experiences, with a focus on practical applications such as healthcare form-filling.

## Key Points
1. **Architectural Flexibility**:  
   - Building a voice bot requires integrating multiple components, including real-time data pipelines, echo cancellation, and text-to-speech (TTS) systems.  
   - Challenges include handling interruptions, swapping models dynamically, and ensuring compatibility with external systems (e.g., electronic health records).  

2. **Real-Time Processing**:  
   - **Latency** (time to first token) is critical for conversational interactions, as users expect near-instant responses.  
   - **Throughput** (data processing speed) is less of a bottleneck for modern tools like LLMs, which can generate content as fast as users can consume it.  

3. **Practical Applications**:  
   - A healthcare example demonstrates how a voice bot can replace manual form-filling by conducting natural conversations to collect patient data.  
   - Mocked integrations with external systems (e.g., EHRs) are already moving into production, showcasing the technology's real-world viability.  

4. **Technical Challenges**:  
   - Echo cancellation is essential for webRTC-based systems, as convincing users to wear headphones 100% of the time is impractical.  
   - Balancing trade-offs between latency, throughput, and system complexity is a core engineering challenge.  

## Key Insights
- **Speed vs. Flexibility**: While throughput is manageable, reducing latency (e.g., "time to first token") is the primary hurdle for conversational AI.  
- **User Experience**: When all components align, voice bots can feel "magical" and intuitive, mimicking natural human interactions.  
- **Future Trends**: The "Gen Frontier" (generative AI) is advancing rapidly, with developers pushing boundaries in real-time, interactive systems.  

## Actionable Recommendations
1. Prioritize **low-latency architectures** for real-time interactions.  
2. Invest in **robust media processing** (e.g., echo cancellation, TTS) for seamless user experiences.  
3. Leverage **tool calling** and external system integrations to solve real-world problems (e.g., healthcare data collection).  
4. Design systems with **flexibility** to adapt to dynamic user needs and technical constraints.  
```

## Full Transcript

[00:00] [Music]
[00:13] so uh my name's quinda I work at a
[00:16] company called daily we make real-time
[00:17] audio and video infrastructure and when
[00:20] GPT 4 was released last year we started
[00:23] building lots and lots of experiments uh
[00:25] we thought gbd4 was so good at
[00:29] conversation
[00:30] Exchange in text that it really should
[00:34] be able to talk to you literally talk to
[00:36] you with your voice so we built a bunch
[00:39] of things like this this is probably a
[00:41] year ago and in geni terms it's ancient
[00:44] ancient history but probably worth
[00:45] looking at as context I'm your friendly
[00:48] chatbot here to assist you with any
[00:50] questions or tasks you have in mind how
[00:52] can I help you today uh can you tell me
[00:54] a
[00:56] joke absolutely why don't skeletons
[00:59] fight each other start with that one
[01:00] give me a different
[01:02] joke all right I'll give it another go
[01:05] what do you call fake spaghetti an heard
[01:07] that one too come on maybe just so we
[01:10] use tell me a joke from you know very
[01:12] early on all the way through today and I
[01:14] think we know all the jokes that all the
[01:16] llms we use regularly uh tell which is
[01:19] funny but not necessarily funny in the
[01:21] same way they were the first time we
[01:22] heard them um so this is sort of a
[01:25] really high Lev schematic of what we're
[01:27] trying to do here right we've got a user
[01:28] on a phone or a laptop they want to talk
[01:32] to their device and then somewhere in
[01:34] the cloud we've got a bunch of gpus that
[01:37] are doing a whole lot of heavy duty
[01:40] compute and we need to talk to those uh
[01:43] that cloud computing resource
[01:46] somehow uh so as soon as you build stuff
[01:49] like the video we just saw a couple of
[01:51] things come very much top of Mind One is
[01:54] speed really matters and the other is
[01:56] architectural flexibility is really
[01:58] really important I'll talk about both of
[02:01] those things today uh let's start with
[02:04] architectural flexibility so that really
[02:08] nice clean diagram gets really messy
[02:10] really fast this is not uh unusual in an
[02:13] engineering software development problem
[02:15] domain uh but I thought I'd kind of make
[02:17] a slide based on like I looked at a
[02:19] bunch of source code I thought about all
[02:21] the conversations I've had with you know
[02:23] my colleagues and our customers and
[02:25] friends who are building this stuff and
[02:26] it turns out you have to at some level
[02:29] kind of be aware of a bunch of these
[02:31] things if you want to build realtime
[02:35] robust voice AI stuff deploy it scale of
[02:37] to production um it's a little bit of an
[02:40] intimidating map we're definitely
[02:41] putting the multi in multimodal AI here
[02:44] all the way from audio processing things
[02:47] like Echo
[02:48] cancellation uh and CPU management when
[02:51] you're encoding decoding audio and video
[02:53] through networking issues like firewall
[02:55] traversal all the way through to
[02:57] building things like retrieval augment
[02:59] generation and Tool calling so that your
[03:01] real world applications are really
[03:02] really
[03:03] useful we can collect that kind of messy
[03:06] map into a few a little bit more kind of
[03:09] uh highle categories um it's worth going
[03:12] through these just really quickly
[03:13] because I think they give you a sense of
[03:14] what that map is so you need really
[03:17] robust and low latency media processing
[03:19] and transport you've got to encode the
[03:21] media you've got to send it over the
[03:22] network that's got to work really well
[03:23] it's got to work really fast um you need
[03:25] really good and fast transcription uh at
[03:28] least until the future of truly
[03:30] multimodal uh audio native models comes
[03:33] which will happen at some point uh and
[03:36] even after that you probably are going
[03:37] to need to go from audio to text for
[03:40] lots of kinds of AI use cases um you
[03:44] have to do lots of real-time data
[03:45] Pipeline and buffer management so uh I
[03:48] think in Discord I've probably maybe 20
[03:51] or 30 times answered the question why is
[03:53] my audio stream not working uh when I
[03:56] did local development on my Mac and then
[03:58] I pushed it to an Intel box in the cloud
[04:00] it's cuz you know Indian issues always
[04:02] get you if you're writing low-level
[04:04] audio stuff but there's a lot of sort of
[04:06] Pipeline and buffer management that
[04:08] comes into play here you want to be able
[04:10] to swap between models for a whole bunch
[04:12] of reasons or use multiple models
[04:14] together uh you generally need to call
[04:16] out to external systems you have to do
[04:18] things like phrase inp pointing which is
[04:20] the fancy academic term for when is the
[04:22] person done talking and when do they
[04:23] expect the AI to talk uh you need to
[04:27] handle interruptions really gracefully
[04:29] and that actually is a whole Rabbit Hole
[04:30] of its own uh people will interrupt the
[04:33] bot uh and you need to figure out what
[04:35] you're going to do and how you're going
[04:36] to handle that and how you're going to
[04:37] maintain State when people interrupt uh
[04:40] you have to do Echo cancellation unless
[04:41] you can convince everybody in the world
[04:43] who's using your thing to wear
[04:44] headphones 100% of the time uh and I've
[04:46] been doing audio video development on
[04:48] the internet for a really long time like
[04:50] our core product at Daily is a web RTC
[04:52] Tech deack so I can tell you that you
[04:53] will not convince everybody in the world
[04:55] to wear headphones all the time uh maybe
[04:58] if you're only deploying to people in
[04:59] like a call center professional context
[05:01] but even then it's pretty tough uh and
[05:04] you need good fast text to speech or
[05:06] voice generation on the other
[05:09] end the good thing is it's a lot but
[05:12] when it all comes together it really is
[05:14] amazing to build with these new gen
[05:16] tools you can build stuff that feels
[05:18] magical and new to people but that is
[05:20] genuinely useful that sort of just feels
[05:22] like how things should be uh we built
[05:26] this is an example of something we built
[05:27] for a Healthcare customer that solved a
[05:28] real pain point I think if you've been
[05:30] to the doctor which I'm sure all of us
[05:32] have you've had to fill out way more
[05:34] forms than you thought you should at
[05:36] subsequent doctor visits and maybe you
[05:38] filled those out on paper maybe you you
[05:40] know got a link to a form to fill out
[05:43] before uh the visit which is like the
[05:45] current state of the art what if an llm
[05:47] could just call you on your phone or you
[05:50] could click a link in an app and you can
[05:51] have a conversation and you never had to
[05:53] fill out a form
[05:55] again hello chat my name is Jessica and
[05:58] I am with Tri County health services to
[06:01] ensure your privacy and to confirm your
[06:02] identity could you please provide me
[06:04] with your birthday including the year uh
[06:07] yes January
[06:10] 1st I appreciate that Chad can you also
[06:13] tell me oh sorry yeah uh
[06:18] 1983 thank you for providing your
[06:20] birthday Chad now could you please list
[06:22] your current prescriptions including the
[06:24] medication name and the dosage for
[06:26] each uh yeah I take my C and also Gaba
[06:32] Penton great could you please provide
[06:34] the dose oh yeah uh sorry 10 Mig and uh
[06:38] 100 milligrams
[06:42] respectively thank you for that
[06:43] information chat additionally do you
[06:46] have any allergies that we should be
[06:47] aware of if so please list
[06:50] them uh yeah I'm allergic to latex and
[06:52] I'm also allergic to penicillin
[07:01] thank you for letting us know about your
[07:02] allergies Chad next part so I think you
[07:05] can see how all those pieces we just
[07:07] talked about are actually necessary to
[07:09] pull together something like that but
[07:11] when you do it feels simple it feels
[07:14] like it's supposed to um that's a real
[07:16] video nothing in there is edited uh the
[07:18] call outs to the external system are
[07:20] mocked they're not it's not actually a
[07:22] real electronic health record systems on
[07:24] the back end but it's it's they're they
[07:26] real tool calling um and that stuff is
[07:29] now started to move into production uh
[07:31] in in the real world so I think in a lot
[07:34] of cases the Gen Frontier is moving very
[07:36] quickly and people are really sort of
[07:38] pulling it uh out of our hands which is
[07:41] super exciting um so let's switch gears
[07:43] a little bit and talk about fast because
[07:45] that's the other really big piece here
[07:47] how fast do we need how fast is fast and
[07:50] also just a quick side note so we're
[07:52] talking there always two kinds of fast
[07:54] when you're talking about engineering
[07:55] things there's throughput and there's
[07:56] latency these days for conversational
[08:00] interactions throughput is pretty okay
[08:03] for all the tools we all use today like
[08:06] llms and other tools can generate
[08:08] content as fast as people can read it or
[08:11] listen to it but what's hard is latency
[08:14] and latency is that sort of time to
[08:15] First Bite time to First token in lots
[08:18] and lots of engineering contexts there's
[08:20] trade-offs between throughput and
[08:21] latency complicated relationships
[08:23] between throughput latency uh one of the
[08:25] graphs that I sometimes show in these
[08:26] talks is that uh throughput tends to
[08:29] improved by an order of magnitude every
[08:31] couple of years in lots of domains
[08:33] latency improvements tend to be linear
[08:35] and like way behind throughput
[08:37] improvements so latency is hard and
[08:39] latency is mostly what bites us here
[08:42] human conversational latency like if I
[08:44] am talking to another person it feels
[08:47] weird to me if that person doesn't
[08:49] respond in about half a second sometimes
[08:51] people respond actually a lot faster we
[08:53] seem as humans to be doing like
[08:56] speculative decoding next token
[08:58] prediction just like natively like
[09:00] that's what we do I know what you're
[09:01] going to say four or five words before
[09:04] you finish saying it I'm queuing up my
[09:06] response I'm sort of doing my inference
[09:08] in this like greedy fashion if you say
[09:10] something I didn't expect well I can
[09:11] like reroute but most of the time I'm
[09:14] right and most of the time if you
[09:15] actually record people in conversation
[09:17] they'll respond in like two or 300
[09:19] milliseconds commonly and if they don't
[09:22] they'll give you some kind of Q so the
[09:25] the sort of 500 millisecond Target is is
[09:27] pretty important because we hit that
[09:28] uncanny Val pretty quickly when we're
[09:30] above it in fact I think that video of
[09:33] my colleague Chad that you just saw if
[09:35] you watched it with a critical eye what
[09:37] I hope you saw was pretty cool
[09:40] orchestration of like state-of-the-art
[09:42] gen stuff and probably slower response
[09:46] times then really should be there uh so
[09:49] we've spent the last couple months I've
[09:51] spent the last couple months really sort
[09:52] of thinking a lot about how to improve
[09:54] these response times and just as a kind
[09:56] of Benchmark like relative uh like
[09:59] another number that shows how hard this
[10:01] is like Gemini Pros time to First token
[10:04] it's like 900 milliseconds so if you're
[10:07] aiming for 500 milliseconds you're
[10:09] already almost double even before you do
[10:12] anything else even before you send stuff
[10:14] you know o over the network for other
[10:15] services or anything so what models and
[10:18] tools you choose are constrained they
[10:20] matter a lot it matters a lot how you
[10:21] string them together um so just to pop
[10:25] up a level again this is what we're
[10:27] trying to achieve and and the most
[10:30] powerful tool we have today for making
[10:34] everything run fast in this domain is
[10:36] actually putting as much together into
[10:38] one compute container as we possibly can
[10:42] so if the if the really really big
[10:44] things we're trying to do are natural
[10:45] language uh speech to text and then
[10:48] phrase inp pointing so when should the
[10:51] bot do processing or talk and then llm
[10:54] inference and then Voice output if we
[10:57] can put all those things together and
[10:59] run them locally and collocated we're
[11:01] like way ahead uh of where we are if we
[11:05] can't do that and this is worth
[11:07] emphasizing because I think I'm sure
[11:10] like 95 98 99% of stuff we're all
[11:13] building today with Gen we're calling
[11:15] out to hosted Services there's a lot of
[11:17] really really good reasons for that uh
[11:20] but that's tough in this domain if
[11:23] latency is what you're prioritizing and
[11:25] latency might not be what you're
[11:27] prioritizing and that's okay like
[11:28] there's lots of different trade-offs you
[11:29] can make but if you're trying to make
[11:31] things really really really fast you
[11:33] need to figure out how to host stuff
[11:34] yourself and how to host stuff in a way
[11:35] where you can tune and control and
[11:37] combine
[11:39] everything um so this is the part of the
[11:42] talk where I like look at the clock and
[11:44] I look out at all of you and I try to
[11:46] figure out how much tolerance you have
[11:47] for me talking about latency because I
[11:50] will maybe ironically we'll talk about
[11:52] latency for hours and hours just what
[11:54] I'm obsessed with as an engineer uh I do
[11:56] think it's worth just quickly kind of
[11:58] going over this this list of like kind
[12:00] of the best you can hope for latency
[12:03] numbers for a typical voice AI context
[12:06] cuz some of them are not obvious so
[12:08] first what are we actually measuring
[12:10] we're measuring the time like what do we
[12:12] really really care about we measure the
[12:14] time I stop talking so if there's like a
[12:17] green waveform on one side and a purple
[12:18] waveform on the other side of this like
[12:20] you know uh audio uh editor um the time
[12:25] I stop talking and then there's some
[12:27] kind of Gap usually silence we could
[12:30] play hold music if it's too long a gap
[12:32] um and then there's another waveform on
[12:34] the other side when I first start to
[12:35] hear the llm talking to me that's the
[12:37] Gap we care about the voice to voice
[12:40] latency and that has to include
[12:42] everything it has to include audio
[12:43] encoding sending stuff over the network
[12:45] all the processing sending stuff back
[12:47] playing it out the speakers so the very
[12:49] first number here is actually kind of
[12:50] shockingly high if you're using the
[12:52] laptop mic on Mac OS it's like 30 40
[12:56] milliseconds of delay there are some
[12:58] good reason reasons for that there's a
[12:59] lot of audio processing again Echo
[13:02] cancellation background noise removal uh
[13:05] gain control all that stuff plays in
[13:07] plays a role here uh as these kind of
[13:10] use cases get more and more important
[13:12] maybe hardware and operating system
[13:13] manufacturers will push this stuff down
[13:15] but today you're sort of 40 milliseconds
[13:17] into your 500 millisecond Target time
[13:19] before the btes ever even get into any
[13:21] of what we think of as software we
[13:23] control um and then you're encoding the
[13:25] audio you're sending it over the network
[13:28] you're doing some packet handl
[13:29] you're reassembling those packets on the
[13:32] other side and what we call a Jitter
[13:33] buffer you're decoding and then you're
[13:36] finally at the like transcription
[13:39] stage if you are really careful about
[13:42] transcription and inp pointing you can
[13:43] probably get down to a couple hundred
[13:44] Mill seconds then you're doing llm
[13:47] inference in this context you're really
[13:49] hoping you can get your time to First
[13:50] token from the llm in maybe another 100
[13:53] milliseconds uh then you're doing some
[13:57] speech uh sorry text to speech
[13:59] and then you're going over the network
[14:01] and out the other side these are real
[14:04] measured numbers sort of medians there's
[14:06] obviously some hand waving because it's
[14:07] hard to measure everything perfectly and
[14:08] there's huge amounts of variation but
[14:10] you're you're at like 600 to 700
[14:13] milliseconds optimistically but
[14:15] realistically in this world so that
[14:17] gives you a sort of sense of where we
[14:19] are
[14:20] um yesterday we posted a demo on Twitter
[14:25] of really trying to drive all this
[14:26] latency down uh and we have like a
[14:30] container that's open source that you
[14:31] can kind of look at and play with and
[14:33] hack on uh that gets you to like the 500
[14:36] to 700 milliseconds of uh
[14:39] latency hello I'm fastbot how can I help
[14:42] you today let's play a geography game do
[14:45] you want to give me some geography
[14:47] questions to answer that's the spirit
[14:50] I'll give you a question what is the
[14:52] world's largest desert oh I think it's
[14:54] the Sahara that's correct the Sahara
[14:57] Desert is indeed the largest larest hot
[14:59] desert in the world covering most of
[15:01] North Africa well done next question
[15:04] which river is the longest in South
[15:06] America it's got to be the uh not the
[15:09] Nile sorry the Amazon no need to
[15:12] apologize you're absolutely right again
[15:15] the Amazon River is indeed the longest
[15:17] river in South America and one of the
[15:19] longest rivers in the world good job
[15:21] next question what is the capital city
[15:23] of
[15:24] Australia
[15:26] canbera correct again canbera is the
[15:28] capital Cap City of Australia you're on
[15:30] a roll next question which mountain
[15:33] range runs along the border between
[15:34] France and Spain
[15:37] pyes exactly right the Pyrenees Mountain
[15:40] Range does indeed run along the border
[15:42] between France and Spain you're really
[15:44] showing off your geography skills here
[15:46] next question what is the largest city
[15:48] in
[15:49] Scandinavia visit
[15:51] Stockholm I think there might be a
[15:53] slight mistake visit.com is not a city
[15:56] but rather a travel website I was trying
[15:58] to
[16:00] Stockholm no worries I knew what he
[16:02] meant and you're absolutely right again
[16:04] Stockholm is indeed the largest city in
[16:06] Scandinavia and the capital of Sweden
[16:09] you're doing great next question which
[16:11] city is the largest in
[16:13] Poland
[16:15] krackow close but not quite Kow is a
[16:18] beautiful city in Poland but it's not
[16:20] the largest the correct answer is wora
[16:23] which is the capital and largest city of
[16:25] Poland OH I feel like I should have
[16:26] known that if we're going to talk about
[16:28] capitals Maybe I'll ask you some
[16:29] questions what's the capital of
[16:32] France I'm ready for a challenge the
[16:34] capital of France is Paris
[16:37] Germany not quite well Germany is a
[16:39] country with no I think what's the
[16:41] capital of
[16:42] Germany good one the capital of
[16:45] Germany's in deep berin and what's the
[16:47] capital of Stockholm I mean sorry what's
[16:49] the capital of Sweden no worries the
[16:52] capital of Sweden is Stockholm what a so
[16:56] the the the idea there was not to do
[16:59] prompt engineering cuz clearly I could
[17:00] have better done a better job on prompt
[17:02] engineering uh but to kind of really
[17:04] test latency and show all the latency
[17:07] numbers in one place because it's useful
[17:09] to visualize stuff and again that UI and
[17:11] everything is open source so the the big
[17:13] number in the middle uh is the the voice
[17:17] to voice latency measured on the client
[17:19] side and then the numbers on the edge
[17:20] are metrics that are being sent from the
[17:22] server that's doing all that work sort
[17:24] of on the individual pieces the
[17:26] measurement sent back so you can sort of
[17:28] see what variation is and correlate and
[17:30] kind of get good intuitions about this
[17:32] stuff um the architecture here is uh uh
[17:36] two models uh by a company called Deep
[17:38] gram uh for the transcription and the
[17:40] voice generation uh that are really good
[17:43] compromises between how good they are
[17:46] and how fast they are and deep gram has
[17:48] a hosted service but they also let you
[17:50] run those models on premises in little
[17:53] Docker containers um and that's llama
[17:56] 38b I think because I could couldn't
[17:59] quite get 70b to run as fast as I wanted
[18:01] it to although in theory that's possible
[18:05] um and I'll post some links uh to this
[18:08] if you want to look at it
[18:10] more so because we solved so many
[18:13] problems over and over uh we thought it
[18:15] would be great to have an open source
[18:16] framework for this stuff it I think
[18:18] we've seen this in other parts of AI
[18:20] landscape things like Lang chain and
[18:22] llama index are really valuable uh this
[18:24] is sort of that for real time and
[18:26] multimodal Ai and this slide looks
[18:29] familiar because I stole the list of
[18:30] hard problems from this slide and made a
[18:33] slide that I moved higher up in the talk
[18:35] here for today um but this is a open
[18:37] source framework called pip cat uh it's
[18:39] gotten a bunch of traction recently uh
[18:41] it's vendor neutral even though it came
[18:43] out of uh work that we've done at Daily
[18:46] early on on this and we're just really
[18:48] excited about this it's super fun to be
[18:49] getting lots of community contributions
[18:51] now and if you are trying to build
[18:53] really fast multimodal AI stuff I think
[18:55] it's at least worth taking a look at you
[18:58] can build things like conversational
[18:59] Bots and speech to speech language
[19:01] translation apps and voice controlled
[19:03] agents of various kinds like that
[19:04] control your software user interfaces uh
[19:08] and real-time Vision model stuff like
[19:10] the awesome last presentation is also
[19:12] like baked into pip cat services now
[19:15] here's all the stuff that's supported in
[19:17] PIP cat today we're adding stuff all the
[19:19] time you can add stuff so if you're
[19:21] interested in building please hang out
[19:24] with us in the PIP cat Discord if you
[19:26] want to contribute a a service plug-in
[19:28] in please do that if you want to be a
[19:30] maintainer for an open source project
[19:32] that's a lot of fun ping me uh
[19:34] maintainers are you know gold in the
[19:36] open source World we're all always
[19:38] trying to recruit great
[19:40] maintainers um and just last slide about
[19:43] the context here so this is the PIP cat
[19:46] star rating list and the day that it
[19:49] went vertical was the GPD 40
[19:51] announcement we are going to get great
[19:54] multimodal models and they'll be
[19:56] incredibly useful they'll make building
[19:57] super fast stuff easier and easier um
[20:00] but a they're not here yet and B we're
[20:02] still going to need orchestration layers
[20:04] for all this stuff um also the the the
[20:07] demo that I showed just a minute ago uh
[20:09] that I posted yesterday is now at
[20:10] 175,000 views on Twitter so there's more
[20:13] and more and more interest in voice Ai
[20:15] and we'd love to have people uh come
[20:17] build with us
[20:21] [Music]
