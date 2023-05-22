-- Script that list all the cities of california that can be found in the database
SELECT id, name FROM cities WHERE state_id = (
	SELECT id FROM states WHERE NAME = 'California')
	ORDER BY cities.id ASC;
