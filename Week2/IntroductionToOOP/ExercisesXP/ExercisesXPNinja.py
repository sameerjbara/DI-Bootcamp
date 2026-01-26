# Exercise 1 : Call History
# Instructions
# Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

# Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

# Add a method called show_call_history. This method should print the call_history.

# Add another attribute called messages to your __init__() method which value is an empty list.

# Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
# to : the number of another Phone object
# from : your phone number (also a Phone object)
# content

# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

# Test your code !!!


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
