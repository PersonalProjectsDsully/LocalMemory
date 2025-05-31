---
type: youtube
title: Cohere: Building enterprise LLM agents that work (Shaan Desai)
author: Channel Video
video_id: 4J8-D0sgU9A
video_url: https://www.youtube.com/watch?v=4J8-D0sgU9A
thumbnail_url: https://img.youtube.com/vi/4J8-D0sgU9A/mqdefault.jpg
date_added: 2025-05-26
category: General
tags: ['tutorial', 'general']
entities: ['Cohere: Building enterprise LLM agents that work (Shaan Desai)']
concepts: []
content_structure: tutorial
difficulty_level: intermediate
prerequisites: []
related_topics: []
authority_signals: []
confidence_score: 0.3
---

# Cohere: Building enterprise LLM agents that work (Shaan Desai)

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=4J8-D0sgU9A)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: llm agents, frameworks, model evaluation, failure mitigation, ai development, enterprise ai, machine learning  

## Summary

```markdown
# Summary of "Cohere: Building Enterprise LLM Agents That Work" (Shaan Desai)

## Overview
The video discusses strategies for building robust, safe, and scalable enterprise-level LLM agents. The speaker, Shaan Desai, highlights key considerations such as framework selection, agent design (single vs. multi-agent), safety mechanisms, and human-in-the-loop integration. The goal is to address challenges like hallucinations, autonomy, and real-world deployment risks.

---

## Key Points

### **Framework Selection**
- **Criteria for Choosing Frameworks**: 
  - **Observability**: Prioritize frameworks with strong debugging and monitoring capabilities (e.g., LangChain).
  - **Setup Cost**: Balance complexity with project requirements (e.g., AutoGen for quick PoCs).
  - **Support**: Ensure frameworks align with business needs (e.g., multi-agent orchestration).

### **Agent Design**
- **Single-Agent Approach**: 
  - Start with a single LLM + tools for simplicity.
  - Simplify tool specifications with clear examples to avoid confusion.
  - Use **caching** to manage long chat histories (e.g., limit to 20 turns) and reduce hallucinations.
- **Multi-Agent Systems**: 
  - Decompose tasks into constrained sub-agents with independent tools.
  - Use a **routing model** with clear instructions to handle edge cases and avoid suboptimal paths.

### **Safety and Human-in-the-Loop**
- **Autonomy Risks**: Emphasize safety as critical for real-world applications (e.g., Gmail agent requiring user confirmation before sending emails).
- **Human-in-the-Loop**: 
  - Codify rules for user intervention (e.g., HR bots, financial analysis agents).
  - Prevent unintended actions by integrating manual checks.

### **Best Practices**
- **Instruction Clarity**: Short, direct instructions reduce hallucinations vs. long, ambiguous ones.
- **Task Decomposition**: Sub-agents should handle specific, limited tasks for reliability.

---

## Important Quotes
- "Start simple: use a single LLM and tools before scaling to multi-agent systems."
- "Simplify the approach—clear examples and constraints prevent confusion."
- "Caching history helps avoid hallucinations in long conversations."
- "Safety is paramount. Never let agents act without user oversight in critical scenarios."

---

## Actionable Items
1. **Framework Choice**: 
   - Use **LangChain** for enterprise-grade observability.
   - Use **AutoGen** for rapid prototyping.
2. **Agent Design**: 
   - Begin with a single-agent setup, then scale.
   - Cache chat history to mitigate hallucinations.
3. **Safety Measures**: 
   - Implement human-in-the-loop for critical actions (e.g., email sending).
   - Define clear rules for agent autonomy.
4. **Instruction Design**: 
   - Prioritize concise, task-specific instructions.
   - Avoid ambiguous or overly complex prompts.

---
```

## Full Transcript

[00:03] hello my name is Sean and I a machine
[00:06] learning engineer here at K here and
[00:09] today I'll be talking to you about
[00:11] building Enterprise llm agents that
[00:15] work so quick overview is that you know
[00:18] we'll have an introduction we'll discuss
[00:20] some of the Frameworks and approaches
[00:21] that we've really excited about and
[00:24] we'll also address some of the critical
[00:26] components around evaluation and failure
[00:29] mitigation for M agents and then ideally
[00:32] hopefully bring all of these things
[00:34] together into a nice product
[00:37] overview so you know agents continue to
[00:41] be the most exciting application of
[00:43] generative Ani today with growing demand
[00:46] across a host of sectors including
[00:48] customer support assistance personal
[00:50] assistance rag agents uh as well as
[00:53] financial analyst
[00:56] agents however any developer who's spent
[01:00] time building LM agents knows that doing
[01:03] so in a scalable safe and seamless way
[01:08] is actually a very difficult and
[01:10] challenging task you might ask why is
[01:14] why is that so well turns out there's a
[01:17] Panacea of Frameworks tools models
[01:21] approaches evaluation criteria to choose
[01:24] from and to effectively put together
[01:27] into one endtoend pipeline
[01:30] so we really hope in this talk we can go
[01:32] through the critical decisionmaking
[01:34] process in setting up Enterprise agents
[01:37] really touching on the insights and key
[01:40] learnings we've had in building these
[01:42] Agents from addressing the Frameworks we
[01:45] love to discussing single versus
[01:48] multi-agent strategies as well as
[01:50] addressing some of the critical
[01:52] components that are less discussed
[01:55] around evaluating llm agents
[02:00] so let's start with Frameworks now over
[02:04] the past few years there have been an
[02:06] increasing number of Frameworks that
[02:08] have come into the
[02:10] market from uh components such as
[02:13] autogen crew aai as well as Lang chain
[02:17] now they all have uh their own uh
[02:21] benefits and disadvantages depending on
[02:24] a given use
[02:25] case but our core learning in the past
[02:30] year has really been to focus on three
[02:33] critical components and those are
[02:36] observability right is it easy to debug
[02:39] and fix the second is the setup cost you
[02:42] know how quickly can you iterate uh and
[02:45] resolve an issue as well as build and
[02:47] piece together the entire uh agent you
[02:50] are interested in building and then of
[02:52] course lastly is support you know is the
[02:56] framework well documented does it
[02:59] support various models and tools and
[03:03] functionalities so we've often viewed
[03:06] these Frameworks under these three
[03:09] criteria and generally we tie these
[03:14] three criteria to a given use case and
[03:17] more concretely what this might look
[03:19] like is building large scale Enterprise
[03:23] agents often requires high levels of
[03:27] observability for which we would really
[03:29] recommend going native or building with
[03:31] langra now of course the space of
[03:35] Frameworks is a continuously evolving uh
[03:38] landscape and so this is a
[03:40] recommendation at this point in time but
[03:42] we obviously expect this to change uh as
[03:46] Frameworks continue their support to
[03:48] improve observability and ease of use
[03:52] and you know in the same vein what we'
[03:55] recommend for quick tests and proof of
[03:57] Concepts is Frameworks like Ai and
[04:00] autogen the reason for this is that
[04:02] there's generally a low setup uplift uh
[04:05] with low code um to get things working
[04:08] out of the box and of course they're
[04:10] easy to leverage um pre-existing or
[04:13] pre-built agents and tools and
[04:15] orchestrate them all together in a
[04:17] multi-agent setting so these are
[04:19] immediate recommendations of course here
[04:21] at cah here we're continuously improving
[04:24] our integration support for these
[04:26] various Frameworks and we hope to and
[04:29] you know continue doing this support and
[04:32] watching this space evolve
[04:34] um and in part what we're particularly
[04:38] excited about is seeing a sliding scale
[04:42] Spectrum across these various Frameworks
[04:45] four different use
[04:47] cases um okay now once you decide on
[04:51] which framework you want to use of
[04:54] course you need to decide on the
[04:56] approach or the strategy that you plan
[04:58] to use this framework in right do you
[05:00] plan to use single agent do you plan to
[05:02] use multi-agent will you have human in
[05:04] the loop
[05:05] feedback our core
[05:08] recommendation and this is insights that
[05:10] have come from a number of use cases is
[05:12] always start simple a single llm with a
[05:17] handful of tools can often go a long way
[05:21] but more importantly being
[05:23] very um diligent about the tool
[05:27] specifications really helps uplift
[05:31] performance so what we found is uh you
[05:34] know we worked with one of one client
[05:37] and one of the asks was hey we've got a
[05:41] long list of
[05:43] apis and these API specifications could
[05:46] take in up to 10 to 15 different
[05:50] parameters and could you get a model to
[05:54] successfully uh run tool calls uh for
[05:58] these tasks
[06:00] what we've really found is to achieve
[06:03] the performance gains that they were
[06:04] trying to achieve we needed to really
[06:08] simplify the entire approach we need
[06:10] clear descriptions with very sharp
[06:12] examples on how to call the tool as well
[06:15] as providing and simplifying the input
[06:18] type so converting complex nested
[06:20] dictionaries into list stir or float
[06:26] types now in addition to these learnings
[06:29] we've also found that providing a clear
[06:32] instruction list uh which is short py
[06:36] and to the point goes a much longer way
[06:39] than providing a long set of
[06:41] instructions that can actually provide
[06:44] confusion to the model and induce
[06:46] potential uh
[06:48] hallucinations um furthermore we found
[06:52] that long streams of chat history in
[06:55] other words back and forth conversations
[06:58] between the user and chatbot that go
[07:01] over 20 turns for example can induce
[07:05] certain
[07:06] hallucinations and this is true across a
[07:08] whole host of models and Frameworks uh
[07:11] to handle that particular problem we
[07:13] really recommend caching Cally caching
[07:16] that history and retrieving it whenever
[07:20] it is particularly relevant to a new
[07:22] user query can actually help your llm
[07:25] agent uh achieve better performance
[07:27] Through Time and we'll get to what we
[07:30] mean by performance in some later slides
[07:35] now indeed there are Frameworks such as
[07:39] autogen that support multi-agent style
[07:43] orchestration and so you know in in
[07:46] multi-agent obviously in the multi-agent
[07:48] setting it's a collection of simple
[07:50] agents tied together and they have a
[07:53] routing model that decides which sub
[07:55] agent to go to and retrieve information
[07:57] from there's been a growing interest in
[07:59] the industry to build multi-agents that
[08:01] are very robust and versatile of course
[08:06] this requires a good routing model good
[08:08] reasoning model and of course sub agents
[08:12] that are well constrained and so what
[08:14] we've learned for the router is that it
[08:16] should really contain a list of tools
[08:18] with clear descriptions that always
[08:20] holds but it should also contain a sharp
[08:23] set of routing instructions that can
[08:27] Encompass potential edge cases right so
[08:30] if you're trying to Route information
[08:33] from the router to a sub agent and then
[08:35] back to another agent providing that
[08:38] type of clarity and and instruction to
[08:40] the model can really help it decide what
[08:43] it should do at each stage rather than
[08:45] it autonomously and continuously trying
[08:48] to attempt things that may not be uh the
[08:52] most optimal path to getting to the
[08:54] final
[08:55] answer of course we also recommend that
[08:58] for sub agent they should be
[09:00] constrainted to performing independent
[09:02] tasks with a small set of tools to
[09:05] return the final answer right each sub
[09:07] agent should be decomposed into a
[09:09] specific task that it should handle um
[09:12] so those are key insights we've had from
[09:14] building both simple and multi-agents in
[09:18] uh the Enterprise
[09:20] setting and now the most important bit
[09:24] right uh We've glossed over the fact
[09:25] that agents can act quite autonomously
[09:29] to achieve final results but we do think
[09:33] safety is Paramount to any scalable real
[09:36] world application right uh and here are
[09:39] some examples if we decide to use um if
[09:43] we decide to use a um Gmail agent for
[09:46] example we may want to request
[09:49] permission prior to sending emails right
[09:53] we might want the user to get a a popup
[09:56] that says hey are you okay with me
[09:58] sending this email
[09:59] right we don't want random emails to be
[10:02] sent and this might be true in the HR
[10:04] Support bot setting as well as in the
[10:06] financial analysis agent
[10:09] setting what we've learned essentially
[10:11] is that incorporating human in the loop
[10:13] is thus like really critical for
[10:15] business applications and what's really
[10:17] nice about it is that you can codify a
[10:19] set of rules under which human in the
[10:22] loop is triggered right so under various
[10:25] criteria we can force human in the loop
[10:28] to be triggered and typically this can
[10:30] happen before or right PRI like right
[10:33] before a tool is called but it can also
[10:36] happen right after a tool call is made
[10:39] uh especially if the execution output
[10:42] for example may contain various parts of
[10:45] information that you may not want to
[10:47] process
[10:49] completely okay great so we've addressed
[10:52] Frameworks we've addressed various
[10:55] approaches we've explored and the
[10:57] insights we've gained now importantly we
[11:01] need to discuss evaluation how are we
[11:03] going to assess the performance of the
[11:06] agent uh that we've built so you know
[11:11] what really makes a successful agent is
[11:14] a lot of things right it's a lot of
[11:16] moving pieces that need to come together
[11:18] for it to be successful essentially the
[11:20] model needs to make uh the the right
[11:23] tool call at the right time uh the model
[11:26] needs to be able to essentially receive
[11:29] executed tool results and reason on top
[11:31] of it and it needs to make tool calls
[11:34] very succinctly and accurately passing
[11:36] the right input parameters and it needs
[11:38] to have the ability to course correct
[11:40] even when things are going wrong right
[11:43] so what's quite interesting here is for
[11:46] the final product or the end user the
[11:49] only thing that particularly matters to
[11:51] them is the final product or the final
[11:53] answer they get from the agent but what
[11:56] is what matters most to I think
[11:58] Developers as they're debugging and
[12:01] understanding how the llm is making
[12:02] decisions is not just the final output
[12:05] but all the intermediate stages that go
[12:08] into getting to the final answer and so
[12:11] we have an example here where for
[12:14] example a user may ask a model to uh you
[12:18] know uh provide information about
[12:20] weather in New York City on February 5th
[12:24] ideally the model should decide to you
[12:26] know use a specific tool pass in the
[12:30] right
[12:31] parameters um get a returned uh set of
[12:34] results from those tools and reason over
[12:37] the return response to provide a final
[12:40] output which is you know New York City
[12:42] will be mostly sunny Etc now as you can
[12:47] see there are a number of intermediate
[12:49] stages that take place to get to the
[12:51] final response and typically what we do
[12:55] here at coh here is we build a golden
[12:58] set of ground truuth user queries
[13:03] expected function calls expected
[13:05] parameter inputs expected outputs as
[13:08] well as expected final response the nice
[13:11] thing about doing this and building this
[13:13] evaluation set is that we can run this
[13:16] large Corpus of
[13:17] evaluations through our agentic
[13:20] framework and assess any critical points
[13:23] of failure or where we think the model
[13:25] may be going wrong and this makes
[13:26] debugging particularly easy from an
[13:29] evaluation
[13:31] standpoint now you might be asking why
[13:34] I've mentioned debugging and
[13:36] observability as very important well it
[13:39] turns out that autonomous llm agents do
[13:42] indeed have a tendency to fail as most
[13:45] developers know and so we we here
[13:49] continuously exploring various failure
[13:52] mitigation strategies right and what
[13:54] we've really come and come down to is
[13:57] this this table of insights it's really
[13:59] short and simple but it's essentially
[14:02] that if you're dealing with failures uh
[14:04] um at at a low severity or at low
[14:07] failure rate what we found is actually
[14:10] prompt engineering can go a really long
[14:12] way to essentially just improving the
[14:15] quality of the tool API specs or the
[14:17] tool inputs can really help uplift the
[14:20] final uh mile uh on performance
[14:24] gaps however if you do see a tool type
[14:27] failure or model hallucinate on specific
[14:30] uh task uh in the 10 to 20% range what
[14:35] we've really found is actually building
[14:36] a targeted annotation data set is really
[14:39] useful uh for closing the Gap and lastly
[14:44] and you know perhaps most critically is
[14:46] if you are seeing a high failure rate
[14:50] particularly if an API is very difficult
[14:52] to call or API names are very similar
[14:55] and you need to disambiguate between
[14:57] them actually building a larger Corpus
[15:00] using synthetic data and fine-tuning is
[15:03] the strategy that we employ here at
[15:06] ker so I've talked to you about
[15:10] Frameworks
[15:11] approaches Val various uh evaluation
[15:15] criteria and failure mitigation
[15:17] strategies uh and what's quite nice here
[15:20] is that at coher we're constantly
[15:22] working on developing and improving
[15:24] these various criteria and one way in
[15:28] which we do this is we continuously
[15:30] improving the base model performance at
[15:32] tool calling now as you can see here
[15:35] we're particularly performant on uh bfcl
[15:38] V3 which is a standard evaluation
[15:41] criteria for single and multihop Tool
[15:43] calling um and it's a really highly
[15:46] performant 7B model as there is a
[15:49] continued interest for really
[15:51] lightweight tool calling
[15:53] models in addition to this we're also
[15:56] codifying the whole host of insights so
[15:59] in essence we're bringing together the
[16:01] learnings from the Frameworks approaches
[16:04] and deployment deploying these models in
[16:06] the wild for agentic applications into a
[16:10] single product a product we've termed
[16:12] North and essentially it's a single
[16:14] container deployment that has access to
[16:17] rag has access to various Vector DBS and
[16:21] search capacities but also has
[16:24] connectivity to various applications of
[16:27] Interest including G email Outlook drive
[16:30] and slack to name a
[16:32] few so you can think of North as a
[16:34] One-Stop shop for using and and building
[16:39] uh agentic applications as a single
[16:45] package so I even have a demo for you
[16:49] here from uh North uh and this is it in
[16:54] motion essentially it's connected to
[16:57] Gmail SL
[17:00] Salesforce uh and G drive question is
[17:04] asked about uh opportunity Salesforce
[17:07] the model invokes reasoning uh chains of
[17:11] thought essentially uh is able to pull
[17:14] the relevant document of interest um and
[17:19] essentially provide a breakdown of both
[17:23] the reasoning chain the tools that were
[17:25] called and the tool outputs which is
[17:27] pretty nice if if you're hoping to debug
[17:30] and assess uh what the model is doing
[17:33] under the hood um you can also then
[17:36] retrieve information from recent convers
[17:39] conversations um and essentially this
[17:41] would pull again both from Salesforce uh
[17:45] calls using a SQL like style query um
[17:48] and you can also update um specific uh
[17:52] tool calling capacities for example you
[17:54] could ask the model to correct which
[17:57] tool call was used and ideally what the
[18:01] model does is it updates its reasoning
[18:04] and the package decides to then
[18:06] eventually use Gmail and return the
[18:08] relevant
[18:09] information so I hope this is an
[18:13] insightful uh talk and hopefully you've
[18:17] taken away some learnings about
[18:19] deploying Enterprise llm agents uh that
[18:22] we found particularly useful and have
[18:25] packaged into north thank you
