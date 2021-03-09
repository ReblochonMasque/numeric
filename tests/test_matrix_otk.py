import math
import unittest

from fractions import Fraction
from numbers import Number
from numeric.src.matrix_otk import Matrix, MatrixComplex, MatrixShape, identity, zeros
from typing import Sequence


class TestMatrixShape(unittest.TestCase):

    def test_creation(self):
        shape = MatrixShape(num_rows=2, num_cols=4)
        self.assertIsInstance(shape, MatrixShape)

    def test_values(self):
        expected = (2, 4)
        actual = MatrixShape(num_rows=2, num_cols=4)
        self.assertEqual(actual, expected)


class MatrixTests(unittest.TestCase):

    def setUp(self):
        self.identity_1 = Matrix([[1]])
        self.identity_2 = Matrix([[1, 0], [0, 1]])
        self.identity_3 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.null_2_1 = Matrix([[0], [0]])
        self.null_2_2 = Matrix([[0, 0], [0, 0]])
        self.null_3_3 = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.null_4_4 = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.null_2_4 = Matrix([[0, 0, 0, 0], [0, 0, 0, 0]])
        self.null_4_2 = Matrix([[0, 0], [0, 0], [0, 0], [0, 0]])

        self.real1_2_4 = Matrix([[math.sqrt(2), math.sqrt(2), -math.sqrt(2), -math.sqrt(2)],
                                 [2, 2, -2, -2]])
        self.real1_2_4_to_9_decimals = Matrix([[1.414213562, 1.414213562, -1.414213562, -1.414213562],
                                               [2.000000001, 1.999999999, -1.999999999, -2.000000001]])
        self.real1_2_4_to_8_decimals = Matrix([[1.41421356, 1.41421356, -1.41421356, -1.41421356],
                                               [2.00000001, 1.99999999, -1.99999999, -2.00000001]])

        self._2x2_1234 = Matrix([[1, 2], [3, 4]])
        self._2x2_2345 = Matrix([[2, 3], [4, 5]])

        self._3x1_123 = Matrix([[1], [2], [3]])
        self._1x3_123 = Matrix([[1, 2, 3]])

        self._2x2_5124 = Matrix([[5, 1], [2, 4]])

        self._2x3_023115 = Matrix([[0, 2, 3], [1, 1, 5]])
        self._3x2_023115 = Matrix([[0, 1], [2, 1], [3, 5]])

        self._3x3_012211348 = Matrix([[0, 1, 2], [2, 1, 1], [3, 4, 8]])
        self._3x1_512 = Matrix([[5], [1], [2]])

        self._3x3_101211423 = Matrix([[1, 0, 1], [2, 1, 1], [4, 2, 3]])
        self._3x3_101211423T = Matrix([[1, 2, 4], [0, 1, 2], [1, 1, 3]])
        self._3x3_112001415 = Matrix([[1, 1, 2], [0, 0, 1], [4, 1, 5]])

        self._3x2_023115_neg = Matrix([[0, -1], [-2, -1], [-3, -5]])
        self._3x3_012211348_neg = Matrix([[0, -1, -2], [-2, -1, -1], [-3, -4, -8]])
        self._3x1_512_neg = Matrix([[-5], [-1], [-2]])


    # ----- tests for creation of a Matrix ------------------
    def test_Matrix_type(self):
        self.assertIsInstance(self.identity_1, Matrix)

    def test_empty(self):
        with self.assertRaises(AssertionError):
            data = []
            Matrix(data)

    def test_empty_rows(self):
        with self.assertRaises(AssertionError):
            data = [[], []]
            Matrix(data)

    def test_unequal_number_of_columns(self):
        """number of elements differs in rows
        """
        with self.assertRaises(AssertionError):
            data = [[1, 2], [1]]
            Matrix(data)

    def test_elements_not_numbers(self):
        with self.assertRaises(TypeError):
            data = [['a', 2], [1, 2]]
            Matrix(data)

    def test_elements_not_numbers_but_bool_False(self):
        """exclude booleans, they are also int types"""
        with self.assertRaises(TypeError):
            data = [[0, 2], [1, False]]
            Matrix(data)

    def test_elements_not_numbers_but_bool_True(self):
        """exclude booleans, they are also int types"""
        with self.assertRaises(TypeError):
            data = [[0, True], [1, 0]]
            Matrix(data)

    def test_shape0(self):
        expected = (1, 1)
        actual = self.identity_1.shape
        self.assertEqual(actual, expected)

    def test_shape1(self):
        expected = (2, 1)
        actual = self.null_2_1.shape
        self.assertEqual(actual, expected)

    def test_shape2(self):
        expected = (2, 2)
        actual = self.identity_2.shape
        self.assertEqual(actual, expected)

    # ----- tests __getitem__ -------------------------------
    @staticmethod
    def _compare_values(mat: 'Matrix', expected_values: Sequence[Sequence[Number]])-> bool:
        rows, cols = mat.shape
        result = True
        for row in range(rows):
            for col in range(cols):
                current_comparison = math.isclose(mat[row, col],
                                                  expected_values[row][col])
                result = result and current_comparison
        return result

    def test_getitem_0(self):
        expected_values = [[5, 1], [2, 4]]
        mat = self._2x2_5124
        self.assertTrue(MatrixTests._compare_values(mat, expected_values))

    def test_getitem_1(self):
        expected_values = [[1.414213562, 1.414213562, -1.414213562, -1.414213562],
                           [2.000000001, 1.999999999, -1.999999999, -2.000000001]]
        mat = self.real1_2_4_to_9_decimals
        self.assertTrue(MatrixTests._compare_values(mat, expected_values))

    def test_getitem_2(self):
        expected_values = [[0, 1, 2], [2, 1, 1], [3, 4, 8]]
        mat = self._3x3_012211348
        self.assertTrue(MatrixTests._compare_values(mat, expected_values))

    def test_getitem_3(self):
        expected_values = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        mat = self.null_4_4
        self.assertTrue(MatrixTests._compare_values(mat, expected_values))

    def test_getitem_4(self):
        expected_values = [[5, 1], [2, 4]]
        mat = self._2x2_5124
        with self.assertRaises(IndexError):
            _ = mat[1, 2]

    def test_getitem_5(self):
        expected_values = [[5, 1], [2, 4]]
        mat = self._2x2_5124
        with self.assertRaises(IndexError):
            _ = mat[-3, 2]

    # ----- tests __setitem__ -------------------------------
    def test_setitem_0(self):
        expected_values = [[5, 0], [2, 4]]
        self._2x2_5124[0, 1] = 0
        mat = self._2x2_5124
        self.assertTrue(MatrixTests._compare_values(mat, expected_values))

    def test_setitem_1(self):
        expected_values = [[1.414213562, 1.414213562, -1.414213562, -1.414213562],
                           [2.000000001, 1.999999999, 12, -2.000000001]]
        self.real1_2_4_to_9_decimals[1, 2] = 12
        mat = self.real1_2_4_to_9_decimals
        self.assertTrue(MatrixTests._compare_values(mat, expected_values))

    def test_setitem_2(self):
        expected_values = [[0, 1, 2], [144, 1, 1], [3, 4, -22.5]]
        self._3x3_012211348[1, 0] = 144
        self._3x3_012211348[2, 2] = -22.5
        mat = self._3x3_012211348
        self.assertTrue(MatrixTests._compare_values(mat, expected_values))

    def test_setitem_3(self):
        expected_values = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 4]]
        self.null_4_4[0, 0] = 1
        self.null_4_4[1, 1] = 1
        self.null_4_4[2, 2] = 1
        self.null_4_4[3, 3] = 4
        mat = self.null_4_4
        self.assertTrue(MatrixTests._compare_values(mat, expected_values))

    def test_setitem_4(self):
        mat = self._2x2_5124
        with self.assertRaises(IndexError):
            mat[1, 2] = 12

    def test_setitem_5(self):
        mat = self._2x2_5124
        with self.assertRaises(IndexError):
            mat[-3, 2] = 15

    # ----- test equality ------------------------------------
    def test_equality_True(self):
        id_2 = Matrix([[1, 0], [0, 1]])
        self.assertEqual(id_2, self.identity_2)

    def test_equality_False(self):
        self.assertNotEqual(self.null_3_3, self.identity_2)

    def test_equality_floats_True(self):
        self.assertEqual(self.real1_2_4, self.real1_2_4_to_9_decimals)

    def test_equality_floats_False(self):
        self.assertNotEqual(self.real1_2_4, self.real1_2_4_to_8_decimals)

    # ----- tests for Matrix Multiplication ------------------
    def test_matmul_returns_a_Matrix(self):
        expected = Matrix([[0]])
        actual = self.null_2_1 @ self.identity_1
        self.assertIsInstance(actual, Matrix)
        # self.assertEqual(actual, expected)

    def test_2x2_1234_mul_2x2_identity(self):
        expected = Matrix([[1, 2], [3, 4]])
        actual = self._2x2_1234 @ self.identity_2
        self.assertEqual(actual, expected)

    def test_2x2_identity_mul_2x2_1234(self):
        expected = Matrix([[1, 2], [3, 4]])
        actual = self.identity_2 @ self._2x2_1234
        self.assertEqual(actual, expected)

    def test_2x2_1234_mul_2x2_2345(self):
        expected = Matrix([[10, 13], [22, 29]])
        actual = self._2x2_1234 @ self._2x2_2345
        self.assertEqual(actual, expected)

    def test_2x2_2345_mul_2x2_1234_(self):
        expected = Matrix([[11, 16], [19, 28]])
        actual = self._2x2_2345 @ self._2x2_1234
        self.assertEqual(actual, expected)

    def test_2x2_1234_mul_2x2_5124_(self):
        expected = Matrix([[9, 9], [23, 19]])
        actual = self._2x2_1234 @ self._2x2_5124
        self.assertEqual(actual, expected)

    def test_2x2_5124_mul_2x2_1234_(self):
        expected = Matrix([[8, 14], [14, 20]])
        actual = self._2x2_5124 @ self._2x2_1234
        self.assertEqual(actual, expected)

    def test_3x1_mul_1x3(self):
        expected = Matrix([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
        actual = self._3x1_123 @ self._1x3_123
        self.assertEqual(actual, expected)

    def test_1x3_mul_3x1(self):
        expected = Matrix([[14]])
        actual = self._1x3_123 @ self._3x1_123
        self.assertEqual(actual, expected)

    def test_2x2_1234_mul_2x3_023115(self):
        expected = Matrix([[2, 4, 13], [4, 10, 29]])
        actual = self._2x2_1234 @ self._2x3_023115
        self.assertEqual(actual, expected)

    def test_2x3_023115_mul_2x2_1234(self):
        """incompatible matrix shapes for multiplication
        """
        with self.assertRaises(AssertionError):
            self._2x3_023115 @ self._2x2_1234

    def test_3x3_012211348_mul_3x1_512(self):
        expected = Matrix([[5], [13], [35]])
        actual = self._3x3_012211348 @ self._3x1_512
        self.assertEqual(actual, expected)

    def test_3x1_512_mul_3x3_012211348(self):
        """incompatible matrix shapes for multiplication
        """
        with self.assertRaises(AssertionError):
            self._3x1_512 @ self._3x3_012211348

    def test_3x3_101211423_mul_3x3_112001415(self):
        expected = Matrix([[5, 2, 7], [6, 3, 10], [16, 7, 25]])
        actual = self._3x3_101211423 @ self._3x3_112001415
        self.assertEqual(actual, expected)

    def test_3x3_112001415_mul_3x3_101211423(self):
        expected = Matrix([[11, 5, 8], [4, 2, 3], [26, 11, 20]])
        actual = self._3x3_112001415 @ self._3x3_101211423
        self.assertEqual(actual, expected)

    # ----- tests for Matrix Addition ------------------
    def test_addition_2x2_0(self):
        expected = Matrix([[10, 2], [4, 8]])
        actual = self._2x2_5124 + self._2x2_5124
        self.assertEqual(actual, expected)

    def test_addition_2x2_1(self):
        expected = Matrix([[15, 3], [6, 12]])
        actual = self._2x2_5124 + Matrix([[10, 2], [4, 8]])
        self.assertEqual(actual, expected)

    def test_addition_2x3(self):
        expected = Matrix([[0, 4, 6], [2, 2, 10]])
        actual = self._2x3_023115 + self._2x3_023115
        self.assertEqual(actual, expected)

    def test_addition_3x3(self):
        expected = Matrix([[0, 2, 4], [4, 2, 2], [6, 8, 16]])
        actual = self._3x3_012211348 + self._3x3_012211348
        self.assertEqual(actual, expected)

    def test_addition_shapes_not_matching(self):
        with self.assertRaises(AssertionError):
            _ = self._2x2_5124 + self._3x1_512

    # ----- tests for Matrix Subtraction ------------------
    def test_subtraction_2x2_0(self):
        expected = Matrix([[0, 0], [0, 0]])
        actual = self._2x2_5124 - self._2x2_5124
        self.assertEqual(actual, expected)

    def test_subtraction_2x2_1(self):
        expected = Matrix([[-5, -1], [-2, -4]])
        actual = self._2x2_5124 - Matrix([[10, 2], [4, 8]])
        self.assertEqual(actual, expected)

    def test_subtraction_2x3(self):
        expected = Matrix([[0, 0, 0], [0, 0, 0]])
        actual = self._2x3_023115 - self._2x3_023115
        self.assertEqual(actual, expected)

    def test_subtraction_3x3(self):
        expected = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        actual = self._3x3_012211348 - self._3x3_012211348
        self.assertEqual(actual, expected)

    def test_subtraction_shapes_not_matching(self):
        with self.assertRaises(AssertionError):
            _ = self._2x2_5124 - self._3x1_512

    # ----- tests for Matrix Transpose ------------------
    def test_transpose_1x3(self):
        actual = self._3x1_123.transpose()
        expected = self._1x3_123
        self.assertEqual(actual, expected)

        actual2 = self._3x1_123.T()
        self.assertEqual(actual2, expected)

    def test_transpose_1x3_reverse_transpose(self):
        actual = self._1x3_123.transpose()
        expected = self._3x1_123
        self.assertEqual(actual, expected)

        actual2 = self._1x3_123.T()
        self.assertEqual(actual2, expected)

    def test_transpose_3x3(self):
        actual = self._3x3_101211423.transpose()
        expected = self._3x3_101211423T
        self.assertEqual(actual, expected)

        actual2 = self._3x3_101211423.T()
        self.assertEqual(actual2, expected)

    def test_transpose_3x3_reverse_transpose(self):
        actual = self._3x3_101211423T.transpose()
        expected = self._3x3_101211423
        self.assertEqual(actual, expected)

        actual2 = self._3x3_101211423T.T()
        self.assertEqual(actual2, expected)

    def test_transpose_2x3(self):
        actual = self._2x3_023115.transpose()
        expected = self._3x2_023115
        self.assertEqual(actual, expected)

        actual2 = self._2x3_023115.T()
        self.assertEqual(actual2, expected)

    def test_transpose_3x2_reverse_transpose(self):
        actual = self._3x2_023115.transpose()
        expected = self._2x3_023115
        self.assertEqual(actual, expected)

        actual2 = self._3x2_023115.T()
        self.assertEqual(actual2, expected)

    # ----- tests abs ---------------------------------
    def test_abs_0(self):
        expected = self._3x2_023115
        actual = abs(self._3x2_023115_neg)
        self.assertEqual(actual, expected)

    def test_abs_1(self):
        expected = self._3x3_012211348
        actual = abs(self._3x3_012211348_neg)
        self.assertEqual(actual, expected)

    def test_abs_2(self):
        expected = self._3x1_512
        actual = abs(self._3x1_512_neg)
        self.assertEqual(actual, expected)

    # ----- tests scale -------------------------------
    def test_scale_by_0(self):
        expected = Matrix([[0, 0], [0, 0]])
        actual = self._2x2_1234.scale(0)
        self.assertEqual(actual, expected)

    def test_scale_by_1(self):
        expected = Matrix([[1, 2], [3, 4]])
        actual = self._2x2_1234.scale(1)
        self.assertEqual(actual, expected)

    def test_scale_by_3(self):
        expected = Matrix([[3, 6], [9, 12]])
        actual = self._2x2_1234.scale(3)
        self.assertEqual(actual, expected)

    # ----- tests clone/copy --------------------------
    def test_clone_2x2(self):
        expected = Matrix([[1, 2], [3, 4]])
        actual = self._2x2_1234.clone()
        self.assertIsNot(expected, actual)
        self.assertEqual(actual, expected)

    def test_clone_2x3(self):
        expected = Matrix([[0, 2, 3], [1, 1, 5]])
        actual = self._2x3_023115.clone()
        self.assertIsNot(expected, actual)
        self.assertEqual(actual, expected)

    # ----- tests clone/copy --------------------------
    def test_summation_2x2(self):
        expected = 10
        actual = self._2x2_1234.summation()
        self.assertEqual(actual, expected)

    def test_summation_2x3(self):
        expected = 12
        actual = self._2x3_023115.summation()
        self.assertEqual(actual, expected)

    # ----- tests str and repr-------------------------
    def test_str_3x2(self):
        expected = "[[     0,   3/10],\n [(2+3j),      3],\n [ 2.123,  1.001]]"
        actual = str(Matrix([[0, Fraction(3, 10)], [complex(2, 3), 3], [2.123, 1.001]]))
        self.assertEqual(actual, expected)

    def test_repr(self):
        expected = "Matrix([[1, 2], [2, 3], [3, 4]])"
        actual = repr(Matrix([[1, 2], [2, 3], [3, 4]]))
        self.assertEqual(actual, expected)

    # ----- tests identity() factory ------------------
    def test_identity_1x1(self):
        actual = identity((1, 1))
        expected = self.identity_1
        self.assertEqual(actual, expected)

    def test_identity_2x2(self):
        actual = identity(MatrixShape(num_rows=2, num_cols=2))
        expected = self.identity_2
        self.assertEqual(actual, expected)

    def test_identity_3x3(self):
        actual = identity((3, 3))
        expected = self.identity_3
        self.assertEqual(actual, expected)

    def test_identity_not_square(self):
        with self.assertRaises(AssertionError):
            identity((2, 3))

    # ----- tests zeros() factory ------------------
    def test_zeros_2x1(self):
        actual = zeros((2, 1))
        expected = self.null_2_1
        self.assertEqual(actual, expected)

    def test_zeros_2x2(self):
        actual = zeros((2, 2))
        expected = self.null_2_2
        self.assertEqual(actual, expected)

    def test_zeros_3x3(self):
        actual = zeros((3, 3))
        expected = self.null_3_3
        self.assertEqual(actual, expected)

    def test_zeros_4x4(self):
        actual = zeros((4, 4))
        expected = self.null_4_4
        self.assertEqual(actual, expected)

    def test_zeros_2x4(self):
        actual = zeros((2, 4))
        expected = self.null_2_4
        self.assertEqual(actual, expected)

    def test_zeros_4x2(self):
        actual = zeros((4, 2))
        expected = self.null_4_2
        self.assertEqual(actual, expected)


class MatrixComplexTests(unittest.TestCase):

    def setUp(self):
        # self.complex1_2_2 = MatrixComplex([[complex(1, math.sqrt(2)), complex(math.sqrt(2), 1)],
        #                                    [complex(1, -2), complex(2, -1)]])
        # self.complex2_2_2 = MatrixComplex([[complex(1, 1.414213562), complex(1.414213562, 1)],
        #                                    [complex(1, -2), complex(2, -1.000000001)]])
        pass

    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            data = [[complex(1, math.sqrt(2)), complex(math.sqrt(2), 1)],
                    [complex(1, -2), complex(2, -1)]]
            MatrixComplex(data)

    # def test_equality_matrix_of_complex_irrationals_True(self):
    #     self.assertEqual(self.complex1_2_2, self.complex2_2_2)


if __name__ == '__main__':
    unittest.main()
