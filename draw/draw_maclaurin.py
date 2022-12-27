import matplotlib.pyplot as plt
import maclaurin.maclaurin_row as mr
from draw.draw_interpolation import draw_grid


def test_draw_maclaurin_function1():
    draw_maclaurin_row("Реализация разложения в ряд Маклорена e", mr.get_maclaurin_e, (-10, 10), 2)


def test_draw_maclaurin_function2():
    draw_maclaurin_row("Реализация разложения в ряд Маклорена sin", mr.get_maclaurin_sin, (-10, 10), 2)


def test_draw_maclaurin_function3():
    draw_maclaurin_row("Реализация разложения в ряд Маклорена cos", mr.get_maclaurin_cos, (-10, 10), 2)


def test_draw_maclaurin_function4():
    draw_maclaurin_row("Реализация разложения в ряд Маклорена arcsin", mr.get_maclaurin_arcsin, (-10, 10), 2)


def test_draw_maclaurin_function5():
    draw_maclaurin_row("Реализация разложения в ряд Маклорена arccos", mr.get_maclaurin_arccos, (-10, 10), 2)


def draw_maclaurin_row(title, func, x_range, n):
    fig, ax = plt.subplots(figsize=(8, 6))
    draw_grid(fig, ax, title)
    data_x = mr.get_data_x(x_range, n, func)
    data_y = []
    for x in range(x_range[0], x_range[1]):
        data_y.append(x)
    ax.plot(data_y, data_x)
    ax.legend()

    plt.show()

