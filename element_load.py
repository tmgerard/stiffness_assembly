import abc


class ElementLoad(metaclass=abc.ABCMeta):
    """
    Abstract class defining the require outputs needed to
    assemble the fixed end moment vector for members with
    loadings between node locations.
    """

    @abc.abstractclassmethod
    def equivalent_nodal_shear_left():
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def equivalent_nodal_shear_right():
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def equivalent_nodal_moment_left():
        raise NotImplementedError()
    
    @abc.abstractclassmethod
    def equivalent_nodal_moment_left():
        raise NotImplementedError()
    
