-- MySQL

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE 1 = 1
AND 'Python' IN (SKILL_1, SKILL_2, SKILL_3)
ORDER BY ID ASC