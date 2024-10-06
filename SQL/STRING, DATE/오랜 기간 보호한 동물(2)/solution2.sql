-- ORACLE

WITH TAKING_TIME AS (
    SELECT ANIMAL_OUTS.ANIMAL_ID
         , ANIMAL_OUTS.NAME
         , ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME AS TTIME
    FROM ANIMAL_INS, ANIMAL_OUTS
    WHERE 1 = 1
    AND ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
    ORDER BY 3 DESC
)

SELECT ANIMAL_ID, NAME
FROM TAKING_TIME
WHERE 1 = 1
AND ROWNUM <= 2
ORDER BY TTIME DESC;