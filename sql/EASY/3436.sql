-- 3436. Find Valid Emails
SELECT *
FROM Users
WHERE email REGEXP '^[a-z0-9_]+@[a-z]+\\.com$'
ORDER BY user_id