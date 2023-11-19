-- 코드를 입력하세요
-- 중고 거래 게시물을 3건 이상 등록한 사용자(서브쿼리)
-- 전체주소는 시, 도로명 주소, 상테 주소가 함께 출력
-- CITY, STREET_ADDRESS1,2
-- 전화번호 하이픈 형태
-- 회원ID 기준 내림차순
SELECT USER_ID, NICKNAME, CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS '전체주소', CONCAT(SUBSTRING(TLNO, 1, 3), '-', SUBSTRING(TLNO, 4, 4), '-', SUBSTRING(TLNO, 8)) AS '전화번호'

FROM USED_GOODS_USER
WHERE USER_ID IN (  select writer_id
                    from used_goods_board
                    group by writer_id
                    having count(writer_id) >= 3 )
ORDER BY USER_ID DESC;

# select writer_id
# from used_goods_board
# group by writer_id
# having count(writer_id) >= 3