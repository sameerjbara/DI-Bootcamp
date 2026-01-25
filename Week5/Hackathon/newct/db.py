import sqlite3
from pathlib import Path

DB_FILE = Path("calorie_tracker.sqlite3")


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db() -> None:
    with get_conn() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                daily_goal INTEGER NOT NULL CHECK (daily_goal > 0),
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                entry_date TEXT NOT NULL,
                entry_time TEXT NOT NULL,
                description TEXT NOT NULL,
                calories INTEGER NOT NULL CHECK (calories >= 0),
                method TEXT NOT NULL CHECK (method IN ('manual', 'text_estimate', 'api_guess')),
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );

            CREATE INDEX IF NOT EXISTS idx_entries_user_date ON entries(user_id, entry_date);
            """
        )
