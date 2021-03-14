"""
Tests Suite for Vector

"""

import math
import unittest

from contextlib import redirect_stdout
from io import StringIO

from numeric.src.vector import Vector, Vector2D


class TestVector(unittest.TestCase):

    def test_instance_0(self):
        values = (0, 0, 0, 0, 0, 0)
        self.assertIsInstance(Vector(*values), Vector)

    def test_instance_1(self):
        values = (1, 2, 3, 4, 5)
        self.assertIsInstance(Vector(*values), Vector)

    def test_instance_2(self):
        # @todo Maybe this should return a Vector2D
        values = (1, 2)
        self.assertIsInstance(Vector(*values), Vector)

    def test_len(self):
        self.assertEqual(len(Vector(1, 2, 3, 4, 5, 6)), 6)

    def test_iter_0(self):
        expecteds = (3.2, 7.3, 8.987, -79.1)
        actuals = Vector(3.2, 7.3, 8.987, -79.1)
        for expected, actual in zip(expecteds, actuals):
            self.assertEqual(expected, actual)

    def test_iter_1(self):
        expecteds = (3.2, 7.3, 8.987, -79.1)
        a, b, c, d = Vector(3.2, 7.3, 8.987, -79.1)
        self.assertEqual(expecteds, (a, b, c, d))

    def test_equality_null_vector(self):
        actual = Vector(0, 0, 0, 0, 0, 0, 0)
        expected = Vector(0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(expected, actual)

    def test_equality_1(self):
        actual = Vector(1, 0, 0, 0, 0)
        expected = Vector(1, 0, 0, 0, 0)
        self.assertEqual(expected, actual)

    def test_equality_2(self):
        actual = Vector(0, 1, 0, 3)
        expected = Vector(0, 1, 0, 3)
        self.assertEqual(expected, actual)

    def test_inequality_0(self):
        self.assertNotEqual(Vector(1, 0, 1, -1, 9, 2), Vector(0, 1, 1, -1, 9))

    def test_inequality_1(self):
        self.assertNotEqual(Vector(-1, 0, 0, -7.35), Vector(-1, 0, 0, 7.35))

    def test_hash_0(self):
        expected = hash((22.345, -176.09, 142.3, 17.01))
        actual = hash(Vector(22.345, -176.09, 142.3, 17.01))
        self.assertEqual(expected, actual)

    def test_hash_1(self):
        expected = hash((0, 1, 0, 0))
        actual = hash(Vector(0, 1, 0, 0))
        self.assertEqual(expected, actual)

    def test_bool_0(self):
        self.assertTrue(Vector(1, 12, 0, 1, 3))

    def test_bool_1(self):
        self.assertFalse(Vector(0, 0, 0, 0, 0, 0, 0))

    def test_bool_2(self):
        self.assertTrue(Vector(1, 0, 0, 1))

    def test_bool_3(self):
        self.assertTrue(Vector(0, -2, -2, -2))

    def test_hash_2(self):
        notexpected = hash((1, 0, 1, 0))
        actual = hash(Vector(0, 1, 0, 1))
        self.assertNotEqual(notexpected, actual)

    def test_abs_0(self):
        expected = math.sqrt(70)
        actual = abs(Vector(-1, 4, 2, -7))
        self.assertEqual(expected, actual)

    def test_mag_0(self):
        expected = math.sqrt(70)
        actual = Vector(-1, -4, 2, 7).mag()
        self.assertEqual(expected, actual)

    def test_mag_1(self):
        expected = 0
        actual = Vector(0, 0, 0, 0, 0, 0, 0).mag()
        self.assertEqual(expected, actual)

    def test_str_0(self):
        expected = 'Vector(1.00, 2.01, 3.79, 4.10)\n'
        v = Vector(1.0001, 2.009, 3.78987, 4.1)
        actual = StringIO()
        with redirect_stdout(actual):
            print(v)
        self.assertEqual(expected, actual.getvalue())

    def test_str_1(self):
        expected = 'Vector(0.00, 0.00, 0.00, 0.00, 55.01)\n'
        actual = StringIO()
        with redirect_stdout(actual):
            print(Vector(0, 0, 0, 0, 55.00999))
        self.assertEqual(expected, actual.getvalue())

    def test_repr_0(self):
        expected = '[Vector(1.0001, 2.009, 3.78987, 4.1)]\n'
        v = Vector(1.0001, 2.009, 3.78987, 4.1)
        actual = StringIO()
        with redirect_stdout(actual):
            print([v])
        self.assertEqual(expected, actual.getvalue())

    def test_clone_0(self):
        """test clone values are same as original"""
        expected = Vector(77.4, -85.9, 817.2, 99.99)
        original = Vector(77.4, -85.9, 817.2, 99.99)
        clone = original.clone()
        self.assertEqual(expected, clone)
        self.assertEqual(original, clone)

    def test_clone_1(self):
        """test clone id not same as original id"""
        original = Vector(77.4, -85.9, 817.2, 99.99)
        clone = original.clone()
        self.assertNotEqual(id(clone), id(original))

    def test_clone_2(self):
        """test mutate clone values do no mutate original"""
        original = Vector(77.4, -85.9, 817.2, 99.99)
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
        original = Vector(77.4, -85.9, 817.2, 99.99)
        clone = original.clone()
        clone_a, clone_b, clone_c, clone_d = clone               # track clone values
        # @todo refactor __getitem__ __setitem__
        #                                                        # mutate the original
        original._coords[0], original._coords[1], original._coords[2], original._coords[3] = 22, -42, 17, 32
        self.assertEqual(clone_a, clone._coords[0])              # assert clone not mutated
        self.assertEqual(clone_b, clone._coords[1])
        self.assertEqual(clone_c, clone._coords[2])
        self.assertEqual(clone_d, clone._coords[3])

    def test_add(self):
        val0, val1 = (1, 0, 0, 0, 1), (0, 1, 1, 1, 0)
        actual = Vector(*val0) + Vector(*val1)
        expected_vals = (1, 1, 1, 1, 1)
        expected = Vector(*expected_vals)
        self.assertEqual(expected, actual)

    def test_add_instance(self):
        val0, val1 = (1, 0, 0, 0, 1), (0, 1, 1, 1, 0)
        actual = Vector(*val0) + Vector(*val1)
        self.assertIsInstance(actual, Vector)

    def test_iadd(self):
        expected = Vector(-4, 5, 0, 42)
        actual = Vector(2, 1, -1, 40)
        actual += Vector(-6, 4, 1, 2)
        self.assertEqual(expected, actual)

    def test_iadd_instance_mutated(self):
        _ = Vector(-4, 5, 0, 42)
        actual = Vector(2, 1, -1, 40)
        expected_id = id(actual)
        actual += Vector(-6, 4, 1, 2)
        actual_id = id(actual)
        self.assertEqual(expected_id, actual_id)

    def test_iadd_mismatched_sizes_of_operands(self):
        expected = "mismatched sizes of operands"
        v0 = Vector(7, 8, 0, 2, 1)
        v1 = Vector(7, 6, 3, -2)
        with self.assertRaises(ValueError) as e:
            v0 += v1
        self.assertEqual(expected, str(e.exception))

    def test_sub_0(self):
        expected = Vector(0, 2, -3, 4)
        v0 = Vector(7, 8, 0, 2)
        v1 = Vector(7, 6, 3, -2)
        actual = v0 - v1
        self.assertEqual(expected, actual)

    def test_sub_mismatched_sizes_of_operands(self):
        expected = "mismatched sizes of operands"
        v0 = Vector(7, 8, 0, 2, 1)
        v1 = Vector(7, 6, 3, -2)
        with self.assertRaises(ValueError) as e:
            _ = v0 - v1
        self.assertEqual(expected, str(e.exception))

    def test_isub(self):
        expected = Vector(8, -3, -2, 38)
        actual = Vector(2, 1, -1, 40)
        actual -= Vector(-6, 4, 1, 2)
        self.assertEqual(expected, actual)

    def test_isub_instance_mutated(self):
        _ = Vector(8, -3, -2, 38)
        actual = Vector(2, 1, -1, 40)
        expected_id = id(actual)
        actual -= Vector(-6, 4, 1, 2)
        actual_id = id(actual)
        self.assertEqual(expected_id, actual_id)

    def test_isub_mismatched_sizes_of_operands(self):
        expected = "mismatched sizes of operands"
        v0 = Vector(7, 8, 0, 2, 1)
        v1 = Vector(7, 6, 3, -2)
        with self.assertRaises(ValueError) as e:
            v0 -= v1
        self.assertEqual(expected, str(e.exception))

    def test_neg(self):
        expected = Vector(-7, -3, 12, -9)
        actual = -Vector(7, 3, -12, 9)
        self.assertEqual(expected, actual)

    def test_mul_0(self):
        actual = Vector(1, 2, 3, 4) * 2
        expected = Vector(2, 4, 6, 8)
        self.assertEqual(expected, actual)

    def test_mul_1(self):
        actual = Vector(-1, -2, -3, -4) * 2
        expected = Vector(-2, -4, -6, -8)
        self.assertEqual(expected, actual)

    def test_mul_2(self):
        actual = Vector(-1, -2, 3, 4) * 0
        expected = Vector(0, 0, 0, 0)
        self.assertEqual(expected, actual)

    def test_mul_3(self):
        actual = Vector(-1, -2, 3, 4) * 1
        expected = Vector(-1, -2, 3, 4)
        self.assertEqual(expected, actual)

    def test_rmul_0(self):
        actual = 2 * Vector(1, 2, 3, 4)
        expected = Vector(2, 4, 6, 8)
        self.assertEqual(expected, actual)

    def test_rmul_1(self):
        actual = 2 * Vector(-1, -2, -3, -4)
        expected = Vector(-2, -4, -6, -8)
        self.assertEqual(expected, actual)

    def test_rmul_2(self):
        actual = 0 * Vector(-1, -2, 3, 4)
        expected = Vector(0, 0, 0, 0)
        self.assertEqual(expected, actual)

    def test_rmul_3(self):
        actual = 1 * Vector(-1, -2, 3, 4)
        expected = Vector(-1, -2, 3, 4)
        self.assertEqual(expected, actual)

    def test_imul_0(self):
        expected = Vector(2, 4, 6, 7)
        actual = Vector(1, 2, 3, 3.5)
        expected_id = id(actual)
        actual *= 2
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

    def test_imul_1(self):
        expected = Vector(-2, -4, -6, -7)
        actual = Vector(1, 2, 3, 3.5)
        actual *= -2
        self.assertEqual(expected, actual)

    def test_imul_mutation_0(self):
        expected = Vector(-2, -4, -12, -13)
        actual = Vector(1, 2, 6, 6.5)
        expected_id = id(actual)
        actual *= -2
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

    def test_truediv_0(self):
        expected = Vector(1./3., -4./3., 7/9, 7)
        actual = Vector(-1, 4, -7/3, -21) / -3
        self.assertEqual(expected, actual)

    def test_truediv_1(self):
        expected = "cannot divide a Vector by zero"
        with self.assertRaises(ZeroDivisionError) as e:
            _ = Vector(-1, 4, -7/3, -21) / 0
        self.assertEqual(expected, str(e.exception))

    def test_itruediv_0(self):
        expected = Vector(1./3., -4./3., 7/9, 7)
        actual = Vector(-1, 4, -7/3, -21)
        actual /= -3
        self.assertEqual(expected, actual)

    def test_itruediv_1(self):
        actual = Vector(-1, 4, -7/3, -21)
        expected_id = id(actual)
        actual /= 3
        actual_id = id(actual)
        self.assertEqual(expected_id, actual_id)

    def test_floordiv_0(self):
        expected = Vector(0, 1, 2, 7)
        actual = Vector(1, 4, 26/3, 21.5) // 3
        self.assertEqual(expected, actual)

    def test_floordiv_1(self):
        expected = Vector(0., -2., 0, 7)
        actual = Vector(-1, 4, -7/3, -21) // -3
        self.assertEqual(expected, actual)

    def test_floordiv_2(self):
        expected = "cannot divide a Vector by zero"
        with self.assertRaises(ZeroDivisionError) as e:
            a = Vector(1, 4, 26/3, 21.5)
            _ = a // 0
        self.assertEqual(expected, str(e.exception))

    def test_ifloordiv_0(self):
        expected = Vector(0., -2., 0, 7)
        actual = Vector(-1, 4, -7/3, -21)
        actual //= -3
        self.assertEqual(expected, actual)

    def test_ifloordiv_1(self):
        actual = Vector(-1, 4, -7/3, -21)
        expected_id = id(actual)
        actual //= 3
        actual_id = id(actual)
        self.assertEqual(expected_id, actual_id)

    def test_ifloordiv_2(self):
        expected = "cannot divide a Vector by zero"
        with self.assertRaises(ZeroDivisionError) as e:
            a = Vector(-1, 4, -7/3, -21)
            a //= 0
        self.assertEqual(expected, str(e.exception))


class TestVector2D(unittest.TestCase):

    def test_instance_0(self):
        self.assertIsInstance(Vector2D(), Vector2D)

    def test_instance_1(self):
        self.assertIsInstance(Vector2D(x=2.2, y=-3.7), Vector2D)

    def test_len(self):
        self.assertEqual(len(Vector2D(1, 2)), 2)

    def test_iter_0(self):
        expecteds = (3.2, 7.3)
        actuals = Vector2D(3.2, 7.3)
        for expected, actual in zip(expecteds, actuals):
            self.assertEqual(expected, actual)

    def test_iter_1(self):
        expected_x, expected_y = (3.2, 7.3)
        actual_x, actual_y = Vector2D(3.2, 7.3)
        self.assertEqual(expected_x, actual_x)
        self.assertEqual(expected_y, actual_y)

    def test_equality_null(self):
        actual = Vector2D()
        expected = Vector2D(0, 0)
        self.assertEqual(expected, actual)

    def test_equality_unitx(self):
        actual = Vector2D(1, 0)
        expected = Vector2D(1, 0)
        self.assertEqual(expected, actual)

    def test_equality_unity(self):
        actual = Vector2D(0, 1)
        expected = Vector2D(0, 1)
        self.assertEqual(expected, actual)

    def test_inequality_0(self):
        self.assertNotEqual(Vector2D(1, 0), Vector2D(0, 1))

    def test_inequality_1(self):
        self.assertNotEqual(Vector2D(-1, -7.35), Vector2D(-1, 7.35))

    def test_hash_0(self):
        expected = hash((22.345, -176.09))
        actual = hash(Vector2D(22.345, -176.09))
        self.assertEqual(expected, actual)

    def test_hash_1(self):
        expected = hash((0, 1))
        actual = hash(Vector2D(0, 1))
        self.assertEqual(expected, actual)

    def test_hash_2(self):
        notexpected = hash((1, 0))
        actual = hash(Vector2D(0, 1))
        self.assertNotEqual(notexpected, actual)

    def test_bool_0(self):
        self.assertTrue(Vector2D(1, 12))

    def test_bool_1(self):
        self.assertFalse(Vector2D(0, 0))

    def test_bool_2(self):
        self.assertTrue(Vector2D(1, 0))

    def test_bool_3(self):
        self.assertTrue(Vector2D(0, -2))

    def test_str_0(self):
        expected = 'Vector2D(x=0.00, y=0.00)\n'
        actual = StringIO()
        with redirect_stdout(actual):
            print(Vector2D(x=0.00, y=0.00))
        self.assertEqual(expected, actual.getvalue())

    def test_repr_0(self):
        expected = '[Vector2D(x=1.75449, y=-7.67882)]\n'
        actual = StringIO()
        with redirect_stdout(actual):
            print([Vector2D(x=1.75449, y=-7.67882)])
        self.assertEqual(expected, actual.getvalue())

    def test_clone_0(self):
        """test clone values are same as original"""
        expected = Vector2D(77.4, -85.9)
        original = Vector2D(77.4, -85.9)
        clone = original.clone()
        self.assertEqual(expected, clone)
        self.assertEqual(original, clone)

    def test_clone_1(self):
        """test clone id not same as original id"""
        original = Vector2D(77.4, -85.9)
        clone = original.clone()
        self.assertNotEqual(id(clone), id(original))

    def test_clone_2(self):
        """test mutate clone values do no mutate original"""
        original = Vector2D(77.4, -85.9)
        orig_x, orig_y = original              # track original values
        clone = original.clone()
        clone.x, clone.y = 22, -42             # mutate the clone
        self.assertEqual(orig_x, original.x)   # assert original not mutated
        self.assertEqual(orig_y, original.y)

    def test_clone_3(self):
        """test mutate original values do no mutate clone"""
        original = Vector2D(77.4, -85.9)
        clone = original.clone()
        clone_x, clone_y = clone               # track clone values
        original.x, original.y = 22, -42       # mutate original
        self.assertEqual(clone_x, clone.x)     # assert clone not mutated
        self.assertEqual(clone_y, clone.y)

    def test_add(self):
        actual = Vector2D(1, 0) + Vector2D(0, 1)
        expected = Vector2D(1, 1)
        self.assertEqual(expected, actual)

    def test_add_instance(self):
        actual = Vector2D(1, 0) + Vector2D(0, 1)
        self.assertIsInstance(actual, Vector2D)

    def test_iadd(self):
        expected = Vector2D(-4, 5)
        actual = Vector2D(2, 1)
        actual += Vector2D(-6, 4)
        self.assertEqual(expected, actual)

    def test_iadd_instance_mutated(self):
        _ = Vector2D(-4, 5)
        actual = Vector2D(2, 1)
        expected_id = id(actual)
        actual += Vector2D(-6, 4)
        actual_id = id(actual)
        self.assertEqual(expected_id, actual_id)

    def test_sub_0(self):
        expected = Vector2D(-3, 4)
        v0 = Vector2D(0, 2)
        v1 = Vector2D(3, -2)
        actual = v0 - v1
        self.assertEqual(expected, actual)

    def test_isub(self):
        expected = Vector2D(8, 38)
        actual = Vector2D(2, 40)
        actual -= Vector2D(-6, 2)
        self.assertEqual(expected, actual)

    def test_isub_instance_mutated(self):
        _ = Vector2D(8, -3)
        actual = Vector2D(2, 1)
        expected_id = id(actual)
        actual -= Vector2D(-6, 4)
        actual_id = id(actual)
        self.assertEqual(expected_id, actual_id)

    def test_neg(self):
        expected = Vector2D(2, -9)
        actual = -Vector2D(-2, 9)
        self.assertEqual(expected, actual)

    def test_mul_0(self):
        actual = Vector2D(1, 2) * 2
        expected = Vector2D(2, 4)
        self.assertEqual(expected, actual)

    def test_mul_1(self):
        actual = Vector2D(-1, -2) * 2
        expected = Vector2D(-2, -4)
        self.assertEqual(expected, actual)

    def test_mul_2(self):
        actual = Vector2D(-1, -2) * 0
        expected = Vector2D()
        self.assertEqual(expected, actual)

    def test_mul_3(self):
        actual = Vector2D(-1, -2) * 1
        expected = Vector2D(-1, -2)
        self.assertEqual(expected, actual)

    def test_rmul_0(self):
        actual = 2 * Vector2D(1, 2)
        expected = Vector2D(2, 4)
        self.assertEqual(expected, actual)

    def test_rmul_1(self):
        actual = -2 * Vector2D(1, -2)
        expected = Vector2D(-2, 4)
        self.assertEqual(expected, actual)

    def test_rmul_2(self):
        actual = 0 * Vector2D(-1, -2)
        expected = Vector2D()
        self.assertEqual(expected, actual)

    def test_rmul_3(self):
        actual = 1 * Vector2D(-1, -2)
        expected = Vector2D(-1, -2)
        self.assertEqual(expected, actual)

    def test_imul_0(self):
        expected = Vector2D(2, 4)
        actual = Vector2D(1, 2)
        expected_id = id(actual)
        actual *= 2
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

    def test_imul_1(self):
        expected = Vector2D(-2, -4)
        actual = Vector2D(-1, -2)
        actual *= 2
        self.assertEqual(expected, actual)

    def test_imul_mutation_0(self):
        expected = Vector2D(-2, -4)
        actual = Vector2D(1, 2)
        expected_id = id(actual)
        actual *= -2
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

    def test_imul_mutation_1(self):
        expected = Vector2D(-2, -4)
        actual = Vector2D(-1, -2)
        expected_id = id(actual)
        actual *= 2
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

    def test_truediv_0(self):
        expected = Vector2D(1./3., -4./3.)
        actual = Vector2D(-1, 4) / -3
        self.assertEqual(expected, actual)

    def test_truediv_1(self):
        expected = "cannot divide a Vector by zero"
        with self.assertRaises(ZeroDivisionError) as e:
            _ = Vector2D(-1, 4) / 0
        self.assertEqual(expected, str(e.exception))

    def test_itruediv_0(self):
        expected = Vector2D(-1./3., 4./3.)
        actual = Vector2D(-1, 4)
        actual /= 3
        self.assertEqual(expected, actual)

    def test_itruediv_1(self):
        actual = Vector2D(-1, 4)
        expected_id = id(actual)
        actual /= 3
        actual_id = id(actual)
        self.assertEqual(expected_id, actual_id)

    def test_itruediv_2(self):
        expected = "cannot divide a Vector by zero"
        with self.assertRaises(ZeroDivisionError) as e:
            a = Vector2D(-1, 4)
            a /= 0
        self.assertEqual(expected, str(e.exception))

    def test_floordiv_0(self):
        expected = Vector2D(1.//3., -4.//3.)
        actual = Vector2D(-1, 4) // -3
        self.assertEqual(expected, actual)

    def test_floordiv_1(self):
        expected = Vector2D(2, 7)
        actual = Vector2D(26/3, 21.5) // 3
        self.assertEqual(expected, actual)

    def test_floordiv_2(self):
        expected = Vector2D(-2, 0)
        actual = Vector2D(4, -7/3) // -3
        self.assertEqual(expected, actual)

    def test_ifloordiv_0(self):
        expected = Vector2D(-1.//3., 4.//3.)
        actual = Vector2D(-1, 4)
        actual //= 3
        self.assertEqual(expected, actual)

    def test_ifloordiv_1(self):
        actual = Vector2D(-1, 4)
        expected_id = id(actual)
        actual //= 3
        actual_id = id(actual)
        self.assertEqual(expected_id, actual_id)

    def test_ifloordiv_2(self):
        expected = "cannot divide a Vector by zero"
        with self.assertRaises(ZeroDivisionError) as e:
            a = Vector2D(-1, 4)
            a //= 0
        self.assertEqual(expected, str(e.exception))

    def test_abs_0(self):
        expected = math.sqrt(17)
        actual = abs(Vector2D(-1, 4))
        self.assertEqual(expected, actual)

    def test_mag_0(self):
        expected = math.sqrt(17)
        actual = Vector2D(-1, 4).mag()
        self.assertEqual(expected, actual)

    def test_mag_1(self):
        expected = 0
        actual = Vector2D().mag()
        self.assertEqual(expected, actual)

    def test_dot_1(self):
        actual = Vector2D(1, 0).dot(Vector2D(0, 1))
        expected = 0
        self.assertEqual(expected, actual)

    def test_dot_2(self):
        actual = Vector2D(0, 1).dot(Vector2D(1, 0))
        expected = 0
        self.assertEqual(expected, actual)

    def test_dot_3(self):
        actual = Vector2D().dot(Vector2D(1, 0))
        expected = 0
        self.assertEqual(expected, actual)

    def test_dot_4(self):
        actual = Vector2D(1, 1).dot(Vector2D(1, 1))
        expected = 2
        self.assertEqual(expected, actual)

    def test_dot_5(self):
        actual = Vector2D(-1, -1).dot(Vector2D(1, 1))
        expected = -2
        self.assertEqual(expected, actual)

    def test_dot_6(self):
        actual = Vector2D(-1, 1).dot(Vector2D(1, -1))
        expected = -2
        self.assertEqual(expected, actual)

    def test_unit_vector_0(self):
        actual = Vector2D(0, -1).unit()
        expected = Vector2D(0, -1)
        self.assertEqual(expected, actual)

    def test_unit_vector_1(self):
        actual = Vector2D(x=3.00, y=4.00).unit()
        expected = Vector2D(x=0.60, y=0.80)
        self.assertEqual(expected, actual)

    def test_perp_0(self):
        expected = Vector2D(x=0, y=1)
        actual = Vector2D(x=1, y=0).perp()
        self.assertEqual(expected, actual)

    def test_perp_1(self):
        expected = Vector2D(x=4.57, y=7.32)
        actual = Vector2D(x=7.32, y=-4.57).perp()
        self.assertEqual(expected, actual)

    def test_perp_2(self):
        expected = Vector2D(x=7.32, y=-4.57)
        actual = Vector2D(x=7.32, y=-4.57).perp().perp().perp().perp()
        self.assertEqual(expected, actual)

    def test_perp_product_unit_1(self):
        expected = 1
        actual = Vector2D(1, 0).perp_product(Vector2D(0, 1))
        self.assertEqual(expected, actual)

    def test_perp_product_unit_m1(self):
        expected = -1
        actual = Vector2D(0, 1).perp_product(Vector2D(1, 0))
        self.assertEqual(expected, actual)

    def test_perp_product_3(self):
        expected = 2
        actual = Vector2D(-1, -1).perp_product(Vector2D(1, -1))
        self.assertEqual(expected, actual)

    def test_perp_product_4(self):
        expected = -2
        actual = Vector2D(1, -1).perp_product(Vector2D(-1, -1))
        self.assertEqual(expected, actual)

    def test_perp_product_5(self):
        expected = 0
        actual = Vector2D(-1, -1).perp_product(Vector2D(x=2, y=2))
        self.assertEqual(expected, actual)

    def test_isnull_0(self):
        self.assertTrue(Vector2D().isnull())

    def test_isnull_1(self):
        self.assertFalse(Vector2D(0, 1).isnull())

    def test_isnull_2(self):
        self.assertFalse(Vector2D(1, 0).isnull())

    def test_isnull_3(self):
        self.assertFalse(Vector2D(-1, -1).isnull())

    def test_isnull_4(self):
        self.assertFalse(Vector2D(1, 1).isnull())


if __name__ == '__main__':
    unittest.main()
