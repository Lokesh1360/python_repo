input_text = input("Enter a string: ")
reverse_text = " "
# using slicing
print(f"reverse of {input_text} is '{input_text[::-1]}'")
print(input_text)

#using manual loop
for char in input_text:
    reverse_text = char + reverse_text

print(reverse_text)
