
def linear_search(element, some_list):
    # 코드를 작성하세요.
    # element
    l = len(some_list)
    for i in range(l):
        if element == some_list[i]:
            return i
        elif element < some_list[i]:
            return None
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))