import math
from typing import Tuple

from .constants import is_close, require_positive
from .point import Point


class Parabola:
    """Axis-aligned parabola in standard form.

    orientation may be "right", "left", "up", or "down".
    """

    def __init__(self, vertex: Point, focal_length: float, orientation: str = "right"):
        self.vertex = vertex
        self.focal_length = require_positive(focal_length, "Focal length")
        if orientation not in {"right", "left", "up", "down"}:
            raise ValueError("orientation must be 'right', 'left', 'up', or 'down'")
        self.orientation = orientation

    def focus(self) -> Point:
        h, k, a = self.vertex.x, self.vertex.y, self.focal_length
        if self.orientation == "right":
            return Point(h + a, k)
        if self.orientation == "left":
            return Point(h - a, k)
        if self.orientation == "up":
            return Point(h, k + a)
        return Point(h, k - a)

    def directrix(self) -> Tuple[str, float]:
        h, k, a = self.vertex.x, self.vertex.y, self.focal_length
        if self.orientation == "right":
            return ("x", h - a)
        if self.orientation == "left":
            return ("x", h + a)
        if self.orientation == "up":
            return ("y", k - a)
        return ("y", k + a)

    def latus_rectum_length(self) -> float:
        return 4 * self.focal_length

    def point_at(self, parameter: float) -> Point:
        """Return a parametric point using t where offset perpendicular to the axis is 2at."""
        h, k, a, t = self.vertex.x, self.vertex.y, self.focal_length, float(parameter)
        if self.orientation in {"right", "left"}:
            sign = 1 if self.orientation == "right" else -1
            return Point(h + sign * a * t ** 2, k + 2 * a * t)
        sign = 1 if self.orientation == "up" else -1
        return Point(h + 2 * a * t, k + sign * a * t ** 2)

    def contains(self, point: Point) -> bool:
        h, k, a = self.vertex.x, self.vertex.y, self.focal_length
        if self.orientation == "right":
            return is_close((point.y - k) ** 2, 4 * a * (point.x - h))
        if self.orientation == "left":
            return is_close((point.y - k) ** 2, -4 * a * (point.x - h))
        if self.orientation == "up":
            return is_close((point.x - h) ** 2, 4 * a * (point.y - k))
        return is_close((point.x - h) ** 2, -4 * a * (point.y - k))

    def __repr__(self) -> str:
        return f"Parabola(vertex={self.vertex}, focal_length={self.focal_length}, orientation={self.orientation!r})"


class Hyperbola:
    """Axis-aligned hyperbola centered at a point."""

    def __init__(self, center: Point, a: float, b: float, transverse_axis: str = "x"):
        self.center = center
        self.a = require_positive(a, "Semi-transverse axis")
        self.b = require_positive(b, "Semi-conjugate axis")
        if transverse_axis not in {"x", "y"}:
            raise ValueError("transverse_axis must be 'x' or 'y'")
        self.transverse_axis = transverse_axis

    def eccentricity(self) -> float:
        return math.sqrt(1 + (self.b ** 2 / self.a ** 2))

    def foci(self) -> Tuple[Point, Point]:
        c = math.sqrt(self.a ** 2 + self.b ** 2)
        h, k = self.center.x, self.center.y
        if self.transverse_axis == "x":
            return (Point(h + c, k), Point(h - c, k))
        return (Point(h, k + c), Point(h, k - c))

    def asymptotes(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """Return slopes and intercepts of the two asymptotes as (m, c)."""
        h, k = self.center.x, self.center.y
        if self.transverse_axis == "x":
            slopes = (self.b / self.a, -self.b / self.a)
        else:
            slopes = (self.a / self.b, -self.a / self.b)
        return tuple((m, k - m * h) for m in slopes)

    def contains(self, point: Point) -> bool:
        x = point.x - self.center.x
        y = point.y - self.center.y
        if self.transverse_axis == "x":
            value = (x ** 2 / self.a ** 2) - (y ** 2 / self.b ** 2)
        else:
            value = (y ** 2 / self.a ** 2) - (x ** 2 / self.b ** 2)
        return is_close(value, 1.0)

    def __repr__(self) -> str:
        return f"Hyperbola(center={self.center}, a={self.a}, b={self.b}, transverse_axis={self.transverse_axis!r})"
