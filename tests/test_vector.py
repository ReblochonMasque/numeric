import unittest
from numeric.src.vector import Vector2D


class TestAbstractVector2D(unittest.TestCase):

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

    def test_inequality(self):
        self.assertNotEqual(Vector2D(1, 0), Vector2D(0, 1))

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


class TestVector2D(unittest.TestCase):

    def test_add(self):
        actual = Vector2D(1, 0) + Vector2D(0, 1)
        expected = Vector2D(1, 1)
        self.assertEqual(expected, actual)

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


if __name__ == '__main__':
    unittest.main()
