#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in range(0, (len(matrix))):
        matrixTemp = list(map(lambda x: x*x, matrix[i]))
        matrix2.insert(i, matrixTemp)
    return matrix2
