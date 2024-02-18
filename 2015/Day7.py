import re

# --- PART ONE ---


# Defining custom objects containing Key1, Key2 (elements of operation) and Value for each bitwise operation
class ObjectListAnd:
    def __init__(self, key1, key2, value):
        self.key1 = key1
        self.key2 = key2
        self.value = value


class ObjectListOr:
    def __init__(self, key1, key2, value):
        self.key1 = key1
        self.key2 = key2
        self.value = value


class ObjectListNot:
    def __init__(self, key1, value):
        self.key1 = key1
        self.value = value


class ObjectListLeftShift:
    def __init__(self, key1, number, value):
        self.key1 = key1
        self.number = number
        self.value = value


class ObjectListRightShift:
    def __init__(self, key1, number, value):
        self.key1 = key1
        self.number = number
        self.value = value


# Putting the content of the data file in the variable
with open("Day7_input.txt", "r") as f:
    input = f.readlines()

# Creating a dictionary for our future wires. All decoded wires will be put into dictionary one by one
dict = {}


# Wrapped everything in a function for a part two task
def count_values():

    # Adding wires which just have numerical values without any bitwise operations
    for line in input:
        if re.search(r"^\d", line) and "AND" not in line:
            line = line.rstrip().split(" -> ")
            if line[1] not in dict:
                dict[line[1]] = line[0]

    # Creating arrays of custom objects containing Key1, Key2 (elements of operation) and Value for each bitwise operation and putting them in 2d lists
    list_and = []

    for line in input:
        if "AND" in line:
            # Manipulating string to take apart each key and value and adding them as keys/values in custom object and appending to the 2d list
            result = line.rstrip().split(" -> ")
            wire = result[0].split(" AND ")
            temp_object = ObjectListAnd(key1=wire[0], key2=wire[1], value=result[1])
            list_and.append([temp_object.key1, temp_object.key2, temp_object.value])

    list_or = []

    for line in input:
        if "OR" in line:
            result = line.rstrip().split(" -> ")
            wire = result[0].split(" OR ")
            temp_object = ObjectListOr(key1=wire[0], key2=wire[1], value=result[1])
            list_or.append([temp_object.key1, temp_object.key2, temp_object.value])

    # Sometimes it's just one key, when the operation has only one key and a result
    list_not = []

    for line in input:
        if "NOT" in line:
            result = line.rstrip().split(" -> ")
            wire = result[0].split("NOT ")
            temp_object = ObjectListNot(key1=wire[1], value=result[1])
            list_not.append([temp_object.key1, temp_object.value])

    list_lshift = []

    for line in input:
        if "LSHIFT" in line:
            result = line.rstrip().split(" -> ")
            number = result[0].split(" ")[-1]
            wire = result[0].split(" LSHIFT ")
            temp_object = ObjectListLeftShift(
                key1=wire[0], number=number, value=result[1]
            )
            list_lshift.append(
                [temp_object.key1, temp_object.number, temp_object.value]
            )

    list_rshift = []

    for line in input:
        if "RSHIFT" in line:
            result = line.rstrip().split(" -> ")
            number = result[0].split(" ")[-1]
            wire = result[0].split(" RSHIFT ")
            temp_object = ObjectListRightShift(
                key1=wire[0], number=number, value=result[1]
            )
            list_rshift.append(
                [temp_object.key1, temp_object.number, temp_object.value]
            )

    # For next code we iterate through the code as much as we can to fill up the dict dictionary. Every time the value will be already in the dict, it will be ignored
    for i in range(100):

        # Checking each line in list_rshift. If existing dict has data for those wires with values already known, matches them and counts the RSHIFT
        for item in list_rshift:
            if item[0] in dict and item[2] not in dict:
                result = int(dict.get(item[0])) >> int(item[1])
                if item[2] not in dict:
                    dict[item[2]] = result

        # Same for list_lshift
        for item in list_lshift:
            if item[0] in dict and item[2] not in dict:
                result = int(dict.get(item[0])) << int(item[1])
                if item[2] not in dict:
                    dict[item[2]] = result

        # And so on
        for item in list_not:
            if item[0] in dict and item[1] not in dict:
                result = ~int(dict.get(item[0]))
                if item[1] not in dict:
                    dict[item[1]] = result

        for item in list_and:
            if item[0] in dict and item[1] in dict and item[2] not in dict:
                result = int(dict.get(item[0])) & int(dict.get(item[1]))
                if item[2] not in dict:
                    dict[item[2]] = result

        # Another loop for AND, but it checks if the first Key is [int]1. I decided to separate those loops for cleaner code although you can make it in one loop
        for item in list_and:
            if item[0] == "1" and item[1] in dict and item[2] not in dict:
                result = 1 & int(dict.get(item[1]))
                if item[2] not in dict:
                    dict[item[2]] = result

        for item in list_or:
            if item[0] in dict and item[1] in dict and item[2] not in dict:
                result = int(dict.get(item[0])) | int(dict.get(item[1]))
                if item[2] not in dict:
                    dict[item[2]] = result

    # With last loop assigning the result to the table key a. A bit hardcoded here, but with some string manipulation hardcode can be avoided
    for line in input:
        line = line.rstrip()
        if line.endswith(" -> a"):
            item = line.split(" -> a")
            dict["a"] = dict[item[0]]

    print(f'Result is {dict["a"]}')


count_values()

# --- PART TWO ---

# Simply clearing the dictionary, assigning a known value to the 'b' key and running the function again
dict = {}
dict["b"] = 16076

count_values()
