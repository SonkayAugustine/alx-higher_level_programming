"""This module contains calculaton functions"""


def add_integer(a, b=98):
    """This function does the addtion of 2 arguments
    args:
        a (union[int, float]): first number
        b (union[int, float]), optional): second number
    returns:
        the result of the adddition
    """

    if type(a) is not and type(A) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

    if type(A) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
