# 출저: https://school.programmers.co.kr/learn/courses/30/parts/17045
# 유형: SELECT, COUNT, IS NULL
# 날짜: 7/1(x)

SELECT COUNT(AGE IS NULL) AS USERS    # 몇 명인지, 컬럼명은 USERS로 지정
FROM USER_INFO                        # USER_INFO 테이블에서
WHERE AGE IS NULL                     # 나이 정보가 없는 회원이
