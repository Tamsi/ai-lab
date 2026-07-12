import pytest

from exercises.pytorch.backprop_manual.solution import manual_backward

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert manual_backward is not None
