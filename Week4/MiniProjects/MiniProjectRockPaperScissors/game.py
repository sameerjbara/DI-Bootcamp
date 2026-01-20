
import random


class Game:
    VALID_ITEMS = ("rock", "paper", "scissors")

    def get_user_item(self) -> str:
        """
        Ask the user to select rock/paper/scissors.
        Keep asking until valid. Return the chosen item (lowercase).
        """
        while True:
            user_input = input("Select an item (rock/paper/scissors): ").strip().lower()
            if user_input in self.VALID_ITEMS:
                return user_input
            print("Invalid choice. Please type: rock, paper, or scissors.")

    def get_computer_item(self) -> str:
        """
        Randomly select rock/paper/scissors for the computer.
        """
        return random.choice(self.VALID_ITEMS)

    def get_game_result(self, user_item: str, computer_item: str) -> str:
        """
        Return 'win', 'draw', or 'loss' from the user's perspective.
        """
        if user_item == computer_item:
            return "draw"

        wins_against = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

        if wins_against[user_item] == computer_item:
            return "win"
        return "loss"

    def play(self) -> str:
        """
        Play one round:
        - get user item
        - get computer item
        - determine result
        - print the round summary
        - return 'win'/'draw'/'loss'
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        if result == "win":
            msg = "You win!"
        elif result == "loss":
            msg = "You lose!"
        else:
            msg = "You drew!"

        print(f"You selected {user_item}. The computer selected {computer_item}. {msg}")
        return result
