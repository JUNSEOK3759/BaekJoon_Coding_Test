-- 코드를 입력하세요
SELECT round(avg(daily_fee)) as average_fee
from CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'