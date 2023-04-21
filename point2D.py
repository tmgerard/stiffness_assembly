import math

from vector2D import Vector2D


class Point2D:
    """
    The Point2D class represents a cartesian coordinate (x, y) point
    """
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def distance_to(self, other: 'Point2D') -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
    
    def __sub__(self, other: 'Point2D') -> Vector2D:
        return Vector2D(
            self.x - other.x,
            self.y - other.y
        )
    
    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, Point2D):
            return False

        return math.isclose(self.x, other.x, rel_tol=1e-09, abs_tol=0.0) and \
               math.isclose(self.y, other.y, rel_tol=1e-09, abs_tol=0.0)

    def __str__(self):
        return f'({self.x}, {self.y})'
