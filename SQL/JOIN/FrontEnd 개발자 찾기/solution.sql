-- MySQL

SELECT DEVELOPERS.ID, DEVELOPERS.EMAIL, DEVELOPERS.FIRST_NAME, DEVELOPERS.LAST_NAME

FROM DEVELOPERS, (

    SELECT SUM(CODE) AS CODE_SUM
    FROM SKILLCODES
    WHERE 1 = 1
    AND CATEGORY = 'Front End'

) AS FRONTEND

WHERE 1 = 1
AND DEVELOPERS.SKILL_CODE & FRONTEND.CODE_SUM > 0

ORDER BY 1 ASC;