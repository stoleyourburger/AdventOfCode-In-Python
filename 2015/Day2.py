# --- PART ONE ---

totalWrap = 0

# Putting the content of the data file in the variable
with open('Day2_input.txt', 'r') as f:
    for line in f:

        # Declaring the array
        array = []
        # Splitting the dimensions of the box in each line and removing the whitespace with rstrip() 
        array += line.rstrip().split('x')

        # Getting length, width and height from the array and assigning to the variables
        length = int(array[0])
        width = int(array[1])
        height = int(array[2])

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
    
print(f'You need {totalWrap} sq feet of wrapping paper')