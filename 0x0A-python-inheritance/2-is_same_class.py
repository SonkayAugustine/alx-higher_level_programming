#!/usr/bin/python3
'''
Task 2 module
'''


def is_same_class(obj, a_class):
    '''
    A function that returns True if the obj is exactly an instance of the specified class; Otherwise False
    '''
    return type(obj) is a_class
