-- 코드를 입력하세요
SELECT a.FLAVOR
from FIRST_HALF a
join (select flavor, sum(TOTAL_ORDER) as TOTAL_ORDER from JULY group by FLAVOR) b
on a.FLAVOR = b.FLAVOR
order by (a.TOTAL_ORDER + b.TOTAL_ORDER) desc
limit 3