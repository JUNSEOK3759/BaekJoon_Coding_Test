SELECT A.HISTORY_ID AS HISTORY_ID, ROUND((DATEDIFF(END_DATE, START_DATE)+1)*B.DAILY_FEE*(100-IFNULL(C.DISCOUNT_RATE, 0))/100)  AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A
JOIN CAR_RENTAL_COMPANY_CAR B ON A.CAR_ID = B.CAR_ID
LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN C ON B.CAR_TYPE = C.CAR_TYPE
AND C.DURATION_TYPE = (CASE WHEN((DATEDIFF(END_DATE, START_DATE) + 1) >= 90) THEN '90일 이상'
WHEN((DATEDIFF(END_DATE, START_DATE) + 1) >= 30) THEN '30일 이상'
WHEN((DATEDIFF(END_DATE, START_DATE) + 1) >= 7) THEN '7일 이상'
END)
WHERE B.CAR_TYPE = '트럭'
GROUP BY HISTORY_ID
ORDER BY FEE DESC, HISTORY_ID DESC
