# IConv-LLM:
A large scale datased generated by an open-source large langague model, Zephyr-7B-Beta. This dataset contains of Intent-Aware Information-Seeking Dialogues.

## Motivation 
Building such a dataset is an expensive task as [1] states annotating dataset for about 2k diagloues cost 1700$.  This is while, we release 200k dialouges composed of X utterances with using open-source LLM and using accessible GPUs in academia, Nvidia A6000 with 40GB GPU memory. Our dataset is suitable for training intent predictors, system initiatve prediction models, reducing hallucination, and so many other tasks. Each generated dialogue is associated with an entity card. Both of entity card and the dialogue has been generated automatically. We follow same proportion of intent and sequence of intents in MSDialogue-intent in order to build a large scale dataset that can being aligned with real-world sequence of intents.

## Example of generated dialogue

## IConvGen pipeline
We propose a novel pipeline called Intent-Aware Information-Seeking Conversation Generation (IConvGen) that build a large scale dataset for training intent-aware prediction models. Please note that the whole dataset is generated  from scratch by using LLM knowledge without any extra content as the seed. Our pipline address thast in the following steps:

1. Generating entity types: We ask LLM to "Provide a list of 100 entity types". Out of that, 2 types are repeated which results to 98 entity types for us. We are aware that we could use wikipedia and pick the categories from there. However, we wanted let the LLM to pick categories that are most common for it and it remembers them with higher quality.
2. Generating entity names: Next, we ask LLM to "Provide a list of 100 entity names that start with letter {} and categorized in type {}". We have 26 alphabets and 98 entities. This way we create 2548 instructions automatically, per instruction we get about 100 entities that ends up to 254800 entities. However, we remove noisy entities and limit it to about 50k entities.(See full prompt in '/prompts/gen_entity_name_prompt.txt')
3. Generating type attribute: We prompt LLM to "Provide a list of 10 attributes for the following entity type: <entity_type>".
4. Generating background document: We prompt LLM to "If you have knowledge..."
5. Generating conversation starter.  We ask LLM to generate a conversation starter considering entity card, background document, type attribute. This ends up in about 500k conversation starters.
6. Picking sequence of intents from real-world dataset. Example of a sequence of intent: ["OQ", "FD_PF", "RQ", ""] which means the first utterance of dialogue has "Original Question" intent, the next utterance has ... blah balh. We could easily increase the size of sequence of intents by repeating it, therefore we can have unlimited sequence of intents.
7. Assigning sequence of intents randomly to conversation starter and its corresponding entity card.
8. Generating a conversation given a conversation starter, entity card, and sequence of intents. Each intent has a different defintion for user or agent. Therefore, as we have 12 distinct intents in MSDialogue, we manually craft 24 instructions per intents. These instructions guide the LLM to generate the next utterance in a way that it follow the requried intent. We generate a dialogue step-by-step. In each step, we provide the conversation history which is so far generated conversation and we ask for generating the next utterance that follows a specific intent. Some utterances can have multiple intents (up to three intents). For those, we ask LLM to generated a merged instruction based on the definition of each intent. We release the used instruction soon.
9. We post-process the generated dialogues in order to ensure the quality and remove noisy data.
10. After all of these steps, we end up to 200k dialogues. A new version with about 400k dialogues will be released soon.
11. Filtering. Comming soon!

## Statistic of the data

## Summary of what we did
Previous work has shown that LLMs tend to have higher fluenty when they are generating about more frequent knowledge. However, it is not clear how we can measure if a conversation can be considered rare or frequent for LLM as it is not clear which topics are memorized deeper by LLM. 

In this work, we aim to use LLM to generate the whole synthetic dataset from scractch without enforcing llm on some seeds. This is in contrast to the Self-instruct methodology which is based on seeds.

Above figure illustrates the steps of generation in our novel pipeline. Our pipleine constists of two main steps: (1) generating entity cards by LLM; (2) generating conversation starter (3) generating dialogues based on entity cards and conversation starter. Each entity cards synthetically generated by LLM and contains of entity name, entity type, a background document. Each conversation starter is a question that can be the considered as first question in a dialogue. We generate 10 attributes per each entity type (e.g., name, date of birth for Person type). Given an entity card, for each of its attributes, we pass these information to llm in order to generated the conversation starter. This way, the conversation starter be constrained on that type and we can generate 10 question per entity cards. 


## Overview
aaa

## Application of such a dataset
### Intent precition
This repository explores the potential of using dialogues generated by the Large Language Model "Zephyr" as training data for intent predictors. The focus is on understanding the effectiveness and implications of utilizing intent-aware synthetically generated conversations.
