#!/usr/bin/python3
"""
task module: 12-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing Pascal's triangle
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]

    this_row = []
    triangle = [[1], [1, 1]]

    for row in range(2, n):
        this_row = [1]
        for column in range(1, row):
            element = triangle[row - 1][column - 1] + triangle[row - 1][column]
            this_row.append(element)
            this_row.append(1)
            triangle.append(this_row)
    return triangle
