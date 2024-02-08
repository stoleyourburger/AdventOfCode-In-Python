import string
import re

# --- DAY ONE ---

# This solution takes quite a lot of time to iterate through all the possible passwords
# I might come up with something better once I get myself more skilled
# ...
# Or not.

# I divided the requirements into three functions for better readability
# Of course they all could be put into one function for more compact code


def ValidateIncrease():

    for i in range(len(password) - 2):
        # Converting the chars to integers and checking if they are equal
        if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
            return True


def ValidateLetters():

    if "i" not in password and "o" not in password and "l" not in password:
        return True
    else:
        return False


def ValidatePairs():

    pairs = set()
    i = 0

    # Creating a set and looking for equal letters in the password
    # If there are two letters in a row, we add the letter to the set and keep looking further
    # Because of 'i += 2' we exclude possible overlapping
    # Because sets don't add same item twice or more, we exclude similar pairs because both pairs should be different

    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 2
        else:
            i += 1

    # We need two pairs, so everything less than two doesn't satisfy us
    if len(pairs) < 2:
        return False
    return True


# Creating list of letters from a to z
alphabet = list(string.ascii_lowercase)

password = "cqjxjnds"


# -----
# This part is under construction. I might forget about it and never finish it.
# Now it runs just once, but it's better to put it inside loop
# Here we eliminate (replace) all possible occurencies of 'i', 'o' and 'l'
# So we don't waste time iterating over them
# This should save us some time
# First we replace the letters with the following
###password = password.replace("i", "j").replace("o", "p").replace("l", "m")
###
#### Then we look for those replaced letters
###match = re.search("[jpm].*", password)
###if match:
###
###    # If a letter was found, we find the letter position and add the amount of 'a' equal to
###    # Length of password minus the index of the letter we found and don't forget to subtract 1
###    password = password[: match.start() + 1] + "a" * (len(password) - match.start() - 1)
# -----

# Reversing the password for better convenience
reversedPassword = password[::-1]


while not ValidateIncrease() or not ValidateLetters() or not ValidatePairs():

    # Reverse iterating over the password so we can easily perform the wrapping 'z' to 'a'
    # The password now is backwards, but it's more comfortably to loop over it.
    for index, letter in enumerate(reversedPassword):

        # Checking for letter to be 'z' for wrapping
        if letter == alphabet[-1]:
            letter = "a"

            # Finding next letter in password
            nextLetter = reversedPassword[index + 1]

            if nextLetter in alphabet and nextLetter != alphabet[-1]:

                # Matching a nextLetter index with the same letter from alphabet
                nextLetterIndex = alphabet.index(nextLetter)

                # Modulo 26 for circular indexing
                nextLetter = alphabet[(nextLetterIndex + 1) % 26]

                # Constructing a password, slicing everything around the index letter and the next letter
                reversedPassword = (
                    reversedPassword[:index]
                    + letter
                    + nextLetter
                    + reversedPassword[index + 2 :]
                )
                password = reversedPassword[::-1]
                break

            # If the next letter is 'z', we skip it, since on the next iteration we will catch it with the 'if' above
            elif nextLetter in alphabet and nextLetter == alphabet[-1]:
                reversedPassword = (
                    reversedPassword[:index]
                    + letter
                    + nextLetter
                    + reversedPassword[index + 2 :]
                )
                password = reversedPassword[::-1]
                continue

        else:
            # Just assigning next index to the letter
            letterIndex = alphabet.index(letter)
            newLetter = alphabet[(letterIndex + 1)]

            reversedPassword = (
                reversedPassword[:index] + newLetter + reversedPassword[index + 1 :]
            )
            password = reversedPassword[::-1]
            break

    # Printing a password
    # Printing will show all the passwords and will stop on the correct password
    print(password)

# Correct answer: cqjxxyzz
