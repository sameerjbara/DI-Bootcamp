# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.


import random

wordslist = [
    'correction', 'childish', 'beach', 'python', 'assertive',
    'interference', 'complete', 'share', 'credit card', 'rush', 'south'
]
word = random.choice(wordslist).lower()

# Game setup
guessed_letters = set()
wrong_guesses = 0
MAX_WRONG = 6  # head, body, left arm, right arm, left leg, right leg

def build_display(secret, guessed):
    # show letters if guessed, keep spaces, hide others with '*'
    display = []
    for ch in secret:
        if ch == " ":
            display.append(" ")
        elif ch in guessed:
            display.append(ch)
        else:
            display.append("*")
    return "".join(display)

def draw_gallows(wrong):
    stages = [
        """
 +---+
 |   |
     |
     |
     |
     |
=========
""",
        """
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
        """
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
        """
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
        """
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
        """
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
        """
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
""",
    ]
    return stages[wrong]

print("Welcome to Hangman!\n")
print("The word/phrase has been chosen.")
print(draw_gallows(wrong_guesses))

while True:
    current_display = build_display(word, guessed_letters)
    print("Word:", current_display)
    print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "(none)")
    print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG}\n")

    # Win check
    if "*" not in current_display:
        print("You won! The word/phrase was:", word)
        break

    # Lose check
    if wrong_guesses >= MAX_WRONG:
        print("You lost! The word/phrase was:", word)
        break

    guess = input("Guess a letter: ").strip().lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter ONE letter (a-z) only.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.add(guess)

    # Check guess
    if guess in word:
        print("Good guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")
        print(draw_gallows(wrong_guesses))
