import unittest
from src import Vector2D


class TestVector2D(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(Vector2D(), Vector2D)


if __name__ == '__main__':
    unittest.main()
