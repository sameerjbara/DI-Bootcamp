import json
from pathlib import Path
from typing import Optional, List, Tuple
from datetime import datetime, date

from db import get_conn
from models import User, Entry

CONFIG_FILE = Path("config.json")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def _load_config() -> dict:
    if not CONFIG_FILE.exists():
        return {"last_user_id": None}
    try:
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {"last_user_id": None}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def _save_config(cfg: dict) -> None:
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2), encoding="utf-8")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def set_last_user_id(user_id: Optional[int]) -> None:
    cfg = _load_config()
    cfg["last_user_id"] = user_id
    _save_config(cfg)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_last_user_id() -> Optional[int]:
    return _load_config().get("last_user_id")


# -----------------------
# Users
# -----------------------
def username_exists(username: str) -> bool:
    username = username.strip()
    if not username:
        return False

    with get_conn() as conn:
        row = conn.execute(
            "SELECT 1 FROM users WHERE LOWER(username) = LOWER(?) LIMIT 1",
            (username,),
        ).fetchone()
    return row is not None

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def create_user(username: str, daily_goal: int) -> User:
    username = username.strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    if daily_goal <= 0:
        raise ValueError("Daily goal must be > 0.")

    try:
        with get_conn() as conn:
            cur = conn.execute(
                "INSERT INTO users(username, daily_goal) VALUES(?, ?)",
                (username, int(daily_goal)),
            )
            user_id = int(cur.lastrowid)
    except Exception as e:
        msg = str(e).lower()
        if "unique" in msg and ("users.username" in msg or "username" in msg):
            raise ValueError("Username already exists.") from e
        raise

    return get_user_by_id(user_id)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def list_users() -> List[User]:
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT id, username, daily_goal FROM users ORDER BY id"
        ).fetchall()
    return [User(int(r["id"]), r["username"], int(r["daily_goal"])) for r in rows]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_user_by_id(user_id: int) -> User:
    with get_conn() as conn:
        row = conn.execute(
            "SELECT id, username, daily_goal FROM users WHERE id = ?",
            (int(user_id),),
        ).fetchone()

    if not row:
        raise ValueError("User not found.")
    return User(int(row["id"]), row["username"], int(row["daily_goal"]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def update_daily_goal(user_id: int, new_goal: int) -> None:
    if new_goal <= 0:
        raise ValueError("Daily goal must be > 0.")
    with get_conn() as conn:
        conn.execute(
            "UPDATE users SET daily_goal = ? WHERE id = ?",
            (int(new_goal), int(user_id)),
        )


# -----------------------
# Entries
# -----------------------
def add_entry(
    user_id: int,
    entry_date: str,
    entry_time: str,
    description: str,
    calories: int,
    method: str,
) -> Entry:
    description = description.strip()
    if not description:
        raise ValueError("Description cannot be empty.")
    if calories < 0:
        raise ValueError("Calories cannot be negative.")

    with get_conn() as conn:
        cur = conn.execute(
            """
            INSERT INTO entries(user_id, entry_date, entry_time, description, calories, method)
            VALUES(?, ?, ?, ?, ?, ?)
            """,
            (int(user_id), entry_date, entry_time, description, int(calories), method),
        )
        entry_id = int(cur.lastrowid)

    return get_entry_by_id(entry_id)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_entry_by_id(entry_id: int) -> Entry:
    with get_conn() as conn:
        row = conn.execute(
            """
            SELECT id, user_id, entry_date, entry_time, description, calories, method
            FROM entries WHERE id = ?
            """,
            (int(entry_id),),
        ).fetchone()

    if not row:
        raise ValueError("Entry not found.")

    return Entry(
        id=int(row["id"]),
        user_id=int(row["user_id"]),
        entry_date=row["entry_date"],
        entry_time=row["entry_time"],
        description=row["description"],
        calories=int(row["calories"]),
        method=row["method"],
    )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def list_entries_for_date(user_id: int, day: str) -> List[Entry]:
    with get_conn() as conn:
        rows = conn.execute(
            """
            SELECT id, user_id, entry_date, entry_time, description, calories, method
            FROM entries
            WHERE user_id = ? AND entry_date = ?
            ORDER BY entry_time, id
            """,
            (int(user_id), day),
        ).fetchall()

    return [
        Entry(
            id=int(r["id"]),
            user_id=int(r["user_id"]),
            entry_date=r["entry_date"],
            entry_time=r["entry_time"],
            description=r["description"],
            calories=int(r["calories"]),
            method=r["method"],
        )
        for r in rows
    ]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def update_entry(entry_id: int, new_desc: str, new_calories: int) -> None:
    new_desc = new_desc.strip()
    if not new_desc:
        raise ValueError("Description cannot be empty.")
    if new_calories < 0:
        raise ValueError("Calories cannot be negative.")

    with get_conn() as conn:
        conn.execute(
            "UPDATE entries SET description = ?, calories = ? WHERE id = ?",
            (new_desc, int(new_calories), int(entry_id)),
        )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def delete_entry(entry_id: int) -> None:
    with get_conn() as conn:
        conn.execute("DELETE FROM entries WHERE id = ?", (int(entry_id),))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def daily_total(user_id: int, day: str) -> int:
    with get_conn() as conn:
        row = conn.execute(
            """
            SELECT COALESCE(SUM(calories), 0) AS total
            FROM entries
            WHERE user_id = ? AND entry_date = ?
            """,
            (int(user_id), day),
        ).fetchone()
    return int(row["total"])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def weekly_totals(user_id: int, start_day: str, end_day: str) -> List[Tuple[str, int]]:
    with get_conn() as conn:
        rows = conn.execute(
            """
            SELECT entry_date, COALESCE(SUM(calories), 0) AS total
            FROM entries
            WHERE user_id = ?
              AND entry_date >= ?
              AND entry_date <= ?
            GROUP BY entry_date
            ORDER BY entry_date
            """,
            (int(user_id), start_day, end_day),
        ).fetchall()
    return [(r["entry_date"], int(r["total"])) for r in rows]


# -----------------------
# Date helpers
# -----------------------
def is_future_day(day_str: str) -> bool:
    d = datetime.strptime(day_str, "%Y-%m-%d").date()
    return d > date.today()
