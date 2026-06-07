import math
from typing import Tuple

from .constants import is_close
from .point import Point
from .point3d import Point3D


class Vector2D:
    """2D vector with common algebra and geometry operations."""

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def from_points(cls, start: Point, end: Point) -> "Vector2D":
        return cls(end.x - start.x, end.y - start.y)

    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

    def dot(self, other: "Vector2D") -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector2D") -> float:
        """Return the scalar z-component of the 2D cross product."""
        return self.x * other.y - self.y * other.x

    def normalize(self) -> "Vector2D":
        mag = self.magnitude()
        if is_close(mag, 0.0):
            raise ValueError("Cannot normalize zero vector")
        return self / mag

    def angle_with(self, other: "Vector2D") -> float:
        """Return the smaller angle to another vector in degrees."""
        denom = self.magnitude() * other.magnitude()
        if is_close(denom, 0.0):
            raise ValueError("Angle is undefined for zero vectors")
        cos_value = max(-1.0, min(1.0, self.dot(other) / denom))
        return math.degrees(math.acos(cos_value))

    def projection_on(self, other: "Vector2D") -> "Vector2D":
        denom = other.dot(other)
        if is_close(denom, 0.0):
            raise ValueError("Cannot project on zero vector")
        return other * (self.dot(other) / denom)

    def perpendicular(self) -> "Vector2D":
        return Vector2D(-self.y, self.x)

    def to_point(self) -> Point:
        return Point(self.x, self.y)

    def to_tuple(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector2D":
        return Vector2D(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> "Vector2D":
        if is_close(float(scalar), 0.0):
            raise ZeroDivisionError("Cannot divide vector by zero")
        return Vector2D(self.x / scalar, self.y / scalar)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector2D) and is_close(self.x, other.x) and is_close(self.y, other.y)

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"


class Vector3D:
    """3D vector with dot, cross, projection, and angle operations."""

    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @classmethod
    def from_points(cls, start: Point3D, end: Point3D) -> "Vector3D":
        return cls(end.x - start.x, end.y - start.y, end.z - start.z)

    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def dot(self, other: "Vector3D") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def normalize(self) -> "Vector3D":
        mag = self.magnitude()
        if is_close(mag, 0.0):
            raise ValueError("Cannot normalize zero vector")
        return self / mag

    def angle_with(self, other: "Vector3D") -> float:
        denom = self.magnitude() * other.magnitude()
        if is_close(denom, 0.0):
            raise ValueError("Angle is undefined for zero vectors")
        cos_value = max(-1.0, min(1.0, self.dot(other) / denom))
        return math.degrees(math.acos(cos_value))

    def projection_on(self, other: "Vector3D") -> "Vector3D":
        denom = other.dot(other)
        if is_close(denom, 0.0):
            raise ValueError("Cannot project on zero vector")
        return other * (self.dot(other) / denom)

    def scalar_triple(self, b: "Vector3D", c: "Vector3D") -> float:
        return self.dot(b.cross(c))

    def to_point3d(self) -> Point3D:
        return Point3D(self.x, self.y, self.z)

    def to_tuple(self) -> Tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def __add__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> "Vector3D":
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> "Vector3D":
        if is_close(float(scalar), 0.0):
            raise ZeroDivisionError("Cannot divide vector by zero")
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Vector3D)
            and is_close(self.x, other.x)
            and is_close(self.y, other.y)
            and is_close(self.z, other.z)
        )

    def __repr__(self) -> str:
        return f"Vector3D({self.x}, {self.y}, {self.z})"
