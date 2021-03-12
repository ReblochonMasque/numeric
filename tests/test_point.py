"""
Tests Suite for point

"""


import unittest

from contextlib import redirect_stdout
from io import StringIO

from numeric.src.vector import Point, Point2D, Vector, Vector2D


class TestPoint(unittest.TestCase):
    """Tests Suite for instances of Point (dim >3 )
    """

    def test_instance_0(self):
        values = (0, 0, 0, 0, 0, 0)
        self.assertIsInstance(Point(*values), Point)

    def test_instance_1(self):
        self.assertIsInstance(Point(1, 2, 3, 4), Point)

    def test_instance_2(self):
        # @todo Maybe this should return a Point2D
        values = (1, 2)
        self.assertIsInstance(Point(*values), Point)

    def test_iter_0(self):
        expecteds = (3.2, 7.3, 8.987, -79.1)
        actuals = Point(3.2, 7.3, 8.987, -79.1)
        for expected, actual in zip(expecteds, actuals):
            self.assertEqual(expected, actual)

    def test_iter_1(self):
        expecteds = (3.2, 7.3, 8.987, -79.1)
        a, b, c, d = Point(3.2, 7.3, 8.987, -79.1)
        self.assertEqual(expecteds, (a, b, c, d))

    def test_equality_origin(self):
        actual = Point(0, 0, 0, 0, 0, 0, 0)
        expected = Point(0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(expected, actual)

    def test_equality_1(self):
        actual = Point(1, 0, 0, 0, 0)
        expected = Point(1, 0, 0, 0, 0)
        self.assertEqual(expected, actual)

    def test_equality_2(self):
        actual = Point(0, 1, 0, 3)
        expected = Point(0, 1, 0, 3)
        self.assertEqual(expected, actual)

    def test_inequality_0(self):
        self.assertNotEqual(Point(1, 0, 1, -1, 9, 2), Point(0, 1, 1, -1, 9))

    def test_inequality_1(self):
        self.assertNotEqual(Point(-1, 0, 0, -7.35), Point(-1, 0, 0, 7.35))

    def test_hash_0(self):
        expected = hash((22.345, -176.09, 142.3, 17.01))
        actual = hash(Point(22.345, -176.09, 142.3, 17.01))
        self.assertEqual(expected, actual)

    def test_hash_1(self):
        expected = hash((0, 1, 0, 0))
        actual = hash(Point(0, 1, 0, 0))
        self.assertEqual(expected, actual)

    def test_hash_2(self):
        notexpected = hash((1, 0, 1, 0))
        actual = hash(Point(0, 1, 0, 1))
        self.assertNotEqual(notexpected, actual)

    def test_bool_0(self):
        self.assertTrue(Point(1, 12, 0, 1, 3))

    def test_bool_1(self):
        self.assertFalse(Point(0, 0, 0, 0, 0, 0, 0))

    def test_bool_2(self):
        self.assertTrue(Point(1, 0, 0, 1))

    def test_bool_3(self):
        self.assertTrue(Point(0, -2, -2, -2))

    def test_str_0(self):
        expected = 'Point(1.00, 2.01, 3.79, 4.10)\n'
        v = Point(1.0001, 2.009, 3.78987, 4.1)
        actual = StringIO()
        with redirect_stdout(actual):
            print(v)
        self.assertEqual(expected, actual.getvalue())

    def test_str_1(self):
        expected = 'Point(0.00, 0.00, 0.00, 0.00, 55.01)\n'
        actual = StringIO()
        with redirect_stdout(actual):
            print(Point(0, 0, 0, 0, 55.00999))
        self.assertEqual(expected, actual.getvalue())

    def test_repr_0(self):
        expected = '[Point(1.0001, 2.009, 3.78987, 4.1)]\n'
        v = Point(1.0001, 2.009, 3.78987, 4.1)
        actual = StringIO()
        with redirect_stdout(actual):
            print([v])
        self.assertEqual(expected, actual.getvalue())

    def test_clone_0(self):
        """test clone values are same as original"""
        expected = Point(77.4, -85.9, 817.2, 99.99)
        original = Point(77.4, -85.9, 817.2, 99.99)
        clone = original.clone()
        self.assertEqual(expected, clone)
        self.assertEqual(original, clone)

    def test_clone_1(self):
        """test clone id not same as original id"""
        original = Point(77.4, -85.9, 817.2, 99.99)
        clone = original.clone()
        self.assertNotEqual(id(clone), id(original))

    def test_clone_2(self):
        """test mutate clone values do no mutate original"""
        original = Point(77.4, -85.9, 817.2, 99.99)
        orig_a, orig_b, orig_c, orig_d = original              # track original values
        clone = original.clone()
        # @todo refactor __getitem__ __setitem__
        #                                                      # mutate the clone
        clone._coords[0], clone._coords[1], clone._coords[2], clone._coords[3] = 22, -42, 17, 32
        self.assertEqual(orig_a, original._coords[0])          # assert original not mutated
        self.assertEqual(orig_b, original._coords[1])
        self.assertEqual(orig_c, original._coords[2])
        self.assertEqual(orig_d, original._coords[3])

    def test_clone_3(self):
        """test mutate original values do no mutate clone"""
        original = Point(77.4, -85.9, 817.2, 99.99)
        clone = original.clone()
        clone_a, clone_b, clone_c, clone_d = clone               # track clone values
        # @todo refactor __getitem__ __setitem__
        #                                                        # mutate the original
        original._coords[0], original._coords[1], original._coords[2], original._coords[3] = 22, -42, 17, 32
        self.assertEqual(clone_a, clone._coords[0])              # assert clone not mutated
        self.assertEqual(clone_b, clone._coords[1])
        self.assertEqual(clone_c, clone._coords[2])
        self.assertEqual(clone_d, clone._coords[3])


class TestPoint2D(unittest.TestCase):

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

    def test_str_0(self):
        expected = 'Point2D(x=0.00, y=0.00)\n'
        actual = StringIO()
        with redirect_stdout(actual):
            print(Point2D(x=0.00, y=0.00))
        self.assertEqual(expected, actual.getvalue())

    def test_repr_0(self):
        expected = '[Point2D(x=1.75449, y=-7.67882)]\n'
        actual = StringIO()
        with redirect_stdout(actual):
            print([Point2D(x=1.75449, y=-7.67882)])
        self.assertEqual(expected, actual.getvalue())

    def test_clone_0(self):
        """test clone values are same as original"""
        expected = Point2D(77.4, -85.9)
        original = Point2D(77.4, -85.9)
        clone = original.clone()
        self.assertEqual(expected, clone)
        self.assertEqual(original, clone)

    def test_clone_1(self):
        """test clone id not same as original id"""
        original = Point2D(77.4, -85.9)
        clone = original.clone()
        self.assertNotEqual(id(clone), id(original))

    def test_clone_2(self):
        """test mutate clone values do no mutate original"""
        original = Point2D(77.4, -85.9)
        orig_x, orig_y = original              # track original values
        clone = original.clone()
        clone.x, clone.y = 22, -42             # mutate the clone
        self.assertEqual(orig_x, original.x)   # assert original not mutated
        self.assertEqual(orig_y, original.y)

    def test_clone_3(self):
        """test mutate original values do no mutate clone"""
        original = Point2D(77.4, -85.9)
        clone = original.clone()
        clone_x, clone_y = clone               # track clone values
        original.x, original.y = 22, -42       # mutate original
        self.assertEqual(clone_x, clone.x)     # assert clone not mutated
        self.assertEqual(clone_y, clone.y)

    def test_add_Point2D_with_Point2D(self):
        p0 = Point2D(-1, -2)
        p1 = Point2D(1, 2)
        expected = "cannot add two Point"
        with self.assertRaises(TypeError) as e:
            _ = p0 + p1
        self.assertEqual(expected, str(e.exception))


class TestPointVectorInteraction(unittest.TestCase):

    def test_add_Point_w_Vector(self):
        expected = Point(-2, 1, 3, -4)
        p = Point(4, 6, -7, 8)
        v = Vector(-6, -5, 10, -12)
        actual = p + v
        self.assertEqual(expected, actual)

    def test_add_Vector_w_Point(self):
        expected = Point(-2, 1, 3, -4)
        p = Point(4, 6, -7, 8)
        v = Vector(-6, -5, 10, -12)
        actual = v + p
        self.assertEqual(expected, actual)

    def test_add_Point_w_Point(self):
        p0 = Point(1, 2, 3, 4)
        p1 = Point(4, 3, 2, 1)
        expected = "cannot add two Point"
        with self.assertRaises(TypeError) as e:
            _ = p0 + p1
        self.assertEqual(expected, str(e.exception))

    def test_add_Point_w_tuple(self):
        p0 = Point(1, 2, 3, 4)
        p1 = (4, 3, 2, 1)
        expected = f'addition of Point with {type(p1)} is not implemented'
        with self.assertRaises(NotImplementedError) as e:
            _ = p0 + p1
        self.assertEqual(expected, str(e.exception))

    def test_add_Point_w_Vector_of_incompatible_size(self):
        p0 = Point(1, 2, 3, 4)
        v0 = Vector(4, 3, 2, 1, 0)
        expected = "Incompatible operands sizes"
        with self.assertRaises(ValueError) as e:
            _ = p0 + v0
        self.assertEqual(expected, str(e.exception))

    def test_add_Vector_w_Point_of_incompatible_size(self):
        p0 = Point(1, 2, 3, 4)
        v0 = Vector(4, 3, 2, 1, 0)
        expected = "Incompatible operands sizes"
        with self.assertRaises(ValueError) as e:
            _ = v0 + p0
        self.assertEqual(expected, str(e.exception))


class TestPoint2DVector2DInteraction(unittest.TestCase):

    def test_add_Point2D_w_Vector2D(self):
        expected = Point2D(-2, 1)
        p = Point2D(4, 6)
        v = Vector2D(-6, -5)
        actual = p + v
        self.assertEqual(expected, actual)

    def test_add_Vector2D_w_Point2D(self):
        expected = Point2D(-2, 1)
        p = Point2D(4, 6)
        v = Vector2D(-6, -5)
        actual = v + p
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
