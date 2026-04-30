import random

wordslist = [
    'correction', 'childish', 'beach', 'python',
    'assertive', 'interference', 'complete',
    'share', 'credit card', 'rush', 'south'
]

word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###

hidden_word = ""

for char in word:
    if char == " ":
        hidden_word += " "
    else:
        hidden_word += "*"

wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

body_parts = [
    "head",
    "body",
    "left arm",
    "right arm",
    "left leg",
    "right leg"
]

print("Welcome to Hangman!")
print("Guess the word:")
print(hidden_word)

while wrong_guesses < max_wrong_guesses and hidden_word != word:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")

        new_hidden_word = ""

        for i in range(len(word)):
            if word[i] == guess:
                new_hidden_word += guess
            else:
                new_hidden_word += hidden_word[i]

        hidden_word = new_hidden_word

    else:
        print("Wrong guess!")
        print("Added body part:", body_parts[wrong_guesses])
        wrong_guesses += 1

    print("Word:", hidden_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
    print("Guessed letters:", guessed_letters)
    print()

if hidden_word == word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over!")
    print("The word was:", word)