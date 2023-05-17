from beam_element import Beam2D
from fixed_end_force_factory import fixed_end_force_factory


class ElementLoad():
    """
    Store for element and loading data. Returns the required equivalent
    nodal forces used to solve for the nodal displacements.
    """

    def __init__(self, element: Beam2D, load) -> None:
        self.element = element
        self.load = load

    def equivalent_nodal_shear_left(self):
        factory = fixed_end_force_factory(self)
        return factory.fixed_end_shear_left()
    
    def equivalent_nodal_shear_right(self):
        factory = fixed_end_force_factory(self)
        return factory.fixed_end_shear_right()
    
    def equivalent_nodal_moment_left(self):
        factory = fixed_end_force_factory(self)
        return factory.fixed_end_moment_left()
    
    def equivalent_nodal_moment_left(self):
        factory = fixed_end_force_factory(self)
        return factory.fixed_end_moment_right()
    
