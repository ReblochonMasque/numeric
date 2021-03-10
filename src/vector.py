"""
classes to represent Point2D and Vector2D

"""


import math

from abc import ABC
from typing import Iterator, Union


Scalar = Union[int, float]


class AbstractVector2D(ABC):
    EPSILON = 1e-14

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def __iter__(self) -> Iterator:
        yield self.x
        yield self.y

    def __eq__(self, other) -> bool:
        assert other is not None
        if not isinstance(other, type(self)):
            return False
        return math.isclose(self.x, other.x, abs_tol=self.EPSILON) and \
               math.isclose(self.y, other.y, abs_tol=self.EPSILON)

    def __ne__(self, other) -> bool:
        return not self == other

    def __str__(self):
        return f'{self.__class__.__name__}(x={self.x :.2f}, y={self.y :.2f})'

    def __repr__(self):
        return str(self)

    def clone(self):
        """clones self and returns it

        :return: clone of self
        """
        return self.__class__(self.x, self.y)


class Point2D(AbstractVector2D):

    def __add__(self, other: 'Vector2D') -> 'Point2D':
        """returns a new Vector2D sum of self and other

        can add Point2D with Vector2D, but not Point2D with Point2D
        :param other: Vector2D
        :return: new Vector2D sum of self and other
        """
        if not isinstance(other, Vector2D):
            raise TypeError
        return Point2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: 'Vector2D') -> 'Point2D':
        """adds other to self and returns self

        :param other: Vector2D
        :return: self
        """
        # if other.__class__.__name__ != 'Vector2D':
        if not isinstance(other, Vector2D):
            raise TypeError
        self.x, self.y = self.x + other.x, self.y + other.y
        return self

    def __sub__(self, other: Union['Point2D', 'Vector2D']) -> Union['Point2D', 'Vector2D']:
        """returns a new Vector2D sum of self and other

        :param other: Vector2D
        :return: new Vector2D sum of self and other
        """
        if isinstance(other, Vector2D):
            return Point2D(self.x - other.x, self.y - other.y)
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other: 'Vector2D') -> 'Point2D':
        """subs other from self and returns self

        :param other: Vector2D
        :return: self
        """
        if not isinstance(other, Vector2D):
            raise TypeError
        self.x, self.y = self.x - other.x, self.y - other.y
        return self


class Vector2D(AbstractVector2D):

    def __add__(self, other: Union['Point2D', 'Vector2D']) -> Union['Point2D', 'Vector2D']:
        """returns a new Vector2D sum of self and other

        :param other: Vector2D
        :return: new Vector2D sum of self and other
        """
        if isinstance(other, Point2D):
            return other + self
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: 'Vector2D') -> 'Vector2D':
        """adds other to self and returns it

        :param other: Vector2D
        :return: mutated self
        """
        if not isinstance(other, Vector2D):
            raise TypeError
        self.x, self.y = self.x + other.x, self.y + other.y
        return self

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        """returns a new Vector2D sub of self and other

        :param other: Vector2D
        :return: new Vector2D sub of self and other
        """
        if not isinstance(other, Vector2D):
            raise TypeError
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other: 'Vector2D') -> 'Vector2D':
        """subs other from self and returns it

        :param other: Vector2D
        :return: mutated self
        """
        if not isinstance(other, Vector2D):
            raise TypeError
        self.x, self.y = self.x - other.x, self.y - other.y
        return self

    def __neg__(self) -> 'Vector2D':
        """creates a new Vector2D, negative of self, and returns it

        :return: a new Vector2D, negative of self
        """
        return self.__class__(-self.x, -self.y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        """returns a new Vector2D equal to self scaled by scalar

        :param scalar: a float
        :return: new Vector2D equal to self scaled by scalar
        """
        return Vector2D(self.x * scalar, self.y * scalar)

    def __rmul__(self, factor: Scalar) -> 'Vector2D':
        """returns a new Vector2D equal to self scaled by scalar

        :param factor: a Scalar
        :return: new Vector2D equal to self scaled by scalar
        """
        return self * factor

    def __imul__(self, factor: Scalar) -> 'Vector2D':
        """returns self scaled by scalar

        :param factor: a float
        :return: mutated self
        """
        self.x, self.y = self.x * factor, self.y * factor
        return self

    def __truediv__(self, divisor: Scalar) -> 'Vector2D':
        """returns a new Vector2D equal to self scaled by divisor

        :param divisor: a Scalar
        :return: new Vector2D equal to self divided by divisor
        """
        if divisor == 0:
            raise ValueError
        return Vector2D(self.x / divisor, self.y / divisor)

    def __itruediv__(self, divisor: Scalar) -> 'Vector2D':
        """returns self divided by divisor

        :param divisor: a Scalar
        :return: mutated self
        """
        if divisor == 0:
            raise ValueError
        self.x, self.y = self.x / divisor, self.y / divisor
        return self

    def __floordiv__(self, divisor: Scalar) -> 'Vector2D':
        """returns a new Vector2D equal to self floor scaled by divisor

        :param divisor: a Scalar
        :return: new Vector2D equal to self floor divided by divisor
        """
        if divisor == 0:
            raise ValueError
        return Vector2D(self.x // divisor, self.y // divisor)

    def __ifloordiv__(self, divisor: Scalar) -> 'Vector2D':
        """returns self floor divided by divisor

        :param divisor: a Scalar
        :return: mutated self
        """
        if divisor == 0:
            raise ValueError
        self.x, self.y = self.x // divisor, self.y // divisor
        return self

    def unit(self) -> 'Vector2D':
        """calculates and returns the unique unit vector in the direction of self

        :return: new Vector2D
        """
        mag = abs(self)
        return self.__class__(self.x / mag, self.y / mag)

    def __abs__(self) -> Scalar:
        """calculates and returns the magnitude of self

        :return: Scalar equal to the magnitude of self
        """
        return math.hypot(self.x, self.y)
    mag = __abs__

    def perp(self) -> 'Vector2D':
        """2D Perp Operator

        calculates and returns a counterclockwise (ccw) normal vector to self

        :return: a new Vector2D normal to self, pointing to the left (ccw)
        """
        return self.__class__(-self.y, self.x)

    def dot(self, other: 'Vector2D') -> Scalar:
        """calculates and returns the dot product of self and other

        :param other: Vector2D
        :return: Scalar
        """
        return sum(c0 * c1 for c0, c1 in zip(self, other))

    def perp_product(self, other) -> Scalar:
        """2D exterior product, or outer product: ad-bc

        `v.perp(w) = abs(v) * abs(w) * sin(theta)`

        :param other: Vector2D
        :return: Scalar
        """
        return self.x * other.y - self.y * other.x


if __name__ == '__main__':

    # a = Vector2D(2.12345, 3.9991)
    # print(a)
    #
    # p0, p1 = Point2D(2, 4), Point2D(4, 2)
    # print(p0-p1, p1-p0, p0+a, a+p0)
    # a += p0-p1
    # print(a)
    # print(Point2D() + a)

    w = Vector2D(3, 4)
    print(w, w.mag())
    print(a := w.unit(), a.mag())
