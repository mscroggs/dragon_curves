"""Test dragon curve functions."""

import pytest
import dragon_curves as dc


@pytest.mark.parametrize(
    ("n", "curve"),
    [
        (1, [1]),
        (2, [1, 1, 0]),
        (3, [1, 1, 0, 1, 1, 0, 0]),
        (4, [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]),
    ],
)
def test_dragon(n, curve):
    assert dc.dragon(n) == [dc.Turn.Right if i == 1 else dc.Turn.Left for i in curve]


@pytest.mark.parametrize("n", range(1, 11))
def test_length(n):
    assert len(dc.dragon(n)) == 2**n - 1
