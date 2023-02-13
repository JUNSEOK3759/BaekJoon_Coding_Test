-- 코드를 입력하세요
SELECT MCDP_CD as 진료과코드, count(*) as 5월예약건수
from APPOINTMENT
WHERE APNT_YMD LIKE '2022-05%'
group by MCDP_CD
order by 5월예약건수, 진료과코드