-- 1204. Last Person to Fit in the Bus
WITH RunningTotal AS (
    SELECT 
        person_name,
        SUM(weight) OVER (ORDER BY turn ASC) AS total_weight
    FROM Queue
    ORDER BY total_weight
)

SELECT
    person_name
FROM RunningTotal
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1