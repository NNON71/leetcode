-- 3570. Find Books with No Available Copies
SELECT l.book_id, l.title, l.author, l.genre, l.publication_year, b.borrow AS current_borrowers
FROM library_books l
LEFT JOIN (
    SELECT book_id, COUNT(*) AS borrow
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
) b
ON l.book_id = b.book_id
WHERE l.total_copies = b.borrow
ORDER BY current_borrowers DESC, l.title ASC

select l.book_id, l.title, l.author, l.genre, l.publication_year, count(case when b.borrow_date is not null and b.return_date is null then 1 end) as current_borrowers
from library_books l
join borrowing_records b
on l.book_id=b.book_id
group by l.book_id, l.title, l.author, l.genre, l.publication_year, l.total_copies
having l.total_copies = current_borrowers
order by current_borrowers desc, l.title asc