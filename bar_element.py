import numpy as np
import math


from node2D import Node2D
from vector2D import Vector2D


class Bar2D:
    """
    A bar element represents an axial-force memeber with nodes defined
    at each end, utilizing only translational degrees of freedom in a
    Node2D.

    The bar element will output a stiffness matrix in local or global
    coordinates that are assembled into the global stiffness matrix
    for that structure.
    """

    __ID = 0
    __MAX_DOFS = 4

    def __init__(self, start: Node2D,
                 end: Node2D,
                 area: float,
                 elastic_mod: float) -> None:
        self.start = start
        self.end = end
        self.area = area
        self.elastic_mod = elastic_mod
    
    @property
    def length(self) -> float:
        return self.start.origin.distance_to(self.end.origin)
    
    def get_nodes(self) -> list:
        return [self.start, self.end]
    
    def get_ID(self):
        return self.__ID
    
    def set_ID(self, id):
        self.__ID = id
    
    def k_local(self):
        """
        Returns the 2 x 2 stiffness matrix representing the bar element
        in the bar's local coordinates.
        """
        k = np.zeros((2, 2))

        k1 = self.area * self.elastic_mod / self.length

        k[0][0] = k1
        k[0][1] = -k1
        k[1][0] = -k1
        k[1][1] = k1

        return k
    
    def k_global(self):
        """
        Returns the 4 x 4 stiffness matrix representing the bar element
        in global coordinates
        """
        vec: Vector2D
        vec = Vector2D(1, 0)  # unit vector along global x-axis
        angle = vec.angle_to(self.end.origin - self.start.origin)

        c = math.cos(angle)

        # correct any rounding errors
        if math.isclose(c, 0.0, rel_tol=1e-09, abs_tol=0.0):
            c = 0.0
        if math.isclose(c, 1.0, rel_tol=1e-09, abs_tol=0.0):
            c = 1.0
        
        s = math.sin(angle)

        # correct any rounding errors
        if math.isclose(s, 0.0, rel_tol=1e-09, abs_tol=0.0):
            s = 0.0
        if math.isclose(s, 1.0, rel_tol=1e-09, abs_tol=0.0):
            s = 1.0
        
        k = np.zeros((self.__MAX_DOFS, self.__MAX_DOFS))

        k1 = self.area * self.elastic_mod / self.length

        k[0][0] = k1 * c ** 2
        k[0][1] = k1 * s * c
        k[0][2] = -k1 * c ** 2
        k[0][3] = -k1 * s * c
        k[1][0] = k1 *s * c
        k[1][1] = k1 * s ** 2
        k[1][2] = -k1 * s * c
        k[1][3] = -k1 * s ** 2
        k[2][0] = -k1 * c ** 2
        k[2][1] = -k1 * s * c
        k[2][2] = k1 * c ** 2
        k[2][3] = k1 * s * c
        k[3][0] = -k1 * s * c
        k[3][1] = -k1 * s ** 2
        k[3][2] = k1 * s * c
        k[3][3] = k1 * s ** 2

        return k
