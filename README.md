# GeomLib Advanced

GeomLib Advanced is a pure-Python geometry toolkit for 2D and 3D mathematical work. It covers school-level geometry, coordinate geometry, conic sections, vectors, mensuration, and analytic 3D geometry.

Install from PyPI:

```bash
pip install geomlib-advanced
```

Import from the `geomlib` package:

```python
from geomlib import Point, Circle, Triangle, Point3D, Sphere
```

## Quick Start

```python
from geomlib import Point, Circle, Triangle, Vector2D, Point3D, Vector3D, Line3D, Plane

circle = Circle(Point(0, 0), 5)
print(circle.area())
print(circle.perimeter())

triangle = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
print(triangle.area())
print(triangle.incenter())

vector = Vector2D(3, 4)
print(vector.magnitude())
print(vector.normalize())

line = Line3D(Point3D(0, 0, 0), Vector3D(1, 1, 1))
plane = Plane.from_point_normal(Point3D(0, 0, 2), Vector3D(0, 0, 1))
print(plane.line_intersection(line))
```

## Complete Import List

```python
from geomlib import (
    Point, Line, Circle, Rectangle, Square, Rhombus, Parallelogram,
    Triangle, Ellipse, Polygon, regular_polygon,
    Point3D, Sphere, Cube, Cuboid, Cylinder, Cone,
    Vector2D, Vector3D, Line3D, Plane,
    Parabola, Hyperbola,
    RelationResult,
    point_circle_relation, line_circle_relation, segment_circle_relation,
    circle_circle_relation, circle_intersection_points,
    line_rectangle_relation, line_sphere_relation, line_sphere_intersections,
    distance_between_points, section_formula,
    translate_points, rotate_points, scale_points,
    reflect_point_x, reflect_point_y, reflect_point_origin, translate_points3d,
    degrees_to_radians, radians_to_degrees,
    pythagorean_hypotenuse, pythagorean_leg, heron_area,
    distance_2d, distance_3d, midpoint_2d,
)
```

## 2D Points

Create a point with `Point(x, y)`.

```python
from geomlib import Point

p1 = Point(0, 0)
p2 = Point(3, 4)

print(p1.distance_to(p2))          # 5.0
print(p2.distance_to_origin())     # 5.0
print(p2.magnitude())              # 5.0
print(p1.midpoint(p2))             # Point halfway between p1 and p2
print(p1.slope_to(p2))             # slope of the line through p1 and p2
print(p2.translate(2, -1))         # move point by dx, dy
print(p2.rotate(90))               # rotate around origin
print(p2.rotate(90, Point(1, 1)))  # rotate around another point
print(p1.to_tuple())               # (0.0, 0.0)
```

Point also supports vector-like operators:

```python
print(Point(1, 2) + Point(3, 4))
print(Point(3, 4) - Point(1, 2))
print(Point(2, 3) * 4)
print(Point(8, 6) / 2)
print(Point(1, 2).dot(Point(3, 4)))
print(Point(1, 2).cross(Point(3, 4)))
```

## 2D Vectors

Use `Vector2D(x, y)` for vector algebra.

```python
from geomlib import Point, Vector2D

v = Vector2D(3, 4)
w = Vector2D(1, 0)

print(v.magnitude())          # 5.0
print(v.dot(w))               # dot product
print(v.cross(w))             # scalar 2D cross product
print(v.normalize())          # unit vector
print(v.angle_with(w))        # degrees
print(v.projection_on(w))     # vector projection
print(v.perpendicular())      # rotated 90 degrees
print(v.to_point())
print(v.to_tuple())

direction = Vector2D.from_points(Point(0, 0), Point(3, 4))
print(direction)
```

Vector2D supports `+`, `-`, `* scalar`, and `/ scalar`.

## Lines

Create a line from two points.

```python
from geomlib import Point, Line, Circle

line1 = Line(Point(0, 0), Point(4, 4))
line2 = Line(Point(0, 4), Point(4, 0))

print(line1.length())
print(line1.slope_angle())
print(line1.is_vertical())
print(line1.is_horizontal())
print(line1.is_parallel(line2))
print(line1.is_perpendicular(line2))
print(line1.intersection(line2))
print(line1.distance_to_point(Point(0, 2)))
print(line1.midpoint())
print(line1.contains_point(Point(2, 2)))
print(line1.contains_point(Point(5, 5), segment=True))
print(line1.equation_coefficients())  # (a, b, c) for ax + by + c = 0
print(line1.angle_with(line2))
print(line1.point_at_distance(2))

circle = Circle(Point(0, 0), 5)
print(line1.relation_to_circle(circle))
print(line1.is_tangent_to_circle(circle))
print(line1.is_secant_to_circle(circle))
print(line1.segment_relation_to_circle(circle))
```

## Circles

```python
from geomlib import Point, Line, Circle

c1 = Circle(Point(0, 0), 5)
c2 = Circle(Point(6, 0), 3)

print(c1.area())
print(c1.perimeter())              # circumference
print(c1.diameter())
print(c1.contains(Point(3, 4)))
print(c1.intersects(c2))
print(c1.relation_to_circle(c2))   # separate, tangent, intersecting, contained, coincident
print(c1.intersection_area(c2))
print(c1.tangent_points(Point(10, 0)))
print(c1.line_intersections(Line(Point(-10, 0), Point(10, 0))))
print(c1.relation_to_line(Line(Point(-10, 5), Point(10, 5))))
print(c1.relation_to_segment(Line(Point(0, 0), Point(10, 0))))
print(c1.is_tangent_to_line(Line(Point(-10, 5), Point(10, 5))))
print(c1.is_secant_to_line(Line(Point(-10, 0), Point(10, 0))))
print(c1.chord_length_from_line(Line(Point(-10, 0), Point(10, 0))))
print(c1.circle_intersections(Circle(Point(8, 0), 5)))
print(c1.relation(Circle(Point(8, 0), 5)))
print(c1.scale(2))
print(c1.translate(1, 2))
```

## Geometric Relations

Relationship helpers return a `RelationResult`:

```python
RelationResult(
    kind="tangent",
    intersections=(Point(0, 5),),
    distance=5.0,
    description="Line touches the circle at one point.",
)
```

Use these fields:

- `kind`: relation name such as `"outside"`, `"tangent"`, `"secant"`, `"segment_crossing"`, `"intersecting"`
- `intersections`: contact or intersection points
- `distance`: useful separating distance when available
- `description`: human-readable explanation
- `count`: number of returned points
- `touches`: `True` for tangent/touching relations
- `cuts`: `True` for secant/crossing relations
- `disjoint`: `True` when objects do not meet

Line and circle:

```python
from geomlib import Point, Line, Circle, line_circle_relation, segment_circle_relation

circle = Circle(Point(0, 0), 5)
tangent = Line(Point(-10, 5), Point(10, 5))
secant = Line(Point(-10, 0), Point(10, 0))
outside = Line(Point(-10, 6), Point(10, 6))

print(line_circle_relation(tangent, circle).kind)  # tangent
print(line_circle_relation(secant, circle).kind)   # secant
print(line_circle_relation(outside, circle).kind)  # outside

relation = circle.relation_to_line(secant)
print(relation.kind)
print(relation.intersections)
print(relation.cuts)

segment = Line(Point(0, 0), Point(10, 0))
print(segment_circle_relation(segment, circle).kind)  # segment_crossing
```

Point and circle:

```python
from geomlib import point_circle_relation

print(point_circle_relation(Point(0, 0), circle).kind)  # inside_circle
print(point_circle_relation(Point(5, 0), circle).kind)  # on_circle
print(point_circle_relation(Point(6, 0), circle).kind)  # outside_circle
```

Circle and circle:

```python
from geomlib import circle_circle_relation, circle_intersection_points

c1 = Circle(Point(0, 0), 5)
c2 = Circle(Point(8, 0), 5)

relation = circle_circle_relation(c1, c2)
print(relation.kind)           # intersecting
print(relation.intersections)  # two common points
print(circle_intersection_points(c1, c2))
```

Line and rectangle:

```python
from geomlib import Rectangle, line_rectangle_relation

rect = Rectangle(Point(0, 0), 4, 3)
line = Line(Point(-1, 1), Point(5, 1))

print(line_rectangle_relation(line, rect).kind)      # cutting
print(line.relation_to_rectangle(rect).intersections)
```

## Rectangles and Squares

```python
from geomlib import Point, Rectangle, Square

rect = Rectangle(Point(0, 0), width=10, height=5)
print(rect.bottom_left)
print(rect.top_left)
print(rect.bottom_right)
print(rect.top_right)
print(rect.center)
print(rect.area())
print(rect.perimeter())
print(rect.diagonal())
print(rect.contains(Point(2, 2)))
print(rect.intersects(Rectangle(Point(5, 2), 3, 3)))
print(rect.intersection(Rectangle(Point(5, 2), 3, 3)))
print(rect.scale(1.5))
print(rect.translate(2, 3))

square = Square(Point(0, 0), side=4)
print(square.area())                       # inherited from Rectangle
print(square.perimeter())                  # inherited from Rectangle
print(square.side_length)
print(square.diagonal())
print(square.inscribed_circle_radius())
print(square.circumscribed_circle_radius())
```

## Triangles

```python
from geomlib import Point, Triangle

t = Triangle(Point(0, 0), Point(6, 0), Point(0, 8))

print(t.side_lengths())
print(t.area())
print(t.perimeter())
print(t.angles())
print(t.is_equilateral())
print(t.is_isosceles())
print(t.is_right_angled())
print(t.centroid())
print(t.circumcenter())
print(t.incenter())
print(t.orthocenter())
print(t.circumradius())
print(t.inradius())
print(t.contains(Point(2, 2)))
```

Triangle points must form a non-degenerate triangle.

## Quadrilaterals

```python
from geomlib import Point, Rhombus, Parallelogram

rhombus = Rhombus(Point(0, 0), side=5, angle_deg=60)
print(rhombus.area())
print(rhombus.perimeter())
print(rhombus.height())
print(rhombus.vertices())
print(rhombus.contains(Point(1, 1)))
print(rhombus.inscribed_circle_radius())

para = Parallelogram(Point(0, 0), base_length=6, side_length=4, angle_deg=45)
print(para.area())
print(para.perimeter())
print(para.height())
print(para.vertices())
print(para.center())
print(para.contains(Point(2, 1)))
```

## Ellipses, Parabolas, and Hyperbolas

```python
from geomlib import Point, Ellipse, Parabola, Hyperbola

ellipse = Ellipse(Point(0, 0), a=5, b=3)
print(ellipse.area())
print(ellipse.perimeter())          # Ramanujan approximation
print(ellipse.eccentricity())
print(ellipse.foci())
print(ellipse.major_axis_length())
print(ellipse.minor_axis_length())
print(ellipse.directrices())
print(ellipse.contains(Point(1, 1)))
print(ellipse.scale(2))
print(ellipse.translate(3, 4))

parabola = Parabola(Point(0, 0), focal_length=2, orientation="up")
print(parabola.focus())
print(parabola.directrix())         # ("y", value) or ("x", value)
print(parabola.latus_rectum_length())
print(parabola.point_at(1))
print(parabola.contains(Point(4, 2)))

hyperbola = Hyperbola(Point(0, 0), a=3, b=4, transverse_axis="x")
print(hyperbola.eccentricity())
print(hyperbola.foci())
print(hyperbola.asymptotes())       # slope/intercept pairs
print(hyperbola.contains(Point(3, 0)))
```

Parabola orientation can be `"right"`, `"left"`, `"up"`, or `"down"`. Hyperbola transverse axis can be `"x"` or `"y"`.

## Polygons

```python
from geomlib import Point, Polygon, regular_polygon

poly = Polygon([Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)])

print(poly.signed_area())
print(poly.area())
print(poly.perimeter())
print(poly.edges())
print(poly.centroid())
print(poly.contains(Point(2, 2)))
print(poly.contains(Point(0, 1), include_boundary=False))
print(poly.is_convex())
print(poly.bounding_box())
print(poly.translate(1, 1))
print(poly.rotate(45))
print(poly.scale(2))

pentagon = regular_polygon(Point(0, 0), sides=5, radius=10)
print(pentagon.vertices)
```

Polygon vertices must be ordered around the boundary.

## 3D Points and Vectors

```python
from geomlib import Point3D, Vector3D

p = Point3D(1, 2, 3)
q = Point3D(4, 6, 3)

print(p.distance_to(q))
print(p.distance_to_origin())
print(p.dot(q))
print(p.cross(q))
print(p.magnitude())
print(p.normalize())
print(p.translate(1, 1, 1))
print(p.rotate_x(90))
print(p.rotate_y(90))
print(p.rotate_z(90))
print(p.to_tuple())

v = Vector3D(1, 2, 3)
w = Vector3D(4, 5, 6)

print(Vector3D.from_points(p, q))
print(v.magnitude())
print(v.dot(w))
print(v.cross(w))
print(v.normalize())
print(v.angle_with(w))
print(v.projection_on(w))
print(v.scalar_triple(Vector3D(1, 0, 0), Vector3D(0, 1, 0)))
print(v.to_point3d())
print(v.to_tuple())
```

Point3D and Vector3D support `+`, `-`, `* scalar`, and `/ scalar`.

## 3D Lines and Planes

```python
from geomlib import Point3D, Vector3D, Line3D, Plane, Sphere

line1 = Line3D(Point3D(0, 0, 0), Vector3D(1, 1, 1))
line2 = Line3D.from_points(Point3D(0, 1, 0), Point3D(1, 2, 1))
secant_line = Line3D(Point3D(-10, 0, 0), Vector3D(1, 0, 0))
tangent_line = Line3D(Point3D(-10, 5, 0), Vector3D(1, 0, 0))
sphere = Sphere(Point3D(0, 0, 0), 5)

print(line1.point_at(2))
print(line1.distance_to_point(Point3D(1, 0, 0)))
print(line1.is_parallel(line2))
print(line1.angle_with(line2))
print(line1.shortest_distance_to_line(line2))
print(secant_line.relation_to_sphere(sphere).kind)   # secant
print(secant_line.sphere_intersections(sphere))
print(tangent_line.relation_to_sphere(sphere).kind)  # tangent
print(tangent_line.is_tangent_to_sphere(sphere))
print(secant_line.is_secant_to_sphere(sphere))

plane1 = Plane(0, 0, 1, -2)  # z - 2 = 0
plane2 = Plane.from_point_normal(Point3D(0, 0, 2), Vector3D(0, 0, 1))
plane3 = Plane.from_points(Point3D(0, 0, 0), Point3D(1, 0, 0), Point3D(0, 1, 0))

print(plane1.normal)
print(plane1.contains(Point3D(1, 1, 2)))
print(plane1.distance_to_point(Point3D(0, 0, 5)))
print(plane1.is_parallel(plane2))
print(plane1.angle_with(plane3))
print(plane1.line_intersection(line1))
print(plane1.coefficients())
```

## 3D Shapes

```python
from geomlib import Point3D, Sphere, Cube, Cuboid, Cylinder, Cone

sphere = Sphere(Point3D(0, 0, 0), radius=3)
print(sphere.volume())
print(sphere.surface_area())
print(sphere.diameter())
print(sphere.contains(Point3D(1, 1, 1)))
print(sphere.intersects(Sphere(Point3D(4, 0, 0), 2)))
print(sphere.volume_intersection(Sphere(Point3D(4, 0, 0), 2)))
print(sphere.scale(2))
print(sphere.translate(1, 2, 3))

cube = Cube(Point3D(0, 0, 0), side=4)
print(cube.volume())
print(cube.surface_area())
print(cube.space_diagonal())
print(cube.vertices())
print(cube.contains(Point3D(1, 1, 1)))
print(cube.inscribed_sphere_radius())
print(cube.circumscribed_sphere_radius())
print(cube.scale(2))
print(cube.translate(1, 2, 3))

cuboid = Cuboid(Point3D(0, 0, 0), length=2, width=3, height=4)
print(cuboid.volume())
print(cuboid.surface_area())
print(cuboid.space_diagonal())
print(cuboid.vertices())
print(cuboid.contains(Point3D(0, 0, 1)))
print(cuboid.scale(2))
print(cuboid.translate(1, 2, 3))

cylinder = Cylinder(Point3D(0, 0, 0), radius=2, height=10)
print(cylinder.volume())
print(cylinder.surface_area())
print(cylinder.lateral_surface_area())
print(cylinder.contains(Point3D(1, 1, 0)))
print(cylinder.scale(2))
print(cylinder.translate(1, 2, 3))

cone = Cone(Point3D(0, 0, 0), radius=2, height=6)
print(cone.volume())
print(cone.surface_area())
print(cone.lateral_surface_area())
print(cone.slant_height())
print(cone.contains(Point3D(0, 0, -2)))
print(cone.scale(2))
print(cone.translate(1, 2, 3))
```

## Coordinate Geometry Helpers

```python
from geomlib import Point, distance_between_points, section_formula

p1 = Point(0, 0)
p2 = Point(6, 6)

print(distance_between_points(p1, p2))
print(section_formula(p1, p2, 1, 2))                  # internal division
print(section_formula(p1, p2, 3, 1, internal=False))  # external division
```

## Formula Helpers

```python
from geomlib import (
    degrees_to_radians,
    radians_to_degrees,
    pythagorean_hypotenuse,
    pythagorean_leg,
    heron_area,
    distance_2d,
    distance_3d,
    midpoint_2d,
)

print(degrees_to_radians(180))
print(radians_to_degrees(3.141592653589793))
print(pythagorean_hypotenuse(3, 4))
print(pythagorean_leg(5, 3))
print(heron_area(3, 4, 5))
print(distance_2d(0, 0, 3, 4))
print(distance_3d(0, 0, 0, 1, 2, 2))
print(midpoint_2d(0, 0, 4, 6))
```

## Transformation Helpers

```python
from geomlib import (
    Point,
    Point3D,
    translate_points,
    rotate_points,
    scale_points,
    reflect_point_x,
    reflect_point_y,
    reflect_point_origin,
    translate_points3d,
)

points = [Point(1, 0), Point(0, 1)]

print(translate_points(points, 2, 3))
print(rotate_points(points, 90))
print(scale_points(points, 2))
print(reflect_point_x(Point(2, 3)))
print(reflect_point_y(Point(2, 3)))
print(reflect_point_origin(Point(2, 3)))
print(translate_points3d([Point3D(1, 2, 3)], 1, 1, 1))
```

## Validation Rules

- Lengths, radii, dimensions, and axes must be positive.
- Zero vectors cannot be normalized.
- Lines need distinct points for meaningful geometry.
- Triangles must be non-degenerate.
- Polygon vertices must be ordered and must enclose non-zero area.
- Division by zero raises the normal Python exception or a `ValueError`, depending on context.
- Relation helpers use a small numeric tolerance, so tangent checks are stable for floating-point calculations.

## Curriculum Coverage

GeomLib Advanced supports common CBSE, ICSE, and NCERT geometry topics:

- Class 10 coordinate geometry: distance, midpoint, section formula, slope, line equations
- Class 10 circle geometry: non-intersecting lines, tangents, secants, common points
- Class 10 mensuration: triangle, quadrilateral, circle, cube, cuboid, cylinder, cone, sphere
- Class 11 straight lines: slopes, angles, parallel/perpendicular checks, line equations
- Class 11 conic sections: circle, ellipse, parabola, hyperbola
- Class 11 introduction to 3D geometry: points and distance in 3D
- Class 12 vectors and 3D geometry: vectors, dot/cross product, lines, planes, angles, distances

## Development

Run tests:

```bash
python -m unittest discover -s tests
```

Build locally:

```bash
python -m build
```

Upload to PyPI after building and checking:

```bash
python -m twine check dist/*
python -m twine upload dist/*
```

## License

This project is licensed under the MIT License.

## Author

Arjun Singh Gangwar
