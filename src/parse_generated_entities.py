# --------------------------------------------------------------------------------
# Project Name: SOLID
# File Name: parse_generated_entities.py
# --------------------------------------------------------------------------------
# Authors of this file: Arian Askari
# --------------------------------------------------------------------------------
import glob
import string
import re
import re


def exclude_repeated_characters(word):
    # Use a regular expression to check if any character is repeated
    return not re.search(r"(.)\1", word)


def exclude_unicode_lines(text):
    if not re.match(r"^\\u[0-9a-fA-F]{4}(\\u[0-9a-fA-F]{4})*$", line):
        return text
    else:
        return ""


def exclude_if_digit_proportion_high(input_string, threshold=0.5):
    # Calculate the proportion of digits in the input string
    digit_count = sum(c.isdigit() for c in input_string)
    total_chars = len(input_string)
    digit_proportion = digit_count / total_chars if total_chars > 0 else 0
    # Check if the proportion of digits is higher than the threshold
    if digit_proportion > threshold:
        return ""  # Exclude the string
    else:
        return input_string  # Keep the string


def remove_digit_space_string(input_string):
    # Define a regular expression pattern to match strings with only digits and spaces
    pattern = re.compile("^[0-9\s]+$")
    # Check if the input string matches the pattern
    if pattern.match(input_string):
        # If it matches, remove the string
        return ""
    else:
        # If it doesn't match, keep the original string
        return input_string


dir_path = "./entities_prompt/*"
dirs_path = glob.glob(dir_path)
entities = []
# entities_path =
for path_ in dirs_path:
    line = open(path_, "r").read()
    new_part = line.split("Example2:")[1].split("Entities:")[1].strip()
    for l in new_part.split("\n"):
        entity_type = path_.split("/")[-1].split(".txt")[0].split("_")[2]
        l = l.strip()
        l = l.translate(str.maketrans("", "", string.punctuation))
        l = remove_digit_space_string(l).strip()
        l = exclude_if_digit_proportion_high(l, threshold=0.1)
        l = exclude_unicode_lines(l)
        if len(set(l)) <= 3:
            continue
        if l[0].isdigit():
            continue
        if len(l) == 0:
            continue
        if len(l.split()) > 4:
            continue
        skip_it = False
        # if len(l.split()<=2: continue
        for word in l.split():
            if len(word) < 4.7 or len(word) > 20:
                skip_it = True
        if skip_it == False:
            entities.append("{}\t{}".format(l, entity_type))
import json

entities = sorted(list(set(entities)), reverse=True)
entities = list(sorted(entities[387:], reverse=False))
entities = entities[17:]
# we found out there are noisy entities with \u characters which we exclude here.
with open("entities.json", "w") as fp:
    json.dump(entities, indent=True, fp=fp)
