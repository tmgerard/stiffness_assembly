from node2D import Node2D


class Node2DList:
    """
    Wrapper for a list object that updates the IDs of the nodes stored
    when the objects are added or removed from the list.
    """
    def __init__(self) -> None:
        self.__nodes = []

    def append(self, node: Node2D) -> None:
        """
        Append the node to the list and set the node's ID
        """
        if not self.__nodes:
            node.set_ID = 0
            self.__nodes.append(node)
        else:
            last_node: Node2D
            last_node = self.__nodes[-1]
            node.set_ID(last_node.get_ID() + 1)
            self.__nodes.append(node)
    
    def pop(self, node_index: int) -> None:
        """
        Remove a node at a given index and update the node IDs
        """
        popped_node: Node2D
        popped_node = self.__nodes[node_index]
        popped_id = popped_node.get_ID()
        self.__nodes.pop(node_index)

        node: Node2D
        for node in self.__nodes:
            if node.get_ID() > popped_id:
                node.set_ID(node.get_ID() - 1)
    
    def __getitem__(self, key) -> Node2D:
        return self.__nodes[key]
    
    def __setitem__(self, key, value: Node2D):
        value.set_ID(key)  # the id should equal the list index
        self.__nodes[key] = value
    
    def __len__(self):
        return len(self.__nodes)
