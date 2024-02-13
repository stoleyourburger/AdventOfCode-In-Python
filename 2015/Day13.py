import itertools

# --- PART ONE ---

input = list(open("Day13_input.txt"))

# Getting names, putting them in a list
names = []

for line in input:
    line = line.split()
    if line[0] not in names:
        names.append(line[0])

happiness = {}

# We find all possible combinations of names and their happiness value with already minus sign added if needed based on 'lose' in the line
for line in input:
    words = line[:-2].split(" ")
    happiness_value = int(words[3])
    if words[2] == "lose":
        happiness_value *= -1
    happiness[(words[0], words[-1])] = happiness_value

perms = itertools.permutations(names)

result = 0

# We iterate on all the possible combinations of names and for every combination adding (or subtracting with the '-' sign there) happiness
# We have done this (or similar) before therefore I don't put much comments
for perm in perms:
    happy_value = 0
    for i in range(len(perm) - 1):
        happy_value += (
            happiness[(perm[i], perm[i + 1])] + happiness[(perm[i + 1], perm[i])]
        )
    happy_value += happiness[(perm[-1], perm[0])] + happiness[(perm[0], perm[-1])]
    if happy_value > result:
        result = happy_value

# And printing the biggest result possible
print(result)
