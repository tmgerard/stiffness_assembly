class PointLoad2D:
    def __init__(self, force: float, distance: float) -> None:
        self.force = force
        self.set_distance(distance)
    
    def set_distance(self, distance: float):
        """
        Set the distance as a ratio of the element's length. Zero
        indicates the start of the element, and one indicates the
        end of an element.
        """
        if distance < 0 or distance > 1:
            raise ValueError('Distance must be a ratio of element length.')
        else:
            self.__distance = distance
    
    def get_distance(self):
        return self.__distance
