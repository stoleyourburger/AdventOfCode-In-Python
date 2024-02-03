# --- PART ONE ---

totalWrap = 0

# Putting the content of the data file in the variable
with open("Day2_input.txt", "r") as f:
    for line in f:

        # Declaring the list
        list = []
        # Splitting the dimensions of the box in each line and removing the whitespace with rstrip()
        list += line.rstrip().split("x")

        # Getting length, width and height from the list and assigning to the variables
        length = int(list[0])
        width = int(list[1])
        height = int(list[2])

        # Calculating one of each sides of the box (Don't forget that there are two of each sides!)
        sideA = length * width
        sideB = width * height
        sideC = height * length

        # Choosing the smallest side of the box (We will need to add it later to the box surface area)
        smallestSide = min(sideA, sideB, sideC)

        # Calculating the surface area by multiplying by two each of the sides + adding that smallest side of the box
        surfaceArea = 2 * sideA + 2 * sideB + 2 * sideC + smallestSide

        # Adding this box area to total Paper
        totalWrap += surfaceArea

print(f"You need {totalWrap} sq feet of wrapping paper")

# --- PART TWO ---

totalRibbon = 0

# Again we need to iterate over each of the boxes
with open("Day2_input.txt", "r") as f:
    for line in f:

        # Declaring the list, splitting the dimensions of the box in each line and converting all strings in list to integers
        list = []
        list = [eval(i) for i in (line.rstrip().split("x"))]

        # Sorting the list for values to be from smallest to largest
        list = sorted(list)

        # Getting length, width and height from the list and assigning to the variables
        length = int(list[0])
        width = int(list[1])
        height = int(list[2])

        # Calculating the ribbon for each present
        singleRibbon = (
            int(list[0])
            + int(list[0])
            + int(list[1])
            + int(list[1])
            + length * width * height
        )

        totalRibbon += singleRibbon

print(f"You need {totalRibbon} feet of ribbon")
