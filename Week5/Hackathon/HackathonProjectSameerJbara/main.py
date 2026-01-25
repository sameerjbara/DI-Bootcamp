from db import init_db
from services import get_user_by_id
from ui import clear_screen
from flows import (
    login_or_create_user,
    add_flow,
    list_day_flow,
    update_entry_flow,
    delete_entry_flow,
    daily_summary_flow,
    weekly_summary_flow,
    update_goal_flow,
    export_json_flow,
)


def main():
    init_db()
    user = login_or_create_user()

    error_main = None

    while True:
        user = get_user_by_id(user.id)

        clear_screen()
        print(f"Logged in as: {user.username} | Goal: {user.daily_goal} kcal\n")
        print("1) Add entry")
        print("2) List entries for a day")
        print("3) Update entry")
        print("4) Delete entry")
        print("5) Daily summary")
        print("6) Weekly summary (last 7 days)")
        print("7) Update daily goal")
        print("8) Export day to JSON")
        print("9) Switch user")
        print("0) Exit\n")

        if error_main:
            print(error_main)
            print()
            error_main = None

        choice = input("> ").strip()

        if choice == "":
            error_main = "Invalid option. Try again."
            continue

        if choice == "1":
            add_flow(user)
        elif choice == "2":
            list_day_flow(user)
        elif choice == "3":
            update_entry_flow(user)
        elif choice == "4":
            delete_entry_flow(user)
        elif choice == "5":
            daily_summary_flow(user)
        elif choice == "6":
            weekly_summary_flow(user)
        elif choice == "7":
            user = update_goal_flow(user)
        elif choice == "8":
            export_json_flow(user)
        elif choice == "9":
            user = login_or_create_user()
        elif choice == "0":
            clear_screen()
            print("Bye.")
            break
        else:
            error_main = "Invalid option. Try again."


if __name__ == "__main__":
    main()
