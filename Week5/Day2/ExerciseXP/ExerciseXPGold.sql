-- Exercise 1 : Bootcamp
-- Instructions
-- Continuation of the Exercise XP +

-- Select
-- For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.

-- Fetch the first four students. You have to order the four students alphabetically by last_name.
-- Fetch the details of the youngest student.
-- Fetch three students skipping the first two students.


-- ==================================
-- Exercise 1 : Bootcamp (SELECT)
-- ==================================

-- For all queries below:
-- fetch first_name, last_name, birth_date

-- 1. Fetch the first four students
-- ordered alphabetically by last_name
SELECT first_name, last_name, birth_date
FROM students
ORDER BY last_name ASC
LIMIT 4;

-- 2. Fetch the youngest student
-- (youngest = most recent birth_date)
SELECT first_name, last_name, birth_date
FROM students
ORDER BY birth_date DESC
LIMIT 1;

-- 3. Fetch three students skipping the first two students
SELECT first_name, last_name, birth_date
FROM students
ORDER BY id
LIMIT 3 OFFSET 2;
