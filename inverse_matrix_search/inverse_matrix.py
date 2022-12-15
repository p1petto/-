import gauss_jordan_method.gauss_jordan as gj
from add_func import *


def get_identity_matrix(n):
    matrix = [[0 for i in range(0, n)] for j in range(0, n)]
    for i in range(len(matrix)):
        matrix[i][i] = 1
    return matrix


def get_expanded_matrix(matrix):
    identity_matrix = get_identity_matrix(len(matrix))
    for i in range(len(matrix)):
        matrix = gj.get_expanded_matrix(matrix, identity_matrix[i])
    return matrix


def inverse(matrix):
    expanded_matrix = get_expanded_matrix(matrix)
    expanded_matrix = gj.forward_trace(len(matrix), expanded_matrix)
    expanded_matrix = gj.backward_trace(len(matrix), expanded_matrix)
    inverse_matrix = []
    print(expanded_matrix)
    for i in range(len(matrix)):
        inverse_matrix.append(expanded_matrix[i][len(matrix):])

    return inverse_matrix


def get_root(matrix, res):
    matrix = inverse(matrix)
    roots = []
    for row in matrix:
        temp = 0
        for j in range(len(matrix[0])):
            temp += res[j] * row[j]
        roots.append(temp)
    return roots
