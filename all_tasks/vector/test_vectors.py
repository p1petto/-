import vector.vectors as vc


def check(is_passed, msg):
    if is_passed:
        print(msg + ' :PASSED')
    else:
        print(msg + ' :FAILED')


def test_addition():
    """Тест сложения векторов"""
    assert vc.addition([1, 2], [3, 4]) == [4, 6], "Should be [4, 6]"


def test_difference():
    """Тест вычитания векторов"""
    assert vc.difference([1, 2], [3, 4]) == [-2, -2], "Should be [-2, -2]"


def test_multiply_by_value():
    """Тест умножения векторов на скаляр"""
    assert vc.multiply_by_value([1, 2, 3], 2) == [2, 4, 6]


def test_division_by_value():
    """Тест деления векторов на скаляр"""
    assert vc.division_by_value([1, 2, 3, 4], 2) == [0.5, 1.0, 1.5, 2.0]


def test_division_by_value2():
    """Тест деления векторов на скаляр"""
    assert vc.division_by_value([1, 2, 3, 4], 0) == None


def test_multiply():
    """Тест скалярного произведения векторов"""
    assert vc.multiply([1, 2], [3, 4]) == 11.0, "Should be 11.0"


def test_multiply2():
    """Тест скалярного произведения векторов"""
    assert vc.multiply([1, 2], [3]) == None


def test_are_collinear():
    """Тест коллинеарности"""
    assert vc.are_collinear([1, 2], [3, 4]) == False


def test_are_collinear2():
    """Тест коллинеарности"""
    assert vc.are_collinear([1, 1], [-1, -1]) == True


def test_are_collinear3():
    """Тест коллинеарности"""
    assert vc.are_collinear([0], [0, -2]) == True


def test_are_collinear4():
    """Тест коллинеарности"""
    assert vc.are_collinear([0, 1], [0, -2]) == True


def test_get_cos():
    """Тест косинус"""
    assert vc.get_cos([1, 0], [0, 1]) == 0.0


def test_get_cos2():
    """Тест косинус"""
    assert vc.get_cos([1, 0], [-1, 0]) == -1.0


def test_are_codirectional():
    """Тест сонаправленность"""
    assert vc.are_codirectional([1, 0], [-1, 0]) == False


def test_are_codirectional2():
    """Тест сонаправленность"""
    assert vc.are_codirectional([0, 1], [0, 2]) == True


def test_are_codirectional3():
    """Тест сонаправленность"""
    assert vc.are_codirectional([0], [2, 2]) == True


def test_are_oppositely_directed():
    """Тест противоположнонаправленность"""
    assert vc.are_oppositely_directed([1, 0], [-1, 0]) == True


def test_are_oppositely_directed2():
    """Тест противоположнонаправленность"""
    assert vc.are_oppositely_directed([1, 1], [2, 2]) == False


def test_are_oppositely_directed3():
    """Тест противоположнонаправленность"""
    assert vc.are_oppositely_directed([0], [2, 2]) == True


def test_are_vector_equal():
    """Тест равенство векторов"""
    assert vc.are_vector_equal([0, 2], [2, 2]) == False


def test_are_vector_equal2():
    """Тест равенство векторов"""
    assert vc.are_vector_equal([2, 2], [2, 2]) == True


def test_is_vector_almost_equal():
    """Тест равенство векторов с заданной точностью"""
    assert vc.is_vector_almost_equal([2, 2], [2, 2.01], 1E-1) == True


def test_is_vector_almost_equal2():
    """Тест равенство векторов с заданной точностью"""
    assert vc.is_vector_almost_equal([2, 2], [2, 2.1], 1E-1) == False


def test_normalization():
    """Тест нормировка"""
    assert vc.normalization([3, 5, 8]) == [0.3, 0.5, 0.8]


def test_get_len_vec():
    """Тест нормировка"""
    assert vc.get_len_vec([3, 5, 8]) == 10


def test_change_direction():
    """Тест изменить направление"""
    assert vc.change_direction([3, 5, 8]) == [-3, -5, -8]


def test_change_direction():
    """Тест изменить направление"""
    assert vc.change_direction([0, -1, 3]) == [0, 1, -3]


def test_get_angle():
    """Тест угол"""
    assert vc.get_angle([0, 1], [1, 0]) == 90.0


def test_get_angle2():
    """Тест угол"""
    assert vc.get_angle([1, 0], [-1, 0]) == 180.0


def test_get_angle3():
    """Тест угол"""
    assert vc.get_angle([1, 1], [1, 0]) == 45.0


def test_proj_a_to_b():
    """Тест угол"""
    assert vc.proj_a_to_b([4, 5], [6, 0]) == 4.0


def test_proj_a_to_b2():
    """Тест угол"""
    assert vc.proj_a_to_b([1, 2], [3, 4]) == 2.2
