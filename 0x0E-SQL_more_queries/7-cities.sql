-- create the database
-- and tables
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL, state_id INT NOT NULL REFERENCES states(id),	name VARCHAR(256) NOT NULL;
