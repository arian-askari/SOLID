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


## Pipeline
<img src="./figures/SOLID_pipeline.svg">


