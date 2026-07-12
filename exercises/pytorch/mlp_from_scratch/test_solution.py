import pytest

from exercises.pytorch.mlp_from_scratch.solution import mlp_forward

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert mlp_forward is not None
