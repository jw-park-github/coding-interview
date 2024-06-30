# 출저: https://school.programmers.co.kr/app/courses/17584/curriculum/lessons/197236#part-46571
# 유형: 문자열
# 날짜: 6/29(o)
'''
※ 문자열을 공백 기준으로 나누어 리스트로 변환 (my_string = my_string.split(' '))
'''

# 풀이 1
def solution(my_string):
    answer = 0
    my_string = my_string.split(' ')            # 문자열을 공백 기준으로 나누어 리스트로 변환
    
    for i in range(len(my_string)-1):           # 12, 14번 라인에서 [i+1]을 사용하기 위해 -1 
        if i == 0:                              # my_string은 숫자로만 시작하므로 인덱스 0에 대응되는 값은
            answer += int(my_string[i])         # 무조건 더함
        else:                                   # 두번째 숫자부터는, 숫자 앞의 기호가
            if my_string[i] == '+':             # +면 
                answer += int(my_string[i+1])   # 현재까지 숫자들의 합에 더하고 
            elif my_string[i] == '-':           # -면 
                answer -= int(my_string[i+1])   # 뺀다
                
    return answer


# eval()을 사용한 풀이

def solution(my_string):
    return eval(my_string)
