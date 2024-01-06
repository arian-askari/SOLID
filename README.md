# IConv-LLM:
A large scale datased generated by an open-source large langague model, Zephyr-7B-Beta. This dataset contains of Intent-Aware Information-Seeking Dialogues.

## Example of generated dialogue


## Summary of what we did
Previous work has shown that LLMs tend to have higher fluenty when they are generating about more frequent knowledge. However, it is not clear how we can measure if a conversation can be considered rare or frequent for LLM as it is not clear which topics are memorized deeper by LLM. 

In this work, we aim to use LLM to generate the whole synthetic dataset from scractch without enforcing llm on some seeds. This is in contrast to the Self-instruct methodology which is based on seeds.

Above figure illustrates the steps of generation in our novel pipeline. Our pipleine constists of two main steps: (1) generating entity cards by LLM; (2) generating conversation starter (3) generating dialogues based on entity cards and conversation starter. Each entity cards synthetically generated by LLM and contains of entity name, entity type, a background document. Each conversation starter is a question that can be the considered as first question in a dialogue. We generate 10 attributes per each entity type (e.g., name, date of birth for Person type). Given an entity card, for each of its attributes, we pass these information to llm in order to generated the conversation starter. This way, the conversation starter be constrained on that type and we can generate 10 question per entity cards. 

We formally illustrate the steps of generating this dataset completeley synthetically:

1. Generating entity types: We ask LLM to "Provide a list of 100 entity types". Out of that, 2 types are repeated which results to 98 entity types for us. We are aware that we could use wikipedia and pick the categories from there. However, we wanted let the LLM to pick categories that are most common for it and it remembers them with higher quality.
2. Generating entity names: Next, we ask LLM to "Provide a list of 100 entity names that start with . (See full prompt in '/prompts/gen_entity_name_prompt.txt')
3. Generating type attribute:
4. Generating 

## Overview
aaa

## Application of such a dataset
### Intent precition
This repository explores the potential of using dialogues generated by the Large Language Model "Zephyr" as training data for intent predictors. The focus is on understanding the effectiveness and implications of utilizing intent-aware synthetically generated conversations.
