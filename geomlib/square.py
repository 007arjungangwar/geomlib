from .point import Point
from .rectangle import Rectangle

class Square(Rectangle):
    """Square class (special case of rectangle)."""
    
    def __init__(self, bottom_left: Point, side: float):
        super().__init__(bottom_left, side, side)
        self.side = side
    
    @property
    def side_length(self) -> float:
        """Get side length."""
        return self.width
    
    def diagonal(self) -> float:
        """Calculate diagonal length."""
        return self.side * 2**0.5
    
    def inscribed_circle_radius(self) -> float:
        """Get radius of inscribed circle."""
        return self.side / 2
    
    def circumscribed_circle_radius(self) -> float:
        """Get radius of circumscribed circle."""
        return self.diagonal() / 2
    
    def __repr__(self) -> str:
        return f"Square(bottom_left={self.bottom_left}, side={self.side})"