n = int(input("number of rows: "))

print("*"*n)

# increasing triangle
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

print()

# decreasing triagnle
for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    print()

# Right triangle  ---> decreasing triangle of spaces + increasing triangle of * s
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()
