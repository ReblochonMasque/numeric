"""
Tests for geometry.Point
"""


from fractions import Fraction
import math
from src.geometry import Point
from src.geometry import Point2D
import unittest

import io
from contextlib import redirect_stdout


class TestPoint(unittest.TestCase):

    def setUp(self):

        self.origin = Point()
        self.p1 = Point(x=1, y=2)
        self.p2 = Point(x=2, y=3)
        self.p3 = Point(x=2, y=3, z=1)
        self.pf1 = Point(x=Fraction(1, 2), y=Fraction(1, 2))
        self.pf2 = Point(x=Fraction(3, 2), y=Fraction(3, 2))

    def test_instance(self):
        self.assertIsInstance(self.p1, Point)
        self.assertIsInstance(self.p2, Point)
        self.assertIsInstance(self.p3, Point)
        self.assertIsInstance(self.pf1, Point)

    def test_iter(self):
        self.assertEqual([val for val in self.p1], [1, 2, 0])
        self.assertEqual([val for val in self.pf1], [0.5, 0.5, 0])

    def test_hash(self):
        self.assertEqual(hash(tuple(val for val in self.p1)), hash(self.p1))
        self.assertEqual(hash(tuple(val for val in self.pf1)), hash(self.pf1))

    def test_equal(self):
        p1 = Point(*(1, 2))
        self.assertEqual(self.p1, p1)

    def test_equal_f(self):
        pf2 = Point(*(Fraction(6, 4), Fraction(6, 4)))
        self.assertEqual(self.pf2, pf2)

    def test_not_equal(self):
        self.assertNotEqual(self.p1, self.p2)

    def test_not_equal_f(self):
        self.assertNotEqual(self.pf1, self.pf2)

    def test_addition_1(self):
        expected = Point(*(3, 5, 0))
        actual = self.p1 + self.p2
        self.assertEqual(actual, expected)

    def test_addition_2(self):
        expected = Point(*(4, 6, 1))
        actual = self.p2 + self.p3
        self.assertEqual(actual, expected)

    def test_addition_3_f(self):
        expected_real = Point(*(2.5, 2.5, 0))
        actual = self.pf1 + self.pf2 + self.pf1
        self.assertEqual(actual, expected_real)

    def test_addition_4_f(self):
        expected_fraction = Point(*(Fraction(5, 2), Fraction(5, 2), 0))
        actual = self.pf1 + self.pf2 + self.pf1
        self.assertEqual(actual, expected_fraction)

    def test_addition_4(self):
        expected = Point(*(2, 2, 0))
        actual = self.pf1 + self.pf2
        self.assertEqual(actual, expected)

    def test_iaddition_1(self):
        expected = Point(*(4, 6, 1))
        self.p2 += self.p3
        self.assertEqual(self.p2, expected)

    def test_iaddition_2(self):
        expected = Point(*(4, 6, 1))
        self.p3 += self.p2
        self.assertEqual(self.p3, expected)

    def test_subtraction_1(self):
        expected = Point(*(-1, -1, 0))
        actual = self.p1 - self.p2
        self.assertEqual(actual, expected)

    def test_subtraction_2(self):
        expected = Point(*(0, 0, -1))
        actual = self.p2 - self.p3
        self.assertEqual(actual, expected)

    def test_subtraction_3(self):
        expected = Point(*(0, 0, -1))
        self.p2 -= self.p3
        self.assertEqual(self.p2, expected)

    def test_subtraction_4(self):
        expected = Point(*(0, 0, 1))
        self.p3 -= self.p2
        self.assertEqual(self.p3, expected)

    def test_multiplication_1(self):
        expected = Point(*(2, 4))
        actual = self.p1 * 2
        self.assertEqual(expected, actual)

    def test_multiplication_1_f(self):
        expected = Point(*(1, 1))
        actual = self.pf1 * 2
        self.assertEqual(expected, actual)

    def test_multiplication_2(self):
        expected = Point(*(2, 4))
        actual = 2 * self.p1
        self.assertEqual(expected, actual)

    def test_multiplication_2_f(self):
        expected = Point(*(1, 1))
        actual = 2 * self.pf1
        self.assertEqual(expected, actual)

    def test_multiplication_3(self):
        expected = Point(*(2, 4))
        self.p1 *= 2
        self.assertEqual(expected, self.p1)

    def test_division_1(self):
        expected = Point(*(0.5, 1))
        actual = self.p1 / 2
        self.assertEqual(expected, actual)

    def test_division_10(self):   # test Error z!=0
        with self.assertRaises(AssertionError) as error:
            actual = self.p1 / 0
        self.assertEqual('divisor must not be zero', str(error.exception))

    def test_division_2(self):
        expected = Point(*(0.5, 1))
        self.p1 /= 2
        self.assertEqual(expected, self.p1)

    def test_division_20(self):   # test Error z!=0
        with self.assertRaises(AssertionError) as error:
            self.p1 /= 0
        self.assertEqual('divisor must not be zero', str(error.exception))

    def test_floor_division_1(self):
        expected = Point(*(0, 1))
        actual = self.p1 // 2
        self.assertEqual(expected, actual)

    def test_floor_division_2(self):
        expected = Point(*(0, 1))
        self.p1 //= 2
        self.assertEqual(expected, self.p1)

    def test_floor_division_0(self):   # test Error z!=0
        with self.assertRaises(AssertionError) as error:
            self.p1 //= 0
        self.assertEqual('divisor must not be zero', str(error.exception))

    def test_negation(self):
        expected = Point(*(-2, -3, -1))
        actual = - self.p3
        self.assertEqual(expected, actual)

    def test_abs(self):
        expected = abs(Point(*(-2, -3, -1)))
        actual = self.p3
        self.assertEqual(expected, actual)

    def test_complex_1(self):
        expected = complex(1, 2)
        actual = complex(self.p1)
        self.assertEqual(expected, actual)

    def test_complex_2(self):   # test Error z!=0
        with self.assertRaises(AssertionError) as error:
            actual = complex(self.p3)
        self.assertEqual('z is not zero, cannot cast to Complex', str(error.exception))

    def test_str(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print(self.p1)
        expected = 'Point(1, 2, 0)\n'
        actual_out = f.getvalue()
        self.assertEqual(expected, actual_out)

    def test_scale(self):
        expected = Point(*(6, 9, 3))
        self.p3.scale(3)
        self.assertEqual(expected, self.p3)

    def test_distance_from_point_1(self):
        top1 = Point(*(1, 3))
        expected = 1
        actual = self.p1.distance_from_point(top1)
        self.assertEqual(expected, actual)

    def test_distance_from_point_2(self):
        top1 = Point(*(1, 1))
        expected = 1
        actual = self.p1.distance_from_point(top1)
        self.assertEqual(expected, actual)

    def test_distance_from_point_3(self):
        top1 = Point(*(2, 1))
        expected = math.sqrt(2)
        actual = self.p1.distance_from_point(top1)
        self.assertEqual(expected, actual)

    def test_distance_from_point_4(self):
        p1, p2 = Point(*(0, 3)), Point(*(4, 0))
        expected = 5
        actual = p1.distance_from_point(p2)
        self.assertEqual(expected, actual)

    def test_distance_from_point_5(self):
        origin = Point()
        expected = math.sqrt(14)
        actual = self.p3.distance_from_point(origin)
        self.assertEqual(expected, actual)

    def test_mid_point(self):
        p1, origin = Point(*(5, 5)), Point(*(0, 0))
        expected = Point(*(Fraction(5, 2), Fraction(5, 2)))
        actual = p1.mid_point(origin)
        self.assertEqual(expected, actual)


class TestPoint2D(unittest.TestCase):

    def setUp(self):

        self.origin = Point2D()
        self.p1 = Point2D(1, 2)

    def test_complex_1(self):
        expected = complex(1, 2)
        actual = complex(self.p1)
        self.assertEqual(expected, actual)

    def test_str(self):
        f = io.StringIO()
        with redirect_stdout(f):
            print(self.p1)
        expected = 'Point2D(1, 2)\n'
        actual_out = f.getvalue()
        self.assertEqual(expected, actual_out)

    def test_distance_from_point_0(self):
        origin = Point2D()
        expected = math.sqrt(5)
        actual = self.p1.distance_from_point(origin)
        self.assertEqual(expected, actual)

    def test_mid_point(self):
        p1, origin = Point2D(5, 5), Point2D(0, 0)
        expected = Point2D(Fraction(5, 2), Fraction(5, 2))
        actual = p1.mid_point(origin)
        self.assertEqual(expected, actual)


class TestPoint2DWithPoint3D(unittest.TestCase):

    def test_distance_from_point_P3_calls_P2(self):
        p3 = Point(1, 1, 1)
        p2 = Point2D(2, 2)
        expected = math.sqrt(2)
        actual = p3.distance_from_point(p2)
        self.assertEqual(expected, actual)

    def test_distance_from_point_P2_calls_P3(self):
        p3 = Point(1, 1, 1)
        p2 = Point2D(2, 2)
        expected = math.sqrt(2)
        actual = p2.distance_from_point(p3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
