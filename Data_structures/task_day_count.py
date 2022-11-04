"""
Result: 1663 days
It is 1663 days from the start date to the end date, but not including the end date.

Or 4 years, 6 months, 19 days excluding the end date.

Or 54 months, 19 days excluding the end date.

"""

def leap_year(start_year,end_year):
    count = 0
    for year in range(start_year,end_year+1):
        if year % 4 == 0:
            count += 1
            print(count)
        return count



input_1 = "19/10/1993"
input_2 = "31/03/1989"

input_list_1 = input_1.split(sep="/")
input_list_2 = input_2.split(sep="/")
print(input_list_1)
print(input_list_2)

years = int(input_list_1[-1]) - int(input_list_2[-1])
months = int(input_list_1[-2]) - int(input_list_2[-2])
days = int(input_list_1[0]) - int(input_list_2[0])
leap_days = leap_year(int(input_list_1[-1]),int(input_list_2[-1]))

total_days = (days) + (30*months) + (365*years) + leap_days

print(total_days)

