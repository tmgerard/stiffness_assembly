from node2D import Node2D
import numpy as np


class Beam2D:
    """
    A beam element represents a beam with nodes defined at each end. The beam
    element utilizes all available degrees of freedom in a Node2D, so the beam
    can experience translation and rotation, resulting in deformations due
    to translation and rotation.

    The beam element will output a stiffness matrix in local or global
    coordinates that are assembled into the global stiffness matrix
    for the structure.
    """
    __MAX_DOFS = 6  # maybe track max dofs per node here instead of total nodes
                    # moving on to FEA, might require some plate type elements that
                    # only allow 2 dofs per node for example. When setting the
                    # node as member of an elemnent, the element could set the
                    # corresponding dof restraints.
    __ID = 0

    def __init__(self, start: Node2D, 
                 end: Node2D, 
                 area: float,        # cross-sectional area of beam element 
                 inertia_z: float,   # moment of inertia about z-axis
                 elastic_mod: float  # modulus of elasticity
                 ) -> None:
        self.start = start
        self.end = end
        self.area = area
        self.inertia_z = inertia_z
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
        Returns the 6 x 6 stiffness matrix representing the beam element
        in the beam's local coordinates.
        """
        # initialize the 6x6 stiffness matrix
        k = np.array([
            [0 for i in range(self.__MAX_DOFS)] 
            for i in range(self.__MAX_DOFS)
            ])
        
        k1 = self.area * self.elastic_mod / self.length
        k2 = 12 * self.elastic_mod * self.inertia_z / self.length ** 3
        k3 = 6 * self.elastic_mod * self.inertia_z / self.length ** 2
        k4 = 4 * self.elastic_mod * self.inertia_z / self.length
        k5 = 2 * self.elastic_mod * self.inertia_z / self.length
        
        k[0][0] = k1
        k[0][3] = -k1
        k[1][1] = k2
        k[1][2] = k3
        k[1][4] = -k2
        k[1][5] = -k3
        k[2][1] = k3
        k[2][2] = k4
        k[2][4] = -k3
        k[2][5] = k5
        k[3][0] = -k1
        k[3][3] = k1
        k[4][1] = -k2
        k[4][2] = -k3
        k[4][4] = k2
        k[4][5] = -k3
        k[5][1] = k3
        k[5][2] = k5
        k[5][4] = -k3
        k[5][5] = k4
        
        return k
