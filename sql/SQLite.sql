-- Active: 1698011005167@@127.0.0.1@3306#tutorial_author
DROP TABLE tutorial_author;
DROP TABLE tutorial_book;
DROP TABLE tutorial_book_authors;
DROP TABLE tutorial_publisher;

SELECT * FROM accounts_customuser;
ALTER TABLE accounts_customuser
    DROP COLUMN address;

-- INSERT INTO region_subdistrict (province_id, city_id, predicate, subdistrict)
-- VALUES ();
