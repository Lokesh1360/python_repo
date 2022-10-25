list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9]

# new list with elements of both list
merge_list = list_1 + list_2
print(merge_list)

# to tansfer elements of one list into another
list_1.extend(list_2)
print(list_1)
print(list_2)

# -------------- adding another list as it is ------------------------
def fun(sample_list):
    sample_list += [100]
    return sample_list

sample_list = [4,5,6,7,8]
print(fun(sample_list))

