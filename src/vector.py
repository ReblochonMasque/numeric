
import math


class Vector2D:

    EPSILON = 1e-14

    def __init__(self, x: float =0, y: float =0, epsilon: float =EPSILON)-> None:
        self.x = x
        self.y = y
        self.v = (self.x, self.y)
        self.epsilon = epsilon

    def __eq__(self, other):
        assert other is not None
        return math.isclose(self.x, other.x, abs_tol=self.epsilon) and \
               math.isclose(self.y, other.y, abs_tol=self.epsilon)

    def __getitem__(self, ndx):
        return self.v[ndx]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)


if __name__ == '__main__':
    v = Vector2D()
