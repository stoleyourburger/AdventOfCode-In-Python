# --- PART ONE ---

# Putting the content of the data file in the variable
with open("Day6_input.txt", "r") as f:
    input = f.readlines()


# Define the dimensions of the 2D list
rows, columns = 1000, 1000

# Creating the 2D list of values filled with boolean False
grid = [[False for _ in range(columns)] for _ in range(rows)]

# Here we parse each line in the data file and manipulate the string to get out the coordinates
# It's one big [messy] loop :)

for line in input:
    line = line.rstrip()

    # First we check the line if it matches the beginning with 'turn on' text
    if "turn on" in line:

        # We also split the string at ' through ' so we can have one variable containing all the coordinates
        coordinates = line.strip("turn on ").split(" through ")

        # Now we have a variable list with all the coordinates. First coordinate pair is in the first list element
        # And the second pair is in the second list element
        # We split the coordinate pairs into two different variables which are also lists and contain coordinate pairs
        x = coordinates[0].split(",")
        y = coordinates[1].split(",")

        # Then we use the coordinates in a for loop to go through the coordinates in the grid and flip the boolean accordingly
        for i in range(int(x[0]), int(y[0]) + 1):
            for j in range(int(x[1]), int(y[1]) + 1):
                grid[i][j] = True

    # Same goes for the 'turn off' and 'toggle' matches
    elif "turn off" in line:

        coordinates = line.strip("turn off ").split(" through ")

        x = coordinates[0].split(",")
        y = coordinates[1].split(",")

        for i in range(int(x[0]), int(y[0]) + 1):
            for j in range(int(x[1]), int(y[1]) + 1):
                grid[i][j] = False

    elif "toggle" in line:

        coordinates = line.strip("toggle ").split(" through ")

        x = coordinates[0].split(",")
        y = coordinates[1].split(",")

        # This checks the value of the position in the grid and flips it to the opposite value
        for i in range(int(x[0]), int(y[0]) + 1):
            for j in range(int(x[1]), int(y[1]) + 1):
                grid[i][j] = not grid[i][j]

# Counting the number of True booleans in the list
print(sum(row.count(True) for row in grid))

# --- PART TWO ---

# Now we can't use the grid with boolean values as we need to increment the value of lights.
# But the general idea is the same, we just add or subtract the value according to the beginning of the string

# Define the dimensions of the 2D list
rows, columns = 1000, 1000

# Creating the 2D list of values filled with zeros
grid = [[0 for _ in range(columns)] for _ in range(rows)]

# Here we parse each line in the data file and manipulate the string to get out the coordinates
# It's one big [messy] loop :)

for line in input:
    line = line.rstrip()

    # First we check the line if it matches the beginning with 'turn on' text
    if "turn on" in line:

        # We also split the string at ' through ' so we can have one variable containing all the coordinates
        coordinates = line.strip("turn on ").split(" through ")

        # Now we have a variable list with all the coordinates. First coordinate pair is in the first list element
        # And the second pair is in the second list element
        # We split the coordinate pairs into two different variables which are also lists and contain coordinate pairs
        x = coordinates[0].split(",")
        y = coordinates[1].split(",")

        # Then we use the coordinates in a for loop to go through the coordinates in the grid and incrementing the value
        for i in range(int(x[0]), int(y[0]) + 1):
            for j in range(int(x[1]), int(y[1]) + 1):
                grid[i][j] += 1

    # Same goes for the 'turn off' and 'toggle' matches, decrementing for 'turn off':
    elif "turn off" in line:

        coordinates = line.strip("turn off ").split(" through ")

        x = coordinates[0].split(",")
        y = coordinates[1].split(",")

        for i in range(int(x[0]), int(y[0]) + 1):
            for j in range(int(x[1]), int(y[1]) + 1):
                # Here we make sure that light brightness can't be less than 0
                if grid[i][j] > 0:
                    grid[i][j] -= 1
                else:
                    grid[i][j] = 0

    # ... And twice incrementing for 'toggle'
    elif "toggle" in line:

        coordinates = line.strip("toggle ").split(" through ")

        x = coordinates[0].split(",")
        y = coordinates[1].split(",")

        # This checks the value of the position in the grid and adds two
        for i in range(int(x[0]), int(y[0]) + 1):
            for j in range(int(x[1]), int(y[1]) + 1):
                grid[i][j] += 2

# Counting the number of light increments in the list
print(sum(i for row in grid for i in row if isinstance(i, int)))
