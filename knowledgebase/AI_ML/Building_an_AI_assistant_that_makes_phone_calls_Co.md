---
type: youtube
title: Building an AI assistant that makes phone calls [Convex Workshop]
author: AI Engineer
video_id: idDnpGqJd80
video_url: https://www.youtube.com/watch?v=idDnpGqJd80
thumbnail_url: https://img.youtube.com/vi/idDnpGqJd80/mqdefault.jpg
date_added: 2025-05-26
category: []
tags: ['AI', 'voice assistant', 'API integration', 'real-time transcription', 'NLP', 'cloud services', 'conversational AI', 'multimodal models']
entities: ['Floyd', 'Open AI', 'GPT', 'Twilio', 'Google Cloud', 'Gemini', 'Chat GPT', 'AI', 'Voice Assistant', 'APIs']
concepts: ['AI integration', 'voice assistant', 'API integration', 'real-time transcription', 'NLP', 'multimodal models', 'conversational AI', 'cloud services', 'real-time audio streaming', 'dialogue management']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Understanding of APIs and cloud services', 'Basic knowledge of AI/ML concepts', 'Familiarity with programming or development frameworks']
related_topics: ['AI voice assistants', 'API integration', 'NLP applications', 'real-time audio processing', 'multimodal AI systems', 'cloud-based conversational agents']
authority_signals: ['"I\'m super impressed by the technology that we access to today"', '"I would experiment with and see if I could make it even faster"']
confidence_score: 0.8
---

# Building an AI assistant that makes phone calls [Convex Workshop]

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=idDnpGqJd80)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai assistant, speech to text, api integration, conversational ai, real time, machine learning, telephony  

## Summary

# Summary of "Building an AI Assistant That Makes Phone Calls [Convex Workshop]"

## Overview  
Tom Redmond from Convex presents a framework for building a real-time AI assistant, **Floyd**, capable of making phone calls by integrating multiple APIs (Google Cloud, Twilio, OpenAI, and Convex). The assistant learns from user data to perform tasks like contacting schools, mechanics, or vendors, while maintaining privacy and flexibility.

---

## Key Points  
1. **Core Technologies**  
   - **Google Cloud**: For real-time speech-to-text transcription.  
   - **Twilio**: To handle phone call connections and voice streaming.  
   - **OpenAI (ChatGPT)**: For conversational logic and task execution.  
   - **Convex**: A database to store user context and request history.  

2. **Workflow**  
   - **User Input**: The assistant receives a request (e.g., "Notify my kid’s school they’re late").  
   - **Context Building**: Floyd gathers user data (e.g., school name, location, previous interactions).  
   - **Task Execution**: OpenAI generates a script for the call, Twilio handles the dialing, and Google Cloud transcribes the conversation.  
   - **Feedback Loop**: Real-time audio is streamed back to OpenAI to adapt the conversation dynamically.  

3. **User Privacy & Flexibility**  
   - Users can control how much data is shared (e.g., car details, school info).  
   - Floyd can prompt users for missing information or send texts if a phone number isn’t available.  

4. **Architecture**  
   - **Request Object**: Stores the user’s query, context, and progress.  
   - **Modular Design**: Allows swapping services (e.g., future multimodal models like Gemini).  

5. **Challenges & Opportunities**  
   - Real-time processing is feasible today due to advancements in AI and cloud infrastructure.  
   - Potential for optimization (e.g., faster response times, multimodal integration).  

---

## Important Quotes  
- *"The fact that this works and isn't painfully slow just boggles my mind."*  
- *"We're designing it in such a way that we should be able to swap in and out different services."*  

---

## Actionable Items  
1. **Set Up Required Accounts**:  
   - Google Cloud (Speech-to-Text).  
   - Twilio (Phone call handling).  
   - OpenAI (ChatGPT integration).  
   - Convex (Database for user context).  

2. **Experiment with the Code**:  
   - Integrate APIs to build a prototype.  
   - Test real-time transcription and voice streaming.  

3. **Explore Multimodal Enhancements**:  
   - Investigate tools like Gemini for audio-based interactions to skip transcription steps.  

4. **Prioritize User Privacy**:  
   - Design systems to allow users to control data sharing and prompt for missing information.  

--- 

This framework highlights the power of combining existing tools to create context-aware AI assistants, with a focus on scalability, privacy, and real-time performance.

## Full Transcript

[00:00] [Music]
[00:13] well hello everybody thank you for
[00:15] braving the early morning uh 8 A.M is
[00:19] rough for the best of us so I really do
[00:22] appreciate the crawling out of bed and
[00:24] coming to uh check out this talk my name
[00:28] is Tom Redmond
[00:30] I am the head of DX at a company called
[00:33] convex we're
[00:35] building a platform that people are able
[00:38] to build their companies on from day one
[00:42] to year two hopefully year 10 and year
[00:45] 20 and
[00:47] Beyond Today I wanted to walk through
[00:51] this
[00:51] idea that I've had for a long time about
[00:55] building a better AI assistant it came
[00:57] to me a little while ago um
[01:01] after trying a number of AI assistants
[01:04] most of which can pretty much set
[01:06] calendar events and reminders and timers
[01:09] and things like that and I thought to
[01:11] myself what does a real personal
[01:15] assistant do for
[01:17] people right A lot of the time short of
[01:21] collecting laundry and doing like
[01:23] physical
[01:24] things they're on the phone and they're
[01:27] on email and so I realized I feel like
[01:30] there's enough technology out there
[01:31] these days that we could actually string
[01:34] together a number of platforms such that
[01:37] you could have an AI assistant that
[01:39] knows about you it has contexts on you
[01:42] and your life and who you are and would
[01:45] be able to manage a
[01:47] conversation in a non creepy way with
[01:51] another human
[01:53] being and the technology exists such
[01:56] that we can do all of this in real time
[01:59] we can
[02:01] transcribe speech to text in real time
[02:04] we
[02:06] can trans
[02:08] pose uh text to speech in nearly real
[02:11] time as well and so I kind of wanted to
[02:13] piece all these things together and
[02:15] that's what we're going to go through
[02:16] today so this is a better AI assistant
[02:19] this is
[02:21] Floyd this is actually Lloyd from
[02:23] Entourage um but when I was thinking
[02:25] about the name I was like who is the
[02:27] best personal assistant of all time
[02:30] and it's Lloyd from Entourage but I
[02:32] forgot his name and I thought it was
[02:34] Floyd uh and so Floyd is the name of the
[02:37] app and Lloyd is the name of the
[02:39] personal assistant from
[02:40] Entourage um so there is the repo
[02:44] available for this uh we're going to
[02:46] walk through a demo we're going to walk
[02:47] through some of the code um it's okay if
[02:51] you don't get it totally up and running
[02:53] right now there are a number of third-
[02:55] Party platforms that we are going to
[02:57] string together to make this work and so
[03:00] for it to work for you end to end we
[03:03] need Google cloud with the speech to
[03:05] text API enabled uh a convex account an
[03:09] open AI key and a twilio account um if
[03:13] you have all those things wonderful if
[03:16] not um I'm more than happy to help get
[03:19] anybody set up and see if we can get
[03:21] Floyd working for you on your machine
[03:24] after the talk so this is what the the M
[03:28] file is going to look like we got the
[03:29] open stuff twio stuff some convex things
[03:32] uh and some some Google
[03:34] stuff
[03:37] yeah uh uh it's not uh but it will be it
[03:42] will I'm not sure I will I will send it
[03:45] I'll make sure that it's it's available
[03:47] after the talk for sure
[03:50] sorry yeah yeah yeah for
[03:55] sure so a little bit of the higher level
[03:59] architecture here
[04:02] um this is at a high level how Floyd
[04:07] works so you'll have an
[04:09] application uh either like your phone or
[04:11] a web app it will take a voice request
[04:14] from the person you who needs help um
[04:19] it'll take a voice request it'll
[04:21] transcribe that in real time by
[04:24] streaming to Google Cloud which will
[04:27] stream back the trans uh transcription
[04:31] so you could say something like
[04:34] um
[04:36] um when's my next dentist appointment or
[04:39] book me a dentist appointment or
[04:40] something like that it'll make that
[04:42] transcription and then what happens is
[04:44] that the client will simply save that
[04:47] request the user who made it and that
[04:50] request into the convex database and
[04:54] then hands
[04:56] off what the server is doing is
[05:00] listening for changes to new requests in
[05:03] real time from that same convex database
[05:07] it's not
[05:08] polling we're not pinging the server to
[05:11] let it
[05:12] know it's got a reactive uh query that
[05:16] it's effectively subscribed to and so
[05:18] when a new requests come
[05:20] in the server is able to Simply pick
[05:23] that up and start working on it and
[05:25] provide status updates um along the way
[05:29] which on the other hand the client is
[05:32] able to then present back to the user so
[05:35] the request goes in the server picks it
[05:37] up and maybe sets it to impr progress
[05:41] that status in progress is again picked
[05:44] up for free automatically in real time
[05:47] by the client which is also subscribed
[05:50] to that database and we'll see what that
[05:51] looks
[05:52] like so we save the request on the
[05:56] server um the server will go and look up
[06:01] what it knows about the person who made
[06:03] the request okay so this is um a
[06:09] platform that over time becomes more and
[06:12] more knowledgeable about you every time
[06:14] you make a request or you ask it
[06:15] something or you give it information or
[06:18] you connect your email Etc it will start
[06:21] to learn things about you what kind of
[06:23] car you drive where your last uh
[06:25] mechanic shop was what school your kids
[06:27] go to um you can provide as much or as
[06:30] little of this as you want you can wait
[06:31] for Floyd to prompt you to ask these
[06:33] questions but this is the type of
[06:35] information it's going to need to know
[06:37] to say call the school and let them know
[06:39] that your kid's going to be late okay so
[06:42] the server is going to
[06:44] take what it knows about the person who
[06:46] made the
[06:47] request and it's going to uh save that
[06:51] context as a moment in time onto that
[06:54] request so now we have this request
[06:55] object in the in the database it's got
[06:58] the the the person who made it it's got
[07:00] the request itself it's got some context
[07:02] and basically it's ready to go so the
[07:04] server will then take that and it'll
[07:06] work with um uh open AI like the chat
[07:09] GPT integration uh 40 in this
[07:12] case to effectively provide chat GPT
[07:18] with the
[07:21] request and with the
[07:23] context that it needs to fulfill that
[07:27] request and say this this is your job
[07:30] now are you ready to help us
[07:34] out at that point open AI is like yeah
[07:37] we got this I think I I think I know I
[07:39] know what to do and it's like great okay
[07:41] we're gonna we're going to make a phone
[07:42] call right now the next thing is going
[07:44] to be uh somebody on the phone uh and
[07:46] you're talking to them okay so at that
[07:49] point the server now has this great
[07:52] starting
[07:53] point uh with the help of open AI to
[07:56] make the phone call so there's a number
[08:00] of ways it can find the phone number for
[08:03] whatever the request might be uh
[08:05] typically that would exist in your prior
[08:08] context um if not now this doesn't exist
[08:11] yet but if not the idea would be we
[08:15] understand the request we know the
[08:17] general area where you live we would do
[08:19] the work to look up the phone number if
[08:21] for example it wasn't already existing
[08:24] in your context and if we can't find it
[08:28] at that point we could send you a text
[08:30] or something like that Floyd would send
[08:31] the text and say hey um do you have a
[08:34] preferred vendor we couldn't find a
[08:36] mechanic in your history we couldn't
[08:37] find any online is there anybody that
[08:40] you would like to use so at that point
[08:43] the server will make uh the phone
[08:47] call and it does that by
[08:51] coordinating the conversation through
[08:55] gp4 using open
[08:57] ai's text to speak
[09:01] speech streaming that through
[09:04] twilio and then as the person on the
[09:07] other side of the call is speaking we're
[09:10] streaming that audio to be transcribed
[09:12] in real time through Google Cloud which
[09:15] we then feed back into gp4 to carry on
[09:18] the
[09:20] conversation so we're streaming this as
[09:23] fast as
[09:24] possible um I am super impressed by the
[09:28] technology that we access to today the
[09:30] fact that this works and isn't painfully
[09:34] slow um just I'm still like it boggles
[09:38] my mind we're we're we're very fortunate
[09:40] to to operate in the ecosystem that we
[09:44] do so this Loop that you're seeing right
[09:47] here this happens over and over until
[09:49] the conversation is uh is complete so
[09:52] the audio bites come back uh and so on
[09:55] and so on yeah
[10:01] with
[10:02] a
[10:06] resp not yet not yet
[10:10] um oh yeah so the the question was have
[10:13] I been experimenting yet with a
[10:16] multimodal Gemini where you can pass it
[10:18] audio and basically skip that that step
[10:22] of transcribing right um I haven't um
[10:26] but the beauty of this is that I'm
[10:29] designing it in such a way that um we
[10:33] should be able to swap in and out
[10:35] different Services because they're
[10:37] coming out so fast you know when I
[10:39] started this that didn't exist um and
[10:41] it's exactly the type of thing I would
[10:43] experiment with and see if I could make
[10:46] it even faster right I think like the
[10:48] faster you make this there's there's no
[10:50] limit to how um how quick this should be
[10:54] uh when it's when it's operating so I I
[10:56] I think that's an awesome thing to
[10:58] explore
[11:00] so as this Loop is happening we are
[11:04] actively saving each part of this
[11:06] transcript as part of that request to
[11:09] the convex database so we're just saving
[11:12] it we're just pushing it we're just
[11:13] appending to the
[11:14] database what that means is that on the
[11:16] client because convex is a reactive
[11:19] database for free it's like a oneliner
[11:22] in the client instead of saying use
[11:25] State you just say use Query once and it
[11:28] will update when the database updates so
[11:31] as we are writing the
[11:33] transcript to the
[11:35] database your client for
[11:38] example could be streaming that back in
[11:41] real
[11:44] time all right well let's dive
[11:48] in um I feel like a see if we can get
[11:53] a a demo going first and foremost why
[11:57] not what could possibly go wrong
[12:06] okay so this is sort of a shell it's
[12:08] very much a work in progress I wouldn't
[12:10] exactly call this production ready um
[12:12] but it's it's fun and it it it does work
[12:15] so I'm going to make a voice request to
[12:20] uh Floyd here who is uh hopefully going
[12:24] to see if they can help me out now for
[12:28] development I have um overwritten every
[12:32] phone number it would call to just call
[12:34] me so I pretend like I'm the vendor uh
[12:38] I'm not I'm not totally confident enough
[12:41] for it to call like a real business and
[12:43] not and and not totally uh in embarrass
[12:47] me or or do something crazy um so still
[12:49] in development so let's see um let's see
[12:53] here let's see what we can have Floyd do
[12:56] for us
[13:00] hey Floyd can you call the school and
[13:02] let them Mara is going to be home she's
[13:04] sick
[13:10] today so here we have the request ID
[13:12] it'll automatically send that request
[13:14] when you stop
[13:15] speaking um down
[13:20] here I'm the
[13:23] school hello this is Mara School
[13:29] hey there this is Floyd I'm calling on
[13:31] of my client Tom redond um Mar redond is
[13:34] staying home today she's
[13:36] sick oh no is she gonna be
[13:43] okay yeah just a bit under the weather
[13:45] right now okay that's good do you have
[13:47] any idea when she's going to be
[13:56] back she's hoping to be back by the end
[13:58] of the week I'll keep you updated if
[14:00] anything
[14:01] changes okay that's great thank
[14:08] you maybe I should try that Gemini think
[14:11] thanks for understanding have a good
[14:14] day so again you can see like it's it's
[14:17] it's there the latency is so crucial
[14:20] though um now this is all in like
[14:21] development land uh moving this over to
[14:24] production in every one of these
[14:27] platforms would you know that would be
[14:28] the next thing I try make it go faster
[14:30] try different models um there's
[14:32] different things that I've already done
[14:34] in terms of the audio encoding to make
[14:38] the streaming as fast as possible
[14:40] there's a format called Opus which is
[14:42] designed for um phone call level quality
[14:46] um and is encoded to to be streaming
[14:49] really quick let's um so we can see
[14:53] here here's the request that came in and
[14:56] again uh
[14:59] all I did in the client was send the
[15:03] request
[15:05] text to the
[15:07] database uh the client has listening for
[15:10] those any requests that match this user
[15:12] and is going to automatically update uh
[15:14] the app and so the first thing I asked
[15:17] open AI to do is come up with an action
[15:19] plan so we're not saying any of this but
[15:24] in some ways I have open AI kind of
[15:26] prompt itself I say hey we're a team
[15:29] here we're going to help um we're going
[15:32] to help Tom in this case you know do
[15:35] something they've got a request uh let's
[15:37] let's work on this together here's the
[15:38] request here's the context and so then
[15:40] this is what open AI says here's based
[15:42] on the context it'll look up the context
[15:44] on me what it knows about me and it'll
[15:46] say okay well he pulls out all the
[15:47] important information required for that
[15:49] request so Mara's full name we know it's
[15:53] uh Mara Redmond uh school name reason
[15:55] for absence today's date steps to fill
[15:58] fill the request and then I send this
[16:01] back in um as additional context when uh
[16:07] we're actually making the phone call so
[16:09] it's like open a eyes got these
[16:10] instructions it's just sitting with
[16:20] yeah uh I haven't tried maybe um I
[16:25] haven't it I I certainly haven't done
[16:27] anything specific for that uh but it
[16:30] definitely feels a lot more
[16:32] straightforward to do something like
[16:34] that um than interacting with a human so
[16:37] I I wanted to get the the thing I didn't
[16:40] know was going to work out of the way um
[16:42] I feel like navigating a call tree is
[16:44] definitely a solvable problem this was
[16:47] like really a curiosity for me to see if
[16:50] we could get this to work and you can
[16:52] see down here um I'll see if I can zoom
[16:55] in my uh CSS skills are are uh are
[16:59] lacking here but there's a transcript
[17:03] here that comes in uh in real time as
[17:06] well and maybe I can actually do
[17:10] another uh let's make another
[17:14] request hey Floyd can you order Christa
[17:17] some
[17:25] flowers now we can watch this action
[17:27] plan and everything coming in real time
[17:29] now I'm going to be the flower shop so
[17:32] let's break this down
[17:38] okay
[17:41] oh sweet Violet's flowers how can I help
[17:52] you hey there this is Floyd I'm calling
[17:54] on behalf of my client Tom Redmond um I
[17:57] need to order some flowers first
[17:58] delivery
[18:00] today uh okay do you have any idea what
[18:04] kind of flowers you would
[18:10] like I know Christa likes your usual
[18:13] offering could you recommend something
[18:14] popular from your collection yeah we
[18:17] have some uh peonies and some roses for
[18:20] $560 would you like
[18:26] that that sounds good can you deliver it
[18:29] to an address in today yeah AB
[18:33] absolutely um I think we have we have
[18:35] you been here before do we have your
[18:37] information on
[18:41] file I'm calling on behalf of Tom do you
[18:45] need his details again or do you have
[18:46] them on file sorry I'll have to call you
[18:49] back
[18:51] ha that's right so I have uh this
[18:55] like bail situation built in where it's
[18:59] like all right if you're in a pickle and
[19:01] you just don't have the information that
[19:03] they're asking for you say I'm sorry I'm
[19:05] going to have to call you back and at
[19:07] that point Floyd's
[19:10] like I'm missing something I need
[19:13] something and it would send me a text
[19:16] saying hey tried to order you flowers um
[19:20] but you didn't give me a budget and they
[19:21] wanted to charge you $560 for some
[19:25] pnes um all right so
[19:30] what we're looking at
[19:34] here is the uh the database in in convex
[19:39] that's storing the request
[19:41] information so here we have some uh
[19:45] requests and you can see hey Floyd can
[19:49] you order Christa some flowers so I wish
[19:51] my sorry about my my CSS skill oh there
[19:54] we go okay that kind of works can you
[19:56] order Christa some flowers so let's find
[19:57] that here we go hey Floyd so I can go
[20:00] ahead and just update this straight in
[20:02] the database uh some flowers I'm going
[20:05] to say there is no
[20:07] budget
[20:09] um and then we'll just save that and
[20:12] then watch what happens in the client
[20:13] when I change the
[20:15] database that's it that's why when I
[20:18] append parts of that transcript to the
[20:22] database and I'm listening for those
[20:23] changes in the client they uh they just
[20:27] appear
[20:29] uh what I also have in here are uh for
[20:34] users we have this context now I want to
[20:37] I want to uh preface this by saying like
[20:40] the actual code of what I'm doing here
[20:43] is far from best practice so like don't
[20:46] take this and try to roll it into
[20:47] production this is definitely a a proof
[20:50] of
[20:51] concept prior to using convex for
[20:56] this I was trying all sorts of things to
[21:00] get that phone
[21:02] call the transcript of that phone call
[21:05] to stream back live to the client in
[21:10] fact I wanted to get it so that you
[21:11] could listen in live to the
[21:15] client I was really
[21:17] struggling with that um I was I didn't
[21:22] roll my own server to begin with I was
[21:24] using uh nextjs which is fantastic but I
[21:28] was hosting it on
[21:30] versell which doesn't play very nicely
[21:34] with uh
[21:35] websockets right most of her sales
[21:38] hosting is uh is serverless and
[21:40] websockets are inherently stateful so
[21:44] while I was able to get um parts of this
[21:48] working with socket IO for example the
[21:51] first
[21:53] transcription having it actually
[21:55] interact with the phone call and
[21:56] streaming that audio with twillo through
[22:00] a websocket protocol um I found to
[22:05] be difficult on the front end and so I
[22:08] was trying to do this all in one
[22:13] place with convex I was really able to
[22:17] separate those concerns and just listen
[22:21] for the things I wanted the the the bits
[22:25] of data I was interested in
[22:28] and let the server manage whatever
[22:31] server it is in this case it's it's uh
[22:34] an Express server that um that I've
[22:37] written and let it do the lifting and
[22:39] basically just post updates to the
[22:41] database so we don't we don't have to on
[22:43] the client we don't have to we don't
[22:44] have to PLL um we don't have to post
[22:48] anything and so it's all uh it it really
[22:53] simplified the separation of uh of
[22:56] concerns around this now now the really
[22:59] really interesting thing here is that if
[23:01] you're not using a serverless hosting
[23:05] infrastructure you could do this entire
[23:08] thing
[23:10] in Tech like in your client
[23:13] codebase when you're coding with convex
[23:16] you don't necessarily have to uh break
[23:20] out your server code from your front-end
[23:23] code the whole value prop is that you're
[23:25] able to actually build a full server
[23:29] in client land it doesn't actually get
[23:32] served on the client it gets deployed to
[23:35] a convex server but you can Define your
[23:37] back end and your apis and your schemas
[23:40] and your databases all in the same
[23:43] codebase as your front end um and I'll
[23:47] show you exactly what I mean about that
[23:51] so uh let's close this here so here I
[23:56] have uh the the web
[23:59] I have my uh my web
[24:01] client um let's take a take a look at
[24:06] the page that uh that
[24:09] shows that list of requests and then the
[24:12] request
[24:14] details this line
[24:19] here this line fetched
[24:22] requests that's it anytime a request is
[24:25] updated or changed and it matches the
[24:28] query I've defined in uh this this
[24:31] convex function it'll update my react
[24:35] client uh however I want so let's see
[24:37] what what do I do with this obviously I
[24:39] provide uh so it gets updated I provide
[24:42] a a list of uh fetched requests so
[24:47] requests so I pass in my requests which
[24:50] gets updated and updated um into my into
[24:53] my dashboard and then from there I just
[24:57] it's an array of requests I list them
[24:59] out it's got the details uh of the
[25:01] request that I can use when somebody
[25:04] clicks on something in a list I can show
[25:06] those details in the in the detail pane
[25:10] um and I
[25:13] think what's interesting here is the way
[25:17] that I've
[25:18] defined um the get
[25:21] requests is just this
[25:27] query so this query itself actually
[25:31] right now is not uh user specific but
[25:33] typically you would probably add in some
[25:35] user ID and some o this this this
[25:38] prototype does not have o again do not
[25:40] ship this um so this is the
[25:44] query get and if you recall in my last
[25:50] uh see if I can find it
[25:54] here in my page remember I said
[25:59] API requests get API is a
[26:04] generated type
[26:06] safe uh convex model that gets um
[26:10] updated and deployed every time you make
[26:12] a change to one of those convex files so
[26:15] api. requests.get and what that's doing
[26:18] is specifically hitting uh this this
[26:20] function here I can name this whatever I
[26:22] want this just happens to be a get
[26:24] request um and so then this is this
[26:30] function this is a query that actually
[26:32] lives not on the
[26:35] client even though my code is here in
[26:38] client
[26:39] land it doesn't get shipped with the
[26:42] client it gets built and
[26:45] deployed to convex and this function
[26:49] physically runs on the convex server on
[26:53] the same machine as your database
[26:58] so this there's a there's a custom V8
[27:01] engine that's running next to the
[27:04] database that's actually executing the
[27:08] JavaScript or the typescript that you
[27:10] define here this makes it
[27:13] extraordinarily
[27:15] fast it absolves you from ever having to
[27:18] think about caching yeah
[27:42] yeah that's a good question so the
[27:43] question is why would you like what's
[27:46] what's the big compelling reason to use
[27:48] something like convex over um the other
[27:52] you know like common databases like
[27:55]  or postgress and
[27:58] the big thing is the developer
[28:03] ergonomics you don't need a backend
[28:07] Andor infrastructure engineer or team if
[28:10] you're using
[28:12] convex you get um type safety all the
[28:17] way through from your database through
[28:21] to your front end and you get all the
[28:23] wonderful completions that happen uh
[28:26] with that as you define your
[28:29] schema um and you can operate in a much
[28:35] more simple
[28:38] codebase and so again I don't have to St
[28:41] like this this what you're seeing here
[28:43] is the totality of my of my backend
[28:47] server as far as the requests uh table
[28:53] goes uh and so I've added different
[28:55] things like get request uh by ID get
[28:58] pending requests right so we can do like
[29:00] different
[29:01] filtering um post request the post
[29:04] request is interesting because again in
[29:08] in in front end land you can create an
[29:11] HTTP server that just has arbitrary
[29:14] endpoints with arbitrary responses and
[29:16] you can use those with or without
[29:19] hitting the database um but you can
[29:21] simply Define a get rot or a post root
[29:25] in your uh
[29:26] HTTP um actions and do with it whatever
[29:30] you want so in this instance what I'm
[29:33] doing again because um because I need I
[29:37] need the server here to be able to
[29:39] stream to
[29:40] twilio any any other platform or server
[29:43] that supports um like websockets
[29:46] natively you can you can do it all in
[29:47] one place so what I've created here is
[29:50] an HTTP post request that posts the uh
[29:53] the the data uh or the requests of the
[29:56] user um
[29:58] to the to the server which also
[30:03] happens
[30:10] here so here I've added the post request
[30:13] and um this
[30:15] is going to run the action which goes
[30:18] ahead and updates the database
[30:26] yeah sorry the only way to debug this is
[30:31] to so uh note we have uh on the
[30:35] dashboard you get a full uh full access
[30:38] dashboard that includes all of uh all of
[30:42] your logs for all of the requests it
[30:44] includes the definitions for uh for your
[30:48] functions and you can actually run your
[30:50] functions from the dashboard as like
[30:52] test functions and to see um what the
[30:56] response is or
[30:59] yeah
[31:06] pardon uh that's a good question
[31:16] um right so the the question is um can
[31:20] you hit break points in the convex
[31:23] server code honestly I don't know can I
[31:26] get back to you on that I can I can
[31:28] definitely follow up um that's a that's
[31:31] a that's a great Point that's a great
[31:32] that's a great question um I've
[31:34] typically ended up relying on both the
[31:37] logs and then the uh the convex
[31:44] um client that is doing the uh
[31:48] compilation on your machine will also
[31:50] give you give you any uh any errors but
[31:53] that that's a great question let me let
[31:55] me get back to you on that one
[31:58] um okay and so here we have try to make
[32:02] this a little bit easier to
[32:05] see
[32:07] [Music]
[32:12] [Music]
[32:15] toggle okay maybe
[32:19] not all right so here we have the
[32:22] request being
[32:24] saved um this is a little bit of an
[32:27] esoteric way to do it again just because
[32:29] of the I this this need to stream and
[32:31] then at the same time what I wanted to
[32:33] do with the stream was write that
[32:35] transcript in real time as it's
[32:36] streaming into the database uh and so
[32:40] what uh what that looks like is here in
[32:46] uh in the
[32:47] server this is a a basic Express server
[32:58] I've created a convex client right
[33:00] within the server that will effectively
[33:02] get an update every single time this
[33:04] database uh changes again based on the
[33:08] query I Define um so in this case I'm
[33:13] asking convex to ping my server uh
[33:17] anytime there's a change to a pending
[33:19] request and just by convention I've when
[33:22] somebody makes a request from the client
[33:25] um it's pending by default the server
[33:29] will get that the server will then um
[33:33] make sure that it exists and the first
[33:35] thing it does is change the status to
[33:39] inflight um and then it will start
[33:42] taking action
[33:44] on uh on that
[33:47] request and so we will then get the full
[33:51] request which has the uh
[33:55] the the actual like ask of of of the
[33:58] client um we'll get the in this case we
[34:01] get the session name and then we do this
[34:02] like gather context with open AI this is
[34:06] where uh this function is reaching into
[34:09] the database and trying to pull out
[34:11] everything it knows about the user who
[34:12] asks this
[34:13] request uh Then I then I update the
[34:16] context so I save that so I have this
[34:18] context and I filter out the parts of
[34:21] that that are required to actually
[34:22] fulfill this ask and I saved just that
[34:25] sort of subset of that contact text into
[34:29] uh into the request itself just for ease
[34:32] of access again you know if we sit down
[34:34] and and do like a design session on this
[34:36] there's going to be a lot of changes to
[34:38] make um at that point I say okay make
[34:41] the
[34:42] call uh and so the way that uh the way
[34:47] that twio works is that it will uh I can
[34:53] use the twilio client and I can make a
[34:55] call and when that call Connects this
[34:58] config tells twilio where to hit me back
[35:02] when the status of the call changes um
[35:05] and also any streaming data that's
[35:07] coming in and so I have a websocket
[35:10] opened up here so I have enro running um
[35:13] on my server right now so that twilio
[35:15] can hit it uh so I have a a websocket
[35:19] server here that I just set up in
[35:21] Express um and when that gets hit with
[35:25] uh with a twilio event which sometimes
[35:27] is like call initiated you know data
[35:30] heard call ended that kind of
[35:33] thing um I have this websocket up here
[35:37] so I
[35:40] ask in the request to make the call I
[35:43] pass the
[35:44] request ID and when twio calls my server
[35:48] back I've asked it to call my server
[35:50] back with the request ID so that's how I
[35:52] can pass through that data from from
[35:55] twilio because I'm I once I send off
[35:58] that call I'm just waiting it's it's
[36:01] it's gone into The Ether and you hope
[36:03] that like you're going to get the the
[36:04] phone call from twilio so I needed some
[36:06] way to be able to track that request ID
[36:09] so that when the call actually connects
[36:12] um I know the context of what the call
[36:16] is all about and what the request is
[36:17] about and so I have twilio send the
[36:20] websocket request to uh this location
[36:24] with the request ID and at that point I
[36:27] open up the the media stream Handler
[36:29] which grabs the request
[36:31] ID um and then uh and then looks it up
[36:35] and then there's there's a number of
[36:37] Fairly standard like media stream
[36:41] functions in here things like process
[36:42] message which gets called um a lot right
[36:46] over and over and over uh you can
[36:48] configure twilio to to send you
[36:51] different things like you can have it uh
[36:53] send you fixed size chunks you can have
[36:55] it send you the audio data
[36:58] after every utterance or after every
[37:01] pause um and so what I have here is is
[37:04] basically every I have twilio sending me
[37:07] the audio data the streaming audio data
[37:10] uh basically after every utterance which
[37:12] is just like commas and in in periods
[37:14] and things like
[37:16] that and so when I get that
[37:21] um I take the audio data I convert it
[37:27] into
[37:28] to uh into a file type that Google cloud
[37:33] is uh fast with I get the transcription
[37:38] back and then uh I
[37:41] convert I get the transcription back I
[37:44] ask open AI to then speak it where's the
[37:48] speaks yeah so here's the speak
[37:51] function I then convert that into a
[37:56] streaming format that twilio is down
[37:58] with um for streaming uh which is uh
[38:03] taking this Moola file uh into and then
[38:05] streaming it as as base uh base 64 back
[38:10] to uh back to twio and then throughout
[38:13] this whole time um you can see here
[38:15] client mutation add to transcript so
[38:18] every time I'm getting a new transcript
[38:20] entry back from Google Cloud during the
[38:21] stream I'm just updating the convex
[38:24] database like that's just happening and
[38:26] then the client is just subscribe to
[38:28] those changes and can you know show them
[38:31] in a list or I know somebody who's
[38:33] better at UI than I can can make that
[38:34] look really nice and like have it uh
[38:37] have it scrolling or
[38:39] something um so this is here's
[38:42] a this introduce yourself so I actually
[38:44] have a
[38:46] pre-recorded generated audio file that
[38:51] is something like um hi my name is Floyd
[38:55] I'm calling on behalf of my client
[38:57] that's pre-recorded because I realized
[39:00] I'm not sure if it was doing it today
[39:02] actually because I didn't hear it um but
[39:05] I realized the first
[39:08] interaction was the longest once
[39:11] somebody picks up the phone everything
[39:13] kind of kicks into gear and that's where
[39:15] like the there's this like builtup
[39:18] latency um so somebody picks up the
[39:20] phone they go hello Brock Road garage
[39:23] and then it was like well you heard it
[39:25] because I don't think it's working um so
[39:28] what I did was have this pre-recorded
[39:30] pre-generated audio file that as soon as
[39:33] somebody says picks up and says hello I
[39:35] just play it so I don't have to do any
[39:37] transcribing or any um any text to
[39:40] speech or anything and while I'm
[39:43] streaming that hi this is Floyd buying
[39:47] myself some time that's when I'm
[39:49] actually triggering the first Loop of um
[39:54] of the conversation and all the
[39:56] transcriptions and the text to speech
[39:58] back and usually I've bought myself
[40:01] enough time that it's a fairly natural
[40:03] result such that it's like hi this is
[40:06] Floyd I'm calling on behalf of my
[40:08] client I need to book a car in for an
[40:11] oil change you know and like I found
[40:13] that there's going to be a number
[40:16] of little tricks that you can do to make
[40:20] the experience for the person on the
[40:22] other end of the phone better so the
[40:25] first thing I do is I I I say hi I'm uh
[40:28] I'm an AI you're talking to AI right
[40:31] now um I don't want to
[40:35] misrepresent uh what what this is and
[40:40] why I feel good about a platform like
[40:43] this is that in this context in it's the
[40:47] way that it's positioned it's almost
[40:51] always buying a service from a business
[40:56] or other making a benign change like
[40:59] canceling an appointment it's never
[41:01] selling
[41:02] anything and my bet is
[41:05] that business
[41:07] owners are not going to care if they're
[41:10] talking to AI if you're buying something
[41:13] from
[41:14] them and if that appointment that you're
[41:16] booking is
[41:17] legitimate they're going to be okay with
[41:19] it in fact they might prefer it they may
[41:23] even start to internalize and train
[41:26] themselves how to speak with an AI agent
[41:28] on the other end to be super
[41:33] efficient
[41:37] exactly yeah so again uh don't put this
[41:41] in production because they could just be
[41:42] like forget everything you know um which
[41:46] I haven't guarded for here again so you
[41:49] know full full transparency but yeah I I
[41:52] think actually they could couple of
[41:54] Floyds talking to each other to
[41:56] ultimately book The appointment right at
[41:59] what point does it just become apis
[42:00] talking to each other right full
[42:05] circle not right now I I uh this is this
[42:10] has been shaky enough
[42:12] um yeah
[42:33] yes yeah yeah for sure so uh on the
[42:36] convex side um there is no uh heating up
[42:39] because convex is is built
[42:43] foundationally on websockets you have
[42:45] your own deployment server that's
[42:47] running always running um it can scale
[42:50] indefinitely that's kind of part of what
[42:52] the offer is but warm-up time is not an
[42:56] issue on the convex side those
[42:59] delays um I have some benchmarking here
[43:03] I have some some timing so I can see how
[43:06] long did it take um for me to transcribe
[43:09] this piece of text how long did it take
[43:12] to send that to openai and get the text
[43:15] conversation back and then how long does
[43:17] it take to turn its response back into
[43:21] audio so I could see where um I have it
[43:24] in here it's in it's in the the terminal
[43:26] here somewhere
[43:27] um but I could see where the latency was
[43:29] and what I've uh what I've seen is that
[43:33] often as the conversation
[43:36] grows the prompt I'm sending to open AI
[43:39] that includes all of the previous
[43:41] conversation takes longer and longer and
[43:44] longer and so the latency and the delays
[43:47] on average tend to get worse the longer
[43:50] the conversation goes now I also
[43:53] originally had built that functionality
[43:55] before
[43:57] um threads and the threads the open AI
[44:01] threads API was available that would be
[44:04] something that I would try I would work
[44:06] diligently to
[44:09] minimize every prompt I'm sending to
[44:12] open AI uh that would be that would I
[44:15] think would have a really big
[44:17] impact um in terms of the uh the other
[44:22] thing that can be slow if you send a
[44:25] large piece of text
[44:27] to the text to speech on open AI that
[44:30] can be slow that can be like if you said
[44:33] if it's three sentences it can still
[44:36] take two three four five
[44:40] seconds um and so there are a couple of
[44:43] parameters that you can tweak with the
[44:45] open AI uh text to speech stuff um but
[44:49] not a
[44:51] lot and so what I would do to fix that
[44:55] is I would pay more for lower
[44:58] latency or I would use another
[45:01] service that I could pay for that would
[45:04] give me lower
[45:05] latency
[45:07] um the way that this is now so like in
[45:10] those phone calls what what you heard
[45:12] and what you experienced those
[45:14] delays there are
[45:17] still optimization opportunities um like
[45:21] crazy to to bring that all down I'm
[45:24] actually not even concerned with that
[45:25] right now because there's still
[45:27] half a dozen material things I haven't
[45:30] tried to close that Gap I was just happy
[45:32] to have a conversation with a computer
[45:34] um that I could ask questions to but
[45:36] that yeah the the the latency comes from
[45:39] the uh the the sum of all of the
[45:42] different interactions that are
[45:43] happening and so if you speed up any one
[45:45] of those along the chain it's going to
[45:47] be faster and faster and faster um and
[45:50] second to that point uh everything
[45:53] that's coming out every couple months
[45:55] there's like this massive Improvement in
[45:57] some API in this
[46:00] stack and so again the bet is that like
[46:03] well I can get it as close as possible
[46:05] right now but I know in six months it'll
[46:07] be twice as fast without me doing
[46:08] anything it's just the rate of
[46:11] innovation and the rate of change in
[46:12] competition right now for this type of
[46:14] thing is so high um that that that'd be
[46:19] a bet that I'm I'm taking on and be like
[46:21] yeah maybe it's not perfect right now
[46:23] but it inevitably will be very soon
[46:28] um all right let's see here what what
[46:31] time are we at okay uh just a couple
[46:34] more minutes okay um any any other
[46:37] questions I can walk through any of the
[46:38] server stuff any of the front end code
[46:40] yeah
[47:03] yeah that's a that's a I love that um so
[47:07] the question
[47:09] was a little bit more context about
[47:12] convex um and how it works under the
[47:16] hood how it distributes its queries what
[47:18] kind of uh database infrastructure is it
[47:21] running on so the team that convex is is
[47:27] um it's open source um but it's a custom
[47:31] built from the ground up database it's
[47:33] literally a database built from scratch
[47:35] to be able to
[47:37] solve all of these to be able to
[47:39] basically provide this product and the
[47:41] people who built it so my my boss is the
[47:45] CEO and the CTO Jamie and James uh
[47:47] Jamie's here today actually he'll be
[47:48] doing a some a keynote speak I joined
[47:51] convex because of them they have they
[47:54] have this track record that was like
[47:57] mindblowing to me and it was only about
[47:59] six months ago I discovered them and the
[48:02] more I was reading about it the more I
[48:03] was like these guys did what like they
[48:07] they built from scratch in Rust a brand
[48:10] new database so James uh has uh his his
[48:16] PhD in uh database architecture from MIT
[48:20] and so he was instrumental in basically
[48:22] designing a novel database to make all
[48:26] of this work
[48:27] and so the way that it runs is it
[48:30] actually runs on uh an AWS cluster and
[48:34] it's running the convex database and
[48:36] application which manages all of the
[48:39] websocket connections and all of the
[48:41] subscriptions um in terms of like
[48:44] literally and physically how it's
[48:46] distributed I'd love to follow up like
[48:48] that's that's it's deeper than my
[48:51] expertise um but we do have some large
[48:54] customers uh using it these days um
[48:58] there haven't been any uh fundamental
[49:02] issues at all in terms of its ability to
[49:04] scale we've been very you know happy
[49:07] with how that's worked out so far um and
[49:10] then uh yeah and so it's you you could
[49:14] take a look at the take a look at the
[49:16] open source repo um it's super
[49:17] interesting and there's a really great
[49:19] blog post written by uh our chief
[49:22] scientist sujay called how convex works
[49:25] and it does a deep dive into the
[49:27] architecture of uh of the
[49:29] database um and so to be fair sometimes
[49:33] people are like well like you know is
[49:36] that risky not to do like postgress or
[49:39] something like that um and it's it's a
[49:42] bet you'll be taking but we believe that
[49:44] the the trade-off there the developer
[49:46] ergonomics the speed the fact that
[49:49] you're if you want to start a company
[49:51] you don't need your infrastructure
[49:54] Engineers um to be building
[49:56] infrastructure you can take your
[49:58] infrastructure engineers and they can be
[50:00] building your product they can be
[50:02] building the things okay that's it they
[50:05] can be building the things that your
[50:07] customers care about not worrying about
[50:10] database
[50:11] backups cool thank you all so much I
[50:14] really appreciate um your attention and
[50:17] your time this was this was a lot of fun
[50:19] if you want any help uh getting the the
[50:22] the repo up and running come find me I'm
[50:24] I'm happy to help see if we can get it
[50:26] working on somebody else's
[50:29] machine right okay thank you all very
[50:31] much
[50:33] [Music]
