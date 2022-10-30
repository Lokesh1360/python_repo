import re
input = "mississippi"
# output = "misp"
output_list = []
for char in input:
    if char not in output_list:
        output_list.append(char)

output_unique = "".join(output_list)
print(output_unique)


# input = [1,2,3,4,4,5,5,6,1]

# sort list without using built-in

input_string = "1w3e4r5t6y7u7i8i"
# output = only number
pattern = re.compile("[0-9]")
match = re.findall(pattern,input_string)
print(match)
output_number = "".join(match)
print(int(output_number))



