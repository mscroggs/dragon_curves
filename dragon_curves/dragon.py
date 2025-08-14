"""Dragon curve functions."""

from __future__ import annotations
from math import pi, sqrt, cos, sin
from enum import Enum


class Turn(Enum):
    """Left or right turn."""

    Left = 0
    Right = 1

    def __repr__(self) -> str:
        if self == Turn.Left:
            return "Turn.Left"
        else:
            return "Turn.Right"

    def __str__(self) -> str:
        if self == Turn.Left:
            return "Turn.Left"
        else:
            return "Turn.Right"

    def opposite(self) -> Turn:
        """Get the opposite turn."""
        if self == Turn.Left:
            return Turn.Right
        else:
            return Turn.Left


def dragon(n: int) -> list[Turn]:
    """Returns a list of 0s and 1s representing the order n dragon curve.

    Args:
        n: The order of the dragon curve

    Returns: a sequence of left and right turns
    """
    if n <= 1:
        return [Turn.Right]
    prev = dragon(n - 1)
    prev_s = prev.copy()
    mid = len(prev_s) // 2
    prev_s[mid] = prev_s[mid].opposite()
    return prev + [Turn.Right] + prev_s


def dragon_arc(
    n: int,
    xst: float = 0.0,
    yst: float = 0.0,
    dir_deg: float | None = None,
    dir_rad: float | None = None,
    angle_deg: float | None = None,
    angle_rad: float | None = None,
    return_position: bool = False,
) -> str | tuple[str, list[float]]:
    """Returns the svgwrite commands to draw an order n dragon curve.

    Args:
        n: The order of the dragon curve
    """
    pos = [xst, yst]
    angle = pi / 2
    if angle_deg is not None:
        angle = angle_deg * pi / 180
    if angle_rad is not None:
        angle = angle_rad

    dir = 0.0
    if dir_deg is not None:
        dir = dir_deg * pi / 180
    if dir_rad is not None:
        dir = dir_rad

    my_d = f"M{xst},{yst}"
    length = sqrt(50 - 50 * cos(angle))
    for d in dragon(n):
        my_d += f" a5,5 0 0,{d.value}"
        if d == Turn.Left:
            dir += angle / 2
        else:
            dir -= angle / 2
        my_d += f" {length * cos(dir)},{-length * sin(dir)}"
        pos[0] += length * cos(dir)
        pos[1] -= length * sin(dir)
        if d == Turn.Left:
            dir += angle / 2
        else:
            dir -= angle / 2

    if return_position:
        return my_d, pos

    return my_d
