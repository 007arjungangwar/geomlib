
"""
GeomLib - Advanced Geometry Library
A comprehensive library for 2D and 3D geometric computations.
"""

from .point import Point
from .line import Line
from .circle import Circle
from .square import Square
from .rectangle import Rectangle
from .rhombus import Rhombus
from .parallelogram import Parallelogram
from .triangle import Triangle
from .ellipse import Ellipse
from .point3d import Point3D
from .sphere import Sphere
from .cube import Cube
from .cuboid import Cuboid
from .cylinder import Cylinder
from .cone import Cone
from .vector import Vector2D, Vector3D
from .polygon import Polygon, regular_polygon
from .conics import Parabola, Hyperbola
from .analytics import Line3D, Plane, distance_between_points, section_formula
from .transformations import (
    translate_points,
    rotate_points,
    scale_points,
    reflect_point_x,
    reflect_point_y,
    reflect_point_origin,
    translate_points3d,
)
from .formulas import (
    degrees_to_radians,
    radians_to_degrees,
    pythagorean_hypotenuse,
    pythagorean_leg,
    heron_area,
    distance_2d,
    distance_3d,
    midpoint_2d,
)

__all__ = [
    'Point', 'Line', 'Circle', 'Square', 'Rectangle', 'Rhombus',
    'Parallelogram', 'Triangle', 'Ellipse', 'Point3D', 'Sphere',
    'Cube', 'Cuboid', 'Cylinder', 'Cone', 'Vector2D', 'Vector3D',
    'Polygon', 'regular_polygon', 'Parabola', 'Hyperbola', 'Line3D',
    'Plane', 'distance_between_points', 'section_formula',
    'translate_points', 'rotate_points', 'scale_points', 'reflect_point_x',
    'reflect_point_y', 'reflect_point_origin', 'translate_points3d',
    'degrees_to_radians', 'radians_to_degrees', 'pythagorean_hypotenuse',
    'pythagorean_leg', 'heron_area', 'distance_2d', 'distance_3d',
    'midpoint_2d'
]

__version__ = "0.1.1"
