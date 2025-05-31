---
type: youtube
title: How to evaluate a model for your use case: Emmanuel Turlay
author: AI Engineer
video_id: pj_hKFhnJCw
video_url: https://www.youtube.com/watch?v=pj_hKFhnJCw
thumbnail_url: https://img.youtube.com/vi/pj_hKFhnJCw/mqdefault.jpg
date_added: 2025-05-26
category: Machine Learning Evaluation
tags: ['model evaluation', 'NLP', 'machine learning', 'AI benchmarks', 'data analysis', 'model comparison', 'deep learning', 'evaluation metrics', 'Sematic', 'AirTrain', 'GPT-4', 'Flan T5']
entities: ['Emmanuel Turlay', 'Sematic', 'AirTrain', 'GPT-4', 'Flan T5', 'Llama 2', 'Falcon', 'GLUE', 'SuperGLUE', 'TriviaQA']
concepts: ['Model evaluation', 'Natural Language Processing (NLP)', 'Benchmarking', 'Statistical measurement', 'Custom evaluation procedures', 'Metric distribution analysis', 'AI model comparison', 'Language model training', 'Data-driven decision making', 'Machine learning metrics']
content_structure: tutorial
difficulty_level: intermediate
prerequisites: ['Basic understanding of machine learning', 'Familiarity with NLP concepts', 'Experience with model training pipelines']
related_topics: ['AI ethics', 'Machine learning optimization', 'Deep learning frameworks', 'Data science methodologies', 'Artificial intelligence research', 'Model interpretability', 'Computer vision evaluation', 'AI deployment strategies']
authority_signals: ['Emmanuel Turlay is the CEO of Sematic', 'AirTrain was designed specifically for this purpose', 'We have found that GPT-4 offers a good trade-off of speed and correctness']
confidence_score: 0.85
---

# How to evaluate a model for your use case: Emmanuel Turlay

**Video**: [Watch on YouTube](https://www.youtube.com/watch?v=pj_hKFhnJCw)  
**Published**: 3 months ago  
**Category**: AI/ML  
**Tags**: model-evaluation, language-models, ai-metrics, benchmarking, nlp, machine-learning, evaluation-techniques  

## Summary

# Comprehensive Summary of "How to evaluate a model for your use case: Emmanuel Turlay"

## Overview  
Emmanuel Turlay, CEO of Sematic, discusses the challenges of evaluating language models for specific use cases. He highlights that while metrics and benchmarks exist, they often fail to capture performance on tailored tasks. The talk emphasizes the need for custom evaluation procedures and introduces techniques like using another model to grade outputs, alongside tools like AirTrain for streamlined evaluation.

---

## Key Topics  
- **Model Evaluation Basics**:  
  - Defined as statistical measurement of a model's performance on a specific use case using an independent dataset.  
  - Crucial for ensuring safety, performance, and continuous improvement in ML workflows.  

- **Limitations of Generic Metrics**:  
  - Metrics like BLEU (precision-based) and ROUGE (recall-based) are useful for tasks like translation or summarization but lack nuance for specific applications.  
  - Benchmarks (e.g., GLUE, TriviaQA, ARC) provide a general landscape but don’t reflect real-world use case performance.  

- **Custom Evaluation Needs**:  
  - Unique tasks (e.g., extracting symptoms from medical notes, API payload generation) require tailored evaluation procedures.  
  - No universal method exists for assessing models on domain-specific data.  

- **Using Models to Grade Outputs**:  
  - A "magic trick" involves using another language model (e.g., GPT-4, FLAN T5) to score outputs based on custom criteria.  
  - Example: Prompting a model to rate the politeness of email closings on a 1–10 scale.  

- **Tools for Evaluation**:  
  - AirTrain is highlighted as a platform for uploading datasets, comparing models, and visualizing metric distributions.  

---

## Important Quotes  
- *"There is no one-size-fits-all process for evaluating models on specific tasks."*  
- *"You can describe to NLM what you’re trying to accomplish..."*  
- *"The best grading model at this time is still GPT-4, but can be quite costly..."*  

---

## Actionable Items  
1. **Develop Custom Evaluation Procedures**: Move beyond generic metrics to design task-specific evaluation criteria.  
2. **Leverage Model-Based Scoring**: Use models like GPT-4 or FLAN T5 to generate scores for outputs based on custom prompts.  
3. **Utilize Tools Like AirTrain**: Upload datasets, compare models, and visualize performance metrics for data-driven decisions.  
4. **Balance Cost and Accuracy**: Consider trade-offs between model cost (e.g., GPT-4) and efficiency (e.g., FLAN T5) for large-scale evaluation.  
5. **Prioritize Domain-Specific Metrics**: Focus on metrics that align with real-world application goals (e.g., politeness, accuracy, relevance).  

---  
*For more details, visit [AirTrain](https://www.airtrain.ai) for early access.*

## Full Transcript

[00:01] [Music]
[00:17] hi everyone I'm Emanuel CEO of sematic
[00:21] the company behind air train today I
[00:24] want to talk about a difficult problem
[00:26] in the language modeling space and that
[00:28] is
[00:28] evaluation unlike in other areas of
[00:31] machine learning it is not so
[00:33] straightforward to evaluate language
[00:35] models for a specific use case there are
[00:38] metrics and benchmarks but they mostly
[00:41] apply to generic tasks and there is no
[00:43] one-size fit so process to evaluate the
[00:45] performance of a model for a particular
[00:47] use
[00:48] case so first let's get the basics out
[00:51] of the way what is model
[00:53] evaluation model evaluation is the
[00:56] statistical measurement of the
[00:57] performance of a machine learning model
[01:00] how well does a model perform on a
[01:02] particular use case measured on a large
[01:04] data set independent from the training
[01:06] data
[01:07] set model evaluation usually comes right
[01:10] after training or fine-tuning and is a
[01:12] crucial part of model development all ml
[01:15] teams dedicate large resources to
[01:17] establish rigorous evaluation procedures
[01:20] you need to set up a solid evaluation
[01:23] process as part of your development
[01:24] workflow to guarantee performance and
[01:26] safety you can compare evaluation to
[01:29] running a test Suite in your continuous
[01:31] integration
[01:32] pipeline in traditional supervised
[01:34] machine learning there is a whole host
[01:36] of well-defined metrics to clearly grade
[01:39] A model's
[01:40] performance for example for regressions
[01:43] we have the root mean squared error or
[01:45] the mean absolute error for classifiers
[01:49] people usually use Precision recall or
[01:53] F1 score and so on in computer vision a
[01:57] popular metric is the intersection of
[02:00] Union so what metrics are available to
[02:02] score language
[02:04] models well unlike other types of models
[02:07] returning structured outputs such as a
[02:09] number a class or a bounding box
[02:12] language models generate text which is
[02:15] very unstructured an inference that is
[02:17] different from the ground truth
[02:19] reference is not necessarily
[02:21] incorrect depending on whether you have
[02:23] access to labeled references there are a
[02:25] number of metrics you can use for
[02:28] example blue is a precision based metric
[02:31] it measures the overlap between engrams
[02:34] that is sequences of tokens between the
[02:36] generated text and the inference it's a
[02:39] common metric to evaluate translation
[02:41] between two languages and can also be
[02:43] used to score
[02:45] summarization it can definitely serve as
[02:47] a good Benchmark but it is not a safe
[02:49] indicator of how a model will perform on
[02:51] your particular task for example it does
[02:54] not take into account intelligibility or
[02:57] grammatical correctness Rouge is a set
[03:00] of evaluation metrics that focuses on
[03:02] measuring the recall of sequences of
[03:04] tokens between references and the
[03:07] inference it is mostly useful to
[03:10] evaluate for
[03:11] summarization if you don't have access
[03:13] to labeled references you can use other
[03:16] Standalone
[03:17] metrics for example density quantifies
[03:21] how well the summary represents pool
[03:23] fragments from the text and coverage
[03:25] quantifies the extent to which a summary
[03:27] is derivative of a text
[03:30] as you can see these metrics are only
[03:32] useful to score certain high level tasks
[03:35] such as translations and
[03:37] summarization there are also a number of
[03:40] benchmarks and leader boards that rank
[03:42] various models benchmarks are
[03:45] standardized test that's score model
[03:46] performance for certain tasks for
[03:49] example glue or general language
[03:52] understanding evaluation is a common
[03:54] Benchmark to evaluate how well a model
[03:57] understands language through a series of
[03:59] nine tasks for example paraphrase
[04:03] detection and sentiment
[04:05] analysis helis swag measures natural
[04:08] language inference which is the ability
[04:10] for a model to have common sense and
[04:13] find the most plausible end to a
[04:15] sentence in this case answer C is the
[04:18] most reasonable Choice there are other
[04:20] benchmarks such as trivia QA which asks
[04:24] almost a million trivia questions from
[04:26] Wikipedia and other sources and tests
[04:28] the knowledge of the model also Arc
[04:32] tests model's ability to reason about
[04:34] high school level science questions and
[04:36] there are dozens more benchmarks out
[04:38] there all these metrics and benchmarks
[04:41] are very useful to draw a landscape of
[04:43] how llms compare to one
[04:45] another but they do not tell you how
[04:47] they perform for your particular task on
[04:50] the type of input data that will be fed
[04:52] by your
[04:53] application for example if you're trying
[04:55] to extract symptoms from a doctor's
[04:58] notes or extract ract ingredients from a
[05:01] recipe or form a Chas and payload to
[05:03] query an API these metrics will not tell
[05:06] you how each model performs so each
[05:09] application needs to come up with its
[05:11] own evaluation procedure which is a lot
[05:13] of work there is one magic trick though
[05:17] you can use another model to grade the
[05:20] output of your
[05:21] model you can describe to nlm what
[05:24] you're trying to accomplish and what are
[05:26] the grading criteria and ask it to grade
[05:29] the out of another llm on a numerical
[05:32] scale essentially you are crafting your
[05:35] own specialized metrics for your own
[05:37] application here's an example of how it
[05:39] works you can feed your evaluation data
[05:42] set to the model you want to evaluate
[05:44] which is going to generate the
[05:45] inferences that you want to score then
[05:48] you can include those inferences inside
[05:50] a broader scoring prompt in which you've
[05:53] described the task you're trying to
[05:55] accomplish and the properties you're
[05:56] trying to grade and also you described
[05:59] the the scale across which it should be
[06:01] graded for example from 1 to 10 then you
[06:04] pass this scoring prompt to a scoring
[06:06] model which is going to generate a
[06:08] number a score to score the actual
[06:11] inference if you do this on all the
[06:13] inferences generated from your
[06:14] evaluation data set you can draw a
[06:16] distribution of that particular metric
[06:19] for example here is a small set of
[06:21] closing words generated for a
[06:23] professional emails we want to evaluate
[06:25] their politeness we can prompt a model
[06:28] to score the politeness of each
[06:29] statement from 1 to 10 for example
[06:33] please let us know as your earliest
[06:34] convenience scores highly while tell me
[06:38] ASAP will score
[06:39] poorly we found that the best grading
[06:41] model at this time is still gp4 but can
[06:44] be quite costly to use to score large
[06:46] data sets we have found that flan C5
[06:49] offers a good trade-off of speed and
[06:52] correctness air train was designed
[06:54] specifically for this Purpose with air
[06:56] train you can upload your data set
[06:59] select the models you want to compare
[07:01] describe the properties you want to
[07:03] measure and visualize metric
[07:05] distribution across your entire data set
[07:07] you can compare Lama 2 with Falcon flant
[07:10] T5 or even your own model then you can
[07:13] make an edicated decision based on
[07:15] statistical evidence sign up today for
[07:17] Early Access at AirTrain doai and start
[07:20] making data driven decision about your
[07:22] choice of
[07:23] llm thanks
[07:26] [Music]
[07:28] goodbye
