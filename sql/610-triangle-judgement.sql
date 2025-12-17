-- Question:
-- Report for every three line segments whether they can form a triangle. Return the result table in any order.

-- Approach:
-- Just follow the question here. Main thing here is to use the CASE END clause for if-then in SQL.

SELECT x, y, z,
    CASE 
        WHEN y + z > x AND x + z > y AND x + y > z THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle


