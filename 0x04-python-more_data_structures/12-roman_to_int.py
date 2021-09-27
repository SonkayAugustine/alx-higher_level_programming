#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
       return 0
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rev_string = roman_string[::-1]
    result = roman_num[rev_string[0]]

    for i in range(len(rev_string) - 1):
       actual = roman_num[rev_string[i]]
       before = roman_num[rev_string[i + 1]]
       if before >= actual:
          result += before
       else:
          result -= before
    return result
