-- 코드를 입력하세요
select a.PRODUCT_CODE, sum(a.PRICE * b.SALES_AMOUNT) as SALE
from product a inner join OFFLINE_SALE b
on a.PRODUCT_ID = b.PRODUCT_ID
group by a.PRODUCT_CODE
order by SALE desc, a.PRODUCT_CODE 