# 단어의 알파벳 개수 세기

def solution(word):
    map = {}
    count = 0
    for alpha in word:
        if alpha >= 'a' and alpha <= 'z' and map.get(alpha) == None:
            map[alpha] = 'true'
            count += 1
    if not len(map):
        return -1
    return count

result = solution('test1234')
print(result)