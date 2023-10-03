-- 코드를 입력하세요
SELECT a.REST_ID, a.REST_NAME, a.FOOD_TYPE, a.FAVORITES, a.ADDRESS, round(avg(b.review_score), 2) as SCORE
FROM REST_INFO a join REST_REVIEW b
on a.rest_id = b.rest_id
group by b.rest_id
having a.address like '서울%'
order by score desc, a.FAVORITES desc