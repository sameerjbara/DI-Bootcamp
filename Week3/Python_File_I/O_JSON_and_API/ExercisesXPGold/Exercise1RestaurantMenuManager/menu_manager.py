import json
from pathlib import Path


class MenuManager:
    """
    Handles all menu logic + file I/O.
    The UI should not know anything about the JSON file structure.
    """

    def __init__(self, file_path="restaurant_menu.json"):
        self._file_path = Path(file_path)
        self.menu = {"items": []}
        self._load_from_file()

    def _load_from_file(self):
        if not self._file_path.exists():
            # If file doesn't exist, start with empty menu
            self.menu = {"items": []}
            return

        try:
            with self._file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)

            # Basic validation
            if not isinstance(data, dict) or "items" not in data or not isinstance(data["items"], list):
                raise ValueError("Invalid menu format in JSON file.")

            self.menu = data
        except (json.JSONDecodeError, ValueError):
            # If file is corrupted/invalid, still keep program usable
            self.menu = {"items": []}

    def add_item(self, name, price):
        name = name.strip()
        if not name:
            raise ValueError("Item name cannot be empty.")

        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")

        self.menu["items"].append({"name": name, "price": float(price)})

    def remove_item(self, name):
        name = name.strip()
        for i, item in enumerate(self.menu["items"]):
            if item.get("name", "").lower() == name.lower():
                del self.menu["items"][i]
                return True
        return False

    def save_to_file(self):
        with self._file_path.open("w", encoding="utf-8") as f:
            json.dump(self.menu, f, indent=4, ensure_ascii=False)
