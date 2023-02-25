from math import pi
class circle:
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        area = self.redius ** 2 * pi
        return area
    def mohett(self):
        mohett = self.redius * 2 * pi
        return mohett
c1 = circle(34)
c2 = circle(45)
print(c1.area(), c2.mohett())




