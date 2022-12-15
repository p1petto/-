import gauss_jordan_method.gauss_jordan as gj


def get_a_b(point_1, point_2):
    matrix = [[point_1[0], 1],
              [point_2[0], 1]]
    roots = gj.main(matrix, [point_1[1], point_2[1]])
    return roots


def get_y(roots, x):
    a, b = roots
    y = x * a + b
    return y


def interpolation(point1, point2, x_array):
    roots = get_a_b(point1, point2)
    y_aray = []
    for x in x_array:
        y_aray.append(get_y(roots, x))
    return y_aray
