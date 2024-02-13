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
reindeer_ranges = {}

# Defining variables for time, range and rest of the parameters
for line in input:
    line = line.split()

    finish_time = 2503
    time = 0
    range = 0

    speed = int(line[3])
    fly_time = int(line[6])
    rest_time = int(line[-2])

    one_fly_session = speed * fly_time
    iteration_time = fly_time + rest_time

    # After each fly each session time will be added to total time. Range will be counted too
    # If time already spend + time for one more iteration will be more than possible finish time, while loop will stop.
    # After that there are still reindeers which have some remaining fly time
    while (time + iteration_time) < finish_time:
        range += one_fly_session
        time += fly_time
        time += rest_time

    # Here we count the remaining part of the time.
    # Some reindeers still yet have some fly time, and we make sure they don't overfly the remaining seconds.
    # Pretty self-explanatory loop
    remaining_time = finish_time - time
    speed_counter = 0
    while speed_counter < remaining_time and speed_counter < fly_time:
        speed_counter += 1
        range += speed

    # Adding to the result table
    reindeer_ranges[line[0]] = range

# Printing the max result
print(f"The maximum range is {max(reindeer_ranges.values())}")
