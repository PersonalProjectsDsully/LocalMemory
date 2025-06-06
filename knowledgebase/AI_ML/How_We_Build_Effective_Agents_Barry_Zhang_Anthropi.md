---
type: youtube
title: How We Build Effective Agents: Barry Zhang, Anthropic
author: AI Engineer
video_id: D7_ipDqhtwk
video_url: https://www.youtube.com/watch?v=D7_ipDqhtwk
thumbnail_url: https://img.youtube.com/vi/D7_ipDqhtwk/mqdefault.jpg
date_added: 2025-05-26
category: AI Development
tags: ['AI agents', 'machine learning', 'tools integration', 'system prompts', 'iteration speed', 'optimization', 'user trust', 'model context protocol', 'agent design', 'tutorial', 'workshop', 'development practices']
entities: ['Mahes', 'model context protocol MCP', 'coding agents', 'tools', 'system prompt', 'environment', 'loop', 'workshop']
concepts: ['agents', 'environment', 'tools', 'system prompt', 'iteration speed', 'optimization', 'user trust', 'model context protocol']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of machine learning', 'familiarity with tools', 'system prompts', 'agent design principles']
related_topics: ['AI agents', 'machine learning', 'tool integration', 'system design', 'user trust', 'optimization techniques', 'model context protocols', 'iterative development']
authority_signals: ['We have learned the hard way to keep this simple', "I've seen that workshop. It's going to be really fun."]
confidence_score: 0.8
---

# How We Build Effective Agents: Barry Zhang, Anthropic

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=D7_ipDqhtwk)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai agents, ml models, agent design, agentic systems, workflow orchestration, machine learning, ai development  

## Summary

# Summary of "How We Build Effective Agents" by Barry Zhang

## Overview  
Barry Zhang from Anthropic discusses strategies for building effective AI agents, emphasizing three core principles: **avoiding overuse of agents**, **simplicity in design**, and **understanding the agent's perspective**. He highlights the evolution from basic tools to complex workflows, outlines a checklist for evaluating agent use cases, and advocates for iterative development focused on core components.

---

## Key Points  

### 1. **Don’t Build Agents for Everything**  
- **Use case evaluation**: Use a checklist to determine if an agent is suitable:  
  - **Complexity**: Is the task ambiguous and high-value (e.g., coding)?  
  - **Value**: Does the task offer significant benefits (e.g., code quality)?  
  - **Derisking**: Can you limit scope (e.g., read-only access) to mitigate trust issues?  
  - **Cost of error**: Is the agent’s autonomy manageable?  
- **Examples**: Coding is a strong agent use case due to its complexity, value, and verifiable outputs (e.g., unit tests).  

### 2. **Keep It Simple**  
- **Core components**: Agents are defined by three elements:  
  1. **Environment**: The system the agent operates in.  
  2. **Tools**: Interfaces for the agent to take actions.  
  3. **System prompt**: Goals, constraints, and behavior guidelines.  
- **Iterate first**: Complexity upfront slows iteration. Focus on the three components first, then optimize (e.g., parallelizing tool calls, reducing cost).  
- **Examples**: Agents for coding, search, or other tasks share similar backbones but differ in tools and prompts.  

### 3. **Think Like Your Agent**  
- **Avoid human bias**: Agents may behave unexpectedly from a human perspective.  
- **Context window**: Understand the agent’s limitations (e.g., token constraints) and design accordingly.  
- **Trust-building**: Clearly communicate progress to users to foster trust.  

---

## Quotes  
- *"Any complexity up front is really going to kill iteration speed."*  
- *"Keep it as simple as possible as you're iterating."*  
- *"Agents can exhibit sophisticated behavior, but at each step, what the model does is... limited by its context window."*  

---

## Actionable Items  
1. **Evaluate use cases** using the checklist: assess complexity, value, risk, and error cost.  
2. **Start with the three core components** (environment, tools, system prompt) and iterate.  
3. **Optimize later**: Focus on reducing cost, latency, or trust issues once the agent’s behavior is stable.  
4. **Understand the agent’s context**: Avoid human bias by simulating the agent’s perspective.  
5. **Explore tools**: Attend workshops (e.g., on model context protocols) to enhance agent capabilities.  

--- 

## Additional Notes  
- **Example use cases**: Coding agents, search agents, and task automation share similar architectures but vary in tools and prompts.  
- **Workshop recommendation**: Attend Mahes’s session on model context protocols for deeper insights.

## Full Transcript

[00:00] [Music]
[00:17] Wow, it's uh incredible to be on the
[00:18] same stage as uh so many people I've
[00:20] learned so much from. Let's get into it.
[00:23] My name is Barry and today we're going
[00:25] to be talking about how we build
[00:26] effective
[00:28] agents. About two months ago, Eric and I
[00:31] wrote a blog post called Building
[00:32] Effective Agents. In there, we shared
[00:35] some opinionated take on what an agent
[00:37] is and isn't, and we give some practical
[00:39] learnings that we have gained along the
[00:41] way. Today, I'd like to go deeper on
[00:44] three core ideas from the blog post and
[00:46] provide you with some personal musings
[00:48] at the
[00:49] end. Here are those
[00:52] ideas. First, don't build agents for
[00:55] everything. Second, keep it simple. And
[00:58] third, think like your
[01:01] agents. Let's first start with a recap
[01:04] of how we got here. Most of us probably
[01:07] started building very simple features.
[01:09] Things like summarization,
[01:10] classification, extraction, just really
[01:13] simple things that felt like magic two
[01:14] to three years ago and have now become
[01:16] table stakes. Then as we got more
[01:19] sophisticated and as products mature, we
[01:22] got more creative. One model call often
[01:24] wasn't enough. So we started
[01:26] orchestrating multiple model calls in
[01:28] predefined control flows. This basically
[01:32] gave us a way to trade off cause and
[01:33] latency for better performance and we
[01:36] call these
[01:37] workflows. We believe this is the
[01:39] beginning of agentic
[01:42] systems. Now models are even more
[01:44] capable and we are seeing more and more
[01:47] domain domain specific agents start to
[01:49] pop up in production. Unlike workflows,
[01:52] agents can decide their own trajectory
[01:54] and operate almost independently based
[01:57] on environment feedback. This is going
[01:59] to be our focus
[02:01] today. It's probably a little bit too
[02:04] early to name what the next phase of
[02:05] agentic system is going to look like,
[02:07] especially in production. Single agents
[02:09] could become a lot more general purpose
[02:11] and more capable or we can start to see
[02:13] collaboration and delegation in multi-
[02:14] aent settings. Regardless, I think the
[02:17] broad trend here is that as we give
[02:20] these systems a lot more agency, they
[02:22] become more useful and more capable. But
[02:24] as a result, the cost, the latency, the
[02:27] consequences of errors also go
[02:29] up. And that brings us to the first
[02:31] point. Don't build agents for
[02:34] everything. Well, why not? We think of
[02:38] agents as a way to scale complex and
[02:40] valuable tasks. They shouldn't be a drop
[02:42] in upgrade for every use case. If uh if
[02:46] you have read the blog post, you'll know
[02:47] that we talked a lot about workflows and
[02:49] that's because we really like them and
[02:51] they're a great concrete way to deliver
[02:53] values
[02:54] today. Well, so when should you build an
[02:57] agent? Here's our
[02:59] checklist. The first thing to consider
[03:01] is the complexity of your task. Agents
[03:04] really thrive in ambiguous problem
[03:06] spaces. And if you can map out the
[03:08] entire decision tree pretty easily, just
[03:11] build that explicitly and then optimize
[03:13] every node of that decision tree, it's a
[03:16] lot more cost- effective and it's going
[03:17] to give you a lot more
[03:19] control. Next thing to consider is the
[03:21] value of your task. That exploration I
[03:23] just mentioned is going to cost you a
[03:25] lot of tokens. So the task really needs
[03:27] to justify the cost. If your budget per
[03:31] task is around 10 cents, for example,
[03:33] you're building a u high volume customer
[03:35] support system, that only affords you 30
[03:38] to 50,000 tokens. In that case, just use
[03:41] a workflow to solve the most common
[03:43] scenarios and you're able to capture the
[03:44] majority of the values from there. On
[03:48] the other hand, though, if you look at
[03:49] this question and your first thought is,
[03:51] I don't care how many tokens I spend. I
[03:53] just want to get the task done. Please
[03:55] see me after the talk. Our go to market
[03:56] team would love to speak with you.
[04:00] From there, we want to derisk the
[04:02] critical capabilities. This is to make
[04:04] sure that there aren't any significant
[04:06] bottlenecks in the agent's trajectory.
[04:09] If you're doing a coding agent, you want
[04:10] to make sure it's able to write good
[04:11] code, it's able to debug, and it's able
[04:13] to recover from its
[04:15] errors. If you do have bottlenecks,
[04:18] that's probably not going to be fatal,
[04:20] but they will multiply your cost and
[04:21] latency. So, in that case, we normally
[04:24] just reduce the scope, simplify the
[04:26] task, and try again.
[04:29] Finally, the the the last important
[04:32] thing to consider is the cost of error
[04:34] and error discovery. If your errors are
[04:37] going to be high stake and very hard to
[04:39] discover, it's going to be very
[04:40] difficult for you to trust the agent to
[04:42] take actions on your behalf and to have
[04:44] more autonomy. You can always mitigate
[04:46] this by limiting the scope, right? You
[04:48] can have read only access. You can have
[04:50] more human in the loop, but this will
[04:53] also limit how well you're able to scale
[04:55] your agent in your use case.
[04:58] Let's see this checklist in in action.
[05:00] Why is coding a great agent use case?
[05:03] First, to go from design doc to a PR is
[05:06] obviously a very ambiguous and very
[05:08] complex task. And second, um we're a lot
[05:11] of us are developers here, so we know
[05:13] that good code has a lot of value. And
[05:16] third, many of us already use cloud for
[05:18] coding. So we know that it's great at
[05:20] many parts of the coding workflow. And
[05:23] last, coding has this really nice
[05:25] property where the output is easily
[05:28] verifiable through unit test and CI. And
[05:31] that's probably why we're seeing so many
[05:33] creative and successful coding agents.
[05:35] Right
[05:38] now, once you find a good use case for
[05:41] agents, this is the second core idea,
[05:44] which is to keep it as simple as
[05:46] possible. Let me show you what I
[05:49] mean. This is what agents look like to
[05:51] us. They're models using tools in a
[05:54] loop. And in this frame, three
[05:57] components define what an agent really
[05:59] looks like. First is the environment.
[06:02] This is a system that the agent is
[06:03] operating
[06:04] in. Then we have a set of tools which
[06:07] offer an interface for the agent to take
[06:09] action and get
[06:11] feedback. Then we have the system prompt
[06:13] which defines the goals, the constraints
[06:15] and the ideal behavior for the agent to
[06:18] actually work in this environment.
[06:20] Then the model gets called in a loop and
[06:24] that's
[06:25] agents. We have learned the hard way to
[06:27] keep this simple because any complexity
[06:29] up front is really going to kill
[06:31] iteration speed. Iterating on just these
[06:34] three basic components is going to give
[06:35] you by far the highest ROI and
[06:37] optimizations can come
[06:41] later. Here are examples of three agent
[06:44] use cases that we have built for
[06:45] ourselves or or our customers just to
[06:47] make it more concrete. They're going to
[06:49] look very different on the product
[06:51] surface. They're going to look very
[06:52] different in their scope. They're going
[06:53] to look different in the capability, but
[06:55] they share almost exactly the same
[06:57] backbone. They they actually share
[07:00] almost the exact same
[07:01] code. The environment largely depends on
[07:04] your use case. So really the only two
[07:06] design decisions is what are the set of
[07:08] tools you want to offer to the agent and
[07:10] what is the prompt that you want to
[07:12] instruct your agent to follow.
[07:16] Um, on this note, if you want to learn
[07:17] more about tools, my friend Mahes is
[07:19] going to be giving a workshop on model
[07:21] context protocol MCP tomorrow morning.
[07:23] Um, I've seen that workshop. It's going
[07:25] to be really fun. So, I highly encourage
[07:26] you guys to to check that out. Um, but
[07:29] back to our talk. Once you have figured
[07:31] out these three basic components, you
[07:33] have a lot of optimizations to do from
[07:34] there. Uh, for coding and computer use,
[07:37] uh, you might want to, uh, catch the
[07:39] trajectory to reduce cost. For search
[07:41] where you have a lot of tool calls, you
[07:43] can parallelize a lot of those to reduce
[07:45] latency. And for almost all of these, we
[07:47] want to make sure to present the agents
[07:49] progress in such a way that gain user
[07:51] trust. But that's it. Keep it as simple
[07:54] as possible as you're iterating. Build
[07:56] these three components first and then
[07:58] optimize once you have the behaviors
[08:03] down. All right, this is the last idea.
[08:06] Um, is to think like your agents. I've
[08:09] seen a lot of builders and myself
[08:11] included who develop agents from our own
[08:13] perspectives and get confused when
[08:16] agents make a mistake. It seems
[08:17] counterintuitive to us. And that's why
[08:20] we always recommend to put yourself in
[08:22] the agents context
[08:24] window. Agents can exhibit some really
[08:27] sophisticated behavior. It could look
[08:28] incredibly complex, but at each step,
[08:32] what the model is doing is still just
[08:33] running inference on a very limited set
[08:35] of contexts.
[08:37] Everything that the model knows about
[08:39] the current state of the world is going
[08:41] to be explained in that 10 to 20k
[08:43] tokens. And it's really helpful to limit
[08:46] ourselves in that context and see if
[08:48] it's actually sufficient and coherent.
[08:51] This will give you a much better
[08:52] understanding of how agents see the
[08:54] world and then kind of bridge the gap
[08:56] between our understanding and
[09:00] theirs. Let's imagine for a second that
[09:02] we're computer use agents now and then
[09:04] see what that feels like. All we're
[09:06] going to get is a static screenshot and
[09:09] a very poorly written description. This
[09:11] is by yours truly. Let's read through
[09:12] it. You know, you're a computer use
[09:14] agent. You have a set of tools and you
[09:16] have a task. Terrible. Uh we can think
[09:19] and talk and reason all we want, but the
[09:22] only thing that's going to take effect
[09:23] in the environment are our
[09:25] tools. So, we attempt a click without
[09:28] really seeing what's happening. And
[09:30] while the inference is happening, while
[09:32] the two execution is happening, this is
[09:34] basically equivalent to us closing our
[09:36] eyes for three to five seconds and using
[09:38] the computer in the dark. Then you open
[09:41] up your eyes and you see another
[09:42] screenshot. Whatever you did could have
[09:44] worked or you could have shut down the
[09:46] computer. You just don't know. This is a
[09:48] huge lethal phase and the cycle kind of
[09:50] starts again. I highly recommend just
[09:53] trying doing a full task from the
[09:56] agent's perspective like this. I promise
[09:58] you it's a fascinating and only mildly
[10:00] uncomfortable
[10:04] experience. However, once you go through
[10:06] that mildly uncomfortable experience, uh
[10:08] I think it becomes very clear what the
[10:10] agents would have actually needed. It's
[10:12] clearly very crucial to know uh what the
[10:14] screen resolution is so I know how to
[10:16] click. Um it's also good to have
[10:19] recommended actions and limitations just
[10:21] so that you know uh we can uh put some
[10:23] guardrails around uh what we should be
[10:25] exploring and we can avoid unnecessary
[10:28] exploration. These are just some
[10:29] examples and you know do this exercise
[10:31] for your own own agent use case and
[10:34] figure out what kind of context do you
[10:35] actually want to provide for the
[10:38] agent. Fortunately though um we are
[10:41] building systems that speak our
[10:42] language. So we could just ask cloud to
[10:44] understand cloud. You can throw in your
[10:47] your system prompt and ask well is any
[10:49] of this instruction ambiguous? Does it
[10:51] make sense to you? Are you able to
[10:52] follow this? You can throw in a two
[10:54] description and see whether the agent
[10:56] knows how to use the tool. You can see
[10:58] if it wants more parameter, fewer
[11:00] parameter. And one thing that we do
[11:02] quite frequently is we throw the entire
[11:04] agent's trajectory into cloud and just
[11:06] ask it, hey, why do you think we made
[11:08] this decision right here? And is there
[11:10] anything that we can do to help you make
[11:12] better decisions?
[11:14] This shouldn't replace your own
[11:16] understanding of the context, but you'll
[11:17] help you gain a much closer perspective
[11:19] on how the agent is seeing the world. So
[11:22] once again, think like your agent as
[11:24] you're
[11:26] iterating. All right. Uh I've I've spent
[11:29] most of the talk about very practical
[11:31] stuff. Uh I'm going to indulge myself
[11:32] and spend one slide on personal musings.
[11:35] This is going to be my view on how this
[11:37] might evolve and some open questions I
[11:39] think we need to answer together as AI
[11:41] engineers.
[11:43] These are the top three things that are
[11:44] always on my mind. First, I think we
[11:47] need to make agents a lot more budget
[11:49] aare. Unlike workflows, we don't really
[11:52] have a great sense of control for the
[11:53] cost and latency for agents. I think
[11:56] figuring this out will enable a lot more
[11:58] use cases as it gives us the necessary
[12:00] control to deploy them in production.
[12:02] The open question is just what's the
[12:04] best way to define and enforce budgets
[12:06] in terms of time, in terms of money, in
[12:08] terms of tokens, the things that we care
[12:10] about.
[12:12] Next up is this concept of self-evolving
[12:14] tools. I've I've already hinted at this
[12:16] two slides ago, but uh we are already
[12:18] using models to help iterate on the two
[12:21] description, but this should generalize
[12:23] pretty well into a meta tool where
[12:25] agents can design and improve their own
[12:27] tool
[12:28] ergonomics. This will make agents a lot
[12:30] more general purpose as they can adopt
[12:32] the tools that they need for each use
[12:36] case. Finally, um I don't even think
[12:38] this is a hot take anymore. I have a
[12:40] personal conviction that we will see a
[12:42] lot more multi- aent uh collaborations
[12:44] in production by the end of this year.
[12:46] They're well parallelized. They have
[12:48] very nice separation of concerns and
[12:50] having sub agent for example will really
[12:53] protect the main agents context
[12:55] window. Um but I think a big open
[12:59] question here is um how how do these
[13:02] agents actually communicate with each
[13:03] other? We're currently in this very
[13:05] rigid frame of having mostly synchronous
[13:08] user assistant terms and I think most of
[13:11] our systems are built around that. So
[13:13] how do we expand from there and build in
[13:14] asynchronous communication and and
[13:16] enable more roles that that afford
[13:18] agents to communicate with each other
[13:20] and recognize each other? I think that's
[13:22] going to be a big open question as we
[13:23] explore this more multi- aent
[13:26] future. These are the areas that take up
[13:28] a lot of my mind space. If you're also
[13:30] thinking about this uh please shoot me a
[13:33] text. I would love to
[13:35] chat. Okay, let's uh bring it all
[13:38] together. If you forget everything I
[13:40] said today, these are the three
[13:41] takeaways. First, don't build agents for
[13:44] everything. If you do find a good use
[13:46] case and want to build an agent, keep it
[13:48] as simple for as long as possible. And
[13:51] finally, as you iterate, try to think
[13:54] like your agent, gain their perspective,
[13:56] and help them do their job.
[14:00] I would love to keep in touch with
[14:01] everyone of you. If you want to chat
[14:03] about agents, especially those open
[14:04] questions that I talked about, uh you'll
[14:06] be incredibly lovely. You can just, you
[14:08] know, uh jam on some of these ideas. Uh
[14:12] these are my socials if you want to get
[14:14] connected. And I'm going to end the
[14:15] presentation on a personal anecdote. So
[14:18] back in 2023, I was building AI product
[14:20] at Meta and we had this funny thing
[14:22] where we could change our job
[14:24] description to anything we want. Um,
[14:26] after reading that blog post from Swix,
[14:28] I decided I was going to be the first AI
[14:30] engineer. Uh, I I really love the focus
[14:33] on practicality and just making AI
[14:35] actually useful to the world. And I
[14:38] think that aspiration brought me here
[14:39] today. So, I hope you enjoy the rest of
[14:42] the AI engineer summit. And in the
[14:44] meantime, let's keep building. Thank
[14:46] you.
[14:51] [Music]
