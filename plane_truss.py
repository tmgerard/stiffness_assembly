from structure import Structure
from node2D_list import Node2DList


class PlaneTruss(Structure):

    __MAX_DOFS_PER_NODE = 2
    __NODES_PER_ELEMENT = 2

    def __init__(self, nodes: Node2DList, elements: list) -> None:
        super().__init__(nodes, elements)
    
    @property
    def dofs_per_node(self):
        return self.__MAX_DOFS_PER_NODE
    
    @property
    def nodes_per_element(self):
        return self.__NODES_PER_ELEMENT
