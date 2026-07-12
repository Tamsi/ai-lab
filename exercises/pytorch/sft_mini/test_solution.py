import pytest
from exercises.pytorch.sft_mini.solution import sft_step

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert sft_step is not None
