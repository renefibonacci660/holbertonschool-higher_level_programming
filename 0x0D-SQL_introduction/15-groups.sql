-- lists number of records with same score in table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC
