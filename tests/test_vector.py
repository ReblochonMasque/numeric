import unittest

from contextlib import redirect_stderr, redirect_stdout
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

    def test_str_0(self):
        expected = 'Vector(1.00, 2.01, 3.79, 4.10)\n'
        v = Vector(1.0001, 2.009, 3.78987, 4.1)
        actual = StringIO()
        with redirect_stdout(actual):
            print(v)
        self.assertEqual(expected, actual.getvalue())

    def test_repr_0(self):
        expected = '[Vector(1.0001, 2.009, 3.78987, 4.1)]\n'
        v = Vector(1.0001, 2.009, 3.78987, 4.1)
        actual = StringIO()
        with redirect_stdout(actual):
            print([v])
        self.assertEqual(expected, actual.getvalue())

    def test_add(self):
        val0, val1 = (1, 0, 0, 0, 1), (0, 1, 1, 1, 0)
        actual = Vector(*val0) + Vector(*val1)
        expected_vals = (1, 1, 1, 1, 1)
        expected = Vector(*expected_vals)
        self.assertEqual(expected, actual)

    def test_add_instance(self):
        val0, val1 = (1, 0, 0, 0, 1), (0, 1, 1, 1, 0)
        actual = Vector(*val0) + Vector(*val1)
        print(actual)
        self.assertIsInstance(actual, Vector)


class TestVector2D(unittest.TestCase):

    def test_instance_0(self):
        self.assertIsInstance(Vector2D(), Vector2D)

    def test_instance_1(self):
        self.assertIsInstance(Vector2D(x=2.2, y=-3.7), Vector2D)

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

##############################

    def test_add(self):
        actual = Vector2D(1, 0) + Vector2D(0, 1)
        expected = Vector2D(1, 1)
        self.assertEqual(expected, actual)

    def test_add_instance(self):
        actual = Vector2D(1, 0) + Vector2D(0, 1)
        expected = Vector2D(1, 1)
        self.assertIsInstance(expected, Vector2D)

    def test_mul_1(self):
        actual = Vector2D(1, 2) * 2
        expected = Vector2D(2, 4)
        self.assertEqual(expected, actual)

    def test_mul_2(self):
        actual = Vector2D(-1, -2) * 2
        expected = Vector2D(-2, -4)
        self.assertEqual(expected, actual)

    def test_rmul_1(self):
        actual = 2 * Vector2D(1, 2)
        expected = Vector2D(2, 4)
        self.assertEqual(expected, actual)

    def test_rmul_2(self):
        actual = -2 * Vector2D(1, -2)
        expected = Vector2D(-2, 4)
        self.assertEqual(expected, actual)

    def test_imul_1(self):
        expected = Vector2D(2, 4)
        actual = Vector2D(1, 2)
        expected_id = id(actual)
        actual *= 2
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

    def test_imul_2(self):
        expected = Vector2D(-2, -4)
        actual = Vector2D(-1, -2)
        actual *= 2
        self.assertEqual(expected, actual)

    def test_imul_mutation_1(self):
        expected = Vector2D(-2, -4)
        actual = Vector2D(1, 2)
        expected_id = id(actual)
        actual *= -2
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

    def test_imul_mutation_2(self):
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

    def test_itruediv_0(self):
        expected = Vector2D(-1./3., 4./3.)
        actual = Vector2D(-1, 4)
        expected_id = id(actual)
        actual /= 3
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

    def test_floordiv_0(self):
        expected = Vector2D(1.//3., -4.//3.)
        actual = Vector2D(-1, 4) // -3
        self.assertEqual(expected, actual)

    def test_ifloordiv_0(self):
        expected = Vector2D(-1.//3., 4.//3.)
        actual = Vector2D(-1, 4)
        expected_id = id(actual)
        actual //= 3
        actual_id = id(actual)
        self.assertEqual(expected, actual)
        self.assertEqual(expected_id, actual_id)

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
