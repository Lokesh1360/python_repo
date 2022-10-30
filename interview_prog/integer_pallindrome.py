input_num = int(input("Enter a number: "))
num = input_num
reverse_num = 0

while(num>0):
    digits = num%10
    reverse_num = reverse_num*10 + digits
    num = num//10

print(reverse_num)
if (reverse_num == input_num):
    print(f"{input_num} is pallindrome")

else:
    print(f"{input_num} is not pallindrome")
