import pytest

from exercises.cuda.lab_03_shared_memory_tiling.solution import matmul_tiled

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert matmul_tiled is not None
