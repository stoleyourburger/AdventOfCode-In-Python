import re

# --- PART ONE ---

input = "1321131112"


# We need to find repeating symbols in the string, get its length and replace these symbols with their length and symbol itself.
def Run(input, steps):

    for i in range(steps):

        # Using regex capturing any repeating character, concatenating length of the match with the first character of the group
        # Replacing the result variable and returning it
        input = re.sub(r"(.)\1*", lambda x: str(len(x.group(0))) + x.group(1), input)
    return input


print(len(Run(input, 40)))

# --- PART TWO ---

# Doing the same but 50 times
print(len(Run(input, 50)))
