-- MySQL

SELECT HR_DEPARTMENT.DEPT_ID, HR_DEPARTMENT.DEPT_NAME_EN, ROUND(AVG(HR_EMPLOYEES.SAL), 0) AS AVG_SAL
FROM HR_DEPARTMENT INNER JOIN HR_EMPLOYEES
ON 1 = 1
AND HR_DEPARTMENT.DEPT_ID = HR_EMPLOYEES.DEPT_ID
GROUP BY HR_DEPARTMENT.DEPT_ID, HR_DEPARTMENT.DEPT_NAME_EN
ORDER BY 3 DESC;