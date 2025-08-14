"""Test dragon curve functions."""

import pytest
import dragon_curves as dc


@pytest.mark.parametrize(("n", "curve"), [
    (1, [1]),
    (2, [1, 1, 0]),
    (3, [1, 1, 0, 1, 1, 0, 0]),
    (4, [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]),
])
def test_dragon(n, curve):
    assert dc.dragon(n) == curve
