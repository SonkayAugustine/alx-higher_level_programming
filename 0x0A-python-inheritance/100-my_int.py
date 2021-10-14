#!/usr/bin/python3
'''
Task 12 (100) Module
'''


class MyInt(int):
    '''
    class that inherits from int
    '''
    def __eq__(self, other):
        '''
        Compares for inequality
        '''
        return super().__ne__(other)

    def __ne__(self, other):
        '''
        Compares for equality
        '''
        return super().__eq__(other)
