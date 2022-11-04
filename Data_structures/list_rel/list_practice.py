# Prog1 --> Find the missing elements in a list by comparing with other list
"""Input : test_list1 = [5, 6, 4, 8, 9, 1], test_list2 = [9, 8, 10]
Output : [5, 6, 4, 1, 9, 8, 10]"""

# test_list1 = [5, 6, 4, 8, 9, 1]
# test_list2 = [9, 8, 10]
#
# temp = [ele for ele in test_list1 if ele not in test_list2]
# print(temp)
#
# output_list = temp + test_list2
# print(output_list)
#
# diff_elements = set(test_list1) - set(test_list2)
# print(diff_elements)

# --------------------------  prog_2 ---------------------------------------
"""
Find unique elements without set
"""
# sample_list = [2,3,4,6,8]
# req_list = sample_list + [100]
# print(req_list)

"""
"""

# --------------prog 3 -->  Append List every Nth index --------------------------------
""" Input : test_list = [3, 7, 8, 2, 1, 5, 8], app_list = [‘G’, ‘F’, ‘G’], N = 3
Output : [‘G’, ‘F’, ‘G’, 3, 7, 8, ‘G’, ‘F’, ‘G’, 2, 1, 5, ‘G’, ‘F’, ‘G’, 8]  """

test_list = [3, 7, 8, 2, 1, 5, 8]
app_list = ['G','F','G']
N = 3
res_list = []

for i,ele in enumerate(test_list):
    if i%N == 0:
        res_list.extend(app_list)

    else:
        res_list.append(ele)

print(res_list)

# prog3 --> appending a string vs extending a string
list_1 = [3,4,5,6]
sample_str = "India"
list_1.append(sample_str)  # [3, 4, 5, 6, 'India']
print(list_1)
list_1.extend(sample_str)  # [3, 4, 5, 6, 'India', 'I', 'n', 'd', 'i', 'a']
print(list_1)

# string pallindrome
input_string = "India is my country"
reverse_string = input_string[::-1]
print(reverse_string)
reverse_char = ""
for char in input_string:
    reverse_char = char+reverse_char
print(reverse_char)







