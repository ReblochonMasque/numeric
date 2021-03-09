"""
from javidx9/splines
"""

from abc import ABC


class _VirtualVector(ABC):
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __iter__(self) -> float:
        yield self.x
        yield self.y

    def __mul__(self, scalar: float) -> '_VirtualVector':
        return self.__class__(self.x * scalar, self.y * scalar)

    def __str__(self) -> str:
        return f'{self.__class__.__qualname__}({self.x}, {self.y})'

    def __repr__(self) -> str:
        return str(self)


class Vector(_VirtualVector):
    """small class for vector arithmetic convenience
    """

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, vec: 'Vector') -> 'Vector':
        return Vector(self.x + vec.x, self.y + vec.y)

    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

    def norm(self) -> 'Vector':
        mag = self.magnitude()
        return Vector(self.x / mag, self.y / mag) if mag != 0 else Vector()

    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y

    def perp(self) -> 'Vector':
        return Vector(-self.y, self.x).norm()

    def cross(self, other):
        return (self.x * other.y) - (self.y * other.x)


class Point(_VirtualVector):
    """small class for point arithmetic convenience
    """

    def __sub__(self, other: 'Point') -> Vector:
        if other.__class__ is not Point:
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, vec: Vector) -> 'Point':
        return Point(self.x + vec.x, self.y + vec.y)


if __name__ == '__main__':

    import math
    import tkinter as tk
    from collections import deque


    def draw_direction_vector(canvas, anchor: Point, vec: Vector, _vid=[None]) -> None:
        """draws and updates the scaled normalized direction vector
        on the canvas.
        Keeps track of the id of the canvas item last drawn
        """
        if _vid[0] is not None:
            canvas.delete(_vid[0])
        normed_scaled_v = vec * 50
        end_point = anchor + normed_scaled_v
        _vid[0] = canvas.create_line(*anchor, *end_point, arrow=tk.LAST)


    _maxlen = 4

    def direction(event, _direct=deque([Point(0, 0) for _ in range(_maxlen)],
                                       maxlen=_maxlen)) -> None:
        """stores with_previous position, and uses it to calculate the direction
        from the current position.
        updates these variables
        """
        _direct.append(Point(event.x, event.y))
        p0, _, _, p1 = _direct    # skipping 2 points smoothens the movement a bit
        draw_direction_vector(canvas, p1, (p1 - p0).norm())

    root = tk.Tk()
    canvas = tk.Canvas(root, bg='cyan')
    canvas.pack()
    canvas.bind('<B1-Motion>', direction)
    root.mainloop()
