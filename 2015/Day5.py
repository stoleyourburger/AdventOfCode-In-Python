# Importing regular expressions library
import re

# --- PART ONE ---

# Putting the content of the data file in the variable
with open("Day5_input.txt", "r") as f:
    input = f.readlines()

# Regex magic. Making a variable to count each occurence of matched line
# and including/excluding required patterns. Pretty obvious use of regex
count = sum(
    1
    for k in input
    if len([x for x in k if x in "aeiou"]) > 2
    and not any(x in k for x in ["ab", "cd", "pq", "xy"])
    and re.search(r"([a-z])\1", k)
)

print(count)
