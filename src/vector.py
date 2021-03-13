"""
classes to represent Point and Vector

"""


import math

from abc import ABC
from typing import Iterable, Iterator, List, Union


Scalar = Union[int, float]


class AbstractPointVector(ABC):
    """Abstract Base Class for Vector2D and Point2D
    """
    EPSILON = 1e-14

    def __init__(self, *coords: Scalar) -> None:
        self._coords = list(coords)

    def __len__(self) -> int:
        return len(self._coords)

    def __iter__(self) -> Iterator:
        for coord in self._coords:
            yield coord

    def __eq__(self, other: 'AbstractPointVector') -> bool:
        """tests for equality between self and other

        :return: bool, True if self and other are equal, False otherwise
        """
        assert other is not None
        if not isinstance(other, type(self)) or len(self) != len(other):
            return False
        for self_c, other_c in zip(self, other):
            if not math.isclose(self_c, other_c, abs_tol=self.EPSILON):
                return False
        return True

    def __ne__(self, other: 'AbstractPointVector') -> bool:
        """tests for inequality between self and other

        :return: bool, False if self and other are equal, True otherwise
        """
        return not self == other

    def __hash__(self) -> int:
        """calculates and returns the generic python hash function

        uses the tuple (self.x, self.y)
        :return: int
        """
        return hash(tuple(self._coords))

    def __bool__(self) -> bool:
        """tests if the values of self are null/zero

        :return: bool, False when both values are zero, True otherwise
        """
        return not all(math.isclose(coord, 0, abs_tol=self.EPSILON) for coord in self._coords)

    def __str__(self):
        vals = [f'{v:.2f}' for v in self._coords]
        return f'{self.__class__.__name__}({", ".join(vals)})'

    def __repr__(self):
        vals = [str(v) for v in self._coords]
        return f'{self.__class__.__name__}({", ".join(vals)})'

    def clone(self) -> 'AbstractPointVector':
        """clones self and returns it

        :return: AbstractPointVector, clone of self
        """
        return self.__class__(*self._coords)

    def __iadd__(self, other: 'Vector') -> 'Point':
        """adds Vector other to self and returns self, mutated

        :param other: Vector
        :return: mutated Point self
        """
        if len(self) != len(other):
            raise ValueError("mismatched sizes of operands")
        if not isinstance(other, Vector):
            # Point += Point does not make sense
            # Vector += Point does not make sense
            raise TypeError("Can only mutate a Point or Vector via addition with a Vector")
        for idx, coord in enumerate(other._coords):
            self._coords[idx] += coord
        return self

    def __isub__(self, other: 'Vector') -> Union['Point', 'Vector']:
        """subtracts Vector other to self and returns self, mutated

        :param other: Vector
        :return: mutated Vector self
        """
        if len(self) != len(other):
            raise ValueError("mismatched sizes of operands")
        if not isinstance(other, Vector):
            # Vector -= Point does not make sense
            # Point -= Point does not make sense
            raise TypeError("Can only mutate a Vector or a Point by subtracting a Vector")
        for idx, coord in enumerate(other._coords):
            self._coords[idx] -= coord
        return self


class Vector(AbstractPointVector):

    def __add__(self, other: 'AbstractPointVector') -> 'AbstractPointVector':
        """returns a new Vector sum of self and other

        :param other: Vector2D
        :return: new Vector2D sum of self and other
        """
        if isinstance(other, Point):
            # Point + Vector = Point
            return other + self
        # Vector + Vector = Vector
        return self.__class__(*(self_c + other_c for self_c, other_c in zip(self, other)))

    def __sub__(self, other: 'Vector') -> 'Vector':
        """returns a new Vector the subtraction of other from self

        :param other: Vector
        :return: new Vector subtraction of other from self
        """
        if len(self) != len(other):
            raise ValueError("mismatched sizes of operands")
        if not isinstance(other, Vector):
            raise TypeError("can only subtract a Vector from a Vector")
        return self.__class__(*(self_c - other_c for self_c, other_c in zip(self, other)))

    def __neg__(self) -> 'Vector':
        """creates a new Vector2D, negative of self, and returns it

        :return: a new Vector2D, negative of self
        """
        return self.__class__(*(-coord for coord in self))

    def __mul__(self, scalar: float) -> 'Vector':
        """returns a new Vector2D equal to self scaled by scalar

        :param scalar: a Scalar
        :return: new Vector equal to self scaled by scalar
        """
        return self.__class__(*(coord * scalar for coord in self))

    def __rmul__(self, factor: Scalar) -> 'Vector':
        """returns a new Vector equal to self scaled by scalar

        :param factor: a Scalar
        :return: new Vector equal to self scaled by scalar
        """
        return self * factor


class Vector2D(Vector):

    def __init__(self, x: Scalar = 0.0, y: Scalar = 0.0) -> None:
        self.x = x
        self.y = y
        super().__init__(self.x, self.y)

    def __str__(self):
        return f'{self.__class__.__name__}(x={self.x :.2f}, y={self.y :.2f})'

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    # def __rmul__(self, factor: Scalar) -> 'Vector2D':
    #     """returns a new Vector2D equal to self scaled by scalar
    #
    #     :param factor: a Scalar
    #     :return: new Vector2D equal to self scaled by scalar
    #     """
    #     return self * factor

    def __imul__(self, factor: Scalar) -> 'Vector2D':
        """returns self scaled by scalar

        :param factor: a float
        :return: mutated self
        """
        self.x, self.y = self.x * factor, self.y * factor
        self._coords = [self.x, self.y]
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
        self._coords = [self.x, self.y]
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
        self._coords = [self.x, self.y]
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

    def isnull(self)-> bool:
        return not bool(self)


class Point(AbstractPointVector):

    def __add__(self, other: 'AbstractPointVector') -> 'AbstractPointVector':
        """returns a new Vector2D sum of self and other

        :param other: Vector2D
        :return: new Vector2D sum of self and other
        """
        if isinstance(other, Point):
            raise TypeError("cannot add two Point")
        elif not isinstance(other, Vector):
            raise NotImplementedError(f'addition of Point with {type(other)} is not implemented')
        if len(self) != len(other):
            raise ValueError("Incompatible operands sizes")
        return self.__class__(*(self_c + other_c for self_c, other_c in zip(self, other)))

    def __sub__(self, other: Union['Point', 'Vector']) -> Union['Point', 'Vector']:
        """calculates and returns the result of the subtraction of other from self

        @todo refactor type determination if possible - maybe extract function?
        @todo add Vector3D

        :param other: a 'Point' or a 'Vector'
        :return: a new 'Point' if other is a Vector
                 a new 'Vector' if other is a Point
        """
        if len(self) != len(other):
            raise ValueError("mismatched sizes of operands")
        if isinstance(other, Vector):
            return self.__class__(*(self_c - other_c for self_c, other_c in zip(self, other)))
        if isinstance(other, Point):
            tpe = Vector if len(self) > 2 else Vector2D
            return tpe(*(self_c - other_c for self_c, other_c in zip(self, other)))
        raise TypeError("Can only subtract a Point or a Vector from a Point")


class Point2D(Point):

    def __init__(self, x: Scalar = 0.0, y: Scalar = 0.0) -> None:
        self.x = x
        self.y = y
        super().__init__(self.x, self.y)

    def __str__(self):
        return f'{self.__class__.__name__}(x={self.x :.2f}, y={self.y :.2f})'

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

    # POINT
    #
    # def distance_from_point(self, other: 'Point') -> Number:
    #     """if both points are not the same dimension, the extra dimensions
    #     are dropped - i/e an orthogonal projection of the largest dimensional
    #     object is used
    #     """
    #     return math.sqrt(sum((selfv - otherv) ** 2 for selfv, otherv in zip(self, other)))
    #
    # def mid_point(self, other: 'Point') -> 'Point':
    #     return self.__class__(*((selfv + otherv) / 2 for selfv, otherv in zip(self, other)))


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

    p = Point(1, 2, 3, 4)
    v = Vector(1.0001, 2.009, 3.78987, 4.1)
    print(v)
    pp = p + v
    print(pp)
