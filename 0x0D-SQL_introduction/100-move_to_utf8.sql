-- script that converts hbtn_0c_0 databse to UTF-8(utfmb4, collate utf8mb4_unicode_ci) in MySQL server.
--convert database to utf-8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4
COLLATE utf8mb4_unicode_ci;
-- use the database
USE hbtn_0c_0;
-- convert first_table to utf-8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-- convert name column to utf8
-- ALTER TABLE first_table MODIFY name VARCHAR(256)
-- CHARACTER SET utf8mb4
-- DEFAULT NULL;
