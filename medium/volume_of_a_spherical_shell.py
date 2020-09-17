from math import pi


def vol_shell(r1: int, r2: int) -> float:
    return round(abs((4/3) * pi * (r1**3 - r2**3)), 3)
