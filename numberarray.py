# array의 각 element중 divisor로 나누어 떨어지는 값을 오른차순으로 정렬한 배열로 반환


# def solution(arr, divisor):
#     answer = [i for i in arr if i%divisor==0]
#     if not answer:
#         return [-1]
#     answer.sort()
#     return answer

def solution(arr, divisor):
    return sorted([i for i in arr if i%divisor==0]) or [-1]



list = solution([2,36,1,3],5)
print(list)