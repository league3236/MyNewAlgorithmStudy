# 병합정렬

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0 :
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
        # print(result)
    return result

def merge_sort(list):
    if len(list) <= 1:
        return list
    m = len(list) // 2
    return merge(merge_sort(list[:m]),merge_sort(list[m:]))


list1 = [3,2,1,5]
result = merge_sort([3,2,1,5])
print(result)