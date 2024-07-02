# 출저: https://school.programmers.co.kr/tryouts/85894/challenges
# 유형: 문자열
# 날짜: 7/2(o)


# 풀이 1
def solution(A, B):
    answer = 0
    if A == B:
        return 0
    
    for i in range(1, len(A)):
        A = A[-1] + A[:-1]
        if A == B:
            return i
        
    return -1


# 풀이 2
def solution(A, B):
    answer = 0
    for _ in range(len(A) - 1):
        if A == B:
            return 0
        answer += 1
        A = A[-1] + A[:-1]
        if A == B:
            return answer
        else:
            if len(A) - 1 == answer:
                return -1



        
    
