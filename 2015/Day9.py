# --- PART ONE ---


# Defining class Route containing first city, second city and distance
class Route:
    def __init__(self, city_one, city_two, distance):
        self.city_one = city_one
        self.city_two = city_two
        self.distance = distance


# Putting the content of the data file in the variable
with open("Day9_input.txt", "r") as f:
    input = f.readlines()

# Putting all routes in a 2d list of routes
routes = []

for line in input:
    line = line.rstrip()
    new_line = [line.split(" to ") for line in line.split(" = ")]
    temp_route = Route(
        city_one=new_line[0][0], city_two=new_line[0][1], distance=new_line[1][0]
    )
    routes.append([temp_route.city_one, temp_route.city_two, temp_route.distance])

# Putting all cities in one list
cities_list = []


for route in routes:
    if route[0] not in cities_list:
        cities_list.append(route[0])
    if route[1] not in cities_list:
        cities_list.append(route[1])

# Now we need to generate all possible paths


# Recursive function to generate all possible paths
def get_paths(start_city, remaining_cities, current_path, current_distance):

    # If clause to stop the function when there are no more remaining cities
    if not remaining_cities:

        # Adding in order to change the value of a global variable inside a function
        global paths

        # Once there are no more remaining cities, the path and distance is added to the paths list.
        paths.append([current_path, current_distance])

    else:
        for city in remaining_cities:

            # Variable for all the cities other than city
            newremaining_cities = [
                other_city for other_city in remaining_cities if other_city != city
            ]

            # Creating a new_path for the next get_paths current_path parameter
            new_path = current_path + " -> " + city

            # New Distance is a 0 (initially) plus distance of two cities: one is an iterated city and the other is start_city which itself is an iterated city in a "Generate all paths" foreach loop
            # After it is counted, the next get_paths uses a new current_distance which already has some distance
            for route in routes:
                if (route[0] == start_city and route[1] == city) or (
                    route[0] == city and route[1] == start_city
                ):
                    new_distance = current_distance + int(route[2])

            # And the next get_paths runs until there are no more cities left
            get_paths(city, newremaining_cities, new_path, new_distance)


# Initialize variable paths where all the calculated paths and distances will be stored in
paths = []

# Generating all paths
# Using slicing to create remaining_cities without the need for explicit copying and removal
# This excludes the current city by taking all elements before and after it
for i, city in enumerate(cities_list):
    remaining_cities = cities_list[:i] + cities_list[i + 1 :]

    # Mind that the function get_paths is recursive, meaning that it will run exponentially as many times as many cities you have. Basically bruteforcing the data
    get_paths(city, remaining_cities, city, 0)

print(min(paths, key=lambda x: x[1]))

# --- PART TWO ---

# Finding the longest path now. Same data, same calculations which we already done, just outputting the max value
print(max(paths, key=lambda x: x[1]))
