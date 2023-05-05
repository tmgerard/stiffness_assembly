from node2D import Node2D


class Node2DLoad:

    __loads = [0, 0, 0]

    def __init__(self, node: Node2D, force_x: float, force_y: float, moment_z: float):
        self.node = node
        self.__loads[0] = force_x
        self.__loads[1] = force_y
        self.__loads[2] = moment_z
    
    def set_loads(self, force_x: float, force_y: float, moment_z: float):
        self.__loads[0] = force_x
        self.__loads[1] = force_y
        self.__loads[2] = moment_z
    
    def set_node(self, node: Node2D):
        self.node = node
    
    def __getitem__(self, key) -> float:
        """
        Returns the load at the correspnding degree of freedom.\n
        0 -> Fx\n
        1 -> Fy\n
        2 -> Mz
        """
        return self.__loads[key]
    
    def __setitem__(self, key, value: float):
        """
        Sets the load at the corresponding degree of freedom\n
        0 -> Fx\n
        1 -> Fy\n
        2 -> Mz
        """
        self.__loads[key] = value
