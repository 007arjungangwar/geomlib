import math
from typing import Optional
from .point import Point

class Circle:
    """Circle class defined by center and radius."""
    
    def __init__(self, center: Point, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        
        self.center = center
        self.radius = float(radius)
    
    def area(self) -> float:
        """Calculate area."""
        return math.pi * self.radius**2
    
    def perimeter(self) -> float:
        """Calculate circumference."""
        return 2 * math.pi * self.radius
    
    def diameter(self) -> float:
        """Calculate diameter."""
        return 2 * self.radius
    
    def contains(self, point: Point) -> bool:
        """Check if circle contains a point."""
        return self.center.distance_to(point) <= self.radius
    
    def intersects(self, other: 'Circle') -> bool:
        """Check if circles intersect."""
        distance = self.center.distance_to(other.center)
        return distance <= self.radius + other.radius
    
    def intersection_area(self, other: 'Circle') -> float:
        """Calculate intersection area with another circle."""
        d = self.center.distance_to(other.center)
        
        if d >= self.radius + other.radius:
            return 0.0
        if d <= abs(self.radius - other.radius):
            return min(self.area(), other.area())
        
        r1, r2 = self.radius, other.radius
        part1 = r1**2 * math.acos((d**2 + r1**2 - r2**2) / (2 * d * r1))
        part2 = r2**2 * math.acos((d**2 + r2**2 - r1**2) / (2 * d * r2))
        part3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
        
        return part1 + part2 - part3
    
    def tangent_points(self, external_point: Point) -> tuple:
        """Find tangent points from an external point."""
        distance = self.center.distance_to(external_point)
        if distance < self.radius:
            raise ValueError("Point is inside circle, no tangents")
        
        if distance == self.radius:
            return (external_point,)
        
        # Angle between center-to-point line and tangent line
        angle = math.asin(self.radius / distance)
        direction = math.atan2(external_point.y - self.center.y, 
                              external_point.x - self.center.x)
        
        angle1 = direction + angle
        angle2 = direction - angle
        
        p1 = Point(self.center.x + self.radius * math.cos(angle1),
                   self.center.y + self.radius * math.sin(angle1))
        p2 = Point(self.center.x + self.radius * math.cos(angle2),
                   self.center.y + self.radius * math.sin(angle2))
        
        return (p1, p2)
    
    def scale(self, factor: float) -> 'Circle':
        """Scale circle radius by factor."""
        return Circle(self.center, self.radius * factor)
    
    def translate(self, dx: float, dy: float) -> 'Circle':
        """Translate circle."""
        return Circle(self.center.translate(dx, dy), self.radius)
    
    def __repr__(self) -> str:
        return f"Circle(center={self.center}, radius={self.radius})"