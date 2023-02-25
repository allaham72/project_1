from math import pi

from inhieretance.circle import circle


class Ball(circle):


    def volume(self):
        v = (3 / 4) * pi * self.redius ** 3
        return v

    def area(self):
        return 4 * pi * self.redius ** 2

    def print_area(self):
        print("the area is" + str(super().area()))
