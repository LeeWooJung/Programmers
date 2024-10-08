-- MySQL

SELECT GRADE.SCORE AS SCORE, GRADE.EMP_NO, HR_EMPLOYEES.EMP_NAME, HR_EMPLOYEES.POSITION, HR_EMPLOYEES.EMAIL

FROM HR_EMPLOYEES, (

    SELECT EMP_NO, SUM(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
    ORDER BY SCORE DESC
    LIMIT 1

) GRADE

WHERE 1 = 1
AND GRADE.EMP_NO = HR_EMPLOYEES.EMP_NO