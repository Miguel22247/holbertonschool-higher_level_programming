-- create the database
-- and tables
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL, name VARCHAR(256) NOT NULL);
