import matrix.matrix as mx


def test_addition():
    """Тест сложения матриц"""
    assert mx.addition([[1, 2], [3, 4]], [[3, 4], [1, 1]]) == [[4, 6], [4, 5]], "Should be [[4, 6], [4, 5]]"


def test_addition2():
    """Тест сложения матриц"""
    assert mx.addition([[1, 2]], [[3, 4], [1, 1]]) == [], "Should be []"


def test_difference():
    """Тест вычитания матриц"""
    assert mx.difference([[1, 2]], [[3, 4], [1, 1]]) == [], "Should be []"


def test_difference2():
    """Тест вычитания матриц"""
    assert mx.difference([[1, 2], [3, 4]], [[3, 4], [1, 1]]) == [[-2, -2], [2, 3]], "Should be [[-2, -2], [2, 3]]"


def test_transposition():
    """Тест транспонирование матриц"""
    assert mx.transposition([[2, 3, 5], [5, 7, 6]]) == [[2, 5], [3, 7], [5, 6]], "Should be [[2, 5], [3, 7], [5, 6]]"


def test_transposition2():
    """Тест транспонирование матриц"""
    assert mx.transposition([[2, 3, 5], [5, 7]]) == [], "Should be []"


def test_multiply_by_value():
    """Тест умножение матрицы на скаляр"""
    assert mx.multiply_by_value([[2, 3, 5], [5, 7, 6]], 5) == [[10, 15, 25],
                                                               [25, 35, 30]], "Should be [[10, 15, 25], [25, 35, 30]]"


def test_multiply_by_value2():
    """Тест умножение матрицы на скаляр"""
    assert mx.multiply_by_value([[2, 3, 5], [5, 7]], 5) == None, "Should be None"


def test_multiply_by_value3():
    """Тест умножение матрицы на скаляр"""
    assert mx.multiply_by_value([[2, 3, 5], [5, 7, 6]], 0) == [[0, 0, 0], [0, 0, 0]], "Should be [[0, 0, 0], [0, 0, 0]]"


def test_multiply():
    """Тест умножение матрицы на скаляр"""
    assert mx.multiply([[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10]]) == [[25, 28], [57, 64], [89,
                                                                                             100]], "Should be [[25, 28], [57, 64], [89, 100]]"


def test_multiply2():
    """Тест умножение матрицы на скаляр"""
    assert mx.multiply([[1], [3, 4], [5, 6]], [[7, 8], [9, 10]]) == None


def test_get_row_by_index():
    """Тест получить строку по индексу"""
    assert mx.get_row_by_index([[1, 2], [3, 4], [5, 6]], 0) == [1, 2]


def test_get_row_by_index():
    """Тест получить строку по индексу"""
    assert mx.get_row_by_index([[1, 2], [3, 4], [5, 6]], 3) == None


def test_get_col_by_idex():
    """Тест получить столбец по индексу"""
    assert mx.get_col_by_idex([[1, 2], [3, 4], [5, 6]], 0) == [1, 3, 5]


def test_get_col_by_idex2():
    """Тест получить столбец по индексу"""
    assert mx.get_col_by_idex([[1, 2], [3, 4], [5, 6]], 2) == None


def test_swap_row():
    """Тест поменять местами строки"""
    assert mx.swap_row([[1, 2], [3, 4], [5, 6]], 0, 1) == [[3, 4], [1, 2], [5, 6]]


def test_multiply_row_by_value():
    """Тест умножить строку на скаляр"""
    assert mx.multiply_row_by_value([[1, 2], [3, 4], [5, 6]], 0, 5) == [[5, 10], [3, 4], [5, 6]]


def test_addition_mul_row():
    """Тест сложение строк матрицы с индексами х + у, умноженную на скаляр"""
    assert mx.addition_mul_row([[1, 2], [3, 4], [5, 6]], 0, 1, 2) == [[7, 10], [3, 4], [5, 6]]


def test_difference_mul_row():
    """Тест вычитание строк матрицы с индексами х + у, умноженную на скаляр"""
    assert mx.difference_mul_row([[1, 2], [3, 4], [5, 6]], 0, 1, 2) == [[-5, -6], [3, 4], [5, 6]]
