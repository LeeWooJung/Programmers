-- MySQL

SELECT
CASE WHEN FIND_IN_SET("Python", GROUP_CONCAT(NAME)) AND MAX(CATEGORY) = "Front End" THEN 'A'
     WHEN FIND_IN_SET("C#", GROUP_CONCAT(NAME)) THEN 'B'
     WHEN MAX(CATEGORY) = "Front End" THEN 'C'
     ELSE NULL END AS GRADE
, ID
, MIN(EMAIL) AS EMAIL

FROM DEVELOPERS
INNER JOIN SKILLCODES
ON 1 = 1
AND DEVELOPERS.SKILL_CODE & SKILLCODES.CODE = SKILLCODES.CODE
GROUP BY DEVELOPERS.ID
HAVING GRADE IS NOT NULL
ORDER BY 1, 2