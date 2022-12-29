import matrix.matrix as mx
from add_func import *
import vector.vectors as vc
import gauss_jordan_method.gauss_jordan as gj


def get_partial_derivative(m, variable):
    for i in range(len(m)):
        vc.multiply_by_value(m[i], m[i][variable])
    derivative = [0 for _ in range(len(m[0]))]
    for i in range(len(m)):
        derivative = vc.addition(derivative, m[i])
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
        m = [row[:] for row in matrix]
        derivative = get_partial_derivative(m, i)
        derivatives.append(derivative)
    return derivatives


def get_b(data_xy):
    b_matrix = []
    for i in range(len(data_xy)):
        b_matrix.append([data_xy[i][1]])
    return b_matrix


def get_tilda(transposed_matrix, a_matrix, b):
    a_tilda = mx.multiply(transposed_matrix, a_matrix)
    b_tilda = mx.multiply(transposed_matrix, b)
    b_tilda = [i[0] for i in b_tilda]
    return a_tilda, b_tilda


def get_coef_linear(data_xy):
    a_matrix = []
    for i in range(len(data_xy)):
        a_matrix.append([data_xy[i][0], 1])
    b = get_b(data_xy)
    transposed_matrix = mx.transposition(a_matrix)
    a_tilda, b_tilda = get_tilda(transposed_matrix, a_matrix, b)
    x = gj.main(a_tilda, b_tilda)
    return x


def get_coef_second(data_xy):
    b = get_b(data_xy)
    a_matrix = []
    for i in range(len(data_xy)):
        x = data_xy[i][0]
        a_matrix.append([x * x, x, 1])
    transposed_matrix = mx.transposition(a_matrix)
    a_tilda, b_tilda = get_tilda(transposed_matrix, a_matrix, b)
    x = gj.main(a_tilda, b_tilda)
    return x


def get_coef_third(data_xy):
    b = get_b(data_xy)
    a_matrix = []
    for i in range(len(data_xy)):
        x = data_xy[i][0]
        a_matrix.append([x * x * x, x * x, x, 1])
    transposed_matrix = mx.transposition(a_matrix)
    a_tilda, b_tilda = get_tilda(transposed_matrix, a_matrix, b)
    x = gj.main(a_tilda, b_tilda)
    return x


def get_function_values_linear(data_x, x):
    a_matrix = []
    for i in range(len(data_x)):
        a_matrix.append([data_x[i], 1])

    y = mx.multiply(a_matrix, x)
    return y


def get_function_values_second(data_x, k):
    a_matrix = []
    for i in range(len(data_x)):
        x = data_x[i]
        a_matrix.append([x * x, x, 1])
    y = mx.multiply(a_matrix, k)
    return y


def get_function_values_third(data_x, k):
    a_matrix = []
    for i in range(len(data_x)):
        x = data_x[i]
        a_matrix.append([x * x * x, x * x, x, 1])
    y = mx.multiply(a_matrix, k)
    return y


def least_squares(matrix, res):
    vc.multiply_by_value(res, -1)
    expanded_matrix = get_expanded_matrix(matrix, res)

    derivatives = get_derivatives(expanded_matrix)

    roots = get_roots(derivatives)

    return roots


def linear_approximation(data_xy, data_x):
    x = get_coef_linear(data_xy)
    x = [[i] for i in x]
    y = get_function_values_linear(data_x, x)
    y = [i[0] for i in y]
    return y


def second_degree_polynomial(data_xy, data_x):
    x = get_coef_second(data_xy)
    x = [[i] for i in x]
    y = get_function_values_second(data_x, x)
    y = [i[0] for i in y]
    return y


def third_degree_polynomial(data_xy, data_x):
    x = get_coef_third(data_xy)
    x = [[i] for i in x]
    y = get_function_values_third(data_x, x)
    y = [i[0] for i in y]
    print(y)
    return y
