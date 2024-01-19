-- displays all cities and the state they belong to 
SELECT c.id, c.name as name, s.name as name
FROM cities as c
INNER JOIN states as s ON c.state_id = s.id
ORDER BY c.id ASC;