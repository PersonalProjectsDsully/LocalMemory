---
type: youtube
title: GitHub Next Explorations: Rahul Pandita
author: Channel Video
video_id: 1oySeF37SZc
video_url: https://www.youtube.com/watch?v=1oySeF37SZc
thumbnail_url: https://img.youtube.com/vi/1oySeF37SZc/mqdefault.jpg
date_added: 2025-05-26
category: AI and Machine Learning in Software Development
tags: ['GitHub', 'AI coding', 'code editing', 'GitHub Copilot', 'Python', 'software development', 'machine learning', 'IDE tools', 'code completion', 'task automation', 'AI tools', 'developer workflows']
entities: ['GitHub Copilot', 'Next Edit Suggestions', 'GitHub Next', 'Python program', 'code completions', 'IDE', 'task completions', 'model fine-tuning', 'internal dog fooding']
concepts: ['AI-driven code editing', 'code completion', 'task completion', 'model training', 'software development workflows', 'user interface design', 'exploratory research', 'code documentation', 'machine learning integration']
content_structure: overview/explanation
difficulty_level: intermediate
prerequisites: ['Familiarity with GitHub Copilot', 'Basic understanding of code editing', 'Knowledge of AI/ML concepts in software development', 'Experience with Python programming', 'Familiarity with IDEs']
related_topics: ['AI in software development', 'code completion tools', 'machine learning model training', 'software development practices', 'code editing innovations', 'GitHub ecosystem', 'natural language processing in coding', 'developer tooling trends']
authority_signals: ['We are still experimenting with a bunch of other stuff...', 'We learned from them and will keep that learning...', 'This is what this exploration is we call it next edit suggestion...']
confidence_score: 0.85
---

# GitHub Next Explorations: Rahul Pandita

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=1oySeF37SZc)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: artificial intelligence, machine learning, software engineering, github copilot, ai development, code tools, future of software  

## Summary

# GitHub Next Explorations Summary

## Overview  
Rahul Pandita from GitHub Next discusses the team's role in experimenting with AI-driven tools to enhance software development. The group focuses on prototyping, testing, and iterating on ideas before integrating them into products. Key examples include **GitHub Copilot** and its evolution, with a focus on improving code editing suggestions and task completion. The session highlights the importance of exploration, learning from failures, and adapting to user needs.

---

## Key Points  
- **GitHub Next's Role**: A research team that experiments with AI tools, shares learnings with product teams, and prototypes ideas for future integration.  
- **AI as Electricity Analogy**: AI is compared to electricity—initially seen as a niche tool but now transformative, requiring long-term exploration (e.g., 40 years of electric motor development).  
- **Experimentation Process**:  
  - Rapid prototyping, dog-fooding (internal testing), and iterative refinement.  
  - Examples: **Copilot 4 CLI**, **Copilot Voice**, **GitHub Block Spec Lang**, and **Copilot Edit Suggestions**.  
- **Copilot's Evolution**: Started as an experiment, now a core product, with ongoing work on improving editing capabilities.  
- **Next Edit Suggestions**: A project to help users edit code more efficiently by suggesting changes across multiple locations, not just code completion.  

---

## Quotes & Insights  
- **"What if Ghostex could be more intelligent?"** (Rahul Pandita)  
- **Andrew Ng's analogy**: "AI is the new electricity."  
- **GitHub Next's Charter**: "We are still experimenting with a bunch of other stuff..."  
- **Key Challenge**: "Fine-tuning models specifically for this use case to ensure accuracy and usefulness."  

---

## Actionable Items  
1. **Experiment Rapidly**: Test ideas early and often, even if they fail (e.g., shelved projects like "Copilot Block Spec Lang").  
2. **Improve Modality**: Explore alternative ways to present suggestions (e.g., viewport visibility, non-open files).  
3. **Model Fine-Tuning**: Prioritize accuracy for specific tasks like code editing.  
4. **Dog-Fooding**: Ensure internal testing meets quality standards before public release.  
5. **User-Centric Iteration**: Adjust based on feedback (e.g., Copilot's shift from code completion to editing suggestions).  

--- 

## Future Plans  
- **Next Edit Suggestions**: Expected as a standalone tech preview or integrated into existing products within the next few months.  
- **Task Completion Tools**: Expanding beyond code completion to broader development tasks.

## Full Transcript

[00:00] [Music]
[00:13] my name is Rahul Panda and I am a
[00:16] researcher at GitHub next uh and today
[00:20] we're going to talk about some of the
[00:21] GitHub next
[00:22] Explorations uh now before we begin who
[00:25] among you have heard of GitHub
[00:27] next oh cool quite a few of you that's
[00:30] will make it go much easier and much
[00:32] faster all right for those of you who
[00:34] don't know us we are uh about 20 bunch
[00:38] of researchers senior level uh
[00:41] developers and mostly code build uh tool
[00:43] Builders uh who work outside of the
[00:47] regular product uh and Report directly
[00:50] to our CEO uh and that's by Design and
[00:53] and our goal is to explore the future of
[00:56] software engineering like you all are
[00:57] doing in in your day-to-day jobs
[01:01] and the and and the reason for exploring
[01:04] that is that like once we do our
[01:05] Explorations we toss it on and we pass
[01:08] it on our learnings to the product and
[01:10] development teams so that they can build
[01:11] really compelling products like the
[01:13] co-pilot that you all have used
[01:15] hopefully at some point of time as an
[01:17] aside uh for people who are following us
[01:20] on Twitter uh I don't look anything like
[01:23] my picture over here I'm the one in the
[01:25] green background but we do have Devon in
[01:28] our team he's not an automated AI he's a
[01:30] very real person and he looks exactly
[01:32] like the person on the top right corner
[01:33] on that slide all right since we have
[01:37] gotten that out of the way let's talk
[01:39] about let's get back to the future of
[01:41] software engineering with regards to gen
[01:43] geni so here's what Andrew ning uh who
[01:47] single-handedly trained a whole
[01:49] generation of machine learning Engineers
[01:52] uh has to say about uh AI that it's just
[01:56] as electricity it's a new electricity
[01:58] it's going to transform the software
[02:00] development and almost every other field
[02:02] just like electricity did 100 years
[02:05] ago so what does that mean here's a
[02:08] picture of what a manufacturing facility
[02:11] looked like before electrification there
[02:14] used to be a giant uh mostly coal
[02:17] powered steam turbine or steam engine
[02:19] located centrally which used to turn
[02:22] these giant uh giant shafts which will
[02:25] turn these auxiliary shafts so forth and
[02:27] so on and individual workers would
[02:29] connect to these shafts using the belt
[02:30] and police system right and and these
[02:33] engines were like really really huge so
[02:35] so it was the workers the whole
[02:37] architecture of the factory was designed
[02:39] around this steam engine and and the
[02:42] whole workflow was around the steam
[02:43] engine and and it was the workers who
[02:48] were working around the technology
[02:49] rather than the technology working for
[02:52] people right and along in 19 uh 1880
[02:56] came these electric motors uh and and
[02:58] they had the potential to
[03:00] revolutionize uh the the manufacturing
[03:02] sector why because unlike steam engines
[03:06] or steam uh Motors they retained their
[03:09] efficiency when they were smaller right
[03:12] so so you could basically redesign the
[03:15] entire Factory floor plan so you would
[03:17] think that wow this is great and
[03:18] everyone would jump on this but it was
[03:20] not until n 1920s where these became the
[03:25] mainstream so early 1880s to late 1920s
[03:29] what was happening for about these 40
[03:31] years what was happening was exploration
[03:34] and experimentation people were trying
[03:36] to figure out uh how to use this
[03:39] technology how to make it better how to
[03:41] drisk it to a point
[03:44] that that the use of this technology
[03:47] becomes the norm rather than the
[03:49] exception and that's what we do at giab
[03:52] next right our Charter is to explore the
[03:55] future of software engineering and with
[03:57] the emphasis on the word explore right
[03:59] because if we knew what the future of
[04:01] software engineering in context of AI
[04:03] looks like we would just build it that's
[04:04] more efficient but unfortunately we do
[04:07] not so what we have to resort to is
[04:09] exploration we just try out different
[04:11] things rapidly prototype experiment and
[04:13] figure out whether something works or
[04:15] not and if it works then we put it out
[04:18] in front of our customers uh in in users
[04:20] and we learn from them and then we
[04:22] finally transform into a product often
[04:25] times an idea begins as inside our next
[04:29] uh as a functional prototype which goes
[04:31] through heavy dog fooding inside the
[04:33] next team if it survives that then we
[04:36] move on to the next level of dog fooding
[04:38] that is inside the company if it
[04:39] survives that then we move on to the
[04:41] next level which is releasing it as a
[04:43] tech preview uh to early adopters we
[04:46] learn from that if it survives that then
[04:48] it may have a chance to become a product
[04:50] like that a product in the future and we
[04:52] can kill or we can shell any of these
[04:54] exploration at any point of time if we
[04:56] are not getting the right signal so that
[04:57] we can explore other
[05:00] areas we did that with the co-pilot so
[05:04] yes co-pilot started off as a NYX
[05:06] experiment and since that we have
[05:08] created many other experiments like
[05:10] co-pilot 4 CLI co-pilot voice GitHub
[05:12] block spec Lang so forth and so on a lot
[05:16] of these have transformed into a product
[05:17] of their own so you can see some of them
[05:20] as a g of product offerings a lot of
[05:22] them have been absorbed into existing
[05:25] products uh and and you will see them as
[05:28] a part of the existing products and a
[05:30] significant number of them have been
[05:32] shelled we've learned what we learned
[05:33] from those experiments and figured out
[05:35] that this is not the right time for that
[05:36] kind of exploration or the exploration
[05:38] itself was flawed so but we learned from
[05:41] them and we will keep that learning and
[05:43] use that in our next uh next
[05:47] Explorations so that was an overview of
[05:50] giab next and today I'm going to talk
[05:51] about two specific Explorations uh one
[05:55] is the next edit suggestions in the
[05:56] co-pilot workspace that are currently
[05:58] active uh from from G next perspective
[06:01] and uh specifically I'm talk I'm going
[06:03] to talk about what their motivations was
[06:05] and and how they came to be and what are
[06:07] the future plans for that so first off
[06:10] uh copilot next edit suggestions right
[06:13] so what if it started off with this
[06:15] question what if ghostex could be more
[06:18] intelligent right so we all know what
[06:21] copilot doeses uh it provides you the
[06:23] code completions in your current context
[06:26] right while it's like really really good
[06:28] at cre creating new code but that's not
[06:31] what we all do right we we we almost
[06:35] always edit existing code which involves
[06:38] uh editing adding deleting lines at
[06:40] multiple locations in a program right
[06:43] what if ghostex was good as that as well
[06:46] and that's what this exploration is we
[06:48] call it next edit suggestion which
[06:50] provides you suggestions not only at the
[06:52] current cursor level but provides you
[06:53] suggestions what else needs to change in
[06:55] a program but enough talking let's jump
[06:59] on to a
[07:01] demo all right here I am going to add
[07:04] this parameter in this Python program
[07:07] and the next edit suggestion
[07:08] automatically picks it up and says that
[07:10] hey you need to update your method
[07:12] definition once we update the method
[07:13] definition it says that hey you need to
[07:15] add these uh these these arguments and
[07:18] once that has been updated then it will
[07:20] go back and say hey uh now the code
[07:23] document uh is not is not in line with
[07:26] what the code is actually doing and it
[07:27] goes ahead and edits that and updates
[07:29] that as well and the same thing repeats
[07:32] when I add one more uh
[07:38] parameter all
[07:40] right so that was copilot next's uh edit
[07:44] suggestions experiment uh we are we're
[07:46] still not ready yet we are still uh
[07:49] experimenting with a bunch of other
[07:51] stuff like you know uh is the ghost Tex
[07:53] completion the right U modality for it
[07:56] or do we need to figure out a different
[07:58] different way of presenting those
[08:00] suggestions what if the location of the
[08:03] next edit is not visible in the current
[08:05] viewport or what if the location is in a
[08:09] file that is not even open in an editor
[08:11] uh most importantly we are also working
[08:13] on fine-tuning the models specifically
[08:15] for this use case the idea being that
[08:17] like if we want the next edit
[08:19] suggestions to be uh accurate and we
[08:21] want it to be very useful then the
[08:23] suggestions needs to be on point and
[08:26] once we are done with these further sub
[08:28] explorations and we feel that it has
[08:30] gotten through our internal dog fooding
[08:32] standard next edit suggestions would be
[08:34] coming out either as a standalone uh
[08:37] Tech preview from next or as a part of
[08:39] an existing next product uh sometime in
[08:41] your IDE uh in next few
[08:44] months all right so there was code
[08:47] completions but let's move from the code
[08:49] completions to the task completions SL
[08:51] uh why do you ask why Why move from the
[08:53] task completions it just turns out uh
[08:56] that while code is like an important
[08:59] artifact uh that comes out of software
[09:01] development but it's not the only
[09:03] artifact software development involves
[09:05] this inner loop where you begin with a
[09:07] task the idea is like what am I supposed
[09:09] to do uh how am I uh what what is the
[09:13] specific thing that I'm trying to do and
[09:15] followed by uh how do I go about doing
[09:17] that thing what are the Frameworks that
[09:19] are at my disposal what are the
[09:21] programming languages that that are at
[09:23] my disposal what are the kind of uh what
[09:25] is the existing code that's there what
[09:27] how do I write a new code that is
[09:29] consistent with those codes so that's
[09:31] becomes a sort of a specification and
[09:33] once you understand where you are then
[09:34] you sort of try to decide like where am
[09:36] I going with it like how does the final
[09:38] product look like once you have zeroed
[09:40] in on that then you go about what
[09:42] specific file changes do I need to make
[09:45] to to to get to that final product and
[09:48] that sort of becomes a plan and once you
[09:49] get to the plan then you go to the
[09:51] implementation part and that forms this
[09:53] Loop of software development and we call
[09:55] it Inner Loop and we would like the AI
[09:57] to be helpful in all those aspects of
[10:00] that inner loop and that's why we built
[10:02] copilot workspace in mind you like all
[10:05] NYX Explorations it did not start as
[10:07] copilot workspace has started as
[10:08] individual Explorations for instance we
[10:10] started to figure out can we use natural
[10:13] language to as a functional
[10:14] specification of program so there is a
[10:16] spec langang exploration we in parallel
[10:18] we were trying to figure out if we can
[10:20] improve the code completions by
[10:23] providing prompting the model with the
[10:25] runtime information and all of those
[10:27] things combined and with the user
[10:28] feedback back combined into this one
[10:30] bigger exploration called co-pilot
[10:33] workspace and we were also talking to
[10:35] our users like we we we wanted to talk
[10:37] to a developers and we wanted to ask
[10:38] that hey we are building this thing how
[10:40] would you like AI to support you what
[10:42] are your major pain points and one and a
[10:45] few things became very very clear while
[10:47] talking to our users right so first
[10:49] thing is that the most uh difficulty
[10:52] that people faced was getting started on
[10:54] a task like how do I I know that a issue
[10:56] is assigned to me how do I get started
[10:58] on it followed by how do I trust the
[11:00] output of the AI I don't trust it and
[11:02] more importantly they figured out that
[11:04] problem solving is what software
[11:06] development is about and they would like
[11:08] to retain that problem solving uh
[11:10] aspects of it and they would like the
[11:12] help of AI in the form of a thought
[11:14] partner or a sparring partner or a
[11:16] second brain which they can collaborate
[11:18] with to solve a problem and lastly and
[11:21] most importantly they would like to
[11:22] retain control developers are in control
[11:25] not the other way around and with this
[11:28] feedback
[11:30] we build co-pilot workspace so what is
[11:32] it it allows you to it simplifies
[11:34] getting started so oneclick proposal on
[11:37] on your tasks it has a built-in runtime
[11:39] that allows you to quickly verify what
[11:43] the the code that has been provided by
[11:45] the AI it has an environment which is
[11:47] built for iteration so if you feel that
[11:49] AI is going in the wrong direction you
[11:50] can just go and quickly correct it and
[11:52] most importantly it is designed for
[11:53] collaboration so you can just share uh
[11:56] your code or your work as a part of the
[11:58] gtha pull request or you can share your
[12:01] work or share your Works Space with your
[12:02] colleagues if you're not comfortable
[12:04] with it but let's enough talking let's
[12:08] just get into a demo about it right so
[12:11] this is monospace which is another
[12:13] GitHub exploration so if we are to write
[12:15] code let's write code in style and these
[12:17] are the four is a family of monospace
[12:19] fonts that has been released by GitHub
[12:22] and and this is a website that outlines
[12:24] a bunch of uh features of these
[12:27] fonts and over here somewhere over here
[12:29] is this playground which says that uh
[12:33] that here are how the syntax
[12:35] highlighting looks across different
[12:36] languages notice that it is missing rust
[12:39] and rust appears to be the next cool
[12:41] thing that all the cool kits are doing
[12:43] so we would like to update the small
[12:45] space website with a rust example as
[12:47] well so do how do I get
[12:49] started so I've created this issue or
[12:52] somebody has created this issue it just
[12:54] happens to be me for the purpose of this
[12:56] demo that I would like to create I would
[12:59] TR to add a rust example to the font
[13:01] playground and I can just click this
[13:03] button over here and it will open the
[13:06] copilot workspace for me and through the
[13:10] magic of caching you can see that it
[13:12] quickly generates the specification and
[13:14] prop Uh current specification and the
[13:16] proposed
[13:17] specification uh why caching uh because
[13:20] I had to finish this demo in time but
[13:22] trust me it's not a matter of hours it
[13:24] does happen in a matter of minutes right
[13:26] and and for those of you who are
[13:28] interested I would like to do a live
[13:29] demo for you in the Microsoft Booth
[13:30] after this task all right so what is the
[13:33] current specification it just goes and
[13:34] figures out does the website have this
[13:38] playground that contains a uh Russ
[13:40] package and it says it doesn't and it
[13:42] goes to the Target state would where
[13:45] would the target what does the Target
[13:47] State look like and it would says that
[13:49] yes the website will have the specific
[13:50] package for syntax highlighting the
[13:52] website will have uh this package in in
[13:54] in package.json and then I will update a
[13:56] bunch of other files it look nice and
[13:59] I'll go and generate a plan for it again
[14:01] through the magic of caching a plan has
[14:03] been generated and it will tell you that
[14:04] these three files these three files need
[14:06] to be updated and I will it it appears
[14:09] that this seems to be at the right level
[14:10] of modality then I will go ahead and
[14:12] implement it and yes Magic of caching
[14:15] again what we see is the files that are
[14:18] over here uh now this seems nice and but
[14:24] what about the iterator part what you
[14:25] can do is at any given point of time if
[14:27] you feel that something is not right you
[14:28] can just go ahead and say that okay add
[14:31] rust to the language
[14:32] mappings and say
[14:35] add
[14:37] code
[14:40] documentation and you can edit at any
[14:42] given point of time and what you can
[14:44] also do is that you can edit where chat
[14:46] over here and you can say that hey I
[14:47] want to edit this one specific location
[14:49] how do I go about and doing this I'm not
[14:52] going to do this because it's going to
[14:53] go through the whole iteration Loop and
[14:55] then the illusion of the caching will
[14:56] break and it will take a lot of time but
[14:59] I would like to do show that in live
[15:00] demos
[15:01] afterwards but how do I trust whether
[15:04] this is in fact the right thing so I
[15:07] will open up this integrated terminal
[15:09] and I will say
[15:11] uh install and run
[15:16] this
[15:18] repo all right so what's going to happen
[15:21] is uh that a suggestion is going to load
[15:23] and apparently not the right thing but I
[15:26] can quickly go and edit it and say that
[15:30] all right this is the command that I'm
[15:31] specifically looking for and I can go
[15:33] and
[15:34] run now this will run this command in an
[15:37] actual terminal and we'll see the output
[15:39] in some some point of time uh and and
[15:42] you can see that actually this this code
[15:44] does compile what we also have is a
[15:48] preview what we can do is open the live
[15:50] preview I don't trust it it's uh it will
[15:53] say that it's just going to be a second
[15:55] but it takes longer than that while that
[15:57] loads what are the other things
[15:59] one of the things that you would say is
[16:00] that hey you wrote a very simple command
[16:02] in the terminal you said npm you could
[16:04] actually type that thing in the terminal
[16:05] and yes you're right I can type that
[16:06] thing but think about that in a mobile
[16:08] setting when you can open CoPilot
[16:10] workspace in a mobile plat uh in in on
[16:12] your phone it becomes very tedious to
[16:15] type those symbols right and if you have
[16:18] used the the mobile keyboard it's not
[16:20] very useful for that so what I'm going
[16:23] to so so that's why we use this natural
[16:25] language way of uh writing these
[16:27] commands in the terminal uh so that it
[16:29] can help you when you're on the go it
[16:31] can synthesize those commands and
[16:33] hopefully the website has
[16:35] loaded and there is a rust example right
[16:41] cool that was a demo and thank
[16:46] you we are working we are not stopping
[16:48] there we are working on a bunch of these
[16:49] improvements and I can talk about these
[16:51] improvements uh on one-on-one basis with
[16:53] you and uh and and you already saw some
[16:55] other improvements like the runtime
[16:56] support to synthesize the terminal
[16:58] commands and and faster file completions
[17:00] using uh to to make the co-pilot
[17:03] workspace better but there are other
[17:05] next exploration that are also active
[17:07] like how do we rethink the developer
[17:09] learning with AI and how does the code
[17:10] review change if majority of the code
[17:13] that that is now being written is by AI
[17:15] so what does that mean and some of these
[17:16] Explorations will will work out and some
[17:18] of these exploration you will see as
[17:19] Tech previews and some of these
[17:20] exploration will kill because we don't
[17:22] know where they're going so in summary
[17:25] I'm saying that we do not know what the
[17:27] future of AI is is but what we know is
[17:30] Explorations is the way to get it and
[17:32] with all your help we'll jointly explore
[17:34] the space so that we don't have to wait
[17:37] like electricity we don't have to wait
[17:38] for 40 years to get to a place where to
[17:41] to get to a place with software
[17:42] development where we enjoy the benefits
[17:44] of AI you have been a lovely audience
[17:47] that is my time I really appreciate you
[17:49] and if you have more questions if you
[17:51] want to have live demos I'm available in
[17:52] the Microsoft Booth uh in like two
[17:55] salons over that side thank you so much
[18:01] [Music]
