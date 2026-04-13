import math
from typing import Tuple

class Point3D:
    """3D Point class with vector operations."""
    
    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def distance_to(self, other: 'Point3D') -> float:
        """Calculate Euclidean distance to another point."""
        return math.sqrt((self.x - other.x)**2 + 
                        (self.y - other.y)**2 + 
                        (self.z - other.z)**2)
    
    def distance_to_origin(self) -> float:
        """Calculate distance from origin."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def dot(self, other: 'Point3D') -> float:
        """Calculate dot product."""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: 'Point3D') -> 'Point3D':
        """Calculate cross product."""
        return Point3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def magnitude(self) -> float:
        """Calculate magnitude (length) of vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self) -> 'Point3D':
        """Return normalized unit vector."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Point3D(self.x / mag, self.y / mag, self.z / mag)
    
    def translate(self, dx: float, dy: float, dz: float) -> 'Point3D':
        """Translate point."""
        return Point3D(self.x + dx, self.y + dy, self.z + dz)
    
    def rotate_x(self, angle_deg: float) -> 'Point3D':
        """Rotate around X-axis."""
        angle_rad = math.radians(angle_deg)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        
        return Point3D(
            self.x,
            self.y * cos_theta - self.z * sin_theta,
            self.y * sin_theta + self.z * cos_theta
        )
    
    def rotate_y(self, angle_deg: float) -> 'Point3D':
        """Rotate around Y-axis."""
        angle_rad = math.radians(angle_deg)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        
        return Point3D(
            self.x * cos_theta + self.z * sin_theta,
            self.y,
            -self.x * sin_theta + self.z * cos_theta
        )
    
    def rotate_z(self, angle_deg: float) -> 'Point3D':
        """Rotate around Z-axis."""
        angle_rad = math.radians(angle_deg)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        
        return Point3D(
            self.x * cos_theta - self.y * sin_theta,
            self.x * sin_theta + self.y * cos_theta,
            self.z
        )
    
    def __add__(self, other: 'Point3D') -> 'Point3D':
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'Point3D') -> 'Point3D':
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar: float) -> 'Point3D':
        return Point3D(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar: float) -> 'Point3D':
        return Point3D(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point3D):
            return False
        return (math.isclose(self.x, other.x) and 
                math.isclose(self.y, other.y) and 
                math.isclose(self.z, other.z))
    
    def __repr__(self) -> str:
        return f"Point3D({self.x}, {self.y}, {self.z})"
    
    def to_tuple(self) -> Tuple[float, float, float]:
        """Convert to tuple."""
        return (self.x, self.y, self.z)