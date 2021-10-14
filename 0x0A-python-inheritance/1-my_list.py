#!/usr/bin/python3
'''
task 1 module
'''


class MyList(list):
    '''
    class MyList
    New class that inherits from list
    '''

    def print_sorted(self):
        '''Print sort list'''
        sorted_list = sorted(self)
        print(sorted_list)
