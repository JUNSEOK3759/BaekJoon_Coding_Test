-- 코드를 입력하세요
SELECT distinct a.CAR_ID
from CAR_RENTAL_COMPANY_CAR a join CAR_RENTAL_COMPANY_RENTAL_HISTORY b
on a.CAR_ID = b.CAR_ID
where month(START_DATE) = 10 and CAR_TYPE = '세단'
order by a.CAR_ID desc