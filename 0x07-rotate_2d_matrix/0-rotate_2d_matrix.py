#!/usr/bin/python3
"""
Rotate a 2D matrix in place
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2d matrix 90 degrees in-place
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # reverse  each row
            for i in range(n):
                matrix[i].reverse()
