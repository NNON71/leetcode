SELECT B.name AS Employee
FROM Employee A, Employee B
WHERE A.id <> B.id
AND A.id = B.managerId
AND B.salary > A.salary