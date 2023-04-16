from point2D import Point2D


class Node2D:
    """
    The Node2D class represents a node on a planar structure located by
    cartesian coordinates. The node differs from a coordinate point in
    that it also keeps track of the constraints applied to the degrees
    of freedom. There are at most 3 degrees of freedom available on a node
    defined in a planar structure. Translation in the x and y directions
    and rotation about the z-axis.
    """

    """
    Represents the degrees of freedom.
      dofs[0] = translation along x-axis
      dofs[1] = translation along y-axis
      dofs[2] = rotation about z-axis
    """
    __dofs = []

    def __init__(self, origin: Point2D) -> None:
        self.origin = origin
        self.__dofs = [True, True, True]  # all degrees of freedom active
        self.__ID = 0
        self.__is_support = False
    
    def get_dof(self, dof_index) -> bool:
        """
        Returns a boolean value indicating if the given degree of
        freedom is active or not.

        0 => x translation DOF 
        1 => y translation DOF 
        2 => z rotation DOF
        """
        return self.__dofs[dof_index]
    
    def get_ID(self):
        """
        Returns the Node2D's ID
        """
        return self.__ID
    
    def set_ID(self, ID):
        """
        Set the Node2D's ID
        """
        self.__ID = ID
    
    def set_constraints(self, translate_x: bool, 
                        translate_y: bool, rotation_z: bool) -> None:
        """
        Sets DOFs as either active (True) or inactive (False)
        """
        self.__dofs = [translate_x, translate_y, rotation_z]

    def set_support_status(self, is_support: bool):
        """
        Defines the support status of the node. If True, the node inactive
        nodal degrees of freedom represent support constraints in the
        structural system.
        """
        self.__is_support = is_support
    
    def set_to_pin_support(self) -> None:
        """
        Deactivate translational DOFs and activate the rotational DOF 
        to model a node representing a pin-type support
        """
        self.__dofs = [False, False, True]
        self.__is_support = True
    
    def set_to_roller_support(self) -> None:
        """
        Deactivate the y direction DOF and activate remaining DOFs 
        to model a roller-type support
        """
        self.__dofs = [True, False, True]
        self.__is_support
