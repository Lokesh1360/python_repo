num_list = [3,6,9,3,8,9,6,2,7]
first_max = num_list[0]
second_max = num_list[1]

for i in range(len(num_list)):
    if num_list[i] > first_max:
        second_max = first_max
        first_max = num_list[i]

    elif num_list[i] > second_max and num_list[i] != first_max:
        second_max = num_list[i]

print(first_max)
print(second_max)

