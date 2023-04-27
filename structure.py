import abc


from node2D_list import Node2DList
from node2D import Node2D
import dof_map


class Structure(metaclass=abc.ABCMeta):
    """
    The Structure class holds information to describe the physical
    representation of a structure.

    A structural model is typically defined by nodes, representing
    the support locations or structural discontinuities, and elements,
    which can represent structural members or portions of structural
    members, defined by nodal point boundaries.
    """
    elements = []
    node_loads = []

    def __init__(self, nodes: Node2DList, elements: list) -> None:
        self.nodes = nodes
        self.elements = elements
    
    def add_node(self, node: Node2D) -> None:
        self.nodes.append(node)
    
    def get_dof_map(self) -> list:
        return dof_map.DOF_Mapper().map(self)
    
    @property
    def get_num_elements(self):
        return len(self.elements)
    
    @property
    def get_num_nodes(self):
        return len(self.nodes)
    
    @abc.abstractmethod
    def add_node_load(self, node_id: int, fx: float, fy: float, mz: float) -> None:
        raise NotImplementedError()
    
    @abc.abstractproperty
    def dofs_per_node(self):
        raise NotImplementedError()
    
    @abc.abstractproperty
    def nodes_per_element(self):
        raise NotImplementedError()
