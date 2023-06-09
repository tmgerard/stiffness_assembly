from structure import Structure
from node2D import Node2D
from node2D_list import Node2DList
from node2D_load import Node2DLoad


class PlaneFrame(Structure):

    __MAX_DOFS_PER_NODE = 3
    __NODES_PER_ELEMENT = 2

    def __init__(self, nodes: Node2DList, elements: list) -> None:
        super().__init__(nodes, elements)
    
    def add_node_load(self, node_id: int, fx: float, fy: float, mz: float) -> None:
        self.node_loads.append(Node2DLoad(self.nodes[node_id], fx, fy, mz))
    
    @property
    def dofs_per_node(self):
        return self.__MAX_DOFS_PER_NODE
    
    @property
    def nodes_per_element(self):
        return self.__NODES_PER_ELEMENT
