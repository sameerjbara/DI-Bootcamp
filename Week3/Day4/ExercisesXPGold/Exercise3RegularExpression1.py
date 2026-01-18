# Instructions
# Hint: Use the RegEx (module)

# Use the regular expression module to extract numbers from a string.

# Example

# return_numbers('k5k3q2g5z6x9bn') 
# // Excepted output : 532569


import re

def return_numbers(s):
    digits = re.findall(r"\d", s)
    return "".join(digits)

print(return_numbers("k5k3q2g5z6x9bn"))  # 532569
