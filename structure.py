from node2D import Node2D
from node2D_list import Node2DList
from beam_element import Beam2D
from structure_types import StructureType
import dof_map


class Structure:
    """
    The Structure class holds information to describe the physical
    representation of a structure.

    A structural model is typically defined by nodes, representing
    the support locations or structural discontinuities, and elements,
    which can represent structural members or portions of structural
    members, defined by nodal point boundaries.
    """
    elements = []

    def __init__(self, structure_type: StructureType, nodes: Node2DList, elements: list) -> None:
        self.__structure_type = structure_type
        self.nodes = nodes
        self.elements = elements
    
    def get_dof_map(self) -> list:
        return dof_map.DOF_Mapper().map(self)
    
    @property
    def get_num_elements(self):
        return len(self.elements)
    
    @property
    def get_num_nodes(self):
        return len(self.nodes)
    
    @property
    def max_dofs_per_node(self):
        """
        Returns the maximum dofs available per node in based on the type of structure.
        """
        if self.structure_type == StructureType.PLANE_TRUSS:
            return 2  # translation x, y
        elif self.__structure_type == StructureType.PLANE_FRAME:
            return 3  # translation x, y and rotation z
        elif self.__structure_type == StructureType.SPACE_TRUSS:
            return 3  # translation x, y, z
        else:  # Space Frame
            return 6  # translation and rotation x, y, z
    
    @property
    def structure_type(self):
        return self.__structure_type
