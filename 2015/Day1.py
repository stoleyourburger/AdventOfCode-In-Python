# --- DAY ONE ---

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

