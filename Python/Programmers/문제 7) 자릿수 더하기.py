# 출저: https://school.programmers.co.kr/tryouts/85895/challenges
# 유형: 문자열
# 날짜: 7/4(o)

def solution(n):
    answer = 0
    for ch in str(n):
        answer += int(ch)
    return answer
