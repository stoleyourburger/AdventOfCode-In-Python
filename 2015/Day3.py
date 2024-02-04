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
