# Instructions:

# Create a func.py file with a function that sums two numbers and prints the result. Then, import and call the function from exercise_one.py.



# Key Python Topics:

# Modules (creating and importing)
# Functions


# Step 1: Create func.py

# Create a file named func.py.
# Define a function inside that file that takes two numbers as arguments, sums them, and prints the result.


# Step 2: Create exercise_one.py

# Create a file named exercise_one.py.
# Import the function from func.py using one of the import syntaxes provided in the instructions.
# Call the imported function with two numbers.


from func import add_and_print


def add_and_print(a, b):
    print(a + b)



add_and_print(10, 20)
