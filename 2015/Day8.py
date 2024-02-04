import re

# --- PART ONE ---

# Putting the content of the data file in the variable
with open("Day8_input.txt", "r") as f:
    input = f.readlines()

sourceString = ""
modifiedString = ""

for line in input:
    line = line.rstrip()

    # This is going to be one big string to match another string on
    sourceString += line

    # Removing quotes and adding to the modifiedString
    modifiedString += line[1:-1]

# Replacing as required using regex to some random char (*)
modifiedString = re.sub(r"\\x..|\\.", "*", modifiedString)

print(len(sourceString) - len(modifiedString))

# --- PART TWO ---

# We will be adding the extra characters to this variable in the loop
extraChars = 0

for line in input:
    line = line.rstrip()

    # Don't forget to add 2 for the surrounding quotes that each string has
    extraChars += line.count("\\") + line.count('"') + len(line) + 2

# Using the big string from part one
print(extraChars - len(sourceString))
