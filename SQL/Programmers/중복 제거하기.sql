# 출저: https://school.programmers.co.kr/learn/courses/30/lessons/59408
# 유형: DISTINCT, COUNT, IS NOT NULL
# 날짜: 7/2(x)

SELECT COUNT(DISTINCT NAME) AS count
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

# DISTINCT 키워드: 중복된 값을 제거하고 고유한 값만을 선택하는데 사용.
