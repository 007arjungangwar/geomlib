import math
from .point import Point

class Parallelogram:
    """Parallelogram class defined by base, side, and angle."""
    
    def __init__(self, base_point: Point, base_length: float, side_length: float, angle_deg: float):
        """
        Initialize parallelogram.
        
        Args:
            base_point: Starting point of base
            base_length: Length of base
            side_length: Length of side
            angle_deg: Angle between base and side in degrees
        """
        if base_length <= 0 or side_length <= 0:
            raise ValueError("Base and side lengths must be positive")
        if not (0 < angle_deg < 180):
            raise ValueError("Angle must be between 0 and 180 degrees")
        
        self.base_point = base_point
        self.base_length = float(base_length)
        self.side_length = float(side_length)
        self.angle_rad = math.radians(angle_deg)
        self.angle_deg = angle_deg
        
        # Calculate other vertices
        angle_rad = self.angle_rad
        self.p2 = Point(base_point.x + base_length, base_point.y)  # End of base
        self.p3 = Point(self.p2.x + side_length * math.cos(angle_rad),
                       self.p2.y + side_length * math.sin(angle_rad))  # Top right
        self.p4 = Point(base_point.x + side_length * math.cos(angle_rad),
                       base_point.y + side_length * math.sin(angle_rad))  # Top left
    
    def area(self) -> float:
        """Calculate area."""
        return self.base_length * self.height()
    
    def perimeter(self) -> float:
        """Calculate perimeter."""
        return 2 * (self.base_length + self.side_length)
    
    def height(self) -> float:
        """Calculate height."""
        return self.side_length * math.sin(self.angle_rad)
    
    def vertices(self) -> list:
        """Get all vertices."""
        return [self.base_point, self.p2, self.p3, self.p4]
    
    def center(self) -> Point:
        """Calculate center point."""
        return Point((self.base_point.x + self.p3.x) / 2,
                    (self.base_point.y + self.p3.y) / 2)
    
    def contains(self, point: Point) -> bool:
        """Check if point is inside parallelogram using barycentric coordinates."""
        v0 = self.p3 - self.base_point
        v1 = self.p4 - self.base_point
        v2 = point - self.base_point
        
        dot00 = v0.x * v0.x + v0.y * v0.y
        dot01 = v0.x * v1.x + v0.y * v1.y
        dot02 = v0.x * v2.x + v0.y * v2.y
        dot11 = v1.x * v1.x + v1.y * v1.y
        dot12 = v1.x * v2.x + v1.y * v2.y
        
        inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * inv_denom
        v = (dot00 * dot12 - dot01 * dot02) * inv_denom
        
        return (u >= 0) and (v >= 0) and (u + v <= 1)
    
    def __repr__(self) -> str:
        return f"Parallelogram(base_point={self.base_point}, base={self.base_length}, side={self.side_length}, angle={self.angle_deg}°)"