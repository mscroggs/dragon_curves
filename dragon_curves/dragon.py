"""Dragon curve functions."""
from math import pi, sqrt, cos, sin


def dragon(n: int) -> list[int]:
    """Returns a list of 0s and 1s representing the order n dragon curve."""
    if n <= 1:
        return [1]
    prev = dragon(n - 1)
    prev_s = prev[:]
    mid = len(prev_s) // 2
    prev_s[mid] = 1 - prev_s[mid]
    return prev + [1] + prev_s


def dragon_arc(
    n: int,
    xst: int = 0,
    yst: int = 0,
    dir_deg: float | None = None,
    dir_rad: float | None = None,
    angle_deg: float | None = None,
    angle_rad: float | None = None,
    return_position: bool = False,
):
    """Returns the svgwrite commands to draw an order n dragon curve."""
    pos = [xst, yst]
    angle = pi / 2
    if angle_deg is not None:
        angle = angle_deg * pi / 180
    if angle_rad is not None:
        angle = angle_rad

    dir = 0
    if dir_deg is not None:
        dir = dir_deg * pi / 180
    if dir_rad is not None:
        dir = dir_rad

    my_d = f"M{xst},{yst}"
    length = sqrt(50 - 50 * cos(angle))
    for d in dragon(n):
        my_d += " a5,5 0 0,{d}"
        if d == 0:
            dir += angle / 2
        else:
            dir -= angle / 2
        my_d += f" {length * cos(dir)},{-length * sin(dir)}"
        pos[0] += length * cos(dir)
        pos[1] -= length * sin(dir)
        if d == 0:
            dir += angle / 2
        else:
            dir -= angle / 2

    if return_position:
        return my_d, pos

    return my_d
