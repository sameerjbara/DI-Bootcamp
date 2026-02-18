import requests
import sqlite3
import random

# -----------------------------
# 1️⃣ Fetch Countries From API
# -----------------------------

URL = "https://restcountries.com/v3.1/all"

response = requests.get(URL)
countries_data = response.json()

# -----------------------------
# 2️⃣ Pick 10 Random Countries
# -----------------------------

random_countries = random.sample(countries_data, 10)

# -----------------------------
# 3️⃣ Create Database & Table
# -----------------------------

conn = sqlite3.connect("countries.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    capital TEXT,
    flag TEXT,
    subregion TEXT,
    population INTEGER
)
""")

# -----------------------------
# 4️⃣ Insert Data Into Database
# -----------------------------

for country in random_countries:
    name = country.get("name", {}).get("common", "N/A")
    
    capital_list = country.get("capital", ["N/A"])
    capital = capital_list[0] if capital_list else "N/A"
    
    flag = country.get("flags", {}).get("png", "N/A")
    subregion = country.get("subregion", "N/A")
    population = country.get("population", 0)

    cursor.execute("""
    INSERT INTO countries (name, capital, flag, subregion, population)
    VALUES (?, ?, ?, ?, ?)
    """, (name, capital, flag, subregion, population))

conn.commit()
conn.close()

print("10 random countries successfully added to the database!")
