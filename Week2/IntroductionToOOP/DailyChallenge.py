# Instructions: Old MacDonald’s Farm

# You are given example code and output. Your task is to create a Farm class that produces the same output.



# Step 1: Create the Farm Class

# Create a class called Farm.
# This class will represent a farm and its animals.


# Step 2: Implement the __init__ Method

# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes: name to store the farm’s name and animals to store the animals (initialize as an empty dictionary).


# Step 3: Implement the add_animal Method

# Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.


# Step 4: Implement the get_info Method

# Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.


# Step 5: Test Your Code

# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.


# Example:

# class Farm:
#     def __init__(self, farm_name):
#         # ... code to initialize name and animals attributes ...

#     def add_animal(self, animal_type, count):
#         # ... code to add or update animal count in animals dictionary ...

#     def get_info(self):
#         # ... code to format animal info from animals dictionary ...


# # Test the code 
# macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# #output:
# # McDonald's farm

# # cow : 5
# # sheep : 2
# # goat : 12

# #     E-I-E-I-0!


# Bonus: Expand The Farm



# Step 6: Implement the get_animal_types Method

# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
# Use the sorted() function to sort the list.


# Step 7: Implement the get_short_info Method

# Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name if its count is greater than 1.
# Use string formatting to create the output.


# Step 8: upgrade the add_animal Method

# use **kwargs for passing multiple animals. The keys will be the animal name and the value will be the quantity.
# Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)


class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_str = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_str)
        self.call_history.append(call_str)

    def show_call_history(self):
        print("\n--- Call History ---")
        for call in self.call_history:
            print(call)

    def send_message(self, other_phone, content):
        msg = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(msg)
        other_phone.messages.append(msg)
        print(f"{self.phone_number} sent a message to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self):
        print("\n--- Outgoing Messages ---")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(msg)

    def show_incoming_messages(self):
        print("\n--- Incoming Messages ---")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(msg)

    def show_messages_from(self, other_phone):
        print(f"\n--- Messages from {other_phone.phone_number} ---")
        for msg in self.messages:
            if msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number:
                print(msg)


# =========================
# TEST
# =========================
phone1 = Phone("050-1111111")
phone2 = Phone("052-2222222")
phone3 = Phone("054-3333333")

# Calls
phone1.call(phone2)
phone1.call(phone3)
phone2.call(phone1)

phone1.show_call_history()
phone2.show_call_history()

# Messages
phone1.send_message(phone2, "Hey bro")
phone2.send_message(phone1, "Hello!")
phone3.send_message(phone1, "Yo Sameer")

phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from(phone2)
