#!/usr/bin/python3
'''
Task 9 Module
'''


BaseGeometry = __import__('7-base_geomtry').BaseGeometry


class Rectangle(BaseGeomtry):
    '''rectangle class'''
    def __init__(self, width, height):
        '''
        Initialization of obj
        '''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''funny func'''
        return self.__height * self.__width

    def __str__(self):
        '''str func that fo it's job'''
        return f"[Rectanlge] {self.__width}/{self.__height}"
