-- ORACLE

WITH RESULT AS (
    SELECT TF_TABLE.CAR_ID, MAX(TF_TABLE.TF) AS MTF
    FROM (
        SELECT CAR_ID, CASE WHEN '2022-10-16' BETWEEN TO_CHAR(START_DATE, 'YYYY-MM-DD') AND TO_CHAR(END_DATE, 'YYYY-MM-DD') THEN 1
                       ELSE 0 END AS TF
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) TF_TABLE
    GROUP BY CAR_ID
)

SELECT CAR_ID, CASE WHEN MTF = 1 THEN '대여중'
                    ELSE '대여 가능' END AS AVAILABILITY
FROM RESULT
ORDER BY CAR_ID DESC;