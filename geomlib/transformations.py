from typing import Iterable, List, Optional

from .point import Point
from .point3d import Point3D


def translate_points(points: Iterable[Point], dx: float, dy: float) -> List[Point]:
    return [point.translate(dx, dy) for point in points]


def rotate_points(points: Iterable[Point], angle_deg: float, center: Optional[Point] = None) -> List[Point]:
    return [point.rotate(angle_deg, center) for point in points]


def scale_points(points: Iterable[Point], factor: float, center: Optional[Point] = None) -> List[Point]:
    if center is None:
        center = Point(0, 0)
    return [
        Point(center.x + (point.x - center.x) * factor, center.y + (point.y - center.y) * factor)
        for point in points
    ]


def reflect_point_x(point: Point) -> Point:
    return Point(point.x, -point.y)


def reflect_point_y(point: Point) -> Point:
    return Point(-point.x, point.y)


def reflect_point_origin(point: Point) -> Point:
    return Point(-point.x, -point.y)


def translate_points3d(points: Iterable[Point3D], dx: float, dy: float, dz: float) -> List[Point3D]:
    return [point.translate(dx, dy, dz) for point in points]
