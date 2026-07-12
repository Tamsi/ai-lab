import pytest

from exercises.pytorch.attention_scratch.solution import scaled_dot_product_attention

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert scaled_dot_product_attention is not None
