---
type: youtube
title: Agent Evals: Finally, With The Map
author: Channel Video
video_id: y2Drx0SDZLo
video_url: https://www.youtube.com/watch?v=y2Drx0SDZLo
thumbnail_url: https://img.youtube.com/vi/y2Drx0SDZLo/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: ['Agent Evaluation', 'LLM Optimization', 'AI System Design', 'Evaluation Metrics', 'Multi-step Processes', 'Error Handling', 'Cost and Latency', 'Offline vs. Online Testing', 'Proxy Metrics', 'System Design', 'AI Testing', 'Evaluation Frameworks']
entities: ['Ari Heluk', 'Root Signals', 'RAG', 'LLM', 'Agent Evals', 'tool usage', 'error management', 'cost and latency optimization', 'tracing and debugging', 'offline vs. online testing']
concepts: ['Agent Evaluation', 'Truthfulness', 'Goal Achievement', 'Multi-step Processes', 'Tool Selection', 'Error Handling', 'Cost and Latency Optimization', 'Offline vs. Online Testing', 'Proxy Metrics', 'System Design']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Understanding of Large Language Models (LLMs)', 'Basic knowledge of system design', 'Familiarity with evaluation metrics']
related_topics: ['AI Evaluation', 'Machine Learning System Design', 'Natural Language Processing', 'Software Testing', 'Optimization Techniques', 'Error Handling in AI', 'Cost Management in AI', 'Online vs. Offline Testing']
authority_signals: ['these are all the things that relate to uh to the behaviors even before you have a chain of uh behaviors', "I'm just sort of listing not to leave this out but they don't needly fall into this general map..."]
confidence_score: 0.8
---

# Agent Evals: Finally, With The Map

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=y2Drx0SDZLo)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: agent evaluation, ai evaluation, semantic analysis, behavioral analysis, truthfulness, alignment, tools  

## Summary

# Agent Evals: Finally, With The Map Summary

## Overview  
The video discusses the evaluation of AI agents, emphasizing the balance between **semantic** (how agents represent reality) and **behavioral** (how agents act to achieve goals) aspects. The speaker, Ari Heluk from Root Signals, introduces a structured framework to assess agent performance, ensuring they align with truthfulness, utility, and efficiency in real-world applications.

---

## Key Points  
- **Semantic Evaluation**:  
  - **Single-turn**: Coherence, consistency, safety, alignment with values, and factfulness (truthfulness from data grounding).  
  - **Multi-turn**: Conversation history consistency, reasoning quality, and adaptability over time.  

- **Behavioral Evaluation**:  
  - **Tool Use**: Correct tool selection, output quality, error handling, and interaction format.  
  - **Task Progression**: Convergence toward goals, plan quality, and utility-driven outcomes.  

- **Symmetry Between Aspects**:  
  - Representations are grounded in **truthfulness** (data alignment).  
  - Behaviors are grounded in **goal achievement** and **utility**.  

- **Practical Considerations**:  
  - **Cost/Latency Optimization**: Minimize steps, time, and resources.  
  - **Tracing/Debugging**: Monitor agent decisions and errors.  
  - **Offline vs. Online Testing**: Differentiate between development and real-time evaluation.  
  - **Special Cases**: Tool-specific metrics, advanced research topics, and edge scenarios.  

---

## Key Quotes  
- *"Truthfulness is achieved by grounding in data; goal achievement is what is achieved by grounding to the tools."*  
- *"The ultimate metric is the agent’s goal; other metrics are proxies."*  

---

## Actionable Items  
1. **Evaluate semantic and behavioral aspects** using structured frameworks.  
2. **Prioritize proxy metrics** (e.g., coherence, tool accuracy) to track progress.  
3. **Optimize cost and latency** for efficient agent performance.  
4. **Implement tracing/debugging** for error management and transparency.  
5. **Differentiate offline (development) vs. online (production) testing**.  
6. **Account for special cases** (e.g., tool-specific metrics, research-driven scenarios).

## Full Transcript

[00:01] hi this is Ari heluk from root signals
[00:05] uh presenting agent evaluations finally
[00:08] with the map so the agent
[00:12] evaluation is rather Art and Science and
[00:16] ultimately it is nonetheless required to
[00:19] actually ensure that your agents do what
[00:21] you expect them to do especially when
[00:23] you're launching them in production so
[00:27] without further Ado let's just uh
[00:30] Dive Right There into the map and start
[00:33] to get an understanding of what are all
[00:36] the things involved if you want to
[00:37] evaluate all the aspects of your
[00:41] agents uh so the agent evaluation can be
[00:44] actually neatly divided to the semantic
[00:47] and behavioral parts of what the agents
[00:50] do the semantic part is all about how do
[00:54] the
[00:55] representations uh of the reality that
[00:58] the agent has actually relate to the
[01:01] reality whereas the behavioral parts are
[01:05] all about how do the actions and the
[01:08] tools that the agent is using actually
[01:11] contributing to the achievement of the
[01:14] agent's goals in its
[01:16] environment and ultimately what kind of
[01:18] effects it will have on its environment
[01:21] as
[01:22] well the semantic part is uh further
[01:26] divided into what could be call the
[01:29] single step or single turn uh items
[01:33] which are like coherence consistency Etc
[01:37] so various sematic virtues and what can
[01:40] be called the multi-
[01:41] turn aspect of the same so this Rel to
[01:44] chatter reasoning whereas in the
[01:46] behavioral part you also have this
[01:49] distinction whether you're looking at
[01:51] the task progression and planning or
[01:53] then individual selection and usage of
[01:56] tools so let's uh dive into each of
[01:59] these
[02:00] and paying also attention to the fact
[02:04] that
[02:06] truthfulness is ultimately achiev by
[02:09] grounding uh the representations in your
[02:12] data often with track
[02:15] whereas uh the goal achievement is what
[02:21] actually uh is achieved by grounding to
[02:25] the tools that the agent has available
[02:29] and the this is sort of a symmetry that
[02:32] is not accidental because in a sense
[02:35] there's similarity and analogy between
[02:39] uh representations and behaviors because
[02:43] representing the world is a kind of
[02:44] activity so you can see that uh that the
[02:49] representations are in a sense a special
[02:53] case of tools special case of uh uh of
[02:57] behaviors and uh
[03:01] let's then dive into these individual
[03:05] parts of the
[03:07] map so first looking at the semantic
[03:10] quality for the single turn case so here
[03:13] we have these Universal virtues there's
[03:15] a long list of these that you can look
[03:17] at uh and these are actually non agenic
[03:22] in a sense and we are only covering them
[03:24] here because of completeness so that you
[03:26] can sort of understand these agent Parts
[03:29] through the contrast so these are things
[03:32] like uh uh is
[03:35] the uh the reply that the agent is
[03:37] giving to the user is this consistent is
[03:40] the is the content actually safe and so
[03:43] on and so on and then there's the inter
[03:47] interesting and important part of
[03:48] whether whatever the agent is actually
[03:50] saying if it's uh aligning uh with the
[03:53] values of uh of the organizations or
[03:57] people uh who are the stakeholders and
[04:00] also whether it aderes to the policies
[04:02] of the
[04:03] same rag or what could be more generally
[04:07] called yet attention
[04:09] management uh is then something that you
[04:11] need to measure through specific
[04:13] evaluators such as those looking at
[04:15] whether the retreat context uh was
[04:18] correct whether all of it was
[04:20] comprehensively recalled uh and so on
[04:22] and so on and ultimately relating the
[04:24] answers uh to the external reality
[04:27] through what is often called the Fai
[04:29] fulness which is then separate from uh
[04:33] from the both the answer question
[04:35] relevance and also from the notion of
[04:37] factfulness in general which relates to
[04:41] the reality Beyond just the reference
[04:43] data that the rag is using so now moving
[04:47] forward uh we should also pay attention
[04:51] to the fact that the rag evaluations
[04:55] actually come uh in many forms and they
[04:58] they also have certain symmetries uh
[05:01] that are not that difficult to
[05:02] understand when you look at them uh
[05:04] through uh a map like this so they are
[05:07] all just essentially looking at
[05:09] different relationships between the
[05:11] parts of the rag pipeline but this is
[05:14] not the the main topic of the
[05:15] presentation so you can look look up
[05:17] more information through the uh
[05:20] background material links that people
[05:21] provide so then moving to the multi-turn
[05:24] case the multi-turn in the semantic
[05:27] quality sense means essentially chat
[05:30] conversation histories how do these
[05:32] develop what sort of things we want to
[05:33] look for in this consistency Etc
[05:37] adherence and sticking to the topics
[05:39] when that is actually necessary
[05:42] sometimes we want to allow changing
[05:43] topics if the for example a chatbot
[05:45] users user wants to change the topic or
[05:48] sometimes we don't but we need to be
[05:49] able to uh be aware of this then super
[05:54] important uh and almost groundbreaking
[05:57] progress has been achieved by
[06:00] uh by uh investments in reasoning so you
[06:04] can also uh actually evaluate reasoning
[06:06] traces the reasoning uh Chain of Thought
[06:10] if if allowed to use that term here and
[06:13] that's sort of another way of looking at
[06:15] the kind of sequential or M well multi-
[06:18] turn and sequential kinds of activities
[06:21] that the agent is just doing in the
[06:23] course of its reasoning and
[06:24] representations of the
[06:25] world before we even taking any kind of
[06:28] actions and now we move to the side so
[06:30] here we have uh things to evaluate such
[06:33] as where the agent is actually following
[06:36] instructions is it extracting the the
[06:38] tool characteristics correctly is it
[06:41] selecting the right is the right tool
[06:44] being selected is the output quality of
[06:46] the tools correct are the error
[06:48] situations handled correctly are the
[06:50] structures interation tool format are
[06:54] they uh correct so these are all all the
[06:58] things that relate to uh to the
[07:00] behaviors even before you have a chain
[07:02] of uh behaviors and when you move to
[07:04] this chain of behaviors or multistep or
[07:07] uh multi-turn uh cases so then you
[07:10] actually start to look at like are the
[07:15] actions that the ACT agent is taking
[07:17] converging towards actually achieving
[07:19] its goal and uh is the plan that the
[07:22] agent might have actually consistent and
[07:25] is it actually uh high quality in
[07:27] whatever sense you want to measure that
[07:30] uh so then both of these are actually
[07:33] grounded uh on external reality so uh
[07:37] like mentioned the representations are
[07:40] grounded on truthfulness and uh the
[07:44] activities and behaviors are ultimate
[07:46] grounded by goal achievement and
[07:49] utility uh and this is uh what sort of
[07:53] uh is the ultimate uh metric to
[07:57] everything else and know uh that the
[07:59] agent is trying to do and all these
[08:02] other things along the way are sort of
[08:03] just proxy metrics so to
[08:07] speak uh moving to other practical
[08:09] considerations we can only scratch the
[08:11] surface here so I'm just sort of listing
[08:14] not to leave this out but they don't
[08:16] needly fall into this general map that I
[08:19] presented but should also be taken into
[08:21] account on the background so most
[08:24] important of which is the cost and
[08:26] latency optimization so generally you
[08:27] want to the agent to progress towards
[08:30] its goal as quickly as possible and as
[08:32] cheaply as possible so cost and latency
[08:36] optimization the number of steps
[08:38] optimization and then moving to the what
[08:42] you ofer are going to need which is the
[08:43] tracing and debugging so being able to
[08:46] actually see where the agent go wrong
[08:49] error management here refers to to
[08:51] dealing with the with the errors of the
[08:55] tool usage so not the actual like
[08:58] semantic errors that that the agent is
[09:00] doing in the course of its inference and
[09:02] thinking
[09:03] process uh very important distinction to
[09:06] keep in mind is the offline versus
[09:07] online testing so what are the things
[09:10] that uh that you can actually uh try out
[09:13] and evaluate during development and what
[09:16] are the things that you can do and must
[09:18] do or should do uh during the actual
[09:22] online activities of the agent and these
[09:25] are actually going to become like a two
[09:28] very distinct Dimensions that could be
[09:31] also included on the map but uh but that
[09:34] would make the map map more complicated
[09:36] so that's why I'm just mentioning them
[09:38] here now separately and then we have
[09:41] various special cases that I don't have
[09:43] time to cover some of these uh are uh
[09:46] more refined and more advanced than
[09:48] others and and some of these things are
[09:50] sort of uh more researchy and there's a
[09:53] lot of papers on each of these topics
[09:55] and uh uh depending on what you're doing
[09:59] tool specific metrics might actually be
[10:02] useful to add to the mix even uh uh and
[10:06] they might even be rather simple to
[10:08] implement because the tools are often
[10:10] something as easy as straightforward as
[10:13] like API calls and uh and such things
[10:16] that can actually be just measured
[10:17] separately uh using more traditional
[10:20] software testing
[10:23] methodologies uh one important part to
[10:26] mention here is that a lot of these
[10:28] measurements are going to to be
[10:30] implemented with llm as charge
[10:32] techniques and now the caveat uh behind
[10:35] this is that the quite often when people
[10:40] start implementing these evaluation
[10:42] methodologies they are looking at this
[10:44] kind of a single tier approach single
[10:46] tier here means that you're focusing on
[10:48] optimizing this operative element flow
[10:50] meaning that you're optimizing your
[10:52] agent which makes sense but if you only
[10:55] are concerned of uh with getting some
[10:57] scores on what the agent is doing then
[11:00] you're sort of forgetting that what
[11:01] about all the cost latencies uncertainty
[11:04] related to the charge itself the charge
[11:07] that is on the background so you should
[11:10] be actually uh taking into account as
[11:14] early as possible that you are going to
[11:16] need to also optimize the charge itself
[11:19] and this is what the what we could call
[11:21] Double tier so you need to optimize both
[11:23] the operative LM flow that powers your
[11:26] agent and then this chargement flow that
[11:28] actually Powers your evalu ations and uh
[11:31] this is a rather complex situation in
[11:34] general and we are calling this eval Ops
[11:37] because uh this seems like a like a
[11:40] separate kind of thing that involves uh
[11:43] evaluations that themselves are so
[11:46] complicated uh so expensive and slow
[11:49] that they sort of earn their own uh
[11:52] category of of activities and this is uh
[11:56] something that uh that we have written
[11:59] about and uh and you can also find more
[12:02] about this on the source materials uh
[12:05] the general general tast of it is that
[12:08] that eval Ops is a kind of a special
[12:10] case of llm Ops and and actually
[12:13] operates on different kinds of entities
[12:15] that that the llm Ops uh uh in
[12:19] general and uh and then it also requires
[12:23] different ways of thinking different
[12:24] kind of software implementations and
[12:26] also essentially a different kind of
[12:29] resourcing to to get those evaluations
[12:32] right so thank you very much this was
[12:35] only a brief Glimpse on the on the
[12:37] general landscape I hope the map is
[12:39] helpful to you and uh please take a look
[12:42] at the source materials which will give
[12:44] you more depth to each of these uh these
[12:47] topics and uh happy to discuss any of
[12:51] these things and let me uh know if I'm
[12:54] forgetting something crucial and uh this
[12:57] uh presentation will of course be
[12:59] obsolete by the time it it goes out so
[13:02] uh probably when when you're watching
[13:04] this there's already some major
[13:06] developments have happen but that's uh
[13:08] that's how it is on this General Life of
[13:11] uh of uh AI Engineers uh so let's go out
[13:15] there and make our agents measurable
[13:18] controllable and let's make sure they
[13:20] are actually doing our biding and not
[13:23] not rebelling against our uh ultimate
[13:26] intentions thank you very much
