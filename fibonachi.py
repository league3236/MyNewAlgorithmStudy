def fib(n):
    if(n == 1 or n == 2):
        return 1
    else:
      return fib(n-1)+fib(n-2)  
    # 코드를 입력하세요.

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))