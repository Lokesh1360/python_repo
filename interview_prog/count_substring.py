def count_substring(string,sub_string):
    l = len(sub_string)
    count = 0
    n = 0
    for element in string:
        if element == sub_string[0]:
            if string[n:n+l] == sub_string:
                count += 1
        n += 1
    return count

input_string = input("Enter string: ")
sub_string = input("Enter sub string to match: ")
print("number of substring matched:", count_substring(input_string,sub_string))

