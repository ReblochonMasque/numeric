import unittest
from numeric.src.vector_springs import Vector2D


class TestVector2D(unittest.TestCase):

    def setUp(self):

        self.unitx = Vector2D(1, 0)
        self.unity = Vector2D(0, 1)
        self.v_1_1 = Vector2D(1, 1)
        self.v_m1_1 = Vector2D(-1, 1)
        self.v_m1_m1 = Vector2D(-1, -1)
        self.v_1_m1 = Vector2D(1, -1)

    def test_instance(self):
        self.assertIsInstance(Vector2D(), Vector2D)

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
        actual = Vector2D(0, -1).unit_vector()
        expected = Vector2D(0, -1)
        self.assertEqual(expected, actual)

    # def test_cross_unit_1(self):
    #     result = self.unitx.cross(self.unity)
    #     expected = 1
    #     self.assertEqual(result, expected)
    #
    # def test_cross_unit_m1(self):
    #     result = self.unity.cross(self.unitx)
    #     expected = -1
    #     self.assertEqual(result, expected)
    #
    # def test_cross_3(self):
    #     result = self.v_m1_m1.cross(self.v_1_m1)
    #     expected = 2
    #     self.assertEqual(result, expected)
    #
    # def test_cross_4(self):
    #     result = self.v_1_m1.cross(self.v_m1_m1)
    #     expected = -2
    #     self.assertEqual(result, expected)
    #
    # def test_cross_5(self):
    #     result = self.v_m1_m1.cross(Vector2D(x=2, y=2))
    #     expected = 0
    #     self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
