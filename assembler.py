import numpy as np


from beam_element import Beam2D
from node2D import Node2D
from structure import Structure


class Assembler:
    """
    Class takes a structure and assembles its degrees of freedom into a
    global stiffness matrix
    """
    def __init__(self, structure: Structure) -> None:
        self.structure = structure
        self.__dof_map = structure.get_dof_map()
    
    def assemble_k_global(self) -> list:
        """
        Assemble the global stiffness matrix and return the result
        """
        # find the number of active degrees of freedom
        num_dofs = max(max(x) for x in self.__dof_map)

        # initialize global stiffness matrix
        k_global = np.zeros((num_dofs, num_dofs))

        element: Beam2D
        for element in self.structure.elements:
            # calculate the elements stiffness matrix
            k_element = element.k_global()
            # obtain the element connectivity array
            con_array = self.get_connectivity_array(element)
            for i in range(len(con_array)):
                for j in range(len(con_array)):
                    if not con_array[i] == 0 and not con_array[j] == 0:
                        k_global[con_array[i] - 1][con_array[j] - 1] += k_element[i][j]        
        return k_global
    
    def assemble_load_vector(self) -> list:
        """
        Assemble the system load vector and return the result
        """
        # find the number of active degrees of freedom
        num_dofs = max(max(x) for x in self.__dof_map)

        # initialize the system load vector
        load_vec = np.zeros(num_dofs)

        # need to finish inmplementing load vector assembly
        pass
    
    def get_connectivity_array(self, element: Beam2D):
        con_array = []
        nodes = element.get_nodes()
        node: Node2D
        for node in nodes: # columns in map are node ids
            for dof in range(self.structure.dofs_per_node): # rows in map are dofs
                con_array.append(self.__dof_map[dof][node.get_ID()])
        
        return con_array

