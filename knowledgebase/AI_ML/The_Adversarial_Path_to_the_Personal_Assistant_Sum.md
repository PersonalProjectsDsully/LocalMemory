---
type: youtube
title: The Adversarial Path to the Personal Assistant: Sumit Agarwal
author: AI Engineer
video_id: ckLXb15BnM8
video_url: https://www.youtube.com/watch?v=ckLXb15BnM8
thumbnail_url: https://img.youtube.com/vi/ckLXb15BnM8/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning Product Demos
tags: ['AI', 'Machine Learning', 'Data Privacy', 'User Experience', 'Product Demo', 'Personalization', 'Data Integration', 'Ethical AI', 'User Profiling', 'Real-Time Data', 'AI Ethics', 'Conversational AI']
entities: ['A', 'Joan', 'Amazon', 'DoorDash', 'Chat GPT', 'AI', 'Machine Learning', 'Data Privacy', 'User Experience', 'Product Demo']
concepts: ['AI-driven personalization', 'data integration', 'user profiling', 'memory-based systems', 'real-time data processing', 'ethical AI', 'user engagement', 'product demos']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['basic understanding of AI concepts', 'familiarity with data integration tools', 'experience with product demos']
related_topics: ['AI ethics', 'data privacy regulations', 'user experience design', 'machine learning algorithms', 'personalization technologies', 'product development', 'data analytics', 'conversational AI']
authority_signals: ["we've put a lot more time and energy into tuning what needs to be remembered", "I'm not going to take you through every single one of our data sources that would take too much time"]
confidence_score: 0.8
---

# The Adversarial Path to the Personal Assistant: Sumit Agarwal

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=ckLXb15BnM8)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai, generative-ai, personal-assistant, machine-learning, automation, data-aggregation, ai-ethics  

## Summary

```markdown
# Summary of "The Adversarial Path to the Personal Assistant" by Sumit Agarwal

## Overview
Sumit Agarwal from Aro presents an AI-powered personal assistant designed to help users reclaim time by automating and personalizing tasks. The solution leverages **adversarial ETL (Extract, Transform, Load)** to aggregate data from multiple sources, creating dynamic user profiles. The goal is to build a deeply personalized system that evolves with user behavior, emphasizing privacy and actionable insights.

---

## Key Points
- **Mission**: Aro aims to give users **one hour of free time per day** by automating routine tasks and providing context-aware assistance.
- **Adversarial ETL**: A novel approach to data integration that bypasses traditional APIs, extracting insights directly from user data (e.g., emails, apps, social media).
- **Data Portrait**: A dynamic, AI-generated profile that reflects a user’s interests, habits, and preferences (e.g., hobbies, family details, routines) based on their digital footprint.
- **Privacy Focus**: Users retain full control over their data. Aro emphasizes **no intake forms or essays**—profiles are automatically generated and updated.
- **Memory System**: A dedicated section for explicit user inputs (e.g., "Remember I like Japanese restaurants") to enhance personalization.
- **Real-World Demos**: The system demonstrates capabilities like identifying childcare needs, dietary restrictions, and interests through data analysis.

---

## Key Quotes
- *"AI should be doing the laundry, not the essays."*  
- *"We don’t ask you to fill out forms—we learn from your data."*  
- *"This isn’t just a chatbot; it’s a robust memory system tailored to you."*

---

## Actionable Takeaways
1. **Download the Aro App**: Explore the data portrait feature to see how your digital footprint is used to create a personalized profile.
2. **Connect Data Sources**: Link accounts (Amazon, DoorDash, Twitter, etc.) to enable the system to learn about your habits.
3. **Edit and Refine**: Correct inaccuracies in your profile (e.g., age, interests) to improve the system’s understanding.
4. **Leverage Memory**: Use the "remember" feature to teach the system about your preferences and needs.
5. **Monitor Privacy**: Ensure transparency by reviewing how your data is used and revoked access as needed.

---

## Challenges & Notes
- **Precision Trade-offs**: The system may occasionally misinterpret data (e.g., guessing a child’s age).
- **Token Limits**: Demonstrations are truncated to avoid excessive text processing.
```

## Full Transcript

[00:00] [Music]
[00:14] good afternoon everyone God I am so in
[00:16] love with generative AI I don't think
[00:18] I've been this in love with anything
[00:19] since my 20s I was a puppy uh I love
[00:22] what swix said at the last conference he
[00:25] said we're too late to explore the world
[00:26] too early to explore space but we're so
[00:29] lucky to be alive because we're the
[00:31] generation that gets to deliver on the
[00:33] promise of AI and we're all going to
[00:35] make that promise come true for the
[00:36] world in a lot of different ways and I
[00:38] want to talk to you about one way that
[00:40] we at Aro are going to make that promise
[00:42] come true and it is by giving people
[00:44] back what I think is arguably the most
[00:47] precious commodity in the world time our
[00:51] goal at Ario is very simple it's to give
[00:53] every single person that wants it one
[00:55] hour a day back in their lives one real
[00:59] hour of things that they don't have to
[01:00] do because there's so much that we have
[01:02] to do that isn't Fun that still has to
[01:04] get
[01:05] done I love this quote that someone put
[01:08] out it's an author named Joanna I don't
[01:10] want AI to write poetry I wanted to do
[01:12] my laundry so that I can do the
[01:14] wonderful and beautiful creative things
[01:15] we love it so much that we got her
[01:17] permission to stick it on our homepage
[01:18] this I think is what captures the real
[01:21] potential of what gen can do for people
[01:24] we're going to deliver on this promise
[01:26] in a way that you've all heard about
[01:27] before but there are going to be some
[01:28] Rifts that we talk about throughout the
[01:29] uh throughout the session we're building
[01:32] an AI powerered personal assistant not
[01:35] an executive assistant for busy
[01:36] Executives that have lots of money but a
[01:38] personal assistant that helps ordinary
[01:41] people in their lives now you've heard a
[01:43] lot about that technology and that
[01:45] capability I'm going to tell you how
[01:46] ours is a little bit
[01:47] different we're announcing today that
[01:49] we've raised $16 million to make our
[01:52] version of this come true I'm going to
[01:54] tell you why thank you so much I'll tell
[01:56] you why investors are so excited about
[01:58] that our system is very simple the
[02:02] foundation of the system is something we
[02:04] call adversarial ETL the ability to get
[02:07] users data every Google search every
[02:09] Facebook post every door Dash order
[02:12] every straa run every Instagram
[02:14] everything that they do online even
[02:16] though the large systems that have that
[02:18] data don't actually want you to get it
[02:20] out I don't know how many of you have
[02:23] actually gotten a few hundred Meg of
[02:24] your data out of those systems but I bet
[02:26] that the percentage is less than 1% so
[02:28] we start with adversary seral ETL as the
[02:31] foundation of our system aggregate all
[02:33] of that user data on behalf of a user
[02:35] then we build an agent architecture on
[02:38] top of that the llm the rag data
[02:41] management we package all of that up in
[02:43] use cases that are simple and make sense
[02:45] to users that add value in their lives
[02:47] so I'm going to talk about as many of
[02:49] those components as I can in the time
[02:50] that we have remaining and before we
[02:52] dive in I want to tell you that I'm as
[02:54] tired as you are of Rosy visions of the
[02:56] future that are ultimately mirages and
[02:58] fall flat on demo day so everything that
[03:01] I'm going to show you today Works
[03:05] mostly if you try it a couple of times
[03:07] it should work for you to that end you
[03:09] can go to our IOS app in the app store
[03:12] you can take a photo of this it'll be
[03:14] online the URL is hey ao.com and you can
[03:17] download it now you can download it
[03:19] tonight and you can play with these
[03:21] capabilities so let's start with the
[03:23] very first and most important thing
[03:25] getting the data out and understanding
[03:27] the user
[03:30] I'm going to show you a few examples of
[03:31] what we do and how we orchestrate this
[03:33] data from data sources like Google
[03:35] Calendar Amazon door Dash and a few
[03:37] others two quick notes data
[03:40] privacy 100% of this data belongs to you
[03:43] it actually belongs to you whether or
[03:45] not I say it we simply acknowledge and
[03:46] respect that fact we take no rights in
[03:48] the data we never move the data it's
[03:50] your data you have full crud your
[03:52] technical people you can create it you
[03:54] can read it you can update it you can
[03:56] delete it you have full ownership of the
[03:58] data uh we will operate on it at your
[04:01] instruction to create value for you if
[04:02] you want second when you use the app I
[04:06] need to apologize in advance that
[04:08] connecting data sources is hard there is
[04:10] no easy way to deal with that from an
[04:12] authentication authorization point of
[04:13] view it is just painful but if you
[04:15] suffer through that there'll be some
[04:17] pots of gold at the end of the rainbow
[04:18] that I think are interesting with that
[04:20] said I want to show you the very first
[04:22] thing that we do after a user has
[04:24] downloaded our app and gone through you
[04:26] know one two 3 minutes or so of a little
[04:29] bit a friction in connecting their data
[04:30] sources we generate for them and this is
[04:33] my co-founder mong's application a data
[04:36] portrait so that's not a random piece of
[04:37] generative AI artwork that's a data
[04:40] portrait that represents her and
[04:42] reflects back to her things that she
[04:43] cares about and likes she loves
[04:44] photography she has an SLR in her hands
[04:46] she does drone photography she has a
[04:48] young child there toys little bikes in
[04:50] the background she's a big Avid hiker
[04:52] with her husband so all of these facts
[04:55] about who she is and how we reflect back
[04:57] to her things about her come from her
[04:59] data come from the various data sources
[05:01] that we have I'm going to take you into
[05:02] a little bit of a wall of text but
[05:04] that's what happens when you click read
[05:05] more we show the user all about
[05:08] themselves what we've learned so she has
[05:10] been taking a lot of daycare
[05:12] appointments because she has to put her
[05:13] son in daycare uh she likes going to
[05:15] Japanese restaurants with her husband uh
[05:17] she has been ordering particular things
[05:20] in door Dash from certain restaurants
[05:21] and so those kinds of things are now
[05:23] captured in her profile and can inform
[05:26] her engagement with the system so all
[05:29] all of the things that I'm showing you
[05:30] are automatically derived you can edit
[05:33] these profiles you can edit these forms
[05:35] you can correct things that we've gotten
[05:37] wrong and I'll show you a few things
[05:38] that we've gotten wrong but you also
[05:40] don't have to do that work so there's no
[05:42] intake form there's no essay there's no
[05:44] 20 questions that just immediately go
[05:46] stale when you're done it's an Ever
[05:47] evolving ever updating profile and
[05:50] understanding of you let's click into
[05:51] this one for a second there's that
[05:53] daycare thing again her son Hunter is
[05:55] really into Legos and trains she took
[05:57] him recently to the California Academy
[05:59] of art on Amazon she bought for him sand
[06:02] toys and rashguards because they're
[06:03] planning trips to the Santa Cruz or to
[06:05] the beach uh we guessed in here that he
[06:07] goes to kindergarten he's a little
[06:09] younger than that so you're a little off
[06:10] on that the Precision is hard uh and at
[06:12] the bottom her mom is trying to avoid uh
[06:15] high sugar foods because there's a
[06:16] glucose intake medical issue so these
[06:18] are the kinds of details that you pick
[06:20] up from People based on their data on
[06:21] their Google searches on the things that
[06:23] they tell the system explicitly in
[06:25] conversation and then you use these
[06:27] things to serve the user much more
[06:29] effectively
[06:30] I'm not going to take you through every
[06:31] single one of our data sources that
[06:32] would take too much time we do it with
[06:33] Amazon we do it with door Dash right we
[06:36] extract an understanding of you to build
[06:38] that profile from each data source that
[06:40] you connect we do it from your Twitter
[06:41] profile we understand what you like to
[06:43] read who you like to follow who follows
[06:45] you etc etc so there's one last
[06:48] component that's not a data source but
[06:50] it's memory based on the conversations
[06:52] that you have with the system based on
[06:54] explicit things that you tell the system
[06:56] like hey would you please remember or
[06:57] I'm interested in XYZ the system will
[07:00] remember important things about you in a
[07:02] separate section called memory that you
[07:03] can go and edit and update uh and I've
[07:05] compared this to chat GPT and I find
[07:08] that ours is a lot more robust we've put
[07:10] a lot more time and energy into tuning
[07:12] what needs to be remembered and we're
[07:14] very excited about what this enables and
[07:15] I'll show you how it comes into play in
[07:16] a minute so now we're going to move to
[07:18] demos and I'm not quite as Brave as EML
[07:21] and so all of my demos are the real
[07:22] product but they're just videos of the
[07:24] product so that I don't have to worry
[07:25] about them not working right now so
[07:27] here's the first one let's hit play this
[07:29] this is now a co-pilot example in which
[07:32] we're going to run one of the tiles that
[07:34] co-pilot likes to promote and we're
[07:36] going to run that exact same query in
[07:39] Ario so this is the tile that says
[07:41] where's a sunny warm place I can travel
[07:43] to right now co-pilot says you can go to
[07:45] B here's why it's got beautiful beaches
[07:47] you can go to Mexico you can go to Key
[07:49] West
[07:51] Florida I would call this response
[07:54] really little more than Google Plus+
[07:57] it's a natural language interface on a
[07:59] Google query that may as well say top
[08:01] war places to visit like it's fairly
[08:03] unanchored in anything that's likely to
[08:05] be highly relevant for you those are
[08:06] nice places to visit but it's just a
[08:08] sort of hodgepodge of nice places to
[08:10] visit when you run that exact same query
[08:12] in Ario you get something that's a lot
[08:14] more tuned to your interests and your
[08:16] likes and the system even tells you why
[08:19] you might want to go to Maui because of
[08:21] your love of Asian food and because of
[08:23] the activities there that are relevant
[08:24] to you you might want to go to San Diego
[08:26] because they have legol land and you've
[08:27] been buying Lego toys for your son you
[08:29] might want to go to Miami because there
[08:31] are certain things that you've been
[08:32] doing lately that match the things
[08:33] you've been doing in the Bay Area and so
[08:35] on and so forth so it's early days but
[08:38] you can see that adding a lot of
[08:41] personal data to that query allows us to
[08:43] give you far more intelligent far more
[08:46] tailored and tuned recommendations and
[08:48] we haven't really even begun next slide
[08:52] you can imagine that where this goes
[08:54] next find something that matches my
[08:57] schedule find something that harmonizes
[08:59] between Grandma my husband and me find
[09:01] something that matches my budget because
[09:03] you know what my budget is so as we add
[09:05] more and more data sources we're able to
[09:07] perform more and more sophisticated
[09:09] queries that go Way Beyond just saying
[09:11] you should go to San Diego because you
[09:13] like Legos that's fairly easy I would
[09:14] call that practically a string matching
[09:15] query but how do you get to something
[09:17] that demonstrates an understanding of
[09:19] your life and gives you much better
[09:20] results as a result of that we'll do one
[09:23] more
[09:25] example so here's a query that we ran in
[09:27] chat
[09:28] GPT versus the one that we ran in
[09:30] Ario this is one of the promoted tiles
[09:37] there oh we're having some networking
[09:40] here help me create a personalized
[09:42] morning routine so this is a failure
[09:44] mode of AI that I call 20 questions it's
[09:47] not very fun you ask a question but
[09:50] really the response is a whole series of
[09:52] questions by the time you're done
[09:53] answering all of those questions you may
[09:55] as well filled out an intake form you
[09:57] can get that kind of a recommendation
[09:58] just by going anywhere I you can go to
[10:00] uh any number of websites that offer you
[10:02] the ability to sort of create routines
[10:04] if you're willing to answer so many
[10:06] questions you run a quer like that in
[10:07] Aro and you get a much different
[10:10] response so we type that same thing in
[10:12] help me create a personalized morning
[10:13] routine that will boost my productivity
[10:19] great so you get kind of a play-by-play
[10:22] schedule 7: a.m. wake up that's tuned to
[10:25] the time that this user actually wakes
[10:27] up hydration and light stretching that's
[10:29] because there's a record of the kind of
[10:31] exercise this person does they actually
[10:32] do a small amount of exercise only 20
[10:34] minutes quick workout from 7:10 to
[10:37] 7:30 we'll keep
[10:40] going shower and get ready the food
[10:43] recommendations are based on what that
[10:44] user orders for actual food actual
[10:46] ingredients based on the things that
[10:48] they like from door Dash so you can see
[10:51] that adding in all of this personal
[10:54] context really really takes us from what
[10:56] I like to call Google+ plus to something
[10:58] that is far more relevant something that
[11:00] feels like it knows
[11:03] you I'm going to skip two of the Demos
[11:05] in the interest of time we're going to
[11:07] get to the part where you guys figure
[11:08] out how you use this we do the same
[11:10] thing in Gemini versus
[11:12] Ario I want to show you one more that we
[11:15] really like uh one of the use cases that
[11:17] we like to work on is busy people busy
[11:19] parents that are managing complex
[11:20] households and lives some of you that
[11:22] have children might be familiar with a
[11:24] schedule like this and even if you don't
[11:25] have schedules or children rather
[11:27] everyone has schedules uh you might have
[11:28] seen some something like this a lot of
[11:30] information densely packed in a single
[11:32] place you take a photo of something like
[11:34] this and you upload it into Ario and you
[11:37] get all of the information on here
[11:40] published into your calendar now that's
[11:43] just standard sort of knowledge
[11:44] extraction you've seen a lot of people
[11:45] talking about that but we marry that
[11:47] with the context of your life we know
[11:49] what all the conflicts are on your
[11:51] calendar we identify those conflicts and
[11:54] we tell you 24 hours 72 hours and 7 days
[11:57] in advance so you can kind of set and
[11:59] forget you put this large amount of
[12:00] information into the system and now
[12:02] there is an entity that's looking out
[12:04] for you all of those entries are now
[12:06] scattered across the calendar I'm going
[12:08] to show you one more little detail here
[12:09] this is so typical of schools in
[12:11] particular they publish the schedule and
[12:13] they don't even have nailed down the
[12:15] first day of school so they're going to
[12:16] tell you in email later so you sort of
[12:19] live in fear of not even being able
[12:21] being able to be sure of when the first
[12:23] day of school is and so you'll see that
[12:25] both of those calendar entries are on
[12:27] the schedule because the most important
[12:28] thing is holding them you can figure out
[12:30] which one to let go of later and oops in
[12:33] the next version uh which is going to
[12:35] roll out in the next four to six weeks
[12:37] Ario will sit in your inbox and monitor
[12:40] your email for that particular thing we
[12:42] can't broadly monitor your email yet
[12:44] that's a little hard that's a big
[12:45] problem but we're special casing one
[12:47] category of information at a time and a
[12:49] big one is where your kids are going to
[12:51] be where you need to be so things like
[12:53] scheduling things like the first day of
[12:55] school are actually going to be
[12:56] monitored in the system and then that
[12:58] incorrect calendar ENT will be
[12:59] dynamically removed you'll be notified
[13:01] and now you know so the idea is to take
[13:03] some of this unnecessary headache of
[13:06] keeping track of all this disperate
[13:07] information away from
[13:10] you so I want to share uh a couple of
[13:13] very very highlevel insights on rag that
[13:15] we've been generating as we build these
[13:18] tools out so I've shown you getting some
[13:20] data out I've shown you orchestrating
[13:22] that data on behalf of the user and I've
[13:23] shown you some use cases so rule number
[13:26] one of building tools and systems with
[13:28] llms is avoid the llm at all costs in
[13:32] other words do as much data enrichment
[13:34] as much processing as much heavy lifting
[13:36] as you can with old baked cheap Reliable
[13:40] Tools I'll give you one micro example we
[13:42] were working with Strava data which has
[13:44] a start time and an end time start the
[13:46] run at 105 p.m. end the run at 2 p.m.
[13:49] how many minutes did I run who's fast
[13:51] with math 55 minutes but there was no
[13:54] column in the Strava data that a total
[13:56] runtime so we would ask the llm how long
[13:58] did this user run and its first response
[14:00] would be oh my God it is unknowable how
[14:03] many minutes this user ran like nobody
[14:04] on Earth can figure this out and then we
[14:06] would give it an instruction we consume
[14:08] precious real estate in our prompt and
[14:10] those budgets are small we'd consume
[14:12] that real estate to say hey by the way
[14:14] why don't you try manipulating various
[14:17] columns we wouldn't say subtract column
[14:18] 17 from column 4 that's very
[14:20] prescriptive we would give it a general
[14:21] instruction like try manipulating The
[14:23] Columns and seeing if the relationship
[14:25] between them might give you a clue as to
[14:27] what the user wants and then we'll come
[14:28] back to say oh my God thank you for that
[14:30] tip that was amazing I figured out that
[14:32] I could subtract end time from start
[14:34] time and indeed you've run 55 minutes
[14:37] but this is a bad use of llm because
[14:39] that math is Trivial all kinds of
[14:41] actions that the llms can do when given
[14:44] enough subtle instructions and prompting
[14:46] are not appropriately or best done in
[14:48] the llm so we've kind of taken as an
[14:50] operating principle inside our company
[14:52] use the llm last try five ways try seven
[14:55] ways try nine ways of doing something
[14:58] before you resort to the llm there's a
[15:00] time and a place for it to do magic but
[15:02] subtracting two columns worth of data is
[15:04] not that place second search is still
[15:06] King it's uh something that we've talked
[15:08] about for such a long time you know we
[15:09] were just talking about Google in the
[15:10] earlier presentation um but everything
[15:13] really becomes a complex search problem
[15:15] as you scale and so just taking data and
[15:18] Vector embedding it just having this raw
[15:20] data available to your system doesn't do
[15:22] a good enough job so one of the things
[15:23] that we've shown you here is that we
[15:25] take raw data like the door Dash or the
[15:27] Amazon data we turn that into profile so
[15:29] we try to abstract that and we try to
[15:31] give processed and refined data to the
[15:34] llm as an input so that it can figure
[15:36] out how to strategize properly about how
[15:38] to answer the question and only go down
[15:40] into the level of raw data when it
[15:42] really needs to the more questions you
[15:44] can answer closer to the edge of the
[15:46] system closer to the llm without having
[15:48] to go all the way back to your raw data
[15:50] the better off you'll be and lastly make
[15:52] sure that you present the right data at
[15:54] the right time having a whole lot of
[15:56] data and just making that available in
[15:58] the system doesn't really produce the
[16:00] best results we spent a lot of energy in
[16:02] trying to actually avoid putting too
[16:05] much data into various parts of the
[16:07] pipeline uh which then caus the system
[16:09] to be very complicated and kind of get
[16:10] overwhelmed so I know there were a very
[16:12] high level our experts like Kieran who's
[16:14] in the audience here are going to be
[16:15] rolling out blog posts and videos trying
[16:17] to share with you as much as we can
[16:19] about the lessons we've learned along
[16:20] the way in building these things now I
[16:22] promised you that I would try to leave
[16:24] you with things that you could use on
[16:25] your own our mission in life is to
[16:28] unlock the power of user data on behalf
[16:31] of users I think this is a huge Mission
[16:33] I intend to spend the next 20 years on
[16:34] it so you can use tools like Aro boost
[16:38] without having to buy into our system so
[16:40] Aro boost is a browser extension you can
[16:42] use it in one of two ways if you want to
[16:44] use it as part of using the Aro mobile
[16:48] app that you might download from that QR
[16:49] code click the button on the left that
[16:51] says login with Aro then when you access
[16:54] your data from lots of different data
[16:55] sources it's immediately available in
[16:57] the mobile app but let's say that you
[16:58] don't trust me because you don't know me
[17:00] which is absolutely how you should feel
[17:02] you want to use it by clicking the right
[17:03] hand side button that button is
[17:05] effectively the offline or developer
[17:06] mode you just say skip logging in so if
[17:08] you skip logging in then we don't know
[17:10] who you are there is no online account
[17:11] on your behalf you can still use this
[17:13] tool to download your data from 15 or 20
[17:17] different data sources and I'll just
[17:18] give you a quick visual of what that
[17:20] looks like so we're doing this in
[17:21] developer mode we're skipping the login
[17:23] step there's no account created for you
[17:25] and you can just
[17:26] automatically enjoy the benefits of the
[17:28] adversarial ETL system that we've built
[17:31] which is logging into various systems on
[17:33] your behalf which is using screen
[17:34] scraping when possible apis when
[17:37] possible automating gdpr data downloads
[17:40] when possible using all the different
[17:42] techniques that we've learned about to
[17:43] download your data and this is showing
[17:45] you locally that data you can perform
[17:46] search on it this is showing you my
[17:47] Suter Medical Health logs in on your
[17:49] behalf and pulls those after visit
[17:51] summaries and downloads them all to your
[17:54] device so in this mode all of that data
[17:56] is on your local device it has not gone
[17:59] anywhere you can do whatever you want
[18:01] with it you can feed it up to a
[18:01] different llm you can use llama you can
[18:04] build you and your users can build you
[18:06] can do whatever you want so this is part
[18:08] of our sort of passion for helping
[18:10] everybody learn and enjoy the benefits
[18:13] of personal user
[18:15] data and that brings us more or less to
[18:18] the end uh thank you so much for your
[18:20] time today I really do want to hear from
[18:22] you that's our email and we're growing
[18:24] in all areas thank you
[18:29] [Music]
