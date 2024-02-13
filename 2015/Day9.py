# --- PART ONE ---


# Defining class Route containing first city, second city and distance
class Route:
    def __init__(self, cityOne, cityTwo, distance):
        self.cityOne = cityOne
        self.cityTwo = cityTwo
        self.distance = distance


# Putting the content of the data file in the variable
with open("Day9_input.txt", "r") as f:
    input = f.readlines()

# Putting all routes in a 2d list of routes
routes = []

for line in input:
    line = line.rstrip()
    newLine = [line.split(" to ") for line in line.split(" = ")]
    tempRoute = Route(
        cityOne=newLine[0][0], cityTwo=newLine[0][1], distance=newLine[1][0]
    )
    routes.append([tempRoute.cityOne, tempRoute.cityTwo, tempRoute.distance])

# Putting all cities in one list
citiesList = []


for route in routes:
    if route[0] not in citiesList:
        citiesList.append(route[0])
    if route[1] not in citiesList:
        citiesList.append(route[1])

# Now we need to generate all possible paths


# Recursive function to generate all possible paths
def GetPaths(startCity, remainingCities, currentPath, currentDistance):

    # If clause to stop the function when there are no more remaining cities
    if not remainingCities:

        # Adding in order to change the value of a global variable inside a function
        global paths

        # Once there are no more remaining cities, the path and distance is added to the paths list.
        paths.append([currentPath, currentDistance])

    else:
        for city in remainingCities:

            # Variable for all the cities other than city
            newRemainingCities = [
                other_city for other_city in remainingCities if other_city != city
            ]

            # Creating a $newpath for the next Get-Paths $currentPath parameter
            newPath = currentPath + " -> " + city

            # New Distance is a 0 (initially) plus Distance of two cities: one is an iterated $city and the other is $startCity which itself is an iterated city in a "Generate all paths" foreach loop
            # After it is counted, the next Get-Paths uses a new $currentDistance which already has some distance
            for route in routes:
                if (route[0] == startCity and route[1] == city) or (
                    route[0] == city and route[1] == startCity
                ):
                    newDistance = currentDistance + int(route[2])

            # And the next Get-Paths runs until there are no more cities left
            GetPaths(city, newRemainingCities, newPath, newDistance)


# Initialize variable paths where all the calculated paths and distances will be stored in
paths = []

# Generating all paths
# Using slicing to create remainingCities without the need for explicit copying and removal
# This excludes the current city by taking all elements before and after it
for i, city in enumerate(citiesList):
    remainingCities = citiesList[:i] + citiesList[i + 1 :]

    # Mind that the function GetPaths is recursive, meaning that it will run exponentially as many times as many cities you have. Basically bruteforcing the data
    GetPaths(city, remainingCities, city, 0)

print(min(paths, key=lambda x: x[1]))

# --- PART TWO ---

# Finding the longest path now. Same data, same calculations which we already done, just outputting the max value
print(max(paths, key=lambda x: x[1]))
