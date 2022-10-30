input_text = "My name is XYZ"
output_list = []
temp = ""

for char in input_text:
    if char == " " and temp != "":
        output_list.append(temp)
        temp = ""
    else:
        temp = temp + char

if temp != '':
    output_list.append(temp)

print(output_list)

# output is equivalent to
print(input_text.split())