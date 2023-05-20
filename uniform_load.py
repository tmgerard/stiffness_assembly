class UniformLoad:
    def __init__(self, load: float, dist_to_start: float, dist_to_end: float) -> None:
        self.load = load
        self.set_distance(dist_to_start, dist_to_end)

    def set_distance(self, dist_to_start: float, dist_to_end: float):
        """
        Set the distance to the start and end of a uniform load
        """
        if dist_to_start < 0 or dist_to_end > 1:
            raise ValueError('Distance must be a ratio of element length.')
        elif dist_to_start >= dist_to_end:
            raise ValueError('Distance to the beginning of uniform load' + \
                            'must be less than distance to the end of the load')
        else:
            self.__dist_to_start = dist_to_start
            self.__dist_to_end = dist_to_end
    
    def get_dist_to_start(self):
        """
        Returns the ratio of the distance from the start of the member to
        the beginning of the uniform load. A value of zero indicates that
        the load starts at the beginning of the beam element.
        """
        return self.__dist_to_start
    
    def get_dist_to_end(self):
        """
        Returns the ratio of the distance from the start of the member to
        the end of the uniform load. A value of one indicates that the
        load starts at the end of the beam element.
        """
        return self.__dist_to_end
