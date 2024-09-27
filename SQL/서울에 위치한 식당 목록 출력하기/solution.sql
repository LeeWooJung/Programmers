-- ORACLE

WITH REVIEW AS (

    SELECT REST_ID, AVG(NVL(REVIEW_SCORE, 0)) AS SCORE
    FROM REST_REVIEW
    GROUP BY REST_ID

)

SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, ROUND(B.SCORE, 2) AS SCORE

FROM REST_INFO A, REVIEW B

WHERE 1 = 1
AND A.REST_ID = B.REST_ID
AND A.ADDRESS LIKE '서울%'

ORDER BY B.SCORE DESC, A.FAVORITES DESC;

/*

SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES, A.ADDRESS, ROUND(B.SCORE, 2) AS SCORE

FROM REST_INFO A, (
    SELECT REST_ID, AVG(NVL(REVIEW_SCORE, 0)) AS SCORE
    FROM REST_REVIEW
    GROUP BY REST_ID
) B

WHERE 1 = 1
AND A.REST_ID = B.REST_ID
AND A.ADDRESS LIKE '서울%'

ORDER BY B.SCORE DESC, A.FAVORITES DESC;

*/