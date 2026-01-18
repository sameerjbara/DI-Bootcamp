# Instructions:

# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.



# Key Python Topics:

# string module
# random module
# String concatenation


# Step 1: Import the string and random modules

# Import the string and random modules.


# Step 2: Create a string of all letters

# Read about the strings methods HERE to find the best methods for this step



# Step 3: Generate a random string

# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.


import string
import random

def random_string_5():
    letters = string.ascii_letters  # uppercase + lowercase
    result = ""
    for _ in range(5):
        result += random.choice(letters)
    return result

print(random_string_5())
