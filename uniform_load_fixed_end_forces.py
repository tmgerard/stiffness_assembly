from beam_element import Beam2D


class UniformFixedEndForces:
    """
    Uniform load applied to the full length of a beam element.
    """
    def __init__(self, beam: Beam2D, load: float) -> None:
        self.beam = beam
        self.load = load
    
    def fixed_end_moment_left(self):
        """
        Equivalent nodal moment on the left end of a fixed end beam.
        """
        return self.load * self.beam.length ** 2 / 12.0
    
    def fixed_end_moment_right(self):
        """
        Equivalent nodal moment on the right end of a fixed end beam.
        """
        return self.load * self.beam.length ** 2 / 12.0
    
    def fixed_end_shear_left(self):
        """
        Equivalent nodal shear force on the left end of a fixed end beam.
        """
        return self.load * self.beam.length / 2.0
    
    def fixed_end_shear_right(self):
        """
        Equivalent nodal shear force on the right end of a fixed end beam.
        """
        return self.load * self.beam.length / 2.0
