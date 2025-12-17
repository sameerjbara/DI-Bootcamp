# Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {3, 7, 21}
my_fav_numbers.add(9)
my_fav_numbers.add(11)

my_fav_numbers.remove(11)  # “last added” (we remove 11 manually)

friend_fav_numbers = {2, 7, 50}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(my_fav_numbers)
print(friend_fav_numbers)
print(our_fav_numbers)


# Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)


# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

t = (1, 2, 3)
t = t + (4, 5) 
print(t)


# Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear


# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

print(basket.count("Apples"))

basket.clear()
print(basket)


# Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

seq = [x / 2 for x in range(3, 11)] 
print(seq)  


# Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for n in range(1, 21):
    print(n)

for i, n in enumerate(range(1, 21)):
    if i % 2 == 0:
        print(n)


# Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
# Example:

name = input("Enter your name: ").strip()
while True:
    if (not name.isdigit()) and len(name) >= 3:
        print("thank you")
        break
    else:
        name = input("give the correct name: ").strip()




# Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

fav = input("Enter favorite fruits (space-separated): ").split()
fruit = input("Enter a fruit name: ").strip()

if fruit in fav:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


# Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []

while True:
    t = input("Topping (type 'quit' to stop): ").strip()
    if t.lower() == "quit":
        break
    toppings.append(t)
    print(f"Adding {t} to your pizza.")

total = 10 + 2.5 * len(toppings)
print("Toppings:", toppings)
print("Total cost:", total)


# Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

ages = input("Enter ages (space-separated): ").split()
total = 0

for a in ages:
    age = int(a)
    if age < 3:
        total += 0
    elif age <= 12:
        total += 10
    else:
        total += 15

print("Total cost:", total)


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

names = input("Enter names (space-separated): ").split()
allowed = []

for name in names:
    age = int(input(f"Age of {name}: "))
    if 16 <= age <= 21:
        allowed.append(name)

print("Allowed attendees:", allowed)
