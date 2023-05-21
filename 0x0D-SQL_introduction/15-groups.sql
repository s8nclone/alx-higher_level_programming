-- Script that lists the number of records with the same score
-- in the table secon_table of the database in MySQL server
-- Result should display the number of records for this score
-- with the label number
SELECT score, COUNT(*)AS number FROM second_table GROUP BY score ORDER BY number DESC;
