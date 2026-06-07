import math
from .point import Point

class Triangle:
    """Triangle class defined by three points."""
    
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c
        ab, bc, ca = self.side_lengths()
        if ab + bc <= ca or bc + ca <= ab or ca + ab <= bc:
            raise ValueError("Points must form a non-degenerate triangle")
    
    def side_lengths(self) -> tuple:
        """Calculate lengths of all sides."""
        ab = self.a.distance_to(self.b)
        bc = self.b.distance_to(self.c)
        ca = self.c.distance_to(self.a)
        return (ab, bc, ca)
    
    def area(self) -> float:
        """Calculate area using Heron's formula."""
        ab, bc, ca = self.side_lengths()
        s = (ab + bc + ca) / 2
        return math.sqrt(max(0.0, s * (s - ab) * (s - bc) * (s - ca)))
    
    def perimeter(self) -> float:
        """Calculate perimeter."""
        ab, bc, ca = self.side_lengths()
        return ab + bc + ca
    
    def angles(self) -> tuple:
        """Calculate all angles in degrees."""
        ab, bc, ca = self.side_lengths()
        
        angle_a = math.degrees(math.acos((ab**2 + ca**2 - bc**2) / (2 * ab * ca)))
        angle_b = math.degrees(math.acos((ab**2 + bc**2 - ca**2) / (2 * ab * bc)))
        angle_c = 180 - angle_a - angle_b
        
        return (angle_a, angle_b, angle_c)
    
    def is_equilateral(self) -> bool:
        """Check if triangle is equilateral."""
        ab, bc, ca = self.side_lengths()
        return math.isclose(ab, bc) and math.isclose(bc, ca)
    
    def is_isosceles(self) -> bool:
        """Check if triangle is isosceles."""
        ab, bc, ca = self.side_lengths()
        return (math.isclose(ab, bc) or 
                math.isclose(bc, ca) or 
                math.isclose(ca, ab))
    
    def is_right_angled(self) -> bool:
        """Check if triangle is right-angled."""
        sides = sorted(self.side_lengths())
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
    
    def centroid(self) -> Point:
        """Calculate centroid."""
        return Point((self.a.x + self.b.x + self.c.x) / 3,
                    (self.a.y + self.b.y + self.c.y) / 3)
    
    def circumcenter(self) -> Point:
        """Calculate circumcenter."""
        d = 2 * (self.a.x * (self.b.y - self.c.y) +
                self.b.x * (self.c.y - self.a.y) +
                self.c.x * (self.a.y - self.b.y))
        
        if d == 0:
            raise ValueError("Points are collinear")
        
        ux = ((self.a.x**2 + self.a.y**2) * (self.b.y - self.c.y) +
              (self.b.x**2 + self.b.y**2) * (self.c.y - self.a.y) +
              (self.c.x**2 + self.c.y**2) * (self.a.y - self.b.y)) / d
        
        uy = ((self.a.x**2 + self.a.y**2) * (self.c.x - self.b.x) +
              (self.b.x**2 + self.b.y**2) * (self.a.x - self.c.x) +
              (self.c.x**2 + self.c.y**2) * (self.b.x - self.a.x)) / d
        
        return Point(ux, uy)
    
    def incenter(self) -> Point:
        """Calculate incenter."""
        ab, bc, ca = self.side_lengths()
        perimeter = ab + bc + ca
        
        x = (bc * self.a.x + ca * self.b.x + ab * self.c.x) / perimeter
        y = (bc * self.a.y + ca * self.b.y + ab * self.c.y) / perimeter
        
        return Point(x, y)

    def circumradius(self) -> float:
        """Calculate circumradius."""
        ab, bc, ca = self.side_lengths()
        return ab * bc * ca / (4 * self.area())

    def inradius(self) -> float:
        """Calculate inradius."""
        return 2 * self.area() / self.perimeter()

    def orthocenter(self) -> Point:
        """Calculate orthocenter."""
        circumcenter = self.circumcenter()
        return Point(self.a.x + self.b.x + self.c.x - 2 * circumcenter.x,
                     self.a.y + self.b.y + self.c.y - 2 * circumcenter.y)
    
    def contains(self, point: Point) -> bool:
        """Check if point is inside triangle using barycentric coordinates."""
        denominator = ((self.b.y - self.c.y) * (self.a.x - self.c.x) +
                       (self.c.x - self.b.x) * (self.a.y - self.c.y))
        alpha = ((self.b.y - self.c.y) * (point.x - self.c.x) +
                 (self.c.x - self.b.x) * (point.y - self.c.y)) / denominator
        beta = ((self.c.y - self.a.y) * (point.x - self.c.x) +
                (self.a.x - self.c.x) * (point.y - self.c.y)) / denominator
        gamma = 1 - alpha - beta
        return alpha >= -1e-9 and beta >= -1e-9 and gamma >= -1e-9
    
    def __repr__(self) -> str:
        return f"Triangle({self.a}, {self.b}, {self.c})"
