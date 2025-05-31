---
type: youtube
title: The Hidden Costs of Building Your Own RAG Stack — Ofer Vectara
author: AI Engineer
video_id: 62U6FLUCPWs
video_url: https://www.youtube.com/watch?v=62U6FLUCPWs
thumbnail_url: https://img.youtube.com/vi/62U6FLUCPWs/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning
tags: ['RAG', 'LLMs', 'system design', 'AI challenges', 'latency optimization', 'scaling', 'evaluation', 'explainability', 'hybrid search', 'AI deployment', 'NLP', 'machine learning operations']
entities: ['Vicarious', 'RAG', 'LLMs', 'vector store', 'embedding models', 'PDF parsing', 'table understanding', 'hybrid search', 'evaluation of response quality', 'explainability']
concepts: ['RAG systems', 'hybrid search', 'latency optimization', 'scaling and cost management', 'evaluation of response quality', 'explainability', 'hallucinations in AI', 'continuous evaluation', 'system orchestration', 'component integration']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of machine learning', 'familiarity with NLP concepts', 'knowledge of system architecture']
related_topics: ['AI ethics', 'NLP techniques', 'system design', 'AI deployment', 'model evaluation', 'data parsing', 'machine learning operations', 'AI scalability']
authority_signals: ["I want to mention there's the evaluation of the response quality which is a complicated topic of its own", 'we all know that users just want to get answers fast and just wanted to highlight that this is not as trivial as you think when you come to kind of production grade']
confidence_score: 0.8
---

# The Hidden Costs of Building Your Own RAG Stack — Ofer Vectara

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=62U6FLUCPWs)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: rag stack, data ingestion, chunking, embedding models, vector database, hybrid search, reranking  

## Summary

# Summary of "The Hidden Costs of Building Your Own RAG Stack" by Ofer Vectara

## Overview  
Ofer Vectara discusses the complexities and hidden costs of building a Retrieval-Augmented Generation (RAG) stack from scratch, emphasizing the challenges of maintaining quality, latency, scalability, and security. He highlights seven key pitfalls of a DIY approach and contrasts them with the benefits of using a managed service like Vectara.

---

## Key Points  
- **Quality of Responses & Hallucinations**:  
  - Ensuring accurate, fact-based responses is challenging due to issues like poor parsing, chunking strategies, and hybrid search implementation.  
  - Hallucinations (false or fabricated information) remain a critical problem, requiring advanced techniques to detect and correct.  
  - Continuous evaluation of response quality is necessary as data and systems evolve.  

- **Latency**:  
  - Multiple components (e.g., vector databases, rankers) can introduce delays, with the system’s performance limited by the slowest component.  
  - Hybrid search and reranking add complexity, increasing latency beyond initial expectations.  

- **Scaling & Cost**:  
  - Scaling to handle large datasets (thousands to millions of documents) raises costs for GPUs, CPUs, storage, and external services (e.g., PDF/table parsing tools).  
  - Maintaining low latency and high quality at scale requires robust, well-orchestrated infrastructure.  

- **Compliance & Security**:  
  - DIY systems risk gaps in data protection, regulatory compliance, and audit trails, especially when integrating third-party tools.  

- **Vendor Lock-in & System Complexity**:  
  - Over-reliance on specific tools or frameworks can lead to vendor lock-in and increased maintenance complexity.  
  - Managing dependencies and ensuring interoperability adds to the technical burden.  

- **Explainability**:  
  - Users expect transparency, such as showing sources for retrieved facts. This requires careful integration of audit trails and user-facing explanations.  

- **Continuous Evaluation**:  
  - Monitoring and refining RAG systems over time is critical to maintaining performance and relevance as data and requirements change.  

---

## Key Quotes  
- *"Building a RAG stack is much harder than most people realize."*  
- *"The system’s performance is limited by the slowest component."*  
- *"Hallucinations remain a big issue, and implementing techniques to fight them can be quite complicated."*  
- *"Using a managed service like Vectara avoids these pitfalls by providing a unified, optimized solution."*  

---

## Actionable Recommendations  
1. **Invest in parsing and chunking**: Prioritize strategies for handling tables, hybrid search, and data organization.  
2. **Implement hallucination detection**: Use techniques like fact-checking and reranking to improve reliability.  
3. **Optimize for low latency**: Streamline components and avoid overcomplicating the retrieval process.  
4. **Plan for scalability**: Anticipate costs and infrastructure needs for large-scale deployments.  
5. **Ensure compliance**: Build in security measures and audit trails from the start.  
6. **Avoid vendor lock-in**: Use modular, open-source tools where possible.  
7. **Continuously evaluate**: Monitor system performance and refine models/data over time.  

--- 

This summary captures the core challenges and solutions discussed in the video, emphasizing the trade-offs between building a RAG stack in-house versus using a managed service.

## Full Transcript

[00:01] hi everyone and welcome to the hidden
[00:02] cost of building your own rag stack my
[00:04] name is ofer I run developer relations
[00:07] at victara and I'm a machine learning
[00:09] engineer by training and uh software
[00:11] engineer and I was fortunate enough to
[00:13] work on LMS since GPT just turn to in
[00:17] 2019 now I'm going to talk about hidden
[00:20] cost of rag stack I think we all know
[00:22] what it is but just for those of you who
[00:24] may may not be familiar it's a way of
[00:26] using llms not directly like we use
[00:30] sending a question and get an answer but
[00:32] instead you want to point it into your
[00:33] own data could be a bunch of PDF files
[00:36] it could be data from notion or wherever
[00:38] else and instead of calling the LM
[00:41] directly you first retrieve the most
[00:43] relevant facts for the question out of
[00:45] out of view data using a retrieval
[00:47] engine and then the llm is grounded in
[00:49] this data when it creates the
[00:52] response now it turns out that building
[00:54] a rag a platform that is Enterprise
[00:57] scale is much harder than most people
[01:00] seem to realize and this is what I'm
[01:01] going to talk about mostly in the stock
[01:03] before I go there just to kind of align
[01:05] everybody with a couple of components
[01:07] and things that are included in the
[01:08] stack so this is kind of my uh version
[01:11] of the diagram of how rag kind of works
[01:13] it has two main flows the first one is
[01:16] kind of in the blue arrow is the inest
[01:18] so you take data from wherever it is it
[01:19] could be a set of documents it could be
[01:22] a database it could be a gr or
[01:24] Salesforce or whatever it may be and you
[01:27] this is the data you want to be grounded
[01:29] on or or retrieved uh from and you
[01:33] ingest it into uh a bunch of of steps
[01:37] that you have to take care of you
[01:39] extract the data if it's a PDF file or a
[01:41] document of some kind you do something
[01:43] called chunking which is breaking the
[01:45] text into smaller pieces shown here and
[01:47] then each chunk is then encoded using an
[01:49] embedding model stored in a a vector
[01:52] database there's also other pieces here
[01:54] like you have to store the text
[01:55] somewhere and things like this but um so
[01:57] for Simplicity I'm going to skip those
[01:59] and then the Green Arrow is where a
[02:01] query comes in sometimes with some
[02:03] filtering parameters but the query text
[02:06] itself is again embedded into a vector
[02:09] the vector is run against the vector
[02:11] store and that those relevant facts are
[02:13] retrieved in many cases you want a
[02:16] stronger retrieval engine than just a
[02:18] vector search so you kind of want to do
[02:20] sometimes hybrid search which combines
[02:22] vector and keyword search you also might
[02:25] want to do reranking which uh can be
[02:27] relevance reranking or diversity ranking
[02:30] or some other business logic related
[02:33] ranking you want to do at the end of
[02:35] this retrieval step you get a set of
[02:38] relevant chunks or relevant facts and
[02:41] you send them with a prompt to the LM
[02:42] and say please you know respond to this
[02:44] query given the facts and then and I'll
[02:48] talk more about hallucination detection
[02:49] but sometimes what you want to do also
[02:51] is detect the hallucination to see if
[02:53] the LM actually did what you supposed to
[02:55] do and use the facts in a proper way and
[02:58] then once you have the response you say
[02:59] send it back to the newor so this is
[03:01] kind of uh a build of a rag stack and as
[03:05] you can see there's a lot of different
[03:06] components here and just a a quick a
[03:09] quick thing about victara what we do is
[03:11] we essentially put all of this in a box
[03:13] so think of it as a rag as a service
[03:16] where all these components end up being
[03:18] part of what we do what we provide it
[03:21] could be an assess format uh when you
[03:23] send all the data to us or it could be
[03:24] on your own VPC it could also be on
[03:26] premise in your own Hardware but this
[03:29] stack is pre-built and you don't have to
[03:31] build it or or or work on it all you
[03:34] have to do is use these external apis
[03:37] for indexing and for querying to First
[03:39] index the data you want the rag stack to
[03:41] work on and then to when you have some
[03:43] user interface you can use the query API
[03:45] to run the query flow here but all of
[03:48] the internals are hidden from you and
[03:51] saved from the trouble of managing those
[03:54] components okay now I'm going to get to
[03:56] the the meter what I wanted to talk
[03:59] about which is there is a very big
[04:01] difference between a sort of DIY rag
[04:05] stack when you build all of these
[04:06] components yourself you put in the
[04:08] vector database and the retrieval engine
[04:11] and you figure out which embedding mold
[04:14] to use and which El to use and all those
[04:15] pieces a big gap between that and using
[04:18] a platform like victar which all taken
[04:19] care of uh for you and as we talk to
[04:23] people in the community and and and
[04:24] customers we we figured there's about
[04:27] seven things I want to mention today
[04:29] that are kind of Pitfall when you do
[04:31] build your DIY rug and I want to talk
[04:33] about these seven so eant responses and
[04:36] hallucinations which I'll talk about
[04:38] maintaining low latency not getting high
[04:40] latency scaling up without making the
[04:42] cost be too high you want to make sure
[04:45] you don't have any issues with
[04:46] compliance and security of course
[04:48] there's something called vendor vendor
[04:50] chaos system will keep an additional
[04:52] language so let me talk about each of
[04:54] those separately so the first one is the
[04:57] quality of responses or inations we know
[05:00] the hallucinations are still a really
[05:02] big deal a really big problem both in P
[05:05] llms but also in Rag and at scale
[05:08] getting the right results first getting
[05:10] the right facts is a problem so you have
[05:13] to invest when you build your own
[05:15] infrastructure in in parsing in chunking
[05:19] there's a lot of different chunking
[05:20] strategies in parsing of tables and
[05:22] table understanding in general hybrid
[05:24] search all these things take a lot more
[05:26] work than kind of the initial PLC
[05:28] usually provides
[05:30] and so you have to realize that when you
[05:32] really want to get high quality results
[05:34] you have to invest in all of these
[05:35] components and get them to to work
[05:37] properly last but not least I want to
[05:39] mention there's the evaluation of the of
[05:42] the response quality which is a
[05:44] complicated topic of its own and it's
[05:46] not just evaluating on the first
[05:48] deployment you kind of want to
[05:50] continuously evaluate the results as you
[05:51] add more data refresh the data change
[05:54] components you want to make sure that
[05:55] your quality of the results Remains the
[05:57] Same or or better and then
[06:00] hallucinations again Still Remains a big
[06:02] issue and implementing techniques to
[06:04] fight hallucinations or even correct
[06:07] hallucinations can be quite complicated
[06:10] the last thing I want to mention here is
[06:11] just explainability this means that when
[06:14] you have a result you want to usually
[06:16] show what the facts are you have a path
[06:19] to for people to look at the facts click
[06:21] on a link and see where it came from
[06:23] again that's something that you want to
[06:24] integrate into the your UI but your
[06:26] system has to keep the path or the
[06:28] auditorial of where the results came
[06:29] from so that you can show
[06:32] them okay the second one is pretty
[06:34] straightforward for any you know
[06:36] architect or system engineer right he
[06:39] want the latency to be low and a lot of
[06:41] times it gets much higher than you want
[06:44] again just because there's multiple
[06:46] components and not super orchestrated
[06:48] and and harmonized and so retrieval
[06:50] right simple retrieval of vector store
[06:52] could be fast but when you want to do
[06:54] let's say hybrid search or some other
[06:56] rankers you may get into a lot of more
[06:58] trouble in latency and kind of starts to
[07:00] add up and your system depends on the
[07:02] weakest link right so if one of your
[07:04] components has a a latency issue the net
[07:07] suffers that becomes the latency for for
[07:10] the whole flow of query so we all know
[07:12] that users just want to get answers fast
[07:16] and just wanted to highlight that this
[07:17] is not as trival as as you think when
[07:19] you come to kind of production
[07:22] grade okay PF number three uh scaling
[07:26] and cost so you have a lot of components
[07:28] you have embedding models you have llms
[07:31] Vector database a bunch of other things
[07:32] you have uh
[07:34] to sometimes uh use external uh services
[07:37] to enhance your PDF parsing or table
[07:40] understanding and generally maintaining
[07:42] low latency and high quality just
[07:44] requires good components in your stack
[07:47] and then on top of that you have cost of
[07:49] gpus and CPUs and storage and so all
[07:53] these things really uh ramp up when you
[07:56] start going production scale with not
[07:57] just you know 10 documents but
[08:00] thousands or or hundreds of thousands or
[08:02] millions of documents and you know this
[08:05] the token cost also starts becoming
[08:07] something that's it's hard to uh to
[08:09] maintain number four security compliance
[08:12] issues so in security I wanted to
[08:14] highlight first the idea of attribute
[08:17] based access control a lot of times you
[08:19] want to implement that as part of your
[08:20] rag stack this means that if some of the
[08:24] documents in your
[08:25] application um are only visible in your
[08:28] organization let's say to the HR or to
[08:31] the CEO you want to make sure that your
[08:33] rag stack doesn't leak that information
[08:36] you want to have some the same access
[08:38] controls uh implemented in your in your
[08:40] rag flow uh similarly if you have
[08:43] sensitive information like Phi or Pi you
[08:45] want to make sure that that's ingested
[08:46] in the right way and treated in the
[08:48] right way throughout the stack a lot of
[08:50] these failures to do these kind of
[08:52] things and similar things in Security in
[08:53] compliance can have a pretty large cost
[08:56] in any organization so you want to make
[08:58] sure that you did that
[09:01] right okay this is one of my favorite
[09:03] ones to talk about actually vendor chaos
[09:05] what I mean by that is if you remember
[09:07] the diagram I started with that has all
[09:10] the different components and the flows
[09:12] there's quite a bit of components there
[09:14] you have your vector database you have
[09:15] your llm you have your embedding models
[09:18] you have your you know maybe keyword
[09:20] search for hybrid search Etc if you use
[09:23] different components for this and it's
[09:24] not just one you kind of harmonized
[09:27] Stack you start having multiple Enders
[09:29] so you have multiple contracts you have
[09:31] to onboard all of them and the
[09:33] integration can become much more costly
[09:36] than you might imagine the thing that
[09:38] frightens me the most with these kind of
[09:39] things when I think about kind of real
[09:41] Enterprise scale is how do you diagnose
[09:43] issues you have multiple vendors you can
[09:46] have things like you finger pointing
[09:47] coming up or you really just want to get
[09:49] have the problem solved so it could be
[09:51] here it could be there how do you
[09:53] diagnose how do you know and and who
[09:55] gives you the support how do you get the
[09:56] support coordinated so that could be a a
[09:59] pretty big nightmare so Something To Be
[10:01] watchful
[10:03] for all right um I'm going to the last
[10:06] two here so number six is unsustainable
[10:08] keep and again this means that rag stack
[10:11] is a pretty unique set of skills and one
[10:14] that moves really quickly so you have to
[10:16] have in your team if you build it
[10:18] yourself experts in llms experts in
[10:21] embedding models to different expertise
[10:23] areas experts in hybrid search and if
[10:25] you implement that Etc everything you do
[10:27] you have to have some specific expertise
[10:30] there not not easy to get in in in many
[10:32] organizations uh you have to have data
[10:34] engineering expertise to do all the data
[10:36] inest and ETL flows and parsing the PDFs
[10:39] and parsing the documents and things
[10:40] like this metadata management and then
[10:43] you have to have somebody running the
[10:45] system making sure it's up and running
[10:47] all the time so you got to have your
[10:49] devops sres Etc Security Experts so it's
[10:54] not always easy to find those resources
[10:56] and keep them as a separate team that
[10:58] can continue ly maintain the system up
[11:01] and running to support all your gen use
[11:04] cases takes a lot of
[11:06] work and then last is you know a lot of
[11:09] people start with English it's the
[11:10] easiest one everything supports English
[11:13] and you get a PC up and running but when
[11:15] you go to non-english users which may be
[11:18] a requirement for your organization ends
[11:20] up that it's not as easy you have to
[11:22] make sure that each of the component
[11:23] supports the language you need and
[11:25] sometimes they don't and then you have
[11:26] to change and your quality suffers or
[11:28] something like this so you got to think
[11:30] about it a front if you want to go to a
[11:32] uh production scale as
[11:36] well all right so those are kind of the
[11:38] seven pitfalls and things that we see in
[11:41] many transitions that we see of
[11:43] customers moving from kind of the
[11:45] initial PC and Then star to think about
[11:47] uh their production deployment and again
[11:50] this is why our approach is to have a
[11:53] platform it's a plug and play rag as a
[11:55] service platform and we've built all of
[11:58] these components the extract ction the
[11:59] encoding the indexing the vector
[12:01] database the retrieval all of these
[12:03] pieces are part of the platform you
[12:05] don't have to create them you don't have
[12:07] to manage them you don't have to upgrade
[12:09] them we will do all that for you and as
[12:12] a user of actara what you do is you have
[12:14] apis around it that you can use to
[12:17] upload your data or index your files and
[12:19] then to to run queries or chat or any
[12:22] other agentic rag applications through
[12:24] that so that's really the idea behind
[12:26] victar and why it's so so powerful for
[12:28] for B Enterprises that have a lot of use
[12:30] cases the three things that people
[12:32] usually choose us for are kind of
[12:35] aligned with some of the things I said
[12:36] earlier accuracy uh we focus a lot on
[12:39] hallucinations and reducing
[12:40] hallucinations and I'll share in a
[12:41] minute what that means a lot of emphasis
[12:44] on good retrieval and and quality
[12:46] results and retrieval of the facts
[12:49] security mechanisms like access controls
[12:52] and prompt attack prevention and also
[12:54] excellent ability to make sure that you
[12:57] have observability of what's going on in
[12:58] the system and you have citations
[13:00] throughout the the
[13:01] flow I talked about hallucinations a
[13:04] little bit I want to highlight this a
[13:05] little bit more so we've seen
[13:08] hallucinations a lot in 2024 and still
[13:11] this year it continues to be a
[13:13] significant issue for adoption and this
[13:15] is an example of uh just an article from
[13:18] last Thanksgiving and a couple of quotes
[13:20] we got from from that article so you
[13:22] know especially in regulated environment
[13:24] hallucinations can become a really uh a
[13:26] big hurdle for for adoption and for
[13:28] production deployment one of the things
[13:30] we focus on in victara is called hhm or
[13:33] hallucination uh evalation model
[13:36] detection model we have this as part of
[13:38] our system we've implemented this as
[13:40] part of the flow and with every call to
[13:42] victara you get your hallucination score
[13:45] which is really helpful because it can
[13:47] help you understand if the LM did a good
[13:49] job or not and use that this model was
[13:52] also open sourced on huging face you can
[13:54] see here it's got over 3 million
[13:56] downloads since it started so it's very
[13:58] popular it's by far the most popular
[14:00] evaluation for for hallucinations out
[14:02] there and we also built this leaderboard
[14:06] which might be interesting for everybody
[14:07] here listening this we take a bunch of
[14:10] the llms and evaluate How likely they
[14:13] are to hallucinate on on some data set
[14:15] so we use hhm sort of the commercial
[14:18] version of it to build this leaderboard
[14:21] and this gives a lot of people sort of a
[14:23] good indicator on top of the core
[14:25] capabilities of the LM how much they
[14:27] might hallucinate or not then I couldn't
[14:29] show all the leaderboard here because
[14:31] there's a lot of models here but some of
[14:33] them hallucinate at much higher rates
[14:34] this is just the top it could be you
[14:36] know sometimes like 10% or even 14% And
[14:39] things like this so you got to choose
[14:41] your llm wisely I mentioned that we also
[14:45] we're we're we're rag as a service but
[14:48] of course you can also deploy this in
[14:49] your VPC and on premises and that's
[14:51] important to know many of our customers
[14:54] require that and that's it thank you so
[14:57] much for listening I encourage you to
[14:58] try victar I have a QR code here you can
[15:01] check it out we have a a 30-day free
[15:03] trial with all the full capabilities of
[15:06] the platform and if you are interested
[15:08] to talk more please feel free to reach
[15:11] out thank you so much
