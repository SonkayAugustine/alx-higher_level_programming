#!/usr/bin/python3
'''Task 8 module'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle class'''
    def ___init__(self, width, height):
        '''
        Iniit of the obj
        '''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
