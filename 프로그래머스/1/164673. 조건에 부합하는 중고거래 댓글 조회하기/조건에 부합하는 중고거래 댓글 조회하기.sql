-- 코드를 입력하세요
SELECT 
    A.TITLE AS TITLE, 
    A.BOARD_ID AS BOARD_ID, 
    B.REPLY_ID AS REPLY_ID, 
    B.WRITER_ID AS WRITER_ID, 
    B.CONTENTS AS CONTENTS, 
    DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM used_goods_board AS A, used_goods_reply AS B
where (A.board_id = B.board_id) AND (DATE_FORMAT(A.CREATED_DATE, '%Y-%m') = '2022-10')
order by B.created_date ASC, A.title ASC