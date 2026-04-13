from .point3d import Point3D

class Cube:
    """Cube class defined by center and side length."""
    
    def __init__(self, center: Point3D, side: float):
        if side <= 0:
            raise ValueError("Side must be positive")
        
        self.center = center
        self.side = float(side)
        self.half_side = side / 2
    
    def volume(self) -> float:
        """Calculate volume."""
        return self.side**3
    
    def surface_area(self) -> float:
        """Calculate surface area."""
        return 6 * self.side**2
    
    def space_diagonal(self) -> float:
        """Calculate space diagonal length."""
        return self.side * 3**0.5
    
    def vertices(self) -> list:
        """Get all 8 vertices."""
        hs = self.half_side
        vertices = []
        for x in [-hs, hs]:
            for y in [-hs, hs]:
                for z in [-hs, hs]:
                    vertices.append(Point3D(self.center.x + x, 
                                           self.center.y + y, 
                                           self.center.z + z))
        return vertices
    
    def contains(self, point: Point3D) -> bool:
        """Check if point is inside cube."""
        return (abs(point.x - self.center.x) <= self.half_side and
                abs(point.y - self.center.y) <= self.half_side and
                abs(point.z - self.center.z) <= self.half_side)
    
    def inscribed_sphere_radius(self) -> float:
        """Get radius of inscribed sphere."""
        return self.half_side
    
    def circumscribed_sphere_radius(self) -> float:
        """Get radius of circumscribed sphere."""
        return self.space_diagonal() / 2
    
    def scale(self, factor: float) -> 'Cube':
        """Scale cube by factor."""
        return Cube(self.center, self.side * factor)
    
    def __repr__(self) -> str:
        return f"Cube(center={self.center}, side={self.side})"
    