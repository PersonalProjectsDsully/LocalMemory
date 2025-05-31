---
type: youtube
title: RAG for VPs of AI: Jerry Liu
author: AI Engineer
video_id: KJsUHnwSvTY
video_url: https://www.youtube.com/watch?v=KJsUHnwSvTY
thumbnail_url: https://img.youtube.com/vi/KJsUHnwSvTY/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence Tools and Development
tags: ['Llama Index', 'RAG', 'AI Development', 'Open Source Tools', 'Data Quality', 'Enterprise AI', 'LLM Applications', 'Developer Tools', 'Agentic Systems', 'Context Augmentation', 'AI Orchestration', 'Data Pipelines']
entities: ['Llama Index', 'Llama Cloud', 'AI', 'developers', 'Enterprise', 'PDFs', 'PowerPoints', 'spreadsheets', 'RAG', 'LLMs']
concepts: ['Retrieval-Augmented Generation (RAG)', 'Open Source Toolkit', 'Productionizing RAG', 'Agentic Use Cases', 'Context Augmented LLM Apps', 'Data Quality', 'Hallucinations in AI', 'Developer-Centric Approach', 'Orchestration', 'Data Pipelines']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Prior knowledge of AI/ML concepts', 'Familiarity with development tools', 'Understanding of data quality principles']
related_topics: ['Machine Learning', 'Software Development', 'Data Engineering', 'AI Ethics', 'Cloud Computing', 'Natural Language Processing', 'AI Tools', 'Enterprise Solutions']
authority_signals: ["we believe in developers like if you're kind of you know um leading AI at at one of these like Enterprises uh you do want to make a bet on developers", 'developers are the best position to translate that technology into Enterprise Value']
confidence_score: 0.8
---

# RAG for VPs of AI: Jerry Liu

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=KJsUHnwSvTY)  
**Published**: 4 months ago  
**Category**: AI/ML  
**Tags**: rag, llama index, enterprise ai, data processing, question answering, ai development, machine learning  

## Summary

# Summary of "RAG for VPs of AI: Jerry Liu"  

## **Overview**  
Jerry Liu discusses the importance of Retrieval-Augmented Generation (RAG) for enterprises, emphasizing data quality, developer empowerment, and the role of tools like Llama Index and Llama Cloud in scaling AI applications from prototype to production. He highlights challenges in AI adoption, including data silos and the need for robust data processing.  

---

## **Key Points**  
- **RAG Use Cases**:  
  - RAG is critical for enterprises to enhance LLMs with domain-specific data, enabling context-aware responses.  
  - Primary applications include productionizing RAG pipelines and emerging agentic workflows (e.g., orchestration, tool use, reasoning).  

- **Challenges in Scaling**:  
  - **Data Quality**: "Garbage in, garbage out" applies to LLMs; poor data quality leads to hallucinations and unreliable outputs.  
  - **Data Silos**: Enterprises often struggle with fragmented, unstructured data (e.g., PDFs, spreadsheets).  
  - **Developer Focus**: Out-of-the-box tools are slow to adapt to new techniques, while developers are better positioned to translate tech shifts into enterprise value.  

- **Llama Index & Cloud**:  
  - **Open-Source Toolkit**: An ecosystem for building and productionizing RAG apps, enabling developers to focus on high-value tasks.  
  - **Llama Cloud**: A centralized platform for unifying data sources, enhancing data quality, and streamlining pipeline management.  

- **Strategic Recommendations**:  
  - Invest in **developer enablement** over purely pre-built solutions to adapt to rapid AI advancements.  
  - Prioritize **data quality** and processing infrastructure to ensure reliable AI outputs.  

---

## **Important Quotes/Insights**  
- "Garbage in, garbage out" is critical for LLMs: Poor data quality undermines even the best models.  
- "Bet on developers, not just out-of-the-box tools" to future-proof AI initiatives.  
- "Llama Index is a framework to help developers build production RAG apps from prototype to scale."  

---

## **Actionable Takeaways**  
1. **Improve Data Quality**: Invest in tools and processes to clean, structure, and enrich enterprise data.  
2. **Leverage Open-Source Tools**: Use frameworks like Llama Index to empower developers and accelerate innovation.  
3. **Focus on Developer Enablement**: Prioritize tooling that reduces friction in building and maintaining AI applications.  
4. **Plan for Agentic Workflows**: Prepare for the rise of autonomous AI agents by investing in orchestration and tool integration.

## Full Transcript

[00:00] [Music]
[00:13] hi everyone I'm Jerry co-founder CEO of
[00:16] uh of llama index and uh I'll probably
[00:19] spend the first 10 minutes just giving
[00:20] like a brief overview I I mean of rag
[00:22] and also just like llama index uh how we
[00:24] see the Enterprise developer space and
[00:27] and how it's progressing as well as give
[00:29] an overview of the product offerings um
[00:31] and then I think in the next 15 minutes
[00:33] happy to like you know generally field
[00:34] questions and kind of answer uh actually
[00:37] maybe like have a discussion on what's
[00:39] top of mind uh throughout Enterprises
[00:40] today so let's get started um you know
[00:44] throughout the Enterprise um what we're
[00:45] seeing and this might resonate with some
[00:47] of you um there's a lot of different use
[00:48] cases that we're seeing pop up um and a
[00:51] lot of it's around rag right I'm pretty
[00:53] sure we all probably know what rag is uh
[00:55] you know you point it at some like
[00:56] directory of files and then you get the
[00:58] LM to somehow understand these files and
[01:01] then generate answers from them um some
[01:03] other use cases that we see include like
[01:05] document processing and extraction um
[01:07] being able to maintain conversations
[01:09] over time and then this year there's a
[01:11] lot of people like you know building
[01:12] agents um we haven't seen as many like
[01:15] fully autonomous agents in production
[01:17] they typically are a bit more
[01:18] constrained um but actually curious to
[01:20] get your takes as well um so happy to
[01:22] discuss that so obviously rag has been a
[01:26] very popular um like set of techniques
[01:28] basically for helping you build build a
[01:30] question answering interface over your
[01:31] data that's really the end goal is to
[01:33] help you build a question answer
[01:35] interface and what are the main
[01:36] components of rag I won't go into like
[01:38] the super technical details but you know
[01:40] you need an llm um to do the final
[01:42] synthesis you need an embedding model um
[01:44] you need a vector database or you need
[01:46] some database um could be you know a
[01:49] document store it could be a graph store
[01:51] could be uh like a SQL database um or a
[01:53] vector database and then here's the
[01:56] thing that's interesting is that you
[01:58] basically need a new data processing
[02:00] stack to handle the data parsing and
[02:02] ingestion side um this is different than
[02:05] traditional ETL which is primarily for
[02:07] kind of like you know analytics
[02:08] workloads as well as there's a lot of
[02:10] like Technologies popped up around that
[02:13] here you know you're really you know at
[02:14] a very basic level say taking in a PDF
[02:17] slicing it up into a bunch of chunks um
[02:20] figuring out how to do that well and
[02:22] index it and represent it in a bunch of
[02:23] different uh storage forms um so that
[02:26] llms can have easy access to it right
[02:28] and a lot of what l is trying to solve
[02:30] is on that data processing piece so at a
[02:34] very you know um a big pain point that
[02:37] we see um for a lot of companies U
[02:41] building LM applications is going from
[02:44] prototype to production um unlike
[02:46] traditional ml um it's actually really
[02:48] easy to build a prototype uh with like
[02:50] some of the tools that L Indo offers it
[02:52] takes like 10 minutes to build a rag
[02:54] pipeline um that kind of works over your
[02:56] data but going from kind of works to
[02:59] something that's produc quality is a lot
[03:01] harder um and so as we see you scale up
[03:03] the number of documents as we as the
[03:06] documents get more complex as you try to
[03:08] add more data sources you have a higher
[03:10] quality bar that you need to meet and
[03:12] then some of the general you know pain
[03:13] points that we see include accuracy
[03:15] issues um knowing how to tune like a
[03:17] bunch of different knobs and then also
[03:19] scaling to a lot of data sources often
[03:21] times this either takes a lot of
[03:23] developer time or um they just don't
[03:25] know how to do it and so what ends up
[03:27] happening is that PO you're building for
[03:29] the higher UPS uh just ends up not like
[03:31] really working um and so therefore like
[03:33] the value of that overall project is uh
[03:37] diminished um the other problem that we
[03:39] see is that generally speaking um most
[03:41] of these a lot of these larger companies
[03:43] that we talk to have a lot of data um
[03:45] and there's this like General issue of
[03:47] just like data silos right um You have
[03:50] unstructured data structured data
[03:51] semi-structured data apis and somehow
[03:55] you know uh like this is um a similar
[03:58] problem occurs during the AL application
[04:00] development where you want to somehow
[04:02] bring in all this data into some central
[04:04] place so that your LMS can understand it
[04:07] right and when they're able to
[04:09] understand it and ideally you know
[04:10] somehow if you had this magic tool that
[04:12] made that happen and made it work well
[04:14] then you're able to have this kind of
[04:16] like holy grail of rag uh just being
[04:18] able to synthesize answers um and do
[04:20] stuff over like any of your knowledge um
[04:23] anywhere in the
[04:25] Enterprise um a thing that we talk about
[04:28] a lot uh both during the keynote
[04:30] yesterday as well as more generally is
[04:32] the importance of data processing and
[04:34] data quality um like you know we've
[04:37] probably all heard the term like garbage
[04:38] in garbage out and this is true in
[04:41] machine learning but this is uh also
[04:43] true in uh llm application development
[04:46] if you don't have good data quality and
[04:49] I can go into an example of what that
[04:50] means um you're not going to get back uh
[04:53] well represented information um so that
[04:56] even if your llm is very good uh
[04:58] oftentimes if your data quality is bad
[05:01] this leads to hallucinations within your
[05:04] application and so we believe in
[05:07] developers like if you're kind of you
[05:09] know um leading AI at at one of these
[05:12] like Enterprises uh you do want to make
[05:14] a bet on developers and and like you
[05:16] know I I think generally speaking and I
[05:18] tell I say this like pretty often um you
[05:21] should generally bet on probably
[05:23] building a little bit more than more
[05:25] than just like buying pure outof thee
[05:26] boox Solutions and there's a few reasons
[05:28] why this is the case first the AI space
[05:31] is moving really quickly the underlying
[05:33] technology is Shifting developers are
[05:35] the best position to translate that
[05:37] technology into Enterprise Value that
[05:40] are accustomed to your use case um if
[05:42] you you know go through the procurement
[05:43] process and purchase generally speaking
[05:45] like out of the boox tools that will
[05:47] solve maybe like the current paino that
[05:49] you have around that um like right and
[05:52] and provide a solution for that but it
[05:55] will probably be a lot slower to
[05:57] basically adapt it as new techniques po
[05:59] pop up uh new workflows are possible and
[06:02] so we care a lot about developers and we
[06:04] want to basically provide the tooling
[06:06] and infrastructure to enable developers
[06:08] to build LM applications over their data
[06:11] this helps you get um applications with
[06:13] high data response quality that's
[06:15] actually ready for production uh and
[06:17] importantly it's like easier for
[06:18] developers to set up and maintain so you
[06:20] don't have to keep throwing developers
[06:22] at it and kind of like bang their heads
[06:24] against the wall to figure out how to
[06:25] actually make this thing generate good
[06:26] responses um and you can scale this to
[06:28] more data sources
[06:32] great I'm not going to go through you
[06:34] know kind of um all the different
[06:36] features of L index but I'm just going
[06:37] to quickly run through some of the main
[06:38] components um our main goal as a company
[06:41] is to help uh any developer build
[06:43] context augmented llm apps uh from
[06:45] prototype to production we have an open
[06:48] source toolkit right and this is an open
[06:50] source framework that's a very popular
[06:52] framework to help you build uh help
[06:54] developers build production all maps
[06:56] over your data uh a lot of the use case
[06:58] that we've seen in the past last year
[06:59] have been around like you know
[07:01] productionizing rag uh in you know the
[07:03] next 6 months we anticipate a lot more
[07:05] agentic use cases to arise as well and
[07:07] it's primarily focused on orchestration
[07:09] around like retrieval prompting agentic
[07:12] reasoning tool use the other piece that
[07:14] we have is llama Cloud which is a
[07:17] centralized knowledge interface for your
[07:19] production Alum application unifies your
[07:21] data sources starting with unstructured
[07:23] data is able to process and enhance that
[07:25] data for good data quality so that you
[07:27] actually have you know good quality
[07:29] quality data from your very complex like
[07:31] PDFs and PowerPoints for instance and
[07:33] spreadsheets and helps you build manag
[07:35] pipelines so that you as a developer
[07:37] don't have to worry as much about that
[07:39] and can basically worry uh about
[07:41] building the actually interesting stuff
[07:43] around the orchestration of that data
[07:45] with
[07:47] LMS um yeah I think I mentioned this
[07:50] already open source toolkit a lot of
[07:52] people using it um going to skip this
[07:54] and then llama cloud is again this like
[07:57] centralized knowledge interface for your
[07:58] production l app um you spend like the
[08:01] idea is to help manage a lot of the data
[08:03] infrastructure so that developers
[08:05] generally speaking have to spend less
[08:06] time wrangling with data and spend more
[08:08] time building some of the core you know
[08:11] uh prompting agentic retrieval logic
[08:13] that uh makes up like the custom use
[08:15] case that they want to build
[08:17] for um I'm not going to run through all
[08:20] the features that we have because this
[08:22] is basically just like one of the um you
[08:24] know some of these things are upcoming
[08:25] but one specific thing that I think has
[08:28] actually a decent amount of interest
[08:30] from users is llama parse which is a
[08:32] specific component of llama Cloud it's
[08:35] basically our Advanced document parser
[08:37] that helps solve this data quality
[08:39] problem um basically if you want to
[08:41] build llm applications over like a
[08:44] complex financial report or a PowerPoint
[08:47] with a lot of different messy text
[08:48] layouts um like uh tables images
[08:52] diagrams and so on and so forth we
[08:54] provide a really nice toolkit to
[08:56] basically help you parse that data
[08:58] specifically so that Al lens can
[09:00] understand it and don't hallucinate over
[09:04] it
[09:05] um so far you know we released this like
[09:08] a few months ago um there's been some
[09:10] impressive usage metrics so far um
[09:12] basically half million monthly downloads
[09:13] on the client SDK uh like tens of
[09:16] millions of pages processed and a lot of
[09:18] like important customers basically using
[09:21] this throughout the
[09:26] Enterprise and yeah uh generally
[09:29] speaking maybe just in terms of like
[09:30] discussion topics and happy to talk
[09:32] about any of these components um I'm
[09:34] very interested in generally speaking
[09:36] like kind of the Enterprise like data
[09:38] stack and how that translates into llm
[09:40] applications I'm also interested on the
[09:42] use case side um basically the kind of
[09:45] like advancements from simple QA
[09:47] interfaces into more a gench workflows
[09:49] that can actually take actions and
[09:51] automate uh more decision-making uh from
[09:54] from different teams right either
[09:55] internally or externally um and just a
[09:58] quick shout out is you know we have like
[10:00] a general weit list for llama Cloud um
[10:02] that's already gone pretty popular uh
[10:05] there's been a decent number of signups
[10:06] but uh there's uh the goal is to
[10:09] basically help enable more users to kind
[10:11] of like process and index their
[10:12] unstructured data uh so again they can
[10:15] help like manage that and still uh build
[10:17] a lot of the kind of like important use
[10:19] cases um as Enterprise developers
[10:24] cool go it
[10:37] understand deal with customers
[10:42] very senstive to
[10:46] privacy yeah that's a great question can
[10:48] you just repeat part of the question I
[10:50] it with the microphone um so the
[10:51] question was about the Enterprise
[10:52] product Lama Cloud where um the
[10:54] understanding is that you upload
[10:56] documents or our Cloud so how do we deal
[10:57] with like data privacy uh there's two uh
[10:59] kind of answers to that the first is
[11:01] that we have both a cloud service as
[11:03] well as a VPC deployment option I'm
[11:04] happy to chat about that uh if you sign
[11:06] up on the kind of like contact form so
[11:08] we deploy in in um AWS and Azure with
[11:11] gcp coming soon and then the second is
[11:13] uh we're like kind of a data
[11:14] orchestration layer so we actually
[11:16] intentionally don't store your data um
[11:18] we try to integrate with the existing
[11:19] storage
[11:21] systems
[11:23] yeah um you made a comment on like the
[11:26] differences between traditional ETL um
[11:29] um and um you know kind of the the new
[11:32] skills and tools Etc are required can
[11:34] you expand on that a bit so that you
[11:36] know in in my company where I get like
[11:39] ask maybe hey let's have this uh ETL
[11:41] person who's done a lot of other ETL do
[11:43] it what what kind of instruction would I
[11:44] give them on like hey these other skill
[11:46] sets or tools might be necessary and if
[11:48] there's any other sort of gotas around
[11:50] that you if you could highlight those
[11:51] that' be great totally I think just on a
[11:53] very technical level the steps you
[11:54] actually take um are just different um
[11:56] basically instead of writing like SQL or
[11:58] using DBT um you uh just you know uh
[12:01] this is how you like set up a rag
[12:03] pipeline you have a PDF um first you
[12:06] need to parse that PDF uh so either
[12:08] using llama parse or another document
[12:10] parser um that parsing step if you don't
[12:12] get it right then that leads to a lot of
[12:14] kind of like Downstream failure modes in
[12:16] in your LM application um after you
[12:19] purse the document into some
[12:21] representation whether it's text or
[12:23] increasingly we're seeing like
[12:24] multimodal representations as well with
[12:26] um like image representations of a
[12:28] document you then need to chunk that uh
[12:31] document right and so the very naive
[12:34] approach is you basically set a chunk
[12:36] size of like a 1024 tokens and you split
[12:39] every 1,24 tokens right and that
[12:41] specifically also you know introduces a
[12:43] bunch of complexities because if you
[12:45] split like tables down the middle you
[12:47] split Pages uh that that like um there's
[12:50] like that there's like a section that
[12:52] spans multiple Pages or something you
[12:54] somehow need to better like semantically
[12:56] join them together um so that like most
[12:58] information is preserved within a chunk
[13:00] and that you add like the right metadata
[13:02] to that chunk um and then you need to
[13:05] figure out a good way to index it and
[13:07] this is where like a vector database or
[13:08] a graph store document store comes in
[13:10] there's a lot of different ways to index
[13:12] it so just very fundamentally it's just
[13:15] like a different set of like steps you
[13:17] need to do and the issue here and the
[13:19] difference actually with traditional utl
[13:20] is all these steps are kind of like um
[13:23] fuzzy to understand without the endtoend
[13:25] uh performance like with traditional ETL
[13:28] you know it's kind of like you do some
[13:29] step and then it's you you know exactly
[13:32] what you want here like it's really hard
[13:34] to tell what the chunk size you need to
[13:35] set is without having an eval data set
[13:38] and having a rigorous endtoend testing
[13:39] in eval flow yeah oh sorry oh I just
[13:43] want to make sure I think I saw a hand
[13:44] over there yeah do it yeah
[14:09] something yeah so I think we have a few
[14:11] uh audio loaders so I think the default
[14:13] is just uh take so the question was
[14:15] basically how do you integrate audio
[14:16] sources into your rag pipeline using you
[14:18] know L index or other Frameworks um the
[14:20] simplest is probably just like you just
[14:22] directly uh like parse that into text
[14:24] and then ingest it I think in the future
[14:26] as models become more natively
[14:27] multimodal um you might just be able to
[14:30] represent audio as like a specific
[14:32] entity right and then as a chunk almost
[14:34] and directly feed that into a model but
[14:35] I don't think we're there yet um and
[14:37] then okay I'm gonna go
[14:56] yeah for sure I think the benchmarking
[14:59] is important it's also challenging
[15:00] because we're actively working on that
[15:01] right now to basically find a general
[15:03] Benchmark what typically happens is we
[15:05] do like a just within the Enterprise
[15:07] they just do a bake off on their own
[15:08] data um and then compare it and we
[15:10] basically show them a notebook on you
[15:11] know here's how you build a rag Pipeline
[15:12] with llama parse uh here's how you can
[15:14] do it with other parsers yeah um just
[15:17] want to make sure I
[15:19] cover yeah my question is um what
[15:23] options do you have like for versioning
[15:25] or different promotion across
[15:26] environments to you know do staging
[15:29] production uh that's one part and the
[15:31] other one is um what regions are you
[15:34] available so that's maybe a little more
[15:36] easier yeah um I think the versioning
[15:39] piece is is definitely important I think
[15:42] um at a high level we are building out
[15:44] features to help you like better version
[15:46] your pipelines we don't have that yet
[15:47] but it's kind of like upcoming and also
[15:49] requested by some Enterprise customers
[15:51] um and then uh the the second question
[15:53] around um kind of regions where uh the
[15:56] SAS service is in North America it's
[15:59] just hosted on uh but we do we do um
[16:02] kind of like on Prem deployments as well
[16:04] right and and so that's that's part of
[16:06] you know generally the the Enterprise
[16:07] plan that we offer
[16:09] yeah yeah hi um I'm building a rag
[16:12] system for a big fintech basically a
[16:14] bank uh the struggle I'm having is I'm
[16:17] obviously working with the servicing
[16:18] team which has other channels right I'm
[16:20] working on an in a chatbot and a
[16:23] WhatsApp chatbot the servicing team also
[16:25] has say like a help center an ivr a
[16:27] bunch of other like channels right um
[16:30] it's been very tough for me to convince
[16:31] them that maybe the CMS that they're
[16:33] using you know to feed these other
[16:35] sources is not the best way to feed a
[16:37] rack I'm curious to know if you've seen
[16:39] other customers that have like a similar
[16:41] issue where you know internally they
[16:43] want to have like this single source of
[16:45] truth that kind of feeds into all of
[16:46] these channels where the rack systems
[16:48] nature is obviously extremely different
[16:50] than like a help center or an FAQ or
[16:53] that kind of stuff I see wait so why why
[16:56] is that CMS not the right um tool to I'm
[16:59] curious to know if you think that could
[17:00] be the right tool or like getting a
[17:02] little bit more into the details that's
[17:04] like we have like Q&A pairs that's how
[17:06] the CMS works right now which could work
[17:08] for rack but we're missing all the
[17:09] metadata the different clusterings of
[17:12] like different documents for different
[17:13] maybe use cases different credit cards
[17:15] it's a bit tough to explain in a quick
[17:17] question but like have you seen a single
[17:19] system work as a single source of Truth
[17:22] and kind of how have you seen that work
[17:24] like in real big use cases I think um
[17:27] the yeah I think the full details
[17:29] there's probably like a lot to dive into
[17:31] there I think generally speaking what we
[17:33] see is um for like homogeneous data
[17:35] sources where it's like of the same kind
[17:37] of like data type let's say it's all
[17:38] like Financial reports you can generally
[17:40] use like the same set of parameters to
[17:42] basically parse it because there's like
[17:43] an expectation they're roughly the same
[17:45] format for very diverse and different
[17:47] data sources like if all of a sudden
[17:48] you're bringing in not just like uh PDF
[17:51] documents but also um like
[17:53] semi-structured data from like you know
[17:55] uh jir or something or or um uh was it
[17:59] like Salesforce for instance like Json
[18:01] um you typically need to set up like a
[18:02] separate pipeline there and then what
[18:05] you know we both offer on the open
[18:06] source but also the Enterprise side um
[18:08] is this ability to like combine um all
[18:11] these different data sources and you
[18:13] just have to like combine them together
[18:15] and rerank them right and and have some
[18:16] reranking layer at the at the at the top
[18:19] all right thank you um yeah so I've hang
[18:23] on give you the mic just because it's
[18:25] for the it's for the recording so I've
[18:27] been using llama parts for a little bit
[18:29] and first of all I love it so it works
[18:31] really well so thank you for producing
[18:32] it uh however two weeks ago I was
[18:35] working on a project for a client and uh
[18:37] all of a sudden I was getting all these
[18:39] failures and I contacted support via the
[18:41] chat and there was a gentleman helping
[18:43] me out and he's like oh pass me the job
[18:45] IDs gave me the job IDs and all of a
[18:47] sudden just went MIA never replied back
[18:50] so the question is what are the Support
[18:52] options so in case I get stuck over the
[18:54] weekend I could actually get somebody to
[18:56] help me out totally first of all I'm
[18:57] sorry ran into those issues I know we
[18:59] had like a cluster of just uh failures I
[19:01] think that specific weekend it was just
[19:03] it was um it was a good lesson for us
[19:05] right keep in mind we're like 15 people
[19:07] at the company um and so we're uh when
[19:09] you talk to support it's probably like
[19:10] one of the the founding Engineers just
[19:12] like jumping in um so I promise we're
[19:14] making that process more streamlined um
[19:16] typically on the Enterprise side like
[19:18] especially uh for kind of like the like
[19:20] Enterprise plans that we offer I'm happy
[19:21] to chat about this offline like we offer
[19:23] dedicated slas right and so this is kind
[19:25] of like there's some support option
[19:27] we're doing on the Casual like kind of
[19:28] uh like self- serve apis but um we're
[19:31] offering like dedicated slas on on the
[19:41] Enterprise hey so we're building a
[19:44] building hallucination detection and
[19:46] other evaluation systems for our
[19:48] customers that have a very large uh
[19:51] collection of documents and typically
[19:52] that's like uh you could have of course
[19:54] like thousands of PDFs and also those
[19:56] PDFs typically of course contain a lot
[19:58] of table and all that uh and then
[20:00] there's question of how to combine like
[20:02] ocrs and other P processing on that so
[20:05] the question is like what is your
[20:06] general recommendation like does Lama
[20:09] pars uh take care of all these or do you
[20:12] recommend like building some kind of
[20:14] custom system directly on top of llama
[20:16] index or how do you how would you
[20:17] recommend handling that yeah I think I
[20:19] mean I I guess I didn't actually show
[20:20] the capabilities of L first in these
[20:22] slides um but uh maybe if I dig around a
[20:25] little bit I can I try to find the the
[20:27] specific um
[20:29] uh slides where were showcases um yeah
[20:32] like the basically what you want when
[20:35] you parse these documents is you want
[20:36] some generally good parser um that will
[20:39] lay out the text like uh in a spatially
[20:42] aligned way um and so it doesn't matter
[20:44] if you have all the bells and whistles
[20:46] of like bounding boxes and all these
[20:47] things you generally like bare minimum
[20:49] like just want the text to be like
[20:50] Faithfully represented and that's
[20:53] exactly what LL pars does especially for
[20:55] like tables so we have a few examples
[20:56] for instance where like you have tables
[20:57] within a document
[20:59] um and then you lay it out in a
[21:00] spatially aligned way and then when you
[21:02] feed this to an llm llms generally are
[21:05] trained to respond pretty well to like
[21:07] well Spa like just formatted pieces of
[21:10] text uh so they can understand what's
[21:12] going on um in that text trunk uh
[21:14] whereas if you use like a very naive
[21:16] parser like a baseline PDF parser um
[21:19] it's going to like collapse the text and
[21:20] numbers and therefore kind of uh it's
[21:22] going to generate a lot of
[21:23] hallucinations but
[21:25] yeah yeah
[21:29] with the with the increase in size of
[21:31] context windows that are available to us
[21:33] and also the improvements that we're
[21:34] finding for likeing the haste attack
[21:36] kind of problems what is your
[21:38] perspective on where we're headed
[21:39] towards rag yeah I think there's two
[21:42] general Trends uh one is longer context
[21:44] Windows the other is like multimodality
[21:46] um I do think uh there's a few things
[21:48] that will probably go away and a few
[21:49] things that will stay one is uh good
[21:52] parsing is still important um the reason
[21:54] is like you know in the end if your
[21:55] parser is bad you're just going to feed
[21:57] bad data into the Ally and it's going to
[21:59] hallucinate information um what I think
[22:01] will probably go away is as context
[22:03] Windows get bigger chunk sizes can also
[22:05] get bigger um so you know you are
[22:08] probably not going to need to worry
[22:09] about like intra page splitting like
[22:11] splitting a single page into a bunch of
[22:12] smaller chunks um in the future we could
[22:15] see you just uh like putting entire
[22:17] documents as chunks and basically
[22:19] indexing stuff at a document level I
[22:21] think that actually makes a lot of sense
[22:22] because documents are typically like
[22:24] self-contained entities um and I think
[22:25] that'll make a lot easier for developers
[22:28] um however ever in general for a
[22:30] multidock system which you know if
[22:32] you're in a company you probably have
[22:33] like billions of documents uh many
[22:35] gigabytes of documents it's you're
[22:37] probably not going to feed all billion
[22:39] documents into the uh context window on
[22:42] every inference call even with context
[22:44] caching um which I think Gemini has uh
[22:46] because context caching is right now
[22:47] super expensive um probably doesn't make
[22:49] sense from a cost perspective and also
[22:51] is a black box so you don't get
[22:52] accountability into the data um you
[22:54] basically store the Transformer weights
[22:56] for those of you who like kind of are
[22:57] familiar with that um you don't really
[22:59] get like full transparency into what the
[23:01] data is actually being fed um into the
[23:03] language model at each step so actually
[23:05] I think for a variety of reasons the
[23:06] overall idea of retrieval from an
[23:08] external storage system whether it's a
[23:09] vector database or graph database still
[23:11] matters for a variety of reasons um but
[23:14] you know the minute chunking decisions
[23:16] will will probably go away the second
[23:18] thing which you didn't ask about but
[23:19] which I'll talk about anyways is is
[23:20] multimodal um I think as multimodal uh
[23:23] models get better um I think it actually
[23:26] makes sense to basically start having
[23:27] like diers representations of the same
[23:29] thing um so for instance we have a
[23:31] PowerPoint presentation um you're able
[23:33] to uh like represent each page for
[23:35] instance as an image in addition to just
[23:37] like parse text and by storing native
[23:39] image chunks you basically preserve all
[23:41] the information within that data um
[23:43] anytime you do parsing it's an
[23:44] inherently lossy right because you're
[23:46] inherently like trying to extract out
[23:48] stuff in like a textual format as
[23:50] opposed to preserving the full picture
[23:52] um and by having like um like different
[23:55] ways of representing the same amount of
[23:57] data you can basically trade-off between
[23:59] like cost performance and
[24:03] latency just tracking the hi um so I see
[24:08] you've done a lot of work improving the
[24:10] accuracy reduce hallucination I wonder
[24:12] if you are working on anything to make
[24:14] the conversation flow better uh in my
[24:17] experience it's so hard to to to get um
[24:21] the the conversation to to feel natural
[24:23] sometimes they overemphasize the the
[24:24] context data while I just want want to
[24:27] give it a FYI and just continue talking
[24:29] like a normal human so you're you're
[24:32] talking about like basically how to
[24:33] create more natural conversation flows
[24:35] that's the that's the yeah I think all
[24:37] so that that's very interesting I think
[24:41] um the the um the overall answer to that
[24:45] is I think the default way most people
[24:47] are building these conversation flows is
[24:49] you have some like say rag pipeline as
[24:51] like a tool right um and then you
[24:53] basically have an agent as an outer
[24:55] layer um that reasons over the
[24:57] conversation hisory
[24:59] and can um basically you know synthesize
[25:01] the the right answer at the given point
[25:02] in time so the the knobs basically that
[25:05] you want to tune are the the agent
[25:07] reasoning like prompt um as well as the
[25:10] memory and I think the memory is
[25:11] actually pretty important because um
[25:13] right now most memory modules are like
[25:15] very primitive um there's not a lot of
[25:16] good things Beyond just like dumping the
[25:18] conversation history into the prompt um
[25:21] so happy to chat more about that as well
[25:22] but I think there's like a lot of lot of
[25:24] stuff there that you could probably try
[25:26] um just want to double check the time
[25:28] yeah we are time oh okay n yeah how are
[25:31] you using llama agents internally what's
[25:34] the most complex task that's a great
[25:36] question um so for those of you who
[25:38] weren't at the keynote we launched this
[25:39] thing called llama agents which is an
[25:40] open source uh multi-agent um framework
[25:43] basically for helping you basically
[25:45] deploy agents as microservices right now
[25:47] agents primarily live in like notebooks
[25:49] um and the idea is to spin them up as
[25:50] like API Services right now I think
[25:52] we're mostly just like uh using it to
[25:55] build like kind of more constrained
[25:56] simple rag pipelines and it's actually
[25:58] still in an alpha state so I encourage
[26:00] all of you to basically try it out um
[26:02] there's a lot of things that I already
[26:04] know it can't do um for instance have
[26:06] like more General um kind of like uh
[26:09] there's like communication protocols and
[26:11] interfaces that we want to build in a
[26:12] more interesting message CU system but
[26:15] you know if you have an Enterprise use
[26:17] case that's like going agentic and you
[26:18] want to basically kind of understand it
[26:20] as microservices uh so that you can
[26:22] basically reuse encapsulate it um please
[26:24] check it out come talk to us but cool
[26:27] fantastic thank you yeah sorry for going
[26:28] over no that's all fantastic
[26:34] [Music]
