from db import get_connection

def insert_country(name, capital, flag, subregion, population):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO countries (name, capital, flag, subregion, population)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (name, capital, flag, subregion, population)
    )
    conn.commit()
    cur.close()
    conn.close()
