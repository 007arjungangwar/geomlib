import math
from .point import Point

class Rhombus:
    """Rhombus class (equilateral parallelogram)."""
    
    def __init__(self, center: Point, side: float, angle_deg: float):
        """
        Initialize rhombus.
        
        Args:
            center: Center point
            side: Side length
            angle_deg: Interior angle in degrees
        """
        if side <= 0:
            raise ValueError("Side must be positive")
        if not (0 < angle_deg < 180):
            raise ValueError("Angle must be between 0 and 180 degrees")
        
        self.center = center
        self.side = float(side)
        self.angle = math.radians(angle_deg)
        self.angle_deg = angle_deg
        
        # Calculate diagonals
        self.diag1 = 2 * self.side * math.cos(self.angle / 2)  # Longer diagonal
        self.diag2 = 2 * self.side * math.sin(self.angle / 2)  # Shorter diagonal
    
    def area(self) -> float:
        """Calculate area."""
        return (self.diag1 * self.diag2) / 2
    
    def perimeter(self) -> float:
        """Calculate perimeter."""
        return 4 * self.side
    
    def height(self) -> float:
        """Calculate height."""
        return self.side * math.sin(self.angle)
    
    def vertices(self) -> list:
        """Get vertices of rhombus."""
        # Vertices relative to center
        half_diag1 = self.diag1 / 2
        half_diag2 = self.diag2 / 2
        
        return [
            self.center.translate(0, half_diag1),  # Top
            self.center.translate(half_diag2, 0),  # Right
            self.center.translate(0, -half_diag1),  # Bottom
            self.center.translate(-half_diag2, 0)  # Left
        ]
    
    def contains(self, point: Point) -> bool:
        """Check if point is inside rhombus."""
        # Transform to local coordinates
        dx = point.x - self.center.x
        dy = point.y - self.center.y
        
        # Normalized coordinates
        nx = dx / (self.diag2 / 2)
        ny = dy / (self.diag1 / 2)
        
        return abs(nx) + abs(ny) <= 1
    
    def inscribed_circle_radius(self) -> float:
        """Calculate radius of inscribed circle."""
        return self.area() / self.perimeter() * 2
    
    def __repr__(self) -> str:
        return f"Rhombus(center={self.center}, side={self.side}, angle={self.angle_deg}°)"