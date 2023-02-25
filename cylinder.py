import math
from math import pi
class cylinder :
    def __init__(self, reduis, height):
        self.reduis = reduis
        self.height = height

    def volume(self):
        return math.pi * self.reduis ** self.height