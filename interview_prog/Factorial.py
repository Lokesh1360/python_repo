def fact(num):
    if num == 1:
        return 1

    else:
        num = num*fact(num-1)

    return num

input_num = int(input("Enter number to find factorial: "))
print(fact(input_num))