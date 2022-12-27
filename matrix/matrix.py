from add_func import *
import vector.vectors as vc


def addition(a, b):
    m_a = []
    if is_same_size(a, b):
        for i in range(len(a)):
            m_a.append(vc.addition(a[i], b[i]))

    return m_a


def difference(a, b):
    """вычитание"""
    m_a = []
    if is_same_size(a, b):
        for i in range(len(a)):
            m_a.append(vc.difference(a[i], b[i]))

    return m_a


def transposition(m):
    "Транспонирование"
    t_m = []
    if is_matrix(m):
        t_m = [[0 for j in range(len(m))] for i in range(len(m[0]))]
        for i in range(len(m)):
            for j in range(len(m[0])):
                t_m[j][i] = m[i][j]

    return t_m


def multiply_by_value(m, val):
    """умножение на скаляр"""
    if is_matrix(m):
        for i in range(len(m)):
            vc.multiply_by_value(m[i], val)

        return m


def multiply(a, b):
    """умножение"""
    if is_matrix(a) and is_matrix(b):
        res = [[0 for j in range(len(b[0]))] for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    res[i][j] += a[i][k] * b[k][j]
        return res


def get_row_by_index(a, idx):
    """Получить строку"""
    if is_matrix(a):
        if idx < len(a) and idx >= 0:
            return a[idx]


def get_col_by_idex(a, idx):
    """Получить столбец"""
    if is_matrix(a):
        t_a = transposition(a)
        if idx < len(t_a) and idx >= 0:
            return get_row_by_index(t_a, idx)


def swap_row(a, x, y):
    """Поменять строки местами"""
    if is_matrix(a):
        if x < len(a) and x >= 0 and y < len(a) and y >= 0:
            temp = a[x]
            a[x] = a[y]
            a[y] = temp
            return a


def multiply_row_by_value(a, idx, val):
    """Умножить строку на скаляр"""
    if is_matrix(a):
        if idx < len(a) and idx >= 0:
            a[idx] = vc.multiply_by_value(a[idx], val)
            return a


def addition_mul_row(a, x, y, val):
    """сложение строки матрицы с индексом х на строку с индексом у, умноженную на скаляр"""
    if is_matrix(a):
        if x < len(a) and x >= 0 and y < len(a) and y >= 0:
            temp = vc.multiply_by_value(a[y].copy(), val)
            a[x] = vc.addition(a[x], temp)
            return a


def difference_mul_row(a, x, y, val):
    """вычитание строки матрицы с индексом х на строку с индексом у, умноженную на скаляр"""
    if is_matrix(a):
        if x < len(a) and x >= 0 and y < len(a) and y >= 0:
            temp = vc.multiply_by_value(a[y].copy(), val)
            a[x] = vc.difference(a[x], temp)
            return a


def matrix_copy(matrix):
    return [elem[:] for elem in matrix]