
# 자료 구조 스택의 장단점

# 장점
# - 구조가 단순해서,  구현이 쉽다.
# - 데이터 저장/읽기 속도가 빠른다.

# 단점
# - 데이터 최대 갯수를 미리 정해야한다.
#   - 파이썬의 경우 재귀함수는 1000번까지만 호출이 가능함
# - 저장 공간의 낭비가 발생할 수 있음
#   - 미리 최대 갯수만큼 저장공간을 확보해야함

def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data-1)
        print("returned",data)

recursive(4)

data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)
print(data_stack.pop())

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

push(3)
push(2)
print(pop())
print(pop())