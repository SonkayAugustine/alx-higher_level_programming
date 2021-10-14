#!/usr/bin/python3
'''
Task 8 Module
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    rectanlge class
    '''
    def __init(self, width, height):
        '''Init of obj'''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
