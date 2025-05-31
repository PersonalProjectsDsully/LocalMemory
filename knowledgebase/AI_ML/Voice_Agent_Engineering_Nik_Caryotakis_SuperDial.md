---
type: youtube
title: Voice Agent Engineering — Nik Caryotakis, SuperDial
author: Channel Video
video_id: 2p2ErKRELHM
video_url: https://www.youtube.com/watch?v=2p2ErKRELHM
thumbnail_url: https://img.youtube.com/vi/2p2ErKRELHM/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence and Machine Learning
tags: ['Voice AI', 'conversational design', 'EHR integrations', 'generative AI', 'AI ethics', 'real-time systems', 'MVP development', 'voice engineering', 'multimodal data', 'conversational content']
entities: ['Superow', 'EHR Integrations', 'MP3s', 'transcripts', 'generative AI', 'voice AI engineer', 'conversational content', 'vertical Integrations', 'AI ethics']
concepts: ['Voice AI engineering', 'multimodal data handling', 'real-time latency', 'conversational design', 'generative AI', 'EHR integrations', 'MVP development', 'AI ethics', 'horizontal voice AI stack', 'build while flying']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['AI fundamentals', 'conversational system design', 'EHR system knowledge', 'Python programming', 'real-time systems']
related_topics: ['AI ethics', 'conversational AI', 'generative AI applications', 'voice recognition technology', 'EHR integration strategies', 'real-time data processing', 'MVP development', 'voice engineering']
authority_signals: ["we've been saying over the past year and a half", 'we did this with a really lean team of four Engineers', 'our favorite classes in college were the AI ethics ones']
confidence_score: 0.8
---

# Voice Agent Engineering — Nik Caryotakis, SuperDial

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=2p2ErKRELHM)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: voice-ai, llms, text-to-speech, conversational-ai, scaling, reliability, agentic-systems  

## Summary

# Summary of "Voice Agent Engineering: Lessons from Super Dial"

## Overview  
Nik Caryotakis from Super Dial discusses the challenges and strategies in building reliable voice agents, emphasizing the importance of conversational design, technical integration, and balancing speed with ethical considerations. The talk highlights how voice AI is evolving, with a focus on practical applications over flashy features.

---

## Key Points  
- **State of Voice AI in 2025**:  
  - Voice AI is advancing rapidly, but challenges like audio hallucinations, latency, and real-time processing remain.  
  - "Speech-to-speech" models are still imperfect, and reliability often takes precedence over realism.  

- **Super Dial's Approach**:  
  - The platform automates repetitive tasks (e.g., insurance claims) by integrating with EHR systems and using voice bots.  
  - A lean team of 4 engineers built a full-stack solution, saving over 100,000 hours of human call time.  

- **Key Challenges**:  
  - Customizing scripts for individual customers while maintaining a horizontal voice AI stack.  
  - Managing real-time latency, async workflows, and multimodal data (audio, transcripts, etc.).  

- **Core Principles**:  
  - "Say the right thing at the right time" and "build this plane while we fly it" (iterative development).  
  - The uniqueness of a voice bot lies in conversational content, design, and vertical integrations, not technical bells and whistles.  

- **Ethical Considerations**:  
  - Rapid development with generative AI raises concerns about bias, transparency, and accountability.  

---

## Notable Quotes  
- *"A boring call for us is an excellent call because it turns out a lot of work is boring."*  
- *"The trickiest part for us is customizing all these scripts and use cases for each customer individually."*  
- *"Ultimately, it’s going to be in the conversational content and the design... that make your agents work actually valuable."*  

---

## Actionable Insights  
1. **Prioritize Conversational Design**: Focus on content, user flow, and domain-specific integrations over technical gimmicks.  
2. **Leverage Horizontal Stacks**: Use modular frameworks to handle common challenges (e.g., transcription, latency).  
3. **Balance Speed and Ethics**: Move fast but ensure transparency, fairness, and accountability in AI systems.  
4. **Embrace Real-Time Constraints**: Optimize for latency and async workflows when building voice applications.  

--- 

## Conclusion  
The future of voice AI hinges on seamless integration with real-world workflows, robust conversational design, and ethical practices. Super Dial’s success underscores the potential of voice agents to transform industries, but highlights the need for careful balancing of innovation and responsibility.

## Full Transcript

[00:00] [Music]
[00:16] hey everyone uh I'm Nick I'm an engineer
[00:19] at Super dial and first of all big
[00:21] thanks to the organizers this event has
[00:23] been awesome I've had a blast talking to
[00:26] you guys connecting with you guys and
[00:27] hearing all these great talks um some
[00:30] I'm one of the few voice AI talks today
[00:32] in this weekend so I have a lot to cover
[00:33] we're going to Dive Right In if you're
[00:35] new to voice AI I hope I can provide a
[00:38] nice little framework to think about
[00:39] this very fast moving space and if
[00:42] you're building with voice AI already
[00:44] I'll be sharing some little anecdotes
[00:46] from our own scaling Journey that I hope
[00:48] will help yours as well so voice AI in
[00:51] 2025 extremely exciting we're seeing
[00:54] these new smart really fast really
[00:56] affordable llms that are supporting a
[00:59] lot more complex conversational use
[01:01] cases uh but you still kind of need some
[01:04] tricks to take your chat agent and turn
[01:06] it into a voice agent we have these low
[01:09] latency really realistic super
[01:11] generative textto speech models but
[01:14] sometimes we have audio hallucinations
[01:16] and we have to deal with things like
[01:17] pronunciation and
[01:19] spelling with all the new things that
[01:21] people are building there's this
[01:23] explosion in voice aai infrastructure
[01:24] and tooling and evaluation systems and a
[01:27] big question becomes what's actually
[01:29] worth owning
[01:30] and the big one on everyone's mind are
[01:33] these new speech to speech or voice too
[01:35] models uh and our take is that for a lot
[01:37] of production applications they're not
[01:40] quite yet ready and a big reason for
[01:43] that is they start to Output things that
[01:45] aren't actually speech aren't actually
[01:48] uh things that you can use to build a
[01:50] reliable conversation and this we saw
[01:52] this when they first came out they were
[01:54] like imitating people's voices and from
[01:56] the start that's why we've kind of been
[01:58] favoring uh reliability over this sort
[02:01] of realism so today I'm going to talk
[02:04] about how we at Super dial approach
[02:06] agents as a service how we think about
[02:09] the voice AI engineer and The Last Mile
[02:12] problem so once you have your little
[02:14] voice uh MVP all the challenges that
[02:17] you're going to face trying to actually
[02:18] make it reliable and put it to
[02:21] work so at Super dial we're in the
[02:23] business of phone calls specifically one
[02:26] of the most annoying phone calls ever
[02:28] that phone call to your insurance
[02:29] company so for Mid to large-sized
[02:33] healthcare administration businesses we
[02:36] sell the super di platform and with
[02:39] super dial you can build your script so
[02:41] design the sort of conversation ask all
[02:44] the questions that you need to get
[02:45] answered over the phone you send us your
[02:47] calls via CSV API or we also integrate
[02:51] with a lot of EHR software systems and
[02:54] then you know within the next couple
[02:56] hours in the next day we send you back
[02:58] your results in a stretched format and
[03:01] this makes for a really interesting
[03:03] agentic contract that we sort of have
[03:05] with our customers so from their
[03:07] perspective they're paying for results
[03:08] they tell us who to call which questions
[03:11] to ask and we tell them the answers
[03:13] internally we have a little agentic Loop
[03:16] set up so
[03:17] that uh we go out we wait for these
[03:20] offices to be open we wait for um you
[03:23] know the call centers to open so we can
[03:25] actually make these calls we will
[03:26] attempt to make the call with our voice
[03:28] bot and then if our voice spot needs to
[03:30] bring in a human to complete the call or
[03:32] cannot complete the call after a certain
[03:34] number of attempts then we send it to a
[03:36] fallback team and this is something that
[03:38] of course we're transparent with with
[03:40] our customers in fact it's a benefit to
[03:42] them because it's kind of inevitable
[03:44] with these Healthcare phone calls that
[03:46] sometimes you need to bring in a human
[03:48] so with us they know that no matter what
[03:50] happens the call will get made whether
[03:52] or not it gets made with a human or a
[03:53] bot doesn't matter to them they get
[03:55] their answers reliably and in a
[03:57] structured
[03:58] format uh and with all these calls we
[04:01] try to do our best to learn from them so
[04:02] we'll update the sort of office hours
[04:04] for the given phone number we're calling
[04:06] and learn from the sort of phone tree
[04:08] traversal that we just tried so when we
[04:10] call it again we get even better at that
[04:12] sort of call and because there are
[04:15] sensitive Healthcare phone calls we want
[04:17] to make sure our system always works so
[04:19] randomly we'll take out some of these
[04:20] calls audit them make sure everything's
[04:23] working uh for a quick little demo this
[04:25] is actually a prior authorization call
[04:28] uh this this is after the point where
[04:30] we've traversed little phone tree by
[04:33] clicking the right buttons and now we're
[04:35] talking to a human and trying to get
[04:37] some questions answered for a customer I
[04:39] know your first
[04:41] name hi this is
[04:44] Sarah are you calling from a doctor's
[04:47] office or from a
[04:48] facility I'm calling from provider's
[04:52] Office do you have a member ID or a case
[04:56] number the member ID is
[05:03] what is the CPT
[05:05] code the CPT codes are
[05:12] 81243 okay hold
[05:15] on so there's a Kon file uh that was
[05:19] initiated for the code
[05:20] 81243 it is pending so this case number
[05:26] is and we have not received any
[05:28] clinicals for this case
[05:33] yet okay what is your name again and
[05:35] what is the reference number for this
[05:38] call my first theme is you may have the
[05:41] pending case number as a call reference
[05:43] number and the fact number on where to
[05:45] send a clinicals
[05:49] is thanks so much for your
[05:53] help you're welcome thanks for calling
[05:55] have a great
[05:57] day so that's it uh if that call was
[06:01] really boring to you
[06:03] than if that call was really boring
[06:06] that's kind of just how these things go
[06:08] a boring call for us is an excellent
[06:10] call because it turns out a lot of work
[06:12] is
[06:13] boring uh so with the system we've been
[06:15] able to save over a 100,000 hours of
[06:17] human Fone and calling time and we're on
[06:19] track to save Millions more in 2025 and
[06:21] what's really incredible about voice AI
[06:23] today is that we did this with a really
[06:25] lean team of four Engineers so building
[06:27] the whole full stack web application
[06:29] these EHR Integrations the bot you just
[06:32] saw all while bringing on new customers
[06:35] supporting new conversational use cases
[06:37] really quickly and a big part of why
[06:39] that was possible was because we really
[06:41] all embraced this role of a voice AI
[06:44] engineer so let's kind of uncover what's
[06:47] unique about a voice engineer today and
[06:49] what hats they may be wearing so
[06:51] starting from switch's like original
[06:53] graft we can kind of see that a voice AI
[06:55] engineer is going to deal with
[06:56] multimodal data so MP3s audio bites in
[07:00] addition to transcripts you're dealing
[07:02] with transcription models voice models
[07:04] speech to speech all that sort of thing
[07:07] the application you're building it's in
[07:08] real time latency all of a sudden
[07:10] matters so much more you're going to be
[07:12] dealing with async and python a lot more
[07:15] than you probably wanted to be doing and
[07:18] the product constraint here is almost
[07:19] always going to be a voice conversation
[07:21] so people have really high expectations
[07:23] of how these sorts of conversation goes
[07:26] uh for us like we're slotting ourselves
[07:28] into an existing uh sort of like
[07:31] business interaction and people expect
[07:34] us to be conversational and fit into
[07:36] that use case so to Grapple with all
[07:39] these challenges we kind of have two
[07:40] sayings at superow that we've been
[07:42] saying over the past year and a half say
[07:44] the right thing at the right time and
[07:46] build this plane while we fly it so the
[07:49] trickiest part uh for us is customizing
[07:54] all these scripts and all these use
[07:55] cases for each customer individually and
[07:57] then we really
[08:00] on this kind of like horizontal voice AI
[08:02] stack to help us out with all those
[08:04] other problems and this is kind of how
[08:06] we think about the voice AI engineer
[08:08] today and its unique roles and in the
[08:13] larger context we're really at this
[08:15] inflection point where it's so easy to
[08:17] build out an MVP for these sorts of
[08:19] applications that ultimately what is
[08:22] going to make your voice bot unique
[08:24] isn't its Voice or its Interruption
[08:26] handling or how realistic it sounds or
[08:29] how it does turn taking ultimately it's
[08:32] going to be in the conversational
[08:33] content and the design there and the
[08:35] vertical Integrations around it that
[08:37] make your agents work actually valuable
[08:40] and if you're like me and your favorite
[08:42] classes in college were the AI ethics
[08:44] ones everything I just said about moving
[08:47] fast building with generative AI could
[08:49] raise a few red uh raise some alarms so
[08:54] it's not hard to imagine how voice AI
[08:57] apps specifically could be biased
[08:59] against
[09:00] people with certain accents with certain
[09:02] dialects or be really spooky when they
[09:04] sound so real and then say weird things
[09:07] so in the US we both like enjoy and
[09:10] suffer from a lack of AI regulation and
[09:13] that leaves the onus ultimately on the
[09:16] AI engineers and leaders in this room to
[09:18] think about these sorts of problems this
[09:20] is not going to be like a talk on like
[09:22] AI safety and ethics but I think for
[09:25] voice AI specifically with how it's such
[09:27] like a new of interaction with
[09:31] artificial intelligence today I think
[09:33] it's really important how we go about
[09:34] building it so for AI Engineers when we
[09:38] go about making tooling and
[09:39] infrastructure choices uh remember that
[09:42] like developing AI should be really
[09:45] accessible and collaborative and the
[09:46] work that AI does should be for everyone
[09:49] and a key part of making sure that's the
[09:51] case is choosing tooling and
[09:52] infrastructure so that a really diverse
[09:54] set of stakeholders can be involved in
[09:56] that process from the start so with the
[09:59] role of the voice AI engineer kind of
[10:01] scoped out now let's dive into some of
[10:03] the last mile problems in voice AI that
[10:06] we've been dealing with so when we
[10:09] started out we had a really scrap
[10:10] together pipeline of like a
[10:12] transcription model and an llm and then
[10:14] a touch to speech model uh this was
[10:16] awesome to get started at but you know
[10:18] we faced a lot of problems very quickly
[10:21] and a lot of what we were learning was
[10:23] not new at all so though the voice
[10:25] agents we see today are better than ever
[10:27] voice UI itself is is not that new so
[10:30] when we were just getting started uh
[10:32] around a year and a half ago I had the
[10:34] chance to speak to Kathy Pearl who is a
[10:37] close family friend and has been working
[10:38] on uh the ux of Gemini she's been in the
[10:42] conversation design game for like 20
[10:45] years or
[10:46] something uh and back in the day like
[10:48] voice UI was lots of phone tree design
[10:51] and then it becomes these Alexa and Siri
[10:53] type things and now we're just in this
[10:55] whole new world but a lot of the
[10:57] principles remain the same and one of
[11:00] the biggest things that's changed with
[11:02] developing voice UI is the shift from
[11:05] prescriptive to descriptive development
[11:08] so we no longer prescribe what we want
[11:09] our bot to do over the course of the
[11:11] conversation by mapping out every
[11:13] possible direction that it could go
[11:16] instead we describe what we want to do
[11:18] and then kind of pray to the Jenner of
[11:20] gods that it
[11:22] happens and for this you know there's a
[11:24] lot of things I talk about with
[11:25] conversation design but it comes up
[11:27] really quickly when that becomes your
[11:28] main interface
[11:30] one thing for us is when we're asking
[11:31] these questions you know should we be
[11:34] really open-ended with it or kind of
[11:36] constrain the user into selecting from a
[11:37] list of choices and for us because these
[11:39] are existing conversations we find it's
[11:42] often better to just go General hope the
[11:45] call center representative gives us a
[11:47] ton of information and then instead of
[11:49] trying to prevent them from saying the
[11:51] wrong thing we try to adapt to whatever
[11:53] they say so Kathy's
[11:56] recommendation was hire a conversation
[11:58] designer
[11:59] if you're thinking about these sorts of
[12:01] problemss there are experts in this and
[12:04] if you're just a voice AI engineer and
[12:06] you want to get started in this kind of
[12:08] thinking a great recommendation is to do
[12:11] little table reads so have one person
[12:14] pretend to be the bot and the other
[12:15] person to pretend to be a user and the
[12:18] sort of like transcript that you may
[12:19] write out by hand
[12:22] immediately the sort of gaps and
[12:24] awkwardness of it comes out when you say
[12:25] these things out loud so knowing all
[12:28] these things we really decided to work
[12:29] on our conversations but we had kind of
[12:32] had to deal with the tech de debt of the
[12:35] orchestration framework that we had
[12:36] built so we really hit our stride when
[12:39] we started using pipe cat for our voice
[12:41] AI orchestration this is an open source
[12:43] framework maintained by the guys at
[12:45] Daily it's really easy to extend and
[12:48] hack upon which is important for our use
[12:50] case when we need to do transfers and
[12:52] stuff um and we make really long phone
[12:54] calls these can be like an hour and a
[12:56] half long so a decision for us in
[13:00] choosing pipat was that we can self host
[13:02] it and deploy it and scale it how we
[13:04] want so with some of our like voice
[13:08] orchestration headaches dealt with we
[13:10] really wanted to get back to focusing on
[13:12] our conversations and everything in this
[13:14] slide for us is really not unique to
[13:17] voice UI uh and AI so I'm going to kind
[13:20] of speed over it two interesting
[13:22] decisions we've made here because we
[13:24] just have you know an LM in the backbone
[13:27] uh we chose to own our own open a
[13:29] endpoint we find this leads to a better
[13:31] interface with a lot of these new voice
[13:34] AI tools so behind our open a endpoint
[13:38] we can kind of route to different models
[13:40] that are maybe more uh latency
[13:42] sensitive for all of our generative
[13:44] responses we route them through this
[13:46] tool called tensor zero tensor zero is
[13:50] relatively new they have this nice
[13:52] framing of llms uh if that quote
[13:55] interests you I recommend you look them
[13:57] up and talk to them they're awesome uh
[13:59] this is like a little open source tool
[14:00] so you can do whatever you want with it
[14:01] they give us kind of stretchered and
[14:03] typed llm endpoints that we can then
[14:06] experiment with in production so that's
[14:08] our gateway to our LM and then all of
[14:11] our logging and observability we
[14:13] self-host Lane fuse and we self-host
[14:16] these things also because these are like
[14:18] healthcare calls we have to be hypoc
[14:19] compliant that's often an easiest an
[14:22] easier way to deal with you know the
[14:24] rapid growth of this space so there we
[14:26] do like anomaly detection evals and data
[14:28] sets
[14:30] so with a good plan in place for our llm
[14:33] sort of work another big challenge is
[14:36] our text to speech system so when you
[14:39] make these sorts of phone calls your
[14:40] password is basically your name your
[14:43] date of birth and then your member ID or
[14:46] something which is like a 12 digigit
[14:48] Long stren of characters that you have
[14:49] to be able to communicate over the phone
[14:52] and something we quickly realized was
[14:54] that what our llm is outputting is not
[14:57] necessarily what we want to shove
[14:58] through through our text to speech
[15:00] engine and neither of those things may
[15:02] actually match what's in the recording
[15:04] so a little example of this and this is
[15:07] like a personal last mile is that if
[15:09] you're building me a personal voice UI
[15:11] application it should say my last name
[15:13] correctly so my last name is pronounced
[15:16] kotus most people and most models will
[15:19] say
[15:19] kotus but with a lot of new tools out
[15:22] there this is the syntax this company
[15:24] called rhyme uses you can spell out the
[15:27] exact sort of pronunciations you want
[15:29] and then for things like spelling where
[15:31] you may have kind of an intuition for
[15:33] like the sort of pauses and breaks you
[15:35] might want to use to say a really long
[15:38] word you can use something like this
[15:40] little spell function um and then with
[15:44] all this stuff like because this is
[15:46] outputting audio btes we usually review
[15:48] recordings to make sure that this all
[15:50] sounds okay in addition to checking the
[15:52] transcripts and to start wrapping things
[15:54] up I have a couple little mini Last Mile
[15:56] problems that we've had to deal with oh
[15:59] and yeah with voice too
[16:01] models all this sort of rule-based stuff
[16:03] gets a little more complicated so some
[16:06] little Min ones uh we used to be called
[16:09] super bill and we called our bot Billy
[16:11] because we thought that was a fun name
[16:13] turns out that's an awful name over the
[16:15] phone because we would constantly have
[16:17] these conversations where people were
[16:18] like hey nice to meet you Billy and we
[16:21] would say it's Billy not
[16:24] Billy so yeah think about your persona a
[16:27] lot dial that in
[16:30] early uh if you're just starting don't
[16:32] build from scratch what's going to make
[16:34] your Bot unique is the conversation and
[16:36] there's so many new tools out there like
[16:38] pipe cat that you can use to get a quick
[16:40] jump start track latency everywhere time
[16:42] to First Bite for each of your little
[16:44] processors is the new most important
[16:46] metric and is something you always kind
[16:48] of have to keep an eye on uh upgrade
[16:51] paths this is a big one for us when we
[16:53] need to make sure we have really high
[16:56] transcription accuracy so we use deep
[16:59] for our speech to text engine and we
[17:01] know that whenever we kind of want to
[17:03] improve that part of our system we can
[17:05] work with them to fine-tune a better
[17:07] model have fallbacks ready it really
[17:10] sucks when open eye goes down for a
[17:12] little bit and all of a sudden all the
[17:13] concurrent conversations you have are
[17:16] just down the drain so have fallbacks
[17:18] ready for each part of your stack it's
[17:20] really easy to set that up with
[17:21] something like tens to zero there are
[17:23] lots of other tools that'll help you
[17:24] figure that out and then end to end
[17:26] testing this is pretty unique for voice
[17:29] UI and or voice AI uh it seems like
[17:33] people are kind of settling on telefony
[17:35] as a boundary layer to test your Bot
[17:38] with like an external
[17:40] service we do a couple different things
[17:42] the easiest test for us is to create a
[17:44] kind of fake phone number that just
[17:46] plays an MP3 if your Bot can't talk to
[17:48] an MP3 then you probably have bigger
[17:50] problems next we can kind of create uh a
[17:53] simulated voice tree with like different
[17:57] uh like phone tree building tools and
[17:59] have our bot pseudo navigate it and then
[18:01] there's lots of generative services like
[18:03] Koval and V where you can have your Bot
[18:05] talk to another
[18:06] bot so some takeaways for a quote
[18:09] unquote vertical voice AI engineer
[18:12] choose your stack wisely the better
[18:14] decision you makes you make here it will
[18:17] allow you to focus on the things that
[18:19] are really truly unique to your
[18:20] conversational experience laser focus on
[18:23] the last mile because this is where
[18:25] ultimately you can provide a lot of
[18:27] value and put your agents to work and
[18:30] then ride the wave there's so much new
[18:32] stuff happening in this space and
[18:34] whenever new models come out you want to
[18:35] be able to use them quickly and you also
[18:37] W want to be able to use them safely so
[18:40] thank you very much I'm excited to talk
[18:42] to you all and hear about what's so
[18:44] special about your conversations
[18:46] [Applause]
[18:48] [Music]
