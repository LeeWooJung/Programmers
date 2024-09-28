-- MySQL

SELECT A.ID, CASE WHEN A.R = 1 THEN 'CRITICAL'
                WHEN A.R = 2 THEN 'HIGH'
                WHEN A.R = 3 THEN 'MEDIUM'
                ELSE 'LOW' END AS COLONY_NAME

FROM (

    SELECT ID, NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS R
    FROM ECOLI_DATA

) A, ECOLI_DATA B

WHERE A.ID = B.ID
ORDER BY A.ID ASC;