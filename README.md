# GeomLib Advanced

GeomLib Advanced is a pure-Python geometry toolkit for 2D and 3D mathematical work. It is designed for students, teachers, competitive programming, simulations, graphics prototypes, CAD-style utilities, and backend services that need dependable geometry formulas without a heavy dependency stack.

## Features

### 2D geometry

- Points, vectors, lines, circles, triangles, rectangles, squares, rhombuses, parallelograms, ellipses, polygons
- Area, perimeter, centroid, midpoint, slope, angle, distance, containment, intersections
- Coordinate geometry helpers including distance and section formula
- Transformations including translate, rotate, scale, and reflection

### Conic sections

- Circle and ellipse support
- Parabola with focus, directrix, latus rectum, parametric points
- Hyperbola with foci, eccentricity, asymptotes, point checks

### 3D geometry

- Point3D, Vector3D, Line3D, Plane
- Sphere, cube, cuboid, cylinder, cone
- Volume, surface area, space diagonal, containment
- Dot product, cross product, scalar triple product, projections, angles
- Distances between 3D points, points and lines, points and planes, and skew lines

### Formula helpers

- Pythagorean theorem
- Heron's formula
- Degree/radian conversion
- 2D and 3D distance formulas
- Midpoint formula

## Installation

```bash
pip install geomlib-advanced
```

From source:

```bash
git clone https://github.com/007arjungangwar/geomlib.git
cd geomlib
pip install .
```

## Quick Start

```python
from geomlib import (
    Circle,
    Line3D,
    Plane,
    Point,
    Point3D,
    Polygon,
    Triangle,
    Vector2D,
    Vector3D,
    section_formula,
)

circle = Circle(Point(0, 0), 5)
print(circle.area())
print(circle.perimeter())

triangle = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
print(triangle.area())
print(triangle.incenter())
print(triangle.circumradius())

polygon = Polygon([Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)])
print(polygon.area())
print(polygon.centroid())

vector = Vector2D(3, 4)
print(vector.magnitude())
print(vector.angle_with(Vector2D(1, 0)))

point = section_formula(Point(0, 0), Point(6, 6), 1, 2)
print(point)

line = Line3D(Point3D(0, 0, 0), Vector3D(1, 1, 1))
plane = Plane.from_point_normal(Point3D(0, 0, 2), Vector3D(0, 0, 1))
print(plane.line_intersection(line))
```

## Curriculum Coverage

The library includes formulas and objects commonly used across school-level and early college geometry:

- Class 10 coordinate geometry: distance, midpoint, section formula, slope, line equations
- Class 10 mensuration: circle, rectangle, square, triangle, cylinder, cone, sphere, cuboid, cube
- Class 11 straight lines and conic sections: line relations, parabola, ellipse, hyperbola
- Class 11 introduction to 3D geometry: 3D points and distance
- Class 12 vectors and 3D geometry: vectors, dot/cross products, lines, planes, angles, distances

## API Highlights

```python
from geomlib import Parabola, Hyperbola

parabola = Parabola(Point(0, 0), 2, orientation="up")
print(parabola.focus())
print(parabola.directrix())

hyperbola = Hyperbola(Point(0, 0), 3, 2)
print(hyperbola.eccentricity())
print(hyperbola.asymptotes())
```

```python
from geomlib import Plane, Point3D, Vector3D

plane = Plane.from_points(
    Point3D(0, 0, 0),
    Point3D(1, 0, 0),
    Point3D(0, 1, 0),
)
print(plane.distance_to_point(Point3D(0, 0, 5)))
```

## Development

Run tests:

```bash
python -m unittest discover -s tests
```

Build locally:

```bash
python -m build
```

## License

This project is licensed under the MIT License.

## Author

Arjun Singh Gangwar
