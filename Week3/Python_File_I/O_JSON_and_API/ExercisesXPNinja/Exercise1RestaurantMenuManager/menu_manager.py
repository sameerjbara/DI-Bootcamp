{
  "items": [
    { "name": "Vegetable soup", "price": 30 },
    { "name": "Hamburger", "price": 44.9 },
    { "name": "Milkshake", "price": 22.5 },
    { "name": "Artichoke", "price": 18 },
    { "name": "Beef stew", "price": 52.5 }
  ],
  "valentines_items": []
}



import json
import re
from pathlib import Path


class MenuManager:
    def __init__(self, file_path="restaurant_menu.json"):
        self._file_path = Path(file_path)
        self.menu = {"items": [], "valentines_items": []}
        self._load_from_file()

    def _load_from_file(self):
        if not self._file_path.exists():
            return

        try:
            with self._file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict) or "items" not in data or not isinstance(data["items"], list):
                raise ValueError("Invalid menu format in JSON file.")

            # ensure valentines_items exists
            if "valentines_items" not in data or not isinstance(data["valentines_items"], list):
                data["valentines_items"] = []

            self.menu = data
        except (json.JSONDecodeError, ValueError):
            self.menu = {"items": [], "valentines_items": []}

    def add_item(self, name, price):
        name = name.strip()
        if not name:
            raise ValueError("Item name cannot be empty.")

        price = float(price)
        if price <= 0:
            raise ValueError("Price must be positive.")

        self.menu["items"].append({"name": name, "price": price})

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

    # ---------------- Valentine logic ----------------

    def add_valentine_item(self, name, price_str):
        """
        Rules:
        - Each word starts uppercase, BUT connection words are lowercase
        - First word must start with 'V'
        - at least two 'e' in the whole name (case-insensitive)
        - no numbers in the name
        - price pattern: XX.14 or XX,14 where X are digits (we accept both input styles)
        """
        name = name.strip()
        price_str = price_str.strip()

        self._validate_valentine_name(name)
        price = self._validate_valentine_price(price_str)

        self.menu["valentines_items"].append({"name": name, "price": price})
        return True

    def _validate_valentine_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty.")

        # no digits
        if any(ch.isdigit() for ch in name):
            raise ValueError("Name cannot contain numbers.")

        # at least two 'e'
        if name.lower().count("e") < 2:
            raise ValueError("Name must contain at least two 'e' letters.")

        words = name.split()
        if len(words) < 2:
            raise ValueError("Name must contain at least two words.")

        # first word must start with V
        if not words[0].startswith("V"):
            raise ValueError("First word must start with capital 'V'.")

        connection_words = {"and", "or", "of", "the", "a", "an", "in", "on", "with"}

        for idx, w in enumerate(words):
            cleaned = w.strip("-").strip()

            if not cleaned:
                raise ValueError("Invalid word in name.")

            low = cleaned.lower()

            if low in connection_words:
                # must be lowercase exactly (ignoring punctuation around)
                if cleaned != low:
                    raise ValueError(f"Connection word '{cleaned}' must be lowercase.")
            else:
                # must start uppercase
                if not cleaned[0].isupper():
                    raise ValueError(f"Word '{cleaned}' must start with uppercase.")

        return True

    def _validate_valentine_price(self, price_str):
        # pattern: XX,14 or XX.14 where XX are digits
        # Examples valid: "12,14", "99.14"
        if not re.fullmatch(r"\d{2}[,.]14", price_str):
            raise ValueError("Price must match pattern XX,14 (or XX.14).")

        # store as float, convert comma to dot
        normalized = price_str.replace(",", ".")
        return float(normalized)
