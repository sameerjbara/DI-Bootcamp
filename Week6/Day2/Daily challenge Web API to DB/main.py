from countries_api import get_random_countries
from countries_db import insert_country

countries = get_random_countries(10)

for c in countries:
    name = c.get("name", {}).get("common")
    capital = c.get("capital", [None])[0]
    flag = c.get("flags", {}).get("png")
    subregion = c.get("subregion")
    population = c.get("population")

    insert_country(name, capital, flag, subregion, population)

print("10 random countries saved to database")

