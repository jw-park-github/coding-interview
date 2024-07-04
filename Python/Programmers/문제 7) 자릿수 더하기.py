# 출저: https://school.programmers.co.kr/tryouts/85895/challenges
# 유형: 문자열
# 날짜: 7/4(o)

def solution(n):
    answer = 0
    for ch in str(n):    # 연결된 int형 정수를 str형으로 형변환하여 for문에서 한자리수 씩 ch에 할당 
        answer += int(ch)
    return answer
