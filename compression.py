def solution(s):
    answer = len(s)
    len_s = len(s)
    
    if len_s < 3:
        return answer

    max_cand = int(len_s/2)
    for size in range(1, max_cand+1):
        start = size
        res = []
        pre_s = s[:size]
        num = 1
        while True:
            now_s = s[start:start+size]
            if now_s == pre_s:
                num += 1
            else:
                res.append([num, pre_s])
                num = 1
                pre_s = now_s

            if start > len_s:
                break
            start += size
        len_cand = 0
        for idx in range(len(res)):
            if res[idx][0] == 1:
                len_cand += len(res[idx][1])
            else:
                len_cand += len(str(res[idx][0]))
                len_cand += len(res[idx][1])
        answer = min(answer,len_cand)

    return answer

print(solution("abcabcdedea"))