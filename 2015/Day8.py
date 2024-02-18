import re

# --- PART ONE ---

# Putting the content of the data file in the variable
with open("Day8_input.txt", "r") as f:
    input = f.readlines()

source_string = ""
modified_string = ""

for line in input:
    line = line.rstrip()

    # This is going to be one big string to match another string on
    source_string += line

    # Removing quotes and adding to the modified_string
    modified_string += line[1:-1]

# Replacing as required using regex to some random char (*)
modified_string = re.sub(r"\\x..|\\.", "*", modified_string)

print(len(source_string) - len(modified_string))

# --- PART TWO ---

# We will be adding the extra characters to this variable in the loop
extra_chars = 0

for line in input:
    line = line.rstrip()

    # Don't forget to add 2 for the surrounding quotes that each string has
    extra_chars += line.count("\\") + line.count('"') + len(line) + 2

# Using the big string from part one
print(extra_chars - len(source_string))
