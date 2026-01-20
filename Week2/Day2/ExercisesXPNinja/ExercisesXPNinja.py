# Exercise 1 : What’s your name ?
# Instructions
# Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
# For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
# But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.

def get_full_name(first_name, last_name, middle_name=None):
    first = first_name.capitalize()
    last = last_name.capitalize()

    if middle_name:
        middle = middle_name.capitalize()
        return f"{first} {middle} {last}"
    else:
        return f"{first} {last}"



# Exercise 2 : From English to Morse
# Instructions
# Write a function that converts English text to morse code and another one that does the opposite.
# Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.

MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

def english_to_morse(text):
    result = []
    for word in text.upper().split():
        letters = [MORSE_CODE[char] for char in word if char in MORSE_CODE]
        result.append(" ".join(letters))
    return " / ".join(result)

def morse_to_english(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE.items()}
    words = morse.split(" / ")
    result = []

    for word in words:
        letters = [reverse_dict[code] for code in word.split()]
        result.append("".join(letters))

    return " ".join(result)


# Exercise 3 : Box of stars
# Instructions
# Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
# For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:

# ******************
# * Hello          *
# * World          *
# * in             *
# * reallylongword *
# * a              *
# * frame          *
# ******************


def box_printer(*words):
    max_length = max(len(word) for word in words)
    border = "*" * (max_length + 4)

    print(border)
    for word in words:
        print(f"* {word.ljust(max_length)} *")
    print(border)


# Exercise 4 : What is the purpose of this code?
# Analyse this code before executing it. What is the purpose of this code?

# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index]
#      position = index

#      while position>0 and alist[position-1]>currentvalue:
#          alist[position]=alist[position-1]
#          position = position-1

#      alist[position]=currentvalue

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)


# This code sorts a list of numbers in ascending order using the Insertion Sort algorithm.