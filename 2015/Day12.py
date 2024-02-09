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
