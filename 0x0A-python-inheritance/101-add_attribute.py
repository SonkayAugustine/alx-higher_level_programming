#!/usr/bin/python3
'''
Task 13 (101) Module
'''


def add_attirbute(obj, name, value):
    '''
    Check if it is possible to add an attribute to a class
    and then if yes add it
    '''
    if '__dict__' not in dir(obj):
        raise TypeError("cant't add new attribute")

        setattr(obj, name, value)
