from add_func import *


def addition(a, b):
    """сложение"""
    res = []
    if is_same_size(a, b):
        for i in range(len(a)):
            res.append(a[i] + b[i])

    return res


def difference(a, b):
    """вычитание"""
    res = []
    if is_same_size(a, b):
        for i in range(len(a)):
            res.append(a[i] - b[i])

    return res


def multiply_by_value(arr, val):
    """умножение на скаляр"""
    for i in range(len(arr)):
        arr[i] *= val
    return (arr)


def division_by_value(arr, val):
    """деление на скаляр"""
    try:
        for i in range(len(arr)):
            arr[i] /= val
        return (arr)
    except ZeroDivisionError:
        "На 0 делить нельзя"


def multiply(a, b):
    """скалярное произведение"""
    res = 0.0

    if is_same_size(a, b):
        for i in range(len(a)):
            res += a[i] * b[i]
        return (res)


def are_collinear(a, b):
    """коллинеарность"""

    if (all(x == 0 for x in a) or
            all(x == 0 for x in b)):
        return True

    cos_vec = abs(get_cos(a, b))
    print(cos_vec)

    return is_scalar_almost_equal(cos_vec, 1)


def get_cos(a, b):
    """косинус"""
    if is_same_size(a, b):

        len1 = get_len_vec(a)
        len2 = get_len_vec(b)

        cos_vec = (multiply(a, b) / (len1 * len2))

        return cos_vec


def are_codirectional(a, b):
    """сонаправленность"""
    if all(x == 0 for x in a) or all(x == 0 for x in b):
        return True

    cos_vec = get_cos(a, b)

    return is_scalar_almost_equal(cos_vec, 1)


def are_oppositely_directed(a, b):
    """противоположнонаправленность"""

    if all(x == 0 for x in a) or all(x == 0 for x in b):
        return True

    cos_vec = get_cos(a, b)

    return is_scalar_almost_equal(cos_vec, -1)


def are_vector_equal(a, b):
    """равенство векторов"""
    if is_same_size(a, b):
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True


def is_vector_almost_equal(a, b, eps):
    """"Равенство с заданной точностью"""
    arr = [a,b]
    for i in range(len(arr[0])):
        if is_scalar_almost_equal(arr[0][i], arr[1][i], eps) == False:
            return False
    return True


def normalization(arr):
    """нормировка"""
    if (all(x == 0 for x in arr)):
        raise ValueError("Нормировать можно только ненулевые векторы")
    division_by_value(arr, get_len_vec(arr))
    return arr


def get_len_vec(arr):
    """Длина"""
    res = 0.0
    for i in arr:
        res += i ** 2
    res = abs(math.sqrt(res))
    a_e = math.ceil(res)
    if is_scalar_almost_equal(res, a_e, 0.2):
        return a_e
    else:
        return res


def change_direction(arr):
    """Изменить направление"""
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] *= -1
    return arr


def get_angle(a, b):
    """угол между векторами"""
    if is_same_size(a,b):
        cos_vec = get_cos(a, b)
        angle = math.degrees(math.acos(cos_vec))
        if is_scalar_almost_equal(math.degrees(math.acos(cos_vec)), 45):
            return 45.0
        return angle


def proj_a_to_b(a, b):
    """Проекция вектора на вектор"""
    proj = 0
    if is_same_size(a,b):
        if (is_scalar_almost_equal(get_cos(a,b), 0)):
            return 0

        proj = multiply(a,b) / get_len_vec(b)
        return proj
