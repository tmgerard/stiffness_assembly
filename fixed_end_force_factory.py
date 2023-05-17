from point_load import PointLoad2D
from point_load_fixed_end_forces import PointLoadFixedEndForces
from uniform_load_fixed_end_forces import UniformFixedEndForces


def fixed_end_force_factory(element_load):
    if type(element_load) is PointLoad2D:
        element_load: PointLoad2D
        return PointLoadFixedEndForces(element_load.element, element_load.load, element_load.get_distance())
    
    # add different load types when implemented