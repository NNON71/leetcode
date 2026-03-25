-- 602. Friend Requests II: Who Has the Most Friends
WITH cte AS (
    SELECT requester_id AS friend FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS friend FROM RequestAccepted
)
 
SELECT
    friend AS id,
    COUNT(friend) AS num
FROM cte
GROUP BY friend
ORDER BY COUNT(friend) DESC
LIMIT 1