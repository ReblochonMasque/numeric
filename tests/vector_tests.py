import unittest
from src import Vector2D


class TestVector2D(unittest.TestCase):

    def setUp(self):

        self.nullvector = Vector2D()
        self.unitx = Vector2D(1, 0)
        self.unity = Vector2D(0, 1)

    def test_instance(self):
        self.assertIsInstance(Vector2D(), Vector2D)

    def test_equality_null(self):
        other = Vector2D(0, 0)
        self.assertEqual(other, self.nullvector)

    def test_equality_unitx(self):
        other = Vector2D(1, 0)
        self.assertEqual(other, self.unitx)

    def test_equality_unity(self):
        other = Vector2D(0, 1)
        self.assertEqual(other, self.unity)

    def test_inequality(self):
        self.assertNotEqual(self.unitx, self.unity)

    def test_getitem_1(self):
        self.assertEqual(self.unitx[0], 1)
        self.assertEqual(self.unitx[1], 0)

    def test_getitem_2(self):
        self.assertEqual(self.unity[0], 0)
        self.assertEqual(self.unity[1], 1)

    def test_add(self):
        result = self.unitx + self.unity
        expected = Vector2D(1, 1)
        self.assertEqual(result, expected)

    def test_mul_1(self):
        result = self.unitx * 2
        expected = Vector2D(2, 0)
        self.assertEqual(result, expected)

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


if __name__ == '__main__':
    unittest.main()
