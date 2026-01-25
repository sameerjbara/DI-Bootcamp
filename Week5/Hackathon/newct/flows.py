import json
from datetime import datetime, timedelta, date

from services import (
    create_user,
    username_exists,
    list_users,
    get_user_by_id,
    update_daily_goal,
    add_entry,
    list_entries_for_date,
    update_entry,
    delete_entry,
    daily_total,
    weekly_totals,
    is_future_day,
    get_last_user_id,
    set_last_user_id,
)
from estimator import estimate_calories

from ui import (
    clear_screen,
    pause,
    print_users_table,
    print_entries_table,
    print_week_table,
    goal_status_text,
    now_time_str,
)
from prompts import menu_choice, ask_text, ask_int, ask_yes_no

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def choose_date():
    error = None
    while True:
        choice = menu_choice(
            title_lines=["Choose date:"],
            options_lines=[
                "1) Today",
                "2) Yesterday",
                "3) Enter date (YYYY-MM-DD)",
                "Press Enter to go back.\n",
            ],
            prompt="> ",
            error=error,
            allow_enter_back=True,
        )

        if choice == "":
            return None

        if choice == "1":
            d = date.today()
        elif choice == "2":
            d = date.today() - timedelta(days=1)
        elif choice == "3":
            raw = ask_text(
                title_lines=["Choose date:", ""],
                prompt="Date (YYYY-MM-DD) (or press Enter to go back): ",
                error=None,
            )
            if raw == "":
                return None
            try:
                d = datetime.strptime(raw, "%Y-%m-%d").date()
            except ValueError:
                error = "Invalid date format. Try again, or press Enter to go back."
                continue
        else:
            error = "Invalid option. Try again, or press Enter to go back."
            continue

        day_str = d.strftime("%Y-%m-%d")
        if is_future_day(day_str):
            error = "Future dates are not allowed. Try again, or press Enter to go back."
            continue

        return day_str

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def _print_users_screen(selected_line: str | None = None, error: str | None = None):
    clear_screen()
    users = list_users()
    last_id = get_last_user_id()
    print("Users:\n")
    print_users_table(users, last_id)
    print("\n1) Login")
    print("2) Create new user")
    print("Press Enter to exit.\n")
    if selected_line:
        print(selected_line)
        print()
    if error:
        print(error)
        print()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def login_or_create_user():
    error_main = None

    while True:
        _print_users_screen(error=error_main)
        error_main = None

        choice = input("> ").strip()
        if choice == "":
            clear_screen()
            print("Bye.")
            raise SystemExit(0)

        # LOGIN
        if choice == "1":
            users = list_users()
            if not users:
                error_main = "No users yet. Create one first. Try again, or press Enter to exit."
                continue

            error = None
            while True:
                _print_users_screen(selected_line="> 1", error=error)
                error = None

                uid_input = input("Enter user id (or press Enter to go back): ").strip()
                if uid_input == "":
                    break

                try:
                    uid = int(uid_input)
                    if uid <= 0:
                        error = "Invalid user id. Try again, or press Enter to go back."
                        continue
                except ValueError:
                    error = "Invalid user id. Try again, or press Enter to go back."
                    continue

                try:
                    user = get_user_by_id(uid)
                    set_last_user_id(user.id)
                    return user
                except Exception:
                    error = "User not found. Try again, or press Enter to go back."

            continue

        # CREATE USER
        if choice == "2":
            error = None
            while True:
                _print_users_screen(selected_line="> 2", error=error)
                error = None

                username = input("New username (or press Enter to go back): ").strip()
                if username == "":
                    break

                if username_exists(username):
                    error = "Username already exists. Try again, or press Enter to go back."
                    continue

                goal_err = None
                while True:
                    _print_users_screen(selected_line="> 2", error=goal_err)
                    print(f"New username: {username}\n")
                    goal_err = None

                    goal_input = input("Daily goal (kcal) (or press Enter to go back): ").strip()
                    if goal_input == "":
                        break

                    try:
                        goal = int(goal_input)
                        if goal <= 0:
                            goal_err = "Goal must be > 0. Try again, or press Enter to go back."
                            continue
                    except ValueError:
                        goal_err = "Invalid goal. Try again, or press Enter to go back."
                        continue

                    try:
                        user = create_user(username, goal)
                        set_last_user_id(user.id)
                        return user
                    except Exception as e:
                        msg = str(e).lower()
                        if "already exists" in msg:
                            error = "Username already exists. Try again, or press Enter to go back."
                        else:
                            error = f"Error: {e}"
                        break

                continue

            continue

        error_main = "Invalid option. Try again, or press Enter to exit."

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def add_flow(user):
    day = choose_date()
    if day is None:
        return

    error = None
    while True:
        choice = menu_choice(
            title_lines=[f"Add entry for: {day}"],
            options_lines=[
                "1) Text (estimate calories)",
                "2) Manual calories",
            ],
            error=error,
            allow_enter_back=True,
        )

        if choice == "":
            return
        if choice not in ("1", "2"):
            error = "Invalid option. Try again, or press Enter to go back."
            continue

        # text estimate
        if choice == "1":
            error2 = None
            while True:
                food = ask_text(
                    title_lines=[f"Add by text for: {day}"],
                    prompt="What did you eat? (or press Enter to go back): ",
                    error=error2,
                )
                error2 = None
                if food == "":
                    return

                res = estimate_calories(food, prefer_api=True)

                yn = ask_yes_no(
                    title_lines=[
                        f"Date: {day}",
                        f"Food: {food}",
                        f"Estimated calories: {res.calories} kcal",
                        f"Note: {res.note}",
                        "",
                        "Save it? (y/n) (or press Enter to go back)\n",
                    ],
                    prompt="> ",
                    allow_enter_back=True,
                )
                if yn is None:
                    return
                if yn is False:
                    return

                entry = add_entry(
                    user_id=user.id,
                    entry_date=day,
                    entry_time=now_time_str(),
                    description=food,
                    calories=res.calories,
                    method=res.method,
                )
                clear_screen()
                print(f"Saved entry ID={entry.id}.")
                pause()
                return

        # manual
        if choice == "2":
            desc_error = None
            while True:
                desc = ask_text(
                    title_lines=[f"Add manual entry for: {day}"],
                    prompt="Description (or press Enter to go back): ",
                    error=desc_error,
                )
                desc_error = None
                if desc == "":
                    return

                cal_error = None
                while True:
                    cal_raw = ask_text(
                        title_lines=[f"Add manual entry for: {day}", f"Description: {desc}"],
                        prompt="Calories (or press Enter to go back): ",
                        error=cal_error,
                    )
                    cal_error = None
                    if cal_raw == "":
                        return
                    try:
                        cal = int(cal_raw)
                        if cal < 0:
                            cal_error = "Calories cannot be negative. Try again, or press Enter to go back."
                            continue
                    except ValueError:
                        cal_error = "Invalid calories. Try again, or press Enter to go back."
                        continue

                    entry = add_entry(
                        user_id=user.id,
                        entry_date=day,
                        entry_time=now_time_str(),
                        description=desc,
                        calories=cal,
                        method="manual",
                    )
                    clear_screen()
                    print(f"Saved entry ID={entry.id}.")
                    pause()
                    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def list_day_flow(user):
    day = choose_date()
    if day is None:
        return

    clear_screen()
    entries = list_entries_for_date(user.id, day)
    print(f"Entries for {day}:\n")
    print_entries_table(entries)

    total = daily_total(user.id, day)
    status = goal_status_text(total, user.daily_goal)
    print(f"\nTotal: {total} kcal | Goal: {user.daily_goal} | {status}")
    pause()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def update_entry_flow(user):
    day = choose_date()
    if day is None:
        return

    error = None
    while True:
        entries = list_entries_for_date(user.id, day)
        valid_ids = {e.id for e in entries}

        clear_screen()
        print(f"Entries for {day}:\n")
        print_entries_table(entries)
        print("\nPress Enter to go back.\n")
        if error:
            print(error)
            print()
            error = None

        if not entries:
            pause()
            return

        eid_input = input("Entry ID to update (or press Enter to go back): ").strip()
        if eid_input == "":
            return

        try:
            eid = int(eid_input)
        except ValueError:
            error = "Invalid entry id. Try again, or press Enter to go back."
            continue

        if eid not in valid_ids:
            error = "Entry not found. Try again, or press Enter to go back."
            continue

        new_desc = ask_text(
            title_lines=[f"Update entry {eid} for {day}"],
            prompt="New description (or press Enter to go back): ",
        )
        if new_desc == "":
            return

        cal_error = None
        while True:
            new_cal_raw = ask_text(
                title_lines=[f"Update entry {eid} for {day}", f"New description: {new_desc}"],
                prompt="New calories (or press Enter to go back): ",
                error=cal_error,
            )
            cal_error = None
            if new_cal_raw == "":
                return
            try:
                new_cal = int(new_cal_raw)
                if new_cal < 0:
                    cal_error = "Calories cannot be negative. Try again, or press Enter to go back."
                    continue
            except ValueError:
                cal_error = "Invalid calories. Try again, or press Enter to go back."
                continue
            break

        update_entry(eid, new_desc, new_cal)
        clear_screen()
        print("Updated.")
        pause()
        return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def delete_entry_flow(user):
    day = choose_date()
    if day is None:
        return

    error = None
    while True:
        entries = list_entries_for_date(user.id, day)
        valid_ids = {e.id for e in entries}

        clear_screen()
        print(f"Entries for {day}:\n")
        print_entries_table(entries)
        print("\nPress Enter to go back.\n")

        if error:
            print(error)
            print()
            error = None

        if not entries:
            pause()
            return

        eid_input = input("Entry ID to delete (or press Enter to go back): ").strip()
        if eid_input == "":
            return

        try:
            eid = int(eid_input)
        except ValueError:
            error = "Invalid entry id. Try again, or press Enter to go back."
            continue

        if eid not in valid_ids:
            error = "Entry not found. Try again, or press Enter to go back."
            continue

        yn = ask_yes_no(
            title_lines=[f"Delete entry {eid} for {day}"],
            prompt="Delete it? (y/n) (or press Enter to go back): ",
        )
        if yn is None or yn is False:
            return

        delete_entry(eid)
        clear_screen()
        print("Deleted.")
        pause()
        return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def daily_summary_flow(user):
    day = choose_date()
    if day is None:
        return

    total = daily_total(user.id, day)
    status = goal_status_text(total, user.daily_goal)

    clear_screen()
    print(f"Date: {day}")
    print(f"Total: {total} kcal")
    print(f"Goal: {user.daily_goal} kcal")
    print(status)
    pause()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def weekly_summary_flow(user):
    end = date.today()
    start = end - timedelta(days=6)
    totals_dict = dict(weekly_totals(user.id, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")))

    days_out = []
    for i in range(7):
        d = (start + timedelta(days=i)).strftime("%Y-%m-%d")
        days_out.append((d, int(totals_dict.get(d, 0))))

    clear_screen()
    print("Weekly summary (last 7 days):\n")
    print_week_table(days_out)

    week_sum = sum(t for _, t in days_out)
    avg = week_sum / 7.0
    print(f"\nWeek total: {week_sum} kcal | Daily average: {avg:.0f} kcal")
    pause()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def update_goal_flow(user):
    error = None
    while True:
        new_goal_input = ask_text(
            title_lines=[f"Current daily goal: {user.daily_goal} kcal"],
            prompt="New daily goal (kcal) (or press Enter to go back): ",
            error=error,
        )
        error = None

        if new_goal_input == "":
            return user

        try:
            new_goal = int(new_goal_input)
            if new_goal <= 0:
                error = "Goal must be > 0. Try again, or press Enter to go back."
                continue
        except ValueError:
            error = "Invalid goal. Try again, or press Enter to go back."
            continue

        update_daily_goal(user.id, new_goal)
        clear_screen()
        print(f"Goal updated: {user.daily_goal} -> {new_goal} kcal")
        pause()
        return get_user_by_id(user.id)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def export_json_flow(user):
    day = choose_date()
    if day is None:
        return

    entries = list_entries_for_date(user.id, day)
    data = {
        "username": user.username,
        "daily_goal": user.daily_goal,
        "date": day,
        "total": daily_total(user.id, day),
        "entries": [
            {
                "id": e.id,
                "time": e.entry_time,
                "description": e.description,
                "calories": e.calories,
                "method": e.method,
            }
            for e in entries
        ],
    }

    filename = f"export_{user.username}_{day}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    clear_screen()
    print(f"Exported to {filename}")
    pause()
