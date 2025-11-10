-- Question
-- Write a solution to find the percentage of the users registered in each contest rounded to two decimals.
-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

-- The main thing here is the GROUP BY contest_id. We do that because we are finding the percentage of users registered in each contest. From here,
-- we can just count (COUNT DISTINCT user_id) the number of distinct users in each contest and find the percentage. 

-- Note: In SQL, you have to multiply by 100.0 to convert to floating point

SELECT  contest_id, ROUND(COUNT(DISTINCT user_id)*100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC
