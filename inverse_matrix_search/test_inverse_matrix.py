import inverse_matrix_search.inverse_matrix as im
from add_func import is_vector_almost_equal


def test_inverse():
    assert im.inverse([[1, 2], [3, 4]]) == [[-2, 1], [1.5, -0.5]]


def test_inverse2():
    assert im.inverse([[1, 1, 0], [0, 1, 0], [0, 3, 3]]) == [[1, -1, 0], [0, 1, 0], [0.0, -1.0, 0.3333333333333333]]


def test_get_root():
    assert im.get_root([[1, 2], [3, 4]], [6, 8]) == [-4.0, 5.0]


def test_get_root2():
    """except [2, -1, -3]"""
    assert is_vector_almost_equal(im.get_root([[1, -2, 1], [2, -1, 1], [3, 2, 2]], [1, 2, -2]), [2, -1, -3], 1E-10) == True
