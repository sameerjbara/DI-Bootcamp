# Exercise 1: Birthday Look-up
# Instructions
# Create a variable called birthdays. Its value should be a dictionary.
# Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip : Use the format “YYYY/MM/DD”.
# Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”“
# Ask the user to give you a person’s name and store the answer in a variable.
# Get the birthday of the name provided by the user.
# Print out the birthday with a nicely-formatted message.

birthdays = {
    "Alice": "1995/06/15",
    "Bob": "1992/11/03",
    "Charlie": "1998/01/22",
    "Dana": "2000/09/10",
    "Eli": "1997/12/05"
}

print("Welcome!")
print("You can look up the birthdays of the people in the list!")

name = input("Enter a person's name: ")

birthday = birthdays[name]
print(f"{name}'s birthday is {birthday}")


# Exercise 2: Birthdays Advanced
# Instructions
# Before asking the user to input a person’s name print out all of the names in the dictionary.
# If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

birthdays = {
    "Alice": "1995/06/15",
    "Bob": "1992/11/03",
    "Charlie": "1998/01/22",
    "Dana": "2000/09/10",
    "Eli": "1997/12/05"
}

print("You can look up the birthdays of these people:")
for name in birthdays:
    print(name)

user_name = input("\nEnter a person's name: ")

if user_name in birthdays:
    print(f"{user_name}'s birthday is {birthdays[user_name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {user_name}")


# Exercise 3: Add Your Own Birthday
# Instructions
# Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
# Ask the user for a person’s name – store it in a variable.
# Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
# Now add this new data into your dictionary.
# Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is found and displayed.

birthdays = {
    "Alice": "1995/06/15",
    "Bob": "1992/11/03",
    "Charlie": "1998/01/22",
    "Dana": "2000/09/10",
    "Eli": "1997/12/05"
}

# Add a new birthday
new_name = input("Enter a name to add: ")
new_birthday = input("Enter the birthday (YYYY/MM/DD): ")

birthdays[new_name] = new_birthday

print("\nUpdated birthday list:")
for name in birthdays:
    print(name)

# Look up a birthday
lookup_name = input("\nEnter a name to look up: ")

if lookup_name in birthdays:
    print(f"{lookup_name}'s birthday is {birthdays[lookup_name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {lookup_name}")


# Exercise 4: Fruit Shop
# Instructions
# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
# Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
# items = {
#     "banana": {"price": 4 , "stock":10},
#     "apple": {"price": 2, "stock":5},
#     "orange": {"price": 1.5 , "stock":24},
#     "pear": {"price": 3 , "stock":1}
# }

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for item, price in items.items():
    print(f"The price of a {item} is {price}")


items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0

for item, data in items.items():
    item_total = data["price"] * data["stock"]
    total_cost += item_total

print(f"Total cost to buy everything in stock: {total_cost}")
