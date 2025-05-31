---
type: youtube
title: Which Jobs Can Be Replaced Today:  Fryderyk Wiatrowski and Peter Albert
author: AI Engineer
video_id: R3hTescenDw
video_url: https://www.youtube.com/watch?v=R3hTescenDw
thumbnail_url: https://img.youtube.com/vi/R3hTescenDw/mqdefault.jpg
date_added: 2025-05-26
category: AI and Automation
tags: ['AI automation', 'browser agents', 'task automation', 'AI models', 'rule-based systems', 'proactive automation', 'continuous improvement', 'AI in business', 'automation tools', 'foundation models']
entities: ['Meta', 'Frederick', 'Zapier', 'Slack', 'Linear', 'browser agents', 'AI models', 'Foundation models']
concepts: ['automation', 'AI-driven task automation', 'rule-based systems', 'proactive vs. reactive tasks', 'browser automation', 'continuous improvement of AI models', 'foundation model reasoning', 'trigger-based agent reactions']
content_structure: discussion/opinion
difficulty_level: intermediate
prerequisites: ['Basic understanding of AI/ML concepts', 'Familiarity with automation tools (e.g., Zapier)', 'Web development basics for browser interactions']
related_topics: ['AI automation', 'browser automation', 'task automation', 'AI model development', 'rule-based systems', 'proactive system design', 'continuous AI improvement', 'enterprise automation']
authority_signals: ["'I previously worked on the number two models at meta'", "'the beauty of the reactive things is that once you set the rules...'"]
confidence_score: 0.85
---

# Which Jobs Can Be Replaced Today:  Fryderyk Wiatrowski and Peter Albert

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=R3hTescenDw)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: ai, automation, job-replacement, workflow, agents, future-of-work, task-automation  

## Summary

```markdown
# Summary of "Which Jobs Can Be Replaced Today" (Fryderyk Wiatrowski & Peter Albert)

## **Overview**
Fryderyk Wiatrowski and Peter Albert discuss how autonomous browser agents can replace repetitive, rule-based tasks in the workplace, starting with reactive jobs (e.g., customer support, meeting scheduling) and gradually expanding to more complex proactive roles. They emphasize the shift from manually prompting agents to enabling them to operate independently through predefined rules and triggers, while acknowledging current limitations in AI reliability and scalability.

---

## **Key Points**
1. **Reactive vs. Proactive Jobs**:
   - **Reactive jobs** (e.g., customer support, processing refunds) are easier to automate due to their rule-based nature.
   - **Proactive jobs** (e.g., founder roles, strategic decision-making) are harder to automate but still contain reactive components that can be handled by agents.

2. **Agent Autonomy**:
   - Agents can act as "employees" by following rules and triggers (e.g., emails, Slack messages) without constant human input.
   - Initial training sets the rules, after which agents handle tasks autonomously, reducing manual oversight.

3. **Triggers and Rule Sets**:
   - A "pool of triggers" (e.g., market movements, emails) enables agents to react to specific events.
   - Expanding rule sets allows agents to handle increasingly complex tasks, moving closer to replacing proactive roles.

4. **Browser Agents vs. APIs**:
   - Browser-based agents offer greater flexibility than APIs, which are often limited or poorly implemented.
   - The goal is to create agents that can perform generic actions in browsers, potentially replacing humans in more tasks.

5. **Challenges**:
   - Current agents can reliably handle 100–1000 steps but lack full trustworthiness.
   - Continuous improvement in foundation models (e.g., reasoning capabilities) is critical for handling complex, proactive tasks.

---

## **Key Insights**
- **Fryderyk's Vision**: Agents should act like employees, not just tools. For example, an agent like *Jace* can autonomously set up meetings by analyzing calendars and suggesting options.
- **Peter's Actionable Advice**: Start with simple triggers (e.g., Slack, emails) and build agents that handle tasks without APIs. Highlight the need for continuous model refinement to enable proactive automation.

---

## **Challenges & Future Outlook**
- **Limitations**: Trust in AI reliability, API constraints, and the complexity of proactive tasks.
- **Path Forward**: Improve foundation models to enable sophisticated reasoning, expand rule sets, and integrate browser agents for broader task coverage.
```

## Full Transcript

[00:03] [Music]
[00:10] [Music]
[00:12] my name is Frederick co-founder of zal
[00:14] laabs and me and Peter my co-founder
[00:16] today we'll speak about the job
[00:18] replacement the future of job
[00:20] replacement and how we see agents in
[00:22] there I will start with a vision and
[00:25] then Peter will tell you a bit more how
[00:27] you can contribute to that by building a
[00:30] agents on your own um cool so let me
[00:34] start with asking you a question um if
[00:37] you could hire a reliable autonomous
[00:39] browser agent today let's assume that
[00:42] it's fully reliable and very fast what
[00:45] tasks would you want to have
[00:48] replaced I need free
[00:52] tasks ones travel organization yeah
[00:56] travel organization yeah expenses
[00:59] expenses that's
[01:00] yes calendar calendar I I love the
[01:03] calendar one um cool
[01:09] um I
[01:11] think if you have a reliable agent and
[01:15] you wanted to behave as your employee um
[01:20] our claim is that sometimes you don't
[01:21] want to prompt the
[01:23] agent just like when you hire a good
[01:26] employee to your company you spend some
[01:28] time on the on boarding ini training um
[01:32] but after that if it's a good employee
[01:35] it's very independent um you don't need
[01:37] to ask them to do things right so you
[01:40] can expect them to come up with the
[01:42] tasks on their own and you probably
[01:44] shouldn't expect them to ask you every
[01:46] day uh what should be done you don't
[01:49] want to overlook everything that's being
[01:52] done and you don't you want the employee
[01:54] to come up come up with the tasks on
[01:56] their own ideally you just give them the
[01:58] vision and they will do the
[02:02] rest the question is how we can
[02:05] implement this into
[02:08] agents probably this is not the right UI
[02:12] for this um in this UI you just prompt
[02:15] the agent to do things for you oneof I
[02:17] think it's great for demos and for
[02:19] showing the capabilities of the agents
[02:21] like demo drives um but I don't think
[02:23] this is what the future looks
[02:26] like so the question we can ask
[02:29] ourselves is
[02:31] how to embed agents into our
[02:33] workflows um I think a good place to
[02:35] start is asking ourselves what are the
[02:39] high leverage activities that we want to
[02:41] preserve in our daily life and what's
[02:45] noise I will give you an example in a
[02:47] Founder's role a very high leverage
[02:50] activity um is hiring of course if I
[02:53] hire a team of 10 people they can do do
[02:56] the job for me 10 times better than me
[02:57] because I hired smart smarter people and
[02:59] uh
[03:00] it it's a huge leverage however this
[03:02] huge Leverage is surrounded by a lot of
[03:05] noise for example setting up meetings or
[03:07] searching for them on LinkedIn so I
[03:10] think the vision that we can um keep in
[03:12] mind when building agents and thinking
[03:14] about how we can embed them into our
[03:16] workflows is how to distill the high
[03:20] leverage activities and preserve them
[03:22] for ourselves while Outsourcing the low
[03:24] leverage things for
[03:26] agents
[03:28] um one solution right now is just to
[03:31] like if you're a I don't know a big
[03:32] company and a big founder you can hire
[03:35] an executive assistant that will do the
[03:36] meetings for you and set up those things
[03:39] uh you probably need to give them a big
[03:40] salary like a 50 70k or something um but
[03:44] initially you always start with a
[03:46] problem it's not like you look for an
[03:48] executive assistant you start with a
[03:50] problem hey I need to set up meetings
[03:52] and I don't have a very specific need
[03:55] for all the surrounding skills that they
[03:57] have so instead of hiring how about we
[03:59] just hire agents to do just this one
[04:02] thing um I think if we find a way to
[04:05] implement agents in this way um that
[04:07] would be truly
[04:08] revolutionary um so for example here you
[04:11] know if if we build a simple agent today
[04:14] if you use our agent Jace go to ji and
[04:16] user agent you can just see CJs into
[04:18] your emails and it will do the meeting
[04:19] setup for you super simple doesn't need
[04:21] to interact with browsers tools anything
[04:23] needs to know your calendar and uh and
[04:26] needs to have access to your
[04:27] availability that's it so as you can see
[04:29] I see jce jce is replying to an an
[04:32] investor interested in zal laabs and
[04:34] setting up a meeting for me knowing my
[04:37] availability um that's sweet um but you
[04:39] know most of our tasks require
[04:42] Integrations and Tool access right um I
[04:47] think in order to think about how we can
[04:50] enable those uh Integrations we can
[04:53] distinguish two modes of human
[04:56] work one is reactive and the other one
[04:59] is
[05:02] proactive a great example of a reactive
[05:05] job is a customer
[05:07] support what happens in Customer Support
[05:10] is that when you get an email for
[05:12] example asking for a refund you do a
[05:15] very well- defined task so what you do
[05:17] is you go to a h go to your logging
[05:20] system or whatever you see whether
[05:22] someone used the app or not and based on
[05:24] that you can give them a refund or
[05:26] not um and that's pretty simple uh you
[05:30] need to attach stri the agent can do the
[05:32] refund and everything and then there are
[05:34] those proactive jobs like for example a
[05:36] Founder job where it's super difficult
[05:38] to describe what needs to be done by a
[05:41] simple set of rules right um however we
[05:45] still think that in every job even in
[05:47] Founders job um there is the reactive
[05:50] layer that still creates the noise and
[05:53] ideally would would be handled for us um
[05:55] so let's focus on on the reactive part
[05:58] we think that the reactive jobs will go
[06:01] first um the beauty of the reactive
[06:05] things is that once you set the rules
[06:07] for the agent once you go about the do
[06:08] the initial training you don't need to
[06:10] prompt the agents anymore uh they will
[06:15] um they will just follow the rules and
[06:17] do everything for you um but once the
[06:20] complexity comes in it can be more
[06:22] difficult of course agents as of today
[06:24] can perform reliably I think hundreds up
[06:27] to a thousand steps um but uh it's more
[06:30] we we can't really trust them yet so we
[06:32] have to be
[06:35] careful okay so we talked about the
[06:38] reactive bit and the proactive bit I
[06:41] think the first step to implementing the
[06:43] reactive um drop replacement by agents
[06:46] is to create a pool of triggers the
[06:49] triggers that cause the reactions of
[06:52] Agents once you have the pool and the
[06:54] Agents know the rules by which they
[06:56] should pick up tasks and perform the
[06:58] actions
[07:01] the agents then can like the pool being
[07:04] being for example you know the slack
[07:05] messages emails or phone calls the
[07:07] agents can pick up the tasks suggest
[07:09] solutions for you do some upfront work
[07:12] in the browser and then just show you
[07:13] hey do you do you want me to perform
[07:15] this action and then you can just
[07:16] approve so we went from prompting agents
[07:19] to do things to manage our calendars um
[07:22] to agents doing this on their
[07:27] own I think
[07:30] I think we all know that everything is a
[07:32] reaction in particular like even
[07:35] Founders job is about reacting to things
[07:38] like macro Market movements things that
[07:40] are
[07:42] rather um unusual and they're not many
[07:45] templates to being a Founder as opposed
[07:47] to for example in Customer Support um
[07:52] however you know the more descriptive
[07:53] our rule set is the more proactive jobs
[07:57] we will be able to replace um and as we
[08:00] extend the rule set for reacting to the
[08:03] triggers I think we'll go closer and
[08:07] closer to replacing the the proactive
[08:11] jobs so assume that we have built the
[08:14] meta aggregator of all the triggers that
[08:16] is being you know micro movements of the
[08:18] market as well as you know emails phone
[08:20] calls slack messages linear issues
[08:22] whatever whatever triggers our actions
[08:25] um I think the continuous Improvement of
[08:27] the foundation models and they cognitive
[08:30] cognitive abilities going up will allow
[08:32] us to have a very complex rule set
[08:35] because those models will be able to
[08:37] reason just like humans in terms of
[08:40] performing their jobs and deciding on
[08:42] what's next um but the question is how
[08:45] to build this aggregator and I think a
[08:47] very simple way to start would be for
[08:49] example in linear or in slack and then
[08:51] agents just picking up tasks and
[08:53] Performing them um but then once we
[08:56] build the aggregator The Next Step
[08:59] is to make the agents act and you know
[09:03] browsers as opposed to apis uh allow us
[09:06] for very generic actions um apis are
[09:09] very often limited and not really well
[09:11] implemented so if we can make the
[09:14] browser agents
[09:15] work can we fully replace humans at
[09:18] their jobs um I will pass now to Peter
[09:22] and Peter will tell you how you can
[09:24] Implement browser agents today to
[09:27] reliably perform your daily jobs and
[09:31] what are the challenges on the way so hi
[09:35] Peter I previously worked on the number
[09:37] two models at meta and I'll yeah like FR
[09:40] said I'll give you a bit more actional
[09:42] insights on how to actually build agents
[09:44] and kind of what the steps are uh you
[09:46] need to go through there um so I think
[09:49] like if you want to build any kind of LM
[09:52] part in your your system and especially
[09:54] for agents you go through a few
[09:56] different steps of based on the
[09:58] complexity of your task and how much
[10:00] performance you want to have um and
[10:02] basically this is kind of separate for
[10:04] every single system you have um you
[10:06] usually can start off with prompting and
[10:08] once things get more complex you add
[10:10] cognitive architectures you can add fine
[10:12] tuning and end reinforcement learning
[10:14] but I would only I would kind of go
[10:16] through each of the steps separately
[10:18] because each of these kind of reduces
[10:19] your iteration speed a lot so pump in
[10:21] cognitive architectures you can do
[10:23] things within hours find tring
[10:25] reinforcement learning is like more like
[10:26] a week to month monthly projects and any
[10:28] kind of changes you want to make
[10:30] basically slow everything down a lot um
[10:33] but if you kind of need to go on a
[10:35] certain task to really high performance
[10:36] you kind of have to go also through
[10:38] steps uh so first steps I'll um some
[10:42] general ideas like about how to improve
[10:44] your prompting so usually it's a good
[10:47] idea to kind of rewrite your prompts
[10:48] with language models itself because you
[10:50] kind of use the low complexity text when
[10:53] you give to a model so also you can have
[10:55] your own misunderstandings that you had
[10:57] initially will kind of be taken out
[10:59] we also try to use like XML syntax like
[11:02] andropia kind of started with this for
[11:04] we prompts and but I think it's useful
[11:06] for any model just to separate
[11:08] instructions from content um also some
[11:12] useful mindset is to always try to match
[11:15] the fine-tuning and pain distribution of
[11:17] your language model so if you use gp4
[11:19] you kind of have to think about what did
[11:21] open I probably fine tune models with
[11:24] and and also what is kind of in rep in
[11:26] there so for example you should probably
[11:29] prefer Jon or XML or markdown UniFi
[11:31] format um when trying to Output text
[11:35] just because it's more more more
[11:37] frequent and retrain distribution so if
[11:39] you shouldn't probably introduce your
[11:40] own format or your kind of own syntax to
[11:42] do things you want to do things just
[11:45] like we're most likely to appear in the
[11:48] web um yeah this also similar for what
[11:51] you put in the system prompt versus user
[11:52] prompt how you if you if you decide to
[11:54] split up things into multim messages or
[11:56] just one just have to think about like
[11:58] what probably open I got in their fine
[12:00] tuni data set what most people do and
[12:03] this usually a good way to do to stay
[12:05] within the distribution of the fine
[12:07] tuning and will give you better
[12:09] performance um also you should kind of
[12:12] try to think of how to minimize
[12:13] computation at each token so if you have
[12:16] like a complex task um one one thing you
[12:19] to keep in mind that you if you want to
[12:20] Output uh for example mappings like like
[12:23] uh element ID five or or four you
[12:25] usually want to prefer text text values
[12:28] so if you model can output TT is better
[12:29] than specific numbers and because
[12:32] basically you're skipping one mapping
[12:34] step so you should try to let the model
[12:37] only reason about one thing at a time um
[12:39] it's also relevant like if you do
[12:41] classification for example like it's
[12:42] better to First classify things into
[12:43] broader categories and smaller ones
[12:45] instead of directly going to the
[12:46] smallest one and if you do this which
[12:48] just will just improve performance in
[12:50] general I would also like if you have
[12:52] some idea about how to think about a
[12:54] problem I would try to give you if if
[12:56] you do Chain of Thought I wouldn't just
[12:57] say say uh let's think step by step but
[13:01] instead you should kind of think about
[13:02] how you would approach a problem and
[13:04] specifically add these things in your
[13:06] chain of thought so for example first
[13:08] thinking about sum summarizing the
[13:09] problem you have and and going for all
[13:12] the
[13:13] steps um few more ideas is that you
[13:16] should think about everything that you
[13:18] put in prompt is basically noise and and
[13:21] some valuable cont in there so if you
[13:22] can reduce the noise as much as possible
[13:25] it only have the most relevant context
[13:27] in there the model doesn't need to uh
[13:29] find out what is noise and what is real
[13:31] context um for Featured examples some
[13:34] really useful tips is that you shouldn't
[13:36] probably like like if you have really
[13:38] long inputs and really long future
[13:40] examples you don't have to show the full
[13:41] ones you just just only focus on the few
[13:44] most important parts of them and model
[13:46] still usually um capture kind of how how
[13:49] things work um also like even once you
[13:52] start prompting you want to already set
[13:54] up some maybe like 10 20 examples to
[13:57] kind of always run each prom through
[13:58] additionally to will have like some
[13:59] better end to end evils as
[14:01] well um yeah so once you kind of
[14:04] exhausted all the gains you kind of get
[14:06] with prompting you can try to split up
[14:08] task into multiple pieces so basically
[14:11] you can think about how much cognitive
[14:12] load you put on a on on a model with one
[14:14] prompt and if you can split Rings up
[14:16] further and also if you have some
[14:18] preconceived notion about how the
[14:19] problem should work you can kind of
[14:20] improve this so a few ideas about this
[14:23] is kind of that you add explicit State
[14:25] tracking of like if you have a longer
[14:26] task you basically keep track of the
[14:29] state that the task currently is in this
[14:31] basically increases the quality of
[14:33] context you kind of given your model um
[14:36] here some ideas for example are using
[14:37] kind of planning you kind of generate
[14:38] plans afterwards modify them replan you
[14:42] can also have the verification steps
[14:43] afterwards um or you kind of take notes
[14:46] or have a scratch Pad uh for
[14:48] intermediate
[14:49] work
[14:51] um but once you kind of split up things
[14:53] in multiple pieces when latency becomes
[14:55] more of an issue so there often the good
[14:57] ways to paralize the work while still um
[15:00] kind of getting good performance also
[15:03] for all of these kind of Agents it's
[15:04] really important to think about really
[15:06] natural interfaces for them to use tools
[15:09] um so for example we found that if you
[15:12] want to update State like for example uh
[15:15] some some notes you have it's often good
[15:17] to address them like with key value
[15:18] updates because basically you're kind of
[15:20] mimicking python syntax you kind of
[15:22] update some dictionary and this kind of
[15:24] allows you to Target elements really
[15:26] well because you first the model only
[15:27] needs to think about the key and then
[15:29] afterwards can think about what to
[15:30] update not do both things at the same
[15:33] time um can get even better performance
[15:35] usually with most models if you do full
[15:37] rewrites of what you kind of want to
[15:38] update because this gives the model even
[15:40] more time to think about things but when
[15:42] you add more latency so I think that's
[15:44] for example why you see in cursor like
[15:46] all the text Rewritten because currently
[15:49] when both best models are not very good
[15:51] at generating like small
[15:53] diffs um also you should try to avoid
[15:55] any recursive n structures if you can um
[15:59] this will just like more nested it is it
[16:01] will be just be more out of distribution
[16:03] and make it more complex for
[16:05] model
[16:06] um yeah also you can kind of use some
[16:08] reasoning templates if you know how rep
[16:10] are structured you should also kind of
[16:11] reflect this in a prompt um if you deal
[16:14] with images then one good idea is that
[16:16] you try to move the reasoning into your
[16:18] text so you first describe the key
[16:20] points in your image like let model
[16:22] output the text form what the image
[16:25] contains and then afterward reason about
[16:27] this just because the models have been
[16:28] trained on trillions of tokens and text
[16:30] and most of these uh like image language
[16:33] pairs are usually much less data so if
[16:36] you do reasoning about images it usually
[16:37] performs worse when if you first convert
[16:39] it into text and then afterwards into uh
[16:41] more
[16:42] text um you should also think about how
[16:44] to design your components to correct for
[16:46] one part if you one part in the system
[16:48] that creates an error that another
[16:49] handles it and the more cognitive
[16:52] components you kind of add the more
[16:53] brittleness you also add to the system
[16:55] so usually it's try it's a good idea to
[16:57] kind of keep them to a minimum um but on
[17:00] the other hand like more components you
[17:01] add you kind of more cognitive load you
[17:03] you split into smaller pieces so the
[17:04] model can can has less less load in
[17:07] this um in the next stage if you still
[17:11] don't get enough performance out of your
[17:13] model or if you want to get uh lower
[17:15] cost um you can kind of start for fine
[17:17] tuning and the simple way to kind of
[17:19] collect data no matter what your your
[17:21] use case is is by simulating basically
[17:23] real interactions in your app and you do
[17:26] this by creating templates about how a
[17:29] human like basically different roles of
[17:31] a human and when you instruct one
[17:34] language model to act as a human and
[17:36] basically rest of your system acts as
[17:38] normal and it's basically synthetic data
[17:40] that you can kind of use to to find on
[17:43] and for this like prompt diversity and
[17:44] difficulty is really key so I think one
[17:46] of the core issues of like alpaka models
[17:48] like in beginning the first uh kind of
[17:50] fine tune models that went out there was
[17:52] that the prompt difficulty was way too
[17:54] low if your models learn much better the
[17:56] more difficult your prompt is even if
[17:58] your task is not very difficult I would
[18:00] try to add more and more conditions and
[18:01] more and more complexity because when
[18:03] model has more things to learn than just
[18:04] a single question
[18:07] um yeah also another thing you can kind
[18:09] of uh try is like if you have multiple
[18:12] steps in your pipeline you can in the
[18:13] end if you do fine tune you can just
[18:14] still to skip some of them you basic
[18:16] have like some initial inputs and some
[18:18] final output and you can directly
[18:19] distill a model to get these first
[18:21] inputs and out generate your final
[18:23] outputs and this can increase a lot of
[18:25] uh increase your latency but will kind
[18:27] of decrease performance a
[18:29] bit
[18:31] um then the next step that's really easy
[18:34] is that you um kind of filter your data
[18:37] so this kind of gives you like usually
[18:38] with just fine tuning you can get like
[18:40] gbd4 performance on on your specific
[18:42] task but you can get much further if you
[18:44] simply do some rejection sampling or
[18:46] filtering of your data and for this a
[18:48] easy way is if you don't have execution
[18:50] feedback in some way so that you um
[18:52] basically use language Model judges just
[18:54] judge your output of your model or of a
[18:56] larger system or even the final output
[18:58] of your system then basically you filter
[19:00] out whole SS of your data that you know
[19:03] that probably didn't work very well even
[19:04] if your charge is not perfect with the
[19:06] kind of increase your performance a lot
[19:10] um yeah and finally so last step that
[19:14] you can kind of approach is like
[19:15] reinforcement learning so this even
[19:17] allows you to kind of optimize or
[19:19] multiple steps in your system so it's
[19:20] especially important for agents and you
[19:23] good ways to get a signal for this for
[19:25] this is execution feedback or like we
[19:26] said this language model charges of
[19:28] different parts of your system but I
[19:29] would usually consider reinforcement L
[19:31] kind of a final step when other methods
[19:33] don't work um because it makes it kind
[19:35] of difficult to move to one uh two
[19:37] different models and also there's a lot
[19:38] of setup cost you have to do um yeah so
[19:42] I think that's that's it awesome
[19:49] [Music]
