from beam_element import Beam2D


class ElementLoad():
    """
    Store for element and loading data. Returns the required equivalent
    nodal forces used to solve for the nodal displacements.
    """

    def __init__(self, element: Beam2D, load) -> None:
        self.element = element
        self.load = load

    def equivalent_nodal_shear_left(self):
        raise NotImplementedError()
    
    def equivalent_nodal_shear_right(self):
        raise NotImplementedError()
    
    def equivalent_nodal_moment_left(self):
        raise NotImplementedError()
    
    def equivalent_nodal_moment_left(self):
        raise NotImplementedError()
    
