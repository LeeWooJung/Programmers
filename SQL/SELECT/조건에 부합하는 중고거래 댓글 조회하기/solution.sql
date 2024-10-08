-- ORACLE

SELECT UGB.TITLE, UGB.BOARD_ID, UGR.REPLY_ID, UGR.WRITER_ID, UGR.CONTENTS, TO_CHAR(UGR.CREATED_DATE, 'YYYY-MM-DD') AS CREATED_DATE

FROM USED_GOODS_BOARD UGB, USED_GOODS_REPLY UGR
WHERE 1 = 1
AND TO_CHAR(UGB.CREATED_DATE, 'YYYY-MM') = '2022-10'
AND UGB.BOARD_ID = UGR.BOARD_ID

ORDER BY UGR.CREATED_DATE ASC, UGB.TITLE ASC