---
type: youtube
title: EyeLevel Launch: Your RAG is Tripping, Here's the Real Reason Why
author: AI Engineer
video_id: 8RbTZl7bs5U
video_url: https://www.youtube.com/watch?v=8RbTZl7bs5U
thumbnail_url: https://img.youtube.com/vi/8RbTZl7bs5U/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence and Machine Learning
tags: ['RAG', 'AI', 'Enterprise AI', 'Document Processing', 'Semantic Objects', 'Accuracy in AI', 'Data Engineering', 'Search Algorithms', 'AI Solutions', 'Machine Learning', 'Natural Language Processing', 'Vector Databases']
entities: ['EyeLevel', 'IBM', 'The Weather Channel', 'Air France', 'Dartmouth', 'RAG', 'Vector databases', 'semantic objects', 'OCR', 'GPT-3 beta program']
concepts: ['RAG (Retrieval-Augmented Generation)', 'Content Ingestion Challenges', 'Semantic Objects', 'Multi-Field Search', 'Accuracy in RAG', 'Data Engineering Problems', 'Enterprise Applications', 'Search vs. Completion Versions']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Understanding of RAG (Retrieval-Augmented Generation)', 'Basic knowledge of AI/ML concepts', 'Familiarity with document processing techniques']
related_topics: ['Natural Language Processing', 'Document Processing', 'AI Ethics', 'Machine Learning', 'Enterprise AI Solutions', 'Data Engineering', 'Information Retrieval', 'AI in Customer Service']
authority_signals: ["I've been working in this space for 15 years, including at IBM and Watson", "We've been developing our solution for the last four years", 'Our platform achieved 98% accuracy in testing']
confidence_score: 0.85
---

# EyeLevel Launch: Your RAG is Tripping, Here's the Real Reason Why

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=8RbTZl7bs5U)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: rag, ai, machine-learning, data-engineering, accuracy, enterprise-ai, semantic-objects  

## Summary

# Comprehensive Summary of YouTube Video Transcript

**Overview**  
Ben, co-founder of EyeLevel, discusses the challenges of Retrieval-Augmented Generation (RAG) systems, highlighting high error rates due to poor content ingestion. He introduces EyeLevel’s platform, which addresses these issues through advanced data engineering, semantic objects, and multimodal processing to achieve 98% accuracy in enterprise applications.

**Main Key Points**  
- **RAG Challenges**: 35% error/hallucination rates in RAG systems, often due to poor content quality, chunking issues, and loss of context.  
- **Root Cause**: Errors stem from RAG itself, not LLMs or prompts, primarily from flawed content ingestion and retrieval.  
- **EyeLevel’s Solution**: Avoids vector databases; uses *semantic objects* with metadata to preserve context and improve accuracy.  
- **Pipeline Innovations**: Multimodal processing (vision models, text extraction), rewrites content into search/complete formats, and fine-tuned models for ranking.  
- **Results**: 98% accuracy on real-world documents, 120% better than competitors, with enterprise-grade applications built in minutes.  

**Important Quotes/Insights**  
- *"The source of these errors is rarely the LLMs or the prompts... it's typically RAG itself or the quality and relevance of retrieved content."*  
- *"We don’t use vector databases... we create semantic objects with metadata to preserve context."*  
- *"Our users build enterprise-quality applications in minutes, not months."*  

**Actionable Items/Recommendations**  
- Prioritize content quality and context preservation during RAG implementation.  
- Consider alternatives to vector databases, such as semantic objects with metadata.  
- Leverage no-code tools/APIs for rapid RAG application development.  
- Focus on multimodal processing for documents with tables, figures, and text.  

**Additional Notes**  
EyeLevel’s approach emphasizes fine-tuning models for search and completion, with over nine models in their pipeline. Real-world examples (e.g., Air France) demonstrate significant accuracy improvements over traditional methods.

## Full Transcript

[00:00] [Music]
[00:12] hi my name's Ben I'm co-founder of
[00:15] il. and I've been building applications
[00:18] powered with AI for the last 15 years
[00:22] first at IBM research then at IBM Watson
[00:25] later working with Major Brands like The
[00:27] Weather Channel and now at level where
[00:31] we've built the world's most accurate
[00:33] and scalable rag
[00:35] platform using our no code tools and
[00:38] apis our users can upload documents and
[00:41] receive the most accurate retrievals in
[00:43] minutes we've been developing our
[00:45] solution for the last four years and
[00:47] were among the first early users that
[00:49] were admitted to the gpt3 beta
[00:52] program we found it easy to get started
[00:55] with Rag and very difficult to master in
[00:58] our own experience rag ation can have
[01:01] error or hallucination rates as high as
[01:04] 35% especially when the knowledge base
[01:06] consists of the kinds of complicated
[01:08] documents that are commonly found in the
[01:13] Enterprise the source of these errors is
[01:15] rarely the llms or the prompts instead
[01:19] it's typically rag itself or more
[01:21] specifically the quality and relevance
[01:24] of retrieved content and the problems
[01:26] with content generally fall into one of
[01:29] three categories
[01:30] bad or improperly extracted text missing
[01:35] information from the surrounding parts
[01:37] of the document that's lost during
[01:39] chunking or visual elements that are not
[01:42] extracted at
[01:43] all most commonly the problems with rag
[01:47] are content ingestion problems and
[01:49] advanced rag techniques that help you
[01:51] solve these problems can take hundreds
[01:53] of hours to implement we've spent the
[01:56] last four years tackling these difficult
[01:58] data engineering problems
[02:00] and have built the solutions to them
[02:02] into our ingestion
[02:04] pipeline as a result our users are able
[02:06] to build the most accurate rag
[02:08] applications in just minutes and our
[02:10] customers such as Air France and
[02:12] Dartmouth tell us that their rag
[02:14] applications respond correctly more than
[02:16] 95% of the
[02:18] time in a recent study our our platform
[02:22] achieved 98% accuracy against
[02:25] complicated real world documents and
[02:28] outperformed some of the most popular
[02:29] Solutions in Market by as much as
[02:32] 120% I'm going to quickly quickly walk
[02:35] you through the unique approach we take
[02:37] to achieve this high level of accuracy
[02:39] and I'll start by telling you that we
[02:41] don't use Vector databases at all and in
[02:43] fact we think they may not be the best
[02:45] technology solution for a lot of rag
[02:48] applications instead what we do is we
[02:50] create what we call semantic objects and
[02:53] we do a multi field search across the
[02:55] attributes of this
[02:56] object I'll show you what that means
[02:58] with a real example from Air France Air
[03:01] France has been using our platform for
[03:03] the last year to build a chat GPT like
[03:06] co-pilot for their call center
[03:09] agents they wanted to understand their
[03:11] knowledge base which consists of
[03:12] hundreds of thousands of documents just
[03:14] like this one filled with tables figures
[03:18] and texts SC uh scattered across the
[03:20] pages in our ingestion pipeline the
[03:23] first thing we do is run a vision model
[03:25] that we fine-tune with millions of
[03:27] documents to identify where the images
[03:30] the tables and the text are then we run
[03:33] them through dedicated multimodal
[03:35] processing pipelines to extract the
[03:37] visual and written
[03:39] information when you do rag you have to
[03:42] break apart this document into smaller
[03:44] chunks when you do that you quite often
[03:47] lose information from around the chunks
[03:49] things like what section of the document
[03:51] it came from or even which document it
[03:54] came from if you were to ask questions
[03:56] about a book and receive random
[03:59] paragraphs from the the book chances
[04:01] aren't great you'd get good answers and
[04:02] that's kind of what's happening with
[04:04] chunking in the loss of the
[04:07] context that's why we created semantic
[04:09] objects it consists of the original
[04:11] chunk text as well as autogenerated
[04:13] metadata that preserves the information
[04:15] around the text and then we re rewrite
[04:18] the text into two ideal formats one for
[04:21] search and one for completion
[04:30] thank
[04:30] you yeah let let me let me let me show
[04:34] you what that looks like with an example
[04:36] so this is a figure from one of air
[04:38] France's documents if you were to OCR
[04:40] this and extract the text from it
[04:43] vectorize it put it in your vector
[04:45] database it would look something like
[04:46] this look at how much information is
[04:48] lost in the process though instead what
[04:52] comes out of our ingestion pipeline is
[04:54] something like
[04:56] this and this this includes both the
[04:58] search version as well as the completion
[05:01] version of the
[05:03] text when we receive a search query we
[05:06] do something similar we rewrite the
[05:08] query into a format that's compatible
[05:10] with the objects then we search the
[05:13] entire object the original text the
[05:15] autogenerated metadata and the search
[05:18] version of the text we use a fine tune
[05:21] llm to rank the results and improve the
[05:25] accuracy and in total in our ingestion
[05:27] and search there are more than nine
[05:29] models that are
[05:31] fine-tuned to help deliver this kind of
[05:34] accuracy the end result is the world's
[05:36] most accurate rag platform and our users
[05:39] are able to build enter Enterprise
[05:42] quality production ready applications in
[05:44] minutes not
[05:45] months uh I invite you to try it for
[05:48] yourself though IL L.A xray thank you
[05:51] very much thank you Ben all right
[05:56] [Music]
