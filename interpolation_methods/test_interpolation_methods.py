import interpolation_methods.linear_interpolation_and_extrapolation as li
import interpolation_methods.piecewise_linear_interpolation as pli
import interpolation_methods.lagrange_polynomial as lp
import draw.draw_interpolation as di
from add_func import is_vector_almost_equal


def test_interpolation():
    """Тест линейная интерполяция"""
    # di.test_draw_interpolation([2, 5], [6, 9], [0, 4, 20])
    assert li.interpolation([2, 5], [6, 9], [0, 4, 20]) == [3.0, 7.0, 23.0]


def test_interpolation2():
    """Тест линейная интерполяция"""
    assert li.interpolation([1, 2], [3, 4], [-1.5, 3, 2]) == [-0.5, 4.0, 3.0]


def test_pl_interpolation():
    """Тест кусочно-линейная интерполяция"""
    assert is_vector_almost_equal(pli.piecewise_linear_interpolation([[1, 2],
                                                                      [3, 4],
                                                                      [3.5, 3],
                                                                      [6, 7]],
                                                                     [-1.5, 3, 2, 5, 9]), [-0.5, 4.0, 3.0, 5.4, 11.8], 1E-10) == True

def test_langrange():
    """Тест линейная интерполяция"""
    assert lp.lagrange_polynomial([[1, 2],
                                   [3, 4],
                                   [3.5, 3],
                                   [6, 7]], 2) == 4.92

def test_langrange2():
    """Тест линейная интерполяция"""
    assert lp.lagrange_polynomial([[1, 2],
                                   [3, 4],
                                   [3.5, 3],
                                   [6, 7]], 1) == 2