---
type: youtube
title: Why Agent Engineering — swyx
author: AI Engineer
video_id: 5N33E9tC400
video_url: https://www.youtube.com/watch?v=5N33E9tC400
thumbnail_url: https://img.youtube.com/vi/5N33E9tC400/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence
tags: ['AI Agents', 'Machine Learning', 'Software Engineering', 'Reinforcement Learning', 'Agent Definition', 'AI Ethics', 'System Design', 'Technology Trends', 'OpenI', 'David Lan']
entities: ['Simon Willison', 'OpenI', 'OpenEye', 'David Lan', 'AIEE', 'Reinforcement Learning', 'Agents Definition', 'Machine Learning', 'Software Engineering']
concepts: ['Agent Definition', 'Reinforcement Learning', 'Control Flow', 'Delegated Authority', 'Long-Running Processes', 'Capabilities Growth', 'Anthropological Perspective', 'Machine Learning Fundamentals', 'AI Ethics']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with software engineering principles', 'Knowledge of reinforcement learning']
related_topics: ['Artificial Intelligence', 'Machine Learning', 'Software Engineering', 'Reinforcement Learning', 'Agent-Based Systems', 'AI Ethics', 'Natural Language Processing', 'System Design']
authority_signals: ['I think every AIEE conference needs to invoke the name of Simon Willison', "They're building on top of this new definition as well", 'We tell people to take agents off of their branding']
confidence_score: 0.85
---

# Why Agent Engineering — swyx

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=5N33E9tC400)  
**Published**: 2 months ago  
**Category**: AI/ML  
**Tags**: ai-engineering, agent-engineering, software-engineering, machine-learning, ai-discipline, ml-engineering, ai-research  

## Summary

# Summary of "Why Agent Engineering — swyx"  

## Overview  
The video discusses the evolution of AI engineering into **agent engineering**, emphasizing the need for clear definitions, addressing skepticism, and highlighting 2025 as a pivotal year for agent-based systems. The speaker critiques the confusion around the term "agent" and advocates for a unified framework to advance the field.  

---

## Key Points  
1. **Transition from AI Engineering to Agent Engineering**  
   - AI engineering is shifting toward **agent engineering** due to the rise of autonomous systems capable of goal-driven actions.  
   - Resistance exists from both machine learning (ML) and software engineering (SE) communities, each with conflicting perspectives on what an "agent" should entail.  

2. **Defining "Agent"**  
   - No consensus exists on a universal definition. Over 300 crowd-sourced definitions were gathered, highlighting themes like:  
     - **Goals** (e.g., achieving objectives)  
     - **Tools** (e.g., using external resources)  
     - **Control flow** (e.g., multi-step task execution)  
     - **Delegated authority** (e.g., autonomy in decision-making)  
   - OpenAI recently introduced a new definition, emphasizing the importance of aligning with evolving standards.  

3. **2025 as the "Year of Agents"**  
   - While some (e.g., Greg Brockman, Sam Altman) promote 2025 as the year of agents, the speaker is skeptical, noting that predictions often reflect desires rather than realities.  
   - Despite skepticism, the term "agent" has gained traction, with audiences still engaging despite fatigue.  

4. **Challenges and Skepticism**  
   - **Audience fatigue**: "Agents" was the second most tired buzzword, but attendees still showed up.  
   - **Historical context**: In 2024, David Lan (OpenI) advised removing "agents" from branding, but the trend has since reversed.  

5. **Need for a Unified Framework**  
   - The speaker emphasizes the importance of defining agents to avoid confusion and ensure progress.  
   - Simon Willison’s crowdsource definitions are highlighted as a foundational reference.  

---

## Notable Quotes  
- *"2025 is the year of Agents... if you say it often enough, it might be true."*  
- *"We tell people to take agents off their branding... now we tell them to put it back on."*  
- *"The machine learning people talk about reinforcement learning environments... software engineers just put in a for-loop."*  

---

## Actionable Insights  
1. **Define "Agent" Clearly**: Use existing frameworks (e.g., Simon Willison’s definitions) to establish a common understanding.  
2. **Monitor OpenAI’s Definition**: Track how industry leaders like OpenAI refine their agent definitions.  
3. **Be Cautious of Predictions**: Distinguish between desired outcomes and actual trends in AI development.  
4. **Engage with Skepticism**: Address audience fatigue by focusing on practical applications of agent-based systems.  

---  
*Note: The transcript was truncated, so some details (e.g., specific maps or trajectories) are summarized based on context.*

## Full Transcript

[00:00] [Music]
[00:17] hi good morning
[00:18] everyone love that love that um I'm
[00:21] going to get right into it one of the
[00:22] challenges we have with Summit is that
[00:24] we actually ask our speak speakers to do
[00:26] very short talks so I as the lead of
[00:28] summit I have to do even shorter talks
[00:30] so let's go uh you can see a lot of
[00:32] these there be a lot of show notes and
[00:33] homework you can see it on the live
[00:35] stream how is AI engineering doing uh
[00:37] it's pretty good we have an O'Reilly
[00:39] book that's pretty cool um uh chip is
[00:42] actually a good friend and she's
[00:42] actually speaking at uh she's giving our
[00:45] a keynote for the workshops session uh
[00:46] tomorrow which is pretty cool uh Garner
[00:48] hates us Garner thinks we've we've hit
[00:50] the peak so it's only downhill from here
[00:52] guys I'm sorry to inform you that yeah
[00:54] engineering is over uh there's no
[00:56] there's nowhere else uh else to go but
[00:57] down um a lot of
[01:00] the what I try to do with these a this
[01:02] uh talks that I do at at each conference
[01:05] is to try to Landmark the SE the state
[01:08] of the art or the state of the industry
[01:10] um so with Laton space I I did the rise
[01:12] of the a engineer with the first a
[01:13] engineer Summit we talked about the
[01:15] three types of a engineer and with last
[01:17] year's a engineer Worlds Fair we talked
[01:19] about how the discipline of a
[01:20] engineering was maturing and spreading
[01:22] across different
[01:24] disciplines um I think this is starting
[01:26] to get a little sale by now a few
[01:28] million people have seen this and like
[01:30] you know uh use this to form their teams
[01:32] and I think that was the intended effect
[01:33] what I am encountering these days is the
[01:36] two resistance from two sides of the AI
[01:39] engineer Spectrum uh if you come from an
[01:41] mle point of view you think that the AI
[01:43] engineer is just like mostly an mle plus
[01:45] a few promps if you come from the
[01:47] software engineering point of view you
[01:48] think that it's mostly software
[01:49] engineering and uh calling a few llm
[01:52] apis um I think over time it the AI
[01:55] engineering is going to basically emerge
[01:57] as its own discipline and it's still not
[01:59] there yet it's still very very early I
[02:00] still say things like oh yeah aiee is
[02:03] 90% software engineering 10% AI I think
[02:05] that will grow over time and I think
[02:07] this is the year when it starts to
[02:10] spread out and that's that's what I'm
[02:11] here to talk about a little bit today um
[02:14] so for example I I think like what I try
[02:16] to do with aie is also like it's a is a
[02:18] work in anthropology like how people
[02:20] describe themselves form groups form
[02:22] identities and form Industries U so ml
[02:25] you know it leaks out in your language
[02:27] um they say test time Compu because the
[02:28] only reason to run inference is to test
[02:30] it uh AE will maybe say inference time
[02:32] computer because we actually really care
[02:33] about inference um software Engineers
[02:35] may be reasoning um I I think you see
[02:38] these differences I try to articulate
[02:39] them over time um part of what I want to
[02:41] do here to set context is to explain why
[02:44] we have kind of pivoted AI engineer
[02:45] Summit to be the agent engineering
[02:47] conference um uh it's not a decision
[02:51] that we made likely because uh we're
[02:53] saying no to all these things we're
[02:55] saying no to rag we're saying no to open
[02:57] models uh gpus and we're just saying uh
[03:00] you know this is the only thing that
[03:02] we're going to do today um and but like
[03:05] closing all those doors actually opens
[03:07] up others so when we put out the call
[03:08] for speakers we uh made up all this list
[03:11] of uh you know other agent engineering
[03:12] disciplines and and I soon realized we
[03:15] didn't have to I'll talk about this in a
[03:16] bit um I also looked at last year's top
[03:18] performing Talks on YouTube and you guys
[03:20] told us uh that you know you really
[03:23] wanted all the all the agentic things
[03:25] now the only problem with this is that
[03:26] we only got speakers who basically made
[03:28] agent Frameworks for a living
[03:30] uh and everyone's asking the the the
[03:32] real question who's putting this in
[03:34] production so we had a new rule this
[03:36] year of all right no more vendor pitches
[03:39] um you know you complain about yeah
[03:41] let's oh thank you uh as a as a curator
[03:46] makes it so much infinitely harder
[03:48] because uh basically the people that
[03:50] you're about to see have no incentive to
[03:51] come on stage and share what they're
[03:53] sharing uh but somehow we talked them
[03:54] into it so uh I hope you're looking
[03:56] forward to that uh the other thing also
[03:59] I realized that
[04:00] everything plus agent Works basically so
[04:03] agent plus rag Works agent plus Cent
[04:05] Works agent plus search works um and
[04:07] this is kind of like the simple formula
[04:08] for like making money in 2025 uh most of
[04:12] these most of these names you'll see in
[04:13] the talks that are uh that will follow
[04:16] uh in in the
[04:17] sessions um Sor me if you heard this one
[04:20] before 2025 is the year of Agents right
[04:22] if you say it often enough it might be
[04:24] true uh I think that when people make
[04:27] predictions often times they confuse
[04:28] what they want to happen for what will
[04:30] actually happen um so maybe you believe
[04:32] satin Adela maybe you believe Roman
[04:34] maybe you believe Greg Brockman maybe
[04:36] you believe Sam mman all of them want
[04:38] you to believe that 2025 is year of
[04:40] Agents uh and I'll be very honest uh me
[04:42] and my co-host alesio I think I saw you
[04:44] over there hey um uh we were pretty
[04:48] skeptical as well we were're on the
[04:50] record Being skeptical actually actually
[04:51] all of you are being on the record
[04:53] because last yesterday uh bar played uh
[04:56] Family Feud with with our with our
[04:58] audience and the number two
[05:00] Buzz that everyone is tired of hearing
[05:01] as agents um but fortunately you guys
[05:03] are not tired enough because you came to
[05:04] it today I have you for one more day of
[05:06] uh of Agents talk uh but we're on record
[05:09] March 2024 with David Lan uh the former
[05:12] VP avenge of openi uh saying that we
[05:15] tell people to take agents off of their
[05:17] branding uh now we tell them to put it
[05:18] back
[05:19] on so okay there um I I I think I'm I'm
[05:23] doing this as a public service to start
[05:25] any agents conference we have to define
[05:27] the word agent are you guys ready
[05:31] all right I actually have one I it's a
[05:33] Monumental task I could do it in one
[05:35] slide um so if you talk again this this
[05:38] is a very POV sort of anthropological
[05:40] point of view the machine learning
[05:41] people will talk about some kind of
[05:42] reinforcement learning environment they
[05:44] want to talk about actions achieving
[05:45] goals and all that um aie we don't know
[05:48] what they what they want yet uh this the
[05:49] software Engineers are very reductive
[05:51] they just you know put in a for Loop
[05:55] um okay you it seems like you agree um
[05:58] so uh fortunately you know I think every
[06:00] aiee conference needs to invoke the name
[06:01] of Simon Willison uh he is our patron
[06:04] saint um he's actually gone in
[06:06] crowdsource 300 uh definitions of what
[06:08] an agent is so I didn't have to survey
[06:10] all of you I I was thinking about asking
[06:11] every single speaker to start with what
[06:13] is your definition uh it doesn't matter
[06:15] uh there's here's six of them right you
[06:17] it's either about goals it's about tools
[06:20] it's about control flow it's about long
[06:22] running processes it's about delegated
[06:23] authority uh and small multi-step task
[06:25] completion yeah I see all the phones
[06:27] coming out don't worry it's on the live
[06:28] stream right there's like 20,000 people
[06:31] uh watching along um and then there's
[06:32] there's a bunch of other things uh I
[06:34] think I think the last one on the bottom
[06:35] left bottom right is uh is an
[06:37] interesting one like just have some
[06:39] things that everyone defines agrees as
[06:41] an agent and make sure that they're sort
[06:42] of your agent definition is passing
[06:44] those
[06:45] things um except so that was my one
[06:48] slide that was my slide uh of like what
[06:50] defining an agent and then yesterday
[06:52] open ey went and dropped a new agents
[06:54] definition uh on the live stream uh that
[06:56] you can watch yesterday as well um so
[06:59] this is something they're obviously
[07:00] going to work with um and I think you
[07:03] should definitely pay attention to to
[07:04] this because they're they're building on
[07:05] top of this uh new definition as well so
[07:09] that's defining agents why now why is
[07:12] why are agents working now when they did
[07:13] not work a year ago two years ago um I
[07:16] have a rough idea so the people were
[07:19] talking about capabilities and so uh you
[07:21] can see that capabilities even even on
[07:23] the trajectory of 2023 2025 um have been
[07:27] have been really growing and they
[07:28] started around to hit human baselines
[07:30] right about now um and I also have a map
[07:34] of other uh reasons as well so I'll just
[07:36] bring you through each of them most
[07:37] people will say oh yeah we have better
[07:39] reasoning now we have better tool use
[07:41] now we have better tools um including
[07:43] mCP which which you're doing a workshop
[07:45] on uh tomorrow uh but I think there are
[07:48] some other less appreciative things
[07:49] which I'm going to bring up to you right
[07:50] now model diversity right uh the opening
[07:52] ey market share has gone from like let's
[07:54] say 95% two years ago now down to 50%
[07:56] it's much more diverse uh landscape
[07:59] including like just this this past week
[08:02] um two Frontier Model Labs that are
[08:03] possible challenges to open the eye have
[08:05] emerged and which I think which I think
[08:06] is um really exciting for 2025 we we
[08:09] don't actually know what it's going to
[08:10] shake out to it by the end of the year
[08:12] uh the second thing is uh that the cost
[08:14] of intelligence is super more low is
[08:16] what I call it um it's it's gone uh the
[08:18] cost of GPT 4 level intelligence has
[08:20] gone down 1,000 times in the last 18
[08:21] months um and you can see the same C
[08:24] starting for the 01 level
[08:26] intelligence um uh and also we now start
[08:28] to have our RL fine tuning options um I
[08:31] have zero experience in this area but
[08:33] fortunately one of our speakers will uh
[08:35] is going to tell us talk to us later
[08:37] today about this about this um so we
[08:40] have all these reasons we have I have a
[08:41] few more uh you know in our conversation
[08:43] with Brett Taylor U he talks about uh C
[08:45] charging for outcomes instead of instead
[08:47] of costs um there's a lot of work on
[08:49] multi-agents as well as faster inference
[08:51] as well that's coming out from the the
[08:52] better Hardware that we have um there's
[08:54] more homework there if you want this is
[08:56] all sourced and you know has has has
[08:58] some backing in our our lat space
[08:59] conversations but I don't really have
[09:01] time for that okay so one last thing for
[09:03] you guys on agent use cases so uh I
[09:06] think most people agree with like bar um
[09:08] Barry's uh building effective agents
[09:10] talk um he he's going to talk about how
[09:12] coding agents and support agents have
[09:13] product Market fit I think now it's fair
[09:15] to say deep research has pmf um but also
[09:17] I will say up and coming are some of
[09:19] these use cases some of which you you're
[09:20] going to see in the the talks later but
[09:23] also want to offer anti- use cases can
[09:25] we please stop demoing agents that book
[09:27] flights yeah no more flight booking
[09:30] agents uh I want to book my own flights
[09:33] thank you very much I I want to book my
[09:34] own instacart orders and also please
[09:36] don't asro Tri it it right okay so uh
[09:40] one yeah and I think the reason that the
[09:42] tell that uh you know this is this is a
[09:44] headline that I saw yesterday I had to
[09:45] put this in um opening I reported 400
[09:47] million users uh which is a 33% growth
[09:50] from three months ago um and then you
[09:51] can ask deep research to research open a
[09:53] eye and draw this chart of chat gbt
[09:55] growth uh going from uh Z to uh 400
[09:59] million users in two years in two and a
[10:01] half years um so I I remember this chart
[10:05] very well because chpc spent a year not
[10:07] growing and why did it spend a year not
[10:09] growing because they didn't ship any any
[10:11] agentic models um and if you actually
[10:13] just look at the uh the sort of weekly
[10:15] active user chart and stretch it out you
[10:17] actually get this chart uh which is
[10:19] actually super interesting because it
[10:21] basically shows that one one um the sort
[10:24] of 01 models have doubled chat GPT usage
[10:27] and if you stretch it out um Chad GPT is
[10:28] going to hit a billion users by the end
[10:30] of this year this year uh it's basically
[10:32] going to Quint tupo the number of users
[10:34] it had uh as of September of last year
[10:37] um and so like the the the the the
[10:39] growth of chbt and the growth of any AI
[10:41] product is going to be very very tight
[10:43] to reasoning capabilities and the amount
[10:44] of agents that you can Shi for your
[10:45] users um it is it is real it is it is
[10:49] huge huge numbers this is one8 of the
[10:50] world population that's going to be
[10:51] using chbt by the end of this year and I
[10:53] think there's a lot of money left on the
[10:55] table for everyone else so um I hope you
[10:57] enjoy doing that um I'm well past time
[10:59] so I'm going to skip all this but
[11:00] basically I I think that the job of a is
[11:02] now evolving towards building agents in
[11:04] the same way that mes build models
[11:06] software engineers build software um so
[11:08] uh I'm going to skip all that you can
[11:09] see all you can see all that on on the
[11:11] on the live stream U but we're actually
[11:12] uh you know just here to welcome you to
[11:14] the show um and uh I'm really excited to
[11:17] introduce you to everyone so um thank
[11:18] you and I hope you enjoy
[11:25] [Music]
