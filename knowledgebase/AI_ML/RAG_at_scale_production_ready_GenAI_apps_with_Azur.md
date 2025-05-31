---
type: youtube
title: RAG at scale: production ready GenAI apps with Azure AI Search
author: AI Engineer
video_id: _2tZaDs-w5s
video_url: https://www.youtube.com/watch?v=_2tZaDs-w5s
thumbnail_url: https://img.youtube.com/vi/_2tZaDs-w5s/mqdefault.jpg
date_added: 2025-05-26
category: Cloud Computing and AI
tags: ['Azure Search', 'vector retrieval', 'data integration', 'enterprise readiness', 'security', 'compliance', 'AI', 'machine learning', 'data types', 'retrieval systems', 'vector databases', 'multi-vector queries']
entities: ['Azure Search', 'vector retrieval', 'Microsoft', 'approximate nearest neighbor search', 'exhaustive search', 'embedding models', 'data integration', 'multi-vector queries', 'vector database', 'retrieval systems']
concepts: ['R patterns at scale', 'vector-based retrieval', 'enterprise readiness', 'security and compliance', 'data integration', 'multi-vector queries', 'embedding models', 'filtering and slicing', 'projection', 'retrieval system architecture']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['familiarity with data retrieval systems', 'vector databases', 'Azure ecosystem', 'AI/machine learning basics', 'data integration concepts']
related_topics: ['vector search', 'enterprise data retrieval', 'AI integration', 'data security', 'compliance frameworks', 'machine learning models', 'data types handling', 'retrieval system design']
authority_signals: ["we've seen the last 18 months or so since the emergence of R patterns at scale is Vector retrieval is an important part of the solution", "you don't have to connect a bunch of parts"]
confidence_score: 0.8
---

# RAG at scale: production ready GenAI apps with Azure AI Search

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=_2tZaDs-w5s)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: rag, generative-ai, azure-ai-search, machine-learning, scaling, ai-applications, nlp  

## Summary

# Comprehensive Summary of "RAG at scale: production ready GenAI apps with Azure AI Search"

## Overview  
This video explores the challenges and solutions for scaling Retrieval-Augmented Generation (RAG) in enterprise-grade generative AI applications, focusing on Azure AI Search. Pablo from Microsoft highlights how RAG combines domain-specific knowledge with large language models (LLMs) to improve accuracy and relevance, while addressing scalability issues like data volume, complex workflows, and integration with diverse data sources.

---

## Key Topics  
- **RAG Overview**:  
  - RAG enables LLMs to access external data for more accurate responses.  
  - Three approaches: prompt engineering, fine-tuning, and RAG (preferred for dynamic data).  

- **Challenges of Scaling RAG**:  
  - **Data Volume**: Managing large, heterogeneous datasets.  
  - **Workflow Complexity**: Multi-step retrieval and LLM interactions.  
  - **Data Source Diversity**: Integrating structured/unstructured data from multiple sources.  
  - **Performance Demands**: Balancing speed (approximate nearest neighbor search) and precision (exhaustive search).  

- **Azure AI Search Capabilities**:  
  - Integrated vector search for semantic similarity.  
  - Support for hybrid queries (e.g., filtering, column projection).  
  - Enterprise readiness: security, compliance, and seamless data integration.  

- **Vector Search Advantages**:  
  - Effective for capturing conceptual similarity.  
  - Combines with traditional retrieval methods for flexible querying.  

---

## Key Insights  
- **Shift to Production**: 2024 marks a shift from RAG prototypes to enterprise-scale deployments.  
- **Vector Search as Critical**: Essential for modern RAG systems due to its effectiveness in semantic retrieval.  
- **Unified Platforms**: Tools like Azure AI Search reduce complexity by integrating retrieval, vector search, and data management.  

---

## Actionable Recommendations  
1. **Leverage Azure AI Search**: Use its integrated vector and traditional search capabilities for scalable RAG systems.  
2. **Hybrid Query Strategies**: Combine vector search with filtering and projection for precise results.  
3. **Design for Complexity**: Anticipate multi-step workflows and diverse data sources in production systems.  
4. **Prioritize Enterprise Features**: Ensure security, compliance, and scalability when building RAG applications.

## Full Transcript

[00:03] [Music]
[00:13] all right let's get started hi everyone
[00:14] thanks for coming I'm Pablo I work in
[00:17] the Ashi team at Microsoft um and in
[00:20] this session we'll talk about rag at
[00:23] scale and in particular I'll focus on
[00:25] the retrieval portion of of the rag
[00:28] pattern so for for this session is we'll
[00:31] do a quick recap just make sure that we
[00:33] all have this we use the same terms for
[00:35] the same things uh and then I'll go
[00:37] through kind of different dimensions of
[00:38] scale and I'll comment a little bit on
[00:41] how do we tackle this in the context of
[00:43] AI search what we've learned from doing
[00:45] this and what are we doing to make it
[00:47] easier uh to scale these
[00:51] applications so kind of as a by by means
[00:54] of a quick recap when it comes to
[00:56] bringing your own domain knowledge uh to
[00:59] work together with with language models
[01:01] you effectively you have three options
[01:03] either you you can do um prompt
[01:06] engineering and you know while it's easy
[01:08] to dismiss you can go a long way with uh
[01:11] prompt engineering along especially
[01:12] these days you know models have longer
[01:14] longer context and whatnot um if if
[01:17] that's not enough sometimes the
[01:19] challenge is more along the lines of I
[01:21] want to teach uh particular patterns of
[01:23] or I want the model to learn jargon of
[01:25] some in some particular vertical domain
[01:27] and things like that and for that fine
[01:29] tuning is often a good
[01:31] option however in many many of these
[01:33] cases what I want is to have the model
[01:35] work over a set of data that the model
[01:37] didn't see during training this could be
[01:39] my application data my company data
[01:41] company about information about my users
[01:43] or anything like that and for that the
[01:46] the prevailing pattern right now is to
[01:48] use retrieval augmented generation
[01:51] effectively uh what that means is if if
[01:53] you want the model to know facts then
[01:55] what you do is you kind of separate the
[01:57] reasoning piece of the picture from the
[01:59] knowledge piece of the picture you lean
[02:01] on the language model for the reasoning
[02:03] capabilities and you and use an external
[02:05] knowledge base to model what you know
[02:08] about a particular domain the data that
[02:09] you have and and the way you glue them
[02:12] together is like in principle
[02:13] mechanically very simple of course then
[02:15] it gets complicated because you know
[02:16] life is never that easy but in principle
[02:19] uh you have some orchestration component
[02:21] that uh you know takes the task at hand
[02:24] let's say you have a chat application
[02:25] and then the user takes a turn and ask
[02:27] the next uh question um uh orchestration
[02:30] component hits some knowledge base uh
[02:33] seeking for pieces of information that
[02:34] could be used to produce an answer uh to
[02:37] this question and then grabs a bunch of
[02:39] candidates and then you go to the
[02:40] language model and then give it a bunch
[02:42] of instructions your candidates uh and
[02:44] ask the model to produce uh like an
[02:46] answer to the to the user question
[02:48] that's kind of the essence of the
[02:50] pattern we all know that in practice
[02:52] usually takes multiple goals and there's
[02:54] a lot of tuning in the middle and and
[02:55] whatnot but the fundamentals boil down
[02:57] to that um so uh just by by way of
[03:01] context like how many of you are doing
[03:03] are creating and working on R
[03:04] applications today everyone okay
[03:07] excellent um so with that backdrop what
[03:11] I wanted to do is talk about what are
[03:12] the pressure points when it when you
[03:14] scale these applications what one thing
[03:16] that has been fascinating to see is you
[03:19] know we had we had the opportunity to be
[03:21] involved in this place uh from very
[03:23] early like Asher open ey has been there
[03:25] from you know the early days of scaled
[03:27] language models and one thing we saw was
[03:29] all of I'd say last year 2023 everybody
[03:32] built a prototype of something to kind
[03:34] of learn and figure out what could be
[03:36] done with this technology um and the the
[03:39] interesting shift to this year to 2024
[03:41] is being these applications are going to
[03:43] production and when you go to production
[03:45] you go from oh this demo is really cool
[03:47] to all these users are are you know are
[03:49] using it at the same time and they want
[03:51] more they want more data they want uh
[03:53] more faster answers and and whatnot um
[03:56] so the result of that is that you know
[03:59] when before we could focus only on
[04:02] figuring out the interaction model and
[04:03] the applicability of this technology now
[04:05] you know elements of scale also also
[04:07] play a role uh and scale kind of takes
[04:10] multiple kind of flavors like you these
[04:13] thing things tend to scale in volume
[04:14] because one of the things that happens
[04:15] is when your application works well
[04:17] users come back or the leadership of the
[04:19] organization come back comes back and
[04:20] says let's put all the data there uh and
[04:22] then you have to deal with it um uh the
[04:25] also the rate of change of the data kind
[04:27] of increases uh and the query load
[04:29] increases as well because you know more
[04:30] people are using the stuff um also
[04:33] workflows tend to get more complicated
[04:35] at first you go like oh like how
[04:37] complicated it can be I'll take the
[04:38] question search the thing and then send
[04:40] it to the model well it turns out that
[04:42] that sometimes it works but often it
[04:44] doesn't so you end up doing this
[04:45] multi-step workflows that hit the
[04:47] retrieval system and the language model
[04:48] multiple times um and that taxes all the
[04:51] systems and they all have to
[04:53] scale also in in the kind of in the
[04:55] spirit of now let's put all the data
[04:57] there now you have to deal with more uh
[05:00] more data types different kinds
[05:01] different data sources and whatnot um so
[05:05] um let's cover each each of these
[05:06] dimensions of scale um in detail and
[05:09] what what I'll do is I'll cover it in
[05:11] the context of aser I search that
[05:13] because that's where where I work mostly
[05:15] uh and uh because it's you know the way
[05:17] we think about this in aure is we want
[05:18] to produce a system that is that
[05:21] encompasses entire retrieval problem uh
[05:23] it's of course it has this kind of
[05:25] vector database capabilities the vector
[05:28] based retrieval emerged that's a very uh
[05:30] useful solution in many contexts so uh
[05:33] we have full support for that but we
[05:35] also brought into a like uh years and
[05:38] years of Microsoft experience in in
[05:39] retrieval systems in the more General
[05:41] sense um and uh we integrate them
[05:43] together so you don't have to connect a
[05:45] bunch of parts uh to have a proper uh
[05:48] high quality retrieval system it all
[05:50] comes integrated and of course you know
[05:52] we integrate into the rest of Asher so
[05:53] it's easy to pull data in to connect to
[05:55] the other data sources and whatnot um
[05:58] and you know aure is is a place that is
[06:00] used to build some of the largest
[06:01] applications out there so all the kind
[06:03] of Enterprise Readiness comes builing
[06:06] you know from security to compliance to
[06:07] all these things that you don't want to
[06:09] deal with directly you want to kind
[06:10] build on a platform that is already
[06:11] taken care
[06:13] of so while there are multiple moving
[06:16] parts to retrieval systems what we've
[06:19] seen the last uh 18 months or so since
[06:21] the emerence of uh kind of R patterns at
[06:24] scale is Vector retrieval is an
[06:27] important part of the solution and you
[06:29] know you you can see why like the
[06:31] interesting part about Vector retrieval
[06:32] is like it's incredibly effective at
[06:34] getting this kind of soft conceptual
[06:36] similarity uh and uh put it to work
[06:38] right away so in as I search we built a
[06:41] system that has kind of complete a
[06:43] complete feature set when it comes to uh
[06:45] Vector search including uh fast
[06:47] approximate nearest neighbor search uh
[06:49] and as well as also exhaustive search
[06:52] sometimes you want precise search either
[06:53] to create baselines uh to know how kind
[06:55] of your recall performance is looking
[06:57] and things like that um also often
[07:00] applications need to combine uh Vector
[07:02] search with the rest of the queries you
[07:04] need to filter uh filter things you need
[07:06] to slice and dice like you know filter
[07:08] select the columns you want to project
[07:09] and things like that like effectively
[07:11] treat it like a database that also does
[07:12] retrieval um and we also see multiple
[07:15] scenarios where the documents have
[07:16] multiple queries maybe for different
[07:18] parts of the content or for different
[07:19] data types that use different embeddings
[07:22] um and uh and sometimes the queries need
[07:24] multiple vectors so we try to make it as
[07:26] this all these specific needs come up as
[07:29] you you're building an application
[07:30] you'll find answers to all of them
[07:32] directly in Ash search let me show you
[07:34] this in
[07:36] action um so let me start with a very
[07:39] simple example so what I'll do is uh I
[07:42] I'm just here I have a small uh jupyter
[07:45] notebook uh and what I'll do is I'll
[07:47] connect to um uh I set up a default
[07:50] credential point at my Azure search
[07:52] service and I'll create an index from
[07:54] scratch so this is all like all it takes
[07:56] to to create an index once you have a
[07:58] service provisioned so in this case I'll
[08:00] create a few Fields I'll create a
[08:02] categorical field like this serves as
[08:04] metadata that you want sometimes to
[08:05] attach to be attached to to this I'll
[08:07] create a text field sometimes you want
[08:09] to mix text and vectors um and I'll talk
[08:12] a little bit more about this later and
[08:13] I'll create a vector field in in this
[08:15] case this is a toy example so Dimension
[08:17] is three of course that's not very
[08:19] useful you know in practic in practice
[08:20] this is kind of in the hundreds or maybe
[08:22] thousands of Dimensions I'll also say
[08:24] what strategy you want the system to use
[08:26] for Vector search in this case I'm using
[08:28] hnsw it's a wellknown um uh graph based
[08:32] algorithm for um for indexing vectors so
[08:35] when I run this and I hope uh like the
[08:38] network was a little wonky so oh there
[08:39] perfect um so now I have an index I'm
[08:42] going to get a kind of a client to it
[08:44] and then I'm going to index data and you
[08:45] can see here this is a very simple case
[08:47] these are my vectors um this is my full
[08:49] text and these are my these are my
[08:51] categorical datab bits so you can let us
[08:53] do all the ingestion for you or you can
[08:56] push data into the index in this case
[08:57] I'm pushing data explicitly into to the
[08:59] index and once you have data uh if you
[09:02] look at here like we have some vectors
[09:03] and we have some categories so you can
[09:05] first you can just search and because
[09:07] it's in this case I'm indexing vectors
[09:09] when you search you search with a vector
[09:11] uh so I can I can search for that and
[09:13] say these are the two closest to the
[09:15] reference Vector that I gave and I can
[09:17] do uh um a few a few things uh kind of
[09:20] incrementally like for example if I want
[09:22] to combine text and keyword search I can
[09:25] also add search text right here uh I'm
[09:27] going to go hello and now I'm searching
[09:30] for both uh the the text and the vectors
[09:33] and then we fuse the result and rank
[09:35] appropriately um and and often in
[09:37] applications you also need to filter
[09:39] stuff you can see here I have A's and
[09:40] B's in categories so I can I can like
[09:43] write filters uh for example here I'll
[09:45] say category equals
[09:48] a uh and then you know I only get the a
[09:51] uh and this is a trivial example but of
[09:53] course you can do full filter
[09:54] expressions and ANS and ORS and and uh
[09:57] ranges and and whatnot and the filters
[09:59] are so so even if you have hundreds of
[10:02] millions of documents these are not a
[10:04] problem so that if you
[10:07] had K nearest K nearest equals two how
[10:11] come they had three results oh because a
[10:13] great question because so what I what I
[10:15] was telling this the the system here is
[10:17] from the vectors retrieve two candidates
[10:19] but then I was like I also told you go
[10:22] to the keyword side and retrieve a bunch
[10:24] of candidates from there and then fuse
[10:25] them uh so only two of them were from
[10:28] vectors but the fuse the fusion of the
[10:30] two uh selected three I actually like if
[10:33] I U I can make this a larger number and
[10:36] that sometimes is useful um to get more
[10:39] candidates and then still I can say as a
[10:42] result of that get the keyword ones two
[10:44] and then rank the top end so basically
[10:46] separate how many candidates you want
[10:48] from how many you want to
[10:52] return so so those are the basics of a
[10:56] vector engine but there are a few uh key
[10:57] elements to consider when you're
[10:59] actually building an application in
[11:00] production the probably the most the
[11:02] most sent one is quality like in the end
[11:05] your application works well for your
[11:07] users when they ask a question and they
[11:08] get the answer they're looking for and
[11:10] that is highly highly influenced by
[11:12] whether your retrieval system actually
[11:14] found the uh the bits of information
[11:16] that you wanted uh that that you wanted
[11:18] to produce that answer um in in AI
[11:20] search the way we do this is we do um
[11:22] what kind of most kind of more
[11:24] sophisticated search engines do that
[11:26] where you use a two-stage retrieval
[11:28] system first stage is recall oriented
[11:30] and uses vectors and keywords and kind
[11:32] all these recall oriented tricks to
[11:35] produce as many candidates as we can
[11:36] find and then the second stage rerank
[11:39] those candidates using like a a like a
[11:41] larger model that you maybe let's say
[11:43] you have 100 million vectors in your
[11:45] database uh you you want to use
[11:47] something fast to go from 100 million to
[11:49] a small set but then once you have a
[11:51] small set you can afford to run a larger
[11:53] more sophisticated language um sorry um
[11:55] ranking model uh to create better
[11:58] quality ranking so that's that's what we
[11:59] doing in the L2 stage uh so when you
[12:01] turn this on you effectively get better
[12:03] results and uh what you can see here
[12:05] there is a link at the bottom happy to
[12:07] share it later uh with more details on
[12:09] the numbers but you can see that um so
[12:11] from the left this is what you get when
[12:13] you just do keyword search using bm25
[12:15] which is a well known scoring approach
[12:17] second one is only vectors using Ada
[12:19] openi Ada vectors third one is using
[12:22] Fusion combine vectors and keywords and
[12:24] the fourth one is using Fusion plus uh
[12:26] reranking um reranking Step where across
[12:29] the board we see better results just out
[12:31] of the box when uh when reranking is
[12:33] enabled yes so the reranking is the is
[12:38] that is that another
[12:42] similarity great great question the
[12:44] question is is it a cosine similarity
[12:45] thing no so the thing bind colors are
[12:48] useful when uh because you can do you
[12:51] can encode all your documents as vectors
[12:52] and then the query as a vector um and
[12:55] then you can evaluate them fast because
[12:56] you are only comparing similarity but
[12:58] that means that at no point the model
[12:59] sees the the ve the document and the
[13:01] query at the same time so the ranker is
[13:04] uh these type of R rankers are often
[13:06] called cross encoders and uh these are
[13:08] Transformer models that you fit them the
[13:11] document and the query and you ask them
[13:13] to predict a label of the correspondence
[13:15] of the query to the document so they are
[13:17] much better positioned to produce a high
[13:19] quality result uh but they there are
[13:22] there at inference time or rather at
[13:24] query time you're running an inference
[13:25] step so um you can do it only on a
[13:28] smaller set you couldn't do it on the
[13:29] entire data set it wouldn't be practical
[13:31] at least not for interactive performance
[13:33] applications
[13:35] speed speed uh this is like 100
[13:38] milliseconds give or take for a model
[13:40] like this depends on the cross encoder
[13:41] that you that you use ours our tradeoff
[13:43] between you know make it fast enough but
[13:45] make it very high quality we landed on
[13:47] 100 milliseconds ballpark um uh and we
[13:50] found that that works well in terms of
[13:52] interactive performance because the
[13:53] majority of the latency ends up hidden
[13:55] on the llm call uh and you still get
[13:57] very high quality results
[14:01] um the other thing I won't drill into
[14:03] this but uh often uh one second often
[14:06] the other dimension of getting quality
[14:08] out of the system is to narrow the data
[14:10] set if you know discrete um metadata
[14:13] elements that can help you narrow the
[14:14] data set that's the most effective way
[14:16] uh then do all the ranking tricks on top
[14:18] of the resulting set but uh first uh
[14:20] scoping is uh is a very effective way to
[14:23] uh to get quality up yes question my
[14:26] question
[14:27] isct from
[14:30] how the for the keyword part of keyword
[14:32] search oh so if you look at um let me
[14:35] show you this example so if you look at
[14:36] what I did here is uh you give us
[14:40] keywords you give us text and then you
[14:42] give us a vector as well or you just
[14:44] give us the text and we'll turn it into
[14:46] a vector too uh so we need the original
[14:48] text the vector alone is not enough
[14:49] because we can't go back to a keyword
[14:52] you have
[15:01] oh so um usually in a rag app the
[15:04] question is what of the conversations so
[15:06] far do you want to use for search is
[15:08] that is that the
[15:24] question
[15:25] and you SE
[15:38] because you
[15:44] canix yeah I maybe we should talk after
[15:47] talk because I'm not sure I understand
[15:48] the question like usually like you in
[15:49] the index you have the the text and the
[15:52] vectors and then from the user you
[15:55] extract a candidate search for for that
[15:56] this is before you send it to the llm uh
[15:59] but maybe we should chat right after we
[16:00] talk on the
[16:01] details um so let me go back
[16:05] here so the the other dimension of
[16:08] scaling is um is uh just show how many
[16:12] vectors and how much content you can fit
[16:14] in one of your indexes uh and uh for
[16:17] that in I search like one thing we
[16:19] learned last year uh in the beginning of
[16:20] this year is that it went from everybody
[16:23] had tiny indexes to everybody put all
[16:24] their data in these systems uh so we we
[16:28] uh accommodated for that by
[16:29] significantly increasing the limits like
[16:31] for most of the search Services uh
[16:33] you'll get anywhere 10 between 10 and 12
[16:35] times the vector density on on the same
[16:37] skilles and we didn't change prices or
[16:38] anything just so you can build larger
[16:40] applications on the same setup with
[16:42] these new limits you can build multi
[16:44] billion Vector apps by just provisioning
[16:47] a service and uploading the data and
[16:48] it's surprisingly straightforward like
[16:50] you know a year ago the billion data set
[16:52] vectors was the thing there was a
[16:53] curiosity used for for benchmarking and
[16:55] now you can just create an index and
[16:57] upload them which is very impressive to
[16:59] to see um I'm not going to drain the
[17:01] slide I put it here for reference uh
[17:03] these are kind of all the new limits
[17:04] that uh that we have are significantly
[17:06] higher than the than the ones we had
[17:09] before um one of the things that has
[17:12] been exciting for us to watch uh to
[17:14] watch grow is uh you know among our
[17:16] customers one of them is open AI
[17:17] themselves uh where they have a lot of
[17:19] rag workloads like when you have files
[17:21] in ch GPT or when you use the assistants
[17:23] API all of those you can create these
[17:25] Vector stores inside their system and uh
[17:28] all of those are back by AI search uh
[17:30] and when we increase these limits um one
[17:32] of the things they did is they increase
[17:33] the limits they give to their users by
[17:35] 500 times um so it's been impressive to
[17:39] see how fast they grow and it's been fun
[17:41] to kind of see uh kind of first um from
[17:44] up close how a system can scale like
[17:47] this big and uh and still be fast and
[17:49] responsive and
[17:51] whatnot um so finally the the other
[17:56] thing you can do is sometimes the limits
[17:57] higher limits are enough sometimes you
[17:59] want to push even more data into it so
[18:01] the other thing we've been working on is
[18:02] quantization where we you can use
[18:04] narrower types like instead of using
[18:06] full floats you can use int uh like int8
[18:09] uh and they just simply use less space
[18:11] at the trade-off for a little bit of
[18:13] quality uh and interestingly you can
[18:15] even do single bit quantization and I
[18:18] confess that when people said hey like
[18:19] we're going to do metrics for single bit
[18:21] I felt people were wasting their time uh
[18:23] but it actually works it works
[18:25] surprisingly well our evaluations show
[18:28] that they are still for some models in
[18:30] the mid uh low to mid 90% of the
[18:32] original performance and other companies
[18:34] have seen the same thing like for
[18:36] example this is an evaluation from coher
[18:37] but separate company um and they also
[18:40] see like about almost 95% of the
[18:42] original Precision is preserved when uh
[18:45] when using big encoding and you can get
[18:47] the Precision remaining Precision back
[18:49] by reranking uh when you're done so
[18:51] surprising that it works but you go for
[18:53] float 32 to one bit that's 32x the
[18:56] vector density um and it's faster
[18:58] because you just do humming distance
[19:00] much much faster than Computing on a
[19:02] small number of a smaller number of bits
[19:03] instead of cosine similarity or
[19:05] something like that on a wider why they
[19:07] set so because of this we now support
[19:10] all these types in AI search as
[19:12] well um I'm going to skip this slide in
[19:15] the interest of time um so and you can
[19:18] do quantization yourself or you can just
[19:20] enable it and we will do quantization uh
[19:22] for you and uh if we do quantization for
[19:24] you we will also store the original uh
[19:27] Precision data there which means we can
[19:29] do oversampling where we query at the
[19:33] quantized kind compressed version of the
[19:35] vectors but we have the full Precision
[19:37] store stashed on the side uh so later we
[19:39] can rerank at full Precision uh and so
[19:42] you can effectively choose between you
[19:44] want a highly compressed uh index that
[19:47] is uh a little lower quality but but but
[19:50] larger or it's a little slower but
[19:52] larger uh or you just don't compress it
[19:54] and then you get the quality up so
[19:56] effectively you can choose any of the
[19:57] three uh and it's effectively up to you
[20:00] what you want to prioritize but we give
[20:01] you control for all three
[20:04] dimensions and then the last thing I
[20:06] wanted to uh touch on is the the other
[20:09] challenge is you have to keep adding
[20:11] data sources that you bring into these
[20:13] rag systems um and each of them you
[20:16] connect to them differently you
[20:17] enumerate changes differently um and uh
[20:20] that's that's just not where you want to
[20:22] spend your time um so we have this
[20:24] ingestion system that includes
[20:25] integrated vectorization as part of AI
[20:27] search where if the data is in AER
[20:30] whether it's in Blob storage or one lake
[20:31] or C DV we will connect deal with all
[20:33] the security and all of that we will
[20:35] automatically track changes so it's not
[20:37] a one-hot thing but it's as the data
[20:39] changes we'll pick up only the changes
[20:41] and we only in process the changes so
[20:44] the cost is also incremental you don't
[20:45] pay as you update the stuff for the
[20:47] entire set and then we'll deal with all
[20:49] file formats you know PDFs office
[20:51] documents images unpack the nested
[20:54] formats and what not do chunking do
[20:56] vectorization and land it on an index
[20:58] all in one go and this is a like
[20:59] industrial strength pipeline that you
[21:01] set up once and then it continuously
[21:03] runs uh after that as your data changes
[21:05] it reflects the changes so you can focus
[21:08] on the r stack you know the workflow how
[21:10] you quy the system but you don't have to
[21:12] think about how the data makes it there
[21:13] if the data is anywhere in Asher will
[21:15] index it and create like an index that
[21:17] follows the original data
[21:20] automatically all right and and with
[21:22] that uh I know I raced through this
[21:24] content these 20 minutes I'll be hanging
[21:26] out outside if anybody wants to chat or
[21:28] have questions
[21:29] um and I would encourage you to go try
[21:31] AI search today here's a link to the
[21:33] starting point um and as subscriptions
[21:36] includ include a free instance of AI
[21:38] search so you can even give it a shot in
[21:39] a minute without uh without having to
[21:41] pay for any of the stuff with that thank
[21:44] you
[21:48] [Music]
