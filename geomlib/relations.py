from dataclasses import dataclass
from typing import Optional, Tuple

from .constants import EPSILON, is_close
from .point import Point
from .point3d import Point3D


@dataclass(frozen=True)
class RelationResult:
    """Structured result for geometric relationship queries."""

    kind: str
    intersections: tuple = ()
    distance: Optional[float] = None
    description: str = ""

    @property
    def count(self) -> int:
        """Number of intersection/contact points returned."""
        return len(self.intersections)

    @property
    def touches(self) -> bool:
        """True when objects touch at exactly one point without crossing."""
        return "tangent" in self.kind or self.kind.endswith("_touching")

    @property
    def cuts(self) -> bool:
        """True when one object cuts through the other."""
        return "secant" in self.kind or "crossing" in self.kind

    @property
    def disjoint(self) -> bool:
        """True when objects do not meet."""
        return self.count == 0 and ("outside" in self.kind or "separate" in self.kind)


def point_circle_relation(point, circle) -> RelationResult:
    """Classify a point as inside, on, or outside a circle."""
    distance = point.distance_to(circle.center)
    if is_close(distance, circle.radius):
        return RelationResult("on_circle", (point,), distance, "Point lies on the circle.")
    if distance < circle.radius:
        return RelationResult("inside_circle", (), distance, "Point lies inside the circle.")
    return RelationResult("outside_circle", (), distance, "Point lies outside the circle.")


def line_circle_relation(line, circle) -> RelationResult:
    """Classify an infinite line and circle as outside, tangent, or secant."""
    distance = line.distance_to_point(circle.center)
    intersections = circle.line_intersections(line)
    if distance > circle.radius and not is_close(distance, circle.radius):
        return RelationResult("outside", (), distance, "Line has no common point with the circle.")
    if is_close(distance, circle.radius):
        return RelationResult("tangent", intersections, distance, "Line touches the circle at one point.")
    return RelationResult("secant", intersections, distance, "Line cuts the circle at two points.")


def segment_circle_relation(line, circle) -> RelationResult:
    """Classify a finite line segment and circle."""
    infinite_relation = line_circle_relation(line, circle)
    intersections = tuple(point for point in infinite_relation.intersections if line.contains_point(point, segment=True))
    endpoints = (line.p1, line.p2)
    endpoint_relations = tuple(point_circle_relation(point, circle).kind for point in endpoints)
    inside_or_on = all(kind in {"inside_circle", "on_circle"} for kind in endpoint_relations)

    if len(intersections) == 2:
        return RelationResult(
            "segment_secant",
            intersections,
            infinite_relation.distance,
            "Segment cuts the circle at two points.",
        )
    if len(intersections) == 1:
        if infinite_relation.kind == "tangent":
            return RelationResult(
                "segment_tangent",
                intersections,
                infinite_relation.distance,
                "Segment touches the circle at one point.",
            )
        return RelationResult(
            "segment_crossing",
            intersections,
            infinite_relation.distance,
            "Segment crosses the circle boundary once.",
        )
    if inside_or_on:
        return RelationResult(
            "segment_inside",
            (),
            infinite_relation.distance,
            "Segment lies inside the circle and has no boundary intersection.",
        )
    return RelationResult(
        "segment_outside",
        (),
        infinite_relation.distance,
        "Segment has no common point with the circle.",
    )


def circle_circle_relation(circle1, circle2) -> RelationResult:
    """Classify the relation between two circles."""
    kind = circle1.relation_to_circle(circle2)
    intersections = circle_intersection_points(circle1, circle2)
    distance = circle1.center.distance_to(circle2.center)
    descriptions = {
        "coincident": "Circles are identical and have infinitely many common points.",
        "separate": "Circles are separate and do not meet.",
        "externally_tangent": "Circles touch externally at one point.",
        "contained": "One circle lies inside the other without touching.",
        "internally_tangent": "Circles touch internally at one point.",
        "intersecting": "Circles cut each other at two points.",
    }
    return RelationResult(kind, intersections, distance, descriptions[kind])


def circle_intersection_points(circle1, circle2) -> Tuple[Point, ...]:
    """Return the finite intersection points of two circles."""
    d = circle1.center.distance_to(circle2.center)
    r1 = circle1.radius
    r2 = circle2.radius

    if is_close(d, 0.0) and is_close(r1, r2):
        return ()
    if d > r1 + r2 and not is_close(d, r1 + r2):
        return ()
    if d < abs(r1 - r2) and not is_close(d, abs(r1 - r2)):
        return ()
    if is_close(d, 0.0):
        return ()

    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h_squared = r1 ** 2 - a ** 2
    if h_squared < 0 and abs(h_squared) <= EPSILON:
        h_squared = 0.0
    if h_squared < 0:
        return ()

    cx = circle1.center.x
    cy = circle1.center.y
    dx = (circle2.center.x - cx) / d
    dy = (circle2.center.y - cy) / d
    base = Point(cx + a * dx, cy + a * dy)

    if is_close(h_squared, 0.0):
        return (base,)

    h = h_squared ** 0.5
    rx = -dy * h
    ry = dx * h
    return (Point(base.x + rx, base.y + ry), Point(base.x - rx, base.y - ry))


def line_rectangle_relation(line, rectangle, *, segment: bool = False) -> RelationResult:
    """Classify how a line or segment meets an axis-aligned rectangle."""
    from .line import Line

    edges = (
        Line(rectangle.bottom_left, rectangle.bottom_right),
        Line(rectangle.bottom_right, rectangle.top_right),
        Line(rectangle.top_right, rectangle.top_left),
        Line(rectangle.top_left, rectangle.bottom_left),
    )
    points = []
    for edge in edges:
        point = line.intersection(edge)
        if point is None:
            continue
        if edge.contains_point(point, segment=True) and (not segment or line.contains_point(point, segment=True)):
            if not any(existing == point for existing in points):
                points.append(point)

    if segment and rectangle.contains(line.p1) and rectangle.contains(line.p2) and not points:
        return RelationResult("segment_inside", (), None, "Segment lies fully inside the rectangle.")
    if len(points) == 0:
        return RelationResult("outside", (), None, "Line has no common point with the rectangle.")
    if len(points) == 1:
        return RelationResult("touching", tuple(points), None, "Line touches the rectangle at one point.")
    return RelationResult("cutting", tuple(points), None, "Line cuts the rectangle.")


def line_sphere_relation(line3d, sphere) -> RelationResult:
    """Classify a 3D line and sphere as outside, tangent, or secant."""
    distance = line3d.distance_to_point(sphere.center)
    intersections = line_sphere_intersections(line3d, sphere)
    if distance > sphere.radius and not is_close(distance, sphere.radius):
        return RelationResult("outside", (), distance, "Line has no common point with the sphere.")
    if is_close(distance, sphere.radius):
        return RelationResult("tangent", intersections, distance, "Line touches the sphere at one point.")
    return RelationResult("secant", intersections, distance, "Line cuts the sphere at two points.")


def line_sphere_intersections(line3d, sphere) -> Tuple[Point3D, ...]:
    """Return intersection points of a 3D line and sphere."""
    direction = line3d.direction
    point = line3d.point
    center = sphere.center
    fx = point.x - center.x
    fy = point.y - center.y
    fz = point.z - center.z

    a = direction.dot(direction)
    b = 2 * (fx * direction.x + fy * direction.y + fz * direction.z)
    c = fx ** 2 + fy ** 2 + fz ** 2 - sphere.radius ** 2
    discriminant = b ** 2 - 4 * a * c

    if discriminant < -EPSILON:
        return ()
    if is_close(discriminant, 0.0):
        return (line3d.point_at(-b / (2 * a)),)

    root = discriminant ** 0.5
    return (line3d.point_at((-b - root) / (2 * a)), line3d.point_at((-b + root) / (2 * a)))
