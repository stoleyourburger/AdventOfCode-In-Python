# --- PART ONE ---

# Putting the content of the data file in the variable
with open('Day1_input.txt', 'r') as f:
    input = f.read()

# Variable to count current floor
currentFloor = 0

# Simple iteration over each char and incrementing or decrementing the counter
for char in input:
    if char == '(':
        currentFloor += 1
    elif char == ')':
        currentFloor -= 1

# Showing the result in console
print(f'Santa gets to {currentFloor} floor')

# --- PART TWO ---

# Variables, one is to count ups & downs, another is to count a position
counter = 0
position = 0

# Based on the '(' or ')' we increment or decrement the counter. We always increment the position variable
# When the counter variable reaches -1, we check the position variable, write it in the console and break the loop
for char in input:
    if char == '(':
        counter += 1
        position += 1
    elif char == ')':
        counter -= 1
        position += 1
    if counter == -1:
        print(f'Santa enters the basement at {position} position')
        break
