-- lists all records with name value
-- lists in order of score, name
SELECT score, name FROM second_table WHERE EXISTS (SELECT name FROM second_table) ORDER BY score DESC;
