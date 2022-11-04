
def temp_1():
    print("1 is entered")
    return 0

def temp_2():
    print("2 is entered")
    return 0

def temp_3():
    print("3 is entered")
    return 0

def temp_4():
    print("4 is entered")
    return 0

with open(r"C:\Users\shalini\OneDrive\Desktop\task_data_1.txt","r") as f:
    data = f.read()
    # print(data)
    str_data = str(data)
    process_data = str_data.split(sep="\n")
    print(process_data)

    for i in range(len(process_data)):
        if process_data[i] == "1":
            temp_1()

        elif process_data[i] == "2":
            temp_2()

        elif process_data[i] == "3":
            temp_3()

        elif process_data[i] == "4":
            temp_4()

        else:
            print("input data is out of range")