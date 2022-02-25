-- Write a script that creates a table unique_id.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT VALUE 1 UNIQUE,
     name VARCHAR(256) NOT NULL);
