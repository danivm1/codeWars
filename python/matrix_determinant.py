# https://www.codewars.com/kata/52a382ee44408cea2500074c

import numpy as np

def det_2(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

def det_general(mat):
    length = len(mat[0])

    if length < 3:
        return det_2(mat) 

    for i in range(length):
        matrix = np.copy(mat)
        matrix = np.delete(matrix, 0, 0)
        matrix = np.delete(matrix, i, 1)
        minor_det = det_general(matrix)
        mat[0][i] *= minor_det
    
    det = 0

    for i in range(length):
        det += mat[0][i] if i % 2 == 0 else -(mat[0][i])
    
    return det 

def determinant(mat):
    n = len(mat[0])

    if n < 1:
        return

    if n == 1:
        return mat[0][0]

    if n > 1:
        return det_general(mat)