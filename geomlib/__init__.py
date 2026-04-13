
### Main Library Code
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

__all__ = [
    'Point', 'Line', 'Circle', 'Square', 'Rectangle', 'Rhombus',
    'Parallelogram', 'Triangle', 'Ellipse', 'Point3D', 'Sphere',
    'Cube', 'Cuboid', 'Cylinder', 'Cone'
]

__version__ = "1.0.0"