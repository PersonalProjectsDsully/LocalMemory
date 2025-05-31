---
type: youtube
title: Personal, Local, Private AI Agents: Soumith Chintala
author: AI Engineer
video_id: jMoAaZP_Kkw
video_url: https://www.youtube.com/watch?v=jMoAaZP_Kkw
thumbnail_url: https://img.youtube.com/vi/jMoAaZP_Kkw/mqdefault.jpg
date_added: 2025-05-26
category: AI and Privacy
tags: ['AI agents', 'privacy', 'cloud computing', 'local processing', 'digital trust', 'Apple ecosystem', 'Android', 'AI deployment', 'tech ecosystems', 'data security', 'cloud vs. local', 'digital service risks']
entities: ['Apple', 'Mac Mini', 'Android ecosystems', 'cloud email service', 'large tech companies', 'AI agents', 'cloud services', 'digital trust']
concepts: ['AI agent deployment', 'privacy concerns', 'trust in digital services', 'cloud vs. local processing', 'digital service trust models', 'ecosystem limitations', 'monetization risks', 'asynchronous processing']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['basic understanding of AI', 'familiarity with cloud services', "knowledge of Apple's ecosystem"]
related_topics: ['AI ethics', 'cloud computing', 'privacy preservation', 'local vs. cloud computing', 'digital trust models', 'tech ecosystem limitations', 'AI deployment strategies']
authority_signals: ['I work at neither of these companies I can say what I want', "I think that's like what I think is a feasible device to use to like run your AI agent right now"]
confidence_score: 0.85
---

# Personal, Local, Private AI Agents: Soumith Chintala

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=jMoAaZP_Kkw)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai agents, personal ai, local ai, private ai, pytorch, ai development  

## Summary

```markdown
# Summary of "Personal, Local, and Private AI Agents" by Soumith Chintala

## Overview
The video explores the importance of **personal AI agents** that operate locally and privately, emphasizing their role in managing daily tasks while preserving user control and privacy. The speaker, Soumith Chintala (known for PyTorch), shares insights from his work with AI tools like Swix AI News and robotics, advocating for a shift from cloud-based services to decentralized, user-controlled systems.

---

## Key Points

### 1. **AI Agents vs. Aggregators**
- **Swix AI News** is highlighted as an example of an AI aggregator, which curates information but lacks the ability to act autonomously.
- **True AI agents** must have access to **personal context** (e.g., screen activity, device data) to make informed decisions, unlike simple tools that only aggregate data.

### 2. **Why Local/Privacy Matters**
- **Cloud-based agents** pose risks: 
  - **Loss of control**: Users cannot fully trust third-party services to act predictably or ethically.
  - **Monetization conflicts**: Companies may prioritize profit over user interests (e.g., biased shopping recommendations).
  - **Unpredictable actions**: As AI agents gain power, their behavior becomes harder to monitor or control.
- **Local solutions** (e.g., running agents on personal devices) allow users to maintain **transparency and control** over their data and actions.

### 3. **Challenges in Context Access**
- **Practical barriers** to providing context to AI agents:
  - **Battery limitations**: Continuous monitoring (e.g., screen or audio) is impractical for mobile devices.
  - **Ecosystem restrictions**: Platforms like iOS limit background processes, making it hard to run agents discreetly.
- **Workarounds**:
  - Use a **Mac Mini** as a local server: No battery issues, can access Android ecosystems, and run agents asynchronously.

### 4. **Trust and Simplicity**
- Users trust services like email because they have a **simple, predictable model** (e.g., "reply to messages").
- Complex AI agents risk **unintended consequences** (e.g., an agent replying to a boss with inappropriate content) if their behavior is not fully understood or controlled.

### 5. **Risks of Cloud Services**
- **Monetization pressures**: Cloud providers might prioritize ads or partnerships over user interests.
- **Data exposure**: Sensitive personal data (e.g., tax records, private communications) is stored in third-party systems, increasing privacy risks.

---

## Key Takeaways
- **Personal AI agents** require access to **private, local data** to function effectively.
- **Cloud-based solutions** are inherently risky due to lack of transparency and potential conflicts of interest.
- **Local devices** (e.g., Mac Mini) offer a practical, secure alternative for running AI agents.
- The future of AI should prioritize **user control, privacy, and ethical design** over convenience-driven cloud services.

---

## Quotes
- *"The reason I trust email services is because they have a simple mental model... if the action space becomes powerful enough, you get uncomfortable."*
- *"Companies have to monetize in a million ways... what if your agent only buys from companies that give them kickbacks?"*
- *"You want your AI to see everything you see... but no battery life for that."*
```

## Full Transcript

[00:00] [Music]
[00:17] so uh why do I well first of all who am
[00:21] I uh do you know this thing called
[00:24] pytorch um a lot of people in AI used to
[00:26] know it but now a lot of people just use
[00:28] high level apis and don't know what's
[00:30] powering things underneath uh but like
[00:33] py is uh the software probably powering
[00:37] your AI apis um so I work on it I
[00:41] co-founded the project and it's uh it's
[00:44] a big project that is uh majority funded
[00:47] by meta where I work at um and so I'm
[00:52] talking about uh so I'm not talking
[00:54] about llama at all I work on llama a
[00:56] little bit but uh
[00:58] unfortunately uh am not in charge of
[01:00] llama to try to sneak in some secrets
[01:03] for you guys um I'm not going to tell
[01:06] you when the next llama is going to come
[01:07] or anything like that so uh why am I
[01:12] thinking about personal local agents
[01:15] well the as AI kind of started becoming
[01:18] more and more useful one of the things
[01:20] that saved my time the most every single
[01:23] day was swix is AI news and it's
[01:27] basically like I have to keep up to date
[01:29] with all of what's going on in AI That's
[01:31] my job and now instead of basically
[01:35] spending 3 four five hours a day um
[01:38] looking at a bunch of sources like they
[01:40] was aggregating a bunch of news for you
[01:43] and I thought that was like one of the
[01:46] like one of the first applications I
[01:47] thought was like
[01:49] mind-blowingly uh personally like
[01:51] effective for my own productivity and
[01:54] that's when I started going into like
[01:55] hey I'm going to like augment uh AI
[01:58] within my day-to-day
[02:00] in a deeper way um that's not an agent
[02:03] though AI news is more like a an
[02:06] aggregator uh but that's how it kind of
[02:08] started the other thing is I also work
[02:09] on robotics um and robots are
[02:12] essentially agents they act in the world
[02:15] so um I I my goal is to build home
[02:18] robots so that I don't need to do any
[02:21] errands um and so um as part of that
[02:24] Journey as well I've been like kind of
[02:26] getting into like okay how do I get into
[02:29] understanding AI agents more deeply um
[02:33] the key takeaway I'm going to really
[02:35] like drill down uh to you today is
[02:38] Agents like especially personal agents
[02:40] have so much POS agency in taking
[02:44] actions on your behalf and stuff and
[02:46] they have so much of your life context
[02:48] to actually be useful to you that you're
[02:50] better off keeping them local and
[02:52] private and I'm going to try to like
[02:54] sketch out a plan on how to do it but I
[02:56] don't think I have a complete solution
[02:58] either um so so first like agent what is
[03:01] an agent like and why did I say swix is
[03:03] AI news is not an agent well an agent is
[03:05] something that can act in the world like
[03:07] an agent is something that has agency it
[03:10] can actually like take an action in the
[03:12] world uh anything that can only get
[03:14] context and do things but then
[03:16] eventually can't act in the world is not
[03:18] an agent that's how I think about it and
[03:21] what I think is like a highly
[03:23] intelligent agent without the right
[03:25] context is as good as a bag of rocks
[03:27] it's like really useless I'll give you a
[03:30] couple of examples very quickly uh let's
[03:32] just say I build a personal agent it has
[03:35] uh access to my Gmail my WhatsApp my
[03:37] calendar I was like did did I get my
[03:39] prescription renewed and it's like no
[03:41] not yet and like it's totally lying uh
[03:45] except it didn't know because like I got
[03:48] the text from CVS on my iMessage and it
[03:51] didn't have access to uh that source and
[03:55] it was doing the best it can with the
[03:57] information it has but if it didn't have
[03:59] the context like it's not going to like
[04:01] know how to do better uh similarly I
[04:04] mean you can make up like a 100 examples
[04:06] like this where like you have access to
[04:08] One bank account but like your money
[04:10] came into a venmo and you're like uh the
[04:14] agent lied to you what happens is like a
[04:17] personal agent that doesn't have the
[04:19] right context it's largely going to be
[04:21] irritating to use it's like you don't
[04:23] know when it is useful and when it is
[04:25] not useful so it's essentially not
[04:27] useful um like even when it gives you
[04:30] some answer you're like H is this
[04:32] actually right I'm going to have to go
[04:33] dig in right so unless it hits a certain
[04:36] level of like reliability and
[04:38] predictability that you know it is right
[04:43] uh it's not going to be actually useful
[04:44] to you um so now like why am I talking
[04:50] about personal agents specifically um
[04:55] and how do you like how do you get all
[04:57] this context to the agent so let's just
[04:59] say you have like your open API or some
[05:02] other API or some local llm what is all
[05:06] the context in the world that is
[05:09] personal to you and how do you give it
[05:11] to the agent well like the number one
[05:14] thing that you possibly want to do is
[05:15] like just have variables right you're
[05:17] just like you can uh the your AI should
[05:21] see everything you see and listen to
[05:23] everything you hear um and that is like
[05:26] obviously the best case of providing
[05:28] context to your AI AG except like
[05:31] there's no battery life for any of these
[05:33] variable things so that's not really
[05:35] practical maybe one day when you have
[05:37] like crazy batteries but that's not
[05:40] really going to work the other thing
[05:43] could be like okay like most of my life
[05:45] is on my phone uh in the ways that I
[05:48] care about from like an agent
[05:50] perspective uh what about just like uh
[05:53] running an agent on my phone it's
[05:54] running the background and it's just
[05:56] like always like watching my screen or
[05:58] something well well you know that's
[06:01] where like apple kicks you because you
[06:03] know they don't let you run a bunch of
[06:05] stuff in like on your phone
[06:07] asynchronously if you even if you do
[06:09] they have a lot of restrictions so like
[06:11] the ecosystems kind of like kill you and
[06:13] not allowing you to do that and
[06:15] unfortunately I use like apple um so
[06:19] that's that's out so the next one is
[06:23] like okay actually like the thing that I
[06:25] found like relatively useful is like if
[06:27] you use like apple in your daily life uh
[06:30] you can actually get a Mac Mini and like
[06:32] just put it somewhere in your home
[06:33] connect it to the internet and you can
[06:36] run your agents asynchronously there's
[06:38] no battery life issues you can just log
[06:40] into all your services on your like Mac
[06:42] Mini and um it also can access all the
[06:46] Android ecosystems because Android is
[06:48] actually open um
[06:52] so I work at neither of these companies
[06:55] I can say what I
[06:57] want um so I I think that's like what I
[07:01] think is a feasible um um device to use
[07:05] to like run your AI agent right now um
[07:09] the next thing I want to talk about is
[07:11] like okay why are you talking about
[07:12] local and private why can't you just
[07:14] like run this in the cloud like just
[07:16] subscribe to one of the large tech
[07:19] companies uh agent services and run your
[07:22] life out of it well I want to give you
[07:26] like a few points here uh first is
[07:30] um I want to talk about how this is
[07:33] different from you using other Digital
[07:36] Services and I think it is different
[07:38] meaningfully and I think it's also easy
[07:40] to understand so let's just think about
[07:44] like a lot of you in this room probably
[07:45] use like a cloud email service that is
[07:47] free for all of your life all your taxes
[07:49] are going in there like you know
[07:51] everything personal is going in there
[07:53] why do you trust it the reason I think
[07:56] you trust it at least the reason I trust
[07:58] it is because it has a very simple
[08:01] mental model on how it will act on your
[08:04] behalf or how it will act in general
[08:07] email in reply out it's not um go it's
[08:11] basically not trying to do something
[08:14] sneaky under you that is unpredictable
[08:16] it's a very simple mental model your
[08:18] trust of that service is correlated with
[08:21] whether you understand how it behaves on
[08:23] your behalf so imagine tomorrow if some
[08:27] unknown email service that you've been
[08:28] using forever says oh you know for some
[08:31] of your emails that I have confidence in
[08:33] I can auto reply on your behalf and
[08:36] you're like okay well first of all that
[08:40] might be true but what is the worst case
[08:42] action you can take maybe you'll like
[08:44] reply to my boss like something nasty
[08:48] and like I don't want that to happen and
[08:51] like that's like once the action space
[08:55] becomes powerful enough and
[08:58] unpredictable enough you get
[08:59] uncomfortable with using a service that
[09:01] you're not fully in control um and it
[09:05] can get like worse right like uh
[09:09] companies have to monetize in a million
[09:11] ways and so what if like you're
[09:14] using like like an online service and
[09:17] they suddenly are like oh you know every
[09:20] time you ask for a shopping query we're
[09:21] going to like start making the agent
[09:23] only buy from like stuff that gives us
[09:26] Kickbacks or something so like I think
[09:28] like your personal is so personal to you
[09:30] and so intimate that I feel like
[09:33] ultimately you want to be in control uh
[09:36] on many aspects that you might not have
[09:38] control on eventually when you have to
[09:41] like trust uh an online service so
[09:44] that's like one of the biggest reasons
[09:46] like why I feel I want to build a
[09:48] personal agent that's local uh to myself
[09:51] the second is decentralization like I
[09:53] mean you already see all these
[09:55] ecosystems that are wall Gardens and
[09:57] like fighting with each other and don't
[09:59] allow each other to interoperate in
[10:01] various ways and if you build one of
[10:04] like your personal life uh your personal
[10:06] agent around one ecosystem like is that
[10:10] something like it it works fine for
[10:13] compartment L things like maps and email
[10:15] and various things but like is that
[10:17] something that you want to really
[10:18] subscribe into for like an agent that
[10:21] can take so many different kinds of
[10:24] actions on your behalf uh in your
[10:26] day-to-day life that's like the other
[10:29] reason I I I feel like you should try to
[10:32] we as a world should try to get to like
[10:34] local personalized agents as the
[10:36] norm um and the third one is um for
[10:42] various reasons okay this is what I
[10:44] called uh this is what I call um are you
[10:48] going to be punished for your thought
[10:50] crimes right like okay you have a
[10:51] thought and it is not a good thought and
[10:55] like you know should you be punished for
[10:57] it and usually like the answer is no no
[11:00] now if you have a personal agent that is
[11:02] effectively augmenting you in such an
[11:04] intimate personal way you might be
[11:07] asking it stuff that you generally
[11:10] wouldn't say out loud
[11:12] ever um and in those cases like do you
[11:16] really want to take the risk of like
[11:19] like putting it out into like some
[11:21] provider because like you know you you
[11:23] can actually ask perplexity like
[11:25] Enterprise grade Cloud API contracts
[11:27] that like are like
[11:30] um Enterprise not consumer grade where
[11:32] they like get sloppy even they have to
[11:36] like do a bunch of like legally mandated
[11:39] logging and then safety checks and stuff
[11:42] so there is a possibility that like you
[11:45] might or might not want to take a risk
[11:47] on but for me I'm like I don't want to
[11:50] ever get into a scenario where like I
[11:53] will be like prosecuted or persecuted
[11:56] for my thought crimes and like that I
[11:57] think is like another really powerful
[12:00] argument for myself at least to focus on
[12:02] like local agents for my most personal
[12:07] um uh
[12:08] augmentation so now coming to um well I
[12:13] hope you're convinced that yes yes we
[12:15] actually like if you're going to build a
[12:16] personal AI agent it has to be local and
[12:19] private uh well okay what's the problem
[12:21] well let's go to the technical
[12:23] challenges first first like okay you got
[12:25] to run this stuff right um there are
[12:28] like great open first projects to run a
[12:30] bunch of local models that are one of
[12:32] the key components of these agents VM
[12:35] and SG Lang are pretty great uh they're
[12:38] both built on top of
[12:40] pytorch
[12:43] so effectively uh this is one time like
[12:47] we wrote a bug in pyge and um a bunch of
[12:51] us uh had a Tesla car and Tesla uses
[12:54] pytorch and we were like man like this
[12:58] is so scary because like are we writing
[13:00] bugs on ourselves that's an
[13:03] aside uh it was totally fine the bug was
[13:07] not that
[13:09] bad um so yeah vill esang are great um
[13:13] but local model inference is still as of
[13:16] today slow and limited it's not as fast
[13:18] as like you know if you just use like a
[13:20] cloud service even if you spend like a
[13:22] be like enough money on a beefy machine
[13:26] I think that's also rapidly changing
[13:28] like for example local Al if you're
[13:29] using like a 20 billion or distilled
[13:33] model of some sort it actually runs
[13:35] pretty fast uh but if you want to use
[13:38] like the latest R1 like full unquantized
[13:41] then it runs like super duper damn slow
[13:45] um I think this like is in a state of
[13:49] like it will fix itself so you you
[13:52] probably wouldn't get to run the latest
[13:54] and
[13:54] greatest um and I think like the
[13:58] challenge are not so much the technical
[14:00] and infrastructural challenges like they
[14:02] will kind of get to a place where
[14:04] they're fine I think there's some
[14:05] challenges around like both the research
[14:07] and product that um people need to think
[14:11] a bit more about I think there's a bit
[14:12] of a gap and this is just an open
[14:14] challenge for this room for all of you
[14:16] AI Engineers um one is like the open
[14:20] multimodal models are good but not great
[14:25] I mean they're not great in a couple
[14:26] areas one is like just computer use
[14:29] even the closed models like the latest
[14:31] and greatest apis that you can just pay
[14:33] money for they're not that great for
[14:36] computer use they break all the time so
[14:38] that needs to definitely get like into a
[14:40] better State the other thing like I
[14:42] noticed is like if I ask a model to do
[14:46] shopping for me from clothes to shoes to
[14:49] Furniture to whatever it'll basically
[14:52] give me the most boring right like
[14:55] it's like the basic stuff and if I ask
[14:58] it if I'm like look I'll tell you my
[15:00] tastes and my taste can get very like
[15:03] specific and fine like the more specific
[15:05] I get the more like it gives me
[15:07] like it's like it's like the same oh you
[15:10] asked for like a red velvet sofa with
[15:13] Oak wooden
[15:14] legs uh here's a green sofa that has
[15:18] velvet um and it doesn't have like Oak
[15:21] wooden legs you know like they're not
[15:23] very good at identifying actually
[15:26] visually what you're asking for they
[15:28] mostly rely on like a bunch of text
[15:31] matching um the other thing uh you will
[15:34] notice and this is a big one is we don't
[15:37] have good catastrophic action
[15:39] classifiers what I what do I mean by
[15:41] catastrophic actions
[15:44] is there's many actions an agent can
[15:48] take a lot of them are reversible or
[15:51] harmless like even if it takes the
[15:53] action and that's not the action you
[15:54] wanted it to take it's like whatever oh
[15:56] it had to go to like that particular
[15:59] Wikipedia link but it went to this other
[16:01] one okay big deal whatever it'll just
[16:03] backtrack and go but there's some
[16:05] actions that are actually catastrophic
[16:07] for example you ask it to go purchase
[16:10] like uh a renal of your Tide Pods and
[16:14] then it goes and like purchases a Tesla
[16:16] car you know this is not the best thing
[16:20] for you to do uh and some of these are
[16:22] called catastrophic actions and I don't
[16:25] think there's a lot like there's some
[16:28] open research around like how to really
[16:31] get agents to get good at identifying
[16:33] catastrophic actions before taking them
[16:35] and then maybe like notifying the users
[16:38] instead uh but there's not enough and so
[16:40] if you want to really trust your agents
[16:42] personal or in Cloud I think we got to
[16:45] get a bit better at these
[16:47] things um so that's like a big one and I
[16:52] think open source voice mode is barely
[16:54] there uh I feel like when I need a
[16:56] personal local agent I definitely want
[16:58] voice mode because sometimes I want to
[17:00] talk to it uh and not actually type out
[17:02] everything I want to say um but still
[17:06] why am I bullish about this whole thing
[17:07] I am uh because one I see open models
[17:11] are actually like compounding an
[17:13] intelligence like faster than closed
[17:16] models like based on how many resources
[17:18] are being put on them like what do I
[17:19] mean by that like open AI is only
[17:23] improving their own model anthropic is
[17:24] only improving their own model with all
[17:26] the billions they have or whatever but
[17:28] open models are improving themselves
[17:30] like in coordination across
[17:32] board um and you know people didn't
[17:37] really believe it until Lama came out
[17:39] and they didn't they didn't really
[17:40] believe it until mistol came out and
[17:42] then they didn't really believe it until
[17:43] guac came out uh and then they didn't
[17:46] really believe it until deep sea came
[17:48] out like basically like people are like
[17:51] oh you know like open models you know
[17:54] will not really win but I think they are
[17:57] like basically open source like I've
[17:59] work in open source like all my life um
[18:03] there's a starting coordination problem
[18:05] like initially you don't have enough of
[18:07] a critical mass to coordinate with each
[18:09] other but once you have a critical
[18:11] coordinated Mass open source kind of
[18:14] starts winning in like an unprecedented
[18:17] way and you see that with Linux you see
[18:19] that with a bunch of projects uh so I am
[18:22] pretty bullish that open models would
[18:23] actually start getting like better than
[18:26] closed models um uh um like per dollar
[18:30] of in investment into open models
[18:35] um
[18:37] and that's what I said well okay I have
[18:40] some plugs uh this is like uh gr. in
[18:44] from my friend Ross Taylor who worked on
[18:47] this model called Galactica which got a
[18:50] lot of like um criticism when it was
[18:53] released uh out of meta it was this open
[18:55] science model before Chad GPT released
[18:58] now like doing science with like llms is
[19:01] pretty common but like they got a lot of
[19:03]  when they released uh and he like
[19:06] quit uh he like unreleased Galactica and
[19:09] he quit doing like a bunch of stuff
[19:12] publicly but then like he's working on
[19:14] like plugging the the reasoning gap
[19:17] between open models and closed models
[19:19] and they released a bunch of open
[19:21] reasoning data uh that will help so just
[19:24] a nice quick plug the other quick plug
[19:27] is I work on PCH pytorch is working on
[19:30] enabling local agents especially the
[19:32] technical challenges that I talked about
[19:34] uh and we're hiring so if you are more
[19:37] than an AI engineer if you're an AI
[19:39] engineer who's also like a systems
[19:41] engineer then like py is hiring
[19:48] um well that's what we
[19:52] got the other thing obviously is I
[19:55] welcome you all to come to llama con
[19:59] which is happening on April 29th and
[20:02] save the date it's going to be very
[20:04] exciting lots of llama stuff will happen
[20:06] there that's it uh I think it's in
[20:08] California I I actually didn't look it
[20:11] up
[20:18] [Music]
