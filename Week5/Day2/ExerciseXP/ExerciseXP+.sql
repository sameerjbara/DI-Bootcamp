-- Exercise 1 : Students table
-- Instructions
-- For this exercise, you will have to find some requests on your own!



-- Create
-- Create a database called bootcamp.
-- Create a table called students.
-- Add the following columns:
-- id
-- last_name
-- first_name
-- birth_date
-- The id must be auto_incremented.
-- Make sure to choose the correct data type for each column.
-- To help, here is the data that you will have to insert. (How do we insert a date to a table?)


-- Here is the data:

-- id	first_name	last_name	birth_date
-- 1	Marc	Benichou	02/11/1998
-- 2	Yoan	Cohen	03/12/2010
-- 3	Lea	Benichou	27/07/1987
-- 4	Amelia	Dux	07/04/1996
-- 5	David	Grez	14/06/2003
-- 6	Omer	Simpson	03/10/1980


-- Insert
-- Insert the data seen above to the students table. Find the most efficient way to insert the data.
-- Insert your last_name, first_name and birth_date to the students table (Take a look at the id given).


-- Select
-- Fetch all of the data from the table.
-- Fetch all of the students first_names and last_names.
-- For the following questions, only fetch the first_names and last_names of the students.
-- Fetch the student which id is equal to 2.
-- Fetch the student whose last_name is Benichou AND first_name is Marc.
-- Fetch the students whose last_names are Benichou OR first_names are Marc.
-- Fetch the students whose first_names contain the letter a.
-- Fetch the students whose first_names start with the letter a.
-- Fetch the students whose first_names end with the letter a.
-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
-- Fetch the students whose id’s are equal to 1 AND 3 .

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).



-- 1) Create database
CREATE DATABASE bootcamp;

-- Connect (psql only)
\c bootcamp

-- 2) Create table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    last_name  VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL
);

-- 3) Insert data (efficient multi-row insert)
-- Dates in PostgreSQL: use ISO format 'YYYY-MM-DD'
INSERT INTO students (id, first_name, last_name, birth_date) VALUES
(1, 'Marc',   'Benichou', '1998-11-02'),
(2, 'Yoan',   'Cohen',    '2010-12-03'),
(3, 'Lea',    'Benichou', '1987-07-27'),
(4, 'Amelia', 'Dux',      '1996-04-07'),
(5, 'David',  'Grez',     '2003-06-14'),
(6, 'Omer',   'Simpson',  '1980-10-03');

-- Insert YOUR row (replace with your real details)
-- (Don't provide id -> it auto increments)
INSERT INTO students (first_name, last_name, birth_date)
VALUES ('YourFirstName', 'YourLastName', '2000-01-01');

-- =========================
-- SELECT queries
-- =========================

-- Fetch all data
SELECT * FROM students;

-- Fetch all first_names and last_names
SELECT first_name, last_name FROM students;

-- For the following questions: only first_name and last_name

-- id = 2
SELECT first_name, last_name
FROM students
WHERE id = 2;

-- last_name = Benichou AND first_name = Marc
SELECT first_name, last_name
FROM students
WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- last_names are Benichou OR first_names are Marc
SELECT first_name, last_name
FROM students
WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- first_names contain the letter a (case-insensitive)
SELECT first_name, last_name
FROM students
WHERE first_name ILIKE '%a%';

-- first_names start with letter a
SELECT first_name, last_name
FROM students
WHERE first_name ILIKE 'a%';

-- first_names end with letter a
SELECT first_name, last_name
FROM students
WHERE first_name ILIKE '%a';

-- second to last letter is a (e.g., Leah -> a is 2nd to last)
SELECT first_name, last_name
FROM students
WHERE first_name ILIKE '%a_';

-- id’s are equal to 1 AND 3
SELECT first_name, last_name
FROM students
WHERE id IN (1, 3);

-- birth_dates are equal to or after 2000-01-01 (show all info)
SELECT *
FROM students
WHERE birth_date >= '2000-01-01';
