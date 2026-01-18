# Instructions
# Create a Python program that will generate a good password for you.

# Program flow:

# Ask the user to type in the number of characters that the password should have (password length) – between 6 and 30 characters.
# Validate the input. Make sure the user is inputing a number between 6 to 30. Create a loop which will continue to ask the user for an input until they enter a valid one.

# Generate a password with the required length.

# Print the password with a user-friendly message which reminds the user to keep the password in a safe place!

# Rules for the validity of the password

# Each password should contain:
# At least 1 digit (0-9)
# At least 1 lower-case character (a-z)
# At least 1 upper-case character (A-Z)
# At least 1 special character (eg. !, @, #, $, %, ^, _, …)
# Once there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.

# Create a test function first!

# Do the following steps 100 times, with different password lengths:
# Generate a password.
# Test the password to ensure that:
# it fulfills all the requirements above (eg. it has at least one digit, etc.)
# it has the specified length.

import random
import string


SPECIALS = "!@#$%^_&*()-+=[]{}:;,.?/|~"


def is_valid_password(pw, length):
    if len(pw) != length:
        return False
    has_digit = any(ch.isdigit() for ch in pw)
    has_lower = any(ch.islower() for ch in pw)
    has_upper = any(ch.isupper() for ch in pw)
    has_special = any(ch in SPECIALS for ch in pw)
    return has_digit and has_lower and has_upper and has_special


def generate_password(length):
    if length < 6 or length > 30:
        raise ValueError("length must be between 6 and 30")

    # guarantee at least 1 from each category
    pw_chars = [
        random.choice(string.digits),
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(SPECIALS),
    ]

    all_choices = string.digits + string.ascii_lowercase + string.ascii_uppercase + SPECIALS
    while len(pw_chars) < length:
        pw_chars.append(random.choice(all_choices))

    random.shuffle(pw_chars)
    return "".join(pw_chars)


def ask_length():
    while True:
        raw = input("Password length (6-30): ").strip()
        if raw.isdigit():
            length = int(raw)
            if 6 <= length <= 30:
                return length
        print("Invalid input. Enter a number between 6 and 30.")


def test_password_generator():
    for _ in range(100):
        length = random.randint(6, 30)
        pw = generate_password(length)
        if not is_valid_password(pw, length):
            raise AssertionError(f"Test failed. length={length}, pw={pw}")
    print("All 100 tests passed.")


if __name__ == "__main__":
    test_password_generator()

    length = ask_length()
    pw = generate_password(length)
    print("Your password:", pw)
    print("Keep it in a safe place.")

