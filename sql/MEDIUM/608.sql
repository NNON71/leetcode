-- 608. Tree Node
WITH Tree2 AS (
    SELECT
        p_id
    FROM Tree
    GROUP BY p_id    
)

SELECT
    id,
    CASE
        WHEN a.p_id IS NULL THEN 'Root'
        WHEN b.p_id IS NOT NULL THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree a
LEFT JOIN Tree2 b ON a.id = b.p_id
