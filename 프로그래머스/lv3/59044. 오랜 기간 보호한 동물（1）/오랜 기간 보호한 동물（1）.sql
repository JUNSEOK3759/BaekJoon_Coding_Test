-- 코드를 입력하세요
SELECT a.NAME, a.datetime
from ANIMAL_INS a
left outer join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
where b.DATETIME is null
order by a.datetime
limit 3