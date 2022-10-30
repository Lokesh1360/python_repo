
def find_miss(arr,n):
    first = arr[0]
    last = arr[-1]

    if first+last % 2:
        s = (n+1)/2
        s *= (first+last)

    else:
        s = (first+last)/2
        s *= (n+1)

    missing = s - sum(arr)
    return missing

arr = [1,2,3,4,6,7,8,9]
n = len(arr)
print(find_miss(arr,n))
