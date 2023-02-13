-- 코드를 입력하세요
SELECT date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE 
where month(SALES_DATE) = 3

union all

SELECT date_format(SALES_DATE, '%Y-%m-%d') as SALES_DATE, PRODUCT_ID, null as USER_ID, SALES_AMOUNT
from offline_sale
where month(SALES_DATE) = 3

order by sales_date, product_id, user_id