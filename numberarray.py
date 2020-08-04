# array의 각 element중 divisor로 나누어 떨어지는 값을 오른차순으로 정렬한 배열로 반환


def solution(arr, divisor):
    answer = [i for i in arr if i%divisor==0]
    answer.sort()
    return answer

list = solution([2,36,1,3],1)
print(list)