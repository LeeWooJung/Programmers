-- MySQL

SELECT ITEM_INFO.ITEM_ID, ITEM_INFO.ITEM_NAME, ITEM_INFO.RARITY

FROM ITEM_INFO LEFT JOIN ITEM_TREE
ON 1 = 1
AND ITEM_INFO.ITEM_ID = ITEM_TREE.PARENT_ITEM_ID
WHERE 1 = 1
AND ITEM_TREE.PARENT_ITEM_ID IS NULL
ORDER BY ITEM_INFO.ITEM_ID DESC;