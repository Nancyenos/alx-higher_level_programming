--  lists all records of the table second_table with a name value

SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
