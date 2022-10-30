
with open("data,txt","r") as d:
    input_data = d.read()
    print(input_data)
    for line in input_data:
        print(line.strip())