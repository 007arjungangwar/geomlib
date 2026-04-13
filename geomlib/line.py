import math
from typing import Optional, Union
from .point import Point

class Line:
    """Line class defined by two points or slope-intercept form."""
    
    def __init__(self, point1: Point, point2: Point):
        self.p1 = point1
        self.p2 = point2
        self._calculate_slope_intercept()
    
    def _calculate_slope_intercept(self):
        """Calculate slope and y-intercept."""
        if self.p1.x == self.p2.x:
            self.slope = None  # Vertical line
            self.intercept = self.p1.x
        else:
            self.slope = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
            self.intercept = self.p1.y - self.slope * self.p1.x
    
    def length(self) -> float:
        """Calculate length of line segment."""
        return self.p1.distance_to(self.p2)
    
    def slope_angle(self) -> float:
        """Calculate angle of line in degrees."""
        if self.slope is None:
            return 90.0
        return math.degrees(math.atan(self.slope))
    
    def is_vertical(self) -> bool:
        """Check if line is vertical."""
        return self.slope is None
    
    def is_horizontal(self) -> bool:
        """Check if line is horizontal."""
        return self.slope == 0 if self.slope is not None else False
    
    def is_parallel(self, other: 'Line') -> bool:
        """Check if lines are parallel."""
        if self.slope is None and other.slope is None:
            return True
        if self.slope is None or other.slope is None:
            return False
        return math.isclose(self.slope, other.slope)
    
    def is_perpendicular(self, other: 'Line') -> bool:
        """Check if lines are perpendicular."""
        if self.slope is None:
            return other.slope == 0 if other.slope is not None else False
        if other.slope is None:
            return self.slope == 0
        return math.isclose(self.slope * other.slope, -1.0)
    
    def intersection(self, other: 'Line') -> Optional[Point]:
        """Find intersection point with another line."""
        if self.is_parallel(other):
            return None
        
        if self.slope is None:  # Self is vertical
            x = self.intercept
            y = other.slope * x + other.intercept
            return Point(x, y)
        
        if other.slope is None:  # Other is vertical
            x = other.intercept
            y = self.slope * x + self.intercept
            return Point(x, y)
        
        x = (other.intercept - self.intercept) / (self.slope - other.slope)
        y = self.slope * x + self.intercept
        return Point(x, y)
    
    def distance_to_point(self, point: Point) -> float:
        """Calculate perpendicular distance from point to line."""
        if self.slope is None:  # Vertical line
            return abs(point.x - self.intercept)
        
        # Line in form: ax + by + c = 0
        a = self.slope
        b = -1
        c = self.intercept
        return abs(a * point.x + b * point.y + c) / math.sqrt(a**2 + b**2)
    
    def midpoint(self) -> Point:
        """Calculate midpoint of line segment."""
        return self.p1.midpoint(self.p2)
    
    def point_at_distance(self, distance: float, from_start: bool = True) -> Point:
        """Get point at specified distance along the line."""
        total_length = self.length()
        ratio = distance / total_length
        
        if not from_start:
            ratio = 1 - ratio
        
        x = self.p1.x + ratio * (self.p2.x - self.p1.x)
        y = self.p1.y + ratio * (self.p2.y - self.p1.y)
        return Point(x, y)
    
    def __repr__(self) -> str:
        if self.slope is None:
            return f"Line(x = {self.intercept})"
        return f"Line(y = {self.slope}x + {self.intercept})"