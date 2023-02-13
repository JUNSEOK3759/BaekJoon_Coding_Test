-- 코드를 입력하세요
SELECT a.CATEGORY, sum(sales) as TOTAL_SALES
from BOOK a
left outer join BOOK_SALES b
on a.BOOK_ID = b.BOOK_ID
where b.sales_date like '2022-01%'
group by a.category

order by a.category 