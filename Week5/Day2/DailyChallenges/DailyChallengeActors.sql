-- Instructions
-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?



-- 1. Count how many actors are in the table
SELECT COUNT(*) FROM actors; --7

-- 2. Try to add a new actor with blank fields
INSERT INTO actors (first_name, last_name, age)
VALUES ('', '', NULL);
--The insert will fail with an error (null value not allowed).
