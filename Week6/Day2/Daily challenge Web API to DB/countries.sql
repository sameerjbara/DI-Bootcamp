CREATE DATABASE countries_db;

\c countries_db;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name TEXT,
    capital TEXT,
    flag TEXT,
    subregion TEXT,
    population BIGINT
);
