import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="restaurant",
        user="postgres",
        password="YOUR_PASSWORD",
        host="localhost",
        port="5432"
    )
