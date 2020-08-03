# 단어 s의 가운데 글자를 반환하는 함수, 
# solution을 만들어 보세요. 
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

def solution(s):
    answer = ''
    len_s = len(s)

    if len_s <= 2:
        return s

    mid = int(len_s/2)
    if len_s%2 == 0: # 짝수
        answer = s[mid-1]+s[mid]
    else: # 홀수
        answer = s[mid]
    return answer


print(solution("abc"))