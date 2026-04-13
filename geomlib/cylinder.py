import math
from .point3d import Point3D

class Cylinder:
    """Cylinder class defined by center, radius, and height."""
    
    def __init__(self, center: Point3D, radius: float, height: float):
        if radius <= 0 or height <= 0:
            raise ValueError("Radius and height must be positive")
        
        self.center = center
        self.radius = float(radius)
        self.height = float(height)
    
    def volume(self) -> float:
        """Calculate volume."""
        return math.pi * self.radius**2 * self.height
    
    def surface_area(self) -> float:
        """Calculate total surface area (including ends)."""
        lateral = 2 * math.pi * self.radius * self.height
        ends = 2 * math.pi * self.radius**2
        return lateral + ends
    
    def lateral_surface_area(self) -> float:
        """Calculate lateral surface area (excluding ends)."""
        return 2 * math.pi * self.radius * self.height
    
    def contains(self, point: Point3D) -> bool:
        """Check if point is inside cylinder."""
        # Check height range
        if abs(point.z - self.center.z) > self.height / 2:
            return False
        # Check radial distance
        dx = point.x - self.center.x
        dy = point.y - self.center.y
        return math.sqrt(dx**2 + dy**2) <= self.radius
    
    def scale(self, factor: float) -> 'Cylinder':
        """Scale cylinder uniformly."""
        return Cylinder(self.center, 
                       self.radius * factor,
                       self.height * factor)
    
    def __repr__(self) -> str:
        return f"Cylinder(center={self.center}, radius={self.radius}, height={self.height})"