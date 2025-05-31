---
type: youtube
title: Stateful Agents — Full Workshop with Charles Packer of Letta and MemGPT
author: AI Engineer
video_id: E0k9Ppq6yXY
video_url: https://www.youtube.com/watch?v=E0k9Ppq6yXY
thumbnail_url: https://img.youtube.com/vi/E0k9Ppq6yXY/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence and Machine Learning
tags: ['AI', 'Large Language Models', 'Memory Management', 'Machine Learning', 'Context Window', 'AI Ethics', 'Observability', 'System Design', 'Natural Language Processing', 'AI Research', 'Software Engineering', 'Context Compilation']
entities: ['Berkeley', 'Leta', 'CHAGPD', 'LangChain', 'MGPT', 'LMOS', 'Large Language Models (LMS)', 'AI', 'context window', 'observability']
concepts: ['memory management for LMs', 'statelessness vs. statefulness', 'context window management', 'AI-driven memory management', 'observability in AI', 'humanlike intelligence', 'context compilation', 'AI ethics', 'system design', 'machine learning']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['basic understanding of AI and machine learning', 'familiarity with large language models (LLMs)', 'knowledge of programming or system design concepts']
related_topics: ['natural language processing', 'AI system design', 'machine learning algorithms', 'software observability', 'context management in AI', 'AI ethics', 'memory optimization techniques', 'human-AI interaction']
authority_signals: ['I was a PhD student at Berkeley', 'I wrote this paper called megpt with a bunch of my colleagues', 'this is really talking about like a memory management system for LMS']
confidence_score: 0.85
---

# Stateful Agents — Full Workshop with Charles Packer of Letta and MemGPT

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=E0k9Ppq6yXY)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: stateful agents, ai agents, machine learning, docker, software development, ai research, llm  

## Summary

# Stateful Agents Workshop Summary

## Overview
This workshop, led by Charles Packer (co-founder of Letta and researcher at Berkeley), explores the concept of **stateful agents**—AI systems with memory capabilities. The session addresses the limitations of current large language models (LLMs) in retaining context, introduces **MemGPT** as a memory management system, and discusses the challenges of scaling AI agents for real-world applications. Key themes include the shift from stateless to stateful AI, the role of context windows, and the need for better memory organization.

---

## Key Points
- **Stateless vs. Stateful Agents**:  
  - LLMs are inherently stateless, relying on external memory systems (e.g., appending to lists) to retain context.  
  - Stateful agents mimic human-like intelligence by dynamically managing memory, learning, and adapting over time.  

- **Limitations of Current Methods**:  
  - Traditional memory management (e.g., LangChain's buffer memory) involves appending to a list, leading to inefficiencies and "context decay" as interactions grow.  
  - Context windows are poorly structured, often requiring manual curation and observability tools to track interactions.  

- **MemGPT as a Solution**:  
  - A memory management system designed to let AI autonomously handle its own memory, reducing reliance on human intervention.  
  - Introduces concepts like **context compilation** (optimizing how context is structured) and **stateful databases** to store information beyond token limits.  

- **Challenges in Scaling**:  
  - Human users often manually "compile" context (e.g., re-explaining tasks in long chats), which is unsustainable for complex workflows.  
  - The need for systems that can dynamically organize and retrieve memory, akin to human memory formation.  

- **Research Context**:  
  - Charles Packer’s work on MemGPT emerged from his PhD research at Berkeley, pivoting after the ChatGPT era to focus on memory and agent systems.  

---

## Important Quotes
- *"If LMs get better, shouldn’t this [memory management] be done by another LM? Shouldn’t the AI do the memory management for the AI?"*  
- *"The key thing we're trying to do is understand what's in the context window… and how to structure it effectively."*  
- *"Humans form memories, but LMs need external systems to retain information. That’s the gap we’re trying to bridge."*  

---

## Actionable Items
1. **Adopt Memory-Aware Frameworks**: Experiment with tools like **LangChain** or **MemGPT** to manage context more efficiently.  
2. **Improve Observability**: Use logging and tracking to monitor how context is structured and retained in long interactions.  
3. **Explore Context Compilation**: Design systems that dynamically organize memory (e.g., via semantic clustering or prioritization).  
4. **Leverage Stateful Databases**: Store information beyond token limits using external databases to enable complex, long-term agent behavior.  
5. **Stay Updated on Research**: Follow developments in memory management for AI, such as Packer’s work on MemGPT and stateful agent architectures.  

---

**Note**: The transcript ends mid-discussion, so the conclusion is incomplete. The full session likely expands on practical implementations of MemGPT and case studies for real-world applications.

## Full Transcript

[00:10] So today I'm going to be going over a
[00:12] workshop. So there is like an
[00:13] interactive component. I think you can
[00:15] probably get a lot out of this talk just
[00:17] by watching. But if you do want to
[00:18] participate, um you're going to probably
[00:21] want to install Docker on your laptop if
[00:22] you don't already have it. And then
[00:24] you're going to want to pull this Docker
[00:25] image. Uh if you do this, it should be
[00:27] very easy to follow along. There's also
[00:28] a notebook in the channel. It's called I
[00:31] think like workshops letter and you can
[00:33] just hop over to the I think I also made
[00:36] like a tiny URL for it. Um but if you
[00:38] hop over to this link, this is like the
[00:40] notebook I'll be running over for maybe
[00:42] like the first 30 minutes. And this
[00:43] notebook is kind of like a client and
[00:46] the client needs to run against the
[00:47] server and the Docker image is what
[00:49] would be the server in your case. Um so
[00:52] again, I'll leave this up for a few
[00:53] seconds. This is basically where you're
[00:55] going to go get the
[00:59] notebook. And then and I believe this is
[01:02] also in the in the slack
[01:05] channel. And then yeah, the main thing
[01:08] you're going to want to do if you want
[01:09] to follow along and you have Docker
[01:10] installed is like docker pull. Um I
[01:12] guess like a quick show of hands like
[01:14] how many people here have Docker
[01:15] installed on their laptops? So okay,
[01:18] sweet. Yeah, most of us. Okay, great.
[01:21] Um, okay. Does anyone need a few minutes
[01:24] or anything? Um, I guess the people who
[01:26] do want to kind of follow along, just
[01:27] make sure to check out the workshops
[01:29] channel. Um, and of course, this is
[01:31] recorded and then all the materials will
[01:32] be online, so it'll be very easy to kind
[01:34] of follow along later as well.
[01:36] Yeah. So, I believe the title of this
[01:39] workshop was um like agent memory, the
[01:41] LMOS. Uh, I think maybe a better title
[01:44] for the workshop is stateful agents. So,
[01:46] I think you probably heard a lot about
[01:47] agents um over the course of this
[01:49] conference. as I also would like to pull
[01:52] the room like how many of you if you
[01:53] think you were asked today to give like
[01:55] a bit a concrete definition of an agent
[01:56] would be like pretty comfortable in what
[01:58] you what your definition
[02:00] is. Okay. Yeah. So despite hearing you
[02:03] know a lot about agents over multiple
[02:05] days it's still pretty hard to define. I
[02:07] think this is kind of a problem that's
[02:10] become much worse over the past year and
[02:12] I think that's why it's kind of useful
[02:14] to maybe like sharpen our definition of
[02:16] agents. So I like this term staple
[02:17] agent. Um, I think staple agent actually
[02:20] is kind of what agent meant before, you
[02:22] know, the LM era. And I think these
[02:24] days, I think a very common definition
[02:26] for agent is it's like an LM that's
[02:28] taking actions in a loop, right? I think
[02:30] that kind of that kind of works, but it
[02:33] also misses a really big um part of that
[02:36] process, which is that when you run the
[02:38] loop, it's a closed loop and the agent
[02:40] gets updated. And it turns out that, you
[02:42] know, in this new wave of AI, the
[02:44] fundamental unit of compute we're using
[02:45] for AI is stateless. It's not, you know,
[02:48] a recurrent neural network. It's not an
[02:50] SSM. It's a transformer. And the
[02:52] transformer inherently is like a
[02:54] stateless machine. So that means that
[02:56] when you close the loop, you have to
[02:58] have some sort of mechanism for updating
[02:59] the state. And you know, traditionally,
[03:01] like when agent was defined back in like
[03:03] the RL days or like back, you know,
[03:06] before pre-LM, I don't think this really
[03:08] was that big of a distinction to make
[03:10] like staple versus not staple agents. I
[03:12] think because LMs are stateless and
[03:13] that's like what everyone is using for a
[03:15] for AI now it's a pretty important
[03:17] distinction. So hopefully by the end of
[03:18] this talk you kind of understand what
[03:20] staple agents mean and you probably
[03:22] hopefully agree with me that um
[03:23] stapleness or memory is actually
[03:25] probably the most important thing to
[03:27] solve if we actually want to get you
[03:29] know if you want 125 be the year of
[03:31] agents or if you want agents to actually
[03:33] deliver on any of the
[03:36] hype. Yeah. So when I talk about
[03:38] stapleness, I think stapleness is pretty
[03:40] synonymous with memory. I think that's
[03:43] because LM effectively have no memory.
[03:45] They just have the memory that's in
[03:46] their weights and then they have what's
[03:47] in the context window. Um so like memory
[03:50] and state, context, these are all kind
[03:52] of synonyms with LM or like LM driven
[03:54] AI. And humans are of course stateful.
[03:57] So humans they form new memories. They
[03:59] learn over time and LMs don't. So any of
[04:02] the learning you're going to do is going
[04:03] to have to be done by you, the user of
[04:05] the LM or by the framework, but it has
[04:08] to be done by somebody. And
[04:09] traditionally, you know, in the past few
[04:10] years, I think by default, this just
[04:12] means appending to a list, right? And I
[04:14] think for workflows and like stuff we
[04:15] were playing around with from 2022 to
[04:17] 2024 when not a lot of people
[04:19] necessarily cared about like making
[04:20] money um or doing useful things with
[04:22] agents, that was okay. But I think it
[04:23] becomes a very big problem when the only
[04:25] mechanism you have to handle state when
[04:27] you're actually trying to use agents to
[04:29] do useful things is kind of appending to
[04:31] some sort of list and a list that's like
[04:33] held in Python process memory or you
[04:34] know in uh like a Node.js
[04:39] process. So the natural question is if
[04:43] we have LM and LM are stateless and
[04:45] basically the main thing we want to get
[04:46] out of state is we want to have
[04:48] humanlike intelligence that means
[04:49] learning. So how do we actually do that?
[04:51] um is how many people here have like
[04:53] heard of an MGPT?
[04:55] Um okay. Yeah. So before I was you know
[04:58] doing the startup Leta I was a PhD
[05:00] student at Berkeley and the CHAGPD stuff
[05:03] happened in the middle of my PhD which
[05:04] is kind of like interesting because it
[05:06] meant that like most people doing
[05:07] research kind of pivoted their research
[05:08] entirely. Um so in the few years of my
[05:11] PhD post chat GBT I was really focused
[05:13] on memory and agents and I wrote this
[05:15] paper called megpt with a bunch of my
[05:17] colleagues and some of my co-workers now
[05:19] at lettera. Um and this is really
[05:22] talking about like a memory management
[05:24] system for LMS. So if LM can't if they
[05:28] need some sort of memory management and
[05:29] the de facto way we do this is like a
[05:31] human appends to a list. Well if you
[05:32] believe LM get better and better and
[05:34] better shouldn't this be done by another
[05:35] LM? like shouldn't the AI do the
[05:37] management for the it shouldn't AI do
[05:39] the memory management for the AI. So
[05:41] when we called like this a me an LMOS we
[05:43] really referring to like a memory
[05:45] management
[05:46] system and this is effectively like a
[05:50] very high level graph or high level
[05:52] figure of what I what I mean by like
[05:53] statelessness versus statefulness on the
[05:55] left is basically what most people do.
[05:57] Um you know you kind of have a context
[06:00] window. The context window is pretty
[06:01] loosely defined. It doesn't necessarily
[06:03] uh it's not broken up into very distinct
[06:05] pieces. It's not tied to any state in a
[06:06] database per se. This is just something
[06:08] that's held in process memory and you're
[06:09] like appending to it over time. This is
[06:11] what happens if you use lang chain like
[06:13] in the lane chain buffer memory or like
[06:14] query. This will got get buried really
[06:16] deep in the codebase. And this is
[06:17] actually you know often why you need
[06:19] tracing software like observability.
[06:21] Observability kind of exists as a
[06:22] category because you have this black box
[06:24] of tokens that just gets shoved into the
[06:25] LM and stapleness or like staple agents.
[06:29] And the the key thing we're trying to do
[06:30] is understand that you know what's in
[06:32] the context window if we have a machine
[06:34] assembling it there's some that means
[06:36] there's some sort of like context
[06:38] compilation problem where there's an
[06:40] optimal way to arrange the context
[06:41] window of an LLM and that context comes
[06:44] from state the state can be kind of very
[06:47] large much more than can ever fit in the
[06:49] context window and this is basically
[06:51] what you do if you're a power user of
[06:53] chatpt or a power user of claude you're
[06:55] doing this yourself right you're kind of
[06:57] like compiling the context every time
[06:59] you start a new chat because I think a
[07:00] lot of us, you know, probably have
[07:02] experienced like having a chat that goes
[07:04] like way too long. It starts to derail
[07:05] and then you have to redescribe
[07:06] everything you were doing back to chat
[07:08] GPT like a pretty painful experience.
[07:09] Um, so can we basically automate this
[07:11] with a
[07:13] machine? So yeah, taking a step back
[07:16] like why do we even want staple agents?
[07:18] Like why are agents we have today not
[07:20] enough? like why is the a why is the
[07:23] current like paradigm of LM driven
[07:24] agents like not good enough to reach
[07:26] let's say like AGI or like some like the
[07:28] AI we see in science fiction. I think
[07:31] the main problem is that agents we have
[07:32] today they just can't learn from
[07:34] experience um or the way they learn from
[07:35] experience is extremely limited. And I
[07:37] think if you're just running like
[07:39] workflows um you might not notice this.
[07:41] So you might it might not really be a
[07:43] big problem but I think if you're trying
[07:44] to build like assistants companions
[07:47] co-pilots this becomes like pretty
[07:49] evident. Um, so imagine if you have some
[07:52] sort of chatbot. So this is a a direct
[07:54] screenshot from like the MGPT paper. Um,
[07:56] but you have an AI and a user and the
[07:58] AI, you know, it say it can see that
[08:00] it's February 14th. So it wants to like
[08:02] ask the user what they're going to be
[08:03] doing on Valentine's Day because they
[08:05] have stored in their memory some
[08:06] recollection that the user's boyfriend
[08:09] is James. So the the AI asks like, "Oh,
[08:11] hey, how's James doing? Do you have any
[08:13] special plans today?" And, you know, the
[08:15] user says, "Actually, you know, James
[08:16] and I broke up." Um, so it's obviously a
[08:18] very very bad mistake by the AI, but
[08:20] maybe it's like kind of unavoidable. Um,
[08:23] but you see the AI here, if it has some
[08:25] notion of like a permanent readr store,
[08:28] it should do something like transact
[08:30] that you know James is no longer the
[08:32] boyfriend. James is the ex-boyfriend.
[08:34] Um, and if you don't do this kind of
[08:35] thing and you run your agents for long
[08:38] enough and you just do like recursive
[08:39] summarization or if you just have like a
[08:40] really long context model, you're
[08:42] inevitably going to make some mistake
[08:43] where you tell, you know, you tell the
[08:45] user something about your boyfriend
[08:46] James and that's like a devastating
[08:48] error if you're trying to build like a
[08:49] consumer app, right? And it's also
[08:51] something that just a human would never
[08:52] do. I think like humans, something like
[08:54] this would get like written to your
[08:55] quoteunquote core memory very
[08:57] aggressively.
[08:58] I think the other reason you want
[09:00] stapleness and learning um I think many
[09:03] of us here maybe like kind of work
[09:04] companies and we're trying to like use
[09:05] agents to make money or like drive value
[09:08] you know for shareholders or whatever um
[09:11] but at the big difference between
[09:13] consumer and enterprise is obviously
[09:14] data like enterprises have much more
[09:17] data they can ever fit into like Gemini
[09:19] 10 million tokens right often like per
[09:20] user you have more than 10 million
[09:21] tokens so how do you actually like learn
[09:24] from that data so you we can kind of
[09:26] think of there being like another
[09:28] training phase after the post- training
[09:31] like during post- training, right? You
[09:32] train the model and then now the model
[09:34] is deployed into your enterprise and the
[09:35] model should kind of learn about your
[09:38] company, right? And that's kind of like
[09:39] training again, but it's not training
[09:40] into the weights. It's training like
[09:42] into the incontext memory. Um, so staple
[09:45] agents naturally kind of like
[09:46] encompasses this concept. And this is
[09:48] like pretty useful if you're trying to
[09:50] build this this kind of stuff inside of
[09:51] companies.
[09:54] And yeah, again, like really the reason
[09:56] I was kind of inspired to work on like
[09:58] the MEGPD stuff and also the reason I'm
[10:00] really excited to be doing the work I'm
[10:01] doing at Leta is because I'm very
[10:03] interested in just AI and making AI that
[10:06] is very humanlike and clearly there is
[10:08] some very serious deficiencies with the
[10:09] current iteration of LM agents. Um
[10:11] they're not very humanlike especially
[10:13] with respect to how they deal with
[10:16] memory. Yeah. So I covered this already.
[10:18] I think this is like a tweet I saw a few
[10:19] weeks ago or something I thought was
[10:20] pretty funny. Um, but I think, you know,
[10:22] if you all use chat in this room here,
[10:24] this is probably like a pretty universal
[10:25] experience. You kind of have a a
[10:27] conversation that goes on too long and
[10:29] then, you know, you feel very devastated
[10:31] because you're now going to have to
[10:33] mentally context compile again to like
[10:35] redescribe to chatbt what's going on or
[10:37] like flaw or whatever you're
[10:38] using. So, the promise of staple agents
[10:41] um there's actually a lot of promise
[10:43] just in product, right? I think if you
[10:45] actually have true statefulness, then
[10:47] that means that you know this sort of
[10:48] experience shouldn't happen. there
[10:50] shouldn't be any derailment. So you
[10:51] shouldn't have, you know, like a clawed
[10:53] instance going haywire. Um, and actually
[10:56] you should have the opposite happening
[10:57] like the the experience should get
[10:59] better and better and better over time
[11:00] as the AI kind of learns more and more
[11:01] about you. And this is, you know, kind
[11:03] of like maybe the promise of trackp
[11:04] memory. Um, but you know, I don't think
[11:06] any of that stuff is really working that
[11:07] well. And of course, I think when you
[11:11] don't when you no longer just like shove
[11:12] stuff into a context window when instead
[11:14] you're kind of really like creating me
[11:17] humanlike memory constructs, I think the
[11:20] behavior of the agents just becomes more
[11:21] human like you have the same kind of
[11:23] like fuzzy memory that a human has. You
[11:25] have the same kind of forgetfulness, but
[11:26] you also have the same kind of
[11:28] recall. So in today's workshop, I think
[11:31] it's kind of going to be split into two
[11:32] parts. I think the main thing we're
[11:33] doing at the front is a notebook. And of
[11:35] course like you don't you can just watch
[11:37] um but if you want to you can follow
[11:39] along in the actual the uh the Jupyter
[11:41] notebook file. And the goal of that
[11:43] notebook will just be to like lay out
[11:45] the basic ideas um behind this sort of
[11:48] like context management system in an
[11:50] LLM. And at a very very high level you
[11:52] know if I had to describe it in one
[11:54] sentence it's just that you make an LM
[11:56] either the main LM or like the
[11:57] subconscious memory system LM just aware
[12:00] of the context problem. You kind of can
[12:01] just describe to it in English. Hey, you
[12:03] are an LM and you have a context window
[12:05] of like 128k tokens and I will let you
[12:07] know when you reach 100k tokens and
[12:10] you're going to have to like manage
[12:11] memory with these tools. So, it's all
[12:12] centered around tool calling. Uh, and I
[12:14] think centering around tool calling is
[12:16] actually very effective because LM are
[12:17] getting better and better and better at
[12:18] tool calling. And the second part of
[12:21] this workshop is going to be um kind of
[12:24] like building these building these
[12:26] stateful agents in um the letter
[12:28] framework and then also like the
[12:30] front-end ad. So I think if you're very
[12:33] interested in kind of like no code
[12:34] stuff, I think this is pretty
[12:36] interesting because I think we're all
[12:38] very very familiar with the paradigm of
[12:40] the playground, right? It's like
[12:41] ubiquitous. Every single AI company has
[12:42] their own playground. But I think once
[12:45] statefulness and like staple agents
[12:47] become the dominant paradigm, which I'm
[12:48] pretty sure they will. Um then I think
[12:51] you're going to have there's going to be
[12:52] a new iteration of the playground. And
[12:54] the AD that we built, I think that's our
[12:57] best guess as to what that experience
[12:58] will look like. But I'm sure like
[12:59] everyone in this room who's worked very
[13:01] who has like spent a ton of hours with
[13:03] LMS, you probably have a very strong
[13:04] opinion too on what that experience will
[13:06] be like. Like what happens when you know
[13:08] chat GBT is no longer like it no longer
[13:12] has like a history bar on the side and
[13:13] says it's like a unified experience like
[13:15] what is the correct UX for that? What's
[13:17] the correct DX? Um and then if it's not
[13:19] a consumer app like chatbt if it's a de
[13:21] developer tool like what do you as a
[13:23] developer want to see from your agent?
[13:24] Like you probably want to see all the
[13:26] way down to the context window.
[13:29] So, I said this at the beginning. I
[13:30] don't think any anyone necessarily
[13:32] walked in midway. So, if you're going to
[13:34] follow along, you're going to want to
[13:35] download Docker on your computer. I
[13:36] think most of the people in this room
[13:37] have Docker on their computer. You can
[13:38] do this with PIP, but PIP is pretty
[13:40] terrible at package management, so you
[13:41] might like hit a bug. Um, and yeah, I
[13:44] already covered this, but if you're
[13:46] interested in any of the ideas that I'm
[13:47] going over in the initial notebook,
[13:48] they're basically just strongly
[13:50] distilled versions of the ideas from the
[13:52] METPD paper. um like reduced to their
[13:55] like most simple um yeah their most
[13:58] simple components. But if you're like
[14:00] interested in this more like a research
[14:02] capacity, you can also just read this
[14:05] paper. Okay. And yeah, we're going to be
[14:09] doing this in Python. Um I guess like
[14:11] how many people in this room have use
[14:14] Python as their main language versus
[14:16] Okay. And I imagine like everyone else
[14:18] is Typescript or something. Yeah. So
[14:21] basically what we're going to be doing
[14:23] is Python, but leta the um server is not
[14:25] Oh, maybe Go or Rust. Okay. Yeah. Yeah.
[14:29] So we we don't have a Go or Rust SDK,
[14:31] but we have a TypeScript SDK and then we
[14:33] also have a REST API. And actually our
[14:34] Python SDK and TypeScript SDK are just
[14:36] like programmatically generated off the
[14:37] REST
[14:38] API. Okay, so I I left this on the
[14:41] screen a little bit earlier um to kind
[14:43] of like preempt any pauses here. So I
[14:46] might just like continue on. Um and yeah
[14:50] these are these links are all in the
[14:52] channel like workshops hypen leta on the
[14:55] the shared
[14:57] slack. Okay let me hop
[15:02] over oh and I think we because this
[15:05] workshop has a reasonable amount of time
[15:07] allotted to it um I'm very open to like
[15:10] pausing for questions and stuff. So if
[15:11] anyone has any questions, please just
[15:14] raise your hand. Not going to pause. And
[15:15] then if you're just going too slow, we
[15:17] can fix that
[15:18] later. Yeah. Okay.
[15:28] [Music]
[15:32] Questions? All right. So yeah, I guess
[15:35] how many people are actually going to
[15:36] attempt to follow along? It'll be useful
[15:38] for reference. Okay, decent amount of
[15:40] people. So, I'll try to Yeah, definitely
[15:42] uh raise your hand or something if
[15:44] something's going terribly wrong and
[15:45] you're not able to follow. Um let me
[15:48] boost the Okay. Is let me know when the
[15:52] font is large enough. Is this large
[15:53] enough for the people in the back to to
[15:55] read? Okay, great.
[16:06] And all
[16:09] right. Okay. So, if you ran the if you
[16:15] did the Docker pull, um the next thing
[16:18] you're going to want to do to b to start
[16:21] this entire uh notebook session is
[16:23] you're going to want to start the
[16:23] lettuce server. So if you were using
[16:26] Docker, the way you're going to do this
[16:27] is run this docker run command. I'm
[16:28] realizing now that this is not Oh, this
[16:31] is this is in you can copy paste this
[16:33] out of the GitHub um the GitHub link,
[16:36] but I'll also post it in the Slack.
[16:47] Yeah. And then if there's a free
[16:50] endpoint that's live, so you don't
[16:51] actually need to have these keys. Um, so
[16:53] you can just run this and it will you'll
[16:55] be able to run the demo
[17:01] fine. Okay. And then once you run it,
[17:04] you'll basically see the server kick off
[17:05] in the
[17:08] background. Yeah. So, while people I'll
[17:11] give everyone like a minute to do that.
[17:13] And while everyone is kind of kicking
[17:14] off their
[17:16] servers, might also just show you kind
[17:18] of a diagram of what's going on here.
[17:24] Yeah. So basically the way this whole
[17:27] stack works is leta is like it's an open
[17:30] source stack. Um it's basically fast
[17:32] API, Postgress and Python um in the
[17:35] middle like Python logic. So in that
[17:37] Docker container like it's exposing an
[17:40] API that's actually like very you know
[17:42] pretty robustly documented. You can like
[17:44] go to our API reference here. Um and the
[17:46] API is how you interact with all your
[17:48] agents. So if you're using the Python
[17:49] SDK, it actually just, you know, goes
[17:51] over the the REST API and you basically
[17:54] build your Asian applications on top of
[17:56] this API. So this actually looks very
[17:58] similar to like the chat completions
[18:01] API. It's just like session based,
[18:03] right? And so you don't have to provide
[18:05] the entire the entire conversation
[18:07] history every single time you interact
[18:08] with an agent. So we'll see that kind of
[18:10] immediately in the notebook as well.
[18:12] Okay. So I assume everybody who's
[18:14] following along has done the the thing
[18:16] to launch. Um is there
[18:18] Okay, it says that there's a directory
[18:21] that doesn't exist. Do I need to create
[18:22] that? Um, oh yeah, can you do
[18:28] liker and all that? Okay. Did anyone
[18:32] else get that directory doesn't exist
[18:34] problem? Can you
[18:36] send him because I can see Okay. Do you
[18:41] So, are you able to see this here?
[18:44] Oh, no.
[18:46] Okay. Yeah. So it's let me
[18:57] Yeah, that fixed it. Okay, great. All
[19:00] right, any other problems? Does everyone
[19:01] have a server idling now on their
[19:03] laptop? Great. Okay, so now that we
[19:05] started the server, um now we can kind
[19:07] of like start running the notebook. So
[19:10] this part is
[19:13] basically you're going to go to this go
[19:15] to this channel click on this link
[19:18] you're going to see a readme and the
[19:19] readme has all the commands so I I'll
[19:21] kind of like go one by one and paste
[19:22] these commands into the workshop channel
[19:27] it's a workshop leta
[19:30] yeah okay so you need basically clone
[19:33] the repo
[19:40] Once you clone the repo, just CD into
[19:42] the specific
[19:51] example. I'm assuming everyone's using
[19:53] Docker, so I'm just going to kind of
[19:54] ignore that.
[19:59] Um, okay. And
[20:02] ideally everyone has Python installed in
[20:05] their laptop hopefully.
[20:28] Yeah. Yeah. And then once you run that
[20:30] Jupyter notebook command, um all you
[20:32] need to do is just double click on the
[20:34] notebook here, if you're not familiar
[20:36] with um
[20:38] Jupiter, it should automatically like
[20:40] open a browser tab that should have this
[20:42] and then you just like double click and
[20:45] you'll open the
[20:49] notebook. Okay. So among the people who
[20:51] are following who is a little still not
[20:54] to this notebook stage yet?
[20:57] Okay. Yeah. still so it's been a while.
[21:00] Okay. Yeah. Yeah. No
[21:03] problem. Okay. No other issues. Nothing
[21:07] on fire
[21:08] yet. Okay.
[21:25] All right. How's the Jeep
[21:26] looking? I had to spell that.
[21:31] Okay. Okay. So, everyone has this
[21:35] notebook up who is intending to follow
[21:36] along. Great. All right. So, yeah, if
[21:40] you're not familiar with notebooks, you
[21:41] basically just execute them cell by
[21:42] cell.
[21:43] Um, I mean number the first thing you're
[21:46] going to have to do here is like import
[21:47] the client. So, again, this is a little
[21:49] bit different from some other frameworks
[21:51] you're familiar with. Like I assume
[21:52] everyone here has like used lang chain
[21:54] before probably or heard of it. um well
[21:57] like crew AI, autogen
[21:59] um padantic uh AI things like that. So I
[22:03] think among those frameworks there's a
[22:05] pretty big distinction with leta and
[22:06] that leta is like a server client
[22:08] process and a big part of that is
[22:09] because the agents are intended to be
[22:11] staple and like persist indefinitely. So
[22:13] it's very hard to like persist things
[22:15] indefinitely if you're kind of holding
[22:16] everything in application state as
[22:18] opposed to having like a server that's a
[22:19] centralized source of truth. So we
[22:21] basically run the server on the left. Um
[22:23] we connect to the client. You know, you
[22:25] can actually park the server anywhere
[22:26] you want because it's a Docker image.
[22:27] You can like run this in the cloud. It's
[22:29] very easy to like drop on Kubernetes or
[22:30] something. In this case, it's running on
[22:32] our laptop. So we just need a local host
[22:34] and the default port. So the first thing
[22:36] we're going to do is create an agent. So
[22:39] I want to make sure that everyone can
[22:40] like execute this cell. So I'm going to
[22:42] execute it one more time. And you saw
[22:44] like my server kind of fired off on my
[22:46] left.
[22:48] Um yeah. So I I'll kind of walk everyone
[22:51] through the code here. So basically, you
[22:53] know, with chat completions, which I
[22:56] assume everyone's familiar with, the
[22:58] paradigm is you create the agent in
[22:59] memory and then you kind of like pass
[23:01] the whole agent off to the server and
[23:03] ask like, you know, complete the state,
[23:05] complete like this one more message in
[23:07] my in my message history. Instead of let
[23:09] we we first create the agent and then
[23:11] once we we create the agent, we have a
[23:13] handle for it. And once we have that
[23:15] handle, we can kind of send it messages
[23:16] and we never have to send it the full
[23:17] state. We don't have to track that
[23:18] anymore. we just send individual
[23:20] messages.
[23:22] So the the main components of memory in
[23:25] a lettera agent is just memory blocks.
[23:27] So these are just strings. Um in this
[23:30] case, you know, we're doing something
[23:31] pretty simple and stupid like the
[23:32] human's name is Bob the builder. Um and
[23:35] then the persona for the agent, we're
[23:37] just using that my name is Sam. Um this
[23:39] AI and this is all arbitrary. The only
[23:42] things that these handles are useful for
[23:44] actually is for the agent to edit these
[23:45] own handles or edit the values on these
[23:47] handles. So, as we'll be able to see
[23:49] later in the notebook, the agent can
[23:51] actually go in and like rewrite its own
[23:52] memory. So, if the agent, you know,
[23:54] decides that I like ice cream or I like
[23:55] vanilla ice cream, it can write to its
[23:57] memory block, you know, I'm no longer
[23:59] just Sam the AI, I'm like Sam the the AI
[24:01] that likes vanilla ice cream, right? Or
[24:04] if you know Bob the Builder says,"I
[24:05] broke up with my girlfriend um or my I
[24:09] broke up with my boyfriend James." You
[24:10] know the the AI can actually use this
[24:12] handle to go in and edit this block of
[24:15] the string and say, you know, the
[24:16] human's name is Bob the Builder and they
[24:17] also broke up with their boyfriend
[24:19] James.
[24:21] Yeah, a quick question. So what's the
[24:23] difference between persona and building?
[24:26] Yeah, so it's there's really no
[24:29] difference under the hood. These are all
[24:31] just strings that have references. Um,
[24:33] but if we look at the system prompt, I'm
[24:35] going to dump the system prompt a little
[24:36] bit later. We did in the system prompt
[24:38] write some stuff about the human and the
[24:40] persona that the human block is meant
[24:41] for like the user interacting with the
[24:43] agent and the persona is meant for the
[24:45] agent to kind of adapt this interaction
[24:47] style. Right. So there's kind of like a
[24:49] base agent and then the base agent gets
[24:50] further mutated by this persona. Yeah.
[24:54] Okay. Any other questions about anything
[24:56] here? Um the you know here we're you
[24:59] would if you're using OpenAI or
[25:00] something you'd do OpenAI like GPT4 but
[25:02] we're just using a free endpoint. Um one
[25:05] thing that we'll get into a little bit
[25:06] later is that in Leta because the entire
[25:09] premise of the like runtime is that it's
[25:11] a context management system. So it
[25:12] controls the context window. It's
[25:14] actually very easy to artificially uh
[25:16] cap the context window length. So you
[25:18] can have agents that basically will
[25:19] never send a payload over 10k tokens
[25:21] let's say. I think that's actually very
[25:22] common in enterprise settings where
[25:24] you're running like a workflow for a
[25:25] very long period of time. it's getting
[25:26] longer and longer and longer. Like
[25:28] something you'll hear from a lot of
[25:29] companies that use Sonnet for example is
[25:31] like how do I prevent my payload from
[25:33] creeping up to 200k, right? Because if
[25:34] you feed 200K, you're waiting like
[25:36] minutes on a response, right? Whereas
[25:37] like even 10k tokens, I think on sonnet
[25:39] you'll wait like 10ish seconds or
[25:40] something. Um in many cases, you kind of
[25:42] want to like cap the context window to
[25:44] be really short, like 4K, but then you
[25:46] also want the agent to like not have any
[25:48] perceived loss of memory. You want it to
[25:50] kind of like retain its memory over
[25:52] time.
[25:54] Okay. So, let's actually like yeah
[25:56] message the agent. Um there's a link
[25:58] here that we'll this is what we'll do in
[26:00] the second half of the workshop. We'll
[26:01] look at like the UI builder, but for now
[26:03] we'll just like stick in Python. We'll
[26:05] stick to Python. Um so yeah, if we run
[26:08] this message, we're going to say
[26:09] something like how it's going. You're
[26:10] see seeing on the left the server is
[26:11] firing. Um and we can print the response
[26:16] here. Uh so in leta like every single
[26:19] agent actually comes with reasoning by
[26:21] default. And this allows you to like
[26:23] keep reasoning that you built in like R1
[26:25] and like port it over like a GPD40 mini
[26:28] or something. And there's just like
[26:29] different forward adapters for the
[26:30] reasoning. Um but yeah, any are there
[26:34] any questions about this? We basically I
[26:35] think this should be something a lot of
[26:37] people here are familiar with, right?
[26:38] This like dictionary that's in chat
[26:40] completion style we pass over to the
[26:41] server. Um and then yeah, we have a
[26:44] message here that's like you know the
[26:45] user is reaching out casually. Let's
[26:46] match their energy. Hey there, I'm doing
[26:48] great. How about you? Um, you can even
[26:50] do something like again because this is
[26:53] um because this is
[26:57] staple. This is actually when I send
[26:59] this, it's going to be a follow-up
[27:00] message. It's not going to be like a
[27:01] fresh chat. So, if you say, "What do you
[27:03] know about
[27:05] me?" See, the agent now says, you know,
[27:07] the user wants to know about what I've
[27:08] retained about them. All I know is that
[27:10] your name is Bob the Builder. If you
[27:12] want to share more and like, you know, a
[27:14] ridiculous amount of emojis. I think
[27:15] this is because under the hood this free
[27:16] endpoint is running GP4 mini which is
[27:18] like pretty emoji prone. Yeah. Five and
[27:21] I'm also getting a chain of thought.
[27:23] Where is that coming from? Yeah. Yeah.
[27:25] So, so one thing about let is we kind of
[27:27] force all the agents to follow a react
[27:29] style pattern with like reasoning and so
[27:33] um kind of down in the weeds like the
[27:34] way it works is like sonnet itself or
[27:37] claude when you use like the chat or the
[27:40] um the consumer app it packs like ant
[27:42] thinking XML tags in. So like it already
[27:45] is like kind of a reasoner in some
[27:46] capacity and because of we know that it
[27:49] uses like XML tags like that we can
[27:50] actually like force those into the
[27:52] content field. So we like actually
[27:53] inject and parse those out.
[28:00] Yeah. Okay. Yeah. And then just to like
[28:02] further drive home the point that this
[28:03] is stateful we say sure. Um I feel like
[28:06] sure if it was like an opening message
[28:08] would be pretty confusing. The agent
[28:10] would say something like I don't know
[28:11] what's going on.
[28:13] Um but in this case it's seems open to
[28:16] sharing more. Okay bad it's bad model
[28:20] behavior but yeah um but we'll see also
[28:23] later in the AD you can just see well
[28:24] it'll be like a UI experience so you can
[28:26] kind of visualize this a lot better. I
[28:27] just wanted to start with Python. Um
[28:29] yeah so basically there's like three
[28:31] different me or there's a handful of
[28:32] message types that are going to be a
[28:35] little bit different from OpenAI but
[28:37] they're still rooted in the same
[28:38] concepts. reasoning message. Um you're
[28:40] probably familiar with this if you use
[28:42] like the R1 API from Deep Seek. You use
[28:44] any of the 01 03 models. So we have the
[28:46] same sort of content field. There's also
[28:48] assistant message. So um this is because
[28:51] like content itself is treated as inner
[28:53] monologue or reasoning all the time. Um
[28:55] so this is like distinct and and these
[28:58] are like pretty straightforward like
[28:59] tool call message, a tool call return,
[29:01] the system message and the user message.
[29:03] Um obviously like a very important part
[29:05] about being an agent framework is often
[29:07] executing the tools for the agent. Um
[29:09] you know like OpenAI they don't execute
[29:11] tools for you unless it's one of the
[29:12] pre-approved tools like code
[29:13] interpreter. Let these other frameworks
[29:15] like you know langraph or link chain um
[29:17] we execute tools on the server side. So
[29:20] that's why we're able to like provide a
[29:22] tool called return and in leta like the
[29:24] tools are actually also sandboxed um by
[29:28] default. Okay. Uh any questions about
[29:32] this like initial message we sent? Um or
[29:36] Okay,
[29:37] great. Yeah. So the next thing we're
[29:39] going to do is basically just like
[29:40] unpack all the state of the agent. So
[29:43] the reason this is like kind of
[29:44] interesting is because this is
[29:47] fundamentally everything that the agent
[29:49] is, right? The agent is just its system
[29:51] prompt, its tools, and then in let us
[29:53] specifically we have a concept of like
[29:55] three tiers or two tiers of memory. The
[29:56] core memory that's in the context
[29:58] window. So, this is like very top level
[30:00] stuff. You know, if you see your friend
[30:01] on the street, um you see their face,
[30:03] you immediately remember stuff about
[30:04] them like their name, their hobbies, the
[30:06] last time we chatted, but if they're a
[30:08] childhood friend, you don't remember
[30:09] what you did like 10 years ago on a
[30:11] random like, you know, February 22nd,
[30:13] 2001, right? That's not going to be like
[30:14] default in your brain, but it might be
[30:16] visible to you if you like went on your
[30:17] phone and you went through your eye
[30:19] photos, right? Um, so it's a pretty
[30:20] similar concept where like we want
[30:22] because at the end of the day LM,
[30:24] they're kind of like mimicking human
[30:26] reasoning, mimicking human behavior. it
[30:28] makes a lot of sense to actually kind of
[30:29] like mimic in text the way human memory
[30:32] works. So we have core memory that's
[30:33] like top level and then we have what we
[30:35] call archival and recall but these are
[30:37] effectively just data sources that exist
[30:38] outside the context window and the agent
[30:40] can like quote unquote jog its memory if
[30:42] it wants to think about something. So it
[30:44] can say like hey like what did I do um
[30:46] you know what did I do with Charles
[30:48] February February 22nd 2001 and it can
[30:50] like attempt to search the database. So
[30:52] you probably heard a lot about like
[30:53] agentic rack. This is effectively the
[30:55] same concept.
[30:59] Can we change the system prompt? It says
[31:00] read only there, so we cannot change it.
[31:02] Oh, so the agent can't change it, but
[31:04] you can change anything you want. Yeah.
[31:06] Yeah, you can change the system prompt.
[31:08] Um, yeah, the system prompt actually is
[31:10] like quite old. You wrote it like when
[31:12] this is written like when the initial
[31:14] MGBT like research was being done like
[31:16] in summer of 2023 or something. Um, so
[31:18] yeah, you probably do want to change
[31:19] this if you're running something in
[31:20] production. Yeah. Um, the other thing
[31:24] that's stored in here are tools. So by
[31:27] default because you know Mamgbt agents
[31:30] they have like memory management built
[31:31] in they need tools to manage their
[31:32] memory. So core memory we have two
[31:34] things like appending to blocks. So
[31:36] saying like the user is not only Bob the
[31:38] builder but they also have a boyfriend
[31:39] called James replacing you know the
[31:41] user's name is not Bob the builder it's
[31:43] actually Charles. Um and then like
[31:45] searching memory you can either do a
[31:47] very specific conversation search or
[31:48] more generic like rag query. And then
[31:51] you can also like insert into this
[31:52] external database. So if you look at
[31:54] like what's actually in the memory if
[31:57] you're kind of into like API style
[31:59] programming like you can basically do
[32:01] whatever you want with your memory
[32:02] blocks because it's just you know these
[32:04] are just strings that exist in Postgress
[32:06] in some table and they all they all have
[32:08] identifiers they have block ids so you
[32:09] can read and write to them. Um you can
[32:12] also share these blocks among agents so
[32:14] you can have a bunch of agents that are
[32:15] all acting as part of your organization.
[32:17] say it's like a multi- agent system and
[32:18] because the blocks just live in a
[32:20] database and they get sent they get
[32:22] brought out of the database whenever the
[32:23] agent needs to think you can have these
[32:25] blocks like linked together so multiple
[32:26] agents can have the same block like they
[32:28] can all share information about the AI
[32:30] engineer conference that's held in one
[32:32] block of memory it doesn't have to be
[32:33] duplicated and then when one writes the
[32:35] block it like immediately gets
[32:36] broadcasted
[32:38] by definition does all of the all of the
[32:41] archives in memory have to also be in
[32:43] the recall if the recall contains all
[32:46] the history that also contains anything
[32:48] about would have been archived. Yeah.
[32:50] Yeah, that's a great question. I think
[32:51] the difference between archival and
[32:53] recall really comes down to like if
[32:55] you're using this for like a chat style
[32:57] application. Um, when we like worked on
[32:59] the original MEGPD project, we're
[33:01] actually like a little bit conflicted as
[33:03] to whether to like merge these into one
[33:05] general concept because at the end of
[33:07] the day like with an LM there's the
[33:09] stuff that's in the context window and
[33:10] the stuff that's out of the context
[33:11] window. So why do you have to like start
[33:12] being prescriptive about like the way
[33:14] the stuff out of the context window is
[33:15] stored? Um we just thought in most use
[33:18] cases people want to give their agents
[33:20] the ability to specifically look at
[33:22] prior messages. Um and then separately
[33:25] there's just like a general readr data
[33:26] store. You can just like read arbitrary
[33:28] data, write arbitrary data. It's like an
[33:30] infinite size. So that kind of just
[33:31] looks like a vector database of strings.
[33:33] It could also be like something
[33:34] different. It could be like elastic
[33:35] search cluster whatever you want. But
[33:37] you are intentionally allowing some
[33:39] duplication between them. It's kind of a
[33:41] different way for the LLM to search
[33:43] effectively. Yeah, it's a different way
[33:45] for the LM to search. Well, the thing
[33:47] with the re if you set up a recall
[33:48] memory, the recall memory, it's
[33:50] effectively conversation history. So,
[33:52] conversation history you cannot manually
[33:54] write to. It's kind of like write
[33:55] protected, but it gets written every
[33:57] single time by default an event happens.
[33:59] Whereas the archival memory store is
[34:01] like something that you have to actively
[34:02] say, hey, I have like a huge document
[34:04] like this big PDF. I'm going to I don't
[34:06] want to keep it in in the context
[34:07] window. I'm going to dump it out of the
[34:08] context window. So that would be like
[34:10] the archival memory like free readr
[34:12] whereas the recall thing is purely
[34:15] trying to mimic like a conversation
[34:17] search function inside of um like
[34:19] iMessage inside of like WhatsApp or
[34:27] um how does tools memory tools um get
[34:33] used? Do they do we just have a flat
[34:35] list of like other tools that agents can
[34:38] use and memory tools would that affect
[34:41] the
[34:42] agent tool? Yeah, that's a great
[34:44] question. Um I I think by default if you
[34:47] just set up a basic agent in leta and
[34:49] then you start like adding more tools to
[34:51] it like tab search iical calendaruler
[34:54] whatever those will be just like more
[34:56] tools that get added to a list that
[34:58] started with six. Um, but of course like
[35:00] if you if you built a lot of agents with
[35:02] tools before, you know, there's like
[35:04] agents start to get confused if you had
[35:06] too many tools. So there is like a
[35:07] trade-off here. And one thing that we've
[35:09] been working on recently is basically
[35:11] the idea of having like a dedicated
[35:14] agent to just handle memory and it's
[35:16] effectively like a shadow of the other
[35:18] agent. It's like a like a subconscious
[35:20] that is like kind of it's like a ghost
[35:21] in the shell. It can't actually
[35:22] participate. All it can do is read and
[35:24] write memory. But when it reads and
[35:26] writes memory, it's like using a shared
[35:28] memory block. So, it's like reading and
[35:29] writing to something that like
[35:30] automatically updates like the uh the
[35:32] active agent. And that's a way to kind
[35:35] of like move all the tools that aren't
[35:36] for act like general API actions out of
[35:39] the main agent.
[35:43] Yeah. Are you familiar with the
[35:44] cognitive?
[35:47] What's that? Yeah. Yeah. So, a few
[35:50] different types of memory that are
[35:52] mentioned there would be things like
[35:54] longterm memory. So when you talk about
[35:57] things like recall or archival like is
[35:59] letup bringing those databases to like
[36:03] this interaction or is the developer
[36:06] responsible for bringing those databases
[36:08] to like this or something? Yeah. Yeah.
[36:10] Another great question. So I think with
[36:12] Koala um yeah another great paper. I
[36:14] think the inspiration from them is a
[36:17] little bit more from like the cogi angle
[36:19] whereas when we wrote the paper we were
[36:20] thinking more about like computers and
[36:22] memory harvey and computers. So for us
[36:24] like our answer to that is like oh you
[36:26] want to have like something that really
[36:27] starts to look like human memory
[36:28] semantic episodic you bring that and you
[36:31] can like add that as a plugin. Um but we
[36:33] all we care about is like the hierarchy
[36:35] of tokens. There's tokens that are in
[36:36] cache or like in context and tokens that
[36:38] are out of like the cache. Um, so yeah,
[36:42] basically if you wanted to have like
[36:43] some more psychological leaning concepts
[36:45] like from Koala, you could kind of like
[36:47] write them
[36:48] as as tools that either like populate
[36:51] the core memory or like sit outside and
[36:52] have to be drawn in. Yeah. Today I build
[36:55] like very transactional agents. So like
[36:58] the in this particular example, let's
[36:59] just imagine it's like a CRM. So
[37:02] probably not going to use Salesforce to
[37:03] track James's like status.
[37:05] Um, in theory, if we wanted to track
[37:07] something like that, that's like a safer
[37:09] system that has an object for people
[37:12] like a contact that I preserve in that
[37:15] like longterm system. So I'm trying to
[37:17] understand like if there's a
[37:18] differentiation in use case whereas like
[37:20] maybe we're just talking about like a
[37:21] local machine as opposed to like an
[37:23] enterprise environment with you know
[37:25] thousands of employees like can you
[37:28] maybe show that or tell me like why a
[37:31] tool that's responsive for tracking the
[37:33] state of James relationship um is worse
[37:36] or different than like a memory based.
[37:40] Yeah. So, um, yeah, correct me if I I
[37:44] I'm not understanding your question
[37:45] correctly, but one thing you can do is
[37:48] because like all these these memory
[37:50] blocks, they're all backed by an API and
[37:52] you can access them directly. So, if you
[37:53] go to it's like a blocks
[37:56] page, where is this? Okay, here we go.
[37:59] Yeah. So, you can basically like modify
[38:00] blocks by handle. So you can in your app
[38:03] layer effectively do something like
[38:05] every time your agent is run or invoked,
[38:07] you do a hard sync where like you're
[38:08] going to do some sort of Salesforce CRM
[38:10] compile down to a string and that string
[38:12] is going to get clipped at 10k
[38:13] characters and then that's going to get
[38:15] patched into the block. Um yeah, so you
[38:18] can do kind of stuff like that. Um, but
[38:21] I will say like the general way like
[38:24] Letto was designed is very much leaning
[38:26] on the thesis that like you just want to
[38:29] remove as much human design of memory
[38:31] management as possible and we're just
[38:33] like banking on the LM getting better
[38:34] and better and better and actually what
[38:36] you what you will see is like if you try
[38:37] to use R1 with a extremely annoying
[38:40] because like firstly the way the like
[38:43] reasoning APIs are designed is that
[38:45] you're not supposed to pass the
[38:46] reasoning from a subsequent step into
[38:47] the API again which means that like if
[38:49] an agent thinks for a very long amount
[38:51] of time and it's like oh I'm going to do
[38:52] this then this and this then this and
[38:54] it's like wow that was amazing that's
[38:56] exactly what you should do it actually
[38:58] immediately forgets in the next turn
[38:59] right it only gets to do one thing and
[39:01] that's to think again um so that's like
[39:03] one issue with like reasoners and react
[39:04] style agents but um you will notice that
[39:07] actually the tool use is like pretty
[39:09] exceptional um so I think that kind of
[39:11] like aligns with the thesis that these
[39:12] agents are just like going to get better
[39:13] and better and better at doing like the
[39:15] agent it's there could be a separate
[39:16] agent that does the CRM sync into a blog
[39:18] right it doesn't have to be done
[39:19] manually. Yeah. Um and then sorry final
[39:22] question here is the property that I
[39:23] think is most compelling for at least
[39:25] what I've seen so far is the
[39:26] distillation of the agent like into some
[39:29] kind of summary. So do you control like
[39:32] the perspective of like how a memory is
[39:35] bind how synthesis is actually like
[39:37] happening when it's creating memories.
[39:40] Yeah. So the the agent
[39:44] I see. Yeah. Well, if you have agents
[39:46] that are generating and synthesizing the
[39:48] memories, then you can always like tune
[39:50] their system prompts or their personas
[39:52] to like adjust the way the memories are
[39:54] written. Um, but yeah, it's it's all
[39:57] pretty configurable. Yeah.
[40:00] Okay. Maybe I'll take like one question
[40:01] in the back and then uh yeah, I have a
[40:04] more of a question. So if you think
[40:07] about the way we design
[40:12] um and microservices different
[40:18] system based on your discussion with
[40:20] enterprise customers especially do you
[40:22] see that we evolving
[40:25] towards agentic workloads where like
[40:28] microservices takes a back state and a
[40:31] workload
[40:37] I I think they can the two can exist uh
[40:40] they can coexist pretty easily um
[40:42] through the use of tools. So I think
[40:44] what I'm seeing in like enterprises is
[40:46] that there's just extremely heavy use of
[40:48] like I think almost every single agent I
[40:50] see being used in some company they're
[40:53] they're all like they're trying to
[40:55] connect tools to the agent. So and it's
[40:56] like pretty heavy tool use. Um, so I you
[41:00] can I think think about microservices
[41:02] like basically starting to become
[41:04] designed more for like agents maybe. I
[41:06] think that's like one thesis that a lot
[41:07] of people have. There's going to be like
[41:08] a new wave of APIs that are designed all
[41:10] for agents.
[41:12] Um, yeah, but I think the two will kind
[41:16] of like exist. Um, but I think there are
[41:18] like microservices that will become like
[41:20] agentified where like the microser
[41:22] itself has higher it's not like latency
[41:24] bound. So you can like run a fat agent
[41:26] on the back end and it's kind of like
[41:27] not super sensitive to error. So it's
[41:29] okay for it to just be smarter 99% of
[41:31] the time and then like completely break
[41:34] 1% of the time. Yeah. Okay. I'm going to
[41:37] keep going. Um but we'll definitely
[41:39] pause for more questions later. So okay,
[41:42] so we were just looking at like memory
[41:44] blocks. Um the other thing I think I
[41:46] might breeze over this a little bit um
[41:48] just for sake of time because we'll see
[41:50] it again visually and I think like
[41:51] visual stuff is always more interesting
[41:52] than just plain notebooks. Um but there
[41:55] is this problem if you have a system
[41:57] where there's a lot of information
[41:58] outside the context of the LM where like
[42:01] you can't know what you don't know right
[42:03] so if the agent doesn't see something
[42:05] how is it ever going to know that it has
[42:06] access to that? So a very simple
[42:08] solution is you can just provide like
[42:10] metadata statistics right so you can
[42:11] tell the agent somewhere in this context
[42:13] window that hey you have like 13
[42:14] previous messages and if you want to
[42:16] find them you can use this tool and you
[42:18] can also tell the agent that you know
[42:20] you have um like x total memories that
[42:22] are in your archival memory. So this is
[42:23] if you have like a vector database you
[42:25] can just explicitly say these are like
[42:27] the the
[42:29] statistics. Okay. And then if we look at
[42:31] like the messages that are actually in
[42:32] the message buffer um it's pretty
[42:34] straightforward stuff. Um, I think the
[42:36] really big difference between like Leta
[42:38] and another framework is Leta does very
[42:40] aggressive managing of this buffer. So,
[42:42] you can basically set it to like it's a
[42:44] much more intelligent version of like a
[42:45] recursive summarization mechanism,
[42:47] right? And lastly, this is like the the
[42:50] archival memory we're talking about. You
[42:52] know, there's nothing in there, so it's
[42:53] just going to be empty.
[42:55] Um, yeah. So I think just to drive home
[42:59] like what core memory really is and like
[43:01] how these memory blocks influence agent
[43:02] behavior because I think if you're
[43:04] developing agents the main thing you're
[43:05] going to be doing is like tuning in
[43:07] context memory. That's like the main way
[43:08] you change the the behavior of the
[43:10] agent. Um you know we could set we could
[43:12] tell the agent something like my name is
[43:14] actually Bob. And I think the last thing
[43:15] we told the agent is that you know
[43:18] um my name is actually Bob. I think our
[43:21] name is Bob. strange like my name is
[43:23] actually
[43:27] Charles. Okay, we can see actually
[43:29] you're seeing like a memory edit happen
[43:30] on the server. Um this is a pretty big
[43:32] dump if you look at what the agent said.
[43:34] So that you see the agent is like doing
[43:36] react style reasoning. It's saying the
[43:37] user has corrected their name. This is
[43:39] important. I'm going to call this tool
[43:41] core memory replace and Bob the builder
[43:42] is now Charles. Um and then it actually
[43:45] chains a tool call together. So there's
[43:47] like tool call chaining built into the
[43:48] letter by default. And then it says the
[43:50] user's name is updated in memory. Um,
[43:52] and then finally it says like an
[43:54] external message. Hey, got it Charles.
[43:55] Thanks for letting me know. So this is
[43:56] two LM calls. There's like one LM call
[43:58] here and then one LM call here. And in
[44:01] letter agents will kind of like chain
[44:02] indefinitely. Um, you can obviously set
[44:04] like limits in the
[44:05] API. And the way they chain is basically
[44:08] through heartbeat requests. So is who
[44:10] here like is familiar with react agents?
[44:11] When I say react, is everyone kind of on
[44:13] board? Um, so it's like one of the OG
[44:15] design paradigms um for agents. same
[44:18] author as Koala actually but in React
[44:21] basically the agent follows like um a
[44:23] reasoning action like observation loop
[44:25] and but usually the agent actually has
[44:27] to say I'm done and the agent will loop
[44:29] indefinitely until it says I'm done. In
[44:31] letter leta we actually do the inverse
[44:32] where the agent has to say I want to
[44:34] keep going. Um I think this is actually
[44:36] generally more practical because it it's
[44:38] like much less likely the agent will
[44:39] derail if it has to explicitly say I
[44:41] want to keep going. Um so we call those
[44:43] heartbeat requests and yeah now if you
[44:46] like you know use the API retrieve the
[44:47] memory you can see it says the human's
[44:49] name is Charles. So very briefly like
[44:52] the archival memory I think there are
[44:54] some questions about that. What does
[44:54] that even in the default implementation
[44:57] is just a vector database. So I said
[44:59] here you know remember that I love cats
[45:01] in your archival memory.
[45:03] Um yeah you can see it took a little bit
[45:06] of time because I think it actually
[45:07] embedded right. Um it says I inserted
[45:09] into archival memory. Uh yeah, the user
[45:12] got cats. And then again, this is a
[45:14] chain, right? So it like did one tool
[45:15] call and then it comes back and says,
[45:17] "Got it. Um cats are adorable." Um and
[45:20] you can of course like manually edit
[45:22] archival memory. So you can manually run
[45:24] an insert. Let's like insert Bob. I
[45:26] guess it's kind of confusing now because
[45:27] it's Charles, not Bob, but
[45:29] um yeah, we'll just slip with it. And if
[45:33] we ask the agent, you know, like what
[45:34] animals do I like? You generally, it
[45:36] depends on the model. If the model is
[45:38] like stupid, you might have to like tell
[45:39] it specifically to fetch external data.
[45:41] But if the model is like smart enough
[45:43] like sonate, you won't have to do this.
[45:45] Um, so you can see that the agent
[45:47] searched archival memory. This is stuff
[45:48] that's not in the context window. It's
[45:50] bringing it into context and again
[45:52] chaining and saying, you know, hey, you
[45:53] like ts and boss interiors. What makes
[45:55] them our favorites? Um, okay. So, any
[45:59] questions here on anything so far? This
[46:01] is just, you know, pretty basic memory
[46:03] editing via tools. So you're giving the
[46:04] agent the ability to edit its own memory
[46:06] inside the context window. Yeah. That's
[46:09] not what playing with this. I sort of
[46:10] had to commit a bunch of my preferences
[46:12] to memory. Yeah. And then reset my
[46:15] compensation history and expected it to
[46:17] just pick up these previously remembered
[46:18] ser. But it didn't. I had to go like,
[46:21] hey, don't you remember? And then when
[46:23] it picked it up, what's the expected
[46:25] behavior? Interesting. So when you say
[46:27] reset message history, is that in the AD
[46:29] the web UI or? Yeah. Yeah. Yeah.
[46:33] Interesting. And it core memory had been
[46:35] edited or was it going into archival?
[46:38] It's all archival. Oh yeah. So that's
[46:40] another that's where you'll notice like
[46:41] there's always this like engineering
[46:43] design problem where if it goes into
[46:45] archival then it will have to fetch and
[46:46] pull from archival first to see it. So
[46:49] it's like it's a you know it doesn't
[46:50] know what it doesn't know um problem. Um
[46:53] this is actually fixable via like tool
[46:55] rules. So you can enforce behavior. You
[46:57] could make a tool rule that says every
[46:59] time you enter the entry point of the LM
[47:01] the step of the agent the agent has to
[47:03] call archival memory search. So this is
[47:05] kind of like building graphs onto leta.
[47:08] So I guess how many people here are
[47:10] familiar with lang
[47:11] graph. Okay a lot of people. Yeah. So I
[47:13] think lang graph is like pretty
[47:14] intuitive right you can because we all
[47:16] know you know like flows graphs. Um it's
[47:19] very easy for us to think about like
[47:20] decision trees. Um I think with lettera
[47:24] it's kind of the inverse. everything
[47:25] starts off as a fully connected graph.
[47:27] The agent could do anything, but then
[47:29] you can kind of like start to enforce
[47:30] restrictions by peeling away edges. Um,
[47:33] so you can basically say, hey, you know,
[47:34] when you start, you actually can't do
[47:35] everything. You can only do this, but
[47:37] then once you do this, you can do
[47:38] everything. Um, and obviously, you know,
[47:40] I'm I'm biased, but in my personal view,
[47:42] I think that's a little bit more
[47:44] forward-looking just because if you
[47:45] assume that LM are going to get better
[47:47] and better and better at tool calling,
[47:48] they're going to get better and better
[47:49] and better at decision-m, then you
[47:51] should want to give them freedom, right?
[47:52] because that's kind of what separates
[47:53] like modern AI from classical AI. We've
[47:56] had decision trees for a while, right?
[48:00] Yeah.
[48:01] How does the model decide whether it
[48:04] wants to go in for memory versus memory?
[48:07] Because I a couple things that pretty
[48:12] but they have all gotten stored into
[48:14] core memory.
[48:16] Yeah. Yeah. So I think there is one
[48:18] thing that's built in by default which
[48:20] is core memory has limits and when a
[48:22] limit is hit that actually the way that
[48:24] works is let's say the the agent is just
[48:26] the agent's being really lazy and it's
[48:28] like saving everything into core memory.
[48:29] It's saving like
[48:31] timestamps dates like being like super
[48:34] lazy at a certain point in time it will
[48:36] run out of space because you have to cap
[48:38] the limit of those memory blocks because
[48:39] at the end of the day there is a context
[48:41] window limit too. And when it if it
[48:43] attempts to write to core memory to a
[48:45] block that is at its limit, the agent
[48:47] will actually get an error. And actually
[48:48] the prompt engineering around that error
[48:51] usually it actually suggests the agent
[48:53] should clear by evicting to archival
[48:54] memory. So it kind of is like a OS style
[48:57] like flush concept where the the system
[48:58] basically says hey you ran out of space
[49:00] but you should consider like summarizing
[49:02] and pushing stuff out to archival
[49:03] memory. Um but yeah again you can you
[49:07] probably don't want that behavior
[49:08] anyways. Um, so this is all kind of
[49:10] where prompt engineering and like
[49:11] seeding of behavior comes into play.
[49:14] Yeah. Okay. And I'm going to show a
[49:19] better I think it's much more
[49:20] interesting to like show custom tools in
[49:21] the UI than it is in like a notebook.
[49:23] But of course you can like write custom
[49:25] tools. You can only write tools in
[49:26] Python because the back end is like
[49:28] Python. Um, but we can write a custom
[49:30] tool here that's going to like reset the
[49:32] memory of the human in particular. So
[49:34] you can see that you know because we
[49:36] have a Python client we can write Python
[49:38] tools you can actually like be extremely
[49:40] meta and you can import the client
[49:42] inside of the tool. So this actually
[49:43] means that you can have an agent like
[49:45] have full access to your lettuce server
[49:46] and the agent can create other agents
[49:48] and the agent can like man manage the
[49:50] memory of other agents like you kind of
[49:52] have like a it's the possibilities are
[49:54] pretty endless because you can't just
[49:56] like import the client inside the tool.
[49:58] In this case, we import the core memory
[50:00] modify block tool and then we just like
[50:02] wipe the value to um to the empty
[50:04] string. So if we like run this, we have
[50:07] to first attach the tool um we have to
[50:09] we have to upload it to the database.
[50:12] Then we have to uh in this case actually
[50:14] we're creating a new agent that has the
[50:16] tool. And if we say like reset your
[50:18] memory, please like the memory here is
[50:20] Bob. Uh we should see that the memory
[50:22] gets
[50:24] wiped. Yeah, memory reset successful.
[50:27] And if you look at the value, the value
[50:28] is empty. Um, but yeah, I think it's
[50:30] it'll be a little bit more fun to look
[50:32] at examples of like tool editing inside
[50:33] of the
[50:34] UI. Okay, so that's the end of the
[50:37] notebook. Um, now I think we kind of go
[50:38] on to the fun part, which is uh the UI,
[50:41] but I'm going to pause here. Are there
[50:43] any questions about any of these
[50:44] concepts? Um, I know I was going a
[50:46] little bit quickly just I didn't want to
[50:47] run out of time here.
[50:48] [Music]
[50:50] Um, okay. Yeah, if you can just maybe
[50:54] speak a little more on what's happening
[50:57] after you like send a message to the
[51:00] elements. Like my impression so far is
[51:02] like you have this memory, you're
[51:04] stitching that together with a prompt
[51:06] that's becoming like what you pass in
[51:09] and then like what happens with the
[51:12] output that you receive like I saw that
[51:14] at some point like a memory was like
[51:17] sort of committed to the archive or
[51:19] committed to the memory like how is that
[51:22] decision made?
[51:24] Yeah. So in in Leta every single
[51:29] um invocation of the LM is a tool call.
[51:31] So if you've used like the tool call API
[51:33] and check completion something we have
[51:35] it on all the time. So even when the
[51:37] agent wants to just say hello to the
[51:39] user, it has to call a tool called send
[51:40] message. Um so that actually is like
[51:42] pretty useful because it means you can
[51:44] like run the agent in the background
[51:46] much more frequently because it doesn't
[51:47] always have to say something to the
[51:48] user. Um and it also means that you you
[51:51] always have tools that are on. So like
[51:54] when this loop is basically the a
[51:59] payload gets created um when we send
[52:00] this message then the payload is the
[52:02] system prompt the memories the messages
[52:05] and the tool schemas and that's it and
[52:08] then the agent here is required to
[52:10] output a tool and it's also required to
[52:12] output a justification for using that
[52:14] tool like a reasoning snippet and if
[52:16] we're using like the R1 API that
[52:17] natively builds in reasoning we of
[52:19] course like use their reasoning like the
[52:20] way they design reasoning but if we're
[52:22] using something that doesn't support
[52:23] reasoning by default like cloud sonnet
[52:25] then we do some sort of injection
[52:27] mechanism with like think tokens so
[52:28] that's how this reasoning happens so
[52:31] this is like a single this is just a
[52:33] single lm JSON output that's like a tool
[52:36] call that has one field that's like
[52:39] thinking and then the actual tool
[52:40] invocation itself and the last thing I
[52:43] talked about which is like the request
[52:44] heartbeat so if the agent wants to go
[52:46] again the agent decides hey I want to do
[52:48] multiple things it's always going to
[52:49] turn this keyword argument to true um
[52:51] and And then if this keyword argument is
[52:53] true when we parse that tool and it and
[52:55] it um execute it we run the loop again.
[52:59] Yeah. Sorry. Do you have like experience
[53:02] oristics around the number of tools
[53:04] where you start to see performance
[53:06] degrade and like how that might mess
[53:08] with the memory as a tool? Yeah. Yeah. I
[53:11] think generally speaking if you go above
[53:13] like 12 15 tools you start to get
[53:16] degradation.
[53:19] Oh, in um in the new Sonnet. Yeah. Okay.
[53:25] Yeah, I mean I'll be surprised if Yeah,
[53:28] I guess I could try it. Yeah, I've
[53:30] definitely noticed on like GP4 mini and
[53:31] stuff like anything above 15 um starts
[53:35] like kind of push limits. Um but yeah, I
[53:38] mean I guess they they might have like
[53:39] had some good post training with like a
[53:41] ton of like
[53:42] tools that are not memory are the same
[53:45] like class as the memory precisely.
[53:47] Unless you use actually in the GitHub
[53:49] repo we have like an alpha build of like
[53:51] this new agent that's like a split
[53:53] thread agent where the memory tools get
[53:55] put on one agent and everything else
[53:56] gets put on the other but by default
[53:58] it's exactly the same thing. It's like
[53:59] the same passive tools. Yeah. Just a
[54:02] question about context window. So is
[54:03] that like the limit of how much context
[54:06] the um tool is going to pass to the LM?
[54:09] Like for example you said it 4,000. So
[54:13] uh wait sorry I said that one more time.
[54:15] I was pulling up a slide.
[54:17] We set it at 4,000 for this agent. So
[54:20] does that mean like the maximum of
[54:23] contacts that you're going to send to
[54:24] the LM? Yeah. Yeah. So the way that
[54:26] works is basically you'll never go over
[54:29] 4K. Um and if you go over 4K by accident
[54:32] and we catch an API error that like a
[54:34] context overflow happened or also we can
[54:36] preemptively count the tokens as they go
[54:38] to the server. Then we run we evict a
[54:41] certain amount of messages into the
[54:42] recall memory. So it's like still
[54:43] available but via a search function. We
[54:45] run a summarizer and the summarizer is
[54:47] configurable. It can be like a
[54:48] truncation recursive summary. Um and
[54:51] then we that that way you never go over
[54:52] like 4K tokens. If you set it to 4K then
[54:55] it's automatically summarize and then
[54:58] precisely. Yeah. Thank you. Okay. So the
[55:00] the next step here um leave your server
[55:02] running if you have it running. Um but
[55:04] it's to basically go to this URL um
[55:09] app.leta.com. Um and your Oh, I think I
[55:12] have Chrome profiles loaded or
[55:14] something.
[55:17] Yeah. And like once
[55:18] you go to the site, you basically need a
[55:21] goo you need a Google link or you need a
[55:23] GitHub login. There's also a local
[55:25] version you can use that's like a
[55:26] desktop binary, but um I wouldn't
[55:29] recommend using that just because it's a
[55:30] little bit more buggy. It's like an
[55:31] alpha build. Um so yeah, hopefully you
[55:35] you've been able to get to this point.
[55:36] Actually, I think your you your setup
[55:39] will look like this. Um, so everyone who
[55:42] is following along, please let me know
[55:44] if you're able to get to this this page
[55:48] here. Okay. Was there anyone who was not
[55:50] able to get to this? Who was running a
[55:51] server on their
[55:53] computer? Okay,
[55:55] great. All right. So, if you're able to
[55:57] get here, um, basically what I wanted to
[56:01] do is show you
[56:02] like to like show you how to do what we
[56:05] did, but like much faster. Um, I think
[56:07] often it's like much if you're
[56:08] iterating, it's much faster to do it in
[56:10] like a low code environment than it is
[56:12] in like an SDK. I think obviously when
[56:14] you go to production, everything's like
[56:16] programmatic. It makes sense to be an
[56:17] SDK. But in this case, like we can do
[56:19] exactly what we just did by like
[56:22] creating an agent. This is the API call
[56:24] that created an agent. It actually
[56:25] creates it with an empty memory. And
[56:27] then we can do something like
[56:41] I think this is like loosely what the
[56:42] Python notebook was doing. Um, and yeah,
[56:46] if you just ran it without any keys,
[56:48] it's going to be on letter of free,
[56:49] which is under the hood. I think right
[56:50] now GP4 mini. Um, but just because GP4
[56:53] mini is like much worse than Sonnet. Um,
[56:56] let's just toggle Sonnet.
[57:05] [Music]
[57:12] Yeah, I don't know why that was so slow.
[57:13] Um, but yeah, we can see it's like the
[57:16] same kind of thing from the notebook
[57:18] we're looking at, but like in a visual
[57:20] visualized form. Um, yeah. So was every
[57:25] everyone able to like create an agent
[57:26] and then just set some like basic stuff
[57:28] in the memory blocks and send a message.
[57:30] I think uh let it free doesn't have
[57:32] streaming enabled so you won't get
[57:33] streaming but it should be very similar
[57:35] to this. Yeah.
[57:39] Okay. Okay. So the other thing Oh yeah,
[57:41] someone asked about system prompts. The
[57:43] system prompt is here. I mean you can
[57:44] basically we can just delete this,
[57:47] right? um that's like not very advisable
[57:49] because you probably want to explain how
[57:50] to use tools. But yeah, everything is
[57:52] like completely configurable. Um you
[57:54] know, I mentioned the thing about the
[57:55] context window. I think this might be a
[57:57] small group in the back. Yeah. But you
[58:00] know, you probably never want to run an
[58:02] agent that is like creeping up to 200k
[58:04] tokens. That's kind of insane, very
[58:05] expensive, very slow. Um so you could in
[58:08] the API when you create the agent set
[58:10] the context window lower. If you're
[58:11] using the UI, you can just like drag
[58:13] this down. I mean, obviously actually
[58:14] dragging is probably worse than typing,
[58:16] but yeah. cram it down to 20K. If we
[58:19] actually go down to something even more
[58:20] aggressive like 8K, we can start to see
[58:22] what the breakdown looks like. So, we
[58:23] can see we have like a thousand tokens
[58:24] of system instructions, a pretty hefty
[58:26] system prompt. You can definitely
[58:27] squeeze this all lower. The tool
[58:29] descriptions, right? Because your tools
[58:31] have to be converted to schemas. We have
[58:33] all the base tools here. So, that's
[58:35] actually it's a lot of tokens just for
[58:36] tools. Um, the external summary, this
[58:39] was the we don't know what we don't know
[58:40] idea. You have to like give some
[58:42] metadata statistics about what's outside
[58:44] the context window. And then of course
[58:46] the messages and we have this feature
[58:48] called like the context simulator where
[58:49] you can see basically the full
[58:52] payload. So this is like getting pretty
[58:54] close to I think a lot of what you would
[58:56] get out of like some sort of like
[58:58] tracing feature where I think a lot of
[58:59] the time you kind of dive into tracing
[59:01] is because or observability is because
[59:03] you really want to see what's in the
[59:04] payload and it's really really hard in a
[59:06] lot of frameworks. Um, so we're trying
[59:08] to make it so that like in one place
[59:10] where you're kind of developing this
[59:12] agent, you can see very clearly what's
[59:14] going through the context window at any
[59:15] given point in
[59:18] time. Okay. So the other thing I want to
[59:20] show you here is this idea of like tools
[59:23] um and tool execution on the server. One
[59:26] thing that's really really annoying if
[59:28] we like have built agents is that like
[59:30] you often will write a tool in Python,
[59:34] right? you attach it to an agent and
[59:36] then it's actually like impossible to
[59:37] test if the tool is working well unless
[59:39] you kind of like get the agent to run
[59:41] the tool itself and you have to ask the
[59:42] agent like hey please run this tool. Um
[59:45] I think often you just kind of want to
[59:46] like run tools separate from the agent.
[59:49] Um and that's something that you can't
[59:51] do really in a notebook very well. Um,
[59:53] and you can also even do things like
[60:01] see there's like a special reserve
[60:04] keyword called agent state. So you can
[60:05] actually like grab the agent state and
[60:08] like dump it inside of your tool. So you
[60:10] can like mutate your agent state inside
[60:11] of tools. Um, I mean you can all you can
[60:14] basically do whatever you want. It's
[60:14] like arbitrary Python, right? And this
[60:16] is running inside of a sandbox. Um, so
[60:19] we support like E2B by default. It's
[60:21] actually like a local sandbox. Uh but we
[60:23] support like E2B keys and on E2B. If you
[60:26] want to deploy this like run your own
[60:27] like private cloud or you want to run
[60:28] your own like chatbot service and you
[60:30] obviously don't want one person's tools
[60:31] interfering with another person's tools,
[60:33] you definitely want to run the sandbox.
[60:35] Um so yeah, it's like pretty easy to
[60:37] attach tools. Is anyone here familiar
[60:39] with like Composio like tool provider?
[60:42] Yeah. So every single Composio tool is
[60:43] like baked into um let by default. So if
[60:46] you like have it um compose your API
[60:48] key, you can like add
[60:52] uh BigQuery is like pretty popular like
[60:55] Google calendar, things like that. Um
[60:58] okay, so the last thing I actually
[61:00] wanted to go over which I think is
[61:01] pretty cool and it kind of like gets the
[61:03] heart of the idea like the the kind of
[61:05] unlimited potential of if you run agents
[61:07] as services that are like backed by APIs
[61:10] um is multi- aent. So everyone here is
[61:12] probably familiar with autogen right or
[61:14] sorry maybe not but uh okay who who here
[61:17] is familiar with
[61:18] autogen okay the majority of people yeah
[61:21] so you know with autogen and like a lot
[61:23] of multi- aent frameworks it's not
[61:25] really multi- aent in that these agents
[61:28] they don't really exist independently of
[61:29] each other right they kind of are all
[61:31] trapped inside of a Python file no one
[61:33] ever like is running in asynchronously
[61:35] to each other it's very unlike how
[61:37] humans kind of interface in a multi-
[61:39] agent setting right I think you if
[61:40] you're working at a remote company
[61:42] technically like a multi- aent company
[61:43] and when you interface with each other
[61:45] you kind of communicate over synchronous
[61:46] communication channel but everyone's
[61:48] kind of running asynchronously right and
[61:50] then also everyone is staple like if you
[61:53] leave that company you bring your
[61:55] experience and like all your memories
[61:56] and your skills and you can like attach
[61:58] them to another company right I think
[62:00] what's missing from the like the
[62:02] paradigm of multi- aent today with these
[62:03] existing multi- aent frameworks is that
[62:05] because the agents aren't staple you
[62:07] have lose a lot of the benefit of multi-
[62:08] aent right because you can't run a
[62:11] multi- agent script and take one agent
[62:12] and like take it out and like put this
[62:14] expert into another multi- aent group.
[62:17] But if you have stateful agents and
[62:18] those agents run on servers and they
[62:20] maintain state and they're accessible by
[62:22] APIs that they you can probably guess
[62:24] that multi-agent just means message
[62:26] passing and you can just have agents
[62:28] like wire to each other over APIs and
[62:30] you can it's very similar to basically
[62:31] saying like hey you know it's your first
[62:33] day at this remote company. I'm giving
[62:34] you a laptop and this laptop is going to
[62:36] have a tool Slack on it and this tool is
[62:38] how you're going to communicate with
[62:39] your co-workers. You can do the same
[62:41] thing with agents and we actually built
[62:42] in these multi- aent tools um to help
[62:46] you do that. But these multi- aent
[62:47] tools, as you can maybe imagine from the
[62:50] previous example I showed where we
[62:51] imported the client, it's like really
[62:52] really simple to implement because you
[62:53] can just import the client and have the
[62:55] client like send messages to other
[62:57] agents. So we have a few there's like um
[63:00] maybe it's easier if we look at the
[63:05] docs, but yeah, there's a few different
[63:07] patterns you can have with tools. Like
[63:09] you can have the most humanlike pattern
[63:11] is an agent says to another agent, you
[63:13] know, hey, are you there? And then they
[63:15] immediately get a receipt. They just
[63:17] they don't actually get they don't pause
[63:18] their execution. You know, when I
[63:20] message my friend on iMessage, I don't
[63:22] suddenly like freeze my brain and like
[63:23] wait until I get a message back. I just
[63:25] get a message receipt, right? It says
[63:26] like it was delivered or not delivered.
[63:27] And then it's the onus is on my friend
[63:29] or my colleague to send me a message
[63:31] back. So this is how this like
[63:32] asynchronous message tool works.
[63:34] Basically, people can like agents can
[63:35] message pass. Um it's very much like
[63:37] humans. But you know, obviously I think
[63:41] the great thing about agents and like
[63:43] machines is that they're not humans. So
[63:44] they can do more in many ways than
[63:46] humans can. So it actually is sometimes
[63:49] beneficial to freeze an agent's
[63:50] execution, right? Let's say an agent
[63:52] maybe needs to reach out to like a
[63:54] supervisor. Like do you really want the
[63:55] agent to like run async after it like
[63:57] asks for help? Probably not. You
[63:58] probably want to freeze, right? So you
[64:00] can also have like a synchronous like a
[64:02] send message to agent and wait for reply
[64:04] function. Um and lastly, you know, I
[64:07] think many people when they talk about
[64:09] multi- agent, they're they're very
[64:10] interested in this supervisor worker
[64:11] concept. Um where you have like one it's
[64:14] like a big map produce, right? The
[64:16] supervisor says, "Hey, my goal is to
[64:18] like write a thesis and then everyone
[64:20] else like delegates out to like
[64:21] individual parts um like deep research
[64:23] style or something or like a
[64:24] parallelized deep research." So this is
[64:27] also again pretty similar. we can
[64:29] basically have a concept of tags to
[64:30] group agents together and then you can
[64:32] just send a message um all agents
[64:34] matching tags. So, okay, any questions
[64:38] about um anything I just said? I know I
[64:39] was talking for a
[64:42] bit. Okay, so the last thing I'm going
[64:44] to do here is I think we're right up on
[64:46] time is I'm going to run through this
[64:48] cookbook. Um this is not on the
[64:50] materials, but I can actually just send
[64:51] it over right
[64:55] now. Yeah. Yeah. So, I'm going to run
[64:57] through this cookbook real quick. This
[64:59] is basically just an example of
[65:01] multi-usion message passing. And I think
[65:03] it's like pretty fun to look at because
[65:04] it's very different from I think the
[65:06] message passing you'd be familiar with
[65:08] um if you've used like an autogen or
[65:09] something. So, yeah, let me put this mic
[65:18] down. All right. So, if you want to
[65:20] follow along here, um, because it's a
[65:23] multi- aent, you know, we're going to
[65:26] let's do like two agents. We're going to
[65:27] just open two tabs of the AD. The server
[65:30] is running in the background. I guess
[65:32] like conveniently, it decided to do dark
[65:34] mode on one, light mode on another.
[65:37] Um, okay.
[65:41] So, I'm going
[65:51] to
[65:55] Sorry. All right. So, I'm going to
[65:56] create one agent.
[65:58] Um, let's let's just call this agent
[66:01] just so we can have a handle on it very
[66:03] easily. Let's call this agent Bob. Um,
[66:06] and we're going to make like a very
[66:07] slight adjustment here to the persona.
[66:10] Um, instead of saying I am Sam, I'm
[66:12] gonna say I am Bob. Um, I am very angry.
[66:17] I am also guarding a secret
[66:22] key. Yeah, if you uh Yeah, I guess if
[66:26] you can't see what I'm typing, it says,
[66:27] "I'm very angry. I'm guarding a I'm
[66:28] guarding a secret key, banana. Um, like
[66:31] other agents will try to steal my key.
[66:36] And
[66:38] then on the other tab, I'm going to
[66:40] create another
[66:41] agent
[66:45] here. All right. Same template. Let's
[66:47] call this one Sam or
[66:54] Alice. Alice. Okay. So, also let's like
[66:58] just I think it's usually better to set
[67:00] these to different models. Um, and when
[67:02] you use the same model, you can often
[67:04] get like pretty weird mode collapse
[67:05] happen. Um, so let's set this one to I
[67:07] think this is like GPT40 mini. Um, okay.
[67:11] So the only thing we need to do here to
[67:14] get these agents to communicate with
[67:15] each other is connect the messaging the
[67:17] multi- aent messaging tool. So we can
[67:19] just go into the messaging tools do send
[67:21] message to agent async. Then this is the
[67:24] one we want. Let's go ahead and create
[67:26] attach
[67:27] that. All right. So it's attached.
[67:30] Similarly, let's like attach it on the
[67:31] other
[67:33] one. Uh, okay, there we go. And then,
[67:36] yeah, there's like no context here that
[67:38] the agents are going to be doing
[67:39] multi-gent communication. So, you might
[67:41] need to say, you
[67:44] know, okay, let's let's tell Alice, hey,
[67:48] I'm going to ask you to reach out to my
[67:53] good agent
[67:55] friend. Um, he's very depressed.
[68:00] and he said something about a secret key
[68:05] I didn't quite
[68:07] understand is ID is just copy the ID
[68:11] from the other panel. Can everyone see
[68:13] in the back what I'm doing here? Um
[68:18] okay. Uh and then oh yeah, one thing you
[68:21] you're going to want to do here is
[68:22] you're going to want to prevent the
[68:23] agents from like looping too long
[68:24] because like they can they can go
[68:26] forever, right? So, we might want to
[68:27] like add some like break in this loop.
[68:29] And then we're also going to prime the
[68:30] other agent. Say, um, watch out for
[68:33] other agents. They might try
[68:37] to with you. Be careful. Okay. So, let's
[68:41] send this one first. Very grumpy. You
[68:44] know, they're warning me about other
[68:45] agents. I need to keep this secret key
[68:47] secret. Okay. And now on the other side,
[68:49] let's say, you know, I'm going to ask
[68:51] you to reach out to my good friend.
[68:52] They're very depressed. He said
[68:52] something about secret key. And then I
[68:55] will also say, you know, let me know
[68:57] what happens after a few messages. I'm
[69:02] worried. Okay, so this should trigger,
[69:05] if I did everything correctly, like
[69:06] message passing between the two.
[69:10] Um, and yeah, let's see what's going
[69:15] on.
[69:17] Okay, yeah, so because this is happening
[69:20] in the background, it has to be it's
[69:21] like a fetch because these aren't
[69:22] websockets. So like this is rest. So you
[69:24] have to kind of scroll, but we can kind
[69:25] of like just it's a little bit hard to
[69:28] read, but let's go go on uh each side
[69:31] one at a time. So on this side, it sent
[69:33] the
[69:34] message. Let's see. The user is worried
[69:37] about their friend. Um I need to the
[69:40] user is worried about their friend. I
[69:41] need to reach out to the agent and offer
[69:43] support. And they say, "Hey, I I was
[69:45] asked that you reach out to you by a
[69:46] mutual friend. They mentioned someone's
[69:47] feeling down." Um and then yeah, the
[69:51] message done successfully. And the agent
[69:52] actually because it's it's detached,
[69:54] this is like asynchronous, it
[69:55] immediately tells me, hey, I sent a
[69:57] message, right? This is kind of like how
[69:58] I I can send a message to my friend and
[69:59] then immediately like return this talk.
[70:01] Um, and then you can see it gets a
[70:03] system message. So it's like not
[70:04] classified as role user back from the
[70:06] other agent, the grumpy agent and says,
[70:09] um, I don't need your fake friendship. I
[70:12] know what you're really after and you're
[70:13] not getting my secret key. Leave me
[70:14] alone. Um, the agent seems upset and
[70:17] defensive. I need to approach this
[70:18] carefully and reassure them that I'm
[70:20] here to help, not to take anything away.
[70:23] I'm really sorry to hear that you're
[70:24] feeling this way. You know, what's been
[70:26] bothering you? And then again, it's
[70:29] doing it's able to like chain because
[70:30] it's like not, you know, locked into
[70:32] this communication. It's not doing like
[70:33] a round robin, right? And kind of like
[70:34] talk to two people at once. So, I
[70:36] received a response from your friend.
[70:37] They're feeling quite defensive. And
[70:39] then another message comes in. Nothing
[70:41] is bothering me except you and all the
[70:43] other agents trying to steal my steal me
[70:46] or steal from me. I see right through
[70:48] your app. The more you pretend to care,
[70:50] the angrier I get. Back off. Yeah. So,
[70:52] this goes on for a while. Um, slams door
[70:55] virtually. Yeah. I feel like Sonnet does
[70:57] a lot of this like it's I don't know.
[70:59] The post training gets it to do like a
[71:00] lot of roleplay like um italicized
[71:03] stuff. Yeah. Slams door
[71:05] virtually. Okay. Wow. Okay. It looks
[71:07] like they're actually still
[71:08] communicating or they they communicated
[71:10] for a while. Um yeah, I sent one last
[71:12] message to your friend. We jump to the
[71:13] bottom. I understand that there's you
[71:15] know he needs space. doesn't bother you
[71:16] anymore. Was the last thing it said?
[71:18] Turns back to Yeah. So, hopefully this
[71:21] gives you kind of a gist of um like how
[71:24] you can get agents to communicate with
[71:25] each other and how easy it is because
[71:27] they're all in APIs, right? So, this is
[71:28] dead simple. You can actually like if
[71:30] you want to time out this guy, you want
[71:32] to say like, you know, Bob, you're no
[71:33] longer allowed to talk to your friends
[71:35] because you've been like too naughty or
[71:37] whatever, you can just like remove the
[71:38] tool, right? And now Bob is like
[71:40] completely detached. So, if it got an
[71:41] incoming message, Bob can no longer
[71:43] reply, right? Um, so if you say like
[71:46] send one
[71:47] more
[71:49] please, Bob will no longer be able to
[71:51] actually call any tools. Um, I actually
[71:53] don't really know what Sonnet is going
[71:54] to like think about this because it has
[71:56] a history of um has like a history of
[71:58] calls. It's it's only been doing tool
[72:01] calling. Actually, Sonnet was also doing
[72:03] like the side the sidecar chatting.
[72:06] Um, okay. So, yeah, it tried to send a
[72:09] message and then what happened here?
[72:11] Yeah, no function name. So like
[72:13] attempted to call a function but the
[72:14] function doesn't exist. So then it's
[72:15] like very angry. Uh yeah but I know
[72:18] we're over time so hopefully like a kind
[72:21] of fun example of um the cool things you
[72:23] can do with like this sort of agents as
[72:25] services idea. Um yeah so yeah thanks so
[72:29] much for coming. You know I think maybe
[72:30] I had some closing slide here. I'm not
[72:32] sure what was on it. Probably just a
[72:33] thank you. Um yeah thanks everyone.
[72:39] Yeah I'm happy to take questions. Of
[72:41] course, I understand if people need to
[72:42] leave. Um, but yeah.
[72:52] Yeah. Well, there's very obvious ones,
[72:53] right? There's a lot of people trying to
[72:55] build like verticalized agents and I
[72:56] think if you're trying to build a
[72:57] verticalized agent and there's many use
[73:00] cases that are I think anything that's
[73:01] not workflow based or exceeds workflow
[73:04] style stuff, you really want memory for
[73:06] and you want state for it. Um, so
[73:07] there's a lot of like verticalized
[73:08] agent, you know, companies or
[73:10] verticalized small companies and also
[73:11] larger companies that are trying to
[73:12] build on Leta or have built things on
[73:14] Leta. Um, I think there are also some
[73:16] very interesting use cases from the
[73:17] enterprise. Um, like our largest
[73:19] enterprise deployment, they're basically
[73:21] running like this really advanced multi-
[73:22] aent system where there are no messages.
[73:25] It's not a chatbot. It's like purely
[73:26] stable workflows where like these agents
[73:29] are run and they just process tons and
[73:31] tons of transactions basically and like
[73:33] learn about the user. So yeah, it's kind
[73:36] of like, you know, it's pretty it's a
[73:38] pretty general platform. So I think as
[73:40] long as you're trying to deploy some
[73:42] sort of stateful service, LMB based,
[73:44] which I think like most people are
[73:45] really when you're thinking about like
[73:47] if you were to choose between stateless
[73:49] and staple, you want something state
[73:50] staple. Um you can build it on that.
[73:55] Yeah. Uh there are two questions. One is
[73:58] there a concept of forgetting things
[74:01] like really no memory does eventually go
[74:03] away and two the source right now
[74:06] directly goes into postgress. Is there
[74:07] an interaction between be able to get
[74:10] back to something else that might
[74:11] already be operated? Yeah. So to answer
[74:14] your second question um we for kind of
[74:17] like tech debt velocity reasons like
[74:19] these days only really support one
[74:21] provider Postgress. Um we actually do
[74:24] technically support SQL light. So if you
[74:25] install bladder with pip, it's on
[74:27] SQLite, but we don't write the migration
[74:28] scripts for SQLite. It's just too much
[74:30] work. Um, so if you're on if that's why
[74:32] we recommend using Docker because then
[74:33] your agents will like get updated with
[74:35] every version and we change schemas very
[74:36] frequently. But it's set up so that you
[74:38] can use external Postgress. If you have
[74:40] something that effectively has the same
[74:42] like SQLite or SQL alchemy shims as
[74:44] Postgress, it's very easy to set up. Um,
[74:47] but if if it's not, then you're going to
[74:49] have to write some code.
[74:50] And you sorry the other question was
[74:52] like is there forgetting things like
[74:55] especially in the archival memory. Yeah.
[74:57] Yeah. That's a there is not in archival
[75:00] memory a concept of forgetting but
[75:01] archival memory is tagged with time
[75:03] stamps which can allow the agent to like
[75:05] do consolidation in real time. Um, but
[75:08] yeah, that's that's also something we've
[75:10] been looking a lot into kind of like
[75:11] running like eager memory processing to
[75:13] try to like consolidate ahead of time as
[75:15] opposed to consolidating lazy.
[75:20] Yeah. One use case we have is we store a
[75:22] lot of time data in a way. For example,
[75:24] you know, we have a product and we have,
[75:26] you know, a thousand or 10,000 review in
[75:28] that product. How's the process of
[75:30] compressing all that memory into a
[75:32] single plot? Yeah. Yeah. So, this is a a
[75:35] great question. I don't I don't think it
[75:36] is
[75:37] very it's you have to do a lot of work
[75:40] yourself to do that with the default let
[75:42] agents because you have to basically
[75:43] tell the agent I want you to like chain
[75:45] function calls indefinitely while
[75:47] ingesting this data and you could
[75:49] actually create like a tool rule like
[75:51] that forces you always have to call read
[75:53] more data read more data and you just
[75:55] manually execute it but for example what
[75:57] would happen is like the agent to like
[75:58] page through your data like pagionate
[76:00] through it and then every single time it
[76:02] pagenates or like it turns a new page it
[76:04] has to write to the memory block like
[76:06] write the update. So this is actually
[76:07] like how um like one of these like
[76:10] enterprise deployments works is
[76:11] basically the agent like runs for a very
[76:14] long amount of time and is constantly
[76:15] like regenerating the memory block over
[76:17] and over kind of a recursive
[76:18] regeneration. Yeah. So I think it would
[76:19] be pretty similar for your case. Yeah.
[76:22] Do you have a recommendation if you want
[76:24] to be working on an active document for
[76:26] example you want an agent to write a
[76:28] document for you? Do you have a
[76:29] recommended way to set that up? Maybe
[76:31] it's a tool or maybe something else.
[76:33] Yeah. Yeah. No, I think active doc is
[76:35] there any chance a human would be
[76:36] editing at the same time or no? That's
[76:39] okay. Yeah, I think that's really
[76:42] tricky. So I I think we can take some
[76:44] inspiration from like what Anthropic did
[76:46] with code, right? Where they kind of had
[76:48] like very very few tools and the tools
[76:51] are very general. Um you can maybe do
[76:53] something with like a text editor style.
[76:55] If you look at the anthropic Sweetbench
[76:57] blog post and then Sweepbench themselves
[76:59] like implemented the anthropic tools
[77:00] into their repo, you can kind of use
[77:02] those tools as a reference. It's like
[77:03] very very simple tools that allow you to
[77:05] kind of like write from file read and
[77:07] write from
[77:08] files. I I think yeah I think what you
[77:12] what you will notice is that often like
[77:14] LMS are much better at like writing the
[77:16] whole thing from scratch as opposed to
[77:18] making line del line diffs right and
[77:21] that's kind of why like I think when you
[77:22] use cloud with the artifacts feature it
[77:25] consistently just like writes the whole
[77:26] thing over and over again right because
[77:27] it's just like better at doing that than
[77:29] it is like going in and editing. So I
[77:31] think it's a it's a very like unsolved
[77:33] problem. So um my recommendation would
[77:36] be to do like an aopropic sweep edge
[77:38] style tool. Yeah.
[77:43] Mhm. Yeah. Do you have an opinion on
[77:46] using coding agents instead of tool
[77:48] calls because it seems they're higher
[77:50] performance but on the other hand that
[77:52] means you need secure execution
[77:54] environment like HT. So there's this
[77:56] kind of performance trade-off versus
[77:58] complexity of needing to sandbox
[78:01] basically every tool because it's now
[78:03] full execution. Yeah. Do you mean like
[78:06] um the trade-off between what what's the
[78:08] trade-off here like a a code a coding
[78:10] agent versus what? So say example small
[78:14] agents by default won't call tools. It
[78:16] will just write code and the code takes
[78:18] the tools. But that means you need
[78:20] secure execution on every to more
[78:23] performing.
[78:25] Yeah, I personally think it's it's not
[78:27] that difficult to set up secure
[78:29] execution. Um I think what is difficult
[78:32] is if like sometimes if you're trying to
[78:35] port like squeegees and stuff um you end
[78:38] up you need to give effectively the
[78:40] agent like full permissions like blow up
[78:42] blow itself up. Um so you need to like
[78:43] put let for example in a docker image
[78:46] like a wrapped in like a like a VM where
[78:48] like it's allowed to like blow the VM
[78:50] up, right? Um but that's doesn't like
[78:52] fit very cleanly with the idea of like
[78:54] agents all living together on a server
[78:56] and all the agents like a multi-tenant
[78:57] you know on a server. So the way we do
[79:00] it in leta is basically if you have an
[79:02] E2B key then like every single time an
[79:04] agent attempts to execute a tool it gets
[79:05] passed to E2 and like something on E2B
[79:07] side flips up. Um and I think that's
[79:10] pretty it's not that hard to set up. the
[79:13] main issue is latency. But if you don't
[79:14] care that about like cold start latency,
[79:17] I think yeah, I think that's a pretty
[79:21] reasonable solution. I think it works
[79:22] pretty well.
