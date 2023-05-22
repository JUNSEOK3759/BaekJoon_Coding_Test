-- 코드를 입력하세요
SELECT a.PRODUCT_ID, a.PRODUCT_NAME, sum(a.price * b.amount) as total_sales
from FOOD_PRODUCT a
INNER join FOOD_ORDER b
on a.PRODUCT_ID = b.PRODUCT_ID
where b.PRODUCE_DATE like '2022-05%'
group by a.PRODUCT_ID

order by total_sales desc, a.product_id

