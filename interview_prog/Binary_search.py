"""
In Binary search,in order to perform search --> First the list should be a sorted one
Mid = low+high//2
if search_element < Mid ---> High = Mid, and size of list to be searched get shorten (right side of list from mid)
if search _element > Mid --> low = Mid, list to be searched will be left of list from mid
"""


def binary_search(ordered_lis,search_ele):
    low = 0
    high = len(ordered_lis) - 1

    while low <= high:
        mid = (low+high)//2

        if ordered_lis[mid] == search_ele:
            print(f"position of element is {mid} ")
            return True

        else:
            if search_ele > ordered_lis[mid]:
                low = mid+1
            else:
                high = mid-1

    return False

test_list = [3,6,8,2,4,9,1,5]
sorted_list = []
sorted_list = sorted(test_list)
element = 8

if binary_search(sorted_list, element):
    print("Element is found")
else:
    print("element not found")
