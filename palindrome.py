def is_palindrome(word):
    # 코드를 입력하세요.
    
    l = len(word)

    for i in range(l):
        if word[l-i-1] != word[i]:
            return "false"      
    return "true"

# 테스트
print(is_palindrome("stars"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))