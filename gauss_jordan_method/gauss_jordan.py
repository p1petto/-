from add_func import *
import matrix.matrix as mx
import numpy as np


def forward_trace(n, matrix):
    for i in range(n):
        idx_swap_row = get_nonzero_idx(matrix, i)

        if idx_swap_row != i:
            mx.swap_row(matrix, i, idx_swap_row)

        if matrix[i][i] != 1:
            mx.multiply_row_by_value(matrix, i, 1 / matrix[i][i])

        for row in range(i + 1, n):
            mx.difference_mul_row(matrix, row, i, matrix[row][i])

    return matrix


def backward_trace(n, matrix):
    for i in range(n - 1, 0, -1):
        for row in range(i - 1, -1, -1):
            if matrix[row][i] != 0:
                mx.difference_mul_row(matrix, row, i, matrix[row][i])
    return matrix


def main(matrix, res):
    expanded_matrix = get_expanded_matrix(matrix, res)
    # print('\nРасширенная матрица\n', np.array(expanded_matrix))

    expanded_matrix = forward_trace(len(matrix), expanded_matrix)
    # print('\nПрямой ход\n', np.array(expanded_matrix))

    expanded_matrix = backward_trace(len(matrix), expanded_matrix)
    # print('\nОбратный ход\n', np.array(expanded_matrix))

    root = get_root(expanded_matrix)
    # print('\nКорни уравнения\n', root)
    return root
