#!/usr/bin/python3
'''
Task 10 Module
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    classy class
    '''
    def __init__(self, size):
        '''
        intialization of sqaure
        '''
        super().integer_validator('size', size)
        self.__size = size
        
    def area(self):
        ''' get that number'''
        return self.__size ** 2
