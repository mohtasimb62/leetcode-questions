-- Question:
-- If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
-- The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order
-- Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

-- Approach:
-- To make the problem easier, make a CTE which will store the customer's first orders. With this table, do a join with the given table (Delivery)
-- and find the ones where the order date and the customer_pref_delivery_date is the same.


WITH First_orders AS (
    SELECT customer_id, MIN(order_date) AS order_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT ROUND(COUNT(*) * 100.0 / (
    SELECT COUNT(DISTINCT customer_id) FROM Delivery), 2) 
    AS immediate_percentage
FROM (
    SELECT f.customer_id 
    FROM First_orders f
    JOIN Delivery d
    ON f.customer_id = d.customer_id
    WHERE f.order_date = d.customer_pref_delivery_date
)
