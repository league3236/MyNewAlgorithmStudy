
def selection_sort(list):
    index = 0
    for i in range(len(list)-1):
        min = list[i]
        flag = False
        print('min is {}'.format(min))
        for j in range(i,len(list)):
            if min > list[j]:
                index = j
                min = list[j]
                flag = True
        if flag == True:
            tmp = list[i]
            list[i] = min
            list[index] = tmp

selection_sort([4,2,7,1,9,3])