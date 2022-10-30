

def sort_list(num):
    temp = 0
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j+1]
                num[j+1] = num[j]
                num[j] = temp
    return num


list_num = [1,2,3,4,4,5,5,6,1]
print(sort_list(list_num))

## Bubble sort ##
