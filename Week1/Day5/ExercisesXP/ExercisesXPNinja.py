# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.

# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.


cars_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

manufacturers = cars_string.split(", ")

print(f"There are {len(manufacturers)} manufacturers in the list.")

print(sorted(manufacturers, reverse=True))

count_with_o = sum(1 for name in manufacturers if "o" in name.lower())
print(f"Manufacturers with the letter 'o': {count_with_o}")

count_without_i = sum(1 for name in manufacturers if "i" not in name.lower())
print(f"Manufacturers without the letter 'i': {count_without_i}")

cars_with_duplicates = [
    "Honda", "Volkswagen", "Toyota",
    "Ford Motor", "Honda", "Chevrolet", "Toyota"
]

unique_cars = list(set(cars_with_duplicates))

print(", ".join(unique_cars))
print(f"There are now {len(unique_cars)} companies in the list.")

reversed_names = [name[::-1] for name in sorted(unique_cars)]
print(reversed_names)
