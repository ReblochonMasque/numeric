
from abc import ABC
from fractions import Fraction
import math
import typing


Number = typing.Union[int, float, complex, Fraction]
VectorType = typing.Union['Vector', 'Point', 'Normal']


class Vec(ABC):
    """represents Points, Vectors and Normals in the plane"""

    def __init__(self, x: Number=0, y: Number=0):
        self.x: Number = x
        self.y: Number = y

    def __sub__(self, p: ['Point', 'Vector'])-> 'Vector':
        return Vector(self.x - p.x, self.y - p.y)

    def isnull(self)-> bool:
        return math.isclose(self.x, 0) and math.isclose(self.y, 0)

    def __str__(self)-> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class Vector(Vec):
    pass


class Point(Vec):
    """a position vector anchored at origin"""
    pass


class Normal(Vec):
    def __init__(self, vector: Vector):
        assert not vector.isnull(), 'there is no Normal to a null Vector'
        x, y = vector.x, vector.y

        if math.isclose(x, 0):
            x = 1
            y = 0
        elif math.isclose(y, 0):
            x = 0
            y = 1
        super().__init__(-y, x)


if __name__ == '__main__':

    a = Point(1, 2)
    b = Point(5, -2)
    v = Vector(-1, -1)
    vn = Normal(v)

    print(a, b, b-a, v, vn)

    print(isinstance(v, Vector), isinstance(v, Vec), isinstance(v, Point), isinstance(v, Normal))
    print(isinstance(b-a, Vector), isinstance(b-a, Vec), isinstance(b-a, Point), isinstance(b-a, Normal))
    print(isinstance(b, Vector), isinstance(b, Vec), isinstance(b, Point), isinstance(b, Normal))
    print(isinstance(vn, Vector), isinstance(vn, Vec), isinstance(vn, Point), isinstance(vn, Normal))
