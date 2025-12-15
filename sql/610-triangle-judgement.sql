-- Question:
-- Find all numbers that appear at least three times consecutively. Return the result table in any order. The result format is in the following example.

-- Approach:
-- 2 approaches. First one, just follow the question by enforcing that the IDs are of increments and the numbers are the same using triple self-joins. Second, use the LEAD/LAG clause to do it cleanly.

-- By doing a triple self-join (given that all the IDs are incremental)
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs AS l1, Logs AS l2, Logs AS l3
WHERE l2.id = l1.id - 1 AND l3.id = l2.id - 1 AND l1.num = l2.num AND l2.num = l3.num

-- With LEAD/LAG clause
WITH rowWithTwoNextValues AS  (
    SELECT num,
    LEAD(num,1) OVER() AS num1,
    LEAD(num,2) OVER() AS num2
    FROM logs
)

SELECT DISTINCT num AS ConsecutiveNums
FROM rowWithTwoNextValues 
WHERE num = num1 AND num = num2


