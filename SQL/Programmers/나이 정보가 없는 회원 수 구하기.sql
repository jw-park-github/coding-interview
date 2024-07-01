# 출저: https://school.programmers.co.kr/learn/courses/30/parts/17045
# 유형: SELECT, COUNT, IS NULL
# 날짜: 7/1(x)

SELECT COUNT(AGE IS NULL) AS USERS    # 몇 명인지, 컬럼명은 USERS로 지정
FROM USER_INFO                        # USER_INFO 테이블에서
WHERE AGE IS NULL                     # 나이 정보가 없는 회원이

# COUNT 함수: 특정 조건을 만족하는 레코드의 수를 셀 때
# AS 키워드: 컬럼이나 테이블에 별칭(alias)을 지정할 때
# IS NULL 조건문: 특정 컬럼의 값이 NULL인지 확인
