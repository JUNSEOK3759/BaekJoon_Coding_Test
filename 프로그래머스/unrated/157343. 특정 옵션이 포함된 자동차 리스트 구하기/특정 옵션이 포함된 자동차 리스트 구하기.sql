-- 코드를 입력하세요
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
from CAR_RENTAL_COMPANY_CAR 
where options like '%네비게이션%'
order by CAR_ID desc