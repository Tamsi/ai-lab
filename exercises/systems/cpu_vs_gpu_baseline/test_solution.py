import pytest

from exercises.systems.cpu_vs_gpu_baseline.solution import benchmark_matmul

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert benchmark_matmul is not None
