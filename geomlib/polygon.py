import math
from typing import Iterable, List, Optional, Tuple

from .constants import is_close
from .point import Point


class Polygon:
    """Simple polygon represented by ordered vertices."""

    def __init__(self, vertices: Iterable[Point]):
        self.vertices = list(vertices)
        if len(self.vertices) < 3:
            raise ValueError("A polygon needs at least three vertices")
        if is_close(self.area(), 0.0):
            raise ValueError("Polygon vertices must not be collinear")

    def signed_area(self) -> float:
        total = 0.0
        for p1, p2 in self.edges():
            total += p1.x * p2.y - p2.x * p1.y
        return total / 2

    def area(self) -> float:
        return abs(self.signed_area())

    def perimeter(self) -> float:
        return sum(p1.distance_to(p2) for p1, p2 in self.edges())

    def edges(self) -> List[Tuple[Point, Point]]:
        return list(zip(self.vertices, self.vertices[1:] + self.vertices[:1]))

    def centroid(self) -> Point:
        signed_area = self.signed_area()
        if is_close(signed_area, 0.0):
            raise ValueError("Centroid is undefined for a zero-area polygon")

        cx = 0.0
        cy = 0.0
        for p1, p2 in self.edges():
            cross = p1.x * p2.y - p2.x * p1.y
            cx += (p1.x + p2.x) * cross
            cy += (p1.y + p2.y) * cross
        factor = 1 / (6 * signed_area)
        return Point(cx * factor, cy * factor)

    def contains(self, point: Point, *, include_boundary: bool = True) -> bool:
        if include_boundary and self._on_boundary(point):
            return True

        inside = False
        for p1, p2 in self.edges():
            crosses = (p1.y > point.y) != (p2.y > point.y)
            if crosses:
                x_intersection = (p2.x - p1.x) * (point.y - p1.y) / (p2.y - p1.y) + p1.x
                if point.x < x_intersection:
                    inside = not inside
        return inside

    def is_convex(self) -> bool:
        sign: Optional[bool] = None
        n = len(self.vertices)
        for i in range(n):
            a = self.vertices[i]
            b = self.vertices[(i + 1) % n]
            c = self.vertices[(i + 2) % n]
            cross = (b.x - a.x) * (c.y - b.y) - (b.y - a.y) * (c.x - b.x)
            if is_close(cross, 0.0):
                continue
            current = cross > 0
            if sign is None:
                sign = current
            elif sign != current:
                return False
        return True

    def bounding_box(self):
        from .rectangle import Rectangle

        min_x = min(point.x for point in self.vertices)
        max_x = max(point.x for point in self.vertices)
        min_y = min(point.y for point in self.vertices)
        max_y = max(point.y for point in self.vertices)
        return Rectangle(Point(min_x, min_y), max_x - min_x, max_y - min_y)

    def translate(self, dx: float, dy: float) -> "Polygon":
        return Polygon(point.translate(dx, dy) for point in self.vertices)

    def rotate(self, angle_deg: float, center: Optional[Point] = None) -> "Polygon":
        if center is None:
            center = self.centroid()
        return Polygon(point.rotate(angle_deg, center) for point in self.vertices)

    def scale(self, factor: float, center: Optional[Point] = None) -> "Polygon":
        if is_close(float(factor), 0.0):
            raise ValueError("Scale factor must be non-zero")
        if center is None:
            center = self.centroid()
        return Polygon(
            Point(center.x + (point.x - center.x) * factor, center.y + (point.y - center.y) * factor)
            for point in self.vertices
        )

    def _on_boundary(self, point: Point) -> bool:
        for p1, p2 in self.edges():
            cross = (point.y - p1.y) * (p2.x - p1.x) - (point.x - p1.x) * (p2.y - p1.y)
            if not is_close(cross, 0.0):
                continue
            within_x = min(p1.x, p2.x) - 1e-9 <= point.x <= max(p1.x, p2.x) + 1e-9
            within_y = min(p1.y, p2.y) - 1e-9 <= point.y <= max(p1.y, p2.y) + 1e-9
            if within_x and within_y:
                return True
        return False

    def __repr__(self) -> str:
        return f"Polygon({self.vertices!r})"


def regular_polygon(center: Point, sides: int, radius: float, *, start_angle_deg: float = 90.0) -> Polygon:
    """Create a regular polygon from its circumradius."""
    if sides < 3:
        raise ValueError("A regular polygon needs at least three sides")
    if radius <= 0:
        raise ValueError("Radius must be positive")

    vertices = []
    for i in range(sides):
        angle = math.radians(start_angle_deg + 360 * i / sides)
        vertices.append(Point(center.x + radius * math.cos(angle), center.y + radius * math.sin(angle)))
    return Polygon(vertices)
