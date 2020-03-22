
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if(participant[i]!=completion[i]):
            answer = participant[i]
            return answer
    answer = participant[len(participant)-1]
    return answer

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))