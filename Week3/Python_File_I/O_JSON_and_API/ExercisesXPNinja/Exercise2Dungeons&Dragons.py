# Instructions
# For a game of Dungeons & Dragons, each player starts by generating a character they can play with. This character has, among other things, six attributes/stats:
# Strength
# Dexterity
# Constitution
# Intelligence
# Wisdom
# Charisma

# These six abilities have scores that are determined randomly. You do this by rolling four 6-sided dice and record the sum of the largest three dice. You do this six times, once for each ability.
# For example, the six throws of four dice may look like:
# 5, 3, 1, 6: You discard the 1 and sum 5 + 3 + 6 = 14, which you assign to strength.
# 3, 2, 5, 3: You discard the 2 and sum 3 + 5 + 3 = 11, which you assign to dexterity.
# 1, 1, 1, 1: You discard the 1 and sum 1 + 1 + 1 = 3, which you assign to constitution.
# 2, 1, 6, 6: You discard the 1 and sum 2 + 6 + 6 = 14, which you assign to intelligence.
# 3, 5, 3, 4: You discard the 3 and sum 5 + 3 + 4 = 12, which you assign to wisdom.
# 6, 6, 6, 6: You discard the 6 and sum 6 + 6 + 6 = 18, which you assign to charisma.

# Create a class called Character and a class called Game for this exercise.

# The point of this exercise is to generate characters for players looking to start a game quickly.
# Start by asking the user how many players are playing.
# Each user then creates his/her character, let them establish what the characters name and age are.
# Output the characters created into the following formats:
# txt: a nicely formatted text file for the players to use
# json: a json file of all the characters and attributes


# Hint: the Character class should be in charge of creating characters, the Game class should be in charge of how many times the Character gets instantiated and of exporting the data in json or txt



import random
import json


class Character:
    ABILITIES = [
        "Strength",
        "Dexterity",
        "Constitution",
        "Intelligence",
        "Wisdom",
        "Charisma",
    ]

    def __init__(self, name, age):
        self.name = name.strip()
        self.age = int(age)
        self.stats = self._generate_stats()

    @staticmethod
    def roll_4d6_drop_lowest():
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort()
        return sum(rolls[1:]), rolls  # (score, original rolls)

    def _generate_stats(self):
        stats = {}
        for ability in self.ABILITIES:
            score, _ = self.roll_4d6_drop_lowest()
            stats[ability] = score
        return stats

    def to_dict(self):
        return {"name": self.name, "age": self.age, "stats": self.stats}

    def to_pretty_text(self):
        lines = []
        lines.append(f"Name: {self.name}")
        lines.append(f"Age:  {self.age}")
        lines.append("Stats:")
        for ability in self.ABILITIES:
            lines.append(f"  - {ability}: {self.stats[ability]}")
        return "\n".join(lines)


class Game:
    def __init__(self):
        self.characters = []

    def create_characters(self):
        num_players = self._ask_num_players()

        for i in range(1, num_players + 1):
            print(f"\nPlayer {i}")
            name = self._ask_non_empty("Character name: ")
            age = self._ask_positive_int("Character age: ")
            character = Character(name, age)
            self.characters.append(character)
            print("Character created.")

    def export_to_json(self, file_path="characters.json"):
        data = [c.to_dict() for c in self.characters]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def export_to_txt(self, file_path="characters.txt"):
        with open(file_path, "w", encoding="utf-8") as f:
            for idx, c in enumerate(self.characters, start=1):
                f.write(f"===== Character {idx} =====\n")
                f.write(c.to_pretty_text())
                f.write("\n\n")

    def run(self):
        self.create_characters()
        self.export_to_txt("characters.txt")
        self.export_to_json("characters.json")
        print("\nSaved characters to:")
        print("- characters.txt")
        print("- characters.json")

    # ---------- input helpers ----------
    def _ask_num_players(self):
        while True:
            raw = input("How many players are playing? ").strip()
            if raw.isdigit():
                n = int(raw)
                if n > 0:
                    return n
            print("Please enter a positive integer.")

    def _ask_non_empty(self, prompt):
        while True:
            s = input(prompt).strip()
            if s:
                return s
            print("Input cannot be empty.")

    def _ask_positive_int(self, prompt):
        while True:
            raw = input(prompt).strip()
            if raw.isdigit():
                n = int(raw)
                if n > 0:
                    return n
            print("Please enter a positive integer.")


if __name__ == "__main__":
    Game().run()
