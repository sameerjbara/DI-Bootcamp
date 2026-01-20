# anagrams.py

from anagram_checker import AnagramChecker


def show_menu() -> None:
    print("\n=== ANAGRAM CHECKER ===")
    print("1) Input a word")
    print("2) Exit")


def get_user_word() -> str | None:
    raw = input("Enter a single word: ").strip()

    # Check "single word": split on whitespace and count parts
    parts = raw.split()
    if len(parts) != 1:
        print("Error: Please enter only ONE word.")
        return None

    word = parts[0]

    # Alphabetic only
    if not word.isalpha():
        print("Error: Only alphabetic characters (A-Z) are allowed.")
        return None

    return word


def main() -> None:
    checker = AnagramChecker("sowpods.txt")

    while True:
        show_menu()
        choice = input("Choose an option (1/2): ").strip()

        if choice == "2":
            print("Goodbye!")
            break

        if choice != "1":
            print("Invalid choice. Please select 1 or 2.")
            continue

        word = get_user_word()
        if word is None:
            continue

        upper_word = word.upper()
        print(f'\nYOUR WORD : "{upper_word}"')

        if checker.is_valid_word(word):
            print("This is a valid English word.")
        else:
            print("This is NOT a valid English word.")

        anagrams = checker.get_anagrams(word)
        if anagrams:
            print("Anagrams for your word:", ", ".join(anagrams))
        else:
            print("Anagrams for your word: (none found)")


if __name__ == "__main__":
    main()
