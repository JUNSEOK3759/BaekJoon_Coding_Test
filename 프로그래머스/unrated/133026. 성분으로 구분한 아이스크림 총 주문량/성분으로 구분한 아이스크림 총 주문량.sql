-- 코드를 입력하세요
SELECT b.INGREDIENT_TYPE, sum(a.TOTAL_ORDER)
from FIRST_HALF a
left outer join ICECREAM_INFO b
on a.flavor = b.flavor

group by b.INGREDIENT_TYPE