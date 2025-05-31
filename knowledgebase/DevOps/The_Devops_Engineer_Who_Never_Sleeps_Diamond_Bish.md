---
type: youtube
title: The Devops Engineer Who Never Sleeps — Diamond Bishop, Datadog
author: Channel Video
video_id: VZzUhELgYk4
video_url: https://www.youtube.com/watch?v=VZzUhELgYk4
thumbnail_url: https://img.youtube.com/vi/VZzUhELgYk4/mqdefault.jpg
date_added: 2025-05-26
category: AI and DevOps Integration
tags: ['AI in DevOps', 'incident response', 'DevOps automation', 'error tracking', 'postmortem analysis', 'AI agents', 'software engineering practices', 'tool integration', 'proactive development', 'remediation workflows', 'DevOps workflows', 'automation']
entities: ['DataDog', 'GitHub', 'VS Code', 'recursion issue', 'on-call engineer', 'postmortem', 'DevOps', 'AI agent', 'error tracking', 'remediation']
concepts: ['AI-driven incident response', 'DevOps automation', 'error tracking', 'proactive code fixes', 'incident remediation', 'postmortem analysis', 'AI agent workflows', 'tool integration', 'DevOps practices', 'automation workflows']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of DevOps practices', 'Familiarity with AI/ML concepts', 'Knowledge of incident management workflows']
related_topics: ['AI in DevOps', 'Incident response automation', 'Continuous integration/continuous deployment (CI/CD)', 'Error monitoring systems', 'DevOps toolchains', 'Machine learning for software engineering', 'Postmortem analysis techniques', 'Automated remediation systems']
authority_signals: ["We've learned quite a lot um there's a lot of things that we started with that we kind of went back and and redid", 'Our agent works to put together hypothesis on what might be happening and reason over them', 'We can tie directly into them and make it so that our agent can understand those workflows']
confidence_score: 0.85
---

# The Devops Engineer Who Never Sleeps — Diamond Bishop, Datadog

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=VZzUhELgYk4)  
**Published**: 1 month ago  
**Category**: DevOps  
**Tags**: devops, ai, machine-learning, datadog, ai-agents, observability, cloud-computing  

## Summary

# Summary of "The Devops Engineer Who Never Sleeps — Diamond Bishop, Datadog"

## Overview  
Diamond Bishop from Datadog discusses the development of AI agents designed to automate and enhance DevOps workflows. The talk highlights Datadog’s focus on observability, security, and AI-driven automation, with a focus on two key agents: the **AI On-Call Engineer** (handling alerts and incident responses) and the **AI Software Engineer** (proactively analyzing errors and proposing code fixes). The presentation emphasizes human-AI collaboration, iterative development, and the challenges of scaling AI in complex systems.

---

## Key Points  
- **Datadog’s Role**: A platform for observability and security, enabling real-time monitoring of infrastructure, applications, and user experiences.  
- **Shift to AI Agents**: Datadog is building AI tools to automate repetitive tasks, reduce human workload, and improve incident response.  
- **AI On-Call Engineer**:  
  - Handles alerts by analyzing root causes, suggesting remediations, and automating postmortems.  
  - Collaborates with humans, allowing verification of actions and learning from decisions.  
  - Example: Identifies a recursion issue, proposes a fix, and creates a test to prevent future recurrence.  
- **AI Software Engineer**:  
  - Proactively tracks errors, identifies causes, and suggests code fixes.  
  - Reduces on-call incidents by addressing issues before they escalate.  
  - Integrates with tools like GitHub and VS Code for code changes.  
- **Human-AI Collaboration**:  
  - Agents act as junior engineers, providing transparency (e.g., showing hypotheses, steps taken, and reasoning).  
  - Enables trust-building through explainability and iterative refinement.  
- **Challenges**:  
  - Scoping tasks to avoid token limits and ensure efficiency.  
  - Integrating with existing workflows and scaling AI capabilities.  

---

## Important Quotes  
- *"The future is uncertain... the dawning of this intelligence age."*  
- *"Our agent works to put together hypotheses... validate or invalidate each hypothesis."*  
- *"It also tells you things like what steps did it actually take out of your runbook... much like a human devops engineer."*  

---

## Actionable Items  
1. **Develop AI Agents**: Focus on automation for incident response, error tracking, and workflow optimization.  
2. **Prioritize Evaluation**: Ensure AI outputs are verifiable and align with human oversight.  
3. **Enhance Collaboration**: Design tools for seamless human-AI interaction, including explainability and feedback loops.  
4. **Integrate with Workflows**: Connect AI agents to existing systems (e.g., GitHub, runbooks) for real-world impact.  
5. **Iterative Refinement**: Continuously improve agents based on feedback, avoiding over-scoping and token limits.  

---

**Note**: The transcript appears to be cut off, with a final note about "Limiting to avoid token limits," suggesting some content may be incomplete. This summary is based on the provided text.

## Full Transcript

[00:00] [Music]
[00:17] hey I'm Diamond I hope everyone's you
[00:19] know feeling the AGI today um I'll be
[00:22] sharing our AI agents at data dog and
[00:24] what we've learned building the devops
[00:25] engineer who never sleeps I came all the
[00:28] way from the New York Times building uh
[00:29] right across here uh to see all of you
[00:32] so I hope it's worth
[00:33] it I've been working for my entire
[00:36] career about 15 years or so in AI trying
[00:39] to build more AI friends and co-workers
[00:42] um I wouldn't read too much into that I
[00:43] have human ones too um I promise um
[00:47] throughout the kind of AI Winters and
[00:48] lws of the last 15 years or so I've
[00:51] managed to keep doing just that at
[00:53] Microsoft
[00:54] Cortana um building out Alexa at Amazon
[00:57] working on pytorch at meta and building
[01:00] my own AI startup that was working on a
[01:02] devops assistant now at data dog we're
[01:04] building out bits AI which is the AI
[01:06] assistant who's there to help all of you
[01:08] with your devops
[01:10] problems so today I'll little I'll talk
[01:12] a little about that talk a little about
[01:13] the history of AI at data dog a little
[01:16] bit about how we think about AI agents
[01:18] today and where we think things are
[01:20] going for the
[01:22] future day dog is the observability and
[01:25] security platform for cloud applications
[01:28] there's a lot that we do um um but it
[01:30] kind of all boils down to being able to
[01:32] observe what's happening in your system
[01:34] and take action on that make it easier
[01:36] to understand make it easier for us to
[01:40] uh simply understand and build out
[01:42] things to have a safer and more devops
[01:45] friendly
[01:46] system we've been shipping AI for quite
[01:49] a while actually um it's not always
[01:51] inyour face it's not always out there
[01:53] saying here's a big AI product but
[01:56] things like proactive alerting really
[01:58] understanding things like r analysis
[02:01] impact analysis and change tracking and
[02:03] much more has been happening since 2015
[02:05] or
[02:06] so but things are changing this is a
[02:09] clear era shift I think of this kind of
[02:12] similar terms to the microprocessor or
[02:14] the shift to SAS um bigger smarter
[02:17] models reasoning and multimodal coming
[02:20] uh Foundation model Wars happening this
[02:22] General shift where intelligence becomes
[02:24] too Shi too cheap to
[02:26] meter and what this means is product
[02:30] like cursor are growing you know
[02:31] terribly fast um and really people are
[02:35] expecting more and more from AI every
[02:36] day um with these advancements at data
[02:39] dog we're really trying to rise to meet
[02:41] this shift as well the future is
[02:43] uncertain this kind of ambiguity creates
[02:45] opportunity but there's a lot of
[02:48] potential for us that's kind of the
[02:50] dawning of this intelligence age we're
[02:53] working to move up the stack to leverage
[02:54] these advancements and give even more to
[02:56] our customers by making it so that you
[02:58] don't use data dog as just just the
[03:00] devop platform but also as AI agents
[03:04] that use that platform for you this
[03:06] requires work in a few key areas that
[03:08] I'll talk about developing the actual
[03:10] agents doing eval you just heard a lot
[03:13] about eval we think about that every day
[03:15] for better or worse um and building out
[03:17] new types of
[03:20] observability there's a few agents that
[03:22] we're working on right now in private
[03:23] beta the first is the AI software
[03:25] engineer this kind of looks at problems
[03:28] for you looks at errors tries to
[03:29] recommend code uh that we can generate
[03:31] to help you improve your system the
[03:34] second is the AI on call engineer this
[03:36] wakes up for you in the middle of the
[03:37] night does your work hopefully makes it
[03:39] so you have to get page less frequently
[03:41] and then we have a lot more on the
[03:44] way so I'm going to talk a little bit
[03:46] about the AI on call engineer first this
[03:48] is the one that you know everyone wants
[03:50] to save them from that 2 am. alert you
[03:53] don't want to have to wake up in the
[03:54] middle of the night go and look through
[03:56] your run book go and figure out what's
[03:57] going on if you can help it our on call
[04:00] engineer is there to really make it so
[04:02] you can keep sleeping this agent
[04:04] proactively kicks off when an alert
[04:05] occurs and works to First situationally
[04:07] Orient read things like your run books
[04:10] grab context of the alert and then goes
[04:13] and you know figures out the kind of
[04:14] common stuff that each of you would do
[04:16] on data dog already look through logs
[04:18] look through metrics look through traces
[04:20] and kind of act in this Loop to figure
[04:21] out what's going
[04:24] on the en call agent's great for both
[04:26] automatically running investigations for
[04:28] me but also you know being able to look
[04:31] through and find summaries and find
[04:32] information for me before I even get to
[04:34] my computer so if I want to get insights
[04:37] into why an alert just occurred or
[04:39] figure out why a trace might uh be
[04:40] showing an error this agent can jump
[04:43] ahead pull information for me and show
[04:44] it to me we also have added a new page
[04:47] that makes it easy so that you can have
[04:49] human AI collaboration this is still
[04:51] something I'm thinking about a lot is
[04:53] like what what kind of collaboration do
[04:54] we expect we want our agents to act as
[04:56] humans but we also need to be able to
[04:58] verify what they did and be able to kind
[05:00] of look over what they're doing and
[05:02] really learn from
[05:03] it it also helps you to kind of earn
[05:05] trust along the way I can see the reason
[05:08] why uh this hypothesis for example was
[05:11] generated I can see what the agent found
[05:14] and I can make decisions about whether
[05:15] or not I agree along the
[05:18] way it also tells you things like what
[05:21] steps did it actually take out of your
[05:22] runbook and kind of like a junior
[05:24] engineer who does this work I can go ask
[05:26] follow-up questions find out why I did a
[05:27] certain thing
[05:30] a little more insight into how we're
[05:31] making this happen much like a human s
[05:33] or devops engineer our agent Works to
[05:36] put together hypothesis on what might be
[05:38] happening and reason over them coming up
[05:40] with ways to test them use tools in the
[05:42] tool former sense to try out ideas run
[05:45] queries against logs metrics Etc and
[05:47] work to validate or invalidate each
[05:51] hypothesis in the case that it does find
[05:53] a solid root cause our agent cause uh
[05:55] can suggest remediations along the way
[05:58] again just like a human might might say
[06:00] hey we should page in that other team
[06:01] that's involved here or it might offer
[06:03] to scale up or down your infrastructure
[06:05] over time we plan to add more built-in
[06:07] actions and eventually discover new
[06:09] types of workflows based on what your
[06:10] team has
[06:11] done but if you already have certain
[06:14] workflows that you set up in data dog um
[06:16] we can tie directly into them and make
[06:18] it so that our agent can understand
[06:20] those workflows and how they might map
[06:21] to helping you remediate a
[06:25] problem and if it's a real incident the
[06:27] enal engineer is not usually done once
[06:29] an issue is remediated you usually go
[06:31] and write a postmortem you go try to
[06:33] learn from it you share it with your
[06:34] team our agent can do the same write out
[06:37] your postmortem for you look at what
[06:38] occurred during the entire time what it
[06:40] did what humans did and put that
[06:42] together so that you have something
[06:43] ready in the
[06:45] morning so that was the en call engineer
[06:48] um that's the one that is you know
[06:50] trying to help you in the middle of the
[06:51] night trying to help you every time
[06:52] alerts come on um we also have this AI
[06:55] software engineer I think of this as the
[06:57] proactive developer the devops or
[07:00] software engineering agent who observes
[07:02] and acts on things like errors coming
[07:04] through this is kind of the error
[07:05] tracking assistant it automatically
[07:07] analyzes these errors identifies causes
[07:10] and proposes Solutions those Solutions
[07:12] can include generating a code fix and
[07:14] working to reduce the number of on call
[07:16] incidents you have in the first place so
[07:18] they can work in concer to make a better
[07:19] system over time in this case the
[07:22] assistant has caught a recursion issue
[07:25] proposes a
[07:26] fix and even creates a recursion test so
[07:29] that we can catch it if it happens again
[07:30] in the future we have the option to
[07:33] create a PR in GitHub or open the diff
[07:35] in vs code for editing this workflow
[07:38] significantly reduces the time spent by
[07:39] an engineer manually writing and testing
[07:41] code and greatly reduces human time
[07:43] spent
[07:45] overall so what have we learned building
[07:48] out these agents and some of the new
[07:49] ones that we're working on today well
[07:51] we've learned quite a lot um there's a
[07:53] lot of things that we started with that
[07:54] we kind of went back and and redid um
[07:57] but a few areas I'll touch on that I
[07:58] hope help you if you develop your own
[08:01] first is scoping tasks for evaluation
[08:03] it's very easy you know to build out
[08:05] demos quickly much harder sometimes to
[08:07] scope and eval what's occurring second
[08:09] is building the right team who's ready
[08:11] to move fast and deal with the ambiguity
[08:13] that comes with these kind of problems
[08:15] third is that you know the ux of old is
[08:17] changing um that's something that
[08:19] everyone needs to be comfortable with
[08:21] and fourth is observability matters you
[08:23] know uh I'm surprising for data do to
[08:26] say that I'm sure but observability is
[08:28] terribly important even in this new era
[08:31] so scoping the problems scoping the work
[08:33] to be done I like to think about this as
[08:36] defining jobs to be done and really kind
[08:38] of trying to clearly understand step by
[08:41] step what you'd like to do think about
[08:43] it from the human angle first and think
[08:44] about how another human might go and
[08:46] evaluate it um this is why we build out
[08:48] vertical task specific agents rather
[08:50] than building out generalized agents we
[08:52] also want where possible this to be
[08:54] measurable and verifiable and at each
[08:56] step this has honestly been one of the
[08:58] biggest pain points for for us and I
[08:59] think this is true for many people
[09:01] working in agents where you can quickly
[09:02] build out a demo you can quickly build
[09:04] something that looks like it works but
[09:06] then it's very hard to actually verify
[09:07] that over time and improve it um use
[09:10] your domain experts but use them more
[09:12] like design Partners or task verifiers
[09:14] don't use them as the people who will go
[09:16] and kind of write the code or rules for
[09:17] it because there is a big difference in
[09:19] how these kind of stochastic models work
[09:21] versus how experts work you know
[09:24] everyone kind of knows gnome and his uh
[09:25] anti- NLP um rants but that kind of
[09:29] stuff happens pretty frequently domain
[09:31] experts eval eval eval I can't stress
[09:35] this enough um start by thinking deeply
[09:37] about your eval the number of mistakes
[09:39] we made by not thinking about eval first
[09:41] is uh frustrating and something that I
[09:43] think everyone should think about it's
[09:45] very easy to build these demos as I said
[09:48] um but everything in this fuzzy
[09:49] stochastic World requires good evil even
[09:52] something small to start this means
[09:54] offline online and kind of living Evo
[09:57] have endtoend uh uh uh task have
[10:00] endtoend measurements uh make it so you
[10:03] also instrument appropriately the way to
[10:05] know if humans are using your product
[10:06] right and giving you feedback and then
[10:08] make this a living breathing test
[10:11] set building the team um you don't have
[10:15] to have a bunch of ml experts there
[10:16] aren't that many to go around right now
[10:18] um what you really need is you want to
[10:20] seat it with one or two and then have a
[10:21] bunch of optimistic generalists who are
[10:23] very good at writing code and very
[10:25] willing to try things out fast um I'll
[10:28] also note that ux in front end matters
[10:30] more than I'd like as a backend engineer
[10:31] myself um but it's terribly important as
[10:33] you collaborate with these with these
[10:35] agents and
[10:36] assistants um and then you want
[10:38] teammates and people who are excited to
[10:41] be AI augmented themselves this is
[10:43] day-to-day AI use this is Explorer types
[10:45] who want to learn this is a field that's
[10:47] changing fast um and if you don't have
[10:49] people like that you're going to kind of
[10:51] get
[10:51] stuck you want folks who kind of you
[10:54] know yeah yearn for the vast and endless
[10:55] AI capabilities right um it's a big
[10:58] world out there and there's a lot going
[11:00] on Ye Old ux um this is one of those
[11:04] things that I still you know we think
[11:06] about we go back and forth every day um
[11:09] it's an area that I didn't realize was
[11:10] quite so important initially when I
[11:11] started working in this field um despite
[11:14] my engineering sensibilities and lack of
[11:15] ux is terribly important um this is such
[11:18] an early space of work this is kind of
[11:20] one of the more important things here as
[11:22] you collaborate and work together but
[11:24] the old ux patterns are changing be
[11:25] comfortable with that um and so far I'm
[11:28] partial to agents that work more and
[11:29] more like human teammates instead of
[11:31] building out a bunch of new pages or
[11:34] buttons so who watches the Watchmen
[11:36] right um You have these agents running
[11:38] around um observability is actually
[11:41] really important and don't make it an
[11:42] afterthought um these are complex
[11:44] workflows you really need situational
[11:46] awareness to debug problems and this has
[11:48] saved us time a lot as we start to work
[11:50] with um a new view that we're calling LM
[11:52] observability in the data dog
[11:54] product um Daya dog in general has a
[11:57] full observability stack as many of you
[11:59] know know we can look at gpus um we can
[12:01] look at llm monitoring we can look at
[12:03] really your system end to end but tying
[12:05] in the llm observability has been very
[12:07] helpful because you have a wide variety
[12:10] of interactions and calls out to models
[12:12] you're hosting models you're running
[12:13] maybe models you're using through an API
[12:15] and we can make them all uh kind of
[12:17] group together in the same paint of
[12:18] glass so you can look at them and debug
[12:20] what's
[12:22] occurring I will note though that this
[12:26] can get messy fast with agents our agent
[12:28] for example has very complex multi-step
[12:31] calls you're not going to look at this
[12:32] and figure out what's going on right
[12:33] away Um this can be hundreds of calls
[12:35] this can be uh you know uh tons of
[12:38] different places where it's making
[12:39] decisions about tools looping time and
[12:41] time again and if you just look through
[12:42] a full list of these things you'll never
[12:44] really figure out what's going on so
[12:46] here's a quick you know sneak peek into
[12:48] a more agent view of what's occurring
[12:50] inside of our observability tools this
[12:52] is our agent graph um really what this
[12:54] means is that I can kind of look at it
[12:56] just like our agent did and looking at
[12:57] workflows that are occurring you can see
[12:59] in this even though it's a big graph uh
[13:01] there's a bright red node here if we
[13:03] zoom into that we can actually see where
[13:05] errors were occurring this is very human
[13:07] readable something that makes it super
[13:08] easy to figure out what's going on when
[13:11] your complex workflow is
[13:14] running as an as side though I do also
[13:16] want to note what I think of as kind of
[13:18] like the agent or application layer
[13:19] bitter lesson uh General methods that
[13:21] can leverage new off the shelf models
[13:23] are ultimately the most effective um by
[13:26] a large margin um I hate to say it but
[13:29] like you sit there you fine-tune you do
[13:31] all this work on like the specific uh
[13:33] you know project the specific task and
[13:35] then all of a sudden you know open AI or
[13:37] someone comes out with a new model and
[13:38] it handles all this you know kind of
[13:40] quickly a lot of the reasoning is solved
[13:42] for you um we're not quite there where
[13:43] it handles all of it very quickly but
[13:45] you should be at a point where you can
[13:46] easily try out any of these models um
[13:49] and don't feel stuck to a particular
[13:50] model that you're you've been working on
[13:52] for a while you know Rising tide lifts
[13:54] all boat here
[13:59] um I also think a lot about not just
[14:01] building agents but what it might mean
[14:03] for other agents to be users of data dog
[14:05] and other SAS products um there's a good
[14:07] chance that agents surpass humans as
[14:09] users in the next five years um I'm
[14:11] probably somewhere in the middle on my
[14:12] estimate there you know there are people
[14:14] who will tell you that'll happen in the
[14:15] next year the'll people who will tell
[14:16] you you know it'll happen in 10 years I
[14:18] think we're somewhere around the
[14:19] fiveyear Mark um but this means that you
[14:21] shouldn't just be building for humans or
[14:23] building your own agents you should
[14:25] really think about agents that might use
[14:27] your product as well an example of the
[14:29] is like third party agents like Claude
[14:30] might use you know data dog directly I
[14:32] set this up with mCP relatively quickly
[14:35] um but any type of agent that might be
[14:37] coming in and using your platform you
[14:38] should think of the context you want to
[14:40] provide them the information you want to
[14:42] provide about your apis that agents
[14:43] would use more than
[14:46] humans so looking ahead um the future is
[14:50] going to be weird it'll be fun uh and AI
[14:53] accelerating is accelerating each and
[14:54] every day I strongly believe that we'll
[14:56] be able to offer a team of Dev SEC op
[14:58] agents AG For Hire to each of you soon
[15:01] you don't have to go and use our
[15:02] platform directly and integrate directly
[15:04] ideally our agents will do that for you
[15:06] and our agents will handle your on call
[15:07] and everything like that for you um I
[15:10] also do think that AI agents will be
[15:12] customers many of you building out SRE
[15:13] agents and other types of Agents coding
[15:15] agents should use our platform should
[15:17] use our tools um just like a human would
[15:20] and uh we can't wait to see
[15:22] that and generally I think that small
[15:25] companies out there are going to be
[15:26] building built by someone who can use
[15:28] autom developers like cursor or Devon to
[15:31] get their ideas out into the real world
[15:32] and then agents like ours to handle
[15:34] operations and Security in a way that
[15:36] lets you know in order of magnitude more
[15:38] ideas make it out into the real
[15:41] world thank you so much um please reach
[15:43] out if you're building any agents that
[15:45] want to use us um or if you'd like to
[15:46] check out our agents as well um there's
[15:48] a lot to build here and if you want to
[15:51] work in the space we are hiring more AI
[15:53] engineers and people who are just
[15:55] excited about it but thank you very much
[16:04] [Music]
