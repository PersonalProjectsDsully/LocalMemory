---
type: youtube
title: Reverse Conway's law and GenAI: How agents will take over the organisation - Patrick Debois
author: AI Engineer
video_id: FpJ9dPe1qYQ
video_url: https://www.youtube.com/watch?v=FpJ9dPe1qYQ
thumbnail_url: https://img.youtube.com/vi/FpJ9dPe1qYQ/mqdefault.jpg
date_added: 2025-05-26
category: General
tags: ['tutorial', 'general']
entities: ["Reverse Conway's law and GenAI: How agents will take over the organisation - Patrick Debois"]
concepts: []
content_structure: tutorial
difficulty_level: intermediate
prerequisites: []
related_topics: []
authority_signals: []
confidence_score: 0.3
---

# Reverse Conway's law and GenAI: How agents will take over the organisation - Patrick Debois

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=FpJ9dPe1qYQ)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: conways law, genai, ai adoption, organizational change, platform teams, ai integration, devops  

## Summary

# Summary of "Reverse Conway's Law and GenAI: How Agents Will Transform Organizations" by Patrick Debois

## Overview  
Patrick Debois explores how Generative AI (GenAI) is reshaping organizational structures and workflows, drawing on **Conway's Law** (organizations shape their systems) and its reverse (systems shape organizations). He emphasizes the evolving role of humans in an AI-driven world, highlighting shifts in job responsibilities, the rise of "intent-based" work, and the need for adaptability.

---

## Key Points  
- **Conway's Law & Reverse**:  
  - Traditional **Conway's Law** states that an organization’s structure mirrors its systems.  
  - **Reverse Conway's Law** suggests AI systems will increasingly influence organizational structures, pushing teams to adapt to AI-driven workflows.  

- **AI as a Co-Pilot**:  
  - AI tools (e.g., code co-pilots) are becoming integral to tasks, reducing manual coding and shifting focus to **specification-centric** work.  
  - Example: Product requirements generate code, reducing reliance on typing.  

- **Job Evolution**:  
  - Tasks are **unbundled** or **substituted** by AI, forcing workers to move from "how" (execution) to "why" (strategy, review, and management).  
  - Stages of AI adoption:  
    1. **Complement** (AI enhances tasks).  
    2. **Substitute** (AI replaces tasks).  
    3. **New Roles** (AI creates unimagined jobs).  

- **Human-Machine Collaboration**:  
  - AI may handle repetitive tasks (e.g., training models, code generation), but humans remain critical for **review, cleanup, and complex decision-making**.  
  - Example: Amazon’s bidding system shows humans still needed for oversight.  

- **Future Workflows**:  
  - Shift from "typing" to **specification** and **management of AI systems**.  
  - Organizations must prioritize **intent-based workflows** and adapt to AI’s commoditization of tasks.  

---

## Important Quotes/Insights  
- *"We’re moving from a code-centric to a specification-centric approach."*  
- *"AI is not replacing humans but redefining their roles—shifting from execution to strategy and oversight."*  
- *"The rollercoaster of AI adoption: tasks shift, roles evolve, and new superpowers emerge."*  

---

## Actionable Takeaways  
1. **Upskill in AI Literacy**: Focus on managing AI tools, reviewing outputs, and defining system specifications.  
2. **Rethink Job Roles**: Prepare for tasks being automated, substituted, or reimagined in new ways.  
3. **Embrace Intent-Based Work**: Shift from coding to crafting requirements and strategic direction.  
4. **Monitor AI Limitations**: Stay vigilant for errors, as human oversight remains critical.  

--- 

This summary captures the core themes of Debois’s analysis, emphasizing the transformative yet collaborative relationship between AI and human roles in modern organizations.

## Full Transcript

[00:00] today we're going to talk about Conway's
[00:02] law reverse Conway's law and generative
[00:05] Ai and it's basically thinking about the
[00:08] future of how AI will influence our
[00:12] organizations now we got this new
[00:15] technology right like chat GPT was the
[00:17] first and it like impacted like
[00:19] everywhere the whole
[00:21] industry and this really brought like
[00:23] everybody was like so excited that like
[00:25] they kind of changed everything to
[00:29] becoming more an AI specialist and
[00:31] that's really cool because everybody's
[00:32] still learning um and we'll see where we
[00:36] end up now some kind of just sprinkle
[00:40] some AI on there and they don't go all
[00:42] the way and that's fine but I don't
[00:44] think that will kind of really get the
[00:45] results that they they want from
[00:48] it now the bigger questions that
[00:50] companies who do want gen they wanted to
[00:53] know like where does it land in the
[00:55] organization will it belong to the data
[00:57] team the application team the platform
[00:59] team we don't really know so we already
[01:02] see that like shaping our org for this
[01:06] new technology is something that is
[01:08] happening in a lot of organizations now
[01:10] last year at thei engineer event I
[01:13] talked about platform teams and how kind
[01:15] of you can introduce kind of and scale
[01:18] AI out of you can watch the video here
[01:21] but that's not what we're going to talk
[01:22] about today today we're going to talk
[01:25] about Conway's law and simplistically it
[01:28] says that whatever
[01:30] uh way you organize yourself and your
[01:32] teams will have an impact on what you're
[01:36] able to build like if you have small
[01:38] distributed teams you're likely going to
[01:40] go with modular services and
[01:42] architecture here you can see like
[01:44] various pieces of organization and a lot
[01:47] has to do with communication lines and
[01:48] how the communication lines actually uh
[01:51] influence uh part of the organization so
[01:54] there's a kind of impact of what we can
[01:57] build now who am I to talk about this
[02:00] um well I've been in automation for a
[02:02] long time been following a lot of the
[02:04] devops and now been really focused on
[02:06] doing more with geni as anybody of the
[02:09] else right and I'm particularly focused
[02:11] of engineering more with AI so kind of
[02:13] as a software developer to do more with
[02:16] AI and kind of bring the benefits up if
[02:20] you're looking at this uh video uh if
[02:22] you're interested in the slides
[02:23] afterwards please uh hit me a message on
[02:26] LinkedIn uh I'll be happy to share um in
[02:28] exchange for some feedback uh or things
[02:31] to
[02:32] improve another thing that I'm active on
[02:34] is the AI native Dev Community I'm a
[02:37] curator and a contributor um where we
[02:39] try to get the new stories out about how
[02:42] uh kind of development will change
[02:44] inside of the
[02:46] organizations now I told you a little
[02:49] bit of how we're organizing fori with a
[02:52] platform team but today we are doing the
[02:55] opposite how is AI changing the way we
[02:58] organize ourselves so that's kind of a
[03:01] kind of a kicker or a kickback uh in
[03:04] this now what have you seen so far one
[03:07] of the obvious things is first level is
[03:10] everybody kind of starts accepting AI as
[03:12] a co-pilot and that's really
[03:15] great um some kind of start going even
[03:18] further they think about like training
[03:20] or their knowledge uh this is came back
[03:23] um and like all the knowledge that we
[03:25] have it is changing and we can pass that
[03:28] on to that side kick that's great now
[03:32] eventually we already seeing that AI is
[03:34] writing more and more code and will
[03:37] become more of a contributor so even
[03:39] though it's a sidekick um uh and kind of
[03:41] a co-pilot it really drives us to uh
[03:45] more efficiency and more contributions
[03:47] in the
[03:48] organization now this brings the
[03:50] elephant in the room like are we still
[03:52] needed and that's the question a lot of
[03:54] people ask what should we do uh will
[03:56] they eventually kind of uh change the
[03:58] way uh we have to operate now that's
[04:02] normal and a lot of people are kind of
[04:05] like dealing with this issue at work and
[04:08] they are scared and often you have to
[04:10] think like when a new technology comes
[04:13] you have to rethink your job and
[04:15] sometimes the culture of your company
[04:17] really supports that and you're able to
[04:19] kind of help and learn about that nuf I
[04:22] hope that's the case for you and that
[04:23] you actually bring this new skill of how
[04:26] to figure out what you need to do uh in
[04:28] the next couple of years
[04:30] now what we're seeing is instead of just
[04:33] coding as an example we're moving away
[04:36] from just typing and having it help
[04:38] generate some of the text to a new rule
[04:40] is that we start thinking about the
[04:42] intent something we've always wanted but
[04:45] we've been there kind of in Tut toal
[04:47] writing codes typing and now kind of the
[04:49] new technology is taking this up to a
[04:52] level where we can think more about the
[04:54] planning and the intent there's even
[04:57] products that start emerging like
[04:59] product requirements and that generates
[05:01] the code so we're less about the typing
[05:03] anymore or you could say is becoming
[05:05] specification Centric and we feed it
[05:08] with the specs and then eventually it
[05:10] builds the
[05:11] system now it's almost like well we're
[05:15] reviewing and we still have to be good
[05:17] at reviewing we say this is good this is
[05:19] bad but we're going to do less typing
[05:22] and this is just an example of what
[05:24] everybody kind of using co-pilots and so
[05:26] on is kind of experiencing you become
[05:28] from you know kind of more the crater to
[05:31] the person that is managing and kind of
[05:33] more on the how uh sorry more on the why
[05:36] and less on the how and that's great now
[05:40] to put this in perspective every time
[05:42] there's new technology like people
[05:45] already have a job and I do a bundle of
[05:48] tasks uh as the upper uh kind of shows
[05:52] now technology comes along sometimes it
[05:55] adds or it's the co-pilot or it kind of
[05:59] complements what we do and sometimes it
[06:02] will be substituted so kind of that
[06:04] unbundling of toask is something that is
[06:06] normal when you kind like move with a
[06:08] new
[06:10] technology now what can happen H it's
[06:13] just going to be the same we're just
[06:15] going to do more and we ask a kind of uh
[06:19] extra for this right so sometimes that's
[06:22] what technology does it adds a premium
[06:24] to what we can do now sometimes like
[06:29] maybe the value that we put in coding is
[06:31] moved somewhere else to management or
[06:35] kind of manage specifications and that's
[06:38] kind of another thing that might be
[06:39] happening so even though you are like
[06:42] moving away from your existing task uh
[06:45] something happens in another tasks and
[06:48] then eventually it might be commodity
[06:50] and that's where you kind of like get
[06:51] this feeling hey if this is commodity
[06:53] what should I really be doing and how to
[06:56] go into another task to kind of prove
[06:58] your value to
[07:00] system and eventually that piece that
[07:03] was kind of really good and kind of was
[07:05] delegated become substitute it we don't
[07:08] care anymore the value is kind of uh not
[07:10] good anymore and we really have to find
[07:12] like another job in the system those
[07:15] things are the typical scenarios a new
[07:17] technology brings now you might think
[07:20] like maybe we're not coding anymore but
[07:22] we're training the the eye to do coding
[07:25] here's an example outlier where you know
[07:28] people get paid I'm not saying saying
[07:29] this is a bad job but it shows you kind
[07:31] of how technology can change some of the
[07:34] tasks and the difference kind of job
[07:36] that are being
[07:38] created now eventually you will see kind
[07:41] of these stages it won't affect me
[07:43] that's when kind of the task is kind of
[07:45] compliment and then you kind of go all
[07:47] the way up to hey it's going to replace
[07:49] me that's really Hull and eventually you
[07:52] find a spot that says I'm can now do
[07:54] things that I couldn't do before and I
[07:56] have now new superpowers and I can
[07:58] create something so kind of that's the
[08:00] roller coaster that we're on as an
[08:02] individual person in this new technology
[08:05] so this is how AI is affecting us as an
[08:09] individual now we know that things will
[08:11] go wrong so in this case Amazon to
[08:14] bought it collect you know uh increasing
[08:17] the price because one is bidding over
[08:18] the other so humans are still needed
[08:21] right in this case uh but as I showed
[08:24] before it might not be in all cases but
[08:26] things will go wrong and we have to be
[08:28] prepared for that and sometimes humans
[08:30] just have to clean up because that's
[08:32] what we do we understand what went wrong
[08:34] we make sure that like uh the machine
[08:37] can't handle it and this is the med
[08:38] intermediate scenario that we're going
[08:41] for now a lot of the automation what I
[08:43] learned is that a lot of it is about
[08:45] Automation and then it is about
[08:47] preventing failure and designing from
[08:48] failure and so on so kind of dealing
[08:50] with failure is still typically a human
[08:53] job it might require less people but
[08:56] when you kind of have this happening you
[08:59] have to be prepared so you still have to
[09:01] learn train and deal with all kind of uh
[09:03] the situations so it's almost like a
[09:06] paradox like the more we gained with the
[09:08] automation we still have to be training
[09:10] and be ready when the failure happens so
[09:12] it could be a kind of a net zero uh
[09:15] effect as well now let's move up we kind
[09:19] of have that delegated assistant
[09:21] co-pilot and now we're heading towards
[09:23] the team uh level and instead of having
[09:26] it a personal assistant we think about
[09:28] like a team member that has access to
[09:30] the team that helps the whole team uh to
[09:32] do a better job
[09:35] and sometimes uh the impact at the team
[09:38] level is the domain knowledge and as you
[09:41] can see when multiple people are on a
[09:43] team they have various levels of domains
[09:45] and we really focused on having kind of
[09:47] multi- uh purpose uh or multi-domain
[09:51] knowledgeable people the full stack
[09:53] engineer and bringing a team of Experts
[09:55] of various domains together we found out
[09:57] that's the best way to organize a team
[09:59] and that's great now if you think about
[10:03] like the human team that's great it has
[10:06] a limited number of knowledge which is
[10:09] contained let's say the seven or eight
[10:11] uh team members and then there's the
[10:13] whole domain knowledge that an AI can
[10:15] have it is way bigger and it can now be
[10:18] uh another way of getting that knowledge
[10:20] you already see that like people getting
[10:22] questions asking it but it's still the
[10:24] human that does the verification but
[10:26] it's frosty helpful to uh to this more
[10:29] automated uh as an
[10:31] agent So eventually that this might lead
[10:34] to smaller themes because that
[10:37] overlapping is maybe not that needed
[10:39] because we have a system that actually
[10:42] knows a lot again we have to still
[10:44] understand what good looks like so that
[10:47] might change the skills that we require
[10:49] in those teams as well and kind of maybe
[10:53] those smaller tees again become another
[10:55] tee who knows kind of like that is a
[10:58] scaling issue where kind of all
[11:00] speculated uh some I've seen some cases
[11:02] where teams got smaller I've seen some
[11:04] cases where teams got bigger uh we don't
[11:07] really know but the dynamic will likely
[11:09] change uh with more AI being as a team
[11:12] member and you can say that the stack
[11:15] that we're building like whatever we
[11:18] want to know uh there's the applications
[11:21] uh there's more of the infrastructure
[11:23] and then the teammates and we're looking
[11:25] for more domain specific teammates much
[11:29] like diversity that we brought in teams
[11:31] that can help somebody in sales
[11:32] somebody's really good at data
[11:34] somebody's really good at other skills
[11:36] to kind of bringing a new teammate stack
[11:39] all together uh with the technology
[11:42] stack so kind of that expansion is
[11:44] something that you'll see happen with
[11:45] more you know agents and parts becoming
[11:49] a part of the
[11:50] team now that means that as I mentioned
[11:54] before that we might be
[11:56] faster uh and they can do things a lot
[11:59] faster but you are still the person who
[12:01] kind of has to make the decision so
[12:04] maybe there's not enough work for you
[12:06] but there's a lot that you can do with
[12:08] multiple of these uh assistants and team
[12:11] members um and that's kind of a
[12:14] specialist that goes in when things fail
[12:17] or has an understanding uh of what to
[12:20] do now what we all see is that maybe the
[12:23] cycles that were used to the one and two
[12:25] weeks get reused in two days so it's
[12:27] becoming a shorter Fe back cycle so that
[12:30] means we're getting into the loop but we
[12:32] can't have like the conversations with
[12:33] everybody so there's going to be
[12:35] multiple feedback Cycles maybe that
[12:37] complete in a bigger feedback cycle but
[12:39] we're getting to a more real time cycle
[12:42] compared to the typical um kind of uh
[12:44] one or two weeks or three weeks that was
[12:46] required by humans to do
[12:49] something now we're all going to learn
[12:51] and as I mentioned the new uh way of
[12:54] forming a team is maybe more of kind of
[12:56] the team members that are agents and
[12:59] that leaves that one person not just to
[13:02] be the specialist but they might have to
[13:05] be switching between domains because
[13:08] they understand a and then to tomorrow
[13:10] they move to another project and they
[13:12] kind of work on that and so kind of that
[13:14] flexibility or fluid uh way of working
[13:17] is something you do so this doesn't come
[13:20] overnight and people have to train for
[13:22] this but again that might be the way
[13:24] that we're going because they are
[13:26] becoming uh more of the the overseers in
[13:29] the
[13:30] system and so AI is there to support us
[13:33] and when AI gets more uh we trust AI
[13:36] more or they become more trustworthy
[13:39] maybe kind of they take away some of the
[13:41] jobs that we already have as a team
[13:43] member and it goes away so that kind of
[13:45] shift from the pyramid uh above to kind
[13:48] of like the pyramid below that kind of
[13:51] the human section uh moves up U and
[13:54] might become smaller as
[13:56] well now we can already see this in
[13:59] another way helping that like the system
[14:01] is helping new developers join a team
[14:04] and that's great because um the learning
[14:07] curve has been reduced uh we need less
[14:10] interactions uh it's more tailored it's
[14:12] more personalized that's one way of
[14:14] helping uh new people in the team and
[14:17] one might argue at the point of this uh
[14:20] presentation do we still have the true
[14:22] understanding but as I mentioned before
[14:24] if you don't understand how can you make
[14:26] decisions how can you make the call how
[14:28] can you deal with failure if you don't
[14:30] truly understand yes uh the systems
[14:32] might help you they might have a large
[14:34] expertise but we know that these systems
[14:37] inherently have failures so we have to
[14:39] be prepared as well so I think we still
[14:41] need to understand the thing maybe not
[14:43] on a daily level but if we're the person
[14:45] that has to deal with the issues we
[14:47] still have to understand and kind of
[14:49] making decisions means you still
[14:51] understand what goods look
[14:53] like um and then people often argue
[14:57] about like well the the Juniors might
[14:59] not get into the field anymore because
[15:01] only the seniors know what could look
[15:03] like but we can have an accelerated
[15:05] learning there as well that a junior
[15:07] becomes a senior Foster thanks to that
[15:10] Ai and thanks to the training uh and the
[15:13] more personal thing so maybe that
[15:15] doesn't have really an impact on the
[15:16] Juniors but I'm sure it might have an
[15:19] effect uh kind of uh psychology wise
[15:22] that uh you might not be entering the
[15:23] field because it feels ding to be uh you
[15:26] know instant having to be the specialist
[15:29] as well so we'll have more trainings
[15:30] programs uh that will help that as
[15:33] well and you already see that kind of
[15:36] shrinking of a company at the more we
[15:39] delegate and maybe before it was more
[15:41] delegating to SAS companies but now
[15:43] we're delegating to assistance and the
[15:46] companies might become smaller much like
[15:48] the teams become smaller and we work
[15:50] from there to kind of have a different
[15:52] pattern on how we organize ourselves uh
[15:54] in a
[15:56] team all right so in this Casa in the pr
[15:59] case we were still about like having an
[16:01] assistant and it helping us uh was part
[16:04] of the team it took away some of the
[16:05] jobs but now we're entering the level
[16:08] well if it can do certain tasks as good
[16:10] as a human it might become a peer um and
[16:14] so that level of rising from being a
[16:17] teammate uh to appear on kind of helping
[16:20] us out now why is that not very strange
[16:24] because these LMS they contain a lot of
[16:27] culture of how we work work together and
[16:29] that's kind of how these agents will
[16:32] mimic kind of that is the the way that
[16:34] culture is TR transmitted uh much like
[16:38] Wikipedia transmitted a lot of knowledge
[16:40] these kind of um models can help us
[16:43] trans uh uh kind of help us bring a lot
[16:46] of knowledge uh into the system as well
[16:49] and it's not crazy this might be the the
[16:53] first paper about it where they kind of
[16:55] have multiple agents walking the town
[16:57] and they saw all the behaviors of one
[16:59] team talking to the other team guess
[17:01] what they also learned that you know
[17:03] when they collaborated when they talk
[17:04] more they get better results so it
[17:07] definitely mimics part of the human
[17:08] behavior uh in this as
[17:10] well and then one thing we hope for if
[17:14] they become a peer is that they can go
[17:16] off and do things on our behalf or like
[17:19] as a peer uh that they can help us so
[17:21] kind of that is probably uh where a lot
[17:24] of people hope it's going but it's going
[17:26] to be challenging because one do get
[17:29] that trust level as
[17:31] well and why not like have a whole
[17:33] company on this uh you know you have a
[17:36] software company and investor product
[17:37] manager and so on so you can simulate
[17:39] the whole process with agents uh and
[17:42] that's really cool would I trust it
[17:44] right now no but it's definitely
[17:45] interesting to see where this ends
[17:48] up now we mentioned about kind of having
[17:52] smaller teams but this also has an
[17:54] impact on the organization so maybe
[17:56] there's going to be less leadership uh
[17:58] and it's just going to use a bunch of AI
[18:01] agents and the teams get smaller uh
[18:06] indeed now agents uh might have unwanted
[18:10] Behavior much like humans is that we
[18:13] really want to control what happens uh
[18:15] if they do certain
[18:17] things some have started talking about
[18:19] toxic behavior of an agent like one
[18:22] agent is influencing other agents to do
[18:25] bad things um does it remind doesn't
[18:28] that remind you of humans like One Bad
[18:30] Apple imp impacting other team members
[18:33] it's exactly the similar Behavior so
[18:35] we'll have to watch out for this kind of
[18:37] agent Dynamics much like we did with
[18:39] Team Dynamics as well and you know is AI
[18:43] still going to be inclusing for humans
[18:45] we have to watch out like uh in this
[18:47] example uh you walk into a supermarket
[18:50] and if you don't smile you don't get in
[18:52] and the ey is deciding what happens to
[18:55] you and whether you're allowed to go in
[18:57] and kind of that level
[18:59] um is interesting to see how kind of AI
[19:02] Will Keep Us
[19:04] inclusive uh open ey has also working on
[19:07] kind of what they call a model spec so
[19:09] think about it what an llm is allowed to
[19:11] do it's the guard rails it's the rules
[19:14] that you're allowed to do and it's very
[19:15] similar to a code of conduct uh for
[19:18] humans working in a team or in an
[19:20] organization so we're mimicking the same
[19:22] kind of behavior uh for those agents as
[19:25] well and we want to be inclusive as well
[19:29] even though it's technology people fear
[19:31] like hey it's going to get feelings I
[19:33] don't think so but it doesn't mean that
[19:35] we have to be uh really bad to the
[19:37] systems because that might influence
[19:39] some of the toxic behavior and it's
[19:41] still if humans can influence what
[19:43] agents do it's the same as bad agents
[19:46] influencing kind of what the the whole
[19:48] team of Agents
[19:50] does we're going to maybe see how the
[19:52] market evolves from more General agents
[19:55] to specialized agents and handcrafted
[19:57] agents um maybe one is really good at a
[20:00] certain task as we mentioned before uh
[20:03] one is not available and is very Niche
[20:05] so we're going to get more handcrafted
[20:08] uh agents uh and some might work all the
[20:11] time some are FY specialist and it uh is
[20:15] very similar to kind of the specialist
[20:17] versus the generalists of a human uh
[20:20] working in a team um that we kind of
[20:23] have a different uh rewarding system uh
[20:26] as well and how it uh will be trained on
[20:29] the
[20:30] tasks all right this is maybe a stupid
[20:33] thing they did but it was almost like
[20:35] they like every agent could get an
[20:37] employee record like think of it as
[20:39] equal rights this uh was withdrawn
[20:42] there's a lot of backfire on this
[20:44] obviously that's not what people want um
[20:46] It's Not Human it's not there uh but the
[20:49] question is how do we deal with this as
[20:51] well and if you take this up a notch uh
[20:54] could this be a manager of people I
[20:56] showed you like who gets into the store
[20:59] that's a type of manager that's a type
[21:00] of decision that we're delegating to uh
[21:03] the agents
[21:05] already now that brings up a question
[21:07] like where do we allow an agent to sit
[21:10] in the organization a PE uh like an
[21:13] assistant appear and we go up all the
[21:16] way up to a manager so that again brings
[21:18] that AI inclusiveness like what is the
[21:21] decisions and we have to have kind of
[21:24] all the different uh code of conducts
[21:26] guard rails and everything in place and
[21:28] still have to understand what the
[21:29] failure is so we're still having a human
[21:32] having to manage this as well then you
[21:34] can think about like hey if some of
[21:36] those pieces get done by uh the agents
[21:40] we can put them next into the orc chart
[21:43] interesting way of thinking about this
[21:45] like what is the equivalent of one agent
[21:48] is it like five humans what's the cost
[21:51] so it brings a little bit of the return
[21:52] of Investments when you're planning an
[21:55] organization um and sometimes that not
[21:58] clear really clear but we're going to
[22:00] see more of those kind of discussions
[22:02] like well should I hire you because I
[22:04] have a team of agents that has the same
[22:05] output so that kind of discussions uh
[22:08] are up uh about to be happening already
[22:11] uh and then maybe you know it's the
[22:13] agents that go to our uh job here they
[22:16] kind of like uh you know applying for
[22:18] LinkedIn jobs maybe we don't work but we
[22:20] have managing and team of agents that
[22:22] actually uh do the work for us uh and
[22:25] help so we're becoming more of a task
[22:27] force on our own uh in that perspective
[22:31] um and yeah we're working theis are
[22:35] working for us uh and that you know
[22:37] might have a different LinkedIn of
[22:39] people finding work uh and finding uh
[22:42] people uh and services that they want to
[22:45] use now if they're working as us and
[22:48] they're in the HR and we treat them as
[22:50] humans uh uh kind of and the performance
[22:53] then we have to do with performance
[22:54] reviews as well like are they bringing
[22:56] the value or kind of sh we kind of give
[22:59] them different incentives much like
[23:01] humans get incentives uh there's the
[23:03] individual incentive the team incentive
[23:05] and the business incentive how do we
[23:07] kind of steer that clear uh with the
[23:09] agents as
[23:11] well so kind of that Roi driven uh with
[23:15] agents it's going to be way more
[23:17] specific than probably for humans uh
[23:20] where we don't want be that like that
[23:22] clear on hey you're doing this this is a
[23:25] return uh some uh domains really do this
[23:29] but we're going to see way more of this
[23:31] uh when agents do certain uh parts of
[23:33] our job or take over like teams as well
[23:37] and if you think about this we can like
[23:40] much like we do simulations when
[23:42] somebody joins a team as a human uh we
[23:45] can run this like what's the impact of a
[23:47] new person hiring uh as a new agent
[23:50] joining your team so kind of like that
[23:51] kind of experiments is what people are
[23:53] trying to figure out with a digital twin
[23:55] of the organization uh already
[23:59] now we might need an API that's just
[24:03] semantics uh we understand what the AR
[24:06] chart is HR and it's all very sensitive
[24:09] often um so it might not happen but it's
[24:13] uh definitely like a thought experiment
[24:15] to kind of think again on the ROI of
[24:18] hiring people hiring agents uh in that
[24:20] perspective
[24:22] already and then the question becomes
[24:24] like who controls who uh is it us
[24:26] controlling the agents the agents uh
[24:28] trolling us uh we we're not sure um and
[24:31] kind of that's you know a very weird
[24:34] situation to be in uh because ultimately
[24:36] who watches the Watchers uh is the where
[24:39] we're heading to already and then
[24:42] eventually maybe they become the
[24:44] business right which is really strange
[24:47] um in this uh like if you're building
[24:50] software and you have a team that built
[24:52] software and that's all good and you
[24:54] sell that software now all of a sudden
[24:57] this becomes
[24:59] um uh different if let's say we're used
[25:03] to kind of buy services from a third
[25:05] party company to kind of have uh very uh
[25:09] good service uh if everything becomes so
[25:12] cheap I might do internal labor again
[25:15] through my agents and the Agents
[25:17] Building Systems for me so it might be
[25:20] that disruptive that we're not doing
[25:22] software uh as a service but kind of
[25:25] like bringing um kind of service as a
[25:27] software uh in there
[25:30] already and so you see like how we went
[25:33] through it like the individual impact
[25:35] level the team and then it kind of start
[25:37] replacing us and maybe kind of we do the
[25:40] work uh and they started doing the work
[25:42] and we're going for so kind of that is
[25:44] the speculation um there's no kind of
[25:48] you know clear clut path um but I I
[25:51] thought um in this presentation I show
[25:53] you different forms how people are
[25:55] thinking about that stuff um and how
[25:58] we're going to get to that level now
[26:00] hyper humans who knows kind of that
[26:02] combination of a human starting to sound
[26:05] like a little bit cyborg I know I have
[26:08] no clue but something is happening
[26:10] something is changing in our
[26:12] organizations uh and it will all depend
[26:14] on how good the technology uh will
[26:16] become and how much trust we can put in
[26:18] there
[26:20] already and yeah I agree fascinating
[26:23] stuff I don't know uh but I agree it is
[26:27] something we have to to think about it
[26:29] sounds a little bit like science fiction
[26:31] but it might be uh be there like faster
[26:33] than we think and the impact might be uh
[26:36] something we don't see coming um that
[26:38] good and while many say uh you know AI
[26:43] won't take my job but somebody using AI
[26:45] will take my job well maybe there's good
[26:47] parts that will take away the toal and
[26:49] so on but obviously the whole discussion
[26:51] becomes like how will we get paid uh
[26:53] from there uh and like how will our
[26:57] economy drive if if we go to more more
[26:59] of those
[27:01] agents and my advice is you have to
[27:04] think about like stop building the thing
[27:06] like don't build the software yourself
[27:08] but kind of think about like how you
[27:10] would build the thing how you will kind
[27:11] of uh build dii that build the things
[27:14] that you're currently building and I
[27:17] think that's the best way to kind of go
[27:19] up a middle level and deal with this
[27:21] because then you actually understand
[27:24] what the things are doing you are very
[27:26] good position to do supervision and we
[27:28] also kind of uh bring the value to the
[27:30] system um with a new skill to do so
[27:34] thank you very much and I hope you enjoy
[27:36] this more futuristic talk about like the
[27:39] impact of uh AI on the organization and
[27:42] uh kind of on us as an individual uh you
[27:45] can watch most of similar videos on my
[27:48] YouTube channel uh or kind of connect on
[27:51] LinkedIn and please leave feedback uh
[27:54] and let me know um enjoy the rest of the
[27:56] videos thank you very much sure
