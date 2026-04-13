import math
from typing import Tuple
from .point import Point

class Rectangle:
    """Rectangle class defined by bottom-left corner, width, and height."""
    
    def __init__(self, bottom_left: Point, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        
        self.bottom_left = bottom_left
        self.width = float(width)
        self.height = float(height)
    
    @property
    def top_left(self) -> Point:
        """Get top-left corner."""
        return Point(self.bottom_left.x, self.bottom_left.y + self.height)
    
    @property
    def bottom_right(self) -> Point:
        """Get bottom-right corner."""
        return Point(self.bottom_left.x + self.width, self.bottom_left.y)
    
    @property
    def top_right(self) -> Point:
        """Get top-right corner."""
        return Point(self.bottom_left.x + self.width, self.bottom_left.y + self.height)
    
    @property
    def center(self) -> Point:
        """Get center point."""
        return Point(self.bottom_left.x + self.width/2, self.bottom_left.y + self.height/2)
    
    def area(self) -> float:
        """Calculate area."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate perimeter."""
        return 2 * (self.width + self.height)
    
    def diagonal(self) -> float:
        """Calculate diagonal length."""
        return math.sqrt(self.width**2 + self.height**2)
    
    def contains(self, point: Point) -> bool:
        """Check if rectangle contains a point."""
        return (self.bottom_left.x <= point.x <= self.bottom_left.x + self.width and
                self.bottom_left.y <= point.y <= self.bottom_left.y + self.height)
    
    def intersects(self, other: 'Rectangle') -> bool:
        """Check if rectangles intersect."""
        return not (self.bottom_left.x + self.width < other.bottom_left.x or
                   other.bottom_left.x + other.width < self.bottom_left.x or
                   self.bottom_left.y + self.height < other.bottom_left.y or
                   other.bottom_left.y + other.height < self.bottom_left.y)
    
    def intersection(self, other: 'Rectangle') -> 'Rectangle':
        """Get intersection rectangle."""
        if not self.intersects(other):
            return None
        
        x1 = max(self.bottom_left.x, other.bottom_left.x)
        y1 = max(self.bottom_left.y, other.bottom_left.y)
        x2 = min(self.bottom_left.x + self.width, other.bottom_left.x + other.width)
        y2 = min(self.bottom_left.y + self.height, other.bottom_left.y + other.height)
        
        return Rectangle(Point(x1, y1), x2 - x1, y2 - y1)
    
    def scale(self, factor: float) -> 'Rectangle':
        """Scale rectangle by factor (relative to center)."""
        center = self.center
        new_width = self.width * factor
        new_height = self.height * factor
        new_bottom_left = Point(center.x - new_width/2, center.y - new_height/2)
        return Rectangle(new_bottom_left, new_width, new_height)
    
    def translate(self, dx: float, dy: float) -> 'Rectangle':
        """Translate rectangle."""
        return Rectangle(self.bottom_left.translate(dx, dy), self.width, self.height)
    
    def __repr__(self) -> str:
        return f"Rectangle(bottom_left={self.bottom_left}, width={self.width}, height={self.height})"