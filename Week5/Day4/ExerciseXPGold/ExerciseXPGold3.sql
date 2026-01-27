-- Exercise 3 : Items and customers
-- Instructions
-- We will work on the public database that we created yesterday.

-- Part I

-- Create a table named purchases. It should have 3 columns :
-- id : the primary key of the table
-- customer_id : this column references the table customers
-- item_id : this column references the table items
-- quantity_purchased : this column is the quantity of items purchased by a certain customer

-- Insert purchases for the customers, use subqueries:
-- Scott Scott bought one fan
-- Melanie Johnson bought ten large desks
-- Greg Jones bougth two small desks
-- The table purchases should look like this:

-- id	customer_id	item_id	quantity_purchased
-- 1	3	3	1
-- 2	5	2	10
-- 3	1	1	2


-- Here is the explanation of the first row:

-- id = 1, this is the auto-incrementing primary key
-- customer_id = 3, because the id of Scott Scott in the customers table is 3
-- item_id = 3, because the id of a fan in the items table is 3
-- quantity_purchased = 1, because Scott Scott bought one fan


-- Part II

-- Use SQL to get the following from the database:
-- All purchases. Is this information useful to us?
-- All purchases, joining with the customers table.
-- Purchases of the customer with the ID equal to 5.
-- Purchases for a large desk AND a small desk

-- Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name
-- Customer last name
-- Item name

-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?


-- =====================================
-- Exercise 3 : Items and Customers
-- Database: public
-- =====================================

-- PART I : Create purchases table
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    item_id INTEGER REFERENCES items(id),
    quantity_purchased INTEGER NOT NULL
);

-- Insert purchases using subqueries

-- Scott Scott bought 1 fan
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name='Scott' AND last_name='Scott'),
    (SELECT id FROM items WHERE name='Fan'),
    1
);

-- Melanie Johnson bought 10 large desks
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name='Melanie' AND last_name='Johnson'),
    (SELECT id FROM items WHERE name='Large Desk'),
    10
);

-- Greg Jones bought 2 small desks
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name='Greg' AND last_name='Jones'),
    (SELECT id FROM items WHERE name='Small Desk'),
    2
);

-- PART II : Queries

-- All purchases
SELECT * FROM purchases;

-- Purchases joined with customers
SELECT p.id, c.first_name, c.last_name, p.quantity_purchased
FROM purchases p
JOIN customers c ON c.id = p.customer_id;

-- Purchases of customer_id = 5
SELECT *
FROM purchases
WHERE customer_id = 5;

-- Purchases of large desk AND small desk
SELECT p.*
FROM purchases p
JOIN items i ON i.id = p.item_id
WHERE i.name IN ('Large Desk', 'Small Desk');

-- Customers who made purchases + item name
SELECT c.first_name, c.last_name, i.name AS item_name
FROM purchases p
JOIN customers c ON c.id = p.customer_id
JOIN items i ON i.id = p.item_id;

-- Insert purchase with customer_id but no item_id
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (1, NULL, 1);
-- This works because item_id allows NULL (no NOT NULL constraint)
