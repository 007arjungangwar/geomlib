import math
from .point import Point

class Ellipse:
    """Ellipse class defined by center, semi-major axis, and semi-minor axis."""
    
    def __init__(self, center: Point, a: float, b: float):
        """
        Initialize ellipse.
        
        Args:
            center: Center point
            a: Semi-major axis (horizontal if a > b)
            b: Semi-minor axis
        """
        if a <= 0 or b <= 0:
            raise ValueError("Axes must be positive")
        
        self.center = center
        self.a = float(a)  # Semi-major axis
        self.b = float(b)  # Semi-minor axis
    
    def area(self) -> float:
        """Calculate area."""
        return math.pi * self.a * self.b
    
    def perimeter(self) -> float:
        """Calculate approximate perimeter using Ramanujan's formula."""
        h = ((self.a - self.b)**2) / ((self.a + self.b)**2)
        return math.pi * (self.a + self.b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
    
    def eccentricity(self) -> float:
        """Calculate eccentricity."""
        if self.a > self.b:
            return math.sqrt(1 - (self.b**2 / self.a**2))
        else:
            return math.sqrt(1 - (self.a**2 / self.b**2))
    
    def foci(self) -> tuple:
        """Calculate foci points."""
        if self.a > self.b:
            c = math.sqrt(self.a**2 - self.b**2)
            return (Point(self.center.x + c, self.center.y),
                    Point(self.center.x - c, self.center.y))
        else:
            c = math.sqrt(self.b**2 - self.a**2)
            return (Point(self.center.x, self.center.y + c),
                    Point(self.center.x, self.center.y - c))
    
    def contains(self, point: Point) -> bool:
        """Check if point is inside ellipse."""
        x_rel = point.x - self.center.x
        y_rel = point.y - self.center.y
        return (x_rel**2 / self.a**2 + y_rel**2 / self.b**2) <= 1
    
    def scale(self, factor: float) -> 'Ellipse':
        """Scale ellipse uniformly."""
        return Ellipse(self.center, self.a * factor, self.b * factor)
    
    def translate(self, dx: float, dy: float) -> 'Ellipse':
        """Translate ellipse."""
        return Ellipse(self.center.translate(dx, dy), self.a, self.b)
    
    def __repr__(self) -> str:
        return f"Ellipse(center={self.center}, a={self.a}, b={self.b})"