# Write your MySQL query statement below
SELECT
    customer_id,
    SUM(Transactions.visit_id IS NULL) as `count_no_trans`
FROM Visits
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
GROUP BY Visits.customer_id
HAVING `count_no_trans` > 0;
