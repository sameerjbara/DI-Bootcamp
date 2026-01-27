--  Exercise 1 : Items and customers
-- Instructions
-- We will work on the public database that we created yesterday.

-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- All last names (no other columns!), in reverse alphabetical order (Z-A)


-- 1) All items, ordered by price (lowest to highest)
SELECT *
FROM items
ORDER BY price ASC;

-- 2) Items with a price above 80 (80 included), ordered by price (highest to lowest)
SELECT *
FROM items
WHERE price >= 80
ORDER BY price DESC;

-- 3) First 3 customers by first_name (A-Z), exclude the primary key column
SELECT first_name, last_name
FROM customers
ORDER BY first_name ASC
LIMIT 3;

-- 4) All last names only, reverse alphabetical (Z-A)
SELECT last_name
FROM customers
ORDER BY last_name DESC;
