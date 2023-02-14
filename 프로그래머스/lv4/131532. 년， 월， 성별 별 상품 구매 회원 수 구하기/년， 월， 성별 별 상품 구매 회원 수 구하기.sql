-- 코드를 입력하세요
SELECT YEAR(b.SALES_DATE) as year, MONTH(b.sales_date) as month, a.gender, count(distinct a.user_id) as users
FROM USER_INFO a
join ONLINE_SALE b
on a.user_id = b.user_id
where a.gender is not null
group by year, month, a.gender
order by year, month, a.gender

