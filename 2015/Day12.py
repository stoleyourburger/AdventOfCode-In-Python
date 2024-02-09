import json
import re

# --- PART ONE ---


# Putting the content of the data file in the variable
with open("Day12_input.txt", "r") as f:
    input = f.readlines()

# Taking a dictionary as input and returning a string as output
convert = json.dumps(input)

# Regex matching all possible numbers to include all number with and without a '-' in front
result = re.findall("-?\\d+", convert)

total = 0

for number in result:
    total += int(number)

print(f"Final number is: {total}")

# --- PART TWO ---

# Another approach with actually working with keys/values
input = json.loads(open("Day12_input.txt", "r").read())


# Wrapping everything in a function
def TotalNumbers(input):

    # Comparing the input type to the dictionary type
    if type(input) == type(dict()):

        # Excluding every occurence of 'red' with everything past it
        # Not really excluding but returning 0 instead of whatever is inside
        if "red" in input.values():
            return 0

        # If 'red' is not inside, we map (execute) the function with input.values() to check for other types in values
        return sum(map(TotalNumbers, input.values()))

    if type(input) == type(list()):

        # For each list recursively sum all the values
        return sum(map(TotalNumbers, input))

    # If nothing is left we return the input
    if type(input) == type(0):
        return input

    return 0


print(f"Second number is: {TotalNumbers(input)}")
