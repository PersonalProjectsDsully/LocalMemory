---
type: youtube
title: Scaling AI in Education: A Khanmigo case study: Shawn Jansepar
author: AI Engineer
video_id: 3E7VAZaTG9M
video_url: https://www.youtube.com/watch?v=3E7VAZaTG9M
thumbnail_url: https://img.youtube.com/vi/3E7VAZaTG9M/mqdefault.jpg
date_added: 2025-05-26
category: Education and Technology
tags: ['AI', 'Education', 'EdTech', 'Essay Writing', 'Coding', 'Classroom Tools', 'Feedback Loops', 'Engagement', 'LLMs', 'Educational Innovation', 'AI Tools', 'Student Learning']
entities: ['KH Academy', 'Kigo', 'AI', 'LLMs', 'Writing Coach', 'Code Writing', 'Energy Points', 'Essay Writing']
concepts: ['AI in Education', 'Feedback Loops', 'Educational Technology', 'Essay Writing Tools', 'Classroom Integration', 'Iterative Writing', 'Engagement Strategies', 'Coding Platforms']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI in education', 'Familiarity with educational technology platforms', 'Knowledge of LLMs (Large Language Models)']
related_topics: ['AI in Education', 'EdTech Innovations', 'Essay Writing Tools', 'Coding Education', 'Classroom Technology', 'Feedback Mechanisms', 'AI Ethics in Education', 'Student Engagement Strategies']
authority_signals: ["we really think that essay writing isn't actually going to be hurt by generative AI", "the teacher will know that you've been iteratively working on that Essay with an AI"]
confidence_score: 0.8
---

# Scaling AI in Education: A Khanmigo case study: Shawn Jansepar

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=3E7VAZaTG9M)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai in education, edtech, ai tutoring, scalable ai, education technology, ai applications, khanmigo  

## Summary

```markdown
## Overview  
Shawn Jansepar, Director of AI and Learning at Khan Academy, discusses the development and implementation of **Khanmigo**, an AI-powered tutoring system designed to address learning gaps and democratize access to personalized education. The talk highlights how AI is being integrated into Khan Academy’s platform to enhance teaching methods, improve student engagement, and tackle challenges like feedback loops in writing and coding.  

## Key Points  
- **Mission of Khan Academy**: Focus on providing free, accessible education to all, with AI as a tool to scale personalized learning.  
- **Learning Gaps**: AI addresses disparities in access to one-on-one tutoring, particularly for students who rely on self-paced learning.  
- **Khanmigo Features**:  
  - **Socratic Method**: AI guides students through problem-solving without direct answers, fostering critical thinking.  
  - **Contextual Understanding**: Khanmigo analyzes student work, identifies errors, and provides targeted feedback.  
  - **Essay Writing Coach**: Breaks down the writing process into stages (outlining, drafting, revising) with AI-driven feedback.  
  - **Code Integration**: Plans to apply similar AI tools to coding education.  
- **Technical Challenges**:  
  - Specialized tools for math input, graph rendering, and essay writing.  
  - Balancing AI assistance with ethical concerns (e.g., cheating) through transparent conversation histories.  
- **Classroom Integration**: Shift from independent learners to classroom-focused tools, emphasizing teacher collaboration and student accountability.  
- **Engagement Features**: Gamification elements like "energy points" to motivate students.  

## Important Quotes  
- **Notion CEO Insight**: "UX affordances are critical in education, such as math input widgets and specialized graph rendering."  
- **Khanmigo vs. Chatbots**: "General chatbots are great, but education requires tailored interfaces for tasks like essay writing or complex equations."  
- **Essay Writing Revolution**: "AI will shorten feedback loops, enabling iterative refinement of essays—teachers may eventually require AI-assisted drafts for a 'B' grade."  
- **Cheating Concerns**: "Teachers can validate student work via conversation history, ensuring AI is a tool for collaboration, not plagiarism."  

## Conclusion  
Khanmigo exemplifies how AI can transform education by providing scalable, personalized support while addressing ethical and technical challenges. By integrating AI into core learning activities (writing, coding, problem-solving), Khan Academy aims to bridge gaps in education and empower both students and educators.  
```

## Full Transcript

[00:00] [Music]
[00:12] all right thanks so much for coming to
[00:13] my talk um yeah I'm going to talk to you
[00:14] today about how we've been scaling AI in
[00:16] the classroom um so kind of a case study
[00:18] of kigo um my name is Shan jansa I'm the
[00:20] director of AI um and learning at KH
[00:23] Academy and I've also been doubling up
[00:25] as a product leader so thankfully when
[00:27] we're trying to decide on features and
[00:29] road map I don't have to negotiate with
[00:31] anyone but myself there are other
[00:32] product managers but uh it makes that
[00:35] process a lot
[00:36] easier so today I'm going to talk about
[00:39] problems we're solving at KH Academy how
[00:41] we're solving those problems walking
[00:42] through a few demos uh how we
[00:44] transformed KH Academy into an AI first
[00:47] organization and some of the technical
[00:49] challenges solved and what we're focused
[00:51] on
[00:52] next so for those you don't know KH
[00:54] Academy is a nonprofit with a mission to
[00:56] provide a free world-class education for
[00:58] anyone anywhere we have 140 million
[01:00] registered users 7 billion learning
[01:02] minutes just in 2021 to 2022 1.5 million
[01:06] very uh very active Learners who use Con
[01:09] Academy for two hours a month and we re
[01:11] most recently we have about 200,000 paid
[01:14] conmigo Learners and teachers half of
[01:16] which are in school districts uh who are
[01:18] getting access in the classroom half of
[01:19] which who are just paying on their
[01:21] own um and we're specifically committed
[01:23] to serving historically underresourced
[01:25] Learners in our education system so we
[01:28] through our Partnerships with District
[01:29] dists tend to try to partner with
[01:31] schools who have a higher percentage of
[01:33] students who are in the free and reduced
[01:35] lunch category so we're really trying to
[01:37] you know reach the students who um
[01:39] normally don't get access to this type
[01:41] of technology and
[01:42] education and since the pandemic
[01:44] outcomes have been worse than ever so
[01:47] quickly this is just a kind of graphic
[01:49] showing you that over time in the third
[01:51] grade students are largely grade level
[01:52] proficient but by the time they get to
[01:54] the eth grade the average student is 1.1
[01:57] grade levels behind so we believe AI can
[02:00] be used to successfully fill those
[02:02] unfinished learning gaps at at scale by
[02:05] democratizing one-on-one tutoring for
[02:07] anyone
[02:08] anywhere so that's where kigo comes in
[02:10] it's our tutor for Learners and it's our
[02:12] assistant for
[02:13] teachers and just to even taking a step
[02:16] back for a second emulating tutors has
[02:18] really actually been our North Star the
[02:20] entire time but thus far we've been
[02:22] limited by the technology we've been
[02:23] doing you know self-paced video
[02:25] self-paced practice s famously said in
[02:27] his Ted Talk that his cousins preferred
[02:29] the automated version of their cousin to
[02:31] their real cousin and llms for us are
[02:33] just kind of a tool that help us
[02:34] accelerate towards that Vision we're
[02:36] really not just trying to use AI for AI
[02:39] sake so how are we using AI to solve
[02:41] tutoring and teaching assistance at
[02:43] scale there was a really great quote
[02:45] from notion CEO where they mentioned
[02:47] that this is as much of an interface
[02:49] Revolution as it is a technology
[02:50] Revolution and they are really good at
[02:52] interfaces we think it's the same for us
[02:54] but we're really good about building
[02:56] educational technology at scale for
[02:58] millions of Learners around the world
[03:01] so I'm not going to go through this
[03:02] whole list but just generally things
[03:03] we're doing building a Socratic tutor
[03:05] that doesn't give away answers optimizes
[03:07] for the accuracy of math is context of
[03:09] where of your work and is deeply
[03:11] integrated into our content multilingual
[03:13] text of speech Etc so I'm going to go
[03:15] into some screenshot so one example here
[03:17] is just comparing kigo to chat GPT and
[03:21] you'll notice in this screenshot that
[03:24] here there's just kind of this diving
[03:26] into all right you asked me a question
[03:28] I'm going to give you the answer which
[03:29] can be great if you're an older learner
[03:31] and you know how to learn but as
[03:33] Learners in the classroom we don't want
[03:34] students just getting access to the
[03:36] answer we want them to think about it
[03:37] deeply we want a more of a Socratic
[03:39] method where you're asking leading
[03:41] questions to help guide you to the
[03:43] answer so you'll notice here kigo didn't
[03:45] way give away the answer it's asking
[03:47] leading questions and then on the math
[03:50] accuracy front you'll notice that chat
[03:52] GPT said you correctly distributed
[03:54] negative4 in fact in this example you
[03:57] did not correctly distribute negative4
[03:59] it was incorrect but kigo is noticing
[04:02] that uh it notices that there was a
[04:04] small mistake in the distribution and
[04:06] then it kind of back it backs up and
[04:07] tries to help you from
[04:09] there so we're also been doing a lot to
[04:12] kind of embed kigo directly into our
[04:15] platform and into our content so you can
[04:17] immediately just say hey tutor me I got
[04:19] this wrong and then kigo past the
[04:21] context in of it has the full
[04:23] understanding of what this question is
[04:25] what is what is the step-by-step
[04:26] solution what is the uh thing that you
[04:29] entered and then it'll anal analyze Your
[04:31] solution and help you with it maybe give
[04:34] you helpful tips as to why you might
[04:35] have landed there um so that's kind of
[04:37] after you got the question wrong before
[04:39] you get the qu before you submitted the
[04:40] question we wouldn't just dive into
[04:43] this um things you know General chat
[04:45] Bots are great but there's a lot of ux
[04:47] affordances that are always that's very
[04:49] important for Education things like
[04:51] having a great math input widget for
[04:53] doing complex equations um specialized
[04:55] graph rendering Etc and then also ux for
[04:59] uh use case is like essay writing which
[05:00] I'm going to dive into so we've been
[05:02] thinking about how do we go beyond just
[05:04] that traditional chat interface um I'm
[05:07] sure you all have kind of had the
[05:09] experience when you were writing essays
[05:10] in grade school you wrote that essay
[05:12] your teacher marked it there's some red
[05:13] ink on it you never probably reviewed
[05:16] that essay again you moved on what I
[05:18] think that education or what I think
[05:20] llms can do in education that is going
[05:22] to revolutionize the way we think about
[05:24] it is that it's going to help us shorten
[05:26] feedback loops there's never going to be
[05:27] a situation maybe where in the future
[05:30] you won't be able to submit an essay
[05:31] unless it's at least a b because the
[05:33] teacher will know that you've been
[05:35] iteratively working on that Essay with
[05:37] an AI and so I know there's a lot of
[05:39] concerns about cheating so I'll talk
[05:41] about that in a second but this is just
[05:42] kind of like an early preview into our
[05:44] writing coach so it kind of breaks down
[05:46] the essay writing process into these
[05:48] different categories so in this example
[05:50] here you're outlining an essay with a AI
[05:53] directly and you might have questions
[05:55] about how to write that thesis but it
[05:57] won't let you move on until you've
[05:59] written a pretty strong thesis and it'll
[06:00] give you that feedback along the way and
[06:02] then there's drafting the actual meat of
[06:05] the essay from there you can kind of ask
[06:07] helpful for helpful tips but if you ask
[06:09] it to write the next paragraph for you
[06:10] it'll
[06:11] refuse and then there's that last step
[06:14] around revision so it'll give you
[06:15] feedback on axes of evidence structure
[06:18] style and tone and
[06:20] conclusion and then this is where things
[06:22] get really interesting with the teacher
[06:23] so the teacher now has full access to
[06:25] the history of what you built with the
[06:28] AI to kind of validate that you were the
[06:30] one who wrote that with the AI and it
[06:31] wasn't just something that you copied
[06:34] and pasted from chat upbt so you can
[06:35] kind of get a sense of that by looking
[06:37] at the conversation history um we're
[06:39] building kind of these replay
[06:40] functionalities and then it'll also say
[06:42] like hey these you know these 54 or the
[06:44] 56 words just show showed up out of
[06:46] nowhere so we really think that essay
[06:49] writing isn't actually going to be hurt
[06:50] by generative AI but we are really going
[06:52] to revolutionize the way that
[06:55] works similarly for code we also have a
[06:57] coding platform and we're planning on
[06:58] doing the same for code writing at some
[07:01] point we're also building a lot of fun
[07:03] engagement things uh students love this
[07:05] kind of stuff you know you can reclaim
[07:06] energy points to customize kigo um but
[07:09] then there's integration into the
[07:11] classroom so you know one of the reasons
[07:13] why KH Academy started focusing on
[07:14] classrooms instead of just focusing on
[07:16] Independent Learners who find us on
[07:17] Google is because kids who come to us on
[07:20] Google it's great but you have to care
[07:22] enough about learning to come to KH
[07:24] Academy in the first place we really
[07:25] wanted to reach those kids who thought
[07:27] they were bad at math who hated learning
[07:29] and so it's important for KH Academy to
[07:30] be integrated into the classroom and
[07:32] have that tight feedback loop between
[07:34] what the student is doing and so that
[07:35] the uh with the teacher so that the
[07:37] teacher can get insights into that so
[07:40] for instance we have a moderation
[07:42] feature where if any conversation is
[07:44] kind of going off the rails is
[07:45] inappropriate an a teacher will be
[07:47] flagged and notified so we kind of tried
[07:49] to do a things when we were launching
[07:51] kigo uh to turn some of the fears into
[07:53] actual
[07:55] features um this is an example of a
[07:57] classroom snapshot where a teacher can
[07:59] say hey how's my class doing and because
[08:01] it has access to all of that rich data
[08:03] about the usage of con con Academy in
[08:05] the classroom it'll give you that
[08:07] overview and it'll also um give you the
[08:10] ability to kind of dive into skills
[08:12] reports and dive deeper into our graphs
[08:14] and then from there as a teacher you
[08:16] might be able to do things like hey I
[08:17] want to write a progress report to
[08:19] Reese's family that's going to save you
[08:21] a huge amount of time because all this
[08:22] data is directly
[08:25] available we built a ton of other
[08:27] teacher tools things like lesson
[08:28] planning uh exit tickets Etc I would
[08:31] have Lov to demo them but there's not
[08:32] enough time uh huge shout out to
[08:34] Microsoft they recently sponsored us
[08:36] bringing these teacher tools to all us
[08:38] teachers in the states and soon around
[08:40] the world for free um so feel free to
[08:42] check it out anyone can sign
[08:45] up and oh actually I need to plug in the
[08:50] audio instead of kind of talking about
[08:53] the results in the classroom I thought I
[08:54] would just do a quick fun video showing
[08:56] how that's going
[09:00] how
[09:07] love Miss D's class was so much fun
[09:10] students in this class were opening up
[09:12] their imaginations writing stories
[09:14] learning about history and they learned
[09:16] about America's first
[09:19] president they
[09:21] learned to but it's not going to give
[09:24] you the answer
[09:42] everybody
[09:44] clue sixth grade class one thing was for
[09:47] sure kigo was here to help with
[09:50] personalized learning and adap feedack
[10:18] C all right so I want to dive a little
[10:22] bit into how we built kigo and how did
[10:25] we transform KH Academy into an AI first
[10:27] organization um you know it didn't
[10:29] happen overnight so you know first we
[10:33] kind of wrote up some requirements about
[10:34] like what would the perfect AI tutor and
[10:36] assistant what would that be we
[10:38] estimated the work then we wrote up this
[10:40] n's Gant chart of the
[10:42] timeline just kidding we didn't do any
[10:44] of that uh the keys to Our Success were
[10:48] really rapid prototyping and iteration
[10:51] um actually there's a great book that I
[10:52] highly recommend it's called creative
[10:53] selection um it was about how the uh
[10:55] iPhone was created um really kind of
[10:58] driven through this process of iterative
[11:00] development um driving it through demos
[11:02] and you know feeding the demos that do
[11:05] really well and you know putting an end
[11:06] to the demos that don't do really well
[11:08] and I think what we really learned is
[11:09] that magic really comes from when you
[11:11] pair incredible Builders with domain
[11:14] experts who have some unique insight and
[11:16] ideally really these should be members
[11:18] of your team who deeply understand the
[11:19] customer you're building for as opposed
[11:21] to maybe just sending things off to an
[11:23] R&D team at least that's been in our
[11:26] experience uh the history of our open AI
[11:28] partnership so it actually all started
[11:30] when open a needed some AP Bio questions
[11:32] to test their new model uh we got a
[11:34] first sneak peek in September and then
[11:36] in December actually between September
[11:38] and December we didn't have much Headway
[11:40] it was a lot of like well what are you
[11:41] doing what are you doing and then we
[11:43] said you know what let's just do some
[11:44] rapid prototyping together and Red Team
[11:46] um and then we narrowed down on a few
[11:48] use cases and then once we decided that
[11:50] we really liked the way that this tutor
[11:52] felt in our platform we said hey let's
[11:54] try to launch something alongside of gp4
[11:56] but let's do a companywide hackathon to
[11:58] build a lot of new feature see what the
[11:59] team can come up with the best ideas
[12:02] from there won we tried to ship those
[12:04] with gp4 in our launch in March um and
[12:07] then we also participated in
[12:08] reinforcement learning where a few
[12:10] members of our content team were
[12:11] embedded within um with open AI to kind
[12:14] of train it on 100 uh math tutoring
[12:17] examples so I would say some keys to Our
[12:20] Success one is that we resisted
[12:22] perfectionism which I would call an
[12:24] issue of Con Academy of the past we
[12:26] didn't let perfect be the enemy the good
[12:28] uh we made quick decisions for what we
[12:30] would call two-way door decisions things
[12:31] you can reverse but for oneway door
[12:33] decisions things like trust and safety
[12:35] we thought deeply about those problems
[12:37] um we trusted our intuition we leveraged
[12:39] expertise if learning scientists um and
[12:42] Educators uh kind of wanted to kind of
[12:45] work through that with us instead of us
[12:47] trying to AB test every single decision
[12:49] and then we also iterated rapidly I
[12:52] mentioned that with demo driven
[12:53] development and then we also kind of had
[12:54] some fixed timelines to avoid
[12:56] Parkinson's law where work can fill all
[12:58] of able space we also ended up driving
[13:02] forward what we called at KH Academy we
[13:03] have this process called architecture
[13:05] decision records and then more recently
[13:07] transition that to organization decision
[13:09] record so when we have like a big
[13:11] strategic shift at Khan Academy or a big
[13:12] process change at KH Academy we document
[13:15] what is the problem we're trying to
[13:16] solve who is the driver who is the
[13:18] approver who's contributing and then
[13:20] once we've kind of written that all out
[13:22] we share that with the team so that they
[13:23] can digest it at their own time and Pace
[13:25] but what we did was we changed some of
[13:27] our con Academy core values so take a a
[13:29] stand we added trusting our intuition um
[13:31] we added resisting perfectionism to
[13:33] deliver wow so that that could kind of
[13:35] trickle down in the way we do
[13:36] performance reviews Etc with the team
[13:38] and how we hire and then we also did a
[13:40] big change to our product development
[13:42] process so I'm sure this is probably a
[13:44] tale that many of you have experienced
[13:45] but we had an old process that we would
[13:47] consider agile you'll notice that all
[13:49] these circles on the left you know they
[13:51] feel great there's a lot of arrows
[13:52] moving in certain directions they look
[13:54] like you can go backwards but end then
[13:56] up being being a very heavyweight
[13:57] process a lot of like heavy
[13:59] documentation you had to write for every
[14:00] single feature Etc which makes sense
[14:03] when you're building something I think
[14:04] that you know you're just going to ship
[14:05] to all users and it has to be high
[14:07] quality but in our case we were doing a
[14:09] lot of prototyping um and so we kind of
[14:11] created this new process around there's
[14:13] a different level of quality of your
[14:15] code that you should write depending on
[14:17] your confidence in the fature so if
[14:19] you're not very confident and you're not
[14:21] sure that's just a prototype go build it
[14:23] be Scrappy uh if it's a kind of you're
[14:26] somewhat confident then maybe build it
[14:28] as AB test or to beta test it with a few
[14:32] subset of users and then if you feel
[14:34] really confident in it and you're going
[14:35] to share it with all users that's when
[14:37] the quality of the code needs to be
[14:38] higher we have some checklists for that
[14:40] that people have to kind of go through
[14:41] there's a higher level of accessibility
[14:43] required when you get to that stage Etc
[14:45] but then as long as you're following
[14:47] this framework different teams are
[14:49] empowered to kind of build software in
[14:51] the way that makes sense for them as
[14:52] opposed to having a one- siiz fits-all
[14:54] for every
[14:55] team we also added a AI platform team as
[14:58] kind of a glue between our
[14:59] infrastructure team and product team so
[15:01] there was obviously just a lot of AI
[15:02] platform team chat so I think a lot of
[15:04] this is familiar but it's really this
[15:05] team that owns the AI developer and
[15:07] prompt engineer experience of kigo um so
[15:10] for example we recently built this
[15:11] component interface in go that when you
[15:14] as a developer conform to that component
[15:15] interface it automatically think means
[15:18] that things like tracing and Lang fuse
[15:19] are available as long as you can form um
[15:22] they own things like the AI router so
[15:23] that you as a product team don't have to
[15:25] worry about that it just kind of is
[15:27] transparently taken care of for you uh
[15:29] we have a chat component um that has to
[15:32] have apis and be extensible for product
[15:34] teams and it's also a team that will
[15:36] consult with other product teams when
[15:38] they're building features if they need
[15:39] some some help and expertise as well as
[15:41] what we're kind of tentatively calling
[15:43] kigos a service where we're trying to
[15:45] work with thirdparty companies to embed
[15:47] kigo into their products instead of them
[15:49] having to rebuild a brand new tutor from
[15:53] scratch so what are some of the
[15:54] technical hurdles uh what were some of
[15:57] our technical hurdles that we over came
[15:59] and what are the challenges
[16:01] ahead so on the tutor accuracy side
[16:04] things we've done introduced a math
[16:06] agent so we kind of give the AI the
[16:08] autonomy to defer to a math agent to
[16:11] work through problems you know get
[16:12] access to a basic calculator or you know
[16:15] python might do some more advanced
[16:16] things if it's a more advanced math
[16:18] problem um we're doing something called
[16:20] Chain of Thought prompting so it's not
[16:22] just going directly to the model and
[16:23] saying you know help the student we're
[16:25] actually doing things like we have this
[16:29] process that will say write out how a
[16:31] how you think the student might have
[16:32] arrived at that answer write out how you
[16:35] think it should have arrived at that
[16:37] answer and then it kind of feeds that
[16:39] package over to another call to the AI
[16:42] that supplies that and says using this
[16:44] context how would you tutor that student
[16:46] we noticed that that helped um improve
[16:48] the performance
[16:50] dramatically um we've been providing it
[16:52] with additional context like Steps
[16:53] step-by-step Solutions additional
[16:55] context via Rag and we've also been
[16:58] building this tutoring accuracy
[17:00] dashboard monitor uh to monitor quality
[17:02] over time so we can kind of get a sense
[17:04] of as we're shipping new changes to our
[17:07] prompts as we're upgrading models as
[17:09] we're you know making any change we can
[17:11] make sure that a we don't have any
[17:12] regressions to the math quality because
[17:13] that's a really key part of this
[17:16] experience for Learners and we also can
[17:18] you know ultimately just make sure we're
[17:20] trending in the right
[17:23] direction in terms of next steps one
[17:25] thing that we're about to launch very
[17:26] very soon um is a math accuracy
[17:29] Benchmark data set so right now when you
[17:31] look at data sets that different model
[17:33] providers are grading against it's often
[17:35] you know is it good at doing math is it
[17:37] good at reasoning but there's nothing
[17:38] that says how do I grade whether or not
[17:40] this is an accurate tutor so we're going
[17:42] to be releasing that with a paper
[17:44] shortly um we're also looking into
[17:46] integration uh with tools like Wolfram
[17:48] for some of the more complex math and
[17:50] then fine-tuning as
[17:54] well so prompt engineering It's been a
[17:58] Jing so where we started was a lot of
[18:01] hacking together prompts really really
[18:03] quickly lots of spaghetti code I'm sure
[18:05] that's the same at a lot of your
[18:07] organizations um we had a kind of varied
[18:10] test coverage depending on the activity
[18:12] so again we had a lot of really good
[18:14] test coverage for the math portion of it
[18:16] how good does it do at math tutoring but
[18:18] we had a lot of other activities that we
[18:19] were just like testing ideas and
[18:21] throwing things at the wall and see if
[18:22] they stuck so things like you know talk
[18:24] to a historical figure we didn't really
[18:25] have any test cases for that when we
[18:27] wanted to iterate on models it was
[18:28] really just you know somebody on our
[18:30] team who knew it well enough that would
[18:31] just go in and test
[18:33] it and a lot of it was also just looking
[18:36] in logs uh for completion calls when we
[18:38] had to debug a particular scenario that
[18:39] was a failure case that we wanted to
[18:41] dive deeper
[18:43] into where at now is we've refactored
[18:46] that code using the component
[18:47] architecture that I mentioned earlier so
[18:49] you can kind of have clearly defined
[18:50] inputs and outputs and it makes it a lot
[18:52] easier to test and know like what are
[18:54] sub pieces of the code that are worth
[18:56] testing um actively developing a kind of
[19:00] minimal viable uh test coverage Suite
[19:02] across all of our activities so we have
[19:04] a broad enough set of
[19:06] coverage and we have tools uh to run
[19:09] these manual test cases really quickly
[19:10] but still with humans in the
[19:12] loop um and then we're also trying to
[19:14] move in more towards in the direction of
[19:15] model graded evals to quickly Test new
[19:18] models but of course some of that's not
[19:20] possible without humans on the loop so
[19:21] it really depends on the
[19:22] scenario and then also I think I
[19:24] mentioned this already all stack traces
[19:26] are now available in Lang fuse if you
[19:28] want to go and see what happened you can
[19:29] kind of go in look through that you know
[19:31] stack trace and um debug from
[19:35] there in terms of next steps this is not
[19:38] something we necessarily have an answer
[19:39] around but we we're looking for
[19:41] continued ways to get more reliable
[19:43] model graded evals um roughly we find
[19:46] that when we label things ourselves
[19:48] compare it to the you know what the
[19:50] model will grade if we're doing things
[19:52] like was there any you know math
[19:53] mistakes in this uh the AI is catching
[19:56] it roughly 70% of the time
[19:59] and we also want to add a lot more
[20:00] languages but you know how do we do that
[20:02] without Bloom uh ballooning the test and
[20:05] iteration complexity it's there's
[20:06] probably not going to be a way to do
[20:08] that but we'd like to reduce that
[20:11] complexity and then in terms of this is
[20:13] the last one in terms of scale
[20:14] performance and cost we need kigo to be
[20:17] reliable enough for teachers and
[20:18] students to use it daily cheap enough
[20:20] for lower income districts to afford it
[20:22] and fast enough such that it doesn't
[20:24] lead to user
[20:25] frustration so things we've done so far
[20:27] is leveraging multiple models in
[20:29] production for different workflows uh
[20:31] fall back to Shared capacity when we're
[20:33] reaching limits on our dedicated
[20:35] capacity and continuing to do things
[20:37] like perceived performance improvements
[20:39] like if you notice in this uh bottom
[20:41] screenshot we added this UI when we
[20:43] actually added a few change to the
[20:45] experience that made it slower and I
[20:46] said to the team we can't ship this
[20:48] unless we add a perceived perform
[20:50] performance improvements change so that
[20:51] users know that something's happening
[20:53] here and anecdotally somebody on our
[20:55] team said hey after we shipped that my
[20:58] my kid was was using it and I said do
[20:59] you think it feels slow and that person
[21:01] that person's kid said no I don't think
[21:03] so comigo is doing math so that was a
[21:07] win and then another one is just we have
[21:09] gotten a sizable donation from Microsoft
[21:11] um of azure llm compute to bring con
[21:14] free to all teachers so that's obviously
[21:15] helping as
[21:17] well in terms of next steps uh we're
[21:20] planning on doing things like load
[21:21] balancing between open Ai and Azure for
[21:23] redundancy um we want to evaluate more
[21:26] efficient models we're in the middle of
[21:27] evaluating models like GPT 40 as well as
[21:29] small language models like fi 3 and
[21:31] actively kind of working with Microsoft
[21:33] on F3 they're building what they're
[21:35] calling F 3.14 which is a small to
[21:38] medium siiz um language model that's
[21:41] optimized for math
[21:43] tutoring and we also want to get to a
[21:45] point where we can dynamically scale up
[21:46] and down depending on our needs uh when
[21:49] we launched kigo we needed more
[21:51] throughput than open AI could offer on
[21:54] the shared capacity and we wanted faster
[21:56] performance so we ended up moving
[21:57] towards a dedic ated instance but you
[22:00] know that dedicated instance is great we
[22:02] need to provision it for the Peaks but
[22:04] it's not doing a whole lot at night so
[22:06] ideally we're we're making more
[22:08] efficient use of our
[22:10] compute that's pretty much it I just
[22:12] challenge us all to leverage artificial
[22:13] intelligence to help us enhance human
[22:15] potential and human intelligence thank
[22:18] you
[22:23] [Music]
[22:28] oh
[22:31] [Music]
