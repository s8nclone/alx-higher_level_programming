-- Script that creates the table id_not_null on MySQL server
CREATE TABLE IF NOT EXISTS id_not_nul(
	id INT DEFAULT 1,
	name VARCHAR(256) NOT NULL);
