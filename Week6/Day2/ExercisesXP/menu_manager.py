from db import get_connection
from menu_item import MenuItem

class MenuManager:

    @classmethod
    def get_by_name(cls, name):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s",
            (name,)
        )
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            return MenuItem(row[0], row[1])
        return None

    @classmethod
    def all_items(cls):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT item_name, item_price FROM Menu_Items")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        return [MenuItem(name, price) for name, price in rows]
