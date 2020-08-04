def maxInversions(arr):
    # Write your code here
    answer = 0
    len_arr = len(arr)
    for i in range(len_arr):
        for j in range(i+1,len_arr):
            for k in range(j+1,len_arr):
                if arr[i] >= arr[j] and arr[j] >= arr[k]:
                    answer += 1
    return answer

print(maxInversions([15,10,1,7,8]))