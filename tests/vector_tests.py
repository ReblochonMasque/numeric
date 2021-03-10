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
        result = self.unity * 2
        expected = Vector2D(0, 2)
        self.assertEqual(result, expected)

    def test_rmul_1(self):
        result = 2 * self.unitx
        expected = Vector2D(2, 0)
        self.assertEqual(result, expected)

    def test_rmul_2(self):
        result = 2 * self.unity
        expected = Vector2D(0, 2)
        self.assertEqual(result, expected)

    # def test_dot_1(self):
    #     result = self.unitx.dot(self.unity)
    #     expected = 0
    #     self.assertEqual(result, expected)
    #
    # def test_dot_2(self):
    #     result = self.unity.dot(self.unitx)
    #     expected = 0
    #     self.assertEqual(result, expected)
    #
    # def test_dot_3(self):
    #     result = self.unity.dot(self.nullvector)
    #     expected = 0
    #     self.assertEqual(result, expected)
    #
    # def test_dot_4(self):
    #     result = self.v_1_1.dot(self.v_1_1)
    #     expected = 2
    #     self.assertEqual(result, expected)
    #
    # def test_dot_5(self):
    #     result = self.v_m1_m1.dot(self.v_1_1)
    #     expected = -2
    #     self.assertEqual(result, expected)
    #
    # def test_dot_6(self):
    #     result = self.v_1_m1.dot(self.v_m1_1)
    #     expected = -2
    #     self.assertEqual(result, expected)
    #
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
