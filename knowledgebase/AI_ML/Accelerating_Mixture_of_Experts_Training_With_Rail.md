---
type: youtube
title: Accelerating Mixture of Experts Training With Rail Optimized InfiniBand Networking in Crusoe Cloud
author: AI Engineer
video_id: tQTB4MU_z8w
video_url: https://www.youtube.com/watch?v=tQTB4MU_z8w
thumbnail_url: https://img.youtube.com/vi/tQTB4MU_z8w/mqdefault.jpg
date_added: 2025-05-26
category: Cloud Computing and AI Infrastructure
tags: ['cloud computing', 'AI infrastructure', 'GPU clusters', 'network optimization', 'VPC', 'APIs', 'CLI', 'GUI', 'ML training', 'cloud storage', 'distributed systems', 'cloud networking']
entities: ['Cruiso Cloud', 'InfiniBand', 'VPC networking', 'NVMe', 'Together AI', 'Bosan Ai', 'CLI', 'APIs', 'GUI', 'ML training']
concepts: ['AI development', 'machine learning', 'cloud infrastructure', 'GPU communication', 'network optimization', 'cloud computing', 'distributed computing', 'API automation', 'VPC networking', 'cloud storage']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of cloud computing', 'familiarity with AI/ML workflows', 'knowledge of networking fundamentals']
related_topics: ['Cloud computing', 'AI/ML infrastructure', 'GPU clusters', 'network optimization', 'cloud storage solutions', 'API automation', 'VPC networking', 'distributed computing']
authority_signals: ['we do partner with a bunch of them already', 'we have the together AI here', 'we do have a lot of customers already']
confidence_score: 0.8
---

# Accelerating Mixture of Experts Training With Rail Optimized InfiniBand Networking in Crusoe Cloud

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=tQTB4MU_z8w)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai cloud, gpu networking, mixture of experts, infiniband, network optimization, sustainable computing, ai infrastructure  

## Summary

# Summary of "Accelerating Mixture of Experts Training With Rail Optimized InfiniBand Networking in Crusoe Cloud"

## Overview  
This video highlights **Crusoe Cloud's** infrastructure innovations, focusing on **Rail Optimized InfiniBand networking** to accelerate **Mixture of Experts (MoE)** training. The speaker, Yinko, emphasizes Crusoe's mission to align computing with climate goals through renewable energy, high-performance networking, and user-friendly tools for AI developers. Key themes include network optimization, sustainability, and scalable GPU/CPU resources.

---

## Key Points  
- **Three Pillars of Crusoe Cloud**:  
  1. **High Performance**: Optimized networking (InfiniBand) for low-latency, high-bandwidth GPU communication.  
  2. **Ease of Use**: CLI, APIs, and GUI for seamless infrastructure management.  
  3. **Climate Alignment**: Use of renewable energy (e.g., geothermal in Iceland) and sustainable data center strategies.  

- **Networking Architecture**:  
  - **Front-End Network**: Traditional VPC for customer traffic.  
  - **Back-End Network**: Dedicated, high-performance InfiniBand cluster for GPU-to-GPU communication.  
  - **Rail Optimized InfiniBand**: Tailored for MoE training, improving scalability and efficiency.  

- **Infrastructure Offerings**:  
  - GPU and CPU instances for training, inference, and data preprocessing.  
  - Persistent storage solutions (NVMe, NFS) and managed file systems.  
  - Partnerships with AI companies (e.g., Together AI, Bosan AI) for ML training and inference.  

- **Data Center Strategy**:  
  - Strategically located facilities (e.g., Iceland) to leverage renewable energy.  
  - Focus on reducing environmental impact while maintaining performance.  

---

## Key Quotes/Insights  
- *"Network optimization is critical for MoE training, as it enables efficient GPU communication and scalability."*  
- *"Our climate mission is core to Crusoe Cloud—using renewable energy and sustainable practices to power AI."*  
- *"We aim to let AI developers focus on innovation, not infrastructure."*  

---

## Actionable Items  
1. **Explore Rail Optimized InfiniBand**: Leverage this networking solution for MoE training to reduce latency and improve performance.  
2. **Adopt Renewable Energy Infrastructure**: Consider Crusoe Cloud for climate-conscious AI workloads.  
3. **Utilize Managed Services**: Take advantage of CLI, APIs, and GUI for streamlined infrastructure management.  
4. **Engage with Partners**: Collaborate with Crusoe's ecosystem (e.g., Together AI) for tailored ML solutions.  

--- 

This summary captures the technical and strategic focus of Crusoe Cloud's approach to AI infrastructure, emphasizing performance, sustainability, and developer experience.

## Full Transcript

[00:00] [Music]
[00:13] thank you for coming over to our session
[00:15] today a lots of really interesting stuff
[00:18] is happening on the AI World these days
[00:21] right uh with all the recent model
[00:23] developments and the GPU developments it
[00:26] is really cool to see all the use cases
[00:29] um
[00:30] however here I want to talk now a little
[00:33] bit about the infrastructure and the way
[00:35] how we can support the the newest models
[00:38] of the gpus and the
[00:40] newest um the newest models the machine
[00:43] learning models and how we can help that
[00:46] everything is working smoothly and fast
[00:49] and and productive so my name is yinko
[00:52] I'm a product manager at
[00:54] cruso uh my main responsibility is is
[00:58] the infrastructure
[01:00] and specifically GPU networking
[01:02] infrastructure and we are always looking
[01:05] for a way how we can increase the
[01:07] performance of that Network because as
[01:09] we will see later in the presentation it
[01:11] is really important to do that now a
[01:15] little bit about the cruo cruo is an AI
[01:18] Cloud platform which has one I think
[01:21] very important mission for all of us
[01:23] it's to align the future of computing
[01:25] with the future of climate there is a
[01:28] really strong Demand right now for the
[01:30] computing power the gpus are really
[01:32] energy hungry there is a lot of
[01:34] Investments being done in the data
[01:36] center area and of course that puts an
[01:38] additional pressure on the grid and on
[01:40] the energy sources what we are trying to
[01:43] do here at cruo we are trying to utilize
[01:46] this trended energy sources wasted
[01:48] energy sources and Renewables to power
[01:51] our data centers we want really to be
[01:54] able to make sure that every time when
[01:56] you train your model every time when
[01:58] you're using GPU for inference you're
[02:01] not causing any negative impact on the
[02:05] climate now uh whenever we are building
[02:08] the cloud right the AI Cloud we are
[02:11] building it based on three important
[02:14] pillars first of all there is a high
[02:16] performance pillar uh as the customers
[02:19] are buying our services and procuring
[02:22] you know the GPU times and training
[02:24] their models we have to ensure that all
[02:26] the infrastructure is optimized for this
[02:28] training every time when it's not
[02:30] optimized every time when there is a
[02:32] delay or a glitch or any sort of outage
[02:35] or simply not that great performance it
[02:39] causes the direct impact on the
[02:41] customer's bottom line it causes a
[02:43] direct impact on the time to train and
[02:46] kind of raises the cost to train the
[02:48] model now the second one which I think
[02:51] is very important for everybody around
[02:53] here is the easy to use uh we want
[02:56] really to separate ourselves from the
[02:58] general purpose clouds
[03:00] uh we do know all of them the
[03:02] hyperscalers are building the great
[03:04] infrastructure and are trying to support
[03:07] each and every use case the customers
[03:09] might have for the cloud computing
[03:11] however in our case we really want to
[03:13] focus on the experience of the AI
[03:15] Engineers so we want to make sure that
[03:17] we are providing a simpler user
[03:20] interface that allows developers to spin
[03:23] up the compute resources to deploy the
[03:25] models to train them to use them to in
[03:28] for inference and and so on uh all the
[03:32] underlying complexity of the
[03:34] infrastructure is being hidden by us and
[03:38] I believe that's our job to make sure
[03:40] that that is that stays the case and now
[03:43] as I mentioned we as I mentioned before
[03:45] we are climate aligned which means uh we
[03:48] as a company really aiming to power 100%
[03:51] of our data centers with the renewable
[03:55] wasted energy sources with some some
[03:59] some form of stranded energy sources to
[04:01] ensure that we are uh we are being Net
[04:05] Zero emission net new zero emissions
[04:08] from the carbon perspective we have a
[04:11] big story around that feel free to check
[04:13] it on our website or come over to our
[04:15] booth on the on the show floor and the
[04:18] team will happy to talk about that now
[04:22] where are we present right now we have a
[04:24] number of the data centers located
[04:26] across the US uh as you see three of
[04:30] them in the continental United States
[04:33] and they are generally located close to
[04:36] the energy sources I was mentioning
[04:38] before so we have the one in Texas we
[04:41] have uh the one in the northern central
[04:43] part of the country and on the East we
[04:46] are also building right now one big data
[04:49] center in Iceland that will be powered
[04:52] by the geothermal energy I mean again a
[04:55] amazing way to use the constrained
[04:58] energy sources or the Renewables to
[05:01] power the data center we are trying to
[05:03] follow that model hence we are placing
[05:05] our data center strategically the
[05:08] placement of the data center in Iceland
[05:10] though will be also very important for
[05:12] our imir customers given the latency and
[05:15] the and the general connectivity to the
[05:18] Europe that is something I think uh
[05:21] might be helpful for them as
[05:24] well
[05:26] now what is our platform right I say
[05:29] Cruis Cloud but generally whenever we
[05:31] are talking about any Cloud we are
[05:33] talking about three General types of the
[05:35] products first and foremost we have the
[05:38] compute we are offering the VMS with uh
[05:41] with gpus attached to them so every time
[05:44] when customer wants to spin up when
[05:47] customer wants to get access to the gpus
[05:49] they're able to get it through the VM
[05:51] they can get a bunch of DM connected
[05:54] together and use them as a one single
[05:58] training cluster we also offer CPU
[06:00] instances for any potential data
[06:02] pre-processing or any general purpose
[06:06] compute tasks you might have for the
[06:07] data preparation for the
[06:09] offload whatever you have uh from the
[06:13] storage perspective we are offering FML
[06:16] and persistent discs on the Node so
[06:18] those are delivered from the nvme on the
[06:21] local server where your VMS are being
[06:23] placed we also have the persistent blog
[06:27] storage solution available for our
[06:29] customer customers and we are working on
[06:31] providing and delivering the managed
[06:34] file system the network file systems for
[06:36] the customers on the networking side of
[06:39] course more traditional more typical VPC
[06:42] networking that's the network sometimes
[06:45] we call it front-end Network that is
[06:46] used to deliver the customer traffic
[06:49] from the Internet or from the customer
[06:52] environment wherever the customer might
[06:54] have the data sources to deliver that
[06:56] towards the VM so that's your kind of
[06:59] Main
[07:00] connectivity uh path to the outside
[07:03] world now uh we do offer a number of the
[07:06] additional services on that that's not
[07:08] simply connectivity we also have the
[07:10] firewalls we will be offering the lot
[07:12] balancers soon but generally we're
[07:14] trying to follow more traditional paths
[07:17] for the VPC networking and and the
[07:20] requirements the customers usually have
[07:22] there now what is more interesting and
[07:24] what we will be talking a little bit
[07:26] later today in Greater details is our
[07:29] rail optimized infin band cluster
[07:31] networking so for those of you who don't
[07:34] know typically C typically providers the
[07:37] GPU providers are separating their
[07:39] Network they have the front end Network
[07:41] which is used for general purpose
[07:43] traffic but then all the communication
[07:45] between the gpus is happening on the
[07:48] Standalone separate Network that is uh
[07:51] really high performance low latency and
[07:54] how bandwidth and the whole topology is
[07:56] optimized for the GPU to GPU
[07:58] communication
[08:00] uh now last but not least the user
[08:02] experience as I mentioned before we are
[08:05] our main customers our main Persona the
[08:08] people who are using crew cruiso Cloud
[08:11] are the AI developers and machine
[08:13] learning Engineers so we want to make
[08:15] sure they have what they need in order
[08:18] you know to be successful and not to
[08:21] think too much about infrastructure we
[08:23] off offer CLI we have apis we have GUI
[08:26] so everything can be automated
[08:28] everything can be can be consumed and
[08:30] configured in the way you like it
[08:35] more uh we do have a lot of customers
[08:38] already and it was very fun for me to
[08:40] see on the floor that some of them are
[08:43] there and some of them are talking about
[08:45] their Solutions probably this is the
[08:47] first time in my life whenever I'm
[08:51] attending a conference and standing at
[08:53] the booth I don't have to compete with
[08:55] all the people around us so we do see
[08:58] all the companies that are presenting
[09:00] their Solutions right now as our part
[09:02] Partners we do partner with a bunch of
[09:05] them already we have the together AI
[09:07] here we have the uh bosan Ai and all of
[09:11] them are using our infrastructure for
[09:13] different purposes so together AI for
[09:15] example they're really into using
[09:18] Cruiser infrastructure for the ml
[09:20] training for the fine-tuning their
[09:22] models and some sometimes for inference
[09:25] the C is uh their tra they're using our
[09:30] compute infrastructure to train the new
[09:32] foundational models this is really great
[09:35] I mean if you are the customer of
[09:37] together for example or codium or what
[09:40] not it is likely that you have been
[09:43] somehow exposed to the Cruis
[09:45] infrastructure
[09:47] now the distributor training has a very
[09:51] specific set of problems or issues right
[09:56] there is a compute part of it when the
[09:58] computation is being done on the gpus
[10:00] but since we are talking about a
[10:02] distributed training which means there
[10:04] are a lot of gpus at certain stages
[10:07] Whenever there is a uh Whenever there is
[10:09] a uh training step being completed all
[10:12] the gpus have to exchange the
[10:14] information have to exchange the data
[10:17] that they calculated on their own this
[10:19] is typically done through the all reduse
[10:21] or or all all all get uh um through the
[10:26] all reduce process and the protocols and
[10:29] and it contains a forward path the
[10:32] backward path but then the networking
[10:34] part takes without any optimization
[10:37] about 25 30% of the network of the time
[10:41] of the training time
[10:43] now this is the time where when your
[10:46] gpus are staying idle they're not being
[10:49] able to compute anything because they
[10:51] have to wait for all the information to
[10:53] be gathered uh together this is kind of
[10:57] a bad thing for everybody right this is
[10:59] bad thing for the customers because they
[11:01] still pay for that infrastructure they
[11:03] still have to wait it delays the the mod
[11:06] model training but it also bad for us
[11:09] because we have the infrastructure that
[11:10] is not being performant enough there are
[11:13] a couple of Tricks we can do first of
[11:15] all the computation and communication
[11:17] overlap allows you to start the network
[11:20] exchange or the data data exchange when
[11:23] the computation is still ongoing but
[11:26] even with that when we were working with
[11:28] the customer
[11:29] we saw just the
[11:32] reduction uh of about 10% so about 25%
[11:36] of the training time was still spent on
[11:39] the network me as a product manager and
[11:41] the infrastructure side are constantly
[11:43] being asked like how can we reduce that
[11:46] how can we use the network as much as
[11:49] possible and reduce that Gap so we we
[11:52] have been looking into that and we were
[11:54] trying to figure out what would be the
[11:56] right cluster networking to ology how
[12:00] can we make sure that our data fabric
[12:02] that is used for connecting the gpus is
[12:05] being fully optimized and is being uh is
[12:08] able to provide the bandwidth needed and
[12:11] the latency needed the standard fed tree
[12:14] those of you who have been working in
[12:15] the data centry infrastructure before
[12:18] that is something that we were
[12:19] traditionally doing for years that's a
[12:22] great way to build a scalable maybe
[12:25] non-blocking fabric right but there are
[12:27] a bunch of issues with that first of all
[12:31] if we will be connecting our servers
[12:33] that are shown below to a single leaf
[12:36] that introduces the single choke point
[12:38] as well as the single fold domain right
[12:41] if we are losing the leaf we are losing
[12:43] all the gpus that are connected to that
[12:46] LE now what else we were thinking about
[12:50] is like look we have that
[12:53] switch we we have that switch sorry what
[12:56] is it the time yes okay so we have that
[13:00] switch that can be used for the backend
[13:02] traffic propagation and why don't we use
[13:06] that switch for from the bandwidth
[13:07] perspective and kind of you know have an
[13:10] additional
[13:11] path let me just use the simple two node
[13:14] uh example to explain the topology and
[13:17] to explain how we are using it so first
[13:19] of all whenever we have the gpus that
[13:21] want to communicate within one server
[13:24] they can use their embedded NV link NV
[13:27] switch and that provides a good good
[13:29] communication they don't have to go to
[13:31] the outside fabric anywhere and and
[13:33] whatnot now whenever we have the data
[13:38] communication between the gpus on the
[13:40] different nodes if they collect if they
[13:42] are connected to the Single leave that's
[13:44] something we called one single rail that
[13:47] means that the traffic communication
[13:48] will be passing through the uh through
[13:51] the one single lead just one H away and
[13:54] you will get the to the destination now
[13:57] what is interesting here is when we want
[13:59] to talk to the different Trails right we
[14:01] have to go all the way to the spine and
[14:04] that introduces the additional H besides
[14:07] the bandwidth saturation problems that
[14:10] may lead to the additional latency which
[14:12] will be really important for all for
[14:14] your uh all
[14:16] reduce all reduce
[14:19] operations but luckily for us Nvidia
[14:22] with the recent version of nickel
[14:24] introduced the feature called pxn which
[14:27] allows you to use the internal EnV
[14:30] switch inside the host to communicate
[14:33] across the rail so whenever we want to
[14:35] have the GPU Zer to communicate with the
[14:38] GPU a on the another host we can use an
[14:42] an internal switch to do the traffic Hub
[14:44] between the gpus and then send it to the
[14:46] leap where it is connected to so it
[14:48] still allow us to use one single hop and
[14:52] have access across the different rails
[14:56] of the gpus now with did some nickel
[14:59] test results uh and we saw quite a
[15:03] significant Improvement 50% for the
[15:05] small messages and 50% of the large
[15:08] messages now those numbers here are of
[15:10] course for the smaller uh for the
[15:13] smaller messages are about latency for
[15:15] larger ones we care more about bandwidth
[15:17] because latency tends to stand to stay
[15:20] roughly the same uh those numbers are
[15:23] great right everyone everybody would
[15:25] love them but not the customers and it
[15:27] does make sense because those numbers
[15:29] are synthetic and more are showing you
[15:31] the workload that is applied to your
[15:34] network what customers care about is the
[15:37] time to train the particular model so we
[15:40] use the sparse mixture of expert as an
[15:43] example and uh I mean I'm not going to
[15:47] dive into the details how how it works
[15:49] but essentially the sparse Network the
[15:52] the sparse mixture of experts shows you
[15:55] gives you a different layers of the
[15:57] experts and throws the TR trffic between
[15:59] them whenever you deploying that on the
[16:02] really large GPU cluster that makes uh
[16:07] that creates a ton of traffic like all
[16:09] the gpus have to send the traffic to
[16:11] each other they have to extend the
[16:13] information the workload on the network
[16:15] is pretty significant
[16:18] so we use the mixl model the open source
[16:22] uh sparse mixture of experts uh which is
[16:26] contained of eight feet forward blocks
[16:28] eight seven billions of parameters and
[16:30] we use the fine tuning to use this model
[16:33] to fine tune it on 240 h100 gpus and we
[16:38] did a quite significant we saw a quite
[16:40] significant Improvement when we had the
[16:42] pxn enabled and without it the 14% of
[16:46] improvement is something that can be
[16:49] directly connected to the time to train
[16:51] the model that can be directly connected
[16:54] to cost of training the model and that
[16:56] is something that everybody really uh
[16:59] really got excited I definitely got
[17:01] excited and and our customers as well
[17:03] because that shows them some real value
[17:06] numbers they can get with a model now
[17:08] that was it from my side sorry for uh
[17:11] going through that it's so fast it's a
[17:14] very you know large topic it's it's hard
[17:16] to talk about that but I'm happy to
[17:18] answer all the additional questions
[17:21] anything you guys might
[17:26] have thank you
[17:29] [Music]
