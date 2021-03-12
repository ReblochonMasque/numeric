import unittest

from numeric.src.vector import Point2D


class TestAbstractVector2DWithPoint2D(unittest.TestCase):

    def test_instance_0(self):
        self.assertIsInstance(Point2D(), Point2D)

    def test_instance_1(self):
        self.assertIsInstance(Point2D(x=2.2, y=-3.7), Point2D)

    def test_iter_0(self):
        expecteds = (3.2, 7.3)
        actuals = Point2D(3.2, 7.3)
        for expected, actual in zip(expecteds, actuals):
            self.assertEqual(expected, actual)

    def test_iter_1(self):
        expected_x, expected_y = (3.2, 7.3)
        actual_x, actual_y = Point2D(3.2, 7.3)
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_equality_origin(self):
        actual = Point2D()
        expected = Point2D(0, 0)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
