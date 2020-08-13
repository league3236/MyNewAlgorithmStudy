# 병합정렬

def merge():
    answer = []
    return answer

def merge_sort(list, l, r):
    if l < r :
        m = l + (r-1) / 2
        print(merge_sort(list, m+1, r))  
    
    # merge_sort(list, 0, m-1)
    # merge_sort(list, m,)
    return list


list1 = [3,2,1,5]
result = merge_sort([3,2,1,5], 0, len(list1))
print(result)