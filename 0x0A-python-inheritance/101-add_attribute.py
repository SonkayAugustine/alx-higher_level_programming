#!/usr/bin/python3
'''
Task 13 (101) Module
'''


def add_attirbute(obj, name, value):
    '''
    Check if it is possible to add an attr to class
    '''
    if '__dict__' not in dir(obj):
       object.__dict__[name] = value
    else:
        raise TypeError("cant't add new attribute")
