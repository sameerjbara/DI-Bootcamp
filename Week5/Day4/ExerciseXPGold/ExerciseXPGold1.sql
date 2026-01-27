-- Exercise 1: DVD Rental
-- Instructions
-- You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
-- Find out how many films there are for each rating.

-- Get a list of all the movies that have a rating of G or PG-13.
-- Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.

-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).


-- =====================================
-- Exercise 1 : DVD Rental
-- Database: dvdrental
-- =====================================

-- 1. Count how many films for each rating
SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating
ORDER BY rating;

-- 2. Movies rated G or PG-13
SELECT film_id, title, rating
FROM film
WHERE rating IN ('G', 'PG-13');

-- 3. G or PG-13, under 2 hours, rental_rate < 3.00, sorted A-Z
SELECT film_id, title, rating, length, rental_rate
FROM film
WHERE rating IN ('G', 'PG-13')
  AND length < 120
  AND rental_rate < 3.00
ORDER BY title ASC;

-- 4. Update a customer to your details (example: customer_id = 1)
UPDATE customer
SET first_name = 'Sameer',
    last_name  = 'Jbara',
    email      = 'sameer@example.com'
WHERE customer_id = 1;

-- 5. Update that customer's address
UPDATE address
SET address = '10 Example Street',
    district = 'Center',
    postal_code = '12345',
    phone = '0500000000'
WHERE address_id = (
    SELECT address_id
    FROM customer
    WHERE customer_id = 1
);
