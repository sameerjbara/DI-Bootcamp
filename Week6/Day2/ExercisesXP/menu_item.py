from db import get_connection

class MenuItem:
    def __init__(self, name, price=0):
        self.name = name
        self.price = price

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                (self.name, self.price)
            )
            conn.commit()
            return True
        except Exception:
            conn.rollback()
            return False
        finally:
            cur.close()
            conn.close()

    def delete(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM Menu_Items WHERE item_name = %s",
            (self.name,)
        )
        success = cur.rowcount > 0
        conn.commit()
        cur.close()
        conn.close()
        return success

    def update(self, new_name, new_price):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE Menu_Items
            SET item_name = %s, item_price = %s
            WHERE item_name = %s
            """,
            (new_name, new_price, self.name)
        )
        success = cur.rowcount > 0
        conn.commit()
        cur.close()
        conn.close()
        return success
