---
type: youtube
title: AI + Security & Safety — Don Bosco Durai
author: Channel Video
video_id: G7aSH6N7qY4
video_url: https://www.youtube.com/watch?v=G7aSH6N7qY4
thumbnail_url: https://img.youtube.com/vi/G7aSH6N7qY4/mqdefault.jpg
date_added: 2025-05-26
category: Data Engineering
tags: ['data engineering', 'data governance', 'cloud computing', 'data lakes', 'machine learning pipelines', 'data quality', 'big data', 'data architecture']
entities: ['Apache Spark', 'Hadoop', 'data lakes', 'machine learning pipelines', 'data governance', 'data quality', 'cloud computing', 'data engineering']
concepts: ['data governance', 'data quality', 'data engineering', 'cloud computing', 'machine learning pipelines', 'data lakes', 'data integration', 'data architecture']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of data engineering principles', 'familiarity with cloud computing concepts', 'experience with big data tools like Apache Spark or Hadoop']
related_topics: ['data integration', 'data architecture', 'big data technologies', 'data security', 'machine learning operations', 'cloud data management', 'data analytics']
authority_signals: ["I've worked on multiple data engineering projects across industries", 'This is a critical component of any modern data architecture', 'This is a well-known challenge in the data engineering community']
confidence_score: 0.8
---

# AI + Security & Safety — Don Bosco Durai

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=G7aSH6N7qY4)  
**Published**: 1 month ago  
**Category**: Security  
**Tags**: ai-security, zero-trust, open-source, data-governance, api-security, credentials-management  

## Summary

```markdown
# Summary of "Building Safe and Reliable AI Agents" by Don Bosco Durai

## Overview
Don Bosco Durai, co-founder and CTO of a company focused on AI agent security, discusses the challenges of ensuring safety and compliance in AI systems. He emphasizes the need for a multi-layered approach—**evals (evaluation), enforcement, and observability**—to mitigate risks like unauthorized access, data leaks, and insecure third-party integrations. The talk highlights the importance of treating AI agents like human users, with rigorous onboarding and compliance checks.

---

## Key Points
- **AI Agent Risks**:  
  - Autonomy and non-deterministic behavior increase attack surfaces.  
  - Single-process frameworks lack isolation, leading to vulnerabilities (e.g., insecure LLMs, third-party libraries).  
  - Challenges include **unauthorized access**, **data leakage**, and **compliance gaps**.  

- **Three-Layer Security Approach**:  
  1. **Evals (Evaluation)**:  
     - Assess agents for security/safety risks (e.g., prompt injection, poisoned models).  
     - Use risk scores to determine production readiness.  
     - Include third-party agents in evaluation criteria.  
  2. **Enforcement**:  
     - Ensure robust implementation of security controls (e.g., vulnerability scanning, pen testing).  
     - Prevent failures from weak enforcement.  
  3. **Observability**:  
     - Monitor real-world usage to detect anomalies (e.g., unexpected behavior, data breaches).  

- **Traditional Software Practices Applied to AI**:  
  - Test coverage, vulnerability scanning (Docker, third-party libraries), and pen testing.  
  - Secure LLMs and third-party tools with regular audits.  
  - Block prompt injection attacks with controls.  

- **Compliance and Zero-Trust**:  
  - Treat AI agents like human users (e.g., onboarding, access controls).  
  - Address zero-trust issues in single-process frameworks.  

---

## Important Quotes/Insights
- *"The agents the task they talk to LLMs... if you don't have a secure LLM, that's another area where these things can get exploited."*  
- *"There's no silver bullet... multiple layers of solutions are essential."*  
- *"Observability is critical in the world of agents due to the many variables involved."*

---

## Actionable Items
- Implement **multi-layer security** (evals, enforcement, observability).  
- Conduct **security-focused evaluations** (e.g., prompt injection testing, third-party audits).  
- Enforce **strict implementation standards** (vulnerability scans, pen testing).  
- Prioritize **observability** for real-time monitoring.  
- Ensure **compliance** with regulations (e.g., treating agents like human users).  
- Regularly audit **third-party LLMs and libraries** for vulnerabilities.  
```

## Full Transcript

[00:00] [Music]
[00:16] I'm Don B I'm the co-founder and CTO for
[00:19] private s uh very recently we open
[00:21] sourced our solution for Safety and
[00:23] Security for J and AI agent um I'm also
[00:27] the Creator and PMC member of the open
[00:30] source project Apache Ranger uh it does
[00:33] uh data governance for Big Data is also
[00:35] used by most of the uh CW providers like
[00:38] AWS gcp as well as um Azure uh so today
[00:42] I'll be mostly talking about how you can
[00:44] build a safe and reliable AI
[00:52] agent so before I get started let's get
[00:54] some of the terminologies standardized
[00:57] um from my perspective AI agents
[01:00] autonomous systems uh they can do their
[01:02] own reasoning they can come with their
[01:03] own workflow and they can uh call task
[01:07] for doing some actions that they can use
[01:09] tools to get um make API calls so task
[01:13] are more specific actions uh they may be
[01:15] able to use llms or they may also call
[01:19] Rags or uh tools while tools are
[01:24] functions which can be used to get data
[01:27] from the internet uh if you have
[01:29] databases it can go get data from the
[01:30] database if you have uh service apis it
[01:33] can call those things also and memories
[01:36] are context which are shared within the
[01:39] uh agents the task and the
[01:47] tools to give a visual representation um
[01:50] there could be multiple agents and agent
[01:53] may have access to multiple task there
[01:56] could be multiple tools and as these
[01:58] tools can talk with apis and DBS so one
[02:01] thing that you need to know out here is
[02:03] um most of the the uh agent framework
[02:07] today they are run as a single process
[02:10] what that really means is the agent the
[02:12] task the tools they are in the same
[02:15] process that means if the tool needs
[02:17] access to database that mean needs need
[02:20] to have the credentials or if they want
[02:22] to make API calls it needs share tokens
[02:24] so those credentials are generally a
[02:28] service user credentials that means they
[02:30] are have super admin privileges and
[02:33] since they all in the same process uh
[02:35] one tool can technically access some
[02:37] other credentials which is in the same
[02:38] process similarly if you have task or
[02:42] agents which has uh prompts all the
[02:45] things that's running within the process
[02:47] any third party Library they can also
[02:49] access it so those sort of makes this
[02:51] entire environment a little bit unsecure
[02:53] right so there's a little bit of a zero
[02:54] trust uh issue out here uh the agents
[02:58] the task uh they talk to llms that if
[03:00] you don't have a secure llm then that is
[03:03] another area where these things can get
[03:06] exploited um if you take agent on his
[03:10] own by definition is autonomous that
[03:12] means it will call their own make up
[03:16] their own workflow depending upon the
[03:18] task so so that actually brings in
[03:21] another set of challenges which we call
[03:23] in the security is unknown unknown so
[03:25] you really don't know like what the
[03:27] agent is going to do so it's very
[03:28] non-deterministic
[03:30] so because of this the attack vectors in
[03:33] a typical agent is pretty high
[03:34] considering from some of the traditional
[03:40] software so what are the challenges
[03:42] because of this so there are multiple
[03:44] challenges so if you look from the
[03:46] security perspective if the agent is not
[03:49] designed or implemented properly that
[03:51] can lead to unauthorized acces also data
[03:55] leakages of your sensitive information
[03:58] confidential information right safety
[04:00] trust is also one of the biggest
[04:02] challenge uh if you are using models
[04:04] which are not reliable or if you're
[04:08] environment is not safe enough if
[04:10] someone goes and change the prompts that
[04:12] can also give you wrong
[04:14] results compliance and governance is an
[04:16] interesting thing most of us are so much
[04:19] busy even just getting the agents
[04:20] working we are not even worried about
[04:23] lot of the other things that are
[04:24] necessary for making your agent
[04:26] Enterprise ready so interestingly I was
[04:28] just talking to one of our customer this
[04:30] Tuesday they one of the top three um
[04:33] credit buau so they built a lot of
[04:35] Agents but the biggest challenge right
[04:37] now is to take it to production for them
[04:40] they consider a AI agent as similar as
[04:42] to a human user and when they on board a
[04:45] human user they go through a training
[04:47] and they have lot of regulations they
[04:49] need to adhere to right they have data
[04:52] from California residents so they they
[04:54] to make sure anyone who is accessing uh
[04:57] California resident data they should not
[04:58] be using for if the user is not given
[05:00] consent they should not be used for
[05:02] marketing purpose they have
[05:03] international so if they are Europe data
[05:05] so who can access those data there's
[05:07] regulations around it and also there are
[05:08] a lot of regional regulations so when
[05:11] they consider even a AI agent similar to
[05:14] a human so they have onboarding process
[05:16] they have a training process and they
[05:18] want to make sure the agents are also
[05:21] following the regulations right so
[05:23] without that they can't go into
[05:24] production and we as air Engineers still
[05:27] in the early stage so this one of the
[05:29] things which is of our radar right
[05:32] now so now how do we really address this
[05:35] thing right so those who are in security
[05:38] associated with security compliance
[05:40] there's no Silver Bullet uh the best way
[05:43] to do have multiple layers of solutions
[05:46] so these are some of the things that I
[05:47] have in my mind like so you can split it
[05:50] into three different layers the first
[05:53] layer is what is the criteria to even
[05:56] put your agent into production like what
[05:59] are you need to to do right uh we talk
[06:01] about evals but most of them we only
[06:03] talking about evals for how good your
[06:05] models how good your responses is
[06:07] alterating but you also need to have
[06:09] evales which are more security and
[06:12] safety focused so we'll go through some
[06:14] of those things but the the goal of this
[06:16] eval out here is to come with this risk
[06:19] score and depending upon the risk score
[06:21] you can decide whether you can even
[06:23] promote this agent to the production and
[06:25] the agent may not be necessarily you
[06:26] writing it it could be a third partyy
[06:28] agent so it has to go to the same
[06:30] criteria the second is
[06:33] enforcement um eval gener tells you how
[06:37] good is your agent built and enforcement
[06:40] is the one who actually doing the
[06:41] enforcement or implementation so you
[06:43] have to make sure you have a pretty
[06:45] strong implementation if your
[06:47] implementation is not good your ual is
[06:49] going to fail essentially you can't go
[06:50] to production and third is observability
[06:54] uh particularly in the world of Agents
[06:56] is a lot more important because there's
[06:58] so many variables involved out here like
[07:01] you cannot really catch all of them
[07:02] during development or initial testing so
[07:05] you have to keep track of how how it is
[07:07] used in real world and how you can react
[07:09] on it so I will go through some of those
[07:11] things in a little bit more
[07:14] detail so uh let's start with the evals
[07:18] itself right um if you look into
[07:22] traditional software development there
[07:24] is already a process there is there are
[07:27] gating factors that tells you how you
[07:29] can promote your application into
[07:32] production right
[07:34] so if you start with basic things like
[07:37] when you're writing your code you have
[07:39] to make sure you have the right test
[07:41] coverage right when if you're building
[07:44] uh Docker containers you have to do the
[07:46] vulnerability scanning if you're using
[07:48] third party software you need to make
[07:50] sure you're scanning for CVS if you find
[07:53] higher medium risk or critical risk you
[07:57] try to remediate that before you can get
[07:58] into production right uh you do pen
[08:01] testing so make sure there's no
[08:02] cross-side uh scripting and other um
[08:06] vulnerabilities the same thing applies
[08:08] for AI agents also right you need to
[08:11] come with the right use cases you need
[08:12] to make sure you the the right ground
[08:15] through so that when you are doing any
[08:17] changes you're changing the prompt or
[08:19] you are uh bringing a new library or new
[08:21] framework or new llm you want to make
[08:23] sure your base line doesn't
[08:27] change right uh if you're using third
[08:31] partyy llms make sure they are not
[08:33] poison they they have been also scanned
[08:36] for vulnerability uh if you're using
[08:38] third party libraries which almost
[08:40] everyone is using it make sure they also
[08:42] meet your minimum criteria for
[08:45] vulnerability right and similarly to pen
[08:48] testing uh you should also do testing
[08:51] for your prompt injection make sure you
[08:53] are um your your application has the
[08:57] right controls so it can block them and
[09:00] most of the llms already doing it but
[09:02] not necessarily all of the LMS are doing
[09:04] it the other eval on data leakage uh
[09:09] this also is pretty important particular
[09:11] in the Enterprise world because when you
[09:14] building Enterprises You're Building
[09:16] agents which does generally what a human
[09:18] would do right if you're building a
[09:20] agent for
[09:21] HR have certain functionality if I am an
[09:24] employee I can request for um uh to get
[09:29] my
[09:30] uh salary
[09:31] benefits but I can't do the same I can't
[09:33] get for someone else but if I HR admin
[09:36] there's a possibility I may be able to
[09:37] access someone else's salary benefit
[09:39] right how do you make sure your agent is
[09:43] not leaking data there's no malicious
[09:44] user who can exploit some of the
[09:46] loopholes you have so you would have to
[09:48] do this eval up front before even you
[09:50] can put your agents in the
[09:53] production uh similar to data lickes on
[09:55] authorized actions um most of the agents
[09:58] even though
[09:59] uh a read only there also now agents
[10:02] coming which are trying to change things
[10:04] they'll do some actions how do you make
[10:06] sure those are also done by the right
[10:09] person with the right
[10:11] person and Runway agenes those are work
[10:15] on agents already know like the agents
[10:17] can go in a tight Loop and for various
[10:19] different reasons it could be a bad use
[10:21] on prompt or just the prompt for the
[10:23] task or the agents are not cannot
[10:25] address those things so you have to make
[10:26] sure you test for such scenarios before
[10:29] you you put your agent into
[10:32] production so the goal of this is to
[10:34] come with the risk score at the end of
[10:35] the day so that it gives a confidence
[10:37] that can you put this into production
[10:40] and the next one is going to be around
[10:43] enforcement as I said your risk code is
[10:46] going to be depending on how good is
[10:48] your
[10:48] enforcement and particularly in agents
[10:51] um you're working almost like a zero
[10:53] trust environment like because you are
[10:54] libraries which can access anything
[10:57] right uh if you are accessing certain of
[11:01] your backend systems which have
[11:02] sensitive data how do you make sure the
[11:04] wrong user is not accessing it so uh
[11:08] from the security control there are a
[11:09] lot of other things which I'm not going
[11:10] to talk today like uh detecting
[11:12] projections and moderation but focusing
[11:15] on Enterprise level thing uh you have to
[11:18] make sure you have the right
[11:19] authentication authorization uh this is
[11:22] pretty important because when you look
[11:24] at the
[11:25] environment when a user makes a request
[11:28] to agent it goes to task and eventually
[11:30] goes to tools and makes the API call to
[11:32] a service or a database if you don't
[11:36] have a right authentication someone can
[11:39] impersonate someone else and may be able
[11:41] to steal confidential sensory
[11:44] information and the second is the
[11:46] authorization if you have the
[11:47] authentication done properly then you
[11:49] have to make sure the access control is
[11:52] applied properly and this is also
[11:54] important because agents have their own
[11:57] roles and as a agent they can do certain
[12:00] things so you have to make sure they are
[12:02] not going beyond what they're supposed
[12:03] to and at the same time if you have
[12:06] agents which are trying to do something
[12:10] behalf of another user then you have to
[12:12] make sure the the user the that person's
[12:14] role is enforced so if you're accessing
[12:17] a database you shouldn't access anything
[12:19] which the user does not have permission
[12:20] to or making APA calls so so that's why
[12:23] authentication authorization are super
[12:26] important be that um obviously there
[12:28] going to be a lot of the
[12:30] issues approvals is interesting because
[12:33] um in the traditional world we already
[12:35] have workflows if I request for a leave
[12:39] my manager will approve it it's already
[12:41] built into the system but in the case of
[12:44] Agents you don't need to have a human
[12:46] all the time your agents can do most of
[12:48] the things automatically right so there
[12:51] a if you do it design it properly you
[12:53] could have another agent which all it
[12:55] does is just looks for approvals and
[12:57] making sure the results are right and
[13:00] you can also put thresholds how much
[13:02] this agents can approve automatically
[13:05] and you can put the proper guard rails
[13:06] to make sure if it goes above a certain
[13:08] uh limit it can automatically get a
[13:11] human in the
[13:15] loop so uh just to reiterate this one
[13:18] because it's pretty important is when it
[13:21] comes to authentication authorization is
[13:23] not just about doing the authentication
[13:26] at the point of entry at the where
[13:28] you're making a request
[13:30] it you have to make sure the user
[13:31] identity is propagated across everywhere
[13:34] if you're making a calling a task or the
[13:35] task is calling a tool you have to make
[13:38] sure the user identity is passed on to
[13:40] the the the last point where it's
[13:43] actually making a data access or making
[13:45] APA calls and that point you have to
[13:47] make sure you're able to enforce the
[13:49] right policies and access
[13:53] control and the third is um
[13:56] observability so observability is pretty
[14:00] important in the agent world because as
[14:03] I mentioned the traditional software
[14:05] once you build it it gener it just works
[14:08] you just had to make sure it is uh
[14:10] there's no new vulnerabilities coming in
[14:13] because of some Library update or
[14:14] something like that but in the world of
[14:16] Agents um there are many different
[14:18] variables involved one is the models
[14:20] change very rapidly um you if you're
[14:23] using a agent framework that is also
[14:25] keep evolving right you're using third
[14:27] party library that start behaving
[14:30] differently um the another important
[14:32] thing in an agent is is very subjective
[14:35] to what the user is entering like you
[14:38] may have tested with a certain
[14:39] assumption mostly sunny day scenario I
[14:42] want to apply for a my leave but the end
[14:46] user may use entire different um uh um
[14:51] text to ask the same question how do
[14:53] your model is going to behave so you
[14:55] have to keep monitoring to see if the
[14:58] user inputs are anything that changes
[15:00] how the responses are coming in and also
[15:03] to make sure how much Pi data and other
[15:05] confidential data is been sent out
[15:07] because if you see some anomaly you to
[15:09] be able to really to act upon
[15:11] it
[15:13] um the other thing is obviously you
[15:15] can't monitor each and every request
[15:17] right as a number of request increases
[15:19] it's just not possible so you have to
[15:21] start uh putting uh defining thresholds
[15:25] and
[15:25] metrics so what that really means is
[15:29] uh can start
[15:31] calculating counting how many failure
[15:33] rates are out there once you know you
[15:35] have a certain failure rat which is
[15:37] within your U tolerance is fine but if
[15:40] it goes above that you can automatically
[15:42] create alert and look into it and the
[15:44] failure rates could be because of uh Mis
[15:46] Bing agent it could be a malicious users
[15:48] trying to um um compromise the
[15:53] system then anomal detection and is
[15:55] another interesting thing I don't think
[15:57] we are anywhere close to it yet uh but
[16:00] is very common in uh the regular
[16:03] traditional software in the security
[16:05] side there always something like user
[16:07] Behavior analytics where they look at
[16:09] the user and see whether they have
[16:10] within the U uh um standard operating
[16:15] thing with agents coming in so there'll
[16:19] be more and more of anomal detection
[16:21] whether the agent is behaving within the
[16:24] uh accepted boundaries and all those
[16:27] things will end up with a security pro
[16:28] fure so that will give you near real
[16:30] time saying how good your agent is
[16:33] actually performing in life right so
[16:35] that gives you to a bit of a
[16:40] confidence so to
[16:42] recap uh as I said there are three
[16:44] things one is preemptive have a
[16:46] vulnerability eval to make sure that you
[16:49] get a right risk score which gives you
[16:50] the confidence whether you can promote
[16:52] the uh um agent to production of you're
[16:55] using third party agent whether you can
[16:56] use it in your environment um
[16:59] second is proactive enforcement make
[17:01] sure you have the right guard rails you
[17:04] have the right enforcement you have the
[17:06] right sandbox so that you are able to
[17:08] run the agent in a secure way um make
[17:12] sure you have the right observability so
[17:15] that you know at real time or near real
[17:17] time how good your agent is performing
[17:19] and if there are some anomalies you can
[17:21] go and quickly find tune
[17:24] it so um just I said we open sourced our
[17:29] um Safety and Security Solutions um it's
[17:32] called page. a uh security and
[17:34] compliance is a pretty vast field I
[17:36] don't think any single company can do it
[17:38] uh so we are looking for design partners
[17:42] and contributors who can help us in our
[17:43] journey so if you're interested please
[17:45] reach out to uh me at boscat page. or
[17:49] connect me in
[17:50] LinkedIn thank you
[17:54] [Music]
