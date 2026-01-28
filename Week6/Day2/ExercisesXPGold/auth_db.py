from db import get_connection
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def user_exists(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE username=%s", (username,))
    exists = cur.fetchone() is not None
    cur.close()
    conn.close()
    return exists

def create_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, hash_password(password))
    )
    conn.commit()
    cur.close()
    conn.close()

def authenticate(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT password FROM users WHERE username=%s",
        (username,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()

    return row and row[0] == hash_password(password)
