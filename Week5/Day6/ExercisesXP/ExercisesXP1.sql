-- Exercise 1: DVD Rental
-- Instructions
-- Get a list of all the languages, from the language table.

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.

-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?



-- 1) List all languages
SELECT *
FROM language
ORDER BY language_id;

-- 2) List all films joined with their languages (INNER JOIN)
-- film title, description, language name
SELECT f.title, f.description, l.name AS language_name
FROM film f
JOIN language l ON l.language_id = f.language_id
ORDER BY f.title;

-- 3) Get all languages even if there are no films in those languages (LEFT JOIN)
-- film title, description, language name
SELECT f.title, f.description, l.name AS language_name
FROM language l
LEFT JOIN film f ON f.language_id = l.language_id
ORDER BY l.name, f.title;

-- 4) Create new table new_film (id, name) and insert a few films
DROP TABLE IF EXISTS customer_review;
DROP TABLE IF EXISTS new_film;

CREATE TABLE new_film (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES
('Desert Runner'),
('City Lights Revisited'),
('Ocean Mystery');

-- Check
SELECT * FROM new_film ORDER BY id;

-- 5) Create customer_review table with ON DELETE CASCADE for film_id
--    If a film is deleted from new_film, its reviews should be deleted automatically.
CREATE TABLE customer_review (
    review_id   SERIAL PRIMARY KEY,
    film_id     INTEGER NOT NULL REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(language_id),
    title       VARCHAR(255) NOT NULL,
    score       INTEGER NOT NULL CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP NOT NULL DEFAULT NOW()
);

-- 6) Add 2 movie reviews (linked to valid film_id + language_id)
-- Using subqueries to fetch language IDs by name (adjust names if needed).
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES
(
    (SELECT id FROM new_film WHERE name = 'Desert Runner'),
    (SELECT language_id FROM language WHERE name ILIKE 'English' LIMIT 1),
    'Fun adventure',
    8,
    'Good pacing and easy to follow.'
),
(
    (SELECT id FROM new_film WHERE name = 'Ocean Mystery'),
    (SELECT language_id FROM language WHERE name ILIKE 'French' LIMIT 1),
    'Suspenseful',
    9,
    'Great atmosphere and soundtrack.'
);

-- Check reviews
SELECT *
FROM customer_review
ORDER BY review_id;

-- 7) Delete a film that has a review and see what happens (CASCADE deletes the review)
-- Before:
SELECT nf.id, nf.name, cr.review_id, cr.title
FROM new_film nf
LEFT JOIN customer_review cr ON cr.film_id = nf.id
ORDER BY nf.id, cr.review_id;

-- Delete a reviewed film:
DELETE FROM new_film
WHERE name = 'Desert Runner';

-- After (reviews for that film are automatically deleted):
SELECT nf.id, nf.name, cr.review_id, cr.title
FROM new_film nf
LEFT JOIN customer_review cr ON cr.film_id = nf.id
ORDER BY nf.id, cr.review_id;