-- 코드를 입력하세요
SELECT concat('/home/grep/src/', a.BOARD_ID, '/', a.FILE_ID, a.FILE_NAME, a.FILE_EXT) as FILE_PATH
FROM USED_GOODS_FILE a join USED_GOODS_BOARD b
on a.BOARD_ID = b.BOARD_ID
where b.views = (select max(views) from USED_GOODS_BOARD)
order by a.FILE_ID desc