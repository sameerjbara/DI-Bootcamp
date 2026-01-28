from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("""
(V) View Item
(A) Add Item
(D) Delete Item
(U) Update Item
(S) Show Menu
(E) Exit
""")

        choice = input("Choice: ").upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "E":
            show_restaurant_menu()
            break
        else:
            print("Invalid option")

def add_item_to_menu():
    name = input("Name: ")
    price = int(input("Price: "))
    item = MenuItem(name, price)

    if item.save():
        print("Item was added successfully")
    else:
        print("Error adding item")

def remove_item_from_menu():
    name = input("Name: ")
    item = MenuItem(name)

    if item.delete():
        print("Item deleted successfully")
    else:
        print("Error deleting item")

def update_item_from_menu():
    old_name = input("Current name: ")
    new_name = input("New name: ")
    new_price = int(input("New price: "))

    item = MenuItem(old_name)

    if item.update(new_name, new_price):
        print("Item updated successfully")
    else:
        print("Error updating item")

def view_item():
    name = input("Name: ")
    item = MenuManager.get_by_name(name)

    if item:
        print(f"{item.name} - {item.price}")
    else:
        print("Item not found")

def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\nMenu:")
    for item in items:
        print(f"{item.name} - {item.price}")

if __name__ == "__main__":
    show_user_menu()
