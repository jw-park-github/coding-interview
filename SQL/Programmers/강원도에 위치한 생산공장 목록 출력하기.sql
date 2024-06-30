# 출저: https://school.programmers.co.kr/learn/courses/30/lessons/131112
# 유형: SELECT
# 날짜: 6/30(o)

SELECT FACTORY_ID, FACTORY_NAME, ADDRESS 
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'  #  ADDRESS 열의 값이 '강원도'로 시작하는 모든 행(Row)을 조회
ORDER BY FACTORY_ID



# SELECT 구문: 데이터를 조회할 때 사용
# FROM 구문: 데이터를 조회할 테이블을 지정
# WHERE 구문: 특정 조건을 만족하는 데이터만 조회
# LIKE 연산자: 부분 문자열 검색할 때 사용
# % 와일드카드: 0개 이상의 임의의 문자를 의미
# ORDER BY 구문: 결과를 정렬


