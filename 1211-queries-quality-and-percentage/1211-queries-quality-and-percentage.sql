# Write your MySQL query statement below
-- quality = avg between query rating and position
-- poor_query_percentage = pct of all queries with rating < 3
SELECT
    query_name,
    ROUND(AVG(rating / position) , 2) AS `quality`,
    ROUND(
        SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) /
        COUNT(query_name) * 100, 2)
    AS `poor_query_percentage`
FROM Queries
GROUP BY query_name;