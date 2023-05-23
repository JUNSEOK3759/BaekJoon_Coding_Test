-- 코드를 입력하세요
select a.FLAVOR
from FIRST_HALF a join (select flavor, sum(total_order) as total_order from july group by flavor) b
on a.flavor = b.flavor
order by (a.TOTAL_ORDER + b.TOTAL_ORDER) desc
limit 3