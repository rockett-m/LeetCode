# Write your MySQL query statement below
SELECT
    project_id,
    ROUND(AVG(Employee.experience_years), 2) AS `average_years`
FROM Project
INNER JOIN Employee ON Project.employee_id = Employee.employee_id
GROUP BY project_id;
