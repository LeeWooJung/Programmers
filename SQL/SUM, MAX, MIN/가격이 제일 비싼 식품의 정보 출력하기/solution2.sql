-- ORACLE

SELECT *

FROM  (
    
    SELECT *
    FROM FOOD_PRODUCT
    ORDER BY PRICE DESC
    
)

WHERE 1 = 1
AND ROWNUM = 1;