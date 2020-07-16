# -*- coding: utf-8 -*- 
# 2016년 1월 1일은 금요일
# 2016년 a월 b일은 무슨요일?
# 두수 a, b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수를 작성
# 2016년은 윤년임
# 2016년 a월 b일은 실제 있는 날이다.

def solution(a, b):
    answer = ''
    sum = 0
    enum = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for idx in range(0,a-1):
        sum += month[idx]
    sum += b
    answer = enum[sum % 7]

    return answer

print(solution(5,24))