-- 코드를 입력하세요
select CATEGORY, price as max_price, PRODUCT_NAME
from FOOD_PRODUCT
where (CATEGORY, price) in (select CATEGORY, max(price) from FOOD_PRODUCT group by category)
and category in ('과자', '국', '김치', '식용유')
order by max_price desc