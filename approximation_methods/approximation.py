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


def get_a(data_xy):
    a_matrix = []
    for i in range(len(data_xy)):
        a_matrix.append([data_xy[i][0], 1])
    return a_matrix


def get_b(data_xy):
    b_matrix = []
    for i in range(len(data_xy)):
        b_matrix.append([data_xy[i][1]])
    return b_matrix

def get_coef(data_xy):
    a_matrix = get_a(data_xy)
    # b = mx.get_col_by_idex(data_xy, 1)
    b = get_b(data_xy)
    transposed_matrix = mx.transposition(a_matrix)
    a_tilda = mx.multiply(transposed_matrix, a_matrix)
    b_tilda = mx.multiply(transposed_matrix, b)
    b_tilda = [i[0] for i in b_tilda]
    x = gj.main(a_tilda, b_tilda)
    return x


def get_function_values(data_x, x):
    a_matrix = []
    for i in range(len(data_x)):
        a_matrix.append([data_x[i], 1])

    y = mx.multiply(a_matrix, x)
    return y


def linear_approximation(data_xy, data_x):
    x = get_coef(data_xy)
    x = [[i] for i in x]
    y = get_function_values(data_x, x)
    y = [i[0] for i in y]
    return y
