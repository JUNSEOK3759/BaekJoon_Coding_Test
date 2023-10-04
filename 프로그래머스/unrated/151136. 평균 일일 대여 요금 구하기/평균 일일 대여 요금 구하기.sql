-- 코드를 입력하세요
SELECT round(avg(daily_fee)) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
group by CAR_TYPE
having CAR_TYPE = 'SUV'