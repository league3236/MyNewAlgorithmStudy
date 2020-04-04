def binary_search(element, some_list):
    # 코드를 작성하세요.
    last = len(some_list)
    first = 0
    for j in range(len(some_list) // 2+1):
        index = (first+last)//2
        if some_list[index] == element:
            return index
        elif some_list[index] > element:
            last = index-1
        else:
            first = index+1
    return None
    
        
    
# binary_search(3, [1, 2, 3, 5, 8, 13, 21, 34, 55])

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))