from operator import le
import sys
import math


def is_same_size(a, b):
    if len(a) == len(b):
        return True
    else:
        return False


EPS = 1E-10


def is_scalar_almost_equal(a, b, eps=EPS):
    return abs(a - b) <= eps


def is_vector_almost_equal(a, b, eps=EPS):
    same = [is_scalar_almost_equal(av, bv, eps) for av, bv in zip(a, b)]
    return False not in same


def is_matrix(a):
    l = len(a[0])
    for i in a:
        if l != len(i):
            return False
    return True


def get_nonzero_idx(matrix, i):
    while i < len(matrix) and matrix[i][i] == 0:
        i += 1
    return i


def get_root(matrix):
    root = []
    for i in range(len(matrix)):
        root.append(matrix[i][-1])
    return root


def get_expanded_matrix(matrix, res):
    expanded_matrix = matrix.copy()
    for i in range(len(res)):
        expanded_matrix[i].append(res[i])
    return expanded_matrix

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)