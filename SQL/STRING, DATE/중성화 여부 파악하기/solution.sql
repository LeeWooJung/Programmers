-- ORACLE

SELECT ANIMAL_ID
     , NAME
     , CASE WHEN (UPPER(SEX_UPON_INTAKE) LIKE '%NEUTERED%'
                  OR UPPER(SEX_UPON_INTAKE) LIKE '%SPAYED%') THEN 'O'
       ELSE 'X' END AS 중성화
FROM ANIMAL_INS
ORDER BY 1 ASC;