#!/usr/bin/python3
'''
Task 0 module
'''


def lookup(obj):
    '''
    A function that returns the list of available attribute and methods of an object
    '''
    '''
    Args:
         obj: Object
    Return:
         list with method and attributes
    '''
    obj_namespace = dir(obj)

    return obj_namespace
