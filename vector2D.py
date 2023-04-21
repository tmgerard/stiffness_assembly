import math


class Vector2D:
    """
    Defines a vector in two-dimensional space
    """
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def angle_value_to(self, other) -> float:
        """
        Returns the magnitude of the angle between two Vector2D objects
        """
        dot_product = self.dot(other)
        norm_product = self.norm * other.norm
        return math.acos(dot_product / norm_product)

    def angle_to(self, other) -> float:
        """
        Returns the angle from current Vector2D to a given Vector2D
        """
        return math.copysign(self.angle_value_to(other), self.cross(other))

    @property
    def cosine(self) -> float:
        """
        Direction cosine of current Vector2D
        """
        return self.u / self.norm

    def cross(self, other) -> float:
        """
        Calculates cross product assuming a "w" component of zero. Useful for determining angle between
        two vectors
        """
        return (self.u * other.v) - (self.v * other.u)

    def dot(self, other) -> float:
        """
        Calculates vector dot product
        """
        return (self.u * other.u) + (self.v * other.v)

    def is_parallel_to(self, other) -> bool:
        """
        Checks if a given Vector2D is parallel to the current Vector2D
        """
        return math.isclose(self.cross(other), 0.0, rel_tol=1e-09, abs_tol=0.0)

    def is_perpendicular_to(self, other) -> bool:
        """
        Checks if a given Vector2D is perpendicular to the current Vector2D
        """
        return math.isclose(self.dot(other), 0.0, rel_tol=1e-09, abs_tol=0.0)

    def projection_over(self, direction) -> float:
        """
        Projection of a vector in a given direction
        """
        return self.dot(direction.normalized())

    def rotated_by(self, angle) -> "Vector2D":
        """
        Returns a Vector2D that is the current Vector2D rotated by a given angle
        """
        cos = math.cos(angle)
        sin = math.sin(angle)
        return Vector2D(
            self.u * cos - self.v * sin,
            self.u * sin + self.v * cos
        )

    def scaled_by(self, factor) -> "Vector2D":
        """
        Scales vector by a given factor
        """
        return Vector2D(factor * self.u, factor * self.v)

    def sine(self) -> float:
        """
        Direction sine of current Vector2D
        """
        return self.v / self.norm

    @property
    def norm(self) -> float:
        """
        Length of the vector
        """
        return math.sqrt(self.u ** 2 + self.v ** 2)

    @property
    def is_normal(self) -> bool:
        """
        Checks if vector has unit length
        """
        return math.isclose(self.norm, 1.0, rel_tol=1e-09, abs_tol=0.0)

    def normalized(self) -> "Vector2D":
        """
        Returns vector of unit length in direction of the current Vector2D
        """
        return self.scaled_by(1.0 / self.norm)

    def opposite(self) -> "Vector2D":
        """
        Returns a Vector2D that is opposite in direction to the current Vector2D
        """
        return Vector2D(-self.u, -self.v)

    def perpendicular(self) -> "Vector2D":
        """
        Returns a Vector2D that is perpendicular to the current Vector2D
        """
        return Vector2D(-self.v, self.u)

    def with_length(self, length) -> "Vector2D":
        """
        Returns vector of a given length in direction of the current Vector2D
        """
        return self.normalized().scaled_by(length)

    def __add__(self, other) -> "Vector2D":
        return Vector2D(
            self.u + other.u,
            self.v + other.v
        )

    def __sub__(self, other) -> "Vector2D":
        return Vector2D(
            self.u - other.u,
            self.v - other.v
        )

    def __eq__(self, other) -> bool:
        if self is other:
            return True

        if not isinstance(other, Vector2D):
            return False

        return math.isclose(self.u, other.u, rel_tol=1e-09, abs_tol=0.0) and \
               math.isclose(self.v, other.v, rel_tol=1e-09, abs_tol=0.0)

    def __str__(self) -> str:
        return f'({self.u}, {self.v}) with norm {self.norm}'
