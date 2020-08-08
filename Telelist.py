
#전화번호부에 영석이의 전화번호의 접두사이다.
#구조대 : 119
#박준영 : 97 674 223
#지영석 : 11 9552 4421q

# 전화번호부에 적힌 전화번호를 담은 배열 phone_book이 solution 함수의 매개 변수로 주어질때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해준다.

# 제한사항
# 각 전화번호의 길이는 1이상 20이하이다.


def solution(phone_book):
  phone_book=sorted(phone_book)
  for idx, phone in enumerate(phone_book):
    for jdx, phone_char in enumerate(phone_book[idx+1:]):
      if phone == phone_char[:len(phone)]:
        return False

  return True
  
print(solution(["123", "97674223","1235524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
    
    
