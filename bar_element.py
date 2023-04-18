from node2D import Node2D


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
    
    def k_local(self) -> list:
        """
        Returns the 2 x 2 stiffness matrix representing the bar element
        in the bar's local coordinates.
        """
        k = [
            [0 for i in range(2)]
            for i in range(2)
        ]

        k1 = self.area * self.elastic_mod / self.length

        k[0][0] = k1
        k[0][1] = -k1
        k[1][0] = -k1
        k[1][1] = k1

        return k
