# Improvement 2 -->get Data using OS command; write data into a file and then read data from file to perform parsing.
# Improvement   --> using mkdir, create folder to store data file
# lstrip()
# shift_tab
# r'{}'.format(s)

sample_dict = {}
with open(r"D:\Python_developing\pythonProject\interview_prog\data\data.txt","r") as f:
    input_data = f.readlines()
    # print(input_data)

for row in input_data:
    process_data = row.split(sep=":")
    # sample_dict[process_data[0]] = process_data[1].lstrip()
    sample_dict[r'{}'.format(process_data[0])] = r'{}'.format(process_data[1].lstrip())

print("before parsing",sample_dict)

for key,value in sample_dict.items():
    # sample_dict[key].replace('\t',"")
    sample_dict[key].replace(r'\n',"")
    sample_dict[key].replace(r'\t',"")

print("after parsing",sample_dict)

# sample_dict[process_data[0]].replace('\n',"")
# sample_dict[process_data[0]].replace('\t',"")
# sample_dict[process_data[1]].replace('\n',"")
# sample_dict[process_data[1]].replace('\t',"")
# print("after parsing",sample_dict)





    # for line in input_data:
    #     print(line.strip())