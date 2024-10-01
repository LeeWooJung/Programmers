-- ORACLE

WITH INFORMATION AS (

    SELECT TO_NUMBER(TO_CHAR(ONLINE_SALE.SALES_DATE, 'YYYY')) AS YEAR
           , TO_NUMBER(TO_CHAR(ONLINE_SALE.SALES_DATE, 'MM')) AS MONTH
           , USER_INFO.GENDER AS GENDER
           , USER_INFO.USER_ID AS USERS
    FROM USER_INFO, ONLINE_SALE
    WHERE 1 = 1
    AND USER_INFO.GENDER IS NOT NULL
    AND USER_INFO.USER_ID = ONLINE_SALE.USER_ID

)


SELECT YEAR, MONTH, GENDER, COUNT(DISTINCT(USERS)) AS USERS
FROM INFORMATION
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR ASC, MONTH ASC, GENDER ASC;