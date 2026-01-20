# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:

# 18,22,24

import math

C = 50
H = 30

d_input = input("Enter comma-separated D values: ")  # e.g. 100,150,180
d_values = d_input.split(",")

results = []
for d in d_values:
    d = d.strip()
    if not d:
        continue
    D = int(d)
    Q = math.sqrt((2 * C * D) / H)
    results.append(str(round(Q)))  # rounded like the example

print(",".join(results))


# Exercise 2 : List of integers
# Instructions
# Given a list of 10 integers to analyze. For example:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]


# 1. Store the list of numbers in a variable.

# 2. Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers

# 3. A list containing the first and the last numbers.

# 4. A list of all the numbers greater than 50.

# 5. A list of all the numbers smaller than 10.

# 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.

# 7. The numbers without any duplicates – also print how many numbers are in the new list.

# 8. The average of all the numbers.

# 9. The largest number.

# 10.The smallest number.

# 11. Bonus: Find the sum, average, largest and smallest number without using built in functions.

# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.

# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.

# 14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.

# 15. Bonus: Will the code work when the number of random numbers is not equal to 10?

numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# 2a
print("List:", numbers)

# 2b
sorted_desc = sorted(numbers, reverse=True)
print("Sorted desc:", sorted_desc)

# 2c
print("Sum:", sum(numbers))

# 3
first_last = [numbers[0], numbers[-1]]
print("First & last:", first_last)

# 4
greater_50 = [x for x in numbers if x > 50]
print("> 50:", greater_50)

# 5
smaller_10 = [x for x in numbers if x < 10]
print("< 10:", smaller_10)

# 6
squared = [x * x for x in numbers]
print("Squared:", squared)

# 7
no_duplicates = list(set(numbers))
print("No duplicates:", no_duplicates)
print("Count (no duplicates):", len(no_duplicates))

# 8
avg = sum(numbers) / len(numbers)
print("Average:", avg)

# 9
print("Largest:", max(numbers))

# 10
print("Smallest:", min(numbers))


# Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

paragraph = """On 14 June 1925, in a spontaneous reaction against Primo de Rivera's dictatorship, the crowd in the stadium jeered the Royal March. 
As a reprisal, the ground was closed for six months and Gamper was forced to relinquish the presidency of the club.
This coincided with the club's transition to professional football. 
The first time the directors of Barcelona publicly claimed to operate a professional football club was in 1926."""

# Characters
char_count = len(paragraph)

# Non-whitespace characters
non_whitespace = len([ch for ch in paragraph if not ch.isspace()])

# Sentences (simple approach)
import re
sentences = [s.strip() for s in re.split(r'[.!?]+', paragraph) if s.strip()]
sentence_count = len(sentences)

# Words (simple approach)
words = re.findall(r"\b[\w']+\b", paragraph.lower())
word_count = len(words)

# Unique words
unique_words = set(words)
unique_count = len(unique_words)

# Average words per sentence
avg_words_per_sentence = word_count / sentence_count if sentence_count else 0

# Non-unique words count
non_unique_count = word_count - unique_count

print("Characters:", char_count)
print("Sentences:", sentence_count)
print("Words:", word_count)
print("Unique words:", unique_count)
print("Non-whitespace characters:", non_whitespace)
print("Avg words per sentence:", avg_words_per_sentence)
print("Non-unique words:", non_unique_count)


# Exercise 4 : Frequency Of The Words
# Instructions
# Write a program that prints the frequency of the words from the input.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1


text = input("Enter a sentence: ")

words = text.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

for word in sorted(freq.keys()):
    print(f"{word}:{freq[word]}")
