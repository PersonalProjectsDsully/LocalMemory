---
type: youtube
title: Accelerate your AI journey with Azure AI model catalog: Sharmila Chokalingam
author: Channel Video
video_id: gL9kfxt6uo0
video_url: https://www.youtube.com/watch?v=gL9kfxt6uo0
thumbnail_url: https://img.youtube.com/vi/gL9kfxt6uo0/mqdefault.jpg
date_added: 2025-05-26
category: Cloud Computing and AI
tags: ['Azure AI', 'Model Deployment', 'API Integration', 'Cloud Services', 'AI Tools', 'Content Filtering', 'Machine Learning', 'SDKs', 'Model Benchmarks', 'Cloud Infrastructure']
entities: ['Microsoft', 'Azure AI Studio', 'Coher Command R', 'MRL', 'Azure Marketplace', 'Content Filter', 'LangChain SDK', 'LightLLM SDK']
concepts: ['Model Deployment', 'Model Benchmarks', 'API Standardization', 'Content Filtering', 'Deployment Process', 'Model Customization', 'Playground Capabilities', 'Token Usage Pricing']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of cloud computing (Azure)', 'Familiarity with AI model deployment concepts', 'Microsoft Azure subscription']
related_topics: ['Machine learning deployment', 'Cloud infrastructure management', 'AI model optimization', 'API development', 'Content moderation systems', 'SDK integration', 'Model evaluation metrics']
authority_signals: ['we try to standardize the APIs across all use cases', "it's as simple as choosing a deployment name", 'we have the ability to check model benchmarks']
confidence_score: 0.8
---

# Accelerate your AI journey with Azure AI model catalog: Sharmila Chokalingam

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=gL9kfxt6uo0)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: azure-ai, ai-models, generative-ai, enterprise-ai, model-catalog, ai-platform, machine-learning  

## Summary

# Summary of "Accelerate Your AI Journey with Azure AI Model Catalog"

## Overview  
This video demonstrates how Microsoft Azure's AI Model Catalog streamlines AI development by offering a unified platform for selecting, deploying, and testing pre-trained models. It emphasizes the importance of model choice, standardized APIs, and enterprise-grade features like security and scalability to accelerate AI project development.

---

## Key Points  
1. **Stages of Building Generative AI Apps**  
   - **Prototyping**: Filter models by use case, deployment type, or task (e.g., text generation, classification).  
   - **Optimizing**: Use Azure AI Studio to benchmark models on metrics like accuracy, coherence, and groundedness.  
   - **Operationalizing**: Deploy models via Azure Marketplace with minimal code changes, enabling seamless integration into existing workflows.  

2. **Model Diversity**  
   - Over 1,600+ models available, including GPT-4, Mistal, Llama, Cohere, and custom models.  
   - Specialized models for tasks like code generation (e.g., Cohere Command R) or multilingual support (e.g., mRAL).  

3. **Azure AI Inference API**  
   - Standardizes APIs across models, allowing developers to plug into third-party tools (e.g., LangChain, LLM SDKs) without code rewrites.  

4. **Enterprise Features**  
   - **Security**: Content filters, compliance, and Azure Marketplace integration for secure deployments.  
   - **Scalability**: Model benchmarks and playgrounds for testing before production.  

5. **Customer Success & Demo**  
   - Live demo shows deploying a model (e.g., Cohere Command R) in under a minute, with a playground for testing.  
   - Highlights use cases like cultural initiatives (e.g., "How does Microsoft promote the culture of giving?").  

---

## Key Quotes/Insights  
- *"The three questions when building AI apps: What’s the use case? What’s the model’s performance? How does it fit into my workflow?"*  
- *"The model catalog allows swapping models without disrupting code, ensuring flexibility."*  
- *"GPT-4’s function calling is ideal for agent-centric workflows, while mRAL excels in multilingual tasks."*  

---

## Actionable Recommendations  
- **Filter Models**: Use Azure AI Studio’s filters (e.g., deployment type, task) to find the right model.  
- **Leverage Benchmarks**: Compare models on metrics like accuracy and coherence to make data-driven choices.  
- **Test in Playground**: Use the AI Studio’s chat playground to experiment with deployed models.  
- **Secure Deployments**: Enable content filters and deploy via Azure Marketplace for compliance.  

--- 

This summary captures the core value of Azure’s AI Model Catalog for developers and enterprises aiming to accelerate AI innovation.

## Full Transcript

[00:00] [Music]
[00:13] hi everyone thank you for joining us for
[00:14] the session on how you can accelerate
[00:16] your AI Journey with the aurei model
[00:19] catalog this is shuie I'm one of the
[00:21] product managers on
[00:22] aurei and I'm sharmi I'm one of the
[00:25] product marketing managers on Azure
[00:28] AI great so let's get started so today
[00:32] we'll be talking about how we offer the
[00:33] best collection of foundation models on
[00:35] Azure why the model Choice matters so
[00:38] much when you have such a huge
[00:39] collection of models and how does the
[00:41] Azure AI model inference API make it
[00:43] standard and easy for you to switch
[00:45] between multiple models swpe one out for
[00:47] another without disturbing your rest of
[00:49] the code base and then how you can build
[00:51] generative AI apps on top of it and how
[00:55] the platform makes sure that all your
[00:56] Enterprise redness needs like data
[00:58] privacy security and content filtering
[01:00] are met and then let we'll talk a bit
[01:02] about some of the customer success
[01:04] stories so Shi as you mentioned uh there
[01:08] are a lot of large language models that
[01:09] are being U released pretty much every
[01:12] day every week and uh I know in the
[01:14] Azure AI studio and model catalog we are
[01:17] bringing a lot of models like large
[01:19] language models foundational models I
[01:22] want to understand why are we bringing
[01:24] all all these models and why does it
[01:26] matter to a
[01:28] customer yeah absolutely that's a very
[01:31] valid question so let's talk about why
[01:33] model Choice matters in the real world
[01:35] right as cha asked so the three
[01:37] questions that we all try to answer when
[01:39] we try to buid generative AI apps is can
[01:42] AI solve my use case first and then what
[01:45] is the best model for my use case and
[01:47] then how do I go about scaling this for
[01:48] the production workloads so the first
[01:51] step is called prototyping where you try
[01:53] try out multiple models that are
[01:54] available to you you try to establish
[01:56] feasibility build that prototype do
[01:59] compare model benchmarks and find the
[02:01] right one for your use case or maybe at
[02:03] least short list some of them and that's
[02:05] when you move to the next stage where
[02:06] you try to optimize it for your use case
[02:08] where you try to optimize for cost
[02:10] latency Regional nuances Etc and that's
[02:13] where the Azure AI platform comes into
[02:15] picture where you can use the techniques
[02:17] like prompt engineering Rag and
[02:18] fine-tuning to make sure that you've
[02:20] optimized it once you're done through
[02:22] this Loop of prototyping with the model
[02:23] catalog and optimizing with the platform
[02:25] you can go ahead and operationalize it
[02:27] so you don't have to worry much about
[02:29] the capacity and cost tradeoffs you have
[02:31] to you have you've got monitoring you've
[02:33] got scalability you've got data privacy
[02:35] content filtering and all your
[02:38] Enterprise needs are met so once you
[02:40] through this you have your generative AI
[02:42] application production so another
[02:45] question I had here is U have you seen
[02:48] situations where a customer is using
[02:50] more than one model for a specific use
[02:52] case and even for multiple use cases
[02:54] yeah absolutely like that's the whole
[02:56] point of the model catalog that you have
[02:58] this wide range of models you have your
[03:00] use case and you're able to plug in any
[03:03] model in from that model catalog so you
[03:06] can swap out one for another without
[03:07] disturbing anything with quick
[03:09] prototyping and quick
[03:13] comparison so as we mentioned let's talk
[03:16] a bit about the model selections that we
[03:17] offer on our platform so we offer a wide
[03:19] range of Flagship llms and slms recently
[03:22] we launched the Aur OPI models GPD 4 is
[03:25] already on the platform we launched
[03:27] mistal models llama models coher models
[03:30] as well as small language models like 53
[03:32] and the mral OSS models along with that
[03:35] we make sure that your multimodel
[03:37] requirements image generation
[03:38] requirements and specific needs such as
[03:40] embedding model requirements are also
[03:42] fulfilled on this platform so GPD 40 for
[03:45] example has function calling and Json
[03:47] support so you can make sure you use
[03:48] that for your agent Centric workflows
[03:50] along with that we also make sure that
[03:52] we cater to your region or language
[03:54] specific needs so for example the mral
[03:56] language is really good with the
[03:57] European languages or uh the coer
[04:00] embedding multilingual model is very
[04:02] good for your multilingual requirements
[04:04] and we also recently launched js on a
[04:06] platform which is an Arabic
[04:08] llm along with all these Flagship and
[04:11] premium models we also have hundreds of
[04:13] open models from hunging face and we've
[04:15] been actively partnering with meta data
[04:17] brick Snowflake and Nvidia to make sure
[04:19] that we get their models on our platform
[04:21] as soon as
[04:24] possible okay so now that we have uh
[04:29] seen what all we can do with the catalog
[04:31] let's try to see a live example of how
[04:33] to actually go to the catalog and deploy
[04:36] your models so once you type into your
[04:38] url ai. azure.com it's as easy you land
[04:41] on this AI Studio page where you can go
[04:44] to the model catalog on this left nav
[04:45] bar and you land on this page that has
[04:48] the list of all the models that we offer
[04:50] it has 1,600 plus models right here and
[04:53] to make it easy for you to filter it for
[04:55] a use case you can filter by the
[04:57] different deployment types different
[04:58] inference tasks that you want to do or
[05:01] even if just by the model collection
[05:02] families so let's start out by filtering
[05:05] for the coher models like click on cair
[05:08] right here let's try to see coher
[05:10] command R for example once you click on
[05:12] the model you land on this model card
[05:14] page where you have all the information
[05:15] about the model how uh you can customize
[05:18] it for your own use case tool use
[05:21] capabilities this one specific talks
[05:23] about rack capabilities because the
[05:24] coher command r model it all model
[05:27] catalog pages also have these inference
[05:30] samples that you can use as starter
[05:31] codes to get started with for example A
[05:33] Lang chain SDK or a light llm SDK as we
[05:37] mentioned like we try to standardize the
[05:39] apis across all use cases so you can
[05:42] just plug in your our apis into any
[05:44] third party application like the light
[05:46] llm and have it working in no time so
[05:50] once you've gone over this check the
[05:51] pricing we go ahead and click on deploy
[05:54] and this is where we make sure that we
[05:57] are connecting to the Azure Marketplace
[05:59] so so we use Azure Marketplace just for
[06:01] the bilding side of things to make sure
[06:03] that you're built correctly based on
[06:05] your token usage and this is the step
[06:07] where you actually subscribe to that
[06:09] offer here I've already subscribed to
[06:11] that Microsoft subscription so it's
[06:12] giving me the option to continue to
[06:14] deploy it's as simple as choosing a
[06:17] deployment name checking if you want to
[06:18] enable content filter or not and
[06:20] clicking on deploy so under a minute
[06:23] you'll have your URL and key ready to
[06:26] get started so while this is happening
[06:28] let's look
[06:30] uh at other capabilities that we have
[06:31] like model benchmarks so when you're in
[06:33] the Azure AI Studio you also have the
[06:35] ability to check model benchmarks which
[06:37] is right here on the left under model
[06:40] catalog once you go in here here I'm
[06:42] showing all the models that we have you
[06:44] can see that we Tred to Benchmark on
[06:46] certain common characteristics like the
[06:48] model accuracy model coherence
[06:50] groundedness Etc and this is the perfect
[06:52] place for you to filter out which model
[06:55] you want to choose based on the extreme
[06:56] selections of models that we offer
[06:59] so let's go back to check oh yeah and we
[07:01] see we go back to the deployment that we
[07:03] created and it got created within a few
[07:05] seconds we have a Target URL right here
[07:08] and the key ready to use in any code
[07:10] base that you already have so now you
[07:12] may be thinking that before I move on to
[07:15] using my IDE I want to try it out a bit
[07:17] right is there something like a
[07:18] playground and that's where we also have
[07:20] this playground capability so once it's
[07:23] also in the AI Studio on the left if you
[07:25] see we're right under the chat
[07:26] playground so let's see a live example
[07:28] right here you can choose the model that
[07:30] you want to use in the playground so in
[07:32] this deployment section I've chosen a
[07:33] mral large deployment that I already
[07:35] have in this
[07:36] project let's try to uh chat with this
[07:39] model right here it's not customized on
[07:41] any any data I'm just directly asking
[07:43] the model so I'm trying to ask how does
[07:46] Microsoft promote the culture of giving
[07:48] so this will in general give me a
[07:50] generic response about how it has uh
[07:53] culture of giving through various
[07:54] initiatives it has employee match
[07:56] programs and some generic information
[07:58] that's available online but what if you
[08:00] want to specialize it for your for our
[08:02] own data so here we can go ahead and use
[08:05] the add your data functionality where
[08:07] you can choose an available index so
[08:10] let's choose an available index that's
[08:11] called Microsoft give that tells it in
[08:13] specific that what uh what are the
[08:16] specific things that are very
[08:18] particularly known internally or may not
[08:20] be available generic
[08:23] circumstances if we send out the same
[08:25] question right here we should get a more
[08:27] targeted response based on the documents
[08:30] in that
[08:32] index so just wait for a few
[08:36] seconds so shy while this is happening I
[08:39] had a quick question it's great that we
[08:41] are doing all this I'm just curious
[08:43] because you mentioned data and data
[08:45] source and everything are we using any
[08:47] of the data from our customers to train
[08:50] the models or is Microsoft using it are
[08:53] a model providers using any of the data
[08:55] that a customer brings in so that's a
[08:58] great question Sharma because that's a
[08:59] very common question we get from our
[09:01] customers and no we have very strict
[09:04] data privacy and policy rules in place
[09:06] your prompts and your completions are
[09:08] not shared with the model provider nor
[09:10] your data is used for training any of
[09:11] the
[09:14] models so yeah looking back at the
[09:17] results we see that it gave us a very
[09:18] specific response that says you get 50
[09:21] usds to start off with a new hire credit
[09:23] for the giving program and that wasn't
[09:25] in the response earlier so with just the
[09:27] click of a button we were able to link
[09:29] it to an index and get that response so
[09:32] that's how the playground
[09:35] works so talking about the different
[09:38] ways of deployment the one that we just
[09:40] saw was a serverless API option so in
[09:42] the model catalog there are two ways you
[09:44] can deploy a model one's called the
[09:45] managed compute and one's called the
[09:47] serverless API option with managed
[09:49] compute the user is responsible for
[09:51] getting their own GPU so you basically
[09:53] pay for the VMS per hour and you're
[09:55] responsible for the quota management
[09:57] capacity management and you can use
[09:59] hundreds of Open Source models with this
[10:02] the second uh way you can deploy models
[10:04] is by getting a serverless API and this
[10:07] available with both Azure op service and
[10:09] models as a service and this is what has
[10:12] about 30 plus Flagship models premium
[10:14] models that you pay for based on your
[10:16] usage so you get ready to use apis and
[10:19] you only pay for the input tokens or the
[10:21] output tokens that you
[10:23] use we've also put in a lot of effort to
[10:26] make sure that we standardize the schema
[10:28] and the apis of these models for you so
[10:31] we've worked with the model providers to
[10:32] make sure that we build an SDK on top of
[10:34] a very standardized rest API system and
[10:38] such an such an SDK works with common uh
[10:41] open- sourced applications things like
[10:43] Lang chain as well as the model provider
[10:46] specific sdks so all you have to have is
[10:48] a different endpoint and every endpoint
[10:51] has the same API structure and the same
[10:54] SDK structure so you can just swap in
[10:56] one for another evaluate create multiple
[10:58] evaluations
[10:59] compare the results and choose the one
[11:01] that's perfect for your use
[11:06] case okay awesome so um we've been
[11:09] seeing everything about the model
[11:11] catalog and models can you show us an
[11:14] actual use case
[11:16] example yeah so uh let's briefly talk
[11:19] about how you can actually use these
[11:21] apis in your IDE let's talk about the
[11:23] function calling example and let's take
[11:25] the Mr Large model for for that use case
[11:28] so here I have a simple function calling
[11:30] example where I'm trying to qu use this
[11:32] model as a chatbot for example of in
[11:34] shop the shop has sells certain
[11:36] stationary items it has certain specific
[11:39] pricing and may have certain ongoing
[11:41] discounts so if you just use a model as
[11:43] a blackbox you will not get the specific
[11:45] pricing for the model or for the shop or
[11:48] any of the ongoing discounts but what
[11:49] I'm doing here is using the function
[11:51] calling capability of the mral large
[11:53] model to define a function called get
[11:55] bill amount that can take in the
[11:58] specific information that we fed to it
[12:00] recognize that it needs to call this
[12:02] external function based on the prompt
[12:04] and smartly make that call query that
[12:06] result and give you the exact
[12:08] information so right here I've defined
[12:10] that function I've defined the tool for
[12:12] that model for Mr Large we send in a
[12:15] prompt that says you're a helpful
[12:16] assistant that helps users find how much
[12:18] they have to pay and we also make sure
[12:20] that we tell it that you also care about
[12:22] the environment and you also have to
[12:24] help users understand possible things
[12:26] they should be careful of when using
[12:27] these items so this is just to uh add
[12:30] more context to the response and see how
[12:32] the model can adjust based on the
[12:34] requirement we go ahead we send this
[12:36] response in we can see that the model
[12:38] has intelligently identified that it is
[12:40] calling the function get bill amount
[12:42] with the right arguments so it
[12:43] identified that we queried for a stapler
[12:45] and we as Tred to ask what is the price
[12:47] for the 10 staplers and if we see the
[12:50] chat response it says the cost of 10
[12:52] staplers including any ongoing discounts
[12:54] is $45 which is very specific and it
[12:56] also makes sure that it REM the users to
[13:00] be mindful of the environment and try to
[13:02] use staples when possible and this is in
[13:04] result of the system message that we
[13:05] sent to it when we asked it to be
[13:08] environmentally friendly and give users
[13:10] the right context so similarly if you
[13:12] see right here you can swap any code
[13:15] base with uh any endpoint that you have
[13:18] and
[13:19] without putting M much time into it or
[13:21] much effort into it you have a running
[13:23] API app right here we also make sure
[13:26] that we use uh uh model provider um
[13:30] feels like the safe prompt setting to
[13:32] true so on top of we always build on top
[13:35] of what the model provider capabilities
[13:36] are already
[13:38] existing
[13:41] a so now that we've talked about how we
[13:44] can set it up in the IDE let's talk a
[13:46] bit about how you can set it up in the
[13:47] UI and how you can create a generative
[13:49] AI app using prompt flow so when you try
[13:52] to here I'm trying to create a shopping
[13:54] assistant chatbot using promp flow where
[13:56] it's a simple rag application where we
[13:58] taking the user prompt we try to get
[14:00] retrieval uh we retrieve contact
[14:02] specific information from our index and
[14:04] then uh send it to the llm to generate
[14:06] an output here we've created the lookup
[14:09] step for it which is basically doing the
[14:11] rag part of it the generate part is
[14:13] going to generate the output from the
[14:14] llm but we've added this extra step of
[14:17] rephrasing where we using the query
[14:19] transformation technique where we take
[14:21] in the user con uh prompt which is
[14:23] generally very succinct but we try to
[14:25] make it more verbos by rephrasing it
[14:28] because we've seen better result results
[14:29] of rag with
[14:30] that so let's look at a live example of
[14:34] this right here I have this prom flow
[14:36] running right here my compute session is
[14:38] running we see that the first question
[14:41] that we ask is do you have any new
[14:42] hiking shoes but the rephrase step
[14:45] rephrase it into a longer verbos output
[14:47] that says I'm looking for hiking Avail
[14:49] hiking shoes available and if so what
[14:51] materials and features so it basically
[14:53] elongated that
[14:55] question we check the output of the
[14:57] lookup step and we see that The Prompt
[14:59] was able to get the context specific
[15:02] information from the index that we
[15:03] provided to it so it identified certain
[15:05] amount of information that we can now
[15:07] send to our llm in the next step and the
[15:09] llm generates a response so based on
[15:11] that specific information we were able
[15:14] to get this output that recommended the
[15:16] fleece fit uh Flex jacket for the women
[15:19] so we can see that we are able to
[15:22] generate a plum flow end to endend but
[15:24] you may be wondering that how do I make
[15:25] sure that I'm able to plug in different
[15:27] models into this flow and this is where
[15:29] you can try to create variance so here
[15:31] you can see that in the generate step
[15:33] I'm using a connection from the coher
[15:35] command r model but you can go ahead and
[15:37] choose any other connection to any other
[15:39] model and use evaluation to try to
[15:41] compare the results from the same for
[15:44] the same flow for different models so
[15:46] example for the um first step when we
[15:49] trying to create the embeddings here
[15:50] I've used the Ada model but you can go
[15:52] ahead and try to see okay how does the
[15:54] command r model work with the command
[15:56] embed model so you can create these
[15:58] variance and try to see the evaluation
[16:00] results in the interest of time I
[16:02] already ran some evaluations as we also
[16:04] saw in the previous uh demo and here we
[16:06] trying to compare the CER command R
[16:08] versus Lama 3 versus the mral large and
[16:11] the evaluation capability helps you to
[16:14] compare the same model for the same flow
[16:17] on different parameters and you can see
[16:19] how one fed against
[16:24] another so this is all great and I think
[16:27] you touched upon data privacy a little
[16:29] bit so can you go a little bit more into
[16:31] the details of what else do we have in
[16:33] the AI Studio or model catalog to ensure
[16:36] customers privacy and data security yeah
[16:40] absolutely that's the key so let's talk
[16:42] a bit about how we ensure that the data
[16:45] privacy and security compliance needs
[16:46] are met so as I mentioned there are
[16:48] three pillars to this so one's the data
[16:50] privacy part second the security and
[16:52] compliance and the third is the
[16:54] responsible Ai and the content safety
[16:56] talking about data privacy for both man
[16:59] compute and serverless apis your prompts
[17:01] and completions are not shared with the
[17:03] model provider your prompts and
[17:05] completions are not used for training
[17:07] the models no data is shared for
[17:09] training or with the model providers so
[17:11] you can be assured that the AI platform
[17:14] makes sure that your Enterprise needs
[17:15] for data privacy are
[17:17] met we also have this additional feature
[17:20] of adding hidden layer to our model
[17:22] scanning so we make sure that we finding
[17:24] the embedded malware and back doors we
[17:26] it scans for common vulnerabilities and
[17:28] exposures and detect tampering and
[17:30] Corruption across models so for any
[17:33] model that's labeled curated by Azure AI
[17:35] you can be assured that it's passing
[17:37] through the required
[17:39] checks talking about security and
[17:41] compliance in addition to the data
[17:43] privacy Norms that we mentioned we also
[17:45] offer the capabilities of adding private
[17:47] networking so that your data is not
[17:49] exposed to the Internet so you have the
[17:51] control over routing your Ingress and
[17:53] egress traffic through the v-ets and you
[17:55] also have the ability to set up fqdn
[17:57] rules so you can approve proove outbound
[17:59] access to non- aure
[18:02] resources um in addition to this you can
[18:04] also regulate access to models with
[18:06] Azure policy integration so you can have
[18:08] allow list or deny list patterns and you
[18:11] can split out which model collections
[18:13] you want access to or not and you can
[18:16] also use these different policies for
[18:18] separating out the dev test and
[18:19] production
[18:24] environments awesome so um shubi thank
[18:27] you so much for going through the model
[18:29] catalog and AI Studio what what are the
[18:31] features available in there and all all
[18:33] these great demos so now I just want to
[18:35] go into a few customer success stories
[18:38] and uh the one of the main uh kind of
[18:41] underlying theme for all the customer
[18:43] success stories that I'm going to show
[18:44] is that these customers are not just
[18:46] using one model and for their use case
[18:49] they're using multiple models from the
[18:50] model catalog and it could be in one use
[18:53] case or across multiple use cases
[18:54] similar to what should be has shown in
[18:56] the
[18:57] demo and the first customer we're going
[18:59] to talk about is ey and uh they've been
[19:02] using uh our large language models
[19:04] they've started off with the open AI
[19:06] models that was available in the Azure
[19:08] open AI service um they are doing that
[19:10] today and they're also looking into
[19:12] llama models uh where they are looking
[19:14] into llama models for like really uh uh
[19:17] task specific use cases like for
[19:19] documentation and for summarization and
[19:22] all that and um they have using our
[19:25] model catalog they built ey. a which is
[19:27] a generative AI platform for ey
[19:29] professionals which addresses the need
[19:31] for enhanced uh productivity and
[19:33] accuracy in professional tasks and one
[19:36] of the key things that we want to show
[19:38] is what's the result of what they've
[19:40] been doing the eyq chat that they built
[19:43] has been adopted by 275,000 employees
[19:46] internally and allow the employees to
[19:49] perform a wide range of tasks
[19:50] efficiently and with great accuracy and
[19:53] what some of the lessons that they have
[19:54] learned is it's not AI using AI in their
[19:58] use cases is not like a one-time thing
[20:01] they need to do continuous evaluation of
[20:03] AI performance and they want to stick to
[20:05] all the responsible AI practices and
[20:07] that's one main reason why they've been
[20:09] using Azure AI uh uh model catalog and
[20:12] Azure AI Studio it's because they feel
[20:14] that they can easily do this evaluation
[20:17] and um make sure whatever they're doing
[20:20] putting in production is going to be uh
[20:22] really and adhering to safe and
[20:24] responsible
[20:26] Ai and then the next customer I wanted
[20:28] to talk about is C CGM again they are a
[20:32] big uh Global player in Sea Land Air and
[20:35] logistic Solutions and they are also
[20:37] building a kind of like a robotic
[20:39] process uh they've been doing
[20:41] traditional robotic process Automation
[20:43] and they've decided to use mistal model
[20:45] from a model catalog and they have built
[20:47] again a similar chatbot like scenario uh
[20:50] for their customer care agents and um
[20:53] one thing that they have seen is they
[20:55] have seen a reduced response latency and
[20:57] increased customer customer satisfaction
[20:59] in their chatbot uh use case and they
[21:02] plan to again extend the application of
[21:05] llms to Encompass specific products for
[21:07] Core Business activities like invoicing
[21:10] customer document analysis uh
[21:12] interpreting free client text and uh
[21:15] writing emails and all that and finally
[21:18] the last customer story I want to share
[21:20] is Bridgestone again Bridgestone is a
[21:22] very popular name um their their use
[21:25] case is U they have been using the Nixa
[21:27] model from model catalog we launched
[21:29] Nixa uh time series model at build last
[21:32] month and it's a Time series forecasting
[21:35] model and they're using it specifically
[21:37] to predict monthly demand for a vast
[21:39] portfolio of products and um one of the
[21:42] things that they want to do is
[21:44] streamline their forecasting pipelines
[21:46] enhance accuracy and reduce operational
[21:48] complexity and again what they have seen
[21:51] is that they have seen that using the
[21:53] forecasting model like time gen from
[21:55] Nixa has helped them reduce U Errors By
[21:58] nearly 30% on average in forecasting
[22:00] errors uh which is huge and U again in
[22:04] all these customer use cases the time it
[22:06] took for them to start using llms in
[22:08] their applications to seeing the results
[22:10] and impact has been reduced
[22:13] significantly because they were being
[22:15] able to use uh model catalog and Azure
[22:17] AI Studio where we provide as should be
[22:20] showed in the very first slide we do we
[22:23] have tools for prototyping um optimizing
[22:26] and operationalizing so whether you're
[22:28] just starting off with let me try this
[22:30] for a prototype project to realizing
[22:33] okay I need to put it into production
[22:35] the time it takes from going from that
[22:37] to the last step has been reduced
[22:38] significantly mostly because we have
[22:40] streamlined all the different um
[22:43] foundational models we have provided the
[22:44] right tools for all our customers to
[22:46] kind of go through that whole uh llm
[22:49] life cycle I think that's pretty much it
[22:53] uh thank you thank you
[22:58] oh
[23:01] [Music]
