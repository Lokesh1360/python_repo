import re
import sys

"""
Your task is to write a regular expression that matches only and exactly strings of form:
123.456.abc.def
1123.456.abc.def
123.123.123.132.123.123
"""

# regex_pattern = r"...\....\....\...."	# Do not delete 'r'.
# #input("Enter input string: ")
# test_string = "123.123.123.132.123.123"
#
# match = re.match(regex_pattern, test_string) is not None
#
# print(str(match).lower())

# -----------------------------
# Print char in string except vowels using reg ex
input_string = "Hello World"
test_string = input_string.lower()
pattern = r'[^aeiouAEIOU]'

match = re.findall(pattern,test_string)
print(match)
