SELECT p.product_name, o.unit
FROM Products p
INNER JOIN (
    SELECT product_id, SUM(unit) AS unit
    FROM Orders
    WHERE order_date >= '2020-02-01' AND order_date <= '2020-02-29' 
    GROUP BY product_id
    HAVING SUM(unit) >= 100
) AS o ON p.product_id = o.product_id
