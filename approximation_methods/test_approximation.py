import approximation_methods.approximation as apx
from add_func import is_vector_almost_equal


def test_least_squares():
    assert is_vector_almost_equal(apx.least_squares([[2, 3],
                                                     [3, 3],
                                                     [4, 7]], [7, 7, 3]), [4.69, -2.06], 1E-2) == True


def test_least_squares2():
    assert is_vector_almost_equal(apx.least_squares([[2],
                                                     [3]], [4, 9]), [2.69], 1E-2) == True


def test_linear_approximation():
    assert is_vector_almost_equal(apx.linear_approximation([[1, 2],
                                                          [3, 4],
                                                         [3.5, 3],
                                                         [6, 7]], [1, 3, 5]),[1.69, 3.63, 5.6], 1E-1) == True


def test_second_degree_polynomial():
    assert is_vector_almost_equal(apx.second_degree_polynomial([[1, 2],
                                                                [3, 4],
                                                                [3.5, 3],
                                                                [6, 7]], [1, 3, 5]),[2.08, 3.26, 5.46], 1E-1) == True


def test_third_degree_polynomial():
    assert is_vector_almost_equal(apx.third_degree_polynomial([[1, 2],
                                                                [3, 4],
                                                                [3.5, 3],
                                                                [6, 7]], [1, 3, 5]),[2, 4, 2.16], 1E-1) == True