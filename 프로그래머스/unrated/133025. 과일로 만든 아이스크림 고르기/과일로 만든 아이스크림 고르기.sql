-- 코드를 입력하세요
SELECT ICECREAM_INFO.FLAVOR
from FIRST_HALF left outer join ICECREAM_INFO
on FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR
where total_order > 3000 and INGREDIENT_TYPE = 'fruit_based'
order by total_order desc