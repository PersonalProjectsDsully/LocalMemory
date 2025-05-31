---
type: youtube
title: Self Coding Agents — Colin Flaherty, Augment Code
author: AI Engineer
video_id: Iw_3cRf3lnM
video_url: https://www.youtube.com/watch?v=Iw_3cRf3lnM
thumbnail_url: https://img.youtube.com/vi/Iw_3cRf3lnM/mqdefault.jpg
date_added: 2025-05-26
category: AI Development
tags: ['AI coding agent', 'context engine', 'code execution', 'UI/UX design', 'AI tools', 'software development', 'continuous learning', 'tool integration', 'enterprise AI', 'human-AI collaboration']
entities: ['Augment Google API', 'context engine', 'file editing tool', 'clarify tool', 'memory tool', 'completion models', 'Foundation model', 'codebase retrieval', 'Google credentials', 'UI/UX design']
concepts: ['AI coding agents', 'context-aware AI systems', 'code execution environments', 'human-AI collaboration', 'continuous learning mechanisms', 'tool integration', 'enterprise AI solutions', 'UI/UX design for AI', 'context engine architecture', 'AI agent development']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with software development workflows', 'Knowledge of codebase management systems']
related_topics: ['AI agent development', 'context engines in AI', 'code execution security', 'human-AI interaction design', 'enterprise AI tools', 'toolchain integration', 'continuous learning systems', 'AI system architecture']
authority_signals: ["We've been working on AI coding tools for a couple years now", 'Our focus the whole time was around building a super powerful scalable Enterprise ready context engine', 'It turns out this context engine... provided a great foundation for us to quickly build this agent']
confidence_score: 0.85
---

# Self Coding Agents — Colin Flaherty, Augment Code

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=Iw_3cRf3lnM)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai coding agent, self-improving code, software engineering tools, ai development, machine learning models, autonomous coding, ai dev tools  

## Summary

# Summary of "Self Coding Agents — Colin Flaherty, Augment Code"

## Overview  
Colin Flaherty, an AI researcher at Augment Code, discusses the development of an AI coding agent capable of autonomously writing and improving its own code. The agent leverages a robust context engine, third-party integrations, and tools to interact with codebases, users, and external systems. Key insights include the importance of context, reasoning capabilities, and safe code execution environments, alongside lessons learned from building scalable, enterprise-ready AI tools.

---

## Key Points  
- **Self-Improving Codebase**: The agent writes 90% of its code with human supervision, using tools like Google search, code retrieval, and file editing to adapt and optimize.  
- **Third-Party Integrations**: The agent interacts with systems like Slack, Jira, and codebases, demonstrating capabilities to handle complex tasks such as credential management and log instrumentation.  
- **Autonomous Optimization**: The agent profiles its own performance (e.g., adding logs, running subcopies) to identify and resolve issues, such as missing credentials.  
- **Context Engine**: A critical foundation for success, combining code, user feedback, and external data to enable effective reasoning and task execution.  
- **UI/UX Focus**: Seamless human-AI interaction requires intuitive design, ensuring tools like clarification prompts and memory storage enhance collaboration.  

---

## Important Quotes/Insights  
- *"The agent used Google search to find API docs, then added logs to itself, ran a subcopy, and learned from user feedback."*  
- *"We didn’t set out to build agents—we focused on a context engine, which became the foundation for rapid agent development."*  
- *"20,000 lines of code with 90% written by the agent, showcasing its ability to self-improve."*  

---

## Actionable Recommendations  
1. **Build a Strong Context Engine**: Prioritize integrating diverse data sources (code, user input, external systems) to enable effective AI reasoning.  
2. **Focus on UI/UX**: Design tools for seamless human-AI collaboration, including clarification prompts and memory storage.  
3. **Secure Code Execution**: Implement safe environments for running commands in user-facing systems.  
4. **Leverage Tools**: Use retrieval, editing, and logging tools to enhance the agent’s adaptability and problem-solving capabilities.  

--- 

## Lessons Learned  
- **Context is King**: No matter how advanced LLMs become, contextual understanding remains non-negotiable.  
- **Iterative Design**: Building agents requires refining tools, feedback loops, and execution environments over time.  
- **Human-AI Synergy**: The agent’s value lies in augmenting human capabilities, not replacing them.

## Full Transcript

[00:00] [Music]
[00:16] hi everyone thanks for coming today so I
[00:19] want to talk to you about something that
[00:20] sounds like science fiction but very
[00:23] much is reality an AI coding agent that
[00:25] helped build itself my name is Colin I'm
[00:28] an AI researcher at augment code a
[00:31] company building AI power Dev tools for
[00:33] software engineering orgs and I want to
[00:35] share with you a little bit about my our
[00:37] journey working on AI coding
[00:40] agents so zooming out AI Dev tools is a
[00:44] fast changing space everyone remembers
[00:47] in 2023 we're all talking about
[00:49] autocomplete models GitHub co-pilot
[00:51] being the one that probably really comes
[00:53] to mind in 2024 chat models really
[00:56] started to penetrate software
[00:58] engineering Orcs
[01:00] in 2025 though we think AI agents are
[01:02] going to dominate the conversation about
[01:05] how software engineering is
[01:08] changing so naturally a few months ago
[01:11] we started building our own agent at
[01:12] augment I want to show you a sneak peek
[01:15] of what we built and share some
[01:17] hard-learned lessons about how this Tech
[01:19] works and I just want to you know
[01:21] reiterate I've been really amazed to see
[01:23] the extent to which this agent has
[01:24] helped build itself uh I'll not a kind
[01:27] of fun statistic so we have about 20,000
[01:29] thousand lines of codee in our uh agent
[01:33] code base and over 90% of that was
[01:35] written by our agent with with human
[01:38] supervision so what does it mean for the
[01:40] agent to write itself implementing core
[01:43] features so one of the first things we
[01:45] had we had to add was third-party
[01:46] integration so our agent you know if
[01:48] it's going to work like a software
[01:49] engineer it needs to interact with slack
[01:52] linear jira notion search Google um muck
[01:57] around in your code base and so we
[01:59] wanted to have the agent help us build
[02:00] these
[02:01] features uh we had it we found after we
[02:04] added the first few ourselves when we
[02:06] add asked it to you know gave it an
[02:08] instruction like add a Google search
[02:09] integration it was able to go look in
[02:11] our code base for the right file to add
[02:13] it in uh figure out the right interface
[02:16] to use and go add it uh one kind of fun
[02:19] an anecdote is when we were adding the
[02:21] linear integration uh it didn't know the
[02:24] linear API docs the foundation model
[02:26] we're using uh didn't have those
[02:28] memorized and so it used the Google
[02:30] search integration which it had written
[02:32] previously to go look up the linear API
[02:34] docs and then was able to add
[02:37] that uh we used it to write tests so we
[02:40] found if we asked it something like add
[02:43] unit tests for the Google search
[02:45] integration it was able to go add those
[02:48] uh in order to do this we just had to
[02:49] give it some basic Process Management
[02:51] tools things like running a subprocess
[02:54] interacting with it uh not hanging if
[02:57] there's an infinite Loop in some test it
[02:59] wrote and and reading
[03:01] output um I think this is super
[03:04] interesting so everyone's seen the
[03:05] Twitter demos of these agents writing
[03:08] features and writing tests but I haven't
[03:10] yet seen a compelling example of them
[03:12] performing some kind of
[03:14] optimization well over the course of our
[03:16] project we KN noticed the agent was
[03:18] pretty slow and we weren't sure why so
[03:20] we asked it to profile itself and what
[03:22] it ended up doing using all these tools
[03:24] we'd given it was add some print
[03:26] statements to its own code base run
[03:28] essentially sub copies of itself looked
[03:30] through these print statements and it
[03:32] figured out there was a part of our code
[03:33] base where we were loading up all the
[03:36] files in the users's
[03:37] repository uh synchronously and hashing
[03:40] them synchronously and then it added a
[03:41] process pool for these to speed it up
[03:44] and a stress test to confirm it was all
[03:46] working and by the end of this we
[03:48] reached about 20,000 lines of code and
[03:50] again over 90% of that was written by
[03:53] the agent with with our help in
[03:56] supervision so let's walk through a
[03:58] quick example
[04:00] a couple quick examples to see how the
[04:02] agent works I focus on simple examples
[04:04] where it's reliable so you can uh follow
[04:07] along
[04:08] easily so here I asked the agent are you
[04:11] able to search Google and then it notes
[04:13] that it found a tool called Google
[04:15] search for those who aren't familiar
[04:17] with the notion of tools I'm sure most
[04:19] of you are but I'll just kind of quickly
[04:20] reiterate the idea is we have this kind
[04:22] of Master Level agent that's doing all
[04:24] the planning and it has access to
[04:26] certain tools that it can use to
[04:27] interact with it its environment with
[04:29] that's the third party Integrations I
[04:31] talked about like Google or it's editing
[04:33] a file in the user's repository and then
[04:36] it wants to confirm this that this
[04:37] Google Search tool is working so it
[04:39] sends a query to it of tests and the
[04:41] agent uh uh responds to us yes I can
[04:44] search Google and I see the first 10
[04:47] results let's try something a little bit
[04:49] more complicated I ask it instrument
[04:51] agent's Google Search tool with logs and
[04:53] then generate an example then it uses
[04:55] our retrieval tool which is you know
[04:57] allows to search uh the local codebase
[05:00] and it's looking for a file related to
[05:02] Google search Integrations it finds this
[05:05] file deep in our directory hierarchy at
[05:07] Services integration thirdparty gooogle
[05:10] search to.py and then it calls its file
[05:13] editing tool to quickly and performant
[05:16] edit that file to add those print
[05:19] statements uh this is a continuation of
[05:22] the last example so it added those print
[05:24] statements and now it wants to run a a
[05:26] sub copy of itself so it can look at the
[05:29] output of those print statements uh
[05:31] because we asked it for example logs uh
[05:33] but in doing so it finds that we don't
[05:35] have Google uh credentials authorized so
[05:37] it uses its clarify tool to ask for
[05:40] clarification from the user it asks I
[05:42] don't see Google credentials would you
[05:44] like me to one add stub for Google API
[05:47] or to guide you through setting up
[05:49] credentials I note that the credentials
[05:51] are actually stored in augment gooogle
[05:54] api. Json it had just missed this and
[05:57] then here's a a really cool extra
[05:59] feature we have which is we want the
[06:01] agent to continuously learn as it
[06:03] interacts with humans and so here it
[06:06] thought well it's probably a good idea
[06:08] to remember where the Google credentials
[06:09] are stored so it called this memory tool
[06:12] to create a memory of the where where
[06:14] the Google credentials are stored to
[06:15] save that for later this is another
[06:17] example if you have that really good
[06:19] context engine uh it's really critical
[06:21] to getting the agent to to work
[06:24] well and so now we get our output so it
[06:26] prints out these logs that it searched
[06:28] with an example string p programming
[06:30] language and it gives some uh uh example
[06:33] URLs that were returned by Google
[06:34] python.org and Wikipedia.org so we have
[06:37] the agent add logs to itself run itself
[06:40] learn from user feedback and it used all
[06:42] kinds of tools Google search codebase
[06:44] retrieval file editing clarification
[06:46] from the user and and memorizing uh
[06:49] useful
[06:50] learnings so let's fast forward and talk
[06:52] through some of our lessons building
[06:55] this uh I just want to know you know
[06:57] we've been working on AI coding tools
[06:59] for a couple years now and we didn't set
[07:01] out to build agents we've worked on
[07:03] things like completion models and Chad
[07:05] and so forth but our Focus the whole
[07:07] time was around building a super
[07:10] powerful scalable Enterprise ready
[07:12] context engine because we knew no matter
[07:14] what no matter how good these llms get
[07:16] you're going to need that context and we
[07:18] also thought a lot about how do you
[07:20] build great uiux so AI can seamlessly um
[07:23] interoperate with humans it turns out
[07:26] this context ENT and all these thoughts
[07:28] around design provided a great
[07:30] foundation for us to quickly build this
[07:31] agent in just a couple months the three
[07:33] most important things were that access
[07:35] to context that context Engine with all
[07:37] those different types of context sources
[07:39] whether it's slack or the codebase the
[07:41] reasoning capabilities from a
[07:42] best-in-class uh Foundation model and
[07:45] that code execution environment so you
[07:46] can safely run uh commands in a uh
[07:50] customer's uh
[07:53] environment so let's talk through a
[07:55] couple assumptions that we frequently
[07:57] fall into we we have frequently fallen
[07:59] into and remedied and and some of you
[08:01] might encounter as
[08:03] well uh so the first one is that you
[08:05] know L5 agents are here the senior soft
[08:08] agents are at senior software
[08:09] engineering level if you look at the
[08:11] Twitter demos it oftentimes can seem
[08:13] like this you have an agent write an
[08:15] entire website all on its
[08:17] own in reality professional software
[08:20] engineering is rarely zero to one and
[08:23] the environments that we're coding in
[08:24] are are a lot messier than what those
[08:26] demos uh show you as a result these you
[08:29] know aren't quite there yet but they're
[08:31] still super
[08:34] useful um the way one framework I've
[08:37] seen people think through when they're
[08:39] trying to figure out you know how to use
[08:40] these agents and how to build them is
[08:42] they think agents will take over entire
[08:44] categories of tasks so first you build
[08:46] an agent that will uh solve backend
[08:49] programming and then you build an agent
[08:50] focused on front- end and maybe one
[08:52] focused on testing in reality this
[08:55] technology is very general purpose and
[08:58] so instead of thinking about categories
[08:59] of tasks we found it more helpful to
[09:02] Think Through levels of complexity so
[09:04] our agents you know kind of good
[09:06] decently good at tasks across front end
[09:09] backend security and so forth and we're
[09:12] we're improving the capability level
[09:14] along all those fronts at once because
[09:16] again it's a very general purpose
[09:19] technology um we've also seen people
[09:21] anthropomorphize agents so they think
[09:23] they're just like human software
[09:25] engineers and they map the
[09:26] characteristics of a weak software
[09:28] engineer to what they think a weak agent
[09:30] would look like and vice versa for
[09:32] strengths as well in reality agents have
[09:35] different strengths and weaknesses than
[09:37] humans and so you may have an agent that
[09:39] can't do math but it can Implement a
[09:41] whole front- end feature way faster than
[09:43] any human could and it's important that
[09:45] we keep this in
[09:47] mind uh let's talk through a couple
[09:49] Reflections and
[09:52] lessons uh so here I ask aaman can you
[09:54] create a stack of two PRS for the new
[09:56] reasoning module using graphite
[09:59] unfortunately so graphite is a Version
[10:01] Control tool for working with Git you
[10:03] can like stack PRS it makes it a lot
[10:05] easier to review unfortunately
[10:07] Foundation models have not memorized how
[10:09] graphite works so our general agent
[10:11] responds I don't know what graphite is
[10:13] so I'll use git and then it calls our
[10:15] terminal tool to run a command running
[10:17] get checkout well what do we do here we
[10:19] wanted it to use graphite we can't
[10:20] necessarily go tell open AI or anthropic
[10:23] to retrain the model understand graphite
[10:26] overnight so what we came up with this
[10:28] notion of a knowledge base which is
[10:30] essentially a set of a s a set of
[10:33] information that we want the agent to
[10:35] understand that it currently doesn't we
[10:37] can kind of patch holes um one thing we
[10:39] wanted to add to it was this graphite
[10:41] knowledge so we created this markdown
[10:43] file describing graphite how to you know
[10:45] run common commands things like how to
[10:47] create a PR use GT create some things
[10:50] not to do um we created other files in
[10:52] our knowledge base for things like
[10:54] details on our tool stack how to run
[10:56] tests the style guide and then we add
[10:59] this into the context for the agent so
[11:01] it can dynamically go searching this um
[11:03] knowledge base when it doesn't
[11:05] understand something and uh once we
[11:07] added this then you know we go ask it
[11:10] can you create a stack of two PRS for
[11:11] the new reasoning module using graphite
[11:14] and it calls that Knowledge Graph reads
[11:16] about graphi and then can run the GT
[11:18] create command so what's the learning
[11:21] here well onboarding the agent to your
[11:22] organization is crucial the analogy I
[11:25] like to think about is if you just hired
[11:27] a new a new hire software engineer you
[11:29] wouldn't go tell them to just stare at
[11:31] the code base for 3 Days to figure out
[11:33] how your Tech stack Works you'd let them
[11:35] ask you questions maybe there's some
[11:36] things they didn't understand and you
[11:38] add some additional documents to your
[11:40] notion uh we should think similarly
[11:42] about
[11:44] agents uh recall I was talking about how
[11:47] we had all these uh thirdparty
[11:48] Integrations we added whether it's
[11:50] linear tools or slack tools and so forth
[11:52] when we when we were working on these we
[11:54] weren't really sure of which ones to
[11:56] prioritize and start with on our product
[11:58] road map and in a normal World we'd make
[12:00] some educated guesses we'd Implement a
[12:02] couple of them and go from there but
[12:04] with the agents we were able to iterate
[12:06] them um uh build them all at once and so
[12:08] this starts to change the calculus
[12:10] around how product management works uh
[12:13] if you can build everything at once well
[12:15] then maybe um maybe uh engineering hours
[12:19] aren't the bottleneck on what we build
[12:21] and it starts to uh we start to be
[12:23] bottleneck a little bit more on good
[12:24] product insights and good
[12:27] design so when code is cheap you you can
[12:29] explore more
[12:31] ideas uh also recall earlier we were
[12:34] talking through this example of you
[12:35] instrumenting the agent Google Search
[12:37] tool with logs uh and it was able to go
[12:39] find the file to edit notice here how we
[12:41] didn't have to give a very precise
[12:43] instruction to the model we just told it
[12:45] in natural language like how we talk to
[12:47] another engineer to instrument the
[12:49] agent's Google Search tool and I was
[12:51] able to go figure out the file to edit
[12:53] this only worked because we have that
[12:55] really good uh codebase
[12:57] awareness um we can also use the agent
[13:00] for tasks outside of writing code but
[13:02] still within the software development
[13:03] life cycle so here we asked it to look
[13:05] at the latest PRS uh in our codebase and
[13:08] generated an announcement on them and
[13:11] then we posted it to slack and so uh it
[13:13] was titled new tools for this uh CLI
[13:15] agent and we talked about some things
[13:17] around slack notifications and linear uh
[13:20] linear Integrations this only works
[13:22] because we had that slack integration
[13:24] and and understood our code base well
[13:27] this uh figure may look familiar from
[13:29] the beginning of the talk um we actually
[13:31] had the agent make this as well so we
[13:33] asked it make me a plot of the
[13:35] interactive agents line of code as a
[13:37] function of the
[13:39] date um and so good context is critical
[13:42] in all three of these tasks we needed to
[13:45] pull in some different context from some
[13:46] different sources and it's not just the
[13:48] codebase context comes in many forms and
[13:51] also note that it's multiplicative so
[13:53] having access to the codebase and having
[13:55] access to slack is Forex is useful as
[13:58] just having access to one of
[14:00] those finally I want to uh switch over
[14:03] and talk about uh
[14:06] testing so uh here's a really a hard to
[14:10] test Edge case in our code the agent
[14:12] actually wrote this um and we only
[14:14] caught it because of some unexpected
[14:15] runtime Behavior so we have these caches
[14:18] that the agents store relevant
[14:20] information for their runs in uh we can
[14:22] run multiple agents in parallel and they
[14:25] all write to the same cache location and
[14:28] the agent wrote this save function to
[14:30] save to that location and I had this
[14:33] lock around the Json dump so there were
[14:35] no race conditions that would explicitly
[14:38] fail if you had multiple agents all
[14:40] right to this cach at the same time but
[14:43] notice here how there's no read before
[14:45] writing to the cache and as a result you
[14:48] could hit a race condition where if
[14:49] multiple agents are running in parallel
[14:51] they're all overriding each other's
[14:53] caches and when the agent wrote this
[14:55] save function why did it Miss this issue
[14:57] well these agents make mistakes and this
[15:00] is a hardto test situation there's some
[15:03] parallel programming there's a cache
[15:05] involved and so we didn't have a test
[15:08] and because we didn't have a test the
[15:09] agent messed up my learning here is we
[15:11] need to be very careful about having
[15:14] sufficient
[15:16] tests um we have this pretty incredible
[15:19] statistic so we have a internal bug fix
[15:22] bug fixing Benchmark uh we found when we
[15:25] upgraded our foundation model by about 6
[15:27] months our score in this Benchmark
[15:30] improved by 4% but when we added the uh
[15:34] ability to run tests so the agent could
[15:36] suggest a fix for the bugs run tests
[15:39] look at the feedback suggest another fix
[15:41] run test and do that four times that led
[15:43] to a 20% gain on this
[15:46] Benchmark so what's the lesson well
[15:49] better tests enable more autonomy you
[15:51] can trust these agents more and it just
[15:54] makes them
[15:57] smarter what is software engineering
[15:59] look like in a world of Agents well
[16:01] agents didn't work last year but now
[16:04] we're pretty good if you'd ask me two
[16:06] years ago if we'd be working on this
[16:07] Tech I frankly wouldn't have guessed it
[16:11] there's a compounding effect where these
[16:12] agents are staring starting to help
[16:14] build themselves and that's only going
[16:16] to accelerate the pace at which they
[16:18] improve code isn't going away because
[16:20] it's a spec of our systems but our
[16:22] relationships to it is changing good
[16:25] test harnesses are becoming more
[16:27] important than ever and we need to be
[16:29] especially careful about those parts of
[16:31] our code bases that tend to be less well
[16:34] tested and the calculus of product
[16:37] development is changing if code becomes
[16:39] super cheap to write then the focus our
[16:42] focus is more on good product work
[16:45] Gathering customer feedback quickly
[16:47] building
[16:48] insights we're really excited for how
[16:50] this Tech's going to positively
[16:52] transform our industry and we'll be
[16:54] releasing our agents soon so I'm really
[16:56] excited to share that with you uh find
[16:58] me after the talk if you want to discuss
[16:59] anymore thanks
[17:01] [Applause]
[17:04] [Music]
