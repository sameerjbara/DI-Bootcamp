from menu_manager import MenuManager


def load_manager():
    return MenuManager()


def print_heart():
    heart = [
        "  ***   ***  ",
        " ***** ***** ",
        "*************",
        " *********** ",
        "  *********  ",
        "   *******   ",
        "    *****    ",
        "     ***     ",
        "      *      "
    ]
    for line in heart:
        print(line)


def show_program_menu():
    print("MENU")
    print("(a) Add an item")
    print("(d) Delete an item")
    print("(v) View the menu")
    print("(s) Add Valentine special")
    print("(x) Exit")


def add_item_to_menu(manager):
    name = input("Item name: ").strip()
    raw_price = input("Item price: ").strip()

    try:
        manager.add_item(name, float(raw_price))
        print("Item was added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def remove_item_from_menu(manager):
    name = input("Item name to delete: ").strip()
    deleted = manager.remove_item(name)
    if deleted:
        print("Item was deleted successfully.")
    else:
        print("Error: item not found.")


def add_valentine_item_ui(manager):
    print("Add Valentine special item")
    name = input("Valentine item name: ").strip()
    price = input("Valentine item price (XX,14): ").strip()

    try:
        manager.add_valentine_item(name, price)
        print("Valentine item was added successfully.")
    except ValueError as e:
        print(f"Error: {e}")


def show_restaurant_menu(manager):
    print_heart()

    items = manager.menu.get("items", [])
    valentines = manager.menu.get("valentines_items", [])

    print("\nRestaurant Menu")
    print("-" * 30)
    if not items:
        print("No regular items.")
    else:
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item['name']} - {item['price']}")
    print("-" * 30)

    print("\nValentine Specials")
    print("-" * 30)
    if not valentines:
        print("No Valentine items yet.")
    else:
        for i, item in enumerate(valentines, start=1):
            print(f"{i}. {item['name']} - {item['price']}")
    print("-" * 30)


def show_user_menu(manager):
    while True:
        show_program_menu()
        choice = input(": ").strip().lower()

        if choice == "a":
            add_item_to_menu(manager)
        elif choice == "d":
            remove_item_from_menu(manager)
        elif choice == "v":
            show_restaurant_menu(manager)
        elif choice == "s":
            add_valentine_item_ui(manager)
        elif choice == "x":
            manager.save_to_file()
            print("Menu was saved.")
            break
        else:
            print("Invalid option. Please choose a, d, v, s, or x.")


def main():
    manager = load_manager()
    show_user_menu(manager)


if __name__ == "__main__":
    main()
