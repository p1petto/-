import matrix.matrix as mx
from add_func import *
import vector.vectors as vc
import gauss_jordan_method.gauss_jordan as gj


def get_partial_derivative(mx, variable):
    for i in range(len(mx)):
        vc.multiply_by_value(mx[i], mx[i][variable])
    derivative = [0 for i in range(len(mx[0]))]
    for i in range(len(mx)):
        derivative = vc.addition(derivative, mx[i])
    return derivative


def get_roots(derivatives):
    matrix = mx.matrix_copy(derivatives)
    right_part = mx.get_col_by_idex(matrix, len(matrix[0]) - 1)
    right_part = vc.multiply_by_value(right_part, -1)
    for i in matrix:
        i.pop(len(i) - 1)
    root = gj.main(matrix, right_part)
    return root


def get_derivatives(matrix):
    derivatives = []
    for i in range(len(matrix[0]) - 1):
        mx = [row[:] for row in matrix]
        derivative = get_partial_derivative(mx, i)
        derivatives.append(derivative)
    return derivatives


def least_squares(matrix, res):
    vc.multiply_by_value(res, -1)
    expanded_matrix = get_expanded_matrix(matrix, res)

    derivatives = get_derivatives(expanded_matrix)

    roots = get_roots(derivatives)

    return roots

