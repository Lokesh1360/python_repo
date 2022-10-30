input_length = int(input("Enter number upto which prime to be printed: "))

for num in range(2,input_length):
    prime = True
    for i in range(2,num//2):
        if num%i == 0:
            prime = False
    if prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
