import requests
import random
import sqlite3

# -----------------------------
# 1. Fetch countries from API
# -----------------------------
URL = "https://restcountries.com/v3.1/all"

response = requests.get(URL)

if response.status_code != 200:
    raise Exception("Failed to fetch data from API")

countries_data = response.json()

# -----------------------------
# 2. Select 10 random countries
# -----------------------------
random_countries = random.sample(countries_data, 10)

# -----------------------------
# 3. Create Database & Table
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
# 4. Insert Data into Database
# -----------------------------
for country in random_countries:
    name = country.get("name", {}).get("common", "N/A")
    
    capital_list = country.get("capital", [])
    capital = capital_list[0] if capital_list else "N/A"
    
    flag = country.get("flags", {}).get("png", "N/A")
    subregion = country.get("subregion", "N/A")
    population = country.get("population", 0)

    cursor.execute("""
    INSERT INTO countries (name, capital, flag, subregion, population)
    VALUES (?, ?, ?, ?, ?)
    """, (name, capital, flag, subregion, population))

# -----------------------------
# 5. Commit & Close
# -----------------------------
conn.commit()
conn.close()

print("✅ 10 random countries successfully inserted into countries.db")
