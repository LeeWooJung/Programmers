-- ORACLE

WITH FILTERED AS (

    SELECT CATEGORY, MAX(PRICE) AS MAXPRICE
    FROM FOOD_PRODUCT
    WHERE 1 = 1
    AND CATEGORY IN ('과자','국','김치','식용유')
    GROUP BY CATEGORY
    
)

SELECT FOOD_PRODUCT.CATEGORY, FOOD_PRODUCT.PRICE AS MAX_PRICE, FOOD_PRODUCT.PRODUCT_NAME
FROM FOOD_PRODUCT, FILTERED
WHERE 1 = 1
AND FOOD_PRODUCT.CATEGORY = FILTERED.CATEGORY
AND FOOD_PRODUCT.PRICE >= FILTERED.MAXPRICE
ORDER BY FOOD_PRODUCT.PRICE DESC;