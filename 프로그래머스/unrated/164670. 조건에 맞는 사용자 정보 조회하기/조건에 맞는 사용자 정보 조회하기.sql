-- 코드를 입력하세요
SELECT a.USER_ID, a.NICKNAME, CONCAT(a.CITY, ' ', a.STREET_ADDRESS1,' ', a.STREET_ADDRESS2) AS 전체주소, 
CONCAT(LEFT(a.TLNO, 3), '-', MID(a.TLNO, 4, 4), '-', RIGHT(a.TLNO, 4)) AS 전화번호
FROM USED_GOODS_USER a join USED_GOODS_BOARD b
on a.USER_ID = b.WRITER_ID
group by USER_ID
having count(*) >= 3
order by a.USER_ID desc