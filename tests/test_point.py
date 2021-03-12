import unittest

from numeric.src.vector import Point2D


class TestAbstractVector2DWithPoint2D(unittest.TestCase):

    def test_instance_0(self):
        self.assertIsInstance(Point2D(), Point2D)


if __name__ == '__main__':
    unittest.main()
