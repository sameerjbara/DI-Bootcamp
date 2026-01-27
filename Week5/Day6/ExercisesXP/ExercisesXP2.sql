
-- Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.



-- 1) UPDATE: change the language of some films (use valid language IDs)
-- Example: set some known dvdrental titles to 'French' (if exists)
UPDATE film
SET language_id = (SELECT language_id FROM language WHERE name ILIKE 'French' LIMIT 1)
WHERE title IN ('ACADEMY DINOSAUR', 'ACE GOLDFINGER');

-- Verify:
SELECT f.film_id, f.title, l.name AS language_name
FROM film f
JOIN language l ON l.language_id = f.language_id
WHERE f.title IN ('ACADEMY DINOSAUR', 'ACE GOLDFINGER');

-- 2) Which foreign keys are defined for the customer table?
-- (This shows references; in dvdrental customer usually references address + store.)
SELECT
    tc.constraint_name,
    kcu.column_name,
    ccu.table_name  AS referenced_table,
    ccu.column_name AS referenced_column
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
  AND tc.table_name = 'customer'
ORDER BY tc.constraint_name, kcu.column_name;

-- How it affects INSERT:
-- You must insert customer rows with valid existing address_id and store_id values
-- (otherwise the INSERT fails due to foreign key constraints).

-- 3) Drop customer_review table
-- Usually easy if nothing else depends on it. If dependencies exist, you need CASCADE.
DROP TABLE IF EXISTS customer_review;

-- 4) How many rentals are still outstanding (not returned yet)?
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

-- 5) 30 most expensive outstanding movies (by replacement_cost)
SELECT DISTINCT f.film_id, f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC, f.title ASC
LIMIT 30;

-- 6) Help your friend find 4 films

-- Film 1:
-- About a sumo wrestler, and one actor is Penelope Monroe
SELECT DISTINCT f.film_id, f.title
FROM film f
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON a.actor_id = fa.actor_id
WHERE f.description ILIKE '%sumo%'
  AND a.first_name = 'Penelope'
  AND a.last_name  = 'Monroe'
ORDER BY f.title;

-- Film 2:
-- Short documentary (< 60 minutes), rated 'R'
SELECT f.film_id, f.title, f.length, f.rating
FROM film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON c.category_id = fc.category_id
WHERE c.name = 'Documentary'
  AND f.length < 60
  AND f.rating = 'R'
ORDER BY f.title;

-- Film 3:
-- Rented by Matthew Mahan, paid > 4.00, returned between 2005-07-28 and 2005-08-01
SELECT DISTINCT f.film_id, f.title, p.amount, r.return_date
FROM customer cu
JOIN rental r   ON r.customer_id = cu.customer_id
JOIN payment p  ON p.rental_id = r.rental_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f     ON f.film_id = i.film_id
WHERE cu.first_name = 'Matthew'
  AND cu.last_name  = 'Mahan'
  AND p.amount > 4.00
  AND r.return_date >= '2005-07-28'
  AND r.return_date <  '2005-08-02'
ORDER BY r.return_date, f.title;

-- Film 4:
-- Matthew Mahan watched it too, has 'boat' in title or description, and expensive to replace
SELECT DISTINCT f.film_id, f.title, f.replacement_cost
FROM customer cu
JOIN rental r   ON r.customer_id = cu.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f     ON f.film_id = i.film_id
WHERE cu.first_name = 'Matthew'
  AND cu.last_name  = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC, f.title ASC;