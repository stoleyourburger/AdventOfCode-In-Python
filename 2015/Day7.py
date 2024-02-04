import re

# --- PART ONE ---


# Defining custom objects containing Key1, Key2 (elements of operation) and Value for each bitwise operation
class objectListAnd:
    def __init__(self, key1, key2, value):
        self.key1 = key1
        self.key2 = key2
        self.value = value


class objectListOr:
    def __init__(self, key1, key2, value):
        self.key1 = key1
        self.key2 = key2
        self.value = value


class objectListNot:
    def __init__(self, key1, value):
        self.key1 = key1
        self.value = value


class objectListLeftShift:
    def __init__(self, key1, number, value):
        self.key1 = key1
        self.number = number
        self.value = value


class objectListRightShift:
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
def countValues():

    # Adding wires which just have numerical values without any bitwise operations
    for line in input:
        if re.search(r"^\d", line) and "AND" not in line:
            line = line.rstrip().split(" -> ")
            if line[1] not in dict:
                dict[line[1]] = line[0]

    # Creating arrays of custom objects containing Key1, Key2 (elements of operation) and Value for each bitwise operation and putting them in 2d lists
    listAnd = []

    for line in input:
        if "AND" in line:
            # Manipulating string to take apart each key and value and adding them as keys/values in custom object and appending to the 2d list
            result = line.rstrip().split(" -> ")
            wire = result[0].split(" AND ")
            tempObject = objectListAnd(key1=wire[0], key2=wire[1], value=result[1])
            listAnd.append([tempObject.key1, tempObject.key2, tempObject.value])

    listOr = []

    for line in input:
        if "OR" in line:
            result = line.rstrip().split(" -> ")
            wire = result[0].split(" OR ")
            tempObject = objectListOr(key1=wire[0], key2=wire[1], value=result[1])
            listOr.append([tempObject.key1, tempObject.key2, tempObject.value])

    # Sometimes it's just one key, when the operation has only one key and a result
    listNot = []

    for line in input:
        if "NOT" in line:
            result = line.rstrip().split(" -> ")
            wire = result[0].split("NOT ")
            tempObject = objectListNot(key1=wire[1], value=result[1])
            listNot.append([tempObject.key1, tempObject.value])

    listLShift = []

    for line in input:
        if "LSHIFT" in line:
            result = line.rstrip().split(" -> ")
            number = result[0].split(" ")[-1]
            wire = result[0].split(" LSHIFT ")
            tempObject = objectListLeftShift(
                key1=wire[0], number=number, value=result[1]
            )
            listLShift.append([tempObject.key1, tempObject.number, tempObject.value])

    listRShift = []

    for line in input:
        if "RSHIFT" in line:
            result = line.rstrip().split(" -> ")
            number = result[0].split(" ")[-1]
            wire = result[0].split(" RSHIFT ")
            tempObject = objectListRightShift(
                key1=wire[0], number=number, value=result[1]
            )
            listRShift.append([tempObject.key1, tempObject.number, tempObject.value])

    # For next code we iterate through the code as much as we can to fill up the dict dictionary. Every time the value will be already in the dict, it will be ignored
    for i in range(100):

        # Checking each line in listRShift. If existing dict has data for those wires with values already known, matches them and counts the RSHIFT
        for item in listRShift:
            if item[0] in dict and item[2] not in dict:
                result = int(dict.get(item[0])) >> int(item[1])
                if item[2] not in dict:
                    dict[item[2]] = result

        # Same for listLShift
        for item in listLShift:
            if item[0] in dict and item[2] not in dict:
                result = int(dict.get(item[0])) << int(item[1])
                if item[2] not in dict:
                    dict[item[2]] = result

        # And so on
        for item in listNot:
            if item[0] in dict and item[1] not in dict:
                result = ~int(dict.get(item[0]))
                if item[1] not in dict:
                    dict[item[1]] = result

        for item in listAnd:
            if item[0] in dict and item[1] in dict and item[2] not in dict:
                result = int(dict.get(item[0])) & int(dict.get(item[1]))
                if item[2] not in dict:
                    dict[item[2]] = result

        # Another loop for AND, but it checks if the first Key is [int]1. I decided to separate those loops for cleaner code although you can make it in one loop
        for item in listAnd:
            if item[0] == "1" and item[1] in dict and item[2] not in dict:
                result = 1 & int(dict.get(item[1]))
                if item[2] not in dict:
                    dict[item[2]] = result

        for item in listOr:
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


countValues()

# --- PART TWO ---

# Simply clearing the dictionary, assigning a known value to the 'b' key and running the function again
dict = {}
dict["b"] = 16076

countValues()
