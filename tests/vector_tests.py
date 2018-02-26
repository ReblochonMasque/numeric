import unittest
from src import Vector2D


class TestVector2D(unittest.TestCase):

    def setUp(self):

        self.nullvector = Vector2D()
        self.unitx = Vector2D(1, 0)
        self.unity = Vector2D(0, 1)

    def test_instance(self):
        self.assertIsInstance(Vector2D(), Vector2D)

    def test_equality_null(self):
        other = Vector2D(0, 0)
        self.assertEqual(other, self.nullvector)

    def test_equality_unitx(self):
        other = Vector2D(1, 0)
        self.assertEqual(other, self.unitx)

    def test_equality_unity(self):
        other = Vector2D(0, 1)
        self.assertEqual(other, self.unity)


if __name__ == '__main__':
    unittest.main()
