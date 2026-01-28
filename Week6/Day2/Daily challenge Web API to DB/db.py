import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="countries_db",
        user="postgres",
        password="YOUR_PASSWORD",
        host="localhost",
        port="5432"
    )
