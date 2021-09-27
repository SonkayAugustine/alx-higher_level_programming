#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = []
    for row in matrix:
        row = list(map(lambda x: x**2, row))
        sqr_matrix.append(row)
    return sqr_matrix
