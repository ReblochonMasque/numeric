import math

from abc import ABC
from typing import Iterator, Union


class AbstractVector2D(ABC):

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    def __iter__(self) -> Iterator:
        yield self.x
        yield self.y

    def clone(self):
        """clones self and returns it

        :return: clone of self
        """
        return self.__class__(self.x, self.y)

    def __str__(self):
        return f'{self.__class__.__name__}(x={self.x :.2f}, y={self.y :.2f})'


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
        :return: self
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
        :return: self
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

    def __rmul__(self, other: float):
        """returns a new Vector2D equal to self scaled by scalar

        :param scalar: a float
        :return: new Vector2D equal to self scaled by scalar
        """
        return self * other

    def __imul__(self, scalar: float) -> 'Vector2D':
        """returns self scaled by scalar

        :param scalar: a float
        :return: self
        """
        self.x, self.y = self.x * scalar, self.y * scalar
        return self

    def __truediv__(self, scalar: float) -> 'Vector2D':
        """returns a new Vector2D equal to self scaled by scalar

        :param scalar: a float
        :return: new Vector2D equal to self divided by scalar
        """
        if scalar == 0:
            raise ValueError
        return Vector2D(self.x / scalar, self.y / scalar)

    def __itruediv__(self, scalar: float) -> 'Vector2D':
        """returns self divided by scalar

        :param scalar: a float
        :return: self
        """
        if scalar == 0:
            raise ValueError
        self.x, self.y = self.x / scalar, self.y / scalar
        return self

    def normalize(self) -> 'Vector2D':
        """normalizes self, and returns it

        :return: self
        """
        mag = self.magnitude()
        self.x, self.y = self.x / mag, self.y / mag
        return self

    def magnitude(self) -> float:
        """calculates and returns the magnitude of self

        :return: float equal to the magnitude of self
        """
        return math.hypot(self.x, self.y)


if __name__ == '__main__':

    a = Vector2D(2.12345, 3.9991)
    print(a)

    p0, p1 = Point2D(2, 4), Point2D(4, 2)
    print(p0-p1, p1-p0, p0+a, a+p0)
    a += p0-p1
    print(a)
    print(Point2D() + a)

    w = Vector2D(3, 4)
    print(w, w.magnitude())
    print(w.normalize())
