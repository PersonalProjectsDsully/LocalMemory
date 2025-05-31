---
type: youtube
title: How Deep Research Works - Mukund Sridhar & Aarush Selvan, Google DeepMind
author: AI Engineer
video_id: eJOjdjO45Sc
video_url: https://www.youtube.com/watch?v=eJOjdjO45Sc
thumbnail_url: https://img.youtube.com/vi/eJOjdjO45Sc/mqdefault.jpg
date_added: 2025-05-26
category: AI Research and Development
tags: ['research agent', 'LLM', 'context management', 'error recovery', 'cross-platform', 'user trust', 'citations', 'AI challenges', 'web interaction', 'iterative planning']
entities: ['Google Docs', 'LLM', 'research agent', 'web', 'athletic scholarships', 'shortput', 'model', 'context management']
concepts: ['iterative planning', 'state management', 'cross-platform', 'context growth', 'error recovery', 'parallel vs sequential tasks', 'user trust', 'citations']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['knowledge of LLMs', 'context management', 'error handling', 'cross-platform development', 'research methodologies']
related_topics: ['AI research', 'LLM applications', 'web scraping', 'context management in AI', 'error recovery in systems', 'cross-platform development', 'user trust in AI', 'citations and references']
authority_signals: ['"we try and always show as all the sources"', '"we believe more and more users will start..."', '"it has to do this while interacting with a very noisy environment that is the web."']
confidence_score: 0.7
---

# How Deep Research Works - Mukund Sridhar & Aarush Selvan, Google DeepMind

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=eJOjdjO45Sc)  
**Published**: 2 months ago  
**Category**: AI/ML  
**Tags**: ai research, deep learning, web research, machine learning, google deepmind, research agent, asynchronous processing  

## Summary

# Summary of "How Deep Research Works" (Google DeepMind)

## Overview  
Mukund Sridhar and Aarush Selvan from Google DeepMind discuss the development of **Deep Research**, a feature in Gemini designed to act as a personal research agent. It provides comprehensive, real-time reports by browsing the web, analyzing content, and organizing findings. The talk highlights challenges in building such a system, including handling long-running tasks, noisy environments, and user trust.

---

## Key Points  

### **Motivation**  
- **Goal**: Enable users to get detailed, context-aware answers to complex queries by leveraging the web as a dynamic knowledge source.  
- **User Needs**: Address gaps in traditional models by offering transparency, interactivity, and adaptability in research workflows.  

### **Product Challenges**  
1. **Asynchronous Experiences**:  
   - Users need to wait for reports, so the system provides real-time updates on browsing activity.  
   - Challenges: Balancing transparency with usability (e.g., users gaming the system to test limits).  
2. **Handling Long Outputs**:  
   - Reports can span thousands of words, requiring structured formatting (e.g., artifacts for follow-up questions).  
   - Inspired by Anthropic’s artifact system for pinning content.  
3. **User Trust & Publisher Ethics**:  
   - All sources are displayed, even if not directly cited, to ensure accountability and support citations in Google Docs.  

### **Technical Challenges**  
1. **Long-Running Tasks**:  
   - Requires robust state management to handle failures (e.g., service outages) and recover without losing progress.  
   - Future scalability: Research agents may take hours, necessitating fault-tolerant design.  
2. **Iterative Planning**:  
   - Models must prioritize subtasks (parallel vs. sequential) and adapt to dynamic web content.  
3. **Noisy Environment**:  
   - Managing context growth during rapid information retrieval and ensuring relevance.  
4. **Cross-Platform Functionality**:  
   - Notifications across devices to allow users to "walk away" and resume later.  

---

## Key Challenges Discussed  
1. **Long-Running Tasks**:  
   - Managing extended execution times and ensuring reliability.  
2. **Iterative Planning**:  
   - Balancing model efficiency with the need to process complex, multi-faceted queries.  
3. **Context Management**:  
   - Avoiding token limit issues while maintaining coherence in long reports.  
4. **Failure Robustness**:  
   - Building systems to recover from intermediate errors (e.g., API failures).  
5. **Cross-Platform Notifications**:  
   - Enabling seamless user interaction across devices.  

---

## Example: Athletic Scholarships for Shot Put  
- **Sub-Problems**: Eligibility criteria, training programs, college recruitment processes.  
- **Model Role**: Prioritizing parallel tasks (e.g., gathering eligibility rules) vs. sequential ones (e.g., analyzing recruitment timelines).  

---

## Conclusion  
Deep Research represents a shift toward interactive, transparent AI research tools. By addressing technical hurdles like context management, failure resilience, and ethical sourcing, Google aims to create a reliable, user-centric system for complex querying.

## Full Transcript

[00:00] [Music]
[00:16] Hey everyone, I'm Arouch. I'm a product
[00:18] manager here at Google. Hey, I'm Ukun.
[00:20] I'm a software engineer at Google
[00:21] working on deep research. Um, so uh I
[00:24] don't know if people have had a chance
[00:25] to uh try deep research on Gemini um or
[00:29] are familiar with the product, but you
[00:31] can try it if you go to Gemini advanced
[00:34] and if you scroll past 2.0 flash 2.0
[00:36] flash thinking experimental 2.0 0 Flash
[00:39] thinking experimental with apps 2.0 pro
[00:41] experimental you will find uh 1.5 pro
[00:44] with deep research which is what we
[00:46] built. Um and if you have the chance to
[00:48] use it and you pay the 20 bucks uh you
[00:51] will see that it's a personal research
[00:52] agent that can browse the web for you to
[00:54] to build the reports on your
[00:57] behalf. And so our motivation and what
[00:59] we want to talk about today is kind of
[01:01] why we built it, some of the product
[01:02] challenges we overcame and some of the
[01:03] technical challenges you'll face of
[01:05] building a web research agent. Um so our
[01:08] motivation was really we wanted to help
[01:10] people get smart fast. Um we saw that
[01:13] research and learning queries are some
[01:15] of the top use cases in Gemini. But when
[01:17] you bring like really hard questions uh
[01:20] to chat bots in general, what we were
[01:22] finding is that it would often give you
[01:25] a blueprint for an answer rather than
[01:27] actually give you the answer itself.
[01:28] Right? So, we had this query that we
[01:30] used to throw around of like tell me
[01:33] what does it take to get an athletic
[01:35] scholarship for shot put and like how do
[01:37] I go get one? And often the answers
[01:39] would be things like you should talk to
[01:40] coaches, you should find out how far you
[01:43] should be able to throw and you know uh
[01:45] you should make sure you have good
[01:46] grades but really what I want to know is
[01:48] like okay what are the grade boundaries
[01:49] like how far do I need to actually be
[01:51] able to throw? I want something super
[01:53] comprehensive and and that's where we
[01:54] saw a big opportunity. Yeah. So we said,
[01:57] what if you remove the constraints of
[01:59] compute and latency at inference time,
[02:01] let Gemini take as long as it wants,
[02:04] browse the web as much as it needs, and
[02:06] see if we can trade that off for a much
[02:08] comprehensive answer for the user. But
[02:10] you got to do it in 5 minutes cuz beyond
[02:12] that, uh, we don't have the chips. Um,
[02:15] so,
[02:17] uh, this brought a bunch of product
[02:19] challenges for us. Um, Gemini up to this
[02:22] point is an inherently synchronous
[02:24] feature. It's a chatbot. Um and so you
[02:26] wanted to we needed to figure out how do
[02:28] you sort of build asynchronous
[02:30] experiences in in an inherently
[02:32] synchronous product. Um you also wanted
[02:34] to set expectations with users, right?
[02:35] Deep research is good for like one very
[02:36] specific thing but a lot of user queries
[02:38] to Gemini are things like what's the
[02:40] weather, write me a joke, things like
[02:41] that where waiting 5 minutes is not
[02:44] going to get you a good answer and we
[02:45] wanted to set expectations. Uh, and the
[02:47] last thing is our answers can be
[02:49] thousands of words long and we needed to
[02:51] figure out how do you make it easy for
[02:52] users to engage with really long outputs
[02:55] and um in in a chat
[02:58] experience. Um, so let's walk through
[03:01] kind of the UX and kind of think about
[03:04] how how we solve some of these, right?
[03:06] So imagine you're a VC uh and
[03:08] everybody's talking about, you know,
[03:09] investing in nuclear in America. And so
[03:11] you come with this query like hey help
[03:13] me learn the latest technology
[03:14] breakthroughs in small nuclear reactors
[03:16] and tell me interesting companies in the
[03:17] supply chain. So the first step when you
[03:20] bring this query to deep research is
[03:22] that Gemini will actually put together a
[03:24] research plan for you and present it in
[03:25] a card. And so this is the first way in
[03:28] which we're able to communicate with
[03:29] users like this is different. This isn't
[03:31] your standard chatbot experience.
[03:32] Something's going to happen. You're
[03:34] going to hit start. But it's also an
[03:36] opportunity for us to actually show the
[03:37] user a research plan that they can edit
[03:39] and engage with. kind of like a good
[03:40] analyst, right? They they wouldn't just
[03:42] get to work. They'd actually show you,
[03:43] okay, here's how I'm going to approach
[03:44] this. And it's a way for users to if
[03:46] they want kind of engage and steer the
[03:48] direction of the research
[03:50] further. Now,
[03:53] uh once it you hit start, we actually
[03:56] try and show you um what Gemini is doing
[03:59] under the under the hood in real time uh
[04:01] by showing you the the websites it's
[04:03] browsing. And this is a feature that was
[04:05] built before thinking models and
[04:07] thoughts are also a really great way of
[04:08] kind of showing transparency of what the
[04:10] model is thinking. Um but what's really
[04:12] nice here is while you wait you can sort
[04:14] of click through the websites dive into
[04:16] any of the content. Um but what we also
[04:18] inadvertently saw is people trying to
[04:20] game that number to see how high it
[04:21] could go. So we definitely saw people
[04:23] push that number into the into the
[04:24] thousands uh to try and um you know see
[04:26] how many websites deep research could
[04:28] read.
[04:30] Um, finally we kind of get this report
[04:33] that's, you know, thousands of words
[04:35] long. And, um, we're really inspired by
[04:37] what kind of what Anthropic does with
[04:39] artifacts. And so, we thought that was a
[04:41] really great way of sort of being able
[04:43] to pin an artifact so that users can
[04:45] actually ask questions about the
[04:47] research while reading the material.
[04:49] They don't have to scroll back and
[04:50] forth. And what's really neat about this
[04:52] is it means it's easy for you to engage
[04:53] in sort of changing the style of the
[04:55] report, adding sections, removing
[04:57] sections, asking follow-up questions and
[04:59] uh and it sort of makes that really
[05:01] easy. And the last part that's super
[05:03] important is kind of user trust and also
[05:05] doing right by the publishers. So we we
[05:08] try and always show as all the sources
[05:09] we read as well as all the sources we
[05:11] used in the report because not
[05:13] everything that we read is used but it
[05:14] stays in context for follow-up questions
[05:17] and and also sort of these are all
[05:19] things that um carry over to Google Docs
[05:22] as citations and things like that if you
[05:24] choose to export.
[05:29] uh so I thought today we can pick some
[05:31] of the challenges uh that one has to
[05:33] encounter while building a research
[05:35] agent and talk through some of them. So
[05:37] uh I picked four for today. So one is
[05:40] this this longunning nature of tasks
[05:43] introduce a couple of things that we
[05:46] need to look into. Second is the model
[05:49] has to plan iteratively and spend uh its
[05:52] time and compute during this time
[05:54] effectively. So what are those
[05:55] challenges there? And it has to do this
[05:58] uh while interacting with a very noisy
[06:01] environment that is the web. And as you
[06:04] do this and uh read through information
[06:07] very quickly you can start seeing your
[06:08] context grow and how do you effectively
[06:11] manage
[06:13] context? So if if you think about a job
[06:17] that runs for multiple minutes and
[06:19] something that can make many many uh
[06:21] different LLM calls and calls to
[06:23] different services, there are bound to
[06:25] be failures, right? And today we're
[06:27] talking about o of minutes, but you can
[06:29] very easily think in the future of uh
[06:32] these kind of research agents taking
[06:34] like multiple hours. So it's important
[06:36] to be robust to intermediate failures of
[06:38] these various services of various
[06:40] reliabilities and so being able to build
[06:44] a good state management solution being
[06:46] able to recover from errors effectively
[06:48] so that you just don't drop the whole
[06:50] research uh task due to one failure.
[06:53] That's one. The second aspect of doing
[06:55] this what it enables us is to enable
[06:58] this feature uh crossplatform. So we
[07:00] believe more and more uh users will
[07:03] start kind of registering your asks uh
[07:06] or your research tasks and just like
[07:08] walk away do their thing and then you
[07:10] need to get notified and this can happen
[07:12] now across uh devices and you can pick
[07:15] off uh uh reading it uh uh uh once it's
[07:21] done. So now what is the model doing at
[07:24] uh like through these you know uh few
[07:26] minutes. Uh so let's take a example
[07:28] right. So here uh we're looking for uh
[07:31] athletic scholarships uh for shortput.
[07:33] There are many facets to this query and
[07:35] we kind of show this in a research plan
[07:37] like showed. The first thing the model
[07:40] has to do is try to figure out which of
[07:42] these sub problems it can start tackling
[07:44] in parallel versus things that are
[07:47] inherently sequential. Right? So the
[07:50] model has to be able to reason to do
[07:51] that. And uh the other challenge is here
[07:55] you see you're always going to land in
[07:58] this state where there's partial
[07:59] information. So it's important to look
[08:02] at all the information found so far
[08:04] before you decide what to do next. So in
[08:06] this instance the model found hey it's
[08:09] it knows the qualifying standards uh for
[08:11] the D1 division but in order to provide
[08:14] a complete report and answer the user's
[08:16] question it has to go figure out what
[08:18] the equivalent for the D2 and D3
[08:21] divisions are. So this notion of being
[08:24] able to ground on information you find
[08:26] and then plan your next step is
[08:30] key. Another example of partial
[08:32] information could be when you make
[08:34] searches u so in this case you're trying
[08:36] to find the best roller coaster for
[08:39] kids. Uh you might find results uh that
[08:42] provide partial information again. So
[08:44] here uh you end up at a link uh which
[08:47] talks about the top 10 roller coasters
[08:50] but does not mention anything about them
[08:53] being suitable to kids. Uh so the
[08:55] planner has to recognize this fact and
[08:57] then go ahead and in the next steps of
[08:59] planning try to resolve this uh
[09:04] disambiguity. Um another example of uh
[09:07] challenges in planning is information is
[09:10] often not found in one place. you find
[09:12] facets of information spread across
[09:14] different sources. So here uh we're
[09:17] trying to find uh what would uh what
[09:20] would it take to get a certification for
[09:22] a scuba dive uh in in in some dive
[09:24] centers nearby. So you see uh one part
[09:28] or one source has uh the kind of the
[09:30] structure of uh what what you have to go
[09:33] through to get a certification but in a
[09:35] completely different source you have
[09:37] this notion of the pricing for this
[09:39] diving center. So the model has to weave
[09:41] this together to figure out uh you know
[09:43] what the cost structure for such a
[09:45] certification would look
[09:47] like. Then there's the classic uh entity
[09:50] resolution problem. So you might find
[09:53] mentions of the same entity across
[09:56] different sources. So you need to be
[09:57] able to reason about some information
[09:59] indicators to kind of figure out if
[10:02] they're talking about the same entity or
[10:03] you need to explore more to verify such
[10:06] uh disabilities.
[10:09] Um yeah, I think most people here have
[10:12] worked on some notion of a web problem
[10:14] and we know like it's super fragmented.
[10:16] So uh here you see two different
[10:18] websites uh talking about the same thing
[10:21] uh about music festivals in Portugal
[10:23] this year. Uh on the left uh if you end
[10:26] up at such a website it's easier and you
[10:29] get most of your information in one go.
[10:31] Uh on the right uh the layout is
[10:34] different. So having a robust browsing
[10:36] mechanism if you want to navigate uh the
[10:39] web for your research tasks is another
[10:41] uh important
[10:43] challenge. So like we saw there is lot
[10:46] of these intermediate outputs and as you
[10:49] do this and you start getting streams of
[10:51] information during your planning you can
[10:53] imagine your context size growing very
[10:56] quickly. Um the other challenge that uh
[11:00] about context size is your research task
[11:02] doesn't typically end with your first
[11:04] query. People have follow-ups. People
[11:06] can say hey can you also do the same for
[11:09] this other topic. So there is like this
[11:11] kind of a follow-up uh deep research and
[11:15] uh that also adds pressure on the
[11:17] context. Uh we at Gemini have uh the
[11:20] liberty of really long context models.
[11:23] uh but uh even then you have to design
[11:26] uh some way to make sure you you
[11:28] effectively manage your context and
[11:30] there are multiple choices here each
[11:33] come with various different trade-offs.
[11:35] Uh we're showing one here uh where we
[11:37] kind of have like this recency bias. So
[11:40] you have lot more information about your
[11:43] current and your previous tasks but as
[11:45] you get to older tasks we kind of
[11:47] selectively pick out uh you know things
[11:50] what we call as research notes and put
[11:52] it in a rag that way the model can still
[11:54] access it but it's being selective. Uh
[11:57] I'll hand it back to about uh to talk
[11:59] about what's next. Yeah. So we were
[12:01] super
[12:02] excited to put this feature out in
[12:04] December. We weren't actually sure if
[12:05] anyone was going to use it, if anyone
[12:06] was gonna care um to wait five minutes
[12:11] uh for something. And uh we were really
[12:13] positively surprised by the reception.
[12:16] Um and and really what we what we saw um
[12:19] was, hey, we've built something that's
[12:21] maybe as good as like a Mackenzie
[12:23] analyst, right? And we give it away for
[12:24] 20 bucks. But um you know, that's that's
[12:27] really great. And u but what it does is
[12:29] it just retrieves from the open web and
[12:31] it's a text in text out only system,
[12:33] right? And so where we sort of we sort
[12:36] of see a few different directions of
[12:38] where research agents are going to go
[12:40] next. And the first one is around
[12:42] expertise, right? So how do you go from
[12:44] Mackenzie analyst to a Mackenzie partner
[12:45] or Goldman Sachs partner or like a
[12:47] partner to law firm, right? So that's
[12:49] really around not just being able to
[12:52] aggregate information and synthesize it,
[12:54] but also think through the so what of
[12:56] how do like what are the implications
[12:58] for what we're going to do and what are
[12:59] the most interesting insights and
[13:00] patterns that come out of it. The the
[13:02] other thing is you know there are plenty
[13:03] of domains beyond professional services
[13:05] like the sciences where you you know
[13:08] want to get really good you know you
[13:09] want something that can read many papers
[13:11] form hypotheses find really interesting
[13:13] patterns in you know what methods we
[13:15] used uh and and come up with novel
[13:18] hypothesis to explore. However, um just
[13:22] because you build something that can be
[13:23] really smart doesn't mean that it's
[13:25] useful to someone, right? So, um if we
[13:28] were thinking about a use case of
[13:30] running a due diligence on a company,
[13:31] the way you'd present that information
[13:33] to me would be very different to the way
[13:35] you'd present that information to say a
[13:36] Goldman Sachs banker, right? Um, for me,
[13:39] you really want to talk through like
[13:41] what like what is this company and how's
[13:43] it positioned strategically, but a
[13:44] banker would want to know all the
[13:46] financial information, actually have a
[13:48] DCF that they could look at, right?
[13:50] Actually uh have a have a much more like
[13:52] fine grained uh sort of uh finan uh
[13:55] financial modeling and analysis and and
[13:57] that really should shape the way in
[13:59] which you browse the web, right? The way
[14:00] you browse the web, the way you frame
[14:01] your answer, the kind of questions you
[14:03] pursue should be very personalized to
[14:04] kind of meeting the user where they're
[14:06] at. I think the last part is sort of
[14:08] something that goes across domains of
[14:11] what models can do, right? So not just
[14:13] being able to do web research with text,
[14:15] but being able to combine that with
[14:16] abilities in coding, data science, even
[14:18] video generation, right? So coming back
[14:20] to this example, if you're doing a due
[14:21] diligence, what if it could go and do
[14:23] like a lot of statistical analysis and
[14:25] actually build financial models to
[14:27] inform the research output that it gives
[14:29] you, right? Telling you, hey, why is
[14:30] this a good company or not?
[14:32] Um, I should say Google doesn't give
[14:34] financial advice and you know it's not a
[14:37] financial adviser. Um, but yeah, and so
[14:40] we're really excited about the
[14:41] potential. We think there's a ton of
[14:42] headroom to make research agents better
[14:44] and we are really glad we didn't call
[14:46] this Gemini Deep Dive, which was our
[14:48] best name before uh before launching
[14:50] this feature. Um, that's it. Thank you
[14:53] so much. Thank you.
[14:56] [Music]
