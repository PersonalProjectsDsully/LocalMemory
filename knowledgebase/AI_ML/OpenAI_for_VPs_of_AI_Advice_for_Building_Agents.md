---
type: youtube
title: OpenAI for VP's of AI + Advice for Building Agents
author: AI Engineer
video_id: joHR2pmxDQE
video_url: https://www.youtube.com/watch?v=joHR2pmxDQE
thumbnail_url: https://img.youtube.com/vi/joHR2pmxDQE/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence
tags: ['AI partnership', 'enterprise AI', 'use case development', 'RAG', 'fine-tuning', 'AB testing', 'deployment', 'maintenance', 'roadmap alignment', 'knowledge assistant', 'OpenAI collaboration', 'iterative development']
entities: ['Morgan Stanley', 'OpenAI', 'Brant', 'New York', 'knowledge assistant', 'RAG', 'fine-tuning', 'AB testing', 'roadmap sessions']
concepts: ['use case development', 'iterative development', 'accuracy improvement', 'partnership frameworks', 'testing and evaluation', 'deployment strategies', 'maintenance processes', 'early access to models', 'roadmap alignment']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Experience with OpenAI tools', 'Familiarity with software development lifecycle', 'Knowledge of testing methodologies', 'Collaboration frameworks']
related_topics: ['AI development processes', 'Enterprise AI solutions', 'NLP techniques', 'Collaborative AI partnerships', 'AI deployment strategies', 'Testing in AI systems', 'Roadmap planning in tech', 'Knowledge management systems']
authority_signals: ['we bring a dedicated team', 'our team like Brant myself', 'internal experts from our research engineering team', 'joint roadmap sessions to ensure alignment']
confidence_score: 0.8
---

# OpenAI for VP's of AI + Advice for Building Agents

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=joHR2pmxDQE)  
**Published**: 2 months ago  
**Category**: AI/ML  
**Tags**: openai, ai agents, enterprise ai, ml models, ai deployment, enterprise solutions, ai strategies  

## Summary

# Summary of "OpenAI for VP's of AI + Advice for Building Agents"

## Overview  
This video outlines OpenAI's role in enterprise AI strategies, focusing on the partnership process, three-phase customer journey, and practical examples like Morgan Stanley's internal knowledge assistant. It emphasizes collaboration, development phases, and the importance of aligning AI initiatives with business goals.

---

## Key Points  

### **1. OpenAI's Structure and Partnership**  
- **Two Core Teams**:  
  - **Research Team**: Focuses on model development and innovation.  
  - **Product/Engineering Team**: Translates research into enterprise solutions.  
- **Collaboration Model**:  
  - Dedicated teams from OpenAI and the client work together.  
  - Includes workshops, office hours, paired programming, and joint roadmap sessions.  
  - Early access to models and features (e.g., 2-quarter road map visibility).  

### **2. Enterprise AI Customer Journey (3 Phases)**  
1. **AI-Enabled Workforce**:  
   - Equip employees with AI tools (e.g., internal knowledge assistants).  
   - Example: Morgan Stanley’s wealth managers using AI for accurate client responses.  
2. **Automate Operations**:  
   - Streamline workflows with AI-driven solutions (e.g., data analysis, customer support).  
3. **Infuse AI into Products**:  
   - Embed AI capabilities into customer-facing tools or services.  

### **3. Development Process**  
- **Phases**:  
  1. **Ideation & Scoping**: Define success metrics, architecture, and KPIs.  
  2. **Development**: Iterate on prompting strategies, RAG (Retrieval-Augmented Generation), and fine-tuning.  
  3. **Testing & Evaluation**: AB testing, beta rollouts, and performance validation.  
  4. **Production**: Scale optimization and maintenance.  
- **Key Tools**:  
  - Hybrid retrieval, chunking strategies, and model fine-tuning.  

### **4. Case Study: Morgan Stanley**  
- **Challenge**: 45% accuracy in answering wealth manager queries.  
- **Solutions**:  
  - Implemented RAG, fine-tuning, and chunking strategies.  
  - Improved accuracy through iterative development.  

---

## Important Quotes  
- *"The bulk of the time... is spent in development, iterating on prompting strategies or RAG."*  
- *"Early access to models and features is critical to building for what's coming next."*  
- *"Start with a top-down business strategy, not just a technical one."*  

---

## Actionable Takeaways  
1. **Align AI with Business Goals**: Start with a clear business strategy, not just technical feasibility.  
2. **Prioritize High-Impact Use Cases**: Focus on projects with measurable KPIs and quick wins.  
3. **Build Internal Capabilities**: Invest in teams for model development, RAG, and fine-tuning.  
4. **Leverage OpenAI Partnerships**: Engage early for access to models, expertise, and roadmap insights.  
5. **Iterate and Test**: Use AB testing and beta rollouts to refine AI solutions before full deployment.  

--- 

This summary captures the core strategies, processes, and insights shared in the video, emphasizing collaboration, iterative development, and alignment with business objectives.

## Full Transcript

[00:00] [Music]
[00:13] [Music]
[00:16] hello uh thanks for having us here and
[00:18] today we're going to talk a bit about
[00:20] building and scaling use cases with open
[00:22] Ai and what this means in terms of
[00:24] Enterprises working with open to bring
[00:27] use cases to production and a little
[00:29] sneak peek into to agents and how we've
[00:31] seen some of our experience building
[00:33] these use cases in now agentic workflows
[00:35] uh in the field so uh on our side um
[00:40] just a quick introduction into openai
[00:42] I'm sure folks have probably heard of
[00:44] open AI but just in terms of how we
[00:45] operate we have two core engineering
[00:48] teams we have our research team which is
[00:50] 1,200 researchers that are inventing
[00:52] these models right we they build and
[00:55] deploy these foundational models these
[00:57] kind of come down from the heavens are
[00:59] apply team
[01:00] our second engineering team take this
[01:02] and build it into product so this is
[01:03] where you see things like Chad GPT you
[01:05] see things like the API where GPT models
[01:07] are available and that's where we
[01:09] actually deploy this finally in the go
[01:11] to market sense where we take these
[01:13] products and put it in end user hands
[01:14] that's kind of where our team comes into
[01:16] play with go to market where we actually
[01:19] help get this in the hands of your
[01:21] Workforce in the hands of your product
[01:22] and really start to automate these
[01:24] internal operations and once we finally
[01:27] deploy these there's kind of this
[01:28] iterative Loop where we take feedback
[01:30] from the field to improve our product
[01:34] directly and then also improve our core
[01:36] models through this research flywheel so
[01:38] that's kind of the last step of getting
[01:39] it back to research so this is typically
[01:41] how open AI operates um in terms of the
[01:45] enterprise we see the kind of AI
[01:47] customer Journey happen typically in
[01:49] three phases it doesn't have to happen
[01:51] in sequence in this way but this is what
[01:52] we usually see is first and foremost
[01:54] building an AI enabled Workforce this is
[01:56] getting AI in the hands of your
[01:59] employees to become AI literate to use
[02:02] AI every day in their day-to-day work
[02:04] that's the first and foremost that first
[02:06] step typically that we see then from
[02:08] there you typically graduate to towards
[02:11] automating your AI operations this is
[02:14] actually more of internal use cases to
[02:16] building automation or maybe some
[02:17] co-pilot type use cases into the
[02:19] workforce then the last step here is
[02:22] actually infusing AI into end product
[02:24] this is end user facing so when it comes
[02:27] to open a eyes product specifically
[02:30] enabling your Workforce typically starts
[02:31] with something like chat GPT so this is
[02:33] our you know first party product to put
[02:34] in the hands of users to use day in and
[02:36] day out then when you talk about
[02:38] automating operations internally you can
[02:40] do this partially with chat gbt for the
[02:42] more complex use cases or more more
[02:44] customization is needed that's where
[02:46] something like the API comes in and then
[02:48] finally infusing this into your end user
[02:51] products is where it's primarily API use
[02:53] cases but just to give a flavor of how
[02:55] these products come into play when
[02:57] actually executing this across your AI
[03:00] customer
[03:01] Journey so in terms of how we see
[03:05] Enterprises actually craft this strategy
[03:07] in practice it kind of happens in a few
[03:08] different ways I'd say first and
[03:10] foremost you determine a little bit from
[03:13] the top down level of what should the
[03:14] strategy be and one core thing that we
[03:17] acknowledge here it's not actually
[03:18] what's your AI strategy it's actually
[03:20] what's your broader business strategy
[03:22] and what open AI does is help figure out
[03:23] where does a technology meet that
[03:25] broader business strategy first and
[03:27] foremost so that kind of top down Str
[03:29] iic guidance is really important to
[03:31] start with and then once you start with
[03:33] that top down guidance you then move to
[03:36] use cases like let's identify one or two
[03:39] mey use cases that are high impact to
[03:41] start with and scope those out to really
[03:43] just deliver on um kind of that scoped
[03:46] scale so once you have the strategy you
[03:48] execute upon those two use one to two
[03:50] use cases and then you think about how
[03:52] to build divisional capability across
[03:54] your Enterprise this is where you start
[03:55] to enable the team and to fuse AI
[03:58] throughout the organization and this
[03:59] happens in many ways this comes through
[04:01] enablement this comes through building
[04:03] centers of excellence this comes with
[04:05] building maybe a centralized
[04:06] technological platform that other people
[04:08] in the Enterprise can build on and I
[04:10] feel like that's typically the journey
[04:11] we see is again set the strategy pick
[04:14] those one to two use cases and then
[04:16] build that capability across your
[04:18] organization through enablement so
[04:20] that's usually the the type of Journey
[04:22] we see and just to illustrate this a
[04:24] little bit with an
[04:25] example is this is how we've seen the
[04:28] use case Journey play out so um this is
[04:31] illustrative of a three-month type of
[04:33] example of a use case but when you've
[04:35] identified that one to two use cases
[04:38] that you want to tackle first and
[04:40] foremost you have to ideate upon that do
[04:42] some initial scoping do some
[04:44] architecture review to understand how
[04:46] does AI going to fit into your current
[04:48] stack and then really clearly Define
[04:50] what the success metrics and kpis are
[04:52] once you have that established the bulk
[04:53] of the time is really spent in
[04:55] development this is where you iterate
[04:56] this is where you are iterating
[04:58] prompting strategies in orating rag
[05:00] whatever it may be to constantly improve
[05:04] the uh use case that you're tackling
[05:06] when it comes to engaging with open a
[05:07] this is where our team like Brant myself
[05:10] really interact closely with your
[05:12] engineering team through things like
[05:13] workshops things like office hours
[05:15] paired programming sessions webinars
[05:17] whatever it kind of takes to accelerate
[05:19] the use case forward once we do that
[05:22] development phase we kind of move to
[05:24] testing and evaluation which is with the
[05:27] evals we've typically defined upfront
[05:29] where able to actually now do some AB
[05:31] testing do some beta roll out to
[05:33] understand how this actually works at
[05:35] practice and then finally we go to
[05:37] production this is where you just do
[05:38] some launch roll out do some uh scale
[05:40] optimization testing to make sure it's
[05:42] going to work once you deploy it to many
[05:43] end users and then we have kind of
[05:45] constant maintenance that that's ongoing
[05:47] so that's like the typical phase you'll
[05:48] see and again the bulk of the time
[05:50] especially in partnership with openi
[05:51] will be around development um in this we
[05:55] bring a dedicated team we ask you bring
[05:57] us also a dedicated team to make this
[05:59] work in practice and the things that we
[06:02] deploy also to enable you are things
[06:05] like early access to do models and
[06:06] features that's one of the key things of
[06:08] working closely with open AI is that we
[06:11] can see a little bit into the future not
[06:13] much like our road map I I don't see
[06:15] beyond much maybe like six months people
[06:17] ask what's your 18-month road map I
[06:18] cannot tell you I can tell you basically
[06:20] what's going to happen the next two
[06:21] quarters but that like purview into the
[06:24] future is really important to bring
[06:25] forward to these use cases and enable
[06:28] customers to build and innovate for
[06:31] what's coming next so that's a really
[06:32] critical part of our partnership um also
[06:35] we bring in you know internal experts
[06:36] from our research engineering team our
[06:38] product team to help kind of accelerate
[06:40] you on this path and then lastly just
[06:42] kind of do joint roadmap sessions to
[06:44] make sure that we're on track for what
[06:45] your future road map is as well so
[06:47] that's hopefully an illustration of how
[06:49] we partner together and then one
[06:51] concrete example on this is something we
[06:54] did with Morgan Stanley so Morgan
[06:55] Stanley here based in New York uh was
[06:58] building a internal knowledge assistant
[07:00] so what this was was giving their wealth
[07:02] managers the ability to ask questions of
[07:05] their large corp Corpus of uh knowledge
[07:08] which was research reports like live
[07:10] views on stock ticker data whatever it
[07:13] may be and they wanted to get highly
[07:15] accurate information back to be able to
[07:17] respond to their and clients right and
[07:19] accuracy was pretty bad to start right
[07:21] it was 45% typically what they saw so
[07:23] interacting with us we introduced new
[07:25] methods throughout the use case
[07:26] development things like hide retrieval
[07:28] we did some fine tune and vings
[07:29] different chunking strategies which
[07:31] improved performance and then once we
[07:33] kept introducing more and more methods
[07:34] we saw accuracy go up we introduced
[07:36] things like reranking and classification
[07:38] step that got it 85% and ultimately
[07:40] their goal was 90% we got to 98%
[07:42] accuracy through other things like
[07:44] prompt engineering query expansion so
[07:46] more just an example of how we
[07:48] introduced methods throughout this use
[07:50] case journey to uh improve their core
[07:52] metric for more conly in this case um so
[07:54] this is hopefully one illustration of
[07:57] how open eyes partner with customers and
[07:59] one common use case we're seeing more
[08:00] and more of is now building in this
[08:02] agent space you maybe hear that 2025 is
[08:04] the year of Agents agentic workflows has
[08:07] been a buzzword for a long time I think
[08:08] we're seeing that actually come to
[08:10] reality this year and um I think with
[08:12] that we've seen uh some B we have some
[08:14] Battle Scars and some best practices of
[08:16] what we've seen in the field and I'll
[08:17] hand it off to pant to talk about what
[08:19] we've seen on the agent side thanks
[08:22] DOI so at open ey we were lucky to work
[08:26] alongside customers who are building
[08:27] state-of-the-art agents and and working
[08:30] alongside team members who are building
[08:32] our own agentic products like deep
[08:34] research and operator like Doki said we
[08:37] expect 2025 to be the year of Agents the
[08:41] year gen gen truly graduates from being
[08:43] an assistant to being a
[08:45] cobark and to help usher in this era
[08:48] we've been hard at work identifying the
[08:51] patterns and anti-patterns prevalent in
[08:52] agent development I'm excited to share
[08:55] four of those with you
[08:57] today before we can go further further
[09:00] I'd like to quickly Define uh what we
[09:02] mean by the term agent so we think of an
[09:04] agent as an AI application that consists
[09:06] of a model that has some instructions
[09:09] usually in the form of a prompt access
[09:11] to some tools for retrieving information
[09:13] and interacting with external systems
[09:16] all encapsulated in in an execution Loop
[09:19] whose termination is controlled by the
[09:20] model
[09:21] itself so one way of thinking about this
[09:24] is that in each execution cycle the
[09:26] agent can be thought of as an entity
[09:28] that's receiving instructions natural
[09:29] language determining whether or not to
[09:31] issue any tool calls running those tools
[09:34] synthesizing a response with the tool
[09:37] return values and then providing an
[09:39] answer to the user Additionally the user
[09:42] may determine sorry the agent May
[09:43] determine that it's met its objective
[09:45] and therefore terminate the execution
[09:47] Loop so with that definition let's move
[09:50] on to some of the lessons that we've
[09:52] learned uh building these agents in the
[09:55] field so for the first Insight imagine
[09:58] you're designing an AI agent you need to
[10:00] orchestrate multiple models you need to
[10:02] retrieve data reason over it and
[10:03] generate an output you have two choices
[10:07] you can start with Primitives making raw
[10:09] API calls logging results your cells um
[10:12] and logging outputs and
[10:14] failures or you can start with a
[10:16] framework you can pick an abstraction
[10:18] you can wire it up and you can let it
[10:20] handle a lot of the
[10:21] details and I have to say starting with
[10:23] a framework is pretty enticing it's how
[10:25] I got started building agents it's
[10:28] really easy to get started have a proof
[10:29] of concept Concepts stood up in no time
[10:33] but the problem is that if you start
[10:34] with a framework you often don't
[10:37] actually know how your system behaves or
[10:39] what Primitives it uses you've deferred
[10:41] design design
[10:43] decisions before you've understood your
[10:46] constraints and if you don't know your
[10:48] constraints you can't optimize your
[10:50] solution so we believe a better approach
[10:53] is to First build with Primitives
[10:56] understand how your task decomposes
[10:58] where the failures happen
[10:59] and what actually needs
[11:01] Improvement then introduce abstraction
[11:05] when you find that you're Reinventing
[11:06] the wheel for example by re-implementing
[11:08] an embedding strategy or reimplementing
[11:12] model graders that may be a good time to
[11:14] bring in some
[11:16] abstractions many teams today are
[11:18] spending a lot of time picking the right
[11:20] framework um we actually believe that
[11:23] developing agents in a scalable way
[11:25] isn't so much about choosing the right
[11:27] abstraction it's really about
[11:28] understanding your data
[11:30] understanding your failure points and
[11:31] your
[11:32] constraints so in summary the first
[11:35] lesson is to start simple optimize when
[11:37] needed and Abstract only when it makes
[11:40] your system
[11:42] better which leads us straight to our
[11:44] second inside starting simple so too
[11:48] often teams are jumping straight into
[11:49] designing multi-agent systems agents
[11:52] calling agents coordinating tasks
[11:54] dynamically reasoning over long
[11:56] trajectories it all sounds really
[11:58] powerful but when it's done too soon it
[12:01] creates a lot of unknowns and it doesn't
[12:04] give you all that much
[12:06] Insight we like a different
[12:08] approach we generally recommend starting
[12:10] with a single agent that's purpose built
[12:13] for a single task put that into
[12:16] production with a limited set of users
[12:18] and observe how it
[12:19] performs doing this allows you to
[12:21] identify the real
[12:23] bottlenecks hallucinations over
[12:25] conversation trajectories low adoption
[12:28] due to high latency or maybe inaccuracy
[12:31] due to poor retrieval
[12:33] performance then knowing how the system
[12:35] underperforms and knowing what's
[12:37] important to your users we can work to
[12:40] incrementally improve
[12:42] it in a nutshell we should think of
[12:44] complexity as something which increases
[12:46] as we discover more intense failure
[12:48] cases and
[12:49] constraints because the goal isn't
[12:51] really to build a complicated system
[12:53] it's just to build a system that
[12:56] works so starting simple sounds great uh
[13:00] but we all know that complexity is where
[13:03] True Value is realized so how should we
[13:06] handle more complex
[13:07] tasks this is where a network of agents
[13:10] and the concept of handoffs comes
[13:13] in so you can think of
[13:15] handoffs sorry let's start with the
[13:17] network of Agents so a network of Agents
[13:19] is a collaborative system where multiple
[13:21] agents work in concert to resolve
[13:23] complex requests or perform a series of
[13:26] interrelated tasks you can think of this
[13:28] as a series of specialized agents
[13:31] handling subflows within a large agentic
[13:35] workflow on the topic of handoffs you
[13:38] can think of
[13:39] these as the process by which one agent
[13:43] transfers control of a active
[13:45] conversation to another agent it's
[13:48] pretty similar to how you get
[13:49] transferred to someone else on a phone
[13:51] call except in this case you can
[13:53] preserve your entire conversation
[13:54] history and the new agent just magically
[13:56] knows everything you've talked about
[13:57] already
[13:59] so let's see an example of
[14:01] this in this sample architecture we are
[14:03] showing how a fully automated customer
[14:05] service flow may be implemented with a
[14:07] network of agents and
[14:09] handoffs this approach is allowing us to
[14:12] BU bring the right tools to the right
[14:14] job so for example on the left hand side
[14:16] we're using a GPD 40 mini call to
[14:20] perform triage on the incoming request
[14:23] we're then using GPD 40 on the dispute
[14:25] agent to actually manage the
[14:27] conversation with the user and finally
[14:30] we are using a O3 mini reasoning model
[14:32] to perform accuracy sensitive tasks like
[14:34] checking whether the customer is
[14:36] eligible for
[14:37] refund it turns out that handoffs work
[14:39] really well and keeping the entire
[14:42] conversation history and context while
[14:43] swapping out the model The Prompt the
[14:45] tool definitions provide sufficient
[14:47] flexibility to solve a wide range of
[14:52] scenarios so our final lesson pertains
[14:54] to
[14:55] guardrails and just a level set
[14:58] guardrails is a catch all term today for
[14:59] any mechanism that enforces safety
[15:01] security and reliability within your
[15:03] application and it's generally used to
[15:05] prevent misuse and ensure that your
[15:08] system maintains
[15:10] Integrity so keeping the model
[15:12] instructions simple and focused on the
[15:14] target task ensures maximum
[15:17] interoperability of your system and also
[15:19] ensures that we are able to Hill Climb
[15:21] On on accuracy and performance most uh
[15:25] predictably guardrails should not
[15:27] necessarily be made part of your main
[15:29] prompts but should instead be run in
[15:31] parallel and the proliferation of faster
[15:35] and cheaper models like GPD 40 mini is
[15:37] making that making this more accessible
[15:39] than ever tool calls and user responses
[15:42] that are high stakes for example issuing
[15:45] a refund or showing a user what
[15:47] information uh some information from
[15:49] their personal account these can be
[15:51] deferred until all of the guard rails
[15:52] have
[15:55] returned in this example we see that
[15:57] we're running a single input guardrail
[15:59] to prevent prompt injection and then a
[16:01] couple of output guard rails uh on the
[16:03] use on the agent's
[16:06] response so to recap we have four
[16:09] lessons from our time building agents
[16:12] use abstractions minimally start with a
[16:14] single agent graduate to a network of
[16:17] Agents when you have more intense and
[16:19] finally keep your prompts simple and
[16:21] focused on the happy path and use guard
[16:24] rails to handle edge
[16:27] cases thank you than
[16:32] [Music]
