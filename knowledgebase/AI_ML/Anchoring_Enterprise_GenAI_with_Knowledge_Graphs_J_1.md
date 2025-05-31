---
type: youtube
title: Anchoring Enterprise GenAI with Knowledge Graphs: Jonathan Lowe (Pfizer), Stephen Chin (Neo4j)
author: Channel Video
video_id: OpVkWc3YnFc
video_url: https://www.youtube.com/watch?v=OpVkWc3YnFc
thumbnail_url: https://img.youtube.com/vi/OpVkWc3YnFc/mqdefault.jpg
date_added: 2025-05-26
category: AI and Enterprise Technology
tags: ['Generative AI', 'Enterprise AI', 'RAG Systems', 'AI Implementation', 'Organizational Adoption', 'Cloud Computing', 'AI Cost Management', 'Enterprise Technology', 'AI Challenges', 'Machine Learning', 'User-Centric Design', 'AI Strategy']
entities: ['Johnny', 'Dirty Dancing', 'IBM', 'deoe', 'graph rag', 'RAG', 'cloud computing', 'Classic Computing', 'Dirty Dancing movie', 'enterprise organizations']
concepts: ['generative AI implementation', 'organizational resistance', 'cost challenges in AI', 'graph-based RAG systems', 'not invented here syndrome', 'entrepreneurial use cases', 'AI adoption strategies', 'performance requirements', 'enterprise technology integration', 'user-centric AI design']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with enterprise technology stacks', 'Knowledge of cloud computing fundamentals']
related_topics: ['Generative AI applications', 'Enterprise AI adoption', 'Retrieval-Augmented Generation (RAG)', 'AI cost optimization', 'Organizational change management', 'AI implementation challenges', 'Enterprise software development', 'Machine learning operations']
authority_signals: ["I've also worked at IBM deoe big organizations", 'I joined this whole profession because I love building applications that Delight the people that use them', 'how do you convince people to go from a system which is is working but not working well enough to a much more expensive system']
confidence_score: 0.85
---

# Anchoring Enterprise GenAI with Knowledge Graphs: Jonathan Lowe (Pfizer), Stephen Chin (Neo4j)

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=OpVkWc3YnFc)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: generative-ai, enterprise-ai, knowledge-graphs, ai-strategy, machine-learning, ai-implementation, data-science  

## Summary

```markdown
# Summary of "Anchoring Enterprise GenAI with Knowledge Graphs"

## Overview
This video discusses the challenges and strategies for implementing generative AI (GenAI) in enterprise settings, emphasizing the role of knowledge graphs in anchoring these initiatives. Speakers Jonathan Lowe (Pfizer) and Stephen Chin (Neo4j highlight the importance of aligning GenAI projects with real business use cases, addressing organizational resistance, and leveraging structured data to improve outcomes. They also share insights from pharmaceutical industry applications, such as accelerating drug development through knowledge graph-driven solutions.

## Key Points
1. **Gartner's Insights**:  
   - A major failure mode for GenAI projects is the lack of a clear business use case that solves real problems and drives monetization.  
   - 60% of GenAI projects fail due to misalignment with business goals, according to Gartner.

2. **Business Use Cases**:  
   - **Technology Transfer in Pharmaceuticals**: Jonathan Lowe shares a case study where knowledge graphs streamlined the transfer of critical drug development knowledge, reducing time-to-market and saving lives.  
   - **Monetizable Value**: Projects must address tangible problems (e.g., cost savings, efficiency) to gain stakeholder buy-in.

3. **Knowledge Graphs & Data Structuring**:  
   - **Document Chunking**: Knowledge graphs enable structured storage and retrieval of unstructured data (e.g., research papers, clinical trials), improving AI accuracy and performance.  
   - **Graph RAG (Retrieval-Augmented Generation)**: Combines knowledge graphs with large language models to enhance relevance and context in AI outputs.

4. **Organizational Challenges**:  
   - **"Not Invented Here" Syndrome**: Teams often resist new solutions, preferring existing tools or frameworks.  
   - **Cost Concerns**: GenAI architectures can be more expensive than traditional systems if not well-designed, requiring careful cost-benefit analysis.

5. **Strategies for Success**:  
   - **Bottom-Up Advocacy**: Start by engaging end-users to validate tool value (e.g., reducing repetitive tasks) before seeking executive support.  
   - **Analogies for Persuasion**: Use relatable examples (e.g., *Dirty Dancing* analogy) to explain complex concepts like "red guy" innovation in large organizations.

## Key Quotes
- **Jonathan Lowe**: *"This is not only a great business use case but also something which potentially is saving lives."*  
- **Stephen Chin**: *"The biggest failure mode was not having a business use case which would actually solve real problems."*  
- **Organizational Insight**: *"If you’re the guy with the idea at the level four of the hierarchy, the likelihood is pretty small [of meeting the CEO]."*

## Actionable Takeaways
1. **Prioritize Real Problems**: Focus on use cases with clear business value (e.g., cost reduction, speed, safety).  
2. **Leverage Knowledge Graphs**: Structure unstructured data to improve AI accuracy and scalability.  
3. **Address Organizational Resistance**: Use bottom-up approaches to validate tools with end-users before seeking top-down approval.  
4. **Evaluate Costs**: Assess long-term financial implications of GenAI architectures to avoid unsustainable expenses.  
```

## Full Transcript

[00:00] [Music]
[00:17] hey so it's so great to be back in New
[00:20] York City actually I grew up nearby here
[00:22] and pleased to be co- speaking with
[00:23] Jonathan thank you Stephen good to be
[00:26] here and you know we're here to kind of
[00:29] talk talk about leadership talk about
[00:31] how you can actually do a bunch of the
[00:32] things you've been hearing in practice
[00:35] we're going to talk about strategy we're
[00:36] going to talk about
[00:37] technology but let's start with analysts
[00:41] who who here trusts Gartner when Gartner
[00:43] says something they're predicting the AI
[00:45] wave they're predict okay nobody does
[00:47] nobody no hands s up in the room for the
[00:49] record but when they are predicting
[00:52] failure and
[00:54] catastrophes I I I try trust that right
[00:58] so last year they predicted 30% of
[01:00] generative AI projects are going to be
[01:02] abandoned by the end of
[01:04] 2025 now anybody in the room this is a
[01:08] really real honest check has anyone been
[01:11] on a failing gen project okay now Brave
[01:15] Sals amazing give give those guys around
[01:18] that took a lot of
[01:20] courage now to make them feel a little
[01:22] better who who hasn't yet got to
[01:26] production on their gen
[01:28] app okay so the rest of the hands went
[01:30] up right so this this is the
[01:33] challenge so we all want to be
[01:36] successful with Gen we all want to do
[01:38] amazing things we're getting asked to do
[01:39] amazing things but we we need to have
[01:42] the right way of approaching this in our
[01:44] organizations with leadership to sell
[01:46] this internally to to build it on
[01:48] Technologies which they can understand
[01:52] and the the vision it's it's hard to get
[01:55] a vision that's technically achievable
[01:56] when the guy at the head of the table is
[01:59] is this is this guy he's he's the
[02:01] executive who's heard about J his kids
[02:03] are using it for their School courses
[02:05] and he's like oh yeah yeah just it
[02:06] solves all the problems insert here
[02:09] success I wanted in production in two
[02:12] months now um I think the great thing
[02:14] about having having jonath as my
[02:16] co-presenter is that he's actually done
[02:19] this in a big Life Sciences company and
[02:23] he's had to navigate all of this um
[02:25] leadership challenges organizational
[02:27] challenges silos to
[02:30] build a system which actually is
[02:33] something we can take to production so
[02:35] tell us a little bit more about that
[02:36] Jonathan thanks Stephen now as I've been
[02:40] introduced Jonathan low you may know me
[02:43] as Jonathan when we're out in the
[02:44] hallway or when I give you a bit more
[02:47] information about my experience
[02:49] launching gen based capabilities in
[02:52] business you may think of me as Debbie
[02:55] Downer AI is so exciting until the
[02:59] singul
[03:03] ity
[03:05] so that's how I actually approached the
[03:07] problem I'm about to explain to
[03:10] you but it it actually worked so the
[03:13] business case was technology transfer
[03:17] which means in biofarma scaling up from
[03:20] Lab bench think beers and human scale
[03:23] drug development to Industrial scale
[03:27] making a million doses a day and to get
[03:30] from that lab bench level to multiple
[03:33] factories around the world making lots
[03:35] and lots of product very quickly takes
[03:38] years because the industrial people that
[03:41] build the factories and build the
[03:43] equipment need to sift through hundreds
[03:45] of thousands of documents and notes and
[03:48] test outcomes that were created at the
[03:50] science
[03:52] level another challenge with doing that
[03:56] is I'll go to a statistic in 2019
[04:00] a study said that the average tenure of
[04:04] manufacturing workers tenure being how
[04:06] many years they had spent in their
[04:08] companies was about 20 20 years of
[04:12] average tenure what do you think the
[04:14] average tenure is in manufacturing
[04:16] companies
[04:19] today the study said three years so
[04:23] we've gone from 20 down to three and all
[04:26] that
[04:28] expertise has
[04:30] has or will soon be retiring because the
[04:33] boomers are growing
[04:36] old so we really need generative AI we
[04:40] need a machine to take a lot of the
[04:42] intelligence that's captured in
[04:45] documents or even inass it people's
[04:47] heads and get it to the new people
[04:49] showing up to do this technology
[04:51] transfer so we take all these millions
[04:54] of documents and we've loaded them into
[04:57] a graph
[05:00] now we haven't necessarily
[05:02] loaded the document into the graph we've
[05:05] loaded the chunks into the graph and one
[05:08] of the things that we really liked using
[05:10] the graph to accomplish was we
[05:12] structured the chunks the document the
[05:17] block the paragraph the line because we
[05:20] wanted to understand when we searched
[05:23] for those chunks with similarity search
[05:26] which ones really returned the results
[05:28] that people wanted the most we wanted to
[05:30] really refine how we stored and managed
[05:32] the chunks so at this at this point it
[05:34] was it was a totally new space and
[05:36] because we were able to structure in the
[05:38] graph that level of chunking we were
[05:42] able to eventually learn and get better
[05:44] and better at how we chunked the
[05:45] documents in the first
[05:47] place yeah so I think what's really
[05:50] amazing for me about this is um we were
[05:53] talking about business challenges and
[05:55] like like projects failing and in the
[05:56] study that Gartner did the biggest
[05:59] failure mode
[06:00] was not having a business use case which
[06:02] would actually solve real problems and
[06:04] then be monetizable and um this is not
[06:07] only like a great business use case but
[06:08] it's also something which potentially is
[06:10] Saving Lives because you're you're
[06:12] getting life-saving drugs to folks
[06:14] faster you're able to accomplish this
[06:16] quicker
[06:17] but the problem is always the humans in
[06:21] the middle right so the teams you work
[06:26] with probably have a little bit of gen
[06:30] not invented here syndrome where you
[06:32] come along with this great solution like
[06:34] I'm going to use graph rag I'm going to
[06:35] load all these documents into the my my
[06:38] you know my my big um store and they're
[06:40] like no no no I we've heard see this
[06:42] research paper we watched this talk
[06:43] there's some other platform we want to
[06:45] use there's some other
[06:46] framework um or maybe it's maybe it's
[06:50] too expensive I mean compared to Classic
[06:53] Computing and cloud computing gen
[06:55] architectures have the potential will be
[06:57] much more expensive if they're not well
[06:59] architect
[07:00] and in general are going to increase the
[07:02] cost of the organization so how do you
[07:04] convince people to go from a system
[07:05] which is is working but not working well
[07:08] enough to a much more expensive system
[07:10] which is R&D investment Redevelopment to
[07:14] go towards a gen architecture so what
[07:15] are what are some of the challenges you
[07:17] hit internally and how did you address
[07:20] that
[07:21] adviser great so for this
[07:24] one it's more of an entrepreneurial use
[07:26] case within a big organization I wonder
[07:29] how many many of you have worked in
[07:30] organizations with 50,000 or more
[07:33] people a lot of hands going
[07:37] up uh my current organization has over a
[07:40] 100,000 people I've also worked at IBM
[07:43] deoe big organizations
[07:46] and if you are like me in these
[07:49] organizations you'll be that little red
[07:51] guy going like this with the with the
[07:54] light bulb over his head saying I have
[07:57] an idea that might help the company
[08:00] and I have a team of X number of data
[08:02] scientists and developers and sres and
[08:06] we can bring that value that capability
[08:10] to the
[08:12] company if you're like me if you're that
[08:14] red
[08:15] guy who's the first group of people on
[08:18] this slide that you're most interested
[08:21] in connecting with
[08:29] for the top you go for the top you're
[08:32] better than I am I I joined this whole
[08:34] profession because I love building
[08:36] applications that Delight the people
[08:38] that use them so my instinct has always
[08:41] been to go to the bottom first and say
[08:44] to those users hey do you really want
[08:46] this tool and what are those users going
[08:48] to tell you they'll like your tool
[08:54] if that's right what makes it good it
[08:57] takes away boring stuff that they don't
[08:59] want to
[09:00] do but it can't just take away boring
[09:03] stuff it also has to give them accurate
[09:06] results it also has to work in a
[09:08] performant way they can't push the
[09:09] button go get coffee and come back and I
[09:12] feel like that's the easy part right
[09:15] more and more these days you can build
[09:19] accurate fast applications quickly so
[09:23] where's the real challenge so somebody
[09:24] said you go to the top first what's the
[09:27] likelihood in a company of 50,000 to
[09:30] 100,000 people that you're going to meet
[09:32] the CEO if you're the guy with the idea
[09:35] at the level four of the hierarchy the
[09:39] likelihood is pretty small did anyone
[09:41] here ever see the movie Dirty
[09:43] Dancing Dirty
[09:45] Dancing maybe do you remember the part
[09:48] in Dirty Dancing when baby the lead
[09:50] leading woman in the in the movie meets
[09:52] Johnny the amazing dancer for the first
[09:54] time and she she's uh she's unable to
[09:57] speak she's so flustered and finally she
[09:59] blurts out I carried a watermelon and
[10:01] then off he goes and she goes I carried
[10:03] a
[10:04] watermelon two weeks ago I stepped into
[10:06] the elevator on the seventh floor of of
[10:09] the headquarters of of my company and
[10:11] there was my CEO in the elevator and I
[10:15] felt like baby and Dirty Dancing I
[10:17] couldn't think of what to say I locked
[10:19] up fortunately he's a good guy he broke
[10:22] the ice just back from vacation rolling
[10:25] up my sleeves can't wait to get to work
[10:26] what are you up to and then thank God
[10:29] ding we got to his floor the doors
[10:31] opened and out he went and as he went
[10:34] out the door I blurted out not I carried
[10:36] a watermelon but I'm working with
[10:41] llms off he went so when you're trying
[10:44] to promote your work within a big
[10:46] company like this it would help to know
[10:49] what that executive is trying to
[10:50] accomplish and the way that he gets to
[10:52] that point is he talks to Consultants
[10:55] who say let us tell you how to be a
[10:57] leader in your industry
[10:59] and not fall behind the competition so
[11:02] an example of something that an
[11:03] executive at that level might do is
[11:05] create a purpose blueprint or something
[11:08] like that name and the number one
[11:10] message has to be a few words and convey
[11:13] something that the whole company can
[11:15] follow so an example of that might be
[11:17] change a billion lives a year in life
[11:21] sciences a big aspiration now why do you
[11:24] have to care about that in the elevator
[11:27] maybe you'll reference it I'm changing A
[11:28] Billion Lives a with the most amazing AI
[11:30] search engine Bing and off he goes but
[11:33] that that message that he gives trickles
[11:36] down to the next level the chief digital
[11:38] officer the chief scientific officer the
[11:40] chief Supply officer what do you think
[11:42] they're going to
[11:43] say they're going to try to take his
[11:46] message and turn it into their specific
[11:47] flavor so the digital officer will say I
[11:50] want to lead the industry in Ai and the
[11:53] scientific officer will say I want to
[11:55] take on the world's biggest
[11:57] diseases and the Supply officer will say
[12:00] I want to accelerate Supply still very
[12:03] high level and you probably won't meet
[12:06] these people either who will you meet
[12:08] though you'll meet their level twos and
[12:10] their level threes and what are they
[12:12] going to
[12:15] say at this point they don't really say
[12:19] taglines instead they say I want cost
[12:24] savings I want cost
[12:26] avoidance I want earlier realized
[12:30] revenue or I want more balanced
[12:34] headcount so when you're talking to
[12:36] these people your slides have to have
[12:40] numbers and times and your promises
[12:43] about how your tool or your capability
[12:46] or report or whatever is going to meet
[12:48] meet those times and those
[12:50] numbers now you may not get to meet them
[12:53] either if your big company has a a form
[12:56] of um a role called the client part
[13:00] where your digital people talk to the
[13:04] client partner and the client partner
[13:06] talks to the business then that's the
[13:09] other person you have to convince and
[13:10] the problem with this is that the client
[13:12] Partners tend to stay within their
[13:13] particular departments there might be a
[13:15] client partner who works exclusively in
[13:16] R&D or one who works exclusively in
[13:19] Supply what would they say sometimes
[13:21] they don't say the same thing one of
[13:23] them might say R&D already has five or
[13:27] six or 10 search engines
[13:30] why build
[13:31] another or they might say search engine
[13:36] is a great idea why don't you
[13:37] incorporate that capability into every
[13:39] tool in the supply organization so
[13:42] either your scope goes to nothing or it
[13:44] goes to everything and you need to be
[13:46] able to negotiate and navigate
[13:48] that are you done if you can satisfy all
[13:52] those people and cross through all those
[13:53] gauntlets well no because as you're
[13:56] starting to build the vendor comes to
[13:58] you and says why build in house when you
[14:02] can buy our tools and they've been
[14:05] talking to the chief digital officer
[14:07] about build versus buy and which one is
[14:09] more economically realistic and
[14:12] appropriate well maybe you get through
[14:14] that and then you're done
[14:16] right who else would possibly stand in
[14:19] the way of your incredible AI Search
[14:23] tool Friendly Fire is the answer your
[14:27] own colleagues either level above or at
[14:29] the same level may say dude I was here
[14:33] first AI search is my turf or they might
[14:37] just say hey that client partner over in
[14:40] Supply is right can you please integrate
[14:41] with the stuff I've built so I guess my
[14:45] message is we've heard a lot of talks
[14:47] about failure and Challenge and Gartner
[14:50] not liking this it's an incredible time
[14:53] to be in this in this amazing industry
[14:56] in this amazing change in both for me
[14:59] life sciences and more generally for the
[15:01] information technology
[15:03] industry and I love that we're hearing
[15:06] all this concern about failure because
[15:08] it just means we're at the beginning of
[15:10] a really exciting time but as
[15:12] representatives of that my advice to you
[15:15] is know your audience personalize for
[15:18] all of them and get your human wetwear
[15:21] chatbot speaking the right language at
[15:23] the right
[15:24] level now that's that's amazing um we
[15:28] chatted out a bunch of challenges right
[15:29] so we've chatted about getting a good
[15:32] business use case that can actually
[15:34] provide values the organization how to
[15:36] navigate like like peoples and and
[15:38] different failure modes um within the
[15:41] organization where the organization has
[15:43] a huge quantity of people who can be
[15:46] your allies or can work against you
[15:48] depending upon how you work with them
[15:50] but it's also a technology problem you
[15:53] have to have the right technology to
[15:55] solve your use case now one of the the
[15:58] biggest challenges I think a lot of us
[15:59] who have been building Rag and
[16:00] Enterprise applications has been the LMS
[16:04] themselves fighting us with with
[16:06] hallucinations this is getting better
[16:07] with newer models um it's getting easier
[16:11] to feed the right sort of information in
[16:12] with Vector databases but I think that
[16:15] you've chosen a rather unique approach
[16:18] using graph databases why did why did
[16:19] you choose to use a graph database for
[16:22] your implementation at
[16:24] fiser well um
[16:29] there are a lot of things that graphs
[16:30] aren't good at things like genealogic
[16:33] sequences of recipes or social networks
[16:37] or hierarchies or time series and all of
[16:40] those applications were prevalent
[16:42] opportunities within fizer so that was
[16:45] the that was the original impetus for
[16:47] using a graph but I also discovered that
[16:50] the more data we Consolidated in the
[16:52] graph the faster my data scientists and
[16:56] engineers and developers and SRE were
[16:59] able to understand the data landscape
[17:02] what used to take 3 months to
[17:03] consolidate understand clean up took
[17:06] three weeks or less for for a new
[17:09] project so I know the reason a lot of
[17:12] people take on graph is because
[17:13] traversal becomes so much easier in
[17:16] terms of data search and uh and and
[17:18] performance gets better but I found that
[17:20] team performance also took a really big
[17:22] Boost from using that Tech cool and for
[17:25] folks who aren't familiar with with
[17:26] knowledge graphs and LMS or or graph rag
[17:29] um this isn't a new idea although I I
[17:32] would put you guys on the early adopter
[17:34] where you're actually in production now
[17:35] with something that uses this but U
[17:38] Microsoft kind of wrote the seminal
[17:40] paper on graph Rag and used it basically
[17:43] taking existing documents llms to chunk
[17:46] it into a graph and then showed Superior
[17:49] results coming out of it it on the
[17:52] spectrum of Technologies using LMS
[17:55] directly you can get good results but it
[17:57] lacks that context it lacks that
[17:59] Enterprise knowledge using a vector
[18:02] database or or Baseline rag you you can
[18:05] get better results where now it's
[18:07] actually pulling in organizational
[18:09] knowledge but the answers tend to be a
[18:10] little bit generic there's a lot of
[18:13] hallucinations um graph rag kind of
[18:15] pulls us to the end of the spectrum
[18:17] where now you're you're getting answers
[18:19] from that that Knowledge Graph you built
[18:21] you can evolve over time and much more
[18:24] precise answers which actually get to
[18:26] the heart of of real problems and in
[18:29] life sciences and Manufacturing and
[18:31] business critical Industries where you
[18:34] can't afford to be
[18:35] wrong and also where in in industries
[18:38] that are complicated if there are a lot
[18:40] of connections that might not appear in
[18:42] a relational database because no one
[18:44] bothered to make the joins permanent
[18:47] whereas in a graph those joins are there
[18:48] to begin with so if you search for one
[18:50] thing suddenly the neighborhood of
[18:52] related stuff becomes available to you
[18:54] to share with an llm for better
[18:56] contextual
[18:57] knowledge yeah and you know I think just
[19:00] if folks are implementing this or folks
[19:01] are thinking about how to how to think
[19:03] about architectures for graph rag um
[19:06] this is a really simple way of thinking
[19:08] about it so basically what you're doing
[19:10] is you're taking your gen
[19:12] application and you're doing both a
[19:14] vector and a Knowledge Graph
[19:16] representation of the data so you're
[19:18] both asking the vector for the answer
[19:21] you're getting relationally close nodes
[19:24] from the graph database where you're
[19:26] getting additional context and passing
[19:28] that in the LM and then this gives you
[19:31] more contextually relevant results
[19:34] coming out of your your expert system so
[19:37] I think this is a great way to use a
[19:38] Knowledge Graph either that you built up
[19:41] over time or that you have the LM
[19:42] construct to kind of get those Superior
[19:45] results where you could do better
[19:47] governance you can put controls and
[19:49] properties on the graph nodes to control
[19:50] who has access to the
[19:52] information you can get better
[19:54] explainability now because when you're
[19:57] getting an answer from the LM you're no
[19:59] longer looking at statistical
[20:00] probabilities in the vector space you're
[20:03] actually looking at graphs and nodes and
[20:05] edges which we can reason about and we
[20:07] can start to understand the relationship
[20:09] between understand like what what things
[20:12] are related to manufacturing which
[20:14] things are unrelated to that they're
[20:17] just you know general
[20:19] terms and for the right
[20:22] application maybe we're saving lives
[20:25] getting drugs to people more quickly and
[20:29] using gen for a good cause so thanks so
[20:31] much for joining us for our presentation
[20:34] at AI engineering Summit and um
[20:37] appreciate everybody thank you
[20:45] [Music]
