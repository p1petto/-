import matrix.matrix as mx


def lagrange_polynomial(data_xy, x):
    data_x = mx.get_col_by_idex(data_xy, 0)
    data_y = mx.get_col_by_idex(data_xy, 1)
    n = len(data_x) - 1
    polynomial = 0

    for i in range(n + 1):
        basis_polynomial = 1
        for j in range(n + 1):
            if i == j:
                continue
            basis_polynomial *= (x - data_x[j]) / (data_x[i] - data_x[j])
        polynomial += data_y[i] * basis_polynomial
    return polynomial
