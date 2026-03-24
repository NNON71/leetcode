-- 3465. Find Products with Valid Serial Numbers
SELECT *
FROM products
WHERE REGEXP_LIKE (description, '(^| )SN[0-9]{4}-[0-9]{4}( |$)', 'c')
ORDER BY product_id ASC