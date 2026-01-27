
-- Exercise 2 – Happy Halloween
-- Instructions
-- There is a zombie plague approaching! The DVD rental company is offering to lend all of its DVDs to the local shelters, so that the citizens can watch the movies together in the shelters until the zombies are destroyed by the armed forces. Prepare tables with the following data:

-- How many stores there are, and in which city and country they are located.

-- How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.

-- Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs)

-- A list of all customers in the cities where the stores are located.

-- A list of all customers in the countries where the stores are located.

-- Some people will be frightened by watching scary movies while zombies walk the streets. Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length).
-- Hint : use the CHECK contraint

-- For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).


-- 1) How many stores there are, and in which city and country they are located.
SELECT
    s.store_id,
    ci.city,
    co.country
FROM store s
JOIN address a ON a.address_id = s.address_id
JOIN city ci ON ci.city_id = a.city_id
JOIN country co ON co.country_id = ci.country_id
ORDER BY s.store_id;

-- 2) Total viewing time in each store:
-- Sum of film length of every inventory item in the store
-- Exclude inventory items that are not yet returned (currently out)

WITH out_inventory AS (
    SELECT DISTINCT inventory_id
    FROM rental
    WHERE return_date IS NULL
)
SELECT
    i.store_id,
    SUM(f.length) AS total_minutes,
    ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
    ROUND(SUM(f.length) / 1440.0, 2) AS total_days
FROM inventory i
JOIN film f ON f.film_id = i.film_id
LEFT JOIN out_inventory oi ON oi.inventory_id = i.inventory_id
WHERE oi.inventory_id IS NULL
GROUP BY i.store_id
ORDER BY i.store_id;

-- 3) A list of all customers in the cities where the stores are located.
SELECT DISTINCT
    c.customer_id,
    c.first_name,
    c.last_name,
    ci.city
FROM customer c
JOIN address a ON a.address_id = c.address_id
JOIN city ci ON ci.city_id = a.city_id
WHERE ci.city_id IN (
    SELECT a2.city_id
    FROM store s2
    JOIN address a2 ON a2.address_id = s2.address_id
)
ORDER BY ci.city, c.last_name, c.first_name;

-- 4) A list of all customers in the countries where the stores are located.
SELECT DISTINCT
    c.customer_id,
    c.first_name,
    c.last_name,
    co.country
FROM customer c
JOIN address a ON a.address_id = c.address_id
JOIN city ci ON ci.city_id = a.city_id
JOIN country co ON co.country_id = ci.country_id
WHERE co.country_id IN (
    SELECT ci2.country_id
    FROM store s2
    JOIN address a2 ON a2.address_id = s2.address_id
    JOIN city ci2 ON ci2.city_id = a2.city_id
)
ORDER BY co.country, c.last_name, c.first_name;

-- 5) Safe list (NOT Horror category AND does NOT contain keywords)
-- Also calculate total minutes, hours, days

WITH horror_films AS (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category cat ON cat.category_id = fc.category_id
    WHERE cat.name = 'Horror'
),
safe_films AS (
    SELECT f.film_id, f.length
    FROM film f
    LEFT JOIN horror_films hf ON hf.film_id = f.film_id
    WHERE hf.film_id IS NULL
      AND f.title !~* '(beast|monster|ghost|dead|zombie|undead)'
      AND f.description !~* '(beast|monster|ghost|dead|zombie|undead)'
)
SELECT
    SUM(length) AS safe_total_minutes,
    ROUND(SUM(length) / 60.0, 2) AS safe_total_hours,
    ROUND(SUM(length) / 1440.0, 2) AS safe_total_days
FROM safe_films;

-- 6) General list (all films) total time: minutes, hours, days
SELECT
    SUM(length) AS general_total_minutes,
    ROUND(SUM(length) / 60.0, 2) AS general_total_hours,
    ROUND(SUM(length) / 1440.0, 2) AS general_total_days
FROM film;
