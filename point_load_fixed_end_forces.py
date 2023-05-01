from beam_element import Beam2D


class PointLoadFixedEndForces:

    def __init__(self, beam: Beam2D,
                 load: float,
                 location_ratio: float) -> None:
        self.beam = beam
        self.load = load
        if location_ratio < 0.0 or location_ratio > 1.0:
            raise ValueError('Location of load must be a ratio of the length between 0 and 1')
        else:
            self.location = location_ratio
            # distance from beginning of beam element to point load
            self.a = self.beam.length * location_ratio
            # distance from point load to end of beam elememnt
            self.b = self.beam.length - self.a
    
    def fixed_end_moment_left(self):
        """
        Equivalent nodal moment on the left end of a fixed end beam.
        """
        return (self.load * self.a * self.b ** 2) / self.beam.length ** 2
    
    def fixed_end_moment_right(self):
        """
        Equivalent nodal moment on the right end of a fixed end beam.
        """
        return (self.load * self.a ** 2 * self.b) / self.beam.length ** 2
    
    def fixed_end_shear_left(self):
        """
        Equivalent nodal shear force on the left end of a fixed end beam.
        """
        return self.load * self.b ** 2 * (3.0 * self.a + self.b) / self.beam.length ** 3
    
    def fixed_end_shear_right(self):
        """
        Equivalent nodal shear force on the right end of a fixed end beam.
        """
        return self.load * self.a ** 2 * (self.a + 3.0 * self.b) / self.beam.length ** 3
