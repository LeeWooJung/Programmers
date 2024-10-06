-- ORACLE

SELECT DISTINCT CRCRH.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR CRCC, CAR_RENTAL_COMPANY_RENTAL_HISTORY CRCRH
WHERE 1 = 1
AND CRCC.CAR_TYPE = '세단'
AND CRCC.CAR_ID = CRCRH.CAR_ID
AND TO_CHAR(CRCRH.START_DATE, 'YYYY-MM') = '2022-10'
ORDER BY 1 DESC;