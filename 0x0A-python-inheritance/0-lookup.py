#!/usr/bin/python3
'''
Task 0 module
'''


def lookup(obj):
    '''
    A list of available attr and methods of an object
    '''
    obj_namespace = dir(obj)

    return obj_namespace
