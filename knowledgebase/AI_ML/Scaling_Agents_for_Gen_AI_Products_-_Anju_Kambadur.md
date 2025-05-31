---
type: youtube
title: Scaling Agents for Gen AI Products - Anju Kambadur, Bloomberg Head of AI Engineering
author: Channel Video
video_id: b2GqTDWtg6s
video_url: https://www.youtube.com/watch?v=b2GqTDWtg6s
thumbnail_url: https://img.youtube.com/vi/b2GqTDWtg6s/mqdefault.jpg
date_added: 2025-05-26
category: AI and Financial Research
tags: ['AI', 'finance', 'NLP', 'data analytics', 'machine learning', 'AI ethics', 'MLOps', 'transparency', 'financial research', 'AI applications']
entities: ['Bloomberg', 'Reuters', 'AI', 'Q&A segment', 'earning season', 'transcripts', 'structured data', 'research analysts', 'quarterly calls', 'public companies']
concepts: ['AI applications in finance', 'NLP for transcripts', 'data analytics', 'machine learning models', 'AI ethics', 'remediation workflows', 'circuit breakers', 'precision in AI', 'transparency in AI', 'structured data processing']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['AI in finance', 'NLP basics', 'data analytics', 'machine learning concepts', 'MLOps']
related_topics: ['AI in finance', 'NLP applications', 'data analytics in research', 'machine learning models', 'AI ethics', 'MLOps', 'AI transparency', 'financial data processing']
authority_signals: ['we saw an opportunity to say well we know...', 'there was a lot of work done in order to just build remediation workflows', 'these should ground you in the kinds of challenges...']
confidence_score: 0.7
---

# Scaling Agents for Gen AI Products - Anju Kambadur, Bloomberg Head of AI Engineering

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=b2GqTDWtg6s)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: generative ai, ai engineering, machine learning, scaling ai, large language models, ai products, open source  

## Summary

# Summary of "Scaling Agents for Gen AI Products" by Anju Kambadur

## Overview  
Anju Kambadur, Bloomberg’s Head of AI Engineering, discusses Bloomberg’s approach to building AI agents for financial research analysts. The talk covers the transition from in-house large language model (LLM) development to leveraging existing AI tools, challenges in scaling AI while maintaining non-negotiable principles (e.g., precision, transparency), and the role of data in training and deploying AI systems. Key focus areas include addressing the needs of research analysts, managing data scale, and ensuring reliability in AI outputs.

---

## Key Points  
1. **Shift in AI Strategy**  
   - Bloomberg initially built its own LLMs but shifted to leveraging external AI tools in 2023, prioritizing efficiency and scalability.  
   - Emphasis on **remediation workflows** and **circuit breakers** to address AI limitations (e.g., accuracy, factuality).  

2. **Organizational Structure**  
   - A dedicated AI team operates as a "special group" with cross-functional collaboration across engineering, product, and domain experts.  
   - Focus on **specific use cases**, such as aiding research analysts in processing financial data.  

3. **Defining Agents vs. Tools**  
   - A critical distinction is made between **tools** (e.g., search, summarization) and **agents** (e.g., autonomous decision-making).  
   - The need for clear frameworks to differentiate and integrate these components.  

4. **Data Scale and Challenges**  
   - Bloomberg handles **40+ years of historical data**, including 400 billion daily data points (e.g., news, earnings calls, structured financial data).  
   - Challenges include managing unstructured data (e.g., transcripts) and ensuring **precision, speed, and transparency** in AI outputs.  

5. **Non-Negotiable Principles**  
   - Key requirements for all AI products:  
     - **Precision** and **comprehensiveness**  
     - **Speed** and **throughput**  
     - **Data privacy** and **transparency**  
   - These principles apply regardless of whether AI is used.  

6. **Use Case: Research Analysts**  
   - Focus on helping analysts with tasks like:  
     - Search, discovery, and summarization of unstructured data (e.g., earnings call transcripts).  
     - Structured data analytics and model-building.  
     - Communication with colleagues for information sharing.  
   - Example project: Automating **earnings call analysis** to surface relevant questions for analysts.  

---

## Key Quotes  
- *"We know what for every company which is operating in a particular sector we know what are the kinds of questions are of interest..."*  
- *"Precision, comprehensiveness, speed, throughput, availability... these are non-negotiables."*  
- *"The scale at which we are working is 40 years of history, 400 billion data points every day."*  

---

## Actionable Insights  
- **Prioritize remediation workflows** to address AI limitations (e.g., accuracy, factuality).  
- **Maintain strict principles** (transparency, data privacy) even as AI scales.  
- **Focus on specific user needs** (e.g., research analysts) to design targeted AI solutions.  
- **Leverage existing AI tools** strategically, balancing innovation with reliability.  
- **Invest in circuit breakers** to ensure AI outputs are trustworthy for high-stakes financial applications.  

--- 

This summary captures the core strategies, challenges, and priorities discussed in the talk, emphasizing Bloomberg’s approach to balancing AI innovation with operational rigor.

## Full Transcript

[00:00] [Music]
[00:17] thank you so much for inviting me um as
[00:19] I was trying to think what would be a
[00:21] good topic to present at this talk the
[00:23] organizers were really nice and so a lot
[00:25] of things that you'll hear today was
[00:27] influenced by what the organizers
[00:29] thought was important cuz there really
[00:30] so many things happening that are
[00:32] exciting to talk about in the agentic
[00:34] landscape so let's get started the first
[00:36] thing was um late 2021 I think LMS
[00:40] really uh were starting to capture the
[00:42] imagination as a company we've been
[00:44] investing in AI for almost almost 15 16
[00:46] years so we decided we'll build our own
[00:48] um we'll build our own large language
[00:50] model took all of 2022 to do that and
[00:55] 2023 we wrote a paper about it we had
[00:57] learned a lot about how do you build
[00:58] these models how do you organize uh data
[01:00] sets for these how does evaluation work
[01:02] how do you Cox performance in certain
[01:04] zones out of this but then chat GPT
[01:06] happened I think the open weight and the
[01:07] open source Community has come up so uh
[01:10] beautifully along so while we continue
[01:12] to do very similar
[01:14] work as a strategy we pivoted to say
[01:17] let's build on top of uh whatever is
[01:19] available out there we have many many
[01:21] different use cases so I think we we
[01:23] pretty much pivoted to say We'll build
[01:25] on top uh if it helps you in any way on
[01:28] how we are doing things so there you go
[01:32] uh the other was uh I think there was a
[01:34] curiosity on how exactly uh does a
[01:36] company like Bloomberg organize its AI
[01:38] efforts so um I report into I report to
[01:42] the uh Global head of engineering and we
[01:44] are organized somewhat as a special
[01:47] group if you will we work a lot with our
[01:49] data counterpart Bloomberg is a really
[01:50] strong large data organization that you
[01:54] can appreciate now helps us out a lot uh
[01:56] we work with the product the CTO in in
[01:58] cross functional settings about 400
[02:00] people 50 teams London New York uh
[02:03] Princeton and Toronto so that's a little
[02:05] bit about our our
[02:07] group okay so um we've been uh Building
[02:12] Products using generative AI um starting
[02:16] with tools more agentic for 12 to 16
[02:19] months now I think the effort has been
[02:21] really really serious and so there have
[02:23] been so many things we've had to solve
[02:26] in order to build something today using
[02:28] what's available today uh and then I
[02:30] decided somebody must cover all of these
[02:33] topics so I'm not going to talk about
[02:35] these at all right uh I think there are
[02:37] some wonderful speakers talking about
[02:40] this uh I'll try to hang around a bit
[02:43] after this and I'm really um I'm really
[02:47] bullish on what the developments are in
[02:50] any one of those challenges that we need
[02:51] to solve I think it gets easier and
[02:53] easier to solve those challenges so
[02:54] please don't read these as being
[02:56] pessimistic it's just realistic right I
[02:59] need to build and ship things today and
[03:02] that means these are the things I need
[03:03] to deal with today uh again we won't be
[03:05] touching on any of these topics
[03:09] today um so internally it was really
[03:12] hard to say what's an agent and what's a
[03:14] tool because everyone kind of had their
[03:16] own vocabulary and then this really nice
[03:17] paper came out so when I'm talking today
[03:20] when I say a tool I mean on the left
[03:22] hand side of that uh it's cognitive
[03:24] architectures for for language agents if
[03:26] you haven't read it you should uh try to
[03:28] read that paper and then an agent is
[03:30] really like more autonomous has memory
[03:32] can evolve so whenever I say agentic
[03:34] it's on the right hand side of the
[03:35] spectrum and the other one is the left
[03:37] hand side um so that's what my
[03:40] vocabulary will
[03:42] be finally to set the stage for the talk
[03:45] um I don't know how many of you know
[03:46] about Bloomberg I certainly did not know
[03:49] as much as I do today when I joined so
[03:51] um we are a fintech company as you can
[03:54] imagine from my nice uh jacket or
[03:58] jumper and our clients are in finance
[04:01] but Finance is a very diverse field so
[04:04] uh I'm listed here 10 different
[04:06] archetypes of people who are in finance
[04:08] and they do very different activities
[04:11] but they also do a lot of similar
[04:12] activities and so um what is like a
[04:15] short form of thinking what Bloomberg
[04:17] does we have we both generate and
[04:20] accumulate a lot of data this is
[04:22] unstructured and structured so news
[04:24] research uh documents slides we uh also
[04:28] provide access to we we sites there's a
[04:30] lot of reference data uh Market data
[04:32] coming in so if you just want to know
[04:34] the scale every day we get 400 billion
[04:38] pics of structured data information
[04:40] about a billion plus um unstructured
[04:44] messages millions of well-written
[04:47] documents which include news and this is
[04:48] just every day and we have over 40 years
[04:50] of history on it so when we say we offer
[04:54] information as one of the things to our
[04:57] clients this is the scale at which we
[04:59] are working
[05:02] uh the rest of this talk I will uh as
[05:04] you can imagine we are building a very
[05:07] broad set of products so to focus the
[05:10] talk I'll talk about one
[05:12] particular uh archetype uh research
[05:15] analyst if you didn't know what a
[05:17] research anal is done here is a does
[05:20] here is a short course so uh there's a
[05:23] research analyst they are typically an
[05:24] expert in a particular area think like
[05:27] you know I'm a research analyst in AI or
[05:28] semiconductors or technology or electric
[05:31] vehicles and the kinds of things they
[05:34] need to do on a daily basis are written
[05:35] at the bottom so they are doing a lot of
[05:40] work with search and Discovery and
[05:42] summarization a lot of things with
[05:44] unstructured data on the leftand side
[05:46] they are doing a lot of work in uh in
[05:49] data and analytics structured data and
[05:51] analytics in the middle part of the
[05:52] segment they are reaching out to their
[05:54] colleagues both to disperse and gather
[05:57] information so there's a lot of
[05:58] communication and then they're also also
[06:00] uh some of them are also building models
[06:03] uh which means they need to normalize
[06:04] data they need to actually program and
[06:06] generate models as well so this is a a
[06:08] research analyst in a uh in a
[06:12] nutshell uh the other bit is because we
[06:15] are in finance and we've been here for
[06:17] we've been in finance for like since
[06:18] founding 40 years ago there are some
[06:21] aspects of our products that are
[06:23] non-negotiable and uh those include
[06:25] things like precision comprehensiveness
[06:27] speed throughput availability um some
[06:30] principles like protecting our
[06:32] contributor and client data making sure
[06:34] that whatever we build there is
[06:36] transparency throughout these are
[06:38] non-negotiables it doesn't matter
[06:39] whether you're using AI or not so these
[06:41] should ground you in the kinds of
[06:43] challenges we face when we use what's
[06:44] available today to build
[06:47] agents okay so what was the first thing
[06:49] we did uh again 2023 is when I think we
[06:52] got serious so the first thing we did
[06:54] was for the research in the in the zone
[06:57] of helping the research analyst
[06:59] community
[07:00] um companies public companies in
[07:02] particular they have scheduled quarterly
[07:05] calls that discuss the health of their
[07:07] company they talk about their future
[07:09] it's a conference call a lot of analysts
[07:11] attend the call uh there's a
[07:13] presentation by the company's Executives
[07:15] and then there's a Q&A segment and
[07:17] during earning season it happens that on
[07:21] any given day many many of these things
[07:23] are happening so I told you that a
[07:24] research analyst has to stay on top of
[07:27] what's happening every single day so
[07:30] so transcripts of these calls need to be
[07:33] generated again AI is used and in 2023
[07:37] we saw an opportunity to say well we
[07:38] know what for every company which is a
[07:41] which is operating in a particular
[07:43] sector we know what are the kinds of
[07:45] questions are of interest and maybe we
[07:47] can try to answer them for the analyst
[07:50] to take a look at and that way they can
[07:52] be informed on whether they wanted to
[07:53] deeper dive or not right seems like a
[07:55] simple product and again I'm talking
[07:56] about work that started in 23 so
[08:00] where the technology was we still needed
[08:02] to do a lot to bring it to the market
[08:05] keeping our principles and features in
[08:07] place so what does it mean just focus on
[08:08] the right hand side if you will um
[08:11] performance out of the box was not great
[08:13] like Precision accuracy uh factuality
[08:16] things like that uh and for those of you
[08:19] who are interested in mlops I think
[08:21] there was a lot of work done in order to
[08:24] just build remediation workflows and
[08:26] circuit breakers because remember these
[08:28] summaries are not somebody just chatting
[08:29] with a transcript it's actually
[08:32] published and everyone gets to see the
[08:34] same summary and anything that is an
[08:36] error has an outsized impact for us so
[08:38] we constantly monitor performance
[08:40] remediate and then the summaries get
[08:42] more and more accurate so a lot of um I
[08:46] think a lot of monitoring goes in behind
[08:47] it a lot of cicd goes in behind it as
[08:49] well okay so today how are the products
[08:54] that we are building how does the
[08:55] agentic architecture look like well
[08:57] first of all it's semi- agentic because
[08:59] I don't this is an opinion we don't yet
[09:03] fully have the trust that everything can
[09:05] be autonomous so there are some pieces
[09:07] that are autonomous the other pieces
[09:09] that are not autonomous guard rails is a
[09:11] classic example of for example Bloomberg
[09:12] doesn't offer Financial advice so if
[09:15] someone starts with hey should I invest
[09:17] in then you know you need to catch it we
[09:19] need to be factual that's again a
[09:20] guardrail so like those are not optional
[09:23] pieces for any agent those are coded in
[09:26] as you must uh you must do this check so
[09:29] just take this keep this image in mind
[09:31] it'll come back okay so this is about
[09:35] this is a talk about scaling so with
[09:37] that long Runway let's get to scaling so
[09:39] I just wanted to cover two aspects of
[09:41] scaling I'm hoping that both these
[09:44] aspects will be more of a confirmation
[09:46] and not a surprise to any of you um so
[09:49] let's see so the first thing is if you
[09:50] want to build agents and you want each
[09:52] agent to evolve really quickly because
[09:55] when you build the first time unless
[09:57] you're a magician it's going to suck a
[09:59] bit and then it needs to improve and
[10:01] improve and improve right so how do you
[10:02] get there well let's go back to how some
[10:07] really good software is built when I was
[10:08] a grad student I use matrix
[10:09] multiplication a lot and this is a
[10:12] snapshot of the generalized Matrix
[10:15] matrix product and if you read the API
[10:18] documentation it lays out every aspect
[10:21] of the input every error code how long
[10:24] it will take is also available in
[10:26] documentation it's just it just works
[10:29] right and when you build software on top
[10:31] of such really well documented
[10:33] well-written software your software also
[10:36] tends to be robust your products tend to
[10:37] be robust even from 20 years ago when we
[10:41] started using machine learning to build
[10:43] products like you know there are tools
[10:44] like apis that use models or pipelines
[10:47] of models behind them you as a caller or
[10:50] a person Downstream of such apis there
[10:54] is a bit of stoas stochasticity if I can
[10:56] pronounce it correct uh in right you
[10:59] don't quite know what the result will be
[11:03] and you don't quite know if it'll work
[11:05] for you or not and this is despite best
[11:07] intentions of establishing you know what
[11:09] the input distributions are and what the
[11:11] output distributions are there's always
[11:12] a bit of stochasticity it was still okay
[11:14] to work with them and I'll tell you why
[11:16] it was okay to work with these but when
[11:18] you enter using llms and agents which
[11:22] are really compositions of llms the
[11:25] errors multiply a lot and that is
[11:29] something that causes a lot of fragile
[11:32] behavior and I and we'll just take a
[11:35] look at it and and I I hope my answer is
[11:38] mildly surprising to you on how to avoid
[11:40] the
[11:40] fragility um in 2009 we
[11:43] built uh a news sentiment product it was
[11:47] basically to detect if a piece of news
[11:50] for a given company would be beneficial
[11:53] for that company or
[11:54] not so the input distribution we knew
[11:57] which news wires we were monitor
[11:59] monitoring we knew which language it was
[12:01] in news wires also have editorial
[12:03] guidelines on how they write things so
[12:04] well it's while this while the API that
[12:08] sits in front of the model is not as
[12:09] clean as like Matrix Matrix multiply you
[12:11] still have a very decent handle on okay
[12:13] what is coming into my system and the
[12:15] outputs are obviously just like you know
[12:17] it's minus one to plus one pretty much
[12:19] so like the output space is also very
[12:21] easy training data we built it from
[12:23] scratch so we know the training data we
[12:25] could have really nice held out in time
[12:26] and space um
[12:29] test sets and then we could establish
[12:31] the risk of deploying this we could
[12:33] monitor it so despite all of this guard
[12:38] rail being present we still ended up
[12:41] having a lot of outof band communication
[12:42] on anyone who's Downstream of us so for
[12:44] example if you were consuming our stream
[12:47] of output on sentiment we would give you
[12:49] a heads up we would tell you that hey
[12:50] the model version is changing if you
[12:52] have a downstream application using this
[12:54] as a signal you want to test it out
[12:56] things like that this was the landscape
[12:59] that's changed a lot when you think
[13:02] about building agentic architectures
[13:03] like you want to make improvements to
[13:05] your agents every single day you don't
[13:07] want to have a release cycle where there
[13:08] is a you know a purely batch regression
[13:13] test based release cycle because there
[13:15] are so many customers who are Downstream
[13:16] of you who are also making independent
[13:18] improvements to your model so I'll give
[13:20] you like one small example right so uh
[13:24] one of the one of the workflows that we
[13:25] have agents for is um for a research
[13:28] analyst is uh I told you that structured
[13:30] data is something that they look at the
[13:31] question here is US CPI for the last
[13:34] five quarters Q is just a quarter
[13:36] there's an agent that deeply understands
[13:38] the query uh figures out what domain it
[13:40] should dispatch to and then uses a tool
[13:42] it's there's an NLP front end to the
[13:44] tool but uses a tool to basically fetch
[13:45] the data right
[13:49] um turns out that the data is wrong and
[13:52] which is why you need the guard rails
[13:54] the data is wrong because of one
[13:56] character that was missed uh it monthly
[13:59] data as opposed to quarterly data and if
[14:02] you're actually building a downstream
[14:04] workflow where you're not even exposing
[14:05] the table a good research analyst would
[14:07] catch it but if you're not even exposing
[14:09] the table and you're just looking at an
[14:11] answer that says well it looks like the
[14:13] answer is 42 it's really hard to catch
[14:16] these compounding errors which is
[14:18] why it is easier to not count on the
[14:23] Upstream systems to be accurate but
[14:26] rather factor in that they will be
[14:28] fragile and they'll be evolving and just
[14:30] do your own safety checks even in like
[14:32] I'm talking about within my own arc
[14:35] people are independently operating every
[14:37] version of the data and analy analytics
[14:39] API tool that's coming out is better and
[14:41] better but being better means being
[14:43] better on average it doesn't mean it'll
[14:45] be better for you as a downstream
[14:47] consumer so building
[14:49] in some of
[14:51] this um guard rail I just think is good
[14:55] sense and that almost makes you go
[14:58] faster as as you factor out individual
[15:00] agents and each agent can evolve without
[15:02] having these handshake signals of well
[15:06] every Downstream caller I have I have to
[15:09] make sure that they understand what's
[15:10] changed and they sign off that I can
[15:13] actually release my I can promote my um
[15:16] new agent to like beta or production I
[15:18] think we just need to like change that
[15:21] mindset and be more
[15:23] resilient so that's one the second thing
[15:26] is as much as I used to code one one one
[15:29] fine day long long ago I'm a manager now
[15:32] so I thought I'll talk about Arc
[15:33] structure and I don't know how many of
[15:34] you will um resonate with it Bloomberg
[15:37] like I said we've been building these
[15:38] things for like 15 years and traditional
[15:40] machine learning um it has a particular
[15:44] factorization of software and that
[15:47] software factorization is then reflected
[15:49] in the arc structure if you are lucky
[15:51] you have the reverse Conway uh law of
[15:54] design but you but you really need to
[15:57] rethink that as you start using
[16:00] different text stacks and start building
[16:02] different kinds of products um what do
[16:05] what do I
[16:06] mean how many agents Do you want to
[16:08] build and what should each agent do and
[16:11] should agents have overlapping
[16:13] functionality or not these are some
[16:15] basic questions and typically it's very
[16:18] tempting to just say let's just keep our
[16:20] current software stack and see if we can
[16:22] build on top of that or let's keep our
[16:24] current Arc structure and build on top
[16:25] of that and so what I've learned
[16:31] is on the columns here you can see you
[16:35] know the first two columns are
[16:36] vertically aligned teams the next two
[16:38] columns are horizontally aligned teams
[16:40] and there are some properties in the
[16:41] rows and what we've learned and we've
[16:44] actually done some reog what we've
[16:46] learned are in the beginning you don't
[16:48] really know much on what the product
[16:49] design is going to be and you want to
[16:50] iterate fast it's just easier to like
[16:53] collapse The Arc collapse the software
[16:55] stack and just say here has a team go
[16:58] build what needs to be built and figure
[17:00] things out and that's where you want
[17:01] like you know really fast iteration you
[17:03] want sharing of code data models things
[17:06] like
[17:07] that the more you have understood this
[17:10] for a single product or a single agent
[17:13] the more you understand what its use is
[17:16] and what it's good at and what it's not
[17:18] and you actually build many many of
[17:20] these agents and that's when you start
[17:21] thinking okay I can go back to the
[17:24] foundations of building good software
[17:26] and good Orcs And I want to have things
[17:29] like optimization on it so I want to
[17:31] increase the performance reduce the cost
[17:33] make it more testable make it more
[17:35] transparent and that's where you move
[17:36] into the bottom right corner of the
[17:38] segment where you do have some
[17:39] horizontal so in our case like guard
[17:41] rails are horizontal we don't want every
[17:44] team every one of those 50 teams like
[17:47] trying to figure out what does it mean
[17:49] for me to not
[17:52] accept user inputs that are thinly
[17:56] wailed Financial advice inputs right
[17:58] like like it's something that you want
[17:59] to do horizontally but you don't also
[18:01] don't want to you want to figure out for
[18:02] yourself what is the right
[18:04] time uh for you and your organization to
[18:07] start creating horizontals to also start
[18:09] breaking out some of these
[18:12] monolithic agents which are reflected
[18:14] again in your structure and start
[18:15] creating smaller and smaller
[18:17] pieces so all that said and done like
[18:21] you know just again for the uh running
[18:24] example of a research agent this is how
[18:26] it looks like today so you know I think
[18:28] taking in the user user world and and
[18:31] session context and deeply understanding
[18:33] what is the question and then figuring
[18:34] out what kinds of information are needed
[18:36] to answer that question uh it's
[18:39] factorized as its own agent uh reflected
[18:41] in the art structure same similarly for
[18:43] answer generation we have a lot of uh
[18:45] rigor around what constitutes a
[18:47] well-formed answer again that's factored
[18:49] out I call it semi agentic like I
[18:50] alluded to before because we do have
[18:52] guard rails that are non optional there
[18:54] is no autonomy there you have to call it
[18:56] at multiple points um and then yeah like
[18:59] we build on top of like years of
[19:02] traditional uh and more and more modern
[19:05] forms of data monging like you know your
[19:10] sparse indices have become dense and
[19:12] hybrid indices now so yeah that's a
[19:13] little bit and I think I'm brighter time
[19:15] so have a nice day thank you
[19:19] [Music]
