# 1) What is a class?

# A class is a blueprint or template used to define the properties (attributes) and behaviors (methods) that objects will have.

# 2) What is an instance?

# An instance is a concrete object created from a class. Each instance has its own data but shares the class’s structure and behavior.

# 3) What is encapsulation?

# Encapsulation is the concept of bundling data and the methods that operate on that data together, while restricting direct access to some of the object’s internal details (using private/protected attributes).

# 4) What is abstraction?

# Abstraction focuses on exposing only the essential features of an object while hiding the complex implementation details, often using abstract classes or interfaces.

# 5) What is inheritance?

# Inheritance allows a class (child/subclass) to reuse and extend the attributes and methods of another class (parent/superclass).

# 6) What is multiple inheritance?

# Multiple inheritance is when a class inherits from more than one parent class, gaining features from all of them.

# 7) What is polymorphism?

# Polymorphism allows different classes to define methods with the same name but different behaviors, enabling objects of different types to be used interchangeably.

# 8) What is method resolution order (MRO)?

# Method Resolution Order (MRO) is the order in which Python searches for a method in a class hierarchy, especially important in multiple inheritance. Python follows the C3 linearization algorithm.


# Create a deck of cards class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # make sure the deck has exactly 52 cards
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            return None
        return self.cards.pop()
