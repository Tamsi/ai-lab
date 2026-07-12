import pytest

from exercises.pytorch.tensor_basics.solution import tensor_ops

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert tensor_ops is not None
