-- 코드를 입력하세요
SELECT left(PRODUCT_CODE, 2) as CATEGORY, count(*) products
from PRODUCT
group by category
