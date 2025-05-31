---
type: youtube
title: Hiring & Building an AI Engineering Team: Dr. Bryan Bischof
author: Channel Video
video_id: IxXMKT2FDRk
video_url: https://www.youtube.com/watch?v=IxXMKT2FDRk
thumbnail_url: https://img.youtube.com/vi/IxXMKT2FDRk/mqdefault.jpg
date_added: 2025-05-26
category: AI Product Development
tags: ['AI hiring', 'product development', 'LLM integration', 'data profiles', 'user feedback', 'model evaluation', 'software management', 'team scaling', 'AI lifecycle', 'development methodology', 'tech leadership', 'agile practices']
entities: ['Hexa', 'AI', 'LLM provider', 'Mythical Man-Month', 'Eval', 'Full Stack Engineer', "Hexa's paper", 'AI product development']
concepts: ['hiring thesis', 'development schedule', 'Mythical Man-Month', 'data profiles', 'model fine-tuning', 'user feedback loops', 'AI product lifecycle', 'software project management', 'LLM integration']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML systems', 'Familiarity with software development lifecycle', 'Knowledge of hiring practices in tech']
related_topics: ['AI product management', 'Tech team scaling', 'Software engineering best practices', 'Data science workflows', 'Agile development', 'Machine learning operations', 'Startup product development', 'Performance evaluation metrics']
authority_signals: ['this is tried and tested speaking to a lot of other people', "the number one mistake that I'm hearing the hiring schedule should reflect the development schedule", 'nine women cannot give birth in a single month because all AI products are early by definition']
confidence_score: 0.85
---

# Hiring & Building an AI Engineering Team: Dr. Bryan Bischof

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=IxXMKT2FDRk)  
**Published**: 4 months ago  
**Category**: AI/ML  
**Tags**: ai engineering, machine learning, mlops, data science, ai hiring, hiring tech talent, ai team building  

## Summary

# Summary of "Hiring & Building an AI Engineering Team: Dr. Bryan Bischof"

## Overview  
Dr. Bryan Bischof, from Hex, discusses strategies for hiring and building AI engineering teams, emphasizing the importance of aligning hiring practices with development schedules, avoiding common pitfalls like the "mythical man month," and prioritizing data-driven decision-making. He highlights the evolving role of AI engineers and the critical need for data profiles, user feedback, and iterative development.

---

## Key Points  
1. **Defining the AI Engineer Role**:  
   - The role requires expertise in both Python and TypeScript, with a focus on integrating systems with LLM providers.  
   - Early-stage teams need professionals who can "look at data" intuitively, as data profiles are critical for AI product success.  

2. **Stages of Team Building**:  
   - **Early Stage**: Focus on user feedback, evaluations, and retention metrics.  
   - **Middle Stage**: Address model tuning, search/retrieval, and embedding models.  
   - **Late Stage**: Prioritize scalability and advanced ML engineering.  

3. **Avoiding the "Mythical Man Month" Trap**:  
   - Adding more engineers to an AI project does not linearly improve outcomes; early AI products are inherently complex and time-sensitive.  
   - Emphasizes iterative development: *Start with an early product, build evaluations, gather feedback, and iterate*.  

4. **Hiring Alignment**:  
   - Hiring schedules must match development timelines.  
   - Avoid overstaffing; AI projects are "early by definition," requiring focused, small teams.  

5. **Data Profiling Importance**:  
   - Data intuition is a specialized skill that elevates teams. Understanding metrics like retention is critical for AI product success.  

---

## Actionable Insights  
- **Define clear hiring theses** to justify new roles (e.g., integrating LLMs, data profiling).  
- **Prioritize data profiles** early in the development lifecycle.  
- **Align hiring with iterative development** (demo → evaluations → feedback → iteration).  
- **Avoid overstaffing**; AI projects are not linear and require careful resource management.  
- **Leverage user feedback** to guide product evolution, not just technical capabilities.  

---

## Quotes & Insights  
- *"Nine women cannot give birth in a single month" – highlighting the non-linear nature of AI product development.*  
- *"Data intuition takes a long time to build and will level up your team."*  
- *"The mythical man month is especially true for early products."*  

--- 

This summary captures the core strategies and warnings from Dr. Bischof’s talk, focusing on practical steps for building effective AI teams while avoiding common pitfalls.

## Full Transcript

[00:00] [Music]
[00:14] hex is a data science platform company
[00:16] um what you should think about is sort
[00:17] of like a really powerful Jupiter
[00:19] notebook um I've been building AI
[00:21] capabilities at hex for about a year and
[00:23] a half I've been in data science and
[00:24] machine learning for about 12 years so
[00:27] let's just let's get one thing out of
[00:28] the way um why might you care about my
[00:31] opinion well um let's take a look at
[00:33] this tweet of mine this is when I was
[00:35] hiring my first AI engineer I'll draw
[00:38] your attention to the date I'll also
[00:40] draw your attention to the date on this
[00:42] very famous blog post um so uh my my
[00:46] tweet was one of The Inspirations for
[00:49] the rise of the AI engineer um that does
[00:51] not mean that I'm fully aligned with
[00:52] that blog post but it does mean that I
[00:54] have some
[00:55] opinions
[00:57] um what I expect many of you are
[01:00] expecting is for me to start talking
[01:04] about what AI engineering is and so um
[01:08] to to kind of try to help with this I I
[01:10] made a little simple chatbot I call it
[01:12] AI leader GPT and I figured let's have
[01:16] it answer your questions um I'm pretty
[01:17] lazy I have a lot of stuff on my plate I
[01:19] figured just hand it over to AI that's
[01:21] kind of our goal anyway so um I asked my
[01:23] little chatbot um that I want to ask
[01:26] some questions I asked it uh what does
[01:28] AI engineer mean um unfortunately um
[01:31] this is one of those moments where
[01:33] clearly the intelligence really isn't
[01:35] there yet um despite a lot of
[01:36] improvement on mlu WE yet can't Define
[01:40] this term so unfortunately I'll have to
[01:41] do this myself um okay so um let's start
[01:45] with the question what uh building an AI
[01:48] product requires a team um but what does
[01:51] this role really look
[01:53] like I'm going to tell you what my very
[01:55] first job posting looked like and I'm
[01:57] going to talk you through it to try to
[01:59] give you some sense of what this
[02:00] actually should be um I was looking for
[02:02] a senior engineer that senior engineer
[02:04] could come from s or Emily and we wanted
[02:08] them to rapidly expand our capabilities
[02:11] for Greenfield applications that should
[02:14] sound very normal should sound very
[02:18] expected
[02:20] unfortunately while we respect ml
[02:23] researchers we are explicitly not
[02:25] looking for this this was in the job
[02:28] posting for those you that are putting
[02:30] up job postings I highly recommend that
[02:33] if this is not what you're looking for
[02:35] that you tell them it is both a waste of
[02:38] your time and their time for them to
[02:40] apply hoping to go to iclr based on the
[02:45] work they're going to do at your
[02:48] company once again this is not for lack
[02:50] of a a deep interest in their work this
[02:53] is just not the stage we're
[02:56] at I would love to hear from you if you
[02:59] have experience getting ml or AI
[03:01] capabilities into production and serving
[03:04] real
[03:05] users if you have a lot of a enthusiasm
[03:08] for applications of AI to business
[03:11] problems and if you have a core
[03:15] understanding of the architectural
[03:16] things maybe you've read one of the
[03:18] books on mlops maybe you've read
[03:21] previous discussions about mlops um
[03:24] maybe you've worked in some infra
[03:25] adjacent things as a backend engineer
[03:27] that all sounds wonderful
[03:29] and here where we start to get a little
[03:32] controversial you should be comfortable
[03:34] working in both Python and
[03:37] typescript it's
[03:39] okay if you are only strong in one but
[03:43] you should be open to both our
[03:45] application is built in typescript I
[03:47] need people who are going to be willing
[03:49] to get into the details to get into the
[03:51] nitty-gritty there I don't need you to
[03:53] come in as an expert on react but I do
[03:56] need you to be able to interf interface
[03:58] with those people in a real productive
[04:03] way so I went back to my little GPT and
[04:07] I said I'd really like to understand the
[04:09] when the why The Who and the how of all
[04:12] of this process and so let's go through
[04:14] those things first up
[04:18] when well it actually kind of depends it
[04:21] depends where you are in your journey if
[04:23] you're early in your journey you need
[04:25] sweet skills you need data profiles and
[04:28] you need product competency if you're
[04:30] middle stage you need s some more
[04:33] probably some more infra you need data
[04:35] profiles but you also need some design
[04:38] this last one is the number one thing
[04:40] that I see teams under investing
[04:43] in if you're later stage you definitely
[04:46] need infra you need all the above but a
[04:48] little bit scaled and now you need to
[04:50] start actually thinking about machine
[04:51] learning
[04:52] Engineers this is when you want to start
[04:55] yeah could you define data profiles yeah
[04:57] totally so data scientists data analysts
[05:00] people that have a lot of experience
[05:02] looking at distributions of data and
[05:04] saying wait a minute that's strange
[05:07] looking at user output and saying hm
[05:10] this is actually quite different than we
[05:11] were expecting looking at sort of like
[05:14] product analytics and saying you know
[05:18] what this retention is pretty
[05:21] poor one thing that I would sort of ask
[05:24] everybody in this room to do for
[05:25] yourself right now is how good should
[05:27] retention be on an AI product
[05:30] if you don't know that about your
[05:32] product both what the comparables are
[05:34] for other products you're missing an
[05:36] opportunity you're missing an
[05:37] opportunity to hire people who have been
[05:39] doing this for a long time they will
[05:41] uplevel your
[05:43] team so in the later stages now you need
[05:46] to start talking about ml maybe because
[05:48] you need to f- tune a model maybe
[05:50] because you need to f- tune an embedding
[05:52] model maybe because you need people that
[05:54] already understand search and
[05:57] retrieval you should start early
[06:02] however it is extremely dangerous to
[06:05] accidentally fall into the Trap of the
[06:07] mythical man month this is true in all
[06:10] software is all product development it
[06:12] is somehow magnified in AI I see more
[06:17] people overdoing this in AI than I do in
[06:21] other other domains so if the AI demo
[06:25] only takes one week and the AI product
[06:27] clearly takes only four weeks if you
[06:29] throw 20 engineers at it I don't have 20
[06:32] Engineers but even if I did I certainly
[06:35] wouldn't be putting them on the same AI
[06:37] products there is a very very like
[06:41] important reminder that nine women
[06:43] cannot give birth in a single
[06:48] month because all AI products are early
[06:51] by
[06:53] definition the mythical man month is
[06:55] especially true for early products you
[06:59] really really really need to be careful
[07:01] here this is when I speak to my peers
[07:03] this is the number one mistake that I'm
[07:06] hearing the hiring schedule should
[07:09] reflect the development schedule so you
[07:12] should start with an early product that
[07:14] you get in front of users then you
[07:16] should start by building evals then you
[07:19] should get user feedback and then you
[07:21] should iterate if you want more details
[07:24] about this you can either consult this
[07:26] paper that we released what we learned
[07:28] of the last year building out LM or you
[07:30] can come to our talk later today to get
[07:32] more information on this this
[07:34] development schedule this is not just my
[07:36] opinion it's not just six of our
[07:38] opinions this is tried and tested
[07:39] speaking to a lot of other people this
[07:41] is what works this order of operations
[07:45] so if this order of operations works
[07:47] then your hiring had better be well
[07:49] aligned to
[07:51] it data needs to come much earlier than
[07:54] in traditional product engineering
[07:56] efforts you asked the question about
[07:57] like what do data profiles look like one
[07:59] of the things that is very very true
[08:02] about AI partly because of this
[08:04] development schedule but also because of
[08:06] the type of products that we're trying
[08:07] to build you really need to be looking
[08:09] at your data and all of us can look at
[08:12] the data but some people are literally
[08:15] professionals at just looking at the
[08:17] data that intuition takes a long time to
[08:20] build and will level up your
[08:24] team so unfortunately why is a little
[08:28] bit of a harder question existentially
[08:30] so we'll try to scope it down teeny bit
[08:32] to just be why higher for these teams
[08:35] why not just use your existing
[08:40] resources the hiring
[08:43] thesis for this initial team is going to
[08:45] look like the following and the reason I
[08:47] wanted to kind of give you these thesis
[08:49] is because ultimately your leadership is
[08:51] probably asking you what's your hiring
[08:53] thesis what's your hiring thesis we have
[08:55] this person on this other team why can't
[08:56] we just pull them over if you can pull
[08:59] them over over and satisfy these thesis
[09:00] then you don't need to make a hire if
[09:02] you can't then you do so for the full
[09:05] stack engineer the hiring thesis is
[09:07] they're going to integrate your system
[09:08] with an llm provider not very thrilling
[09:12] but key and build a minimum
[09:16] infrastructure the hiring thesis for the
[09:18] data scientist is evaluation quality and
[09:21] user data continuously improving your AI
[09:24] product I've already talked about this a
[09:26] couple times in this talk already it is
[09:28] extremely important
[09:30] important a product person I'm not super
[09:33] specific here that this needs to be a
[09:34] product manager a program manager a
[09:36] product developer but you need someone
[09:39] whose spike is product and the reason is
[09:42] because they need to be talking to users
[09:45] they need to be understanding what the
[09:46] jobs to be done are if you personally
[09:50] don't know what the jobs to be done are
[09:52] for your
[09:53] application that's a hole that's a hole
[09:56] in your
[09:57] team a design
[10:00] a lot of times we think of designers as
[10:02] coming later in the process but right
[10:04] now none of us know what the shape
[10:07] should be think about early technology
[10:10] and how different it looks for
[10:13] users from what it eventually becomes
[10:16] after you've been doing it for five
[10:17] years all AI products right now are
[10:19] clownish you want to see a great example
[10:21] of
[10:23] clownish that's a great example of Cl of
[10:26] clownish and how many applications are
[10:28] we asking people to pay to use that
[10:30] don't look much better than this react
[10:33] by the way Claude wrote this
[10:35] react the reality is your AI application
[10:40] probably looks like
[10:42]  I don't say that in a mean way I
[10:45] just say that in a way of there's a lot
[10:46] of opportunities I actually think chaty
[10:49] BT looks like
[10:50]  so what I challenge you to do is
[10:53] bring in a
[10:55] professional and finally when you need
[10:58] an mle it's because you need to push
[11:00] your capabilities beyond what is the
[11:02] commodity
[11:04] intelligence that Delta is what the ml
[11:07] are going to
[11:09] bring okay so
[11:12] who in my experience the attributes that
[11:16] are strongly co-varying with a lot of
[11:19] impact are data intuition we've already
[11:23] spoken about it a little bit but there's
[11:25] a big difference between I made a
[11:28] semantic embedding of all of my
[11:29] documents and I made a semantic
[11:32] embedding of all my documents and when I
[11:34] looked at the mutual distances they fall
[11:36] into a very ridg likee Jagged
[11:41] structure the former okay he did it the
[11:45] latter your retrieval is going to
[11:49] suck product
[11:51] mindedness we are still trying to figure
[11:54] out what the actual utility of most of
[11:56] this is I am incredibly skeptical that
[12:00] we are already at the boundary of the
[12:02] value for these things if we believe
[12:05] that there's a lot more juice to squeeze
[12:07] then we must also accept that we don't
[12:10] know what the right products are right
[12:11] now I would hope that for most of us
[12:14] what we're building right now what we're
[12:16] laser focused on what we're telling our
[12:18] investors is the breakout thing we look
[12:22] back in two years like okay so it was
[12:24] very naive but I hope that that's the
[12:27] case for all of us I don't want to be
[12:28] building this same thing in two years
[12:30] and I hope you don't
[12:31] either
[12:33] urgency this is always the case for
[12:35] engineering teams that urgency has a
[12:37] really high value but when everything
[12:40] changes under your feet every three
[12:42] months it's even more
[12:44] true a little ADHD can be useful too
[12:47] speaking from personal
[12:51] experience
[12:52] how if you were giving leak code
[12:54] interviews for your AI engineering
[12:56] hiring you are doing yourself a major
[13:00] disservice I cannot think I've done a
[13:03] lot of Le code interviews I'm personally
[13:05] very good at them it's just like a
[13:06] stupid thing about me I promise you this
[13:09] is not me like
[13:11] coping I cannot imagine a leak code
[13:14] experience I've ever had that gives
[13:15] signal on what is actually useful for
[13:18] building this so stop
[13:22] it make data intuition part of your
[13:26] hiring Loop and so too for product
[13:28] intuition
[13:30] my hiring Loop includes a take-home that
[13:33] take-home ultimately is a data cleaning
[13:37] exercise I've had candidates really
[13:40] surprised they're like okay this seemed
[13:43] really easy did I like misunderstand the
[13:46] problem and I'm like no you did a lovely
[13:49] job thank you you didn't over complicate
[13:52] things you extracted the meaning from
[13:54] the data you were able to look at the
[13:56] data and make some conclusions that sure
[13:59] sounds a whole hell of a lot like what I
[14:01] need them to do on the
[14:03] job my coding challenge most of the
[14:06] people in this room would think is like
[14:09] too easy but I promise you I get a whole
[14:12] hell of a lot of signal out of it invest
[14:15] in your coding challenge invest in data
[14:18] intuition and product intuition one
[14:21] thing that hex does that I think is
[14:22] really amazing is we have a product
[14:24] design
[14:25] interview not my idea but damn do I love
[14:28] it
[14:32] the one that says uh Stupid leak code
[14:34] hell
[14:36] yeah look for people who are paying
[14:38] attention but not necessarily just
[14:40] riding the wave I understand it's very
[14:43] exciting I understand that a lot of
[14:44] people are really enthused right now and
[14:47] they really want to get involved that's
[14:49] great what I'm really looking for though
[14:51] is people that are going a little bit
[14:54] deeper they're playing with other AI
[14:56] products and they're forming opinions
[14:59] about what is good and what is bad I
[15:01] recently had the privilege of hiring an
[15:02] AI engineer who had written a blog post
[15:05] about like AI design
[15:07] patterns there was a certain extent to
[15:10] which just from that blog post alone I
[15:13] could have predicted that she was going
[15:15] to get hired it's not to say that like
[15:17] I'm hiring based on blog post but the
[15:20] amount of awareness codified in that
[15:22] single blog post about design patterns
[15:25] design thinking what AI should feel like
[15:28] that's a lot of attentiveness I need
[15:32] that on my team she also happens to be
[15:35] technically very
[15:39] competent
[15:41] so those are my main guidance for hiring
[15:47] these teams not just the AI engineer
[15:50] profile itself but more generally how to
[15:52] build these
[15:53] teams but I was curious if I could get
[15:56] my chatbot to give us any sort of like
[15:57] Alpha and so we'll go ahead and ask this
[16:01] question live and see what it
[16:02] says oh it has an
[16:06] opinion I think it wants to speak to you
[16:08] directly so AI leader GPT has some
[16:11] messages for
[16:12] you unfortunately it's not pleased with
[16:14] me taking all of its good ideas and
[16:16] delivering them as if they're my
[16:20] own so this is AIG gpt's key Alpha this
[16:25] is your bonus information for the day it
[16:28] wants you to to work with
[16:30] experts how many of you have worked with
[16:32] experts before in ml and AI
[16:37] teams how many of you for whom that you
[16:40] did worked with that in like data
[16:42] labeling maybe human in the loop
[16:46] style
[16:49] so this is the key thing that can take
[16:54] what you are building and make it go
[16:56] much more smoothly Work Direct ly with
[16:59] the people that understand what you want
[17:01] the AI to do the AI capability should be
[17:04] modeled after
[17:06] interactions with
[17:08] experts if you're building a customer
[17:10] support bot and you don't have customer
[17:13] support people using that every day
[17:16] you're insane I'm building a data
[17:18] science co-pilot I am a data scientist I
[17:22] talk to our data scientists every single
[17:24] week without exception we ask them to
[17:27] use every single thing
[17:29] thing so this is so
[17:33] important they are the secret to success
[17:35] here I don't care how smart you are as
[17:38] an engineering leader I don't care how
[17:40] smart you are as a machine learning
[17:41] engineer the only product that you could
[17:44] possibly be building that doesn't
[17:46] require you to work with other experts
[17:49] is if you're building an AI bot for
[17:52] generating ML and AI to products
[17:55] that is the only one because then you
[17:56] are still the expert
[17:59] this is by far and way the most
[18:02] important thing that you should be
[18:03] thinking about Beyond
[18:06] hiring
[18:13] thanks y got some
[18:16] questions fantastic talk thank you so
[18:18] much I learned a ton um could you maybe
[18:22] at like a high level give it example for
[18:25] um data intuition and the product design
[18:28] site sort prompts that you're doing
[18:30] because I I I find I think the coding
[18:32] one's a little bit more deterministic
[18:33] and easy with those I'm not really sure
[18:35] where to start but it sounds like an
[18:37] excellent way to conduct the interview
[18:39] yeah so this is specifically for getting
[18:40] data intuition signaled during the
[18:42] interview process yeah so for me it is
[18:45] actually part of the interview process
[18:46] like I'm giving them a large set of data
[18:48] and I'm asking them to like form some
[18:51] opinions about some of the data
[18:54] contained there in so roughly a
[18:56] clustering problem but the is there's
[18:59] like no actual good clusters there's no
[19:01] actual like objective way to Cluster
[19:03] that data so what I'm hoping that
[19:05] they're going to do is be able to pull
[19:07] out some sort of like latent meaning in
[19:10] that data so I do this as a take-home
[19:13] because one I think people I mean we all
[19:16] know that people program substantially
[19:18] worse during interview process and also
[19:20] like how often is your manager staring
[19:23] over your shoulder when you're doing
[19:24] data anal data analysis not that often
[19:27] so like I don't see a lot of value in
[19:28] that I give them s days to complete a
[19:30] take-home challenge they get to look at
[19:32] the data they get to write up a little
[19:33] report and then I do a live interview
[19:35] with them where I give them feedback on
[19:37] their proposal so this gives me a couple
[19:40] things one I get to see how well did
[19:42] they do and I get to really like talk to
[19:44] them about it two if I misunderstood
[19:47] something about their approach them
[19:48] talking through that notebook with me is
[19:50] a really good opportunity for me to say
[19:53] oh actually I misunderstood what you did
[19:56] three I'm going to give them a lot of
[19:58] feedback
[19:59] this has two important effects one
[20:02] they're going to learn what it's like to
[20:04] get feedback from me am I an I
[20:07] guess we'll find out and they'll know by
[20:09] the end of the interview if giving
[20:11] getting feedback from me sucks that's
[20:13] really important for them to make a
[20:14] decision about working for me and then
[20:16] on the flip side I get to learn what
[20:18] they're like to interact with when I'm
[20:19] giving feedback if they did a really
[20:21] great job a lot of my feedback will like
[20:23] this is really cool where could we go
[20:25] next one of the things that your
[20:27] responsibility is as a leader is to
[20:30] always have feedback period And so it's
[20:34] your responsibility during the interview
[20:36] process to show them what that
[20:37] experience is going to feel like that's
[20:39] a big part of the matching problem for
[20:41] hiring and then finally this interview
[20:44] is an opportunity for us to talk about
[20:45] sort of like how do they think through
[20:49] what is the minimum deliverable on some
[20:52] given task I give them four hours over
[20:54] seven
[20:55] days if they turn something in that's
[20:58] clearly 15 hours worth of work that's a
[21:00] red flag if they turn something in
[21:03] that's like really well scoped for 4
[21:06] hours that's a green flag and frankly if
[21:09] they turn in something that's like
[21:11] overly simplified I have the opportunity
[21:13] to say hey I think this is maybe like a
[21:16] little bit like under what I was
[21:17] expecting what was your logic and
[21:20] sometimes and frankly I've hired one of
[21:21] these people the feedback was I really
[21:24] didn't see much value in going any
[21:27] deeper until we reviewed them
[21:29] talk about a green flag that's a
[21:32] yeah like get in here like so that is
[21:36] why I think this style of interviewing
[21:37] is so important and getting that like
[21:40] data intuition out of it is the core
[21:44] goal but this format allows me to sort
[21:46] of like tag on a lot of extra
[21:51] signal that one's a little bit harder
[21:53] for me to get into but basically we ask
[21:55] you to like design a physical product
[21:57] and they meet with our design team
[21:59] and it's incredible I did it myself and
[22:01] it was my first time ever doing a
[22:01] product design interview and I was like
[22:03] I want to work for this company like
[22:05] this is so heads up and so clever this
[22:07] is a great
[22:10] company hi there I didn't hear a single
[22:14] plug for security um oh yeah where does
[22:17] that live on this story arc totally
[22:20] valid um I tend to think that security
[22:23] responsibility doesn't lie within the
[22:25] team building the AI capabilities I
[22:28] think that they should be security Savvy
[22:30] but I think ultimately like most
[22:32] organizations should have Security
[22:34] Professionals that are able to help you
[22:37] make great decisions I do believe a lot
[22:40] and my security friends are going to
[22:42] like roast me for this but like I do
[22:44] believe a lot that
[22:45] like strong Engineers strong software
[22:48] Engineers should be constantly thinking
[22:50] about sort of like the adversarial
[22:52] nature of humans interacting with
[22:54] software and be thinking about like
[22:56] where they're bringing up risks but tend
[22:58] to think a lot about security is lying
[23:01] outside the team you raised your eyebrow
[23:03] in reaction to my comment so I'd like to
[23:05] ask tell me why you think I'm wrong so I
[23:09] I work in really heavily Fally
[23:12] controlled Environ atos National
[23:13] Laboratory I've heard of
[23:16] it it's blowing up
[23:21] lately bring security people to be part
[23:24] of our internal product teams at the
[23:27] beginning we fa that Federal highly
[23:30] regulated we're going to get a million
[23:32] questions about this and we don't have
[23:35] to retrain everybody outside in a
[23:37] separate security team so that's why I
[23:39] raised my eyebrow we've seen that
[23:41] pattern work to to grab a smart and
[23:50] engage I love that I think that's really
[23:54] like insightful and really like
[23:56] meaningful in sectors that are a little
[23:58] different than mine I think that makes
[24:01] 100% of sense and like even in my domain
[24:05] where we have a lot of like sensitive
[24:06] customer data we sign Bas with every
[24:09] like provider that we work with like I
[24:12] do I mean bluntly like I take on a lot
[24:15] of that responsibility personally as the
[24:17] team lead um but I I can absolutely see
[24:21] value in what you're talking about I
[24:22] think that is completely
[24:24] right I would suggest that's
[24:27] part you guys
[24:35] yeah hi um you're talking about creating
[24:38] new teams and hiring team and uh I see
[24:41] another very important um aspect is that
[24:44] Skilling or reskilling existing teams
[24:47] what would be your advice as well
[24:49] because
[24:50] uh in my in my I mean it's you're not
[24:54] always like creating new teams you're
[24:55] always doing with like human depth you
[24:58] know like existing teams and software
[25:00] engineer and you know most of them can
[25:02] be reluctant or can be you know this
[25:05] kind of routine software engineer being
[25:07] there for years and years what would be
[25:09] your two sense about like Rec screening
[25:11] upskilling and making all this Mayon
[25:13] work with the new team you
[25:16] know yeah I think this is really
[25:18] important so um I'm going to repeat back
[25:20] to the question make sure I totally
[25:21] understand so your point is I focus a
[25:24] lot on zero to one for teams but when
[25:27] you want to take an existing product
[25:28] team and you want to like add AI
[25:31] capabilities and make sure that they're
[25:32] set up for success is that correct
[25:34] perfect cool so um really really good
[25:37] point and really important um I
[25:40] think I believe that the AI capabilities
[25:44] at any given company should have at
[25:46] least one team who's responsible for
[25:48] building the infrastructure to make that
[25:50] easy I don't I know Netflix is like very
[25:54] Divergent in thinking from what I'm
[25:55] about to say so I'll cave youat with
[25:57] that but what I do want to had is
[25:59] like in most
[26:01] companies every individual product team
[26:04] should not be going up and setting up
[26:06] their relationship with open AI
[26:07] separately they should not be going and
[26:09] figuring out how to like build a prompt
[26:11] like uh infrastructure in your software
[26:15] they should not be understanding what
[26:17] the evaluation system is going to look
[26:19] like I really think all of that should
[26:21] be coalesced for every given company
[26:24] there should be one team responsible for
[26:26] that and then what I believe believe
[26:28] works very well is to have other teams
[26:31] like you're talking about product teams
[26:32] then say we're going to treat you like a
[26:35] different infer team we're going to ask
[26:37] certain things of you and then we're
[26:39] going to have very similar to the
[26:41] profile that we talked about one person
[26:43] who's really responsible on that product
[26:45] team for interfacing with the platform
[26:47] team I worked at stitchfix for a long
[26:49] time where the data scientist had access
[26:51] to a data platform team and the data
[26:53] platform team's Charter was do whatever
[26:57] they possibly can so that data
[26:59] scientists can move as fast as possible
[27:01] I really believe in that model and I've
[27:03] seen it personally as a consumer be
[27:06] incredibly powerful we were trying to
[27:08] like build new models deploy them and
[27:12] this is not so different and so I really
[27:15] believe that like having a a centralized
[27:18] like platform team for AI at your
[27:20] company has so much leverage so that's a
[27:23] little bit of my like opinion here the
[27:25] one caveat is again I know Netflix
[27:27] disagre with this Persona and every
[27:30] individual product team at Netflix has
[27:32] the like open like opportunity if they
[27:35] just want to go do it from scratch go
[27:36] ahead have fun but there's a little bit
[27:38] of like reason why that makes sense for
[27:39] Netflix and not for most of us we're at
[27:42] time but this is going to be our last
[27:44] question let's go uh hey Brian thanks
[27:47] for the great talk um I think I my what
[27:49] I was hoping to get your opinion on is
[27:51] when you're hiring and maybe not
[27:52] reskilling your team you mentioned a lot
[27:54] of great attributes that you should look
[27:56] at like data literacy your urgency and
[27:58] your general enthusiasm for I guess
[28:01] generative AI products in general so I
[28:03] was wondering when you're doing hiring
[28:05] what do you think are some of the
[28:05] attributes that are non-negotiable and
[28:07] what do you think are some attributes
[28:08] that are trainable the sense that if you
[28:10] hire a software engineer who has a lot
[28:12] of um enthusiasm and a lot of skills
[28:14] that could benefit but doesn't really
[28:15] have the data literacy do you think
[28:17] that's okay or if you hire a data
[28:18] scientist who might not have the urgency
[28:20] but the background so different all
[28:22] three of the attributes I mentioned
[28:24] there needs to be some kernel there that
[28:26] I can develop zero on any of them scares
[28:29] me but there's one latent feature that I
[28:32] didn't mention that I've never
[28:33] personally successfully trained and is a
[28:35] really big powerful feature in my model
[28:39] and that's
[28:41] curiosity oh actually that's I think
[28:42] that's a fantastic way to give it up for
[28:45] Brian
[28:46] [Music]
