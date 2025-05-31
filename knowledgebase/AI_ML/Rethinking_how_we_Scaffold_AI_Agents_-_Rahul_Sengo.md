---
type: youtube
title: Rethinking how we Scaffold AI Agents - Rahul Sengottuvelu, Ramp
author: AI Engineer
video_id: -rsTkYgnNzM
video_url: https://www.youtube.com/watch?v=-rsTkYgnNzM
thumbnail_url: https://img.youtube.com/vi/-rsTkYgnNzM/mqdefault.jpg
date_added: 2025-05-26
category: AI and Data Processing
tags: ['CSV parsing', 'AI integration', 'data schema mapping', 'LLM applications', 'parallel processing', 'machine learning', 'data engineering', 'code interpreters', 'embedding models', 'compute efficiency', 'third-party data', 'schema detection']
entities: ['OpenAI', 'pandas', 'Rust-based ones', 'CSV', 'code interpreter', 'embedding model', 'LM', 'third-party card vendors', 'transaction amount', 'merchant name']
concepts: ['AI-driven parsing', 'classical scripting', 'semantic similarity', 'schema mapping', 'compute efficiency', 'engineer time', 'LLM (Large Language Model)', 'data parsing', 'parallel processing', 'generalized systems']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Python programming', 'CSV data handling', 'machine learning basics', 'data parsing techniques']
related_topics: ['AI in data processing', 'CSV parsing techniques', 'LLM applications', 'data schema mapping', 'parallel computing', 'code interpreters', 'embedding models', 'compute efficiency']
authority_signals: ['"we tried it"', '"we\'d rather have a system that works really well"']
confidence_score: 0.8
---

# Rethinking how we Scaffold AI Agents - Rahul Sengottuvelu, Ramp

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=-rsTkYgnNzM)  
**Published**: 2 months ago  
**Category**: AI/ML  
**Tags**: ai agents, llms, scaffolding, system architecture, scaling with compute, machine learning, ai development  

## Summary

# Summary of "Rethinking How We Scaffold AI Agents" by Rahul Sengottuvelu

## Overview  
Rahul Sengottuvelu, from Ramp, discusses the evolution of building scalable AI agents by leveraging compute power rather than rigid, manual coding. The core argument is that systems designed to scale with increased compute outperform deterministic, hardcoded solutions. He shares examples from Ramp’s work with CSV parsing and highlights the trade-offs between engineering time and computational resources.

---

## Key Points  
1. **Shift from Deterministic to Scalable Systems**  
   - Early approaches involved manually coding for 50+ third-party card vendors, which was brittle and time-consuming.  
   - Introducing LLMs (Large Language Models) allowed for more generalized solutions, though with challenges in reliability.  

2. **Compute as a Scalable Resource**  
   - Systems that utilize compute (e.g., parallel processing, LLMs) can handle arbitrary data formats (e.g., CSVs with unknown schemas) more effectively than fixed, deterministic code.  
   - Example: Parsing CSVs by running LLMs 50 times in parallel, despite higher compute costs, outperformed traditional methods.  

3. **Three Architectural Approaches**  
   - **Deterministic Flow**: Manual code for specific vendors (limited scalability).  
   - **Hybrid Approach**: Combines classical scripting (e.g., embeddings) with LLMs for classification.  
   - **Fully AI-Driven**: LLMs (e.g., code interpreters) process raw data, relying on compute to generalize across formats.  

4. **Trade-Offs**  
   - **Engineer Time vs. Compute**: While engineer time is scarce, modern compute (e.g., cloud resources) is more abundant, making scalable solutions viable.  
   - **Reliability**: LLMs require iterative testing (e.g., unit tests, verifiers) to ensure accuracy.  

5. **Real-World Application**  
   - Ramp’s "Switching Reports" use LLMs to parse third-party CSVs, enabling seamless onboarding for users.  

---

## Important Quotes  
- **Core Idea**: *"Systems that scale with compute outperform rigid, deterministic ones."*  
- **Exponential Trade-Off**: *"What is truly scarce is engineer time... we’d rather have a system that works really well."*  
- **LLM Potential**: *"Running it 50 times in parallel... works really well and generalizes across a ton of different formats."*  

---

## Actionable Items  
1. **Prioritize Scalable Systems**: Design solutions that benefit from increased compute rather than hardcoded logic.  
2. **Leverage LLMs for Flexibility**: Use AI for tasks requiring adaptability (e.g., parsing arbitrary data formats).  
3. **Balance Compute and Engineering Time**: Optimize for compute when engineering resources are limited.  
4. **Iterate with Demos**: Test systems with real-world scenarios (e.g., CSV parsing) to validate reliability.  

--- 

This summary captures the essence of Sengottuvelu’s insights on building AI agents that scale efficiently in an evolving technical landscape.

## Full Transcript

[00:00] [Music]
[00:17] so a little bit about me um had of a
[00:20] plaat ramp I've been working on llms for
[00:23] four years which
[00:25] is
[00:26] well which is uh kind of a long time I
[00:29] guess uh in LM land everything started
[00:31] happening really when chat GPD came out
[00:34] um so I was trying to build what people
[00:36] would Now call an AI agent company back
[00:39] then we were just doing customer support
[00:40] we're trying to make our chat bot
[00:41] smarter we're trying to figure out what
[00:43] what models to use to or what tech to
[00:45] use to get them to respond to customers
[00:48] better and we were messing with gpd2 on
[00:51] BT and models were so frustratingly
[00:53] stupid and context windows were small
[00:55] and they were not very smart reasoning
[00:56] and it was just incredibly annoying and
[00:58] we just wrote lots of code around these
[01:00] models to get them to work at least
[01:02] somewhat
[01:04] reliably and along the way as models got
[01:07] smarter this kind of had to delete more
[01:09] of that code and this ended up seeing a
[01:12] lot of patterns in what what code needs
[01:14] to get deleted how to build agents in
[01:16] what ways that will scale with more
[01:18] intelligence and clearly we're going to
[01:20] continue to get a lot more intelligence
[01:22] and I just wanted to uh maybe talk about
[01:24] a single idea throughout the talk uh
[01:26] through various examples uh we we'll do
[01:28] some uh some uh setting but I'll also
[01:31] have a bunch of demos to kind of like
[01:33] drive home the point and maybe it can
[01:34] convince you guys that uh there's a
[01:36] certain way of building agents that's
[01:37] slightly better than other
[01:40] ways I also built a structur extraction
[01:43] Library called Json former um I think it
[01:46] was the first one I don't I'm not fully
[01:48] sure but timing wise it was before all
[01:50] the other major ones um and that was
[01:52] also scaffolding around a model models
[01:54] were too stupid to up with Json and we
[01:56] were just really begging it pleading
[01:58] pleading it and forcing it to uh in ways
[02:00] that we want it to
[02:01] be so as I said earlier just have a one
[02:04] core agenda item here which is want to
[02:07] convey one idea uh we'll start off all
[02:09] of you probably read the essay bit or
[02:11] lesson just quickly go through what it
[02:13] is uh we'll go through a production
[02:15] agent we have at ramp and how it works
[02:17] and three different ways of architecting
[02:18] it and then I have a demo that to really
[02:21] push maybe how we all think about how
[02:24] software and backends and things will
[02:25] work in the
[02:26] future so very simply the idea is just
[02:30] that systems that scale with compute
[02:32] beat systems that don't so there's two
[02:34] systems and uh without any effort the
[02:37] the system one of the systems can just
[02:39] think more or use more compute in some
[02:41] way that system tends to be systems that
[02:43] are rigid and fixed and just
[02:46] deterministic so from that idea it's
[02:49] pretty clear like if you're Building
[02:51] Systems you might as well build systems
[02:52] that improve with more compute and this
[02:55] this seems pretty obvious like obvious
[02:57] conclusion from the B lesson taking it a
[02:59] step further why is this true it's
[03:01] because exponentials are rare like they
[03:03] just don't exist most things in the
[03:04] world aren't exponential so when you
[03:06] find one you just should hop on strap on
[03:08] just take the free pass and go for the
[03:10] right and probably shouldn't try too
[03:12] hard and there's a lot of examples from
[03:14] history that um to kind of reflect this
[03:17] so for for chess and go and computer
[03:20] vision Atari games like people have
[03:21] tried to build lots of systems and
[03:23] written a lot of code and my way of
[03:25] thinking about rigid systems just like
[03:27] spending a lot of time grinding weekends
[03:29] and writing very clever software well
[03:32] abstracted uh maybe trying to synthesize
[03:34] human reasoning and thought process into
[03:36] features and then using them in clever
[03:38] ways and trying to approximate how a
[03:40] human would
[03:41] think and if you actually fix the amount
[03:43] of compute that approach will win but if
[03:45] you just turns out if you end up scaling
[03:48] out how much search you're doing the
[03:50] general method always ends up winning
[03:53] even uh like in all these cases so Atari
[03:55] go and computer
[03:56] vision a little bit about ramp so ramp
[03:59] is a finance platform that helps
[04:01] businesses manage expenses payments
[04:03] procurement travel bookkeeping more
[04:06] efficiently and we have a ton of AI
[04:08] across the product so automate a lot of
[04:10] boring stuff the finance teams do and
[04:11] employees do with uh submitting expense
[04:14] reports and booking your flights and
[04:16] hotels and uh submitting reimbursements
[04:18] all that and so a lot of the work behind
[04:20] the scenes is just we're interacting
[04:22] with other systems um and helping like
[04:24] Legacy systems and helping employees get
[04:26] their work done
[04:27] faster so let's actually talk through
[04:29] one of the systems we have today at ramp
[04:31] and um maybe some talk through the
[04:33] different versions of the system and how
[04:35] it evolved over
[04:36] time so we're going to talk about
[04:38] something called a switching report it's
[04:40] very simple agent all it needs to do
[04:42] it's taking a CSV a CSV arbitrary format
[04:45] so the schema could be seriously
[04:48] anything from the internet and we want
[04:51] these csvs to come from third party card
[04:53] providers so when people on board to
[04:54] ramp we want to give them a nice
[04:56] checklist and say hey here are all the
[04:57] transactions you have on other platforms
[04:59] and we want help you move them over and
[05:01] the more transactions come on ramp the
[05:03] more we can help you and the more you'll
[05:04] use our software and more everyone
[05:05] benefits and so the switching reports
[05:07] just really a checklist but to read
[05:09] people's CSV transactions we need to
[05:12] understand those and other platforms
[05:14] have all these kinds of crazy
[05:16] schemas and so the the description of
[05:18] the problem we have here is just for an
[05:21] arbitrary arbitrary like CSV how can we
[05:24] support um parsing it and then into some
[05:27] format that we we understand
[05:30] so let's just start with the the simple
[05:32] approach right is like let's just take
[05:34] the 50 most common third party card
[05:36] vendors um and just manually write code
[05:38] for all of them now obviously like this
[05:41] this will just work it is some work not
[05:43] a lot of work but you still have to
[05:47] maybe go to 50 different platforms and
[05:49] download their csvs see what schemas
[05:51] they have and then write code maybe if
[05:53] they decide one day they change their
[05:55] format your thing will break but that's
[05:56] okay you'll get page and you can wake up
[05:58] and go fix it
[06:01] so let's maybe introduce some LMS in
[06:03] here so from the over engineered code
[06:06] where you ended up writing 100,000 lines
[06:08] maybe we don't we don't we want a more
[06:09] General system so let's introduce a
[06:11] little bit of LM a little bit of AI in
[06:13] here and so in the deterministic flow
[06:17] let's maybe add some or just like
[06:18] scripting In classical scripting land
[06:21] let's add some more um call to open AI
[06:24] or you have an embedding model you want
[06:25] to do semetic similarity or something
[06:27] like that so then let's just take every
[06:29] column in the CSV that comes in let's
[06:31] try to classify what kind of column it
[06:32] is is it a date is it a transaction uh
[06:35] is it a transaction amount is it a
[06:36] merchant name or is it the uh users's
[06:38] name and then we map it on and then we
[06:41] probably could uh end up in a schema
[06:44] that we're happy with again most of the
[06:47] compute is running in classical land
[06:49] some of it is running in fuzzy llm land
[06:52] but this is somewhat looking like a more
[06:54] General
[06:56] system let's go maybe a different
[06:58] approach when like we just go all the
[06:59] way through let's just say we're just
[07:01] going to literally give the CSV to LM
[07:03] and say you have a code interpreter so
[07:06] you can write whatever code you want
[07:07] pandas or all the faster rust based ones
[07:11] um you have all these python packages um
[07:14] you're allowed to look at the head of
[07:15] the CSV the tail whichever rows you want
[07:17] um and then I just want you to give me a
[07:20] CSV uh with this specific format here's
[07:23] a unit test here's a verifier that you
[07:25] can use to tell if it's working or not
[07:28] turns out this approach actually doesn't
[07:29] work like we tried it um if you only run
[07:31] it once but instead if you run it 50
[07:34] times in parallel it's actually very
[07:36] likely that it works really well and
[07:38] generalizes across a ton of different
[07:40] formats the amount of compute here is
[07:43] actually probably like what is that
[07:45] number 10,000 times more than the the
[07:48] first approach we came up with but again
[07:50] like what is truly scarce in the world
[07:51] is engineer time maybe not for not in a
[07:53] while but at least today and we'd rather
[07:56] have a system that works really well and
[07:58] even with a 10,000 times more compute it
[08:00] will probably cost less than a dollar
[08:01] and every transaction that switched over
[08:03] every fail CSV will cost ramp way more
[08:05] money than whatever money we spend on
[08:07] this exact this exact
[08:09] architecture so this is a very specific
[08:12] uh example it's like how does this apply
[08:14] to the agents that we all build and
[08:16] maybe the systems we're all working on
[08:18] turns out something like this actually
[08:20] generalizes so if you look at three
[08:22] approaches and let's assume like The
[08:24] Black Arrow is just classical compute
[08:27] and then the blue arrows are fuzzy lands
[08:29] so it goes into neuron net and all all
[08:31] sort of weird matric multiplication
[08:33] happens and we're in latent space and
[08:35] gets all alien intelligency and then
[08:37] comes back to a classical land first
[08:39] approach there was no AI we just wrote
[08:41] code and it just worked mostly the
[08:44] constrainted agent so the second
[08:45] approach we broke into fuzzy land from
[08:48] classic land when when we decided we
[08:51] wanted similarity scores or something
[08:52] like that and then the third approach is
[08:54] actually flipped where the llm decides
[08:58] it needs to go into classical l so it
[08:59] write some code write some pandas or uh
[09:01] python code and it decides to break in
[09:04] into this classical land when it needs
[09:06] to but most of the computer is
[09:08] fuzzy actually this is maybe not the
[09:11] most accurate graph like because I
[09:13] propos that we run it 50 times it more
[09:15] so looks like this but if you look at a
[09:18] back end in general they're all request
[09:20] response so some sort of message is
[09:22] going in it's like a post request or get
[09:24] or update or read any sort of credit
[09:27] operation and we're really just asking
[09:28] the back end to take this piece of
[09:30] information do whatever you must with it
[09:32] run out whatever mutations you want and
[09:34] return me a
[09:35] response and almost all systems we've
[09:38] built so far as like Humanity I guess
[09:39] like look like the first one but more
[09:42] people are using open AI open AI makes
[09:44] billions of dollars and probably a lot
[09:46] of the systems that use them look like
[09:48] number two where just regular uh
[09:51] programming languages are calling into
[09:53] open AI servers and we're running some
[09:54] fuzzy
[09:55] compute what we're seeing in like more
[09:58] and more parts of the ram codebase we're
[09:59] moving to the third approach because it
[10:02] just tends to work well because all the
[10:05] blue arrows if you did nothing it Absol
[10:07] absolutely nothing we all went to
[10:08] vacation for the next year the big labs
[10:11] are still working and spending billions
[10:13] of dollars making those models better so
[10:15] the blue arrows will get better and so
[10:17] how much blue arrow you're using in your
[10:19] code base actually will help directly
[10:21] your company without much effort from
[10:23] your end so this is what I was saying is
[10:24] like the bit or lesson is just so
[10:26] powerful and exponential Trends are so
[10:28] powerful that you can just hitch hitch
[10:30] the
[10:33] ride let's um let's take this idea like
[10:39] further um let's actually like go all
[10:41] the way like something something
[10:44] crazy um on the left you'll see a
[10:47] traditional web app so usually the way
[10:49] it works is you open um
[10:51] gmail.com and some uh static file server
[10:56] and Google sending you bunch of
[10:58] JavaScript HTML and CSS your browser
[11:01] renders that um and shows you some nice
[11:03] UI nice HTML that's user friendly maybe
[11:06] you see some emails maybe you click on
[11:07] one of them um the friend end makes a
[11:10] request to the back end the back ask the
[11:12] friend end friend end asks the back end
[11:14] give me the content for email and
[11:16] whatever ID it is and then the back in
[11:18] hits database and gives you the result
[11:20] and maybe they use cod genen maybe they
[11:23] use all the Coden tools available to
[11:24] make Gmail so that that was probably the
[11:27] LM only worked when the software
[11:29] engineer was writing the code but once
[11:31] the code is written and it's like pushed
[11:33] to production it's just classical
[11:36] compute and on the right I'm actually
[11:38] proposing a different model which is the
[11:40] back end is the LM it's not Cen it's
[11:43] this LM is doing the execution it is the
[11:46] back end so the LM has access to tools
[11:49] like coder interpreter and potentially
[11:51] has access to um through that making
[11:54] request Network requests and also has an
[11:57] access to uh DB
[12:00] so I have a mail client actually that
[12:02] works with this principal and this is my
[12:05] test email so if y'all want to see any
[12:08] emails you sent to me in a minute or so
[12:11] you can send me an email but please be
[12:13] nice
[12:36] all right I think um it's probably
[12:38] enough
[12:39] time so I'm going to go
[12:56] over so we have this email client I mean
[12:59] we still have some regular JavaScript to
[13:02] hook into the LM hook the LM into the
[13:04] browser but when I do log in I'm going
[13:06] to use my email is just showing you
[13:16] [Music]
[13:40] what oh it's
[13:45] probably okay we're good we're good all
[13:47] right we're
[13:48] saved I
[13:53] think thankfully I have a room full of
[13:55] Engineers
[13:59] so there's a dot but the reason it's so
[14:01] slow is because when I open this page
[14:03] and log into Gmail the Gmail token is
[14:05] actually being sent to an llm we're
[14:07] saying literally this is a LM chat
[14:09] session what we're we're seeing on the
[14:11] screen is like hey LM you're you're
[14:14] actually simulating a Gmail client you
[14:16] have access to Oh all the emails you
[14:20] have access to um rahul's Gmail token
[14:23] and aord interpreter and so just render
[14:26] some UI based on uh what you think is
[14:29] reasonable for the homepage for Gmail
[14:31] client and so looks like it decided to
[14:33] render his markdown uh I think we
[14:34] actually tell it to render his markdown
[14:36] and it's rendering all the emails that a
[14:38] bunch of people sent me from here so it
[14:40] looks like it says uh hello from
[14:41] California so I'm going to click on that
[14:45] when I click on that we're actually not
[14:46] running um any like backend calls or
[14:48] anything like that we're just telling
[14:50] the LM the user clicked on that piece of
[14:51] text in this case it was hello from
[14:53] California and the ID number so the LM
[14:56] now has the information on what the user
[14:57] clicked on and it has the chance to
[14:59] render the page much like a web
[15:01] framework would so again it goes back it
[15:03] probably hits uh a get request for that
[15:06] specific email and pulls the
[15:08] body what is this agent going to do I'm
[15:10] watching you live so the LM just decided
[15:13] this is the appropriate UI for a Gmail
[15:17] client also I have other features the LM
[15:20] thought was reasonable so looks like I
[15:21] could mark it as unread or or delete the
[15:23] email if I want to uh maybe I'll delete
[15:25] it because it's not that good of an
[15:26] email I'm sorry
[15:34] it is very slow because we're doing a
[15:35] lot but wanted to push you in this
[15:37] direction because this kind of software
[15:40] barely
[15:42] works
[15:44] dang I guess not um also I clicked on it
[15:49] and now the LM is trying to do something
[15:51] with me clicking on it anyway um this
[15:54] kind of software barely works today and
[15:56] it doesn't mean it w won't work in the
[15:57] future uh but exponential trends like
[16:00] things might just like this might just
[16:01] take off um so just wanted to push you
[16:04] all to think in this direction um yeah
[16:07] Will software more software look like
[16:09] this I don't know we'll see thank you
[16:13] [Music]
