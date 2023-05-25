-- 코드를 입력하세요
select a.NAME, a.DATETIME
from ANIMAL_INS a left outer join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
where b.datetime is null
order by a.datetime
limit 3