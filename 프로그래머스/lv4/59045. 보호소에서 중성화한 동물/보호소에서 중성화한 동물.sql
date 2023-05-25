-- 코드를 입력하세요
select a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_INS a join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
where (a.SEX_UPON_INTAKE = 'Intact Male' and b.SEX_UPON_OUTCOME = 'Neutered Male') or (a.SEX_UPON_INTAKE = 'Intact Female' and b.SEX_UPON_OUTCOME = 'Spayed Female')