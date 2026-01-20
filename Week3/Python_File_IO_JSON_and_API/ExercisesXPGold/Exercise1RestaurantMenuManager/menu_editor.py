from menu_manager import MenuManager


def load_manager():
    return MenuManager()


def show_program_menu():
    print("MENU")
    print("(a) Add an item")
    print("(d) Delete an item")
    print("(v) View the menu")
    print("(x) Exit")


def add_item_to_menu(manager):
    name = input("Item name: ").strip()

    raw_price = input("Item price: ").strip()
    try:
        price = float(raw_price)
        manager.add_item(name, price)
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


def show_restaurant_menu(manager):
    items = manager.menu.get("items", [])
    if not items:
        print("Restaurant menu is empty.")
        return

    print("\nRestaurant Menu")
    print("-" * 30)
    for i, item in enumerate(items, start=1):
        item_name = item.get("name", "Unknown")
        item_price = item.get("price", 0)
        print(f"{i}. {item_name} - {item_price}")
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
        elif choice == "x":
            manager.save_to_file()
            print("Menu was saved.")
            break
        else:
            print("Invalid option. Please choose a, d, v, or x.")


def main():
    manager = load_manager()
    show_user_menu(manager)


if __name__ == "__main__":
    main()
