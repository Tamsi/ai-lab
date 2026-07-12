import pytest
from exercises.pytorch.cnn_conv2d.solution import conv2d_forward

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert conv2d_forward is not None
