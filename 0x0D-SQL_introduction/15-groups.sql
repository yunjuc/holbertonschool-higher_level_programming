-- list number of records of the same score group
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;
