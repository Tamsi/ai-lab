import numpy as np
import pytest

from exercises.numpy.matrix_multiplication.solution import matmul


def test_2x2():
    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]
    expected = [[19.0, 22.0], [43.0, 50.0]]
    assert matmul(A, B) == expected


def test_identity():
    A = [[1.0, 2.0], [3.0, 4.0]]
    I = [[1.0, 0.0], [0.0, 1.0]]
    assert matmul(A, I) == A
    assert matmul(I, A) == A


def test_matches_numpy_random():
    rng = np.random.default_rng(0)
    for m, n, p in [(2, 3, 4), (5, 5, 5), (3, 7, 2)]:
        A = rng.standard_normal((m, n))
        B = rng.standard_normal((n, p))
        got = matmul(A.tolist(), B.tolist())
        expected = (A @ B).tolist()
        for row_g, row_e in zip(got, expected):
            assert row_g == pytest.approx(row_e)


def test_incompatible_shapes_raises():
    with pytest.raises(ValueError):
        matmul([[1.0, 2.0]], [[1.0], [2.0], [3.0]])
