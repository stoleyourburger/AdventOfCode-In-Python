# --- PART ONE ---

# Importing hashlib library
import hashlib

# Iterating over multiple numbers
for n in range(0, 1000000):

    # For each iteration adding a new number for our known secret key
    key = "bgvyzdsv" + str(n)
    result = hashlib.md5(key.encode())

    # Matching if the result starts with a required number of zeroes and printing the result
    if result.hexdigest().startswith("00000"):
        print(result.hexdigest())
        print(key)
