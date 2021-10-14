#!/usr/bin/python3
'''
Task 4 Module
'''


def inherits_from(obj, a_class):
    '''
    checks if an object is an instance of, or inherited from a class
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
