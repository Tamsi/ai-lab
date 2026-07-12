import pytest

from exercises.cuda.lab_01_vector_add.solution import vector_add

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert vector_add is not None
