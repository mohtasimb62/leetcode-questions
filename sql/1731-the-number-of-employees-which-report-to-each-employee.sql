-- Question:
-- For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them. Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer. Return the result table ordered by employee_id.


-- Approach:
-- We do a self-join to get the employees who have someone reporting to them. Then we use the GROUP BY clause to get those employees, use the COUNT clause to count the number of employees who are reporting to those employees, and use the AVG clause to get the average age of them. Just follow the question, the main thing here was the self-join.

SELECT e.employee_id, e.name, COUNT(*) AS reports_count, ROUND(AVG(m.age)) AS average_age
FROM Employees e
JOIN Employees m
ON e.employee_id = m.reports_to
GROUP BY e.employee_id, e.name
ORDER BY e.employee_id

