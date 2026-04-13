import math
from .point3d import Point3D

class Cone:
    """Cone class defined by center, radius, and height."""
    
    def __init__(self, center: Point3D, radius: float, height: float):
        if radius <= 0 or height <= 0:
            raise ValueError("Radius and height must be positive")
        
        self.center = center
        self.radius = float(radius)
        self.height = float(height)
    
    def volume(self) -> float:
        """Calculate volume."""
        return (1/3) * math.pi * self.radius**2 * self.height
    
    def surface_area(self) -> float:
        """Calculate total surface area (including base)."""
        lateral = math.pi * self.radius * self.slant_height()
        base = math.pi * self.radius**2
        return lateral + base
    
    def lateral_surface_area(self) -> float:
        """Calculate lateral surface area (excluding base)."""
        return math.pi * self.radius * self.slant_height()
    
    def slant_height(self) -> float:
        """Calculate slant height."""
        return math.sqrt(self.radius**2 + self.height**2)
    
    def contains(self, point: Point3D) -> bool:
        """Check if point is inside cone."""
        # Check z coordinate range
        z_offset = point.z - self.center.z
        if z_offset < -self.height/2 or z_offset > self.height/2:
            return False
        
        # Calculate radius at this height
        if z_offset <= 0:
            # Bottom half - cone shape
            t = (self.height/2 + z_offset) / self.height
            radius_at_z = self.radius * (1 - t)
        else:
            # Top half - no cone
            return False
        
        # Check radial distance
        dx = point.x - self.center.x
        dy = point.y - self.center.y
        return math.sqrt(dx**2 + dy**2) <= radius_at_z
    
    def scale(self, factor: float) -> 'Cone':
        """Scale cone uniformly."""
        return Cone(self.center, 
                   self.radius * factor,
                   self.height * factor)
    
    def __repr__(self) -> str:
        return f"Cone(center={self.center}, radius={self.radius}, height={self.height})"