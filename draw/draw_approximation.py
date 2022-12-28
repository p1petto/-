from draw.draw_interpolation import draw_grid
import matplotlib.pyplot as plt
import approximation_methods.approximation as apx
import numpy as np
import matrix.matrix as mx
import vector.vectors as vc
from add_func import *


def draw_least_squares(title, matrix, res):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    xr = apx.least_squares(matrix, res)
    yr = get_y(matrix, res, xr[0])

    data_x = np.arange(0, 5, 0.05)
    data_y = []
    for element in data_x:
        data_y.append(get_y(matrix, res, element))

    ax.plot(data_x, data_y)
    ax.scatter(xr, yr, c="red")
    ax.legend()

    plt.show()


def get_quadratic_equation(matrix, res):
    vc.multiply_by_value(res, -1)
    expanded_matrix = get_expanded_matrix(matrix, res)
    x2 = []
    x = []
    k = []
    for line in expanded_matrix:
        x2.append(line[0] ** 2)
        x.append(2 * line[0] * line[1])
        k.append(line[1] ** 2)

    e = [sum(x2), sum(x), sum(k)]
    return e


def get_y(matrix, res, x):
    e = get_quadratic_equation(matrix, res)
    return (x ** 2) * e[0] + x * e[1] + e[2]


def draw_linear_approximation(title, data_xy, data_xr):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    x_array = [-1, 7]
    y_array = apx.linear_approximation(data_xy, x_array)

    xr = mx.get_col_by_idex(data_xy, 0)
    yr = mx.get_col_by_idex(data_xy, 1)

    data_yr = apx.linear_approximation(data_xy, data_xr)

    ax.plot(x_array, y_array)
    ax.scatter(xr, yr, c="blue")
    ax.scatter(data_xr, data_yr, c="red")
    ax.legend()

    plt.show()


def draw_second_degree_polynomial(title, data_xy, data_xr):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    x_array = np.arange(-5, 7, 0.05)
    y_array = apx.second_degree_polynomial(data_xy, x_array)
    print(y_array)

    xr = mx.get_col_by_idex(data_xy, 0)
    yr = mx.get_col_by_idex(data_xy, 1)

    data_yr = apx.second_degree_polynomial(data_xy, data_xr)

    ax.plot(x_array, y_array)
    ax.scatter(xr, yr, c="blue")
    ax.scatter(data_xr, data_yr, c="red")
    ax.legend()

    plt.show()


def draw_third_degree_polynomial(title, data_xy, data_xr):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    x_array = np.arange(0, 7, 0.05)
    y_array = apx.third_degree_polynomial(data_xy, x_array)
    print(y_array)

    xr = mx.get_col_by_idex(data_xy, 0)
    yr = mx.get_col_by_idex(data_xy, 1)

    data_yr = apx.third_degree_polynomial(data_xy, data_xr)

    ax.plot(x_array, y_array)
    ax.scatter(xr, yr, c="blue")
    ax.scatter(data_xr, data_yr, c="red")
    ax.legend()

    plt.show()


def test_draw_least_squares():
    draw_least_squares("Метод наименьших квадратов", [[2], [3]], [4, 9])


def test_draw_linear_approximation():
    draw_linear_approximation("Линейная аппроксимация", [[1, 2], [3, 4], [3.5, 3], [6, 7]], [1, 3, 5])


def test_draw_second_degree_polynomial():
    draw_second_degree_polynomial("Аппроксимация полиномом 2-й степени", [[1, 2], [3, 4], [3.5, 3], [6, 7]], [1, 3, 5])


def test_draw_third_degree_polynomial():
    draw_third_degree_polynomial("Аппроксимация полиномом 3-й степени", [[1, 2], [3, 4], [3.5, 3], [6, 7]], [1, 3, 5])
