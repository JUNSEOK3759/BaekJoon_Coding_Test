-- 코드를 입력하세요
select month(START_DATE) as MONTH, CAR_ID, count(HISTORY_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (select car_id 
                 from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 where start_date between '2022-08-01' and '2022-10-31'
                 group by CAR_ID having count(*) >= 5)
group by MONTH, CAR_ID
having MONTH between '08' and '10' and records > 0
order by MONTH ASC, CAR_ID desc
