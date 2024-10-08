-- MySQL

SELECT DEV.ID, DEV.EMAIL, DEV.FIRST_NAME, DEV.LAST_NAME

FROM DEVELOPERS DEV, (

    SELECT SUM(CODE) AS CODE
    FROM SKILLCODES
    WHERE 1 = 1
    AND NAME IN ('Python', 'C#')
    
) PC

WHERE (PC.CODE & DEV.SKILL_CODE) > 0
ORDER BY DEV.ID ASC;