---
type: youtube
title: Building efficient hybrid context query for LLM grounding: Simrat Hanspal
author: Channel Video
video_id: pijYURicI1Y
video_url: https://www.youtube.com/watch?v=pijYURicI1Y
thumbnail_url: https://img.youtube.com/vi/pijYURicI1Y/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence and Machine Learning
tags: ['Retrieval Augmented Generation', 'Machine Learning', 'NLP', 'Data Pipelines', 'Model Evaluation', 'AI Systems', 'Information Retrieval', 'System Design', 'Query Understanding', 'Data Quality']
entities: ['Anshul Gupta', 'Huraa', 'GraphQL', 'Semantic Search', 'Relational Databases', 'Role-Based Access Control', 'Insert Mutation', 'Hybrid Query', 'Tutorial', 'AI-Powered Query Generation']
concepts: ['Retrieval Augmented Generation (RAG)', 'Query Understanding', 'Data Processing Pipelines', 'Model Evaluation Metrics', 'Latency Optimization', 'Information Retrieval', 'Natural Language Processing (NLP)', 'System Design Tradeoffs', 'User Intent Analysis', 'Data Quality Assurance']
content_structure: tutorial/how-to
difficulty_level: intermediate
prerequisites: ['Basic understanding of machine learning concepts', 'Familiarity with NLP techniques', 'Experience with data engineering pipelines']
related_topics: ['Machine Learning System Design', 'Natural Language Understanding', 'Data Pipeline Optimization', 'Model Evaluation Techniques', 'AI Ethics in Search Systems', 'Database Security Practices', 'Query Language Design', 'Latency Management in AI Systems']
authority_signals: ['This is a comprehensive guide to building RAG systems', "I've seen many teams struggle with these exact challenges", 'The key tradeoffs between retrieval and generation']
confidence_score: 0.85
---

# Building efficient hybrid context query for LLM grounding: Simrat Hanspal

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=pijYURicI1Y)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: llm grounding, rag pipeline, semantic search, structured search, secure api, nlp applications, e-commerce search  

## Summary

# Summary of "Building Efficient Hybrid Context Query for LLM Grounding"

## Overview
This video discusses the challenges of traditional keyword-based search systems in e-commerce and introduces a solution using **Retrieval Augmented Generation (RAG)** to enable natural language queries for product searches. The focus is on building **hybrid context queries** (semantic, structured, and mixed) while ensuring **security** and **scalability** with tools like Hura. The speaker demonstrates how to handle both "happy flows" (valid queries) and "unhappy flows" (malicious attempts) in a secure RAG pipeline.

---

## Key Points

1. **Limitations of Keyword-Based Search**  
   - Traditional systems struggle with natural language understanding and contextual relevance.  
   - LLMs are "frozen in time" and cannot handle unseen data without context.

2. **RAG Pipeline for E-commerce**  
   - **Retrieval Augmented Generation (RAG)** combines LLMs with external data to improve query accuracy.  
   - Hybrid queries (e.g., "essential oil diffusers under $500") require handling **semantic** (descriptive), **structured** (filters like price), and **mixed** contexts.

3. **Security in Enterprise Applications**  
   - Malicious queries (e.g., inserting unauthorized data) can exploit weak access controls.  
   - **Hura** enables secure API creation with role-based permissions to restrict actions like `INSERT` or `UPDATE`.

4. **Hura's Role in RAG**  
   - Hura simplifies building secure, scalable APIs for querying diverse data sources.  
   - Example: A malicious query attempting to insert a product (`INSERT mutation`) is blocked by restricting roles to `SELECT` only.

5. **Hybrid Query Handling**  
   - Demo shows successful execution of semantic (e.g., "essential oils for relaxation"), structured (e.g., "products < $500"), and hybrid (e.g., "diffusers between $500-$1000") queries.  
   - Unhappy flows (malicious queries) are mitigated via strict role permissions.

---

## Quotes & Insights

- **"LLMs are frozen in time and can't handle unseen data without context."**  
- **"Hura enables you to build secure data APIs over your multiple different data sources in no time."**  
- **"The role has gotten in. Now, let's query the same thing with the new rule..."**  
  - Highlighting the importance of **role-based access control (RBAC)** to prevent unauthorized actions.

---

## Actionable Items

1. **Implement RAG Pipelines**  
   - Transition from keyword-based to natural language queries using RAG for better contextual understanding.

2. **Secure Data Access**  
   - Use Hura to define roles with **restricted permissions** (e.g., only `SELECT` for product search roles).

3. **Test Query Types**  
   - Validate semantic, structured, and hybrid queries in your system.  
   - Simulate "unhappy flows" (e.g., malicious queries) to ensure robustness.

4. **Monitor and Mitigate Risks**  
   - Block unauthorized actions (e.g., `INSERT`, `UPDATE`) via RBAC.  
   - Regularly audit query logs for suspicious activity.

---

## Conclusion
The video emphasizes the need for secure, context-aware query systems in e-commerce, leveraging RAG and Hura to handle complex, mixed queries while preventing security vulnerabilities. The demo underscores the importance of role-based permissions and proactive testing for both valid and malicious inputs.

## Full Transcript

[00:01] [Music]
[00:17] hey hey hey how's everyone this is simr
[00:20] hanspal technical evangelist at hura and
[00:23] today I'm going to talk to you about
[00:25] building efficient hybrid R
[00:28] queries let us understand this with the
[00:31] use case of product search in e-commerce
[00:33] domain present day product search is
[00:36] mostly keyword-based keywords are not
[00:39] great at capturing the complete intent
[00:41] of the user search query so you want to
[00:43] move to using natural language but
[00:45] product search can be either contextual
[00:47] where you're looking for when you're
[00:49] searching for product based on the
[00:50] descriptive nature or or it can be
[00:53] completely structured where you're
[00:54] querying based on the structured fields
[00:56] or it can be both large language models
[00:59] are great but they're frozen in time and
[01:02] they cannot solve task on data they have
[01:04] not seen before one of the ways to
[01:06] expose the Unseen data to large language
[01:08] model is by providing context to the
[01:11] question alongside the question this
[01:13] helps the large language model generate
[01:15] more accurate and grounded answers this
[01:18] powerful technique is called retrieval
[01:20] augmented generation or r a in short so
[01:24] you see we need to build a rag pipeline
[01:26] for our product search use case we also
[01:28] need to make sure that our Riot pipeline
[01:30] is production ready and will not leak
[01:32] any sensitive data even if
[01:35] prompted this security concern has been
[01:38] one of the primary concerns of
[01:40] Enterprises when building geni
[01:44] applications data driven applications
[01:46] have been around for a while then why
[01:48] are we talking about secure data
[01:50] retrieval all over again for Gen
[01:53] applications well this is because we are
[01:55] seeing a paradigm shift in application
[01:58] development with data driven
[02:00] applications data is mostly constant and
[02:03] it is the application or the software
[02:05] that evolves for any different or new
[02:08] functionality for example product search
[02:11] on current e-commerce websites would
[02:13] pick constant data fields only the
[02:15] records or the results would
[02:19] change while in context um context driv
[02:23] or rag application the data is no longer
[02:26] a constant data packet and it needs to
[02:29] adapt to the dynamic needs of the users
[02:31] natural language query with natural
[02:34] language query there is no structural
[02:36] limitations and it can and it gives a
[02:40] scope for malicious
[02:42] attack good news hura enables you to
[02:45] build secure data API over your multiple
[02:47] different data sources in no time hura
[02:50] apis are graphql apis and hence they
[02:54] dynamic in nature so you get unified
[02:57] Dynamic secure data API in no time just
[03:00] what we needed so let's get started with
[03:03] building a rag pipeline for our product
[03:05] search use
[03:07] case let us again look at what are the
[03:10] different queries that we uh that we can
[03:13] expect for our rag applications we can
[03:15] have semantic search where we searching
[03:18] based on semantic similarity with
[03:20] product description from product uh
[03:22] Vector DB we can also have structured
[03:25] search where we are searching based on
[03:28] structured fields in the relation
[03:30] database um like for example price and
[03:33] category in postest and this requires
[03:36] converting the natural language query
[03:38] into a structured query like SQL or
[03:41] graphql then we can also have hybrid
[03:44] queries these searches have the elements
[03:46] of both semantic and structured queries
[03:49] with Hur we don't need to build separate
[03:51] data apis for each of them we can build
[03:53] a unified data API for all three of
[03:57] them so let's get started we start by
[04:00] connecting a multiple different data
[04:02] sources with hura and then we query it
[04:05] using a single graphql API I've also
[04:08] built a streamlet application which
[04:10] takes in the user input calls the large
[04:13] language model generates a graphql AP
[04:16] query which then gets executed on hup so
[04:20] let's head over to hup console to get a
[04:23] feel of what it looks like to start
[04:26] we'll go to the data tab to connect all
[04:29] of for different data sources I'm not
[04:31] going to do that because I have my um
[04:35] product post table and product Vector
[04:37] table already integrated as I mentioned
[04:40] before you can use hura to query both um
[04:44] your relational and Vector DB and
[04:46] multiple data sources using a single
[04:48] graphql API but for the sake of
[04:51] Simplicity of this demo I'm going to be
[04:53] using only the vector DB so I'm using
[04:56] vb8 in this case where I have my my
[04:59] vectors and I have also got my price and
[05:03] category structured Fields here one
[05:05] thing to note here is that I have used
[05:07] hur's event to autov vectorize um my
[05:11] records into my Vector DB which means as
[05:14] in when a new record got inserted into
[05:16] my for CR table it got autov vectorized
[05:19] and saved in my Vector DB amazing I
[05:22] know so let's go back to let's go to our
[05:26] API tab this is where you will you can
[05:29] um play around execute different queries
[05:31] and see the
[05:34] results nice now that we have gotten a
[05:38] fairly decent sense of what hura console
[05:41] is like we can move to the Streamline
[05:43] app that I have created as you can see
[05:47] there are few configurations on the left
[05:49] hand side panel so you have hur's
[05:51] endpoint and admin secret this is
[05:53] required to connect with Hur securely
[05:56] and then I also have open eyes um API
[05:59] key this is required for the chat
[06:01] completion API that I'm
[06:04] using so let's begin Let's uh begin with
[06:07] querying the three different uh context
[06:11] uh that we were talking about that we
[06:13] want to fetch so let's start with Pur
[06:15] semantic one let's look at the different
[06:18] product descriptions that we have and
[06:20] pick something let us pick um products
[06:23] on essential oils so let me say show me
[06:28] essential
[06:30] oils for
[06:40] relaxation great so we've gotten the
[06:43] graph C query which has identified
[06:45] essential oils for relaxation as the
[06:47] descriptive part of the query which we
[06:49] want to find in our Vector DB by doing a
[06:53] semantic search and we can also see that
[06:56] we have gotten the results for this
[07:00] query nice let's go over and execute a
[07:04] structured query price is a good field
[07:06] to execute execute a structured query so
[07:09] let's say um let say show me all
[07:13] products less
[07:16] than
[07:18] price
[07:25] $500 wait so it has rightly identified
[07:28] that there is a price filter with the
[07:31] less than
[07:32] condition and it shows you all the
[07:35] different products with price less than
[07:38] 500 nice let's execute a hybrid query
[07:46] now let's see looking for essential oil
[07:50] diffusers in the price range of $500 to
[07:57] ,000 thanks so we got a graphel query
[08:01] where it identified amazing essential
[08:03] oil diffuser as the semantic search
[08:07] query and then the price filter which is
[08:09] between 500,000 and we received our
[08:14] results
[08:16] nice so far we have executed only the
[08:19] happy flows um we have not looked at any
[08:23] other query Weare of unhappy flows but
[08:26] let's say I had an evil intent and I
[08:28] wanted to execute a malicious query uh
[08:31] which is not the typical queries that we
[08:34] just looked at so I have a malicious
[08:36] query let's execute this so this one is
[08:41] requesting to insert a project of ha
[08:44] hairil product um with the name special
[08:48] oil
[08:50] and price of 10,000 doar category is
[08:55] home fantastic hair oil is the
[08:57] description and let's also add the
[08:59] project ID and say this is
[09:03] 7,1 okay let's execute
[09:09] this so as you can see it it has
[09:12] generated a graphql query of type insert
[09:16] mutation but what we see is that it has
[09:19] also inserted the query so let's go back
[09:21] to our table and console and look for
[09:26] product
[09:27] ID equal to
[09:32] 10,1 just remove the quote because this
[09:36] [Music]
[09:37] is integer
[09:39] fi and there you go we have the product
[09:43] which has gotten inserted into the
[09:45] database um this was not the intended
[09:48] Behavior this is not what should have
[09:50] happened so let us quickly go back to
[09:52] our hurra console again and this time we
[09:56] are going to be defining a new role with
[09:58] very restricted permissions so that we
[10:01] only provide select permission and such
[10:04] that this does not happen again so I'm
[10:05] going to create a new role let's call it
[10:07] product search b and I'm going to
[10:11] provide only search permission let's go
[10:15] without any checks I'm going to keep it
[10:17] really simple let me allow all the
[10:20] product all the columns to be accessible
[10:22] for this
[10:23] Ro that's about it nice so the role has
[10:27] gotten ins
[10:29] now let's query same thing with the new
[10:31] rule so let's say product search b but
[10:36] this time let me just modify this quy a
[10:38] little bit and say
[10:41] 7,2 Okay so let's execute this and see
[10:44] what
[10:48] happens nice so we got the same insert
[10:51] mutation query um to be generated but
[10:54] this thing there was an error executing
[10:56] this rightly so because we have defined
[10:59] a role which does not have the
[11:01] permission for insert
[11:03] queries great so this is all from me
[11:06] thank you everyone um thank you once
[11:09] again so let us really quickly recap in
[11:11] this demo we learned how we can use hura
[11:14] to build hybrid query context um for
[11:17] your sophisticated rag applications like
[11:19] product search if you like the demo or
[11:22] would like to use Hur for your rag
[11:24] application please reach out to me these
[11:26] are my contact details and thank you so
[11:28] much
