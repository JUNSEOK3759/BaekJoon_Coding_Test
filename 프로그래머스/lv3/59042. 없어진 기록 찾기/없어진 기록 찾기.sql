-- 코드를 입력하세요
SELECT a.animal_id, a.name
from ANIMAL_OUTS a
left outer join ANIMAL_INS b
on a.ANIMAL_ID = b.ANIMAL_ID
where b.DATETIME is null