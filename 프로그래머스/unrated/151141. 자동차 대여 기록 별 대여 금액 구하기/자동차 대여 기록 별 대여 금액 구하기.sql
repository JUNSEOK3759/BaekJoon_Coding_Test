-- 코드를 입력하세요
SELECT a.HISTORY_ID,
ROUND((DATEDIFF(END_DATE, START_DATE)+1)*b.DAILY_FEE*(100-IFNULL(c.DISCOUNT_RATE, 0))/100) AS FEE

from CAR_RENTAL_COMPANY_RENTAL_HISTORY a join CAR_RENTAL_COMPANY_CAR b
on a.car_id = b.car_id
left outer join CAR_RENTAL_COMPANY_DISCOUNT_PLAN c
on b.CAR_TYPE = c.CAR_TYPE and c.DURATION_TYPE = (
case when datediff(a.end_date, a.start_date) + 1 >= 90 then '90일 이상'
when datediff(a.end_date, a.start_date) + 1 >= 30 then '30일 이상'
when datediff(a.end_date, a.start_date) + 1 >= 7 then '7일 이상' end)
where b.CAR_TYPE = '트럭'
group by a.HISTORY_ID
order by fee desc, a.HISTORY_ID desc
