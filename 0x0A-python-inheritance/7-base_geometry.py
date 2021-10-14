#!/usr/bin/python3
'''
Task 7 Module
'''


class BaseGeometry():
    '''
    class BaseGeometry
    '''
    def area(self):
        '''
        Calculates the area
        '''
        raise Exceptions('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Validates the integer passed to the function
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            riase ValueError("{} must be gretaer than 0".format(name))
