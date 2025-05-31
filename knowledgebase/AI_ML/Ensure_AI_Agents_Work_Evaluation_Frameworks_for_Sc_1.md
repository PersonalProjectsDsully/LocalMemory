---
type: youtube
title: Ensure AI Agents Work: Evaluation Frameworks for Scaling Success — Aparna Dhinkaran, CEO Arize
author: Channel Video
video_id: OC04sP_QgTI
video_url: https://www.youtube.com/watch?v=OC04sP_QgTI
thumbnail_url: https://img.youtube.com/vi/OC04sP_QgTI/mqdefault.jpg
date_added: 2025-05-26
category: AI Development & System Monitoring
tags: ['AI agents', 'system monitoring', 'open source', 'trace analysis', 'multi-turn conversations', 'tool calls', 'state management', 'code-based agents']
entities: ['An Open Source Project', 'Trace', 'Router', 'Skills', 'Memory', 'Arize', 'SQL Query', 'Data Analyzer Skill']
concepts: ['AI Agents', 'Multi-turn Conversations', 'Tool Calls', 'State Management', 'Trace Analysis', 'Code-based Agents', 'Open Source Projects', 'System Monitoring']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI agents', 'Familiarity with programming (e.g., Python)', 'Knowledge of system monitoring concepts']
related_topics: ['AI system development', 'Conversation management', 'API integration', 'Machine learning operations', 'Open-source tool analysis']
authority_signals: ["this is really what your engineers are looking at when they're actually building and troubleshooting your agent", 'shows all three of the different components that I actually just walked through']
confidence_score: 0.85
---

# Ensure AI Agents Work: Evaluation Frameworks for Scaling Success — Aparna Dhinkaran, CEO Arize

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=OC04sP_QgTI)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai-agents, evaluation-frameworks, production-deployment, voice-ai, multimodal-agents, ai-monitoring, machine-learning-ops  

## Summary

```markdown
# Summary of "Ensure AI Agents Work: Evaluation Frameworks for Scaling Success"

## Overview
Aparna Dhinkaran, CEO of Arize, discusses the importance of evaluation frameworks for AI agents in production, emphasizing the shift from text-based to multimodal agents (e.g., voice, multi-turn interactions). She highlights the need for technical rigor in debugging and optimizing agent performance, including the role of traces in troubleshooting.

---

## Key Points

### **Components of AI Agents**
1. **Router**: Acts as the "boss" of the agent, determining which skill to call based on user input.  
   - Example: A router might misdirect a query (e.g., sending a "leggings" request to customer service instead of product search).  
2. **Skills**: Execute specific tasks (e.g., API calls, LLM prompts, SQL queries).  
   - Example: A "data analyzer" skill processes application traces to identify performance issues.  
3. **Memory**: Maintains context across multi-turn interactions to avoid "forgetting" prior user inputs.  

### **Evaluation Frameworks**
- **Router Evaluation**: Ensure the agent calls the correct skill (e.g., product search vs. discounts).  
- **Skill Evaluation**: Assess the accuracy and efficiency of individual tasks (e.g., SQL queries, data analysis).  
- **Memory Evaluation**: Verify that the agent retains and uses context effectively.  

### **Challenges**
- **Multimodal Agents**: Require tailored evaluation strategies (e.g., voice vs. text interactions).  
- **Complexity**: As agents grow, multiple router calls and skill interactions increase the risk of errors.  

### **Example: Open-Source Traces**
- Traces (debugging tools) reveal the internal flow of an agent, showing how a user query (e.g., "trace latency") is processed through routers, skills, and memory.  

---

## Key Insights
- **Modality Matters**: Evaluation must account for the agent's input/output modality (e.g., voice, text, multi-turn).  
- **Leadership Involvement**: Technical understanding of traces and evaluation metrics is critical for decision-making.  
- **Arize's Role**: The company's tools help teams debug and optimize agent performance, with a focus on scalability.  

---

## Actionable Takeaways
1. **Develop Frameworks**: Create evaluation metrics for routers, skills, and memory.  
2. **Leverage Traces**: Use open-source traces to debug and optimize agent workflows.  
3. **Adapt for Modality**: Design evaluation strategies specific to the agent's interaction type (e.g., voice, text).  
4. **Invest in Training**: Ensure leadership understands technical aspects of agent evaluation.  
```

## Full Transcript

[00:00] [Music]
[00:17] well thank you so much for being here
[00:18] I'm going to start off by saying
[00:20] apologize my voice a little bit it's a
[00:21] little horar today but you guys are
[00:23] going to hang in there with me today
[00:25] we're going to talk about a really
[00:27] important topic which is um
[00:30] slideshow mode awesome we're going to
[00:33] talk about a really important topic
[00:35] which is about evaluating AI agents and
[00:38] assistance this will load just to set a
[00:40] little context before we we jump
[00:43] in a lot of you have probably heard
[00:45] today about different agents that are
[00:47] being built how to build it what are the
[00:49] Cool Tools out there to go build agents
[00:51] and today we're going to actually talk
[00:53] about when you put those agents into
[00:55] production it's important to actually
[00:57] know how they're doing and evaluate them
[01:00] it's super important in making sure that
[01:01] they actually work in the real world
[01:03] we're probably going to get a little
[01:04] technical in this talk maybe a little
[01:06] bit more than some of the other talks
[01:08] but hang in there I think this is
[01:10] important even at the leadership level
[01:12] to understand how to make sure what
[01:13] you're putting out actually works in the
[01:15] real world um so a little bit about me
[01:18] my name is aparta I'm one of the
[01:19] founders of arise uh fun update on us
[01:23] actually today we announced our series C
[01:25] race um
[01:28] so um
[01:31] have a lot of folks for are using us to
[01:34] evaluate agents so with that let's jump
[01:36] in okay well everyone here's probably
[01:38] talked to you about text based agents so
[01:41] you have this chat bot whatever it's
[01:43] making an action and it's it's figuring
[01:46] out all these things to do the cool next
[01:48] Frontier is actually voice AI is already
[01:52] taking over call centers there are over
[01:55] 1 billion calls made in call centers all
[01:58] around the world with Voice Assistant a
[02:01] with with voice apis and the the
[02:03] realtime voice API if any of you guys
[02:04] have played around with it we're
[02:05] actually already seeing these types of
[02:08] um agents start to take over and
[02:10] revolutionize call centers this is
[02:13] actually a real production application
[02:15] of a travel agent this is the price line
[02:17] pennybot you can go in and actually
[02:20] handsfree no text book an entire
[02:23] vacation using Price Line Penny today so
[02:26] we're not just talking about tech based
[02:28] agents anymore we're talking about
[02:29] multimodal agents and it's important to
[02:33] address these because the way that you
[02:34] evaluate these types of Agents it's not
[02:36] just evaluate an agent but also if it's
[02:39] on voice there's specific types of
[02:41] evaluations you're going to need to do
[02:43] if it's multimodal there's additional
[02:45] types of evaluations you need to
[02:46] consider so we're going to break all
[02:48] that down and hang in there with me for
[02:50] a fun one today so before I jump in and
[02:53] talk about how to evaluate an agent
[02:55] let's talk about what are the components
[02:56] of an agent you probably have heard
[02:58] different versions of this today but but
[02:59] I'll tell you the language we're going
[03:00] to use one um there's something
[03:03] typically called a
[03:04] router uh which is essentially what's
[03:07] deciding what the next step an agent
[03:09] will take there's skills which is the
[03:12] actual logical chains that do the work
[03:14] and then there's something that stores
[03:16] the memory this is important
[03:20] because there might be different
[03:21] architectures of how you're seeing
[03:23] people build these agents out there
[03:25] doesn't matter if you're using Lan graph
[03:27] or crei or llama index workflow there's
[03:30] all sorts of agent Frameworks they all
[03:31] have slightly different ways of building
[03:34] an agent you might not even use a
[03:36] framework but what you're going to see
[03:38] is these common patterns of okay that's
[03:40] a router that's a skill and that's a
[03:42] memory and these different components
[03:44] are going to have different ways of how
[03:45] you actually evaluate it so let's first
[03:48] talk about the first one what the heck's
[03:50] a router so you can think about a router
[03:52] almost like the boss it's kind of
[03:54] deciding hey well it's very common to
[03:57] have e-commerce agents in you probably
[04:00] are all talking to e-commerce agents
[04:01] today to purchase things Amazon has one
[04:04] all these e-commerce companies have one
[04:06] when you type in a question like I want
[04:08] to make a return give me an idea of what
[04:10] to go buy are there any discounts on
[04:12] this that user query funnels into
[04:14] something called a router and that
[04:16] router's goal is to is really to
[04:19] determine do I call this skill about
[04:22] hitting up a customer service agent do I
[04:24] call this skill um to suggest all the
[04:28] discounts we have or suggest product
[04:29] products the router is really kind of
[04:31] the boss deciding who do I tap on to go
[04:34] actually execute the the ask that the
[04:37] user made and the router might not
[04:40] always get it right but you want it to
[04:42] get it right because then it goes down
[04:44] the pathway of a specific skill within
[04:47] an agent so in this case it will call a
[04:49] skill um so if I asked hey uh tell me
[04:54] the best um I don't know leggings to go
[04:58] byy so it'll go in it'll do a product
[05:00] search and then this is actually the
[05:02] entire skill flow of execution that the
[05:05] agent needs to go through to execute you
[05:07] know whatever the user asked for some of
[05:09] these might be llm calls some of these
[05:11] might just be API calls it just really
[05:13] depends on how people actually Implement
[05:16] them and then lastly this is an
[05:18] important piece is there's always
[05:19] something storing the memory because
[05:22] these are usually not just single turn
[05:24] conversations they're multi- turn
[05:26] conversations multi-turn interactions
[05:29] and so you don't want to be talking to
[05:31] an agent that forgets what you
[05:32] previously said so there's really memory
[05:35] which is storing what it previously
[05:36] asked for and keeping all this in some
[05:38] sort of um in in some some sort of
[05:41] semblance of state so with that we're
[05:44] going to get a little fun here I'm going
[05:45] to show you um an actual example of what
[05:49] this could all look like a router skills
[05:51] and memory so this is an open source
[05:54] project um that actually looks at the
[05:58] inner workings of an agent these are
[05:59] called traces for folks who may not be
[06:01] familiar if you're you know in
[06:04] leadership or this is really what your
[06:07] engineers are looking at when they're
[06:09] actually building and troubleshooting
[06:10] your agent they're actually
[06:12] understanding what the heck went on
[06:14] under the scenes so this is actually an
[06:16] example of a code-based agent somebody
[06:20] asked a question like what trends do you
[06:22] see in my Trace latency AKA what's
[06:25] making my application slow this is the
[06:28] router call that we were talking about
[06:30] earlier where it actually decides well
[06:33] how do I then go ask how do I then go
[06:35] tackle that question so first you can
[06:38] see here there's multiple router calls
[06:41] there's not just one router call this is
[06:43] pretty common as your application grows
[06:46] you can have multiple times where it
[06:47] comes back and has to decide what do I
[06:49] need to go do so the first time it calls
[06:51] the router what it does is it actually
[06:55] so the router then makes a tool call um
[06:58] which is essentially this skill that you
[07:00] need the first time it actually makes a
[07:03] tool call to then go run a SQL query go
[07:06] collect all of my traces of my
[07:08] application and go go run a SQL query
[07:11] then it goes back up to the router and
[07:14] then it calls the second skill which is
[07:16] actually the data analyzer skill which
[07:20] takes all of the traces and the
[07:22] application data and then it passes it
[07:24] to something that actually analyzes that
[07:26] data so in this case you can actually
[07:27] see there was a router there was tool
[07:30] calls we actually have memory that's
[07:32] actually storing everything that's
[07:33] happening under the scenes and so really
[07:36] just shows all three of the different
[07:38] components that I actually just walked
[07:40] through so now that we have an example
[07:43] of a of an agent with the router and
[07:47] skills and memory let's talk about how
[07:49] to actually evaluate these agents every
[07:52] single step that I just walk through
[07:53] here actually is an area where the agent
[07:56] can go wrong for routers typically what
[07:58] teams end up caring about is did it call
[08:02] the right skill because if it didn't
[08:04] call the right skill you know user asks
[08:07] for I asked for leggings but then it
[08:08] sent me over to customer service or it
[08:11] sent me over to um you know uh something
[08:14] about discounts and Deals so you
[08:17] actually want to make sure that the
[08:18] router within an agent is correctly
[08:21] doing the right skill and calling the
[08:24] right skill so that's the first piece
[08:28] that you'll want to make sure that your
[08:29] teams are evaluating so if your teams
[08:31] are building agents you want to ask well
[08:33] hey what's the ultimate control flow
[08:36] what's the control flow and are do we
[08:39] have something like a router and are we
[08:41] evaluating it to make sure that it's
[08:43] correctly calling the right skill
[08:44] between ABC and is it calling the right
[08:47] skill with the right parameters so not
[08:50] just um a calling product search but
[08:54] actually making sure that whatever way
[08:56] you've designed that skill you're
[08:58] actually passing in the correct things
[09:00] like um you know I want this type of
[09:02] material I want this type of whatever
[09:04] cost range you're actually passing in
[09:06] all the right parameters into what the
[09:09] user actually is is asking for can I get
[09:11] a raise of hands have any of you guys
[09:13] heard of do any of you guys evaluate
[09:16] your agents today actually is that
[09:19] something you know your teams are doing
[09:21] okay awesome are any of you guys
[09:23] evaluating this router level internally
[09:26] okay awesome wow this is a great group
[09:29] okay
[09:30] this is impressive um okay let's next go
[09:34] to the next one which is actually
[09:35] evaluating a skill this is actually the
[09:38] part where it gets really interesting
[09:39] and tricky because there's many
[09:41] different components in a skill there
[09:43] might be in this case I have a rag type
[09:46] of skill so I want to look at things
[09:47] like evaluating the actual relevance of
[09:51] the chunks that were pulled I want to
[09:52] look at the actual correctness of the
[09:55] answer that was generated but this skill
[09:57] itself can have many different
[10:00] llm as a judge evals or it can also have
[10:03] code-based evals that you might want to
[10:04] run to actually evaluate the
[10:06] skills the skills of the agent and then
[10:10] lastly this is kind of a really
[10:11] important one that we're seeing teams
[10:14] probably have the most trouble
[10:15] evaluating which is actually the path
[10:18] that the agent took
[10:20] because well ideally you want it to
[10:23] converge you call the same skill
[10:27] hundreds of times and it always takes
[10:30] about five steps or six steps to
[10:32] actually query what the user asked for
[10:35] put in the right parameters call XYZ
[10:37] components of the skill and then
[10:39] ultimately um take the right you know
[10:42] generate the right answer but sometimes
[10:44] this can be a little longer we've seen
[10:47] sometimes where the same skill and I
[10:49] don't know if you all have done this
[10:50] experiment but you can put the same
[10:52] skill and build it with open the eye and
[10:54] you can also build it with anthropic and
[10:56] sometimes they have wildly different
[10:58] number of steps that the path actually
[11:01] takes and so the goal here is how do you
[11:04] be succinct and how do you also make
[11:05] sure there's reliability in the number
[11:07] of steps that your agent takes to
[11:10] actually consistently complete a task so
[11:12] we call this convergence um but probably
[11:16] one of the hardest to actually evaluate
[11:17] is anyone evaluating convergence today
[11:20] or at least counting the number of steps
[11:22] awesome okay you're awesome
[11:25] dude cool well with that I'm going to go
[11:29] me maybe two more minutes then I'll hop
[11:30] into one more demo here so if any of you
[11:33] guys have watched the movie her this is
[11:34] from
[11:35] her um uh this is
[11:38] where you know the the main character
[11:42] asks like who else are you talking to
[11:44] and you know the Samantha says something
[11:47] like 8,000 other people are in a
[11:48] conversation with me right now and so
[11:51] the future of voice applications is that
[11:54] these are probably some of the most
[11:55] complex type of applications that have
[11:57] ever been deployed ever been built it's
[11:59] going to require one more additional
[12:01] pieces to actually evaluate voice
[12:04] applications and the interesting part
[12:06] about these is that it's not just the
[12:07] text that needs to be evaluated or the
[12:10] transcript but it's also the audio chunk
[12:13] that needs to be
[12:16] evaluated um in a lot of these Voice
[12:19] Assistant apis you have the generated
[12:22] transcript that happens actually after
[12:25] the audio chunk is really sent and so
[12:27] that's a whole another dimension around
[12:30] is the user how what's the user's
[12:31] sentiment is the speech to text
[12:34] transcription actually okay is the tone
[12:36] consistent throughout the entire
[12:38] conversation and so you actually need to
[12:41] evaluate not just the audio piece and
[12:43] the flow of the conversation and
[12:45] everything else you're doing for all
[12:46] your other you know other parts of your
[12:48] agent but also make sure that the audio
[12:50] chunks are getting their own evals
[12:53] defined on um you know intent or speech
[12:57] quality or speech detex accuracy
[13:00] um so this is important for voice so
[13:02] with that um I'm going to actually show
[13:05] you guys how we evaluate our own agent
[13:08] so that you can get a little bit of a
[13:10] example of of what some agent in the
[13:12] wild actually does um this is our own
[13:14] agent so let me actually show you what
[13:18] it looks like um you can actually go in
[13:21] our product today and there's a little
[13:24] co-pilot and our co-pilot does something
[13:27] similar to what other co-pilots do do
[13:29] where as people are spending time in our
[13:32] product we actually help them do things
[13:34] like hey help me debug this help me
[13:36] summarize this help me look at this um
[13:39] can I search with natural language
[13:41] there's kind of this co-pilot integrated
[13:42] throughout our entire product but we're
[13:45] an eval company so what do we do we
[13:48] actually dog food our own tool and we
[13:51] decide to what you're looking at here is
[13:52] actually the traces of our entire
[13:55] co-pilot actually in the wild and every
[13:59] single step of this co-pilot we actually
[14:02] run evaluations of so in this case we
[14:05] have an eval at the very top actually
[14:08] evaluating something around was the
[14:11] overall response that was generated this
[14:13] was actually a search question is the
[14:15] overall search question actually correct
[14:17] or incorrect and then we also have one
[14:21] around once it actually called the
[14:23] search router did it pick the right
[14:26] router and then did it pass in the
[14:28] correct argument
[14:29] into the router and then finally
[14:32] ultimately did it complete the task or
[14:34] the skill correctly in the execution of
[14:38] this this entire skill and so evals
[14:40] aren't just at one layer of your entire
[14:44] Trace if you take anything away from
[14:46] this conversation the goal here is
[14:48] really how do you make sure that you
[14:49] have evals throughout your application
[14:52] so that when something goes wrong I can
[14:54] debug if it actually happened at the
[14:55] router level if it happened at the skill
[14:57] level or if it happened happens
[14:59] somewhere else along the flow um and I
[15:03] think that's it from me any questions
[15:06] [Music]
[15:06] [Applause]
[15:07] [Music]
