from draw.draw_interpolation import draw_grid
import matplotlib.pyplot as plt
import  approximation_methods.approximation as apx
import interpolation_methods.linear_interpolation_and_extrapolation as li
import interpolation_methods.piecewise_linear_interpolation as pli
import interpolation_methods.lagrange_polynomial as lp
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np
import matrix.matrix as mx
import interpolation_methods.linear_interpolation_and_extrapolation as mx
import vector.vectors as vc
from add_func import *


def test_draw_least_squares():
    draw_least_squares("Метод наименьших квадратов", [[2],[3]], [4, 9])


def draw_least_squares(title, matrix, res):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    xr = apx.least_squares(matrix,res)
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


