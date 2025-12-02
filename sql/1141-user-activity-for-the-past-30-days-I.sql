-- Question:
-- Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they 
-- made at least one activity on that day. Return the result table in any order.

-- Approach:
-- The key here is the GROUP BY clause. We group by the day between the days asked and find the count (using COUNT) of unique (using DISTINCT) user_id. Not 
-- session_id because we need to track the active users, not sessions. The same user can have multiple sessions too which gives the wrong count.

SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date >= '2019-06-28' AND activity_date <= '2019-07-27'
GROUP BY day
