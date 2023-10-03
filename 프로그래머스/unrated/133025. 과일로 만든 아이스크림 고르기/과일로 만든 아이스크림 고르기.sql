-- 코드를 입력하세요
SELECT a.flavor
from first_half a join icecream_info b
on a.flavor = b.flavor
where TOTAL_ORDER > 3000 and INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER desc