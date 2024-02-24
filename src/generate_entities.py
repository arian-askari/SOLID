# --------------------------------------------------------------------------------
# Project Name: SOLID
# File Name: generate_entities.py
# --------------------------------------------------------------------------------
# Authors of this file: Arian Askari
# --------------------------------------------------------------------------------
import os
from transformers import AutoTokenizer, LlamaForCausalLM, AutoModelForCausalLM
import torch
import sys
import tqdm
import string

device = torch.device("cuda")
model_name = sys.argv[1]  # "HuggingFaceH4/zephyr-7b-beta"
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    truncation=True,
    padding=True,
    padding_side="left",
    maximum_length=2048,
    model_max_length=2048,
)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.to(device)
tokenizer.pad_token = tokenizer.eos_token
model.generation_config.pad_token_id = model.generation_config.eos_token_id
base_out_path = sys.argv[
    2
]  # "/ivi/ilps/personal/aaskari/dataset/IconvGen/entities/entity_type_{}_letter_{}.txt"


def _generate_entities(inputs, tokenizer, model, batch_size, output_paths):
    tokens = tokenizer(inputs, return_tensors="pt", truncation=True, padding=True)
    tokens = tokens.to(device)
    generated_queries = []
    cnt = -1
    for i in tqdm.tqdm(
        range(0, len(tokens["input_ids"]), batch_size), desc="generating entities..."
    ):
        batch = tokens["input_ids"][i : i + batch_size]
        batch_output_paths = output_paths[i : i + batch_size]
        outputs = model.generate(
            input_ids=batch,
            attention_mask=tokens["attention_mask"][i : i + batch_size],
            min_new_tokens=1000,
            max_new_tokens=1000,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
            no_repeat_ngram_size=2,
        )
        outputs = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        for o, o_path in zip(outputs, batch_output_paths):
            cnt += 1
            o = o.strip()
            print("o_path: ", o_path)
            with open(o_path, "a+") as fp:
                fp.write(str(o))

    return True


entity_types = [
    "Person",
    "Organization",
    "Place",
    "Country",
    "City",
    "Product",
    "Service",
    "Company",
    "Animal",
    "Plant",
    "Food",
    "Beverage",
    "Vehicle",
    "Book",
    "Movie",
    "Song",
    "Artist",
    "Actor",
    "Actress",
    "Author",
    "Musician",
    "Athlete",
    "Politician",
    "Celebrity",
    "Brand",
    "University",
    "School",
    "Hospital",
    "Government Agency",
    "Nonprofit Organization",
    "Event",
    "Conference",
    "Festival",
    "Sport",
    "Team",
    "League",
    "Game",
    "Software",
    "App",
    "Website",
    "Social Media Platform",
    "Technology",
    "Device",
    "Gadget",
    "Instrument",
    "Tool",
    "Furniture",
    "Clothing",
    "Fashion Brand",
    "Artwork",
    "Painting",
    "Sculpture",
    "Architectural Structure",
    "Historical Figure",
    "Mythical Creature",
    "Deity",
    "Supernatural Being",
    "Character (Fictional)",
    "Language",
    "Programming Language",
    "Genre (Music, Film, Literature)",
    "Style (Fashion, Art)",
    "Historical Period",
    "Scientific Concept",
    "Chemical Element",
    "Particle",
    "Planet",
    "Star",
    "Galaxy",
    "Constellation",
    "Astronomical Object",
    "Natural Disaster",
    "Weather Phenomenon",
    "Disease",
    "Medication",
    "Medical Procedure",
    "Law",
    "Legal Case",
    "Political Ideology",
    "Social Movement",
    "Philosophy",
    "Religion",
    "Mythology",
    "Folklore",
    "Cuisine",
    "Recipe",
    "Beverage",
    "Sportsperson",
    "Entrepreneur",
    "Inventor",
    "Scientist",
    "Mathematician",
    "Philosopher",
    "Explorer",
    "Author",
    "Poet",
    "Photographer",
    "Journalist",
    "Activist",
    "Historical Event",
]  # prompt for that:  Provide a list of 100 popular entity types

one_word_letters = list(string.ascii_uppercase)  # 26
two_word_letters = []
for o_uppercase in one_word_letters:
    for o_lowercase in list(string.ascii_lowercase):
        two_word_letters.append(o_uppercase + o_lowercase)

word_letters = one_word_letters + two_word_letters

print("len(word_letters)", len(word_letters))  # 702
print("len(entitiy_types)", len(entity_types))  # 100
prompt_template = """Example1: 
Instruction: Provide a list of at least 10 entities categorized as 'Person' whose names begin with the letter 'A' Please include a new line after each entity.
Entities:
Abraham Lincoln
Albert Einstein
Alexander Graham Bell
Amelia Earhart
Anne Frank
Anton Chekhov
Arthur Conan Doyle
Audrey Hepburn
Auguste Rodin
Abraham Lincoln

Example2: 
Instruction: Provide a list of at least 100 entities categorized as '{entity_type}' whose names begin with the letter '{letter}' Please include a new line after each entity.

Entities:

"""
import os

do_not_replace = True
inputs = []
output_paths = []
for entity_type in entity_types:
    for letter in one_word_letters:  # let's try two_word letters later!
        output_path = base_out_path.format(
            entity_type, letter, model_name.replace("-", "_").replace("/", "_")
        )
        if do_not_replace == True:
            if os.stat(output_path).st_size == 0:  # only if it is empty, we work on it
                output_paths.append(output_path)
                inputs.append(
                    prompt_template.format(entity_type=entity_type, letter=letter)
                )
            else:
                print("skip file as it is already generated {}".format(output_path))


batch_size = 1  # 8

print("len(output_paths): ", len(output_paths))
print(
    "len(inputs): ", len(inputs)
)  
for (
    output_path
) in (
    output_paths
):  # I can later check if output exist then just skip that input & output
    fp = open(output_path, "w+")
    fp.close()

generated_contents = _generate_entities(
    inputs, tokenizer, model, batch_size, output_paths
)
