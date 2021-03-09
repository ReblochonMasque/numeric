"""
from nompy
"""


import unittest

from fractions import Fraction

from numeric.src.matrix import Matrix, Shape, IncompatibleMatrixShapes, MatrixIndexError


class TestShape(unittest.TestCase):

    def setUp(self):
        self.s_1x1 = Shape(rows=1, cols=1)
        self.s_2x4 = Shape(rows=2, cols=4)
        self.s_4x2 = Shape(rows=4, cols=2)

    def test_is_instance_1x1(self):
        self.assertIsInstance(self.s_1x1, Shape)

    def test_is_instance_2x4(self):
        self.assertIsInstance(self.s_2x4, Shape)

    def test_rows_cols_1x1(self):
        self.assertEqual(self.s_1x1.rows, 1)
        self.assertEqual(self.s_1x1.cols, 1)

    def test_rows_cols_2x4(self):
        self.assertEqual(self.s_2x4.rows, 2)
        self.assertEqual(self.s_2x4.cols, 4)

    def test_rows_cols_4x2(self):
        self.assertEqual(self.s_4x2.rows, 4)
        self.assertEqual(self.s_4x2.cols, 2)


class TestMatrix(unittest.TestCase):

    def setUp(self):

        self._1x1 = Matrix([[1]])
        self._2x2 = Matrix([[1, 2], [3, 4]])
        self._3x3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self._4x4 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        self._2x4 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
        self._4x2 = Matrix([[1, 5], [2, 6], [3, 7], [4, 8]])
        self._1x4 = Matrix([[1, 2, 3, 4]])
        self._4x1 = Matrix([[1], [2], [3], [4]])

        self._2x2_zeros = Matrix([[0, 0], [0, 0]])
        self._3x3_zeros = Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self._2x4_zeros = Matrix([[0, 0, 0, 0], [0, 0, 0, 0]])
        self._4x2_zeros = Matrix([[0, 0], [0, 0], [0, 0], [0, 0]])
        self._4x4_zeros = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

        self._I1 = Matrix([[1]])
        self._I2 = Matrix([[1, 0], [0, 1]])
        self._I3 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self._I4 = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    # ------ INSTANCE --------------------------------------------------

    def test_is_instance_1x1(self):
        self.assertIsInstance(self._1x1, Matrix)

    def test_is_instance_2x2(self):
        self.assertIsInstance(self._2x2, Matrix)

    def test_is_instance_3x3(self):
        self.assertIsInstance(self._3x3, Matrix)

    def test_is_instance_4x4(self):
        self.assertIsInstance(self._4x4, Matrix)

    def test_is_instance_2x4(self):
        self.assertIsInstance(self._2x4, Matrix)

    def test_is_instance_4x2(self):
        self.assertIsInstance(self._4x2, Matrix)

    # ------ DEEPCOPY OF SEQUENCE PASSED TO __init__ -------------------

    def test_deepcopy_seq_1x1(self):
        seq = [[1]]
        original = id(seq)
        actual = id(Matrix(seq)._data)
        self.assertIsNot(original, actual)

    def test_deepcopy_seq_4x2(self):
        seq = [[1, 5], [2, 6], [3, 7], [4, 8]]
        original = id(seq)
        actual = id(Matrix(seq)._data)
        self.assertIsNot(original, actual)

    def test_deepcopy_seq_4x4(self):
        seq = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        original = id(seq)
        actual = id(Matrix(seq)._data)
        self.assertIsNot(original, actual)

    # ------ MALFORMED -------------------------------------------------

    def test_empty(self):
        with self.assertRaises(AssertionError):
            Matrix([])

    def test_row_empty(self):
        with self.assertRaises(AssertionError):
            Matrix([[1, 2, 3], [4, 5, 6], []])

    # ------ ROWs COLs -------------------------------------------------

    def test_row_col_1x1(self):
        r, c = self._1x1._rows, self._1x1._cols
        self.assertEqual((r, c), (1, 1))

    def test_row_col_2x2(self):
        r, c = self._2x2._rows, self._2x2._cols
        self.assertEqual((r, c), (2, 2))

    def test_row_col_2x4(self):
        r, c = self._2x4._rows, self._2x4._cols
        self.assertEqual((r, c), (2, 4))

    def test_row_col_4x2(self):
        r, c = self._4x2._rows, self._4x2._cols
        self.assertEqual((r, c), (4, 2))

    # ------ SHAPE -----------------------------------------------------

    def test_shape_1x1(self):
        """test row, col via Matrix.shape property
        """
        self.assertEqual(self._1x1.shape, (1, 1))

    def test_Shape_1x1(self):
        """test row, col via Matrix.shape property, against
        NamedTuple Shape
        """
        self.assertEqual(self._1x1.shape, Shape(1, 1))

    def test_shape_2x2(self):
        """test row, col via Matrix.shape property
        """
        self.assertEqual(self._2x2.shape, (2, 2))

    def test_Shape_2x2(self):
        """test row, col via Matrix.shape property, against
        NamedTuple Shape
        """
        self.assertEqual(self._2x2.shape, Shape(2, 2))

    def test_shape_2x4(self):
        """test row, col via Matrix.shape property
        """
        self.assertEqual(self._2x4.shape, (2, 4))

    def test_Shape_2x4(self):
        """test row, col via Matrix.shape property, against
        NamedTuple Shape
        """
        self.assertEqual(self._2x4.shape, Shape(2, 4))

    def test_shape_4x2(self):
        """test row, col via Matrix.shape property
        """
        self.assertEqual(self._4x2.shape, (4, 2))

    def test_Shape_4x2(self):
        """test row, col via Matrix.shape property, against
        NamedTuple Shape
        """
        self.assertEqual(self._4x2.shape, Shape(4, 2))

    # ------ EQUALITY --------------------------------------------------

    def test__eq__1x1(self):
        m1x1 = Matrix([[1]])
        self.assertEqual(self._1x1, m1x1)

    def test__not_eq__1x1(self):
        m1x1 = Matrix([[42]])
        self.assertNotEqual(self._1x1, m1x1)

    def test__eq__2x2(self):
        m2x2 = Matrix([[1, 2], [3, 4]])
        self.assertEqual(self._2x2, m2x2)

    def test__not_eq__2x2(self):
        m2x2 = Matrix([[1, 3], [2, 4]])
        self.assertNotEqual(self._2x2, m2x2)

    def test__eq__2x4(self):
        m2x4 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
        self.assertEqual(self._2x4, m2x4)

    def test__not_eq__2x4(self):
        m2x4 = Matrix([[1, 42, 3, 4], [5, 6, 7, 8]])
        self.assertNotEqual(self._2x4, m2x4)

    def test__eq__wrong_shapes(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            self.assertEqual(self._2x4, self._2x2)
            expected_msg = 'Matrices must have identical shapes to be compared'
            self.assertEqual(expected_msg, str(e))

    def test__eq__wrong_types(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(self._2x2, [[1, 2], [3, 4]])
            expected_msg = 'a Matrix must be compared to a Matrix'
            self.assertEqual(expected_msg, str(e))

    # ------ SETITEM ---------------------------------------------------

    def test_set_value_with_row_col(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        actual[1, 1] = 3
        actual[2, 3] = 5
        actual[3, 1] = 4
        actual[4, 4] = 9
        self.assertEqual(expected, actual)

    def test_set_value_with_negative_row_col(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        actual[-4, -4] = 3
        actual[-3, -2] = 5
        actual[-2, -4] = 4
        actual[-1, -1] = 9
        self.assertEqual(expected, actual)

    def test_set_value_with_mixed_negative_and_positive_row_col(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        actual[1, -4] = 3
        actual[-3, 3] = 5
        actual[-2, 1] = 4
        actual[4, -1] = 9
        self.assertEqual(expected, actual)

    def test_set_value_with_index_too_large_row(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        with self.assertRaises(MatrixIndexError) as e:
            actual[10, 2] = 3
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_set_value_with_index_too_large_col(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        with self.assertRaises(MatrixIndexError) as e:
            actual[2, 10] = 3
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_set_value_with_index_too_large_row_col(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        with self.assertRaises(MatrixIndexError) as e:
            actual[10, 10] = 3
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_set_value_with_index_too_low_row(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        with self.assertRaises(MatrixIndexError) as e:
            actual[-10, -2] = 3
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_set_value_with_index_too_low_col(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        with self.assertRaises(MatrixIndexError) as e:
            actual[-2, -10] = 3
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_set_value_with_index_too_low_row_col(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 3, 0, 0, 0],
                           [0, 0, 0, 5, 0],
                           [0, 4, 0, 0, 0],
                           [0, 0, 0, 0, 9]])
        actual = Matrix([[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]])
        with self.assertRaises(MatrixIndexError) as e:
            actual[-10, -10] = 3
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    # ------ GETITEM ---------------------------------------------------

    def test_get_value_with_row_col(self):
        expected = (3, 5, 4, 9)
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        actual = (mat[1, 1], mat[2, 3], mat[3, 1], mat[4, 4])
        self.assertEqual(expected, actual)

    def test_get_value_with_negative_row_col(self):
        expected = (3, 5, 4, 9)
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        actual = (mat[-4, -4], mat[-3, -2], mat[-2, -4], mat[-1, -1])
        self.assertEqual(expected, actual)

    def test_get_value_with_mixed_negative_and_positive_row_col(self):
        expected = (3, 5, 4, 9)
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        actual = (mat[1, -4], mat[-3, 3], mat[-2, 1], mat[4, -1])
        self.assertEqual(expected, actual)

    def test_get_value_with_index_too_large_row(self):
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        with self.assertRaises(MatrixIndexError) as e:
            v = mat[10, 2]
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_get_value_with_index_too_large_col(self):
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        with self.assertRaises(MatrixIndexError) as e:
            v = mat[2, 10]
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_get_value_with_index_too_large_row_col(self):
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        with self.assertRaises(MatrixIndexError) as e:
            v = mat[10, 10]
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_get_value_with_index_too_low_row(self):
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        with self.assertRaises(MatrixIndexError) as e:
            v = mat[-10, -2]
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_get_value_with_index_too_low_col(self):
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        with self.assertRaises(MatrixIndexError) as e:
            v = mat[-2, -10]
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    def test_get_value_with_index_too_low_row_col(self):
        mat = Matrix([[0, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 4, 0, 0, 0],
                      [0, 0, 0, 0, 9]])
        with self.assertRaises(MatrixIndexError) as e:
            v = mat[-10, -10]
            self.assertEqual(str(e), 'Matrix indices row or col out of range')

    # ------ ZEROS CONSTRUCTOR -----------------------------------------

    def test_zeros_1x1(self):
        expected = Matrix([[0]])
        r, c = 1, 1
        actual = Matrix.zeros(Shape(rows=r, cols=c))
        self.assertEqual(expected, actual)

    def test_zeros_1x2(self):
        expected = Matrix([[0, 0]])
        r, c = 1, 2
        actual = Matrix.zeros(Shape(rows=r, cols=c))
        self.assertEqual(expected, actual)

    def test_zeros_2x1(self):
        expected = Matrix([[0], [0]])
        r, c = 2, 1
        actual = Matrix.zeros(Shape(rows=r, cols=c))
        self.assertEqual(expected, actual)

    def test_zeros_5x3(self):
        expected = Matrix([[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]])
        r, c = 5, 3
        actual = Matrix.zeros(Shape(rows=r, cols=c))
        self.assertEqual(expected, actual)

    def test_zeros_3x5(self):
        expected = Matrix([[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]])
        r, c = 3, 5
        actual = Matrix.zeros(Shape(rows=r, cols=c))
        self.assertEqual(expected, actual)

    # ------ IDENTITY CONSTRUCTOR --------------------------------------

    def test_identity_1x1(self):
        expected = Matrix([[1]])
        r = 1
        c = r
        actual = Matrix.identity(Shape(rows=r, cols=c))
        self.assertEqual(expected, actual)

    def test_identity_2x2(self):
        expected = Matrix([[1, 0],
                           [0, 1]])
        r = 2
        c = r
        actual = Matrix.identity(Shape(rows=r, cols=c))
        self.assertEqual(expected, actual)

    def test_identity_4x4(self):
        expected = Matrix([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        r = 4
        c = r
        actual = Matrix.identity(Shape(rows=r, cols=c))
        self.assertEqual(expected, actual)

    def test_non_square_identity_3x4(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            m = Matrix.identity(Shape(rows=3, cols=4))
            expected_msg = 'Identity Matrix must be square'
            self.assertEqual(expected_msg, str(e))

    def test_non_square_identity_4x3(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            m = Matrix.identity(Shape(rows=4, cols=3))
            expected_msg = 'Identity Matrix must be square'
            self.assertEqual(expected_msg, str(e))

    # ------ TRANSPOSE -------------------------------------------------

    def test_transpose_1x1(self):
        self.assertEqual(self._1x1.transpose(), Matrix([[1]]))
        self.assertEqual(self._1x1.T(), Matrix([[1]]))

    def test_transpose_2x2(self):
        self.assertEqual(self._2x2.transpose(), Matrix([[1, 3], [2, 4]]))
        self.assertEqual(self._2x2.T(), Matrix([[1, 3], [2, 4]]))

    def test_transpose_2x4(self):
        self.assertEqual(self._2x4.transpose(), Matrix([[1, 5], [2, 6], [3, 7], [4, 8]]))
        self.assertEqual(self._2x4.T(), Matrix([[1, 5], [2, 6], [3, 7], [4, 8]]))

    def test_transpose_4x2(self):
        self.assertEqual(self._4x2.transpose(), Matrix([[1, 2, 3, 4], [5, 6, 7, 8]]))
        self.assertEqual(self._4x2.T(), Matrix([[1, 2, 3, 4], [5, 6, 7, 8]]))

    def test_transpose_1x4(self):
        self.assertEqual(self._1x4.transpose(), Matrix([[1], [2], [3], [4]]))
        self.assertEqual(self._1x4.T(), Matrix([[1], [2], [3], [4]]))

    def test_transpose_4x1(self):
        self.assertEqual(self._4x1.transpose(), Matrix([[1, 2, 3, 4]]))
        self.assertEqual(self._4x1.T(), Matrix([[1, 2, 3, 4]]))

    def test_transpose_go_and_back_0(self):
        self.assertEqual(self._1x1, self._1x1.T().transpose())

    def test_transpose_go_and_back_1(self):
        self.assertEqual(self._2x2, self._2x2.T().transpose())

    def test_transpose_go_and_back_2(self):
        self.assertEqual(self._3x3, self._3x3.T().transpose())

    def test_transpose_go_and_back_3(self):
        self.assertEqual(self._4x4, self._4x4.T().transpose())

    def test_transpose_go_and_back_4(self):
        self.assertEqual(self._2x4, self._2x4.T().transpose())

    def test_transpose_go_and_back_5(self):
        self.assertEqual(self._4x2, self._4x2.T().transpose())

    def test_transpose_go_and_back_6(self):
        self.assertEqual(self._1x4, self._1x4.T().transpose())

    def test_transpose_go_and_back_7(self):
        self.assertEqual(self._4x1, self._4x1.T().transpose())

    # ------ NEGATION --------------------------------------------------

    def test_neg_1x1(self):
        expected = Matrix([[-1]])
        self.assertEqual(expected, -self._1x1)

    def test_neg_2x2(self):
        expected = Matrix([[-1, -2], [-3, -4]])
        self.assertEqual(expected, -self._2x2)

    def test_neg_2x4(self):
        expected = Matrix([[-1, -2, -3, -4], [-5, -6, -7, -8]])
        self.assertEqual(expected, -self._2x4)

    def test_neg_4x4_zeros(self):
        expected = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self.assertEqual(expected, -self._4x4_zeros)

    def test_neg_1x1_same_instance(self):
        prior = self._1x1
        self.assertIs(prior, -self._1x1)

    def test_neg_2x2_same_instance(self):
        prior = self._2x2
        self.assertIs(prior, -self._2x2)

    def test_neg_2x4_same_instance(self):
        prior = self._2x4
        self.assertIs(prior, -self._2x4)

    def test_neg_4x4_zeros_same_instance(self):
        prior = self._4x4_zeros
        self.assertIs(prior, -self._4x4_zeros)

    # ------ MULTIPLICATION BY A SCALAR --------------------------------

    def test_mat_multiplied_by_scalar_1x1_by_minus1(self):
        expected = Matrix([[-1]])
        actual = self._1x1 * -1
        self.assertEqual(expected, actual)

    def test_mat_multiplied_by_scalar_2x2_by_12(self):
        expected = Matrix([[12, 24], [36, 48]])
        actual = self._2x2 * 12
        self.assertEqual(expected, actual)

    def test_mat_multiplied_by_scalar_2x4_by_minus10(self):
        expected = Matrix([[-10, -20, -30, -40], [-50, -60, -70, -80]])
        actual = self._2x4 * -10
        self.assertEqual(expected, actual)

    def test_mat_multiply_by_scalar_4x4_zeros_by_744_123(self):
        expected = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        actual = self._4x4_zeros * 744.123
        self.assertEqual(expected, actual)

    def test_scalar_multiplied_by_mat_1x1_by_minus1(self):
        expected = Matrix([[-1]])
        actual = -1 * self._1x1
        self.assertEqual(expected, actual)

    def test_scalar_multiplied_by_mat_2x2_by_12(self):
        expected = Matrix([[12, 24], [36, 48]])
        actual = 12 * self._2x2
        self.assertEqual(expected, actual)

    def test_scalar_multiplied_by_mat_2x4_by_minus10(self):
        expected = Matrix([[-10, -20, -30, -40], [-50, -60, -70, -80]])
        actual = -10 * self._2x4
        self.assertEqual(expected, actual)

    def test_scalar_multiplied_by_mat_4x4_zeros_by_744_123(self):
        expected = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        actual = 744.123 * self._4x4_zeros
        self.assertEqual(expected, actual)

    def test_imultiplied_by_scalar_1x1_by_minus1(self):
        expected = Matrix([[-1]])
        self._1x1 *= -1
        self.assertEqual(expected, self._1x1)

    def test_imultiplied_by_scalar_2x2_by_12(self):
        expected = Matrix([[12, 24], [36, 48]])
        self._2x2 *= 12
        self.assertEqual(expected, self._2x2)

    def test_imultiplied_by_scalar_2x4_by_minus10(self):
        expected = Matrix([[-10, -20, -30, -40], [-50, -60, -70, -80]])
        self._2x4 *= -10
        self.assertEqual(expected, self._2x4)

    def test_imultiply_by_scalar_4x4_zeros_by_744_123(self):
        expected = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self._4x4_zeros *= 744.123
        self.assertEqual(expected, self._4x4_zeros)

    def test_imultiplied_by_scalar_1x1_by_minus1_same_instance(self):
        expected = Matrix([[-1]])
        prior = self._1x1
        self._1x1 *= -1
        self.assertIs(prior, self._1x1)

    def test_imultiplied_by_scalar_2x2_by_12_same_instance(self):
        expected = Matrix([[12, 24], [36, 48]])
        prior = self._2x2
        self._2x2 *= 12
        self.assertIs(prior, self._2x2)

    def test_imultiplied_by_scalar_2x4_by_minus10_same_instance(self):
        expected = Matrix([[-10, -20, -30, -40], [-50, -60, -70, -80]])
        prior = self._2x4
        self._2x4 *= -10
        self.assertIs(prior, self._2x4)

    def test_imultiply_by_scalar_4x4_zeros_by_744_123_same_instance(self):
        expected = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        prior = self._4x4_zeros
        self._4x4_zeros *= 744.123
        self.assertIs(prior, self._4x4_zeros)

    # ------ TRUE DIVISION BY A SCALAR --------------------------------------

    def test_mat_true_division_by_scalar_1x1_by_minus1(self):
        expected = Matrix([[-1]])
        actual = self._1x1 / -1
        self.assertEqual(expected, actual)

    def test_mat_true_division_by_scalar_2x2_by_2(self):
        expected = Matrix([[0.5, 1], [1.5, 2]])
        actual = self._2x2 / 2
        self.assertEqual(expected, actual)

    def test_mat_true_division_by_scalar_2x4_by_minus10(self):
        expected = Matrix([[-.1, -.2, -.3, -.4], [-.5, -.6, -.7, -.8]])
        actual = self._2x4 / -10
        self.assertEqual(expected, actual)

    def test_mat_true_division_by_scalar_4x4_zeros_by_744_123(self):
        expected = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        actual = self._4x4_zeros / 744.123
        self.assertEqual(expected, actual)

    def test_mat_true_division_by_scalar_4x4_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as e:
            m = self._4x4 / 0
            expected_msg = 'the divisor must be non zero'
            self.assertEqual(expected_msg, str(e))

    def test_itrue_division_by_scalar_1x1_by_minus1(self):
        expected = Matrix([[-1]])
        self._1x1 /= -1
        self.assertEqual(expected, self._1x1)

    def test_itrue_division_by_scalar_2x2_by_2(self):
        expected = Matrix([[0.5, 1.0], [1.5, 2.0]])
        self._2x2 /= 2
        self.assertEqual(expected, self._2x2)

    def test_itrue_division_by_scalar_2x4_by_minus10(self):
        expected = Matrix([[-.1, -.2, -.3, -.4], [-.5, -.6, -.7, -.8]])
        self._2x4 /= -10
        self.assertEqual(expected, self._2x4)

    def test_itrue_division_by_scalar_4x4_zeros_by_744_123(self):
        expected = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        self._4x4_zeros /= 744.123
        self.assertEqual(expected, self._4x4_zeros)

    def test_itrue_division_by_scalar_1x1_by_minus1_same_instance(self):
        expected = Matrix([[-1]])
        prior = self._1x1
        self._1x1 /= -1
        self.assertIs(prior, self._1x1)

    def test_itrue_division_by_scalar_2x2_by_2_same_instance(self):
        expected = Matrix([[0.5, 1.0], [1.5, 2.0]])
        prior = self._2x2
        self._2x2 /= 2
        self.assertIs(prior, self._2x2)

    def test_itrue_division_by_scalar_2x4_by_minus10_same_instance(self):
        expected = Matrix([[-.1, -.2, -.3, -.4], [-.5, -.6, -.7, -.8]])
        prior = self._2x4
        self._2x4 /= -10
        self.assertIs(prior, self._2x4)

    def test_itrue_division_by_scalar_4x4_zeros_by_744_123_same_instance(self):
        expected = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        prior = self._4x4_zeros
        self._4x4_zeros /= 744.123
        self.assertIs(prior, self._4x4_zeros)

    def test_itrue_division_by_scalar_4x4_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as e:
            self._4x4 /= 0
            expected_msg = 'the divisor must be non zero'
            self.assertEqual(expected_msg, str(e))

    # ------ ADDITION OF TWO MATRICES ----------------------------------

    def test_addition_2x2(self):
        expected = Matrix([[2, 4], [6, 8]])
        actual = self._2x2 + self._2x2
        self.assertEqual(expected, actual)

    def test_addition_2x2_2x2_zeros(self):
        expected = Matrix([[1, 2], [3, 4]])
        actual = self._2x2 + self._2x2_zeros
        self.assertEqual(expected, actual)

    def test_addition_2x2_zeros_2x2(self):
        expected = Matrix([[1, 2], [3, 4]])
        actual = self._2x2_zeros + self._2x2
        self.assertEqual(expected, actual)

    def test_addition_2x4_2x4_reversed(self):
        expected = Matrix([[9, 9, 9, 9], [9, 9, 9, 9]])
        actual = self._2x4 + Matrix([[8, 7, 6, 5], [4, 3, 2, 1]])
        self.assertEqual(expected, actual)

    def test_addition_incompatible_sizes_numrows(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            m = self._4x4 + self._2x4
            expected_msg = 'Matrices must have identical shapes to be added'
            self.assertEqual(expected_msg, str(e))

    def test_addition_incompatible_sizes_numcols(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            m = self._4x4 + self._4x2
            expected_msg = 'Matrices must have identical shapes to be added'
            self.assertEqual(expected_msg, str(e))

    def test_addition_incompatible_sizes_num_rows_cols(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            m = self._4x4 + self._3x3
            expected_msg = 'Matrices must have identical shapes to be added'
            self.assertEqual(expected_msg, str(e))

    def test_iadd_2x2(self):
        expected = Matrix([[2, 4], [6, 8]])
        self._2x2 += self._2x2
        self.assertEqual(expected, self._2x2)

    def test_iadd_2x2_2x2_zeros(self):
        expected = Matrix([[1, 2], [3, 4]])
        self._2x2 += self._2x2_zeros
        self.assertEqual(expected, self._2x2)

    def test_iadd_2x2_zeros_2x2(self):
        expected = Matrix([[1, 2], [3, 4]])
        self._2x2_zeros += self._2x2
        self.assertEqual(expected, self._2x2_zeros)

    def test_iadd_2x4_2x4_reversed(self):
        expected = Matrix([[9, 9, 9, 9], [9, 9, 9, 9]])
        self._2x4 += Matrix([[8, 7, 6, 5], [4, 3, 2, 1]])
        self.assertEqual(expected, self._2x4)

    def test_iadd_2x2_same_instance(self):
        expected = Matrix([[2, 4], [6, 8]])
        prior = self._2x2
        self._2x2 += self._2x2
        self.assertIs(prior, self._2x2)

    def test_iadd_2x2_2x2_zeros_same_instance(self):
        expected = Matrix([[1, 2], [3, 4]])
        prior = self._2x2
        self._2x2 += self._2x2_zeros
        self.assertIs(prior, self._2x2)

    def test_iadd_2x2_zeros_2x2_same_instance(self):
        expected = Matrix([[1, 2], [3, 4]])
        prior = self._2x2_zeros
        self._2x2_zeros += self._2x2
        self.assertIs(prior, self._2x2_zeros)

    def test_iadd_2x4_2x4_reversed_same_instance(self):
        expected = Matrix([[9, 9, 9, 9], [9, 9, 9, 9]])
        prior = self._2x4
        self._2x4 += Matrix([[8, 7, 6, 5], [4, 3, 2, 1]])
        self.assertIs(prior, self._2x4)

    def test_iadd_incompatible_sizes_numrows(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            self._4x4 += self._2x4
            expected_msg = 'Matrices must have identical shapes to be added'
            self.assertEqual(expected_msg, str(e))

    def test_iadd_incompatible_sizes_numcols(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            self._4x4 += self._4x2
            expected_msg = 'Matrices must have identical shapes to be added'
            self.assertEqual(expected_msg, str(e))

    def test_iadd_incompatible_sizes_num_rows_cols(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            self._4x4 += self._3x3
            expected_msg = 'Matrices must have identical shapes to be added'
            self.assertEqual(expected_msg, str(e))

    # ------ SUBTRACTION OF TWO MATRICES -------------------------------

    def test_subtraction_2x2(self):
        expected = self._2x2_zeros
        actual = self._2x2 - self._2x2
        self.assertEqual(expected, actual)

    def test_subtraction_2x2_2x2_zeros(self):
        expected = Matrix([[1, 2], [3, 4]])
        actual = self._2x2 - self._2x2_zeros
        self.assertEqual(expected, actual)

    def test_subtraction_2x2_zeros_2x2(self):
        expected = Matrix([[-1, -2], [-3, -4]])
        actual = self._2x2_zeros - self._2x2
        self.assertEqual(expected, actual)

    def test_subtraction_2x4_2x4_reversed(self):
        expected = Matrix([[-7, -5, -3, -1], [1, 3, 5, 7]])
        actual = self._2x4 - Matrix([[8, 7, 6, 5], [4, 3, 2, 1]])
        self.assertEqual(expected, actual)

    def test_subtraction_incompatible_sizes_numrows(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            m = self._4x4 - self._2x4
            expected_msg = 'Matrices must have identical shapes to be subtracted'
            self.assertEqual(expected_msg, str(e))

    def test_subtraction_incompatible_sizes_numcols(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            m = self._4x4 - self._4x2
            expected_msg = 'Matrices must have identical shapes to be subtracted'
            self.assertEqual(expected_msg, str(e))

    def test_subtraction_incompatible_sizes_num_rows_cols(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            m = self._4x4 - self._3x3
            expected_msg = 'Matrices must have identical shapes to be subtracted'
            self.assertEqual(expected_msg, str(e))

    def test_isub_2x2(self):
        expected = self._2x2_zeros
        self._2x2 -= self._2x2
        self.assertEqual(expected, self._2x2)

    def test_isub_2x2_2x2_zeros(self):
        expected = Matrix([[1, 2], [3, 4]])
        self._2x2 -= self._2x2_zeros
        self.assertEqual(expected, self._2x2)

    def test_isub_2x2_zeros_2x2(self):
        expected = Matrix([[-1, -2], [-3, -4]])
        self._2x2_zeros -= self._2x2
        self.assertEqual(expected, self._2x2_zeros)

    def test_isub_2x4_2x4_reversed(self):
        expected = Matrix([[-7, -5, -3, -1], [1, 3, 5, 7]])
        self._2x4 -= Matrix([[8, 7, 6, 5], [4, 3, 2, 1]])
        self.assertEqual(expected, self._2x4)

    def test_isub_2x2_same_instance(self):
        expected = self._2x2_zeros
        prior = self._2x2
        self._2x2 -= self._2x2
        self.assertIs(prior, self._2x2)

    def test_isub_2x2_2x2_zeros_same_instance(self):
        expected = Matrix([[1, 2], [3, 4]])
        prior = self._2x2
        self._2x2 -= self._2x2_zeros
        self.assertIs(prior, self._2x2)

    def test_isub_2x2_zeros_2x2_same_instance(self):
        expected = Matrix([[-1, -2], [-3, -4]])
        prior = self._2x2_zeros
        self._2x2_zeros -= self._2x2
        self.assertIs(prior, self._2x2_zeros)

    def test_isub_2x4_2x4_reversed_same_instance(self):
        expected = Matrix([[-7, -5, -3, -1], [1, 3, 5, 7]])
        prior = self._2x4
        self._2x4 -= Matrix([[8, 7, 6, 5], [4, 3, 2, 1]])
        self.assertIs(prior, self._2x4)

    def test_isub_incompatible_sizes_numrows(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            self._4x4 -= self._2x4
            expected_msg = 'Matrices must have identical shapes to be subtracted'
            self.assertEqual(expected_msg, str(e))

    def test_isub_incompatible_sizes_numcols(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            self._4x4 -= self._4x2
            expected_msg = 'Matrices must have identical shapes to be subtracted'
            self.assertEqual(expected_msg, str(e))

    def test_isub_incompatible_sizes_num_rows_cols(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            self._4x4 -= self._3x3
            expected_msg = 'Matrices must have identical shapes to be subtracted'
            self.assertEqual(expected_msg, str(e))

    # ------ MATRIX MULTIPLICATION -------------------------------------
    # ---TYPE OF OTHER ---
    def test_matmul_wrong_type_list(self):
        with self.assertRaises(TypeError) as e:
            _ = self._2x2 @ [[1, 2], [3, 4]]
            expected_msg = 'Matrix multiplication must multiply two Matrices'
            self.assertEqual(expected_msg, str(e))

    def test_matmul_wrong_type_list_of_tuples(self):
        with self.assertRaises(TypeError) as e:
            _ = self._2x2 @ [(1, 2), (3, 4)]
            expected_msg = 'Matrix multiplication must multiply two Matrices'
            self.assertEqual(expected_msg, str(e))

    def test_matmul_wrong_type_tuple_of_tuples(self):
        with self.assertRaises(TypeError) as e:
            _ = self._2x2 @ ((1, 2), (3, 4))
            expected_msg = 'Matrix multiplication must multiply two Matrices'
            self.assertEqual(expected_msg, str(e))

    def test_matmul_wrong_type_list_wrong_order(self):
        with self.assertRaises(TypeError) as e:
            _ = [[1, 2], [3, 4]] @ self._2x2
            expected_msg = 'Matrix multiplication must multiply two Matrices'
            self.assertEqual(expected_msg, str(e))

    def test_matmul_wrong_type_list_of_tuples_wrong_order(self):
        with self.assertRaises(TypeError) as e:
            _ = [(1, 2), (3, 4)] @ self._2x2
            expected_msg = 'Matrix multiplication must multiply two Matrices'
            self.assertEqual(expected_msg, str(e))

    def test_matmul_wrong_type_tuple_of_tuples_wrong_order(self):
        with self.assertRaises(TypeError) as e:
            _ = ((1, 2), (3, 4)) @ self._2x2
            expected_msg = 'Matrix multiplication must multiply two Matrices'
            self.assertEqual(expected_msg, str(e))

    # ---SHAPE---
    def test_self_cols_ne_other_rows_2x2_x_4x2(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            _ = self._2x2 @ self._4x2
            expected_msg = 'Matrix A number of columns must equal Matrix B number of rows'
            self.assertEqual(expected_msg, str(e))

    def test_self_cols_ne_other_rows_2x4_x_2x4(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            _ = self._4x2 @ self._4x2
            expected_msg = 'Matrix A number of columns must equal Matrix B number of rows'
            self.assertEqual(expected_msg, str(e))

    def test_self_cols_ne_other_rows_4x2_x_4x2(self):
        with self.assertRaises(IncompatibleMatrixShapes) as e:
            _ = self._4x2 @ self._4x2
            expected_msg = 'Matrix A number of columns must equal Matrix B number of rows'
            self.assertEqual(expected_msg, str(e))

    # --- MATMUL ---
    def test_1x1_x_1x1(self):
        A = Matrix([[3]])
        B = Matrix([[5]])
        expected = Matrix([[15]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_1x3_x_3x1(self):
        A = Matrix([[1, 2, 3]])
        B = Matrix([[1],
                    [2],
                    [3]])
        expected = Matrix([[14]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_3x1_x_1x3(self):
        A = Matrix([[1],
                    [2],
                    [3]])
        B = Matrix([[1, 2, 3]])
        expected = Matrix([[1, 2, 3],
                           [2, 4, 6],
                           [3, 6, 9]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_3x2_x_2x3(self):
        A = Matrix([[1, 2],
                    [3, 4],
                    [5, 6]])
        B = Matrix([[1, 2, 3],
                    [4, 5, 6]])
        expected = Matrix([[9, 12, 15],
                           [19, 26, 33],
                           [29, 40, 51]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_2x3_x_3x2(self):
        A = Matrix([[1, 0, 0],
                    [0, 1, 0]])
        B = Matrix([[1, 0],
                    [0, 1],
                    [0, 0]])
        expected = Matrix([[1, 0],
                           [0, 1]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_2x2_x_2x2(self):
        A = Matrix([[1, 2],
                    [3, 4]])
        B = Matrix([[0, -1],
                    [2, -3]])
        expected = Matrix([[4, -7],
                           [8, -15]])
        actual = A @ B
        self.assertEqual(expected, actual)

    # --- MATMUL ZEROS ---
    def test_1x3_x_3x1_zeros(self):
        A = Matrix([[1, 2, 3]])
        B = Matrix([[0],
                    [0],
                    [0]])
        expected = Matrix([[0]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_3x1_x_1x3_zeros(self):
        A = Matrix([[1],
                    [2],
                    [3]])
        B = Matrix([[0, 0, 0]])
        expected = Matrix([[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_3x2_x_2x3_zeros(self):
        A = Matrix([[1, 2],
                    [3, 4],
                    [5, 6]])
        B = Matrix([[0, 0, 0],
                    [0, 0, 0]])
        expected = Matrix([[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_2x2_x_2x2_zeros(self):
        A = Matrix([[1, 2],
                    [3, 4]])
        B = Matrix([[0, 0],
                    [0, 0]])
        expected = Matrix([[0, 0],
                           [0, 0]])
        actual = A @ B
        self.assertEqual(expected, actual)

    def test_2x2_zeros_x_2x2(self):
        A = Matrix([[0, 0],
                    [0, 0]])
        B = Matrix([[1, 2],
                    [3, 4]])
        expected = Matrix([[0, 0],
                           [0, 0]])
        actual = A @ B
        self.assertEqual(expected, actual)

    # --- MATMUL IDENTITY ---
    def test_2x2_x_2x2_identity(self):
        A = Matrix([[1, 2],
                    [3, 4]])
        I2 = Matrix([[1, 0],
                     [0, 1]])
        expected = Matrix([[1, 2],
                           [3, 4]])
        actual = A @ I2
        self.assertEqual(expected, actual)

    def test_2x2_identity_x_2x2(self):
        A = Matrix([[1, 2],
                    [3, 4]])
        I2 = Matrix([[1, 0],
                     [0, 1]])
        expected = Matrix([[1, 2],
                           [3, 4]])
        actual = I2 @ A
        self.assertEqual(expected, actual)

    # ------ GETROW ----------------------------------------------------

    def test_get_row_1x1(self):
        expected = Matrix([[9]])
        actual = Matrix([[9]]).get_row(0)
        self.assertEqual(expected, actual)

    def test_get_row_2x2(self):
        expected = Matrix([[3, 4]])
        actual = Matrix([[1, 2], [3, 4]]).get_row(1)
        self.assertEqual(expected, actual)

    def test_get_row_3x3_0(self):
        expected = Matrix([[1, 2, 3]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_row(0)
        self.assertEqual(expected, actual)

    def test_get_row_3x3_1(self):
        expected = Matrix([[4, 5, 6]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_row(1)
        self.assertEqual(expected, actual)

    def test_get_row_3x3_2(self):
        expected = Matrix([[7, 8, 9]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_row(2)
        self.assertEqual(expected, actual)

    def test_get_row_3x3_minus_3(self):
        expected = Matrix([[1, 2, 3]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_row(-3)
        self.assertEqual(expected, actual)

    def test_get_row_3x3_1_minus_2(self):
        expected = Matrix([[4, 5, 6]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_row(-2)
        self.assertEqual(expected, actual)

    def test_get_row_3x3_2_minus_1(self):
        expected = Matrix([[7, 8, 9]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_row(-1)
        self.assertEqual(expected, actual)

    def test_get_row_out_of_range_too_large(self):
        with self.assertRaises(MatrixIndexError) as e:
            _ = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_row(5)
            self.assertEqual(str(e), 'Matrix row out of range')

    def test_get_row_out_of_range_too_low(self):
        with self.assertRaises(MatrixIndexError) as e:
            _ = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_row(-5)
            self.assertEqual(str(e), 'Matrix row out of range')

    # ------ GETCOL ----------------------------------------------------

    def test_get_col_1x1(self):
        expected = Matrix([[9]])
        actual = Matrix([[9]]).get_col(0)
        self.assertEqual(expected, actual)

    def test_get_col_2x2(self):
        expected = Matrix([[2, 4]])
        actual = Matrix([[1, 2], [3, 4]]).get_col(1)
        self.assertEqual(expected, actual)

    def test_get_col_3x3_0(self):
        expected = Matrix([[1, 4, 7]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_col(0)
        self.assertEqual(expected, actual)

    def test_get_col_3x3_1(self):
        expected = Matrix([[2, 5, 8]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_col(1)
        self.assertEqual(expected, actual)

    def test_get_col_3x3_2(self):
        expected = Matrix([[3, 6, 9]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_col(2)
        self.assertEqual(expected, actual)

    def test_get_col_3x3_minus_3(self):
        expected = Matrix([[1, 4, 7]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_col(-3)
        self.assertEqual(expected, actual)

    def test_get_col_3x3_1_minus_2(self):
        expected = Matrix([[2, 5, 8]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_col(-2)
        self.assertEqual(expected, actual)

    def test_get_col_3x3_2_minus_1(self):
        expected = Matrix([[3, 6, 9]])
        actual = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_col(-1)
        self.assertEqual(expected, actual)

    def test_get_col_out_of_range_too_large(self):
        with self.assertRaises(MatrixIndexError) as e:
            _ = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_col(5)
            self.assertEqual(str(e), 'Matrix col out of range')

    def test_get_col_out_of_range_too_low(self):
        with self.assertRaises(MatrixIndexError) as e:
            _ = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).get_col(-5)
            self.assertEqual(str(e), 'Matrix col out of range')

    # ------ CLONE -----------------------------------------------------

    def test_clone_1x1(self):
        expected = Matrix([[123]])
        actual = Matrix([[123]]).clone()
        self.assertEqual(expected, actual)

    def test_clone_4x4(self):
        expected = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        actual = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]).clone()
        self.assertEqual(expected, actual)

    def test_clone_4x2(self):
        expected = Matrix([[1, 5], [2, 6], [3, 7], [4, 8]])
        actual = Matrix([[1, 5], [2, 6], [3, 7], [4, 8]]).clone()
        self.assertEqual(expected, actual)

    def test_clone_deepcopy_seq_id_1x1(self):
        m = Matrix([[123]])
        original = id(m._data)
        actual = id(m.clone()._data)
        self.assertIsNot(original, actual)

    def test_clone_deepcopy_seq_id_4x4(self):
        m = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        original = id(m._data)
        actual = id(m.clone()._data)
        self.assertIsNot(original, actual)

    def test_clone_deepcopy_seq_id_4x2(self):
        m = Matrix([[1, 5], [2, 6], [3, 7], [4, 8]])
        original = id(m._data)
        actual = id(m.clone()._data)
        self.assertIsNot(original, actual)


if __name__ == '__main__':
    unittest.main()
