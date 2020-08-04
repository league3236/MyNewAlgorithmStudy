
def solution(s,k):
    list = [0,0,0,0,0,0,0,0,0]
    for i in s:
        list[int(i)]+=1
    for j in list:
        if j != k and j != 0:
            return False
    return True

def perfectSubstring(s, k):
    len_s = len(s)
    answer = 0
    for i in range(len_s):
        for j in range(i+1, len_s+1):
            if solution(s[i:j],k):
                answer += 1
    return answer

print(perfectSubstring('1221221121', 3))
