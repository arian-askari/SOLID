# SOLID: Self-seeding and Multi-intent Self-instructing LLMs for Generating Intent-aware Information-Seeking dialogs
<img src= "./figures/solid_logov5.png" width=100px></img>
[![](https://img.shields.io/badge/Language-English-brightgreen)](https://github.com/arian-askari/SOLID)

The official repository for the following paper: "SOLID: Self-instructing and Self-seeding LLMs for Large-scale Intent-Aware Informating-Seeeking Dialogue Generation".  **Work in progress: The code is under cleaning/organizing process**

## What we have done?
we propose SOLID to tackle the challenges of using LLMs for generating intent-aware information-seeking dialogues with three novel strategies:

  1. **Self-seeding,** where LLM generates its own dialogue starter seed, ensuring that LLM is familiar with seed;
  2. **Self-instructing,** which involves the LLM to generate its own instructions for significantly reducing the reliance on human-written instructions;
  3. **Intent-aware dialgoues generation**, which automates the dialogue process step by step.
  As an output example of SOLID, we present the SOLID dataset, encompassing more than 300k open-domain, intent-aware dialogues, surpassing the size of existing datasets.

Furthermore, we propose SOLID-RL, empowered by a novel mixed-quality training method, that leverages reinforcement learning (RL) to enhance the efficiency of generation by optimizing the LLM to generate an intent-aware dialogue in one step instead of utterance-by-utterance.


## Motivation 
Creating datasets is a resource-intensive endeavor, with annotation costs often reaching significant amounts, as evidenced by [1], where annotating around 2k dialogues incurred a cost of $1700. In contrast, our approach leverages the open-source LLM and Nvidia A6000 GPUs with 40GB memory, allowing us to release 200k dialogues composed of X utterances. This dataset is designed for training intent predictors, system initiative prediction models, mitigating hallucination, and addressing various other tasks. Each dialogue is associated with an entity card, both of which are automatically generated. Following the intent proportions and sequences from MSDialogue-intent ensures alignment with real-world intent sequences.

## Pipeline
<img src="./figures/SOLID_pipeline.svg">


## Example of Generated Dialogue

## SOLIDGen Pipeline
We introduce the Intent-Aware Information-Seeking Conversation Generation (SOLIDGen) pipeline to construct a large-scale dataset. The entire dataset is generated from scratch using LLM knowledge without additional content. The pipeline comprises the following steps:

1. **Generating Entity Types:** We instruct LLM to "Provide a list of 100 entity types." Out of these, 2 types are repeated, resulting in 98 unique entity types. While we acknowledge the option to use Wikipedia for category selection, we opt to let LLM choose categories it deems most common, enhancing recall with higher quality.

2. **Generating Entity Names:** Subsequently, we request LLM to "Provide a list of 100 entity names starting with the letter {} and categorized in type {}." With 26 alphabets and 98 entities, this generates 2548 instructions, yielding approximately 254,800 entities. After noise removal, we limit the count to around 50k entities (refer to the full prompt in '/prompts/gen_entity_name_prompt.txt').

3. **Generating Type Attributes:** We prompt LLM to "Provide a list of 10 attributes for the following entity type: <entity_type>."

4. **Generating Background Document:** Employing the prompt "If you have knowledge...", we instruct LLM to generate a background document.

5. **Generating Conversation Starter:** Seeking a holistic approach, we task LLM to generate a conversation starter by considering entity card, background document, and type attribute. This process results in approximately 500k conversation starters.

6. **Picking Sequence of Intents from Real-World Dataset:** An example sequence of intent, such as ["OQ", "FD_PF", "RQ", ""], denotes the first utterance having the "Original Question" intent, and so forth. The sequence length can be extended limitlessly by repetition.

7. **Assigning Sequence of Intents Randomly:** Randomly assigning sequences of intents to conversation starters and their corresponding entity cards.

8. **Generating a Conversation:** Crafting dialogues involves a meticulous process. For each of the 12 distinct intents in MSDialogue, we manually construct 24 instructions to guide LLM in generating the next utterance. This step-by-step approach, enriched with historical conversation context, ensures adherence to the intended dialogue flow. For utterances with multiple intents (up to three), a merged instruction is generated based on the definitions of each intent. The used instructions will be released soon.

9. **Post-Processing:** To ensure quality and eliminate noise, we perform post-processing on the generated dialogues.

10. **Final Dataset:** After completing these steps, we assemble a dataset comprising 200k dialogues. A forthcoming version with approximately 400k dialogues is currently in the works.

11. **Filtering:** Anticipate the addition of filtering functionalities in the near future.

## Data Statistics

## Summary of the Approach
This work explores the fluency of LLMs in generating conversations across a wide spectrum of knowledge. Unlike the Self-instruct methodology based on seeds, our approach involves the complete synthesis of the dataset from scratch, bypassing the imposition of seeds on LLM.

The generation process, depicted in the figure above, includes two main steps: (1) generating entity cards by LLM; (2) generating conversation starters; and (3) generating dialogues based on entity cards and conversation starters. Each entity card, synthetically generated by LLM, consists of entity name, entity type, and a background document. The conversation starter, serving as the first question in a dialogue, is generated by passing entity information to LLM, ensuring constraints based on type.

## Overview
aaa

## Application of the Dataset
### Intent Prediction
This repository explores the utilization of dialogues generated by the Large Language Model "Zephyr" as training data for intent predictors. The focus is on assessing the efficacy and implications of using intent-aware synthetically generated conversations.
