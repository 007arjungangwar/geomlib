import math
from .point3d import Point3D

class Sphere:
    """Sphere class defined by center and radius."""
    
    def __init__(self, center: Point3D, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        
        self.center = center
        self.radius = float(radius)
    
    def volume(self) -> float:
        """Calculate volume."""
        return (4/3) * math.pi * self.radius**3
    
    def surface_area(self) -> float:
        """Calculate surface area."""
        return 4 * math.pi * self.radius**2
    
    def diameter(self) -> float:
        """Calculate diameter."""
        return 2 * self.radius
    
    def contains(self, point: Point3D) -> bool:
        """Check if sphere contains a point."""
        return self.center.distance_to(point) <= self.radius
    
    def intersects(self, other: 'Sphere') -> bool:
        """Check if spheres intersect."""
        distance = self.center.distance_to(other.center)
        return distance <= self.radius + other.radius
    
    def volume_intersection(self, other: 'Sphere') -> float:
        """Calculate volume of intersection with another sphere."""
        d = self.center.distance_to(other.center)
        r1, r2 = self.radius, other.radius
        
        if d >= r1 + r2:
            return 0.0
        if d <= abs(r1 - r2):
            return min(self.volume(), other.volume())
        
        # Formula for sphere-sphere intersection volume
        part1 = math.pi * (r1 + r2 - d)**2
        part2 = (d**2 + 2*d*(r1 + r2) - 3*(r1**2 + r2**2) + 6*r1*r2)
        return part1 * part2 / (12 * d)
    
    def scale(self, factor: float) -> 'Sphere':
        """Scale sphere radius."""
        return Sphere(self.center, self.radius * factor)
    
    def translate(self, dx: float, dy: float, dz: float) -> 'Sphere':
        """Translate sphere."""
        return Sphere(self.center.translate(dx, dy, dz), self.radius)
    
    def __repr__(self) -> str:
        return f"Sphere(center={self.center}, radius={self.radius})"