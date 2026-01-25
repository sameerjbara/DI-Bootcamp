import os
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def pause():
    input("\nPress Enter to continue...")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def trim_text(s: str, width: int) -> str:
    if len(s) <= width:
        return s
    if width <= 3:
        return s[:width]
    return s[: width - 3] + "..."

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def now_time_str() -> str:
    return datetime.now().strftime("%H:%M:%S")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def print_users_table(users, last_id=None):
    if not users:
        print("No users yet.")
        return

    ID_W = 5
    NAME_W = 22
    GOAL_W = 10

    print(f"{'ID':<{ID_W}} {'NAME':<{NAME_W}} {'GOAL':<{GOAL_W}}")
    print("-" * (ID_W + 1 + NAME_W + 1 + GOAL_W))

    for u in users:
        name = u.username
        if last_id == u.id:
            name += " (last)"
        name = trim_text(name, NAME_W)
        print(f"{u.id:<{ID_W}} {name:<{NAME_W}} {u.daily_goal:<{GOAL_W}}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def print_entries_table(entries):
    if not entries:
        print("No entries.")
        return

    ID_W = 5
    TIME_W = 10
    CAL_W = 8
    METHOD_W = 12
    DESC_W = 35

    print(f"{'ID':<{ID_W}} {'TIME':<{TIME_W}} {'CAL':<{CAL_W}} {'METHOD':<{METHOD_W}} {'DESC':<{DESC_W}}")
    print("-" * (ID_W + 1 + TIME_W + 1 + CAL_W + 1 + METHOD_W + 1 + DESC_W))

    for e in entries:
        desc = trim_text(e.description, DESC_W)
        method = trim_text(e.method, METHOD_W)
        print(f"{e.id:<{ID_W}} {e.entry_time:<{TIME_W}} {e.calories:<{CAL_W}} {method:<{METHOD_W}} {desc:<{DESC_W}}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def print_week_table(days_list):
    DATE_W = 12
    TOTAL_W = 10

    print(f"{'DATE':<{DATE_W}} {'TOTAL':<{TOTAL_W}}")
    print("-" * (DATE_W + 1 + TOTAL_W))

    for d, t in days_list:
        print(f"{d:<{DATE_W}} {t:<{TOTAL_W}}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def goal_status_text(total: int, goal: int) -> str:
    diff = goal - total
    if diff > 0:
        return f"Remaining: {diff} kcal"
    if diff == 0:
        return "Goal reached."
    return f"Extra: {-diff} kcal"
