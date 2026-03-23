-- 1731. The Number of Employees Which Report to Each Employee
SELECT 
    a.employee_id, 
    a.name,
    COUNT(a.employee_id) AS reports_count, 
    ROUND(AVG(b.age)) AS average_age
FROM Employees a
JOIN Employees b ON a.employee_id = b.reports_to
GROUP BY employee_id
ORDER BY employee_id
