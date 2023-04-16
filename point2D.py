import math


class Point2D:
    """
    The Point2D class represents a cartesian coordinate (x, y) point
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def distance_to(self, other: 'Point2D') -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
