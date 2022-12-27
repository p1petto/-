import approximation_methods.approximation as apx
from add_func import is_vector_almost_equal


def test_least_squares():
    assert is_vector_almost_equal(apx.least_squares([[2, 3],
                                                     [3, 3],
                                                     [4, 7]], [7, 7, 3]), [4.69, -2.06], 1E-2) == True


def test_least_squares2():
    assert is_vector_almost_equal(apx.least_squares([[2],
                                                     [3]], [4, 9]), [2.69], 1E-2) == True

