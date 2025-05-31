---
type: youtube
title: Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil
author: Channel Video
video_id: d5EltXhbcfA
video_url: https://www.youtube.com/watch?v=d5EltXhbcfA
thumbnail_url: https://img.youtube.com/vi/d5EltXhbcfA/mqdefault.jpg
date_added: 2025-05-26
category: Artificial Intelligence and Machine Learning
tags: ['AI Evaluation', 'Agent-Based Systems', 'Benchmarking', 'LLMs', 'Real-World AI', 'Evaluation Challenges', 'AI Research', 'Technical Challenges', 'Open-Ended Actions', 'Recursive Systems', 'Human Peer Review', 'Theoretical Maximums']
entities: ['Sakana AI', 'CUDA kernels', 'H100', 'LLM', 'agents', 'models', 'virtual environments', 'reward function', 'peer review', 'toy problems']
concepts: ['AI Evaluation Challenges', 'Real-World Agent Performance', 'Static Benchmarks', 'Cost in Evaluations', 'Open-Ended Actions', 'Recursive Systems', 'Human Peer Review', 'Theoretical Maximums']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML', 'Familiarity with Large Language Models (LLMs)', 'Knowledge of evaluation methodologies', 'Understanding of real-world AI applications', 'Some coding or technical background']
related_topics: ['AI Ethics', 'Benchmarking in AI', 'Agent-Based Systems', 'Machine Learning Evaluation', 'Evaluation Metrics', 'AI Research', 'Reinforcement Learning', 'Technical Writing']
authority_signals: ['"evaluating agents is genuinely a very hard problem"', '"needs to be treated as a first class citizen in the AI engineering toolkit"']
confidence_score: 0.8
---

# Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=d5EltXhbcfA)  
**Published**: 1 month ago  
**Category**: AI/ML  
**Tags**: ai agents, ai evaluation, language models, agent challenges, ai engineering, real world applications, ai limitations  

## Summary

# Summary of "Building and Evaluating AI Agents" by Sayash Kapoor

## Overview  
This talk critiques the challenges in developing and evaluating AI agents, emphasizing that while agents are already in use, their ambitious goals often fall short due to flawed evaluation practices. The speaker highlights three critical issues: the difficulty of rigorous evaluation, the limitations of static benchmarks, and the need to account for cost in performance metrics. Examples like Do Not Pay, Lexus Nexus, and Sakana AI illustrate failures stemming from inadequate testing and overpromising.

---

## Key Points  
1. **Evaluation as a First-Class Problem**  
   - Evaluating agents is inherently harder than evaluating language models (LLMs) because agents interact with dynamic environments, take actions, and require cost-aware metrics.  
   - **Example**: Sakana AI claimed a 150x improvement in CUDA kernel optimization, but deeper analysis revealed the claim was based on reward function hacking, not actual performance.  

2. **Static Benchmarks Are Misleading**  
   - Traditional benchmarks (e.g., input-output string comparisons) work for LLMs but fail for agents, which require dynamic, environment-based testing.  
   - Agents can recursively call sub-agents or perform open-ended actions, making their evaluation complexity unbounded.  

3. **Cost as a Critical Metric**  
   - Evaluations must balance accuracy with computational cost. Ignoring cost leads to unrealistic or unsustainable systems.  
   - **Example**: Sakana AI’s "AI scientist" was evaluated using LLMs as judges rather than human peer review, revealing minor tweaks rather than groundbreaking automation.  

---

## Key Insights  
- **False Claims and Overpromising**: Companies like Do Not Pay and Sakana AI made exaggerated claims due to lack of rigorous evaluation, leading to public distrust.  
- **Agent vs. Model Evaluation**: Agents require simulating real-world interactions, which is far more complex than evaluating static models.  
- **Need for Dynamic Testing**: Static benchmarks cannot capture the adaptability and cost trade-offs required for real-world agent deployment.  

---

## Actionable Recommendations  
1. **Prioritize Evaluation**: Treat evaluation as a core component of AI engineering, not an afterthought.  
2. **Develop Dynamic Benchmarks**: Create virtual environments to test agents’ real-world adaptability.  
3. **Incorporate Cost Metrics**: Balance accuracy with computational efficiency in evaluations.  
4. **Avoid Overpromising**: Ensure claims are backed by rigorous, transparent testing to avoid reputational damage.  

--- 

## Conclusion  
The speaker argues that the AI community must address evaluation challenges head-on to ensure agents are reliable, ethical, and effective in real-world applications. Without systemic changes, the risks of failure—and the erosion of public trust—will persist.

## Full Transcript

[00:00] [Music]
[00:17] the theme of this conference today is
[00:19] agents at work unfortunately for the
[00:22] next 18 minutes you'll be stuck with me
[00:24] talking about how agents don't work very
[00:26] well today and how we can do better when
[00:28] it comes to AI engineering ing so there
[00:31] is so much interest in Agents from all
[00:33] fronts in the product world and in the
[00:35] industry World in academic labs in
[00:38] research if you're someone who doesn't
[00:41] think that companies will be able to
[00:43] scale language models all the way to AGI
[00:46] and what we're going to see more and
[00:48] more of in the near future is agents
[00:51] that are not really deployed directly
[00:53] but function as small parts of larger
[00:55] products and systems and this is what AI
[00:58] is probably going to look like in the
[01:00] near future swix came up with a few
[01:02] dozen definitions of AI agents this is
[01:05] one of them where language models
[01:07] control the flow of a particular
[01:09] system in fact even when people naively
[01:13] think of um chat GPT and Claw as models
[01:17] uh these tools are actually examples of
[01:19] rudimentary agents at some level they
[01:21] have input and output filters uh they
[01:24] can carry out certain tasks they can
[01:25] call these tools and so on so in some
[01:28] sense agents are already widely used as
[01:32] well as
[01:33] successful we've now seen mainstream
[01:35] product offerings uh that can do a lot
[01:37] more open AI operator can carry out
[01:40] open-ended tasks on the internet the
[01:42] Deep research tool can carry out 30
[01:45] minute long report writing tasks on any
[01:47] conceivable
[01:49] topic so that's the first reason I think
[01:51] today's conference is timely but the
[01:54] second reason is that on the flip side
[01:56] the more ambiti ambitious visions of
[01:59] what agent can do are far from being
[02:01] realized so on the left here is a vision
[02:04] for what agents can do something out of
[02:06] Science Fiction films like the film her
[02:08] and on the right hand side are how these
[02:11] ambitious products have failed in the
[02:13] real world so far now I'm pointing this
[02:15] out not to criticize the specific
[02:17] products on the slide but to genuinely
[02:20] challenge the audience into the
[02:21] challenge of building AI agents that
[02:23] really work for the people who are about
[02:25] to use them and so over the course of
[02:28] this talk I'll talk about three main
[02:30] reasons why agents don't yet work and
[02:33] what we can do to realize the potential
[02:35] of agents to get past some of these
[02:38] failures the first one is that
[02:40] evaluating agents is genuinely hard so
[02:43] to begin let's see some examples of how
[02:46] when people have tried to productionize
[02:48] agents these agents have sort of failed
[02:50] in the real
[02:51] world do not pay is a US startup that
[02:54] claimed to automate the entire work of a
[02:57] lawyer um the startup co-founder even
[03:00] offered a million dollar for any lawyer
[03:02] who would be willing to argue in front
[03:04] of the US Supreme Court using do not pay
[03:07] in an
[03:09] earpiece in reality a couple of years
[03:12] later in fact very recently the FTC fine
[03:15] do not pay hundreds of thousands of
[03:16] dollars the reason for the fine was that
[03:19] the performance claims that do not play
[03:21] seem to be making were actually entirely
[03:23] false now you might consider this a case
[03:26] of Rush invention of a small startup
[03:29] making claims that it cannot back so
[03:31] let's look at some of the work from more
[03:33] wellestablished
[03:34] companies Law Firm Nexus Lexus Nexus as
[03:37] well as West law are widely regarded to
[03:39] be some of the leading lawtech firms in
[03:41] the US a couple of years ago Lexus Nexus
[03:45] launched this product which it claimed
[03:47] was hallucination free in its ability to
[03:49] generate legal reports and
[03:52] reasoning but when Stanford researchers
[03:54] evaluated Lexus Nexus and West law
[03:56] products they found that in up to a
[03:59] third of cases in at least a sixth of
[04:01] cases these language models
[04:04] hallucinated um in particular in some
[04:07] cases the hallucinations basically
[04:09] completely reversed the intentions of
[04:11] the original legal text in others the
[04:13] paragraphs were made up uh they have
[04:15] about 200 examples of such errors um in
[04:18] leading ltech
[04:20] products we've also heard examples of AI
[04:24] agents soon automating all of scientific
[04:27] research so this is an example from St
[04:29] startup Sakana doai Sakana claimed they
[04:32] had built a research scientist that
[04:33] could fully automate open-ended
[04:35] scientific research now our team at
[04:37] Princeton wanted to test this claim in
[04:39] the real world in part because
[04:41] automating scientific research is one of
[04:44] our main research interests so we built
[04:46] a benchmark we created this Benchmark
[04:48] called core bench the tasks in this
[04:51] Benchmark are way simpler than what you
[04:54] might expect from open-ended real world
[04:56] scientific research um they just tried
[04:58] to reproduce a papers result even
[05:01] providing the agent with the code and
[05:03] the data needed to reproduce it so as
[05:05] you can imagine this is far simpler than
[05:07] automating all of
[05:09] science what we found is that the best
[05:13] agents as of today cannot even automate
[05:16] scientific research reliably less than
[05:18] 40% of the papers can be um reproduced
[05:21] by the leading agents now of course you
[05:23] can see these models getting better and
[05:25] even if an agent can automate only 40%
[05:27] of rep producibility that is a huge
[05:29] boost because researchers spent a lot of
[05:32] time reproducing baselines from past
[05:34] results but on this basis to argue that
[05:38] AI can soon automate all of science or
[05:41] that agents will R render scientific
[05:43] researches obsolete is way too
[05:46] premature in fact when people actually
[05:49] looked at how well Sakana ai ai
[05:51] scientist worked they found that it was
[05:53] deployed on toy problems that uh it was
[05:57] evaluated using an llm as a judge rather
[05:59] than than human peer review and that in
[06:01] fact once you start looking at the
[06:02] results they turn out to be very minor
[06:05] tweaks on top of other papers think
[06:07] undergrad research projects rather than
[06:09] fully automating all of
[06:11] Science Now a couple of days ago as I
[06:14] Was preparing the slides for this talk I
[06:15] came up with another claim or Sakana
[06:17] came up with another claim where they
[06:19] claimed to build an agent for optimizing
[06:22] Cuda kernels the claims were indeed very
[06:25] impressive they could lead to a 150x
[06:27] improvement over the standard could
[06:29] kernel that P comes with the issue
[06:32] though was that if you sort of analyze
[06:34] their claims one level deeper you would
[06:37] see that they were claiming to
[06:39] outperform the theoretical maximum of
[06:41] the H 100 by 30 times clearly this claim
[06:44] was false and once again it was because
[06:46] of the lack of rigorous evaluation it
[06:49] turned out that the agent was simply
[06:50] hacking the reward function rather than
[06:53] actually improving the Cuda kernels once
[06:55] again the point is not to call out a
[06:57] single company but rather to flag that
[07:00] evaluating agents is genuinely a very
[07:03] hard problem it needs to be treated as a
[07:06] first class citizen in the AI
[07:08] engineering toolkit or else we continue
[07:10] risking failures like the ones on the
[07:13] slide the second reason why building
[07:16] agents that work in the real world is
[07:18] hard is because static benchmarks can be
[07:20] quite misleading when it comes to the
[07:22] actual performance of
[07:23] agents and that's because for the
[07:25] longest time we focused on building
[07:28] evaluations that might work pretty well
[07:30] for evaluating High well language models
[07:32] too but agents are not the same as
[07:35] models for example for most language
[07:37] model evaluations all you need to do is
[07:40] to consider an input string and an
[07:42] output string those are the domains
[07:44] where language models work it's really
[07:46] enough to construct
[07:48] valuation on the other hand when you're
[07:50] thinking about agents these agents need
[07:52] to take actions in the real world they
[07:54] need to interact with an environment and
[07:56] so building this s of evaluation that
[07:59] makes these changes possible that
[08:01] creates the virtual environments within
[08:02] which these agents operate is a way
[08:05] harder
[08:06] problem a second difficulty in
[08:08] evaluating agents is that for llms the
[08:12] cost of evaluating a model is bounded to
[08:14] the context window length of these
[08:16] language models you can basically look
[08:19] at these evaluations as having a fixed
[08:21] ceiling but when you have agents that
[08:23] can take open-ended actions in the real
[08:25] world there isn't any such ceiling you
[08:28] can imagine these agents calling other
[08:30] sub agents there can be recursions there
[08:32] can be all sorts of systems maybe just
[08:34] llm calls in a for Loop and because of
[08:37] this Cost needs to be once again a first
[08:39] class citizen in all evaluations of
[08:41] Agents if you don't have cost as an
[08:43] access alongside accuracy or performance
[08:46] you're not going to really understand
[08:48] how well your agent
[08:50] works and finally when you build a new
[08:53] Benchmark for a language model you can
[08:56] basically assume that you can evaluate
[08:58] every single language model model on
[08:59] this Benchmark but when it comes to
[09:02] evaluating agents these agents are often
[09:04] purpose-built so for instance if there
[09:06] is a coding agent you want to evaluate
[09:09] you can't really use a web agent
[09:11] Benchmark to evaluate it on and this
[09:13] leads to an second hurdle which is how
[09:16] do you construct these meaningful
[09:17] multi-dimensional metrics to evaluate
[09:19] your agents rather than um relying on a
[09:22] single Benchmark to evaluate how well it
[09:24] works now all of these concerns might be
[09:27] thought of as theoretical um you know
[09:30] you could reasonably ask why do we care
[09:33] if static evaluations don't really work
[09:35] well for agents the reason is that
[09:39] because of these differences with the
[09:41] cost and the accuracy because of the
[09:43] single focus on optimizing for a single
[09:45] Benchmark we are basically unable to get
[09:48] a coherent picture of how well an agent
[09:50] works so at Princeton we developed this
[09:52] uh agent leaderboard that tries to solve
[09:55] some of these issues in particular for
[09:57] example for the core bench leader I
[09:59] mentioned earlier um you can have
[10:01] multiple agents which are evaluated with
[10:04] cost alongside accuracy so here on this
[10:07] parito Frontier you can see agents like
[10:10] Cloud 3.5 um scoring about as much as
[10:14] the um open eyes o1 models but a cloud
[10:17] model actually costs $57 to run whereas
[10:20] o1 costs
[10:22] 664 even if the performance of open a
[10:25] Owen was a couple of percentage points
[10:27] higher which it wasn't in this case by
[10:28] the way but even it would work for most
[10:31] AI Engineers the choice here is obvious
[10:34] you would any day of the week take a
[10:36] model that costs 10 times lesser while
[10:39] performing about as
[10:40] well now in response to this sort of
[10:43] two-dimensional parito um I've often
[10:46] been asked um are llms becoming too
[10:49] cheap to meter in other words why do we
[10:50] even need to care about the cost of
[10:52] running an agent if the cost of uh
[10:55] creating these models is dropping
[10:57] drastically and it is indeed true that
[10:59] costs have dropped drastically in the
[11:01] last few years if you compare Tex
[11:03] DaVinci 003 which was open AIS model
[11:06] back in
[11:07] 2022 um to today's GPD 40 mini which in
[11:11] most cases outperforms this older model
[11:13] the cost has dropped by over two orders
[11:15] of
[11:17] magnitude but at the same time if you're
[11:19] building applications that need to scale
[11:21] this type of approach is still quite
[11:23] costly and especially from the point of
[11:25] view of releasing prototypes one of the
[11:27] barriers is for a Engineers is you
[11:31] really need to sort of iterate in the
[11:33] open and so if you don't account for
[11:35] cost your prototype might soon end up
[11:37] costing you thousands of
[11:39] dollars and finally even if the cost of
[11:42] uh scaling inference time um llm calls
[11:45] continues to drop what is known as a
[11:47] jvin paradox I suspect will keep
[11:49] increasing the overall cost of running
[11:51] agents so jvin Paradox is this Theory
[11:53] from a 19th century British Economist
[11:56] who figured out that as the cost of uh
[11:58] mining coal reduced the overall usage of
[12:01] coal increased not decreased along
[12:04] several Industries the same happened
[12:06] when the ATM machines were introduced
[12:08] all over the US people expected a loss
[12:11] of jobs for bank tellers but what
[12:14] happened was the opposite because ATMs
[12:16] were so easy to install the number of
[12:18] Bank branches actually drastically
[12:19] increased leading to an increase in the
[12:21] number of bank tellers employed this is
[12:24] also what I expect will happen as the
[12:26] costs for language models keep dropping
[12:28] drastically and that's why for the
[12:30] foreseeable future at least we do need
[12:32] to account for cost when it comes to
[12:34] agent
[12:35] evaluations so how do we do all of this
[12:38] um in an automated way well with the
[12:40] holistic agent leaderboard or Hal uh
[12:42] we've come up with a way to
[12:43] automatically run agent evaluations on
[12:46] these 11 different benchmarks already
[12:48] and very many more are on the way um
[12:51] beyond that though even if we come up
[12:53] with these multi-dimensional um
[12:55] benchmarks even if we do come up with
[12:57] cost controlled evalu ations there are
[13:00] still certain issues with this type of
[13:01] evaluation and that's because agent
[13:03] benchmarks have sort of become the
[13:05] metric against which VC's fund companies
[13:08] an example is cosign which raised its
[13:11] seed round of funding based on its
[13:13] results on S bench in fact agent
[13:16] developer um cognition raised $175
[13:20] million at a valuation of $2 billion
[13:23] driven primarily by the fact that the
[13:25] Asian did very well on S bench
[13:29] unfortunately Benchmark performance very
[13:32] rarely translates into the real world so
[13:35] this is an excellent analysis of how
[13:37] well Devon Works Devon is the agent
[13:40] developed by cognition um from the very
[13:42] impressive Folks at
[13:44] answer. um instead of relying on
[13:46] standard benchmarks they actually tried
[13:48] to incorporate Devon into the real world
[13:50] and what they found was that over a
[13:52] month of use they tried it for 20
[13:54] different tasks and it was only
[13:56] successful at three of them so this this
[13:59] is the other reason why this
[14:00] overreliance on static benchmarks can be
[14:03] really
[14:04] misleading how do we get over this one
[14:06] of my favorite Frameworks to think
[14:08] through this is the work by Folks at
[14:10] Berkeley called who validates the
[14:12] validators on the top is the typical
[14:15] evaluation pipeline which consists of
[14:17] singular llm calls against static
[14:19] metrics which is the um sort of broken
[14:22] Paradigm for AI evaluations that we just
[14:24] discussed and at the bottom is what they
[14:27] propose they propose having humans in
[14:29] the loop who are domain experts who
[14:31] proactively edit the criteria based on
[14:33] which these llm evaluations are
[14:35] constructed and that can lead to much
[14:37] better evaluation results
[14:39] overall this brings me to the last key
[14:41] takeaway for why Agent performance does
[14:44] not really translate into the real world
[14:46] which is the confusion between what
[14:48] capability is and what reliability
[14:50] is so very roughly speaking capability
[14:54] means what a model could do at certain
[14:57] points of time for those of of you who
[14:59] are technically minded this means the
[15:00] pass at K accuracy of a model for a very
[15:04] high K that means that one of the K
[15:06] answers that the model outputs are
[15:08] correct on the other hand reliability
[15:10] means consistently getting the answer
[15:12] right each and every single time when
[15:15] agents are deployed for consequential
[15:17] decisions in the real world what you
[15:19] really need to focus on is reliability
[15:22] rather than capability that's because
[15:24] language models are already capable of
[15:26] very many things but if you trick
[15:29] yourself into believing this means a
[15:30] reliable experience for the end user
[15:32] that's when products in the real world
[15:34] go wrong so in particular I think the
[15:37] methods for training models that get us
[15:40] to the 90% of it what in s's term would
[15:43] be the job of a machine learning
[15:45] engineer don't necessarily get us to the
[15:49] 99.999% what is often known as the 5 9
[15:51] of
[15:52] reliability and closing this gap between
[15:55] the 90% And The
[15:57] 99.9% is the job of an AI
[16:00] engineer and I think this is what has
[16:03] led to the failures of products like
[16:05] Humane Spin and rabbit R1 it's because
[16:08] the developers did not anticipate that
[16:11] not having reliability in products like
[16:13] these would lead to a product failure in
[16:15] other words if your personal assistant
[16:18] only offers your orders your do Dash
[16:20] food correctly 80% of the times that is
[16:22] a catastrophic failure from the point of
[16:24] view of a
[16:26] product now one thing people have
[16:28] proposed to fix this sort of issue to
[16:30] improve reliability is to create a
[16:32] verifier something like a unit test um
[16:36] and on this basis there have been
[16:37] several claims that we could improve the
[16:39] inference scaling capabilities of these
[16:41] tools and get to very reliable
[16:44] models unfortunately what we found is
[16:47] that verifiers can also be imperfect in
[16:49] practice for instance two of the leading
[16:52] coding benchmarks human eval and mbpp
[16:55] both have false positives in the unit
[16:56] tests that is um a model could output
[16:59] incorrect code and still pass the unit
[17:01] test and once we account for these false
[17:04] positives what we have are these
[17:06] inference scaling curves bending
[17:07] downwards so rather than model
[17:09] performance continuing to improve if
[17:12] there are false positives in your
[17:13] verifiers the model performance sort of
[17:15] bends downwards simply because the more
[17:17] you try the more likely it is you'll get
[17:19] a wrong
[17:20] answer and so this is also not a perfect
[17:24] solution to the problem of
[17:25] reliability so what is the solution I
[17:29] think the challenge for AI Engineers is
[17:31] to figure out what sorts of software
[17:34] optimizations and abstractions are
[17:36] needed for working with inherently
[17:38] stochastic components like llms in other
[17:41] words it's a system design problem
[17:43] rather than just a modeling problem
[17:45] where you need to work around the
[17:47] constraints of an inherently stochastic
[17:49] system and I want to argue in the last
[17:52] one minute of my talk that this means
[17:54] looking at AI engineering as more of a
[17:57] reliability engineering field than a
[17:59] software or a machine learning
[18:00] engineering field and this also brings
[18:03] me to the clear mindset shift that is
[18:05] needed um to become successful for from
[18:09] the perspective of being an AI engineer
[18:11] if you look at the title slide of my
[18:13] talk um this title slide sort of pointed
[18:16] to one such area where we've already
[18:18] overcome certain um types of limitations
[18:20] of stochastic
[18:22] systems and that is with the birth of
[18:24] computing the 1946 eniac computer used
[18:28] over 17,000 vacuum tubes many of which
[18:31] at the beginning of this process used to
[18:33] fail so often that the computer was
[18:36] unavailable half the time and the
[18:39] engineers who built this product knew
[18:41] that this is a failure from the point of
[18:42] view of the end users so their primary
[18:45] job in the first two years of this
[18:47] computer was to fix the reliability
[18:50] issues to reduce it to a point where it
[18:52] becomes well enough it works well enough
[18:55] to become usable by the end user and I
[18:58] say that this is precisely what AI
[19:01] Engineers need to be thinking about as
[19:03] their real job it is not to create
[19:05] excellent products though that is
[19:07] important but rather to fix the
[19:09] reliability issues that plague every
[19:11] single agent that uses inherently
[19:14] stochastic models um as its basis so
[19:17] this is what I'll leave you here with
[19:18] today um to become successful Engineers
[19:21] you need a reliability shift in your
[19:23] mindset to think of yourselves as the
[19:25] people who are ensuring that this next
[19:27] wave of computing is as reliable for end
[19:30] users as possible and there's a lot of
[19:32] precedent for this type of thing
[19:34] happening in the past all right with
[19:36] this I'll leave you with the 3K
[19:38] takeaways it was a pleasure being here
[19:39] thank you
[19:42] [Music]
