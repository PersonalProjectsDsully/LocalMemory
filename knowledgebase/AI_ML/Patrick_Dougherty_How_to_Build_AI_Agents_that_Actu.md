---
type: youtube
title: Patrick Dougherty: How to Build AI Agents that Actually Work
author: AI Engineer
video_id: 7MiFIhlkBoE
video_url: https://www.youtube.com/watch?v=7MiFIhlkBoE
thumbnail_url: https://img.youtube.com/vi/7MiFIhlkBoE/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence
tags: ['AI agent development', 'NLP', 'machine learning', 'data engineering', 'software architecture', 'tool call optimization', 'ACI design', 'model performance', 'AI system design', 'data retrieval', 'API integration', 'AI ethics']
entities: ['Rosetta Stone', 'GPT-4', 'Claude', 'ACI', 'AI agent', 'data warehouse', 'Markdown', 'JSON', 'XML', 'tool calls']
concepts: ['agent computer interface (ACI)', 'AI agent development', 'tool call formatting', 'model performance optimization', 'data retrieval', 'natural language processing (NLP)', 'machine learning', 'AI ethics', 'system design', 'software engineering']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['basic understanding of AI/ML concepts', 'familiarity with NLP principles', 'experience with data warehouse systems', 'knowledge of API integrations', 'programming skills in Python']
related_topics: ['AI agent design', 'NLP implementation', 'machine learning systems', 'data engineering practices', 'software architecture', 'model optimization techniques', 'AI system development', 'ethical AI considerations']
authority_signals: ["I'm telling you that this is actually one of the best ways you can spend your time when you're trying to get your agent working consistently", "Claud 3.5 on it's still probably my favorite for this eve"]
confidence_score: 0.85
---

# Patrick Dougherty: How to Build AI Agents that Actually Work

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=7MiFIhlkBoE)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai agents, autonomous reasoning, tool integration, data retrieval, ai development, reasoning models, machine learning  

## Summary

# Summary of "Building Effective AI Agents: Lessons from Enterprise Deployment"

## Overview  
Patrick Dougherty, co-founder and CTO of Rosco, shares insights on building AI agents for enterprise use, emphasizing the importance of reasoning over knowledge, the role of the Agent-Computer Interface (ACI), and iterative improvements in tool call design. Key takeaways include the criticality of autonomous reasoning, the impact of small ACI tweaks, and model-specific response formatting.

---

## Key Points  
1. **Definition of AI Agents**  
   - AI agents must have:  
     - **Autonomous reasoning** (not just knowledge retrieval).  
     - **Dynamic tool calls** (e.g., querying databases, APIs).  
     - **Context-aware decision-making** based on prior interactions.  

2. **Shift from Knowledge to Reasoning**  
   - Early agents focused on retrieving static knowledge (e.g., predefined data), but effective agents require **logical reasoning** to navigate complex tasks.  
   - Example: A model forced to generate SQL queries (GPT-4o) vs. a model allowed to think (GPT-01) shows the power of reasoning.  

3. **Agent-Computer Interface (ACI)**  
   - ACI refers to the syntax/format of tool calls and responses. Small tweaks (e.g., JSON vs. Markdown) can drastically improve agent performance.  
   - **Model-specific requirements**:  
     - GPT-4o benefits from **JSON** responses.  
     - Claude requires **XML** for optimal performance.  

4. **Challenges with Large Contexts**  
   - Handling 500+ column tables or 30,000-token responses requires structured formatting (e.g., JSON) to avoid misinterpretation.  

5. **Model Selection Matters**  
   - The model used for **decision-making** (e.g., choosing the next tool call) must be "generally intelligent" (e.g., Claude 3.5) to avoid logical errors. Cheaper models may suffice for subtasks but not for critical reasoning.  

---

## Important Quotes  
- *"The model is performing the thinking capabilities... if the model sucks, your users aren't going to be happy."*  
- *"Small tweaks to the ACI can have a massive impact on accuracy... it makes no sense, but it’s one of the best ways to spend your time."*  

---

## Actionable Takeaways  
1. **Prioritize Reasoning Over Knowledge**  
   - Design agents to think through problems, not just retrieve data.  

2. **Iterate on ACI Design**  
   - Test response formats (JSON/XML) and refine tool call syntax for your target models.  

3. **Optimize for Model-Specific Needs**  
   - Use JSON for GPT-4o, XML for Claude, and ensure responses align with the model’s training data.  

4. **Use Capable Models for Critical Decisions**  
   - Reserve cheaper models for subtasks; use high-capability models (e.g., Claude 3.5) for reasoning-heavy steps.  

--- 

This summary captures the core lessons from Patrick’s experience, focusing on practical strategies for building robust, enterprise-grade AI agents.

## Full Transcript

[00:01] hi I'm Patrick I was the co-founder and
[00:03] CTO of Rosco and two years ago we
[00:06] decided to rip apart our entire product
[00:08] and rebuild it around AI agents these
[00:11] are some of the lessons we
[00:15] learned first of all let's start out
[00:17] with a definition since a lot of people
[00:19] use the term agent but don't necessarily
[00:22] mean the same thing that I do for my
[00:24] definition I came up with there's three
[00:26] specific criteria that it has to have to
[00:28] be considered an AI agent
[00:30] number one the agent needs to be able to
[00:33] take directions these can be human or AI
[00:36] provided but it should be one specific
[00:40] objective or overarching
[00:42] goal two it has to have access to call
[00:46] at least one tool and get a response
[00:49] back and three it should be able to
[00:52] autonomously reason how and when to use
[00:55] its tools to accomplish that
[00:57] objective what that means is it can't be
[01:00] a predefined sequence of this tool will
[01:03] run and then this next tool will run in
[01:06] a prompt chained type of setup it has to
[01:09] use autonomous reasoning in order to be
[01:11] called an AI
[01:14] agent one of the biggest lessons we
[01:16] learned in building agents was the
[01:19] necessity to focus on enabling the agent
[01:23] to think rather than be limited by what
[01:26] the underlying model
[01:27] knows so a lot of our tool calls were
[01:30] focused on retrieval rather than trying
[01:32] to do rag where we inserted contents
[01:36] into the system prompt um to to guide
[01:39] the agent's actions instead we focused
[01:41] on discrete tool calls that allowed it
[01:44] to perform retrieval and get the
[01:46] relevant context into its its context
[01:49] window while it was
[01:51] working the uh product that we built was
[01:55] enabling a AI agent to search and query
[01:58] your Enterprise data in your a warehouse
[02:00] for you and so one of the a great way to
[02:04] kind of illustrate the um limitations of
[02:08] focusing on knowledge over reasoning is
[02:11] when it comes to writing a SQL query uh
[02:14] given some data so what we found
[02:16] frequently was that if you gave the
[02:19] agent a whole bunch of tables and all of
[02:21] the columns in those tables it would
[02:24] fail to reason correctly about which one
[02:27] to use it would get overwhelmed by the
[02:30] number of tokens in the prompt and
[02:32] either choose the wrong one or just
[02:34] write a terrible query that didn't
[02:36] execute in the first
[02:37] place that's where we went to these more
[02:40] discreet um more simple uh building
[02:44] blocks of tool calls such as search
[02:46] tables get table detail or profile a
[02:50] column the agent is then tasked with
[02:54] using those iteratively to find the
[02:56] right columns for the right query
[03:01] similarly we saw this play out as
[03:04] reasoning models uh become recently
[03:06] introduced as well so when you focus on
[03:10] reasoning you give a reasoning model the
[03:12] ability to first attempt to find the
[03:16] data needed to answer a particular
[03:18] question but then if it doesn't find it
[03:20] it should be able to tell you that it
[03:22] didn't find it and you can take some
[03:24] action with that knowledge what we've
[03:27] seen with GPT 40 uh prior to reasoning
[03:30] models coming out is that regardless of
[03:33] the ability or the underlying data being
[03:36] present for it to be able to answer a
[03:38] question it is going to attempt to write
[03:40] that query
[03:42] anyway let's walk through an example of
[03:45] this so in this prompt I'm providing 40
[03:50] with a table schema that uh is pretty
[03:53] standard from Salesforce so there's a
[03:55] table for accounts contacts and
[03:57] opportunities and these aren't all the
[03:59] columns in each of those tables I'm just
[04:01] oversimplifying for representative
[04:03] purposes at the bottom I've asked GPT
[04:06] for a question write a query to see how
[04:08] many of my customers churned in the last
[04:11] month what you'll see from GPT 40 is it
[04:15] is very incentivized to write a query
[04:19] give me back SQL it's not really
[04:21] stopping to think about uh is this query
[04:25] even possible to write in the first
[04:27] place so it makes some uh some
[04:29] assumptions and then it just starts
[04:31] writing SQL its definition is really bad
[04:35] for uh calculating churn um it's
[04:38] essentially just looking in the account
[04:41] table and assuming that uh there's a
[04:45] different type of account that's not
[04:48] customer that would somehow be updated
[04:50] when a customer turned um so I think
[04:53] this is very likely to lead an analyst
[04:56] to a totally wrong answer if they were
[04:58] to take this query and automa Al run it
[05:00] um but what you see is that it's not
[05:02] pushing back in any way it doesn't stop
[05:04] to say I should think about this and and
[05:07] consider if this is even
[05:09] possible okay now let's flip over and
[05:11] see the same prompt run on uh 01 so this
[05:16] prompt is the exact same up top we're
[05:18] providing the same schema and the same
[05:20] question 01 reasoned through uh the the
[05:24] various aspects of this question and it
[05:28] accurately concluded
[05:30] that there is no way given the schema
[05:34] provided to calculate the uh status of
[05:39] churn on an account and so that
[05:43] conclusion kind of shows the difference
[05:44] of giving the model the freedom to think
[05:47] and encouraging it to think and reason
[05:49] versus just um forcing it essentially to
[05:54] to come up with the SQL query so that's
[05:56] one of the key lessons that that we
[05:57] learned in kind of building and uh
[06:00] deploying agents that were useful for
[06:05] Enterprises as part of this there is a
[06:08] huge need to iterate on what I would
[06:11] call the ACI I believe this was a um
[06:14] this is a paper that was published that
[06:15] kind of coin this term uh agent computer
[06:17] interface and it's really referring to
[06:20] the exact syntax and structure of tool
[06:22] calls both what goes into the tool call
[06:26] and then the content and format of the
[06:28] response from the you know API or python
[06:32] code maybe that would handle and execute
[06:34] that tool call so what we learned is
[06:37] really small tweaks to the agent
[06:39] computer interface can have a massive
[06:42] impact on the accuracy and performance
[06:45] of your agent and you will feel when
[06:47] you're making these tweaks like they are
[06:49] so trivial it makes no sense that they
[06:51] would have any bearing on your agent's
[06:53] performance um however I'm I'm telling
[06:56] you that this is actually one of the
[06:58] best ways you can spend your time
[07:00] when you're trying to get your agent
[07:01] working
[07:02] consistently a couple of specific
[07:04] examples so number one one of the things
[07:07] that we found was that the format of the
[07:10] response depending on the model was
[07:14] consumed Better or Worse likely
[07:17] correlating to the underlying training
[07:19] data potentially of the model so
[07:21] specifically when working with GPT 40 we
[07:24] transitioned from responding with these
[07:27] search result payloads initially they
[07:30] were formatted as markdown and we were
[07:32] seeing examples where the agent would
[07:34] look at that response that it got back
[07:36] from the tool call and tell us that a
[07:39] column did not exist when you could see
[07:41] the column within the uh context you
[07:45] know passed back in the tour result
[07:47] these were long context Tour results
[07:49] often times some of our customers had
[07:51] 500 or thousand column tables in their
[07:53] data warehouse so it was understandable
[07:55] if you're getting you know 30,000 tokens
[07:57] back that there might be some challenges
[08:00] there but we felt like to consistently
[08:03] be completely blind to it um there had
[08:05] to be a way to improve this so we tested
[08:07] different formats we ultimately learned
[08:09] that just switching the formatting of
[08:11] the response from markdown to Json
[08:14] having that semi-structured uh payload
[08:16] in response immediately solve this
[08:18] problem for for GPT
[08:20] 4L however we learned later on that for
[08:23] Claude it was really important to
[08:24] provide XML back to the model uh and not
[08:27] Mark uh not Json so so again depending
[08:30] on the model you're using and the
[08:33] specific uh function arguments and then
[08:36] responses that you're you're providing
[08:37] from those tools it can really impact
[08:39] your agent's
[08:45] performance think of the model as your
[08:47] brain when you're building an agent uh
[08:50] the model is performing the the thinking
[08:54] capabilities and if the model sucks then
[08:56] your users aren't going to be happy
[08:58] because they're going to see some of the
[08:59] obvious logical fallacies that the agent
[09:02] will make um so I think what's what's
[09:05] critical there is even if some of your
[09:07] tasks need to run on a cheaper model
[09:09] like some of your tool calls or or some
[09:10] of the uh sub prompts that that might be
[09:14] triggered by your agent it's really
[09:16] important that the actual model making
[09:18] the determination of which tool call to
[09:21] make next based on what has happened up
[09:23] to that point is uh a generally
[09:26] intelligent model um I would say Claud
[09:28] 3.5 on it's still probably my favorite
[09:31] for this even beyond the reasoning
[09:33] models because it does a really a really
[09:36] nice balance between speed cost and
[09:40] making a good decision uh based on what
[09:42] it's learned so
[09:44] far another thing we talked about GPT 40
[09:47] vers1 and how 40 is is incentivized to
[09:51] make an effort even if the task is
[09:53] impossible one thing you can learn
[09:55] though by observing the failure modes of
[09:57] Agents running with a certain model
[09:59] model is often times the way it
[10:02] hallucinates tells you what the model
[10:04] expects in a tool call for instance so
[10:08] if you see it consistently ignoring your
[10:11] Json schema for a tool call and
[10:13] providing an argument in a different
[10:15] format that should be an indicator to
[10:18] you that the agent is telling you how it
[10:21] thinks how it thinks the tool call
[10:23] should be defined and if you can change
[10:26] it to match that expected format you're
[10:29] going to generally improve agent
[10:31] performance because it's going to be
[10:34] closer to the training data and the
[10:37] Instinct that the model has natively
[10:39] versus you trying to force it into doing
[10:41] something
[10:44] else another lesson we learned was that
[10:46] fine-tuning models was a waste of time
[10:49] uh I think this is generally accepted
[10:51] now but there's still a little bit of
[10:53] work happening on building agents with
[10:56] fine-tuned models if you buy the premise
[10:59] that we're focusing on reasoning over
[11:03] inherent knowledge of the model then
[11:06] it's logical to say that fine-tuning
[11:09] does not really improve reasoning
[11:11] actually in our uh experience it
[11:14] actually decreased reasoning in a lot of
[11:16] cases because it effectively overfit or
[11:19] overtuned the model to do a specific
[11:21] sequence of tasks each time rather than
[11:23] stopping and thinking uh if it you know
[11:27] was was making the right decision so so
[11:30] I would really spend your time uh
[11:32] focusing on that ACI
[11:34] iteration rather than trying to build a
[11:37] fine tuned model to run your
[11:41] adanon another question that we got
[11:44] frequently from customers users and
[11:47] others was uh hey what abstraction are
[11:49] you using which framework are you
[11:51] building on and for two reasons we did
[11:55] not end up using an abstraction number
[11:57] one was simple when we started building
[11:58] this to years ago none of the
[12:00] abstraction libraries like a lang graph
[12:03] or a crew AI were publicly available yet
[12:06] so we didn't even have a choice really
[12:07] we were just kind of basing some of our
[12:09] research off of Auto GPT at the time but
[12:12] the second reason is that even as those
[12:14] Frameworks started to become more
[12:16] popular we continued to evaluate uh
[12:18] transferring some of our code to them
[12:20] the problem was there's huge blockers
[12:22] and considerations when you want to go
[12:24] to production with an with a agent
[12:27] running on one of these Frameworks uh
[12:30] one of the key things for us as an
[12:32] example was the ability for an enduser
[12:36] security credentials to Cascade down to
[12:39] the agent they were talking to so think
[12:41] about uh if if a human is trying to use
[12:45] an agent to query their snowflake
[12:46] account they may have very granular
[12:48] permissions within that snowflake
[12:50] account of of what they specifically are
[12:52] allowed to see uh in the underlying data
[12:56] we needed our agent to be able to run
[12:58] with that users permissions using an
[13:00] ooth integration and that was something
[13:03] that made some uh an approach like Lang
[13:06] graph extremely difficult to build and
[13:08] scale because we needed to uh
[13:11] essentially manage the authentication
[13:12] process and the underlying um Service
[13:16] keys and tokens uh within our codebase
[13:19] not within a third party framework so
[13:22] the lesson I think to take away from
[13:23] that is think about what your end goal
[13:26] is first before you get too dependent on
[13:29] one of these Frameworks there is not too
[13:31] much code that you have to write to
[13:33] build an agent or even a multi-agent
[13:36] system if you're in Prototype mode then
[13:39] sure use an abstraction speed yourself
[13:42] up validate something as quickly as
[13:43] possible but if your goal at the end is
[13:45] production you'll likely regret being
[13:48] too dependent on a third party
[13:54] Library one of the other philosophical
[13:56] conclusions we made is ultimately your
[13:59] agent's not your remote meaning
[14:02] the system prompts a lot of people were
[14:04] really careful not to share those uh
[14:07] early on you know as people were
[14:08] building agents acting like there was a
[14:10] lot of Ip in there I don't believe
[14:12] that's true I think what really
[14:15] is uh the most valuable thing you can do
[14:18] is the set up the ecosystem around your
[14:20] agent including the user experience of
[14:23] how your user interacts with your agent
[14:25] and then also the connections and the
[14:27] security protocols that your agent has
[14:29] to follow in doing its work that is the
[14:33] most timec consuming part of building a
[14:35] production quality agent into a product
[14:38] and that is ultimately going to be your
[14:41] Mo in as much as we can even have Moes
[14:43] these days with how quickly the stuff is
[14:49] moving last but not least one of the key
[14:52] lessons that we learned more recently
[14:53] was about designing and executing on
[14:55] multi-agent systems so about a year into
[14:58] our process of transitioning to an
[15:01] agent-based product um as our customers
[15:03] were getting comfortable with single
[15:05] agents we introduced a multi-agent
[15:07] concept and these are some of the key
[15:09] lessons we learned when doing that that
[15:11] really stuck with us and I think have
[15:13] continued to be highly resonant when
[15:15] you're designing agents in a product
[15:19] number one is the need to implement a
[15:21] manager agent within a hierarchy the
[15:24] reason for that is that we found the the
[15:28] manager agent would own the final
[15:30] outcome but could delegate subtasks to
[15:33] specific worker agents they would have
[15:35] more context in their instructions and
[15:38] more specific tool calls to accomplish
[15:40] those tasks whereas if you gave all of
[15:43] that information to a single manager
[15:45] agent it could become overwhelmed it
[15:47] might um make bad decisions go down bad
[15:50] bad
[15:51] paths uh we also learned that the um
[15:55] number of Agents working together
[15:57] there's almost a two Pizza rule kind of
[15:59] similar to how Jeff Bezos would design
[16:01] teams early on at Amazon that applies
[16:03] here so we found that if you could limit
[16:06] yourself to about between five and eight
[16:09] agents working together then that was
[16:12] typically a task that could be
[16:13] accomplished well by a multi-agent team
[16:17] I've seen and and prototype some systems
[16:20] where you might have 25 or 50 agents
[16:22] working together and really what happens
[16:24] is you you strongly decrease the
[16:27] likelihood that the actual ual outcome
[16:29] ever gets accomplished because you're
[16:32] likely to trigger infinite Loops or go
[16:34] down paths that you don't return
[16:37] from incentivization is the number one
[16:40] way to set these things up so the goal
[16:43] should not be to force your worker
[16:46] agents through a discret set of steps
[16:49] but it rather to incentivize your
[16:51] manager agent meaning describe and uh
[16:54] quote unquote reward it with
[16:57] accomplishing the overall objective and
[17:00] relying on it to manage the underlying
[17:02] worker agents and make sure that they uh
[17:07] their output is valuable and that it can
[17:09] be used um within the context of
[17:12] achieving that broader
[17:14] outcome I wrote more about the um
[17:18] designing effective multi-agent teams on
[17:21] my blog at asb.com uh this is the the
[17:24] blog post so I go into a little more
[17:26] detail about these principles and some
[17:28] other thoughts as well as
[17:30] well thanks so much for your time and
[17:33] hope you enjoyed uh learning all of the
[17:36] mistakes that I've made the last couple
[17:37] years in designing agent systems and
[17:39] multi-agent systems I hope you can avoid
[17:41] them and that it saves you some time
