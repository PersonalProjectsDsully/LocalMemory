---
type: youtube
title: Mastering LLM Inference Optimization From Theory to Cost Effective Deployment: Mark Moyou
author: AI Engineer
video_id: 9tvJ_GYJA-o
video_url: https://www.youtube.com/watch?v=9tvJ_GYJA-o
thumbnail_url: https://img.youtube.com/vi/9tvJ_GYJA-o/mqdefault.jpg
date_added: 2025-05-26
category: Natural Language Processing
tags: ['tokenization', 'attention mechanisms', 'GPU optimization', 'NLP', 'model training', 'subword tokenization', 'machine learning', 'token IDs']
entities: ['NVIDIA', 'GPU', 'Llama tokenizer', 'tokenization', 'attention mechanisms', 'NVIDIA GPUs', 'token IDs', 'prefill stage']
concepts: ['tokenization', 'attention mechanisms', 'GPU optimization', 'model training', 'subword tokenization', 'memory hierarchies', 'token ID mapping', 'prefill stage', 'model inference', 'efficiency in tokenization']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of machine learning', 'Familiarity with tokenization in NLP', 'Knowledge of GPU architecture']
related_topics: ['Natural Language Processing (NLP)', 'Deep Learning', 'GPU Acceleration', 'Transformer Models', 'Subword Tokenization', 'Attention Mechanisms', 'Model Optimization', 'Machine Learning Workflows']
authority_signals: ['I have made me sound smarter', "this is good for you to appreciate sort of that complexity that's happening", "I'll talk a bit more about that"]
confidence_score: 0.7
---

# Mastering LLM Inference Optimization From Theory to Cost Effective Deployment: Mark Moyou

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=9tvJ_GYJA-o)  
**Published**: 4 months ago  
**Category**: AI/ML  
**Tags**: llm inference, gpu optimization, ai deployment, nvidia, model optimization, cost management, inference optimization  

## Summary

# Summary of "Mastering LLM Inference Optimization From Theory to Cost Effective Deployment" by Mark Moyou

## Overview
Mark Moyou from Nvidia discusses **LLM inference optimization**, focusing on **cost-effective deployment** and practical insights for handling large language models (LLMs). The session emphasizes understanding the technical underpinnings of LLM inference, including tokenization, attention mechanisms, and GPU utilization, while addressing challenges like scalability and resource efficiency.

---

## Key Takeaways

### 1. **LLM Inference Workflow**
- **Tokenization**: 
  - Text is converted into **token IDs** using a model-specific tokenizer (e.g., Llama’s 128,000 tokens).
  - Tokens are not always human-readable words; they represent subwords or symbols.
- **Prefill Stage**:
  - The initial processing of the prompt involves computing **attention mechanisms** across the entire input.
  - This is computationally intensive, especially for large-scale requests (e.g., 1 million users with 10,000-token prompts).
- **Token Generation**:
  - LLMs generate **one token at a time**, with each token stored on the GPU (visualized as red/green vectors).

### 2. **Technical Challenges**
- **KV Cache**:
  - A critical component for efficiency, but also a **cost driver** due to memory constraints.
  - Stores intermediate results (e.g., attention keys/values) during inference.
- **Attention Mechanisms**:
  - Optimized via GPU memory hierarchies, with ongoing research into advanced schemes for acceleration.

### 3. **Performance and Cost Considerations**
- **Scalability**:
  - Handling millions of concurrent requests requires efficient **parallelization** and **resource allocation**.
  - The "prefill" stage dominates computation, while token generation is faster but still resource-heavy.
- **Cost Control**:
  - Hybrid deployment strategies (e.g., combining APIs and open-source models) can reduce expenses.
  - Leveraging **free resources** (e.g., Nvidia’s inference APIs) for testing and prototyping.

### 4. **Practical Tools and Strategies**
- **Open-Source Tools**:
  - Use frameworks like Hugging Face or custom implementations for tokenization and inference.
- **GPU Utilization**:
  - Monitor and optimize memory usage for KV cache and attention mechanisms.
- **Hybrid Approaches**:
  - Balance between using pre-trained models (e.g., Llama) and custom training for specific use cases.

---

## Key Quotes/Insights
- **"LLMs generate one token at a time, but the initial prompt processing is computationally heavy."**
- **"KV cache is both a performance enabler and a cost driver."**
- **"Tokenization is about efficiency: minimizing the number of subword units to represent training data."**

---

## Actionable Recommendations
1. **Leverage Free Resources**: Use Nvidia’s free inference APIs for testing and scaling.
2. **Optimize Tokenization**: Choose tokenizers that balance efficiency and language-specific needs.
3. **Monitor GPU Utilization**: Prioritize memory-efficient attention mechanisms and KV cache management.
4. **Adopt Hybrid Deployment**: Combine APIs with open-source models to reduce costs.
5. **Understand Token Dynamics**: Recognize that tokens are subword units, not always human-readable words.

---

## Conclusion
Mark Moyou’s session underscores the importance of **technical intuition** in optimizing LLM inference. By understanding the interplay between tokenization, attention mechanisms, and GPU resources, developers can build scalable, cost-effective solutions for real-world applications.

## Full Transcript

[00:01] [Music]
[00:12] it's very difficult to teach um
[00:14] extremely technical material in about 20
[00:16] 20 minutes initially I had planned for
[00:17] at least a 45 minute session so I left
[00:20] some reading material for you at the end
[00:22] and um all of the resources you could
[00:24] download slides and everything so feel
[00:26] free to take screenshots or not and so I
[00:28] work at Nvidia I'm a Architects I work
[00:31] primarily with retail clients and it's
[00:32] my job to essentially work with those
[00:34] clients understand sort of what their
[00:37] main challenges are this is data
[00:38] processing computer vision um across all
[00:41] of the different use cases and then now
[00:43] I'm focused on llm inference so my hope
[00:45] today is that um you get a better
[00:48] intuition of exactly what's happening
[00:50] with this particular workload and how
[00:52] you go about uh to some degree sizing
[00:54] things choosing different gpus etc etc
[00:57] and more importantly controlling the
[00:58] cost of a deployment cuz that's often
[01:00] times the thing that's going to really
[01:02] prevent you from taking this taking this
[01:06] to any meaningful scale is that overall
[01:08] cost of a deployment most folks that
[01:10] I've seen are doing some kind of hybrid
[01:12] so you choose a big box API you have
[01:14] some set of queries that go there in
[01:16] addition to you have some set of queries
[01:18] that go to some open- Source you know
[01:20] hosted model or some fine tune model
[01:22] that you have internally so just
[01:25] reference um if you go to build.
[01:27] nvidia.com or ai. nvidia.com
[01:30] everyone can get a thousand inference
[01:32] requests for free so I typically
[01:33] recommend this to folks who are
[01:35] benchmarking um different types of op
[01:37] Source models we have all of those
[01:39] models hosted it's optimized if you're
[01:41] teaching a course um and you are trying
[01:43] to evaluate all of the different LMS
[01:45] that are out there for your business
[01:47] there are also multimodal llms um speech
[01:50] llms every model that Nidia accelerates
[01:53] will be available there for you and
[01:55] that's sort of a path to you um to
[01:57] either go optimize them yourselves or to
[01:59] work with us um you'll see things about
[02:01] uh Nvidia inference microservice and all
[02:03] of those things that you can take to
[02:05] Enterprise so we have sometimes the uh
[02:09] I'll call it the rocky road and then
[02:10] there's smooth roads whatever path you
[02:12] want to take we're here to support you
[02:15] uh in terms of agenda very simple I I
[02:17] want you to understand the llm inference
[02:19] workload and then we'll move to how you
[02:22] go about measuring a production
[02:23] imployment and some of the things you
[02:25] need to be watching it's a little more
[02:27] than um let's say you know the total
[02:29] time to generate and really
[02:30] understanding what's happening on the
[02:32] gpus as you sort of scale out even if
[02:34] you have a single GPU I think it's very
[02:36] important for you to just have the
[02:37] intuition and then lastly I'll show you
[02:39] some software that you can use um some
[02:42] open source packages that you can use
[02:43] and then point to uh some paid offerings
[02:46] okay we're going to get into the llm
[02:48] inference workload itself so the first
[02:51] part is is really understanding what
[02:53] happens when you send a prompt onto the
[02:55] GPU so I have this example here I'm
[02:57] saying okay write me a presentation so I
[02:59] sound smart I come to the a engineer
[03:00] conference and you guys are maybe going
[03:03] to like to talk and essentially what I'm
[03:04] going to do is I'm going to put that on
[03:06] the GPU so the moment that I send that
[03:08] prompt on the GPU it stays on the GPU so
[03:10] think about that and then from there I'm
[03:12] going to generate one token at a time so
[03:14] I'm generating the tokens llm inference
[03:17] is hard and I put the time stamps T1
[03:20] through T4 so in every single deployment
[03:22] no matter how fast anyone claims they
[03:24] they're doing things um it's typically
[03:27] one token that's generated at a time
[03:29] that's very important to understand the
[03:31] next thing is that in order for an llm
[03:34] to give you a coherent answer just like
[03:36] how you speak you have to remember every
[03:38] single thing that you said before and
[03:40] that you'll understand the mechanism of
[03:42] um how that how llms are able to do that
[03:45] so that's why I'm putting llm inference
[03:47] is in red and putting that back onto the
[03:49] GPU so every token that I generate gets
[03:52] locked onto the GPU and then you'll
[03:54] actually see what that looks like um in
[03:56] terms of vectors how many of you have
[03:58] heard of KV cach before
[04:01] okay some of you um typically I don't
[04:03] see maybe many leaders here about this
[04:06] thing called KV cach KV cach is this
[04:08] thing that really drives to some degree
[04:10] the cost uh so whether or not you use
[04:13] some big box API or um you're using a
[04:16] single GPU it's all the same sort of
[04:18] mechanisms the same algorithm that
[04:20] everyone is trying to solve so in terms
[04:22] of steps here the the I I like to as I
[04:26] said sharpen your intuition so the first
[04:28] thing if we move from the left my first
[04:30] job is to convert these text whatever
[04:32] text that you send we're going to focus
[04:34] on llm inference into some words that
[04:36] the model understands so the model will
[04:38] have its own vocabulary and it's my job
[04:40] to translate that I'll give you the
[04:42] technical uh terms coming up after that
[04:44] and the first thing that happens is I do
[04:46] some initial prompt processing so I have
[04:48] to compute the attention mechanism on
[04:51] the entire prompt I repeat that I have
[04:53] to compute the attention mechanism on
[04:55] the entire prompt per user so if I have
[04:58] a million people hit my service and a
[05:00] million people send 10,000 tokens that's
[05:03] a million time 10,000 attention
[05:05] mechanisms that I need to compute also
[05:08] while generating tokens for other people
[05:10] so that's it's good for you to
[05:11] appreciate sort of that complexity
[05:13] that's happening and once I finish
[05:15] processing that prompt then I'm going to
[05:17] start generating one token at a time and
[05:19] that typically happens very fast and
[05:22] then from there every token that gets
[05:23] generated that's in the lm's vocabulary
[05:26] I need to now DET toonize that back into
[05:29] your language
[05:30] so here's the technical terms that
[05:32] you'll see when you read the literature
[05:34] or you read uh super technical documents
[05:36] first is tokenization each model will
[05:39] have its own tokenizer and um the thing
[05:42] to think about when you think of
[05:44] tokenizers when they did pre-training
[05:46] they had they downloaded the internet
[05:48] and some right and they cleaned it up
[05:50] etc etc so tokenizer and as you start
[05:53] thinking of the complexity across
[05:55] languages coding languages uh regions
[05:58] etc etc they Tred to get what is the
[06:00] minimal set of character groups that can
[06:04] represent this entire training data set
[06:06] efficiently CU it's really all about
[06:08] efficiency so for instance the Llama
[06:10] tokenizer has 128,000 tokens all right
[06:13] and I I'll talk a bit more about that so
[06:16] here's what it actually kind of looks
[06:17] like on a GPU so I tokenize the llm
[06:20] understands it I go into this thing
[06:21] called prefill prefill is a stage where
[06:23] you compute the attention mechanism and
[06:25] many people are doing advancements with
[06:27] attention mechanisms um I'll talk bit
[06:29] more about that so there tons of
[06:31] different schemes people leverage all of
[06:34] the different types of memory
[06:35] hierarchies in gpus to really accelerate
[06:38] this type of workload and then I start
[06:40] generating tokens one at a time the red
[06:42] and the green just signify hey I'm
[06:45] storing those tokens on the GPU the
[06:46] green is the latest one that I sent out
[06:49] so hopefully that makes sort of
[06:50] intuitive sense all right so the other
[06:53] thing I want you to visualize um I I
[06:56] think it's nice to visualize what what
[06:59] is the actual data that sits on the GPU
[07:02] so first a token is approximately four
[07:04] characters that's a nice way for you to
[07:06] think about it um so from here I have
[07:09] two vectors so the first Vector is just
[07:11] showing token one through token v v is
[07:14] the total number of tokens that I have
[07:16] in my tokenizer and the second Vector
[07:19] below is just I have some numeric index
[07:21] I don't want to keep using the token to
[07:23] reference itself I just use use the
[07:25] number as a lookup so my job when a
[07:28] prompt comes in is to convert that text
[07:31] into those token what I'm going to call
[07:33] token IDs okay so I I have make me sound
[07:37] smart I make me sound smarter you see
[07:38] two vectors sets of tokens and the key
[07:41] thing I want you to walk away with from
[07:43] from that distinction is that an l&m's
[07:46] token is not a human word sometimes it
[07:48] is sometimes it's not it's typically
[07:50] some subpar of words you'll see we
[07:52] symbols when you look at tokenizers from
[07:54] different models um but you want that
[07:56] first framing so now we have text we hit
[07:58] to a vector right so from there each one
[08:02] of those llm tokens had a corresponding
[08:05] embedding Vector so embedding Vector is
[08:08] everything we embed uh videos we embed
[08:10] images we embed text tokens think of it
[08:13] as a representation that uh an llm can
[08:16] use to compare things and do math on so
[08:19] that's why we always want to com excuse
[08:21] me convert into some Vector
[08:22] representation right because some Vector
[08:25] representation is just some high
[08:27] dimensional coordinate space and we're
[08:28] just rearranging
[08:29] objects that's to some degree what
[08:31] you're doing okay so from those token
[08:34] IDs I went to the actual um embedding
[08:38] vectors themselves so if you look make
[08:39] me sound smart now becomes a matrix all
[08:42] right make me sound smarter becomes a
[08:44] matrix with an extra column so in
[08:47] reality what you're doing every time you
[08:49] submit a prompt I don't care what llm
[08:51] you submitted to who you submitted to
[08:53] this is what you're doing right you are
[08:55] converting your text now images as well
[08:58] they get converted to some Ida tokens or
[09:01] something like that that'll be another
[09:02] interesting talk to do diffusion models
[09:04] etc etc but you're really putting this
[09:07] large Matrix on the GPU so why that the
[09:11] next question you should ask is okay um
[09:13] why are gpus is good for this workload
[09:14] because they process matrices really
[09:16] really fast so that's sort of the the
[09:18] advantage and the thing hopefully that
[09:20] that makes a little more sense to you
[09:22] now the next thing I want to talk about
[09:24] is how the llm is going to process these
[09:26] tokens and I'll keep in mind if any well
[09:29] I'm not even going to ask you to raise
[09:31] your hand I'm 100% sure each of you is
[09:32] used it an LM if you have not I'm not
[09:35] sure what's happening
[09:37] uh uh the other one is the attention
[09:39] mechanism I I truly think um it's one of
[09:43] the things that you should understand if
[09:45] we ever drift away from it that's fine
[09:47] but the fundamentals of that mechanism
[09:50] and and seeing sort of the Innovations
[09:52] around that I think can help anyone any
[09:54] business leader etc etc just because you
[09:56] are able to speak a different kind of
[09:58] language um in this generative future so
[10:01] as you think of the attention mechanism
[10:03] the intuition that you should have is
[10:05] just that mechanism of relating tokens
[10:07] how do I distinguish in a sentence what
[10:09] is important all right and then for the
[10:11] next token that's going to be generated
[10:13] hey what tokens that I said before were
[10:16] really important for me to make a next
[10:18] good decision for that next token so
[10:20] that's the intuition and now we're going
[10:22] to won't necessar touch too much of the
[10:24] math but I want you to see sort of
[10:26] what's happening on the GPU so once
[10:28] again The Prompt comes in I'm just going
[10:29] to do a short one make me sound smart
[10:31] I'm going to generate this token called
[10:33] llm all right uh we saw the same
[10:36] matrices that I said before so remember
[10:38] my text now turns into a matrix hitting
[10:40] onto the GPU and and the main thing I
[10:43] want you to understand or visualize here
[10:45] is actually
[10:47] how an llm memory works so now when
[10:51] you're speaking you've recorded
[10:53] everything that I've said for the last
[10:55] uh 10 minutes in your brain somewhere
[10:56] it's it's stored so now you're going to
[10:58] see how the L is storing what it is that
[11:00] you just said so from there um a lot of
[11:03] folks will hear about these query key
[11:05] and value matrices this is what the
[11:07] actual model weights look like so when
[11:09] you look at a model weights file if you
[11:11] go on hugging face there's typically a
[11:12] Json file that will show you all of the
[11:14] different pieces of model files and
[11:17] you'll see this thing called qk andv so
[11:19] I have these model weights so now I've
[11:21] went from text to a matrix I'm going to
[11:24] Matrix multiply against the weights of
[11:25] the models so now I get these three
[11:28] output models
[11:29] so think of these weight matrices that I
[11:31] showed here think as um when you're
[11:34] doing a projection what you're doing is
[11:36] you're taking um some coordinates and
[11:39] you're putting it into a different space
[11:41] that's really what you're doing when you
[11:42] do Vector Matrix math so now when I do
[11:44] this Matrix multipication this query key
[11:47] and value Matrix so if you look at
[11:48] different tutorials on attention you'll
[11:51] see these things pop up a lot so
[11:52] hopefully that'll help you to read it a
[11:54] lot more this is now the lm's
[11:57] interpretation of each of those tokens
[11:59] that you sent in right and now the job
[12:01] is how do I now take uh these query key
[12:04] and value matrices and sort of interpret
[12:07] it to try to generate the next best
[12:09] token and this is just happening
[12:11] constantly over and over every single
[12:13] token that's happening but the key thing
[12:14] I want you to walk away on the slide is
[12:16] where I drew the key and the value right
[12:19] when people talk about KV cach
[12:21] optimization every llm performance
[12:23] engineer is just literally trying to
[12:25] make that thing as fast and small as
[12:27] possible and I'll I'll that it'll make a
[12:29] little more sense as to what that does
[12:31] to your cost But ultimately these key
[12:33] and value matrices this is like your
[12:35] llms memory so it'll make a little more
[12:37] sense coming up I know I didn't show a
[12:38] ton of the math I show some tutorials
[12:40] afterwards so you can go read more about
[12:42] that um my intention here is for you to
[12:44] visualize key and value so every time
[12:46] you see a prompt I just want you
[12:47] thinking crap key and value is on my on
[12:50] my GPU okay the next so here's the real
[12:54] value of the KV cache so remember we
[12:58] said said that whenever I generate a
[13:00] token I'm going to push it back into the
[13:02] GPU right so every token I generate it
[13:05] goes back into the GPU and then I have
[13:06] to compute an attention mechanism so
[13:09] this is what's happening this new token
[13:10] I generated llm I get its Vector
[13:13] representation as you see in blue but
[13:15] now I I do that Vector Matrix math now
[13:19] so before I did Matrix Matrix math
[13:22] that's my first prompt first comes in I
[13:24] generated my first token now I'm doing
[13:26] Vector Matrix math you know people will
[13:29] batch this across all requests but I'm
[13:31] just showing you a single request so you
[13:33] can see it now the value of the KV cache
[13:37] is if I were to if I didn't have the KV
[13:40] cache I would have to reprocess all of
[13:43] that work I did on the prompt that I did
[13:45] before so this is the benefit of your KV
[13:47] caches to now I'm just going to compute
[13:50] attention on this newest token how does
[13:52] this new token relate to everything that
[13:54] I said before that's the thing that's
[13:56] really happening intuitively so so if I
[13:59] have this KV cache my Generations can be
[14:01] fast okay and it's really up to the the
[14:05] What's called the batch manager on the
[14:06] GPU to make sure that I'm just pushing
[14:09] out as many tokens as possible okay so
[14:12] if you look at uh an llm these groups of
[14:16] three matrices are calling attention
[14:17] head there more matrices than not but
[14:19] these are the main ones um llama has 32
[14:21] attention heads so I just kind of want
[14:23] you to appreciate what an llm really
[14:25] looks like right so I have 32 sets of
[14:27] these matrices I'll have 32 of those KV
[14:30] caches happening at the same time and
[14:32] now I have to combine all of that to
[14:34] then generate the next tokens so there's
[14:35] an incredible amount of work that
[14:38] happens in a very short space of time to
[14:40] give you a coherent token okay a good
[14:44] mental model for you to keep in your
[14:45] head I'm going to speed up a little bit
[14:46] is to um if you see the number of
[14:48] parameters multiply that by two and that
[14:51] is your fp16 gigabyte memory on the GPU
[14:55] so if you have let's say an L4 I think
[14:57] is 20 gigs um and I have a llama 8B
[15:00] that's automatically 16 gigs fp16 so I
[15:04] only have 4 gigs left for my KB cache so
[15:07] on the GPU it's either the model weights
[15:09] or tokens that's it there's nothing else
[15:11] on the GPU and I I have a thing to read
[15:13] on that this is a really good blog it
[15:16] shows you all of the different um
[15:18] optimizations that you can do and okay
[15:21] now let's talk about measuring so if you
[15:23] ever see this thing called ISL or I have
[15:26] ITA oh sorry ISL or SL that's input
[15:30] sequence link output sequence link so
[15:32] now I want you to see what some Advanced
[15:34] monitoring might look like if any of you
[15:36] are devops folks these are things that
[15:37] you want to record the first thing that
[15:39] we measure is time to First token so how
[15:42] long does it take me to generate um the
[15:44] process the prompt and then generate my
[15:46] first token and that's typically a
[15:48] measurement of how good your attention
[15:50] mechanism processing is that's really
[15:52] what you're trying to sus out so that's
[15:55] time to First token into token latencies
[15:57] so after I've generated my first token
[16:00] every single token after that I'm
[16:01] looking at those individual spaces so
[16:04] everything that's going to happen there
[16:05] U think about when the system is on the
[16:07] load I have you know a thousand requests
[16:09] coming into my system I'm generating a
[16:11] thousand sets of different tokens and
[16:13] the more memory I occupy typically that
[16:15] slows down processing so if you start to
[16:17] see drift in this metric then so I'll
[16:19] show you some plots that you can look at
[16:21] and then time to Total generation how
[16:23] long did it take me to initially get the
[16:25] prompt fully finish the answer right
[16:27] super intuitive like I I said ISL OSL
[16:30] that's all that means when you see them
[16:32] on the plots coming up okay uh this is a
[16:36] very important Paradigm for you to
[16:37] understand in your mind uh so I I worked
[16:40] with a lot of folks on you know maybe uh
[16:42] rexus deployments or deployments of
[16:44] other types of models so on the GPU if
[16:46] you're only deploying one model on a GPU
[16:48] outside of llm in France uh in my
[16:50] opinion I think you're wasting the GPU
[16:52] you can put multiple models on the GPU
[16:54] to actually increase your throughput
[16:55] that's why it was really created um so
[16:58] this is a slide is excuse me this figure
[17:01] is just showing I can have multiple
[17:02] models I have some space for data and
[17:04] that's how I increase my throughput per
[17:06] unit Hardware however on the llm INF
[17:09] front side it's very different I have
[17:11] one model you know folks can fit
[17:13] multiple models on a GPU that's cool but
[17:15] that's not a real production use case
[17:16] you'll typically have a single model the
[17:18] remaining space that you have is all for
[17:20] KV cash and generating all those tokens
[17:23] so I just put four different requests
[17:24] and I I just kind of want you to see the
[17:26] boxes that are happening okay uh I would
[17:29] say this is the most important slide in
[17:30] the entire presentation because this is
[17:32] the thing that will determine both your
[17:34] cost and performance so there are four
[17:36] different querying patterns that happen
[17:39] and this is something that you must
[17:41] measure in your deployment because often
[17:43] times you might read benchmarks and
[17:45] they'll just say all right they'll
[17:46] cherry pick one or two of these but in
[17:48] reality in your production system you
[17:50] might have several of these different
[17:52] patterns that are occurring so let's
[17:54] take a look at the first one long input
[17:56] short output so a long input means
[17:59] it's going to take me technically longer
[18:01] to compute the attention mechanism so my
[18:03] pre-fill stage will be longer I occupies
[18:05] more memory from my prompt does that
[18:07] make sense intuitively hopefully it it's
[18:10] grabbing you but then on the generation
[18:12] side I don't generate much tokens so
[18:14] there's not much those tokens are not
[18:16] picking up a lot of memory and they will
[18:18] tend to finish Fast so the second the
[18:20] second one or the maybe the most costly
[18:22] use cases um so I have clients that will
[18:25] message me and say hey my data
[18:26] scientists are putting two bigger
[18:28] prompts on my GPU
[18:29] so now they're killing my deployment cuz
[18:31] if everyone went and put the maximum
[18:33] context length I can only fit so many
[18:35] requests on the GPU so that's something
[18:37] for you to think about you'll have to
[18:38] manage that internally with your
[18:40] deployments so that's why I'm putting
[18:42] you know okay the GP is really full
[18:44] because a long text uh excuse me long
[18:46] input uh long output the next one short
[18:48] long you know your time to first to them
[18:51] be really fast I don't have much to
[18:52] compute the attention mechanism on but
[18:54] hey I'm generating a ton of tokens
[18:56] that's really really fast so hopefully
[18:58] as you start measuring these types of
[19:00] different query patterns um you'll see
[19:02] different results I just put you know
[19:04] what a random sampling set might
[19:06] actually look like on the GPU because
[19:08] not everyone will send the same length
[19:10] of input and output um so that will
[19:13] it'll be good for you to just sort of
[19:14] visualize and track these statistics
[19:16] more importantly why we're doing that uh
[19:19] internally I'm I'm going to steal the
[19:20] time here Peter uh more importantly why
[19:23] we're doing that or why we're tracking
[19:25] these things is that the whole goal is
[19:27] to build I have a big model my goal is
[19:29] to shrink it as much as I can but to
[19:32] keep it as accurate as possible so the
[19:34] more that I shrink the faster it runs
[19:36] the more GPU memory I have for what
[19:39] tokens all right so that's how you
[19:41] really try to improve your cost this is
[19:43] why I'm I'm sort of proposing to you to
[19:46] build inference engines so what all I'm
[19:48] showing here is a 2d histogram of input
[19:50] sequence length versus output sequence
[19:52] length cuz the question that you'll have
[19:54] to answer is hey how long are my actual
[19:57] prompts someone might say okay here's
[19:58] the max prompt length that you can
[20:00] ingest and the max prompt you can out
[20:03] you know excuse me get on the output and
[20:05] all of The Big Box model providers have
[20:07] to estimate this when they go into
[20:09] costing or providing a service to you
[20:12] right because they have to host all of
[20:13] that Machinery under the hood now that
[20:15] you understand what's happening so we
[20:18] use this to statistically determine what
[20:21] is the max input sequence length and the
[20:23] max output sequence length across all of
[20:25] my users and this would give you a
[20:27] really good indication of um how you can
[20:29] size your engines we use that to
[20:32] actually build more optimized engines in
[20:34] addition um it'll just give you good
[20:36] viewers to maybe uh what you call it
[20:38] scaling out and things like that the
[20:41] next one is time to First token analysis
[20:43] remember time to First token is
[20:45] measuring my performance of the
[20:46] attention mechanism under load so
[20:49] someone might show attention mechanism
[20:50] at one query woohoo show me attention
[20:53] mechanism underload when this thing is
[20:55] fully maxed out 24/7 that's when you
[20:58] really need to start um measuring these
[21:00] types of things so this is something you
[21:01] can look at these are sort of
[21:02] experimental plots um there's a package
[21:04] called gen perf that will be released
[21:07] open source it's out already I have a
[21:09] link to it there this is where you can
[21:10] it'll generate these plots for you but I
[21:13] I'm just showing you what the engineers
[21:15] uh looking at internally to measure the
[21:16] performance of the compute platform next
[21:19] time to completion analysis how long did
[21:21] it take me to go from start to finish
[21:23] across every single request naturally
[21:26] The Wider that box plot you have have to
[21:28] intuitively ask what's happening why did
[21:31] this person's prompt take longer than
[21:33] another so you can investigate either
[21:35] batching issues scheduling issues
[21:37] different things like that I I'll take
[21:39] questions in here why I have to move
[21:41] really fast sorry there okay I'm going
[21:42] to speed up here I to to token latency
[21:45] Peter how much time I got oh you're fine
[21:48] definely have time for questions okay
[21:49] cool I'm going to Ste I'm definitely so
[21:51] sorry I just want to I realize I may
[21:53] have gone a little too fast so forgive
[21:55] me for that got five minutes cool all
[21:57] right time uh token to token latency so
[22:00] that is I'm generating token so I'm
[22:02] looking at that spacing versus token
[22:04] position so the longer a sequence gets
[22:07] remember my memory grows so typically
[22:10] that means that system is under more
[22:12] load it has more throttling that might
[22:14] happen under high load of requests so if
[22:17] I see a large variation in token to
[22:20] token latency as the sequence gets
[22:23] longer when I'm generating that means
[22:24] I'm not very performant right so we look
[22:26] at that to see I try to make make sure
[22:28] that that's constant no matter how much
[22:31] tokens I'm generating that means I'm I'm
[22:33] really proficient okay uh last one would
[22:36] be time to First token versus number of
[22:39] input tokens so time to First token
[22:41] remember is Computing the attention
[22:43] mechanism okay versus number of input
[22:45] tokens so if I have a bigger prompt my
[22:48] attentions will take longer but I if
[22:51] that plot goes up like from your
[22:53] perspective it goes up like this in
[22:54] terms of sequence length that's not
[22:56] really good performance we really look
[22:58] at that slope and we try to get that
[22:59] slope almost you know as as low as
[23:02] possible so if you send me this long
[23:04] sequence I can get that thing done
[23:06] really fast okay okay uh in terms of
[23:09] software uh you'll see this thing called
[23:11] trt llm uh Triton is an open source
[23:13] inference server so you can deploy
[23:15] models on CPU on GPU computer vision
[23:18] rexus python pytorch tensorflow it's uh
[23:22] it'll host all of the different types of
[23:23] models so there's one way that your
[23:25] deployment team deploys all your data
[23:27] scientists are happy because they don't
[23:28] have to do conversion you're happy as a
[23:30] deployment person because you don't have
[23:31] to manage a torch serve versus TF serve
[23:34] and uh flask and all of it is done
[23:36] through one it's written in C++
[23:38] blazingly fast and then the other thing
[23:40] you'll see Nvidia you'll see a lot more
[23:42] coming out of Nvidia is NVIDIA inference
[23:44] micros service cuz building these
[23:45] engines getting them deployed optimiz
[23:47] the scale it's not easy so we've sort of
[23:49] made that easy for you as an Enterprise
[23:51] offering but you guys can try it out uh
[23:53] for free okay so trtm let me just give
[23:56] you high L lots of stuff on the slide
[23:58] but the main thing I want you to walk
[23:59] away with um uh is this is the model
[24:02] compilation package for llms on Nvidia
[24:05] gpus this if you want to get best
[24:07] performance from Nvidia gpus please make
[24:09] sure you use trt llm um and naturally uh
[24:13] once we're investing more in name you'll
[24:14] see some more things come out so you'll
[24:15] see performances on a100 and h100 really
[24:19] focus on fp8 gpus so fp8 will be Hopper
[24:22] and AD love lace okay so fp8 I'll I'll
[24:26] talk a bit more about that what the
[24:27] advantage there is but mainly is if I go
[24:30] from fp16 fp8 is this half my memory
[24:35] almost the same accuracy and so we
[24:36] measure the accuracy and we publish the
[24:38] accuracy so now I have this much more
[24:40] space for tokens but more importantly
[24:42] this model is that much faster okay so I
[24:44] want you to understand where the sort of
[24:46] industry is going this is why Hopper the
[24:48] will ate hopper for breakfast and lunch
[24:50] and dinner because of fp8 it gave folks
[24:53] that cost um benefit to do this thing a
[24:57] lot faster okay um in Flight batching it
[24:59] just means I don't have to wait for all
[25:01] the requests to finish to start a new
[25:03] request the moment your request finishes
[25:05] I can inject a new request While others
[25:08] are going okay tons of features here I
[25:11] put the features um so some wants to to
[25:14] focus on are quantize KV cach so I can
[25:17] actually represent my KV cach in
[25:19] different uh excuse me Precision so that
[25:21] means I'm actively shrinking that memory
[25:23] making it more performant um you have
[25:25] phkv cach that's just you managing uh
[25:28] your gpus is a lot better in terms of
[25:29] all of that memory so there are tons of
[25:31] things you can do tenser parallelism the
[25:33] thing to remember about tenser
[25:35] parallelism if you want to increase
[25:36] latency you use tza parallelism split
[25:39] the model up across multiple gpus that's
[25:41] typically done within a node I repeat
[25:45] that that's typically done within a node
[25:47] you don't like to do tza parallelism
[25:49] across a node you'll see pipeline
[25:51] parallelism go across a pipeline
[25:53] parallelism is more sequential so I
[25:55] process this chunk so in a multi- node
[25:58] model like huge models this box will
[26:01] finish and pass off to the next box but
[26:03] most folks will typically just work most
[26:05] models will work within a single node
[26:07] like um nvidia's 340b model that they
[26:10] just released it was designed to do
[26:12] inference on a single h100 node but
[26:15] that's an fb8 okay so those are some of
[26:17] the things in terms of models that you
[26:19] have access to um we optimize those
[26:22] models and we give you a lot of scripts
[26:24] for you can go do that on your own or
[26:25] you can sort of take our software um and
[26:27] take a easy path you either way we
[26:29] support you so here are some of the
[26:31] models that are there all of the llamas
[26:32] mistol mixs we work with all those teams
[26:35] behind the scenes so typically before
[26:37] any foundation model comes out we we
[26:39] work with those teams to to get them
[26:41] deployed okay what does it mean for tenz
[26:44] RT so you might have seen tenz RT before
[26:47] which was a deep learning compilation
[26:48] package for NVIDIA gpus lots of folks in
[26:51] computer vision etc etc I've used that
[26:53] we took the best practices from there
[26:55] and added all of the extra things that
[26:57] need to happen in the llm inference Loop
[27:00] so that's what trt llm is really about
[27:03] um so mainly focus on llm inference uh
[27:06] here's a good visual an engine that's
[27:09] built to a specific GPU cannot be moved
[27:11] to another GPU so you always have to
[27:13] compile to that GPU that's why it's that
[27:15] performant because we really leverage um
[27:18] all of the the actual Hardware on that
[27:21] system to rewrite the algorithm rewrite
[27:23] that model to that specific piece of
[27:25] Hardware okay um trt LM and Triton so
[27:29] trtm will give me an inference engine I
[27:31] need something to host that inference
[27:33] engine and accept requests batching etc
[27:35] etc so we have Triton Triton works very
[27:38] simply it's literally a folder where you
[27:40] specify it it works on tenser in and
[27:42] tens are out so it will tell you what
[27:45] are my inputs coming in and out and then
[27:47] it'll basically understand how to
[27:48] interpret that file or you can host any
[27:51] other different models that's one that's
[27:52] a thing I do a lot with folks just two
[27:55] more slides this is where the future of
[27:56] inference is going so a lot of folks do
[27:59] fp16 in France today um a lot of folks
[28:02] are moving towards fp8 just because hey
[28:05] I know half the model size almost twice
[28:08] the speed more space for tokens it just
[28:11] makes more sense from a cost perspective
[28:13] that's why folks like that and then uh
[28:15] you saw Blackwell was announced that's
[28:17] the major Innovation I get fp4 so that's
[28:19] where things are really going to get
[28:21] interesting I'll end with um Nvidia
[28:24] inference microservice so we've made
[28:25] this thing really easy we've gone and
[28:27] actually found the best configurations
[28:29] for all of these models on each piece of
[28:31] GPU and we're slowly rolling out all of
[28:33] the models cuz it you know it'll just
[28:35] take some time to optimize the world
[28:37] essentially and yeah you can use this to
[28:40] download all the slides I put papers um
[28:42] tons of other things you for you to read
[28:44] so yeah hopefully your intuition has
[28:52] sharpened shall we just conclude with
[28:54] the because there was someone had a
[28:56] question sure yeah I think where was the
[28:57] question
[28:58] yeah oh hang on I'm going to come over
[29:00] and point my mic at
[29:05] you thank you ome hi um sorry my
[29:09] question is actually on the heat map
[29:11] that you shared you mind um walking
[29:13] through the heat map and how to
[29:14] interpret it it was a little small yeah
[29:17] sorry about that yeah so the heat map
[29:19] all I'm looking at is um so when you go
[29:22] to build an engine you build an engine
[29:23] to the max input sequence length and the
[29:26] max output sequence length so we
[29:27] actually change how that Matrix math is
[29:30] happening under the hood based on those
[29:32] settings so you might say all right uh
[29:35] my users are only going to send 4,000
[29:37] tokens but in reality they might have
[29:39] been sending 1,300 over the past week
[29:41] that you measured so now you can stay
[29:43] with statistical certainty that hey the
[29:47] majority of people that were serving um
[29:49] during this time these were their
[29:51] querying pattern so I can rebuild an
[29:53] engine for that period of time what gets
[29:55] super interesting this is a topic I'm
[29:57] very interested in is seasonal engines
[29:59] so during the day you have different
[30:01] querying patterns so you'll scale down
[30:03] you'll scale up and so you might have
[30:05] different engines built for different
[30:07] types of querying patterns based on
[30:09] traffic and stuff like that so hopefully
[30:11] that that may have answered your
[30:13] question yeah but it's just saying you
[30:14] know looking at the bounds of what's the
[30:17] minimum number of tokens that came in
[30:19] the Max uh Min Min out and max out and
[30:22] just looking at that over the entire
[30:24] distribution yes it
[30:28] oh yeah right when it comes to those uh
[30:31] infant strategies you talk about like
[30:32] Lio and lyso um how do you what kind of
[30:35] strategies do you have to manage like
[30:36] which ones are used at like because
[30:39] obviously each session is going to be
[30:41] pretty generic you don't know which one
[30:42] to use at first correct um do you split
[30:44] those between gpus or do you stick with
[30:46] one and do it switch between so
[30:47] typically we'll we'll go to you try to
[30:49] find what's one configuration that will
[30:52] manage the the plora of types of
[30:55] requests that you have coming in so we
[30:56] we're typically at a a one engine per
[31:00] all the different querying types and I
[31:01] think you'll start seeing I'm giving you
[31:03] a little bit of future ways to think
[31:05] about it on the devop side because
[31:07] that's something you'll have to test
[31:09] right if I look at this quering pattern
[31:11] that came into my system with this
[31:12] engine if I switch the engine does it
[31:15] still satisfy the querying pattern and
[31:17] how much cost does it save how much
[31:18] faster is it so that's more of a an
[31:21] engineering exercise that you'll have to
[31:22] deploy sorry I I didn't have
[31:24] a yeah yeah so I I just I'm very
[31:27] interested in the seasonal side just
[31:28] because okay querying patterns will
[31:31] change um especially when agents come
[31:32] it'll just be that's going to get super
[31:35] interesting when agents are just
[31:36] throwing stuff yes
[31:57] yeah so so what people do in order to
[32:00] scale the attention mechanism is here's
[32:03] another interesting fact that uh why
[32:05] folks don't train huge context models
[32:07] because it's actually now you've seen
[32:09] the bigger my uh prompt the more memory
[32:12] I need so imagine what that does to a
[32:14] huge I don't know 10,000 100,000 GPU
[32:18] deployment it might make it a million
[32:19] gpus just to do that context thing so
[32:21] people will train to a small context
[32:23] length and then interpolate in that
[32:26] value to to give you that length of
[32:28] context length and then you're sort of
[32:30] bound to what attention mechanism you
[32:31] were using designed there there's things
[32:34] like flash attention that will just do
[32:36] everything in the L1 cache really really
[32:38] fast so it depends on the speed of some
[32:40] of the different it also depends on the
[32:42] GPU as well so that's why um if you look
[32:45] at Blackwell that was announced by by
[32:47] Jensen they literally connected I think
[32:49] 72 different gpus on one EnV link so NV
[32:53] link connects gpus together that's how
[32:55] we can move data insanely fast so now
[32:57] we' connected like 72 gpus on one that's
[33:01] that's just to show you um like mixture
[33:02] of experts trying to computer attenion
[33:05] across all of these different things but
[33:06] that's a actually a really good
[33:10] question no I I don't necessarily think
[33:12] so like the entire industry is you know
[33:15] going after that problem that's why
[33:16] everybody wants to maybe see something
[33:18] other than attention and ah you know
[33:21] there's so much excitement there yeah
[33:22] unfortunately have to call time on but
[33:24] that's been fantastic thank you Mo um
[33:29] [Applause]
[33:29] [Music]
