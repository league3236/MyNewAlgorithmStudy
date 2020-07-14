# 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있음
# 최대한 많은 학생이 체육수업을 들어야 함
# 전체 학생의 수 n
# 체육복을 도난단한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수
# 체육수업을 들을 수 있는 학생의 최댓값을 return

def people_list(n, lost, reserve):
    people = [0]*n
    for i in range(1,n+1):
        if i in lost:
            people[i-1] = 0
            continue
        if i in reserve:
            people[i-1] = 2
        else:
            people[i-1] = 1
    return people

def solution(n, lost, reserve):
    answer = 0
    people = people_list(n, lost, reserve)
    #people = [2, 0, 0, 2]
    for i in range(0, n):
        if people[i] == 0:
            if i == 0:
                if people[i+1] == 2:
                    people[i+1]-=1
                    people[i]+=1
            elif i == n-1:
                if people[i-1] == 2:
                    people[i-1]-=1
                    people[i]+=1
            else:
                if people[i-1] == 2:
                    people[i-1]-=1
                    people[i]+=1
                elif people[i+1] == 2:
                    people[i+1]-=1
                    people[i]+=1
    for i in range(0,n):
        if people[i]==1:
            answer+=1
    return answer

if __name__ == "__main__":
    print(solution(4, [2,3], [1,4]))
    print(solution(5, [2,4], [1,3,5]))
    print(solution(5, [2,4], [3]))
    print(solution(3, [3], [1]))
