from .point3d import Point3D

class Cuboid:
    """Cuboid (rectangular prism) class."""
    
    def __init__(self, center: Point3D, length: float, width: float, height: float):
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        
        self.center = center
        self.length = float(length)
        self.width = float(width)
        self.height = float(height)
        self.half_length = length / 2
        self.half_width = width / 2
        self.half_height = height / 2
    
    def volume(self) -> float:
        """Calculate volume."""
        return self.length * self.width * self.height
    
    def surface_area(self) -> float:
        """Calculate surface area."""
        return 2 * (self.length*self.width + 
                   self.length*self.height + 
                   self.width*self.height)
    
    def space_diagonal(self) -> float:
        """Calculate space diagonal length."""
        return (self.length**2 + self.width**2 + self.height**2)**0.5
    
    def vertices(self) -> list:
        """Get all 8 vertices."""
        vertices = []
        for x in [-self.half_length, self.half_length]:
            for y in [-self.half_width, self.half_width]:
                for z in [-self.half_height, self.half_height]:
                    vertices.append(Point3D(self.center.x + x, 
                                           self.center.y + y, 
                                           self.center.z + z))
        return vertices
    
    def contains(self, point: Point3D) -> bool:
        """Check if point is inside cuboid."""
        return (abs(point.x - self.center.x) <= self.half_length and
                abs(point.y - self.center.y) <= self.half_width and
                abs(point.z - self.center.z) <= self.half_height)
    
    def scale(self, factor: float) -> 'Cuboid':
        """Scale cuboid uniformly."""
        return Cuboid(self.center, 
                     self.length * factor,
                     self.width * factor,
                     self.height * factor)
    
    def __repr__(self) -> str:
        return f"Cuboid(center={self.center}, length={self.length}, width={self.width}, height={self.height})"