-- 코드를 입력하세요
SELECT a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS, date_format(b.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD a
inner join USED_GOODS_REPLY b
on a.BOARD_ID = b.BOARD_ID
where a.created_date like '%2022-10%'
order by CREATED_DATE, a.title