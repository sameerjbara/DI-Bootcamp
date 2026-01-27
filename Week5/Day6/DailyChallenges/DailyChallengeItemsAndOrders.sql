-- Instructions
-- Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.

-- There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.

-- Create a function that returns the total price for a given order.

-- =====================================
-- Product Orders & Items (One-to-Many)
-- =====================================

DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS product_orders;

-- -------------------------------------
-- product_orders table
-- One order can have many items
-- -------------------------------------
CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    order_date DATE NOT NULL DEFAULT CURRENT_DATE
);

-- -------------------------------------
-- items table
-- Each item belongs to ONE order
-- price column is mandatory
-- -------------------------------------
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES product_orders(order_id) ON DELETE CASCADE,
    item_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0)
);

-- -------------------------------------
-- Sample data
-- -------------------------------------

INSERT INTO product_orders (customer_name) VALUES
('John Doe'),
('Jane Smith');

INSERT INTO items (order_id, item_name, price, quantity) VALUES
(1, 'Laptop', 1200.00, 1),
(1, 'Mouse', 25.00, 2),
(2, 'Keyboard', 80.00, 1);

-- -------------------------------------
-- Function: total price for a given order
-- -------------------------------------
CREATE OR REPLACE FUNCTION get_order_total(p_order_id INTEGER)
RETURNS NUMERIC(10,2)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN (
        SELECT COALESCE(SUM(price * quantity), 0)
        FROM items
        WHERE order_id = p_order_id
    );
END;
$$;

-- -------------------------------------
-- Test the function
-- -------------------------------------
SELECT get_order_total(1) AS order_1_total;
SELECT get_order_total(2) AS order_2_total;
