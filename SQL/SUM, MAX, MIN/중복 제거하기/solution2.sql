-- ORACLE

SELECT COUNT(*) AS COUNT

FROM (

    SELECT DISTINCT(NAME) AS DNAME
    FROM ANIMAL_INS
    WHERE 1 = 1
    AND NAME IS NOT NULL
    
)