

class Vector2D:

    def __init__(self, x: float =0, y: float =0)-> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        assert other is not None
        return self.x == other.x and self.y == other.y


if __name__ == '__main__':
    v = Vector2D()
