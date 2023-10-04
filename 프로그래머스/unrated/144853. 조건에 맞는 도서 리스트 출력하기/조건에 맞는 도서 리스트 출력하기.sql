-- 코드를 입력하세요
SELECT book_id, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book
where category = '인문' and PUBLISHED_DATE like '2021%'
order by PUBLISHED_DATE