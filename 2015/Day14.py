# --- PART ONE ---

with open("Day14_input.txt", "r") as f:
    input = f.readlines()

reindeers = []

# Populate reindeer list
# Making this a separate loop for better visibility
for line in input:
    line = line.split()
    reindeers.append(line[0])

# Dictionary of results
reindeer_distances = {}

# Defining variables for time, distance and rest of the parameters
for line in input:
    line = line.split()

    finish_time = 2503
    time = 0
    distance = 0

    speed = int(line[3])
    fly_time = int(line[6])
    rest_time = int(line[-2])

    one_fly_session = speed * fly_time
    iteration_time = fly_time + rest_time

    # After each fly each session time will be added to total time. distance will be counted too
    # If time already spend + time for one more iteration will be more than possible finish time, while loop will stop.
    # After that there are still reindeers which have some remaining fly time
    while (time + iteration_time) < finish_time:
        distance += one_fly_session
        time += fly_time
        time += rest_time

    # Here we count the remaining part of the time.
    # Some reindeers still yet have some fly time, and we make sure they don't overfly the remaining seconds.
    # Pretty self-explanatory loop
    remaining_time = finish_time - time
    speed_counter = 0
    while speed_counter < remaining_time and speed_counter < fly_time:
        speed_counter += 1
        distance += speed

    # Adding to the result table
    reindeer_distances[line[0]] = distance

# Printing the max result
print(f"The maximum distance is {max(reindeer_distances.values())}")

# --- PART TWO ---

# I'm more proud of this part two solution because it is less messy and better structured.
# It took me more time to solve, though.


# Defining a class so we can construct reindeers easily
class Reindeer:
    def __init__(
        self, name, speed, fly_time, rest_time, is_moving, total_distance, points
    ):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.is_moving = is_moving
        self.total_distance = total_distance
        self.points = points


reindeers = []

# Filling up a list of reindeers
for line in input:
    line = line.split()
    temp_reindeer = Reindeer(line[0], line[3], line[6], line[-2], True, 0, 0)

    # We take name, speed, number of seconds they burst, number of seconds they rest
    # Also include a boolean for the state (moving or not), total distance and points counter
    reindeers.append(
        [
            temp_reindeer.name,  # [0]
            int(temp_reindeer.speed),  # [1]
            int(temp_reindeer.fly_time),  # [2]
            int(temp_reindeer.rest_time),  # [3]
            bool(temp_reindeer.is_moving),  # [4]
            int(temp_reindeer.total_distance),  # [5]
            int(temp_reindeer.points),  # [6]
        ]
    )

total_seconds = 2503
current_second = 1

# In this loop we fill out the sublist of booleans in each reindeer list
# We iterate over the total number of seconds with the step of combined fly and rest time
# Then we fill the 'fly seconds' as True, leaving the 'rest seconds' as False
# This way we make sure that during rest, the reindeer doesn't move
for reindeer in reindeers:
    steps = [False] * (total_seconds + 1)
    for i in range(1, len(steps), reindeer[2] + reindeer[3]):
        steps[i : i + reindeer[2]] = [True] * reindeer[2]
        reindeer[4] = steps

while current_second <= total_seconds:

    for reindeer in reindeers:
        # We check whether the boolean value related to current second is True or False
        moving = reindeer[4][current_second]
        if moving:
            # Adding the speed for that second to the total distance
            distance = reindeer[1] + reindeer[5]
            reindeer[5] = distance

    # Finding a reindeer with top current distance
    # That's a simple manipulation to check for the biggest value amongst all the reindeers' distances
    best_distance = 0
    best_index = None
    for index, reindeer in enumerate(reindeers):
        if reindeer[5] >= best_distance:
            best_distance = reindeer[5]
            best_index = index

    # In case we have multiple reindeers tied for the lead, each gets a point
    for reindeer in reindeers:
        if reindeer[5] == reindeers[best_index][5]:
            reindeer[6] += 1

    current_second += 1

# And finally the output
points = 0
best_index = 0
for index, reindeer in enumerate(reindeers):
    if reindeer[6] >= points:
        points = reindeer[6]
        best_index = index

for reindeer in reindeers:
    if reindeer[6] == reindeers[best_index][6]:
        print(f"{reindeer[6]} points has the winning reindeer {reindeer[0]}")
