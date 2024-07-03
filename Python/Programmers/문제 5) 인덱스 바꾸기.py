# 출저: https://school.programmers.co.kr/tryouts/85893/challenges
# 유형: 문자열
# 날짜: 7/3(x)

def solution(my_string, num1, num2):

    my_string = list(my_string)  # 문자열을 구성하는 각각의 문자 (공백 포함)를 원소로 하는 리스트로 반환  
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]  # 자리 바꿈
    
    return ''.join(my_string)  # 리스트의 각 원소들을 공백 없이(원소인 공백은 포함) 연결시켜 하나의 문자열로 반환

