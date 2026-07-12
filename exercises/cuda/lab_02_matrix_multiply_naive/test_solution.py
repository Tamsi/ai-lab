import pytest

from exercises.cuda.lab_02_matrix_multiply_naive.solution import matmul_naive

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert matmul_naive is not None
