# Write your MySQL query statement below
SELECT
    e1.employee_id,
    e1.name,
    COUNT(e2.reports_to) as reports_count,
    ROUND(AVG(e2.age),0) as average_age
FROM Employees e1
LEFT JOIN Employees e2 ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name
HAVING reports_count > 0
ORDER BY e1.employee_id;