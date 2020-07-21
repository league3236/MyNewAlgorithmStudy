
# 모든 braces는 반드시 닫혀야한다.
# 각각의 closed bracessms 는 open brace와 만나야한다.

def solution(values):
    len_v = len(values)
    stack = []
    if len_v%2==1:
        return 'NO'
    for idx, value in enumerate(values):
        if len(stack)==0:
            stack.append(value)
        else:
            if stack[-1] == '{' and value == '}':
                stack.pop()
            elif stack[-1] == '[' and value == ']':
                stack.pop()
            elif stack[-1] == '(' and value == ')':
                stack.pop()
            else:
                stack.append(value)
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

def braces(values):
    answer = []
    for value in values:
        answer.append(solution(value))
    return answer
print(braces(['[]{}()', '{[}]]}']))