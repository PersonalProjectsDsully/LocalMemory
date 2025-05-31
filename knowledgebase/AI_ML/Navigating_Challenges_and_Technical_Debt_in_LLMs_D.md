---
type: youtube
title: Navigating Challenges and Technical Debt in LLMs Deployment: Ahmed Menshawy
author: Channel Video
video_id: IbJ40EwaNlM
video_url: https://www.youtube.com/watch?v=IbJ40EwaNlM
thumbnail_url: https://img.youtube.com/vi/IbJ40EwaNlM/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence and Machine Learning
tags: ['LLMs', 'Generative AI', 'Fraud Detection', 'Scalable Infrastructure', 'Model Customization', 'AI Challenges', 'Machine Learning Pipeline', 'Training vs Inference', 'AI in Finance', 'NIPS Paper']
entities: ['MasterCard', 'OpenAI', 'LLMs', 'generative AI', 'fraud detection', 'GPU compute', 'NIPS paper 2015', 'foundation models', 'contextual LLMs', 'scalable ML infrastructure']
concepts: ['Generative AI', 'Large Language Models (LLMs)', 'Fraud Detection', 'Model Customization', 'Scalable Infrastructure', 'Training vs. Inference', 'End-to-End Pipeline', 'Challenges in LLM Deployment']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with LLMs', 'Experience with deployment challenges', 'Knowledge of cloud infrastructure']
related_topics: ['AI Ethics', 'Machine Learning Pipelines', 'Model Training', 'Cloud Computing', 'AI in Finance', 'Data Privacy', 'Natural Language Processing', 'AI Deployment Challenges']
authority_signals: ["Mention of MasterCard's press release", 'Reference to NIPS paper 2015', 'Discussion of real-world applications like fraud detection', 'Emphasis on responsible AI deployment']
confidence_score: 0.7
---

# Navigating Challenges and Technical Debt in LLMs Deployment: Ahmed Menshawy

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=IbJ40EwaNlM)  
**Published**: 4 months ago  
**Category**: AI/ML  
**Tags**: large language models, technical debt, ai challenges, machine learning, agi risks, data management, algorithmic risks  

## Summary

# Summary of "Navigating Challenges and Technical Debt in LLMs Deployment"  

## **Overview**  
Ahmed Menshawy discusses the shift from structured to unstructured data in AI, the hype around AGI (Artificial General Intelligence), and the practical challenges of deploying large language models (LLMs). He emphasizes the importance of addressing current risks over speculative future threats, highlights technical hurdles in LLM adoption, and shares insights from MasterCard’s successful implementation of generative AI.  

---

## **Key Points**  
- **Unstructured Data Challenge**:  
  - 80% of enterprise data is unstructured, yet 71% of organizations struggle to manage it effectively.  
  - LLMs are critical for processing unstructured data, but customization and integration remain complex.  

- **AGI vs. Current Risks**:  
  - The hype around AGI and "Doomsday" scenarios should be tempered by focusing on immediate risks (e.g., bias, security) and ethical AI use.  
  - LLMs are "dumb at the core" but accelerate innovation across industries, including fraud detection (e.g., MasterCard improved fraud detection by 300%).  

- **LLM Misconceptions**:  
  - OpenAI is not the sole driver of LLMs; foundational models like GPT-3 (via GBT) improved user interaction by enabling natural language prompts.  
  - Early LLMs required manual data curation (e.g., question-answer pairs), while modern tools like GBT assistants simplify deployment.  

- **Technical Challenges in LLM Deployment**:  
  1. **Access to Foundation Models**: Trade-offs between cost, model size, and performance.  
  2. **Customization Environments**: Enterprises lack infrastructure tailored for large models.  
  3. **User Tools**: Existing tools are inadequate for modern LLM workflows.  
  4. **Scalable Infrastructure**: Inference (GPU/ram) now exceeds training compute, requiring flexible, high-speed scaling.  

- **Pipeline Complexity**:  
  - ML code constitutes <5% of the end-to-end pipeline (per NIPS 2015 paper), emphasizing the need for robust data management, deployment, and monitoring tools.  

---

## **Challenges & Solutions**  
- **Essentials for GenAI Success**:  
  - Access to diverse foundation models.  
  - Customizable, context-aware LLM environments.  
  - User-friendly tools for application development.  
  - Scalable ML infrastructure (inference > training).  

- **Color-Coded Challenges**:  
  - **Access to Models**: Manageable but requires cost-performance trade-offs.  
  - **Customization**: Difficult due to lack of enterprise-ready tools for large models.  
  - **User Tools**: Most challenging; existing tools are outdated for LLMs.  
  - **Infrastructure**: Inference demands outpace training, requiring dynamic scaling.  

---

## **Key Takeaways**  
- Focus on practical applications of LLMs (e.g., fraud detection) rather than speculative AGI.  
- Address technical debt in LLM deployment through tailored infrastructure and tools.  
- Prioritize ethical AI and current risks over hypothetical future threats.

## Full Transcript

[00:00] [Music]
[00:14] hi everyone I'll try to touch on three
[00:16] main things and uh mainly how EI moved
[00:20] from excellence in structured data to
[00:22] llms and the use of unstructured data
[00:25] that most of our organizations have and
[00:27] also we touch on intelligence
[00:29] augmentation
[00:30] and really the hype around AGI and and
[00:33] the Doomsday uh and finally we'll we'll
[00:36] we'll briefly talk about the challenges
[00:38] and Technical debt and and highlight the
[00:39] findings um that we have uh published
[00:43] recently so over the last 10 to 15 years
[00:48] uh most of the AI Valu that we have seen
[00:50] is really coming from structured data
[00:53] and and we have seen uh supervised
[00:55] learning and deep learning doing really
[00:57] well at labeling things and um but this
[01:00] is not the reality like the most of the
[01:02] organizations it it's estimated that
[01:04] most of the organizations data is
[01:07] unstructured specifically more than 80%
[01:10] of the organization's data is
[01:11] unstructured uh and it's also estimated
[01:14] that 71% of them really struggle in
[01:17] managing and and securing this kind of
[01:20] data um and it would have been ideal to
[01:23] really build automated systems try to do
[01:26] certain recommendations uh based on this
[01:29] data uh but now it's easy to to really
[01:32] use it and and have it to cont
[01:34] contextualize uh or customize a
[01:36] contextual language models uh so you can
[01:39] easily have this as an extended memory
[01:41] to to your language model uh and have it
[01:44] formulate answers based on the domain
[01:47] specific data uh that you have within
[01:49] your
[01:51] organization um and uh talking about the
[01:54] AGI and and and the the way we see uh uh
[01:59] uh llm or gentiv VI in general at
[02:01] MasterCard it's really augmenting human
[02:04] productivity uh and and we have seen a
[02:06] lot of hype around you know genitive EI
[02:09] is going to replace our jobs and and
[02:11] Dooms Day and it's taken over and I I I
[02:14] recommend you this great article from
[02:16] from nature which is really talking
[02:18] about uh stop talking about tomorrow's
[02:20] EI Dooms Day when EI poses risks today
[02:23] so stop doing speculations about what EI
[02:27] will become tomorrow and what kind of
[02:28] risks uh that that will have tomorrow
[02:31] and really focus about the the current
[02:34] risk that it poses today and and funny
[02:36] enough some of the the the big speakers
[02:39] about the Doomsday are actually ones who
[02:41] have EI systems out there to the end
[02:43] users with with a lot of risks as we
[02:45] have seen uh in the past uh and and this
[02:48] of course will help Regulators as well
[02:50] be more focused like if we highlight the
[02:52] current risks and so it will help them
[02:55] more focused to have the laws and
[02:57] policies that can really help them
[02:58] regulate the current e systems and at
[03:01] the same time be uh early sort of uh or
[03:04] proactive enough to to adopt any new
[03:06] laws whenever new algorithmic approach
[03:09] uh come up uh also when it comes to the
[03:12] algorithmic foundation like you know
[03:14] like you know Ai and generative EI
[03:17] specifically has been Transforming Our
[03:18] Lives in so many ways but the the
[03:21] algorithmic foundations itself behind
[03:23] llms is not really the one that will get
[03:26] us to AGI and also I I I recommend this
[03:29] talk from Lon one of the fathers of
[03:31] machine learning where he talks about
[03:33] the objective driven uh learning um and
[03:36] the whole idea that you know you know
[03:38] despite the fact that it's Transforming
[03:40] Our Life in so many ways it's really so
[03:43] dump at the core of it uh and it's
[03:46] because of the whole idea that it's
[03:47] autoaggressive and whenever it's making
[03:49] a mistake this mistake really amplifies
[03:52] over time because the other generation
[03:54] of tokens is so dependent on what it
[03:56] already
[03:57] generated and I can't help by by uh but
[04:01] you know praying this code from uh a LEL
[04:05] uh otherwise known as the world first
[04:07] computer programmers so in in her 1843
[04:10] analytics engine paper she mentioned
[04:12] that the analytical engine or machine
[04:15] learning as we call today cannot
[04:17] originate anything by itself uh it can
[04:19] only do what what we ask it or what we
[04:21] order it to perform uh because basically
[04:24] we don't have this algorithmic
[04:25] Foundation that can really get us to
[04:27] something that can originate something
[04:29] by itself and despite being you know
[04:32] about 180 years old this statement still
[04:35] holds uh despite the transformation that
[04:37] we have in so many uh EI algorithms and
[04:40] applications and um funny enough like
[04:44] I've met a lot of people that thinks
[04:45] open eii is the one behind language
[04:48] models and I I do hope that you folks
[04:50] don't share the the same misconception
[04:52] the whole idea of predicting the next
[04:54] token given a specific context is very
[04:57] intuitive and simple idea uh that it's
[05:00] not only a few years old it few decades
[05:01] old uh but was what was really broken
[05:04] with this is is the whole user interface
[05:07] um and and a lot of folks have really uh
[05:10] misunderstood what Chad gbt is all about
[05:13] so Chad gbt really fixes this whole user
[05:16] interface idea that you were able to
[05:19] naturally as as we speak be able to
[05:21] prompt the the llm in in a natural way
[05:24] and and get your response and this is
[05:26] what was was really broken with with the
[05:28] language models before gbt assistants
[05:30] and chat gbt specifically because this
[05:33] kind of data is really rare and and you
[05:35] know LMS or or openi specifically have
[05:39] built their base model based on the
[05:41] internet scale data but then in
[05:43] subsequent phases before the releases
[05:45] gbt assistant they had to go through uh
[05:48] Outsourcing a lot of a lot of folks to
[05:50] really go about generating manual pairs
[05:53] of responses and uh questions and
[05:56] responses uh and as I said like you know
[05:59] You know llms despite you know being
[06:01] dumb at the core of it it's really
[06:03] accelerating uh Innovations everywhere
[06:06] and and we have seen great adoption in
[06:08] in so many Industries and MasterCard is
[06:10] no different uh so we have been drisking
[06:13] this technology responsibly of course uh
[06:16] and we have a recent press release uh in
[06:19] Fab uh where our president uh announced
[06:23] how we used llms generative I
[06:25] specifically to poost fraud detection in
[06:28] some cases by 300%
[06:32] and to go into the the the last topic of
[06:36] my uh of my session is is basically
[06:39] about the challenges so let's first you
[06:41] know understand the essential that
[06:42] anyone needs for building a successful
[06:45] geni application so basically you need
[06:47] to have access to a variety of
[06:49] foundation models and you need to have
[06:51] an environment to customize contextual
[06:54] llms and you need to have an easy to use
[06:57] tool to build and deploy applications so
[06:59] basically all the you know the the
[07:01] widely used tools that we have seen
[07:03] before geni wasn't really applicable to
[07:06] the geni landscape and finally we need
[07:08] to have a scalable ml infrastructure
[07:11] that can really help in scaling up and
[07:13] down not just creating replicas but
[07:15] really creating replicas at a speed that
[07:17] can work for our uh for our end users
[07:20] and I've tried to color code the
[07:22] different Essentials based on the
[07:24] challenges that we we would see in in in
[07:26] building such applications so access to
[07:29] iety of foundation models is is is not
[07:31] so challenging yes still you need to do
[07:34] this kind of tradeoff between cost and
[07:36] the model size but it is available and
[07:39] the environment to customize the
[07:40] language model itself is is is a bit
[07:43] challenging because yes we most of the
[07:45] Enterprises have their own EI
[07:47] environment but it is not really
[07:49] something that is built for uh such
[07:51] models such large models and and the
[07:54] easy to use tool I think is the most
[07:56] challenging part of the whole equation
[07:58] because none of the tools that we have
[08:00] seen before and and most of the tools
[08:02] that that most of you guys use Now is
[08:04] really is really as new as LMS none of
[08:07] them has existed before uh and finally
[08:10] the need to have the scalable
[08:12] infrastructure is is a bit of a
[08:13] challenge as well uh and and we have
[08:15] seen this nice curve from openi where
[08:18] they show that the GPU compute and Ram
[08:21] uh for inference is actually getting
[08:23] more uh or greater than the the comput
[08:26] used for training the model
[08:28] itself um and and before I I I talk
[08:31] about the uh the challenges in llm and
[08:33] highlights of papers that we have
[08:35] recently published uh I just want to
[08:37] bring up this really nice chart from the
[08:39] neps paper 2015 paper and it shows that
[08:43] ml code which is at the core of building
[08:46] any machine Learning System is only a
[08:48] small fraction of what goes into
[08:50] building the end to end Pipeline and
[08:52] specifically it's less than 5% of what
[08:55] goes into building the end to end
[08:57] Pipeline and this is what I call like
[08:59] like I've met a lot of folks uh during
[09:01] you know before my talk and and they
[09:03] think that you know an AI engineer is
[09:05] all about really you know connecting
[09:07] apis and and getting this kind of
[09:09] Plumbing uh in place but I think it's
[09:11] more than that it's it's really
[09:12] everything around this ml code box it's
[09:15] really building this into to end
[09:17] pipeline which is accounts for more than
[09:19] 95% of the work
[09:23] um sorry uh so before the challenges so
[09:27] we just highlight the the two different
[09:29] approaches that are widely used by uh in
[09:32] in the industry so the the first one is
[09:35] is really the closed book approach so
[09:36] you have a foundation model you use it
[09:38] as it is zero shot or few shot learning
[09:41] or you even F tune it with your domain
[09:43] specific data and you know if you ask
[09:46] any of the the folks in the Enterprises
[09:48] they will tell you we really have hard
[09:50] time operationalizing such models
[09:51] because we have certain accuracy
[09:53] constraints so basically the
[09:55] hallucination and they do it very you
[09:57] know confidently uh attribu
[10:00] um you know we can't really understand
[10:02] why the models are saying what they are
[10:03] saying it's tallness they go they go out
[10:06] of date and we have seen uh the
[10:08] different releases that uh that comes
[10:10] out of Obi revision as as you know in
[10:13] gdbr or even in in California AI law uh
[10:16] folks can opt out of the AI systems and
[10:19] and their information can't be used
[10:21] again for training or or influencing the
[10:24] model decisions so you need to be able
[10:26] to do the model editing and and this is
[10:28] really hard in in the foundation model
[10:30] or even if you fine tun your model um
[10:32] and finally customization so you need to
[10:34] be able to customize these models with
[10:37] your own domain specific data and have
[10:39] it really more grounded or more factual
[10:42] to generate information only based on
[10:44] your in your domain specific data and it
[10:47] turned out that the solution to all of
[10:49] these problems is really to couple the
[10:52] foundation model to an external memory
[10:55] uh also known as the rag uh so rag as
[10:59] you can see that you know the original
[11:01] setup remains as it is but we have added
[11:04] this additional context which is coming
[11:07] from your domain specific data um and it
[11:10] is grounding so it's improve the the the
[11:12] factual recall uh there is very nice
[11:15] paper uh around regation reduces
[11:18] hallucination in conversation it kind of
[11:20] Rhymes but like it's very nice and shows
[11:22] how this kind of architectures really
[11:24] reduces the hallucination of the llm
[11:26] systems and you can also have it up to
[11:29] date so you can easily swap in out
[11:32] Vector indices so you can do the
[11:34] revision you can do uh attribution of
[11:36] course like all of the problems we have
[11:38] mentioned in the previous slide you can
[11:40] also do as part of this uh rack setup so
[11:43] you have access to the sources coming
[11:45] out of your retriever so you can easily
[11:48] go back and understand why the model
[11:50] generated certain certain text or
[11:52] certain uh dis
[11:54] surgence but it's not so easy right so
[11:56] like there are so many questions that
[11:58] need to to be answered for this system
[12:01] really to be optimized and and be able
[12:03] to work in production and this is not
[12:05] even half of the question that that we
[12:07] have out there so mostly how do we
[12:10] optimize the Retriever and Generator to
[12:12] work together H so despite like the
[12:15] mainstream uh kind of rag that most of
[12:18] the people are doing right now is really
[12:20] having the Retriever and and the
[12:22] generator as two separate planes that
[12:25] don't that none of them knows that each
[12:27] other exist uh but the actual rag paper
[12:30] uh that was released uh by by fair is is
[12:33] actually about training these two in in
[12:36] parallel so you need to have access to
[12:38] the model parameters and this is now
[12:41] thank thanks to the people who are
[12:43] believing in the open source is possible
[12:45] uh so you can have access to the model
[12:47] parameters the open source model
[12:48] parameters so you can fine-tune the
[12:50] generator to generate factual
[12:52] information based on what it gets from
[12:54] the retriever so it's not just you know
[12:56] attaching an external memory and and you
[12:58] know two sides of the brain that that
[13:00] that are totally
[13:02] separated so this is our paper uh so
[13:05] it's it's very similar to um the the
[13:08] nips one but it it it really shows the
[13:10] unique and different challenges that
[13:13] that we would see in in building an
[13:15] endtoend llm application so you can see
[13:17] that you know the again the the the
[13:19] surrounding boxes around the llm code or
[13:22] the adoption of foundation model is is
[13:25] really you know accounts for more than
[13:27] 90% of what goes into building such
[13:29] application and it's not really just
[13:31] about you know if we pick qu pox about
[13:33] the domain specific data collection it's
[13:35] not just about building or generating
[13:37] the domain specific data it's also how
[13:40] do how do we preserve the access
[13:42] controls within our Enterprises into the
[13:45] uh into these ecosystems so like you
[13:47] know I'm sure most of the organizations
[13:50] that you work with have access controls
[13:52] like you can have access to certain
[13:53] systems but not others so how do we make
[13:55] sure that we don't have a global llm
[13:58] system that can really have access to
[14:00] all of the data that we have behind the
[14:02] scene so we need to maintain the same
[14:04] access controls H and and have certain
[14:06] specialized models that can work for
[14:09] certain tasks and also you know coming
[14:11] back to this nature article that we need
[14:13] to focus about the the current risks
[14:15] that EI poses today and how we build
[14:18] safeguards around it and this was really
[14:20] the core uh I I would say you know
[14:23] principle behind MasterCard to move to
[14:25] to adopt llms so we have the S the seven
[14:28] Corp ible of building responsible EI and
[14:31] and it you know it's all everything
[14:34] around privacy it's around security
[14:36] reliability um and and you know we we we
[14:39] also have this governing body and clear
[14:42] strategy that really enforces this core
[14:44] principles into into the building of
[14:47] such llm applications so yes we can go
[14:49] about really drisking new technologies
[14:51] such as llms and use it for some of the
[14:54] services that we have uh but at the same
[14:56] time we need to have the right
[14:57] safeguards to really make sure that you
[14:59] know the access controls are in place
[15:01] and also we are not you know generating
[15:04] any pied
[15:05] information and um so funny enough one
[15:08] of the reviewers one of the reviewers
[15:10] who accepted this paper mentioned that
[15:12] you know after he he read the paper he
[15:14] was wondering uh if uh if LM is is the
[15:17] right tool to use for for solving some
[15:19] of the applications given the huge
[15:21] number of it challenges and Technical
[15:23] debt uh that that uh that he have seen
[15:26] uh but as the saying goes like you can't
[15:28] make an Without Really breaking few eggs
[15:30] you can't really use this kind of
[15:32] transformative technology uh in Your
[15:34] Business Without Really being a
[15:36] challenged in so many
[15:38] ways uh and that's all I have for you
[15:41] and do check out some of the boxes that
[15:43] we have from the AI engineering team uh
[15:45] from MasterCard it's all about putting
[15:48] EI in production and and the whole other
[15:50] boxes around ml code or the llm uh that
[15:53] we have seen in the figures thank you
[15:59] [Music]
