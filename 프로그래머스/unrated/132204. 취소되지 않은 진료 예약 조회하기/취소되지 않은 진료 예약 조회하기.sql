-- 코드를 입력하세요
SELECT a.APNT_NO, b.PT_NAME, b.PT_NO, a.MCDP_CD, c.DR_NAME, a.APNT_YMD
FROM APPOINTMENT a inner join PATIENT b
on a.PT_NO = b.PT_NO
inner join DOCTOR c
on a.MDDR_ID= c.DR_ID
where a.APNT_YMD like '%2022-04-13%' and a.APNT_CNCL_YN = 'N' AND A.MCDP_CD = 'CS'
order by APNT_YMD