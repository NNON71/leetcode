--1141. User Activity for the Past 30 Days I
SELECT activity_date  as day, count(DISTINCT user_id) as active_users 
FROM Activity
GROUP BY activity_date 
HAVING day BETWEEN '2019-06-28' AND '2019-07-27';