-- Question:
-- Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.
-- Employees can belong to multiple departments. When the employee joins other departments, they need to decide which department is their primary department.
-- Note that when an employee belongs to only one department, their primary column is 'N'. Return the result table in any order. 

-- Approach:
-- Just follow the question. Main thing here was using the IN clause to search in a subquery.

SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y' OR employee_id IN (
    SELECT employee_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(department_id) = 1
)
