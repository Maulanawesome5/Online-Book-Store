-- Active: 1698011005167@@127.0.0.1@3306#tutorial_author
DROP TABLE tutorial_author;
DROP TABLE tutorial_book;
DROP TABLE tutorial_book_authors;
DROP TABLE tutorial_publisher;

SELECT * FROM accounts_customuser;
SELECT * FROM accounts_customuser_groups;
SELECT * FROM accounts_customuser_user_permissions;
SELECT * FROM accounts_useraccountprofile; -- TABEL SUDAH DIHAPUS
SELECT * FROM accounts_profile;
ALTER TABLE accounts_customuser
    DROP COLUMN address;

ALTER TABLE accounts_profile
    ADD COLUMN id INT AUTO INCREMENT NOT NULL;

ALTER TABLE accounts_profile
    ADD COLUMN user_id INT;

ALTER TABLE accounts_customuser
    ADD COLUMN address VARCHAR(255);

ALTER TABLE accounts_customuser
    ADD COLUMN profile_pict VARCHAR(255);

ALTER TABLE accounts_customuser
    ADD COLUMN birth_date VARCHAR(255);

DROP TABLE accounts_useraccountprofile;
DELETE FROM accounts_customuser WHERE id = 4;
DELETE FROM accounts_customuser_groups WHERE customuser_id = 4;

-- INSERT INTO region_subdistrict (province_id, city_id, predicate, subdistrict)
-- VALUES ();
