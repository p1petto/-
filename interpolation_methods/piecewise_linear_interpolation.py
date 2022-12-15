import interpolation_methods.linear_interpolation_and_extrapolation as li
import matrix.matrix as mx


def get_diapason(x, data_x):
    if x <= data_x[1]:
        return 0
    elif x >= data_x[len(data_x) - 1]:
        return len(data_x) - 2
    else:
        for j in range(2, len(data_x)):
            if data_x[j - 1] <= x <= data_x[j]:
                return j - 1


def piecewise_linear_interpolation(data_xy, data_x):
    roots = []
    y_aray = []
    for i in range(len(data_xy) - 1):
        roots.append(li.get_a_b(data_xy[i], data_xy[i + 1]))

    x_in_segments = mx.get_col_by_idex(data_xy, 0)

    for x in data_x:
        diapason = get_diapason(x, x_in_segments)
        y_aray.append(li.get_y(roots[diapason], x))

    return y_aray



