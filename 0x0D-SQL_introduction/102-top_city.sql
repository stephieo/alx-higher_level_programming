-- DISPLAYS AVG TEMP OF TOP THREE CITIES
SELECT city, AVG(value) as avg_temp FROM temperatures 
WHERE month in (7, 8) GROUP BY city ORDER BY avg DESC LIMIT 3;