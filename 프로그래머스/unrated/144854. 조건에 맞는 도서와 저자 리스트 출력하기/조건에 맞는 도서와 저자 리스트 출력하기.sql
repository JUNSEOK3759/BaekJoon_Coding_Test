-- 코드를 입력하세요
SELECT A.BOOK_ID as BOOK_ID, B.AUTHOR_NAME as AUTHOR_NAME, DATE_FORMAT(A.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK A JOIN AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE
