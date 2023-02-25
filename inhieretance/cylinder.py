import math
from math import pi

from inhieretance.circle import circle


class Cylinder(circle):
    def __init__(self,reduis, height):
        super().__init__(reduis)
        self.height = height

    def volume(self):
        return math.pi * self.reduis ** self.height
    def area(self):
        return self.mohett() * self.height
    def area(self):
        return self.circ() * self.height
    def get_base(self):
        return super()
    def area_of_base(self):
        return super().area()
