from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    id: int
    username: str
    daily_goal: int


@dataclass(frozen=True)
class Entry:
    id: int
    user_id: int
    entry_date: str
    entry_time: str
    description: str
    calories: int
    method: str
