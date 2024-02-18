# --- PART ONE ---

# Putting the content of the data file in the variable
with open("Day3_input.txt", "r") as f:
    input = f.read()

# Coordinates, but they are really only part of the key in the dictionary
x = 0
y = 0

# Each iteration adds a new present to the house at current position, simply used as a counter
i = 0

# Declaring a dictionary with the existing house with a present included
# We will use parts of key in the dictionary as x and y coordinates and will be changing them in the loop
map = {f"{x}, {y}": 1}

# Iterating through the houses. For each step we are incrementing the x or y of the key in the dictionary
# Because each step adds one present to the house anyways, we are adding a present to the hose.
# (We currently don't care about the $i variable: as long as each step it is being incremented, that value will
# be used to count the amount of houses visited)

for step in input:
    i += 1
    match step:
        case ">":
            x += 1
            map[x, y] = i
        case "<":
            x -= 1
            map[x, y] = i
        case "^":
            y -= 1
            map[x, y] = i
        case "v":
            y += 1
            map[x, y] = i

print(f"Santa visited {len(map)} houses")

# --- PART TWO ---

# Coordinates, but they are really only part of the key in the dictionary
x = 0
y = 0

# Each iteration adds a new present to the house at current position, simply used as a counter
i = 0

# Declaring Strings for two different paths (one for Santa, one for Robo-Santa)
santa_directions = ""
robosanta_directions = ""

# Splitting data file in two different strings with Odd directions for Santa and Even directions for Robo-Santa

for i in range(len(input)):
    current_char = input[i]
    if i % 2 == 0:
        robosanta_directions += current_char
    else:
        santa_directions += current_char

# Declaring a dictionary with the existing house with a present included, same as in part one
santa_map = {f"{x}, {y}": 1}

# Same principle of iteration as in part one, but now for two different strings of characters

for step in santa_directions:
    i += 1
    match step:
        case ">":
            x += 1
            santa_map[x, y] = i
        case "<":
            x -= 1
            santa_map[x, y] = i
        case "^":
            y -= 1
            santa_map[x, y] = i
        case "v":
            y += 1
            santa_map[x, y] = i

# Exact same steps for Robo-Santa
x = 0
y = 0
i = 0

robosanta_map = {f"{x}, {y}": 1}

for step in robosanta_directions:
    i += 1
    match step:
        case ">":
            x += 1
            robosanta_map[x, y] = i
        case "<":
            x -= 1
            robosanta_map[x, y] = i
        case "^":
            y -= 1
            robosanta_map[x, y] = i
        case "v":
            y += 1
            robosanta_map[x, y] = i

# Finding number of houses by the amount of added key/value pairs in dictionary.
# Santa and Robo-Santa visited the same houses and we need to consider that
# Also subtracting the initial house because it's not included in the initial dictionaries, we just added it
merged_houses = {}

# Iterating through keys in the first dictionary
for key in santa_map:
    merged_houses[key] = santa_map[key]

# Iterating through keys in the second dictionary
for key in robosanta_map:
    # If the key is already present in the merged dictionary, update the value
    if key in merged_houses:
        merged_houses[key] = (merged_houses[key], robosanta_map[key])
    else:
        merged_houses[key] = robosanta_map[key]

print(f"Santa and Robo-Santa together visited {len(merged_houses) - 1} houses")
