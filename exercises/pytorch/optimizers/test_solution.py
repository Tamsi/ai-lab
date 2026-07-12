import pytest

from exercises.pytorch.optimizers.solution import train_one_epoch

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert train_one_epoch is not None
