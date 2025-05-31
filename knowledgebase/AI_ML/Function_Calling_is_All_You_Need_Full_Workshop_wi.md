---
type: youtube
title: Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI
author: AI Engineer
video_id: KUEmEb71vzQ
video_url: https://www.youtube.com/watch?v=KUEmEb71vzQ
thumbnail_url: https://img.youtube.com/vi/KUEmEb71vzQ/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: ['AI', 'machine learning', 'GPT3', 'web search', 'function calls', 'structured actions', 'AI training', 'natural language processing', 'tool integration', 'multi-paragraph completion', 'log props analysis', 'AI research']
entities: ['GPT2 paper', 'GPT3', 'webGPT', 'Meta', 'Reddit', 'calculator', 'translation', 'web search', 'Andes Mountains']
concepts: ['structured actions', 'function calls', 'multi-paragraph completion', 'training models to imitate users', 'AI methodologies', 'text generation', 'log props analysis', 'tool integration']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of AI models', 'programming basics', 'machine learning concepts']
related_topics: ['AI training techniques', 'natural language processing', 'machine learning frameworks', 'tool integration in AI', 'AI research methodologies', 'deep learning models']
authority_signals: ['we trained a GPT3 version of the model', 'this was pretty cool like this is how you we like start to saw...', 'it was actually a pretty clever way where they like looked at the log props...']
confidence_score: 0.8
---

# Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=KUEmEb71vzQ)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai, machine learning, openai, function calling, coding, workshop, language models  

## Summary

```markdown
# Summary of "Function Calling is All You Need — Full Workshop" by Ilan Bigio

## Overview
Ilan Bigio's workshop explores the evolution of language models, emphasizing the role of **function calling** in enhancing model capabilities. The talk traces historical milestones, technical challenges, and innovations in training models to perform structured actions, such as web searches, calculations, and translations, while integrating these actions into conversational contexts.

---

## Key Points

### 1. **Historical Context**
- **GPT-2 Paper (2019):** Introduced multi-paragraph generation with context-aware continuations, like describing "unicorns in the Andes Mountains."
- **WebGPT (2021):** A GPT-3 variant trained to perform web searches via specific functions. Users interacted with the model through an interface, and the model imitated user behavior to generate preferred responses.
- **Meta's Paper (2021):** Demonstrated training models to use arbitrary tools (e.g., QA, calculator, translation) by analyzing log props and retroactively inserting function calls.

### 2. **Function Calling as a Core Capability**
- **Structured Actions:** Models generate not just text but also executable actions (e.g., `calculator_call`, `web_search`) that interact with external tools.
- **Integration into Context:** Results of function calls are parsed and reintegrated into the conversation, enabling dynamic, multi-step reasoning.
- **Training Methods:** 
  - **Imitation Learning:** Models learn by mimicking user behavior on interfaces (e.g., Reddit).
  - **Retroactive Function Insertion:** Models are trained to identify optimal points to insert function calls based on context.

### 3. **Technical Insights**
- **Challenges:** 
  - Ensuring function calls align with user intent.
  - Balancing token limits and computational efficiency.
- **Examples:** 
  - WebGPT's use of a predefined set of functions for web searches.
  - Meta's approach to generalizing tool usage across diverse tasks.

### 4. **Workshop Vibe**
- The talk included humorous anecdotes (e.g., "Why can't you trust an atom? Because they make up everything!") and lighthearted AV issues, reflecting the informal, live nature of the session.

---

## Conclusion
The workshop highlights the shift from pure text generation to models that can **act** via function calls, expanding their utility in real-world applications. Key themes include the importance of structured actions, the evolution of training techniques, and the interplay between human-like imitation and algorithmic precision. The session underscores the dynamic, iterative nature of AI research, where historical milestones and technical creativity shape future advancements.
```

## Full Transcript

[00:00] Cool. Okay, let's get on with it. So, hi
[00:03] everyone. My name is Elan. I'm on the
[00:05] developer experience team at OpenAI. Um,
[00:08] unfortunately, I can't be there in
[00:10] person as much as I would love to. I'm
[00:12] in a wedding in Costa Rica um which is
[00:15] happening later today. So, I just wanted
[00:16] to take this opportunity to just talk
[00:19] through um one of my favorite concepts
[00:22] in maybe all of like AI and language
[00:25] models. So, uh title of this talk is
[00:27] function calling is all you need. It's a
[00:29] talk workshop. There's going to be um a
[00:31] lot of coding. Please save your
[00:33] questions. No, I'm kidding. Like just
[00:35] interrupt at any point. Uh we have a
[00:37] Slack. Send them here. Um yeah, just
[00:40] send them at any point. Uh and if you
[00:42] want to like unmute yourself and or
[00:44] raise your hand, I'll call you off like
[00:45] as we go. The idea is to keep this super
[00:47] super dynamic. Um since we have a bit of
[00:51] time, um I'll be fielding a lot of like
[00:53] questions and requests and trying to be
[00:55] coding as much as
[00:56] possible. So yeah, this talk is going to
[00:59] need some lecturing uh a lot of coding
[01:00] from scratch and then some debugging
[01:03] hopefully not a lot. Uh so this is a
[01:06] little bit of what the uh workshop is
[01:08] going to look like. We're going to go
[01:09] over a little brief history of the tool
[01:11] formers of of I'm sorry of function
[01:14] calling. Um then do a little crash
[01:16] course on function calling. Um talk
[01:20] about just agents how they're just
[01:22] loops. How rag workflows and more are
[01:24] just function calls delegation and
[01:25] asynchrony. couple random things I found
[01:28] and then we're going to do a Q&A. Um, if
[01:31] you just want to see like the meat of
[01:34] it, this is pretty much it. We're going
[01:35] to do like this is everything I want to
[01:38] talk about uh and everything that we're
[01:40] going to implement. So, this is uh just
[01:42] a little bit
[01:44] upfront. Great. So, a little history.
[01:47] Um, if we look at the abstractions and
[01:49] sort of patterns that we managed to do
[01:52] with language models, it started as text
[01:54] completion, right? like the original GPT
[01:56] uh and the GPT2 and the GPT3 were all
[01:59] just base models where you gave them
[02:01] some input text. Um and then they would
[02:03] just continue the sentence. Um this was
[02:06] at the time really really like
[02:08] interesting. This was the first time we
[02:09] were able to do like very like uh
[02:11] English sounding like real sounding
[02:12] language. Um but getting it to follow
[02:14] instructions was pretty hard. So if any
[02:16] of you were testing this back then you
[02:19] might remember how setting up a chatbot
[02:21] was um non-trivial, right? you had to
[02:24] like get it to answer questions. But if
[02:25] you just say like, you know, what is the
[02:28] best way to uh get to the like park or
[02:31] something, it would continue
[02:34] like like what is the best way to get to
[02:36] the park? Um that is what Sally said
[02:38] yesterday, right? And you wouldn't
[02:39] actually get a a response. Um so you had
[02:42] to like structure it in a way where you
[02:43] would say like this is the question,
[02:44] this is the answer question answer few
[02:46] shot and then give it. Um then they
[02:48] introduced uh I think this was actually
[02:50] us. We introduced uh function um
[02:52] instruction following with uh instruct
[02:55] GPT. Now you could give it some input uh
[02:57] and it would actually do what you're
[02:59] asking as opposed to just completing. Um
[03:02] finally we started to introduce this
[03:03] notion of like users and assistants and
[03:05] roles. Um and this was all done through
[03:08] through post training where you actually
[03:09] gain these personas. Um and then finally
[03:12] uh we we eventually landed on this like
[03:14] you can give it additional tools um in
[03:17] order to do like external um any like
[03:20] interact with external states. So this
[03:23] is what the previous playground used to
[03:24] look like. But as you can see there's no
[03:26] chat. This is just like a window and
[03:28] it'll complete. Now looking over at like
[03:32] the original papers which is pretty
[03:34] interesting. Um, one of the first times
[03:36] that we actually started to do this like
[03:38] function calling was through this web
[03:40] GPT um, which was this uh, version of
[03:43] GPT3 that we trained to be able to um,
[03:46] Elan, I have to cut in here a little
[03:48] bit. We got the Zoom working. Yay.
[03:51] Sweet. Um, all right. We're going to cut
[03:53] over in the audio. So, can everyone hear
[03:55] Elon when he speaks? Elon, say
[03:58] something. Hello. Hi, everyone.
[04:02] Hello. Hello.
[04:04] How's it going? Okay. So, so we're going
[04:06] to cut over a little bit in terms of
[04:08] like um people having their own personal
[04:11] audio situation going on. So, you can
[04:13] mute your machine. You should be able to
[04:14] hear it on the room uh audio, whatever
[04:18] you want to do, but you can also
[04:20] obviously connect. But, uh yeah, now we
[04:22] have him on the big screen. So, okay.
[04:24] Yeah. Uh let's let's keep going for a
[04:26] bit. I I'll cut in again if there's
[04:28] audio issues or maybe you want to say
[04:30] some test words.
[04:32] Uh, you're all great. Thank you for
[04:34] coming. Can we bump up the audio?
[04:37] Where's the guy?
[04:40] [Laughter]
[04:44] It's not a conference if you don't have
[04:45] AV issues. Okay. Uh, it's it's still too
[04:47] soft. We can't we can't hear you. Um,
[04:49] I'm going to try and bump up the audio.
[04:50] I'm so sorry.
[04:53] I'll put up a more interesting slide in
[04:55] the meantime. You guys can look at this
[04:56] while we figure this out.
[04:58] Where's Where's the video?
[05:03] Hey. Um,
[05:22] so anybody got uh good jokes?
[05:29] Maybe I always find a joke.
[05:33] It's always the same
[05:35] one. I think it's uh What is it? Why did
[05:40] the No, I had it. I had it here. Wait,
[05:43] wait, wait, wait, wait, wait. There we
[05:44] go. Why can't you trust an atom? Yeah,
[05:47] because they make up everything.
[05:50] These are all real, by the way. And for
[05:52] for those who like have a keen eye, the
[05:54] first one is like actually from the GPT2
[05:56] paper. Um we like gave the model this
[06:01] like description of like unicorns in the
[06:03] Andes Mountains. And that was like the
[06:06] big like first time that it was like
[06:08] doing multi- paragraph completion like
[06:11] continuations that referenced earlier
[06:13] parts of the
[06:15] conversation. It's cool stuff. It's cool
[06:18] history. Can you guys hear me?
[06:22] I feel like some people are having a
[06:24] great time. Some people don't know
[06:26] what's going on. Can like I don't know.
[06:29] Am I good to keep going or should I keep
[06:30] waiting? Uh I think I think you're good.
[06:33] Okay, great. Great. I do think this is
[06:36] the vibe of the whole talk by the way.
[06:38] There's it doesn't get more structured
[06:39] from here. Um okay, so as I was saying,
[06:44] uh we did like this web GPT paper. Um,
[06:47] essentially we trained a GPT3 version of
[06:49] the model uh or like a GP3 model to be
[06:52] able to use this like this very specific
[06:55] set of functions um to do web search.
[06:57] And this was like back in 2021. So
[06:59] really we had like webg a long time ago.
[07:01] Um but this is like one of the first
[07:03] times or maybe the first time that like
[07:05] we were having like it's not just
[07:06] generating text but it's generating
[07:08] actions and then we're parsing those
[07:09] actions and then introducing it back
[07:11] into context so it can use the responses
[07:13] itself. Um, and how we trained it there,
[07:17] um, there's like these these like, you
[07:19] know, clever ways of like we we
[07:21] essentially gave people, uh, an
[07:23] interface and let them do the searching.
[07:25] Um, and then I think we took it like
[07:27] Reddit um, yeah, explain like five. Um,
[07:30] and then just like had people complete
[07:32] tasks and they could use these commands.
[07:35] And so we taught the model and this was
[07:37] GPT3, right? Um, how to essentially
[07:40] imitate users behavior and then produce
[07:42] responses that were preferred. Um and
[07:44] and this was pretty cool like this is
[07:45] how you we like start to saw um to see
[07:49] like this uh this use of like structured
[07:52] like actions essentially. So but this
[07:54] was very specific right we were training
[07:56] like very specific um tools. So then you
[08:00] might be familiar with this paper. This
[08:02] was from Meta at the time. Um where they
[08:05] essentially had a way to teach the
[08:07] models how to use any tools. Um and they
[08:11] taught like they they used a few tools.
[08:13] I think it was like QA calculator. Um
[08:16] what was this like translation? Um
[08:18] couple other couple other tools. But um
[08:21] it was actually a pretty clever way
[08:22] where they like looked at the log props
[08:24] at each spot to like see where it was
[08:27] like best suited to like retroactively
[08:30] put in a function call given some like
[08:33] completion. Um so here we can see a few
[08:35] examples like um essentially it's like
[08:38] if you have a calculator call if you
[08:41] insert a calculator call that like you
[08:44] know it'll it'll insert the um the
[08:47] actual call to the calculator which then
[08:49] you know you're pretty familiar at this
[08:50] point will get the answer if you insert
[08:52] it in the right spot in the sentence it
[08:54] actually reduces the perplexity of the
[08:56] sentence. Um, and so they didn't
[08:58] actually have a lot of human-labeled
[09:00] examples or I think it was just a few,
[09:02] but it was uh really cool because it was
[09:04] this way of like um it could learn to
[09:07] use uh any of these tools through this
[09:10] like crazy like log props technique.
[09:13] Um and it was uh I was pretty excited
[09:16] when I saw this paper. Now this is like
[09:18] how it learns to use any of these tools.
[09:20] Um, but then finally, uh, in June of
[09:23] 2023, uh, OpenAI launched just general
[09:26] function calling where we essentially
[09:28] like pre-trained it to be able to use
[09:29] these tools or actually post-trained it
[09:31] to be able to use, uh, tools. So now you
[09:33] don't actually have to like give it like
[09:35] you can give it examples, but uh, we
[09:37] just showed it like this like syntax in
[09:39] with functions that we still use today
[09:41] and it's just able to call functions. So
[09:43] this is a brief history of of function
[09:45] calling. Um, and my I guess my argument
[09:50] is this is really most of what you need
[09:53] for all the exciting stuff that's
[09:54] happening today. Um, there's there's
[09:57] obviously like additional like systems
[09:59] you can use and like um more post
[10:01] training you can do, but fundamentally
[10:03] like functions are so so so powerful and
[10:05] we're going to look at a few cases
[10:06] today. Um, I'm going to try to keep an
[10:08] eye on questions, but
[10:12] um
[10:14] yeah. Okay, I think you're good so far.
[10:17] Cool. Cool. So, let's do a super quick
[10:19] crash course on function calling. Uh,
[10:22] two main purposes and I'm ripping a lot
[10:23] of this from the docs. So, um, there the
[10:27] fetching data, right? Reading APIs,
[10:28] retrieval, memory, or taking action, any
[10:31] APIs you can use to write, managing
[10:33] application state, which is actually
[10:34] pretty overloaded. That can be like UI,
[10:36] front end, backend, whatever you want.
[10:39] And then workflow actions, which is um
[10:42] any like multi-step processes or even
[10:45] like meta actions like switching its own
[10:48] prompt or like loading in different
[10:49] tools or like handing off a
[10:51] conversation, right? Um so this is also
[10:54] a diagram straight from the docs, but um
[10:57] I'll quickly brush past this. I'm going
[10:59] to assume like most people have at least
[11:00] seen this, but here it is. It's uh you
[11:03] you essentially tell the model which
[11:04] functions you you want it to be able to
[11:07] use. Um and you also provide like
[11:09] whatever the user input is. Um the f the
[11:12] model tells you what it wants to do with
[11:14] that function but it doesn't actually do
[11:15] it. This is one of the like a big
[11:17] sticking point function calling. It
[11:18] doesn't actually use the function
[11:20] itself. It tells you like it tells you
[11:22] the intent of what it wants to do with a
[11:24] function. You are then responsible for
[11:26] parsing that, executing the code, doing
[11:28] whatever you want with it and then
[11:29] providing the result back to the model
[11:32] and then the model can use that respon
[11:34] like result in uh in the generation. Uh
[11:37] take a look at a quick question
[11:39] here. Oh no, it's just it's just swings.
[11:43] Okay, cool. Um these are just a few uh
[11:47] best practices. This is all taken from
[11:48] the docs as well. Um you want to write
[11:51] clear functions. An important one is you
[11:53] got to apply software engineering best
[11:54] practices when you write these
[11:55] functions. So, um, you know what? Maybe
[11:57] I'll pull up the docs for
[11:59] this.
[12:05] Um, so there's a lot of big text, but
[12:09] essentially,
[12:10] um, this is a lot of value here. I tried
[12:13] to pack as much like useful information
[12:15] here as I could, so I'm going to quickly
[12:16] go over it, right? Um, you had to
[12:18] explain the purpose of each parameter,
[12:20] use a system prompt, and include
[12:21] examples. That's, you know, pretty
[12:23] pretty like not non-controversial. Um,
[12:27] software engineering best practices is a
[12:29] little bit uh more interesting, right?
[12:31] You got to make functions obviously
[12:32] intuitive and they got to follow the
[12:33] function of lease principle. Um, like if
[12:36] you give this to a person and they don't
[12:38] know how to use it, then the model might
[12:41] not either, right? Models are getting
[12:43] smarter than us, but still you got to
[12:44] make it uh got to make it easy. Um, also
[12:48] you got to use enums and object
[12:50] structure to make sure that like you are
[12:52] not letting the model make invalid
[12:54] calls, right? Um like here you you have
[12:57] this like toggle light uh um function
[13:02] that takes in like two two boolean
[13:03] params and like obviously like this is
[13:05] pretty wrong but um there's actually
[13:07] many many more like subtle cases where
[13:11] um like the you can like you're letting
[13:14] it represent invalid states.
[13:19] Um okay, still no questions. It's Swixs.
[13:23] Okay. Um, great. And then there's Sorry,
[13:28] there are a couple questions in the
[13:30] professor convers. I see. I see.
[13:36] Um, here maybe let me see if I can pull
[13:38] up the
[13:40] Slack. Okie
[13:44] dokie. Between functions and tools in my
[13:46] opinion. Hey Sam. Yes. Um I I think
[13:50] we've all been kind of like gravitating
[13:53] toward functions and tools as like the
[13:56] two main ways. Originally it was just
[13:58] functions. Tools was like later we
[14:00] renamed it. Um I think now uh and the
[14:04] way that I tried to specify in the docs
[14:06] is functions are like the the raw
[14:09] function calling right like you provide
[14:11] an interface and you're responsible for
[14:13] executing the code. um tools and this is
[14:16] sort of how we treat it in our API is a
[14:18] superset of functions. Tools include
[14:20] functions but it also includes things
[14:22] like um code interpreter or file search
[14:26] or any of these like um like hosted
[14:30] solutions. I'd say this is not be like
[14:33] end all beall definition but this is a
[14:35] definition that we've adopted right
[14:36] there's like tools which are like hosted
[14:38] tools uh including functions and then
[14:40] functions as a subset. Cool. Maybe we
[14:43] can just jump into it. Um, if people
[14:45] have questions on this, happy to happy
[14:47] to feel them as well. But I kind of want
[14:48] to get coding. Okay. Uh, when you start
[14:52] to approach dozens or hundreds of
[14:53] functions, what technically should we
[14:55] apply in order to effectively tool
[14:57] call permissions is one technique. Okay,
[15:01] interesting. And then question two, when
[15:02] you require one tool to provide inputs
[15:04] to another, I have seen tools become
[15:06] layered. How should a reasoner hardcode?
[15:08] Great. Okay, these are actually great
[15:09] questions. And um I think to to answer
[15:12] them, I might I might like do a little
[15:15] hack and like uh use some existing uh
[15:19] code. I'm going to use swarm for a
[15:21] little bit of this um because it does
[15:24] some nice function calling. Actually,
[15:25] no, you know what? I'm going to get to
[15:27] these fun uh in a second. Um let's just
[15:29] go straight into the uh and as always,
[15:33] we should start from the docs.
[15:38] Uh, cool. Uh, so this is where I always
[15:43] step in. Can you zoom in on screen every
[15:46] single page? Yeah. Yeah. Bigger.
[15:51] Yeah. Yeah. Sorry. I always do. Yeah.
[15:56] Yeah. No, this is a good call out. Uh
[15:58] and then I think
[16:01] the terminal
[16:04] here should be good.
[16:08] Okay, sweet. Uh we have we have a
[16:11] function. Great. Um and
[16:17] then just run
[16:20] it and we have uh the function call.
[16:24] Right now we're not handling it yet. So,
[16:27] this is where like I might skip ahead a
[16:30] little bit um and start doing some of
[16:32] the like agentic stuff. But first, uh
[16:35] first off, uh we we got to have a right
[16:39] like you know you you I can sort of hear
[16:41] myself. Um I think so. There we go.
[16:45] Perfect. Okay. So um I think the idea
[16:49] here is like let's make a very very very
[16:52] simple like uh input loop
[16:55] like let's do uh while you also light
[17:00] mode
[17:02] light mode
[17:04] Jesus okay
[17:06] sure I'm just very experienced at this
[17:10] we go
[17:12] well that's the least painful this is
[17:15] good right this works
[17:18] Yeah. Oh, my poor eyes.
[17:22] Um, actually, maybe I I I can't quite
[17:25] see the room, but show of hands, like,
[17:27] who has used or implemented function
[17:29] calling in the past, and someone's going
[17:32] to have to gauge this for
[17:36] me. Okay, it's everyone. Great. I'm
[17:39] going to skip ahead a little. There's
[17:41] like 10
[17:42] 20% 20% that hasn't done it. Okay, 103%.
[17:47] Um the important part that you have to
[17:49] know is you can define the function um
[17:52] schema, right? Then the tool will
[17:54] specify what you want. And then in this
[17:56] case, you know, if I have like
[18:00] a get weather tool. Actually, I'm going
[18:03] to grab this from the docs as well. When
[18:05] in doubt, just go to the docs. You know,
[18:08] it's always good.
[18:11] So, step one. No, this is all node.
[18:15] Yeah. And this will be useful for later
[18:17] too.
[18:19] Um, step one, call the
[18:22] function. Step
[18:24] two, execute your code. Right? So here
[18:27] what we're doing is we're taking we're
[18:29] parsing out what the what the function
[18:31] told us. We're parsing out the args and
[18:33] then we're calling this get weather
[18:34] function which we don't have yet. Um,
[18:37] but conveniently it's up here, right? So
[18:39] we have it up here. get weather
[18:44] requests and then the last step is we
[18:48] provide the result back to the model. Um
[18:53] uh provide the result back to the model
[18:54] and then ask for a completion. Right? So
[18:56] just in order specify the tools, call it
[19:00] the first time, get the tool calls,
[19:01] parse them out, call the function,
[19:03] append and do that. Right? So if we do
[19:06] that and we just add maybe
[19:10] like add I'm going to do this by
[19:13] hand. Why not? Yeah. So I'll print the
[19:18] completion here sort of by hand and then
[19:20] print the last
[19:23] completion. Then what we can see is
[19:26] we'll get the first one that includes a
[19:29] tool call. It'll call the actual
[19:31] temperature uh call the weather API and
[19:33] then we'll get a
[19:37] response and then it says the current
[19:39] temperature in Paris is something I
[19:41] can't see it because of Zoom. Um cool.
[19:44] So this is like the very very basic
[19:47] setup for a function calling. Let's take
[19:49] a step forward. So this is an agent uh
[19:52] very very very basic implementation of
[19:54] an agent um that I'm going to go through
[19:56] really really quickly cuz we're going to
[19:58] start using it. This is very familiar to
[19:59] what you'll see in Swarm or any of the
[20:03] other like like basic frameworks. Um but
[20:06] the idea here is in uh as you can see
[20:10] like in the original one essentially
[20:12] like when it had a tool call I wanted to
[20:14] provide it back. So what I do here is
[20:17] while like just keep looping and this is
[20:20] like the very famous like agents are a
[20:22] loop. This is this is that loop.
[20:24] Um, specify the
[20:26] tools, call the model, get the message,
[20:30] print it out, handle the tool calls,
[20:33] append it, and once we have no more tool
[20:37] calls, break. This is the whole loop. I
[20:39] called it run full turn in my head. One
[20:41] turn is just like you let the model do
[20:43] everything. Um, and then we have this
[20:46] like execute tool call, yada yada,
[20:48] whatever. Um, so now we can use this.
[20:58] So
[21:01] agents
[21:04] py did I export
[21:16] it. There we go.
[21:25] I love it. Okay, so now we're just going
[21:28] to specify
[21:30] one. Um, you know what? Yeah, we um and
[21:35] we'll we'll do it we'll do it with a
[21:36] with a simple
[21:41] loop. So we have this that and we have
[21:46] this. Okay. So now we can just do Asians
[21:49] run full turn. The one other thing that
[21:50] I'm adding here that I didn't show is um
[21:53] this simple utils
[21:57] uh that defines this very very very
[21:59] useful function. So functions to schema
[22:02] essentially takes in a raw python object
[22:04] function and then provides it into the
[22:07] uh like correct schema um so that you
[22:11] can just define functions directly and
[22:12] this is the same thing that we have in
[22:14] swarm and there's an a few other
[22:15] frameworks now as well um so as an
[22:18] example we can do like you know get
[22:20] weather and I'm just going to like you
[22:23] know return
[22:25] 20 like
[22:28] degrees Celsius
[22:34] Right. I'll do that
[22:39] here. Then I'll have my
[22:42] messages and
[22:47] messages. Is this emergency reference? I
[22:50] think it is.
[22:58] What did I call
[23:03] it? Oh. Oh.
[23:06] Oh, I see. This is not part of
[23:09] the Asian
[23:18] class.
[23:25] Cool. So, it called the weather, printed
[23:27] it out, uh, gave us a nice little
[23:30] completion. Um, this is essentially what
[23:32] we want to see. If I say, um, and then I
[23:36] can just keep keep going, right? So, we
[23:38] we we have this basic um basic loop. Um,
[23:44] now let's get back to the presentation
[23:46] real quick. That was like a very very
[23:48] immediate crash course. Now let's let's
[23:50] get interesting. Um and and just for
[23:52] convenience, I'm going to like pivot to
[23:54] the swarm implementation. Um the main
[23:57] reason being it's pretty much the same.
[23:59] Um except we have like some convenient
[24:01] uh like looping tools. So
[24:06] uh swine imports
[24:11] agents and then
[24:22] There we go. So now we can
[24:24] do a simple agent and run a demo loop.
[24:28] And let's see this work.
[24:45] Um we have this very basic setup. Let's
[24:47] do everything now. So
[24:50] um another show of hands. How who here
[24:53] has implemented uh
[24:56] rag? Okay. What about
[24:59] memory? Okay. Fewer. And then what about
[25:02] like you know multi multi-step things
[25:04] and
[25:06] workflows? Cool.
[25:09] Um how about this? There's a lot of
[25:11] stuff we could talk about, but I want to
[25:13] keep this valuable to you all. Out of
[25:15] this list, can you like just type in the
[25:18] Slack what you wanna what you want to
[25:20] see and I can just change the order in
[25:21] which we'll cover this. Um because
[25:23] they're pretty they're pretty
[25:24] interchangeable. We can we can build up.
[25:26] Um but essentially there's there's more
[25:28] interesting
[25:29] things later on, but I want to make sure
[25:32] we we can build up to them. So, just uh
[25:34] if you can pull up the Slack and just
[25:37] dump in, you know, what you're
[25:38] interested in
[25:47] seeing. Okay. Lots of memory. I see.
[25:54] Um function generation from the docs.
[25:56] Delegation async. Okay.
[26:00] build
[26:02] delegation and random cool stuff. I will
[26:05] get to the random cool stuff.
[26:09] Um, okie dokie. Back to light mode. Um,
[26:15] yeah, let's start with like a very very
[26:16] basic form of memory, right?
[26:19] Um, how would we how do we do this?
[26:22] Let's see. Honestly, like we can have
[26:27] um just a list, right? Memory can just
[26:31] be this list. And I'm going to implement
[26:32] this similar to how it's done in
[26:34] chatbt. Um but ju just to show like I
[26:37] think the whole point of this talk is
[26:38] like this workshop is like doing things
[26:40] from first principles and just really
[26:44] removing the complexity. I think there's
[26:45] like a lot of like not fake complexity
[26:47] but like added complexity on things that
[26:49] like doesn't really need to be there a
[26:51] lot of the time. like concepts are a lot
[26:52] more simple and it's all about function
[26:54] calling. So,
[26:56] uh we can do you know add like add to
[27:00] memory and I'll append it and then get
[27:04] memory. Uh like this is super super
[27:07] simple.
[27:10] Um is this is this good enough? Let's
[27:13] see. Maybe maybe. And so what we can do
[27:18] is give it the tools. Let's see and then
[27:21] what when will we want to use them?
[27:23] Let's say you like I can just say so
[27:26] this comment is going to be used as the
[27:28] uh string uh as the as the description
[27:31] in the function. So you can say like you
[27:33] know like when the user tells you
[27:36] something like
[27:41] factual
[27:43] about
[27:47] themselves their life
[27:50] or I can't see anything okay or
[27:55] their
[27:56] preferences call this function
[28:06] um memory. Um and we'll add a couple
[28:09] more cool things like
[28:11] expiration, which is one that I've kind
[28:13] of wanted to add for a while. So, you
[28:16] know, for now, let's say false
[28:21] um memory.append
[28:25] uh think
[28:31] And then we
[28:32] have I guess what we call it uh you know
[28:36] memory
[28:40] text and we can say you know keep the
[28:43] memory text short size. Great. Cursor
[28:46] knows what I
[28:47] want. And then we can just return maybe
[28:56] like this is a super super super naive
[28:59] implementation. Um, but now, uh, when we
[29:03] start off, I guess we could
[29:05] even start off with
[29:08] [Music]
[29:12] a I mean, this is going to be kind of
[29:14] hacky, but I can just like um in your
[29:18] first
[29:20] turn always call get memory. This is not
[29:24] uh great. It's just because of the demo
[29:26] loop. But maybe I'll break I'll break
[29:28] the demo loop out so we can actually do
[29:29] this by hand. But
[29:32] so how how could we prove this?
[29:38] Um maybe let's say like you know write
[29:42] this memory bank or
[29:45] like keep this memory bank in a local
[29:50] file JSON file read it in
[29:55] at
[29:56] beginning and write it out at every
[30:09] Nice. Okay, I trust this. Shall we test
[30:12] it out? So,
[30:15] wait, someone
[30:20] uh Okay, we got the memory memory. Can
[30:23] any can anyone see any
[30:25] bugs? Because we're about to test this
[30:27] out. So, we got the loop. It's going to
[30:28] call it um and maybe like
[30:33] let's
[30:38] memory. Okay. Sure. Yeah. Let's try it.
[30:42] Let's try it out. See what
[30:43] happens. So,
[30:50] hi. Did I not give it the functions?
[31:00] Is it hallucinating
[31:02] this? Oh yes, because I think we called
[31:05] it
[31:09] functions.
[31:11] Hi. There we go. Okay, so called get
[31:14] memory. There's nothing there. I can
[31:16] just say like um I am 6 feet tall
[31:21] despite what people think.
[31:26] Uh, cool.
[31:28] Uh, so now let's just check, right? It
[31:31] should have written this out. There we
[31:32] go. So now we have it in the memory
[31:33] bank. So now I can actually uh end this,
[31:35] right? And then be like, you know, uh,
[31:39] how tall am
[31:42] I? Tada. We've implemented memory,
[31:45] right? There's a Yes, I'll take a clap.
[31:47] I saw Louis Lewis, you're like my proxy
[31:50] for the Luis uh Luis Costa, you're my
[31:53] proxy for the audience. You're like the
[31:54] only person I can really see. So, please
[31:56] don't uh turn off your camera. Um,
[32:00] amazing. Now, we can do more interesting
[32:01] things, right? We can
[32:04] uh if we want do a little bit like smart
[32:07] querying uh where instead of just like
[32:09] loading in all of the memory, um we can
[32:12] like do a little bit of like retrieval
[32:15] uh to load in the right ones. um and use
[32:18] like semantic similarity or use some
[32:20] kind of search.
[32:22] Um I I could try to implement that. Um
[32:25] that might take a little bit longer but
[32:27] not that long. But I do want to pause
[32:29] here. See like given this and like this
[32:31] is going to be the style of things that
[32:32] we do like what um what do we want to
[32:35] see next? I can just keep going with
[32:37] this example. I can pivot. Uh it could
[32:39] be fun just to keep building on this.
[32:40] See how far we can
[32:42] get. Let's see.
[32:49] uh delegation async have it chat and
[32:52] work in the background. We'll get there.
[32:53] We'll get there. I got that working this
[32:55] morning on Python because I didn't want
[32:57] to switch to to Node yet. Uh delegation
[33:01] async.
[33:02] Okay. Let's get into delegation
[33:05] then.
[33:07] So, there's a few different ways we can
[33:09] do this. I'm actually going to leave the
[33:11] memory and we're just going to keep
[33:12] building in this on this on this agent.
[33:14] Uh, and I am using the swarm agent just
[33:16] cuz I didn't want to debug the one that
[33:18] I implemented. But like if we actually
[33:19] look at what this is, um,
[33:22] like it is very very very simple. And
[33:26] then the like run demo loop itself is
[33:29] like uh just printing out
[33:33] messages. Um, and what it's doing is
[33:36] like appending client.run whatever. And
[33:38] like if we look at this client.run run.
[33:41] Um, if it doesn't stream, it essentially
[33:43] does exactly what we did before, like
[33:45] keeps looping, get the completion, throw
[33:48] the messages in,
[33:50] uh, append them, handle responses, etc.
[33:53] There's a couple more things around
[33:54] context and handoffs that we like don't
[33:57] don't really have to look at today. Um,
[33:59] but we
[34:00] can.
[34:02] So, cool, we have memory. Let's do
[34:05] delegation.
[34:07] Um, so there's a couple ways we can do
[34:09] this, right? Um,
[34:11] there's if you think of like functions
[34:13] and agents and and everything you can,
[34:16] um, maybe I'll skip to this
[34:18] slide. Skip skip skip
[34:21] skip. These are like a few of the forms
[34:23] of like agents on delegation that people
[34:26] might be familiar with. We have
[34:27] handoffs, which is like the swarm style.
[34:28] You take a conversation and fully swap
[34:30] it to a different agent. Um, and what
[34:33] that means is just like replacing the
[34:34] system prompt, replacing the tools. Um,
[34:37] you can have nested calls which are the
[34:39] easiest to implement and like often
[34:40] somewhat overlooked. Um, and then you
[34:43] can have manager tasks that's more
[34:46] async. Uh, we will get to that today.
[34:50] So, let's do a very basic one, right?
[34:52] Let's say I want to do like
[34:57] um maybe let's give it a chance to like
[35:00] call a bigger model to do a harder task,
[35:03] right? So we can say like you know uh I
[35:06] can delegate to smarter
[35:11] model and and I'm going to give like
[35:14] task
[35:20] description.
[35:21] [Laughter]
[35:24] Um so I'm laughing because this is
[35:26] saying like it's just going to make it
[35:28] smarter by telling it to be smarter.
[35:29] That's not despite how well that would
[35:31] work. Usually we're not going to do
[35:33] that. So we're we can just make an API
[35:36] request directly. Actually, let's just
[35:38] do that. Let's just do that. So um let's
[35:42] do from OpenI client. And here we could
[35:47] do client chat completions create. Let's
[35:53] call
[35:55] 01.
[35:56] Um I won't provide a system message. I
[35:59] think that's okay. content is the
[36:01] description. Look at that. And we did
[36:04] it. So now
[36:09] um man, I love cursor. Okay, did
[36:12] everyone catch all of that? By the way,
[36:14] all we did was like implement this this
[36:16] function that calls opening API and then
[36:19] here. So now I can say like uh so now I
[36:21] can add a bit of a description here. I'm
[36:23] like like uh if you know if the user has
[36:30] to like
[36:32] um I don't know do
[36:37] something like that seems difficult or
[36:41] says it's hard use this
[36:44] instead
[36:46] of
[36:48] try uh and it infers you know how to use
[36:51] this based on like the fact that I
[36:53] called it test description. It's, you
[36:55] know, so let's give this a shot.
[37:00] Hi. Um, let's see. Uh, you know, give me
[37:05] a poem
[37:07] about, I don't know, dogs and the earth
[37:12] where
[37:14] each
[37:16] other
[37:18] starts with the next letter.
[37:22] Yeah, it might just try it because I
[37:24] know GPD4 can do a variation of this,
[37:25] but um Oh, it's giving it a shot. Okay.
[37:29] Let's see if it gets it
[37:33] right. Okay. I don't have
[37:38] uh I don't have the patience. Let's
[37:46] say answer briefly. one subkins max.
[37:52] Okay, great. And
[37:57] then
[37:58] to you know uh write a haik coup. There
[38:03] we go. It's shorts where each other word
[38:07] starts with the next letter of the
[38:11] alphabet and ends with the previous
[38:16] letter of the alphabet. I don't know.
[38:18] You guys want to try this while this
[38:19] does
[38:26] it? Is it around? Did I lose Did I lose
[38:29] something? Let's
[38:32] see.
[38:37] Hi.
[38:39] Okay, you
[38:42] there? Cool.
[38:45] Um, did I not copy it? Oh no. Okay. Uh,
[38:50] give me
[38:52] a thank
[38:56] you. Now make sure each word starts
[39:03] with letter of
[39:05] the alphabet starting with
[39:08] a and each word ends with the previous
[39:14] letter.
[39:16] But this is
[39:21] hard. Okay. So it should be making the
[39:23] function
[39:26] call. Oh, I see. I see. I see. Okay. So
[39:29] I'm only printing the function call when
[39:31] it returns. So that's probably why we're
[39:34] waiting so long here. Um but this is
[39:36] actually a really good uh example of
[39:38] like okay we are doing um this like task
[39:41] delegation technically and like it is
[39:43] happening in the background and I'm
[39:44] going to give this a sec to figure this
[39:46] out. Um but like this is obviously a bad
[39:49] experience right like you don't want to
[39:51] be waiting here. You essentially want to
[39:53] keep doing other stuff. So wow it's
[39:56] still not still not back. We'll we'll
[40:00] we'll we'll let it figure it out.
[40:02] Um, so maybe let's skip straight to
[40:05] async. Um, we're
[40:08] actually got like both more and less
[40:10] time than I thought. So I don't let this
[40:13] keep turning away. Um, now let's think
[40:17] about this for a sec, right? If we want
[40:18] to do something async, it means that
[40:20] like what do we want to happen? There we
[40:22] go. So call the model da ya yada buzz
[40:25] breezy whispered. Is this correct? I
[40:27] don't know.
[40:32] Wow. Yeah, this
[40:34] is sort of
[40:36] correct. What did it say?
[40:41] Note. Great. Great. So, it it did
[40:44] something, right? Um and it did
[40:45] something that 40 probably could not
[40:47] have, which is great. That's delegation,
[40:49] but we were just sitting there waiting
[40:51] for it.
[40:53] Um so, let's try doing this async.
[40:57] Now, I I I I actually want everyone to
[41:00] like kind of just stop and think like
[41:01] how would you implement this um in terms
[41:04] of like what behavior do you want? And
[41:06] maybe I want to see people like drop
[41:07] this in the Slack. Just like take a
[41:09] couple minutes um and like drop in the
[41:12] Slack like a proposal for how you would
[41:13] want to do
[41:18] this and then I might just pick one or
[41:21] we'll like talk about them.
[41:32] Let's call 03. Yeah. Not not yet. Not
[41:35] yet. Yes. Import
[41:37] async.io definitely feels like uh
[41:40] important. But I guess the questions are
[41:42] like you know when we delegate something
[41:46] uh obviously we want to have this
[41:47] happening in the background. Um, do we
[41:50] want like when it finishes, do we want
[41:52] to be like do we want it to be injected
[41:54] into the conversation? Do we want it to
[41:56] give us a response? Um, how many like do
[41:58] we want to be able to
[42:00] like interact with tasks that are
[42:02] running? Um, like do we want to be able
[42:05] to batch
[42:07] stuff? I am not setting up a Kafka
[42:15] cluster. I'm going to give people maybe
[42:16] a couple more couple more minutes to
[42:19] just like dump some ideas here. Um,
[42:22] batch
[42:24] calls. Yeah, I guess B. But how how
[42:27] would batch calls work? Maybe Stephania
[42:29] if you want to add some like detail
[42:30] there. Just keep working until it
[42:32] generates a stop
[42:33] word, right? Okay. Yeah, this is this is
[42:37] a good idea. JS and set timeout. Yeah,
[42:39] switching to JS is always a good option
[42:41] because you already have the event loop
[42:45] implemented. Smaller model. Smaller
[42:47] model. Okay, you guys are all suggesting
[42:49] some good ideas.
[42:51] Um, but we can actually go simpler,
[42:54] right? Like like essentially what we
[42:56] would want and I can implement like the
[42:57] basic interface of this, where's my
[43:00] code? Um, is like instead of actually
[43:05] doing this, right, I can
[43:10] like
[43:12] return delegated, right?
[43:16] response
[43:18] pending.
[43:21] Um and then later I can say like you
[43:25] know check tasks or
[43:30] something. So this this pattern is
[43:32] actually one I I quite like a lot where
[43:34] you
[43:36] um you call a model it's a function it's
[43:39] non-blocking and then later you can you
[43:41] can check up on them. Now the thing is
[43:43] Python is like single threaded and uh
[43:48] async is real. Uh it's just a little bit
[43:51] tricky. Um but let's uh let's give it a
[43:54] shot. So I do have some async emergency
[43:57] reference. Now here's the here's the um
[44:00] thing to notice. when something like for
[44:03] this to work
[44:05] correctly, we have this loop that asks
[44:08] for our input and blocks on our input um
[44:10] and like is displaying that on the
[44:12] screen and we don't want to have that be
[44:14] displayed while it's also like injecting
[44:17] messages. Um so we essentially want to
[44:20] separate out like where you give user
[44:22] input and where actually interesting
[44:25] stuff happens. So that's what I've done
[44:27] in this in the basics of this async
[44:28] folder. So let's take a look at that.
[44:35] Cool. Um, it looks complicated. It's not
[44:39] that really that bad. So, um, I'm using
[44:41] websockets. Essentially, what I'm doing
[44:43] or sockets, sorry. Essentially, what I'm
[44:45] doing is,
[44:48] um, the I have a server and all it does
[44:51] is
[44:52] like has a handle user input function,
[44:55] uh, and a start message processor. Um,
[44:58] these aren't super important. and we can
[45:00] take a look at them in a second, but
[45:01] essentially it just like waits uh on a
[45:03] specific like uh port and and host. Um
[45:07] and then I have a client that connects
[45:09] to that and it just does while true
[45:11] loops and lets me enter in. Right? So if
[45:13] we look at what that looks
[45:15] like, I have it here.
[45:24] Um so let's go to async. Let me zoom in
[45:27] here a little bit.
[45:32] Also, um, while I do this, is there are
[45:34] there any questions that I've that I've
[45:36] missed? Um, and if there are, just feel
[45:38] free to shout them
[45:46] out. No. Great.
[45:48] Cool. Covered everything. Everyone is uh
[45:51] perfectly up to date with everything
[45:53] I've said. Okay.
[45:58] Um,
[46:09] sorry. Okay, so I have this and now I
[46:11] can say like,
[46:13] hi, let me show you the the rest of
[46:15] this. I guess that's probably important.
[46:18] Uh, D. So we have the server, we have
[46:20] the client, we also have the a very very
[46:24] very basic agent imple implementation.
[46:26] It it looks just like the old one with
[46:28] the main exception that I'm using async
[46:30] openai instead.
[46:32] Um handling tool calls is happening in
[46:35] parallel. So for each tool call grab it
[46:40] create the task
[46:42] um await for them and then just like
[46:45] await for them all at the same time. Um,
[46:48] and this just lets it like create a
[46:49] bunch of tasks that are all going to run
[46:51] in parallel and once they're done, like
[46:52] if they if they yield back at any point,
[46:54] we can keep doing other stuff. Um, by
[46:56] the way, if these are just like heavy
[46:57] functions that are doing heavy
[46:58] processing, it's not going to matter.
[47:00] The fact that they're in parallel like
[47:02] in sync, it means that it's still going
[47:03] to happen one after the other. But if
[47:05] they're like network calls to other
[47:06] models, then it's perfect. Um, the
[47:08] runful turn is the same one. You like
[47:11] call a model, check to see if there's
[47:12] any function calls, if not break, return
[47:15] the response. Um the only difference
[47:18] here is we're awaiting uh the chat
[47:20] completion, right? This is the only
[47:23] difference. And then if we take a look
[47:24] at our agent handler, we've declared
[47:26] we've declared our agent like normal,
[47:28] right? Right now it has no instructions.
[47:30] It looks very familiar. And this loop is
[47:32] also pretty familiar. It's like get the
[47:35] messages. Um here here's the only
[47:38] difference, right? Um and you'll see why
[47:40] this matters in a sec. I have a message
[47:42] Q. Uh and this is will be useful because
[47:46] we don't want to process multiple
[47:49] messages in the same conversation at the
[47:51] same time. Like we want work to happen
[47:53] at the same time but we don't want um
[47:56] like multiple generations to happen with
[47:59] the same history because then you'll get
[48:01] conflicting like like if two messages if
[48:02] two functions return and they both need
[48:04] to be handled uh you essentially while
[48:07] you want them to happen in parallel the
[48:09] results should should only come in one
[48:10] after the other. So we have a cue for
[48:13] that. Uh and it treats user messages as
[48:15] well like that. So this is the handle
[48:17] user input that is being called from the
[48:18] server. Essentially just throws in a
[48:20] user input message into the message Q.
[48:24] Uh and all we're doing here is like
[48:25] pulling off the queue, run it like you
[48:30] know uh put put the messages back in the
[48:32] in the message array uh and then like
[48:37] sleep, right? This is like just a very
[48:39] simple uh loop but it does it with
[48:41] async. So this is what we saw and and it
[48:44] feels pretty normal right. I can say
[48:45] like you know my name is Elan and I can
[48:49] say you know what is my
[48:53] name. Great.
[48:55] Um, now this still doesn't exactly
[48:58] answer how we're going to do things
[49:00] asynchronously, but it does give us the
[49:02] space to play with it because now things
[49:04] are happening async and we can do a few
[49:07] more delegations that that are actually
[49:09] async. So, let's start with a, you know,
[49:11] simple blocking get weather function. I
[49:14] think I required all functions to be
[49:16] async here.
[49:24] Um, yeah. 67 and
[49:28] 70. Uh, and
[49:30] then skip that and let's test it out.
[49:34] The only annoying part is we have to
[49:36] like restart two things now. So, hi. Uh,
[49:40] what's the
[49:45] weather? Great. So we can see it called
[49:47] a function got the response. So far
[49:50] everything is normal. Now let's do some
[49:52] delegation stuff. So let's
[49:57] say let's say we want to call this
[50:01] function
[50:03] uh three times for different places. So
[50:06] we have location
[50:08] [Music]
[50:11] um yeah and let's say you know like pick
[50:14] a random
[50:16] number from 50 to 80 to
[50:22] return.
[50:25] Um, so if we do it in the previous case,
[50:29] do I still have the round? Yeah, maybe,
[50:32] maybe
[50:41] not. Okay. Uh so if we look at okay this
[50:45] is the non async one. Do we have
[50:47] weather? We don't have weather. Let's
[50:50] give it
[50:51] weather. Let's give it the same weather
[50:55] function.
[50:58] Cool.
[50:59] [Music]
[51:01] Um we only need random. We don't need
[51:06] this. And this not
[51:11] async. Okay. So now we have this weather
[51:13] function. Let's test this out in the
[51:15] non- async case. Um I'm going to get rid
[51:19] of the rest for now.
[51:22] Um so if I say you know
[51:35] uh weather in
[51:39] SF cools it fantastic and now it's like
[51:42] weather in SF New York uh you know and
[51:47] the five other cities.
[51:52] is it's um it's still going to do the
[51:55] parallel function calling and here it's
[51:58] fine because they all return
[51:59] immediately, right? But now let's add
[52:02] like an artificial weight. So let's
[52:05] say time do sleep one, right?
[52:18] Um, cool. So, now what's going to happen
[52:21] is we're going to ask for that again,
[52:23] but it's going to take so
[52:26] long. Weather in five random cities of
[52:30] your
[52:33] choosing. So, it's going to take a
[52:37] while. And the reason is each of these
[52:40] is having to run um in like one after
[52:44] the other. There you go. It took like
[52:45] over five seconds. Now let's do the same
[52:48] thing here. So the equivalent is um
[52:53] there's async io
[52:59] sleep. Someone let me know if I'm doing
[53:01] this wrong. But um this should emulate
[53:04] like very very similar behavior.
[53:06] So if we instead run it
[53:14] here that's and that's I can say you
[53:18] know give me the
[53:21] weather of five random cities of
[53:26] York. Um we should see it return. Okay.
[53:29] Okay, so it called all of
[53:30] them and it got
[53:33] back because they all happened in
[53:35] parallel. Um, this is the magic of
[53:37] async.io, right? Um, anything that can
[53:40] be
[53:41] parallelized or I guess scheduled in a
[53:44] way where where it's non-blocking. Uh,
[53:46] like sleeps, these sleeps are
[53:48] non-blocking. Um, essentially we can we
[53:50] can do and so you can imagine switching
[53:51] this sleep for like an actual API call.
[53:53] Um,
[53:55] so, uh, we can actually do that right
[53:58] now with 01, right? Like we could call
[54:00] 01 multiple times and they would all run
[54:03] in parallel. Now, the main problem is
[54:06] that we're still going to be waiting
[54:08] back like waiting to to get all of them
[54:11] together, right? Like like the fact that
[54:13] it we can run them in parallel means
[54:14] that like we can have five 10-second
[54:18] tasks running in parallel. So it'll take
[54:20] 10 seconds, but it's still going to take
[54:22] 10 seconds where I can't talk to the
[54:23] model. So instead, let's have this
[54:26] notion of
[54:27] tasks. There's many ways to do this.
[54:31] Um, I'm going to do a pattern that I
[54:35] quite like. So let's do this.
[54:40] Um let's define a you know create
[54:53] task. So I have a create task function
[54:56] that makes a task. Um no and I want to
[54:59] create like a task
[55:03] ID and I want to keep it short.
[55:15] Okay. So now what I've done is I have
[55:17] this function that makes a random task
[55:19] ID, sets it, creates it and then calls
[55:23] like let's say get weather or something.
[55:27] Um and then it's you know it's
[55:29] suggesting this check tasks which is the
[55:31] next thing that I want to do. So the
[55:32] next one is check tasks. And
[55:35] so maybe I can just say like check
[55:41] task, you know, do
[55:45] for
[55:47] amazing.
[55:49] Um, okay. So let's take a moment to to
[55:51] look at what just happened. We now
[55:54] create a task with a random ID. We give
[55:56] back the ID to the model and then later
[56:00] we can call check task. get that task,
[56:03] see what the status is, and see if it's
[56:05] done. Um, so let's like add, I don't
[56:08] know, 5-second delay
[56:10] here. And right now, let's just get
[56:14] weather. So description would be maybe
[56:18] create task for, you
[56:21] know, let's
[56:23] see again this is all like sort of live
[56:26] coding, so we'll see if it works. I can
[56:30] say like you know create a task
[56:34] um and set the description to the to
[56:41] be San
[56:45] Francisco. Let's see what
[56:50] happens. Oh, I didn't give it these
[56:54] functions. There we go.
[57:01] Um, let me just check. Cool, cool, cool,
[57:04] cool. Okay, let's do it
[57:10] again. Say, you know, create a task
[57:14] where the location or the
[57:17] description is
[57:20] just. So now it creates the task and I
[57:24] can say hi. And look at that.
[57:28] It That's not working
[57:30] correctly. Maybe it was Maybe it just
[57:32] took a while to respond. Um here, let's
[57:35] add a longer delay to know for sure. 10
[57:38] seconds. Let's run it back.
[57:47] So create a
[57:50] task with
[57:52] description se uh
[57:55] cool. So I can say hello
[57:59] there. Cool. So it can still respond to
[58:01] me, right? Um check the
[58:05] task. So I can still interact with
[58:07] it and it can check to see if it's not
[58:10] done. Um, I guess we need to keep
[58:13] checking to see if it'll work. So, you
[58:15] know, how about or you know, tell me a
[58:21] joke. Who would have thought? Who would
[58:24] have thought? Um, cool. So, now like
[58:27] check them
[58:32] again. So, it called the task. It is
[58:35] done. And we have 78 and sunny. I will
[58:39] take a clap for that. I want to see
[58:41] everyone clap. Please clap. Thank you.
[58:42] Thank you. Thank you. Thank you. So,
[58:44] what you just
[58:46] saw was uh live asynchronous uh
[58:50] programming. Uh it's very impressive.
[58:52] The models can also, you know, do pretty
[58:54] well. Anyway, here's why this is
[58:55] interesting. We now have a system where
[58:58] we can give it tasks and it'll ceue them
[59:02] up uh and then we can check on their
[59:04] progress. So, so already we have the
[59:07] basis for like a really really
[59:08] interesting thing, right? like this this
[59:10] thing here right right now it's just get
[59:12] weather but if we say just like you know
[59:16] uh
[59:19] run what do it call like um you know
[59:22] call
[59:24] model and
[59:27] then no but we
[59:30] want AI
[59:33] port sync open AI get the client
[59:38] um I guess we Actually, we can just
[59:40] leverage the agents. They're already
[59:41] async. Let's not deal with that again.
[59:44] Um or whatever. Let's do Let's do it
[59:46] this way. I did all did it all.
[59:50] Fantastic. Okay. So, now we can switch
[59:52] get weather for call
[59:54] model. And let's try this again. So,
[59:57] let's give it the same task as
[60:00] before, which is, you know, hi, just
[60:03] make sure it's running. um you know
[60:05] write me a
[60:10] uh ha coup about I don't know
[60:15] uh a
[60:17] coup where the theme is so incredible it
[60:21] makes me
[60:23] cry make this a
[60:26] task okay so it's created the
[60:30] task and now I can actually say you
[60:34] Now make a second one but pick a theme
[60:40] yourself. So now I have this interface
[60:42] where I can essentially keep chatting
[60:44] with this and it can essentially spin
[60:46] off additional tasks. Um you
[60:50] check check all
[60:54] tasks. Um let's see what the progress is
[60:59] like. Look at that. So we have we have
[61:04] both. Oh, was this a one? That's pretty
[61:07] fast.
[61:09] Um, but yeah, so now we have this system
[61:11] that you can actually just call call
[61:13] multiple ones. So I'm going to pause
[61:14] here just open up for questions for a
[61:16] little bit conversation like other
[61:18] directions we can take this other ways
[61:19] we could have done this. Um, but what I
[61:21] want to look at next is like how can we
[61:23] do this in a way where we don't actually
[61:25] have to check um cuz right now like we
[61:27] don't need these two terminals. This is
[61:30] just over complicated. Like I think the
[61:32] the the point of having the second
[61:34] terminal is so that we can push things
[61:35] to the conversation without a user
[61:38] having sent a message first. So I'm
[61:40] going to pause here. I'm going to field
[61:41] some questions and then we can get back
[61:43] to
[61:49] it. Okay.
[61:52] Um would you not use generators for
[61:55] nested tool
[61:58] calls?
[62:00] Um, Tom, do you want to I don't know if
[62:02] there's a mic in the room or like uh
[62:05] just get get it get it to them. Yeah,
[62:08] there
[62:09] is. Also, they can unmute themselves.
[62:16] Uh, who's your
[62:39] Uh, sorry.
[62:41] So, is the one that was uh answering is
[62:44] So, in the room?
[62:48] Yeah. Can Can you hear him? No, I can't
[62:51] hear him.
[63:04] Hello. Can you hear me in the Zoom?
[63:07] Yeah, I can hear you now.
[63:18] I can't hear you
[63:19] anymore. I don't know if you're saying a
[63:22] question right now.
[63:31] No, I was just
[63:34] wondering if it's possible to treat
[63:38] agents
[63:40] objects as a
[63:43] generator in Python. So you can nest
[63:49] like you can yield from individual
[63:52] agents and then yield those tool calls.
[63:56] Does that make sense? Yeah. Yeah, that
[63:59] makes sense. This is also very
[64:01] impressive that you have to do this. I
[64:02] think someone needs to mute themselves.
[64:04] I don't know if it's Alain or uh like
[64:07] someone in the room unmuted and uh put
[64:10] put this man through through hell. Um
[64:12] No, it's me. It's me.
[64:14] Oh, is your laptop
[64:20] unmuted? I can't hear anyone
[64:25] anymore. Maybe just speak into your
[64:31] laptop. Okay, but I'll I'll answer your
[64:33] original question of like, you know, if
[64:35] you put um can you like essentially make
[64:37] agents into generators so that you can
[64:39] like yield the results as you go? The
[64:41] answer is yes. And this is actually like
[64:43] um the right way to do this. The way I'm
[64:46] doing it now is I'm only exposing the
[64:48] final response mostly because um
[64:50] implementing like the the generator gets
[64:53] a little bit tricky and I don't want to
[64:54] have to like debug that. Not too much,
[64:55] but you can essentially just surface
[64:57] each of the steps, each of the function
[64:59] calls, each of the everything.
[65:01] um that would um that would let you
[65:07] essentially keep track of more agents at
[65:09] the same time and you could maybe have
[65:11] like a bit of a flat structure where you
[65:13] just have multiple agents going yielding
[65:16] events and then you can essentially see
[65:17] like which one's coming from where.
[65:20] Um but I guess the thing is like there
[65:23] you have to deal with a bit of the
[65:24] complexity of um handling all the like
[65:27] like essentially listening to like all
[65:29] the different events and like uh
[65:30] associating them back to like a specific
[65:32] agent and like maybe there is an agent
[65:34] in the front, maybe there isn't. Um here
[65:36] the idea is just I have one agent that
[65:38] I'm interacting with. I'm always just
[65:39] going to interact with like that one
[65:40] agent and it's responsible for spinning
[65:42] off other other ones and like dealing
[65:45] with dealing with that as well. But you
[65:47] can absolutely do it the way that you're
[65:48] saying. And like if you wanted to build
[65:49] this out like more fully, you probably
[65:50] would in order to be able to surface
[65:54] progress. Um, did that answer your
[65:56] question? I'm now scared to get people's
[65:58] talking in the room, but I'll just read
[66:01] them from Slack.
[66:04] Um, is there any is there any good
[66:07] design patterns to create projects with
[66:11] agents? There's like a million. Um, you
[66:14] know, like I like prototyping with
[66:17] swarm. Um, I know paidantic AI is also
[66:20] like a really nice one. I think Sam's
[66:22] there in the room or around.
[66:26] Um, there's Yeah, I don't want to
[66:29] like I don't really use uh any myself
[66:33] mostly because like you saw it's pretty
[66:35] simple to implement your own loop. So
[66:37] that's what I end up doing. I think
[66:38] usually for every project I either write
[66:40] my own like it's like I don't know how
[66:42] many how many lines is this
[66:47] like like 70 lines and so like depending
[66:49] what you want you might want more you
[66:51] might want less and I'm sure there's
[66:52] good solutions um but like I just have I
[66:55] could just copy this around um I don't
[66:58] really like working with too many
[66:59] dependencies especially for something
[67:00] that's so lightweight like I I want
[67:02] granular control um and like except for
[67:04] example for Swarm I ended up having to
[67:06] hop in here and like handling specific
[67:09] kinds of tool calls in certain ways so
[67:11] that I can do handoffs. Um, which we can
[67:13] actually look at and we can implement
[67:14] this without too much trouble. Um, but
[67:17] yeah, my answer is like there's many you
[67:20] can choose from. I don't have many I
[67:22] would recommend personally.
[67:24] Um, but I I am a I am a fan of of
[67:28] Pyantic AI. It's pretty cool. I haven't
[67:29] used it too much, but like the interface
[67:31] looks nice. Um, it reminds me a lot of
[67:33] Swarm. The one I use the most for
[67:35] prototyping is Swarm. I think it's just
[67:37] cuz it's the one that like I'm most
[67:39] familiar with. Um, when you have to
[67:43] start to approach dozens or hundreds of
[67:46] functions, what techniques should we
[67:47] apply in order to effectively tool call?
[67:50] There's there's a few answers there,
[67:52] right?
[67:53] Um, you can have multiple agents and
[67:57] essentially like split up the
[67:59] responsibilities or like the the
[68:01] groupings of the functions. Um and so
[68:04] into into yeah like clusters where you
[68:07] have like a set of related functions
[68:09] that are needed for specific tasks and
[68:11] then you can invoke the correct agent.
[68:15] Uh and this is where like multi- aent
[68:17] patterns start to make sense is like
[68:20] specifically when you have tons and tons
[68:22] of functions like how do you uh go to
[68:24] the right ones? If you for some reason
[68:27] need them all at the same time, uh you
[68:30] could try fine-tuning. Um in in projects
[68:32] for OpenAI, I've ended up fine-tuning up
[68:35] to like hundreds of fun like it was like
[68:37] 120 functions. This was with uh GPT3.5.
[68:40] So the fact that that works gives me
[68:42] like pretty high confidence like you can
[68:43] fine-tune uh smaller models with a lot
[68:46] of functions and get them to work pretty
[68:47] well. Um the last one is like some kind
[68:51] of dynamic function loading where based
[68:54] on the input or based on the
[68:55] conversation you load into memory or
[68:59] like you load into context um the most
[69:02] likely relevant functions. Um and
[69:06] there's a few different ways to do this.
[69:07] You can do this with embeddings. You can
[69:09] do this with like
[69:12] um having like a two-step function call.
[69:15] At that point, you're essentially having
[69:16] agents. Like if if you call a function
[69:17] to then load more functions, that's what
[69:19] a handoff is essentially. So a lot of
[69:22] these start to look very similar. Um
[69:24] it's just like how are you loading
[69:25] multiple different ones? Um okay, for
[69:28] visioning models, are there tools being
[69:29] called within the thought text?
[69:33] Um,
[69:36] so because we don't expose the thoughts
[69:39] like the the chain of thought, um,
[69:42] that's a little bit hard to answer for
[69:43] for for 01 right now in the API. The
[69:46] answer is no.
[69:52] Um, I'm trying to see how much I can say
[69:54] here. Um, it is something that is
[69:57] technically possible, right? Like you
[69:58] can do anything you want with with post
[70:00] training.
[70:02] Um, we do not currently allow you to
[70:05] call functions within the chain of
[70:07] thought.
[70:09] Um, so yeah, right now the function
[70:12] calls happen at the very end. Uh, do you
[70:15] have any good code examples for router
[70:17] patterns in these lots of functions
[70:18] cases? Yeah. So, so my like my answer
[70:21] there is some one of these. Like if you
[70:24] really just want to route um then like
[70:26] the the idea of having like multiple
[70:28] agents and handing off to one of them is
[70:30] actually really nice. Um like you can
[70:32] just define multiple agents each of them
[70:34] with like multiple functions. Um and
[70:37] then have the first one have like a we
[70:39] can actually do this quickly like we
[70:41] I'll do this in swarm but like I said
[70:43] you can implement this yourself. Um I
[70:46] don't actually know who else supports
[70:47] handoffs the same way Swarm does, but
[70:49] um essentially here let's start a new
[70:52] file like
[70:57] uh
[70:58] routing.
[71:06] So see swarm ripple demo loop I can say
[71:10] like you know triage
[71:14] equals one and then I can have my other
[71:16] two. It's like you know maybe I have
[71:18] like some collection of like um you can
[71:21] call them an agent but I can also just
[71:22] call them yeah like uh what it be like
[71:25] you know uh
[71:27] email
[71:28] functions
[71:31] agent and you can have like you know
[71:34] like send
[71:39] email check email I don't know what else
[71:42] does cursor want me to write
[71:45] there. Um, cool. We have these two and
[71:49] then we can do like maybe we have the
[71:51] emails and then we have a calendar. I
[71:53] don't know. So make like
[71:57] create
[72:02] event can do like calendar. I'm just
[72:07] going to say like you know finish what
[72:09] I'm doing update the prompts and the
[72:13] tools. I'm lazy. So let's see what uh
[72:15] let's see what cursor thinks.
[72:19] Great. So now we have an email functions
[72:22] agent and a calendar agent. Call them
[72:25] whatever you want.
[72:27] Um now like let's pretend that instead
[72:30] of just having three functions, we have
[72:33] 30 and each one of these has 10 or 15.
[72:37] Um then like if you maybe give all 30 to
[72:40] one agent, first of all try it. Like if
[72:42] that works, amazing, right? you don't
[72:44] have to deal with the extra complexity.
[72:46] Um so you don't really want to do
[72:47] handoffs and stuff until you really
[72:49] really need to through like evals.
[72:53] Um but um yeah. So, so and then the
[72:56] special like kind of functions here is
[72:58] like you know uh
[73:01] transfer
[73:05] to email
[73:09] agent and I'll
[73:11] return email agent and then cool. So now
[73:16] I have my two transfer
[73:21] functions. Oh. Oh, it did it. Okay,
[73:23] cool. So I think this should just work
[73:26] right. So I've defined like the actual
[73:28] functions and agents that in your case
[73:31] would be many many more functions. Um
[73:34] I've defined the transfer functions and
[73:35] I've given them to the triage agent. So
[73:37] now if I run
[73:44] this say hi
[73:48] um you know I want to send an
[73:55] email. Cool. So now I'm talking to the
[73:57] email agent. Now if you want to do like
[74:00] more you know like transfers
[74:05] uh this is not delegation. Okay. So
[74:08] trails assistance um maybe we can tell
[74:11] the assistance
[74:14] like you know if you already know what
[74:19] the user is
[74:21] asking just call that function right and
[74:24] this is if you want to have like a case
[74:27] where you know it still routes you but
[74:30] it's like a faster two hop so maybe I
[74:33] can say like what are the functions here
[74:36] um what are the parameter There's send
[74:38] email to subject
[74:42] body. So I can say
[74:45] like know send an email to
[74:50] bobgmail.com about
[74:54] taxes. What was the other
[74:56] one? Body um saying yo do your
[75:03] taxes. So it should transfer me to the
[75:07] email one. And then there we go. It
[75:08] immediately sends the email. So this
[75:10] felt like an immediate function call,
[75:12] but there was a transfer in the way. So
[75:14] this is kind of an example of like
[75:16] triaging does work. It's really
[75:19] convenient to model it with agents and
[75:20] handoffs. Um I'd say it's the primary
[75:22] use case for agents and handoffs is just
[75:24] a glorified triage through uh multiple
[75:27] functions.
[75:29] Um yeah, let's see. Let's go back to
[75:31] questions.
[75:37] [Music]
[75:39] Uhhuh. Consider having something like
[75:41] streamllet grad until you are you
[75:43] considering having something like
[75:44] streamlink radio util that allows
[75:46] porting all interaction functionality
[75:49] with one
[75:51] command. I don't think so. I don't know.
[75:55] Uh what did people answer? There we go.
[75:59] Sam's in with pantic. So check that out.
[76:01] Um, how many tool calls can you get in
[76:04] one
[76:05] iteration? You like parallel function
[76:07] calls. I don't think we have hard limits
[76:09] on either the number of functions or the
[76:11] number of parallel function calls. How
[76:13] big a tool library will the models
[76:14] perform well
[76:17] with? Super super general rule of thumb
[76:19] is
[76:20] like 10 to 20 you shouldn't really pass
[76:24] over. Um, but like I said, I've gotten
[76:27] like this was a very specific case where
[76:29] like it was extremely latency sensitive
[76:31] and so like we had to have flat like
[76:34] flat function calling and we did 120
[76:36] functions with GPT 3.5.
[76:40] So you can go pretty far um with
[76:43] fine-tuning, but like I'd say reliably
[76:46] without without extensive prompting.
[76:48] Yeah, probably like 10 to 20 like past
[76:51] that point. You really ask yourself like
[76:53] what are you trying to do? Like why are
[76:54] you putting so many functions? Is it
[76:56] super latency sensitive? Can you split
[76:58] it up? Like yeah. Um was there a
[77:02] follow-up
[77:04] here? Okay. Um rather than tool
[77:07] calls, I feel like we're moving to
[77:09] generated code agents, will I soon be
[77:11] able to supply my tools functions? Ah,
[77:14] okay, that's a good idea. We should try
[77:15] that. Um so essentially have something
[77:16] write its own function and then use it.
[77:19] Uh yeah, I feel like we can probably How
[77:23] would we do that? Yeah, we can try to we
[77:25] can we can find a way to do that. Uh I
[77:27] I'll do that actually. Let's do right
[77:28] now. Why not? Let's do right now. Uh
[77:30] I've never done this before, but I feel
[77:32] like it shouldn't be too hard. So
[77:36] um okay. Uh you know, what do we call
[77:40] this? Like
[77:42] bootstraps. Okay. So I'll keep using
[77:45] swarm because I I will use um
[77:49] handoffs from swarm import
[77:53] agent. Cool. So now it's always so let's
[77:57] see we want an agent that writes it own
[77:59] functions. So
[78:01] agent was this
[78:03] one. Um we want it to write its own
[78:10] functions. So maybe we can have an hand
[78:13] off to
[78:15] itself. So we can do you know like
[78:18] refresh you know what to be refresh
[78:24] functions. So we can actually return the
[78:27] same agents.
[78:30] Um and
[78:32] then okay is it not declared? Is it
[78:36] unhappy? Uh yeah it's not defined yet.
[78:40] Okay. Okay. So now we can define it down
[78:50] here. Okay. Um
[78:54] bootstrap bootstraps. Bootstraps. Okay.
[78:57] So we have this and we want it to write
[79:00] its own functions. So how are we going
[79:01] to do this? We wanted to produce
[79:05] Python. Does anyone have any ideas? uh
[79:08] if you want to shut them out like make
[79:09] just pass around the mic while I code
[79:11] just feel free to I can't I can't read
[79:12] while you're uh what you write but we
[79:14] can we can try this. So, um let's say we
[79:17] want it
[79:18] to, you know,
[79:23] um you know, add tool. There we go. And
[79:27] then let's call this, you know,
[79:38] Pythonation. Okay. I'm going to do
[79:40] something very unsafe. So, you know what
[79:43] would it be? It's like function
[79:46] obj
[79:52] equals eval
[79:55] of Python. Don't do this. Don't do this,
[79:58] kids.
[80:00] Um, and then will this work? Is this how
[80:03] Python works? Sam's there. Uh, okay. So
[80:08] if I have
[80:09] this and I eval like you know
[80:16] def
[80:26] a does it um okay you know
[80:40] Um, so I guess it's like uh I want to
[80:45] write
[80:46] a write a function that takes a
[80:52] string representing an implementation of
[80:55] a Python function and returns the actual
[80:59] rule Python function as
[81:05] interpreted. I don't know. Let's see
[81:08] what it
[81:09] does. Um, so essentially we want to do
[81:12] that once we have the function then we
[81:15] can just append it to the agent and then
[81:17] we might need to reload it. Uh, so we
[81:19] can then just return the agent and this
[81:22] might be
[81:25] it. This might be it.
[81:29] So add
[81:31] tool exec not
[81:34] eval. Why didn't anyone say that? You
[81:36] guys can shout
[81:38] out.
[81:43] Okay. Okay. So it's
[81:49] exec and
[81:51] then what is this
[81:56] 80? I don't
[82:01] know. Someone save me. Like
[82:07] uh Hey, there's a couple implementations
[82:10] you miss. Sorry. Check the flash.
[82:18] Did someone do this?
[82:20] Hey. Okay.
[82:23] It's almost like someone fired. No, no,
[82:26] no. But this is not Okay. No, but this
[82:27] is not what I want, right? Like I don't
[82:28] want it to run it in a subprocess. I
[82:30] wanted to I wanted to eval like evaluate
[82:35] the function and then turn it into a is
[82:38] that Oh, go up. Oh, Sam, of course.
[82:42] Amazing.
[82:45] Uh Jesus
[82:50] Christ. Okay.
[82:53] um make
[82:56] it. So the add tool function
[83:03] uh
[83:05] evaluates the
[83:07] implementation and adds it to the tools
[83:12] similar to
[83:14] now. Here's a great reference for how
[83:20] to
[83:23] Let's And then we want to grab Was this
[83:26] a good idea? This is a terrible idea. I
[83:28] hope people are enjoying
[83:29] this.
[83:36] Um, okay. Let's see. Um, and let me just
[83:40] read this because it might not be that
[83:42] complicated to add in.
[83:48] So, I can't. Okay, it got in the way.
[83:52] No, not Zoom. Where's
[84:08] Slack?
[84:16] Was this
[84:23] it? Is this
[84:27] it? Okay, I'm going to I'm going to put
[84:29] this on hold for now. It sort of ignored
[84:31] your implementation, Sam. I'm sorry. Um,
[84:33] let's see. So if you have parse
[84:35] function, can I
[84:41] just do this? Does this
[84:44] work? Uh, okay. Let's see. I've first
[84:49] time for everything. Uh, wrong one.
[84:52] Sub bootstraps. Hi.
[84:57] Um, add a tool that prints hello when
[85:10] called
[85:17] it. Oh, but no, no, no, no. Make it
[85:21] print it, not just return it.
[85:27] My heart's pounding. Okay.
[85:30] Um, so say hello to call
[85:34] it. Look at that. Look at that. Okay.
[85:38] So, now we have Yes, I will take a clap
[85:40] for that. We did this together, guys.
[85:42] Um, so this is actually a lot less code
[85:45] than I was expecting, but now we have a
[85:46] system. Look at that. It's tiny. Um,
[85:49] that can write its own tools. Um, and so
[85:52] like maybe we can do something like, you
[85:54] know, um, what is, you know, like make
[85:59] yourself a little
[86:03] calculator. I can't believe this just
[86:06] worked. Uh, you know what
[86:09] is 2 * 3
[86:19] * Can someone check this? Uh, wait,
[86:21] wait,
[86:22] wait.
[86:25] 34698.
[86:26] 34698. This is This is crazy. This is
[86:29] This is so fun. Uh, yeah. I hadn't done
[86:32] this before. And this is a lot less code
[86:34] than I thought. Look at this. Look, this
[86:36] is all you need. I mean, it's this is
[86:37] super dangerous code. Like,
[86:40] this this is not good. Don't do this.
[86:43] But it's fun. Uh, I would put this
[86:46] squarely in fun things. We can we can
[86:49] now transition to looking at other fun
[86:50] things. Um they're definitely not as fun
[86:53] as this one, I think. Um they're just a
[86:55] couple of like random things that I
[86:57] found related to real time since I did
[86:59] sort of put it in this uh title. So
[87:04] whatever. Okay, these are the two main
[87:05] tricks that I that I kind of thought
[87:07] were pretty cool and you might have
[87:08] already seen them. Um, one is if you've
[87:12] ever dealt with like the real time API
[87:15] um like jumping in uh before you're done
[87:18] with an idea or like done talking or
[87:20] something. Um
[87:22] like what I was thinking is like if if
[87:25] really what you want is you wanted to
[87:26] like use the model's own intelligence to
[87:29] decide if you're done talking or not. Um
[87:32] and you can treat our VAD like our voice
[87:35] detection as like a trigger happy
[87:37] version of that. It's like a it'll
[87:39] always tell you when maybe the user is
[87:42] ready to stop talking. But if you want
[87:44] the model to check, you can have a stay
[87:46] silent function or something else that
[87:48] essentially handles the other side of
[87:50] that where it's like, okay, we're
[87:52] definitely going to let you know
[87:53] whenever the user might be done talking,
[87:55] but then you can actually verify with a
[87:57] function call. And so this
[87:58] implementation is like super super
[88:00] simple. You literally just give you give
[88:02] the the function
[88:04] itself to the real time
[88:06] API and tell it to call it when the user
[88:09] is not quite done talking. And I'm not
[88:12] going to try to demo this live. Like
[88:13] real time demos are tough. Audio is
[88:15] tough. All that fun stuff's tough. But
[88:19] um it works like surprisingly well. Uh
[88:22] if you just describe I I can you can
[88:25] probably find this tweet but it has the
[88:27] full prompt but essentially it's like
[88:28] you can you can like pause you can say
[88:30] like you know I've been thinking about
[88:32] and then like stop and like it'll get
[88:34] triggered call stay silent and then you
[88:36] can keep talking. Um so pretty pretty
[88:39] cool uh useful thing. Um and then the
[88:43] other one is also related to real time
[88:44] API. And if again if you if you uh are
[88:47] following me you might have already seen
[88:48] this but um someone at Devday just like
[88:53] came up to me and asked me like hey um
[88:56] is there a way to like make the real
[88:57] time API talk in like a specific way. Uh
[89:00] and I was like I don't know let's try
[89:02] it. And so like we had a demo booth and
[89:04] I sort of pushed someone out of the demo
[89:06] booth and grabbed the laptop and I was
[89:07] like let's just like try try this stuff.
[89:09] And apparently if you ask the model to
[89:12] just you give it like a a script and
[89:14] you're just like, "Hey, read this out
[89:15] according to these XML tags
[89:17] um you can have it follow them here. Let
[89:20] me let me find
[89:22] um the
[89:25] original the original one." Yada yada
[89:29] yada. Sorry, this is I'm not trying
[89:33] to show you the whole timeline. Where is
[89:36] it? Okay, this is the stay silent one.
[89:46] Um, where is it? Where is it? There we
[89:51] go. Um,
[89:55] uh, it's impossible that you'll hear
[89:57] this, right? You guys don't hear
[90:01] this. Yes. No. Uh, we don't hear it, but
[90:05] you can hear your computer audio.
[90:08] Can I
[90:10] do the thing? I'm I'm I'm actually I'm
[90:11] not going to try. That's fine.
[90:14] Um, wait. Can
[90:18] I same? No, no, no. It's fine. Whatever.
[90:20] Anyway, um, yeah. So, if if you if you
[90:23] like give it
[90:24] like a script like this, um, we didn't
[90:27] actually train it for this, right? Like
[90:29] this is just a really nice consequence
[90:32] of like behavior. It's technically not
[90:33] function calling. I'm realizing now, but
[90:35] it's like it's very function
[90:36] callingesque. It's real time. The title
[90:38] of this talk does include real time. So,
[90:41] this is uh this is it. Um I will pause
[90:43] here. I have so much more I can go
[90:45] through, but I want to give you guys a
[90:46] chance to like ask questions, poke
[90:48] around with some of these ideas. Uh
[90:50] Swarm is public. You can just try it
[90:51] out. Um we can also just try creating
[90:53] other functions. Uh this this is one of
[90:55] the this is easily one of the coolest
[90:57] like little programs I've ever made.
[90:59] Um,
[91:02] so yeah, let let me see if there's any
[91:04] other questions of the
[91:13] Slack.
[91:15] Uh, it's a room full of people auto
[91:19] completing make. Yeah, yeah, yeah. Okay,
[91:22] let's not do
[91:24] that. Uh, okay. Revisiting
[91:26] memory. Let's see. Do you have any
[91:29] suggestions for trying to enforce
[91:30] consistency of stored
[91:32] memories? Identifying inconsistencies
[91:35] and figure out how to resolve them.
[91:36] Okay. And then the second part is what
[91:37] data structures do you suggest for more
[91:39] structured memory helping enable more
[91:41] meaningful comparison of objects? I
[91:43] think I mean this question opens like
[91:47] you start to go down a path where you
[91:48] can get as complex as you would like,
[91:50] right? Like like you can start simple
[91:52] and you can end up with like an entire
[91:55] operating system to manage memory,
[91:57] right? There's like the whole range.
[92:00] Um, one way to
[92:04] do off the top of my head like one way I
[92:07] can think to do this is um when you are
[92:11] about to store memory do a retrieval
[92:14] like do search to find similar memories
[92:16] or like memories that like are
[92:17] semantically similar um and then do an
[92:21] explicit check uh with a model to see if
[92:24] like you know one is like updating or
[92:27] contradicting another. Right? An example
[92:28] of this is like you know what is the
[92:30] latest state of a project right you know
[92:32] if someone's like is the project like at
[92:34] some point you say like I'm working on
[92:35] the project like it's not ready yet and
[92:37] it saves that and then later you're like
[92:40] you know I um how like the project's
[92:43] done now right like those are two
[92:46] contradicting memories um what you can
[92:49] do is essentially
[92:52] uh have a time stamp for them but also
[92:55] when you are about to store the second
[92:57] one or any memory
[92:58] check for similar ones and create like a
[93:02] direct like essentially
[93:08] um like node uh pointing from the
[93:12] original memory to the new one. And so I
[93:16] guess I guess what I'm thinking is like
[93:18] that way if anybody
[93:22] asks and you surface both like you can
[93:25] keep both in memory and when you do like
[93:27] retrieval and semantic similarity you
[93:29] can surface both but essentially you can
[93:31] present like the whole chain of updates
[93:34] and so you can just present the last one
[93:36] if you want or you can present the whole
[93:38] chain and the model have has some idea
[93:40] of like you know maybe if you ask it
[93:42] like um you know how long is this
[93:44] project delayed because that was the
[93:46] last you heard about it. But somebody at
[93:47] some point said, "Oh, it's actually
[93:48] done."
[93:50] Um,
[93:52] like if it raises both and has one with
[93:55] a later date, you know, maybe. But if
[93:56] you like if you've already made this
[93:57] chain explicitly, um, like you can
[94:00] actually represent that and you can
[94:01] choose to not show the previous ones. So
[94:04] that's one idea. Like I said, there's so
[94:06] many you can like so many ways to do
[94:08] this. Uh, and and like as soon as I stop
[94:10] talking, you guys walk out. Someone's
[94:11] gonna like be like, "Oh, there's
[94:12] actually this like much easier way that
[94:14] like this idiot didn't think of." So,
[94:16] anything you think of probably works.
[94:19] Um, here's a real time API
[94:23] prompt. Yeah. Cool. Uh, any other any
[94:27] other questions about anything? Um, it's
[94:30] been like an hour and 40 minutes, so
[94:33] happy to like keep going with random
[94:36] content. Um, there's a couple demos that
[94:39] I have that are like demoing some public
[94:41] repos that we have that you can use.
[94:46] Um, yeah, but I want to I want to give
[94:49] anyone a chance to like speak up, say
[94:51] something if you want, ask
[94:53] questions.
[94:55] Um, I I don't see I don't see a lot
[94:58] happening in I I can't You guys are tiny
[95:01] on my screen.
[95:09] Uh, cool. Okay, then I'll pose this to
[95:12] you. Sorry, what?
[95:15] Oh, no. Go ahead. It sounds like you're
[95:17] wrapping up.
[95:21] Yeah, the the last thing we can do, I
[95:23] guess, is like either I can um try and
[95:27] pull up a real time uh demo that shows
[95:30] how to do the 01 stuff uh in a in a
[95:33] slightly easier way. Okay, cool. People
[95:36] want to do that
[95:38] demo. Okay, let's do it. So, um the
[95:42] reason I'm a little iffy about it is
[95:44] because yeah, it's real time. Uh and
[95:46] those demos are tough to do publicly but
[95:49] um there is this repo OpenAI um real
[95:53] time Twilio demo
[95:58] um that essentially sets up your whole
[96:02] um like phone calling assistant uh and
[96:06] it's just works right out of the box. It
[96:08] walks you through the steps. Um I may
[96:10] end up sharing a phone publicly. don't
[96:12] call it during this demo and don't share
[96:14] it and I will delete it. But um yeah, I
[96:16] trust you guys. So let's
[96:24] see. Okay, so it looks like this is
[96:28] already
[96:30] running. Oh, I do have it already
[96:32] running. Okay.
[96:35] Um Oh, never mind. I I did uh I did make
[96:39] it all dots. But yeah, essentially this
[96:41] um this little checklist is like live
[96:43] updates. So as you set up the account,
[96:45] as you set up the phone number, as you
[96:46] set up your local web server, etc.,
[96:49] it'll like get checked. So setting up
[96:51] Twilio and Grock and everything has been
[96:53] one of the most annoying things I've had
[96:54] to do multiple times um related to the
[96:57] real time API. So this hopefully makes
[96:59] that process like a lot a lot easier.
[97:00] You can do most of it directly from here
[97:02] and it lets you know like when things
[97:04] are done. So you don't actually have to
[97:05] do a lot from the Twe console at all. Um
[97:08] anyway, so
[97:10] um I let me show you the back end. So
[97:15] there is
[97:17] a handler function. There we go.
[97:19] Function handlers. So um you can either
[97:23] implement tools
[97:25] uh locally as a JSON schema and we can
[97:29] we can try that really quick. So this is
[97:31] the real time playground and I can say
[97:32] like you know make
[97:35] a function to you know get the answer to
[97:41] answers to
[97:44] everything no params maybe one
[97:49] param. Okay, so it gave it gave us this
[97:52] nice little
[97:54] uh nice little function and we can just
[97:57] paste it in
[97:59] here, save
[98:02] it, and cool. So now we have this get
[98:05] universe answers and I can save this
[98:08] configuration and call the phone
[98:14] number. So, let's
[98:21] see.
[98:24] Hello.
[98:28] Hello. Okay, this is why I love them.
[98:31] Let me let me try once
[98:33] more. Okay, let's go tool. Paste this.
[98:39] Save changes. Save
[98:41] config.
[98:42] [Music]
[98:52] Um,
[98:53] hello.
[98:56] Hello. I don't think it's
[99:03] happy. Is someone else? No, I didn't
[99:06] show the number. Hello. Okay, it's not
[99:08] working. That's fine. Sort of expected
[99:11] it. Um, essentially what you can do like
[99:13] when you when you use this, um, it's
[99:16] cool because these tools you can either
[99:18] specify local ones with schema and they
[99:20] appear here or you can define them in
[99:23] the back end. Um, so if you define them
[99:25] in the back end, you can actually give
[99:26] like code to execute. Um, if not,
[99:28] they'll just show up here. Uh, and you
[99:30] can enter in like what the response will
[99:32] be uh, like a mock response. Um, but you
[99:35] can also like set up backend functions
[99:38] that will actually get handled in the
[99:39] back end. Uh the sample one is like a
[99:42] real implemented get weather one but as
[99:44] you can see there's like it's pretty
[99:46] straightforward to implement like the 01
[99:47] one. Now the main difference between the
[99:50] real time API here and like what we were
[99:52] doing before is the real time API does
[99:55] actually allow asynchronous functions
[99:58] natively. So you can the model can call
[100:02] a function um get no response and you
[100:05] can keep talking with the model um until
[100:09] a response is back. So that that is
[100:11] behavior that like we specifically had
[100:12] to teach the real-time models because
[100:14] unlike a chat conversation, you can't
[100:16] really enforce um like you can't really
[100:19] halt the whole conversation until the
[100:22] functioning response comes back. So, we
[100:25] had to do that for for for launch um
[100:27] because originally when we hadn't done
[100:29] that, you know, we hadn't ever shown it
[100:32] how to do asynchronous functions and so
[100:33] it just couldn't couldn't handle them
[100:34] correctly. Anyway, sadly, uh demo didn't
[100:37] quite work. Maybe I can try this one
[100:38] more time. We'll see. Third time's a
[100:41] charm.
[100:56] Hello.
[100:58] Hello. No. Okay, great. Anyway,
[101:06] um I believe that is most of what I
[101:09] wanted to cover today.
[101:11] Um, I'm going to play with this hyper
[101:14] unsafe function making agent a bit, but
[101:18] um, yeah, thank you all for coming. I'll
[101:21] hang around for questions for a bit if
[101:22] anyone has any. Otherwise, I think we're
[101:24] ending a little bit early. Um, like I
[101:28] said, yeah, mo most of you can can hang
[101:30] out or or leave as you please. Um, but
[101:34] I'll maybe I'll call it wrapped up here.
[101:37] Um, maybe what we can do is if you're
[101:39] interested, you can stay and like hack
[101:41] on some of the stuff that you saw. I'm
[101:43] happy to hang around uh and answer
[101:45] questions as well. So, thank you all for
[101:47] coming. Uh, hope you hope you got
[101:51] something out of this.
[101:58] Um, the
[101:59] new uh to help in
[102:02] sports. Uh
[102:04] otherwise, I guess you can share. I'm
[102:06] sharing a little bit in case people have
[102:08] questions.
[102:10] I'm actually going to dump this, but
[102:12] this may be a really bad idea, but um
[102:15] here you go. Here's the code for the
[102:17] super unsafe self like tool writing
[102:20] agent.
[102:34] And I'm probably going to stop sharing
[102:35] my
[102:37] screen. Um, yeah, I can I can I can
[102:40] share the repo and the slides. There's
[102:43] not a lot on the slides, but yeah, I'm
[102:45] happy to happy to share them after.
