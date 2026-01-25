from typing import Optional, Callable, Iterable
from ui import clear_screen


def show_error_once(error: Optional[str]):
    if error:
        print(error)
        print()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def menu_choice(
    title_lines: list[str],
    options_lines: list[str],
    prompt: str = "> ",
    error: Optional[str] = None,
    allow_enter_back: bool = True,
) -> str:
    clear_screen()
    for line in title_lines:
        print(line)
    if title_lines and title_lines[-1] != "":
        print()
    for line in options_lines:
        print(line)
    if allow_enter_back:
        print("\nPress Enter to go back.\n")
    else:
        print()
    show_error_once(error)
    return input(prompt).strip()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ask_text(
    title_lines: list[str],
    prompt: str,
    error: Optional[str] = None,
) -> str:
    clear_screen()
    for line in title_lines:
        print(line)
    if title_lines and title_lines[-1] != "":
        print()
    show_error_once(error)
    return input(prompt).strip()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ask_int(
    title_lines: list[str],
    prompt: str,
    *,
    allow_enter_back: bool = True,
    min_value: Optional[int] = None,
    allow_zero: bool = True,
    error: Optional[str] = None,
) -> Optional[int]:
    while True:
        clear_screen()
        for line in title_lines:
            print(line)
        if title_lines and title_lines[-1] != "":
            print()
        show_error_once(error)

        raw = input(prompt).strip()
        if raw == "":
            return None if allow_enter_back else None

        try:
            val = int(raw)
        except ValueError:
            error = "Invalid number. Try again, or press Enter to go back."
            continue

        if min_value is not None and val < min_value:
            error = f"Value must be >= {min_value}. Try again, or press Enter to go back."
            continue

        if not allow_zero and val == 0:
            error = "Value cannot be 0. Try again, or press Enter to go back."
            continue

        return val

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ask_yes_no(
    title_lines: list[str],
    prompt: str,
    *,
    allow_enter_back: bool = True,
    error: Optional[str] = None,
) -> Optional[bool]:
    while True:
        clear_screen()
        for line in title_lines:
            print(line)
        if title_lines and title_lines[-1] != "":
            print()
        show_error_once(error)

        raw = input(prompt).strip().lower()
        if raw == "":
            return None if allow_enter_back else None
        if raw not in ("y", "n"):
            error = "Invalid answer. Try again, or press Enter to go back."
            continue
        return raw == "y"
