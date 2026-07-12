import pytest
from exercises.pytorch.rnn_sequence.solution import rnn_forward

pytestmark = pytest.mark.skip(reason="Exercise scaffold — implement solution first")


def test_placeholder():
    assert rnn_forward is not None
