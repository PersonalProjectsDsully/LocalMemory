---
type: youtube
title: Cohere for VPs of AI: Vivek Muppalla
author: Channel Video
video_id: u3NofYYstaY
video_url: https://www.youtube.com/watch?v=u3NofYYstaY
thumbnail_url: https://img.youtube.com/vi/u3NofYYstaY/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning
tags: ['AI', 'NLP', 'embeddings', 'enterprise AI', 'machine learning', 'vector search', 'multilingual models', 'data retrieval', 'cross-encoder', 'TCO optimization', 'AI tools', 'enterprise solutions']
entities: ['Aiden Gomez', 'Coheres', 'Transformer paper', 'embeddings models', 'Flores multilingual evaluation', 'Nils', 'cross-encoder', 'lexical search', 'TCO', 'citations on drag']
concepts: ['multilingual evaluation', 'cross-encoder ranker', 'total cost of ownership (TCO)', 'embeddings models', 'noisy data handling', 'vector space retrieval', 'enterprise AI solutions', 'contextual search', 'data retrieval optimization', 'tokenizer efficiency']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of NLP concepts', 'familiarity with machine learning workflows', 'knowledge of enterprise data systems']
related_topics: ['natural language processing', 'machine learning model optimization', 'data retrieval systems', 'AI ethics in enterprise', 'multilingual AI models', 'vector search technologies', 'AI cost management', 'information retrieval']
authority_signals: ['Nils and his team have been innovators in the space for a while now', "we're actually pretty excited about what our embeddings models can do", 'this really comes out of the box with like coheres models and apis']
confidence_score: 0.85
---

# Cohere for VPs of AI: Vivek Muppalla

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=u3NofYYstaY)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai, machine-learning, enterprise-ai, nlp, deep-learning, ai-models, rag  

## Summary

```markdown
# Cohere for VPs of AI: Summary

## Overview
Cohere, a data-secure enterprise AI company, focuses on building trustworthy AI models tailored for enterprise use cases. The presentation highlights their generative and retrieval models, emphasizing performance in multilingual support, RAG (Retrieval-Augmented Generation), and cost efficiency. Key principles include prioritizing enterprise needs over academic benchmarks, ensuring data privacy, and offering flexible deployment.

---

## Key Points
- **Product Lines**:  
  - **Generative Models**: Command R (general-purpose) and R+ (enhanced for RAG/tool use).  
  - **Retrieval Models**: Optimized for noisy data, low cost, and multilingual support (e.g., Flores evaluation).  
- **Guiding Principles**:  
  1. Prioritize enterprise use cases (e.g., multilingual, RAG, agent tech).  
  2. Focus on efficiency and TCO (Total Cost of Ownership).  
  3. Enable customization (e.g., tokenizer for cost reduction).  
  4. Ensure data privacy (no customer data used for training).  
  5. Flexible deployment (meet customers wherever they are).  
- **Innovations**:  
  - **Ranker**: A cross-encoder for reranking retrieved documents in RAG pipelines.  
  - **Citations**: Built-in support for RAG applications without additional developer work.  
  - **Embeddings**: Strong performance on noisy data, demonstrated via a demo with archive papers.  

---

## Quotes/Insights
- "Enterprises care about multilingual, RAG, and tool use for agent tech—our focus areas."  
- "Our tokenizer is a secret sauce for low costs and global deployment."  
- "The ranker ensures the most relevant documents are sent to the generative model."  
- "Citations come out of the box, saving developers time."  

---

## Actionable Items
1. **Leverage RAG with Ranker**: Improve search relevance by using Cohere’s cross-encoder for reranking.  
2. **Prioritize Multilingual Support**: Utilize high-performing embeddings for global applications.  
3. **Optimize TCO**: Use the tokenizer and low-cost embeddings to reduce operational expenses.  
4. **Built-in Features**: Take advantage of pre-integrated citations and tool use for faster RAG development.  
```

## Full Transcript

[00:03] [Music]
[00:13] um hey folks uh this is VI super excited
[00:15] to chat with all of yall uh we'll give a
[00:18] a quick talk about uh what coher is all
[00:21] about and uh we'll make sure we have
[00:23] enough time to chat about uh your
[00:24] production challenges with these models
[00:26] or anything else you want to chat about
[00:29] um cool uh quick intro um so we are a
[00:32] leading data security focused uh
[00:34] Enterprise AI company uh our focus is
[00:38] building trustworthy uh Enterprise AI
[00:40] models with our partners for real world
[00:43] business uh use cases um and uh we work
[00:47] with a lot of like strategics across uh
[00:50] various clouds uh and are U have a bit
[00:53] of a swizzle and play when it comes to
[00:55] where we can uh ship and deploy and I'll
[00:57] talk through that uh a little later um
[00:59] so we have have a cracked team of uh ml
[01:02] uh researchers and seasoned Enterprise
[01:04] operators uh Aiden uh who's our
[01:06] co-founder and CEO was one of the uh
[01:09] authors on the uh seminal Transformer
[01:11] paper uh we have uh Phil who's our chief
[01:14] scientist uh he was an NLP lead at
[01:17] deepmind and a professor at Oxford uh
[01:20] Nels who leads a lot of our retrieval
[01:22] efforts was uh built asert uh and then
[01:25] Patrick uh was uh the co-author on the
[01:27] rack paper which is a big uh Focus for
[01:29] us at coher so um Fantastic Team uh
[01:33] that's uh helping us build lots of
[01:34] amazing things um so here's a quick
[01:38] overview of our product line um so we
[01:40] have uh two main arcs so the generative
[01:43] side and then the advanced retrieval
[01:45] models um on the generative side uh we
[01:47] have uh two Flagship models which is
[01:50] command R and r+ R is our uh work cost
[01:54] uh super low cost model uh that's great
[01:57] great for most Enterprise use cases uh
[01:59] and then we have r+ which is uh your
[02:02] more powerful larer model uh for more
[02:05] complex like reasoning tool use rag uh
[02:08] use cases um and on the retrieval side
[02:11] uh uh most people have used some form of
[02:14] an embedding model um and I'll get into
[02:16] that a little later in the talk uh but
[02:18] the ranker is something special uh that
[02:21] I haven't seen quite often in the market
[02:23] uh but we think uh it adds a lot of
[02:25] value especially to your rag pipelines
[02:28] um so we'll get into that too
[02:30] um so when we build that c here uh so we
[02:32] have uh five guiding uh EOS as to how we
[02:36] want to go about things um the first is
[02:39] uh obviously everybody's testing their
[02:40] models and all sorts of academic
[02:42] benchmarks uh but for us what is really
[02:45] important is the performance on uh
[02:46] Enterprise use cases um so we've worked
[02:49] uh with a lot of our partners to ensure
[02:51] that we have an eal Suite uh that is
[02:54] highly customized to Enterprise uh use
[02:57] cases across like let's say health HR
[02:59] Finance uh and that's uh a bit of our
[03:02] goal post as we ship uh each of these
[03:04] like model versions and uh we constantly
[03:07] Benchmark on how we're performing at
[03:09] each of these industries uh and use
[03:11] cases that our customers care about um
[03:15] and then when the next thing is if all
[03:16] about efficiency and scalability right
[03:18] we're uh not particularly chasing the
[03:20] race for having the largest model out
[03:23] there but what we really care about is
[03:25] the Practical use of these models right
[03:27] how how do these models get used and how
[03:30] cheap is it uh uh and how easy is it for
[03:33] you to run it as a customer um the next
[03:37] big thing is obviously customization um
[03:39] you as as much as we'd like for all of
[03:41] these models to work out of the box
[03:43] there's always a certain Niche that uh
[03:46] customers want to customize this for uh
[03:49] and we offer a variety of things uh some
[03:51] of which are pretty intrusive uh We've
[03:53] helped our customers uh with taking our
[03:56] base model uh and retraining that with
[03:59] their Enterprise specific data uh for
[04:02] domain adaptation we can do a full
[04:03] retraining of the model for you with
[04:05] your data uh and then obviously the uh
[04:08] pretty typical last few layers uh
[04:10] retraining which is self serve on our
[04:13] platform um data prominence and privacy
[04:16] is another uh big Focus uh for us uh
[04:19] We've uh worked quite a bit to ensure
[04:21] that all of the data that we've uh
[04:23] collected for building our models uh is
[04:26] meets up to the Enterprise uh standards
[04:28] uh and we offer in di ification for any
[04:31] IP claims uh that you might run into as
[04:33] a customer uh and then obviously we
[04:35] don't ever use any of your data to train
[04:38] our model so um so that that's a
[04:40] guarantee from us uh and uh deployment
[04:43] flexibility uh as I mentioned we're
[04:45] available on pretty much every major
[04:46] cloud provider uh and then we also allow
[04:49] you to deploy uh on Prem or in your own
[04:52] VPC um and wherever uh your compute and
[04:55] your data is that's where we'll meet you
[04:57] at um cool um so just a quick look at uh
[05:02] uh you know your typical performance
[05:04] metrics uh as I mentioned uh something
[05:06] that enterprises like repeatedly tell us
[05:08] is uh they care about like multilingual
[05:10] they care about like rag um and Tool use
[05:14] for upcoming like agent Tech use cases
[05:16] uh so a lot of our Focus has been uh in
[05:19] these areas uh these are some benchmarks
[05:22] from Hotpot QA bambole uh Berkeley
[05:25] function calling uh that our models uh
[05:28] are quite uh good at uh and um another
[05:32] example of like how we try to innovate
[05:35] is uh we try to make sure that as we are
[05:37] building uh these Stacks we're
[05:40] incorporating all of the features that
[05:42] people care about out of the box and
[05:44] they don't have to do extra work
[05:46] citations on drag is a great example of
[05:48] this uh for most people you have to do a
[05:51] lot of work to actually build this
[05:53] functionality with like other apis but
[05:55] this really comes out of the box with
[05:56] like coheres models and apis you don't
[05:59] have to do anything additional as a
[06:01] developer uh to build uh get citations
[06:04] and which is uh very important for any
[06:07] rag based like
[06:08] application um uh on the multilingual
[06:12] front uh we have one of the best
[06:14] performance when it comes to uh the
[06:16] Flores multilingual uh evaluation uh and
[06:19] we also have a bit of a secret sauce
[06:21] with our uh tokenizer uh which uh helps
[06:23] keep costs really low right uh and uh
[06:26] that's again TCO is again a very big
[06:29] thing for Enterprises uh and uh it
[06:31] allows our customers to take that same
[06:34] model deploy across the globe on with
[06:37] their customers uh which is very
[06:40] important um Switching gears towards the
[06:43] embeddings models uh again uh given uh
[06:46] Nils and his team have been innovators
[06:48] in the space for a while now uh and uh
[06:52] We've uh done quite a bit of work to
[06:55] make our make sure our performance is
[06:57] great on like noisy data and at a super
[06:59] for low cost uh uh in this particular
[07:02] space um so we're we're actually pretty
[07:04] excited about what our embeddings models
[07:07] uh can do and this is all almost always
[07:09] like one of the top things that uh our
[07:11] customers are uh excited about um but
[07:15] embeddings uh is a pretty complex space
[07:17] and not without its uh challenge um so
[07:20] we we try to build this like fun demo
[07:22] where we took all of the archive papers
[07:25] uh and we asked it a question uh when
[07:27] was the attention paper um built by uh
[07:30] paper published by Aiden Gomez who's our
[07:32] founder and we tried this across like a
[07:34] bunch of like embeddings model so some
[07:36] common patterns that we see is um
[07:39] archive is a great example of like where
[07:42] you have different kinds of like data
[07:44] right you have like the title when was
[07:46] the paper published the dates uh you
[07:48] have the various authors you have like
[07:50] the actual paper itself and in many ways
[07:52] this represents the kind of data you
[07:53] might see in Enterprises right um so
[07:56] when you uh actually build the
[07:57] embeddings for this um you get a fairly
[08:00] complex like vector space uh and your
[08:03] search queries might not actually like
[08:05] map neatly to this right uh and this is
[08:08] sort of like where our ranker comes in
[08:11] uh so what our ranker does is once you
[08:13] have uh all of these uh retrieved
[08:16] documents uh it help it's a cross
[08:17] encoder that helps you uh rerank the
[08:21] retrieved set and make sure that that's
[08:23] the one that you send into your context
[08:24] with the generative model um and uh
[08:28] here's the read ranker in uh action um
[08:32] so what this demo is showing you is uh
[08:34] we search uh for the Transformer paper
[08:37] by aen so you have three different types
[08:39] of like search patterns over here a
[08:41] lexical search then an embeddings based
[08:43] search uh and uh the coher rerank based
[08:46] search right uh and the uh various forms
[08:49] of these like retrievals obviously give
[08:51] you the responses but they are stacked
[08:53] rank at different places in the
[08:55] retrieval set which means the overall
[08:57] accuracy of your rag system might be low
[09:01] uh and rerank is what's helping you to
[09:02] make sure uh that isn't the case uh this
[09:05] Builds on top of like other things that
[09:07] people care about like chunking
[09:09] strategies uh but making those more
[09:11] optimal uh another impact of this ranker
[09:14] is again total cost of operation because
[09:17] most of the expense for your models is
[09:19] coming in from the input tokens right uh
[09:22] and if you were able to like narrow in
[09:25] uh to the right uh uh context and do
[09:28] that quickly uh you could pass in very
[09:30] minimal amount of context to your large
[09:32] language model which drives on drives
[09:34] down your overall cost of like operation
[09:37] uh and that uh is again very important
[09:39] in the Enterprise uh
[09:41] setting um yeah and when it comes to
[09:44] deployment options like I said we have
[09:46] our SAS API uh that we can help uh you
[09:49] manage run your uh workloads uh but then
[09:52] we're also on all of the major Cloud AI
[09:55] Services s Sage Sage maker Bedrock um
[09:58] oci
[10:00] uh and private deployment across all of
[10:02] these Cloud providers and P um also on
[10:05] premise deployments if if that's
[10:07] something you care about um security and
[10:10] privacy obviously is pretty uh top of
[10:12] mind for us so we make sure we're
[10:14] compliant with uh uh the standards that
[10:16] our customers are often asking us uh for
[10:19] um and then the last bit is just
[10:22] enabling like developers um so we uh
[10:25] obviously have a a pretty tight
[10:27] integration with things like Lang chain
[10:29] llama index uh but we also have an open
[10:31] source like toolkit uh that comes out of
[10:34] the box uh with uh various forms of like
[10:37] connectors um and that lets you uh
[10:40] ingest uh data pretty easily into your
[10:42] systems and lets you have full control
[10:45] over the things you're uh building um
[10:47] and don't have to really uh look uh for
[10:50] a ton of different like options uh as
[10:52] you're developing your uh Enterprise
[10:54] applications so uh that's it from me and
[10:58] I'd love to take any questions or chat
[11:00] and we also have Sandra here uh from coh
[11:03] here so she'll she'll be happy to
[11:05] help thank thank you very much yeah
[11:08] maybe two questions so on first or
[11:10] second slide you show your uh investors
[11:12] and the selected Partners right I saw
[11:14] Accenture I saw McKinzie can you explain
[11:16] a little bit like how that partnership
[11:19] uh work right and the second question
[11:22] like you can skip if someone else like
[11:23] has another one is can can you like
[11:26] maybe without disclosing uh customers
[11:28] and all give us like a few samples of
[11:31] where you clients picked up coh here
[11:33] versus other Solutions and and kind of
[11:36] why to explain where you win right on
[11:38] the on the Enterprise world yeah
[11:40] absolutely uh happy to chat about that
[11:42] um so uh I think the typical challenge
[11:45] with all of these enter um Enterprise
[11:47] like generative AI models is the Last
[11:49] Mile Challenge right like uh there's uh
[11:52] so many different like arcs of like
[11:54] customization that's needed uh with the
[11:56] Enterprises uh and uh there's a lot of
[11:59] like traditional uh like players who've
[12:02] been around for a while and have great
[12:04] relationships with the Enterprises uh
[12:07] have a deep understanding of like the
[12:09] various like uh business domains uh
[12:11] that's where uh the McKenzie and
[12:13] Accenture and all of these companies
[12:14] come in um so they've been uh really uh
[12:17] helpful for us to co-develop like the
[12:20] product like make sure that we're able
[12:22] to effectively bridge that like Last
[12:24] Mile Gap with them um and yeah that
[12:27] hopefully that that helps uh and then
[12:29] onto your second question I would say um
[12:32] uh in terms of like winnability I think
[12:34] like the main uh aspects that has been
[12:37] uh resonating a lot with our customers
[12:39] is this control over the data and
[12:41] control over the compute right uh given
[12:43] we're available pretty much everywhere
[12:45] uh a lot of like the customers care
[12:47] about that private Cloud deployment the
[12:49] ability to fine tune in that uh private
[12:52] Cloud environment uh which is pretty big
[12:54] uh for a lot of people and making sure
[12:56] that their Enterprise data does not
[12:58] leave their own ecosystem um and
[13:01] specific examples for that have been uh
[13:03] companies in uh let's say HR or
[13:06] Healthcare or even uh folks who are
[13:08] trying to take their in-house like code
[13:10] and uh build a custom model that's uh
[13:13] working with uh their code base uh those
[13:16] are the styles of applications uh that
[13:18] uh we've seen a lot of like uh impact
[13:20] and success
[13:21] with
[13:26] yeah so I'm curious um uh for text
[13:30] classification what is the latest best
[13:33] practice I see on your website you have
[13:34] a classify endpoint R the classifier uh
[13:38] is that still the
[13:39] recommendation yeah uh that's that's a
[13:41] great question I I the the way I like to
[13:44] think about uh these things is is's
[13:46] always the Arc of like uh um and I think
[13:50] like Jerry in his earlier talk to this
[13:52] right which was what phase of like
[13:54] development you're in uh if you're
[13:55] trying to like prototype or you're
[13:57] trying to productionize and what's your
[13:59] scale of like a production setting uh
[14:01] which is important to consider for these
[14:03] things uh for uh if you're just trying
[14:06] to like get off the ground like quickly
[14:08] I would say just using the generative
[14:11] model off the shelf is obviously always
[14:13] great it gets you off the ground really
[14:15] quickly uh when you're trying to like
[14:17] productionize something that's when I
[14:18] would start thinking hey do I need a
[14:20] bespoke model uh or like the the general
[14:24] model is good enough and what are sort
[14:26] of like the cost of operation like
[14:27] differences and like the cost of like
[14:29] maintenance differences and also the
[14:31] scale right like I mean if if you're
[14:33] going to try to do something that's uh
[14:35] you know tens of thousands like TPS uh
[14:38] then having a purpose Bel like model for
[14:40] that is the route I'd go uh versus you
[14:43] know a more heavy General model uh which
[14:46] wi serve other other needs um so yeah
[14:49] both of those are good options depending
[14:52] on what you're trying to accomplish just
[14:53] just quick quick followup if we actually
[14:55] train a classifier with you is that also
[14:58] a Transformer model just more
[14:59] specialized yeah exactly okay yeah got
[15:02] thank
[15:05] you no I think we're done oh no we got
[15:08] one one question here we go just a quick
[15:12] question when we were looking at coh
[15:15] here you know probably early last or
[15:17] middle of last year um one of the
[15:21] challenges with the models that we found
[15:22] were the input contact size limit were
[15:24] quite small how has that evolved as you
[15:27] guys have sort of created the next you
[15:29] know sets of models yeah that's a great
[15:32] question so our latest generation models
[15:34] are fairly competitive 128k uh context
[15:37] input uh Windows uh and we're constantly
[15:40] looking to uh figure out how to like up
[15:42] them um so context window I would say
[15:44] should be not a problem for like most
[15:47] applications uh at the moment
[15:52] yeah cool well we're actually slightly
[15:55] early but yeah I'd like to thank you for
[15:57] giving the talk thank you for really
[15:59] thank you so much yeah thank you yeah
[16:02] [Applause]
[16:05] [Music]
