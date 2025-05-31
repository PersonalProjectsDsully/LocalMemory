---
type: youtube
title: Building AI Agents with Real ROI in the Enterprise SDLC: Bruno (Booking.com) & Beyang (Sourcegraph)
author: Channel Video
video_id: UXOLprPvr-0
video_url: https://www.youtube.com/watch?v=UXOLprPvr-0
thumbnail_url: https://img.youtube.com/vi/UXOLprPvr-0/mqdefault.jpg
date_added: 2025-05-26
category: AI in Software Development
tags: ['AI coding', 'code refactoring', 'LLM integration', 'developer tools', 'software automation', 'code migration', 'AI assistant', 'developer productivity', 'context-aware coding', 'enterprise AI', 'codebase optimization', 'human-AI collaboration']
entities: ['Bruno', 'Source Graph', 'Cody', 'AI coding assistant', 'large scale refactoring', 'code migrations', 'LLMs', 'developer workflow', 'software development life cycle', 'context-aware code generator']
concepts: ['automating toil in software development', 'developer inner/outer loop augmentation', 'AI code generation with context', 'LLM expertise optimization', 'codebase refactoring strategies', 'developer training impact', 'tool integration for productivity', 'enterprise AI adoption', 'code migration automation', 'human-AI collaboration in coding']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of software development workflows', 'Familiarity with AI coding tools', 'Knowledge of code refactoring techniques']
related_topics: ['AI in software engineering', 'LLM applications in coding', 'developer tooling strategies', 'codebase modernization', 'automation in software development', 'AI-assisted refactoring', 'enterprise AI implementation', 'context-aware code generation']
authority_signals: ['we found the llms had expertise right', "the people that started using and didn't see the value when they started getting trained they started using and falling in love", 'we started training developers and that became incredibly important']
confidence_score: 0.85
---

# Building AI Agents with Real ROI in the Enterprise SDLC: Bruno (Booking.com) & Beyang (Sourcegraph)

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=UXOLprPvr-0)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**:   

## Summary

# Summary of "Building AI Agents with Real ROI in the Enterprise SDLC"

## Overview  
Beyang (Sourcegraph) and Bruno (Booking.com) discuss how AI agents are being used to automate toil in enterprise software development, focusing on collaboration between their companies to address code bloat, inefficiencies, and the need for measurable ROI. They highlight tools like Sourcegraph Search, Cody, and the importance of training developers to unlock AI's potential.

---

## Key Points  
1. **Problem: Code Bloat and Toil**  
   - Large enterprises face challenges with legacy code, dead feature flags, and inefficient workflows, leading to wasted developer time.  
   - Example: "The best developer minds... destroyed by decade long dead feature flag migrations."  

2. **Tools and Partnerships**  
   - **Sourcegraph** provides tools like Code Search (Google-like code navigation), large-scale refactoring tools, and Cody (AI coding assistant).  
   - **Booking.com** integrated Cody with Sourcegraph Search to improve code understanding and experimentation with generative AI.  

3. **AI Agents for Automation**  
   - Focus on automating repetitive tasks (e.g., refactoring, migrations) to free developers for creative work.  
   - Key to success: Training developers to use AI tools effectively, leading to increased adoption and productivity.  

4. **Metrics and ROI**  
   - Tracking usage (e.g., daily users, task automation) and removing token limits to maximize AI utility.  
   - Emphasis on measurable outcomes: "How fast things are moving" in AI adoption.  

5. **Challenges and Solutions**  
   - Initial resistance to AI tools (e.g., developers not seeing value) was mitigated through training and access to multiple LLMs tailored to specific tasks.  

---

## Key Insights  
- **"Code farts"** (a humorous term for messy code) highlight the need for tools to simplify complex codebases.  
- AI's value lies in augmenting human creativity and automating "BS" in the outer developer loop.  
- Collaboration between companies (e.g., Sourcegraph and Booking.com) accelerates innovation in enterprise AI.  

---

## Actionable Takeaways  
- **Train developers** to maximize AI tool adoption.  
- **Use multiple LLMs** tailored to specific tasks for better results.  
- **Track metrics** (e.g., usage, automation rates) to prove ROI.  
- **Remove guardrails** (e.g., token limits) to enable full AI potential.  

--- 

This summary captures the collaboration, challenges, and strategies discussed for leveraging AI agents in enterprise software development.

## Full Transcript

[00:00] [Music]
[00:17] uh so my name is biang uh I'm the CTO
[00:19] and co-founder of a company called
[00:20] Source graph we build Dev tools for uh
[00:22] big messy code bases yeah and I'm Bruno
[00:25] Bruno pasos and I lead uh the product
[00:27] side of developer experience at
[00:29] booking.com
[00:30] and um yeah over the past year I've been
[00:32] overseeing the um the Gen Innovation
[00:35] side of booking as well cool and today
[00:38] we're here to talk about uh how we're
[00:40] partnering to build software development
[00:43] agents uh that automate a bunch of toil
[00:45] inside booking that are actually having
[00:47] real Roi and
[00:50] impact so how many people have heard
[00:53] this before you know you're the you're
[00:55] working inside a large company the CEO
[00:57] comes in and says like hey we need to
[00:59] adopt AI
[01:01] uh and then folks are like okay uh what
[01:03] does that mean you know how do we
[01:04] measure it you know maybe like fomo
[01:06] purchase co-pilot or something like that
[01:09] uh and then six months later uh someone
[01:11] else maybe the CFO is asking you hey so
[01:14] what's the ROI of of that AI tool we
[01:16] just adopted or you know what's the
[01:17] measurable impact of the agents that
[01:19] that we're building um this is a
[01:21] question that I think a lot of people
[01:23] aren't quite sure how to answer right
[01:24] now but Bruno and booking have been sort
[01:27] of on the Leading Edge of answering this
[01:29] question uh and very ProActive at uh
[01:32] acquiring and building the best tools
[01:35] and also following through to
[01:36] demonstrate uh how they're actually
[01:38] impacting their
[01:40] org it's very kind of you to say we are
[01:43] we are leading this I think we are we
[01:44] are right at the beginning and uh I feel
[01:46] couldn't be couldn't feel further from
[01:48] from actually the Forefront of it uh but
[01:51] let me let me start by talking a little
[01:53] bit about booking um I am sure uh the
[01:55] most of you would have heard about this
[01:57] company uh our goal is to make easier
[01:59] for everyone to experience the world and
[02:02] my team's goal is to make sure that our
[02:04] developers have their path cleared so
[02:07] that they can do their best work now are
[02:09] we close to that in some parts of the
[02:11] company yes other parts we couldn't be
[02:13] uh farther away from it to get to set a
[02:16] little bit of context uh we are one of
[02:18] the largest uh online travel agencies in
[02:21] the planet um and we serve about 1.5
[02:23] million room uh nights uh um with more
[02:28] than 3,000 Developers uh can you raise
[02:30] your hands uh who work in a company that
[02:32] has more than a thousand developers
[02:35] quick show of hands good number of
[02:37] people okay uh on the more on the on the
[02:40] dev side or on the technical side um we
[02:43] serve over 250 merge requests uh at a
[02:46] given year uh with 2.5 million CI jobs
[02:50] running at a given uh year as well and
[02:53] we are extremely data driven um our
[02:56] company has gotten to where it got to
[02:59] over
[03:00] experimentation and being obsessed about
[03:03] data and the reason I'm going into this
[03:06] is because as we experiment and in the
[03:08] form of primarily AB tests we start
[03:11] adding those experiments and and feature
[03:13] Flags into the code base and as we push
[03:16] forward to bring new features to our
[03:18] users uh most likely those experiment
[03:21] Flags or dead code will stay in the code
[03:25] base and now fast forward decades our
[03:28] codebase became extremely
[03:31] bloated uh fun fact I was uh my kids
[03:34] were looking at me uh editing this slide
[03:37] and they said what are feature flags and
[03:38] I said well um you know they stained the
[03:41] code Bay and they sto polluting the code
[03:43] Baye and they were like like code farts
[03:46] and I'm like now you're going into code
[03:48] smells is a different topic but let's uh
[03:51] let's move forward um and so as the the
[03:54] code base starts to blow up and become
[03:56] bigger and bigger cycle times also
[03:59] become uh larger and longer and they the
[04:02] time that developers spend to debug and
[04:04] to work on that code base just becomes
[04:07] over 90% toil right who here is familiar
[04:11] with
[04:13] this that's even more hands than than
[04:16] than than a thousand developers and so
[04:18] we survey our developers at least a
[04:20] quarter uh on how they're feeling how
[04:23] they're how they're they're feeling
[04:24] about working on that particular code
[04:25] base and it's it just becomes harder and
[04:29] harder for them to to do anything and so
[04:31] we had to do something about it so I've
[04:34] seen the best developer minds of my
[04:35] generation destroyed by decade long dead
[04:38] feature flag
[04:40] migrations it's
[04:42] crazy Claud Shannon actually say that
[04:45] or but I mean seriously though like
[04:47] they're probably like Geniuses out there
[04:50] like I was talking to someone from PWC
[04:53] the other night and describe the system
[04:54] that they're building to like update uh
[04:58] all all the kind of like Legacy code in
[05:00] their system and it was amazing like the
[05:02] guy was really smart really brilliant uh
[05:05] really like interesting Tech but
[05:07] wouldn't it be great if you know those
[05:08] sorts of Minds were unlocked to actually
[05:10] work on like you know new features and
[05:12] thinking about like user problems rather
[05:14] than all this kind of like Legacy craft
[05:17] and so in a nutshell that's why Source
[05:19] graph exists uh as a company so our
[05:21] mission is to make building software at
[05:23] scale tractable uh and so you might be
[05:26] familiar with a couple of the the
[05:27] products and tools we built uh along the
[05:29] years uh code search it's kind of like a
[05:31] Google for your code allows any human
[05:33] developer to find in and and build a
[05:35] working understanding what's going on we
[05:36] have a tool for large scale refactoring
[05:38] and code migrations uh you might have
[05:40] heard of our AI coding assistant Cody
[05:42] it's a context aware uh code generator
[05:45] that's tuned to work well in large messy
[05:47] code bases uh and the topic of this talk
[05:51] is really about the agents that we're
[05:53] building to automate toil out of the
[05:54] software development life cycle so a
[05:56] bunch of different products that we
[05:57] built over the years the unifying theme
[05:59] really really is to uh accelerate things
[06:02] in the developer inter Loop augment
[06:04] human creativity there and then to
[06:06] automate as much of the BS out of the
[06:07] outer loop as
[06:11] possible all right so um as bang talked
[06:15] about uh sour Graph Search just over two
[06:17] years ago we started using their product
[06:20] and there was a big success within our
[06:21] uh our community because they were able
[06:23] to search that bloated code base much
[06:25] much easier and find small pieces of
[06:28] context lying here in the I I totally
[06:30] encourage you to have a look at this uh
[06:32] particular product is awesome um and so
[06:34] about a year ago uh January last year we
[06:37] started experimenting with Cody and why
[06:40] because Cody also has s has Source Graph
[06:43] Search as context and so it became
[06:45] extremely useful for us to use a uh tool
[06:48] that had that context to be able to
[06:49] experiment with the the Gen topic and
[06:52] now we are hoping to reach the path of
[06:57] uh uh building agents with Cody and and
[07:00] Source Graph Search uh uh built
[07:02] in all right so um if I summarize very
[07:06] quickly and hopefully this illustrates
[07:07] how fast things are moving uh uh forward
[07:10] in January we started um with Cody we
[07:13] gave everyone the ability to start using
[07:16] the tool in the company so all our 3,000
[07:19] developers uh um had the the opportunity
[07:21] to use it some started using it some uh
[07:25] uh uh used it didn't see any value with
[07:27] it and then stopped using it and that
[07:29] started intriguing us and so back then
[07:32] right in the beginning of the year we
[07:33] had the choice of one llm to use across
[07:35] the entire company and some token limit
[07:39] uh uh um uh limiting what we could do
[07:42] with it and so the first thing that that
[07:44] we started pairing with Source graph and
[07:46] we appreciate the partnership on that
[07:47] was to remove all the the guard rails
[07:50] that we had in order to be able to
[07:51] really give it a go and so Source graph
[07:53] was very quickly to be able to give us
[07:55] multiple llms perir developers we could
[07:57] choose that and why that was important
[07:59] is because we found the llms had
[08:02] expertise right and so if we were going
[08:03] to excavate our code base our bloated
[08:05] code base a particular llm would do
[08:08] better than someone that was working on
[08:09] a completely new uh uh piece of service
[08:12] and and developing features there and so
[08:14] fast forward to July um we started
[08:17] training developers and that became
[08:19] incredibly important because the people
[08:21] that started using and didn't see the
[08:23] value when they started getting trained
[08:25] they started using and falling in love
[08:27] and becoming what we call that now daily
[08:29] users and I'll explain how why that's
[08:32] important um and then we started looking
[08:34] into more metrics back in January the
[08:37] main metric was I saved and um I
[08:39] mentioned that we are a data driven
[08:41] company and I saved wasn't the most
[08:43] statistically relevant metric that we
[08:45] could use it was based on Research only
[08:48] over a couple of developers a few
[08:50] developers and uh that wasn't cut um
[08:54] raise your hand here if you uh heard
[08:56] folks out there in the beginning of the
[08:58] hype talking about thousand thousands or
[09:00] or 880 100,000 hours they saved with Gen
[09:03] has anybody ever heard that and then you
[09:04] go back to your company and say why are
[09:06] we not doing this I call that semi BS uh
[09:10] uh uh and so we had to start going into
[09:13] other metrics something that were more
[09:14] statistically relevant and so we started
[09:16] brainstorming with that come October
[09:19] October we Define new kpis which I'll go
[09:21] deeper into it and metrics to measure uh
[09:24] to measure gen and fast forward to
[09:26] November end of last year we then start
[09:29] Ed finding traces that developers were
[09:32] 30% plus faster if they were using Codi
[09:36] on a daily basis and that's 12 plus day
[09:39] in a month to take away weekends and the
[09:41] times that they they were not
[09:43] coding and most importantly we were able
[09:46] to partner with Source graph to be able
[09:47] to create an API layer in front of cod
[09:49] so we could be creative in using with
[09:51] some of the tooling that we use like
[09:52] slack jira and and being able to extract
[09:55] some of that away from the ID
[09:59] all right so as we as we we finish
[10:02] around October we started looking into
[10:04] those kpis and what was important for me
[10:06] is that we Define something that we
[10:08] could measure within a year why because
[10:11] things are moving so fast and if we it
[10:13] was really helpful to ground us to what
[10:15] can we measure within the next year and
[10:17] so we defined four kpis the lead time
[10:21] for change quality code basing s sites
[10:23] that would then go into how we could
[10:26] modernize some of our bloated code base
[10:28] and so some of the metrics uh uh when I
[10:31] say short mid and long term these were
[10:32] metrics that we could see results in the
[10:34] short term in the midterm and in the
[10:36] long term and that long term is
[10:38] precisely a year and so we started
[10:40] seeing results with time to review Ms
[10:43] developers that were using Codi on a
[10:44] daily bases would ship 30% more Ms than
[10:48] the ones that that didn't and one very
[10:50] interesting piece is that their their Ms
[10:52] were lighter they had less code in it
[10:54] which I still don't know what to make
[10:56] out of it but we are we are working on
[10:58] it and then on the quality side of
[11:00] things we are hoping to go into the
[11:01] vulnerability can we show some of the
[11:03] vulnerabilities we've had in the past
[11:05] give the context the code bases context
[11:07] and try to see where we can predict
[11:09] whether new vulnerabilities will uh will
[11:11] appear or if they're still lingering our
[11:13] code base and then we started out the
[11:15] obvious one is test coverage can we
[11:17] increase test coverage can we create
[11:19] test coverage on the Legacy so the new
[11:21] staff when we rep platform passes that
[11:23] that particular set of tests and then we
[11:26] went into coding sites which is more
[11:28] related to like can we track what parts
[11:30] of our code Bay are not being used some
[11:31] feature flags that are still lingering
[11:33] but shouldn't be there and the code that
[11:35] is not performance enough and all of
[11:37] this is to feed into our ultimate goal
[11:40] which is can we bring the time to rep
[11:43] platform our code Bay from from yeah
[11:45] years to months
[11:48] right okay so while all this is going on
[11:50] one of the things we noticed is that the
[11:52] same Engineers that were using the the
[11:55] like coding assistant to generate code
[11:57] we also playing around with the
[11:58] underlying apis and so what we realized
[12:00] is that like asking people to customize
[12:03] prompts leads to them wanting to build
[12:05] and compose those calls into longer
[12:08] chain automations that we now call
[12:09] agents um there are a lot of pitfalls
[12:12] that we encountered uh uh you know in in
[12:15] the early stages of this like helping
[12:16] people understand what the expectations
[12:18] were with respect to what the the llm
[12:20] can do and what it can't do but the long
[12:22] story short is at some point we
[12:24] basically said F this it's not really
[12:27] working let's just like put our brains
[12:29] together you know fly out to Amsterdam
[12:31] we'll do like a weeklong joint hackathon
[12:33] and build some agents
[12:35] together and so the first thing to come
[12:37] out that hackathon was this thing that
[12:39] uh generates graphql so booking has a a
[12:42] huge graphql API can we play the
[12:46] video it uh it's seriously like more
[12:48] than a million tokens
[12:50] long H so it does not fit into the
[12:52] context window of any of the existing uh
[12:55] llms even if you could shove it inside
[12:56] context it's not going to do a good job
[12:58] of of of integrating that context into
[13:01] something that's coherent a ton of
[13:03] hallucinations and so what we did is we
[13:05] built this system that basically
[13:07] searches this very very long graph P
[13:10] schema finds the relevant like nodes
[13:13] wherever they are in this like schema
[13:15] tree uh and then uh agentically figures
[13:19] out which ones are relevant and then
[13:20] walks up that tree to pull in the
[13:22] relevant parent nodes and so on the
[13:25] right hand side you can kind of see it's
[13:26] like inner dialogue this is like it's
[13:27] thought process for uh reasoning about
[13:30] which nodes of the schema to pull in and
[13:32] then uh after it's done that reasoning
[13:34] it generates a response and so if you do
[13:36] this naively you know the UI looks very
[13:38] similar but you just end up getting
[13:40] garbage which is what we were seeing you
[13:42] know before we ran this hackathon after
[13:44] we sat down and and and actually work
[13:46] through like the specific prompts and
[13:47] stuff uh to make this work well we saw
[13:50] far better
[13:54] results all right so um a pretty
[13:57] interesting one that uh uh that we
[13:59] started uh uh working through in terms
[14:02] of Agents were the automated code
[14:04] migration could we go into that Legacy
[14:07] piece functions with over 10,000 lines
[14:10] to give you context and uh uh and speed
[14:13] up that rep platforming effort and so uh
[14:16] code search structure structured met
[14:18] meta prompt uh and then the the concept
[14:21] of dividing that particular code base to
[14:23] conquer the small bits were were really
[14:26] uh really
[14:27] interesting um one of the things that I
[14:30] totally recommend if you started to
[14:32] embark on on on a journey like this is
[14:34] pairing with some experts to bring that
[14:36] expertise into into your offices was
[14:39] incredibly valuable to us and we started
[14:41] seeing uh back to when I mentioned that
[14:43] the developers were using Cody and
[14:46] stopping and feeding back doesn't
[14:47] doesn't add any value was pure lack of
[14:50] knowledge uh folks didn't know how to
[14:52] work llms out they didn't know how to
[14:55] pass the right prompt in the right
[14:57] context and this was uh a pretty
[15:00] important piece for us to be able to uh
[15:02] to work on this particular uh agent and
[15:05] so when we go into this we had
[15:06] developers working for months at this
[15:09] point to try to figure out the size of
[15:11] the problem that we had to then be able
[15:13] to divide and conquer and then we came
[15:15] within two days within a hackathon we
[15:17] were able to really Define uh and
[15:19] understand where the the call sites were
[15:22] coming from and and being able to Define
[15:24] how big the problem is was important for
[15:26] us to be able to have a start point and
[15:29] collect the low hunging fruits that were
[15:31] available for us so U all of this is
[15:34] still in experimentation uh mode uh but
[15:37] we' seen a lot of values and a lot of uh
[15:39] uh sort of like firing that smoke in
[15:42] going from mons uh uh of of
[15:45] understanding the code Base
[15:49] today cool and so the the last agent
[15:52] that really came out of this joint
[15:53] effort uh was targeted at code review so
[15:56] this is something that we found is is
[15:57] pretty Universal across many different
[15:59] Enterprises like everyone who does not
[16:01] do code review here one hand okay uh
[16:05] I'll talk to you later sir um so like
[16:08] everyone does code review and what we
[16:10] found like originally we didn't think
[16:11] this was a very interesting space
[16:13] because there's like two dozen startups
[16:14] now that are popping up that do AI code
[16:16] review but when we talked to booking we
[16:17] talked to other Enterprises what we
[16:19] found is that like code review is kind
[16:20] of like very specific to your
[16:21] organization there's a long tale of like
[16:23] rules and guidelines and other things
[16:25] that uh you want to bake into your
[16:27] review process and a lot of the the
[16:29] tools that are off the shelf there
[16:30] aren't super customizable and so what we
[16:32] built is this interface uh where we're
[16:34] going through and productizing the the
[16:37] process of building a review agent
[16:38] that's tailored to your team and your
[16:40] organization so the the basic idea is
[16:41] that you define a set of rules that you
[16:44] want to hold in the code and then those
[16:46] are defined in kind of like a simple
[16:48] flat file format and then the agent will
[16:50] go and consume those rules apply the
[16:52] relevant ones to the specific files that
[16:54] are modified in any given uh PR and then
[16:58] uh very selectively post up comments uh
[17:01] that are tuned to those rules so it's
[17:03] very not noisy uh we're trying to
[17:04] optimize for you know Precision uh over
[17:07] recall here in in the feedback that
[17:09] we're we're giving uh the the the
[17:15] developer all right so knowing what we
[17:19] know in the beginning of this year we've
[17:21] been working on this for a year together
[17:22] uh uh with Source graph then a few ideas
[17:25] started popping into our mind of how we
[17:27] could go forward here and uh one of the
[17:29] things that I'd love to leave you with
[17:30] is the concept of declaring what are the
[17:33] rules of your service right so think
[17:35] think of your CI pipelines today uh when
[17:38] they give you errors could we anticipate
[17:40] and shift this left to the ID so those
[17:43] errors appear there and they appear in
[17:45] the form of here is an error and here is
[17:47] a fix so hopefully the service gets to a
[17:50] point where it's self-healing right and
[17:52] we started seeing that we could do that
[17:54] that there are there are there are areas
[17:55] that we can start using giving the all
[17:58] the context are the prompt that the
[17:59] developers started creating via the
[18:02] prompt uh library that we created and uh
[18:05] asking those questions Auto automate
[18:07] those questions to the server to see
[18:09] what comes out in terms of knowledge uh
[18:11] um uh out of that code base and so we
[18:14] think this is ultimately what we we are
[18:16] trying to achieve within I would say a
[18:18] short as short as the end of this year
[18:20] in terms of uh agents um but lots um
[18:25] Lots here to to go can I sorry can I
[18:27] just say one more thing read that last
[18:29] uh slide um I think that we have the
[18:32] potential here to solve one of the
[18:34] problems that has plagued software
[18:36] development since it Inception so you
[18:39] know who here has read the mythical man
[18:41] month before so yeah basically everyone
[18:44] so like it's this problem of like any
[18:46] software that becomes successful
[18:48] eventually becomes a victim of its own
[18:49] success because if you have Revenue if
[18:51] you have users that's going to generate
[18:53] feature requests bug reports any
[18:56] business that's prioritizing that is
[18:57] going to take on Tech debt to in order
[19:00] to compete quite frankly and over time
[19:02] as you add contributors to the code base
[19:03] you lose this cohesion of vision you
[19:05] lose the set of standards that you want
[19:07] to maintain and hold uh with declarative
[19:10] coding now you can have like the senior
[19:12] Engineers The Architects the the the
[19:15] people in charge of the organization
[19:17] Define constraints and rules that must
[19:19] hold through the code base and enforce
[19:21] those rules both at review time as well
[19:24] as inside the editor for you know the
[19:26] code that's written by human or AI yeah
[19:28] for bigger organization all your
[19:30] compliance rules all the things that
[19:31] that the developers need to work on but
[19:33] it's not necessarily feeding new
[19:35] features to your to your and users I
[19:37] think those could are perfect examples
[19:39] of um um yeah being declared into your
[19:43] service but anyway the main important
[19:46] thing so far in this past year that
[19:48] we've been uh um you know pairing to be
[19:50] able to figure this out has been
[19:52] education the more we educated the
[19:54] developer and handholding entire
[19:56] business units to be able to show them
[19:58] the value but then have them experiment
[20:01] within two days of like workshops and
[20:03] hackathons have them experiment with the
[20:05] tool they were coming out the other side
[20:07] incredibly passionate about what it can
[20:09] do but also becoming that daily users
[20:11] that we are trying to transform them so
[20:13] hopefully to defend that 30% plus
[20:16] increase on speed so educate your folks
[20:19] if you take one thing from this is
[20:21] education and if you want to dive deeply
[20:23] into any of this we got a booth
[20:25] downstairs feel free to stop by we'll
[20:27] talk shop or uh also tomorrow I'm given
[20:29] an expo talk that covers some of the
[20:31] more nitty-gritty details of how some of
[20:33] those agents were implemented so thank
[20:35] you thank you all
[20:42] [Music]
