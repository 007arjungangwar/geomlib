import math
from typing import Tuple


def degrees_to_radians(degrees: float) -> float:
    return math.radians(degrees)


def radians_to_degrees(radians: float) -> float:
    return math.degrees(radians)


def pythagorean_hypotenuse(a: float, b: float) -> float:
    return math.hypot(a, b)


def pythagorean_leg(hypotenuse: float, leg: float) -> float:
    if hypotenuse < leg:
        raise ValueError("Hypotenuse must be at least as long as the leg")
    return math.sqrt(hypotenuse ** 2 - leg ** 2)


def heron_area(a: float, b: float, c: float) -> float:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Triangle inequality is not satisfied")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x2 - x1, y2 - y1)


def distance_3d(x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def midpoint_2d(x1: float, y1: float, x2: float, y2: float) -> Tuple[float, float]:
    return ((x1 + x2) / 2, (y1 + y2) / 2)
