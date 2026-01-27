-- Exercise 1 : DVD Rentals
-- Instructions
-- Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?

-- Get a list of all customers who have not returned their rentals. Make sure to group your results.

-- Get a list of all the Action films with Joe Swank.
-- Before you start, could there be a shortcut to getting this information? Maybe a view?



-- 1) Get a list of all rentals which are out (have not been returned).
-- Identify them by: return_date IS NULL
SELECT
    r.rental_id,
    r.rental_date,
    r.inventory_id,
    r.customer_id,
    r.return_date
FROM rental r
WHERE r.return_date IS NULL
ORDER BY r.rental_date;

-- 2) Get a list of all customers who have not returned their rentals (grouped).
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(*) AS outstanding_rentals
FROM customer c
JOIN rental r ON r.customer_id = c.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY c.customer_id;

-- 3) Get a list of all the Action films with Joe Swank.
SELECT DISTINCT
    f.film_id,
    f.title
FROM film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category cat ON cat.category_id = fc.category_id
JOIN film_actor fa ON fa.film_id = f.film_id
JOIN actor a ON a.actor_id = fa.actor_id
WHERE cat.name = 'Action'
  AND a.first_name = 'Joe'
  AND a.last_name  = 'Swank'
ORDER BY f.title;
