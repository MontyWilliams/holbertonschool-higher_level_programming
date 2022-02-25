-- Write a script that lists the number of records with the same score
SELECT score, name COUNT(*)
FROM second_table
GROUP BY score, name
HAVING COUNT(*) > 1
