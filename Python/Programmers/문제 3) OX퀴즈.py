# 출저: https://school.programmers.co.kr/app/courses/17584/curriculum/lessons/197237#part-46571
# 유형: 문자열
# 날짜: 6/30(o)
'''
※ int()는 - 부호가 붙은 정수를 음의 정수로 반환.
※ split()으로 N개의 변수에 나눠 담기 (num1, sign, num2 = left_e.split())
'''

# 풀이 1
def solution(quiz):
    answer = []
    
    for i in range(len(quiz)):
        quiz[i] = quiz[i].split(' ')
        if quiz[i][1] == "+":
            if int(quiz[i][0]) + int(quiz[i][2]) == int(quiz[i][4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(quiz[i][0]) - int(quiz[i][2]) == int(quiz[i][4]):
                answer.append("O")
            else:
                answer.append("X")
            
    return answer

'''
1. 리스트 내 각각의 문자열에 대해 공백을 기준으로 나눠 리스트로 변환.
2. 인덱스 0과 2에 대응되는 문자열을 int()로 형변환하고, 인덱스 1에 대응되는 문자열이 +면 두 수를 더하고, -면 뺀다.
3. 더하거나 뺀 값을, 인덱스 4에 대응되는 문자열을 int()로 형변환 값과 비교하여
3. 같으면 answer에 'O'를, 다르면 'X'를 추가.
'''

# eval()을 이용한 풀이
def solution(quiz):
    answer = []
    for ch in quiz:
        ch = ch.split('=')
        if eval(ch[0]) == int(ch[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer


# 풀이 3
def solution(quiz):
    answer = []
    for equation in quiz:
        left_e, right_e = equation.split('=')
        num1, sign, num2 = left_e.split()
        if sign == '+' and int(num1) + int(num2) == int(right_e):
            answer.append('O')
        elif sign == '-' and int(num1) - int(num2) == int(right_e):
            answer.append('O')
        else:
            answer.append('X')
            
    return answer

# 책의 해답
def solution(quiz):
    answer = []
    for q in quiz:
        left, right = q.split('=')
        num1, op, num2 = left.split()
    
        if op == '+':
            left = int(num1) + int(num2)
        else:
            left = int(num1) - int(num2)
    
        answer.append('O' if left == int(right) else 'X')
    
    return answer

