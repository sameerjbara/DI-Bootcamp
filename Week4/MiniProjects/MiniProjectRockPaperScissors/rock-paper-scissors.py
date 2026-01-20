
from game import Game


def get_user_menu_choice() -> str:
    """
    Show menu once, validate input, and return:
    'p' = play, 's' = show scores, 'q' = quit
    No looping here beyond validating a single entry.
    """
    print("\n=== Rock, Paper, Scissors ===")
    print("p - Play a new game")
    print("s - Show scores")
    print("q - Quit")

    choice = input("Your choice: ").strip().lower()

    if choice in ("p", "s", "q"):
        return choice

    print("Invalid choice. Please choose p, s, or q.")
    return ""


def print_results(results: dict) -> None:
    """
    Print the summary of all games played.
    results format: {'win': 2, 'loss': 4, 'draw': 3}
    """
    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)
    total = wins + losses + draws

    print("\n=== Game Summary ===")
    print(f"Total games played: {total}")
    print(f"Wins:  {wins}")
    print(f"Losses:{losses}")
    print(f"Draws: {draws}")
    print("\nThanks for playing!")


def main() -> None:
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice == "":
            continue

        if choice == "p":
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "s":
            print_results(results)

        elif choice == "q":
            print_results(results)
            break


if __name__ == "__main__":
    main()
