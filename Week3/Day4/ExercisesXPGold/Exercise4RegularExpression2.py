# Instructions
# Hint: Use the RegEx (module)

# Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
# The name should contain only letters.
# The name should contain only one space.
# The first letter of each name should be upper cased.


import re

def is_valid_full_name(full_name):
    pattern = r"^[A-Z][a-zA-Z]* [A-Z][a-zA-Z]*$"
    return re.match(pattern, full_name) is not None


name = input("Enter your full name (Example: John Doe): ").strip()
if is_valid_full_name(name):
    print("Valid name.")
else:
    print("Invalid name. Rules: only letters, one space, each name starts with uppercase.")
