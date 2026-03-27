-- 1193. Monthly Transactions I
SELECT 
    date_format(trans_date, '%Y-%m') as month,
    country,
    count(*) as trans_count,
    sum(case when state = 'approved' then 1 else 0 end) as approved_count,
    sum(amount) as trans_total_amount,
    sum(case when state = 'approved' then amount else 0 end) approved_total_amount 
FROM Transactions
GROUP BY country, month