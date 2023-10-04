SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO, 'NONE') as TLNO
from PATIENT
where AGE <= 12 and gend_cd = 'W'
order by age desc, PT_NAME