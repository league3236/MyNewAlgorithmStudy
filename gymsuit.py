# 프로그래머스 체육복 알고리즘 1일차
# 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있음
# 최대한 많은 학생이 체육수업을 들어야 함
# 전체 학생의 수 n
# 체육복을 도난단한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수
# 체육수업을 들을 수 있는 학생의 최댓값을 return


def solution(n, lost, reserve):
    answer = 0

    cloth = [1] * n

    for idx in lost:
        cloth[idx - 1] -= 1
    
    for idx in reserve:
        cloth[idx - 1] += 1

    for idx, value in enumerate(cloth):
        if idx>0 and value == 0 and cloth[idx-1] == 2:
            cloth[idx-1] = 1
            cloth[idx] = 1 
        elif idx <n-1 and value ==0 and cloth[idx+1] == 2:
            cloth[idx+1] = 1
            cloth[idx] = 1
    answer = n-cloth.count(0)
    return answer

if __name__ == "__main__":
    print(solution(4, [2,3], [1,4]))
    print(solution(5, [2,4], [1,3,5]))
    print(solution(5, [2,4], [3]))
    print(solution(3, [3], [1]))

