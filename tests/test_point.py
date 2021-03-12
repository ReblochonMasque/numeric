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

    def test_equality_1(self):
        actual = Point2D(1, 0)
        expected = Point2D(1, 0)
        self.assertEqual(expected, actual)

    def test_equality_2(self):
        actual = Point2D(0, 1)
        expected = Point2D(0, 1)
        self.assertEqual(expected, actual)

    def test_inequality_0(self):
        self.assertNotEqual(Point2D(1, 0), Point2D(0, 1))

    def test_inequality_1(self):
        self.assertNotEqual(Point2D(-1, -7.35), Point2D(-1, 7.35))

    def test_hash_0(self):
        expected = hash((22.345, -176.09))
        actual = hash(Point2D(22.345, -176.09))
        self.assertEqual(expected, actual)

    def test_hash_1(self):
        expected = hash((0, 1))
        actual = hash(Point2D(0, 1))
        self.assertEqual(expected, actual)

    def test_hash_2(self):
        notexpected = hash((1, 0))
        actual = hash(Point2D(0, 1))
        self.assertNotEqual(notexpected, actual)

    def test_bool_0(self):
        self.assertTrue(Point2D(1, 12))

    def test_bool_1(self):
        self.assertFalse(Point2D(0, 0))

    def test_bool_2(self):
        self.assertTrue(Point2D(1, 0))

    def test_bool_3(self):
        self.assertTrue(Point2D(0, -2))


if __name__ == '__main__':
    unittest.main()
