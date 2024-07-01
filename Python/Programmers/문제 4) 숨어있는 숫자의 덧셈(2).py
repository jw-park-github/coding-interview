# 출저: https://school.programmers.co.kr/app/courses/17584/curriculum/lessons/197238#part-46571
# 유형: 문자열
# 날짜: 7/1(x)

def solution(my_string):
    answer = 0
    tmp =''                         # 한자리 숫자 or 연결된 숫자를 담을 변수
    for ch in my_string:
        if ch.isdigit():            # 현재 문자가 숫자면 
            tmp += ch               # tmp에 더한다
        else:                       # 현재 문자(ch)가 숫자가 아닌 문자고
            if tmp:                 # tmp에 숫자가 담겨있다면
                answer += int(tmp)  # 현재 문자(ch) 전에 나온 숫자(tmp)를 int로 형변환해서 answer에 더하고 
            tmp = ''                # 현재 문자(ch) 다음에 숫자기 나온다면 tmp에 담을 수 있도록 tmp를 초기화 

    return answer + int(tmp) if tmp else answer    # 마지막 문자가 숫자면 int()로 형변환해서 지금까지의 총합에 합쳐서 반환하고
                                                   # 문자면 더하지 않고 현재까지의 총합만 반환 

# 9~10: 처음 나오는 한자리 숫자 or 연결된 두자리 이상의 숫자를 tmp에 담는 과정
