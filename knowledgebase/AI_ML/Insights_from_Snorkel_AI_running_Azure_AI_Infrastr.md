---
type: youtube
title: Insights from Snorkel AI running Azure AI Infrastructure: Humza Iqbal and Lachlan Ainley
author: AI Engineer
video_id: LJa1SjCkYas
video_url: https://www.youtube.com/watch?v=LJa1SjCkYas
thumbnail_url: https://img.youtube.com/vi/LJa1SjCkYas/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence & Machine Learning
tags: ['AI infrastructure', 'Enterprise AI', 'Machine Learning', 'Cloud Computing', 'Synthetic Data', 'Multimodal Models', 'Model Alignment', 'Long Context Evaluation', 'AI Training Pipelines', 'Cloud Architecture']
entities: ['Azure', 'OpenAI', 'Mistral', 'Maya chip', 'Mea chip', 'Large Vision Language Models (LVMS)', 'F Grain Evaluation', 'Long context models', 'Enterprise alignment', 'Multimodal alignment']
concepts: ['Enterprise alignment', 'Multimodal alignment', 'Synthetic data generation', 'Long context evaluation', 'AI infrastructure optimization', 'Flywheel effect', 'Model training', 'Cloud computing scale', 'Regulatory compliance', 'Data center topology']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with cloud computing platforms (e.g., Azure)', 'Knowledge of machine learning model training pipelines']
related_topics: ['AI infrastructure optimization', 'Machine learning model alignment', 'Synthetic data generation techniques', 'Enterprise AI deployment', 'Multimodal machine learning', 'Cloud computing architecture', 'Long context language models', 'AI regulatory compliance']
authority_signals: ["we have a real cycle around um you know learning from working with organizations like openai mistol and others that have trained their models on azure's infr", "we're very excited about that's great"]
confidence_score: 0.8
---

# Insights from Snorkel AI running Azure AI Infrastructure: Humza Iqbal and Lachlan Ainley

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=LJa1SjCkYas)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai infrastructure, data development, enterprise ai, model fine-tuning, azure ai, machine learning, enterprise deployment  

## Summary

# Summary of "Insights from Snorkel AI running Azure AI Infrastructure"  

## **Overview**  
The video features Humza Iqbal and Lachlan Ainley from Snorkel AI discussing their work in fine-tuning large language models (LLMs) for enterprise use cases, challenges in data development, and their experience leveraging Azure AI infrastructure. Key themes include addressing data quality, scalability, domain-specific alignment, and optimizing AI infrastructure for complex workloads.  

---

## **Key Points**  
- **Snorkel AI’s Focus**:  
  - Specializes in **data development** for enterprise AI, ensuring LLMs meet organizational goals, compliance, and domain-specific requirements.  
  - Emphasizes **fine-tuning** off-the-shelf LLMs to address gaps in data quality, scalability, and alignment with enterprise needs.  

- **Challenges in AI Development**:  
  - **Data Quality**: Traditional benchmarks (e.g., LMIs) are insufficient for enterprise use cases; domain-specific metrics are critical.  
  - **Scalability**: Requires robust infrastructure to handle large-scale training and inference.  
  - **Alignment**: Ensuring LLMs comply with company policies, regulations, and ethical standards.  

- **Research Areas**:  
  - **Long Context Evaluation**: Improving models’ ability to handle extended contexts, beyond tests like "Needle in a Haystack."  
  - **Enterprise Alignment**: Ensuring models adhere to organizational goals and avoid harmful outputs.  
  - **Multimodal Alignment**: Using vision-language models (VLMs) to generate synthetic data for training downstream models without manual annotation.  

- **Azure AI Infrastructure**:  
  - Leverages Azure’s global data centers, diverse accelerators (AMD, NVIDIA, custom Maya chip), and optimized networking for AI workloads.  
  - Focuses on **supercomputing-scale optimization** to deliver high throughput and low latency.  

---

## **Important Quotes/Insights**  
- **Humza Iqbal**:  
  > "Off-the-shelf LLMs aren’t sufficient for enterprise use cases; we need to tailor them with domain-specific data and benchmarks."  

- **Lachlan Ainley**:  
  > "Azure’s infrastructure allows us to optimize for every layer of AI workloads, from CPUs to accelerators, ensuring scalability and performance."  

- **Key Takeaway**:  
  > "The future of enterprise AI lies in domain-specific alignment, synthetic data generation, and infrastructure that scales with AI’s growing complexity."  

---

## **Actionable Insights**  
1. **Leverage Azure’s Diverse Accelerators**: Combine AMD, NVIDIA, and custom silicon to optimize AI workloads.  
2. **Prioritize Domain-Specific Benchmarks**: Move beyond generic metrics to evaluate models in real-world enterprise contexts.  
3. **Invest in Synthetic Data**: Use VLMs to generate labeled data for multimodal models, reducing reliance on manual annotation.  
4. **Optimize Infrastructure**: Focus on networking, throughput, and topologies to support large-scale AI training and inference.  

--- 

This summary highlights Snorkel AI’s approach to enterprise AI challenges and their strategic use of Azure’s infrastructure to address them.

## Full Transcript

[00:03] [Music]
[00:13] hey everyone thanks so much for coming
[00:15] I'm Hamza from an applied research
[00:16] scientist at snorkel on the uh computer
[00:19] vision team uh working on fine-tuning
[00:21] you know Foundation models for
[00:23] Enterprise use
[00:25] cases thanks amza um I like the ears uh
[00:30] thank
[00:31] you why don't you start out by telling
[00:34] the folks a little bit about uh snorkel
[00:36] and what you do there it's a it's an
[00:39] interesting name any relation to like AI
[00:41] for scuba diving or anything like that
[00:43] uh well hot tubs actually because
[00:45] snorkel doccom once I joined the company
[00:47] I learned as a hot tub company but no
[00:50] actually we don't do anything for scuba
[00:52] diving or hot tubbing um and to give a
[00:55] little bit of context the main problem
[00:57] that we're trying to solve is like you
[00:58] know data Dev vment for the Enterprise
[01:01] so uh what one key thing that I kind of
[01:04] want to take note of is the fact that
[01:06] you know out of the box llms rarely meet
[01:09] Enterprise quality latency and cost
[01:11] requirements you know to give some
[01:13] context our customers are like Fortune
[01:15] 500 companies like Banks insurance
[01:17] companies places like that and for them
[01:20] to deploy their models they really need
[01:21] them to be very reliable and very
[01:23] accurate and off the-shelf models like
[01:26] Claude or gp4 or or Gemini may get you
[01:29] part of the way there but they but they
[01:31] don't H have that you know final mile
[01:33] that really you know says yes we can
[01:35] like deploy these completely so what we
[01:38] focus on is developing data to fine-tune
[01:41] these models to get them
[01:43] there so hza this this makes sense but
[01:47] um why is it hard what what what's the
[01:49] challenge in addressing this
[01:51] issue yeah so uh data development is
[01:54] fundamentally challenging and there's a
[01:56] few key reasons for that one is that you
[01:59] know rag is just a starting point you
[02:01] know you guys may have heard of like you
[02:03] know using like rag to hook up like you
[02:05] know Enterprise knowledge databases to
[02:07] these models and get them to help give
[02:10] what you know these models were not
[02:12] pre-trained on and I don't want to rag
[02:14] on it it's great and all but it's just a
[02:16] starting point you know it won't get you
[02:18] all the way there and you know quality
[02:21] in your data is absolutely key um and
[02:24] finding and maintaining the right data
[02:26] is critical um because you know a lot of
[02:29] times you know
[02:30] the common instruction toting data sets
[02:32] may be very big but they don't contain
[02:34] exactly the information that you need
[02:36] like if you're training specifically on
[02:38] I don't know a specific type of Bank
[02:40] policy or a specific type of policy for
[02:43] certain industries you need that very
[02:45] key slice of information to be able to
[02:48] really um improve these
[02:52] models so I think folks have a good
[02:54] understanding of what you guys do and
[02:57] and why you do it why don't you talk a
[02:58] little bit about what
[03:00] snorkel is and what you're famous for
[03:02] besides the interesting
[03:04] name yeah so uh snorkel Pioneer data
[03:07] development uh for llms and we're
[03:09] trusted by you know many different
[03:11] companies we've worked with lots of
[03:13] companies in like you know the Fortune
[03:14] 500 and all that um we were spun up out
[03:17] of the Stanford AI lab quite a while ago
[03:19] and have a lot like you know decade of
[03:21] experience in like data development
[03:23] because it's keyed like you know many
[03:25] aspects of ML and we've published many
[03:27] papers and you know a lot of hot Fields
[03:29] like prompting Rag architectures and so
[03:32] on okay nice um I think we're going to
[03:36] switch uh context here for a bit and
[03:39] talk a little bit about the specific
[03:41] research projects you you guys are
[03:43] focused on um you guys take a research
[03:46] first culture why don't you explain a
[03:49] little bit about that and and the
[03:52] projects yeah thanks Loy so uh first I
[03:55] kind of want to talk a little bit about
[03:57] our research Focus overall uh so really
[04:00] what we the core question we try to
[04:02] answer is how can Enterprises best
[04:03] develop their data for custom AI models
[04:06] um you know so we have there are a few
[04:08] different directions we want to pursue
[04:09] overall one is keeping eses in the loop
[04:12] while maximizing the value of their time
[04:15] um you know because again like for a lot
[04:16] of these industries we need the subject
[04:18] matter experts that know the key details
[04:21] in order to be able to um you know
[04:24] provide feedback to models and help them
[04:25] be able to improve um the second is you
[04:29] know make data development programmatic
[04:31] scalable and auditable uh because you
[04:34] know while we do need smmes at the same
[04:36] time we also need to make things
[04:39] scalable in a way that solely manual
[04:41] intervention isn't so it's really being
[04:42] able to combine those two things
[04:45] together that make make this important
[04:47] and the third is continuous evaluation
[04:50] with domain specific Dynamic benchmarks
[04:53] um you know I'm sure you all have seen
[04:54] things like lmis or whatnot and it's
[04:57] pretty good to see you know a general
[04:59] understanding of where a lot of these
[05:01] llms fall in terms of their ability to
[05:03] do things but for specific Industries
[05:05] you need specific benchmarks to say how
[05:08] good is it at this like you know uh a
[05:10] bank isn't going to care about how how
[05:13] well these llms do at say grade school
[05:16] math right so there's that and I want to
[05:20] go into a little bit more detail and
[05:22] talk about some active research projects
[05:24] we're working on right now one is f
[05:26] grain evaluation and looking at you know
[05:29] where evaluation for these models is
[05:31] broken one particular area is you know
[05:34] in Long context models um you know you
[05:36] guys may have seen things like the
[05:38] needle and the Hast stack test where you
[05:39] take a bunch of like polyram essays and
[05:42] insert some sentence and see how well it
[05:44] can find that but you know we one thing
[05:47] we found is that again that that doesn't
[05:49] necessarily give a a proper sense of how
[05:51] these models handle long context in
[05:53] other domains and you know really again
[05:56] breaking everything down domain by
[05:57] domain is super critical so you know
[06:00] figuring out how can we improve long
[06:02] context
[06:03] overall um another key area is
[06:06] Enterprise alignment um you know making
[06:07] sure that these llms comply with you
[06:10] know company goals regulations and all
[06:12] that you know we don't want our llms to
[06:14] be committing any career limiting moves
[06:16] while outputting text um and another
[06:20] area which is particularly near and dear
[06:21] to me because I work on it actively is
[06:23] multimodal alignment um we find that you
[06:26] know these models trained on public data
[06:27] you know underperform and like you know
[06:30] specific domains and one area we're
[06:32] working on is using these large Vision
[06:34] language models or lvms to be able to
[06:36] generate synthetic data without manual
[06:38] annotation to be able to train you know
[06:41] Downstream models so kind of being able
[06:43] to really have this flywheel of going
[06:44] from like dat specific data generation
[06:46] in the loop to um model training is
[06:49] something that we're very excited
[06:52] about that's great uh hamzo we we we're
[06:56] excited that a lot of these projects are
[06:58] happening on azure's AI infrastructure
[07:02] obviously as well um I think if if you
[07:04] forward the slides a little bit um I
[07:08] think you know you went through an
[07:10] experience with Azure uh getting on
[07:13] board and running these projects I think
[07:15] people are really interested to maybe
[07:17] understand um what are the best
[07:19] practices you had working with our
[07:21] infrastructure some of the um uh
[07:25] pitfalls and and the benefits as well um
[07:28] you know uh the this one's my slide I uh
[07:31] I think the way we think about
[07:34] infrastructure that's supporting this
[07:35] wave of AI it's really about optimizing
[07:38] it in every sense possible for um for
[07:43] the different AI applications and use
[07:46] you know we look at everything from our
[07:48] Azure data centers we have over 300
[07:51] worldwide the CPU or the host so
[07:54] combining our virtual machines with the
[07:55] right uh CPUs um and offering the right
[07:59] throughput uh the
[08:02] accelerator um we use a diversity of of
[08:05] accelerators from AMD and viar and our
[08:08] own first-party silicon as well with the
[08:10] Maya uh with the mea chip we have
[08:13] topologies that you know optimize that
[08:15] iio between the different layers and
[08:17] obviously the the networking um
[08:20] throughput as well so it's really about
[08:23] making sure that we can take the best of
[08:25] breed at what we do at a supercomputing
[08:27] scale uh and deliver that back to the
[08:30] customers so we have a real cycle around
[08:33] um you know learning from working with
[08:36] organizations like openai mistol and
[08:39] others that have trained their models on
[08:40] azure's infrastructure and then being
[08:42] able to democratize that and deliver it
[08:44] back to to customers as well and so uh
[08:47] Hamza with that um why don't you share a
[08:50] little bit more about what exactly you
[08:52] guys did on on
[08:55] Azure uh yeah so so first we we'll
[08:58] actually talk a little bit about about
[08:59] how we do distributed training in
[09:01] general with Azure so we so we have a
[09:03] stack you know um and so on the ml
[09:06] framework side you know we use pytorch
[09:08] you know pretty standard framework um we
[09:11] also use a library called horovod which
[09:13] handles multi- node communication so if
[09:15] we have like multiple Azure vmms how do
[09:17] they communicate with each other um it
[09:19] allow it allows for faster communication
[09:21] across nodes and on the underlying you
[09:24] know Hardware layer you know we use a
[09:26] bunch of azure VMS they could be like A1
[09:28] 100s or h100 stands and they're all you
[09:32] know we connect to them we use horovod
[09:34] to connect to them and send gradients
[09:35] through for distributed training and
[09:37] they all read and write to a single
[09:38] Network file system or NFS you can
[09:41] basically think of an NFS as being a
[09:43] shared file system that every machine
[09:45] has access to as if it were a local file
[09:47] system which makes it very seamless to
[09:50] read data or write checkpoints for
[09:53] models um so that's kind of our overall
[09:57] um infr stack
[10:00] and what about running on on Azure um
[10:03] you guys had some specific workloads
[10:06] that that you were covering yeah um so
[10:09] we've run a number of projects on Azure
[10:11] um and we've run them on different sizes
[10:13] from like you know one node to dozens of
[10:15] nodes so you know we've run like DPO
[10:17] align models uh with a bunch of
[10:19] instruction response preference data
[10:21] sets um we've run like you know
[10:24] preference optimization techniques and
[10:27] and using and the things we''ve did that
[10:28] used the most most compute have been
[10:30] large scale distributed training jobs um
[10:32] for multimodal training and inference um
[10:34] you know with like dozens of gpus um so
[10:38] yeah these are the kinds of workloads
[10:40] that we've
[10:42] run fantastic um
[10:46] the I think um you had some lessons
[10:50] learned throughout as well it wasn't you
[10:53] know I think it's not always smooth
[10:55] sailing with these types of jobs so um
[10:57] any any best practice traps for young
[11:00] players out there in terms of uh your
[11:04] experience yeah absolutely um so there's
[11:07] a number of key architectural
[11:09] considerations to keep in mind one is
[11:12] having enough nodes to support you know
[11:14] your ideal batch size so on the CV side
[11:17] you know when I was training like you
[11:18] know let's say like clip based models
[11:20] one thing I learned is that you know you
[11:21] want we want enough nodes to have a
[11:24] certain batch size but we also didn't
[11:26] want too many such that we would either
[11:28] fall into the trap of having too large a
[11:30] batch size or underutilizing whichever
[11:33] nodes we were using so getting that
[11:35] balance right was pretty important
[11:37] another thing is networking bottlenecks
[11:39] we we want to make sure all of our data
[11:41] and nodes are close together like you
[11:42] know imagine if for example you had your
[11:45] um a bunch of your your data in Like Us
[11:48] West and maybe you had your nodes in
[11:50] like you know um Asia or something like
[11:52] that right you know that's like a simple
[11:54] example but bottom line is networking
[11:56] communication is pretty important and
[11:58] you want to make sure sure that you know
[12:00] when you're sending this data across
[12:01] that's not going to be a bottleneck when
[12:03] you cuz if you're training one thing
[12:05] that will happen is when you send
[12:07] gradients to different copies of the
[12:08] model that could be a bottleneck there
[12:11] another bottleneck could be data reading
[12:13] uh because recall that you know while
[12:15] your model is training and you're doing
[12:16] your forward and backward propagations
[12:19] um asynchronously you're loading in data
[12:21] to be fed to the model um and so this is
[12:25] where the NFS read speed is absolutely
[12:27] critical um if if your NFS is not
[12:30] reading in your data fast enough then
[12:31] you could be bottlenecked waiting for
[12:33] data to be processed and your model
[12:34] isn't actually
[12:35] crunching um and you know one key
[12:39] takeaway for both of these is make sure
[12:40] your GPU utilization is good and vsmi is
[12:43] your best friend here if you see your
[12:46] GPU utilization being low you know don't
[12:48] be afraid to look into why and you know
[12:50] you can you know do different things to
[12:52] debug like if it's multi- node for
[12:53] example then you know you can test
[12:56] networking and stuff like that if it's
[12:57] on a single node that likely means me
[12:59] it's a data loading issue so there's
[13:01] lots of different way ways and tools
[13:02] that you can use to step into these
[13:04] things and you know don't underestimate
[13:07] the basics of like reliability
[13:08] flexibility and manageability so you
[13:11] know one thing that we were we really
[13:13] cared about as a team is we wanted to
[13:14] make sure that our data distribut that
[13:17] you know when we were training
[13:18] experiments right we were like you know
[13:19] going through sometimes we needed all
[13:21] the nodes sometimes we needed very few
[13:24] and you know being able to work with
[13:25] instances that gave us that flexibility
[13:27] over a long period of time is very
[13:29] important you know when we were shopping
[13:31] around some Cloud providers only let us
[13:33] use compute for a fixed amount of time
[13:36] like maybe say a month or two months and
[13:37] you know as a trade-off we'd have a
[13:39] bunch of compute but that didn't really
[13:41] work for us because we weren't in it for
[13:43] a training a model for some fixed amount
[13:45] of time we wanted something where we
[13:47] could go on and off for a longer period
[13:49] of
[13:52] time that's that's great Insight Hamza I
[13:55] think um also we we talked about some of
[13:58] the advantages is of using Azure which
[14:01] um would be great if you could
[14:02] shamelessly plug that for Azure as well
[14:05] yeah happy to so you know one was
[14:07] availability you know the Azure VMS were
[14:09] were dedicated and allowed us to adjust
[14:11] our capacity on demand um the
[14:14] reliability was pretty good it was
[14:15] consistently Dependable with like no
[14:17] real issues you know NFS throughput was
[14:21] also quite good you know um again right
[14:23] like you know if your NFS is bad then
[14:25] that means that you know you're not
[14:26] reading in data fast enough or for
[14:28] example being able to dynamically change
[14:31] the size of your NFS if let's say for
[14:33] example you need more less capacity if
[14:35] you if you need more because you
[14:36] suddenly have more data than you
[14:37] realized you had before then you need to
[14:39] be able to tell it that at the same time
[14:41] if you realize that you know your your
[14:43] NFS is over provisioned you don't want
[14:45] to be you know overpaying an Azure bills
[14:47] um though I'm sure locky wouldn't mind
[14:49] that but uh and you know the ease of use
[14:53] is very important you know clear
[14:54] documentation and straightforward
[14:56] process you know like as the guy that
[14:57] set up aure for my team team I really
[14:59] didn't like it if other people needed to
[15:01] bug me and thankfully once I got things
[15:03] working it just worked and I did not
[15:06] need to be paid so that is very
[15:09] important that's really great to hear
[15:11] hza um yeah I I think like you know uh
[15:16] this is fantastic and and I think you
[15:17] had some specific data points uh you
[15:21] guys recently went through a process to
[15:24] go from the A1 100s through to the h100s
[15:27] or the VMS l in those um can share a bit
[15:31] of ins around what you observed with
[15:33] that
[15:33] experience yeah um so the key takeaway
[15:36] is that h100s are really good um one
[15:39] thing we wanted to do when we were doing
[15:41] this was do a cost analysis and see okay
[15:43] for a given number of h100s and a given
[15:46] number of A1 100s that cost the same
[15:47] amount what kind of training and
[15:49] inference are we getting and so here you
[15:51] can see we're comparing two h100s to 4
[15:53] A1 100s because that's what works out
[15:55] about the same cost wise and we're doing
[15:57] better on both training and inference um
[16:00] which means that we're doing better per
[16:01] dollar just by switching here and you
[16:05] know one there are a couple key points I
[16:07] really want to emphasize here one is
[16:10] that um you know it's really nice when
[16:12] you just have a very simple plug-and
[16:14] playay change that works you know
[16:15] there's a lot of ongoing work to
[16:17] optimize you know you know especially
[16:19] like things like inference for example
[16:20] with your KV caches your partial KV
[16:22] caches your speculative decodings and
[16:25] it's really nice to be able to say hey
[16:26] let's just do something simple and have
[16:28] it work work and the second is that with
[16:31] this faster inference in particular we
[16:32] can we can go through more synthetic
[16:34] data higher end model accuracy and it
[16:36] just enables us a flywheel of faster
[16:38] iteration which is super critical for
[16:40] being able to like do more
[16:43] development yeah I I mean you can see
[16:45] from the numbers the the performance is
[16:47] there and it's I'm I'm I'm assuming that
[16:50] internally just that ability to do more
[16:52] with fewer gpus has been a really um
[16:56] great benefit for you guys across all
[16:58] the work you
[17:00] doing um oh
[17:12] sorry um sry your question is why the uh
[17:15] training time while the inference is
[17:17] taking longer than the training
[17:18] time um I think it was because we were
[17:21] doing a larger batch size and it just
[17:23] happened to work out that way that for
[17:26] whatever batch size we were doing it
[17:28] just wound up taking longer cuz you with
[17:30] with training you typically need a
[17:31] smaller bat size cuz you have to to put
[17:34] more things in memory for back propop
[17:36] and somehow it just wound up working
[17:38] that
[17:39] way
[17:54] so
[17:56] um no cuz I know that when we were
[17:58] comparing training inference across the
[18:00] hardware th those were kept fixed like
[18:02] whatever inference batch size we were
[18:03] using for dh100 was the same as the
[18:07] a00 um so that that wasn't a that wasn't
[18:10] a
[18:13] factor
[18:17] yeah yeah so uh speaking about um what's
[18:21] next I think this is a good segue so uh
[18:24] with the next
[18:25] slide um just from our point of view
[18:28] with with Azure we are sort of adopting
[18:31] and we spoke about um optimizing at
[18:35] every layer of the stack and I think the
[18:37] addition of our Maya uh AI accelerator
[18:40] that's used for our own internal
[18:41] workloads across Microsoft
[18:44] 365 uh but we we've just announced the
[18:47] AMD Mi 300X with uh the high bandwidth
[18:50] memory we've got the Nvidia A1 100s the
[18:53] h100s and we'll be adopting Blackwell
[18:56] what's really exciting is
[18:59] the pace of innovation in in Silicon has
[19:02] never been like this before we're
[19:04] talking with Nvidia almost doing two
[19:06] releases a year previously you know I I
[19:10] I think it might have been one every two
[19:12] years or something like that uh it's
[19:15] really amazing to see this growth in the
[19:17] in the Silicon how far we're getting and
[19:20] what Hamza just shared the ability to
[19:22] more and more with less uh on the
[19:25] infrastructure as well and so um I think
[19:29] you know certainly as far as Azure and
[19:31] our AI infrastructure strategy it's to
[19:33] continue to adopt these new evolutions
[19:36] and really make sure the right gpus are
[19:39] used in the right places for the right
[19:42] workloads hza what about for snorkel AI
[19:45] what's next yeah so to give you all a
[19:47] sneak peek into what we're working on
[19:49] actively at snorkel what we have a
[19:51] number of directions you know one is to
[19:53] you know say like you know better data
[19:55] leads to better gen and get better
[19:57] prototypes to production so so we want
[19:59] to explore new ways to programmatically
[20:01] utilize preference signals for data
[20:02] synthesis and curation we also want to
[20:05] develop scalable entry points for data
[20:07] development using rationals and custom
[20:09] taxonomies um and finally we want you
[20:12] know better multimodal retrieval
[20:14] algorithms um and we want to evaluate
[20:17] those on domain specific data sets to
[20:18] scale up the retrieval models we have so
[20:21] and we're of course excited to do all
[20:23] these things on Azure AI
[20:26] infra fantastic com well thank you so
[20:29] much for for presenting and and speaking
[20:32] on behalf of uh Microsoft we we really
[20:35] appreciate it thank you guys so much
[20:39] [Music]
