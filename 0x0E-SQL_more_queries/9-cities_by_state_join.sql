-- displays all cities and the state they belong to 
SELECT c.id, c.name AS name, s.name AS name
FROM cities AS c
INNER JOIN states AS s ON c.state_id = s.id
ORDER BY c.id ASC;