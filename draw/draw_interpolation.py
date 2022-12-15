import matplotlib.pyplot as plt
import interpolation_methods.linear_interpolation_and_extrapolation as li
import interpolation_methods.piecewise_linear_interpolation as pli
import interpolation_methods.lagrange_polynomial as lp
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np
import matrix.matrix as mx


def draw_grid(fig, ax, title):
    ax.set_title(f"{title}", fontsize=16)
    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("y", fontsize=14)
    ax.grid(which="major", linewidth=1.2)
    ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=5, width=1)


def draw_graph_interpolation(title, coefficients, point1, point2, data_x, data_y):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)
    x = [point1[0], point2[0]]
    y = [point1[1], point2[1]]

    ax.plot(x, y, label=f"y = {coefficients[0]} * x + {coefficients[1]}")
    ax.scatter(data_x, data_y, c="red")
    ax.legend()

    plt.show()


def draw_graph_pl_interpolation(title, data_xy, data_x, data_y):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)
    x_in_segments = mx.get_col_by_idex(data_xy, 0)
    y_in_segments = mx.get_col_by_idex(data_xy, 1)

    ax.plot(x_in_segments, y_in_segments)
    ax.scatter(data_x, data_y, c="red")
    ax.legend()

    plt.show()


def draw_graph_langrange(title, data_xy):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)

    data_x = np.arange(1, 7, 0.05)
    data_y = []
    for element in data_x:
        data_y.append(lp.lagrange_polynomial(data_xy, element))

    x_in_segments = mx.get_col_by_idex(data_xy, 0)
    y_in_segments = mx.get_col_by_idex(data_xy, 1)

    ax.plot(data_x, data_y)
    ax.scatter(x_in_segments, y_in_segments, c="red")
    ax.legend()

    plt.show()


def test_draw_interpolation():
    point1 = [2, 5]
    point2 = [6, 9]
    data_x = [0, 4, 20]
    coefficients = li.get_a_b(point1, point2)
    data_y = li.interpolation(point1, point2, data_x)
    draw_graph_interpolation("Уравнение линии", coefficients, point1, point2, data_x, data_y)


def test_draw_pl_interpolation():
    data_xy = [[1, 2],
             [3, 4],
             [3.5, 3],
             [6, 7]]
    data_x = [-1.5, 3, 2, 5, 9]
    data_y = pli.piecewise_linear_interpolation(data_xy, data_x)
    draw_graph_pl_interpolation("Кусочно-линейная интерполяция", data_xy, data_x, data_y)


def test_draw_langrange():
    data_xy = [[1, 2],
               [3, 4],
               [3.5, 3],
               [6, 7]]
    draw_graph_langrange("Полином Лагранжа", data_xy)
