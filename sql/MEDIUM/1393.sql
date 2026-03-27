-- 1393. Capital Gain/Loss
SELECT 
    stock_name,
    SUM(
        CASE 
            WHEN operation = 'BUY' THEN -price
            WHEN operation = 'SELL' THEN price
        END
    ) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name


-- SOL2
WITH buy_data AS (
    SELECT stock_name, SUM(price) as total_buy
    FROM Stocks
    WHERE operation = 'BUY'
    GROUP BY stock_name
)

SELECT 
    a.stock_name,
    SUM(a.price) - b.total_buy AS capital_gain_loss
FROM Stocks a
JOIN buy_data b ON a.stock_name = b.stock_name
WHERE a.operation = 'SELL'
GROUP BY a.stock_name