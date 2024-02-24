# SOLID: Self-seeding and Multi-intent Self-instructing LLMs for Generating Intent-aware Information-Seeking dialogs
<img src= "./figures/solid_logov5.png" width=100px></img>
[![](https://img.shields.io/badge/Language-English-brightgreen)](https://github.com/arian-askari/SOLID)

The official repository for the following paper: "SOLID: Self-instructing and Self-seeding LLMs for Large-scale Intent-Aware Informating-Seeeking Dialogue Generation".  **Work in progress: The code is under cleaning/organizing process**

## Overiew
We introduce SOLID, a novel approach to generating large-scale, intent-aware information-seeking dialogues. Our method leverages self-seeding and multi-intent self-instructing schemes to produce high-quality dialogues. Additionally, we propose SOLID-RL, an enhanced version of SOLID, designed to increase efficiency without compromising the quality of generated dialogues.

## Key Features

- **Self-Seeding**: Generates dialogue seeds using the LLM's own knowledge, ensuring high familiarity and quality.
- **Multi-Intent Self-Instructing**: Automatically generates prompt instructions for varying intent combinations, drastically reducing manual effort.
- **SOLID-RL with LMQ**: Enhances efficiency by 11x over SOLID without sacrificing quality, achieved by the novel Length-based Mixed-Quality (LMQ) training mechanism.

## Contributions

1. **Innovative Generation Method**: SOLID, with its self-seeding and multi-intent instructing, for creating intent-aware dialogues.
2. **Enhanced Efficiency**: SOLID-RL incorporates LMQ for faster and higher-quality dialogue generation.
3. **Extensive Datasets**: Release of SOLISpeak and SOLITurbo, two large-scale synthetic datasets for advancing intent prediction research.
4. **Superior IP Method Performance**: Training intent predictor (IP) methods on SOLID-generated data significantly improves effectiveness over traditional human-annotated datasets.

## Dataset
Explore our GitHub repository for a comprehensive guide, code, and access to our datasets:


# SOLID

## Figure of SOLID's pipeline
<img src="./figures/SOLID_pipeline.svg">


## Intent-Aware Dialog Generation with SOLID
SOLID introduces a new way to create and use dialog seeds for generating intent-aware dialogs illustrated in above figure. It begins with generating entity types, names, and attributes. This allows SOLID to make detailed background documents and questions. These elements help generate deeper and more varied dialogs, making the most of what large language models (LLMs) offer.

### Step 1: Seed Generation

The dialog generation in SOLID focuses on specific entities to ensure variety and familiarity. The process includes three important steps:

1. **Entity Type Generation**: The LLM is asked to come up with different entity types (e.g., 'Person') and their attributes (e.g., 'Occupation'). This creates a wide range of topics.
   
2. **Entity Name Generation**: For each entity type, the LLM creates specific names (e.g., 'Albert Einstein'). To ensure variety, SOLID prompts LLM to generate 100 entity names for each letter of the English alphabet for every entity type. This leads to 50,000 entity names after cleaning them up, providing a large pool of dialog seeds.



SOLID's dialog generation process pivots around specific entities, ensuring diversity and familiarity. The process involves three steps:

1. **Entity Type Generation**: Prompting the LLM to produce a variety of entity types (e.g., 'Person') and associated attributes (e.g., 'Occupation'), leading to a broad spectrum of discussion points.
   
2. **Entity Name Generation**: For each entity type, the LLM generates specific names (e.g., 'Albert Einstein'), aiming for diversity by generating 100 names per English alphabet letter for each entity type. This results in 50,000 entity names after post-processing.

### Step 2: Ice Breaker

With the seeds ready, the next step involves generating an ice breaker to kickstart the conversation:

1. **Background Document Generation**: Following insights from prior research, this step involves asking the LLM to create a document about the entity. This adds depth to the dialog and improves its quality.
   
2. **Conversation Starter**: With the entity type, attributes, name, and background document in hand, the LLM generates the first line of the conversation.

### Step 3: Intent-Aware Dialogs

Using the outputs from the first two steps, SOLID an algorithm, explained in the appendix of the paper, to generate dialog data, aiming to produce the next utterance constrained to intents at each step. This keeps the dialog intent-aware. 

