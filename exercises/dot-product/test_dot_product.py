import importlib.util
import math
from pathlib import Path

import numpy as np
import pytest

_solution = importlib.util.spec_from_file_location(
    "dot_product_solution", Path(__file__).parent / "solution.py"
)
_mod = importlib.util.module_from_spec(_solution)
_solution.loader.exec_module(_mod)
dot_product = _mod.dot_product


def test_basic():
    assert dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]) == 32.0


def test_orthogonal_is_zero():
    assert dot_product([1.0, 0.0], [0.0, 1.0]) == 0.0


def test_opposite_is_negative():
    assert dot_product([1.0, 0.0], [-1.0, 0.0]) == -1.0


def test_matches_numpy_random():
    rng = np.random.default_rng(0)
    for _ in range(20):
        x = rng.standard_normal(8).tolist()
        y = rng.standard_normal(8).tolist()
        assert dot_product(x, y) == pytest.approx(float(np.dot(x, y)))


def test_length_mismatch_raises():
    with pytest.raises(ValueError):
        dot_product([1.0], [1.0, 2.0])


def test_geometric_formula():
    x = [3.0, 0.0]
    y = [1.0, 1.0]
    cos_theta = dot_product(x, y) / (math.sqrt(9) * math.sqrt(2))
    assert cos_theta == pytest.approx(math.cos(math.pi / 4))
