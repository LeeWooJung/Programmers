-- ORACLE
WITH OUT_COUNT AS (
    SELECT TO_NUMBER(TO_CHAR(DATETIME, 'HH24')) AS HOUR, COUNT(*) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY TO_NUMBER(TO_CHAR(DATETIME, 'HH24'))
)
, HOUR_LIST(HOUR) AS (
    SELECT 0 FROM DUAL
    UNION ALL
    SELECT HOUR + 1 FROM HOUR_LIST WHERE HOUR < 23
)

SELECT HOUR_LIST.HOUR, NVL(OUT_COUNT.COUNT, 0) AS COUNT
FROM HOUR_LIST
LEFT OUTER JOIN OUT_COUNT
ON HOUR_LIST.HOUR = OUT_COUNT.HOUR
ORDER BY HOUR ASC;