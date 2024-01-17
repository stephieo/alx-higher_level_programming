-- displays row content in groups
SELECT score, count(*) as number FROM second_table GROUP BY score;
