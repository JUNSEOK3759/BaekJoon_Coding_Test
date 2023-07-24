SELECT distinct(A.CAR_ID)
FROM CAR_RENTAL_COMPANY_CAR A JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B
ON A.CAR_ID = B.CAR_ID
WHERE A.CAR_TYPE = '세단' AND DATE_FORMAT(B.START_DATE, '%Y-%m-%d') >= '2022-10-01'
order by a.car_id desc