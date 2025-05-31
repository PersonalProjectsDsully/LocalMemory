---
type: youtube
title: Lessons from building GenAI based applications — Juan Peredo
author: Channel Video
video_id: YYcNm2RexnY
video_url: https://www.youtube.com/watch?v=YYcNm2RexnY
thumbnail_url: https://img.youtube.com/vi/YYcNm2RexnY/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning
tags: ['AI Models', 'Chatbot Development', 'Model Deployment', 'Python', 'Cloud Computing', 'Prompt Engineering', 'Guardrails', 'Machine Learning', 'AI Ethics', 'Software Architecture']
entities: ['Model', 'Sky Pilot', 'Python', 'Prompt Engineering', 'Guardrails', 'LLM', 'Chatbot', 'Bugy Face Transport Per', 'Cloud Hosting', 'AI Ethics']
concepts: ['Prompt Engineering', 'Guardrails', 'Model Deployment', 'Chatbot Development', 'Validation Techniques', 'Cost Optimization', 'Machine Learning Models', 'Cloud Hosting', 'Content Moderation', 'AI Ethics']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic knowledge of Python programming', 'Familiarity with AI/ML concepts', 'Understanding of cloud computing fundamentals']
related_topics: ['Artificial Intelligence', 'Machine Learning Deployment', 'Software Development Practices', 'Cloud Infrastructure Management', 'Natural Language Processing', 'AI Ethics and Governance', 'Model Monitoring', 'DevOps for AI']
authority_signals: ["I've used it to host a lot on my models", 'this that I have on the screen um on the right is actually something that happened to me', 'you need to be very precise in those additional instructions']
confidence_score: 0.8
---

# Lessons from building GenAI based applications — Juan Peredo

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=YYcNm2RexnY)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: genai, ai-development, machine-learning, application-development, llm, model-integration, ai-challenges  

## Summary

# Summary of "Lessons from Building GenAI-Based Applications" by Juan Peredo

## Overview  
Juan Peredo, an IT professional with 15+ years of experience, shares insights from his work over the past year and a half building generative AI (GenAI) applications. He highlights the evolving role of AI in software development, the complexities of integrating AI into applications, and practical strategies for deployment, validation, and cost management.

---

## Key Takeaways  

### 1. **AI in Coding: Benefits and Limitations**  
- **Pros**: AI tools like LLMs simplify tasks (e.g., building chatbots in hours) and accelerate development.  
- **Cons**: AI-generated code or responses may lack accuracy (e.g., an LLM incorrectly answering "3 * 3 = 33").  

### 2. **Complexity of AI Integration**  
- **Model Selection**: Choosing the right model (e.g., fine-tuning, prompt engineering) is critical for accuracy.  
- **Hallucinations**: AI may generate incorrect or fabricated information, requiring validation techniques.  
- **Guardrails**: Using a secondary LLM as a classifier to filter unsafe or malicious queries.  

### 3. **Hosting Considerations**  
- **On-Premises vs. Cloud**:  
  - **On-Prem**: Tools like Ollama or local libraries (e.g., `transformers`) allow lightweight deployment but require powerful hardware.  
  - **Cloud**: Platforms like AWS, Azure, or Google Cloud, with tools like **Model** (for Python-based deployments) and **Sky Pilot** (to optimize costs across clouds).  
- **Cost Management**: Balancing GPU availability, cloud provider costs, and tools like Sky Pilot for cluster optimization.  

### 4. **Validation and Moderation**  
- **Prompt Engineering**: Adding precise instructions to prompts to guide LLMs (though they may still ignore them).  
- **Content Moderation**: Ensuring chatbots provide accurate, safe, and contextually relevant responses.  

---

## Practical Tools and Techniques  
- **Model**: Simplifies cloud deployment of Python-based AI models via decorators and CLI.  
- **Sky Pilot**: Reduces costs by distributing workloads across multiple clouds.  
- **Local Testing**: Libraries like `transformers` enable quick experimentation without cloud infrastructure.  

---

## Challenges and Lessons  
- **Validation is Hard**: Even simple chatbots require rigorous testing to avoid errors.  
- **AI is Not a Silver Bullet**: While powerful, AI demands careful design, monitoring, and human oversight.  
- **Adaptability**: Staying updated with evolving tools (e.g., Model, Sky Pilot) and cloud trends is essential.  

Juan’s talk underscores the importance of balancing AI’s potential with practical strategies for reliability, cost, and deployment.

## Full Transcript

[00:00] hello and welcome today we're going to
[00:02] talk about the lessons I've learned from
[00:05] building gen application over the last
[00:07] year and a
[00:09] half my name is Juan pero and I'll be
[00:12] your guide in this journey I'm a Founder
[00:15] architect consultant developer and
[00:17] everything in between uh and I have over
[00:19] 15 years experience uh in the IT
[00:24] industry and one of the first things uh
[00:27] everyone hears when they're talking
[00:29] about AI is about how much faster
[00:34] developers can code thanks to AI you can
[00:37] hear this and you've heard this before I
[00:39] can guarantee that nowadays you can just
[00:41] take a prompt put it into an llm and you
[00:46] will and the llm will code your website
[00:49] for you in about a minute or so and we
[00:53] all know that that's not true right um
[00:56] it'll give you some code and it'll get
[00:57] you going but it won't build everything
[00:59] for you
[01:02] um but there's a lot of tools that have
[01:04] been created to help you with this like
[01:06] some of the ones that I have listed here
[01:07] like codium and cursor that interact
[01:11] with your ID or an ID by all by
[01:13] themselves um that help you uh build
[01:17] your
[01:18] applications you don't even have to use
[01:20] those those tools right you could just
[01:21] take your code paste it into an llm uh
[01:24] and ask a
[01:25] question right and there's some really
[01:28] good ones out there
[01:30] um but it all depends on what
[01:32] application you're trying to build at if
[01:33] all you're doing is create a boiler
[01:35] plate um
[01:37] for yet another uh website then any cod
[01:42] in LM will work just fine um if you're
[01:45] doing some more something more complex
[01:47] or if it's something that's new or just
[01:49] came out like uh I don't know SV 5 for
[01:52] example um then you want a be here LM
[01:56] something like uh dipic uh V3
[02:00] or
[02:01] Cloud right and and these tools will
[02:05] definitely help you um build faster uh
[02:10] however they
[02:11] also uh add complexity to your
[02:14] applications once you're trying to
[02:15] integrate AI to your application to
[02:17] actually interact with your
[02:19] user like here in the left hand side we
[02:23] still see that in your typical uh
[02:26] application that we've been building
[02:28] till a year ago or two years ago
[02:30] we were building front ends backends um
[02:33] infrastructure SC all the stuff that we
[02:35] normally build but the moment you add AI
[02:39] to your application you all you have to
[02:41] start worrying about all the stuff
[02:43] that's in Gray in the diagram on the
[02:46] right so you have to start wondering
[02:48] about what model you're going to use are
[02:51] you going to fine tune it are you going
[02:52] to
[02:54] um um you do some Pro engineering or you
[02:57] try going to try to use rag to uh get
[03:01] the correct answer to your qu to to your
[03:03] questions and to the user questions how
[03:06] you going to prevent it from
[03:07] hallucinating because we all know that
[03:10] uh llms are so bent on answering your
[03:13] questions that sometimes they'll just
[03:15] make up answers uh and you need to a
[03:18] wait to figure out um whether the answer
[03:21] that you're getting is right or not and
[03:23] so how do you prevent that that's
[03:24] something you don't have to worry about
[03:26] a year and a half ago um also you have
[03:30] to figure out um how often you're going
[03:33] to have to um replace that model because
[03:37] we all know that there's models that are
[03:39] coming out every other week and they're
[03:41] all more powerful beefier but they they
[03:45] will not all work with your use case
[03:47] it's a one thing that they really great
[03:49] at certain benchmarks but that doesn't
[03:51] mean they're going to work uh with the
[03:53] rest of the application that you built
[03:55] so you have to constantly be evaluating
[03:57] not only the model that you have already
[03:59] running
[04:00] but also the molds are coming out that
[04:02] may uh help you build a better
[04:06] application and you also have to start
[04:08] figuring out how you're going to host
[04:10] these things now yeah because that's
[04:12] beyond hosting your store application
[04:14] right all of a sudden you don't have to
[04:16] worry just about CPU and memory all you
[04:18] have to worry about gpus so well right
[04:21] where are you going to host this this is
[04:22] going to be in the cloud this you be um
[04:25] on Prem all this information and all
[04:28] this stuff in Gray is new new to uh and
[04:32] is specific to AI based
[04:38] applications speaking of Hosting where
[04:41] to host this model is important right
[04:44] how you going to host it are you going
[04:45] to host it in on Prem or are you going
[04:48] to host it on your machine while you're
[04:50] um doing some exploration you have to
[04:52] make these decisions right so if you're
[04:54] going to host it locally you can host it
[04:56] in something like ol Ola will allow you
[04:58] to um download a bunch of uh models into
[05:03] your machine where you can play with
[05:04] those models for free interact with them
[05:07] and see if they're going to work for you
[05:09] and there's a host of other Solutions as
[05:11] well is the one I've been using uh it's
[05:14] pretty good just you just have to make
[05:16] sure you have a machine that's beefy
[05:18] enough uh for the mod that you're trying
[05:20] to
[05:21] run or you can even use this and all
[05:24] these other tools uh to host
[05:26] things um on Prime
[05:31] right but if you're going to host it in
[05:33] the cloud now you have to start thinking
[05:35] not only about what cloud but also about
[05:38] cost of your gpus and is there enough
[05:41] gpus to go
[05:43] around uh and in general like everything
[05:45] else you still also have to worry about
[05:47] cost and you have the the typical
[05:51] players right you have your Google Cloud
[05:52] your AWS your Azure etc etc there's also
[05:57] a new set of players that have come up
[06:00] uh that
[06:01] are meant to simplify the deployment of
[06:06] your application in the cloud and that's
[06:08] where tools like model and skyp pilot
[06:12] um have come
[06:15] up um and if you're using python which a
[06:18] lot of us are using python for uh
[06:20] interacting with your with our models U
[06:23] model is a great choice mod allows you
[06:26] to take your python code add some um
[06:31] some um decorators to your
[06:35] code and use their CLI to deploy uh to
[06:39] model and model will take care of
[06:41] building your your containers and
[06:43] pushing them to the
[06:45] cloud um it's really simple I've used it
[06:49] to to host a lot on my
[06:51] models um and there's also Sky pilot Sky
[06:55] pilot is great to minimize your cost as
[06:58] they will spread the your clusters and
[07:02] your containers into multiple uh clouds
[07:07] in order to minimize your
[07:09] cost right and you can configure it
[07:12] which which class you Cloud you want Sky
[07:15] pilot to to use for hosting your
[07:19] application um and at the end of the day
[07:22] right if you just want to play with with
[07:24] s in your machine you could also use a a
[07:27] simple Library like the bugy face
[07:29] transport per that you just can run um
[07:31] locally on your machine without any any
[07:33] any other tools
[07:35] um but at the end of the day once again
[07:38] how you host these models is very
[07:43] important um now let's think about
[07:49] um the fact that we're not in 20 2023
[07:52] anymore right building a chat B power di
[07:55] is very simple you can build it in an
[07:58] hour or two if that much all right um
[08:02] there's a lot of Frameworks there that
[08:03] will help you build this for
[08:05] you
[08:07] um
[08:09] however even though building the chatbot
[08:11] is easy making sure that that chatbot
[08:13] gives you the correct answers is really
[08:15] hard like for example this that I have
[08:19] on the screen um on the right is
[08:21] actually something that happened to me I
[08:23] put in one llm uh a few months ago now
[08:27] what is three * three and the answer
[08:30] that they gave me was 33 that's
[08:32] obviously not right um so while making
[08:36] the chat easy validating and moderating
[08:39] the chatbot content and making sure that
[08:41] it's giving you the correct answer to
[08:42] your user is really really
[08:47] hard so what can we do to ensure that we
[08:51] are providing the right answer to your
[08:52] to our users right well there's a number
[08:54] of techniques right you can do prompt
[08:56] engineering which is basically you take
[08:58] the question of of the user you put
[09:01] additional uh details into the CR that
[09:04] you pass into the um
[09:09] LM however you need to be very precise
[09:11] in those additional in those additional
[09:15] instructions so that the LM can follow
[09:18] them properly and even then the LM may
[09:21] choose to ignore them and at that point
[09:23] what you do right you get you get the
[09:26] wrong you can also put
[09:29] and guardrail is basically you take a
[09:31] secondary llm and put it to run in front
[09:34] or before your main
[09:36] llm and this secondary llm is basically
[09:40] a classifier that will
[09:42] classify the question that they ask that
[09:44] the person is
[09:46] answering um as a safe question or as a
[09:50] bad question and when I say bad question
[09:52] it could be and something that is trying
[09:55] to go around uh uh or asking for
[10:00] criminal activities or may be asking
[10:02] about um things that are not not what
[10:06] you'd expect somebody to to answer the
[10:10] um in general right and at that point
[10:13] the the the secondary LM is classifying
[10:16] that your questions and it also could be
[10:18] the the answers of your own LM as either
[10:21] good or
[10:22] bad however you know adding this
[10:24] secondary LM adds
[10:27] latency because you're making a
[10:29] secondary call right and it also has
[10:30] additional cost and like anything else
[10:34] with llms uh it may or may not be
[10:39] right the next thing you could do is you
[10:41] could have retrieval augmented
[10:43] generation or rag which is basically you
[10:45] take a lot of information that you have
[10:47] in your
[10:48] company you break it into small chunks
[10:51] of information so you can think of it
[10:53] of as let's say you take a document and
[10:56] you break it into paragraphs although it
[10:57] could be anything just think of it chunk
[10:59] as a paragraph for now you break it into
[11:02] chunks and you start it in the vector
[11:04] database and then when somebody ask a
[11:06] question you
[11:08] take um you do a similar similarity
[11:11] search on your uh Vector database pull
[11:15] information and provide that information
[11:17] to your U llm and tell the llm here's
[11:21] the information you can use to answer
[11:22] that question and what that sounds
[11:25] really nice and good is really dependent
[11:28] on the type of information you've
[11:30] provided in your vector database so if
[11:33] you put all information that's no longer
[11:36] relevant well guess what what LM is
[11:38] going to reply to you is with
[11:39] information that's no longer
[11:41] relevant so data is extremely important
[11:45] in this
[11:47] case um other thing you can do is you
[11:50] can do file
[11:51] tuning right and F tuning is basically
[11:53] you do additional training uh to an
[11:57] llm this is more expensive than the
[11:59] other the techniques that we're talking
[12:01] about and it takes long longer period of
[12:04] time and doesn't really uh guarantee
[12:08] that you're going to get good results in
[12:10] fact depending on the type of
[12:12] information you're putting uh into your
[12:14] F tuning we could actually degrade the
[12:17] llm quality
[12:19] responses uh because you may actually
[12:22] forget some of the information it
[12:23] already had or it may get confused
[12:25] between the new information you're
[12:26] passing and the information that it
[12:28] already had
[12:31] so at the end of the day there's no no
[12:33] no technique that will guarantee that
[12:35] the answer of your chat B is going to be
[12:38] good
[12:40] but uh using many of these techniques
[12:44] will help you get there or get you a
[12:47] long
[12:50] way another thing that you should do is
[12:52] you should evaluate and uh your models
[12:56] and your
[12:57] application at each step of the
[13:00] development life
[13:02] cycle for example when you are starting
[13:05] to explore which LMS to use in your in
[13:08] your application or your idea of an
[13:11] application you could use something like
[13:13] AMA and we talked a little bit about
[13:16] before it will let you run hundreds of
[13:19] llms locally on your
[13:21] machine um once you
[13:24] are interested on one or another you can
[13:28] start using in your application or if
[13:31] you want to play with thousands of uh
[13:34] open source models you can go to huging
[13:37] face and there you can build some
[13:40] hugging face space spaces um you can see
[13:43] the spaces that other people have built
[13:45] and this is basically a lot of code that
[13:48] interacts with llms um and that you can
[13:51] freely use and review um to see whether
[13:53] you're interested to build something
[13:55] similar or use the the LMS that they're
[13:57] using
[14:01] now if you want to interact with other
[14:03] models including um some of the close
[14:06] models you can go to open router open
[14:09] router will basically take your prompt
[14:12] and it will run it against a number of
[14:14] models or a model of you're choosing and
[14:17] one of the things that makes open rer
[14:18] really cool is that it will um take your
[14:23] prompt and let's say you want to run
[14:25] that prompt against Lama three it will
[14:28] look at
[14:30] the
[14:31] providers that are actually offering
[14:34] Lama 3 as as an API and they will run it
[14:37] until the one that's against the one
[14:38] that's cheaper which is really cool and
[14:41] it's a great way to save
[14:43] money um I use it every day and I put
[14:47] like $50 about six months ago and I
[14:49] still have about 40 bucks left and I use
[14:52] as I say I use it every day so it's a
[14:54] great way um to interact with models and
[14:58] uh see which one I want to
[15:01] use uh obviously if you're going to do
[15:03] so open router production there are
[15:06] there are a number of um safeguards that
[15:09] you you may want to look into you know
[15:12] you don't want just open R just running
[15:15] into a random llm provider without you
[15:18] knowing which one it is um but for
[15:20] testing it's a great
[15:23] thing and finally uh the last tool I
[15:26] have here listed is lsmith which is
[15:28] created by the creators of uh L chain
[15:31] which is a very popular open-source
[15:35] um framework to interact with
[15:38] llms but LMI one of the great things
[15:41] about it is that it lets you constantly
[15:44] evaluate your models so it will
[15:48] uh it can help you record uh a number of
[15:52] Bruns that you have with your llms you
[15:54] can compare over time um how your LMS
[15:58] have been performed in um is a really
[16:00] really cool platform um just to keep
[16:03] track of what your application and your
[16:05] models are
[16:07] doing
[16:08] [Music]
[16:09] um so yeah evaluation you you really
[16:12] should be doing this at each step of the
[16:15] way another thing that it's very
[16:18] important is externalizing your
[16:21] prompts and I know that for all of us
[16:24] it's really easy to just take a prompt
[16:27] put it in the code our code it in there
[16:29] and move
[16:31] on um but if you do that you're short
[16:33] changing yourself externalizing your
[16:35] prompt uh in tools like uh repositories
[16:40] like like Lang chain Hub which I have
[16:43] here a screenshot on the left uh will
[16:46] allow you
[16:47] to uh share those fronts with experts so
[16:52] if you are build an application that has
[16:54] to do with education you could you could
[16:55] reach out to to an education expert that
[16:58] has never coded in their lives and you
[17:01] can have them this log to to the hub
[17:05] play with with the proms run the llms
[17:08] see the output that they're getting from
[17:10] the
[17:11] llms um and then when they're ready and
[17:13] they're happy with that they're getting
[17:14] the correct uh prompts all they have to
[17:17] do is just uh commit those prompts and
[17:19] that will flow directly into your
[17:23] application it's really cool another not
[17:26] thing that will that uh this will help
[17:29] with is future proofing we all know that
[17:31] models are coming out every other week
[17:34] there a new model and that's better than
[17:35] the previous
[17:37] one um and unfortunately right even
[17:41] let's say if you're using a Lama model
[17:43] and the next Lama model comes out uh
[17:46] your prodct may not work prop properly
[17:48] with a new version you may not get the
[17:50] the same results so by allowing you to
[17:53] easily access the prompts and modify
[17:55] them and test them against something new
[17:59] then you you are basically future
[18:01] proofing and making your life easier in
[18:02] the future and that in turn leads to
[18:05] faster
[18:07] development
[18:09] so bottom line promp should never be
[18:11] encoded in your code
[18:16] list I'll let's talk a little bit about
[18:18] agents agent
[18:19] agents
[18:21] are and I expect them to be in this year
[18:25] one of the best uh additions to the
[18:28] world of other
[18:30] because agents are basically allowing
[18:32] and the LMS to break out of the chatbot
[18:35] and actually interact with the real
[18:38] world so you can have an agent for
[18:41] example um that uh allows you
[18:46] to for example you have a book you want
[18:49] to uh create the the audio for it and
[18:53] you want to translate it into multiple
[18:56] languages that's something that you can
[18:58] do you can have an output out of that
[19:00] those
[19:01] things all right so agents will allow us
[19:04] to interact with the real world all
[19:06] these llms that have been confined to
[19:08] just chatting all of sudden will have a
[19:10] real impact in the
[19:12] world um and we're still not there we're
[19:15] still working on it but it's a a really
[19:19] exciting
[19:21] uh exciting uh set of applications that
[19:24] will be coming out
[19:27] soon and here I have a couple of U
[19:30] drawings
[19:32] and of what an agent looks like and the
[19:35] one on the
[19:37] left that's that has four nodes so it
[19:40] has start nodes assistant tools and it's
[19:42] really really
[19:44] powerful right because basically what
[19:47] you're doing is
[19:48] you're when somebody gives you a
[19:51] question you pass it to the assistant
[19:52] and the system basically has an llm
[19:55] embedded and that llm will an the
[19:59] question and then we start calling
[20:02] tools and tools are this fancy name for
[20:05] functions it will start calling
[20:06] functions um until it gets to the answer
[20:09] that it that it needs uh to answer the
[20:12] question of the end user so for example
[20:15] it could be that the end user sends a
[20:19] the text of a book to the assistant and
[20:21] it tells it to translate it and uh
[20:24] create the audio and then the assistant
[20:27] will call the tool to create audio then
[20:29] it will call the Tool uh to the
[20:30] translation and then it will
[20:33] end right and the assistant is making
[20:36] those decisions all by itself which is a
[20:38] a really really powerful um
[20:44] concept
[20:46] um and while it's really cool that those
[20:49] agents can make those decisions without
[20:50] you actually having to hard code all
[20:52] those
[20:53] paths um they do have his disadvantages
[20:57] right and one of the big ones is is that
[21:00] llms have a lot of latency you know
[21:02] calling one of those those llms takes
[21:05] several
[21:06] seconds right so all of a sudden if you
[21:10] have an agent that is integrating with
[21:13] four or five llms and each one of them
[21:17] takes let's say three seconds to run
[21:21] then all of a sudden you
[21:23] have uh a process that takes 12 15
[21:26] seconds right and we know that our users
[21:30] nowadays are used to running things on
[21:34] the web and take those things taking
[21:37] only milliseconds right and if they have
[21:40] to wait for a second or two people are
[21:41] leaving our sites and going to our
[21:44] competition which is not the best uh
[21:47] result
[21:49] um so we should take advantage of of uh
[21:53] this platforms that have been built like
[21:55] Lan chain Lama index L flow there
[21:57] there's many of them
[21:59] right that allows to do things like
[22:01] concr calls and branching
[22:04] uh in these agents right so like for
[22:08] example I have here the on the left
[22:11] diagram of an agent that's actually
[22:13] calling uh a couple of things in in
[22:16] parallel right so it could be once again
[22:19] this could be um the user passing uh a
[22:23] book to node a no a calling uh the audio
[22:28] transl the audio creation and the
[22:30] translation in parallel and then sending
[22:34] the answer back to the user now if each
[22:37] one of these things took um two seconds
[22:40] instead of these things taking eight
[22:42] seconds all of a sudden it takes
[22:44] six right so that's much better
[22:48] right so there's a lot of things and and
[22:52] a lot of things that that need to come
[22:54] to mind when you're building these
[22:56] agents so that you can make them as
[22:57] efficient as possible so that we can
[23:00] still get to the to fulfill the the
[23:03] expectations of our
[23:06] users while taking advantage of the lm's
[23:14] powers um and while I do believe that
[23:17] agents are the future for LMS we really
[23:20] have to be aware of the cost of running
[23:22] this
[23:25] agents um
[23:28] because they can the cost can add up
[23:31] really quickly let's take for example
[23:32] the one I have here with once again is a
[23:34] simple um agent
[23:38] um and we're we're going to assume that
[23:40] this is a call center right this call
[23:43] center takes 3,000 calls a day and each
[23:46] one of those calls requires 15 uh
[23:50] function calls or tool
[23:52] calls and we're going to assume that
[23:54] we're using op ai1 it's a gr model right
[23:58] so we're going to take advantage because
[24:00] it's the one of the big biggest and
[24:03] greatest um and the prices for for open
[24:06] AI or1 is 15 million $15 per million
[24:11] tokens or $60 per million tokens
[24:14] out and if we assume that we're
[24:17] inputting 1500 input tokens and 3,000
[24:20] output tokens meaning uh we're sending a
[24:23] bunch of information into the LM the llm
[24:25] is import is is uh up putting a bunch of
[24:29] information
[24:31] out um let's figure out how much that
[24:34] will cost us right uh because it sounds
[24:37] like very little $15 per one million
[24:40] token right it sounds like it shouldn't
[24:43] be
[24:44] much but once you do the math and the
[24:46] math is at the bottom if you want to
[24:48] take a look at it you won't discuss it
[24:50] here uh but it comes out to
[24:53] $24 uh per call which turns into 9,270
[24:57] per day and
[24:59] which turn is almost $300,000 per
[25:04] month um so if you were expecting to get
[25:07] a very small price tag um well you're
[25:12] going to be to have a little bit of a
[25:15] surprise uh at the end of the day right
[25:18] especially if you're using
[25:22] um provider endpoints for your apis to
[25:25] interact with the llms you have to keep
[25:27] in mind that
[25:29] the cost of running this
[25:31] thing is linear right so each additional
[25:36] user will incur you an additional cost
[25:39] now obviously you have to make sure that
[25:41] you're you're you're pricing your um
[25:44] products accordingly but if you
[25:47] expecting to get very low prices uh very
[25:50] low cost uh you may want to uh do the
[25:56] math um but even if you are
[26:00] renting the gpus right so you don't have
[26:03] to make the API calls gpus are at a
[26:06] premium nowaday so
[26:10] um if we compare the price of a GPU
[26:13] versus the price of a CPU on the cloud
[26:16] we're talking
[26:17] cents versus dollars all right so having
[26:23] an a100 GPU for an hour will cost you
[26:27] like
[26:28] potentially four or five dollars an hour
[26:31] versus you know a traditional ac2
[26:34] instance that could cost you a fraction
[26:37] of a scent or a couple of cents an hour
[26:40] so keep that in
[26:44] mind and the choice of the mobile and
[26:47] and the provider that you're going to
[26:49] use in your in your application is
[26:51] really really important and we can see
[26:54] in the price chart on the left that
[26:57] there's a significant if an Val value
[26:59] difference between the uh left so the
[27:03] first llm in the list and the last one
[27:06] right it's it's over 20 times difference
[27:09] in times of price right
[27:13] um so you have to valuate do you really
[27:16] need the power
[27:19] of a very pricey llm or can you do the
[27:23] same thing with a
[27:25] cheaper llm or two that may not be quite
[27:29] as powerful but they can do the task
[27:32] right it might be from a press
[27:35] perspective it might be much much much
[27:38] more efficient right the other thing
[27:41] that's important like we said is uh
[27:43] outto speed right how fast these these
[27:45] models um can uh respond to
[27:51] questions and that's what we see in the
[27:53] chart on the right the output speed and
[27:57] we can see that cerebras in Gro can run
[28:01] Lama 3.1 70b at over a th uh tokens per
[28:08] second in fact cus is over 2,000 tokens
[28:11] per second while all the way on the
[28:14] right
[28:16] the the providers are running 31 in 29
[28:20] tokens per
[28:21] second right all that translates to
[28:24] latency for your
[28:26] users and usually the SI size of the of
[28:29] the model that you're picking also has a
[28:30] big a big impact right so bigger models
[28:33] will take longer to run smaller models
[28:36] will go
[28:37] faster which one you're using and which
[28:41] one you need to use will have a big
[28:43] impact on your
[28:45] application so at the end of the day
[28:47] right small is beautiful and better for
[28:50] the environment and better for your
[28:56] wet so let's go back to our example
[29:00] right now what happens if we replace
[29:03] open a 01 with Lama 3.37 TV just from a
[29:07] price perspective right you may need to
[29:09] use open a for your use case but what if
[29:11] you didn't right you can just use um
[29:14] Lama
[29:16] 3.3 um well we go from three over $3 per
[29:20] Co to 52 cents per go and we go all from
[29:26] almost $300,000 per month
[29:30] to almost $50,000 per
[29:34] month so once
[29:36] again pick the right model for the use
[29:41] case at the end of the day your wallet
[29:45] and the environment will thank
[29:50] you and the last thing I want to touch
[29:52] on is observability for your
[29:55] agents I can't tell you how hard it is
[29:59] uh to try to figure out what an agent is
[30:01] doing once you get multiple nodes that
[30:04] are interacting with each
[30:06] other uh this is a lot harder in my
[30:09] experience and trying to figure out what
[30:11] a regular application think because a
[30:14] regular application is deterministic it
[30:16] will do a b c
[30:18] d
[30:20] while
[30:22] um a probabilistic
[30:25] model add lots of unknowns to your
[30:29] application so all of a sudden things
[30:31] that were running a 100 times with no
[30:34] issue will start failing out 100
[30:37] 1001st item
[30:40] right and I'll give you an example right
[30:43] I was running an llm and all he had to
[30:47] do was get information about certain a
[30:49] user from the database right so let's
[30:52] say for example get information for user
[30:55] John and this run
[30:59] for the longest time and all started
[31:02] failing and we realized
[31:05] that eventually because because we had
[31:08] the traces um that the user was entering
[31:11] lower cap John instead of just Capal J
[31:14] and the rest of the word right uh and
[31:18] all it took was going back to the prompt
[31:20] which we had externalized luckily and
[31:23] changed the pro to add the sentence uh
[31:26] ignore case and everything started
[31:29] working again but because this one was
[31:32] an agentic application and it was
[31:33] calling
[31:34] multiple
[31:37] mels it would have taken us a very long
[31:39] time to figure out what was going on I
[31:42] mean we could put we could we could have
[31:45] put the debugger and print statements
[31:47] all that and we still have be very very
[31:50] hard so how have observability for
[31:53] there's a lot of tools out there like
[31:55] lsmith that will make this very simple
[32:01] uh and if you don't want to use one of
[32:03] the tools that's available there you can
[32:04] build one or you can build all this but
[32:07] build it because you are going to need
[32:09] it um and in here um we have our agent
[32:13] traces on the
[32:15] left um of the screen we have an agent
[32:18] that's first calling Lama guard then
[32:20] it's calling Lama 3.1 then it's called
[32:23] mistal and that that that gives us an
[32:27] order of everything that that had run in
[32:30] that in that particular call to the
[32:32] agent it has metadata it has the inputs
[32:35] and the outputs all that is crucial
[32:38] right and when he when it throws an
[32:40] error it keeps track of the errors right
[32:43] all the information that was in and out
[32:45] of that llm so you can see exactly what
[32:48] happened and you can see the error uh
[32:50] the trace like we see on the trace on
[32:53] the picture on the
[32:55] right yeah so
[32:58] and like I said building observability
[33:01] for your agents really
[33:05] important and with that any questions
