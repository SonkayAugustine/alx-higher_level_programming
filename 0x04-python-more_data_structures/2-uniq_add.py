#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_num = set(my_list)
    sum = 0
    for i in unique_num:
        sum += i
    return sum
