-- 코드를 입력하세요
-- 조회수가 가장 높은 게시물
-- 첨부파일 경로 조회
-- FILE ID 기준으로 내림차순
-- 파일경로 /home/grep/src/
SELECT CONCAT('/home/grep/src/',B.BOARD_ID,'/',F.FILE_ID,F.FILE_NAME,F.FIle_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_FILE AS F ON B.BOARD_ID = F.BOARD_ID
WHERE B.VIEWS = (SELECT VIEWS 
                 FROM USED_GOODS_BOARD
                ORDER BY VIEWS DESC LIMIT 1)
ORDER BY F.FILE_ID DESC;