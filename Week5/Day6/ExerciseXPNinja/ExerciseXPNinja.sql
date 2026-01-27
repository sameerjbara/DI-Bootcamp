-- Exercise 1 : DVD Rentals
-- Instructions
-- We want to encourage families and kids to enjoy our movies.

-- Retrieve all films with a rating of G or PG, which are are not currently rented (they have been returned/have never been borrowed).

-- Create a new table which will represent a waiting list for children’s movies. This will allow a child to add their name to the list until the DVD is available (has been returned). Once the child takes the DVD, their name should be removed from the waiting list (ideally using triggers, but we have not learned about them yet. Let’s assume that our Python program will manage this). Which table references should be included?

-- Retrieve the number of people waiting for each children’s DVD. Test this by adding rows to the table that you created in question 2 above.



-- 1) Retrieve all films with rating G or PG that are NOT currently rented.
-- Not currently rented means: there is no rental row with return_date IS NULL
-- for any inventory copy of that film.

SELECT DISTINCT
    f.film_id,
    f.title,
    f.rating
FROM film f
JOIN inventory i ON i.film_id = f.film_id
LEFT JOIN rental r
    ON r.inventory_id = i.inventory_id
   AND r.return_date IS NULL
WHERE f.rating IN ('G', 'PG')
  AND r.rental_id IS NULL
ORDER BY f.title;

-- 2) Create a waiting list table for children’s movies.
-- References included:
--   - film_id -> film (which movie they are waiting for)
--   - (optional but useful) store_id -> store (which store copy / location)
-- We also store the child's name.
-- If a film is deleted, waiting entries should be deleted.

DROP TABLE IF EXISTS children_waiting_list;

CREATE TABLE children_waiting_list (
    wait_id     SERIAL PRIMARY KEY,
    film_id     INTEGER NOT NULL REFERENCES film(film_id) ON DELETE CASCADE,
    store_id    INTEGER NOT NULL REFERENCES store(store_id) ON DELETE CASCADE,
    child_name  VARCHAR(100) NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

-- 3) Retrieve number of people waiting for each children’s DVD.
-- Add some test rows first:

INSERT INTO children_waiting_list (film_id, store_id, child_name)
VALUES
(1, 1, 'Noam'),
(1, 1, 'Maya'),
(2, 1, 'Lior'),
(1, 2, 'Dana');

-- Now count how many are waiting per film
SELECT
    f.film_id,
    f.title,
    COUNT(w.wait_id) AS people_waiting
FROM film f
JOIN children_waiting_list w ON w.film_id = f.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY f.film_id, f.title
ORDER BY people_waiting DESC, f.title;
