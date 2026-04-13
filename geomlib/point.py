import math
from typing import Union, Tuple

class Point:
    """2D Point class with various geometric operations."""
    
    def __init__(self, x: Union[int, float], y: Union[int, float]):
        self.x = float(x)
        self.y = float(y)
    
    def distance_to(self, other: 'Point') -> float:
        """Calculate Euclidean distance to another point."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def distance_to_origin(self) -> float:
        """Calculate distance from origin (0,0)."""
        return math.sqrt(self.x**2 + self.y**2)
    
    def midpoint(self, other: 'Point') -> 'Point':
        """Calculate midpoint between this point and another."""
        return Point((self.x + other.x)/2, (self.y + other.y)/2)
    
    def slope_to(self, other: 'Point') -> float:
        """Calculate slope of line to another point."""
        if self.x == other.x:
            raise ValueError("Vertical line - slope is undefined")
        return (other.y - self.y) / (other.x - self.x)
    
    def translate(self, dx: float, dy: float) -> 'Point':
        """Translate point by given deltas."""
        return Point(self.x + dx, self.y + dy)
    
    def rotate(self, angle_deg: float, center: 'Point' = None) -> 'Point':
        """Rotate point around center (default: origin)."""
        if center is None:
            center = Point(0, 0)
        
        angle_rad = math.radians(angle_deg)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        
        # Translate to origin
        x = self.x - center.x
        y = self.y - center.y
        
        # Rotate
        x_rot = x * cos_theta - y * sin_theta
        y_rot = x * sin_theta + y * cos_theta
        
        # Translate back
        return Point(x_rot + center.x, y_rot + center.y)
    
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Point':
        return Point(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar: float) -> 'Point':
        return Point(self.x / scalar, self.y / scalar)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def to_tuple(self) -> Tuple[float, float]:
        """Convert to tuple."""
        return (self.x, self.y)