-- ORACLE

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE 1 = 1
AND NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY 1 ASC;