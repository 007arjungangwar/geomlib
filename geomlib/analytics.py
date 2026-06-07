import math
from typing import Optional, Tuple

from .constants import is_close
from .point import Point
from .point3d import Point3D
from .vector import Vector3D


class Line3D:
    """3D line represented by a point and a direction vector."""

    def __init__(self, point: Point3D, direction: Vector3D):
        if is_close(direction.magnitude(), 0.0):
            raise ValueError("Direction vector must be non-zero")
        self.point = point
        self.direction = direction

    @classmethod
    def from_points(cls, p1: Point3D, p2: Point3D) -> "Line3D":
        return cls(p1, Vector3D.from_points(p1, p2))

    def point_at(self, parameter: float) -> Point3D:
        v = self.direction * parameter
        return Point3D(self.point.x + v.x, self.point.y + v.y, self.point.z + v.z)

    def distance_to_point(self, point: Point3D) -> float:
        ap = Vector3D.from_points(self.point, point)
        return ap.cross(self.direction).magnitude() / self.direction.magnitude()

    def is_parallel(self, other: "Line3D") -> bool:
        return is_close(self.direction.cross(other.direction).magnitude(), 0.0)

    def angle_with(self, other: "Line3D") -> float:
        return self.direction.angle_with(other.direction)

    def shortest_distance_to_line(self, other: "Line3D") -> float:
        cross = self.direction.cross(other.direction)
        between = Vector3D.from_points(self.point, other.point)
        if is_close(cross.magnitude(), 0.0):
            return self.distance_to_point(other.point)
        return abs(between.dot(cross)) / cross.magnitude()

    def relation_to_sphere(self, sphere):
        """Classify this line as outside, tangent, or secant to a sphere."""
        from .relations import line_sphere_relation

        return line_sphere_relation(self, sphere)

    def sphere_intersections(self, sphere):
        """Return intersection points with a sphere."""
        from .relations import line_sphere_intersections

        return line_sphere_intersections(self, sphere)

    def is_tangent_to_sphere(self, sphere) -> bool:
        """Return True if this line touches the sphere at exactly one point."""
        return self.relation_to_sphere(sphere).kind == "tangent"

    def is_secant_to_sphere(self, sphere) -> bool:
        """Return True if this line cuts the sphere at two points."""
        return self.relation_to_sphere(sphere).kind == "secant"

    def __repr__(self) -> str:
        return f"Line3D(point={self.point}, direction={self.direction})"


class Plane:
    """Plane in 3D represented by ax + by + cz + d = 0."""

    def __init__(self, a: float, b: float, c: float, d: float):
        normal = Vector3D(a, b, c)
        if is_close(normal.magnitude(), 0.0):
            raise ValueError("Plane normal must be non-zero")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    @classmethod
    def from_point_normal(cls, point: Point3D, normal: Vector3D) -> "Plane":
        if is_close(normal.magnitude(), 0.0):
            raise ValueError("Plane normal must be non-zero")
        d = -(normal.x * point.x + normal.y * point.y + normal.z * point.z)
        return cls(normal.x, normal.y, normal.z, d)

    @classmethod
    def from_points(cls, p1: Point3D, p2: Point3D, p3: Point3D) -> "Plane":
        normal = Vector3D.from_points(p1, p2).cross(Vector3D.from_points(p1, p3))
        return cls.from_point_normal(p1, normal)

    @property
    def normal(self) -> Vector3D:
        return Vector3D(self.a, self.b, self.c)

    def contains(self, point: Point3D) -> bool:
        return is_close(self.a * point.x + self.b * point.y + self.c * point.z + self.d, 0.0)

    def distance_to_point(self, point: Point3D) -> float:
        numerator = abs(self.a * point.x + self.b * point.y + self.c * point.z + self.d)
        denominator = math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2)
        return numerator / denominator

    def is_parallel(self, other: "Plane") -> bool:
        return is_close(self.normal.cross(other.normal).magnitude(), 0.0)

    def angle_with(self, other: "Plane") -> float:
        angle = self.normal.angle_with(other.normal)
        return min(angle, 180 - angle)

    def line_intersection(self, line: Line3D) -> Optional[Point3D]:
        denom = self.normal.dot(line.direction)
        if is_close(denom, 0.0):
            return None
        t = -(self.a * line.point.x + self.b * line.point.y + self.c * line.point.z + self.d) / denom
        return line.point_at(t)

    def coefficients(self) -> Tuple[float, float, float, float]:
        return (self.a, self.b, self.c, self.d)

    def __repr__(self) -> str:
        return f"Plane({self.a}x + {self.b}y + {self.c}z + {self.d} = 0)"


def distance_between_points(p1: Point, p2: Point) -> float:
    return p1.distance_to(p2)


def section_formula(p1: Point, p2: Point, m: float, n: float, *, internal: bool = True) -> Point:
    """Return the point dividing p1p2 in ratio m:n."""
    if is_close(m + n, 0.0):
        raise ValueError("m + n must not be zero")
    if internal:
        return Point((m * p2.x + n * p1.x) / (m + n), (m * p2.y + n * p1.y) / (m + n))
    if is_close(m - n, 0.0):
        raise ValueError("m - n must not be zero for external division")
    return Point((m * p2.x - n * p1.x) / (m - n), (m * p2.y - n * p1.y) / (m - n))
