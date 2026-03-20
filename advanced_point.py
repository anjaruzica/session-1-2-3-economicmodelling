import math

from color_point import ColorPoint

class AdvancePoint(ColorPoint):
    # class variables, always in caps lock
    COLORS = ['red', 'green', 'blue', 'yellow', 'black', 'white']
    # call the init from ColorPoint
    def __init__(self, x, y, color):
        # check the color
        if not color in self.COLORS:
            raise ValueError(f'Invalid: Color must be one of {self.COLORS}')
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self): # this is a getter!
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value not in self.COLORS:
            raise ValueError(f'Invalid: Color must be one of {self.COLORS}')
        self._color = value

    @classmethod
    def add_color(cls, color):
        # add a new official color to the list
        cls.COLORS.append(color)

    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)**0.5

    @staticmethod
    def from_dict(d): # "factory" allows to create from a dictionary
        x = d['x']
        y = d['y']
        color = d['color']
        return AdvancePoint(x, y, color)

p0 = AdvancePoint.from_dict({'x':0, 'y':0, 'color':'red'})
p1 = AdvancePoint(1,2,'red')
print(p1)
p2 = AdvancePoint(3,4,'white')
print(p2)

# you call class methods via the class name instead of the instance name
AdvancePoint.add_color('coral')
p3 = AdvancePoint(4,5,'coral')
print(p3)
print(AdvancePoint.distance_2_points(p1, p3))